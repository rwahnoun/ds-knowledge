"""One-shot migration for items #2 (signal-processing rename) and #3 (path flatten).

After running, regenerate indexes via `python meta/build_index.py`.
"""

from __future__ import annotations
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_BASE = ROOT / "biomarkers" / "papers" / "singleBiomarkers"
PAPERS_DIR = ROOT / "biomarkers" / "papers"
NEW_BASE = ROOT / "biomarkers" / "compounds"

EXCL_DIRS = {".obsidian", ".git", ".space", ".claude", "node_modules", "inbox"}


def is_excluded(p: Path) -> bool:
    rel = p.relative_to(ROOT)
    for part in rel.parts:
        if part in EXCL_DIRS or part.startswith("."):
            return True
    return False


def move_tree() -> None:
    NEW_BASE.mkdir(parents=True, exist_ok=True)

    old_sheets = OLD_BASE / "sheets"
    if old_sheets.is_dir():
        for class_dir in sorted(old_sheets.iterdir()):
            if not class_dir.is_dir():
                continue
            target = NEW_BASE / class_dir.name
            print(f"move {class_dir.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
            shutil.move(str(class_dir), str(target))
        # Drop old sheets/index.md if any then remove dir
        for leftover in list(old_sheets.iterdir()):
            leftover.unlink() if leftover.is_file() else shutil.rmtree(leftover)
        old_sheets.rmdir()

    for fname in ("compendium.md", "instructions.md"):
        src = OLD_BASE / fname
        if src.exists():
            print(f"move {src.relative_to(ROOT)} -> {(NEW_BASE / fname).relative_to(ROOT)}")
            shutil.move(str(src), str(NEW_BASE / fname))

    for sub in ("figures", "papers", ".plans"):
        src = OLD_BASE / sub
        if src.exists():
            target = NEW_BASE / sub
            print(f"move {src.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
            shutil.move(str(src), str(target))

    # Drop stale auto-indexes
    for ix in (OLD_BASE / "index.md", PAPERS_DIR / "index.md"):
        if ix.exists():
            print(f"delete stale index: {ix.relative_to(ROOT)}")
            ix.unlink()

    for d in (OLD_BASE, PAPERS_DIR):
        if d.exists() and not any(d.iterdir()):
            print(f"rmdir empty: {d.relative_to(ROOT)}")
            d.rmdir()


def rename_signal_processing() -> None:
    old_sp = ROOT / "biomarkers" / "signal-processing.md"
    new_sp = ROOT / "biomarkers" / "jimini-signal-processing.md"
    if old_sp.exists():
        print(f"rename {old_sp.relative_to(ROOT)} -> {new_sp.relative_to(ROOT)}")
        shutil.move(str(old_sp), str(new_sp))

    if not new_sp.exists():
        return

    # Tighten aliases so they don't collide with sibling note filenames
    text = new_sp.read_text(encoding="utf-8")
    fm_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    m = fm_re.match(text)
    if not m:
        return
    fm = m.group(1)
    # Replace the aliases block
    new_aliases = (
        "aliases:\n"
        "  - jimini signal processing\n"
        "  - jimini DSP pipeline\n"
        "  - urine spectroscopy preprocessing\n"
        "  - matrix correction (Jimini)"
    )
    fm2 = re.sub(
        r"aliases:\s*\n(?:\s+-\s.*\n)+",
        new_aliases + "\n",
        fm,
    )
    if fm2 != fm:
        text2 = text.replace(fm, fm2, 1)
        new_sp.write_text(text2, encoding="utf-8")
        print(f"  cleaned aliases in {new_sp.relative_to(ROOT)}")


# Wikilink rewrites for path-qualified references.
PATH_PATTERNS = [
    (
        re.compile(r"\[\[biomarkers/papers/singleBiomarkers/sheets/([^/\]|#]+)/([^\]|#]+?)((?:\|[^\]]*)?\]\])"),
        r"[[biomarkers/compounds/\1/\2\3",
    ),
    (
        re.compile(r"\[\[biomarkers/papers/singleBiomarkers/sheets/index((?:\|[^\]]*)?\]\])"),
        r"[[biomarkers/compounds/index\1",
    ),
    (
        re.compile(r"\[\[biomarkers/papers/singleBiomarkers/(compendium|instructions)((?:\|[^\]]*)?\]\])"),
        r"[[biomarkers/compounds/\1\2",
    ),
    (
        re.compile(r"\[\[biomarkers/papers/singleBiomarkers/index((?:\|[^\]]*)?\]\])"),
        r"[[biomarkers/compounds/index\1",
    ),
    (
        re.compile(r"\[\[biomarkers/papers/index((?:\|[^\]]*)?\]\])"),
        r"[[biomarkers/compounds/index\1",
    ),
]

SP_RE = re.compile(r"\[\[signal-processing((?:\|[^\]]*)?\]\])")


def rewrite_wikilinks() -> None:
    for md in ROOT.rglob("*.md"):
        if is_excluded(md):
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        new_text = text
        for pat, repl in PATH_PATTERNS:
            new_text = pat.sub(repl, new_text)

        rel = md.relative_to(ROOT).as_posix()
        if rel.startswith("biomarkers/"):
            # Don't rewrite the file's own self-name change (the file itself
            # was renamed but won't reference its old name); rewrite all other
            # [[signal-processing]] wikilinks inside biomarkers/.
            new_text = SP_RE.sub(r"[[jimini-signal-processing\1", new_text)

        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
            print(f"rewrote: {rel}")


def main() -> None:
    print("=== move tree ===")
    move_tree()
    print("\n=== rename signal-processing ===")
    rename_signal_processing()
    print("\n=== rewrite wikilinks ===")
    rewrite_wikilinks()


if __name__ == "__main__":
    main()
