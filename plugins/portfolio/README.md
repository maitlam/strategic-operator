# portfolio

What a team takes on. Four skills.

## The domain view

Every team without an intake process has one anyway — it's informal, and it runs on proximity to whoever is loudest. That isn't an absence of prioritization. It's prioritization by access, which is the worst available algorithm and the hardest to see from inside.

These four make the portfolio legible in sequence: how things get in, how they're judged, how the whole set is doing, and whether the people exist to do it.

Two principles run through all of them. **Criteria are declared before scoring, never after** — otherwise you get criteria assembled to justify a conclusion someone already reached. And **a portfolio review that never kills anything is not a review**; it's validation with a meeting attached.

Intake and scoring are deliberately separate skills. Intake decides whether something is complete enough to evaluate; scoring decides whether it's good. Merge them and you spend the meeting debating merit on half-specified requests.

| Skill | In → Out |
|---|---|
| `portfolio-intake` | Unsorted requests → a front door with a defined bar |
| `opportunity-scoring` | An opportunity → a comparable read against declared criteria |
| `portfolio-health` | Active initiatives → a portfolio view, including what to kill |
| `resource-allocation` | Portfolio and team → what actually fits, and the binding constraint |

## Install

```
/plugin marketplace add maitlam/strategic-operator
/plugin install portfolio@strategic-operator
```

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`opportunity-scoring`](skills/opportunity-scoring/SKILL.md) | Original | Score an opportunity, proposal, vendor, or investment candidate against explicit criteria and produce a comparable, defensible read |
| [`portfolio-health`](skills/portfolio-health/SKILL.md) | Original | Produce a whole-portfolio read — where the money and people actually are, what has stalled, what should be killed, and whether the mix matches the stated strategy |
| [`portfolio-intake`](skills/portfolio-intake/SKILL.md) | Original | Design or run the front door for a portfolio — how opportunities enter, what information is required before anything is evaluated, and what happens to things that don't… |
| [`resource-allocation`](skills/resource-allocation/SKILL.md) | Original | Match a portfolio's demands against a team's real capacity and show where it is oversubscribed, including the person-level constraints that determine dates |
| [`portfolio-manager`](agents/portfolio-manager.md) (agent) | Original | Track and manage active initiatives across a portfolio — status, resources, dependencies, risks, executive sponsorship — and flag what's at risk or should be killed |
| [`portfolio-prioritizer`](agents/portfolio-prioritizer.md) (agent) | Original | Score new opportunities against declared strategic criteria and recommend invest / pause / kill / investigate |
<!-- catalog:end -->
