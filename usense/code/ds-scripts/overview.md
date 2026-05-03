---
title: ds-scripts repo — Analysis Notebooks & Studies
aliases:
  - ds-scripts
  - scripts repo
tags:
  - topic/repo
  - type/architecture
  - status/complete
date: 2026-04-26
status: complete
type: architecture
author: Usense Healthcare
---

# ds-scripts

Analysis notebooks and scripts. Studies are numbered sequentially (`dsNNN`). Depends on the [[datascience]] library (`ds` package). See [[workspace]] for the dependency graph and [[conventions]] for shared coding rules.

- **Path**: `d:\code\ds-scripts`
- **GitHub**: https://github.com/usense-projects/ds-scripts
- **Indent**: tab

## Structure

```
examples/            # Example notebooks demonstrating typical usage patterns
src/
  notebooks/
    ds000/    # Early studies (holmium, cancer Lyon, conductometry, ...)
    ds200/    # Studies ds2xx
    ds300/    # Studies ds3xx (jimini drift, device comparison, prod records, ...)
    ds400/    # Studies ds4xx
    ds500/    # Studies ds5xx (analytic performance, innov, ...)
    ds600/    # Studies ds6xx (validations, interference methods, ...)
    infection/  # Infection-related sub-studies
  projects/
    AllBiomarkers/   # Multi-biomarker analysis (ingest, notebooks per biomarker)
    infection/       # Infection models (RBC, WBC, epithelial, nitrites, ...)
    HolyGrail/       # HolyGrail project
    biogroupExport/  # Biogroup export/report
    PHA/             # Acute porphyria (TUP, PBG)
    dataFormat/      # Data format proposals
    experiments/     # PHA flow experiments
  cja/              # CJA-specific studies (Cochin, QTP, activation optique, ...)
```

## Repo-specific conventions

Naming, style, and tooling are defined in [[conventions]]. The following are specific to this repo:

- **Indent**: tab
- **Imports**: prefer functions and classes from the [[datascience]] repo
- **Notebooks**: `.ipynb` (Jupyter) or `.py` scripts; both are common
- **Study numbering**: `dsNNN_shortDescription` — add new studies by incrementing the number
- **Project structure**: each project folder has `ingest.py` (data loading), analysis notebooks, `readme.md`
- **Shared helpers**: `common.py` / `know.py` files scoped to a project

## Typical notebook pattern

```python
from ds.dataio.remote.azureUsense import ...   # load data
from ds.process.prcSpectrum import ...         # process
import matplotlib.pyplot as plt                # plot
```

## Development workflow

**Run notebooks**:

```bash
# Execute a notebook and save output (no browser)
python -m ds.notebook src/notebooks/ds000/notebookName.ipynb

# Or use jupyter directly
jupyter nbconvert --to notebook --execute src/notebooks/ds000/notebookName.ipynb

# Or in interactive mode
jupyter notebook
```

**Add a new study**:

1. Create folder: `src/notebooks/dsNNN_shortDescription/`
2. Create `ingest.py` (data loading helper)
3. Create analysis notebooks: `dsNNN_analysis.ipynb`, `dsNNN_plots.ipynb`, etc.
4. Optional: add `common.py` for shared helpers, `readme.md` for study overview

**Run tests & lint**:

```bash
python -m pytest src/tests/ -v
ruff check src/ --fix
ruff format src/
```

## Documentation

Repo-internal docs live in `docs/` as Markdown files.

## Dependencies

Declared in `pyproject.toml` (name: `scripts`). Core: `numpy`, `pandas`, `scipy`, `matplotlib`, `jupyterlab`. The [[datascience]] library is expected to be installed separately in the same environment.

## Sources

| Source | Notes |
|--------|-------|
| [`d:\code\ds-scripts\src\`](file:///D:/code/ds-scripts/src/) | Notebooks and project sources |
| [`d:\code\ds-scripts\pyproject.toml`](file:///D:/code/ds-scripts/pyproject.toml) | Build config, deps |

## Gaps

- No documented retention policy for old `dsNNN` studies — when (if ever) are they archived?
- Project-level `ingest.py` patterns are not standardized; conventions vary across `projects/`.

[workspace]: ../workspace.md "Workspace Layout — datascience, ds-scripts, ds-learn"
[conventions]: ../conventions.md "Code Conventions — Usense Datascience Repos"
