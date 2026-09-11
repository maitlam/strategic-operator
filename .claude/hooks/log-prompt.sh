#!/usr/bin/env bash
# Append each user prompt to a daily session log at .claude/sessions/YYYY-MM-DD.md.
# Reads Claude Code's UserPromptSubmit event JSON from stdin. Session logs are
# gitignored — they're a personal record of what you asked over time.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
sessions_dir="$repo_root/.claude/sessions"
mkdir -p "$sessions_dir"

logfile="$sessions_dir/$(date '+%Y-%m-%d').md"
timestamp="$(date '+%H:%M:%S')"

prompt=$(python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get("prompt", ""))
except Exception:
    print("")
' 2>/dev/null || true)

# Skip if there was no prompt (defensive; UserPromptSubmit always has one).
[ -z "$prompt" ] && exit 0

{
  echo ""
  echo "## $timestamp"
  echo ""
  echo "$prompt"
} >> "$logfile"

exit 0
