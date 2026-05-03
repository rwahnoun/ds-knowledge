#!/usr/bin/env python3
"""Generate hierarchical `index.md` files throughout the Obsidian vault.

For every folder containing markdown notes (recursively), writes an `index.md`
that links back to its parent index and lists its child notes and sub-indexes.
The root `index.md` only links to top-level category indexes -- this avoids
the "star graph" effect that collapses Obsidian's graph view into one clump.

Run from anywhere:

    python meta/build_index.py

Configuration is at the top of this file (excluded folders, root-only files).
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent

# Folders we never descend into (dotfile dirs are also auto-excluded).
EXCLUDED_DIRS = {".obsidian", ".git", ".space", ".claude", "node_modules", "inbox"}

# Vault-root files that aren't part of the curated knowledge base. The root
# index does not list these even though they sit at depth 0.
EXCLUDED_ROOT_FILES = {
    "index.md",
    "updateIndex.md",
    "CLAUDE.md",
    "AGENTS.md",
    "type.md",
    "note.md",
}

INDEX_NAME = "index.md"
# Older convention from before this script existed; ignored when scanning so
# they don't show up as orphan notes, but not auto-deleted.
LEGACY_INDEX_NAMES = {"_index.md"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "-")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1) if FRONTMATTER_RE.match(text) else text


def first_h1(text: str) -> str | None:
    for line in strip_frontmatter(text).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def first_para_after_h1(text: str) -> str | None:
    body = strip_frontmatter(text).splitlines()
    started = False
    para: list[str] = []
    for line in body:
        if line.startswith("# ") and not started:
            started = True
            continue
        if not started:
            continue
        if not line.strip():
            if para:
                break
            continue
        if line.startswith(("#", "|", "-", "*", ">", "`")):
            if para:
                break
            continue
        para.append(line.strip())
    if not para:
        return None
    s = " ".join(para)
    return s[:120].rstrip() + ("…" if len(s) > 120 else "")


def get_meta(md_path: Path) -> tuple[str, str]:
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return md_path.stem, ""
    fm = parse_frontmatter(text)
    title = fm.get("title") or first_h1(text) or md_path.stem
    desc = fm.get("description") or first_para_after_h1(text) or ""
    return title, desc


def is_excluded_relpath(p: Path) -> bool:
    for part in p.parts:
        if part == ".":
            continue
        if part in EXCLUDED_DIRS or part.startswith("."):
            return True
    return False


def collect_folders(root: Path) -> list[Path]:
    """Every folder under root that contains at least one indexable .md file."""
    folders: set[Path] = set()
    for md in root.rglob("*.md"):
        rel = md.relative_to(root)
        if is_excluded_relpath(rel.parent):
            continue
        if md.name in LEGACY_INDEX_NAMES or md.name == INDEX_NAME:
            continue
        if rel.parent == Path(".") and md.name in EXCLUDED_ROOT_FILES:
            continue
        f = rel.parent
        while True:
            folders.add(f)
            if f == Path("."):
                break
            f = f.parent
    return sorted(folders, key=lambda p: (len(p.parts), str(p)))


def list_md_in_folder(folder: Path) -> list[Path]:
    abs_folder = VAULT_ROOT if folder == Path(".") else VAULT_ROOT / folder
    out: list[Path] = []
    for p in abs_folder.iterdir():
        if not p.is_file() or p.suffix != ".md":
            continue
        if p.name in LEGACY_INDEX_NAMES or p.name == INDEX_NAME:
            continue
        if folder == Path(".") and p.name in EXCLUDED_ROOT_FILES:
            continue
        out.append(p.relative_to(VAULT_ROOT))
    return sorted(out)


def list_subfolders(folder: Path, known: set[Path]) -> list[Path]:
    abs_folder = VAULT_ROOT if folder == Path(".") else VAULT_ROOT / folder
    out: list[Path] = []
    for p in abs_folder.iterdir():
        if not p.is_dir():
            continue
        rel = p.relative_to(VAULT_ROOT)
        if is_excluded_relpath(rel):
            continue
        if rel in known:
            out.append(rel)
    return sorted(out)


def count_notes(folder: Path) -> int:
    abs_folder = VAULT_ROOT if folder == Path(".") else VAULT_ROOT / folder
    n = 0
    for md in abs_folder.rglob("*.md"):
        rel = md.relative_to(VAULT_ROOT)
        if is_excluded_relpath(rel.parent):
            continue
        if md.name in LEGACY_INDEX_NAMES or md.name == INDEX_NAME:
            continue
        if rel.parent == Path(".") and md.name in EXCLUDED_ROOT_FILES:
            continue
        n += 1
    return n


def wikilink(target_rel: Path, display: str | None = None) -> str:
    target = str(target_rel.with_suffix("")).replace("\\", "/")
    if display and display != target_rel.stem:
        return f"[[{target}|{display}]]"
    return f"[[{target}]]"


def render_index(folder: Path, known: set[Path]) -> str:
    is_root = folder == Path(".")
    files = list_md_in_folder(folder)
    subs = list_subfolders(folder, known)
    title = "Vault Index" if is_root else f"{folder.name} — index"

    lines: list[str] = []
    lines += [
        "---",
        f"title: {title}",
        "aliases: []",
        "tags: [type/index, status/living]",
        f"date: {date.today().isoformat()}",
        "status: living",
        "type: index",
        "author: claude",
        "BC-list-note-field: down",
        "---",
        "",
        f"# {title}",
        "",
    ]

    if is_root:
        lines += [
            "Navigation hub for this vault. Each section below is its own MOC; "
            "follow the link to drill in. Cross-folder structure is intentional "
            "— the root only links to top-level indexes so Obsidian's graph "
            "view clusters by folder instead of collapsing into one hub.",
            "",
            "Auto-generated by `meta/build_index.py` — see `updateIndex.md`.",
            "",
        ]
    else:
        parent = folder.parent
        parent_target = INDEX_NAME if parent == Path(".") else f"{parent.as_posix()}/{INDEX_NAME}"
        parent_display = "Vault Index" if parent == Path(".") else parent.name
        lines += [
            f"Parent: {wikilink(Path(parent_target), parent_display)}",
            "",
            f"Auto-generated map of `{folder.as_posix()}/`. "
            "Regenerate with `python meta/build_index.py`.",
            "",
        ]

    if subs:
        lines += ["## Subsections", ""]
        for s in subs:
            sub_index = s / INDEX_NAME
            n = count_notes(s)
            lines.append(
                f"- {wikilink(sub_index, s.name)} — {n} note{'s' if n != 1 else ''}"
            )
        lines.append("")

    if files:
        lines += ["## Notes", ""]
        for f in files:
            ftitle, fdesc = get_meta(VAULT_ROOT / f)
            entry = f"- {wikilink(f, ftitle)}"
            if fdesc:
                entry += f" — {fdesc}"
            lines.append(entry)
        lines.append("")

    lines += [
        "## Sources",
        "| Source | Note |",
        "|---|---|",
        "| Filesystem scan | Auto-generated by `meta/build_index.py` |",
        "",
        "## Gaps",
        "- (auto-generated; structural only — no curated gaps)",
        "",
    ]

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    folders = collect_folders(VAULT_ROOT)
    folder_set = set(folders)
    written = 0
    for folder in folders:
        target = VAULT_ROOT / INDEX_NAME if folder == Path(".") else VAULT_ROOT / folder / INDEX_NAME
        target.write_text(render_index(folder, folder_set), encoding="utf-8")
        written += 1
        print(f"wrote: {target.relative_to(VAULT_ROOT)}")
    print(f"\nTotal: {written} index files")


if __name__ == "__main__":
    main()
