#!/bin/bash
# Git helper for daily digest commits
# The actual generation is handled by the Hermes cron job "Twitter Daily Digest"
# This script is only for manual git operations if needed
set -e
cd "$(dirname "$0")/.."
git add x-digests/topics/
git commit -m "Daily Twitter digest update - $(date +%Y-%m-%d)" || echo "No changes to commit"
git push