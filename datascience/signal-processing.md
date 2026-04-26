---
title: Signal Processing & Chemometrics for Spectral Urine Analysis
aliases:
  - DSP Pipeline
  - Spectral Preprocessing
  - signal processing
tags:
  - topic/spectroscopy
  - topic/chemometrics
  - topic/signal-processing
  - topic/ml
  - type/pipeline
  - status/complete
  - device/jimini
date: 2026-04-19

---

# Signal Processing & Chemometrics for Spectral Urine Analysis

Portable LED-based spectrophotometer (275–1078 nm) for urine analysis. Comprehensive pipeline reference: raw photon counts → preprocessing → feature extraction → chemometric/ML model → biomarker prediction. See [[normalization]] for scatter correction detail, [[matrix-correction]] for urine matrix effects, [[calibration-transfer]] for cross-device harmonization, and [[multi-task-modeling]] for multi-output model strategies.

---

## Summary

The optimal preprocessing pipeline for portable LED-based urine spectrophotometry combines **SNV** normalization (proven in direct LED urine spectroscopy) with **Savitzky-Golay smoothing/derivatives**, followed by **arPLS/airPLS baseline correction** when fluorescence drift is present. For 275–1078 nm, **PLS regression** remains the gold-standard for quantification, but **1D-CNN** and hybrid CNN-attention models consistently outperform PLS on larger datasets (>200 samples). For small clinical datasets (50–400 samples), ensemble approaches (SVR + RF) or PLS with wavelength selection (CARS, SPA) are more robust. Spectral data augmentation via WGAN or diffusion models is the key strategy to combat small-sample overfitting.

---

## Part 1: Pipeline Architecture

### Canonical Step Order

```
Stage 0 — Raw → Absorbance
  [dark_correction]       I_corrected = I_raw - I_dark
  [reference_correction]  T = (I_sample - I_dark) / (I_reference - I_dark)
  [absorbance_conversion] A = -log10(T)
  [quality_control]       flag saturation, spikes, negative absorbance

Stage 1 — Physical Preprocessing
  [baseline_correction]   arPLS/airPLS for UV; SNV for Vis-NIR
  [scatter_correction]    MSC / EMSC / SNV  → see [[normalization]]
  [derivative]            Savitzky-Golay 1st/2nd derivative
  [smoothing]             SG window=7–11, polynomial=2

Stage 2 — Biological Correction
  [osc]                   OSC/OPLS: 2–3 components for patient-level variation

Stage 3 — Statistical Processing
  [scaling]               StandardScaler / MinMax / RobustScaler
  [feature_selection]     CARS / SPA / VIP / SelectKBest
  [regressor]             PLS / SVR / RF / 1D-CNN
```

### Why This Order Is Critical

**Stage 0 first:** Dark current must be subtracted before all subsequent steps — electronic noise affects all wavelengths uniformly and is temperature-dependent. Quality control immediately after conversion catches saturation and cosmic rays while still identifiable as physical artefacts.

**Baseline before scatter correction:** Baseline correction removes *additive* effects (instrumental drift, fluorescence background). Scatter correction removes *multiplicative* effects (path-length variation, [[turbidity]] from cells). Reversing the order introduces cross-contamination artefacts.

**Derivatives after scatter correction:** Scatter correction stabilizes the signal foundation. Derivatives amplify noise — clean signal is essential.

**OSC after physical preprocessing:** OSC requires clean spectra to correctly identify variation orthogonal to Y. Physical artefacts in the input would be incorrectly removed as "patient variation".

**Scaling and feature selection last:** All spectral artefacts must be removed before standardization; feature selection on clean spectra avoids encoding instrument noise into the model.

### Reference sklearn Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import GridSearchCV

