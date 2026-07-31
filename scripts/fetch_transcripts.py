#!/usr/bin/env python3
import argparse
import datetime as dt
import html
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path

from bs4 import BeautifulSoup

try:
    import feedparser
except ImportError:
    feedparser = None

try:
    import certifi
except ImportError:
    certifi = None

try:
    import trafilatura
except ImportError:
    trafilatura = None

try:
    from readability import Document
except ImportError:
    Document = None

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    YouTubeTranscriptApi = None


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "sources.json"
INBOX = ROOT / "inbox"
DIGESTS = ROOT / "digests"
RUN_LOGS = ROOT / "run-logs"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
YOUTUBE_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "media": "http://search.yahoo.com/mrss/",
    "yt": "http://www.youtube.com/xml/schemas/2015",
}
if certifi is not None:
    SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
else:
    SSL_CONTEXT = ssl.create_default_context()
ssl._create_default_https_context = lambda: SSL_CONTEXT

TECHNICAL_TERMS = [
    "AGI",
    "AI",
    "alignment",
    "benchmark",
    "chip",
    "compute",
    "context window",
    "data center",
    "deep learning",
    "diffusion",
    "fine-tuning",
    "GPU",
    "inference",
    "language model",
    "LLM",
    "model",
    "neural network",
    "pretraining",
    "reasoning",
    "reinforcement learning",
    "RL",
    "scaling",
    "token",
    "training",
    "transformer",
]
SPONSOR_PATTERNS = re.compile(
    r"\b(sponsor|sponsors|sponsored|brought to you by|thanks to our sponsor|ad read|advertisement)\b",
    re.IGNORECASE,
)


@dataclass
class Episode:
    channel_name: str
    channel_slug: str
    title: str
    title_slug: str
    video_id: str
    url: str
    published: str
    duration_seconds: int
    description: str
    player: dict


@dataclass
class Article:
    source_name: str
    source_slug: str
    title: str
    title_slug: str
    url: str
    published: str
    author: str
    summary: str


def fetch_text(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60, context=SSL_CONTEXT) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def slugify(value, max_length=86):
    value = value.replace("&", " and ")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return (value[:max_length].strip("-") or "untitled")


def iso_date(value):
    if not value:
        return dt.date.today().isoformat()
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return value[:10]


def yaml_escape(value):
    return str(value or "").replace('"', "'")


def parse_entry_date(entry):
    for key in ("published", "updated", "created"):
        value = entry.get(key)
        if not value:
            continue
        try:
            return parsedate_to_datetime(value).date().isoformat()
        except (TypeError, ValueError, IndexError):
            return iso_date(value)
    return dt.date.today().isoformat()


def word_count(text):
    return len(re.findall(r"\b[\w'-]+\b", text or ""))


def parse_timecode(value):
    parts = [int(part) for part in value.split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    return None


def format_timecode(seconds):
    seconds = int(max(seconds, 0))
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def extract_json_after_marker(text, marker):
    index = text.find(marker)
    if index == -1:
        return None
    start = text.find("{", index)
    if start == -1:
        return None
    depth = 0
    in_string = False
    escape = False
    for position in range(start, len(text)):
        char = text[position]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : position + 1]
    return None


def resolve_channel_id(source):
    if source.get("channel_id"):
        return source["channel_id"]
    channel_url = source["channel_url"]
    if "/channel/" in channel_url:
        return channel_url.rstrip("/").split("/channel/", 1)[1].split("/", 1)[0]
    page = fetch_text(channel_url)
    match = re.search(r'"channelId":"(UC[^"]+)"', page)
    if not match:
        match = re.search(r'"externalId":"(UC[^"]+)"', page)
    if not match:
        match = re.search(r'"rssUrl":"https://www\.youtube\.com/feeds/videos\.xml\?channel_id=(UC[^"]+)"', page)
    if not match:
        match = re.search(r'"browseId":"(UC[^"]+)"', page)
    if not match:
        match = re.search(r'<meta itemprop="channelId" content="(UC[^"]+)"', page)
    if not match:
        raise RuntimeError(f"could not resolve channel id from {channel_url}")
    return match.group(1)


