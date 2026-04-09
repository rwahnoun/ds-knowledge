# ds.process.prcPandas
`d:\code\datascience\src\ds\process\prcPandas.py` | `from ds.process.prcPandas import X`

Low-level signal processing functions on pandas Series/DataFrames. Used directly or via `transformers.py` wrappers in sklearn pipelines.

## Index

| Name | Type | Purpose |
|------|------|---------|
| `localMinMaxScaler` | fn | Scale signal between two wavelength regions |
| `correctionStandardNormalVariate` | fn | SNV scatter correction (zero-mean, unit-std) |
| `correctionMultiplicativeScatterCorrection` | fn | MSC scatter correction to mean spectrum |
| `correctionRobustNormalVariate` | fn | RNV — robust SNV using median + IQR |
| `savgol` | fn | Savitzky-Golay filter with wavelength-unit window |
| `fltSavgol` | fn | Savitzky-Golay filter with point-count window |
| `fltLowess` | fn | LOWESS smoothing with optional derivative |
| `baselineRemovalRubberband` | fn | Convex-hull rubberband baseline removal |
| `absorbanceWhite` | fn | Absorbance from white reference |
| `findPeaks` | fn | Peak detection with prominence, width, base info |
| `detrendLocal` | fn | Linear/constant detrending with breakpoints |
| `derive` | fn | Numerical derivative via `np.gradient` |
| `resampleRange` | fn | Resample to new wavelength range + step |
| `impMagPhaseToCplx` | fn | Magnitude/phase → complex impedance |
| `impCplxToMagPhase` | fn | Complex impedance → magnitude/phase DataFrame |
| `prcCplxEIS` | fn | Extract 31 EIS features from complex impedance Series |

## Reference

### `localMinMaxScaler(ser: Series, min=None, max=None, method: str = "minmax") → Series`
Scales signal by subtracting a min region and dividing by a max region.
- `min`: `[start, end]` wavelength range for zero point, or scalar offset
- `max`: `[start, end]` wavelength range for normalization, or scalar divisor
- `method`: `"minmax"` | `"mean"` | `"meanmax"`

### `correctionStandardNormalVariate(ser: ndarray, axis: int = 0) → ndarray`
SNV: centers to zero mean and scales to unit variance. Removes multiplicative scatter.
⚠ Operates on ndarray, not Series — wrapper `ScatterCorrection(method="snv")` preserves DataFrame.

### `correctionMultiplicativeScatterCorrection(spectra: ndarray) → ndarray`
MSC to mean spectrum. Demeans then fits each column to the mean spectrum via polyfit.
⚠ Operates on ndarray — use `ScatterCorrection(method="msc")` in pipelines.

### `correctionRobustNormalVariate(spectra: ndarray, iqr: list = [75, 25], axis: int = 0) → ndarray`
RNV: robust version of SNV using median and IQR percentiles instead of mean/std.
- `iqr`: `[upper_percentile, lower_percentile]`
⚠ Operates on ndarray — use `ScatterCorrection(method="rnv")` in pipelines.

### `savgol(ser: Series, wndWl: float, poly: int, deriv: int) → ndarray`
Savitzky-Golay with window in wavelength units. Converts to points using median index step.
- `wndWl`: window size in same units as Series index (e.g. nm)
- Use this (via `SavitzkyGolay`) when index is wavelengths. Prefer over `fltSavgol`.

### `fltSavgol(data: Series, wndSz: int = 14, polyorder: int = 2, deriv: int = 0, mode: str = "nearest") → Series`
Savitzky-Golay with window in points. Preserves Series index.
- `wndSz`: must be odd — auto-enforced by `savgol` but not here
⚠ Use `savgol` / `SavitzkyGolay` when working with wavelength-indexed data.

### `fltLowess(ser: Series, deriv: int, fraction: float = 0.02, nbIter: int = 2) → Series`
LOWESS smoothing. Trims 2 points per derivative order (index shrinks).
- `deriv`: derivative order (0 = smooth only)
- `fraction`: bandwidth as fraction of data [0, 1]
⚠ Output index is shorter than input when `deriv > 0`.

### `baselineRemovalRubberband(ser: Series) → Series`
Convex-hull baseline removal. Fits lower convex hull and subtracts.
⚠ Fails on spectra with no discernible convex structure (flat or monotone signals).

### `absorbanceWhite(ser: Series, clip: float = 3, level: float = 1, na = np.nan) → Series`
Absorbance via `−log10(ser / level)`, clipped to `[0, clip]`.
- `level`: white reference level (scalar)

### `findPeaks(ser: Series, fpArgs: dict = None, show: bool = False) → dict`
Wraps `scipy.signal.find_peaks` with prominence and width analysis.
- `fpArgs`: passed to `scipy.find_peaks` (e.g. `{"prominence": 0.01, "width": 0}`)
- `show`: plots detected peaks
Returns dict with keys: `idx`, `wavelength`, `height`, `prominence`, `halfWidth`, `halfWidthHeight`, `leftBase`, `rightBase`, `leftIPS`, `rightIPS`

### `detrendLocal(ser: Series, type: str = "linear", breakPoints: list = None) → Series`
Detrend via `scipy.signal.detrend` with optional change points.
- `breakPoints`: list of x-values where trend can change

### `derive(ser: ndarray, order: int = 1, delta: int = 1) → ndarray`
Numerical derivative via `np.gradient`. Applied `order` times.
⚠ Operates on ndarray — use `Derive` transformer to preserve DataFrame.

### `resampleRange(df: DataFrame|Series, rng: list = None, step: int = 1, kind: str = "quadratic") → DataFrame|Series`
Interpolates to a new index range.
- `rng`: `[start, end]`; None = rounded data range
- `kind`: scipy interp1d method (`"quadratic"`, `"linear"`, etc.)

### `impMagPhaseToCplx(df: DataFrame) → Series`
Converts `magnitude` + `phase` columns to complex impedance Series indexed by frequency.

### `impCplxToMagPhase(cplx: Series) → DataFrame`
Converts complex impedance to `magnitude` + `phase` DataFrame.

### `prcCplxEIS(ser: Series) → Series`
Extracts 31 EIS features from a complex impedance Series (frequency-indexed).
Accepts either complex Series or DataFrame with `magnitude`/`phase` columns.
Returns named Series with features: `rsEstimate`, `ohmicResistance`, `rctEstimate`, `cdlEstimate`, `warburgCoeffRandles`, `warburgSlopeNyquist`, `cpeAlphaEstimate`, `maxImpedance`, `minImpedance`, `zMagLow`, `zMagMid`, `zMagHigh`, `lowFreqMeanMag`, `midFreqMeanMag`, `highFreqMeanMag`, `magRatioLowHigh`, `maxPhaseAngle`, `peakPhase`, `peakPhaseFreq`, `phaseMin`, `phaseMax`, `meanPhase`, `nyquistArea`, `aucZMag`, `bodeSlope`, `realLinearTrend`, `imagLinearTrend`, `maxImaginary`, `imagPeakCount`, `zRealStd`, `zImagStd`
⚠ Apply row-wise: `df.apply(prcCplxEIS, axis=1)` — used internally by `ExtractFeaturesEIS`.
