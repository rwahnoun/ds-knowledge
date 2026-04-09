# learn.explain
`d:\code\ds-learn\src\learn\explain.py` | `from learn.explain import ExploreShap`

SHAP-based model explainability for spectral data. Wraps SHAP explainers to provide wavelength importance profiles, contiguous band extraction, per-sample explanations, and publication-ready plots for spectral classification models.

## Index

| Name | Type | Purpose |
|------|------|---------|
| `ExploreShap` | class | SHAP explainer with spectral-aware getters and plots |

## Reference

### `ExploreShap(mdl, X: DataFrame, y: Series = None, explainerType: str = "tree")`
Computes SHAP values on init and exposes getters and plot methods for spectral analysis.
- `mdl`: Fitted model. Tree-based models use TreeSHAP (exact, fast); others use KernelSHAP (slow).
- `X`: Feature matrix (samples x wavelengths). Column names must be castable to float (wavelength values).
- `y`: True labels. Optional, required only for `mkPltSpectraComparison`.
- `explainerType`: `"tree"` (default) or `"kernel"`.

**Attributes** (available after init):
- `sv`: Raw `shap.Explanation` object
- `wavelengths`: numpy array of wavelength values (float)
- `meanAbsShap`: mean |SHAP| per wavelength (numpy array)
- `meanShap`: mean signed SHAP per wavelength (numpy array)

### Getters

#### `getShapValues() → DataFrame`
Raw SHAP values as DataFrame with same shape and columns as input X.

#### `getImportance() → Series`
Mean |SHAP| per wavelength. Series indexed by wavelength (float).

#### `getBands(percentile: int = 75) → DataFrame`
Contiguous wavelength bands above the given importance percentile.
- `percentile`: Threshold as percentile of mean |SHAP| (default 75).
- Returns DataFrame with columns: `start`, `end`, `width`, `peakImportance`, `meanShap`, `direction`.
- `direction`: `"positive"` (pushes toward positive class) or `"negative"`.
- Sorted by `peakImportance` descending.

#### `getTopWavelengths(n: int = 20) → Series`
Top N wavelengths ranked by mean |SHAP|. Series sorted descending, indexed by wavelength.

### Plots

All plot methods accept `ax: Axes = None`. When `ax` is None, a new figure is created and shown. When `ax` is provided, the plot is drawn on the given axes without calling `plt.show()`.

#### `mkPltBar(maxDisplay: int = 20, ax: Axes = None)`
Bar plot of mean |SHAP| per wavelength (top N).

#### `mkPltBeeswarm(maxDisplay: int = 20, ax: Axes = None)`
Beeswarm plot — one dot per sample per wavelength. X-axis = SHAP value, color = feature value (red = high absorbance, blue = low).

#### `mkPltImportanceSpectrum(percentile: int = 75, ax: Axes = None) → Axes`
Mean |SHAP| plotted as a continuous spectrum over the wavelength axis, with contiguous regions above the threshold highlighted in red. This is the key biologist-facing plot.

#### `mkPltWaterfall(idx: int = 0, maxDisplay: int = 15, ax: Axes = None)`
Waterfall plot for a single sample. Shows how each wavelength pushes the prediction from base value to final output.

#### `mkPltForce(idx: int = 0, ax: Axes = None, figsize: tuple = (18, 3))`
Compact horizontal force plot for a single sample. Red = pushes toward positive class, blue = toward negative.

#### `mkPltHeatmap(maxDisplay: int = 20, ax: Axes = None)`
Heatmap of SHAP values. Rows = samples, columns = top wavelengths.

#### `mkPltDependence(n: int = 4, ax: list[Axes] = None) → array[Axes]`
Scatter plots of feature value vs SHAP value for the top N wavelengths, with auto-detected interaction coloring.
- `ax`: List of axes (one per wavelength). Default creates a grid.

#### `mkPltSpectraComparison(labels: dict = None, ax: tuple[Axes, Axes] = None) → tuple[Axes, Axes]`
Two-panel plot: top = mean spectra per class, bottom = SHAP importance spectrum.
- `labels`: Dict mapping class values to display names (default `{0: "Negative", 1: "Positive"}`).
- `ax`: Tuple of two axes `(axSpectra, axShap)`.

⚠ Requires `y` to be passed at init.

## Example

```python
from sklearn.ensemble import GradientBoostingClassifier
from learn.explain import ExploreShap

mdl = GradientBoostingClassifier(n_estimators=200, max_depth=4).fit(xTr, yTr)

es = ExploreShap(mdl, xTe, yTe)

# Key outputs
bands = es.getBands(percentile=75)          # DataFrame of spectral bands
importance = es.getImportance()              # Series: wavelength → mean |SHAP|

# Plots
es.mkPltImportanceSpectrum()                 # Wavelength importance profile
es.mkPltBeeswarm()                           # Per-sample beeswarm
es.mkPltSpectraComparison(labels={0: "WBC < 10k", 1: "WBC ≥ 10k"})

# Embed in custom figure
fig, axes = plt.subplots(1, 2, figsize=(16, 4))
es.mkPltImportanceSpectrum(ax=axes[0])
es.mkPltBar(ax=axes[1])
```
