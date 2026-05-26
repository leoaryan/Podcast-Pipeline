# Podcast pipeline

Automated first stage for the podcast workflow:

```text
Codex daily -> fetch transcripts -> commit to GitHub
Hermes on VPS -> analyzes inbox/ -> writes digests/
Obsidian -> displays digests
```

Codex writes only to `inbox/` and optional `run-logs/`. Hermes owns `digests/`.

## Daily Fetcher

Configured sources live in `sources.json`.

Run manually:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/fetch_transcripts.py
```

Run, commit, and push:

```bash
python3 scripts/fetch_transcripts.py --push --log
```

## Output Format

New transcripts are Markdown files in:

```text
inbox/YYYY-MM-DD_<channel-slug>_<title-slug>.md
```

Each file contains:

- YAML metadata with title, channel, published date, URL, and YouTube video ID
- Episode header
- Chapter sections from YouTube description timestamps when available
- Timestamped transcript paragraphs
- Generic speaker labels when YouTube captions do not provide real speakers

Article sources contain the same YAML block with `source_type: article`, `source_url`, `author`, and `published`, followed by the extracted article body.

## Source Types

YouTube podcast sources use `type: "youtube"`:

```json
{
  "name": "Example Podcast",
  "type": "youtube",
  "slug": "example-podcast",
  "channel_id": "UCxxxxxxxxxxxxxxxxxxxxxx",
  "channel_url": "https://www.youtube.com/@example",
  "enabled": true
}
```

RSS article sources use `type: "rss_article"`:

```json
{
  "name": "Example Publication",
  "type": "rss_article",
  "slug": "example-publication",
  "feed_url": "https://example.com/feed",
  "min_word_count": 1500,
  "max_new_per_run": 2,
  "filter_keywords": ["strategy", "analysis"],
  "enabled": true
}
```

For article sources:

- `min_word_count` defaults to `1500`.
- `max_new_per_run` defaults to `2`.
- `filter_keywords` is optional. If present, at least one keyword must appear in the title, feed summary, or first 500 extracted body characters.
- Articles that look paywalled, too short, or extraction-failed are skipped.

## Idempotency

The fetcher does not use a separate state database. It checks both `inbox/` and `digests/`.

If a file with the same `<channel-slug>_<title-slug>` already exists in either folder, it skips that episode.

## Failure Handling

- Missing transcript: skip and continue.
- Fetch error: log and continue.
- Shorts/clips: skip videos below `min_duration_seconds` in `sources.json`.
- Backlog protection: process at most `max_new_per_channel` new episodes per source per run. The default is one full-length episode per channel.
- Log commits are created only when at least one transcript lands.
- Article rate limits or blocked pages, including HTTP 403 and 429, are skipped and logged without failing the run.
