## Runbook: Sync borrowed skills with upstream

**Owner:** Mai Lam (maitlam) | **Frequency:** Monthly, or before any release
**Last Updated:** 2026-09-10 | **Last Run:** 2026-09-10

### Purpose

Every `included` and `adapted` skill in this repo was copied from Anthropic's
knowledge-work-plugins or borghei's Claude-Skills. Nothing here is a fork, so
upstream fixes never arrive on their own. This runbook pulls their changes in
without losing local edits or provenance labels.

Run it when you want upstream bug fixes, before tagging a release, or when
someone reports that a skill behaves differently than its upstream original.

Do **not** use this to add a *new* skill from upstream — that's
`check_upstream.py --add`, a different procedure.

### Prerequisites

- [ ] Python 3.8+ and git on PATH
- [ ] PyYAML installed (`python3 -m pip install pyyaml`) — `--merge` and `--add` fail without it
- [ ] Network access to github.com (the script clones upstream history on first run)
- [ ] A clean working tree (`git status --short` prints nothing) so the merge diff is readable
- [ ] Run every command from the repo root, `~/github/strategic-operator`

### Procedure

#### Step 1: Confirm a clean starting point

```
cd ~/github/strategic-operator
git status --short
```

**Expected result:** No output. `.cache/` and `.upstream-patches/` are gitignored and
will not appear even after the script runs.
**If it fails:** Commit or stash the pending work first. Merging on top of unrelated
edits makes it impossible to tell your changes from upstream's in the review at Step 5.

#### Step 2: Ask what changed upstream

```
python3 scripts/check_upstream.py
```

**Expected result:** Either `All 89 items you copied match upstream's latest. Nothing to do.`
— stop here, you're done — or a list of changed items. The first run prints
`Downloading history for 'anthropic' (first run only)...` and takes a few minutes;
later runs are fast. The count is 89, not the catalog's 86, because `sources.json`
also tracks non-skill files like `SHARED_OUTPUT_SCHEMA.md`.
**If it fails:** `ModuleNotFoundError: No module named 'yaml'` → install PyYAML.
Network or clone errors → retry; the script re-uses `.cache/` and won't re-download.

#### Step 3: Read the actual diff before merging anything

```
python3 scripts/check_upstream.py --diff pre-mortem
```

**Expected result:** The upstream diff for that one item, between the commit recorded
in `sources.json` and upstream's HEAD. Read it. Upstream sometimes changes things you
deliberately reshaped, and a merge is harder to unpick than a decision not to merge.
**If it fails:** `unknown item` → name it by skill name (`pre-mortem`), `plugin/name`
(`bizops/SHARED_OUTPUT_SCHEMA.md`), or full path.

#### Step 4: Merge

```
python3 scripts/check_upstream.py --merge pre-mortem
```

Use `--merge all` only when Step 3 showed you every diff and you accepted all of them.

**Expected result:** A three-way merge — upstream's old version, upstream's new version,
your copy — so your edits and `metadata.provenance` labels survive.
**If it fails:** Conflicting edits to the same lines produce standard `<<<<<<<` markers
in the file, and the item is deliberately **not** marked synced. Resolve the markers by
hand, keeping your frontmatter `metadata` block, then run
`python3 scripts/check_upstream.py --mark-synced pre-mortem`.

#### Step 5: Review every changed file

```
git diff
```

**Expected result:** Only the merged content changes, plus updated commit SHAs in
`sources.json`. Frontmatter `license`, `metadata.provenance`, `metadata.author`, and
`metadata.source` must be unchanged — those are the repo's licensing record, not
upstream's to overwrite.
**If it fails:** A dropped provenance block will be caught in Step 6, but it's faster
to restore it here from `git diff` than to debug the CI failure.

#### Step 6: Rebuild the catalog and run the same checks CI runs

```
python3 scripts/catalog.py
python3 scripts/catalog.py --check
claude plugin validate .
```

**Expected result:** `✓ 86 items checked: ... READMEs are up to date.` and
`✔ Validation passed`. Run `catalog.py` first — `--check` compares the READMEs against
the files and fails if you skipped the rebuild.
**If it fails:** `unlabeled item` → a merge dropped a `metadata.provenance` line; restore it.
`README out of date` → you ran `--check` without rebuilding.

#### Step 7: Commit

```
git add -A
git commit -m "Sync <item> with upstream <short-sha>"
git push
```

**Expected result:** The `Validate` workflow runs on the push and goes green in ~20s.
**If it fails:** See Troubleshooting.

### Verification

- [ ] `python3 scripts/check_upstream.py` reports nothing left to do for the items you merged
- [ ] `python3 scripts/catalog.py --check` exits 0
- [ ] `git diff HEAD~1 -- sources.json` shows the commit SHAs advanced for exactly the merged items
- [ ] `gh run list --limit 1` shows `completed success`
- [ ] No `<<<<<<<` markers survive: `grep -rn '<<<<<<<' plugins/` returns nothing

### Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `ModuleNotFoundError: No module named 'yaml'` | PyYAML missing from the interpreter on PATH | `python3 -m pip install pyyaml` |
| `Downloading history...` hangs past ~10 min | Slow clone of full upstream history | Let it finish once; `.cache/` makes later runs fast. Don't delete `.cache/` to "reset" |
| CI fails on `catalog.py --check` but it passes locally | Rebuilt READMEs never got committed | `git add -A && git commit --amend --no-edit && git push --force-with-lease` |
| Item shows as changed again right after merging | Conflict markers left it unsynced | Resolve markers, then `--mark-synced <item>` |
| `command not found: timeout` | macOS has no GNU `timeout` | Drop it, or `brew install coreutils` and use `gtimeout` |
| Merge rewrote a skill you adapted | `--merge all` run without reading diffs | `git checkout -- <path>` and merge that item individually after reading its diff |

### Rollback

Nothing is pushed until Step 7, so before that:

```
git checkout -- .        # discard merged content and sources.json changes
```

After pushing, revert the commit rather than force-pushing over it, so the
`sources.json` history stays honest about what was synced when:

```
git revert <sha>
python3 scripts/catalog.py
git add -A && git commit --amend --no-edit && git push
```

### Escalation

| Situation | Contact | Method |
|-----------|---------|--------|
| Upstream changed a skill's license or removed it | Repo owner (maitlam) | Decide whether to keep the copy under the old license or drop it; update `THIRD_PARTY_NOTICES.md` either way |
| Upstream skill looks wrong or broken | Anthropic / borghei | Issue on the upstream repo linked in the skill's `metadata.source` |
| `sources.json` and the files disagree and won't reconcile | Repo owner (maitlam) | Re-derive the entry with `--add` against the current upstream path, then re-apply local edits |

### History

| Date | Run By | Notes |
|------|--------|-------|
| 2026-09-10 | maitlam | First run after repo creation. All 89 tracked items matched upstream; nothing to merge. First-run history download took a few minutes |
