#!/usr/bin/env bash
# PostToolUse (Write|Edit): when a markdown file lands in the notes directory,
# ask Claude to run meeting-analyzer on it and present decisions, actions, and
# open questions FOR CONFIRMATION before anything is appended to the register.
# The hook never extracts or writes anything itself.
#
# Paths (relative to the project root, override with env vars):
#   SO_NOTES_DIR         default: meetings
#   SO_ACTION_REGISTER   default: actions.md
#
# Set SO_NOTE_ACTIONS=off to silence this hook.

set -euo pipefail

[[ "${SO_NOTE_ACTIONS:-on}" == "off" ]] && exit 0

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

notes_dir="${SO_NOTES_DIR:-meetings}"
register="${SO_ACTION_REGISTER:-actions.md}"

# Normalize to a path relative to the project root.
rel="${filepath#"$cwd"/}"

# Only markdown files inside the notes directory. Never the register itself.
[[ "$rel" == "$notes_dir"/*.md ]] || exit 0
[[ "$rel" == "$register" ]] && exit 0

python3 - "$rel" "$register" <<'PY'
import json, sys
rel, register = sys.argv[1], sys.argv[2]
msg = (
    f"bizops hook: a note landed at {rel}. Run the meeting-analyzer skill on it and "
    f"present the extracted decisions, action items (owner, due date, status), and open "
    f"questions to the user for confirmation. Do not infer missing owners or dates — flag "
    f"them. Append to {register} only after the user confirms."
)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
PY
exit 0
