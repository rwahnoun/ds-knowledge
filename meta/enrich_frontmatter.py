"""Item #7: enrich every compound sheet's YAML frontmatter with multi-axis
ontology fields and tags.

Adds these top-level frontmatter keys:
    class:               chemical class (single string)
    subclass:            finer classification (optional)
    clinical-use:        list of clinical contexts (e.g. uti, kidney-function)
    detection-modality:  list of measurement modalities (uv, nir, fluorescence, eis, scattering)
    presence:            normal | trace | trace-or-abnormal | abnormal
    parent:              Breadcrumbs-style typed link to the class index

Augments existing tags with new namespaces:
    class/<class>, clinical/<use>, modality/<m>, presence/<state>

The classification table below is canonical -- edit it to update vault metadata
in one place, then re-run this script.
"""

from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPOUNDS_DIR = ROOT / "biomarkers" / "compounds"

# Canonical ontology table. Keys are the file stems under
# biomarkers/compounds/<class-folder>/<stem>.md
ONTOLOGY: dict[str, dict] = {
    # contaminants/
    "chlorotalonil": dict(
        cls="contaminant", subclass="organochlorine-fungicide",
        clinical=["contamination", "toxicology"],
        modality=["uv", "fluorescence", "eis"],
        presence="abnormal",
    ),
    "metolachlore": dict(
        cls="contaminant", subclass="chloroacetamide-herbicide",
        clinical=["contamination", "toxicology"],
        modality=["uv", "eis"],
        presence="abnormal",
    ),
    "pfas": dict(
        cls="contaminant", subclass="perfluorinated",
        clinical=["contamination", "environmental-exposure"],
        modality=["fluorescence", "eis"],
        presence="abnormal",
    ),
    # fluorophores/
    "fad": dict(
        cls="metabolite", subclass="flavin-coenzyme",
        clinical=["oncology", "metabolism"],
        modality=["fluorescence", "uv", "vis"],
        presence="trace",
    ),
    "nadh": dict(
        cls="metabolite", subclass="pyridine-coenzyme",
        clinical=["oncology", "metabolism"],
        modality=["fluorescence", "uv"],
        presence="trace",
    ),
    "riboflavin": dict(
        cls="vitamin", subclass="vitamin-b2",
        clinical=["nutrition"],
        modality=["fluorescence", "uv", "vis"],
        presence="trace",
    ),
    "tryptophan": dict(
        cls="amino-acid", subclass="aromatic",
        clinical=["oncology", "nutrition"],
        modality=["fluorescence", "uv"],
        presence="trace",
    ),
    # infection-inflammation/
    "bacteria": dict(
        cls="cellular", subclass="microorganism",
        clinical=["uti"],
        modality=["scattering", "eis", "fluorescence"],
        presence="abnormal",
    ),
    "haemoglobin": dict(
        cls="protein", subclass="heme-protein",
        clinical=["hematuria", "renal-injury"],
        modality=["uv", "vis"],
        presence="abnormal",
    ),
    "leukocytes": dict(
        cls="cellular", subclass="immune-cell",
        clinical=["uti", "inflammation"],
        modality=["scattering", "fluorescence", "eis"],
        presence="trace-or-abnormal",
    ),
    "nitrites": dict(
        cls="small-molecule", subclass="anion",
        clinical=["uti"],
        modality=["uv", "vis", "eis"],
        presence="abnormal",
    ),
    "red-blood-cells": dict(
        cls="cellular", subclass="erythrocyte",
        clinical=["hematuria"],
        modality=["scattering", "vis"],
        presence="abnormal",
    ),
    "white-blood-cells": dict(
        cls="cellular", subclass="leukocyte",
        clinical=["uti", "inflammation"],
        modality=["scattering", "fluorescence", "eis"],
        presence="trace-or-abnormal",
    ),
    # metabolites/
    "chloride": dict(
        cls="electrolyte", subclass="anion",
        clinical=["electrolyte-balance", "kidney-function"],
        modality=["nir", "eis"],
        presence="normal",
    ),
    "citrate": dict(
        cls="metabolite", subclass="organic-acid",
        clinical=["nephrolithiasis", "kidney-function"],
        modality=["uv", "ftir", "eis"],
        presence="normal",
    ),
    "copper": dict(
        cls="trace-element", subclass="transition-metal",
        clinical=["wilsons-disease", "trace-mineral"],
        modality=["uv", "vis", "eis"],
        presence="trace",
    ),
    "creatinin": dict(
        cls="metabolite", subclass="nitrogenous-waste",
        clinical=["kidney-function", "normalization-reference"],
        modality=["uv", "nir"],
        presence="normal",
    ),
    "glucose": dict(
        cls="metabolite", subclass="monosaccharide",
        clinical=["diabetes", "glycosuria"],
        modality=["nir", "eis", "raman"],
        presence="trace-or-abnormal",
    ),
    "magnesium": dict(
        cls="electrolyte", subclass="cation",
        clinical=["electrolyte-balance"],
        modality=["eis", "uv"],
        presence="normal",
    ),
    "oxalate": dict(
        cls="metabolite", subclass="organic-acid",
        clinical=["nephrolithiasis"],
        modality=["uv", "eis"],
        presence="normal",
    ),
    "phosphate": dict(
        cls="electrolyte", subclass="anion",
        clinical=["electrolyte-balance", "bone-metabolism"],
        modality=["uv", "vis", "eis"],
        presence="normal",
    ),
    "sodium": dict(
        cls="electrolyte", subclass="cation",
        clinical=["electrolyte-balance", "hydration"],
        modality=["nir", "eis"],
        presence="normal",
    ),
    "urea": dict(
        cls="metabolite", subclass="nitrogenous-waste",
        clinical=["kidney-function", "nitrogen-balance", "normalization-reference"],
        modality=["nir", "raman"],
        presence="normal",
    ),
    "uric-acid": dict(
        cls="metabolite", subclass="purine-end-product",
        clinical=["gout", "nephrolithiasis", "tumor-lysis"],
        modality=["uv"],
        presence="normal",
    ),
    # physico-chemical/
    "ketone": dict(
        cls="metabolite", subclass="ketone-body",
        clinical=["diabetes", "ketosis"],
        modality=["uv", "eis"],
        presence="trace-or-abnormal",
    ),
    "osmolality": dict(
        cls="physico-chemical", subclass="concentration-property",
        clinical=["hydration", "kidney-function"],
        modality=["nir"],
        presence="normal",
    ),
    "ph": dict(
        cls="physico-chemical", subclass="acid-base",
        clinical=["acid-base-balance", "nephrolithiasis-risk"],
        modality=["vis", "eis"],
        presence="normal",
    ),
    "usg": dict(
        cls="physico-chemical", subclass="concentration-property",
        clinical=["hydration"],
        modality=["nir", "refractometry"],
        presence="normal",
    ),
    # pigments-porphyrins/
    "bilirubin": dict(
        cls="pigment", subclass="tetrapyrrole",
        clinical=["liver", "hepatobiliary"],
        modality=["vis", "uv"],
        presence="abnormal",
    ),
    "porphobilinogen": dict(
        cls="pigment", subclass="porphyrin-precursor",
        clinical=["porphyria"],
        modality=["uv", "vis"],
        presence="trace-or-abnormal",
    ),
    "total-urinary-porphyrin": dict(
        cls="pigment", subclass="porphyrin",
        clinical=["porphyria", "lead-toxicity"],
        modality=["fluorescence", "uv", "vis"],
        presence="trace-or-abnormal",
    ),
}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter_lines(fm_text: str) -> list[str]:
    """Return frontmatter lines (without surrounding ---)."""
    return fm_text.splitlines()


