#!/usr/bin/env bash
# Render a deck written in the operator slide grammar.
#
#   render.sh <deck.md> [--engine marp|slidev] [--pdf] [--html] [--pptx] [--all] [-o <dir>]
#
# Defaults: --engine marp, --pdf. Output lands next to the source unless -o is given.
#
# marp   — fast, dependency-light. Uses a global `marp` if installed, otherwise
#          `npx @marp-team/marp-cli` (Node; network on first run). PPTX is
#          image-based: sendable, not editable.
# slidev — richer HTML output, animations, presenter mode. First use runs
#          `npm install` in assets/slidev (Slidev + a headless Chromium; a
#          few minutes and a few hundred MB). Converts the grammar source with
#          to_slidev.py, exports from the workspace, copies the result back.
#          Supports --pdf and --pptx; --html builds a static site into <dir>/<name>-site/.

set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
themes="$here/../assets"
workspace="$here/../assets/slidev"

src=""; outdir=""; engine="marp"; formats=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --engine) engine="$2"; shift 2 ;;
    --pdf|--html|--pptx) formats+=("${1#--}"); shift ;;
    --all) formats+=(pdf html pptx); shift ;;
    -o) outdir="$2"; shift 2 ;;
    -h|--help) sed -n '2,17p' "$0"; exit 0 ;;
    *) src="$1"; shift ;;
  esac
done

[[ -n "$src" && -f "$src" ]] || { echo "render.sh: deck markdown file required" >&2; exit 1; }
[[ ${#formats[@]} -eq 0 ]] && formats=(pdf)
[[ -z "$outdir" ]] && outdir="$(cd "$(dirname "$src")" && pwd)"
mkdir -p "$outdir"
src="$(cd "$(dirname "$src")" && pwd)/$(basename "$src")"
base="$(basename "${src%.*}")"
log="$outdir/.render.log"

# ---- marp ------------------------------------------------------------------
render_marp() {
  if command -v marp >/dev/null 2>&1; then marp_cmd=(marp); else marp_cmd=(npx -y @marp-team/marp-cli@latest); fi
  for f in "${formats[@]}"; do
    out="$outdir/$base.$f"
    # HTML is Marp's default output; `--html` means "allow raw HTML in markdown".
    flag=""; [[ "$f" != "html" ]] && flag="--$f"
    # stdin from /dev/null: marp/npx can block waiting on an open non-TTY stdin.
    if "${marp_cmd[@]}" "$src" --theme-set "$themes" --allow-local-files --html ${flag:+"$flag"} -o "$out" </dev/null >"$log" 2>&1; then
      echo "$out"
    else
      echo "render.sh: marp $f export failed for $src — see $log" >&2; exit 1
    fi
  done
}

# ---- slidev ----------------------------------------------------------------
render_slidev() {
  command -v npm >/dev/null 2>&1 || { echo "render.sh: slidev engine needs Node and npm" >&2; exit 1; }
  if [[ ! -x "$workspace/node_modules/.bin/slidev" ]]; then
    echo "render.sh: first slidev run — installing workspace in $workspace (this takes a few minutes)" >&2
    (cd "$workspace" && npm install --no-audit --no-fund </dev/null >"$log" 2>&1) \
      || { echo "render.sh: npm install failed — see $log" >&2; exit 1; }
  fi
  slides="$workspace/$base.slidev.md"
  python3 "$here/to_slidev.py" "$src" -o "$slides" >/dev/null
  for f in "${formats[@]}"; do
    case "$f" in
      pdf|pptx)
        out="$outdir/$base.$f"
        if (cd "$workspace" && ./node_modules/.bin/slidev export "$(basename "$slides")" --format "$f" --output "$out" </dev/null >"$log" 2>&1); then
          echo "$out"
        else
          echo "render.sh: slidev $f export failed — see $log" >&2; exit 1
        fi ;;
      html)
        site="$outdir/$base-site"
        if (cd "$workspace" && ./node_modules/.bin/slidev build "$(basename "$slides")" --out "$site" </dev/null >"$log" 2>&1); then
          echo "$site/index.html"
        else
          echo "render.sh: slidev html build failed — see $log" >&2; exit 1
        fi ;;
    esac
  done
  rm -f "$slides"
}

case "$engine" in
  marp) render_marp ;;
  slidev) render_slidev ;;
  *) echo "render.sh: unknown engine '$engine' (marp|slidev)" >&2; exit 1 ;;
esac
