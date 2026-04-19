---
title: Physics-Grounded Machine Learning for Spectral Analysis
aliases:
  - physics-grounded ML
  - physics-informed spectroscopy
  - PGML
tags:
  - topic/spectroscopy
  - topic/ml
  - topic/chemometrics
  - type/concept
  - status/complete
  - device/jimini
date: 2026-04-19

---

# Physics-Grounded Machine Learning for Spectral Analysis

ML models for UV-Vis/NIR spectroscopy that produce scientifically grounded, physically interpretable predictions — using wavelength bands tied to known absorbers, Beer-Lambert constraints, derived spectral features, or architectures encoding domain knowledge. Context: Jimini pen-sized spectrophotometer with LEDs at 275/365/405/455 nm + white + 1070 nm NIR; sensors covering 321–1078 nm; target analytes in urine. See [[datascience/spectroscopy-biomarkers]] for analyte-specific wavelength assignments, [[signal-processing]] for preprocessing, and [[multi-task-modeling]] for multi-output architectures.

---

## Taxonomy of Approaches

Six distinct strategies for physically grounded spectral models:

```
                    Physics-Grounded Spectral ML
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
    A. Feature           B. Constrained      C. Symbolic
    Engineering          Architecture         Regression
    (human designs       (physics in the      (discover
     domain features)     network itself)      equations)
          │                   │                   │
    └─────┴─────┐      ┌─────┴─────┐      ┌─────┴─────┐
              │      │           │      │           │
          Band       Beer-      Physics  Genetic   Neural
          ratios/    Lambert    loss     programming symbolic
          indices    layers     terms    (PySR)    (NeSymReS)
          │
    ┌─────┴─────────────────────────────────────────────┐
    │             │
    D. Hybrid    E. Post-Hoc      F. Classical
    Physics+Data Explainability   Chemometrics
    (mix physical (SHAP, LIME,    (PLS, MCR-ALS
     & learned)    attribution)    with constraints)
```

---

## Category A: Physics-Informed Feature Engineering

**Core idea:** Engineer features with physical meaning — band ratios that encode known absorber behavior, derivative features that isolate peak shapes, or spectral indices analogous to NDVI.

### Enhanced Beer-Lambert Features (Most Relevant)

**Paper:** arXiv:2509.12253 (2025) — "Physics-engineered Beer-Lambert model for [[glucose]] monitoring via NIR spectroscopy"

**Key finding:** A simple physics-engineered feature set + ridge regression outperformed all tested PINNs for [[glucose]] prediction (13.6 mg/dL RMSE vs. 21+ mg/dL for PINNs).

**Feature design (56 features):**

| Feature type | Count | Physical basis |
|---|---|---|
| Log-absorbance at selected λ | ~10 | Beer-Lambert: A = ε·c·l |
| Wavelength differences ΔA(λᵢ, λⱼ) | ~20 | Differential absorption between bands |
| PMF-weighted features (physiological model) | ~15 | Tissue scattering model weights |
| Ratio features A(λᵢ) / A(λⱼ) | ~10 | Concentration-independent normalization |
| Derivative features dA/dλ | ~5 | Peak shape, inflection points |

**Jimini analyte assignments:**

| LED | Analyte | ε (M⁻¹cm⁻¹) | Physical basis |
|-----|---------|-------------|----------------|
| A₂₇₅ | [[uric-acid\|Uric acid]] | ~11,300 @ 293 nm | π→π* purine transition |
| A₃₆₅ | [[nadh\|NADH]] (excitation proxy) | ~6,220 @ 340 nm | Nicotinamide ring n→π* |
| A₄₀₅ | Porphyrin Soret band | ~500,000 | Porphyrin ring π→π* |
| A₄₅₅ | Bilirubin | ~60,000 @ 453 nm | Extended π-conjugation |

### Spectral Indices as Neural Network Inputs

**Paper:** arXiv:2207.10530 (2022) — NNs spontaneously learn NDVI-like indices in weights.

General absorption-based spectral index:

$$\text{Index}(i,j) = \frac{A(\lambda_i) - A(\lambda_j)}{A(\lambda_i) + A(\lambda_j)}$$

