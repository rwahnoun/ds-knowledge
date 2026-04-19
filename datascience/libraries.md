---
title: Python Libraries for Spectrophotometry & Biomarker Estimation
aliases:
  - spectroscopy libraries
  - python spectroscopy tools
tags:
  - topic/spectroscopy
  - topic/ml
  - type/reference
  - status/in-progress
date: 2026-04-19
status: in-progress
type: reference
author: Usense Healthcare
---

# Python Libraries for UV-Vis Spectrophotometry in Biomarker Estimation

Python ecosystem reference for UV-Vis spectrophotometry, covering preprocessing, calibration, signal processing, modeling, visualization, and data handling. Used across the Jimini device pipeline from raw photon counts to biomarker predictions. See [[signal-processing]] for usage context and [[calibration-transfer]] for domain-adaptation libraries.

---

## Data Calibration and Preprocessing

| Library | Purpose | URL |
|---------|---------|-----|
| **scipy.signal** | Filters, FFTs, convolution; Savitzky-Golay smoothing | https://docs.scipy.org/doc/scipy/reference/signal.html |
| **pybaselines** | Baseline correction (polynomial, asymmetric least squares) | https://github.com/anthony-wagner/pybaselines |
| **spectral** | Hyperspectral image processing, spectral calibration | https://github.com/spectralpython/spectral |
| **peakutils** | Peak finding and characterization in 1D signals | https://peakutils.readthedocs.io/en/latest/ |
| **scipy.interpolate** | Resampling spectral data to standard wavelengths | https://docs.scipy.org/doc/scipy/reference/interpolate.html |
| **scipy.optimize** | Calibration curve fitting (linear, nonlinear regression) | https://docs.scipy.org/doc/scipy/reference/optimize.html |
| **lmfit** | Least-squares minimization with robust parameter estimation | https://lmfit.github.io/lmfit-py/ |
| **pywt (PyWavelets)** | Wavelet transforms for spectral denoising | https://pywavelets.readthedocs.io/en/latest/ |
| **sklearn.preprocessing** | Normalization and scaling before modeling | https://scikit-learn.org/stable/modules/preprocessing.html |
| **statsmodels** | Robust regression for calibration curve fitting | https://www.statsmodels.org/stable/index.html |
| **pandas** | Spectral dataset handling with wavelength indexing | https://pandas.pydata.org/ |
| **numpy** | Array operations, linear algebra for spectroscopic data | https://numpy.org/ |

---

## Spectral Calibration Methods

| Library | Purpose | URL |
|---------|---------|-----|
| **scikit-learn** | PLS, PCR, PCA; multivariate calibration | https://scikit-learn.org/stable/ |
| **pyopls** | Orthogonal Partial Least Squares (OPLS) | https://pypi.org/project/pyopls/ |
| **sklearn.decomposition** | PCA, dimensionality reduction for spectral data | https://scikit-learn.org/stable/modules/decomposition.html |
| **scipy.linalg** | Linear algebra for multivariate calibration equations | https://docs.scipy.org/doc/scipy/reference/linalg.html |
| **xarray** | N-dimensional labeled arrays for complex spectral structures | https://docs.xarray.dev/en/stable/ |

> [!NOTE]
> For CORAL-based calibration transfer, use the `adapt` Python library: `from adapt.feature_based import CORAL`. See [[calibration-transfer]] for full implementation details.

---

## Signal Processing for UV-Vis Spectroscopy

| Library | Purpose | URL |
|---------|---------|-----|
| **scipy.signal** | Butterworth filters, Savitzky-Golay; core signal processing | https://docs.scipy.org/doc/scipy/reference/signal.html |
| **pyfftw** | Fast Fourier Transform for spectral feature analysis | https://hgomersall.github.io/PyFFTW/ |
| **scipy.signal.windows** | Hamming, Hanning, Blackman windows for FFT | https://docs.scipy.org/doc/scipy/reference/signal/windows.html |
| **pywavelets** | Wavelet transforms for frequency component analysis | https://pywavelets.readthedocs.io/en/latest/ |
| **pyresample** | Resampling with interpolation for wavelength alignment | https://github.com/pytroll/pyresample |

