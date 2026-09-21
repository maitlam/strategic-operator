# Biz Ops

Skills for running the business day to day: the operating rhythm (quarterly planning, OKRs, metrics reviews), the processes and vendors underneath it, and meetings that end in decisions.

Install with `claude plugin install bizops@strategic-operator`, then call any skill directly as `/bizops:<skill-name>` or just describe what you need.

Some skills can pull from connected tools like Slack or Jira; see [CONNECTORS.md](CONNECTORS.md). A few of borghei's skills reference [SHARED_OUTPUT_SCHEMA.md](SHARED_OUTPUT_SCHEMA.md) for their Python tools' output formats. Licenses for borrowed work are in [LICENSES/](LICENSES/).

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`/meeting-prep`](commands/meeting-prep.md) (command) | Original | Prep for a meeting — its purpose and the decision it needs, open items from last time, who's in the room and what they care about, the questions to ask, and a time-boxed… |
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

## Hooks

Ships two hooks. Both are active for anyone who installs this plugin; silence either with an env var rather than uninstalling.

| Event | Script | What it does | Off switch |
|---|---|---|---|
| `PostToolUse` (Write / Edit) | [`note-actions.sh`](hooks/note-actions.sh) | When a markdown file lands in the notes directory, asks Claude to run `meeting-analyzer` on it and present decisions, actions, and open questions **for your confirmation** before anything is appended to the register. The hook itself extracts and writes nothing. | `SO_NOTE_ACTIONS=off` |
| `PostToolUse` (Write / Edit) | [`refresh-status.sh`](hooks/refresh-status.sh) → [`refresh_status.py`](hooks/refresh_status.py) | When the action register changes, recounts it — open, overdue, due within 7 days, undated, unowned, open-by-owner — and rewrites the status block at the top of the file. Deterministic, no model involved, idempotent. | `SO_REFRESH_STATUS=off` |

Paths, relative to the project root (override with env vars):

| Env var | Default | Meaning |
|---|---|---|
| `SO_NOTES_DIR` | `meetings/` | Where processed meeting notes land |
| `SO_ACTION_REGISTER` | `actions.md` | The action register `meeting-analyzer` appends to |

**Register format.** `refresh-status` finds the first markdown table with `Owner`, `Due`, and `Status` columns (any order). Status values `done`, `closed`, `complete`, `cancelled` count as closed; everything else is open. Due dates are `YYYY-MM-DD`. The status block sits between `<!-- status:start -->` and `<!-- status:end -->` and is inserted after the first heading if missing.
