# Google Apps Script — feeding the Operator inbox (Google Workspace)

A worked example for Google Workspace users. Builds a scheduled Apps Script that exports calendar events to Google Drive, which syncs down to `{{STATE_DIR}}/inbox/`.

Zero OAuth setup from your end — Apps Script runs under your Google account with its own permissions.

---

## Prerequisites

- Google Workspace account (personal `@gmail.com` works for Calendar; some tenants restrict Drive sync)
- Google Drive for Desktop installed (or a cloud sync tool you trust)
- You know the local path Drive syncs to (typically `~/Google Drive/` on macOS, `G:\My Drive\` on Windows)

## Step 1 — Decide the sync route

The ritual commands read from `{{STATE_DIR}}/inbox/`. Pick how Apps Script's output ends up there.

**Option A (simplest): symlink.**
Create a Drive folder dedicated to this (e.g., `claude-operator-inbox`). After Drive syncs it locally:

```bash
# macOS / Linux
ln -s "$HOME/Google Drive/My Drive/claude-operator-inbox" {{STATE_DIR}}/inbox
```

**Option B: point `OPERATOR_STATE_DIR` at a path inside Google Drive.** Same tradeoff as the Power Automate version — clean, but mixes state across machines.

## Step 2 — Create the Drive folder

In Google Drive, create a folder called `claude-operator-inbox` at the root of My Drive. Copy its folder ID — it's the last path segment in the URL when you open the folder (e.g., `drive.google.com/drive/folders/1abc...xyz` → ID is `1abc...xyz`).

## Step 3 — Write the Apps Script

1. Go to [script.google.com](https://script.google.com) → **New project**
2. Rename it: `Operator Calendar Export`
3. Replace the default code with:

```javascript
// Operator — calendar export to the ritual inbox
// Runs on time-based triggers (Sunday night, Friday afternoon).

const INBOX_FOLDER_ID = 'PASTE_YOUR_FOLDER_ID_HERE';
const CALENDAR_ID = 'primary'; // or a specific calendar email

function exportMondayWindow() {
  const now = new Date();
  const end = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000); // next 7 days
  writeExport(now, end, 'monday');
}

function exportFridayWindow() {
  const now = new Date();
  const start = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000); // last 7 days
  writeExport(start, now, 'friday');
}

function writeExport(start, end, label) {
  const cal = CalendarApp.getCalendarById(CALENDAR_ID);
  const events = cal.getEvents(start, end).map(e => ({
    subject: e.getTitle(),
    start: e.getStartTime().toISOString(),
    end: e.getEndTime().toISOString(),
    organizer: e.getCreators()[0] || null,
    attendees: e.getGuestList().map(g => ({ email: g.getEmail(), name: g.getName() })),
    location: e.getLocation(),
    description: e.getDescription().slice(0, 500) // trim long bodies
  }));

  const date = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd');
  const filename = `calendar-${date}-${label}.json`;
  const folder = DriveApp.getFolderById(INBOX_FOLDER_ID);
  folder.createFile(filename, JSON.stringify(events, null, 2), MimeType.PLAIN_TEXT);
  console.log(`Wrote ${filename} with ${events.length} events`);
}
```

4. Paste the folder ID from Step 2 into `INBOX_FOLDER_ID`.
5. **Save** (⌘S / Ctrl+S).

## Step 4 — Grant Calendar + Drive permissions

Click **Run** once with `exportMondayWindow` selected in the function dropdown. Apps Script will prompt for Calendar and Drive permissions. Approve.

Confirm the file appears in your `claude-operator-inbox` Drive folder.

## Step 5 — Set up time-driven triggers

In the Apps Script editor:

1. Click the **Triggers** icon (clock on the left sidebar) → **Add Trigger**
2. For Monday:
   - Function: `exportMondayWindow`
   - Event source: `Time-driven`
   - Type: `Week timer`
   - Day: `Every Sunday`
   - Time: `10 PM to 11 PM`
3. **Save** → approve any further permission prompts.
4. **Add Trigger** again, this time:
   - Function: `exportFridayWindow`
   - Day: `Every Friday`
   - Time: `3 PM to 4 PM`
5. **Save**.

## Step 6 — Optional: Gmail signals

Add a second function to export unread Gmail from a watch list. Pattern:

```javascript
function exportUnreadFromWatchList() {
  const watchList = ['sarah@acme.com', 'lauren@acme.com'];
  const query = `is:unread (${watchList.map(a => `from:${a}`).join(' OR ')})`;
  const threads = GmailApp.search(query, 0, 20);
  const data = threads.map(t => ({
    subject: t.getFirstMessageSubject(),
    from: t.getMessages()[0].getFrom(),
    date: t.getLastMessageDate().toISOString(),
    snippet: t.getMessages()[0].getPlainBody().slice(0, 500)
  }));
  const date = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd');
  DriveApp.getFolderById(INBOX_FOLDER_ID)
    .createFile(`email-${date}.json`, JSON.stringify(data, null, 2), MimeType.PLAIN_TEXT);
}
```

Add a trigger for this on the same schedule.

## Verify end-to-end

1. Run `exportMondayWindow` manually from the editor.
2. Wait 30-60 seconds for Drive to sync.
3. Check: `ls "{{STATE_DIR}}/inbox/"` — a `calendar-*.json` should appear.
4. Run: `claude -p "/operator:monday-packet --from-inbox"` and confirm the packet references the calendar.

## Troubleshooting

- **"Script timed out"** — rare on calendar exports; usually means a very large calendar window. Reduce the window in `exportMondayWindow` / `exportFridayWindow`.
- **File lands in Drive but not locally** — Drive for Desktop sync may be slow or paused. Check the Drive menu bar icon.
- **Trigger didn't fire** — Apps Script logs are at **Executions** in the left sidebar. Check for errors or quota issues (unlikely for weekly runs).
- **Permission revoked after a Workspace policy change** — re-run the function once manually to re-prompt for permissions.

## Disabling later

Apps Script editor → **Triggers** → delete the triggers. The script code stays; just no more scheduled runs. The inbox stops receiving files until you re-add the triggers.