def create_urine_biomarker_pipeline(reference_spectrum=None, dark_spectrum=None):
    return Pipeline([
        # Stage 0
        ('dark_correction',       DarkCurrentCorrection(dark_spectrum=dark_spectrum)),
        ('reference_correction',  ReferenceCorrection(reference_spectrum=reference_spectrum)),
        ('absorbance_conversion', AbsorbanceConversion()),
        ('quality_control',       PhotonCountQualityControl()),
        # Stage 1
        ('baseline_correction',   ArPls(lam=1e5)),
        ('scatter_correction',    ExtendedMultiplicativeScatterCorrection()),
        ('derivative',            SecondDerivative()),
        ('smoothing',             SavitzkyGolay(window_length=11, polyorder=2)),
        # Stage 2
        ('osc',                   OrthogonalSignalCorrection(n_components=2)),
        # Stage 3
        ('scaling',               StandardScaler()),
        ('feature_selection',     SelectKBest(f_regression, k=100)),
        ('regressor',             PLSRegression(n_components=5)),
    ], memory='./cache')
```

---

## Part 2: Spectral Preprocessing Methods

### Standard Normal Variate (SNV) — Primary Scatter Correction

SNV is the **most validated preprocessing method for LED-based urine spectrophotometry**. In Kuenert et al. (2025) (n=401 urine samples, 340–850 nm), SNV reduced spectral inter-sample standard deviation by nearly **4 orders of magnitude** — from 1097.62 to 0.24 average SD per wavelength.

```
s̃ᵢ = (sᵢ - μ(s)) / σ(s)
```

**Why SNV works for urine:** Urine samples vary dramatically in [[turbidity]], color, and dilution between patients. SNV corrects both additive (baseline shifts) and multiplicative (path-length variation, turbidity) scatter effects on a per-spectrum basis without requiring a reference mean spectrum.

**Trade-off:** SNV can suppress genuine amplitude differences when analyte concentration affects overall spectrum intensity. In those cases, use SNV + detrending.

See [[normalization]] for full scaling method comparison.

### Multiplicative Scatter Correction (MSC) and Extended MSC (EMSC)

**MSC** corrects per-sample spectra by regressing against a mean reference spectrum:

```
xᵢₖ = cᵢ + bᵢ·x̄ₖ + eᵢₖ
xᵢₖ* = (xᵢₖ - ĉᵢ) / b̂ᵢ
```

**EMSC** extends MSC to include polynomial baseline terms, PCA-based interferent terms (water vapor, temperature), and explicit subtraction of known confounders (urobilin at ~490 nm). Achieved 97% specificity for Crohn's disease biomarkers in FTIR serum analysis.

**Recommendation:** Use **SNV** as default for Vis-NIR (400–1078 nm). Use **EMSC with polynomial correction** in the UV range (275–400 nm) where fluorescence background from urinary compounds ([[total-urinary-porphyrin|porphyrins]], [[nadh|NADH]]) is significant.

See [[matrix-correction]] for interferent subtraction strategies.

### Savitzky-Golay Filter and Derivatives

**Key parameters:**
- Window size (2M+1): typically 5–25 points; larger = more smoothing but peak broadening
- Polynomial order: 2nd or 3rd recommended
- Derivative order: 0 = smoothing only; 1st = removes constant baseline; 2nd = removes linear baseline, enhances peak resolution

**SG 2nd derivatives** are particularly valuable for urine spectroscopy:
1. Eliminate baseline offset and slope (critical for varying urine dilution)
2. Reveal overlapping peaks (discriminating [[creatinin|creatinine]] vs. [[urea]] NIR bands)
3. Combined with SNV provide excellent performance in NIRS biofluid studies

For NIR [[urea]]/[[creatinin|creatinine]] prediction, SG 2nd derivative typically reduces RMSECV by 15–30% vs. raw spectra.

**Fractional-order SG derivatives (FOSGD):** Emerging technique using order α ∈ (0,2) for tuning resolution-noise tradeoff. Showed +17% correlation improvement for chlorophyll estimation vs. integer derivatives.

### Baseline Correction: ArPLS, AirPLS, and Variants

For the UV range (275–380 nm) where urine autofluorescence is strongest, **iterative weighted least squares** methods are essential.

| Method | Key Feature | Recommendation |
|--------|------------|----------------|
| **airPLS** (Zhang 2010) | Most widely used; one hyperparameter λ (10²–10⁷) | Good baseline |
| **arPLS** (Baek 2015) | More robust than airPLS in moderate-SNR conditions | Preferred for UV-Vis |
| **IairPLS** | Sigmoid transition at peak boundaries; RMSE 0.0187 vs. 0.0531 (airPLS) | For sharp peaks |
| **BrPLS** (Bayesian) | State-of-the-art; R²=0.9990 vs. 0.9985 (arPLS); no manual threshold | UV fluorescence correction |

**Recommended for UV range (275–400 nm):**
1. arPLS or IairPLS (λ = 10⁴–10⁵) for LED-excited fluorescence baseline
2. Verify baseline doesn't over-smooth near UV absorption peaks (280 nm aromatic amino acids, 340 nm [[nadh|NADH]], 400–450 nm urobilinogen/bilirubin)

### Orthogonal Signal Correction (OSC) and OPLS

**OSC** removes spectral variation **orthogonal to the Y-variable** before modeling — different from SNV/MSC which correct physical scatter. OSC removes any latent X structure that does not correlate with Y.

**Direct OSC (DOSC) Algorithm:**
1. Project Y into spectral space: Ŷ = X(XᵀX)⁻¹XᵀY
2. Isolate orthogonal spectral space: Z = (I - ŶŶ†)X
3. PCA/SVD of Z → extract noise subspace U
4. Remove: X_corrected = X - UPᵀ

**Impact:** Transformed R² from 0.50 to 0.987 in rice bran oil analysis by eliminating humidity-induced spectral variation.

**OPLS** integrates OSC directly into the PLS algorithm. Cleaner loading plots show only chemically relevant variation. Recommended for clinical reporting where regulatory bodies require interpretable models.

> [!CAUTION]
> OSC can over-correct. Use **2–4 OSC components** maximum. Always validate on a held-out test set.

### Complete Recommended Preprocessing Pipeline

```
Raw spectrum (275–1078 nm)
    ↓
