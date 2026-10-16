# Manual — feeding the Operator inbox by hand

No automation. You drop files into `{{STATE_DIR}}/inbox/` during the week, and the scheduled Monday/Friday rituals pick them up.

This is a legitimate path. It's simpler than any workflow tool, works offline, and matches how plenty of operators actually keep notes (screenshot of calendar → file; copy-paste from email → text file).

The tradeoff: if you forget to drop context, the ritual fires with an empty-inbox warning and a blank packet. Build the habit or wire a workflow tool later.

---

## The contract

The ritual commands read **every file** in `{{STATE_DIR}}/inbox/` on their scheduled fire. You get to pick:

- **File names** — optional prefixes route to specific buckets (`calendar-*`, `email-*`, `docs-*`, `status-*`, `notes-*`). Files without a prefix get classified by content.
- **File formats** — `.md`, `.txt`, `.json`, `.csv` all work.
- **When to drop files** — any time during the week. Monday ritual reads what's there Monday morning; Friday ritual reads what's there Friday afternoon.

After the ritual runs, processed files are **moved** to `{{STATE_DIR}}/inbox/archive/YYYY-WXX/`. The inbox stays clean; nothing is lost.

---

## Examples of what to drop

**Calendar screenshot or paste** — `calendar-2026-10-19.md`:
```markdown
# This week

Mon 10:00 — QBR dry-run w/ Sarah
Tue 14:00 — 1:1 w/ CEO
Wed 11:00 — Launch readiness w/ Platform
Fri 15:00 — All-hands prep
```

**Email thread you need to action** — `email-sarah-q3-variance.txt`:
```
From: Sarah Chen
Subject: Q3 variance
Fri 5:30 PM

Can we walk through the Q3 variance analysis next week?
I'd like to see the breakdown by segment.
```

**Status snapshot from a tracker** — `status-2026-10-18.md`:
```markdown
## Open items
- Pricing memo — stalled, Marco OOO
- Platform launch — on track, SOC2 signoff pending
- Mobile prototype — paused (CEO decision 10/14)

## Risks
- Q3 budget variance $420K; Sarah flagged
```

**Freeform notes** — `notes-friday-thoughts.md`:
```markdown
Things I want next week to resolve:
- Decision on Q4 planning timeline
- Marco's return date + pricing memo DRI backup
```

---

## When to drop what

Suggested weekly rhythm:

- **During the week:** drop one `notes-*.md` as you think of things worth tracking. Three sentences each is fine.
- **Thursday or Friday morning:** paste a `calendar-*.md` for the following week (helps Monday ritual).
- **Friday afternoon before the ritual:** paste a `status-*.md` and any `email-*` threads you want surfaced.

If a week goes by with nothing dropped, the Monday packet will fire with:

```
⚠ Inbox was empty — did you forget to drop context this week?
```

That's the signal to either start the habit or set up a workflow tool.

---

## Verify it works

```bash
# Drop a test file
echo "Test calendar entry: Mon 10am team sync" > {{STATE_DIR}}/inbox/calendar-test.md

# Fire the ritual manually
claude -p "/operator:monday-packet --from-inbox"
```

Check `{{STATE_DIR}}/packets/` for the output and `{{STATE_DIR}}/inbox/archive/` for the moved test file.

---

## When to upgrade from manual

Switch to Power Automate, Apps Script, or bash cron when either:

- You've gone 2+ weeks forgetting to drop files and the empty-inbox warning is noise
- You find yourself hand-exporting the same calendar data every week — automation pays back fast
- Your calendar signals matter more than your freeform notes for the Monday framing

Rerun `/operator:setup-scheduling` with a different workflow tool answer. The schedule stays; only the input feed changes.
