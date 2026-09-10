# Product Planning

Turn strategy into product direction — PRDs, product vision, prioritization frameworks, and outcome-driven roadmaps.

Install with `claude plugin install product-planning@strategic-operator`, then call any skill directly as `/product-planning:<skill-name>` or just describe what you need.

Some skills can pull from connected tools like Slack or Jira; see [CONNECTORS.md](CONNECTORS.md). A few of borghei's skills reference [SHARED_OUTPUT_SCHEMA.md](SHARED_OUTPUT_SCHEMA.md) for their Python tools' output formats. Licenses for borrowed work are in [LICENSES/](LICENSES/).

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`prd-quality-gate`](skills/prd-quality-gate/SKILL.md) | Original | Review a draft PRD against a short quality checklist before it goes to a stakeholder — is a decision actually being requested, is success measurable, are assumptions… |
| [`ai-feature-prd`](skills/ai-feature-prd/SKILL.md) | Included | AI/ML feature PRD scaffolding for the modern AI product manager |
| [`create-prd`](skills/create-prd/SKILL.md) | Included | PRD scaffolding expert that generates structured product requirements documents using an 8-section framework, problem framing canvas, and working-backwards press release |
| [`outcome-roadmap`](skills/outcome-roadmap/SKILL.md) | Included | Transform output-based feature lists into outcome-driven Now/Next/Later roadmaps using the "so what?" technique |
| [`prfaq`](skills/prfaq/SKILL.md) | Included | Amazon Working Backwards PR/FAQ generator that forces customer-outcome thinking before any code is written |
| [`pricing-prd`](skills/pricing-prd/SKILL.md) | Included | Tactical PM PRD for pricing experiments and pricing-page launches |
| [`prioritization-frameworks`](skills/prioritization-frameworks/SKILL.md) | Included | Comprehensive prioritization framework expert covering 9 methods with scoring tools and decision guidance for product managers |
| [`product-vision`](skills/product-vision/SKILL.md) | Included | Write the Product Vision document -- the durable 5-10 year narrative above the north-star metric -- using Pichler's Vision Board, Moore's elevator pitch, Raskin's… |
| [`roadmap-communication`](skills/roadmap-communication/SKILL.md) | Included | Same roadmap, three audiences |
| [`roadmap-update`](skills/roadmap-update/SKILL.md) | Included | Update, create, or reprioritize your product roadmap |
<!-- catalog:end -->
