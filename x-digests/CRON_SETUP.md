# Cron Setup for Daily X Digest

## 1. Make scripts executable
```bash
chmod +x scripts/run_daily.sh
chmod +x scripts/generate_daily_digests.py
```

## 2. Add to crontab
Run this command:
```bash
crontab -e
```

Add this line (runs every day at 07:00):
```cron
0 7 * * * /root/x-daily-digest/scripts/run_daily.sh >> /root/x-daily-digest/run-logs/daily.log 2>&1
```

## 3. Create logs directory
```bash
mkdir -p /root/x-daily-digest/run-logs
```

## 4. Test manually first
```bash
./scripts/run_daily.sh
```

## Notes
- Make sure your Git remote is set and SSH key is configured for passwordless push.
- The script will only commit if there are actual changes.