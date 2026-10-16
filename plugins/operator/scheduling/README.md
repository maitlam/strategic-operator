# Scheduling the Operator rituals

The Monday-packet and Friday-wrap commands can run on a schedule — fed by a staging folder (`~/.claude/operator/inbox/`) that any workflow tool can drop files into.

**Fastest path:** run `/operator:setup-scheduling`. It's a four-question wizard that writes the right scheduler config and a tool-specific setup walkthrough tailored to your OS and workflow tool.

**Manual path:** read the templates in this folder and wire it yourself.

---

## The loose contract

Three pieces, loosely coupled:

```
┌─────────────────┐    writes files    ┌─────────────────┐    runs on cron    ┌──────────────────────┐
│  Workflow tool  │ ─────────────────▶ │  Inbox folder   │ ◀───────────────── │  Scheduler            │
│  (Power Auto,   │                    │  (~/.claude/    │                    │  (launchd / cron /   │
│   Apps Script,  │                    │   operator/     │                    │   Task Scheduler)    │
│   bash, etc.)   │                    │   inbox/)       │                    │  invokes             │
└─────────────────┘                    └─────────────────┘                    │  claude -p "/operator:│
                                                                              │   monday-packet       │
                                                                              │   --from-inbox"       │
                                                                              └──────────────────────┘
```

The ritual command doesn't care what wrote the files; the workflow tool doesn't care who's reading them. Swap either side without touching the other.

---

## What's in this folder

```
scheduling/
├── README.md                    ← you are here
├── scheduler-templates/
│   ├── launchd.plist.tmpl       ← macOS
│   ├── crontab.tmpl             ← Linux
│   └── task-scheduler.xml.tmpl  ← Windows
└── workflow-templates/
    ├── power-automate.md        ← Microsoft 365
    ├── apps-script.md           ← Google Workspace
    ├── bash-cron.md             ← technical / zero-cloud path
    └── manual.md                ← drop files by hand
```

**Scheduler templates** hold variables (`{{CLAUDE_BIN}}`, `{{STATE_DIR}}`, `{{HOUR}}`, etc.) that the setup wizard substitutes. If you run the wizard, the substituted files land in `~/.claude/operator/scheduling/`.

**Workflow templates** are the walkthroughs for feeding the inbox from each tool.

---

## File-naming hints for the inbox

Files with these prefixes get routed to specific sections of the generated packet. Files without a prefix get classified by content.

| Prefix | Routes to |
|---|---|
| `calendar-*` | This week's meetings (Monday) / meetings that happened (Friday) |
| `email-*` or `inbox-*` | Overnight asks (Monday) / new asks (Friday) |
| `docs-*` or `drive-*` | Doc activity |
| `status-*` or `tracker-*` | Open loops, risk list |
| `meetings-*` or `notes-*` | Meeting notes (especially useful for Friday) |
| `decisions-*` | Decision inputs |
| `launches-*` or `ship-*` | Shipped vs. slipped (Friday) |
| `risks-*` or `asks-*` | New risks or new asks surfaced (Friday) |

File formats accepted: `.json`, `.csv`, `.md`, `.txt`.

---

## What the ritual commands do with the inbox

On a `--from-inbox` run, the command:

1. Reads every file in `~/.claude/operator/inbox/`
2. Classifies by filename prefix (if present) or content
3. Produces the packet, written to `~/.claude/operator/packets/YYYY-WXX-{monday,friday}.md`
4. Moves processed files to `~/.claude/operator/inbox/archive/YYYY-WXX/`
5. If the inbox was empty, writes a reminder-mode packet with "⚠ Inbox was empty" at the top

---

## Troubleshooting

- **Scheduled run didn't fire** — check the scheduler itself (`launchctl list | grep operator`, `crontab -l | grep operator`, or `schtasks /query | findstr Operator`). Templates include working verification commands.
- **Packet is thin or missing sections** — the inbox was empty or the files didn't parse. Check `~/.claude/operator/scheduling/*.log` for parse errors.
- **Workflow tool writes files but nothing shows up locally** — your cloud sync (OneDrive / Google Drive for Desktop) may be paused or that folder isn't selected for sync. Not a scheduler problem.

---

## Disabling scheduling

Each scheduler template includes its disable command. Short version:

- macOS: `launchctl unload ~/.claude/operator/scheduling/com.operator.*.plist`
- Linux: `crontab -e` → delete the lines marked `# operator-ritual`
- Windows: `schtasks /delete /tn "OperatorMondayPacket" /f`

Disabling the schedule doesn't affect anything in your inbox or packets folders. You can re-run the ritual manually any time with:

```bash
claude -p "/operator:monday-packet --from-inbox"
```
