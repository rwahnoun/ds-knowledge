---
title: ds.process.transformers — Sklearn-Compatible Spectral Transformers
aliases:
  - ds.process.transformers
  - transformers
  - RobustAbsorbance
  - ScatterCorrection
  - mkPipeline
tags:
  - topic/ml
  - topic/signal-processing
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# ds.process.transformers

`d:\code\datascience\src\ds\process\transformers.py` | `from ds.process.transformers import X`

Scikit-learn compatible transformers for spectral and EIS data. All inherit `BaseEstimator` / `TransformerMixin`. Input/output are pandas DataFrames unless noted. These are the pipeline-safe wrappers around the low-level functions in [[prcPandas]]. See also [[normalization]], [[signal-processing]], [[libraries]].

## Index

| Name | Type | Purpose |
|------|------|---------|
| `PandasTransformer` | class | Base class for DataFrame transformers |
| `DarkCurrentCorrection` | class | Subtract dark current, clip |
| `ReferenceCorrection` | class | Subtract reference with optional dark correction |
| `Absorbance` | class | Log absorbance with dark + reference correction |
| `RobustAbsorbance` | class | Per-device log absorbance using macAddress water reference |
| `RobustFluorescence` | class | Per-device fluorescence by subtracting water reference |
| `ScatterCorrection` | class | SNV / MSC / EMSC / RNV scatter correction |
| `Norm` | class | L1 or L2 norm normalization |
| `SavitzkyGolay` | class | Savitzky-Golay smooth/differentiate (wavelength window) |
| `BaselineCorrection` | class | Baseline removal via `spcBaselineRemoval` |
| `Derive` | class | Numerical derivative |
| `Scaler` | class | Local min-max scaling between wavelength regions |
| `Trim` | class | Trim to wavelength range + optional stride |
| `VarianceFilter` | class | Remove near-constant features by variance threshold |
| `IdentityTransformer` | class | Pass-through (no-op) transformer |
| `ExtractComponent` | class | Extract + process named component from Record/Dataset |
| `ExtractPeaks` | class | Extract peak statistics within wavelength windows |
| `ExtractFeaturesEIS` | class | Extract 31 EIS features per row via `prcCplxEIS` |
| `DatasetExtractFeatures` | class | Extract per-peak stats from all components of a Dataset |
| `mkRef` | fn | Build per-macAddress reference dict from water samples |
| `mkPipeline` | fn | Build sklearn Pipeline from list of step spec dicts |

## Reference

### Base

#### `PandasTransformer(cfg: dict = None)`
Base class. Child classes set `self.fn` (callable) and `self.cfg` (dict passed as kwargs to fn). Handles `feature_names_in_`, `get_feature_names_out`, `__repr__`.
- Supports `allow_nan=True`
- Configures metadata routing (`meta="ignore"`) for sklearn 1.3+

### Signal Correction Transformers

#### `DarkCurrentCorrection(dark=None, clip: list = [0, inf])`
Subtracts dark spectrum and clips result.
- `dark`: dark spectrum (same shape as X or Series); None = passthrough

#### `ReferenceCorrection(dark=None, ref=None, refDark=None, clip: list = [0, inf])`
Subtracts reference from signal. Optionally dark-corrects the reference first.
- If `ref=None`, passthrough — no error raised.

#### `Absorbance(dark=None, ref: float|DataFrame = 0.5, refDark=None, clip: float = 2.5, na: float = 0)`
Calculates `-log10(dark_corrected_signal / ref)`, clipped to `[0, clip]`.
- `ref`: blank spectrum (DataFrame, Series) or float white level
- `na`: fill value for inf/NaN results

#### `RobustAbsorbance(clip: float = 2.5, na: float = 0, minSigValue: float = 2.5e-3, nanNegSignal: bool = True)`
Per-device absorbance via Beer-Lambert law. Reference set explicitly via `setWaterRef()` before pipeline execution.

| Parameter | Description |
|-----------|-------------|
| `minSigValue` | Pixels below threshold masked as NaN before log |
| `nanNegSignal` | Masks wavelengths where sample > reference |

- `setWaterRef(X, meta, sampleType="water")`: computes per-device water reference grouped by macAddress
- `transform(X, meta)` requires `meta` with `macAddress` column via metadata routing (`set_transform_request(meta=True)`)
- `fit()` is a no-op; call `setWaterRef()` before transform

#### `RobustFluorescence(clip: float = 2.5, na: float = 0, minSigValue: float = 2.5e-3, nanNegSignal: bool = True)`
Per-device fluorescence: `clip(signal - ref, 0, clip)`. Same API pattern as `RobustAbsorbance`.
- `nanNegSignal`: zeros wavelengths where sample < reference
- `setWaterRef(X, meta, sampleType="water")`: computes per-device water reference
- `transform(X, meta)` requires `meta` via metadata routing

### Scatter & Normalization

#### `ScatterCorrection(method: str, iqr: list = [75, 25], order: int = 2)`
- `method`: `"snv"` | `"msc"` | `"emsc"` | `"rnv"`
- `iqr`: percentiles for RNV only
- `order`: polynomial order for EMSC baseline terms
- Raises `NotImplementedError` if method is not one of the four above.

#### `Norm(method: str = "L1")`
Normalizes spectra by L1 or L2 norm.
- `method`: `"L1"` (sum of absolutes) or `"L2"` (Euclidean)

### Smoothing & Differentiation

#### `SavitzkyGolay(wndWl: int = 10, poly: int = 2, deriv: int = 1)`
Wavelength-unit window Savitzky-Golay via `prcPandas.savgol`.
- `wndWl`: window in same units as column index (e.g. nm)
- `deriv`: 0 = smooth only

