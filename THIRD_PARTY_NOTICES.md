# Third-Party Notices

This repository includes work from the projects below. Each borrowed skill keeps its original license, which is recorded in its frontmatter (`license`) along with its author and a link to the original (`metadata.author`, `metadata.source` or `metadata.adapted-from`). The exact upstream commit for every borrowed file is recorded in `sources.json`.

## Anthropic: knowledge-work-plugins

- Source: https://github.com/anthropics/knowledge-work-plugins
- License: Apache License 2.0 (full text in `plugins/*/LICENSES/Apache-2.0-Anthropic.txt`)
- Used: skills from the `operations` and `product-management` plugins, and the `brainstorm` command.
- Changes made to all included files:
  - Added `license` and provenance `metadata` (provenance, author, source) to the frontmatter. Skill instructions are unchanged.
  - Reorganized skills from the original two plugins into the `bizops`, `strategy`, and `programs` plugins.
  - Combined the two plugins' `CONNECTORS.md` guides into one guide per plugin, and did not include the original `.mcp.json` connector configurations.
- Skills labeled `adapted` contain further changes, described in the `CHANGES.md` inside each skill's folder.

## Amin Borghei (borghei): Claude-Skills

- Source: https://github.com/borghei/Claude-Skills
- License: MIT with the Commons Clause License Condition v1.0 (full text in `plugins/*/LICENSES/MIT-Commons-Clause-borghei.txt`). Under the Commons Clause, the software may not be sold, including as a paid product or service whose value derives substantially from it.
- Used: all 68 skills from `project-management/`, plus `SHARED_OUTPUT_SCHEMA.md`.
- Changes made to all included files:
  - Added provenance `metadata` (provenance, source) to the frontmatter. The original `author`, `license`, and other metadata are kept, and skill instructions are unchanged.
  - Flattened the nested folders (`execution/`, `discovery/`, `career/`, `gtm/`, `strategy-frameworks/`) and reorganized the skills into the `bizops`, `strategy`, and `programs` plugins. Some example files link to sibling skills by their original relative paths; those links may not resolve in this layout.
- Skills labeled `adapted` contain further changes, described in the `CHANGES.md` inside each skill's folder.
