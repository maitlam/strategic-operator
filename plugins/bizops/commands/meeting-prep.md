---
description: Prep for a meeting — its purpose and the decision it needs, open items from last time, who's in the room and what they care about, the questions to ask, and a time-boxed agenda; or a recommendation to cancel it
argument-hint: "<meeting name, topic, or calendar event>"
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: "0.1.0"
---

# /meeting-prep

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Walk into a meeting knowing what it's for, what was left open last time, who's there and what they want, and what you need to leave with. This command produces a one-page prep pack and a proposed agenda. Its first job is to check whether the meeting needs to happen at all — a meeting with no decision to make and no exchange that needs a room should be an email, and the prep says so.

## Usage

```
/meeting-prep $ARGUMENTS
```

## How It Works

```
┌────────────────────────────────────────────────────────────────┐
│                       MEETING PREP                             │
├────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                     │
│  ✓ Pin down the purpose and the decision sought                │
│  ✓ Surface open actions and undecided items from last time     │
│  ✓ Map who's attending and what each of them needs             │
│  ✓ Draft the questions, the agenda, and the pre-read ask       │
├────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                    │
│  + Calendar: Pull the invite, attendees, and the last instance │
│  + Meeting transcription: Read last time's notes and register  │
│  + Knowledge base: Pull the docs the meeting will reference    │
│  + Chat: Catch what's been discussed since last time           │
└────────────────────────────────────────────────────────────────┘
```

## Workflow

### 1. Identify the meeting

Name, when, recurring or one-off. If **~~calendar** is connected, pull the invite and attendee list. Otherwise ask.

### 2. Pin the purpose

One of: make a decision, resolve a disagreement, exchange information that genuinely needs discussion, or build a relationship. Name which. If none applies, recommend cancelling or going async — and draft the message that replaces it.

### 3. Pull what's open from last time

For a recurring meeting, read the last instance's notes — via **~~meeting transcription** or the register kept by `meeting-analyzer`. List: actions still open and by whom; items raised and not decided; anything promised for this session.

### 4. Map the room

For each attendee (or each role, if the list is long): what they need from this meeting, what they're likely to push back on, and what they know that you don't. For high-stakes meetings, run the `stakeholder-map` lens on power and interest. Note who is missing whose absence blocks a decision.

### 5. Draft the questions

The three to five questions that, answered, make this meeting worth having. Order them by what unblocks the decision.

### 6. Build the agenda

Time-boxed, decision first, information exchange after. Name what "done" looks like for each block. Include a pre-read ask if a decision needs one, and send it early enough to be read.

### 7. Name the exit

What you must leave with. The decision recorded, the owner named, the date set. If the meeting ends without it, what's the fallback?

## Output

```markdown
# Prep — [meeting] · [date/time]
*Purpose: [decision / disagreement / exchange / relationship]. Recommendation: [hold / shorten / go async]*

## The decision this meeting needs
[One sentence. Who makes it. What happens if it isn't made here.]

## Open from last time
| Item | Owner | Status | Needs attention today? |
|---|---|---|---|

## The room
| Who | Needs | Likely to push on | Knows that we don't |
|---|---|---|---|
**Missing and it matters:** [names, why]

## Questions to ask
1. …

## Agenda ([n] min)
| Block | Min | Done looks like |
|---|---|---|

## Pre-read
[What to send, to whom, by when — or "none needed"]

## Must leave with
- [decision · owner · date]
```

## Rules

- **Purpose first, and be willing to cancel.** The most valuable prep sometimes ends the meeting.
- **Open items from last time are always surfaced.** Recurring meetings that forget their own commitments stop deciding anything.
- **Decision before information** on the agenda.
- **The exit is named before the meeting starts.**

## Skills this command uses

- `meeting-analyzer` — the register of decisions, actions, and open questions from prior instances
- `stakeholder-map` (programs plugin) — power × interest read for high-stakes rooms
