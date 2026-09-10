---
name: opportunity-scoring
description: Score an opportunity, proposal, vendor, or investment candidate against explicit criteria and produce a comparable, defensible read. Use whenever the user needs to evaluate or prioritize options, has a backlog to rank, is doing build/buy/partner analysis, or asks whether something is worth pursuing relative to other things. Trigger on "should we pursue," "how does this compare," "help me prioritize these," or any assessment against a bar.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Opportunity Scoring

An opportunity in. A scored, comparable read against declared criteria, out.

## The framework behind this

Scoring exists to make decisions comparable across time and across people. That's the whole point — not to produce a number, but to produce a number that means the same thing in March as it did in January, and the same thing when a colleague assigns it as when you do.

Three things follow.

**Criteria are declared before scoring, never after.** The most common failure is scoring an opportunity against criteria assembled to justify a conclusion someone already reached. If the criteria aren't written down in advance, this skill's first job is to make the user state them.

**A composite score is a conversation starter, not a verdict.** Weighted totals hide their own reasoning; two opportunities at 3.4 can be completely different objects. The dimension-level scores and the stated reasons are the output. The total is an index for sorting.

**Confidence is a separate axis from score.** A high score built on three assumptions is a different thing than a high score built on evidence, and collapsing them is how organizations fund confident guesses. Every screen carries both.

The default criteria below suit venture and portfolio work. Replace them — the framework is that criteria are explicit, weighted, and stable, not that these five are correct.

## Process

1. **Establish the criteria.** Use the user's set exactly if they have one. If not, propose the defaults and get agreement before scoring anything.
2. **Score each dimension 1–5** with a one-line reason. A score without a reason is unauditable.
3. **Rate confidence per dimension** — evidence, inference, or assumption.
4. **Compute the weighted total** and say what it does and doesn't mean.
5. **Name disqualifiers.** Some things don't trade against a high score elsewhere; a regulatory blocker at 1 doesn't average out.
6. **Recommend a disposition** — pursue, park, pass, or insufficient information. The fourth is real and underused.

## Default criteria

| Criterion | Weight | 1 → 5 |
|---|---|---|
| **Problem severity** | 25% | Nice to have → someone already pays to solve it badly |
| **Strategic fit** | 25% | Adjacent curiosity → directly advances a stated priority |
| **Feasibility** | 20% | Needs capability we lack → could start Monday |
| **Time to signal** | 15% | Years to learn if it works → weeks |
| **Defensibility** | 15% | Anyone could do this → real structural advantage |

## Output format

```markdown
# Opportunity Score: [Name]
*[date] · Criteria set: [name/version] · Scored by: [who]*

## Disposition
**[Pursue / Park / Pass / Insufficient information]** — [one line]

## Scores
| Criterion | Score | Weight | Reason | Confidence |
|---|---|---|---|---|
| | /5 | | | Evidence / Inference / Assumption |

**Weighted total: X.X / 5.0**
*Comparable only against screens using the same criteria set.*

## Disqualifiers
- [Anything that overrides the score, or "none identified"]

## What would change this read
- [The specific finding that would move the disposition, and how to get it]

## Assumptions this rests on
- [Every dimension scored Assumption, collected in one place.]
```

## Hold the line on

- **Never invent criteria mid-scoring to fit a conclusion.** If the criteria are wrong, revise them explicitly for every opportunity, not just this one.
- **"Insufficient information" is a real disposition.** Forcing a score on unresearched work produces a number that gets quoted later as though it meant something.
- **Never let a high total bury a disqualifier.** Surface it above the score.
- **Flag criteria drift.** If the criteria changed since earlier screens, prior scores are no longer comparable and the output must say so.