**Urine-specific indices:**
- **Bilirubin index:** $(A_{455} - A_{600}) / (A_{455} + A_{600})$
- **Hemoglobin index:** $(A_{405} - A_{500}) / (A_{405} + A_{500})$
- **Protein index:** $(A_{275} - A_{320}) / (A_{275} + A_{320})$

### Physics-Informed Features (PIFs) — Formal Framework

**Paper:** arXiv:2504.17112 (2025) — Formal PIF framework via Buckingham π theorem.

Form all dimensionally homogeneous combinations of physical quantities as input features. For spectroscopy: peak-to-valley ratios, first/second derivative magnitudes, integrated band areas, fluorescence Stokes shift features. Consistently outperforms raw features and enables ranking that identifies relevant physical mechanisms — especially valuable for small datasets.

### Spectra-Scope: Automated Feature Extraction

**Paper:** arXiv:2603.06011 (2026) — Open-source Python AutoML for spectral data.

Automatically extracts: Gaussian peak fitting (center, width, height), CDF transforms, PCA projections, polynomial fitting coefficients. Models: Random forests + LASSO-Clip-Elastic-Net (LCEN) + fused LASSO (enforces smoothness of selected wavelength regions).

---

## Category B: Physics-Constrained Neural Architectures

### Learnable Beer-Lambert Network (Directly Applicable)

**Paper:** arXiv:2309.16735 (2023) — "Learnable real-time inference of molecular composition from diffuse spectroscopy of brain tissue" (Imperial College / CNRS)

**Architecture:** MLP structured around the differential Beer-Lambert law:
```
ΔA(λ) = Σᵢ εᵢ(λ) · Δcᵢ · l
```

Training uses simulated Beer-Lambert spectral-concentration pairs. The network learns the inverse mapping: spectra → concentrations. Real-time inference (~1000× faster than classical optimization) with accuracy matching classical least-squares fitting.

**For Jimini:** Replace brain chromophores with urine chromophores ([[uric-acid|uric acid]], bilirubin, hemoglobin, [[nadh|NADH]]). Train on simulated Beer-Lambert spectra, fine-tune on real urine data.

### Physics-Constrained Autoencoders for Spectral Unmixing

**Paper:** arXiv:2403.04526 (2024) — Physics-constrained AE for Raman (Imperial College / Oxford)

**Architecture:**
```
Encoder: spectrum → abundances (softmax → non-negative, sum-to-one)
Decoder: abundances × endmembers → reconstructed spectrum
```

Physical constraints embedded: non-negativity (weight clipping in decoder), sum-to-one (softmax in encoder), linear mixing model in decoder (Beer-Lambert for mixtures). The decoder IS the physical mixing model; the encoder learns to invert it. Endmembers discovered by the decoder correspond to pure-component spectra.

**For Jimini:** Urine is a mixture. The autoencoder could decompose each urine spectrum into contributions from known chromophores ([[uric-acid|uric acid]], bilirubin, protein, hemoglobin, urobilinogen) + a "matrix" component.

### Physics-Informed Neural Networks (PINNs) — Caution

Testing from arXiv:2509.12253:

| PINN variant | Physical constraint | RMSE (mg/dL) |
|---|---|---|
| Beer-Lambert PINN | BLL in loss function | 21.3 |
| Scattering PINN | + modified BLL with scattering | 19.8 |
| Full RTE PINN | Radiative transfer equation | 18.5 |
| **Enhanced BLL (features + ridge)** | **Physics in features** | **13.6** |

> [!IMPORTANT]
> For spectroscopy, putting physics into **features** was more effective than putting physics into the **loss function**. PINNs struggled with realistic noise. Architecture-level and feature-level physics (Categories A, B) often outperform loss-function-level physics (PINNs) for spectral problems.

### PhISM: Physics-Informed Spectral Modeling

**Paper:** arXiv:2508.21618 (2025) — Unsupervised deep learning modeling spectrum as a linear combination of continuous basis functions. Enforces spectral smoothness and continuity as physics priors. Disentangles observed spectra into physically meaningful components.

---

## Category C: Symbolic Regression — Equation Discovery

**Core idea:** Discover closed-form equations from spectral data. Output is a human-readable formula, not a neural network.

### Key SR Tools