---

## Modeling and Regression for Spectrophotometry

| Library | Purpose | URL |
|---------|---------|-----|
| **scikit-learn** | Regression, classification, cross-validation | https://scikit-learn.org/stable/ |
| **xgboost** | Gradient boosting for high-dimensional spectral data | https://xgboost.readthedocs.io/en/latest/ |
| **lightgbm** | Fast gradient boosting for large spectroscopic datasets | https://lightgbm.readthedocs.io/en/latest/ |
| **tensorflow / keras** | CNNs and RNNs for spectral data modeling | https://www.tensorflow.org/ |
| **pytorch** | Advanced deep learning for spectral models | https://pytorch.org/ |
| **mlflow** | Experiment tracking and model deployment | https://mlflow.org/docs/latest/index.html |
| **optuna** | Hyperparameter optimization for spectroscopic models | https://optuna.readthedocs.io/en/stable/ |
| **statsmodels** | Linear/polynomial calibration curve fitting | https://www.statsmodels.org/stable/index.html |

See [[multi-task-modeling]] for multi-output model libraries and architectures.

---

## Data Visualization

| Library | Purpose | URL |
|---------|---------|-----|
| **matplotlib** | Core spectral visualization (line plots, heatmaps) | https://matplotlib.org/ |
| **seaborn** | Statistical visualization with matplotlib styling | https://seaborn.pydata.org/ |
| **plotly** | Interactive spectral data exploration | https://plotly.com/python/ |
| **bokeh** | Interactive web visualizations for spectroscopic datasets | https://docs.bokeh.org/en/latest/ |
| **yellowbrick** | ML diagnostic visualizations for spectroscopic models | https://www.scikit-yb.org/en/latest/ |

---

## Statistical Analysis

| Library | Purpose | URL |
|---------|---------|-----|
| **scipy.stats** | Hypothesis testing, distributions | https://docs.scipy.org/doc/scipy/reference/stats.html |
| **sklearn.metrics** | R², RMSE, MAE, AUC for model evaluation | https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics |
| **lmfit** | Advanced calibration curve fitting | https://lmfit.github.io/lmfit-py/ |
| **scipy.optimize.curve_fit** | Nonlinear least squares for spectrophotometric calibration | https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html |
| **scipy.spatial.distance** | Distance metrics for comparing spectra or clustering | https://docs.scipy.org/doc/scipy/reference/spatial.distance.html |

---

## Data Handling and Formats

| Library | Purpose | URL |
|---------|---------|-----|
| **pandas** | Spectral dataset handling, wavelength indexing | https://pandas.pydata.org/ |
| **numpy** | Array operations for spectroscopic data processing | https://numpy.org/ |
| **h5py** | HDF5 for large spectral datasets | https://www.h5py.org/ |
| **pyarrow** | Fast columnar serialization for spectral datasets | https://arrow.apache.org/docs/python/ |
| **scipy.io** | Load/save MATLAB .mat and other scientific formats | https://docs.scipy.org/doc/scipy/reference/io.html |
| **openpyxl** | Read/write Excel for sharing calibration results | https://openpyxl.readthedocs.io/en/stable/ |

---

## Sources

| Resource | URL |
|---------|-----|
| SciPy documentation | https://docs.scipy.org/ |
| scikit-learn documentation | https://scikit-learn.org/stable/ |
| adapt library (CORAL, domain adaptation) | https://adapt-python.github.io/adapt/ |

---

## Gaps

1. No single curated Python chemometrics library covers the full pipeline (SNV + EMSC + arPLS + PLS + CARS). The R `prospectr` and `mdatools` packages are more complete; Python equivalents are fragmented across scipy, sklearn, and smaller packages.
2. EMSC has no maintained Python package — the R `EMSC` package (Khliland) is more complete. A Python port or wrapper is needed.
3. Library availability for some entries (e.g., `pycalibrate`, `pychemviz`) is uncertain and should be verified before use.
