---
name: governance-design
description: Design the review and forum layer for a team or portfolio — which recurring meetings exist, what each one decides, what artifact it requires as input, and which existing meetings should be deleted. Use whenever the user is setting up reviews or steering committees, is drowning in recurring meetings, needs a portfolio or program review cadence, or asks how leadership should oversee something. Trigger on "governance," "steering committee," "review cadence," or too many meetings producing too few decisions.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Governance Design

A team's oversight needs in. The smallest set of forums that produces the required decisions, out.

## The framework behind this

Governance is the most over-built layer of any operating model, and the reason is a category error: forums get created to *increase visibility*, when the only thing that justifies a recurring meeting is that a **decision** comes out of it.

Visibility is a document problem. It is solved by a dashboard or a written update that people read on their own time. Converting a visibility need into a standing meeting is how a six-person team ends up with eleven recurring forums and no time to do the work.

So the governing rule: **every forum must name the decision it makes.** If it can't, it's a written artifact, not a meeting.

Two more.

**Each forum needs a required input artifact, circulated in advance.** A review where people read the material in the room is a reading meeting, and the quality of the decision reflects that. This is also what makes reviews shorter — a forum with a pre-read runs at half the length of one without.

**Design the deletions.** New governance nearly always gets layered on top of what exists, and the old forums persist because nobody has authority to cancel them. Any governance design that doesn't say what stops has increased the load, whatever else it accomplished.

## Process

1. **List the decisions that require a group**, and only those. A decision one person can make does not need a forum.
2. **Group decisions by cadence and by audience.** Most teams need two or three forums, not seven.
3. **For each forum, define** the decision, the required pre-read, the attendees, the decider, and the duration.
4. **Set the escalation route** between forums.
5. **Name what gets deleted or merged.**
6. **Define the failure signal** — what tells you this forum has stopped being worth its time.

## Output format

```markdown
# Governance: [Team / Portfolio]
*[date] · Owner: [name]*

## Forums
### [Forum name] — [cadence, duration]
- **Decides:** [the specific decision. If you can't fill this in, delete
  the forum.]
- **Required pre-read:** [artifact, circulated N days prior]
- **Attendees:** [smallest set with authority]
- **Decider:** [one name]
- **Output:** [what exists afterward that didn't before]

## Escalation between forums
[Route, with names and the threshold that triggers it.]

## Deleting or merging
| Existing forum | Action | Why |
|---|---|---|

## Handled in writing instead
- [Visibility needs that do not become meetings, and where they live.]

## Failure signals
- [e.g. three consecutive sessions with no decision recorded; pre-read
  not circulated; the decider stops attending.]
```

## Hold the line on

- **A forum with no decision is a written update.** Say so and move it.
- **Require a pre-read.** A review without one will produce worse decisions and run twice as long.
- **Insist on the deletions list.** Governance that only adds is a net cost.
- **Keep attendee lists small.** Every additional attendee reduces the odds of a real decision; invite authority, not interest.
- **Do not design a forum the team has no artifact to feed.** Build the artifact first.
