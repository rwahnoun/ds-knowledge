# Literature Review: Urine Biomarker Prediction via Portable LED-Based Spectroscopy

**Context:** Jimini device — pen-like multi-LED spectrophotometer + EIS for reagent-free urinalysis  
**Audience:** Data scientist / ML engineer building biomarker prediction models  
**Date:** 2026-04-09  
**Compiled by:** Feynman (multi-agent research, 4 parallel threads, 60+ sources)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Jimini Device & Measurement Physics](#2-the-jimini-device--measurement-physics)
3. [Detectable Urine Biomarkers](#3-detectable-urine-biomarkers)
4. [Signal Processing Pipeline](#4-signal-processing-pipeline)
5. [Predictive Models: From PLS to Deep Learning](#5-predictive-models-from-pls-to-deep-learning)
6. [Matrix Correction: Turbidity, Dilution, Color, pH](#6-matrix-correction-turbidity-dilution-color-ph)
7. [Cross-Device Calibration Transfer](#7-cross-device-calibration-transfer)
8. [Data Augmentation for Small Datasets](#8-data-augmentation-for-small-datasets)
9. [Validation & Cross-Validation Strategy](#9-validation--cross-validation-strategy)
10. [Open Questions & Recommended Experiments](#10-open-questions--recommended-experiments)
11. [Paper Index & Downloads](#11-paper-index--downloads)
12. [Sources](#12-sources)

---

## 1. Executive Summary

Reagent-free urine biomarker prediction from LED-based spectroscopy is **feasible for a well-defined subset** of analytes. The literature converges on these key findings:

### What works (high confidence)

| Biomarker | Method | Jimini LED | Best reported performance |
|---|---|---|---|
| **Uric acid** | UV absorbance ~293 nm | 275 nm | Beer-Lambert, R² > 0.95 ¹ |
| **Hemoglobin / hematuria** | Vis absorbance (Soret 415 nm + Q-bands) | 405, 455, VIS | R² = 0.99 (PLS) ² |
| **Bilirubin** | Vis absorbance 344–450 nm | 405, 455 | AUC = 0.92 ³ |
| **Urobilinogen** | Vis absorbance ~490 nm | 455, VIS | AUC ~0.85 ³ |
| **Porphyrins** | Fluorescence Ex 405 → Em 620 nm | 405 → C12 | Qualitative/semi-quant ⁴ |
| **Protein (indirect)** | Tryptophan fluorescence Ex 275 → Em 335 nm | 275 → C12 | Semi-quantitative ⁵ |
| **NADH** | Fluorescence Ex 365 → Em 460 nm | 365 → C12 | Metabolic index ⁶ |
| **Riboflavin** | Fluorescence Ex 365/455 → Em 520 nm | 365/455 → C12 | Quantitative ⁶ |
| **Specific gravity / pH** | Multi-wavelength spectral pattern | Broadband | AUC ~0.85–0.89 ³ |

### What partially works (scatter/fluorescence/EIS, not direct Beer-Lambert)

| Biomarker | Method | Jimini channels | Confidence |
|---|---|---|---|
| **WBC (leukocytes)** | Scatter (Mie) + autofluorescence (NADH) + EIS | $A_{1070}$, ex365/em460, EIS | Low (binary pyuria Y/N) |
| **Bacteria** | Scatter + flavin fluorescence + EIS | $A_{1070}$, ex455/em525, EIS | Low-Medium (>10⁵ CFU/mL) |
| **PBG** | Via conversion to porphyrins → Soret + fluorescence | $A_{405}$, $A_{405}/A_{480}$, ex405/em620 | Medium (binary, acute attacks) |
| **TUP (total porphyrins)** | Soret absorption + fluorescence | ex405/em620, $A_{405}/A_{480}$, 2nd deriv | Medium-High |
| **Osmolality** | EIS conductivity + NIR scatter | EIS σ, $A_{1070}$, spectral integral | Medium |
| **Crystals** | Scatter (large particles, wavelength-independent) | $A_{1070}$, $A_{800}/A_{400}$ → 1.0 | Low (binary ≥+) |

### What does NOT work reagent-free in the visible range

| Biomarker | Why | Workaround |
|---|---|---|
| **Glucose** | No chromophore in UV-Vis at physiological levels | NIR >1400 nm or EIS |
| **Albumin (quantitative)** | Colorless in visible | Fluorescence (275→335) or EIS |
| **Creatinine (precise)** | Absorbs at 234 nm (below 275 nm LED) | EIS or NIR |
| **Urea** | No UV-Vis chromophore | NIR >1400 nm |
| **Electrolytes (Na⁺, K⁺, Cl⁻)** | No optical signature | EIS (conductivity) — total ionic, not individual ions |
| **Nitrites** | Spectrally transparent; Griess requires reagent | Indirect via bacterial detection model |
| **Epithelial cells** | No unique chromophore; scatter only | Not separable from WBC/bacteria/crystals by bulk spectroscopy |

### Key ML/modeling insight
PLS regression dominates quantitative spectroscopic prediction and remains competitive with deep learning for datasets under 200 samples. 1D-CNN outperforms PLS above n ≈ 300–500. SNV normalization + Savitzky-Golay derivatives is the proven preprocessing baseline.

### Novel opportunity
**No published paper combines LED multi-wavelength spectroscopy + EIS for multi-biomarker urine analysis.** This is Jimini's potential unique contribution.

---

## 2. The Jimini Device & Measurement Physics

### Hardware Summary

| Component | Specification | Spectroscopic Role |
|---|---|---|
| **Emitters** | 275 nm, 365 nm, 405 nm, 455 nm UV-Vis LEDs + VIS broadband + VISD + R405 | Excitation for absorbance & fluorescence |
| **Detector C12** | 321–870 nm sensing range | UV-Vis absorbance + fluorescence emission |
| **Detector C14** | 570–1078 nm sensing range | Vis-NIR absorbance + water overtone band |
| **EIS** | Electrochemical impedance spectroscopy | Ionic strength, conductivity, protein binding |
| **IRM** | IR matrix sensors (e.g. IRM-1070) | NIR molecular overtones |

### What Each LED Excites

| LED (nm) | Absorbance Targets | Fluorescence Targets |
|---|---|---|
| **275** | Uric acid (290–295), Tryptophan (280), Tyrosine (274), DNA bases (260–280) | Tryptophan Em 330–350 (protein proxy), Indoxyl sulfate (CKD marker) |
| **365** | NADH (340–365), near-UV tail of bilirubin | NADH Em 440–470, Riboflavin Em 520, Hippuric acid Em 420 |
| **405** | Porphyrin Soret band (405–415), Bilirubin (415–450), Hemoglobin Soret | Porphyrin Em 620–640 |
| **455** | Bilirubin peak (430–460), FAD/Flavins (450) | FAD Em 525, Riboflavin Em 520 |
| **VIS** | Hemoglobin Q-bands (541, 555, 576, 630), Urobilinogen (440–500) | — |

### Measurement Principle

Each measurement produces a **signal level channel (SLC)** encoded as `{sensor}-{emitter}-{amplitude}`. The raw signal is photon counts (or ADC values). The fundamental transformation is Beer-Lambert:

$$A(\lambda) = -\log_{10}\left(\frac{I_{\text{sample}}(\lambda) - I_{\text{dark}}(\lambda)}{I_{\text{water}}(\lambda) - I_{\text{dark}}(\lambda)}\right)$$

This water-referenced absorbance removes LED intensity variation and detector baseline per-measurement. It is the natural starting point for all downstream processing.

---

## 3. Detectable Urine Biomarkers

### 3.1 UV Absorbers (275 nm LED → C12)

**Uric acid** is the star analyte for UV-based detection. Its purine ring system produces a strong π→π* transition with λ_max ≈ 293 nm ¹²⁷. Two portable devices have demonstrated reagent-free uric acid quantification:

- **Uricia POC device (2025)**: Compact UV measurement at 295 nm, SD < 0.01, validated against clinical chemistry ⁸
- **Label-free UV portable (2022)**: First demonstration that portable UV spectrophotometry measures uric acid in spot urine without reagents ¹

The 275 nm LED sits on the shoulder of the uric acid absorption band. Matrix interference from tyrosine (274 nm), tryptophan (280 nm), and creatinine (234 nm) is the main challenge. **Derivative spectroscopy or PLS deconvolution is required.**

**Proteins** absorb at 280 nm (aromatic amino acids) and 220–230 nm (peptide bonds). The 275 nm LED captures the aromatic side-chain absorption of tryptophan-containing proteins, providing a total protein proxy ⁹. Albumin has a distinct absorption band at 229 nm ¹⁰ — below Jimini's range, but its tryptophan fluorescence (Ex 275–295 / Em 330–350) is accessible.

### 3.2 Visible Absorbers (405, 455 nm LEDs → C12/C14)

**Hemoglobin / Hematuria**: The strongest visible-range urine signal. The Soret band at 415 nm and Q-bands at 541, 555, 576, 630 nm produce unmistakable spectral features. SpectraPhone (2026) achieved **R² = 0.99, RMSE = 61.6 RBC/µL** using PLS on 2nd-derivative spectra ². The 405 nm LED sits right on the Soret shoulder.

**Bilirubin**: Absorbs broadly from 400–500 nm with peak ~450 nm. Kuenert et al. (2025) demonstrated **AUC = 0.92** for binary detection using logistic regression with random effects on LED spectrometer data (340–850 nm, n = 401 clinical samples) ³. Key wavelengths: 344, 387, 427 nm.

**Urobilinogen**: The main yellow pigment (urochrome). Absorbs around 430–500 nm with pH-dependent shifts (~50 nm across pH 5–8). Detectable at 455 nm.

### 3.3 Fluorescent Biomarkers (Multi-LED excitation → C12 emission)

Jimini's 4 LEDs create a **partial Excitation-Emission Matrix (EEM)** — a powerful diagnostic fingerprint:

| Fluorophore | Excitation | Emission | Clinical meaning | Jimini LED |
|---|---|---|---|---|
| Tryptophan | 275–295 nm | 330–360 nm | Protein/CKD, melanoma staging ⁵¹¹ | 275 nm |
| NADH | 340–365 nm | 440–470 nm | Metabolic activity | 365 nm |
| Riboflavin (B2) | 365–450 nm | 520–560 nm | Nutritional status | 365/455 nm |
| Porphyrins | 405–420 nm | 620–640 nm | Porphyria, bladder cancer ⁴¹² | 405 nm |
| FAD | 450 nm | 525 nm | Flavin metabolism | 455 nm |
| Indoxyl sulfate | ~280 nm | ~330 nm | Uremic toxin (CKD) | 275 nm |
| Hippuric acid | ~320 nm | ~420 nm | Gut bacteria, drug metabolism | 365 nm |

**PARAFAC decomposition** of the multi-LED fluorescence data can separate overlapping fluorophore contributions ¹³. With 4 excitation × broadband detection, this is directly applicable to Jimini.

Cancer detection at 405 nm excitation has been validated: porphyrin-region emissions (620–640 nm) discriminate bladder cancer from controls ⁴. Melanoma shows significant tryptophan fluorescence changes at 295 nm excitation ¹¹.

### 3.4 EIS Biomarkers

EIS completes the panel for analytes invisible to optics:

| Biomarker | EIS mechanism | Literature support |
|---|---|---|
| **Creatinine** | Non-enzymatic impedimetric sensing, ZIF-8 nanoparticles | LOD ~30 µM ¹⁴ |
| **Glucose** | GOx enzyme electrode | Well-established, high accuracy ¹⁵ |
| **Ionic strength / SG** | Low-frequency conductivity | Direct surrogate for osmolality |
| **Albumin** | Immunosensor (anti-HSA antibody) | LOD ~1 pg/mL ¹⁶ |
| **Bacteria** | Label-free impedimetric adhesion/growth | LOD ~10³ CFU/mL ¹⁶ |
| **Uromodulin** | Non-Faradaic EIS, Ta₂O₅ IDEs | 0.5–8 ng/mL range ¹⁷ |

### 3.5 NIR (C14: 570–1078 nm)

The C14 detector accesses the first water overtone band (~970 nm), which is sensitive to total dissolved solutes (correlates with osmolality/specific gravity). Weak vibrational overtones of urea (N-H, C=O) and creatinine (C-H) appear in the 900–1100 nm region but require PLS or ML for extraction from the dominant water background ¹⁸¹⁹²⁰.

### 3.6 Cellular & Particulate Analytes (Scatter-Dominated)

These analytes have no unique absorption chromophore. Detection relies on turbidity (Mie scattering), autofluorescence, and spectral scatter slope — not Beer-Lambert absorption.

**White Blood Cells (WBC / Leukocytes):**  
WBCs (~10–15 µm) produce Mie scattering detectable as elevated $A_{1070}$ and altered spectral baseline. Monteiro-Silva et al. (2022, 2024) demonstrated Vis-NIR spectroscopy for WBC quantification in blood (R² ~0.85 using PLS on 400–1000 nm), but urine WBC concentrations are orders of magnitude lower. Leukocyte esterase (LE) — the enzyme released by WBCs — is the standard dipstick marker, but requires indoxyl ester substrate (reagent). Reagentless, WBC autofluorescence at ex365/em460 (NADH/NADPH from viable neutrophils) provides a weak signal. **Best approached as binary classification (pyuria Y/N) using scatter + fluorescence features rather than direct count.**

Relevant Jimini features: $A_{1070}$ (turbidity), scatter slope $A_{400}/A_{800}$, fluorescence ex365/em460, EIS (intact cell membranes alter impedance at kHz frequencies).

**Epithelial Cells (epiCells):**  
Squamous (20–60 µm), transitional (12–30 µm), and renal tubular epithelial cells contribute to scatter. No unique spectral signature. Banten et al. (2021, Nature Sci. Rep.) showed multispectral autofluorescence imaging can distinguish renal from squamous epithelial cells, but this requires single-cell imaging, not bulk spectroscopy. **Direct detection by bulk UV-Vis spectroscopy is not feasible.** Binary detection (≥+) may be possible as a scatter-correlated auxiliary but with very low confidence and high false-positive rates from confounding particulates (WBCs, bacteria, crystals).

**Crystals:**  
Urinary crystals (calcium oxalate, uric acid, struvite, cystine, calcium phosphate; 10–100+ µm) produce strong Mie scattering. Their large size means scattering is nearly wavelength-independent in the visible range (geometric optics regime). This distinguishes them from smaller particulates: a flat scatter spectrum ($A_{800}/A_{400} → 1.0$) suggests crystals, while steeper wavelength-dependent scatter suggests cells or bacteria. Uric acid crystals additionally contribute UV absorption at 275 nm (indistinguishable from dissolved uric acid). Crystal IS type cannot be determined spectroscopically — only total particulate load.

### 3.7 Porphyria Markers: PBG and Total Urinary Porphyrins (TUP)

**Porphobilinogen (PBG):**  
PBG is a monopyrrole heme precursor. Massively elevated urinary PBG (>20 mg/L vs normal <2 mg/L) is the hallmark of acute porphyria attacks. PBG itself absorbs at ~240 nm (below Jimini's range) and is spectrally invisible at 275–1070 nm. However, PBG spontaneously polymerizes to uroporphyrin on standing or acidification, producing:
- **Soret absorption at ~405 nm** (ε ~500,000 M⁻¹cm⁻¹)
- **Fluorescence at ~618–625 nm** when excited at 405 nm

Mateen et al. (2018, J. Biomedical Optics 23(5):055006) demonstrated rapid spectrophotometric PBG quantification via this acid-heat conversion. For Jimini, the V20 objectives flag "abs 405/480" and "R405 HDR VIDS VIS" as the relevant signal channels, consistent with detecting PBG-derived porphyrins via Soret absorption and fluorescence.

**Total Urinary Porphyrins (TUP):**  
TUP = sum of coproporphyrin, uroporphyrin, and other tetrapyrrole species. Porphyrins have among the highest molar absorptivities of any biological molecule (ε ~500,000 M⁻¹cm⁻¹ at the Soret band, ~400 nm). They are also intensely fluorescent:

| Porphyrin | Soret λ (nm) | Fluorescence emission (nm) |
|---|---|---|
| Coproporphyrin III | 401 | 596, 652 |
| Uroporphyrin III | 398–405 | 618, 675 |
| Protoporphyrin IX | 406 | 632, 695 |

The 405 nm Jimini LED is an almost perfect Soret excitation source. **Fluorescence at ex405/em620 is highly specific for porphyrins** — hemoglobin does NOT fluoresce (paramagnetic quenching), and bilirubin fluorescence is at ~520 nm, not 620 nm. Buttery et al. (1995, Clinical Chemistry 41(1):103) demonstrated quantitative coproporphyrin/uroporphyrin fractionation in urine using second-derivative absorption spectroscopy in the Soret region.

The challenge for TUP quantification is the spectral overlap at 405 nm between porphyrins, hemoglobin (Soret ~415 nm), and bilirubin (broad ~400–500 nm). Deconvolution using the $A_{405}/A_{480}$ ratio and Hb subtraction via Q-bands (540, 575 nm from white LED) is recommended.

### 3.8 Electrolytes and Ions (EIS-Only Targets)

These analytes have **zero UV-Vis absorption** and cannot be measured optically.

**Sodium (Na⁺) and Chloride (Cl⁻):**  
Na⁺ and Cl⁻ are the dominant charge carriers in urine, accounting for ~50% of total osmolality and ~70% of ionic conductivity. EIS measurement at 10–100 kHz provides a direct, physically grounded estimate. However, separating Na⁺ from Cl⁻ from K⁺ requires ion-selective electrodes; bulk EIS measures total ionic strength only. NaCl solutions perturb NIR water absorption bands (~970 nm, ~1450 nm) but the effect at urine concentrations is weak and unlikely to be resolvable by Jimini.

**Nitrites (NO₂⁻):**  
Nitrite is a marker for Gram-negative bacteriuria (bacterial nitrate reductase converts dietary nitrate → nitrite). The nitrite ion is spectrally transparent at Jimini wavelengths (weak absorption at ~354 nm, ε ~23 M⁻¹cm⁻¹ — negligible at clinical concentrations). The gold standard Griess reaction produces an azo dye absorbing at 540 nm (ε ~40,000) but requires sulfanilamide + NED reagent — not reagentless. **Nitrite detection without a chemical reaction is not feasible by UV-Vis spectroscopy.** It is best modeled as a correlate of bacterial detection features (scatter + fluorescence), or via a Griess reagent embedded in a disposable cuvette tip.

---

## 4. Signal Processing Pipeline

### 4.1 Recommended Pipeline (Evidence-Based)

```
Raw ADC counts per SLC
    │
    ├─ [1] Dark subtraction: I_corrected = I_raw - I_dark
    │       (removes electronic noise, thermal baseline)
    │
    ├─ [2] Water-reference normalization: A(λ) = -log₁₀((I_sample - I_dark) / (I_water - I_dark))
    │       (converts to absorbance, cancels LED intensity + detector gain)
    │
    ├─ [3] Quality control:
    │       • Negative absorbance → measurement error flag
    │       • Saturation detection (ADC at limits)
    │       • Outlier detection (Isolation Forest or Hotelling T²)
    │
    ├─ [4] Scatter / baseline correction (SPLIT BY RANGE):
    │   ├─ UV (275–400 nm): arPLS baseline correction (λ=10⁴)
    │   │   Reason: fluorescence background from porphyrins/NADH is strongest here
    │   └─ Vis-NIR (400–1078 nm): SNV normalization
    │       Reason: validated in LED urine spectroscopy (Kuenert 2025 ³),
    │       reduced inter-sample SD by 4 orders of magnitude
    │
    ├─ [5] Savitzky-Golay smoothing/derivatives:
    │       • Smoothing: window=7–11, polynomial=2
    │       • 1st derivative: removes constant baseline offset
    │       • 2nd derivative: removes linear baseline, enhances peak resolution
    │       Proven for hemoglobin PLS (SpectraPhone ²)
    │
    ├─ [6] [Optional] Orthogonal Signal Correction (OSC/OPLS):
    │       2–3 components to remove patient-level variation orthogonal to target analyte
    │       Impact: R² 0.50 → 0.987 in food NIR studies ²¹
    │
    ├─ [7] [Optional] EMSC with known interferent basis spectra:
    │       For UV range with strong fluorescence background
    │       Model: x = a₀ + a₁·x_ref + a₂·z_fluor + a₃·z_scatter + ε
    │       Requires pre-characterized interferent spectra ²²
    │
    ├─ [8] Feature extraction / wavelength selection:
    │       • VIP scores (VIP > 1.0) from PLS loadings
    │       • CARS: competitive adaptive reweighted sampling ²³
    │       • SPA: successive projections algorithm (minimal non-collinear set)
    │       • CARS-SPA combination outperforms either alone
    │
    └─ [9] Model training
```

### 4.2 Key Preprocessing Methods — Mathematical Detail

#### Standard Normal Variate (SNV)

$$x_{\text{SNV}}(\lambda) = \frac{x(\lambda) - \bar{x}}{\sigma_x}$$

Per-spectrum transform. Corrects multiplicative scatter (turbidity, path length variation) and additive offset (dilution, background). **No reference spectrum needed** — applied independently per sample. Mathematically equivalent to MSC when the MSC reference is the dataset mean ²⁴.

**Validated for LED urine spectroscopy**: Kuenert et al. ³ showed SNV on 288-channel LED spectra (340–850 nm, n=401 samples) reduced mean per-wavelength SD from 1097.62 to 0.24.

#### Multiplicative Scatter Correction (MSC)

$$x_i(\lambda) \approx a_i \cdot \bar{x}(\lambda) + b_i \quad \Rightarrow \quad x_{\text{MSC}}(\lambda) = \frac{x_i(\lambda) - b_i}{a_i}$$

Regress each spectrum against a reference (typically calibration-set mean). Provides interpretable scatter parameters ($a_i$ = multiplicative, $b_i$ = additive). **Set-dependent** — reference must be stable.

#### Extended MSC (EMSC) — For Complex Biological Fluids

$$x_i(\lambda) = a_0 + a_1 \cdot \bar{x}(\lambda) + a_2 \cdot \lambda + a_3 \cdot \lambda^2 + \sum_k e_k \cdot f_k(\lambda) + \varepsilon$$

Adds polynomial baseline terms and known interferent spectra $f_k(\lambda)$ (e.g., urochrome, fluorescence background). Critical for UV range where urine autofluorescence confounds absorption measurements ²².

#### Baseline Correction: arPLS

Asymmetrically Reweighted Penalized Least Squares ²⁵. Uses logistic sigmoid weighting to fit a smooth baseline while ignoring spectral peaks. One hyperparameter: λ (smoothness penalty, typical 10²–10⁷). Outperforms airPLS for moderate-SNR conditions.

**BrPLS (Bayesian variant)**: State-of-the-art, R² = 0.999 vs 0.9985 for arPLS. No manual threshold tuning. Recommended for UV fluorescence correction when computational cost is acceptable.

#### Savitzky-Golay Derivatives

SG 2nd derivative is particularly valuable for urine:
1. Eliminates baseline offset AND slope (varying dilution)
2. Reveals overlapping peaks (discriminates creatinine vs. urea NIR bands)
3. Combined with SNV: validated for PLS quantification ²

**Fractional-order SG derivatives** (order α ∈ (0,2)) are emerging — showed +17% correlation improvement for chlorophyll estimation vs. integer derivatives ²⁶.

---

## 5. Predictive Models: From PLS to Deep Learning

### 5.1 Model Selection by Dataset Size

| n (samples) | Recommended model | Rationale |
|---|---|---|
| < 100 | **PLS** with MCCV, SNV+SG+CARS | Robust; sufficient for linear spectral relationships |
| 100–300 | **SVR (RBF kernel)** or RF + PLS ensemble | SVR handles nonlinearities; augment to 500+ for CNN |
| 300–500 | **1D-CNN** with BatchNorm + Dropout | Outperforms classical methods consistently ²⁷ |
| > 500 | **1D-CNN** or Transformer (emerging) | SpectraTr, SpectraViT show promise ²⁸ |

### 5.2 PLS Regression — Gold Standard for Quantitative Spectroscopy

**Why PLS works**: Handles collinear spectral features, extracts latent variables maximizing covariance between X (spectra) and Y (concentrations), robust to matrix interference.

**Best results in urine spectroscopy**:

| Study | Biomarker | Preprocessing | R² | RMSE |
|---|---|---|---|---|
| SpectraPhone 2026 ² | Hematuria (RBC) | 2nd derivative | **0.9913** | 61.6 RBC/µL |
| SpectraPhone 2026 ² | Albumin (reagent-free) | SNV | **0.9981** | 11.85 mg/dL |
| Spectrochip 2024 ²⁹ | 12 parameters | CCM (calibration curve) | > 0.95 | — |
| Shaw et al. 1996 ¹⁸ | Protein, creatinine, urea | NIR PLS | High | Clinical range |

**Hyperparameter selection**: Number of latent variables (LVs) selected by Monte Carlo Cross-Validation (MCCV) — less biased than LOO-CV for small datasets ³⁰.

### 5.3 Logistic Regression with Random Effects (LRRE)

For binary classification (present/absent) with repeated measures per patient, LRRE adds a random intercept per subject to handle within-patient correlation ³.

| Biomarker | AUC | Study |
|---|---|---|
| Bilirubin | **0.921** | Kuenert 2025 ³ |
| Erythrocytes | ~0.88 | Kuenert 2025 ³ |
| Specific gravity | ~0.89 | Kuenert 2025 ³ |
| Protein | good | Kuenert 2025 ³ |

### 5.4 1D-CNN for Spectral Data

The dominant deep learning architecture for 1D spectral regression/classification ²⁷³¹:

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

**Benchmarks**: 1D-CNN outperformed PLS, SVR, RF, MLP on 5 public spectral datasets; average R² improvement over PLS = +0.05–0.12 when n > 500 ²⁷. For n < 200, PLS/SVR remain competitive or superior.

### 5.5 PARAFAC for Multi-LED Fluorescence

When using multiple excitation wavelengths (Jimini's 4 LEDs) with broadband detection, the data forms a partial EEM tensor. **PARAFAC** decomposes the three-way data (samples × excitation × emission) into independent fluorophore components ¹³.

This enables simultaneous quantification of tryptophan, NADH, riboflavin, and porphyrins from Jimini's native multi-LED fluorescence data.

### 5.6 Stacking / Ensemble

For robust performance across dataset sizes:

```
PLS predictions + SVR predictions + 1D-CNN predictions
    → Meta-learner (Ridge regression or simple averaging)
    → Final prediction
```

Ensemble approaches consistently reduce variance and improve generalization in spectral chemometrics.

---

## 6. Matrix Correction: Turbidity, Dilution, Color, pH

### 6.1 Turbidity

**Problem**: Suspended particles (cells, crystals, bacteria, lipids) scatter light at all wavelengths, inflating apparent absorbance.

**Estimation**: At 660–800 nm, urine chromophores have negligible true absorbance → any signal is scatter. Model:

$$A_{\text{scatter}}(\lambda) = \alpha \cdot \exp(-\beta \cdot \lambda)$$

Fit α, β from 600–800 nm baseline region, then subtract from full spectrum ³².

**CIE L\*a\*b\* assessment**: L\* < 89.1 → abnormal turbidity (96% accuracy, AUC = 0.984) ³³. CIE b\* correlates with urochrome concentration (τ = 0.708 with osmolality) ³⁴.

**SNV handles mild turbidity** (per-spectrum normalization). For severe turbidity, use EMSC with scatter basis vectors.

### 6.2 Dilution / Hydration Correction

Urine osmolality ranges 50–1200 mmol/kg (24-fold range). All analyte concentrations scale with dilution.

#### Conventional Creatinine Correction (CCRC)

$$A_{\text{norm}} = \frac{[\text{Analyte}]}{[\text{Creatinine}]}$$

**Limitations**: Creatinine varies with muscle mass (↓20–36% in females/elderly), diet, exercise, disease. WHO excludes CRN < 0.3 or > 3.0 g/L → rejects ~20% of samples ³⁵.

#### V-PFCRC — Variable Power-Functional CRN Correction ⭐

**Best-in-class dilution correction** (Carmine 2025, n = 58,439 samples) ³⁵:

$$A_{\text{corrected}} = A_{\text{raw}} \times \text{CRN}^{-b_{\text{variable}}}$$

where $b_{\text{variable}} = c \cdot \ln(A_{\text{raw}}) + d$ with analyte-specific and sex-specific coefficients c, d.

- Eliminates nonlinear dilution bias across all exposure levels
- Reduces sample rejection rate from 22% to < 1%
- Valid down to CRN ≈ 0.05 g/L
- Requires large reference dataset (≥ 1000 samples) to derive c, d coefficients

#### Specific Gravity Normalization

$$A_{\text{SG}} = A_{\text{raw}} \times \frac{0.024}{\text{SG} - 1.000}$$

Not affected by muscle mass or creatinine physiology. EIS conductivity provides a direct SG surrogate for Jimini.

### 6.3 Color Correction (Urochrome, Bilirubin)

**Urochrome (urobilin)**: Dominant yellow pigment. Broad 400–500 nm absorbance. pH-dependent: peak shifts ~50 nm between pH 5 and pH 8 ³⁶.

**Correction strategies**:
1. **EMSC with urochrome reference spectrum**: Model and subtract urochrome contribution
2. **Include as latent variable in PLS/OPLS**: Let the model learn to orthogonalize against it
3. **CIE b\* flagging**: Samples with b\* > 30 → pre-dilute before measurement

**Bilirubin**: Strong 400–500 nm absorbance (ε ≈ 55,000 L·mol⁻¹·cm⁻¹ at 454 nm). Measure A(454 nm) as bilirubin proxy → subtract scaled reference spectrum.

### 6.4 Inner Filter Effect (IFE) in Fluorescence

When urine absorbs strongly at the excitation or emission wavelength, fluorescence becomes nonlinear.

**Standard correction (Lakowicz)**:

$$F_{\text{corrected}} = F_{\text{observed}} \times 10^{(A_{\text{ex}} + A_{\text{em}})/2}$$

Valid for $A_{\text{ex}} < 0.3$. For higher absorbance: dilute 1:2–1:5 with PBS, or use the iterative secondary IFE algorithm ³⁷.

### 6.5 pH Effects

pH shifts urobilin absorbance by ~50 nm and affects indoxyl sulfate fluorescence (enhanced at pH > 7 due to oxidation) ³⁶.

**Correction options**:
1. Buffer standardization (add 1/9 volume of 0.5M phosphate pH 7.0)
2. Include pH as model covariate
3. EMSC with pH-state reference spectra

---

## 7. Cross-Device Calibration Transfer

### 7.1 The Problem

Two Jimini units produce different spectra from the same sample due to:
- LED peak wavelength shift (±2–5 nm)
- LED intensity variation (±10–20%)
- Detector quantum efficiency variation (2–5% per channel)
- Optical path differences

### 7.2 Recommended Approach (Prioritized)

#### Priority 1: Water-Reference + SNV (Zero overhead)

Already built into the measurement protocol. Water-reference absorbance cancels LED intensity differences. SNV handles remaining scale differences. **Removes ~60–70% of inter-unit variation** ³⁸.

#### Priority 2: Per-Channel Gain Correction (Factory calibration)

Measure 3–5 reference solutions on each new unit during manufacturing QC. Fit per-channel multiplicative gain factors. Store in device firmware. Reduces systematic errors to < 1–2%.

For LED-based sensors, this reduces to a **diagonal DS matrix** — very robust with few transfer samples ³⁹.

#### Priority 3: MVG Augmentation (Training-time, best ROI) ⭐

Leopold-Kerschbaumer et al. (2025) demonstrated that **17 paired reference measurements** (not biological samples) across 2 devices enable effective cross-device model generalization via multivariate Gaussian augmentation ⁴⁰:

```python
# Cross-device covariance from paired reference measurements
diff = X_device1 - X_device2  
Sigma_cross = np.cov(diff.T)

# Augment training: for each sample, generate synthetic device variants
for x in X_train:
    synthetic = np.random.multivariate_normal(mean=x, cov=Sigma_cross, size=100)
    X_augmented.append(synthetic)
```

Cross-device AUC improved from 0.81–0.86 → 0.90–0.92 (matching within-device performance) on blood IR data. **Requires only reference solutions, no patient urine**.

#### Priority 4: CORAL (Post-deployment, unsupervised)

Align covariance matrices of source (training) and target (new device) distributions:

$$X_{\text{aligned}} = (X_{\text{source}} - \mu_s) \cdot C_s^{-1/2} \cdot C_t^{1/2} + \mu_t$$

No paired samples needed — just unlabeled target-device spectra. Good for correcting slow drift over time ⁴¹.

#### Priority 5: Domain Adversarial NN (Advanced, fleet-scale)

DANN with gradient-reversal layer forces device-invariant feature learning ⁴². Requires ~20+ deployed devices with sufficient unlabeled data. **Warning**: "worst scanner syndrome" — forcing domain invariance can destroy information if devices have inherently different SNR ⁴³.

### 7.3 Method Comparison

| Method | Paired samples | Handles gain | Handles offset | For Jimini |
|---|---|---|---|---|
| Water-ref + SNV | None | ✅ | ✅ | **Start here** |
| Per-channel gain | 3–5 ref solutions | ✅ | Partial | **Factory step** |
| MVG augmentation | 15–20 ref solutions (2–3 devices) | ✅ | ✅ | **Best ROI** |
| CORAL | None (unlabeled target data) | ✅ | ✅ | **Post-deploy** |
| DS/PDS | 6–10 paired samples | ✅ | ✅ | If paired available |
| DANN | None (domain labels) | ✅ | ✅ | Fleet-scale |

---

## 8. Data Augmentation for Small Datasets

Clinical urine datasets are typically small (50–500 samples) with class imbalance (pathological rare).

### 8.1 Traditional Augmentation

```python
def augment_spectrum(spectrum, n_augmented=5):
    augmented = []
    for _ in range(n_augmented):
        s = spectrum.copy()
        s += np.random.normal(0, 0.002 * np.std(s), len(s))     # detector noise
        s *= np.random.uniform(0.95, 1.05)                       # dilution variation
        x = np.linspace(-1, 1, len(s))
        s += np.random.normal(0, 0.001) * x + \
             np.random.normal(0, 0.0005) * x**2                  # LED drift
        s = np.roll(s, np.random.randint(-2, 3))                 # wavelength shift
        augmented.append(s)
    return augmented
```

### 8.2 WGAN for Spectral Data

Wasserstein GAN with gradient penalty (WGAN-GP) trained on existing spectra generates realistic synthetic samples. Validated on cancer liquid biopsy FTIR — improved downstream classification accuracy by 8–15% ⁴⁴. Generated spectra indistinguishable from real in PCA space.

### 8.3 Diffusion Models (State-of-the-Art, 2025)

Diffusion probabilistic models produce highest-quality synthetic spectra, outperforming GANs for inter-sample spectral variability. Main limitation: compute-intensive. Consider when dataset exceeds n ≈ 200 ⁴⁵.

### 8.4 Transfer Learning / Cumulative Learning

Pre-train 1D-CNN on large auxiliary spectral dataset (e.g., Kew Garden NIR, LUCAS soil) → fine-tune on urine. Reduces required dataset size by 5–10× ⁴⁶.

---

## 9. Validation & Cross-Validation Strategy

### 9.1 Critical Pitfalls

| Pitfall | How to avoid |
|---|---|
| **Data leakage from preprocessing** | Fit SNV/PCA/wavelength selection on TRAINING set only |
| **Same-patient samples in train+test** | Use Leave-One-Patient-Out (LOPO) or patient-stratified folds |
| **Optimistic RMSECV** | Use MCCV (100+ random splits), not LOO-CV ³⁰ |
| **Overfitting wavelength selection** | Perform CARS/SPA inside the CV loop |

### 9.2 Recommended Protocol

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

### 9.3 Clinical Thresholds to Target

| Biomarker | RMSEP target | Clinical decision point |
|---|---|---|
| Uric acid | < 0.5 mg/dL | Hyperuricemia > 7 mg/dL |
| Hematuria (RBC) | < 10 RBC/µL | Abnormal > 3 RBC/HPF |
| Bilirubin | Binary (present/absent) | Any detectable = abnormal |
| Total protein | < 30 mg/dL | Proteinuria > 150 mg/day |
| Creatinine | < 0.5 mM | For ACR normalization |
| Specific gravity | < 0.002 | Range 1.001–1.035 |

---

## 10. Open Questions & Recommended Experiments

### 10.1 Immediate Priorities

1. **Validate uric acid at 275 nm** in n ≥ 50 real urine samples vs. enzymatic reference. Expected R² > 0.90 for uric acid > 2 mg/dL. Simple Beer-Lambert + interference correction.

2. **Map fluorescence response** at all 4 LED excitations for 20+ diverse urines. Confirm tryptophan (275→335), NADH (365→460), porphyrins (405→620), riboflavin (455→520). Build reference EEM library.

3. **EIS + optical fusion**: Test multi-modal prediction (EIS features + spectral features) for creatinine and specific gravity. No published precedent — Jimini's unique opportunity.

4. **Collect paired device data**: Measure 15–20 reference solutions on 2–3 Jimini units to enable MVG augmentation for cross-device transfer.

### 10.2 Key Unknowns

| Question | Why it matters | How to resolve |
|---|---|---|
| Can 275 nm LED distinguish uric acid from tryptophan? | Both absorb near 280 nm | Derivative spectroscopy on spiked solutions |
| What is the practical LOD for bilirubin at 455 nm? | Clinical threshold is trace amounts | Calibration curve with spiked urine |
| Does PARAFAC work with only 4 excitation wavelengths? | Standard EEM uses 20+ excitations | Test on simulated + real data |
| Can EIS conductivity predict creatinine independently? | Would enable dilution correction without optical measurement | Correlate EIS low-freq impedance with CRN |
| Is tryptophan fluorescence quantitative enough for albumin? | Clinical microalbuminuria = 30–300 µg/mL | Spike-recovery experiment |

### 10.3 What No One Has Published Yet

- **LED multi-wavelength spectroscopy + EIS fusion for multi-biomarker urinalysis** → Jimini's novel contribution
- **UV (275 nm) LED for urine spectroscopy** → all published LED urine studies start at ≥ 340 nm
- **Cross-device MVG augmentation using water/reference scans only** → validated for blood IR but not urine

---

## 11. Paper Index & Downloads

### Downloaded PDFs (in `papers/` directory)

| File | Paper | Year | Key Topic |
|---|---|---|---|
| `spectraphone-urinalysis-2026.pdf` | SpectraPhone: Smartphone spectrometer urinalysis | 2026 | PLS R²=0.99 hematuria, albumin |
| `kuenert-catheter-spectroscopy-2025.pdf` | Continuous catheter spectroscopic monitoring | 2025 | LED urine, SNV, LRRE, n=401 |
| `v-pfcrc-creatinine-normalization-2025.pdf` | V-PFCRC dilution correction method | 2025 | Best-in-class creatinine normalization |
| `bladder-cancer-eem-cnn-2025.pdf` | Bladder cancer EEM + CNN | 2025 | Fluorescence EEM, CNN 72% |
| `body-fluid-fluorescence-2023.pdf` | Body fluid fluorescence signatures | 2023 | Precise Ex/Em peak maps for urine |
| `1d-cnn-vs-chemometrics-2023.pdf` | 1D-CNN vs ML for spectral classification | 2023 | CNN outperforms PLS when n>500 |
| `electrochemical-creatinine-review-2022.pdf` | Electrochemical creatinine detection review | 2022 | EIS creatinine sensing methods |
| `deep-spectral-cnn-libs-2020.pdf` | Deep Spectral CNN for LIBS | 2020 | 1D-CNN architecture for spectra |
| `1d-cnn-review-portable-raman-2020.pdf` | 1D-CNN review for portable Raman | 2020 | CNN architectures for spectral data |
| `dnn-mie-scatter-correction-2020.pdf` | DNN for Mie scatter correction in FTIR | 2020 | Neural network scatter correction |
| `data-augmentation-spectral-cnn-2017.pdf` | Data augmentation for spectral CNN | 2017 | Bjerrum augmentation strategies |
| `coral-original-2016.pdf` | CORAL: Return of Frustratingly Easy DA | 2016 | Covariance alignment for domain transfer |
| `deep-coral-2016.pdf` | Deep CORAL: Correlation alignment for deep DA | 2016 | Deep domain adaptation |
| `domain-adaptation-enose-drift-2015.pdf` | Domain adaptation ELMs for e-nose drift | 2015 | Sensor drift compensation |
| `benchmarking-dl-raman-2026.pdf` | Benchmarking DL for Raman spectroscopy | 2026 | Comprehensive DL vs chemometrics |

### Key Papers Not Downloaded (Paywalled / Restricted)

| Paper                                   | DOI                           | Where to find                |
| --------------------------------------- | ----------------------------- | ---------------------------- |
| Tryptophan & Melanoma (2021)            | 10.3390/ijms22041884          | MDPI (requires browser)      |
| Uric Acid UV Portable (2022)            | 10.3390/s22083009             | MDPI Sensors                 |
| Spectrochip CCM (2024)                  | 10.1016/j.heliyon.2024.e37722 | Heliyon (Elsevier)           |
| MVG Cross-Device Augmentation (2025)    | PMC12096352                   | PMC                          |
| EIS Urine Dipstick (2018)               | 10.4155/fsoa-2017-0142        | PMC5961415                   |
| Surkova LED Multisensor Transfer (2020) | 10.1021/acssensors.0c01018    | ACS Sensors                  |
| Shaw NIR Urine (1996)                   | 10.1016/0009-9120(95)02011-X  | Clinical Biochemistry        |
| Human Fluorescent Profile (2020)        | 10.1016/j.bspc.2019.101693    | Biomedical Signal Processing |

---

## 12. Sources

### Primary References (Numbered)

¹ Label-Free Uric Acid Estimation via Portable UV Spectrophotometry. *Sensors* 2022. DOI: [10.3390/s22083009](https://doi.org/10.3390/s22083009)

² SpectraPhone: Smartphone-Based High-Resolution Urinalysis. *Scientific Reports* 2026. DOI: [10.1038/s41598-026-38307-y](https://doi.org/10.1038/s41598-026-38307-y). GitHub: [Uncommon-Sense-Lab/SpectraPhone](https://github.com/Uncommon-Sense-Lab/SpectraPhone.git)

³ Kuenert et al. Continuous Spectroscopic Catheter Monitoring. *Scientific Reports* 2025. DOI: [10.1038/s41598-025-92802-2](https://doi.org/10.1038/s41598-025-92802-2)

⁴ Cancer Detection by Native Fluorescence of Urine (405 nm). *Photochemistry and Photobiology* 2012. DOI: [10.1111/j.1751-1097.2012.01239.x](https://doi.org/10.1111/j.1751-1097.2012.01239.x)

⁵ Body Fluid Fluorescence Signatures. *Scientific Reports* 2023. DOI: [10.1038/s41598-023-30241-7](https://doi.org/10.1038/s41598-023-30241-7)

⁶ Human Fluorescent Profile of Urine. *Biomedical Signal Processing* 2020. DOI: [10.1016/j.bspc.2019.101693](https://doi.org/10.1016/j.bspc.2019.101693)

⁷ Fossati et al. Uric acid absorbance. *Clinical Chemistry* 1980;26(2):227–231

⁸ Portable POC Uric Acid (Uricia). *Biosensors* 2025. DOI: [10.3390/bios16020076](https://doi.org/10.3390/bios16020076)

⁹ Peters T. Protein UV absorption. *Advances in Clinical Chemistry* 1970;13:37–111

¹⁰ Albumin 229 nm absorption in urine. *Spectrochimica Acta A* 2020

¹¹ Tryptophan Fluorescence & Melanoma. *IJMS* 2021. DOI: [10.3390/ijms22041884](https://doi.org/10.3390/ijms22041884)

¹² Bladder Cancer EEM + CNN. *Scientific Reports* 2025. DOI: [10.1038/s41598-025-15801-3](https://doi.org/10.1038/s41598-025-15801-3)

¹³ EEM PARAFAC for urinary metabolites. *ACS Omega* 2023 (PMC10552475)

¹⁴ Electrochemical Creatinine Detection Review. *RSC Advances* 2022. DOI: [10.1039/D2RA04479J](https://doi.org/10.1039/D2RA04479J)

¹⁵ Free AH et al. Urine glucose testing. *Am J Clin Pathol* 1957;27(5):493–500

¹⁶ Fully Electronic Urine Dipstick with EIS. *Future Science OA* 2018. DOI: [10.4155/fsoa-2017-0142](https://doi.org/10.4155/fsoa-2017-0142)

¹⁷ Fraunhofer Label-Free EIS for Uromodulin. Fraunhofer Publications

¹⁸ Shaw et al. NIR Protein/Creatinine/Urea Quantification. *Clinical Biochemistry* 1996. DOI: [10.1016/0009-9120(95)02011-X](https://doi.org/10.1016/0009-9120(95)02011-X)

¹⁹ Pezzaniti et al. NIR Multi-Analyte Urine. *Clinical Biochemistry* 2001. DOI: [10.1016/S0009-9120(01)00198-9](https://doi.org/10.1016/S0009-9120(01)00198-9)

²⁰ Suzuki et al. NIR POC Spot Urine. *Med. Biol. Eng. Comput.* 2020. DOI: [10.1007/s11517-019-02063-1](https://doi.org/10.1007/s11517-019-02063-1)

²¹ Wold et al. Orthogonal Signal Correction. *Chemom. Intell. Lab. Syst.* 1998;44:175–185

²² Afseth & Kohler. EMSC Tutorial. *Chemom. Intell. Lab. Syst.* 2012;117:92–99

²³ Tang et al. CARS-SPA Combination. *Analyst* 2014. DOI: [10.1039/c4an00837e](https://doi.org/10.1039/c4an00837e)

²⁴ Dhanoa et al. SNV-MSC Equivalence. *J. Near Infrared Spectrosc.* 1994

²⁵ Baek et al. arPLS Baseline Correction. *Analyst* 2015;140:250–257

²⁶ Zhang & Mouazen. Fractional-Order SG for Vis-NIR. *Infrared Phys. Technol.* 2023

²⁷ Lemos et al. 1D-CNN vs Chemometrics. *arXiv* 2023. [2301.10746](https://arxiv.org/abs/2301.10746)

²⁸ Fu et al. SpectraTr: Transformer for NIR. *J. Analytical Chemistry* 2022

²⁹ Spectrochip CCM Urinalysis. *Heliyon* 2024. DOI: [10.1016/j.heliyon.2024.e37722](https://doi.org/10.1016/j.heliyon.2024.e37722)

³⁰ Xu & Liang. Monte Carlo Cross-Validation. *J. Chemometrics* 2004

³¹ Kiranyaz et al. 1D-CNN Survey. *Mech. Syst. Signal Process.* 2021

³² Exponential turbidity model for UV-Vis. *Frontiers in Microbiology* 2023

³³ CIE L\*a\*b\* Turbidity Classification. *PLOS One* 2025. DOI: [10.1371/journal.pone.0323351](https://doi.org/10.1371/journal.pone.0323351)

³⁴ Belasco et al. Urine Color and Osmolality. *Frontiers in Nutrition* 2020

³⁵ Carmine TC. V-PFCRC Method. *Scientific Reports* 2025. PMC: [PMC11782553](https://pmc.ncbi.nlm.nih.gov/articles/PMC11782553/)

³⁶ Indoxyl Sulfate and Ammonium Effects on Urine Autofluorescence. *Talanta* 2010;80(3):1269–1276

³⁷ Liu et al. Secondary IFE Correction. *Analytica Chimica Acta* 2023 (PMID 36473295)

³⁸ Sun et al. MicroNIR Transferability. *Molecules* 2019;24:1997

³⁹ Surkova et al. LED Multisensor Calibration Transfer. *ACS Sensors* 2020. DOI: [10.1021/acssensors.0c01018](https://doi.org/10.1021/acssensors.0c01018)

⁴⁰ Leopold-Kerschbaumer et al. MVG Cross-Device Augmentation. *Anal. Chem.* 2025;97(19):10264. PMC: [PMC12096352](https://pmc.ncbi.nlm.nih.gov/articles/PMC12096352/)

⁴¹ Sun et al. CORAL. *arXiv* 2016. [1612.01939](https://arxiv.org/abs/1612.01939)

⁴² Ganin et al. Domain-Adversarial Training. *JMLR* 2016

⁴³ Moyer & Golland. Scanner Invariant Representations. *arXiv* 2021. [2101.06255](https://arxiv.org/abs/2101.06255)

⁴⁴ Erzina et al. WGAN Spectral Augmentation. *Analyst* 2023. DOI: [10.1039/d3an00669g](https://doi.org/10.1039/d3an00669g)

⁴⁵ Diffusion Models for NIR Augmentation. Precision Agriculture 2025

⁴⁶ Bittremieux et al. Cumulative Learning for Small MS Datasets. *Nature Communications* 2020. DOI: [10.1038/s41467-020-19354-z](https://doi.org/10.1038/s41467-020-19354-z)

---

*Generated by Feynman multi-agent research pipeline. 4 parallel research threads, 60+ sources examined, 15 papers downloaded.*
