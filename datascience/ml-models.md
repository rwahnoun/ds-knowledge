---
title: ML Models for Jimini Urine Spectroscopy
aliases:
  - ml models
  - spectral models
  - model selection
  - data augmentation
  - validation strategy
tags:
  - topic/ml
  - topic/chemometrics
  - topic/spectroscopy
  - type/reference
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# ML Models for Jimini Urine Spectroscopy

Model selection, training, augmentation, and validation strategies for Jimini multi-LED spectrophotometer + EIS biomarker prediction.
Audience: data scientist / ML engineer building biomarker prediction models.
See also: [[signal-processing]] [[optical-signatures]] [[biomarker-panel]] [[literature]]

> [!IMPORTANT]
> PLS regression dominates quantitative spectroscopic prediction and remains competitive with deep learning for datasets under ~200 samples. 1D-CNN outperforms PLS above n ≈ 300–500. SNV + Savitzky-Golay derivatives is the proven preprocessing baseline.

---

## 1. Model Selection by Dataset Size

| n (samples) | Recommended model | Rationale |
|---|---|---|
| < 100 | **PLS** with MCCV, SNV+SG+CARS | Robust; sufficient for linear spectral relationships |
| 100–300 | **SVR (RBF kernel)** or RF + PLS ensemble | SVR handles nonlinearities; augment to 500+ for CNN |
| 300–500 | **1D-CNN** with BatchNorm + Dropout | Outperforms classical methods consistently |
| > 500 | **1D-CNN** or Transformer (emerging) | SpectraTr, SpectraViT show promise |

---

## 2. PLS Regression — Gold Standard for Quantitative Spectroscopy

**Why PLS works:** Handles collinear spectral features, extracts latent variables maximising covariance between X (spectra) and Y (concentrations), robust to matrix interference.

### Best Results in Urine Spectroscopy

| Study | Biomarker | Preprocessing | R² | RMSE |
|---|---|---|---|---|
| SpectraPhone 2026 | Hematuria (RBC) | 2nd derivative | **0.9913** | 61.6 RBC/µL |
| SpectraPhone 2026 | Albumin (reagent-free) | SNV | **0.9981** | 11.85 mg/dL |
| Spectrochip 2024 | 12 parameters | Calibration curve | > 0.95 | — |
| Shaw et al. 1996 | Protein, creatinine, urea | NIR PLS | High | Clinical range |

**Hyperparameter selection:** Number of latent variables (LVs) selected by Monte Carlo Cross-Validation (MCCV) — less biased than LOO-CV for small datasets.

---

## 3. Logistic Regression with Random Effects (LRRE) — Binary Classification

For binary presence/absence classification with repeated measures per patient, LRRE adds a random intercept per subject to handle within-patient correlation.

| Biomarker | AUC | Study |
|---|---|---|
| Bilirubin | **0.921** | Kuenert 2025 |
| Erythrocytes | ~0.88 | Kuenert 2025 |
| Specific gravity | ~0.89 | Kuenert 2025 |
| Protein | Good | Kuenert 2025 |

**When to use:** Binary detection in clinical settings; patient-level repeated measurements (random intercept handles within-patient correlation).

---

## 4. 1D-CNN for Spectral Data

The dominant deep learning architecture for 1D spectral regression and classification.

```python
# Minimal architecture validated for small spectral datasets (150–300 samples)
model = Sequential([
    Conv1D(32, kernel_size=11, padding='same', activation='relu',
           input_shape=(n_wavelengths, 1)),
    BatchNormalization(),
    Conv1D(64, kernel_size=5, padding='same', activation='relu'),
    BatchNormalization(),
    MaxPool1D(2),
    Conv1D(128, kernel_size=3, padding='same', activation='relu'),
    GlobalAveragePooling1D(),
    Dense(64, activation='relu'),
    Dropout(0.4),
    Dense(1)  # regression output
])
```

**Benchmarks:** 1D-CNN outperformed PLS, SVR, RF, MLP on 5 public spectral datasets; average R² improvement over PLS = +0.05–0.12 when n > 500. For n < 200, PLS/SVR remain competitive or superior.

