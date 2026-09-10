# Discovery

Continuous customer discovery — interview design, transcript synthesis, JTBD workshops, opportunity ideation, and the disciplines that keep discovery signal over noise.

Install with `claude plugin install discovery@strategic-operator`, then call any skill directly as `/discovery:<skill-name>` or just describe what you need.

Some skills can pull from connected tools like Slack or Jira; see [CONNECTORS.md](CONNECTORS.md). A few of borghei's skills reference [SHARED_OUTPUT_SCHEMA.md](SHARED_OUTPUT_SCHEMA.md) for their Python tools' output formats. Licenses for borrowed work are in [LICENSES/](LICENSES/).

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`product-discovery-researcher`](agents/product-discovery-researcher.md) (agent) | Original | Run customer discovery workflows — plan interview scripts, run interviews, synthesize transcripts, facilitate JTBD workshops, and ideate opportunities from evidence |
| [`brainstorm-experiments`](skills/brainstorm-experiments/SKILL.md) | Included | Experiment design expert using pretotyping and lean validation for both new product concepts and existing product features |
| [`brainstorm-ideas`](skills/brainstorm-ideas/SKILL.md) | Included | Product ideation expert using Product Trio approach and Opportunity Solution Trees for both new and existing products |
| [`customer-feedback-triage`](skills/customer-feedback-triage/SKILL.md) | Included | Inbound customer-feedback triage system |
| [`customer-interview-script`](skills/customer-interview-script/SKILL.md) | Included | Run high-signal customer discovery interviews using a scripted question hierarchy, behavior-over-opinion probes, and rapport techniques drawn from Portigal, Torres,… |
| [`identify-assumptions`](skills/identify-assumptions/SKILL.md) | Included | Assumption mapping expert that identifies, categorizes, and prioritizes product assumptions across 4-8 risk categories using devil's advocate analysis |
| [`interview-synthesis`](skills/interview-synthesis/SKILL.md) | Included | Customer interview synthesis: raw transcripts to themed insights, an opportunity solution tree, and follow-up questions (Teresa Torres continuous discovery) |
| [`jtbd-workshop`](skills/jtbd-workshop/SKILL.md) | Included | Run a full Jobs-To-Be-Done discovery workshop with switch interviews, forces-of-progress mapping, ODI outcome scoring, and opportunity statements across 2hr, 4hr, and… |
| [`opportunity-solution-tree`](skills/opportunity-solution-tree/SKILL.md) | Included | Opportunity Solution Tree (Teresa Torres) mapping outcomes → opportunities → solutions → assumption tests |
| [`synthesize-research`](skills/synthesize-research/SKILL.md) | Included | Synthesize user research from interviews, surveys, and feedback into structured insights |
| [`/brainstorm`](commands/brainstorm.md) (command) | Included | Brainstorm a product idea, problem space, or strategic question with a sharp thinking partner |
<!-- catalog:end -->