| Tool | Method | Reference |
|---|---|---|
| **PySR** | Genetic programming + regularization | Cranmer (2023), arXiv:2305.01582 |
| **NeSymReS** | Neural symbolic regression (pre-trained transformer) | Biggio et al. (2021), arXiv:2106.06427 |
| **PhySO** | RL + dimensional analysis | Tenachi et al. (2023) |
| **SyMANTIC** | Parsimonious model discovery | Ohio State/Dow Chemical (2025), arXiv:2502.03367 |

**Paper:** arXiv:2506.01862 (2025) — SR for optical properties. Uses PhySO with reinforcement learning to discover Cauchy-model-like expressions for spectral properties.

**For Jimini:** Apply SR to urine spectral data to discover closed-form relationships, e.g.:
```
[bilirubin] = α · (A₄₅₃ - A₆₀₀) / A₃₂₀ + β
```

The discovered equation is deployable on STM32 without a neural network runtime. SR works best when the underlying relationship is genuinely sparse — which is often the case for Beer-Lambert grounded spectroscopy.

---

## Category D: Hybrid Physics + Data-Driven Models

### Physics-Data Integration for Spectral Unmixing

**Paper:** arXiv:2206.05508 (2022) — Autoencoder where decoder mimics the physical mixing model.

**Decoder variants:**

| Decoder type | Physical model | When to use |
|---|---|---|
| Linear | s = Σ aₖeₖ | Well-mixed solutions (Beer-Lambert) |
| Post-nonlinear | s = f(Σ aₖeₖ) | Scattering effects |
| Bilinear | s = Σ aₖeₖ + Σᵢ<ⱼ aᵢaⱼgᵢⱼ | Fluorescence re-absorption |

**For Jimini:** Urine involves both absorption (linear) and scattering (nonlinear). A hybrid decoder with a linear Beer-Lambert core plus a learned nonlinear scattering correction is physically grounded AND adaptive.

### Physics-Based AI + NN Residual

**Paper:** arXiv:2503.08183 (2025) — Physics model + NN residual:
```
ŷ = f_physics(θ) + f_NN(x; w)
```

The physics model provides the physically grounded baseline; the NN fills in systematic deviations that the physics model cannot capture.

---

## Category E: Explainable Spectral Models (Post-Hoc)

### SHAPCA — SHAP + PCA for Spectral Data

**Paper:** arXiv:2603.19141 (2026, very recent — no independent replication yet)

**Problem:** Standard SHAP on spectral data produces noisy per-wavelength attributions because neighboring wavelengths are highly correlated.

**Solution:**
1. PCA for dimensionality reduction
2. SHAP on PCA components
3. Back-project SHAP values to original wavelength space
4. Result: smooth, consistent attribution maps aligned with known spectral bands

**For Jimini:** Train any model, then use SHAPCA to verify model's important wavelengths match known absorber bands. High SHAP attribution at 453 nm for a bilirubin model confirms it's physically grounded.

### SpecReX — Causal Explanations for Spectroscopy

**Paper:** arXiv:2503.14567 (2025) — Uses actual causality theory to identify spectral features that causally determine classification. Outputs "responsibility maps" linking spectral regions to molecular vibrations.

### Spectral-Zone SHAP

**Paper:** Contreras & Bocklitz, 2024 (Leibniz-IPHT) — Groups wavelengths into physically meaningful spectral zones, computes SHAP values at zone level.

**For Jimini zones:** UV-C (270–290 nm), UV-A (350–380 nm), Soret (395–420 nm), bilirubin (440–470 nm), green valley (500–550 nm), water-NIR (900–1100 nm).

---

## Category F: Classical Chemometrics with Physical Grounding

### PLS with Variable Selection (iPLS, siPLS, CARS)

- **iPLS:** Selects contiguous wavelength intervals — each corresponding to an absorption band
- **siPLS:** Selects combinations of intervals
- **CARS:** Iteratively selects wavelengths with high PLS regression coefficients

Physical grounding: selected intervals can be verified against known absorber spectra.

### MCR-ALS — Most Physically Grounded Classical Method

Decomposes spectral data into pure-component spectra + concentrations:
```
D = C · Sᵀ + E
```

Built-in physical constraints: non-negativity (concentrations and spectra), closure (sum to total), unimodality (single-peaked spectra), known spectra (lock pure-component spectra from library). Directly mirrors Beer-Lambert mixing.

