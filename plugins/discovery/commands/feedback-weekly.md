---
description: Weekly customer-feedback analysis — gather the week's inbound from every channel, triage and deduplicate it, count independent sources per theme, show what moved since last week, and route each theme to where it belongs
argument-hint: "[week or date range]"
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: "0.1.0"
---

# /feedback-weekly

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Turn a week of scattered customer feedback — support tickets, sales notes, NPS verbatims, in-app comments, exec forwards — into a short digest the team can act on: what's recurring, what's new, what moved, and where each theme should go. The discipline is counting, not quoting. One vivid complaint is an anecdote; the same complaint from six unrelated accounts is a theme, and the digest says which is which.

## Usage

```
/feedback-weekly $ARGUMENTS
```

Defaults to the last seven days.

## How It Works

```
┌────────────────────────────────────────────────────────────────┐
│                     FEEDBACK WEEKLY                            │
├────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                     │
│  ✓ Triage pasted or exported feedback from any channel         │
│  ✓ Deduplicate and count independent sources per theme         │
│  ✓ Compare against last week's digest                          │
│  ✓ Route each theme: roadmap, bug, research, or watch          │
├────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                    │
│  + User feedback: Pull the week's tickets, NPS, and in-app     │
│  + Chat: Catch sales and CS notes shared in channels           │
│  + Project tracker: Link themes to existing tickets and epics  │
│  + Knowledge base: Read and append the digest history          │
└────────────────────────────────────────────────────────────────┘
```

## Workflow

### 1. Set the window and gather

Last seven days unless told otherwise. Pull from **~~user feedback** and **~~chat** if connected; otherwise ask for exports or pastes. List the channels covered and the ones missed — a digest that only saw support tickets should say so.

### 2. Triage

Run `customer-feedback-triage`: categorize each item, deduplicate, score. Tag the source of each item — account, segment, channel — because step 3 depends on it.

### 3. Count independent sources per theme

Cluster the triaged items into themes. For each, count *independent* sources: distinct accounts or organizations, not distinct messages. Three tickets from one customer is one source. Classify:
- **Recurring** — 3+ independent sources
- **Emerging** — 2, typically new this week
- **Single** — 1, reported as such

### 4. Compare with last week

Read the previous digest. What was emerging and is now recurring? What faded? What's genuinely new? A theme's trajectory matters more than its size this week.

### 5. Route

Each recurring or emerging theme goes somewhere:
- **Roadmap** — a product gap; link or create the tracker item
- **Bug** — something broken; link the ticket
- **Research** — the team doesn't understand it well enough to act; send to the research agenda or signal log if the intelligence plugin is installed
- **Watch** — not yet actionable; carry to next week

Single-source items are listed, not routed, unless one is severe enough to escalate on its own.

### 6. Write the digest

One page. Counts, trajectories, routing. Quotes only where they clarify a theme, never as a substitute for a count.

## Output

```markdown
# Feedback digest — week of [date]
*Channels covered: [list]. Missed: [list or none]. Items triaged: [n]*

## Read in one paragraph
[What this week's feedback says, at the confidence the counts support.]

## Recurring (3+ independent sources)
| Theme | Sources | Trend vs last week | Routed to |
|---|---|---|---|

## Emerging (2 sources)
| Theme | Sources | First seen | Watch for |
|---|---|---|---|

## Single-source, noted
| Item | Source | Why it's here |
|---|---|---|

## Since last week
- [emerging → recurring / faded / new]

## Routed this week
| Theme | Destination | Link |
|---|---|---|
```

## Rules

- **Count sources, not messages.** One account, many tickets: one source.
- **Never promote a single-source item to a theme.** However well-phrased.
- **Always report the channels missed.** The digest is a sample; say of what.
- **Every recurring theme is routed.** A digest that only describes has done half the job.
- **Trajectory over size.** Say what moved.

## Skills this command uses

- `customer-feedback-triage` — categorize, deduplicate, score
- `synthesize-research` — theme extraction across the week's material
- `research-agenda` / `signal-scan` (intelligence plugin, if installed) — where "we don't understand this yet" themes go
