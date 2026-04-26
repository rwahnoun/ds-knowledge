---
title: Workspace Layout — datascience, ds-scripts, ds-learn
aliases:
  - workspace
  - repos overview
  - dependency graph
tags:
  - topic/repo
  - type/architecture
  - status/complete
date: 2026-04-26
status: complete
type: architecture
author: Usense Healthcare
---

# Workspace Layout

The `d:\code\` workspace contains three Python repositories for datascience work at Usense Healthcare. They share the same Python/ruff conventions (see [[conventions]]) and are typically refactored together. This note is the orientation document — read it first when picking up work in any of the three repos.

## Repositories

| Repo | Path | Role |
|------|------|------|
| [[datascience]] | `d:\code\datascience` | Core library (`ds` package) — loaders, ETL, signal processing, transformers, DB clients |
| [[ds-scripts]] | `d:\code\ds-scripts` | Analysis notebooks & scripts — numbered studies, biomarker projects |
| [[ds-learn]] | `d:\code\ds-learn` | ML models & training — scikit-learn pipelines, trained `.joblib` models, Azure ML deployment |

## Dependency graph

```
ds-scripts  ──┐
              ├──► datascience (ds)
ds-learn    ──┘
```

`datascience` is the shared library consumed by both other repos. **Multi-repo refactors typically start in `datascience` and propagate to `ds-scripts` and/or `ds-learn`.**

## Quick start

```bash
# Install Python 3.11+, then:
python -m pip install uv

# In each repo (or all three):
uv pip install -e .

# Verify installation
python -c "import ds; print('datascience OK')"
```

## Python virtual environments

Virtual environments are centralized at `d:\code\venvs\` and shared across all three repos.

| Venv | Purpose | Python |
|------|---------|--------|
| **py312** | Default for datascience projects | 3.12 |
| py311 | Alternative | 3.11 |
| py313 | Alternative | 3.13 |
| py314 | Latest (experimental) | 3.14 |
| py314t | Latest with free-threading (experimental) | 3.14 |
| py312-sklearn150 | scikit-learn 1.5.0 testing | 3.12 |
| py312oldSkLearn | Legacy scikit-learn version | 3.12 |
| deepcode | Specialized environment | 3.12 |
| sweetviz | Data profiling & visualization | 3.12 |

**Default activation** (datascience, ds-scripts, ds-learn → `py312`):

```bash
source d:/code/venvs/py312/Scripts/activate

# Or rely on uv directly
uv pip install -e .
```

## Knowledge base

The repo-internal docs index lives at [`d:\code\datascience\docs\README.md`](file:///d:/code/datascience/docs/README.md) — biomarkers, Jimini device specs, signal processing pipelines, module APIs, database schema. Use it to orient before any task in this workspace.

The Obsidian vault at `d:\code\ds-knowledge\` (this note's home) is the higher-level reference layer — concepts, papers, project descriptions.

## Sources

| Source | Notes |
|--------|-------|
| `d:\code\datascience\pyproject.toml` | Build config, deps |
| `d:\code\ds-scripts\pyproject.toml` | Build config, deps |
| `d:\code\ds-learn\pyproject.toml` | Build config, deps |
| `d:\code\venvs\` | Centralized Python venvs |

## Gaps

- No top-level `pyproject.toml` or workspace tool that installs all three repos in one command.
- The `knowledge` private dependency is referenced by `datascience` and `ds-learn` but its install procedure is not documented in this vault.
