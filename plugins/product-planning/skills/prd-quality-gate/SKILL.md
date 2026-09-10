---
name: prd-quality-gate
description: Review a draft PRD against a short quality checklist before it goes to a stakeholder — is a decision actually being requested, is success measurable, are assumptions surfaced, is the "do nothing" option represented, is scope constrained. Not a PRD writer — a review lens applied after drafting. Use when the user has a draft PRD and wants a defensible read on whether it's ready for stakeholder review, when a PRD gets bounced back from an exec, or when the user's team keeps writing PRDs that no one acts on. Trigger on "review this PRD," "is this PRD ready," "why does this PRD keep getting kicked back," "what's wrong with this PRD," or as the last step before submitting a PRD to a decision-maker.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# PRD Quality Gate

The check between "I finished the PRD" and "the PRD is ready to go anywhere." Not another template — the review lens that catches the eight failure modes 80% of bad PRDs fall into.

## The framework behind this

PRDs fail in the same predictable ways, and most teams don't have a review step that catches them before an exec reads the draft. Executives learn to distrust PRDs from a specific team, and the team never finds out why — the doc just gets ignored or endlessly re-scoped.

The distinction the whole method rests on: **a PRD is a decision request, not a feature description.** If the doc doesn't ask for something specific — approval, investment, tradeoff sign-off, a green light — it's project documentation, not a PRD. Documentation gets filed. Decisions get made.

Three things follow.

**Measurable success beats descriptive success.** "Users will love it" is not success; "40% of active users complete the flow within a week of rollout" is. If nobody can independently score whether the PRD worked, the PRD has already failed as an accountability document.

**Assumptions surface or resurface.** Every PRD rests on assumptions. Good PRDs list them explicitly at the top; bad ones bury them in the middle and then get killed six weeks in when one turns out wrong. Naming an assumption is not weakness — it's what makes the PRD survivable.

**Reversibility calibrates depth.** Small reversible bets need a one-pager; large irreversible ones need real analysis. A PRD that treats every decision like a moon landing wastes the team; one that treats every decision like a hallway chat gets burned. Match effort to reversibility.

## The gate

Score the draft against these eight questions. Any RED must be fixed before the PRD ships anywhere.

### 1. Is a decision being requested?

Read the doc. Can you point to the specific decision the reader is being asked to make?

- ✅ **GREEN:** "Please approve investment of X FTE in Q2 to build Y for segment Z."
- 🟡 **YELLOW:** Decision is implied but not stated. Reader has to infer.
- 🔴 **RED:** No decision request. This is a project description, not a PRD.

### 2. Is success measurable?

- ✅ Success criteria have a number, a timeframe, and a source of truth.
- 🟡 Success criteria have a direction but no threshold ("we want X to increase").
- 🔴 Success criteria are qualitative ("users will love it") or absent.

### 3. Is "do nothing" represented?

Every real decision has "don't do this" as an option. If the PRD doesn't compare against the status quo, the reader has no baseline.

- ✅ The "do nothing" cost is stated: what happens to the business, the customer, or the metric if we don't ship this?
- 🟡 Mentioned in passing.
- 🔴 Not present. The PRD is a fait accompli.

### 4. Are assumptions surfaced?

- ✅ Top-of-document list, each assumption labeled with confidence (high / med / low) and how it would be tested if wrong.
- 🟡 Assumptions exist somewhere in the doc but aren't consolidated.
- 🔴 Assumptions are buried in narrative or unstated. These are the ones that kill the initiative in month 3.

### 5. Is scope constrained?

- ✅ In-scope list is bounded; explicit "not-in-scope" list follows it.
- 🟡 Scope is present but drifts (some sections imply more than the header states).
- 🔴 Feature list masquerading as scope. Doc reads as "we'll do all of this."

### 6. Is reversibility named?

- ✅ Doc states whether the decision is reversible or not, and calibrates analysis depth accordingly.
- 🟡 Implied via the amount of analysis.
- 🔴 Unstated. Small decisions treated as big; big decisions treated as small.

