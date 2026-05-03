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
  - status/complete
date: 2026-04-26
status: complete
type: reference
author: Usense Healthcare
---

# Code Conventions

Shared conventions across [[datascience]], [[ds-scripts]], and [[ds-learn]]. **These are non-negotiable** — they are enforced by ruff config, by code review, and by the people who have to read each other's notebooks. See [[workspace]] for repo layout.

## Language & tools

- **Python**: 3.11+
- **Package manager**: `uv`
- **Build system**: `hatchling`
- **Linter/formatter**: `ruff` (line-length 150)
- **Testing**: `pytest`

## Naming

> [!IMPORTANT]
> All naming rules below are **strict** and apply across all three repos. No underscores in variable, function, or method names.

| Element | Convention | Examples |
|---------|------------|----------|
| Variables, functions, methods | `camelCase` — no underscores | ✅ `xTest`, `dataFrame`, `trainModel()` <br> ❌ `X_test`, `data_frame`, `train_model()` |
| Classes | `CamelCase` (PascalCase) | ✅ `FleetPDS`, `DataLoader`, `SignalProcessor` <br> ❌ `fleet_pds`, `data_loader` |
| Constants | `UPPER_CASE` | `MAX_ITERATIONS`, `DEFAULT_SIZE` |

**Names must be meaningful but kept short.** Use the standard abbreviations:

| Short | Meaning | Short | Meaning |
|-------|---------|-------|---------|
| `src` | source | `cfg` | config |
| `tgt` | target | `val` | value |
| `ds` | dataset | `res` | result |
| `sid` | sampleId | `idx` | index |
| `rec` | record | `df` | DataFrame |
| `slc` | slice / component | | |

**Train/test/validation splits** use the suffix form, never the underscore form:

| ✅ Use | ❌ Don't use |
|--------|--------------|
| `xTr`, `xTe`, `xVal` | `X_train`, `X_test`, `X_val` |
| `yTr`, `yTe`, `yVal` | `y_train`, `y_test`, `y_val` |
| `idxTr`, `idxTe`, `idxVal` | `idx_train`, `idx_test`, `idx_val` |
| `srcDs`, `tgtRec`, `sidList` | `sourceDataset`, `targetRecord`, `sampleIdList` |

## Class member visibility

**Default: write all class members as public** unless explicitly asked otherwise.

- No leading underscore prefixes (`_methodName`, `_attribute`) on methods or properties
- Make everything public by default; only use private/protected if explicitly requested for a particular context

## Code style

- **Indent**: varies by repo — see table below
- **Philosophy**: lean, efficient code; comments only for non-obvious logic
- **Docstrings**: Google format, required on all public functions, methods, and classes

| Repo | Indent |
|------|--------|
| [[datascience]] | **4 spaces** |
| [[ds-scripts]] | **tab** |
| [[ds-learn]] | **tab** |

```python
def myFunction(arg1, arg2):
    """Short description.

    Args:
        arg1: Description.
        arg2: Description.

    Returns:
        Description of return value.

    Raises:
        ValueError: When arg1 is invalid.
    """
```

## Data & models

- **Data models**: Pydantic v2 (`BaseModel`) with `computed_field` and `PlainSerializer` where needed
- **ML pipelines**: scikit-learn `Pipeline` + custom transformers
- **Model serialization**: `joblib` (`.joblib` files)
- **Algorithm versioning**: `name-Vx.y.z`
  - `x` = signal/model change (major)
  - `y` = bugfix (minor)
  - `z` = data version (patch)
  - Example: `mdlPbgCntRngNw-V0.1.joblib`

## Errors

- Define new error types in `exceptions.py` — never use bare strings for error codes
- Use domain-specific error codes with clear messages

## Libraries (preferred)

When available, use:

- `sklearn` (scikit-learn)
- `tensorflow`
- `pandas`
- `numpy`
- `scipy`
- `matplotlib.pyplot`

See [[libraries]] for the full ecosystem reference.

## Visualization

Matplotlib plots use thin lines: `lw=1` for all plot calls.

```python
import matplotlib.pyplot as plt
plt.plot(x, y, lw=1)
```

## Imports

- Prefer importing from the [[datascience]] library (core shared package)
- Keep imports organized: stdlib → third-party → local

## Dependencies

The `knowledge` package (private GitHub repo: device/biomarker ontology) is required in:

- [[datascience]]
- [[ds-learn]]

## Setup

```bash
# Install uv
python -m pip install uv

# Install repo in editable mode
uv pip install -e .

# With extras (ds-learn only)
uv pip install -e ".[azure]"
```

## Common workflows

**Lint & format**:

```bash
ruff check src/ --fix
ruff format src/
```

**Run tests**:

```bash
python -m pytest src/tests/ -v
python -m pytest src/tests/ --cov=<package>
```

**Verify installation**:

```bash
python -c "import ds; print('OK')"
```

## Sources

| Source | Notes |
|--------|-------|
| `~/.claude/code-conventions.md` | (deprecated — content moved here) |
| Each repo's `pyproject.toml` | Ruff config, deps |
| Each repo's `CLAUDE.md` | Pointers back to this note |

## Gaps

- No documented type-hint policy. Some files use full type hints, others don't — convention should be made explicit.
- Pre-commit hook config is not standardized across the three repos.

[workspace]: workspace.md "Workspace Layout — datascience, ds-scripts, ds-learn"
[libraries]: ../../datascience/libraries.md "Python Libraries for Spectrophotometry & Biomarker Estimation"
