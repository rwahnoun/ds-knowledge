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
- `type/` — concept, literature, pipeline, reference, architecture, decision
- `status/` — draft, in-progress, complete
- `device/` — jimini

**Rules:**
- `aliases` must include every name you might use in a `[[wikilink]]` elsewhere
- `title` can be omitted if the H1 heading is identical
- Use nested tags (`topic/ml`) not flat tags (`ml`) — Obsidian renders them as a hierarchy
- `status/draft` = rough notes; `status/in-progress` = active; `status/complete` = stable reference

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