### 7. Are risks and their mitigations paired?

- ✅ Each named risk has either a mitigation or an explicit "accepted risk" note.
- 🟡 Risks listed without mitigations. Reads like a legal disclaimer.
- 🔴 No risks section, or risks buried.

### 8. Would a dissenter be represented?

If someone on the team disagreed with this PRD, is their view captured?

- ✅ The disagreement is named, along with what would change the dissenter's mind.
- 🟡 The disagreement is acknowledged but not represented.
- 🔴 The doc reads as unanimous. Suppressed disagreement resurfaces post-decision.

## The lengths test

Match doc length to reversibility:

- **Reversible (T2), small blast radius** — one-pager or less. If the PRD is longer than a page for a decision that could be undone in a sprint, it's over-engineered.
- **Reversible (T2), medium blast radius** — 2-3 pages max.
- **Irreversible (T1), or large blast radius** — full PRD, but even here rarely more than 5-7 pages. Beyond that you're writing a book.

## Process

1. **Score against the 8 questions.** Take five minutes. If more than 2 are RED, the PRD isn't ready — send it back with the specific gaps.
2. **Calibrate to reversibility.** If the doc is a one-pager on a T1 decision, request deeper analysis. If it's 12 pages on a T2 decision, request cuts.
3. **The stakeholder mock.** Read the doc as the intended decision-maker. What question would they ask that isn't answered? That's the section that needs to be added.
4. **The one-line ask.** Extract or write the specific ask the doc is making. If you can't fit it in one line, the ask isn't clear.

## Common failure modes

**Feature list masquerading as a PRD.** Long section on what the product will do, no section on why or with what tradeoffs. Reject.

**Success = "launch."** Success criteria that are satisfied by shipping. Rewrite as measurable outcomes.

**Assumption laundering.** Assumptions phrased as facts. Sniff-test: does the doc use the word "obviously" or "clearly"? Both are cues to look for a buried assumption.

**Roadmap masquerading as PRD.** A list of things over a quarter, none of which are a decision request. Split into individual PRDs or convert to `outcome-roadmap`.

**Everyone-signed-off doc.** No dissenting view represented. Ask who was NOT in the review, and whether their perspective would have changed anything.

## Output format

```markdown
# PRD Quality Gate — [PRD title], [date]

**Verdict:** GO / REVISE / RESUBMIT
**Reversibility:** T1 (irreversible) / T2 (reversible)

## Gate scores

| # | Question | Score | Note |
|---|---|---|---|
| 1 | Is a decision being requested? | R/Y/G | |
| 2 | Is success measurable? | R/Y/G | |
| 3 | Is "do nothing" represented? | R/Y/G | |
| 4 | Are assumptions surfaced? | R/Y/G | |
| 5 | Is scope constrained? | R/Y/G | |
| 6 | Is reversibility named? | R/Y/G | |
| 7 | Are risks + mitigations paired? | R/Y/G | |
| 8 | Would a dissenter be represented? | R/Y/G | |

## The one-line ask
[What is this PRD actually requesting? If you can't extract it in one line, that's finding #1.]

## RED findings (must fix)
- [Specific gap, with the section to rewrite]

## YELLOW findings (should fix)
- [Softer gaps]

## Length calibration
[Is the doc's length appropriate to the reversibility of the decision? If not, cut or expand.]

## The stakeholder question this doc doesn't answer
[The question the decision-maker will ask that the current draft leaves open.]

## Recommended next step
[Ship it / revise these three sections / start over with a different scope]
```

## When to hand off

- **The PRD is missing structure entirely** → `create-prd` (product-planning)
- **The PRD is an AI/ML feature** → `ai-feature-prd`
- **The PRD is a pricing change** → `pricing-prd`
- **The PRD would be better as a working-backwards press release** → `prfaq`
- **Success criteria need a proper metric tree** → `north-star-metric` or `metrics-dashboard` (bizops)
- **The decision needs a formal memo instead** → `decision-memo` (operating-model)
