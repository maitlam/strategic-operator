# Power Automate — feeding the Operator inbox (Microsoft 365)

A worked example for Microsoft 365 users. Builds two scheduled flows (one weekly before Monday, one weekly before Friday) that export calendar data to OneDrive, which syncs down to `{{STATE_DIR}}/inbox/`.

The ritual commands pick up what's in the inbox. Nothing in this walkthrough is specific to Claude Code — you're just teaching Power Automate to drop a file into a folder your Mac/PC syncs.

---

## Prerequisites

- Microsoft 365 account with Power Automate access
- OneDrive sync client installed, syncing a folder to your machine
- You know the local path where OneDrive syncs (typically `~/OneDrive/` on macOS, `%USERPROFILE%\OneDrive\` on Windows)

## Step 1 — Decide the sync route

Pick one. The ritual commands read from `{{STATE_DIR}}/inbox/`, so Power Automate's output needs to end up there.

**Option A (simplest): symlink.**
Create a OneDrive folder dedicated to this (e.g., `/Documents/claude-operator-inbox/`). After OneDrive syncs it locally, symlink it into the state dir:

```bash
# macOS / Linux
ln -s ~/OneDrive/Documents/claude-operator-inbox {{STATE_DIR}}/inbox
```

```powershell
# Windows
mklink /D "%USERPROFILE%\.claude\operator\inbox" "%USERPROFILE%\OneDrive\Documents\claude-operator-inbox"
```

**Option B: point `OPERATOR_STATE_DIR` at the OneDrive folder.**
Set the env var so the state dir *is* inside OneDrive. Clean, but mixes state across machines if you sign in on multiple.

## Step 2 — Build the Monday flow

1. Open [make.powerautomate.com](https://make.powerautomate.com) → **Create** → **Scheduled cloud flow**
2. Name: `Operator — weekly Monday export`
3. Starting: next Sunday, 10:00 PM local
4. Repeat every: `1 Week`, on `Sunday`
5. Click **Create**

Add these actions in order:

**Action 1: "Get events (V4)"** (Office 365 Outlook connector)
- Calendar Id: your default calendar
- Filter Query (OData): `start/dateTime ge '@{formatDateTime(utcNow(), 'yyyy-MM-ddTHH:mm:ssZ')}' and start/dateTime lt '@{formatDateTime(addDays(utcNow(), 7), 'yyyy-MM-ddTHH:mm:ssZ')}'`
- Top Count: `50`

**Action 2: "Create file"** (OneDrive for Business connector)
- Folder Path: `/Documents/claude-operator-inbox/`
- File Name: `calendar-@{formatDateTime(utcNow(), 'yyyy-MM-dd')}.json`
- File Content: use the expression editor and paste:
  ```
  @{body('Get_events_(V4)')?['value']}
  ```

Save. Test the flow once (**Flow Checker** → **Test** → **Manually**) and confirm the file lands in OneDrive and syncs to `{{STATE_DIR}}/inbox/`.

## Step 3 — Build the Friday flow

Clone the Monday flow (**Save As**) and change:

- Name: `Operator — weekly Friday export`
- Starting: next Friday, 3:30 PM local
- Repeat every: `1 Week`, on `Friday`
- Filter Query (OData): `start/dateTime ge '@{formatDateTime(addDays(utcNow(), -7), 'yyyy-MM-ddTHH:mm:ssZ')}' and start/dateTime lt '@{formatDateTime(utcNow(), 'yyyy-MM-ddTHH:mm:ssZ')}'`  *(last 7 days instead of next 7)*
- File Name: `calendar-@{formatDateTime(utcNow(), 'yyyy-MM-dd')}-friday.json`

Save and test.

## Step 4 — Optional: unread email signals

Add a second flow for Gmail-equivalent inbox signals.

- Trigger: same scheduled timing
- Action: `List emails (V3)` from Outlook, filter `isRead eq false` and sender in a watch list
- Action: Create file in `/Documents/claude-operator-inbox/` named `email-@{formatDateTime(utcNow(), 'yyyy-MM-dd')}.json`

The ritual commands will route `email-*.json` to the "Awaiting your reply" / "New asks" buckets.

## File formats the ritual commands understand

The Monday/Friday commands expect these fields in the calendar JSON. Power Automate's default output already matches:

```json
[
  {
    "subject": "QBR dry-run",
    "start": {"dateTime": "2026-10-20T10:00:00", "timeZone": "Pacific Standard Time"},
    "end": {"dateTime": "2026-10-20T11:00:00", "timeZone": "Pacific Standard Time"},
    "organizer": {"emailAddress": {"name": "Sarah Chen", "address": "sarah@acme.com"}},
    "attendees": [...]
  }
]
```

For email JSON:

```json
[
  {
    "subject": "Q3 variance",
    "from": {"emailAddress": {"name": "Sarah Chen", "address": "sarah@acme.com"}},
    "receivedDateTime": "2026-10-14T17:30:00Z",
    "bodyPreview": "Can we walk through..."
  }
]
```

## Verify end-to-end

1. Trigger the Monday flow manually (**Test** → **Manually**).
2. Wait 30-60 seconds for OneDrive to sync.
3. Check: `ls {{STATE_DIR}}/inbox/` — a `calendar-*.json` should appear.
4. Run: `claude -p "/operator:monday-packet --from-inbox"` and confirm the generated packet references calendar items.

## Troubleshooting

- **File lands in OneDrive but not locally** — OneDrive sync may be paused or the folder isn't selected for sync. Right-click the OneDrive icon → Preferences → Sync folders.
- **Flow fails on the filter query** — Outlook's OData parser is picky about datetime format. The expressions above are tested; if you edit them, keep the `yyyy-MM-ddTHH:mm:ssZ` shape.
- **Scheduled flow doesn't run** — Power Automate pauses flows that haven't been used in 90 days. Set a reminder, or add a monthly "ping myself" step.
- **The packet looks thin even with files in the inbox** — check `{{STATE_DIR}}/scheduling/monday-packet.log` for parse errors. Most issues are malformed JSON from a flow edit.

## Disabling later

In Power Automate: **My flows** → right-click the flow → **Turn off**. The inbox stops receiving files; the ritual commands will fire with an empty-inbox warning until you turn the flow back on or delete the schedule.
