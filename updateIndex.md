# Index Generation

## Vault root

`VAULT_ROOT` = the directory containing this `updateIndex.md` file. All paths below are relative to it. Do not hardcode an absolute path — resolve `VAULT_ROOT` from the location of this file at execution time.

## Purpose

Generate a **hierarchy of `index.md` files**, one per folder, so the vault is navigable both for humans (drill in from the root) and for Obsidian's graph view.

### Why hierarchical (and not one giant root index)

A single root `index.md` that links to every note in the vault is a star graph: every leaf becomes one hop from the same hub, and Obsidian's force layout collapses everything into one clump. The hierarchical pattern keeps each folder's notes one hop from their *local* index, which is itself one hop from its parent index — yielding a tree backbone where folders cluster naturally in the graph view.

## How to regenerate

```bash
python meta/build_index.py
```

That's it. The script:

1. Walks the vault and discovers every folder containing markdown notes (excluding `.obsidian/`, `.git/`, `inbox/`, `node_modules/`, `.claude/`, `.space/`, and any other dotfile dirs).
2. Writes an `index.md` in each such folder, with:
   - YAML frontmatter (`type/index`, `status/living`)
   - A `Parent: [[…]]` link back to the enclosing folder's index (the root index has no parent)
   - A **Subsections** list (wikilinks to child folder indexes, with note counts)
   - A **Notes** list (wikilinks to every `.md` directly in this folder, with title + first-paragraph description)
   - A `Sources` table and a `Gaps` placeholder, matching `meta/tplMarkdown.md`
3. Writes the root `index.md` linking only to the top-level category indexes — not to leaves.

The script is **replace, not merge**: each run overwrites every `index.md` from current filesystem state. There is no curated content in these files; if you want to annotate something, do it in the leaf note's frontmatter `description` (which the index will pick up) — not in the index itself.

## Configuration

All knobs are at the top of `meta/build_index.py`:

- `EXCLUDED_DIRS` — folders never descended into
- `EXCLUDED_ROOT_FILES` — vault-root files not listed in the root index (e.g. `CLAUDE.md`, `AGENTS.md`)
- `INDEX_NAME` — currently `index.md`; one file per folder
- `LEGACY_INDEX_NAMES` — older filenames (e.g. `_index.md`) ignored on scan, not auto-deleted

Edit and re-run; no other state is preserved.

## When to regenerate

After any of:
- Adding, renaming, moving, or deleting a note
- Adding or removing a folder
- Editing a note's frontmatter `title` or `description` (so the index picks it up)

The script is fast (~80 notes, well under a second) — re-run liberally, or wire it into a git pre-commit hook if you want it automatic.

## Frontmatter expectations on leaf notes

The index pulls each entry's title and description from the leaf note. To get a clean index entry, leaf notes should have either:

- `title:` and `description:` keys in YAML frontmatter (preferred), or
- A clean H1 followed by a 1–3 line context paragraph (the script falls back to the first paragraph)

If neither is present, the entry falls back to the filename stem with no description — still functional, just less informative.

## Graph-view tuning (separate from this script)

Once the hierarchical indexes are in place, also tweak Obsidian to make the clusters visually obvious:

1. **Settings → Graph view → Groups** — add color groups by path (`path:biomarkers`, `path:QARA`, `path:datascience`, …) so each folder cluster gets a distinct color.
2. **Forces panel** — increase **Repel force**, decrease **Center force**, increase **Link distance**. This lets weakly-connected subgraphs drift apart instead of being pulled to the center.
3. Optional: install the **Graph Analysis** or **Juggl** plugin for true folder/community-detection clustering if the built-in graph isn't enough.