def has_top_key(lines: list[str], key: str) -> bool:
    return any(re.match(rf"^{re.escape(key)}\s*:", line) for line in lines)


def find_block(lines: list[str], key: str) -> tuple[int, int] | None:
    """Find a YAML block-style key. Returns (start, end_exclusive) of the
    key-line plus its indented children, or None if not found.
    """
    for i, line in enumerate(lines):
        m = re.match(rf"^{re.escape(key)}\s*:(.*)$", line)
        if m:
            j = i + 1
            while j < len(lines) and re.match(r"^\s+(-|\w)", lines[j]):
                j += 1
            return (i, j)
    return None


def render_list_block(key: str, items: list[str]) -> list[str]:
    return [f"{key}:"] + [f"  - {it}" for it in items]


def merge_tags(existing_block: list[str], new_tags: list[str]) -> list[str]:
    """Given existing tag block lines (the 'tags:' header + indented '  - ...'),
    return the merged block as new lines, deduplicated, preserving order.
    """
    if existing_block:
        head = existing_block[0]
        items = []
        for line in existing_block[1:]:
            m = re.match(r"^\s+-\s+(.+)\s*$", line)
            if m:
                items.append(m.group(1).strip())
        for nt in new_tags:
            if nt not in items:
                items.append(nt)
        return [head] + [f"  - {it}" for it in items]
    return render_list_block("tags", new_tags)


