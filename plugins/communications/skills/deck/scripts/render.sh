#!/usr/bin/env bash
# Render a Marp deck with the operator themes (assets/operator*.css).
#
#   render.sh <deck.md> [--pdf] [--html] [--pptx] [--all] [-o <dir>]
#
# Defaults to --pdf. Output lands next to the source unless -o is given.
# Uses a global `marp` if installed, otherwise `npx @marp-team/marp-cli`
# (needs Node and network on first run).
#
# PPTX from Marp is image-based (each slide is a picture) — fine to send,
# not editable. For an editable deck, see the plugin README.

set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
themes="$here/../assets"

src=""; outdir=""; formats=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --pdf|--html|--pptx) formats+=("${1#--}"); shift ;;
    --all) formats+=(pdf html pptx); shift ;;
    -o) outdir="$2"; shift 2 ;;
    -h|--help) sed -n '2,14p' "$0"; exit 0 ;;
    *) src="$1"; shift ;;
  esac
done

[[ -n "$src" && -f "$src" ]] || { echo "render.sh: deck markdown file required" >&2; exit 1; }
[[ ${#formats[@]} -eq 0 ]] && formats=(pdf)
[[ -z "$outdir" ]] && outdir="$(dirname "$src")"
mkdir -p "$outdir"

if command -v marp >/dev/null 2>&1; then
  marp_cmd=(marp)
else
  marp_cmd=(npx -y @marp-team/marp-cli@latest)
fi

base="$(basename "${src%.*}")"
for f in "${formats[@]}"; do
  out="$outdir/$base.$f"
  # HTML is Marp's default output; `--html` means something else (allow raw
  # HTML in markdown), so only pass a converter flag for pdf and pptx.
  flag=""; [[ "$f" != "html" ]] && flag="--$f"
  # stdin from /dev/null: marp/npx can block waiting on an open non-TTY stdin.
  if "${marp_cmd[@]}" "$src" --theme-set "$themes" --allow-local-files --html ${flag:+"$flag"} -o "$out" </dev/null >"$outdir/.render.log" 2>&1; then
    echo "$out"
  else
    echo "render.sh: $f export failed for $src — see $outdir/.render.log" >&2
    exit 1
  fi
done