#### `BaselineCorrection(method=None, order=None, smooth=None, degree=None, roi=None)`
Baseline removal via `prcSpectrum.spcBaselineRemoval`.
- `method`: e.g. `"rubberband"`, `"arPLS"`
- `roi`: region-of-interest tuple

#### `Derive(order: int = 1, delta: int = 1)`
Numerical derivative via `prcPandas.derive` (`np.gradient`).

### Scaling & Trimming

#### `Scaler(min=None, max=None, method: str = "meanmax")`
Local scaling via `prcPandas.localMinMaxScaler`.
- `min` / `max`: `[start, end]` wavelength ranges or scalars
- `method`: `"minmax"` | `"meanmax"` | `"mean"`

#### `Trim(rng=None, step: int = 1)`
Trims columns to wavelength range, then subsamples by stride.
- `rng`: `[start, end]` inclusive; None = keep all

#### `VarianceFilter(thr: float = 1e-6)`
Removes features with variance at or below the threshold.
- `featureMask` computed during `fit()`, applied in `transform()`

#### `IdentityTransformer()`
Pass-through transformer. Declares `meta="ignore"` metadata routing for consistent use alongside other transformers.

### Feature Extraction

#### `ExtractComponent(cmp: str|dict, addCmpName: bool = False, **kwargs)`
Extracts a named component from `Record`, `DatasetRecords`, or `list`.
- `cmp`: component name string or dict
- `cmpRef`: keyword arg — reference component for processing
- `addCmpName`: prefix output columns with `{cmp}_`
- Dispatches to `prcSpectrum`, `prcIRMatrix`, or `prcEIS` based on component class
- Returns empty Series (not error) on extraction failure

#### `ExtractPeaks(peaks=None, method: str = "mean", halfWnd: int = 3, avg: bool = True)`
Extracts statistics within wavelength windows around peaks.

| Parameter | Description |
|-----------|-------------|
| `peaks` | dict `{name: (wl_start, wl_end)}` \| list of wavelengths \| component name string (auto-generates via `jimStimPeaks`) |
| `method` | `"mean"` \| `"max"` \| `"absmax"` \| `"sum"` |
| `avg` | Append global mean column |

- If `peaks=None`, passthrough — no features extracted.

#### `ExtractFeaturesEIS()`
Applies `prcCplxEIS` row-wise. No parameters. Outputs 31 EIS features per row — see [[prcPandas]] for feature list.

#### `DatasetExtractFeatures(**kwargs)`
Extracts per-peak statistics from all components of a `DatasetRecords`.
- `lstCmp`: list of components to process; None = all
- `pkHalfWnd`: half-window around stimulus peaks (default 3)
- `pkType`: `"mean"` | `"max"`
- Only processes components whose names start with `"c"`

> [!WARNING]
> Accepts only `DatasetRecords` — raises `AssertionError` otherwise.

### Pipeline Utilities

#### `mkRef(X: DataFrame, meta: DataFrame, sampleType: str = "water") → dict`
Returns `{macAddress: mean_spectrum}` for rows where `meta.sampleType == sampleType`. Used internally by `RobustAbsorbance` / `RobustFluorescence`.

#### `mkPipeline(stepSpecs: list) → Pipeline`
Builds `sklearn.Pipeline` from a list of step specification dicts.

Each dict has:
- `"name"` (str, required): transformer name from the registry below
- `"kwargs"` (dict, optional): keyword arguments for the transformer `__init__`

Steps are named `step_0`, `step_1`, etc. in the resulting pipeline.

**Registry:**

| Name | Class |
|------|-------|
| `identity` | `IdentityTransformer` |
| `robustAbs` | `RobustAbsorbance` |
| `robustFluo` | `RobustFluorescence` |
| `savgol` | `SavitzkyGolay` |
| `scatter` | `ScatterCorrection` |
| `extractEIS` | `ExtractFeaturesEIS` |
| `darkCurrentCorr` | `DarkCurrentCorrection` |
| `refCorr` | `ReferenceCorrection` |
| `absorbance` | `Absorbance` |
| `extractPeaks` | `ExtractPeaks` |
| `scaler` | `Scaler` |
| `baselineCorr` | `BaselineCorrection` |
| `derive` | `Derive` |
| `trim` | `Trim` |
| `varianceThreshold` | `sklearn.feature_selection.VarianceThreshold` |
| `robustScaler` | `sklearn.preprocessing.RobustScaler` |
| `standardScaler` | `sklearn.preprocessing.StandardScaler` |
| `powerTransformer` | `sklearn.preprocessing.PowerTransformer` |
| `selectKBest` | `sklearn.feature_selection.SelectKBest` |
| `logisticRegression` | `sklearn.linear_model.LogisticRegression` |
| `plsRegression` | `sklearn.cross_decomposition.PLSRegression` |

## Example

```python
from ds.process.transformers import mkPipeline

ppl = mkPipeline([
    {"name": "robustAbs"},
    {"name": "savgol", "kwargs": {"wndWl": 15, "poly": 2, "deriv": 1}},
    {"name": "trim", "kwargs": {"rng": [400, 800]}},
])
```

## Sources

| Source | Notes |
|--------|-------|
| `d:\code\datascience\src\ds\process\transformers.py` | Module source |
| scikit-learn docs | `BaseEstimator`, `TransformerMixin`, metadata routing |

## Gaps

- `RobustAbsorbance` / `RobustFluorescence` require `setWaterRef()` before use — no guard if called without it
- `ExtractComponent` failure mode (returns empty Series) can silently propagate through a pipeline
- `DatasetExtractFeatures` component name filter (starts with `"c"`) is undocumented and surprising
- EMSC `order` parameter behavior not described in detail
