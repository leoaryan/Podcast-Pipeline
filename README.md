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

## Idempotency

The fetcher does not use a separate state database. It checks both `inbox/` and `digests/`.

If a file with the same `<channel-slug>_<title-slug>` already exists in either folder, it skips that episode.

## Failure Handling

- Missing transcript: skip and continue.
- Fetch error: log and continue.
- Shorts/clips: skip videos below `min_duration_seconds` in `sources.json`.
- Backlog protection: process at most `max_new_per_channel` new episodes per source per run. The default is one full-length episode per channel.
- Log commits are created only when at least one transcript lands.