[1] Outlier/spike detection (arPLS residual Z-score > 4σ → flag sample)
    ↓
[2a] UV range (275–400 nm): arPLS/IairPLS baseline correction (λ=10⁴)
[2b] Vis-NIR range (400–1078 nm): SNV
    ↓
[3] Savitzky-Golay smoothing: window=7–11, polynomial=2nd order
    OR SG 1st/2nd derivative if baseline issues persist
    ↓
[4] [Optional] OSC/OPLS: 2–3 components if patient-level variation is large
    ↓
[5] Mean centering (mandatory for PLS, optional for DL models)
    ↓
Feature extraction / modeling
```

**Simplified pipeline (validated Kuenert 2025, AUC 0.921–0.981):**
```
Raw → SNV → correlation-based wavelength selection → logistic regression
```

---

## Part 3: Feature Extraction and Wavelength Selection

### Principal Component Analysis (PCA)

PCA is the standard exploratory step to:
- Identify spectral outliers (Hotelling T² and Q-residuals)
- Visualize sample clustering (healthy vs. pathological urine)
- Determine effective dimensionality before calibration models

For urine spectra: typically 3–8 PCs explain >95% variance. The first PC often captures dilution (color depth), PC2–3 capture specific compound signatures.

### Variable Importance in Projection (VIP) Scores

VIP scores from PLS quantify how much each wavelength contributes to Y-variance across all PLS components. Standard threshold: **VIP > 1.0** selects wavelengths above average importance. Tends to select wide regions rather than specific peaks.

### Competitive Adaptive Reweighted Sampling (CARS)

CARS iteratively removes wavelengths with low PLS regression coefficients:
1. Exponential decay removes a fraction of high-coefficient wavelengths each iteration
2. Competitive penalty reweights survivors
3. Monte Carlo cross-validation selects the optimal subset

Performance: CARS + PLSR achieved R²=0.927 for apple Brix. Particularly valuable for 900–1100 nm NIR where water overtones dominate but [[creatinin|creatinine]]/[[urea]] have weak bands.

**Combined approach: CARS-SPA** — SPA removes collinear wavelengths from the CARS-selected set. Outperforms either method alone.

### Successive Projections Algorithm (SPA)

SPA selects wavelengths by minimizing collinearity. Produces small, non-redundant sets (5–15 wavelengths) ideal for miniature LED systems. For Jimini: reduces ~800 wavelength channels to 5–20 key wavelengths that can guide future LED selection or filter placement.

### Correlation-Based Wavelength Selection

1. Compute Pearson/Kendall-τ correlation between each wavelength channel and the clinical reference value
2. Plot correlation curves across the spectrum
3. Select wavelengths at significant correlation peaks (p < 0.05) aligned with known absorption maxima

**Results for urine analytes** (Kuenert 2025):

| Analyte | Correlating wavelengths | Notes |
|---------|------------------------|-------|
| Bilirubin | 344, 387, 426 nm | Known absorption max ~440 nm |
| Hemoglobin/erythrocytes | ~414 nm, 540/580 nm | Soret + Q-bands |
| Urobilinogen | ~490 nm | — |
| Protein | Multiple (broad) | Diverse protein types |
| [[glucose\|Glucose]], albumin | **None** in 340–850 nm | Confirmed absent in Vis range |

**Key insight:** The UV extension to 275 nm is critical. Below 340 nm: aromatic amino acids ([[tryptophan]] 280 nm, tyrosine 274 nm), nucleobases ~260 nm, [[uric-acid|uric acid]] ~290 nm, nitrite 354 nm.

See [[datascience/spectroscopy-biomarkers]] for full chromophore reference.

---

## Part 4: Chemometric Modeling

### PLS Regression — Gold Standard

**Partial Least Squares (PLS)** simultaneously decomposes X (spectra) and Y (analyte concentrations) into latent variables maximizing their covariance. Handles collinear wavelength variables and more predictors than samples.

**Key hyperparameter:** Number of latent variables — selected by LOO or 10-fold CV minimizing RMSECV.

**Performance for urine NIR:**

| Analyte | R² range | RMSEP |
|---------|----------|-------|
| [[creatinin\|Creatinine]] | 0.85–0.95 | 0.5–1.5 mM |
| [[urea\|Urea]] | 0.80–0.90 | — |
| Total protein | 0.75–0.85 | — |

When PLS is sufficient: for small datasets (n < 200), PLS with proper cross-validation is typically more robust than ML methods which overfit.

For multi-target joint prediction, see [[multi-task-modeling]] (PLS2, SO-PLS).

### OPLS — Interpretable Regression

**OPLS** separates PLS into a predictive component (1 LV per Y) and orthogonal components (removing Y-unrelated variation). Recommended for clinical reporting where regulatory bodies require interpretable models.

### Machine Learning: SVR, Random Forest, XGBoost

| Model | Notes |
|-------|-------|
| **SVR (RBF kernel)** | Consistently outperforms PLS for nonlinear relationships; n = 50–300 with proper regularization; use wavelength selection first |
| **Random Forest** | Built-in variable importance (Gini); robust to outliers; n ≥ 100 |
| **XGBoost** | Usually outperforms RF at n ≥ 150; hyperparameter-sensitive |

**Published comparison (NIR, food/agri):**
- CNN > SVR ≥ RF > PLS on datasets n > 300
- SVR ≈ CNN on datasets n < 150

### PCR (Principal Components Regression)

PCR applies PCA then regresses Y on scores. Consistently **underperforms PLS** because PCA compression ignores Y. Only useful when interpretability of PCA loadings is required.

---

## Part 5: Deep Learning on Spectroscopic Data

### 1D-Convolutional Neural Networks — State of the Art

1D-CNNs apply convolutional filters along the wavelength dimension, learning local spectral patterns without prior knowledge of peak positions.

**Standard architecture:**
```python
model = Sequential([
    Conv1D(32, 11, padding='same', activation='relu', input_shape=(n_wavelengths, 1)),
    BatchNormalization(),
    Conv1D(64, 7, padding='same', activation='relu'),
    BatchNormalization(),
    MaxPooling1D(2),
    Conv1D(128, 3, padding='same', activation='relu'),
    BatchNormalization(),
    GlobalAveragePooling1D(),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(1)
])
```

**Minimal 1D-CNN for small spectral datasets (150–300 samples):**
```python
model = Sequential([
    Conv1D(32, 11, padding='same', activation='relu', input_shape=(n_wavelengths, 1)),
    BatchNormalization(),
    Conv1D(16, 7, padding='same', activation='relu'),
    GlobalAveragePooling1D(),
    Dense(32, activation='relu'),
    Dropout(0.4),
    Dense(1)
])
```

**Dataset size thresholds:**

| N | Recommendation |
|---|---|
| n < 100 | 1D-CNN typically underperforms PLS/SVR |
| n = 100–300 | Competitive with careful regularization + augmentation |
| n > 500 | 1D-CNN consistently best |

For multi-output 1D-CNN across multiple biomarkers, see [[multi-task-modeling]].

### Transformer Models for Spectroscopy

**SpectraTr (Fu et al. 2022):** Transformer encoder for 1D spectral data; multi-head self-attention learns long-range spectral dependencies. Superior for identifying overlapping peaks.

**Key consideration:** Transformers require n > 1000 typically. For n = 150–500, **1D-CNN is preferred**; transformers need larger datasets or transfer learning.

For physics-informed variants, see [[physics-grounded-ml]].

### Transfer Learning and Pre-training

**Cumulative learning (Bittremieux et al. 2020, *Nature Comm.*):** Pre-training on large auxiliary spectral datasets reduces required dataset size by 5–10× for acceptable CNN accuracy.

**Practical approaches:**
1. Pre-train on large public spectral dataset (Kew Garden NIR, LUCAS soil NIR) → fine-tune on urine
2. Domain adaptation: pre-train on water/aqueous solution spectra → fine-tune
3. Pre-train on blood serum spectra (compositionally similar) → fine-tune

### Autoencoders for Feature Extraction and Denoising

**Denoising Autoencoder (DAE):** Pre-processing before PLSR significantly reduces noise; encoder bottleneck features (16–32 dims) can be used directly as input to PLS/SVR.

**SpecFuseNet (Kabiso & Ko 2025, *Sci. Reports*):** Attention-enhanced residual autoencoder; 97.8% NIR grain classification accuracy. Features from encoder outperformed raw spectra + PCA.

**VAE for denoising + generation:** Encodes spectra to probabilistic latent space; can generate synthetic spectra for augmentation.

---

## Part 6: Data Augmentation for Small Spectral Datasets

### Why Augmentation Is Critical

| Method | Minimum N for reliable use |
|--------|--------------------------|
| PLS | ~30 samples per analyte range band |
| 1D-CNN | ~200 (without augmentation) |
| 1D-CNN + augmentation | ~50–100 real + augmented to 500–1000 |

### Traditional Augmentation

- **Noise injection:** Gaussian noise (σ = 0.1–0.5% of signal) — 20–30% improvement for DL on small datasets
- **Spectral shifting:** ±1–3 channels (instrument calibration variations)
- **Intensity scaling:** Multiply by scalar ∈ [0.9, 1.1] (concentration variation)
- **Baseline perturbation:** Random low-frequency polynomial (baseline drift)

**Limitation:** Don't generate genuinely new spectral features — only transformations of existing spectra.

### GAN-Based Augmentation

**WGAN-GP for FTIR spectral augmentation (Erzina et al. 2023, *Analyst*):**
- Generated spectra improved downstream classification accuracy by 8–15%
- Indistinguishable from real spectra in PCA space
- WGAN-GP (gradient penalty) provides more stable training than vanilla GAN

**Recommendation:** Start with WGAN-GP (well-validated for spectral data). If dataset grows to n > 200, consider diffusion models.

### Diffusion Model Augmentation (State-of-the-Art 2025)

Produces highest quality synthetic spectra; significantly outperforms GANs for inter-sample spectral variability. Main limitation: training requires significant compute.

### Practical Augmentation for LED Urine Spectroscopy

```python
def augment_spectrum(spectrum, label, n_augmented=5):
    augmented = []
    for _ in range(n_augmented):
        s = spectrum.copy()
        # 1. Gaussian noise (detector noise)
        noise_level = 0.002 * np.std(s)
        s += np.random.normal(0, noise_level, len(s))
        # 2. Multiplicative scaling (dilution variation)
        s *= np.random.uniform(0.95, 1.05)
        # 3. Baseline polynomial perturbation (LED drift)
        x = np.linspace(-1, 1, len(s))
        s += np.random.normal(0, 0.001) * x + np.random.normal(0, 0.0005) * x**2
        # 4. Spectral shift (±2 channels, wavelength calibration uncertainty)
        s = np.roll(s, np.random.randint(-2, 3))
        augmented.append((s, label))
    return augmented
