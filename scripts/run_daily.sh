#!/bin/bash
# Daily Twitter Digest Runner
# Uses Hermes with Grok model for x_search access

set -e
cd "$(dirname "$0")/.."

echo "=== Generating daily digests (Hermes + Grok) ==="

hermes chat \
  --provider xai-oauth \
  --model grok/grok-4.3 \
  --quiet \
  --yolo \
  -q "Generate today's Twitter Daily Digest for all 7 topics and save to disk.

Topics and their slugs:
1. hermes-agent-applications
2. ai-design-creativity  
3. content-marketing-experiments
4. niche-boring-businesses
5. ai-infrastructure-energy
6. open-source-ai-tools
7. fc-barcelona

For EACH topic:
- Use x_search to find the most interesting recent tweets (past 48 hours)
- Apply strict filter: only include specific examples with concrete workflows, deep insights, and thoughtful opinions. Skip surface-level or obvious content.
- Write the digest as a markdown file to: x-digests/topics/[slug]/YYYY-MM-DD.md (use today's date)

Format for each file:
# [Topic Name]
**Date:** YYYY-MM-DD

## Key Examples
- [detailed examples with specifics]

## Insights
- [patterns and implications]

## Notable Opinions
- [thought-provoking takes, skip ragebait]

## Sources
- [links to original tweets]

Generate ALL 7 files now."

echo "=== Committing changes ==="
git add x-digests/topics/
git commit -m "Daily Twitter digest update - $(date +%Y-%m-%d)" || echo "No changes to commit"

echo "=== Pushing to GitHub ==="
git push

echo "=== Done ==="