### CLS (Classical Least Squares)

Literally Beer-Lambert in matrix form:
```
A = ε · C · l  →  C = (EᵀE)⁻¹Eᵀ · A / l
```

**Limitation:** Requires that all absorbing species are known and their spectra available. For urine with unknown matrix effects, pure CLS fails — needs hybrid models.

---

## Comparison Matrix

| Approach | Physical grounding | Interpretability | Accuracy | Data needs | Complexity | Best for |
|---|---|---|---|---|---|---|
| **A. Enhanced BLL features + ridge** | ★★★★★ | ★★★★★ | ★★★★ | Low | Low | **Jimini few-LED devices** |
| **A. Spectral indices** | ★★★★★ | ★★★★★ | ★★★ | Low | Low | Quick screening, ratios |
| **B. Learnable BLL network** | ★★★★ | ★★★★ | ★★★★ | Medium | Medium | Real-time multi-analyte |
| **B. Physics-constrained AE** | ★★★★ | ★★★★ | ★★★★★ | Medium | Medium | Spectral unmixing |
| **B. PINNs (loss-function)** | ★★★ | ★★★ | ★★★ | High | High | When physics model is complex |
| **C. Symbolic regression** | ★★★★★ | ★★★★★ | ★★★ | Medium | Medium | Discovering new relationships |
| **D. Hybrid physics+NN** | ★★★★ | ★★★ | ★★★★★ | Medium–High | High | Complex matrices with scattering |
| **E. SHAPCA / SpecReX** | ★★★ (post-hoc) | ★★★★ | N/A (add-on) | N/A | Low | Validating any model |
| **F. PLS + iPLS** | ★★★ | ★★★★ | ★★★★ | Medium | Low | Standard chemometrics |
| **F. MCR-ALS** | ★★★★★ | ★★★★★ | ★★★ | Low–Medium | Medium | Mixture decomposition |
| **F. CLS** | ★★★★★ | ★★★★★ | ★★ | Very low | Very low | Known pure systems only |

---

## Relevance to Jimini Device

### Recommended Layered Architecture

```
Layer 1: Physics-Informed Feature Engineering (Category A)
  │
  │  Raw signals: A(275), A(365), A(405), A(455), A(white@λ), A(1070)
  │  ↓
  │  Derived features:
  │  - Band ratios: A(275)/A(320), A(405)/A(500), A(455)/A(600)
  │  - Normalized indices: (Aᵢ - Aⱼ) / (Aᵢ + Aⱼ)
  │  - Derivatives: dA/dλ from white-LED continuous spectrum
  │  - Spectral integrals: ∫A(λ)dλ over known absorption bands
  │  - Fluorescence features: emission@460nm / excitation@365nm
  │  - Scatter features: A(1070) for turbidity/matrix correction
  │
Layer 2: Physically Constrained Model (Category B or F)
  │
  │  Option A (simplest): Ridge/LASSO on physics features
  │  Option B (richer): Learnable Beer-Lambert MLP
  │  Option C (mixture): Physics-constrained autoencoder
  │
Layer 3: Validation via Explainability (Category E)
  │
  │  SHAPCA or spectral-zone SHAP to verify that
  │  model attributions match known absorber bands
```

### Implementation Priority

1. **CLS / band ratios** — direct Beer-Lambert at known wavelengths; fastest to implement
2. **Add scatter correction** — use A₁₀₇₀ and NIR slope for matrix correction (SNV)
3. **Enhanced BLL features + ridge** — 56-feature approach adapted for Jimini LED set
4. **Symbolic regression (PySR)** — discover closed-form equations; deployable on STM32
5. **Learnable BLL network** — small MLP trained on Beer-Lambert simulations; SHAPCA validation
6. **Physics-constrained autoencoder** — for unknown interferents (medications, dietary chromophores)

### Analyte Feature Recipes

