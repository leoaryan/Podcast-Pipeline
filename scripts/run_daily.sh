#!/bin/bash
# Daily X Digest Runner
# Run this via cron

set -e

cd "$(dirname "$0")/.."

echo "=== Generating daily digests ==="
python3 scripts/generate_daily_digests.py

echo "=== Committing changes ==="
git add x-digests/topics/
git commit -m "Daily digest update - $(date +%Y-%m-%d)" || echo "No changes to commit"

echo "=== Pushing to GitHub ==="
git push

echo "=== Done ==="