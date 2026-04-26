---
title: datascience repo — Core ds Library
aliases:
  - datascience
  - ds package
  - ds library
tags:
  - topic/repo
  - type/architecture
  - status/complete
date: 2026-04-26
status: complete
type: architecture
author: Usense Healthcare
---

# datascience

Core Python library (`ds` package) for loading, processing, and analysing spectral/signal data. Consumed by [[ds-scripts]] and [[ds-learn]] (see [[workspace]] for the dependency graph). Conventions live in [[conventions]].

- **Path**: `d:\code\datascience`
- **GitHub**: https://github.com/usense-projects/datascience
- **Indent**: 4 spaces

## Package structure

```
examples/             # Example notebooks demonstrating library usage
src/ds/
  dataio/
    datamodel.py        # Pydantic data models (Record, Biomarker, etc.)
    record.py           # Record abstraction
    dataset.py          # Dataset abstraction
    component.py        # Component abstraction
    loaders/            # Source-specific loaders (jimini, jasco, palmsens, ...)
    etl/                # ETL pipelines — ingest, transform, update databases
    remote/             # DB clients: MongoDB (azureUsense), PostgreSQL (dbpg), SQLite, GDrive, Azure Blob/FileShare
  process/
    transformers.py     # Scikit-learn compatible transformers
    prcPandas.py        # Pandas-based signal processing (filters, peaks, scatter corrections)
    prcSpectrum.py      # Spectrum processing
    prcSWV.py           # Square-wave voltammetry processing
    biomarkers.py       # Biomarker estimation logic
    deconvolution.py    # Spectral deconvolution
    colourScience.py    # Colour science utilities
    metrics.py          # Metrics
    quality.py / qualityV2.py  # Quality checks
    component.py        # Process component base
  qtp/
    qtpAnalyticPerformance/   # Analytic performance QTP protocol
    qtpSignals/               # Signal QTP protocol
  tests/                # Unit tests (HTMLTestRunner)
  exceptions.py         # All error codes with domain/message/status
  loadEnv.py            # .env loader
  notebook.py           # Notebook utilities
  tools.py              # General utilities (jprint, ...)
  viz.py / dataio/viz.py  # Visualisation helpers
```

## Data structures

The `ds` library provides a three-level hierarchy. See [[projectDescription]] for the deeper data-model reference and component subtypes.

**`Dataset` (ds)** — either a dataset of records or a dataset of features.

- Contains metadata (sample info, conditions, etc.) and biomarkers (target variables)
- Access: `ds.meta`, `ds.biomarkers`, `ds.data` (if features), `ds[rec]` (if records)

**`Record` (rec)** — a single sample/record instance.

- Contains metadata and a dict of signals
- Each signal is a DataFrame named after its sensor and LED (e.g., `C12-405` = sensor C12 with LED 405)
- Signals are also called **components** or **slices** (e.g., `slc`)

```python
rec = ds[0]                     # Get first record
rec.meta                        # Metadata: sample ID, type, conditions, etc.
rec.signals                     # Dict: {'C12-405': df, 'C12-530': df, ...}
slc = rec.signals['C12-405']    # Access a component/slice
```

## Examples

Example notebooks demonstrating library usage live in `examples/` at the repo root:

- `transformers.ipynb` — transformer pipeline usage and patterns

## Repo-specific conventions

Naming, style, and tooling are defined in [[conventions]]. The following are specific to this repo:

- **Indent**: space (4 spaces per level)
- **Databases**: MongoDB (Azure) for records, PostgreSQL for biomarkers; clients in `dataio/remote/`
- **Pipelines**: scikit-learn `Pipeline` + custom transformers in `process/transformers.py`
- **Errors**: define new error types in `exceptions.py`, never use bare strings for error codes
- **Class members**: public by default (no leading underscore prefixes)

## Development workflow

**Iterate locally**:

```bash
uv pip install -e .

ruff check src/ds --fix
ruff format src/ds

python -m pytest src/ds/tests/ -v
```

**Before deploying**:

1. Run full test suite locally
2. Run QTP protocols (Algorithm QTP in `qtp/qtpAnalyticPerformance/`, Signals QTP in `qtp/qtpSignals/`)
3. Update algorithm version in code (format: `name-Vx.y.z`)
4. Hand off pickle to `ds-compute` repo for API integration

## Testing

```bash
python -m pytest src/ds/tests/
python -m pytest src/ds/tests/ --cov=ds
```

Tests in `src/ds/tests/` cover loaders, data models, and model staging. QTP protocols (`qtp/`) are run separately at algorithm release time.

## Installation

```bash
python -m pip install uv
# then follow datascience/docs/scripts/setupEnv.ps1
uv pip install -e .
```

## Documentation

Repo-internal docs live in `docs/` as Markdown files. Write new repo-specific documentation there; this vault is for the higher-level reference layer.

## Deployment

Algorithms are serialised as `.joblib` pickles and deployed via Azure Functions (`ds-compute` repo). Deployment sequence: train → QTP → integrate into API → unit tests local → staging → prod. See `docs/datascience.md` for the full deployment workflow.

## Sources

| Source | Notes |
|--------|-------|
| [`d:\code\datascience\src\ds\`](file:///D:/code/datascience/src/ds/) | Source tree |
| [`d:\code\datascience\docs\`](file:///D:/code/datascience/docs/) | Repo-internal docs (deployment, scripts) |
| [`d:\code\datascience\pyproject.toml`](file:///D:/code/datascience/pyproject.toml) | Build config, deps |

## Gaps

- `qtp/` workflow is referenced but the protocol structure is not detailed in this vault.
- `ds-compute` integration step is referenced but that repo is not documented here.