| Analyte | Primary λ | ε (M⁻¹cm⁻¹) | Suggested features |
|---|---|---|---|
| **[[uric-acid\|Uric acid]]** | 275 nm | ~11,300 | A₂₇₅, A₂₇₅/A₃₂₀, A₂₇₅ − α·A₁₀₇₀ (scatter-corrected) |
| **Bilirubin** | 453 nm | ~60,000 | A₄₅₅, (A₄₅₅−A₆₀₀)/(A₄₅₅+A₆₀₀), A₄₅₅/A₄₀₅ |
| **Protein (total)** | 280 nm | ~5,500 (Trp) | A₂₇₅ (proxy), fluorescence ex275/em340 |
| **Hemoglobin** | 405 nm (Soret) | ~128,000 | A₄₀₅, A₄₀₅/A₄₅₅, Q-band doublet 540/575 nm |
| **[[nadh\|NADH]]** | 340 nm abs / 460 nm fluor | ~6,220 | Fluorescence ratio em@460 / ex@365 |
| **[[total-urinary-porphyrin\|Porphyrins]]** | ~405 nm Soret + fluor 620 nm | ~500,000 | Fluor ex405/em620, A₄₀₅/A₄₈₀, 2nd derivative |

**[[creatinin|Creatinine]]** absorbs at 234 nm (below Jimini range). Best approached via EIS conductivity + osmolality proxy. See [[datascience/spectroscopy-biomarkers]] for full [[creatinin|creatinine]] analysis.

---

## Sources

| Paper | Year | ID | Category | Key Contribution |
|---|---|---|---|---|
| Enhanced Beer-Lambert for [[glucose]] | 2025 | arXiv:2509.12253 | A | 56 physics features beat all PINNs |
| NN learning spectral indices | 2022 | arXiv:2207.10530 | A | NNs spontaneously learn NDVI-like indices |
| Physics-informed features (PIFs) | 2025 | arXiv:2504.17112 | A | Formal PIF framework via Buckingham π |
| Spectra-Scope toolkit | 2026 | arXiv:2603.06011 | A | AutoML for interpretable spectral features |
| Learnable Beer-Lambert for brain | 2023 | arXiv:2309.16735 | B | MLP on Beer-Lambert simulations |
| Physics-constrained AE for Raman | 2024 | arXiv:2403.04526 | B | Non-negativity + sum-to-one in autoencoder |
| Principles-driven UV prediction | 2026 | OpenReview ICLR | B | PPA, CLIAS, SCL training constraints |
| PhISM for hyperspectral | 2025 | arXiv:2508.21618 | B | Continuous basis function decomposition |
| SR for optical properties | 2025 | arXiv:2506.01862 | C | PhySO discovers Cauchy-like expressions |
| SR review | 2022 | arXiv:2211.10873 | C | Comprehensive survey |
| Physics+data hyperspectral unmixing | 2022 | arXiv:2206.05508 | D | Decoder = physical mixing model |
| Physics-based AI for optical data | 2025 | arXiv:2503.08183 | D | Physics model + NN residual |
| SHAPCA | 2026 | arXiv:2603.19141 | E | SHAP + PCA backprojection for spectra |
| SpecReX | 2025 | arXiv:2503.14567 | E | Causal XAI for Raman |
| Spectral-zone SHAP | 2024 | Contreras & Bocklitz | E | Grouped spectral explanations |

---

## Gaps

1. **No paper applies physics-constrained ML to LED-based urinalysis.** Learnable BLL (arXiv:2309.16735) covers brain tissue NIR; [[glucose]] PINN (arXiv:2509.12253) covers transcutaneous NIR. Neither addresses discrete-LED excitation in urine.
2. **Fluorescence features are underexplored.** Most papers focus on absorption spectroscopy. Urine fluorescence ([[nadh|NADH]] at 365/460 nm, riboflavin at 370/525 nm) is a major information source that few papers address systematically.
3. **Symbolic regression for biofluids is very new.** The PhySO/PySR applications to optical data are from 2025 — no papers yet apply SR specifically to biofluid UV-Vis data.
4. **Matrix effects in urine are severe.** Physics-grounded models need to account for inner-filter effects, pH-dependent spectral shifts, and variable dilution — most papers assume well-controlled lab conditions. See [[matrix-correction]].
5. **Calibration transfer with physics models.** If model features are truly physically grounded (extinction coefficients, not learned biases), calibration transfer should be easier — but not empirically tested for LED-based devices. See [[calibration-transfer]].
6. **SHAPCA** (arXiv:2603.19141) is from March 2026 — no independent replication yet.
