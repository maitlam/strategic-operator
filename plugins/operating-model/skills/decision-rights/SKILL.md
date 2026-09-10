---
name: decision-rights
description: Map who decides what on a team or program — the authority to approve, to break a tie, to spend, and to stop — and surface where that authority is currently undefined. Use whenever decisions are stalling, two people think they own the same call, work spans teams with no clear arbiter, someone asks "who actually decides this," or a new program is being set up. Trigger on ambiguity about authority, not about tasks.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Decision Rights

A team or program in. An explicit map of who holds which authority, out.

## The framework behind this

Most cross-team dysfunction that gets diagnosed as a communication problem is a decision-rights problem. Nobody is confused about what needs to happen. They're confused about who gets to say so, and the resulting standoff is polite, slow, and invisible until it's expensive.

The distinction that makes this tractable: **a RACI covers tasks; decision rights cover authority.** Listing who is responsible for building the thing tells you nothing about who can approve a scope change to it. Teams produce elaborate responsibility matrices and still stall, because they mapped the wrong object.

Two disciplines.

**Four authorities, named separately.** Approve, break a tie, commit money or people, and stop. These come apart in practice more often than people expect — the person who can approve a scope change frequently cannot stop the project, and the person who can spend often isn't the tie-breaker. Collapsing them into "the owner" is what produces the standoff.

**Consultation is not authority.** Being consulted, being informed, and having a veto are three different things, and conflating them is the second-most-common source of stalling. A stakeholder who believes they hold a veto they were never granted will exercise it anyway.

Then the sharpest question in the whole exercise: **name the decisions that currently have no owner.** That list is usually short, always uncomfortable, and is the actual output.

## Process

1. **List the recurring decisions**, not the tasks.
2. **For each, assign the four authorities** to named individuals.
3. **Distinguish consulted, informed, and veto** — and be strict, because people over-claim veto.
4. **Set the default when the decider is unavailable.** A model that stalls on one person's vacation isn't a model.
5. **Name the escalation path**, one level, with a name.
6. **Surface the unowned decisions.** Do not paper over them.

## Output format

```markdown
# Decision Rights: [Team / Program]
*[date] · Ratified by: [name]*

## Decision map
| Decision | Approves | Breaks ties | Commits $ / people | Can stop |
|---|---|---|---|---|

## Consultation
| Decision | Must consult | Informed after | Holds a veto |
|---|---|---|---|
*Veto is rare. If this column has many entries, they are not real vetoes.*

## Defaults
| If [decider] is unavailable | Decision passes to | Or waits until |
|---|---|---|

## Escalation
[One level up, named. Not "leadership."]

## Currently unowned
- **[Decision]** — [who it's stalling, what it's costing, proposed owner]

*This section is the point of the exercise. Do not leave it empty by
assigning owners that nobody has agreed to.*
```

## Hold the line on

- **Never assign an authority to a group.** A committee cannot break a tie; that's what tie-breaking means.
- **Do not silently propose owners.** An unowned decision with a proposed owner who hasn't agreed is still unowned. Mark it as a proposal.
- **Keep veto scarce.** If everyone has one, the team has consensus governance, and that should be stated plainly rather than discovered.
- **Do not convert this into a RACI.** If the user asks for task ownership, say that's a different artifact and offer it separately.