def rss_entries(channel_id, limit):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    root = ET.fromstring(fetch_text(url))
    for entry in root.findall("atom:entry", YOUTUBE_NS)[:limit]:
        video_id = entry.findtext("yt:videoId", namespaces=YOUTUBE_NS)
        title = entry.findtext("atom:title", namespaces=YOUTUBE_NS) or video_id
        published = entry.findtext("atom:published", namespaces=YOUTUBE_NS) or ""
        yield video_id, title, published


def article_entries(source, limit):
    if feedparser is None:
        raise RuntimeError("feedparser is not installed")
    feed = feedparser.parse(source["feed_url"])
    if feed.bozo and not feed.entries:
        raise RuntimeError(f"could not parse feed: {feed.bozo_exception}")
    for entry in feed.entries[:limit]:
        title = html.unescape(" ".join((entry.get("title") or "").split()))
        link = entry.get("link")
        if not title or not link:
            continue
        summary = html_to_text(entry.get("summary") or entry.get("description") or "")
        author = entry.get("author") or source.get("name", "")
        yield Article(
            source_name=source["name"],
            source_slug=source["slug"],
            title=title,
            title_slug=slugify(title),
            url=link,
            published=parse_entry_date(entry),
            author=html.unescape(" ".join(author.split())),
            summary=summary,
        )


def load_video(channel_name, channel_slug, video_id, fallback_title, fallback_published):
    watch_html = fetch_text(f"https://www.youtube.com/watch?v={video_id}")
    player_json = extract_json_after_marker(watch_html, "ytInitialPlayerResponse")
    if not player_json:
        raise RuntimeError("missing YouTube player metadata")
    player = json.loads(player_json)
    details = player.get("videoDetails", {})
    microformat = player.get("microformat", {}).get("playerMicroformatRenderer", {})
    title = details.get("title") or fallback_title
    description = details.get("shortDescription") or microformat.get("description", {}).get("simpleText", "")
    published = microformat.get("publishDate") or fallback_published
    duration = int(details.get("lengthSeconds") or 0)
    return Episode(
        channel_name=channel_name,
        channel_slug=channel_slug,
        title=title,
        title_slug=slugify(title),
        video_id=video_id,
        url=f"https://www.youtube.com/watch?v={video_id}",
        published=published,
        duration_seconds=duration,
        description=description,
        player=player,
    )


def existing_episode_keys():
    keys = set()
    for folder in (INBOX, DIGESTS):
        if not folder.exists():
            continue
        for path in folder.iterdir():
            if not path.is_file():
                continue
            name = path.stem
            match = re.match(r"\d{4}-\d{2}-\d{2}_(.+)", name)
            keys.add(match.group(1) if match else name)
    return keys


def output_key(episode):
    return f"{episode.channel_slug}_{episode.title_slug}"


def article_output_key(article):
    return f"{article.source_slug}_{article.title_slug}"


def output_path(episode):
    return INBOX / f"{iso_date(episode.published)}_{output_key(episode)}.md"


def article_output_path(article):
    return INBOX / f"{iso_date(article.published)}_{article_output_key(article)}.md"


def caption_track(player):
    tracks = (
        player.get("captions", {})
        .get("playerCaptionsTracklistRenderer", {})
        .get("captionTracks", [])
    )
    if not tracks:
        return None
    manual_english = [
        track
        for track in tracks
        if track.get("languageCode", "").startswith("en") and track.get("kind") != "asr"
    ]
    english = [track for track in tracks if track.get("languageCode", "").startswith("en")]
    return (manual_english or english or tracks)[0]


def fetch_transcript_segments(episode):
    api_segments = fetch_transcript_segments_with_api(episode.video_id)
    if api_segments:
        return api_segments

    track = caption_track(episode.player)
    if not track:
        return []
    base_url = track["baseUrl"]
    separator = "&" if "?" in base_url else "?"
    transcript_xml = fetch_text(f"{base_url}{separator}fmt=srv3")
    segments = parse_xml_transcript(transcript_xml)
    if segments:
        return segments
    transcript_json = fetch_text(f"{base_url}{separator}fmt=json3")
    return parse_json_transcript(transcript_json)


def fetch_transcript_segments_with_api(video_id):
    if YouTubeTranscriptApi is None:
        return []
    try:
        fetched = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    except Exception:
        return []
    segments = []
    for item in fetched:
        text = html.unescape(" ".join(item.text.split()))
        if not text:
            continue
        start = float(item.start)
        duration = float(item.duration)
        segments.append({"start": start, "end": start + duration, "text": text})
    return segments