def class_folder(stem: str) -> str | None:
    for cf in sorted(COMPOUNDS_DIR.iterdir()):
        if not cf.is_dir():
            continue
        if cf.name.startswith("."):
            continue
        if (cf / f"{stem}.md").exists():
            return cf.name
    return None


def enrich_file(md: Path, stem: str) -> bool:
    text = md.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        print(f"  skip (no frontmatter): {md.relative_to(ROOT)}")
        return False
    fm_text = m.group(1)
    lines = parse_frontmatter_lines(fm_text)

    onto = ONTOLOGY[stem]
    cf = class_folder(stem)
    if cf is None:
        print(f"  skip (no class folder): {md.relative_to(ROOT)}")
        return False

    parent_link = f"[[biomarkers/compounds/{cf}/index|{cf}]]"

    # Build / update keys
    updates = {
        "class": onto["cls"],
        "subclass": onto.get("subclass", ""),
        "presence": onto["presence"],
        "parent": parent_link,
    }

    new_tags = (
        [f"class/{onto['cls']}"]
        + [f"clinical/{c}" for c in onto["clinical"]]
        + [f"modality/{m}" for m in onto["modality"]]
        + [f"presence/{onto['presence']}"]
    )
    if onto.get("subclass"):
        new_tags.append(f"subclass/{onto['subclass']}")

    # Replace or insert top-level keys
    out = list(lines)

    # Replace tags block
    tag_block = find_block(out, "tags")
    if tag_block:
        existing = out[tag_block[0]:tag_block[1]]
        merged = merge_tags(existing, new_tags)
        out[tag_block[0]:tag_block[1]] = merged
    else:
        out += render_list_block("tags", new_tags)

    # Replace clinical-use list block
    cu_block = find_block(out, "clinical-use")
    cu_lines = render_list_block("clinical-use", onto["clinical"])
    if cu_block:
        out[cu_block[0]:cu_block[1]] = cu_lines
    else:
        out += cu_lines

    # Replace detection-modality list block
    dm_block = find_block(out, "detection-modality")
    dm_lines = render_list_block("detection-modality", onto["modality"])
    if dm_block:
        out[dm_block[0]:dm_block[1]] = dm_lines
    else:
        out += dm_lines

    # Scalar updates: class, subclass, presence, parent
    for k, v in updates.items():
        if not v:
            continue
        existing_idx = None
        for i, line in enumerate(out):
            if re.match(rf"^{re.escape(k)}\s*:", line):
                existing_idx = i
                break
        rendered = f"{k}: {v}" if k != "parent" else f'{k}: "{v}"'
        if existing_idx is not None:
            out[existing_idx] = rendered
        else:
            out.append(rendered)

    new_fm = "\n".join(out)
    if new_fm == fm_text:
        return False
    new_text = "---\n" + new_fm + "\n---\n" + text[m.end():]
    md.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    if not COMPOUNDS_DIR.is_dir():
        raise SystemExit(f"Missing {COMPOUNDS_DIR} -- run migrate_2_3.py first")
    written = 0
    missing = []
    for stem in sorted(ONTOLOGY):
        cf = class_folder(stem)
        if cf is None:
            missing.append(stem)
            continue
        md = COMPOUNDS_DIR / cf / f"{stem}.md"
        if enrich_file(md, stem):
            written += 1
            print(f"enriched: {md.relative_to(ROOT)}")
    if missing:
        print(f"\nWARNING: no file found for {len(missing)} stems: {missing}")
    print(f"\n{written} files enriched (out of {len(ONTOLOGY)} ontology entries)")


if __name__ == "__main__":
    main()
