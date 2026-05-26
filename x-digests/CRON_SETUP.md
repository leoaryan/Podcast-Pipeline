# X Daily Digest - Cron Setup

## Important: Model Requirement
This pipeline REQUIRES the Grok model (via xai-oauth) for x_search to work.
Other models cannot access X data. Ensure Grok is the active provider.

## 1. Make scripts executable
```bash
chmod +x scripts/run_daily.sh
chmod +x scripts/generate_daily_digests.py
```

## 2. Add to crontab
```bash
crontab -e
```

Add this line (runs every day at 07:00 UTC):
```cron
0 7 * * * cd /root/podcast-pipeline && bash scripts/run_daily.sh >> run-logs/x-digest.log 2>&1
```

## 3. Create logs directory if needed
```bash
mkdir -p /root/podcast-pipeline/run-logs
```

## 4. Test manually first
```bash
cd /root/podcast-pipeline && bash scripts/run_daily.sh
```

## Notes
- Grok model is REQUIRED for x_search to function
- If model is changed, the pipeline will break
- The script commits and pushes automatically on changes