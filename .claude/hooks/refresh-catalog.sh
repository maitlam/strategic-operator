#!/usr/bin/env bash
# Auto-refresh scripts/catalog.py READMEs when a plugin file is edited.
# Reads Claude Code's PostToolUse event JSON from stdin; only fires when
# the edited file is a SKILL.md, agents/*.md, or commands/*.md.
#
# Fails silently on missing PyYAML (prints a warning to stderr). To make
# this hook do its job, ensure PyYAML is installed for whichever Python
# resolves as `python3` on your PATH.

set -euo pipefail

# Extract the edited file path from the tool_input JSON. Fall back to "" if
# absent so downstream regex just no-ops.
filepath=$(python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get("tool_input", {}).get("file_path", ""))
except Exception:
    print("")
' 2>/dev/null || true)

# Only refresh if a plugin item was touched. Everything else is out of scope.
if [[ ! "$filepath" =~ plugins/[^/]+/(skills/[^/]+/SKILL\.md|agents/[^/]+\.md|commands/[^/]+\.md)$ ]]; then
  exit 0
fi

# Locate the repo root (this script lives at .claude/hooks/refresh-catalog.sh).
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

# Run catalog.py silently. If it fails (usually missing PyYAML), print a
# non-blocking warning so the maintainer knows to refresh manually.
if ! python3 scripts/catalog.py >/dev/null 2>&1; then
  echo "hook: catalog.py did not run cleanly — run \`python3 scripts/catalog.py\` to refresh READMEs (requires PyYAML)" >&2
fi

exit 0
