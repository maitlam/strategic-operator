#!/usr/bin/env python3
"""Recount an action register and rewrite its status block in place.

Usage: refresh_status.py <register.md>

Finds the first markdown table with Owner, Due, and Status columns; counts
open / overdue / due-this-week / undated items and open items per owner; then
replaces (or inserts) the block between <!-- status:start --> and
<!-- status:end -->. Idempotent: running it twice produces the same file.
"""
import re
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

START, END = "<!-- status:start -->", "<!-- status:end -->"
CLOSED = {"done", "closed", "complete", "completed", "cancelled", "canceled"}


def find_table(lines):
    """Return (header_idx, col_index_map) for the first table with the needed columns."""
    for i, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        cols = [c.strip().lower() for c in line.strip().strip("|").split("|")]
        needed = {"owner", "due", "status"}
        if needed <= set(cols) and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            return i, {c: cols.index(c) for c in needed}
    return None, None


def parse_rows(lines, header_idx, idx):
    rows = []
    for line in lines[header_idx + 2:]:
        if not line.lstrip().startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) <= max(idx.values()):
            continue
        rows.append({k: cells[v] for k, v in idx.items()})
    return rows


def build_block(rows, today):
    open_rows = [r for r in rows if r["status"].lower() not in CLOSED]
    week_end = today + timedelta(days=7)

    def due_of(r):
        m = re.search(r"\d{4}-\d{2}-\d{2}", r["due"])
        return date.fromisoformat(m.group()) if m else None

    overdue = [r for r in open_rows if (d := due_of(r)) and d < today]
    this_week = [r for r in open_rows if (d := due_of(r)) and today <= d <= week_end]
    undated = [r for r in open_rows if due_of(r) is None]
    unowned = [r for r in open_rows if not r["owner"] or r["owner"].lower() in {"tbd", "?", "unassigned"}]
    by_owner = Counter(r["owner"] or "(unassigned)" for r in open_rows)

    out = [START, f"**Status as of {today.isoformat()}** — auto-refreshed by the bizops plugin", ""]
    out.append(f"- Open: **{len(open_rows)}** of {len(rows)} · Overdue: **{len(overdue)}** · Due within 7 days: **{len(this_week)}** · No date: **{len(undated)}** · No owner: **{len(unowned)}**")
    if by_owner:
        out.append("- Open by owner: " + ", ".join(f"{o} ({n})" for o, n in by_owner.most_common()))
    out.append(END)
    return out


def main(path):
    p = Path(path)
    text = p.read_text()
    lines = text.splitlines()
    header_idx, idx = find_table(lines)
    if header_idx is None:
        return 0  # no register table; nothing to do
    block = build_block(parse_rows(lines, header_idx, idx), date.today())

    if START in lines and END in lines:
        s, e = lines.index(START), lines.index(END)
        new_lines = lines[:s] + block + lines[e + 1:]
    else:
        # Insert after the first heading, or at the top.
        insert_at = next((i + 1 for i, l in enumerate(lines) if l.startswith("#")), 0)
        tail = lines[insert_at:]
        if tail and tail[0].strip() == "":
            tail = tail[1:]
        new_lines = lines[:insert_at] + [""] + block + [""] + tail

    new_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    if new_text != text:
        p.write_text(new_text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
