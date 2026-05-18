---
title: Code Conventions — Usense Datascience Repos
aliases:
  - conventions
  - code conventions
  - coding standards
  - naming conventions
tags:
  - topic/repo
  - type/reference
date: 2026-04-26
---

# Code Conventions

Shared conventions for `datascience`, `ds-scripts`, `ds-learn`. See [[workspace]] for repo layout.

## Behavioral Guidelines

**Think before coding.** State assumptions explicitly. If multiple interpretations exist, present them — don't pick silently. Push back if a simpler approach exists. If something is unclear, ask before implementing.

**Surgical changes.** Touch only what's needed for the request. Don't improve adjacent code, comments, or formatting. Remove imports/variables YOUR changes made unused; mention pre-existing dead code rather than deleting it.

**Goal-driven execution.** For multi-step tasks, state a brief plan with checkpoints before starting. Define verifiable success criteria — "tests pass" beats "make it work".

## Language & Tools

| Tool | Choice |
|------|--------|
| Python | 3.11+ |
| Package manager | `uv` |
| Build system | `hatchling` |
| Linter/formatter | `ruff` (line-length 150) |
| Testing | `pytest` |

## Naming

**Strict — no underscores in variables, functions, or methods.**

| Element | Convention | Example |
|---------|------------|---------|
| Variables, functions, methods | `camelCase` | `xTest`, `trainModel()` |
| Classes | `PascalCase` | `FleetPDS`, `SignalProcessor` |
| Constants | `UPPER_CASE` | `MAX_ITERATIONS` |

Standard abbreviations:

| Short | Meaning | Short | Meaning |
|-------|---------|-------|---------|
| `src` | source | `cfg` | config |
| `tgt` | target | `val` | value |
| `ds` | dataset | `res` | result |
| `sid` | sampleId | `idx` | index |
| `rec` | record | `df` | DataFrame |
| `slc` | slice/component | | |

Train/test splits — suffix form only:

| | x | y | idx |
|---|---|---|---|
| ✅ | `xTr` `xTe` `xVal` | `yTr` `yTe` `yVal` | `idxTr` `idxTe` `idxVal` |
| ❌ | `X_train` `X_test` `X_val` | `y_train` `y_test` `y_val` | `idx_train` `idx_test` `idx_val` |

## Class Members

Default: **all public**. No leading underscores unless explicitly requested.

## Code Style

Indent: **4 spaces** across all repos.

Comments only for non-obvious logic. Docstrings: Google format, required on all public functions, methods, and classes.

```python
def myFunction(arg1, arg2):
    """Short description.

    Args:
        arg1: Description.
        arg2: Description.

    Returns:
        Description.

    Raises:
        ValueError: When arg1 is invalid.
    """
```

## Data & Models

- Pydantic v2 (`BaseModel`) with `computed_field` and `PlainSerializer`
- ML pipelines: sklearn `Pipeline` + custom transformers
- Serialization: `joblib` (`.joblib` files)
- Versioning: `name-Vx.y.z` — `x` signal/model, `y` bugfix, `z` data version

## Errors

Define new types in `exceptions.py`. Never use bare strings for error codes.

## Libraries

Prefer: `sklearn`, `tensorflow`, `pandas`, `numpy`, `scipy`, `matplotlib.pyplot`. See [[libraries]].

## Visualization

`lw=1` for all plot calls.

## Imports

stdlib → third-party → local. Prefer importing from `datascience` and `ds-learn` libraries.

## Dependencies

`knowledge` package (private) required in `datascience` and `ds-learn`.

## Setup

```bash
python -m pip install uv
uv pip install -e .
uv pip install -e ".[azure]"   # ds-learn only
```

## Workflows

```bash
ruff check src/ --fix && ruff format src/
python -m pytest src/tests/ -v
python -m pytest src/tests/ --cov=<package>
```