```

---

## Part 7: Cross-Validation Strategies

### Key Pitfalls

The main risk is **overly optimistic performance estimation** from:
1. **Data leakage:** Preprocessing (SNV, PCA) computed on entire dataset including test set
2. **Correlated samples:** Multiple measurements per patient → random splits leak same-patient data
3. **Improper CV:** Feature selection on full dataset before CV

**Correct procedure:**
```
For each CV fold:
    1. Fit preprocessing parameters (SNV, PCA, CARS) on TRAINING set only
    2. Apply to test set using training parameters
    3. Evaluate
```

### Recommended CV Strategies

| Strategy | Use Case |
|----------|---------|
| **Leave-One-Patient-Out (LOPO)** | Most clinically realistic; holds out ALL samples from one patient |
| **Monte Carlo CV (MCCV)** | 70–80% train / 20–30% test, 100–1000 repeats; best for selecting PLS components |
| **Venetian Blinds** | Every K-th sample to test; preferred when measurement order correlates with analyte values |
| **Representative Splitting (RSCV)** | Kennard-Stone algorithm ensures train/test span spectral space; recommended for n < 200 |
| **5-Fold with Patient Stratification** | Stratify by patient; compute correction term = mean(inner_perf − outer_perf) |

### Systematic Validation Checklist (Ezenarro 2025)

- [ ] Preprocessing computed on training set only, applied to test
- [ ] Wavelength/feature selection within cross-validation loop
- [ ] Number of PLS components selected by MCCV, not LOO-CV
- [ ] Separate validation set held out entirely (never used for tuning)
- [ ] Report RMSECV and RMSEP separately (RMSECV ≈ RMSEP = no overfitting)
- [ ] RMSEP/RMSECV ratio < 1.3
- [ ] External validation with n ≥ 20 independent test samples

---

## Part 8: Comparison Studies — Chemometrics vs. Deep Learning

### Key Benchmark (Zhang et al. 2022, Sensors)

| Method | Dataset Size | Typical R² | Notes |
|--------|-------------|-----------|-------|
| PCR | Any | Worst | Baseline only |
| PLS | n ≥ 30 | 0.80–0.95 | Gold standard |
| PLS + OSC | n ≥ 50 | 0.85–0.97 | Matrix effects |
| SVR (RBF) | n ≥ 50 | 0.85–0.96 | Better nonlinear |
| RF | n ≥ 100 | 0.82–0.95 | Feature importance |
| 1D-CNN | n ≥ 200 | 0.87–0.98 | Needs augmentation |
| Transformer | n ≥ 500 | 0.89–0.99 | Interpretable attention |

**Key conclusion:** "For typical small NIR calibration datasets (30–200 samples), PLS with proper cross-validation remains competitive with or superior to deep learning methods."

### UV-Vis Urine Analysis Benchmarks

| Study | Modality | n | Analyte | Best Method | R²/AUC |
|-------|----------|---|---------|------------|--------|
| Kuenert 2025 | LED Vis (340–850 nm) | 401 | Bilirubin (binary) | LRRE | AUC=0.921 |
| Kuenert 2025 | LED Vis | 401 | Specific gravity | LRRE | AUC=0.890 |
| Kuenert 2025 | LED Vis | 401 | Erythrocytes | LRRE | AUC=0.908 |
| SpectraPhone 2026 | Vis (400–750 nm) | — | Hematuria ([[red-blood-cells\|RBC]]) | PLS + 2nd deriv. | R²=0.9913 |
| Suzuki 2020 | NIR (900–1700 nm) | Small | [[creatinin\|Creatinine]]/[[urea]] | PLS | R²≈0.85 |

**Critical observations for 275–1078 nm range:**
- UV (275–400 nm): Best for UV chromophores (aromatic aa, bilirubin, urobilinogen, nucleotides, nitrite)
- Vis (400–700 nm): Hemoglobin, erythrocytes, urobilin, bilirubin color bands
- NIR (700–1078 nm): Water overtones dominate; weak C-H/N-H/O-H overtones of [[urea]], [[creatinin|creatinine]], protein

---

## Part 9: Practical Implementation

### Recommended Software Stack

```python
import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, LeaveOneGroupOut
from scipy.signal import savgol_filter  # Savitzky-Golay