def parse_xml_transcript(transcript_xml):
    try:
        root = ET.fromstring(transcript_xml)
    except ET.ParseError:
        return []
    segments = []
    for node in root.iter("text"):
        text = html.unescape("".join(node.itertext()))
        text = " ".join(text.split())
        if not text:
            continue
        start = float(node.attrib.get("start", "0"))
        duration = float(node.attrib.get("dur", "0"))
        segments.append({"start": start, "end": start + duration, "text": text})
    return segments


def parse_json_transcript(transcript_json):
    try:
        data = json.loads(transcript_json)
    except json.JSONDecodeError:
        return []
    segments = []
    for event in data.get("events", []):
        pieces = event.get("segs") or []
        text = "".join(piece.get("utf8", "") for piece in pieces)
        text = html.unescape(" ".join(text.split()))
        if not text:
            continue
        start = float(event.get("tStartMs", 0)) / 1000
        duration = float(event.get("dDurationMs", 0)) / 1000
        segments.append({"start": start, "end": start + duration, "text": text})
    return segments


def extract_chapters(description, duration_seconds):
    chapters = []
    for raw_line in description.splitlines():
        line = " ".join(raw_line.strip().split())
        match = re.search(r"(?<!\d)(\d{1,2}:\d{2}(?::\d{2})?)(?!\d)\s*[-–—:]?\s*(.+)", line)
        if not match:
            continue
        start = parse_timecode(match.group(1))
        title = match.group(2).strip(" -–—:\t")
        if start is None or not title:
            continue
        chapters.append({"start": start, "title": title})
    chapters = sorted({chapter["start"]: chapter for chapter in chapters}.values(), key=lambda item: item["start"])
    if chapters and chapters[0]["start"] <= 5:
        for index, chapter in enumerate(chapters):
            chapter["end"] = chapters[index + 1]["start"] if index + 1 < len(chapters) else duration_seconds
        return chapters
    return [{"start": 0, "end": duration_seconds, "title": "Transcript"}]


def is_sponsor_chapter(chapter):
    return bool(SPONSOR_PATTERNS.search(chapter["title"]))


def segment_in_chapter(segment, chapter):
    return chapter["start"] <= segment["start"] < chapter.get("end", 10**9)


def bold_terms(text):
    for term in sorted(TECHNICAL_TERMS, key=len, reverse=True):
        pattern = re.compile(rf"(?<!\*)\b({re.escape(term)})\b(?!\*)", re.IGNORECASE)
        text = pattern.sub(lambda match: f"**{match.group(1)}**", text)
    return text


def group_segments(segments, max_gap=2.2, max_chars=900):
    groups = []
    current = []
    for segment in segments:
        if not current:
            current = [segment]
            continue
        gap = segment["start"] - current[-1]["end"]
        chars = sum(len(item["text"]) for item in current) + len(segment["text"])
        if gap > max_gap or chars > max_chars:
            groups.append(current)
            current = [segment]
        else:
            current.append(segment)
    if current:
        groups.append(current)
    return groups


