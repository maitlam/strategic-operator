# Skill review checklist

A working checklist for curating this collection: which included skills to keep, which to adapt, which to remove, and what's missing. Remove a skill with `python3 scripts/catalog.py --remove <name>`.

## 1. Overlapping skills

These pairs do similar jobs. Claude picks between them based on the request, so overlap can make results less predictable. For each pair, keep one, adapt one to absorb the best of both, or keep both and sharpen their descriptions so they trigger in different situations.

| Decide | Skill | Similar to |
|:---:|---|---|
| [ ] | `programs:status-update-generator` | `bizops:status-report`, `programs:stakeholder-update` |
| [ ] | `programs:sprint-plan` | `programs:sprint-planning` |
| [ ] | `strategy:create-prd` | `strategy:write-spec` (plus the `ai-feature-prd` and `pricing-prd` variants) |
| [ ] | `strategy:interview-synthesis` | `strategy:synthesize-research` |
| [ ] | `strategy:brainstorm-ideas` | `strategy:product-brainstorming` and the `/strategy:brainstorm` command |
| [ ] | `bizops:metrics-dashboard`, `bizops:north-star-metric` | `bizops:metrics-review` |
| [ ] | `strategy:outcome-roadmap`, `strategy:roadmap-communication`, `strategy:prioritization-frameworks` | `strategy:roadmap-update` |
| [ ] | `bizops:summarize-meeting` | `bizops:meeting-analyzer` |
| [ ] | `programs:senior-pm` | `programs:program-manager` (portfolio vs. single program) |
| [ ] | `programs:delivery-manager` (change management parts) | `bizops:change-request` |

Complementary rather than duplicate, and likely worth keeping together: `programs:pre-mortem` with `bizops:risk-assessment`, and `strategy:competitive-brief` with `strategy:porters-five-forces` / `strategy:swot-analysis`.

## 2. Fit with Biz Ops, Strategy, and Programs

Worth asking of each group: does it strengthen the story of this collection, or dilute it?

- [ ] **PM career:** `pm-1on1s`, `pm-career-ladder`, `pm-interview-prep`, `pm-onboarding`
- [ ] **Tool administration:** `atlassian-admin`, `atlassian-templates`, `confluence-expert`, `jira-expert`, `linear-expert`, `notion-pm`, `productboard-expert`
- [ ] **Engineering-team delivery mechanics:** `agile-coach`, `scrum-master`, `backlog-refinement`, `story-mapping`, `story-splitting`, `job-stories`, `wwas`, `test-scenarios`, `feature-flag-strategy`, `release-notes`, `cycle-time-analyzer`, `sprint-retrospective`
- [ ] **Narrow product documents:** `ai-feature-prd`, `pricing-prd`, `eol-communication`

## 3. Best candidates to adapt

Skills where hands-on Biz Ops and Programs experience changes the output most, and where an Adapted version with a clear `CHANGES.md` shows judgment:

- [ ] `bizops:status-report`
- [ ] `bizops:quarterly-planning`
- [ ] `bizops:metrics-review`
- [ ] `bizops:meeting-analyzer`
- [ ] `programs:program-manager`
- [ ] `programs:stakeholder-update`

## 4. Gaps for original skills and agents

Work a strategic operator does that nothing here covers well yet:

- [ ] `bizops:weekly-business-review`: turn a metrics export into a WBR pack
- [ ] `bizops:investor-update`: monthly investor update from metrics and highlights
- [ ] `bizops:board-prep`: board deck outline, pre-reads, and follow-ups
- [ ] `strategy:market-sizing`: TAM/SAM/SOM with explicit, checkable assumptions
- [ ] `strategy:strategy-memo`: a decision memo with options, tradeoffs, and a recommendation
- [ ] `programs:program-health-check`: a quick diagnostic of a struggling initiative
- [ ] `programs:exec-escalation`: a crisp escalation that gets a decision
- [ ] **Agent:** a chief-of-staff agent that takes messy input (a founder brain dump, a meeting transcript) and routes it to the right skills