import torch
import torch.nn as nn  # 1D-CNN
```

**R (classical chemometrics):**
```r
library(pls)       # PLS
library(prospectr) # SNV, MSC, SG, CARS, Kennard-Stone
library(mdatools)  # OPLS, OSC, validation tools
library(EMSC)      # Extended MSC
```

See [[libraries]] for the full curated library reference.

### Minimum Viable Pipeline for 275–1078 nm LED Urine Spectroscopy

**Stage 1 — Baseline (< 1 week):**
1. SNV preprocessing on full spectrum
2. Savitzky-Golay smoothing (window=9, poly=2, derivative=0)
3. PLS regression (leave-one-patient-out CV; MCCV for component selection)
4. Evaluate: RMSECV, RMSEP, R², correlation plots

**Stage 2 — Optimized (2–4 weeks):**
1. Separate preprocessing: arPLS for UV (275–400 nm), SNV for Vis-NIR
2. CARS or SPA wavelength selection within CV loop
3. SVR and RF comparison against PLS

**Stage 3 — Advanced (ongoing):**
1. 1D-CNN with BatchNorm + Dropout + data augmentation
2. WGAN for generating synthetic spectra to balance classes
3. Stacking ensemble (PLS + SVR + CNN)
4. Patient-level random effects model (mixed model logistic regression)
5. OPLS for interpretable single-analyte models
6. Multi-task models for joint prediction → [[multi-task-modeling]]

### Analyte-Specific Preprocessing Notes

| Analyte | Expected UV-Vis Peaks | Key Preprocessing |
|---------|----------------------|------------------|
| Bilirubin | 344, 387, 426 nm | SNV; EMSC if icteric matrix |
| Hemoglobin/[[red-blood-cells\|RBC]] | 414, 540, 576, 630 nm | SNV sufficient; Beer-Lambert holds well |
| Urobilinogen | ~490 nm | SNV; careful baseline at UV edge |
| [[creatinin\|Creatinine]] | No strong Vis abs.; 230 nm UV | UV: arPLS + SNV; SG 2nd derivative |
| [[urea\|Urea]] | No Vis abs.; 200 nm deep UV | NIR overtones 900–1000 nm; SG 2nd derivative |
| Protein | 280 nm (aromatic), broad Vis | SNV + SG derivative; VIP selection |
| Nitrite | 354 nm (UV) | arPLS baseline crucial; near LED noise floor |
| [[glucose\|Glucose]] | No Vis/UV abs. in aqueous | Essentially invisible 275–1078 nm |
| pH | Indirect (multiple chromophores) | PLS on full spectrum; AUC > 0.85 |
| Specific gravity | Refractive/multi-compound | PLS on full spectrum; AUC > 0.89 |

See [[datascience/spectroscopy-biomarkers]] for full chromophore reference.

---

## Sources

| Source | URL | Relevance |
|--------|-----|-----------|
| Kuenert et al. 2025, Sci Reports | https://www.nature.com/articles/s41598-025-92802-2 | LED 340–850 nm, 401 urine samples, SNV |
| Yan et al. 2025, PMC iScience | https://pmc.ncbi.nlm.nih.gov/articles/PMC12221524/ | Comprehensive preprocessing review |
| Zhang et al. 2022, Sensors | https://www.mdpi.com/1424-8220/22/24/9764 | ML-NIR comparison review |
| arxiv 2301.10746 — 1D-CNN vs chemometrics | https://arxiv.org/pdf/2301.10746 | Head-to-head 1D-CNN comparison |
| Erzina et al. 2023, Analyst | https://pubs.rsc.org/en/content/articlehtml/2023/an/d3an00669g | WGAN for FTIR augmentation |
| Bittremieux et al. 2020, Nature Comm | https://www.nature.com/articles/s41467-020-19354-z | Transfer learning for small spectral datasets |
| Tang et al. 2014, Analyst | https://pubs.rsc.org/en/content/articlepdf/2014/an/c4an00837e | CARS-SPA wavelength selection |
| Ezenarro 2025, J. Chemometrics | https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/cem.70036 | Systematic CV review |
| Afseth & Kohler 2012, Chemom. Intell. Lab. Syst. | — | EMSC tutorial |
| Wold et al. 1998, Chemom. Intell. Lab. Syst. | — | OSC original |
| Baek et al. 2015, Analyst | DOI:10.1039/c4an01061b | arPLS |
| Zhang et al. 2010, Analyst | DOI:10.1039/b922045c | airPLS |
| Kabiso & Ko 2025, Sci Reports | https://pmc.ncbi.nlm.nih.gov/articles/PMC12460850/ | Attention autoencoder for NIR |
| Savitzky & Golay 1964, Anal. Chem. | — | SG filter original paper |
| Barnes et al. 1989, Appl. Spectrosc. | — | SNV original paper |

---

## Gaps

1. **LED-specific noise not characterized:** Most preprocessing literature is for bench-top spectrometers. LED-specific noise: thermal drift of LED emission wavelength (~0.1–0.3 nm/°C); intensity fluctuation between LEDs (pulsed vs. continuous); narrow-band gaps if LED coverage is incomplete between 275–1078 nm. Recommendation: characterize noise statistics empirically and use Kalman filter for real-time LED drift correction.

2. **No published 275–400 nm preprocessing for urine:** All current LED urine studies start at ≥340 nm. Key unknowns: fluorescence contribution from urinary [[total-urinary-porphyrin|porphyrins]] and pyridines at 275–320 nm; whether arPLS handles this adequately. Next step: acquire urine spectra at 275–400 nm and compare arPLS vs. EMSC vs. polynomial correction.

3. **Multi-patient temporal stability:** The Kuenert 2025 study used frozen-thawed samples. Real-time catheter urine may show temperature-dependent spectral shifts, bacterial metabolism changes, and foam/turbidity variations in continuous flow.

4. **Quantification vs. classification:** Most recent studies focus on binary classification. Quantitative prediction requires concentration-balanced training sets and RMSEP below clinical decision threshold: [[creatinin|creatinine]] RMSEP < 0.5 mM; total protein RMSEP < 30 mg/24h; specific gravity RMSEP < 0.002 SG units.

5. **Comparison with strip-based systems:** No published comparison between pure spectroscopic methods and semi-quantitative strips for the 275–1078 nm range.
