# Changelog

All notable changes to this repository. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
[Semantic Versioning](https://semver.org/). Every plugin shares the repo
version.

## [0.2.0] — 2026-09-21

Nine plugins, 112 cataloged items — 37 original, 4 adapted, 71 included.

### Added

**Plugins.** Five new plugins alongside the original four: `operating-model`,
`portfolio`, `intelligence`, and `communications` are entirely original;
`discovery`, `positioning`, and `product-planning` were split out of the
former `strategy` plugin.

**Intelligence research loop.** Five skills and one agent that make market
intelligence a standing function rather than a one-off: `signal-scan` (mine
internal notes for signals, count independent sources), `research-agenda`
(rank open questions by the decision each feeds), `research-brief` (scope,
decompose into lenses, fan out, synthesize), `pattern-analysis` (cross-corpus
themes, contradictions, hypothesis ledger), `market-sizing` (bottom-up and
top-down, reconciled, ranges not points), and the `lens-researcher` agent
(one lens per instance, write-as-you-go findings, stuck-detection).

**Communications plugin.** The `deck` skill builds slides from any analysis
using a fixed ten-type slide grammar and an audience profile — `exec`,
`internal`, `external`, `board` — each specifying sequence, cap, tone, and
what to strip and add. Two rendering engines behind one source: Marp
(default, `npx`, fast) and Slidev (self-contained workspace, installed on
first use, richer HTML). The `deck-critic` agent reviews a draft against its
profile — headline test, cover test, four fidelity patterns — and never
rewrites. `lint_deck.py` runs deterministic grammar checks before every
render and in CI. The `/communications:deck` command is the explicit entry
point.

**Ritual commands.** `/programs:standup`, `/programs:sprint-kickoff`,
`/programs:retro`, `/bizops:meeting-prep`, `/discovery:feedback-weekly`.
Each sequences existing skills and carries one opinionated stance.

**Plugin hooks.** The first hooks that ship with a plugin rather than the
repo: `standup-nudge` (programs, `SessionStart`), `note-actions` and
`refresh-status` (bizops, `PostToolUse`), `note-signals` (intelligence,
`PostToolUse`). Extraction hooks ask before writing; `refresh-status` is a
deterministic, idempotent recount. All have `SO_*=off` switches and
env-configurable paths.

**Original agents.** `partner-intelligence`, `market-landscape-analyzer`,
`lens-researcher` (intelligence); `product-discovery-researcher`
(discovery); `operating-model-designer`, `decision-memo` (operating-model);
`portfolio-manager`, `portfolio-prioritizer` (portfolio); `launch-readiness`
(programs); `deck-critic` (communications).

**Repo hooks.** `refresh-catalog.sh` regenerates the catalog on every
plugin-file edit; `log-prompt.sh` keeps a gitignored daily prompt log.

**Runbook.** `docs/runbooks/sync-upstream.md` for the monthly upstream check.

### Changed

- Nine duplicate borrowed skills culled; two persona skills culled; four
  borrowed skills adapted to sharpen their trigger surface
  (`metrics-dashboard`, `north-star-metric`, `risk-assessment`, `pre-mortem`).
- The slide grammar owns every slide-level rule (headline types, number
  provenance and confidence, bullet limits, evidence placement, ask fields,
  caveat placement); audience profiles own only sequence, cap, tone, and
  strip/add. Tightened after a full-chain dogfood in which the critic caught
  three fidelity errors the author introduced.
- `research-brief` gained a lens-researcher launch template.
- README restructured around skills, subagents, automations, and sources;
  documents repo-scoped vs plugin-scoped hooks.
- All GitHub references updated from the previous account name to `maitlam`.

## [0.1.0] — 2026-09-10

Initial release. Three plugins — `bizops`, `strategy`, `programs` — holding
86 skills curated from Anthropic's
[knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)
and Amin Borghei's [Claude-Skills](https://github.com/borghei/Claude-Skills).

### Added

- Provenance system: every item labeled `original`, `adapted`, or `included`
  in frontmatter, with source and license; `catalog.py` generates the READMEs
  from those labels and `--check` fails CI if anything is unlabeled or the
  catalog has drifted.
- `check_upstream.py`: tracks the exact upstream commit each borrowed item
  came from in `sources.json`, detects changes, and three-way-merges them
  while preserving local edits and provenance labels.
- Templates for original and adapted skills; `docs/skill-review.md` curation
  checklist.
- GitHub Action running the catalog check and Claude Code's plugin validator
  on every push.

[0.2.0]: https://github.com/maitlam/strategic-operator/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/maitlam/strategic-operator/releases/tag/v0.1.0
