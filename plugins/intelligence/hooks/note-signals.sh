#!/usr/bin/env bash
# PostToolUse (Write|Edit): when a markdown file lands in the notes directory,
# ask Claude to run signal-scan on it and show candidate signals FOR
# CONFIRMATION before anything is added to the signal log. The hook never
# extracts or writes anything itself.
#
# Paths (relative to the project root, override with env vars):
#   SO_NOTES_DIR    default: meetings
#   SO_SIGNAL_LOG   default: signal-log.md
#
# Set SO_NOTE_SIGNALS=off to silence this hook.

set -euo pipefail

[[ "${SO_NOTE_SIGNALS:-on}" == "off" ]] && exit 0

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
log="${SO_SIGNAL_LOG:-signal-log.md}"
rel="${filepath#"$cwd"/}"

[[ "$rel" == "$notes_dir"/*.md ]] || exit 0
[[ "$rel" == "$log" ]] && exit 0

python3 - "$rel" "$log" <<'PY'
import json, sys
rel, log = sys.argv[1], sys.argv[2]
msg = (
    f"intelligence hook: a note landed at {rel}. Run the signal-scan skill on just this file: "
    f"extract candidate research signals (max five), check each against {log} for duplicates "
    f"and for existing signals now seen from a new independent source, and show the "
    f"candidates to the user. Update {log} only after the user confirms."
)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
PY
exit 0
