---
name: portfolio-health
description: Produce a whole-portfolio read — where the money and people actually are, what has stalled, what should be killed, and whether the mix matches the stated strategy. Use whenever the user is preparing a portfolio or quarterly review, is running multiple initiatives and has lost the aggregate picture, needs to justify a portfolio to leadership, or asks what should be stopped. Trigger on "portfolio review," "how are our initiatives doing," "what should we kill," or any request spanning several efforts at once.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Portfolio Health

A set of active initiatives in. A read on the portfolio as a portfolio, out.

## The framework behind this

Portfolio review usually degenerates into serial project status — each initiative reports, everyone nods, the meeting ends. That produces a list, not a portfolio view, and it's why these reviews rarely change anything.

A portfolio view answers questions no single project report can:

**Where is the money and effort actually going, versus where strategy says it should?** Stated priorities and actual allocation diverge constantly, quietly, and in one direction: toward whatever is easiest to keep funding. The gap between the two is the single most useful number this exercise produces.

**What has stalled without being stopped?** Every portfolio carries initiatives that are technically alive and functionally dormant — no progress, no decision, no owner pushing. They consume attention and headroom rather than budget, which is why they survive scrutiny. Time since last meaningful progress finds them faster than any status field.

**What is the risk concentration?** Six initiatives that all depend on the same team, the same vendor, or the same assumption is one bet, not six.

And the discipline that makes the whole thing worth doing: **a portfolio review that never kills anything is not a review.** If nothing has ever been stopped, the process is validating, not deciding.

## Process

1. **Pull actual allocation** — people and budget by initiative — and compare it against stated priority.
2. **Compute time since last meaningful progress** for each. Not last update; last progress.
3. **Group by strategic theme** and check the mix against the strategy.
4. **Find the concentrations** — shared dependencies, shared assumptions, shared people.
5. **Name explicit kill and park candidates**, with reasons.
6. **Surface what isn't being funded** because of current commitments. Opportunity cost is invisible unless someone writes it down.

## Output format

```markdown
# Portfolio Health: [Team] — [period]

## The read
[Three or four sentences. State of the portfolio as a whole, not a summary
of each item.]

## Allocation vs. stated priority
| Theme | Stated priority | Actual people | Actual $ | Gap |
|---|---|---|---|---|
*The gap column is the point of this table.*

## Initiatives
| Initiative | Stage | Owner | Last real progress | Health | Note |
|---|---|---|---|---|---|

## Stalled
- **[Initiative]** — [N weeks since progress]. [What it's waiting on, or
  whether anyone is still pushing it.]

## Kill / park candidates
- **[Initiative]** — [reason, what stopping frees up, who decides]

## Concentration risk
- [Shared dependency, vendor, assumption, or person across N initiatives.]

## Not funded because of current commitments
- [Opportunity cost, named.]
```

## Hold the line on

- **Measure last meaningful progress, not last update.** A weekly status note is not progress and will mask a dormant initiative indefinitely.
- **Always produce kill candidates**, even weak ones. A review with an empty list has stopped functioning as a review; if nothing genuinely qualifies, say so explicitly rather than leaving the section blank.
- **Never let effort narratives substitute for progress.** Activity is not movement.
- **Report the allocation gap even when it's awkward.** That gap is usually the most valuable output and the most likely to be softened.
