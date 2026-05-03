# Obsidian File Template & Conventions

Instructions for writing new notes or editing existing ones in this vault.

---

## Frontmatter

Every file should start with a YAML frontmatter block:

```yaml
---
title: Human-readable title
aliases:
  - Alternative Name        # used for [[wikilinks]] from other notes
  - Short Name
tags:
  - topic/spectroscopy      # nested tags: topic/subtopic
  - type/concept            # see tag namespaces below
  - status/complete
date: YYYY-MM-DD
status: complete            # draft | in-progress | complete
type: concept               # concept | literature | pipeline | reference | architecture
author: Usense Healthcare
---
```

**Tag namespaces:**
- `topic/` — spectroscopy, ml, chemometrics, hardware, biomarker, signal-processing
- `type/` — concept, literature, pipeline, reference, architecture, decision, index
- `status/` — draft, in-progress, complete, living
- `device/` — jimini

**Biomarker-specific namespaces** (used on compound sheets in `biomarkers/compounds/`):
- `class/` — metabolite, electrolyte, vitamin, amino-acid, protein, cellular, small-molecule, contaminant, pigment, trace-element, physico-chemical
- `subclass/` — finer chemical classification (e.g. `subclass/nitrogenous-waste`, `subclass/heme-protein`)
- `clinical/` — kidney-function, uti, hematuria, diabetes, oncology, electrolyte-balance, nephrolithiasis, contamination, liver, porphyria, normalization-reference, …
- `modality/` — uv, vis, nir, fluorescence, scattering, eis, raman, ftir, refractometry
- `presence/` — normal, trace, trace-or-abnormal, abnormal

**Rules:**
- `aliases` must include every name you might use in a `[[wikilink]]` elsewhere
- `title` can be omitted if the H1 heading is identical
- Use nested tags (`topic/ml`) not flat tags (`ml`) — Obsidian renders them as a hierarchy
- `status/draft` = rough notes; `status/in-progress` = active; `status/complete` = stable reference

---

## Biomarker compound sheets — ontology fields

Compound sheets under `biomarkers/compounds/<class>/` carry additional structured frontmatter so they can be queried by Dataview and visualised by Breadcrumbs/Excalibrain. Generated and refreshed by `meta/enrich_frontmatter.py` — edit the table at the top of that script to update vault-wide.

```yaml
class: metabolite                   # single string, matches a class/ tag
subclass: nitrogenous-waste         # optional finer classification
clinical-use:                       # list of clinical contexts
  - kidney-function
  - normalization-reference
detection-modality:                 # list of measurement modalities
  - uv
  - nir
presence: normal                    # normal | trace | trace-or-abnormal | abnormal
parent: "[[biomarkers/compounds/metabolites/index|metabolites]]"   # Breadcrumbs typed link
```

The `parent:` key is a Breadcrumbs hierarchical relation. The corresponding tags (`class/metabolite`, `clinical/kidney-function`, `modality/uv`, `presence/normal`, etc.) are added to the `tags:` block so the same information is queryable both ways.

---

## Wikilinks

Cross-link related notes inline using `[[note-name]]` or with an alias `[[note-name|display text]]`.

Common vault links to use where relevant:
- `[[normalization]]` `[[matrix-correction]]` `[[calibration-transfer]]`
- `[[signal-processing]]` `[[multi-task-modeling]]` `[[physics-grounded-ml]]`
- `[[turbidity]]` `[[spectroscopy-biomarkers]]` `[[libraries]]`

---

## Callout / Info Box Patterns

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to succeed.

> [!WARNING]
> Urgent info that needs immediate attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```

---

## Structure Conventions

- Use `##` for top-level sections, `###` for subsections
- Lead with a 2–3 line context block (device, date, status) after the H1
- End with a `## Sources` table and a `## Gaps` section for open questions
- Code blocks: always specify language (` ```python `, ` ```yaml `, etc.)
- Tables preferred over bullet lists for comparisons
