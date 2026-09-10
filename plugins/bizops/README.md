# Biz Ops

Skills for running the business day to day: the operating rhythm (quarterly planning, OKRs, metrics reviews), the processes and vendors underneath it, and meetings that end in decisions.

Install with `claude plugin install bizops@strategic-operator`, then call any skill directly as `/bizops:<skill-name>` or just describe what you need.

Some skills can pull from connected tools like Slack or Jira; see [CONNECTORS.md](CONNECTORS.md). A few of borghei's skills reference [SHARED_OUTPUT_SCHEMA.md](SHARED_OUTPUT_SCHEMA.md) for their Python tools' output formats. Licenses for borrowed work are in [LICENSES/](LICENSES/).

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`activation-funnel`](skills/activation-funnel/SKILL.md) | Included | Design and analyze activation funnels (AARRR / AAARRR Pirate Metrics) with conversion + drop-off math, bottleneck detection, and Mermaid funnel diagrams |
| [`brainstorm-okrs`](skills/brainstorm-okrs/SKILL.md) | Included | OKR brainstorming and validation using the Radical Focus framework — outcome objectives, measurable key results, counter-metrics |
| [`capacity-plan`](skills/capacity-plan/SKILL.md) | Included | Plan resource capacity — workload analysis and utilization forecasting |
| [`change-request`](skills/change-request/SKILL.md) | Included | Create a change management request with impact analysis and rollback plan |
| [`compliance-tracking`](skills/compliance-tracking/SKILL.md) | Included | Track compliance requirements and audit readiness |
| [`meeting-analyzer`](skills/meeting-analyzer/SKILL.md) | Included | Turn meeting notes into an accountable register — extract decisions, actions and open questions, flag ownerless items, track follow-through |
| [`metrics-dashboard`](skills/metrics-dashboard/SKILL.md) | Included | Design a product metrics dashboard — North Star, input metrics, and guardrails — that a team actually uses to make decisions |
| [`metrics-review`](skills/metrics-review/SKILL.md) | Included | Review and analyze product metrics with trend analysis and actionable insights |
| [`north-star-metric`](skills/north-star-metric/SKILL.md) | Included | Define a North Star Metric (NSM) and its input metric tree, with leading indicators, anti-metrics, and counter-metrics |
| [`process-doc`](skills/process-doc/SKILL.md) | Included | Document a business process — flowcharts, RACI, and SOPs |
| [`process-optimization`](skills/process-optimization/SKILL.md) | Included | Analyze and improve business processes |
| [`quarterly-planning`](skills/quarterly-planning/SKILL.md) | Included | Run the full quarterly planning cycle -- pre-quarter homework, kickoff, weekly Wodtke rhythm, mid-quarter check-in, and close retro -- using Radical Focus, Cagan… |
| [`risk-assessment`](skills/risk-assessment/SKILL.md) | Included | Identify, assess, and mitigate operational risks |
| [`runbook`](skills/runbook/SKILL.md) | Included | Create or update an operational runbook for a recurring task or procedure |
| [`status-report`](skills/status-report/SKILL.md) | Included | Generate a status report with KPIs, risks, and action items |
| [`summarize-meeting`](skills/summarize-meeting/SKILL.md) | Included | Structured meeting summarization that captures decisions, action items, and open questions in a consistent format |
| [`team-communications`](skills/team-communications/SKILL.md) | Included | Design a delivery team's communication system — channel routing, meeting-load reduction, status structure, escalation SLAs, timezone norms |
| [`vendor-review`](skills/vendor-review/SKILL.md) | Included | Evaluate a vendor — cost analysis, risk assessment, and recommendation |
<!-- catalog:end -->
