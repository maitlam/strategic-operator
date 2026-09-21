#!/usr/bin/env bash
# PostToolUse (Write|Edit): when the action register changes, recount it and
# rewrite the status block at the top. Deterministic — no model involved.
#
# The register is a markdown table with at least these columns (any order,
# case-insensitive): Owner, Due, Status. Rows whose Status is done/closed/
# complete are counted as closed; everything else is open. Due dates are
# YYYY-MM-DD; anything else is treated as "no date".
#
# The status block lives between <!-- status:start --> and <!-- status:end -->
# and is inserted after the first heading if absent.
#
# Paths (relative to the project root, override with env vars):
#   SO_ACTION_REGISTER   default: actions.md
#
# Set SO_REFRESH_STATUS=off to silence this hook.

set -euo pipefail

[[ "${SO_REFRESH_STATUS:-on}" == "off" ]] && exit 0

read -r cwd filepath < <(python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get("cwd", ""), d.get("tool_input", {}).get("file_path", ""))
except Exception:
    print("", "")
' 2>/dev/null || echo "" "")

[[ -z "$filepath" ]] && exit 0
[[ -z "$cwd" ]] && cwd="$PWD"

register="${SO_ACTION_REGISTER:-actions.md}"
rel="${filepath#"$cwd"/}"
[[ "$rel" == "$register" ]] || exit 0
[[ -f "$filepath" ]] || exit 0

python3 "$(dirname "${BASH_SOURCE[0]}")/refresh_status.py" "$filepath" || {
  echo "bizops hook: could not refresh status block in $register" >&2
}
exit 0
