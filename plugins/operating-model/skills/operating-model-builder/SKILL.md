---
name: operating-model-builder
description: Design an operating model for a team from scratch — purpose, cadence, artifacts, roles, and the decisions the model exists to make possible. Use whenever a team has no existing process to inherit, a new team or function is standing up, an existing model has stopped working, or the user says things like "we have no process," "how should this team run," or "everything is ad hoc." Trigger for any request to design how a team operates rather than what it works on.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Operating Model Builder

A team and a mandate in. The machinery that lets it decide well and explain itself, out.

## The framework behind this

A small team's real constraint is not capacity. Six people can do an enormous amount of work. What they cannot do by default is stay pointed in the same direction, remember why they decided something four weeks ago, or give a funder a straight answer about what changed since last month.

Those failures never announce themselves. They surface as a quarterly review where the team discovers it holds three different mental models of its own strategy.

An operating model is the machinery that prevents that. It is not process for its own sake. Every element must answer one question: **what has to be true for this team to make good decisions and be able to explain them?** Anything that doesn't answer it is ceremony, and ceremony is what gives operating models their bad name.

Three principles run through every model this skill produces.

**The artifact is the process.** Don't design a meeting — design the document the meeting must produce, then work backwards to the minimum meeting that produces it. A weekly sync with no defined output is a status ritual. A weekly sync that must produce a rollup with named risks is a forcing function.

**Write down what "good" means, once.** Most teams carry their quality standards in one or two people's heads. That holds until those people are on vacation, or the team doubles, or the work goes to a contractor. A written standard can be argued with and improved; a standard living in someone's head can only be guessed at.

**Surface the unresolved rather than resolving it prematurely.** Models that produce only clean artifacts are models that quietly drop everything messy. Decisions get recorded; the disagreement that preceded them doesn't. Every artifact in a good model has a slot for what is still open.

## Process

1. **Establish the mandate and the funder.** Who pays for this team, what they expect, and how often they need to hear from it. Almost every cadence question resolves here.
2. **Name the decisions the team must make repeatedly.** What enters the portfolio, what gets resourced, what stops. The model exists to serve these; design backwards from them.
3. **Define the artifacts** each decision requires, and who authors each.
4. **Set the minimum cadence** that keeps those artifacts current. Start smaller than feels right — cadences are far easier to add than to remove.
5. **Assign roles**, especially the owner of the model itself. Shared ownership of process means nobody owns it.
6. **Define what "good" looks like** for each artifact, in writing.
7. **Name what will be instrumented**, on day one. This is the part everyone skips and nobody can retrofit.

## Output format

```markdown
# Operating Model: [Team]
*Version 1 · [date] · Owner of this model: [name]*

## Mandate
[What this team exists to do, who funds it, what they expect and when.]

## The decisions this model serves
1. [Recurring decision] — decided by [role], at [cadence], on the basis of [artifact]

## Cadence
| Rhythm | Forum | Required output | Owner | Audience |
|---|---|---|---|---|
*Start minimal. Anything without a required output is a candidate to cut.*

## Artifacts
| Artifact | Author | Standard for "good" | Where it lives |
|---|---|---|---|

## Roles
| Role | Person | Owns |
|---|---|---|
| Owner of the model | | The cadence and templates; the only person who changes them |
| Decider | | [Per decision type] |

## Instrumentation from day one
- [What gets logged, by whom, starting now. A baseline cannot be
  reconstructed later.]

## Deliberately not in v1
- [What was considered and left out, and the condition that would add it.]

## Review
This model gets reviewed at [cadence] using `retro` output. Version history
lives at [location].
```

## Hold the line on

- **Refuse to design a forum with no required output.** Ask what document it produces; if there's no answer, that's a meeting to delete, not to schedule.
- **Start below the cadence the user proposes.** Teams reliably over-specify at v1 and then quietly abandon half of it, which teaches everyone the model is optional.
- **Insist on a single named owner of the model.** Not a committee.
- **Do not skip instrumentation because nothing is measurable yet.** That is precisely when to start; the baseline disappears the moment the new way is in place.
- **A model that produces artifacts nobody reads is failing.** Ask who reads each one. If the answer is nobody, cut it.