---

## 5. PARAFAC — Multi-LED Fluorescence Decomposition

When using multiple excitation wavelengths (Jimini's 4 LEDs) with broadband detection, the data forms a **partial Excitation-Emission Matrix (EEM)** tensor. PARAFAC decomposes the three-way data (samples × excitation × emission) into independent fluorophore components.

This enables simultaneous quantification of tryptophan, NADH, riboflavin, and porphyrins from Jimini's native multi-LED fluorescence data without overlap artefacts.

**Direct application:** Jimini 4 LEDs (275, 365, 405, 455 nm) × C12 broadband detection (321–870 nm) = partial EEM. PARAFAC separates:
- Tryptophan: Ex 275→Em 330–360 nm
- NADH: Ex 365→Em 440–470 nm
- Riboflavin: Ex 365/455→Em 520 nm
- Porphyrins: Ex 405→Em 620–640 nm

---

## 6. Stacking / Ensemble

For robust performance across dataset sizes:

```
PLS predictions + SVR predictions + 1D-CNN predictions
    → Meta-learner (Ridge regression or simple averaging)
    → Final prediction
```

Ensemble approaches consistently reduce variance and improve generalisation in spectral chemometrics.

---

## 7. Data Augmentation for Small Datasets

Clinical urine datasets are typically small (50–500 samples) with class imbalance (pathological cases rare).

### Traditional Augmentation

```python
def augment_spectrum(spectrum, n_augmented=5):
    augmented = []
    for _ in range(n_augmented):
        s = spectrum.copy()
        s += np.random.normal(0, 0.002 * np.std(s), len(s))      # detector noise
        s *= np.random.uniform(0.95, 1.05)                        # dilution variation
        x = np.linspace(-1, 1, len(s))
        s += np.random.normal(0, 0.001) * x + \
             np.random.normal(0, 0.0005) * x**2                   # LED drift
        s = np.roll(s, np.random.randint(-2, 3))                  # wavelength shift
        augmented.append(s)
    return augmented
```

### WGAN for Spectral Data

Wasserstein GAN with gradient penalty (WGAN-GP) generates realistic synthetic spectra. Validated on cancer liquid biopsy FTIR — improved downstream classification accuracy by 8–15%. Generated spectra indistinguishable from real in PCA space.

### Diffusion Models (State-of-the-Art, 2025)

Diffusion probabilistic models produce highest-quality synthetic spectra, outperforming GANs for inter-sample spectral variability. Main limitation: compute-intensive. Consider when dataset exceeds n ≈ 200.

### Transfer Learning / Cumulative Learning

Pre-train 1D-CNN on large auxiliary spectral dataset (e.g., Kew Garden NIR, LUCAS soil) → fine-tune on urine. Reduces required dataset size by 5–10×.

---

## 8. Validation Protocol

### Critical Pitfalls

| Pitfall | How to avoid |
|---|---|
| **Data leakage from preprocessing** | Fit SNV/PCA/wavelength selection on TRAINING set only |
| **Same-patient samples in train+test** | Use Leave-One-Patient-Out (LOPO) or patient-stratified folds |
| **Optimistic RMSECV** | Use MCCV (100+ random splits), not LOO-CV |
| **Overfitting wavelength selection** | Perform CARS/SPA inside the CV loop |

### Recommended Protocol

```
For each CV fold:
    1. Split by patient (patient-stratified K-fold, K=5)
    2. Fit preprocessing (SNV params, wavelength selection) on TRAIN only
    3. Apply to TEST using training parameters
    4. Train model on preprocessed TRAIN
    5. Predict on preprocessed TEST
    6. Record RMSEP, R², MAE

Global metrics:
    - Mean ± SD of RMSEP across folds
    - Check RMSEP/RMSECV ratio < 1.3 (no overfitting)
    - External validation: hold out n ≥ 20 independent samples entirely
```

### Clinical Thresholds to Target

| Biomarker | RMSEP target | Clinical decision point |
|---|---|---|
| Uric acid | < 0.5 mg/dL | Hyperuricaemia > 7 mg/dL |
| Hematuria (RBC) | < 10 RBC/µL | Abnormal > 3 RBC/HPF |
| Bilirubin | Binary (present/absent) | Any detectable = abnormal |
| Total protein | < 30 mg/dL | Proteinuria > 150 mg/day |
| Creatinine | < 0.5 mM | For ACR normalisation |
| Specific gravity | < 0.002 | Range 1.001–1.035 |

---

## 9. Open Questions & Recommended Experiments

### Immediate Priorities

1. **Validate uric acid at 275 nm** in n ≥ 50 real urine samples vs. enzymatic reference. Expected R² > 0.90 for uric acid > 2 mg/dL.
2. **Map fluorescence response** at all 4 LED excitations for 20+ diverse urines. Confirm tryptophan (275→335), NADH (365→460), porphyrins (405→620), riboflavin (455→520). Build reference EEM library.
3. **EIS + optical fusion:** Test multi-modal prediction (EIS features + spectral features) for creatinine and specific gravity. No published precedent — Jimini's unique opportunity.
4. **Collect paired device data:** Measure 15–20 reference solutions on 2–3 Jimini units to enable MVG augmentation for cross-device transfer.

### Key Unknowns

| Question | Why it matters | How to resolve |
|---|---|---|
| Can 275 nm LED distinguish uric acid from tryptophan? | Both absorb near 280 nm | Derivative spectroscopy on spiked solutions |
| What is the practical LOD for bilirubin at 455 nm? | Clinical threshold is trace amounts | Calibration curve with spiked urine |
| Does PARAFAC work with only 4 excitation wavelengths? | Standard EEM uses 20+ excitations | Test on simulated + real data |
| Can EIS conductivity predict creatinine independently? | Would enable dilution correction without optical measurement | Correlate EIS low-freq impedance with CRN |
| Is tryptophan fluorescence quantitative enough for albumin? | Clinical microalbuminuria = 30–300 µg/mL | Spike-recovery experiment |

### Novel Opportunities (Unpublished)

- **LED multi-wavelength spectroscopy + EIS fusion for multi-biomarker urinalysis** — Jimini's potential unique contribution; no published precedent
- **UV (275 nm) LED for urine spectroscopy** — all published LED urine studies start at ≥ 340 nm
- **Cross-device MVG augmentation using water/reference scans only** — validated for blood IR, not yet for urine

---

## Sources

| Reference | Notes |
|---|---|
| Lemos et al. *arXiv* 2023. 2301.10746 | 1D-CNN vs chemometrics benchmark |
| Kiranyaz et al. *Mech Syst Signal Process* 2021 | 1D-CNN survey |
| SpectraPhone *Sci Rep* 2026. DOI: 10.1038/s41598-026-38307-y | PLS R²=0.99 hematuria, albumin |
| Kuenert et al. *Sci Rep* 2025. DOI: 10.1038/s41598-025-92802-2 | LRRE AUC bilirubin 0.92, n=401 |
| Fu et al. *J Anal Chem* 2022 | SpectraTr: Transformer for NIR |
| Xu & Liang. *J Chemometrics* 2004 | Monte Carlo Cross-Validation |
| Erzina et al. *Analyst* 2023. DOI: 10.1039/d3an00669g | WGAN spectral augmentation |
| Bittremieux et al. *Nature Commun* 2020. DOI: 10.1038/s41467-020-19354-z | Cumulative learning for small datasets |
| See [[literature]] for full citation list | |

## Gaps

- PARAFAC applied to partial EEMs (4 excitation wavelengths) vs standard EEMs (20+ wavelengths): theoretical applicability confirmed but not yet benchmarked on Jimini data
- Optimal number of PARAFAC components for Jimini fluorescence decomposition: unknown without real data
- WGAN and diffusion model augmentation: validated on other biological spectral types but not LED-based urine spectroscopy specifically
- Clinical threshold RMSEP targets: derived from literature — Jimini-specific sensitivity/specificity trade-offs at those thresholds not yet characterised
- EIS feature fusion with optical features: no published precedent; optimal fusion strategy (early/late/intermediate) unknown