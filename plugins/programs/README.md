# Programs

Skills for getting cross-functional work over the line: program and portfolio management, launches, dependencies, decision rights, risk, agile delivery, and the tools teams run on.

Install with `claude plugin install programs@strategic-operator`, then call any skill directly as `/programs:<skill-name>` or just describe what you need.

Some skills can pull from connected tools like Slack or Jira; see [CONNECTORS.md](CONNECTORS.md). A few of borghei's skills reference [SHARED_OUTPUT_SCHEMA.md](SHARED_OUTPUT_SCHEMA.md) for their Python tools' output formats. Licenses for borrowed work are in [LICENSES/](LICENSES/).

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`agile-coach`](skills/agile-coach/SKILL.md) | Included | Expert agile coaching: framework selection, maturity assessment, retrospective facilitation, transformation roadmaps |
| [`atlassian-admin`](skills/atlassian-admin/SKILL.md) | Included | Administer the Atlassian suite (Jira/Confluence): user provisioning, groups, SSO/SAML, permissions, security policies, marketplace apps, backups, and org-wide governance |
| [`atlassian-templates`](skills/atlassian-templates/SKILL.md) | Included | Create, modify, and govern reusable Jira and Confluence templates, blueprints, and standardized content structures |
| [`backlog-refinement`](skills/backlog-refinement/SKILL.md) | Included | Backlog refinement playbook covering INVEST quality, vertical story splitting, Definition of Ready, and Definition of Done -- with a Python scorer that grades each story… |
| [`beta-program`](skills/beta-program/SKILL.md) | Included | Closed beta program playbook covering recruitment, success criteria, communication cadence, and beta-to-GA exit gates |
| [`confluence-expert`](skills/confluence-expert/SKILL.md) | Included | Confluence expert for spaces, knowledge bases, documentation, page layouts, macros, templates, and Jira-Confluence integration |
| [`cycle-time-analyzer`](skills/cycle-time-analyzer/SKILL.md) | Included | Flow metrics analyzer (lead time, cycle time, throughput, WIP, aging WIP) for sprint and team health, with cumulative flow diagrams |
| [`daci-framework`](skills/daci-framework/SKILL.md) | Included | DACI decision facilitation framework (Driver, Approver, Contributor, Informed) for clarifying decision ownership, reducing decision thrash, role assignment, and… |
| [`delivery-manager`](skills/delivery-manager/SKILL.md) | Included | Expert delivery management for release planning, deployment strategy, incident response, change management, SLA/error-budget tracking, and DORA metrics across continuous… |
| [`dependency-map`](skills/dependency-map/SKILL.md) | Included | Cross-team dependency tracking with critical path analysis and Mermaid dependency graphs for program coordination |
| [`eol-communication`](skills/eol-communication/SKILL.md) | Included | End-of-life product messaging and sunset communication framework for clear, empathetic EOL announcements that preserve customer trust |
| [`feature-flag-strategy`](skills/feature-flag-strategy/SKILL.md) | Included | PM-facing playbook for phased rollouts with feature flags -- taxonomy (release / experiment / ops / permission), rollout shapes, kill-switch decision tree, holdouts,… |
| [`jira-expert`](skills/jira-expert/SKILL.md) | Included | Jira expert for project setup, workflow design, JQL queries, custom fields, automation rules, dashboards, and reporting |
| [`job-stories`](skills/job-stories/SKILL.md) | Included | Jobs-to-Be-Done story writing that focuses on user situations and motivations rather than personas |
| [`launch-playbook`](skills/launch-playbook/SKILL.md) | Included | Internal and external launch coordination playbook covering pre-launch, launch day, and post-launch with run-of-show, comms, RACI, rollback, and retro |
| [`linear-expert`](skills/linear-expert/SKILL.md) | Included | Linear expert for workspace/team admin, Cycles, Projects, Initiatives, Roadmaps, GraphQL API queries, triage workflows, GitHub integration, bulk operations, and… |
| [`notion-pm`](skills/notion-pm/SKILL.md) | Included | Notion expert for product management workflows |
| [`pm-1on1s`](skills/pm-1on1s/SKILL.md) | Included | Structured PM 1:1 templates by partner type — manager, engineering-manager partner, designer, IC reports, cross-functional — grounded in Radical Candor, the GROW… |
| [`pm-career-ladder`](skills/pm-career-ladder/SKILL.md) | Included | PM career ladder rubrics from APM through VP/CPO across product sense, execution, leadership, strategy, and communication |
| [`pm-interview-prep`](skills/pm-interview-prep/SKILL.md) | Included | Structured PM interview preparation across product sense, execution, strategy, behavioral, and technical rounds, using CIRCLES, AARM, STAR, and the estimation framework |
| [`pm-onboarding`](skills/pm-onboarding/SKILL.md) | Included | 30-60-90 day plan for a new PM joining a company or team, grounded in Michael Watkins' First 90 Days framework and the STARS situational diagnosis |
| [`post-mortem`](skills/post-mortem/SKILL.md) | Included | Blameless post-mortem expert for incidents, outages, regressions, customer escalations, missed launches, and failed experiments |
| [`pre-mortem`](skills/pre-mortem/SKILL.md) | Included | Pre-mortem risk analysis expert that classifies risks as Tigers, Paper Tigers, and Elephants to surface launch-blocking issues before they happen |
| [`productboard-expert`](skills/productboard-expert/SKILL.md) | Included | Productboard expert for workspace setup, Insight-to-Feature triage, Driver scoring, Releases, Roadmap views, and REST API automation |
| [`program-manager`](skills/program-manager/SKILL.md) | Included | Program management for multi-project coordination, portfolio governance, dependency tracking, benefits realization, charters, and steering-committee reporting |
| [`release-notes`](skills/release-notes/SKILL.md) | Included | Structured release notes that translate technical changes (tickets, changelogs, git logs, PRDs) into user-benefit communication |
| [`scrum-master`](skills/scrum-master/SKILL.md) | Included | Data-driven Scrum Master for sprint health scoring, Monte Carlo velocity forecasting, retrospective analysis, capacity planning, and Tuckman team coaching |
| [`senior-pm`](skills/senior-pm/SKILL.md) | Included | Senior PM for enterprise software and SaaS — portfolio management, quantitative risk analysis, prioritization, and executive reporting |
| [`sprint-plan`](skills/sprint-plan/SKILL.md) | Included | Plan a sprint that ships — capacity, commitment vs stretch, dependencies, and risk identification that prevents mid-sprint surprises |
| [`sprint-planning`](skills/sprint-planning/SKILL.md) | Included | Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan |
| [`sprint-retrospective`](skills/sprint-retrospective/SKILL.md) | Included | Data-driven sprint retrospectives from git history — velocity, cycle/lead time, contributor insights, and churn hotspots |
| [`stakeholder-map`](skills/stakeholder-map/SKILL.md) | Included | Map stakeholders by power × interest and design a communication plan that prevents surprise objections |
| [`stakeholder-update`](skills/stakeholder-update/SKILL.md) | Included | Generate a stakeholder update tailored to audience and cadence |
| [`status-update-generator`](skills/status-update-generator/SKILL.md) | Included | Generate weekly executive status updates from Jira/Linear data exports |
| [`story-mapping`](skills/story-mapping/SKILL.md) | Included | Jeff Patton-style user story mapping for visualizing user journeys, MVP definition, release planning, backlog sequencing, and cross-team alignment |
| [`story-splitting`](skills/story-splitting/SKILL.md) | Included | Vertical-slicing playbook with 9 canonical Lawrence patterns for splitting epics into shippable user stories without losing user value |
| [`test-scenarios`](skills/test-scenarios/SKILL.md) | Included | Generate test scenario coverage from a feature spec — happy paths, edge cases, error handling, accessibility, security, and performance — with a coverage analyzer that… |
| [`wwas`](skills/wwas/SKILL.md) | Included | Why-What-Acceptance backlog format that connects every work item to strategic business objectives, with INVEST quality gates and observable acceptance criteria |
<!-- catalog:end -->
