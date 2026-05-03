---
title: ds.process.metrics — Signal & Record Quality Metrics
aliases:
  - ds.process.metrics
  - metSpectrum
  - metRecord
  - Hjorth metrics
tags:
  - topic/ml
  - topic/signal-processing
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# ds.process.metrics

`d:\code\datascience\src\ds\process\metrics.py` | `from ds.process.metrics import X`

Signal and record quality metrics: per-component spectrum/impedance stats, generic time-series features (Hjorth, curve length, entropy), and DataFrame resampling. Used for quality control and feature engineering on [[signal-processing]] outputs from the [[jiminiDevice]].

## Index

| Name | Type | Purpose |
|------|------|---------|
| `metSpectrum` | fn | Spectrum component quality metrics (peak range, min/max/ptp) |
| `metImpedance` | fn | EIS component quality metrics (% inf/NaN) |
| `metRecord` | fn | All component metrics for a Record |
| `metGeneric` | fn | Generic array stats: min/max/mean/std + Hjorth + curve length |
| `resizeDataFrame` | fn | Resize 2D DataFrame to uniform step via image resize |
| `findPeakNaive` | fn | Find peak range at a given percentile of max |
| `lineLength` | fn | Sum of absolute first differences (normalized) |
| `curveLength` | fn | Geometric curve length via hypotenuse approximation |
| `shannonEntropy` | fn | Normalized Shannon entropy (non-stationarity) |
| `hjorthActivity` | fn | Hjorth activity = `var(arr)` (signal power) |
| `hjorthMobility` | fn | Hjorth mobility = mean frequency estimate |
| `hjorthComplexity` | fn | Hjorth complexity = similarity to pure sine |
| `skewness` | fn | Scipy skewness along axis |
| `kurtosis` | fn | Scipy kurtosis along axis |

## Reference

### Record & Component Metrics

#### `metSpectrum(cmp: Spectrum, sampleType: str = None) → dict`
Returns quality metrics for a Spectrum component. Processes if not already processed.

| LED type | Returned keys |
|----------|---------------|
| Dark LEDs | `min`, `max`, `median`, `ptp` |
| Active LEDs | `ptp`, `peakRange`, `peakMin`, `peakMax`, `peakMedian`, `peakPtp` |
| Both | `sensorType`, `knownSensor`, `activeLed`, `ledIntensity`, `sampleType` |

#### `metImpedance(cmp: EISpectrum, sampleType: str = None) → dict`
Returns quality metrics for an EIS component.
- Returns `sensorType`, `pctInf`, `pctNan`, `ledIntensity`, `knownSensor`

#### `metRecord(rec: Record) → dict`
Runs `metSpectrum` or `metImpedance` on each component of a record.
- Returns `{cmpName: metrics_dict}` for all Spectrum and EISpectrum components

#### `metGeneric(arr) → dict`
Generic stats on any array. Returns `min`, `max`, `mean`, `std`, `skewness`, `kurtosis`, `hjorthMobility`, `hjorthComplexity`, `hjorthActivity`, `curveLength`.

> [!WARNING]
> `curveLength` call uses `arr.index.diff()` — expects pandas Series with numeric index.

### DataFrame Utilities

#### `resizeDataFrame(df: DataFrame, step=None, roundIndices: int = 1) → DataFrame`
Resamples a 2D DataFrame to uniform step size via `skimage.transform.resize`.
- `step`: target grid step; defaults to min of both axis diffs
- Preserves index/column names and range

#### `findPeakNaive(ser: Series, pct: float = 0.95) → ndarray`
Returns `[start, end]` wavelengths where signal ≥ `pct * max`.

> [!WARNING]
> Accesses `ser.data` — expects a Component, not a plain Series.

### Time-Series Feature Functions

#### `lineLength(data, norm: bool = True) → float`
Sum of absolute first differences. If `norm=True`, divides by `len(data) - 1`.

#### `curveLength(arr, fs: float, norm: bool = True) → float`
Geometric curve length: `Σ sqrt(Δy² + (1/fs)²)`. Normalized by segment count if `norm=True`.
- `fs`: sampling frequency in Hz

#### `shannonEntropy(data, bins: int) → float`
Normalized Shannon entropy: `H / log(bins - 1)`. Measures non-stationarity.

### Hjorth Parameters

Hjorth parameters characterize signal complexity in the time domain — originally developed for EEG but useful for any time series.

#### `hjorthActivity(arr) → float`
`var(arr)` — estimates signal power.

#### `hjorthMobility(arr) → float`
`sqrt(var(diff(arr)) / var(arr))` — estimates mean frequency.

#### `hjorthComplexity(arr) → float`
`mobility(diff(arr)) / mobility(arr)` — 1.0 for pure sine, higher for complex signals.

### Statistical Wrappers

#### `skewness(arr, axis: int = 0) → float`
Thin wrapper around `scipy.stats.skew`.

#### `kurtosis(arr, axis: int = 0) → float`
Thin wrapper around `scipy.stats.kurtosis`.

## Sources

| Source | Notes |
|--------|-------|
| `d:\code\datascience\src\ds\process\metrics.py` | Module source |
| Hjorth (1970) | Original Hjorth parameter definitions |

## Gaps

- `metGeneric` requires a pandas Series with numeric index; behavior on plain ndarray is not documented
- No aggregate QC thresholds defined — callers must set pass/fail criteria externally
- `resizeDataFrame` uses image resize (bilinear) which may introduce artifacts for sparse spectra

[signal-processing]: ../../../biomarkers/signal-processing.md "Signal Processing & Matrix Correction for Jimini Urine Spectroscopy"
[jiminiDevice]: ../../jiminiDevice.md "Jimini Device"
