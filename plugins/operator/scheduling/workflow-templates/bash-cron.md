# bash cron — feeding the Operator inbox (technical path)

For users who want to hit a calendar API directly from a local shell script and schedule it with cron. More moving parts than Power Automate or Apps Script, but zero cloud dependencies and full control over the data shape.

Choose one calendar source. Each has a slightly different setup; the output contract is the same.

---

## Option A — macOS `icalBuddy` (zero cloud, reads Calendar.app)

If your calendar is in Apple's Calendar.app (connected to iCloud, Exchange, or Google), `icalBuddy` reads it locally with no API or OAuth.

### Install

```bash
brew install ical-buddy
```

### The export script

Write to `{{STATE_DIR}}/scheduling/export-calendar.sh`:

```bash
#!/bin/bash
# Operator calendar export via icalBuddy
set -euo pipefail

STATE_DIR="${OPERATOR_STATE_DIR:-$HOME/.claude/operator}"
OUT="$STATE_DIR/inbox/calendar-$(date +%Y-%m-%d)-${1:-weekly}.md"

mkdir -p "$STATE_DIR/inbox"

{
  echo "# Calendar export · $(date +%Y-%m-%d)"
  echo ""
  if [[ "${1:-}" == "friday" ]]; then
    echo "## Last 7 days"
    icalBuddy -nc -npn -eep "notes,url,uid" -tf "%H:%M" eventsFrom:"7 days ago" to:"today"
  else
    echo "## Next 7 days"
    icalBuddy -nc -npn -eep "notes,url,uid" -tf "%H:%M" eventsFrom:"today" to:"7 days from now"
  fi
} > "$OUT"

echo "Wrote $OUT"
```

Make it executable:

```bash
chmod +x {{STATE_DIR}}/scheduling/export-calendar.sh
```

### Cron entries

```cron
# Monday-ritual input (Sunday 10 PM)
0 22 * * 0 {{STATE_DIR}}/scheduling/export-calendar.sh monday >> {{STATE_DIR}}/scheduling/export.log 2>&1

# Friday-ritual input (Friday 3:30 PM)
30 15 * * 5 {{STATE_DIR}}/scheduling/export-calendar.sh friday >> {{STATE_DIR}}/scheduling/export.log 2>&1
```

Append to your crontab: `crontab -e`.

---

## Option B — `gcalcli` (Google Calendar, OAuth once)

Reads Google Calendar via the official API. One-time OAuth.

### Install

```bash
brew install gcalcli         # macOS
pip install gcalcli          # anywhere
```

### Authenticate (once)

```bash
gcalcli --nocache list       # opens browser for OAuth; approve
```

### The export script

Write to `{{STATE_DIR}}/scheduling/export-calendar.sh`:

```bash
#!/bin/bash
set -euo pipefail

STATE_DIR="${OPERATOR_STATE_DIR:-$HOME/.claude/operator}"
OUT="$STATE_DIR/inbox/calendar-$(date +%Y-%m-%d)-${1:-weekly}.json"

mkdir -p "$STATE_DIR/inbox"

if [[ "${1:-}" == "friday" ]]; then
  gcalcli agenda --tsv "7 days ago" "today" > /tmp/cal.tsv
else
  gcalcli agenda --tsv "today" "7 days from now" > /tmp/cal.tsv
fi

# Convert TSV to JSON (requires jq + awk)
awk -F'\t' 'BEGIN { print "[" }
  NR > 1 { if (NR > 2) printf ",\n"; printf "{\"date\":\"%s\",\"start\":\"%s\",\"end\":\"%s\",\"subject\":\"%s\"}", $1, $2, $3, $4 }
  END { print "\n]" }' /tmp/cal.tsv > "$OUT"

echo "Wrote $OUT"
```

Cron entries same as Option A.

---

## Option C — Raw Google Calendar API with `curl`

Technical users with a service account and refresh token. Pattern:

```bash
# Prerequisites: GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, REFRESH_TOKEN in env
ACCESS_TOKEN=$(curl -s https://oauth2.googleapis.com/token \
  -d "client_id=$GOOGLE_CLIENT_ID" \
  -d "client_secret=$GOOGLE_CLIENT_SECRET" \
  -d "refresh_token=$REFRESH_TOKEN" \
  -d "grant_type=refresh_token" | jq -r .access_token)

TIME_MIN=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
TIME_MAX=$(date -u -v+7d +"%Y-%m-%dT%H:%M:%SZ")  # macOS; use `-d '+7 days'` on Linux

curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=$TIME_MIN&timeMax=$TIME_MAX&singleEvents=true&orderBy=startTime" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  > "{{STATE_DIR}}/inbox/calendar-$(date +%Y-%m-%d).json"
```

Store the secrets in `~/.config/operator/env` (chmod 600), source it in the script. Everything else is the same.

---

## Testing before you schedule

Run the script manually once:

```bash
bash {{STATE_DIR}}/scheduling/export-calendar.sh monday
ls {{STATE_DIR}}/inbox/
```

Confirm a file appeared. Then run the ritual:

```bash
claude -p "/operator:monday-packet --from-inbox"
```

The packet should reference the calendar.

## Troubleshooting

- **Cron didn't fire** — macOS: cron is deprecated; use `launchd` instead (the Operator setup wizard generates launchd configs by default). Linux: check `systemctl status cron` and `grep CRON /var/log/syslog`.
- **Script runs manually but fails in cron** — cron has a stripped environment. Set `PATH`, `HOME`, and any API keys explicitly at the top of the script.
- **File written but empty** — the calendar query returned no events. Check the time range math (date arithmetic differs on macOS vs. Linux).
- **Permission denied on write** — ensure `{{STATE_DIR}}/inbox/` exists and the cron user has write access.

## Disabling later

```bash
crontab -e     # delete the operator-ritual lines
```

Nothing else to tear down. The script sits unused in `{{STATE_DIR}}/scheduling/` until you re-schedule it.