def render_markdown(episode, chapters, segments):
    lines = [
        "---",
        f'title: "{yaml_escape(episode.title)}"',
        f'channel: "{yaml_escape(episode.channel_name)}"',
        "source_type: podcast",
        f"published: {iso_date(episode.published)}",
        f"source_url: {episode.url}",
        f"video_id: {episode.video_id}",
        "---",
        "",
        f"# {episode.title}",
        "",
        f"- **Channel:** {episode.channel_name}",
        f"- **Published:** {iso_date(episode.published)}",
        f"- **Source:** {episode.url}",
        "",
        "## Transcript",
        "",
        "> Speaker attribution is not available from YouTube captions. Turns are labeled generically as Speaker A to avoid false attribution.",
        "",
    ]

    for chapter in chapters:
        if is_sponsor_chapter(chapter):
            continue
        chapter_segments = [segment for segment in segments if segment_in_chapter(segment, chapter)]
        if not chapter_segments:
            continue
        lines.append(f"### {format_timecode(chapter['start'])} - {chapter['title']}")
        lines.append("")
        for group in group_segments(chapter_segments):
            start = format_timecode(group[0]["start"])
            text = " ".join(item["text"] for item in group)
            lines.append(f"**Speaker A [{start}]:** {bold_terms(text)}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def html_to_text(raw_html):
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return html.unescape(" ".join(soup.get_text(" ", strip=True).split()))


def readability_to_markdown(raw_html):
    if Document is None:
        return ""
    try:
        content_html = Document(raw_html).summary(html_partial=True)
    except Exception:
        return ""
    soup = BeautifulSoup(content_html, "html.parser")
    lines = []
    for node in soup.find_all(["h1", "h2", "h3", "p", "li", "blockquote"]):
        text = " ".join(node.get_text(" ", strip=True).split())
        if not text:
            continue
        if node.name in {"h1", "h2"}:
            lines.append(f"## {text}")
        elif node.name == "h3":
            lines.append(f"### {text}")
        elif node.name == "li":
            lines.append(f"- {text}")
        elif node.name == "blockquote":
            lines.append(f"> {text}")
        else:
            lines.append(text)
        lines.append("")
    return "\n".join(lines).strip()


def extract_article_body(raw_html):
    if trafilatura is not None:
        extracted = trafilatura.extract(
            raw_html,
            output_format="markdown",
            include_comments=False,
            include_tables=False,
            favor_recall=True,
        )
        if extracted:
            return extracted.strip()
    return readability_to_markdown(raw_html)


def looks_paywalled_or_useless(body, min_word_count):
    lower = (body or "").lower()
    if word_count(body) < min_word_count:
        return True
    subscribe_hits = sum(
        lower.count(phrase)
        for phrase in (
            "subscribe to continue",
            "subscribe now",
            "sign in to continue",
            "create an account",
            "already a subscriber",
            "free preview",
        )
    )
    if subscribe_hits >= 3 and word_count(body) < min_word_count * 2:
        return True
    return False


def article_matches_filter(article, body_preview, keywords):
    if not keywords:
        return True
    haystack = f"{article.title}\n{article.summary}\n{body_preview[:500]}".lower()
    return any(keyword.lower() in haystack for keyword in keywords)


def render_article_markdown(article, body):
    return "\n".join(
        [
            "---",
            f'title: "{yaml_escape(article.title)}"',
            f'channel: "{yaml_escape(article.source_name)}"',
            "source_type: article",
            f"published: {iso_date(article.published)}",
            f"source_url: {article.url}",
            f'author: "{yaml_escape(article.author)}"',
            "---",
            "",
            body.strip(),
            "",
        ]
    )


def should_skip_episode(episode, keys, min_duration_seconds):
    if episode.duration_seconds and episode.duration_seconds < min_duration_seconds:
        return f"short/clip under {min_duration_seconds // 60} minutes"
    if output_key(episode) in keys:
        return "already present in inbox/ or digests/"
    return None


def should_skip_article(article, keys):
    if article_output_key(article) in keys:
        return "already present in inbox/ or digests/"
    return None


def git_commit(paths, subject, summary, push):
    if not paths:
        return False
    subprocess.run(["git", "add", *[str(path.relative_to(ROOT)) for path in paths]], cwd=ROOT, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode == 0:
        return False
    message = subject + "\n\n" + summary
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
    if push:
        subprocess.run(["git", "push"], cwd=ROOT, check=True)
    return True


def run(args):
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    recent_limit = int(config.get("recent_limit", 8))
    min_duration = int(config.get("min_duration_seconds", 1200))
    max_new_per_channel = int(config.get("max_new_per_channel", 3))
    keys = existing_episode_keys()
    checked = []
    added = []
    skipped = []
    errors = []
    written = []

    for source in config.get("channels", []):
        if source.get("enabled", True) is False:
            continue
        source_type = source.get("type", "youtube")
        channel_name = source["name"]
        channel_slug = source.get("slug") or slugify(channel_name, 40)
        checked.append(channel_name)
        if source_type == "rss_article":
            try:
                min_word_count = int(source.get("min_word_count", 1500))
                max_new = int(source.get("max_new_per_run", 2))
                keywords = source.get("filter_keywords") or []
                added_for_source = 0
                for article in article_entries(source, recent_limit):
                    if added_for_source >= max_new:
                        break
                    try:
                        reason = should_skip_article(article, keys)
                        if reason:
                            skipped.append(f"{channel_name}: {article.title} ({reason})")
                            continue
                        raw_html = fetch_text(article.url)
                        body = extract_article_body(raw_html)
                        if not body:
                            skipped.append(f"{channel_name}: {article.title} (article extraction failed)")
                            continue
                        if not article_matches_filter(article, body, keywords):
                            skipped.append(f"{channel_name}: {article.title} (keyword filter)")
                            continue
                        if looks_paywalled_or_useless(body, min_word_count):
                            skipped.append(
                                f"{channel_name}: {article.title} "
                                f"(extracted body below {min_word_count} useful words)"
                            )
                            continue
                        markdown = render_article_markdown(article, body)
                        path = article_output_path(article)
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(markdown, encoding="utf-8")
                        keys.add(article_output_key(article))
                        written.append(path)
                        added.append(f"{channel_name}: {article.title}")
                        added_for_source += 1
                    except Exception as exc:
                        if isinstance(exc, urllib.error.HTTPError) and exc.code in {401, 403, 429}:
                            skipped.append(f"{channel_name}: {article.title} (HTTP {exc.code})")
                        else:
                            errors.append(f"{channel_name}: {article.title} ({exc})")
                        continue
            except Exception as exc:
                errors.append(f"{channel_name}: source check failed ({exc})")
            continue
        if source_type != "youtube":
            errors.append(f"{channel_name}: unsupported source type {source_type}")
            continue
        try:
            channel_id = resolve_channel_id(source)
            added_for_channel = 0
            for video_id, fallback_title, fallback_published in rss_entries(channel_id, recent_limit):
                if added_for_channel >= max_new_per_channel:
                    break
                try:
                    episode = load_video(channel_name, channel_slug, video_id, fallback_title, fallback_published)
                    reason = should_skip_episode(episode, keys, min_duration)
                    if reason:
                        skipped.append(f"{channel_name}: {episode.title} ({reason})")
                        continue
                    segments = fetch_transcript_segments(episode)
                    if not segments:
                        skipped.append(f"{channel_name}: {episode.title} (transcript unavailable)")
                        continue
                    chapters = extract_chapters(episode.description, episode.duration_seconds)
                    markdown = render_markdown(episode, chapters, segments)
                    path = output_path(episode)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(markdown, encoding="utf-8")
                    keys.add(output_key(episode))
                    written.append(path)
                    added.append(f"{channel_name}: {episode.title}")
                    added_for_channel += 1
                except Exception as exc:
                    errors.append(f"{channel_name}: {fallback_title} ({exc})")
                    continue
        except Exception as exc:
            errors.append(f"{channel_name}: channel check failed ({exc})")

    summary_lines = [
        f"Checked: {', '.join(checked) if checked else 'none'}",
        f"Added: {len(added)}",
        *[f"- added {item}" for item in added],
        f"Skipped: {len(skipped)}",
        *[f"- skipped {item}" for item in skipped],
        f"Errors: {len(errors)}",
        *[f"- error {item}" for item in errors],
    ]
    summary = "\n".join(summary_lines)
    subject = (
        "Automated podcast transcript fetch: "
        f"checked {len(checked)}, added {len(added)}, skipped {len(skipped)}, errors {len(errors)}"
    )
    print(summary)

    if args.log and added:
        RUN_LOGS.mkdir(exist_ok=True)
        log_path = RUN_LOGS / f"{dt.datetime.now().strftime('%Y-%m-%d_%H%M%S')}.txt"
        log_path.write_text(summary + "\n", encoding="utf-8")
        written.append(log_path)

    if args.commit or args.push:
        committed = git_commit(written, subject, summary, args.push)
        if not committed:
            print("No git changes to commit.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Fetch new YouTube podcast transcripts into inbox/ as Markdown.")
    parser.add_argument("--commit", action="store_true", help="Commit generated transcripts.")
    parser.add_argument("--push", action="store_true", help="Commit and push generated transcripts.")
    parser.add_argument("--log", action="store_true", help="Write run summary to run-logs/.")
    args = parser.parse_args()
    if args.push:
        args.commit = True
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
