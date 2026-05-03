---
title: ds-learn repo — ML Models & Training
aliases:
  - ds-learn
  - learn repo
tags:
  - topic/repo
  - topic/ml
  - type/architecture
  - status/in-progress
date: 2026-04-26
status: in-progress
type: architecture
author: Usense Healthcare
---

# ds-learn

ML models and training pipelines. scikit-learn `Pipeline`s + custom transformers from [[datascience]], producing trained `.joblib` models for Azure ML deployment. See [[workspace]] for the dependency graph, [[conventions]] for shared coding rules, and [[projectDescription]] for the data model.

- **Path**: `d:\code\ds-learn`
- **Indent**: tab

## Repo-specific conventions

Naming, style, and tooling are defined in [[conventions]]. Specific to this repo:

- **Indent**: tab
- **Imports**: prefer functions and classes from [[datascience]]
- **Pipelines**: scikit-learn `Pipeline` + custom transformers
- **Model serialization**: `joblib` (`.joblib` files)
- **Algorithm versioning**: `name-Vx.y.z` (see [[conventions#Data & models]])

## Installation

```bash
uv pip install -e .

# With Azure extras
uv pip install -e ".[azure]"
```

## Documentation

Repo-internal docs live in `docs/` as Markdown files.

## Sources

| Source | Notes |
|--------|-------|
| [`d:\code\ds-learn\src\`](file:///D:/code/ds-learn/src/) | Source tree |
| [`d:\code\ds-learn\pyproject.toml`](file:///D:/code/ds-learn/pyproject.toml) | Build config, deps |
| [`d:\code\ds-learn\readme.md`](file:///D:/code/ds-learn/readme.md) | Repo-level intro |

## Gaps

- This repo did not have a `CLAUDE.md` at migration time, so package structure, training entrypoints, and Azure ML deployment workflow are documented only at the readme/code level.
- Need a written counterpart to [[datascience]]'s deployment section: which scripts produce which `.joblib`, where they land, how they reach `ds-compute`.
- Trained-model registry (which versions are deployed, who deployed when) is not documented in this vault.

[workspace]: ../workspace.md "Workspace Layout — datascience, ds-scripts, ds-learn"
[conventions]: ../conventions.md "Code Conventions — Usense Datascience Repos"
[projectDescription]: ../projectDescription.md "ds-learn — Project Description & Data Model"
[conventions#Data & models]: <../conventions.md#Data & models> "Code Conventions — Usense Datascience Repos"
