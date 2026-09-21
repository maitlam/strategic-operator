---
name: signal-scan
description: Sweep the team's own recent conversations — meeting notes, customer calls, interviews, internal briefs — for research signals, deduplicate them against a running signal log, and flag the ones that have now been seen from more than one independent source. Use whenever a batch of new notes has landed and nobody has asked what they add up to, when setting up a standing "what should we know more about" log, or when the user asks what questions keep coming up. Trigger on "scan the notes," "what are we hearing," "signal log," "what should we be researching," or any request to mine internal notes for open questions rather than action items.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Signal Scan

A window of recent internal notes in. A signal log that remembers what the team keeps hearing, out.

## The framework behind this

Teams that talk to a lot of people accumulate questions faster than they notice them. Someone mentions a competitor move in passing, a customer raises a concern nobody follows up on, two interviews a week apart circle the same unresolved thing — and each note gets read once, filed, and forgotten. The pattern was there; nobody was keeping the memory.

The signal log is the memory. A **signal** is anything that produces the reaction "we should know more about that" — an unanswered question, a market move mentioned without follow-up, a claim that contradicts what the team currently believes, a theme recurring across conversations. It is not an action item (those have an owner and a date and belong in a tracker), and it is not a fact the team already has documented.

The discipline that makes the log worth keeping is **counting independent sources.** A signal heard once is a curiosity. The same signal from a second, independent source is a different object — it has earned research time. The scan's most valuable output is not the new rows; it's the rows whose count just went from one to two.

Two guards. **Be selective per source** — a cap on signals per note forces judgment and keeps the log readable. And **every signal is traceable** — a signal without its source can't be checked, weighed, or graduated.

## Gather first

- The signal log. If none exists, create it with the format below — the first scan seeds it.
- The scan window (default: since the last scan, or the last few days) and the sources inside it.
- The team's category set for signals, if one exists. If not, derive categories from the first scan and keep them.

## Process

1. **Set the window.** List the sources that fall inside it. Note any that couldn't be read.
2. **Read each source and extract.** If a note has an explicit section for signals or open questions, take those first — the team has already flagged them. Then read the body for the general kinds: unanswered questions, market moves mentioned in passing, contradictions with current belief, recurring themes.
3. **Exclude** action items, facts already well documented, and one-off opinions with no wider relevance.
4. **Deduplicate against the log.** For each candidate:
   - Exact or near-duplicate from a source already recorded → skip.
   - Same signal, new independent source → update the existing row: increment the count, add the source.
   - Genuinely new → new row.
   An independent source is a different person or organization. The same person raising it twice is one source.
5. **Categorize.** Use the existing category set. Add a category only when nothing fits, and say so in the report.
6. **Update the log.** Append new rows; edit updated rows in place.
7. **Report.** Sources scanned, rows added, rows updated, and — most importantly — rows now at two or more independent sources that are ready to graduate to the research agenda.

## Output format

The log:

```markdown
# Signal Log

| Signal | Category | First seen | Sources | Count | Status |
|---|---|---|---|---|---|
| [One sentence. What we should know more about.] | [Category] | [date] | [source; source] | [N independent] | Monitoring / Graduated / Closed |
```

The scan report:

```markdown
## Signal scan — [window]
- Sources scanned: [N], [list or count by type]
- New signals: [N]
- Updated (new independent source): [N]
- **Ready to graduate (2+ independent sources):**
  - [Signal] — [sources]
- New categories introduced: [none / list with reason]
```

Statuses: **Monitoring** (default for new), **Graduated** (moved to the research agenda — link it), **Closed** (answered or no longer relevant, with a note).

## Hold the line on

- **At most five signals per source.** Selectivity is the job. If a note seems to have ten, the best five are the signal and the rest are noise.
- **One sentence per signal.** If it needs a paragraph, it's a research brief, not a signal.
- **Always cite the source.** An untraceable signal is dropped.
- **Count independent sources, not mentions.** One person three times is one.
- **Never log action items.** They have a home; this isn't it.
- **Graduation is a recommendation, not automatic.** The scan flags; a person moves it to the agenda.
