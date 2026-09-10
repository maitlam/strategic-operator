# Biz Ops

Skills for running the business day to day: the operating rhythm (quarterly planning, OKRs, metrics reviews), the processes and vendors underneath it, and meetings that end in decisions.

Install with `claude plugin install bizops@strategic-operator`, then call any skill directly as `/bizops:<skill-name>` or just describe what you need.

Some skills can pull from connected tools like Slack or Jira; see [CONNECTORS.md](CONNECTORS.md). A few of borghei's skills reference [SHARED_OUTPUT_SCHEMA.md](SHARED_OUTPUT_SCHEMA.md) for their Python tools' output formats. Licenses for borrowed work are in [LICENSES/](LICENSES/).

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`metrics-dashboard`](skills/metrics-dashboard/SKILL.md) | Adapted | Design the whole product metrics dashboard SYSTEM: layers, owners, review cadence, and visualization — the board a team actually reviews on a weekly or monthly rhythm |
| [`north-star-metric`](skills/north-star-metric/SKILL.md) | Adapted | Define the North Star Metric spec: the single number, its input metric tree, leading indicators, anti-metrics, and counter-metrics — with a Python tool that renders it… |
| [`risk-assessment`](skills/risk-assessment/SKILL.md) | Adapted | Identify, assess, and mitigate ongoing operational risks — the standing risk register that lives across a program or team |
| [`activation-funnel`](skills/activation-funnel/SKILL.md) | Included | Design and analyze activation funnels (AARRR / AAARRR Pirate Metrics) with conversion + drop-off math, bottleneck detection, and Mermaid funnel diagrams |
| [`change-request`](skills/change-request/SKILL.md) | Included | Create a change management request with impact analysis and rollback plan |
| [`compliance-tracking`](skills/compliance-tracking/SKILL.md) | Included | Track compliance requirements and audit readiness |
| [`meeting-analyzer`](skills/meeting-analyzer/SKILL.md) | Included | Turn meeting notes into an accountable register — extract decisions, actions and open questions, flag ownerless items, track follow-through |
| [`metrics-review`](skills/metrics-review/SKILL.md) | Included | Review and analyze product metrics with trend analysis and actionable insights |
| [`process-doc`](skills/process-doc/SKILL.md) | Included | Document a business process — flowcharts, RACI, and SOPs |
| [`process-optimization`](skills/process-optimization/SKILL.md) | Included | Analyze and improve business processes |
| [`quarterly-planning`](skills/quarterly-planning/SKILL.md) | Included | Run the full quarterly planning cycle -- pre-quarter homework, kickoff, weekly Wodtke rhythm, mid-quarter check-in, and close retro -- using Radical Focus, Cagan… |
| [`runbook`](skills/runbook/SKILL.md) | Included | Create or update an operational runbook for a recurring task or procedure |
| [`team-communications`](skills/team-communications/SKILL.md) | Included | Design a delivery team's communication system — channel routing, meeting-load reduction, status structure, escalation SLAs, timezone norms |
| [`vendor-review`](skills/vendor-review/SKILL.md) | Included | Evaluate a vendor — cost analysis, risk assessment, and recommendation |
<!-- catalog:end -->
