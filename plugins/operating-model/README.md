# operating-model

How a team runs. Four skills.

## The domain view

Almost nothing about how teams actually operate is written down publicly. Product frameworks are everywhere; the machinery underneath — who decides, which forums exist, what artifact each one requires — lives in the heads of people who've stood one up, and it gets rebuilt badly from scratch every time.

The through-line: **an operating model exists to answer one question — what has to be true for this team to make good decisions and be able to explain them?** Anything that doesn't answer it is ceremony, and ceremony is what gives operating models their bad name.

Two failure patterns these are built against. Governance that only adds, never deletes, until a six-person team carries eleven recurring forums. And authority that was never assigned, producing standoffs that are polite, slow, and invisible until they're expensive.

| Skill | In → Out |
|---|---|
| `operating-model-builder` | A team and a mandate → the machinery to decide well and explain itself |
| `decision-rights` | A team or program → who holds which authority, and what's unowned |
| `governance-design` | Oversight needs → the smallest set of forums that produces decisions |
| `okr-tracking` | Goals → key results that measure outcomes, not activity |

## Install

```
/plugin marketplace add maitlam/strategic-operator
/plugin install operating-model@strategic-operator
```

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`decision-rights`](skills/decision-rights/SKILL.md) | Original | Map who decides what on a team or program — the authority to approve, to break a tie, to spend, and to stop — and surface where that authority is currently undefined |
| [`governance-design`](skills/governance-design/SKILL.md) | Original | Design the review and forum layer for a team or portfolio — which recurring meetings exist, what each one decides, what artifact it requires as input, and which existing… |
| [`okr-tracking`](skills/okr-tracking/SKILL.md) | Original | Draft, review, or check in on objectives and key results — including diagnosing OKRs that are really task lists in disguise |
| [`operating-model-builder`](skills/operating-model-builder/SKILL.md) | Original | Design an operating model for a team from scratch — purpose, cadence, artifacts, roles, and the decisions the model exists to make possible |
<!-- catalog:end -->
