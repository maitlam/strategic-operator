#!/usr/bin/env bash
# SessionStart: if a sprint plan exists in this project and today's standup
# prep hasn't been written, print a one-line nudge. Claude sees stdout from
# SessionStart hooks as context, so the nudge reaches the model, not just the
# transcript. Never writes anything.
#
# Paths (relative to the project root, override with env vars):
#   SO_SPRINT_PLAN   default: sprint.md
#   SO_STANDUP_DIR   default: standups
#
# Set SO_STANDUP_NUDGE=off to silence this hook without uninstalling it.

set -euo pipefail

[[ "${SO_STANDUP_NUDGE:-on}" == "off" ]] && exit 0

cwd=$(python3 -c '
import json, sys
try:
    print(json.load(sys.stdin).get("cwd", ""))
except Exception:
    print("")
' 2>/dev/null || true)
[[ -z "$cwd" ]] && cwd="$PWD"

plan="$cwd/${SO_SPRINT_PLAN:-sprint.md}"
standups="$cwd/${SO_STANDUP_DIR:-standups}"
today="$(date '+%Y-%m-%d')"

# No sprint plan → this project isn't running sprints here. Stay quiet.
[[ -f "$plan" ]] || exit 0

# Weekend → stay quiet.
dow="$(date '+%u')"
[[ "$dow" -ge 6 ]] && exit 0

# Today's prep already exists → stay quiet.
if compgen -G "$standups/$today*.md" >/dev/null 2>&1; then
  exit 0
fi

echo "programs: sprint plan found at ${SO_SPRINT_PLAN:-sprint.md} and no standup prep for $today in ${SO_STANDUP_DIR:-standups}/ — run /programs:standup when you're ready."
exit 0
