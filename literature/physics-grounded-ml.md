# Physics-Grounded Machine Learning for Spectral Analysis

**Research question:** What ML models for UV-Vis/NIR spectroscopy produce scientifically grounded, physically interpretable predictions — using wavelength bands tied to known absorbers, Beer-Lambert constraints, derived spectral features, or architectures that encode domain knowledge?

**Context:** Jimini pen-sized spectrophotometer; LEDs at 275/365/405/455 nm + white + 1070 nm NIR; sensors covering 321–1078 nm; target analytes in urine (uric acid, creatinine, bilirubin, protein, NADH, etc.)

**Date:** 2026-04-09  
**Status:** First pass — 25+ sources synthesized

---

## Table of Contents

1. [Taxonomy of Approaches](#1-taxonomy-of-approaches)
2. [Category A: Physics-Informed Feature Engineering](#2-category-a-physics-informed-feature-engineering)
3. [Category B: Physics-Constrained Neural Architectures](#3-category-b-physics-constrained-neural-architectures)
4. [Category C: Symbolic Regression — Equation Discovery from Spectra](#4-category-c-symbolic-regression--equation-discovery-from-spectra)
5. [Category D: Hybrid Physics + Data-Driven Models](#5-category-d-hybrid-physics--data-driven-models)
6. [Category E: Explainable Spectral Models (Post-Hoc Interpretability)](#6-category-e-explainable-spectral-models-post-hoc-interpretability)
7. [Category F: Classical Chemometrics with Physical Grounding](#7-category-f-classical-chemometrics-with-physical-grounding)
8. [Comparison Matrix](#8-comparison-matrix)
9. [Relevance to Jimini Device](#9-relevance-to-jimini-device)
10. [Gaps & Open Questions](#10-gaps--open-questions)
11. [Sources](#11-sources)

---

## 1. Taxonomy of Approaches

The literature reveals six distinct strategies for building physically grounded spectral models. They can be combined — e.g., physics-informed features fed to an interpretable model, or a constrained architecture explained post-hoc via SHAP.

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
    ┌─────┴─────┐      ┌─────┴─────┐      ┌─────┴─────┐
    │           │      │           │      │           │
  Band       Spectral  Beer-     Physics  Genetic   Neural
  ratios     derivatives Lambert   loss   programming symbolic
  indices    peak params layers   terms    (PySR)    (NeSymReS)
          │                   │                   │
          └─────┬─────────────┼───────────────────┘
                │             │
          D. Hybrid      E. Post-Hoc
          Physics+Data   Explainability
          (mix physical  (SHAP, LIME,
           & learned)    attribution)
                │
          F. Classical
          Chemometrics
          (PLS, MCR-ALS
           with constraints)
```

---

## 2. Category A: Physics-Informed Feature Engineering

**Core idea:** Instead of feeding raw spectra to a model, engineer features that have physical meaning — band ratios that encode known absorber behavior, derivative features that isolate peak shapes, or spectral indices analogous to NDVI in remote sensing.

### 2.1 Enhanced Beer-Lambert Features (★ Most Relevant)

**Paper:** "Physics-engineered Beer-Lambert model for glucose monitoring via NIR spectroscopy" (2025, arXiv:2509.12253)

The key finding: **a simple physics-engineered feature set + ridge regression outperformed all tested PINNs** (physics-informed neural networks) for glucose prediction from NIR spectra (13.6 mg/dL RMSE vs 21+ mg/dL for PINNs).

**Feature design (56 features):**

| Feature type | Count | Physical basis |
|---|---|---|
| Log-absorbance at selected λ | ~10 | Beer-Lambert: $A = \varepsilon \cdot c \cdot l$ |
| Wavelength differences $\Delta A(\lambda_i, \lambda_j)$ | ~20 | Differential absorption between bands |
| PMF-weighted features (physiological modeling function) | ~15 | Tissue scattering model weights |
| Ratio features $A(\lambda_i) / A(\lambda_j)$ | ~10 | Concentration-independent normalization |
| Derivative features $dA/d\lambda$ | ~5 | Peak shape, inflection points |

**Why it matters for Jimini:** This is directly applicable. Each LED wavelength in the Jimini device corresponds to a known absorption band:
- $A_{275}$ → uric acid (ε = 11,300 M⁻¹cm⁻¹ at 293 nm)
- $A_{365}$ → NADH excitation proxy
- $A_{405}$ → porphyrin Soret band
- $A_{455}$ → bilirubin (ε = 60,000 M⁻¹cm⁻¹ at 453 nm)

Ratios like $A_{275}/A_{455}$ or $A_{405}/A_{455}$ encode relative concentrations independent of optical path length.

---

### 2.2 Spectral Indices as Neural Network Inputs

**Paper:** "Neural Network Learning of Chemical Bond Representations in Spectral Indices and Features" (2022, arXiv:2207.10530, Univ. Virginia)

**Key insight:** The paper demonstrates that neural networks spontaneously learn spectral index-like features (normalized band ratios) in their weights when classifying materials from hyperspectral data. The classic example is NDVI:

$$\text{NDVI} = \frac{R_{\text{NIR}} - R_{\text{red}}}{R_{\text{NIR}} + R_{\text{red}}}$$

This index is:
- Physically grounded (chlorophyll absorbs red, reflects NIR)
- Concentration-normalized (the ratio cancels path-length effects)
- Discoverable in network weights

**Generalization:** Any absorption-based spectral index of the form:

$$\text{Index}(i,j) = \frac{A(\lambda_i) - A(\lambda_j)}{A(\lambda_i) + A(\lambda_j)}$$

has the same structure. For urine spectroscopy:
- **Bilirubin index:** $(A_{455} - A_{600}) / (A_{455} + A_{600})$ — bilirubin absorbs at 455 nm, not at 600 nm
- **Hemoglobin index:** $(A_{405} - A_{500}) / (A_{405} + A_{500})$ — Soret band vs green valley
- **Protein index:** $(A_{275} - A_{320}) / (A_{275} + A_{320})$ — aromatic amino acid absorption vs baseline

---

### 2.3 Physics-Informed Features (PIFs) — Formal Framework

**Paper:** "Physics-informed features in supervised machine learning" (2025, arXiv:2504.17112, Univ. Genova)

**Formalism:** PIFs are non-linear feature maps constructed by:
1. Identifying relevant physical quantities and their dimensions
2. Forming all dimensionally homogeneous combinations (via Buckingham π theorem)
3. Using these as input features to standard ML models

**Advantage over raw features:** Improved explainability + better performance with small datasets because the feature space is pre-constrained to physically meaningful combinations. The paper demonstrates that PIFs consistently outperform raw features and enable feature ranking that identifies relevant physical mechanisms.

**Application to spectroscopy:** Instead of feeding 288 raw pixel values from C12880MA, construct PIFs like:
- Peak-to-valley ratios at known absorber bands
- First/second derivative magnitudes at expected absorption maxima
- Integrated band areas within physically meaningful windows
- Fluorescence Stokes shift features (excitation at 365 nm, emission at 460 nm for NADH)

---

### 2.4 Spectra-Scope: Automated Feature Extraction

**Paper:** "Spectra-Scope: A toolkit for automated and interpretable characterization of material properties from spectral data" (2026, arXiv:2603.06011)

**Tool:** Open-source Python AutoML framework specifically for spectral data.

**Features extracted automatically:**
- Gaussian peak fitting (center, width, height)
- Cumulative distribution function transforms
- Principal component projections
- Polynomial fitting coefficients
- Nonlinear feature expansion (augmenting with transformed versions)

**Models:** Random forests + LASSO-Clip-Elastic-Net (LCEN) + fused LASSO for interpretable feature selection.

**Significance:** Automates the process of finding which spectral features matter, while keeping the pipeline interpretable. The fused LASSO is particularly useful for spectral data because it enforces smoothness of selected wavelength regions — neighboring wavelengths that carry the same information are grouped together.

---

## 3. Category B: Physics-Constrained Neural Architectures

**Core idea:** Build the physical law directly into the network structure — not just the loss function, but the architecture itself.

### 3.1 Learnable Beer-Lambert Network (★ Directly Applicable)

**Paper:** "Learnable real-time inference of molecular composition from diffuse spectroscopy of brain tissue" (2023, arXiv:2309.16735, Imperial College / CNRS)

**Architecture:**
```
Input: Δ spectrum (spectral changes, 760-900 nm)
  ↓
MLP with ELU activation
  ↓
Output: Δ[HbO₂], Δ[HHb], Δ[oxCCO], Δ[redCCO]
```

**Physical embedding:**
- The model is structured around the differential Beer-Lambert law: $\Delta A(\lambda) = \sum_i \varepsilon_i(\lambda) \cdot \Delta c_i \cdot l$
- Training uses simulated spectral-concentration pairs generated from the Beer-Lambert equation itself
- The network learns the inverse mapping: spectra → concentrations
- Known extinction coefficients $\varepsilon_i(\lambda)$ of oxyhemoglobin, deoxyhemoglobin, and cytochrome-c-oxidase constrain the training data generation

**Key result:** Real-time inference (~1000× faster than traditional optimization) with accuracy matching classical least-squares fitting.

**For Jimini:** The architecture is directly transferable. Replace brain chromophores with urine chromophores:
- Uric acid: $\varepsilon_{275} = 11,300$ M⁻¹cm⁻¹
- Bilirubin: $\varepsilon_{453} = 60,000$ M⁻¹cm⁻¹
- Hemoglobin (contamination): Soret at 405 nm
- NADH: $\varepsilon_{340} \approx 6,220$ M⁻¹cm⁻¹

Train on simulated Beer-Lambert spectra with known concentrations, then fine-tune on real urine data.

---

### 3.2 Physics-Constrained Autoencoders for Spectral Unmixing

**Paper:** "Hyperspectral unmixing for Raman spectroscopy via physics-constrained autoencoders" (2024, arXiv:2403.04526, Imperial College / Oxford)

**Architecture:**
```
Encoder: spectrum → abundances (softmax → non-negative, sum-to-one)
Decoder: abundances × endmembers → reconstructed spectrum
```

**Physical constraints embedded in architecture:**
1. **Non-negativity of endmembers** — weight clipping in decoder to zero-floor
2. **Non-negativity of abundances** — modified tanh activation
3. **Sum-to-one of abundances** — softmax final layer in encoder
4. **Linear mixing model** in decoder: $\hat{s} = \sum_k a_k \cdot e_k$ (Beer-Lambert for mixtures)

**Why this matters:** The decoder *is* the physical mixing model. The encoder learns to invert it. The endmembers $e_k$ discovered by the decoder correspond to pure-component spectra — each one can be identified with a known chemical species.

**For Jimini:** Urine is a mixture. The autoencoder could decompose each urine spectrum into contributions from known chromophores (uric acid, bilirubin, protein, hemoglobin, urobilinogen) + a "matrix" component (water, scattering). The abundances are directly interpretable as (relative) concentrations.

---

### 3.3 Physics-Informed Neural Networks (PINNs) for Spectroscopy

**Paper:** "Physics-engineered Beer-Lambert model..." (arXiv:2509.12253) — tested multiple PINN variants:

| PINN variant | Physical constraint | RMSE (mg/dL) |
|---|---|---|
| Beer-Lambert PINN | BLL in loss function | 21.3 |
| Scattering PINN | + modified BLL with scattering | 19.8 |
| Full RTE PINN | Radiative transfer equation | 18.5 |
| **Enhanced BLL (features + ridge)** | **Physics in features** | **13.6** |

**Takeaway:** For spectroscopy, putting physics into the **features** was more effective than putting physics into the **loss function**. The PINNs struggled with realistic noise conditions. This is an important lesson: architecture-level constraints (Category B.1, B.2) and feature-level physics (Category A) often outperform loss-function-level physics (PINNs) for spectral problems.

---

### 3.4 Principles-Driven ML for UV Spectral Prediction

**Paper:** "Principles-Driven Machine Learning for UV Spectral Prediction" (Submitted to ICLR 2026, Shinohara et al.)

Three physics-inspired training methods:
1. **PPA (Peak Position Awareness):** Explicitly penalizes incorrect peak positions in predicted spectra — because peak position maps to molecular electronic transitions
2. **CLIAS (Curriculum Learning for Interpolated Abstracted Spectra):** Trains on progressively more detailed spectra, starting from coarse band shapes — mirrors how spectroscopists analyze UV spectra (first identify major bands, then fine features)
3. **SCL (Spectrum Curvature Limitation):** Constrains second derivatives of predicted spectra to be physically realistic — prevents unphysical oscillations

**Result:** 10–22% improvement over baselines; outperforms UV-adVISor (previous SOTA).

**Relevance:** The PPA idea is transferable: if your model predicts a spectrum, penalize peak shifts from known positions. For Jimini, if the model predicts an absorbance spectrum of a urine sample, the loss function should penalize deviations from known absorption band positions (275 nm for uric acid, 453 nm for bilirubin, etc.).

---

### 3.5 PhISM: Physics-Informed Spectral Modeling

**Paper:** "Physics-Informed Spectral Modeling for Hyperspectral Imaging" (2025, arXiv:2508.21618)

**Architecture:** An unsupervised deep learning model that:
- Learns continuous spectral basis functions (not discrete channels)
- Disentangles observed spectra into physically meaningful components
- Enforces spectral smoothness and continuity as physics priors

**Key innovation:** Instead of treating each wavelength as an independent feature, PhISM models the spectrum as a linear combination of continuous basis functions — analogous to how physical mixing models work, but with learned basis functions.

---

## 4. Category C: Symbolic Regression — Equation Discovery from Spectra

**Core idea:** Let the ML system discover closed-form mathematical equations from spectral data. The output is a human-readable formula, not a neural network.

### 4.1 Symbolic Regression for Optical Properties

**Paper:** "Modeling the Optical Properties of Biological Structures using Symbolic Regression" (2025, arXiv:2506.01862, CNRS/CONICET)

**Method:** Uses Physical Symbolic Optimization (PhySO) library with:
- Reinforcement learning to explore expression space
- Dimensional analysis to enforce physical consistency
- RNNs to generate candidate expressions iteratively

**Result:** Discovers Cauchy-model-like expressions for spectral properties:
$$n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$$

**For Jimini:** Apply symbolic regression to urine spectral data to discover:
- Closed-form relationships between absorbance at specific wavelengths and biomarker concentrations
- e.g., $[\text{bilirubin}] = \alpha \cdot \frac{A_{453} - A_{600}}{A_{320}} + \beta$
- The discovered equation would be scientifically interpretable and testable against known chemistry

### 4.2 Key SR Tools

| Tool | Method | Reference |
|---|---|---|
| **PySR** | Genetic programming + regularization | Cranmer (2023), arXiv:2305.01582 |
| **NeSymReS** | Neural symbolic regression (pre-trained transformer) | Biggio et al. (2021), arXiv:2106.06427 |
| **PhySO** | RL + dimensional analysis | Tenachi et al. (2023) |
| **SyMANTIC** | Parsimonious model discovery | Ohio State / Dow Chemical (2025), arXiv:2502.03367 |
| **DrSR** | LLM-driven equation discovery | Chinese Academy of Sciences (2025), arXiv:2506.04282 |

### 4.3 Review Paper

**Paper:** "Interpretable Scientific Discovery with Symbolic Regression: A Review" (2022, arXiv:2211.10873, Qatar Computing Research Institute)

Comprehensive survey of SR methods, benchmarks, and applications in science. Key takeaway: SR works best when the underlying relationship is genuinely sparse (few relevant variables, simple functional form) — which is often the case for spectroscopic relationships grounded in Beer-Lambert.

---

## 5. Category D: Hybrid Physics + Data-Driven Models

### 5.1 Physics-Data Integration for Spectral Unmixing

**Paper:** "Integration of Physics-Based and Data-Driven Models for Hyperspectral Image Unmixing" (2022, arXiv:2206.05508, Northwestern Polytechnical / Côte d'Azur)

**Approach:** Autoencoder where:
- **Decoder mimics the physical mixing model** (linear or nonlinear)
- **Encoder is a learned inverse** (data-driven)
- The decoder design encodes the specific physics: linear mixing, post-nonlinear, bilinear, etc.

**Decoder variants:**

| Decoder type | Physical model | When to use |
|---|---|---|
| Linear | $s = \sum_k a_k e_k$ | Well-mixed solutions (Beer-Lambert) |
| Post-nonlinear | $s = f(\sum_k a_k e_k)$ | Scattering effects |
| Bilinear | $s = \sum_k a_k e_k + \sum_{i<j} a_i a_j g_{ij}$ | Fluorescence re-absorption |
| Generalized additive | $s = \sum_k a_k e_k + h(a_1,...,a_K)$ | Unknown nonlinearities |

**For Jimini:** Urine spectra involve both absorption (linear) and scattering (nonlinear). A hybrid decoder that uses a linear Beer-Lambert core plus a learned nonlinear scattering correction would be physically grounded AND adaptive to real-world data.

---

### 5.2 Spectral Unmixing with Physics-Constrained Autoencoders

**Paper:** See Section 3.2 above (arXiv:2403.04526). This overlaps with both B and D — the autoencoder is constrained by physics but uses learned components.

---

### 5.3 Physics-Based AI for Material Parameter Extraction

**Paper:** "Physics-based AI methodology for Material Parameter Extraction from Optical Data" (2025, arXiv:2503.08183, Eindhoven)

**Approach:** Integrates classical optimization (Levenberg-Marquardt) with neural network for spectroscopic optical data inversion. The NN learns the residual that the physics model cannot capture.

**Architecture:** Physics model + NN residual:
$$\hat{y} = f_{\text{physics}}(\theta) + f_{\text{NN}}(x; w)$$

The physics model provides the physically grounded baseline; the NN fills in systematic deviations.

---

## 6. Category E: Explainable Spectral Models (Post-Hoc Interpretability)

These methods don't constrain the model itself but explain its predictions in physically meaningful terms after training.

### 6.1 SHAPCA — SHAP + PCA for Spectral Data (★ Very Recent)

**Paper:** "SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data" (2026, arXiv:2603.19141)

**Problem:** Standard SHAP on spectral data produces noisy per-wavelength attributions because neighboring wavelengths are highly correlated.

**Solution:** SHAPCA pipeline:
1. PCA for dimensionality reduction
2. SHAP on PCA components
3. Back-project SHAP values to original wavelength space
4. Result: smooth, consistent attribution maps that align with known spectral bands

**For Jimini:** Train any model (even a black-box); then use SHAPCA to verify that the model's important wavelengths match known absorber bands. If a model for bilirubin prediction has high SHAP attribution at 453 nm — it's physically grounded. If attribution is at 600 nm — something is wrong.

---

### 6.2 SpecReX — Causal Explanations for Spectroscopy

**Paper:** "SpecReX: Explainable AI for Raman Spectroscopy" (2025, arXiv:2503.14567, UCL / King's College)

**Method:** Uses actual causality theory (not just correlation-based SHAP) to identify which spectral features causally determine the classification. Iteratively mutates parts of the spectrum and tests if the classification changes.

**Output:** "Responsibility maps" showing which spectral regions are causally responsible for the prediction — directly linkable to molecular vibrations/absorptions.

---

### 6.3 Spectral-Zone SHAP

**Paper:** "Spectral zones based SHAP: enhancing interpretability in spectral deep learning models" (2024, Contreras & Bocklitz, Leibniz-IPHT)

**Key innovation:** Groups wavelengths into physically meaningful spectral zones (e.g., amide I region 1600–1700 cm⁻¹, CH stretching 2800–3000 cm⁻¹) and computes SHAP values at the zone level. This:
- Reduces noise from correlated wavelengths
- Provides explanations in terms of known spectral features
- Matches how spectroscopists actually think

**For Jimini:** Define zones: UV-C (270–290 nm), UV-A (350–380 nm), Soret (395–420 nm), bilirubin (440–470 nm), green valley (500–550 nm), water-NIR (900–1100 nm). Compute zone-level SHAP values.

---

## 7. Category F: Classical Chemometrics with Physical Grounding

These are the established methods that the Jimini device likely already uses to some extent. They remain competitive baselines.

### 7.1 PLS with Variable Selection (iPLS, siPLS, CARS)

**Partial Least Squares** with interval-based variable selection:
- **iPLS:** Selects contiguous wavelength intervals — each interval corresponds to an absorption band
- **siPLS:** Synergy iPLS — selects combinations of intervals
- **CARS (Competitive Adaptive Reweighted Sampling):** Iteratively selects wavelengths, favoring those with high PLS regression coefficients

**Physical grounding:** The selected intervals can be verified against known absorber spectra. If iPLS selects 440–470 nm for bilirubin prediction, that's physically meaningful.

### 7.2 MCR-ALS (Multivariate Curve Resolution — Alternating Least Squares)

**MCR-ALS** decomposes spectral data into pure-component spectra + concentrations:
$$D = C \cdot S^T + E$$

**Built-in physical constraints:**
- Non-negativity (concentrations and spectra can't be negative)
- Closure (concentrations sum to total)
- Unimodality (spectral peaks are single-peaked)
- Known spectra (lock pure-component spectra from library)

**This is the most physically grounded classical method** because the decomposition directly mirrors Beer-Lambert mixing.

### 7.3 CLS (Classical Least Squares) / ILS (Inverse Least Squares)

**CLS** is literally Beer-Lambert in matrix form:
$$A = \varepsilon \cdot C \cdot l \implies C = (E^T E)^{-1} E^T \cdot A / l$$

where $E$ is the matrix of known extinction coefficients.

**Limitation:** Requires that all absorbing species are known and their spectra available. For urine (unknown matrix effects, scattering, fluorescence), pure CLS fails — you need CLS + correction terms, which leads back to hybrid models (Section 5).

---

## 8. Comparison Matrix

| Approach | Physical grounding | Interpretability | Accuracy | Data needs | Complexity | Best for |
|---|---|---|---|---|---|---|
| **A. Enhanced BLL features + ridge** | ★★★★★ | ★★★★★ | ★★★★ | Low | Low | **Few-LED devices like Jimini** |
| **A. Spectral indices** | ★★★★★ | ★★★★★ | ★★★ | Low | Low | Quick screening, ratios |
| **B. Learnable BLL network** | ★★★★ | ★★★★ | ★★★★ | Medium | Medium | Real-time multi-analyte |
| **B. Physics-constrained AE** | ★★★★ | ★★★★ | ★★★★★ | Medium | Medium | Spectral unmixing |
| **B. PINNs (loss-function)** | ★★★ | ★★★ | ★★★ | High | High | When physics model is complex |
| **C. Symbolic regression** | ★★★★★ | ★★★★★ | ★★★ | Medium | Medium | Discovering new relationships |
| **D. Hybrid physics+NN** | ★★★★ | ★★★ | ★★★★★ | Medium-High | High | Complex matrices with scattering |
| **E. SHAPCA / SpecReX** | ★★★ (post-hoc) | ★★★★ | N/A (add-on) | N/A | Low | Validating any model |
| **F. PLS + iPLS** | ★★★ | ★★★★ | ★★★★ | Medium | Low | Standard chemometrics |
| **F. MCR-ALS** | ★★★★★ | ★★★★★ | ★★★ | Low-Medium | Medium | Mixture decomposition |
| **F. CLS** | ★★★★★ | ★★★★★ | ★★ | Very low | Very low | Known pure systems only |

---

## 9. Relevance to Jimini Device

### 9.1 Recommended Architecture

For the Jimini pen spectrophotometer with discrete LED wavelengths, the **most physically grounded AND practical** approach is a layered architecture:

```
Layer 1: Physics-Informed Feature Engineering (Category A)
  │
  │  Raw signals: A(275), A(365), A(405), A(455), A(white@λ), A(1070)
  │  ↓
  │  Derived features:
  │  - Band ratios: A(275)/A(320), A(405)/A(500), A(455)/A(600)
  │  - Normalized indices: (A_i - A_j) / (A_i + A_j)
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

### 9.2 Specific Feature Recipes for Jimini Analytes

#### 9.2.1 Directly Absorbing Analytes (Beer-Lambert accessible)

| Analyte | Primary λ | Physical basis | ε (M⁻¹cm⁻¹) | Suggested features |
|---|---|---|---|---|
| **Uric acid** | 275 nm | π→π* transition of purine ring | ~11,300 @ 293 nm | $A_{275}$, $A_{275}/A_{320}$, $A_{275} - \alpha \cdot A_{1070}$ (scatter-corrected) |
| **Bilirubin** | 453 nm | Extended π-conjugation absorption | ~60,000 @ 453 nm | $A_{455}$, $(A_{455}-A_{600})/(A_{455}+A_{600})$, $A_{455}/A_{405}$ |
| **Protein (total)** | 280 nm | Trp/Tyr aromatic side chains | ~5,500 (Trp) @ 280 nm | $A_{275}$ (proxy), $A_{275}/A_{260}$, integrated band 260–290 nm |
| **Hemoglobin / RBC** | 405, 540, 575 nm | Porphyrin Soret + Q-bands | ~128,000 @ 405 nm (Soret) | See Section 9.2.3 below |
| **NADH** | 340 nm (abs) / 460 nm (fluor) | Nicotinamide ring n→π* | ~6,220 @ 340 nm | Fluorescence ratio: em@460 / ex@365 |

#### 9.2.2 Weakly or Indirectly Absorbing Analytes

| Analyte | Spectral signature | Physical basis | Suggested features | Difficulty |
|---|---|---|---|---|
| **Creatinine** | ~234 nm (weak), NIR C-H/N-H overtones | Creatinine absorbs in deep-UV only: maxima at 190 nm and 234 nm (NIST data; ε ~6,500 @ 234 nm). Below Jimini's 275 nm LED. In NIR (1500–2200 nm), creatinine shows N-H and C-H combination bands used for PLS regression in literature. | $A_{275}$ residual after uric acid subtraction; NIR features from C14 sensor if ≥1000 nm; **EIS features** (creatinine affects ionic conductivity); spectral baseline slope (creatinine contributes to overall solute load) | **Hard** — no direct LED match. Most successful reagentless approaches use NIR PLS (Shaw et al. 1996, Koschack et al. 2001). EIS or indirect estimation via osmolality normalization recommended. |
| **Osmolality** | Broadband: NIR water absorption, refractive index, total scattering | Osmolality measures total dissolved solute concentration (mOsm/kg). Correlates linearly with specific gravity (SG) and refractive index (RI). Water absorption bands at ~970 nm and ~1200 nm shift with solute concentration. Total absorbance baseline and scatter intensity scale with dissolved solids. | $A_{1070}$ (water band edge + scatter), spectral baseline integral $\int A(\lambda) d\lambda$ across 400–850 nm, NIR slope $dA/d\lambda$ in 800–1050 nm region, **EIS conductivity** (osmolality ≈ 1.86 × conductivity in mmol/L), ratio $A_{1070}/A_{600}$ | **Medium** — EIS conductivity is the most direct physical measurement. Optical proxy via total spectral baseline + NIR water band perturbation is feasible as supporting feature. Voinescu et al. (2002) showed SG ≈ osmolality/40 + 1.000. |

#### 9.2.3 Red Blood Cells (Erythrocytes / Hematuria)

**Physical basis:** RBCs contain hemoglobin, which has one of the strongest and most distinctive absorption spectra of any biological molecule.

**Hemoglobin absorption bands:**

| Band | λ (nm) | ε (M⁻¹cm⁻¹) | Physical origin | Jimini LED coverage |
|---|---|---|---|---|
| **Soret (γ)** | 405–415 nm | ~128,000 (oxyHb @ 415 nm) | Porphyrin ring π→π* | ★ 405 nm LED direct hit |
| **Q-band α** | 540–542 nm | ~14,300 (oxyHb) | Vibronic coupling | White LED continuous spectrum |
| **Q-band β** | 576–578 nm | ~15,400 (oxyHb) | Electronic Q-band | White LED continuous spectrum |
| **Deoxy valley** | ~560 nm | ~8,000 (deoxyHb) | Reduced porphyrin | White LED |
| **NIR** | 750–1000 nm | ~700–2,000 | Weak d-d transitions | C14 sensor range |

**Suggested features:**
- $A_{405}$ — **primary indicator**, direct Soret band measurement
- $A_{405}/A_{455}$ — discriminates hemoglobin (high) from bilirubin (high at 455) 
- $(A_{405} - A_{500}) / (A_{405} + A_{500})$ — hemoglobin index; normalized, path-length-independent
- $A_{540}$ and $A_{575}$ from white-LED continuous spectrum — Q-band doublet confirms Hb vs non-specific absorption
- **Oxy vs deoxy discrimination:** $(A_{540} - A_{560}) / (A_{540} + A_{560})$ — positive for oxyHb (double Q-peak), near zero for deoxyHb (single broad peak)
- Scatter features: intact RBCs scatter more than lysed hemoglobin; $A_{1070}$ increases with intact cell count (Mie scattering, cell diameter ~7 µm)

**Physical model:** At Jimini concentrations, Beer-Lambert applies well. Hemoglobin at clinical hematuria levels (>5 RBC/µL ≈ >0.15 mg/dL free Hb) is detectable by Soret absorption. The Soret band is so intense that even trace hemoglobin (<5 RBC/µL) produces measurable signal at 405 nm.

#### 9.2.4 White Blood Cells (Leukocytes / Pyuria)

**Physical basis:** WBCs (primarily neutrophils in UTI) do NOT have a distinctive absorption spectrum like hemoglobin. Their optical signatures are primarily:

1. **Scattering** — WBCs are large cells (~10–15 µm), causing Mie scattering. More WBCs → higher turbidity.
2. **Nucleic acid absorption** — WBCs have a nucleus (unlike RBCs), contributing to UV absorption at ~260 nm from DNA/RNA.
3. **Leukocyte esterase (LE)** — enzyme released by WBCs; can be detected spectrophotometrically at ~405 nm after reaction with indoxyl ester substrates (dipstick chemistry). Without reagents, LE is not directly visible.
4. **Fluorescence** — WBC pyridine nucleotides (NADH/NADPH) fluoresce at 340ex/460em; elevated WBC counts increase overall autofluorescence.

**Suggested features (reagentless):**
- $A_{1070}$ — primary turbidity/scatter indicator (WBCs + bacteria + RBCs all contribute)
- $A_{260}$ or $A_{275}$ residual — after subtracting expected uric acid contribution, excess UV absorption may indicate nucleic acids from WBCs
- Fluorescence intensity at ex365/em460 — NADH/NADPH from viable leukocytes; higher WBC → higher fluorescence (must separate from free-urinary NADH)
- **Spectral scatter slope:** $\log(A_{400}/A_{800})$ — Mie scattering from cells is wavelength-dependent ($\propto \lambda^{-\alpha}$ with $\alpha \approx 0.5$–2 for cells vs $\alpha = 4$ for Rayleigh); the slope encodes particle size information
- **EIS features** — intact cells in suspension alter impedance at specific frequencies (cell membrane capacitance); WBC concentration detectable via multi-frequency EIS

**Confidence:** **Low for direct spectral quantification.** WBC counting from absorption spectroscopy alone is unreliable without reagents. The Vis-NIR study by Monteiro-Silva et al. (2022, 2024) used Vis-NIR spectroscopy to count WBCs in whole blood, achieving R² ~0.85 using PLS on 400–1000 nm spectra — but in urine, WBC concentrations are much lower and the scattering signal is confounded by bacteria and crystals. **Best approached as a classification problem** (pyuria yes/no) rather than quantification, using scatter + fluorescence features combined.

#### 9.2.5 Bacteria Count (Bacteriuria)

**Physical basis:** Bacteria in urine (primarily E. coli, Klebsiella, Enterococcus) produce optical signals via:

1. **Turbidity / scattering** — bacterial cells (~1 µm) cause Mie scattering. Clinically significant bacteriuria (>10⁵ CFU/mL) produces detectable turbidity.
2. **UV absorption** — bacterial nucleic acids absorb at 260 nm; bacterial proteins absorb at 280 nm. At >10⁵ CFU/mL, this is measurable.
3. **Autofluorescence** — bacteria contain tryptophan (ex280/em340), NADH (ex340/em460), and flavins (ex450/em525). These provide species-discriminating fluorescent signatures (Sahar et al., 2023, Nature Sci. Rep.).
4. **Nitrite production** — Gram-negative bacteria reduce nitrate to nitrite; nitrite has weak UV absorption but is better detected by Griess reaction (colorimetric, requires reagent).
5. **Laser scattering patterns** — forward/side scatter intensity encodes cell size and morphology. Giana et al. (2022, PMC8941854) used laser scattering + deep learning for rapid bacterial detection in urine.

**Suggested features (reagentless):**
- $A_{1070}$ — turbidity proxy (most direct physical measurement of bacterial load)
- **Mie scatter wavelength dependence:** $A_{400}/A_{800}$ slope — bacteria (~1 µm) produce a different scatter slope than WBCs (~12 µm) or crystals (~10–50 µm)
- **UV excess:** $A_{275}$ residual after uric acid model subtraction — excess UV absorption may indicate bacterial nucleic acids + proteins
- **Fluorescence signatures:**
  - ex275/em340 → tryptophan (bacterial protein content)
  - ex365/em460 → NADH (metabolically active bacteria)
  - ex455/em525 → flavins (FAD/FMN — more specific to bacteria than human cells)
- **EIS features** — bacteria alter conductivity and impedance at kHz–MHz frequencies (cell membrane capacitance of bacteria differs from eukaryotic cells due to cell wall)
- **Temporal features:** if sequential measurements are possible, bacterial growth causes time-dependent increases in turbidity and fluorescence

**Physical model:** Mendes et al. (2025, MDPI Sensors 25/2/400) developed a ratiometric fluorescence methodology for UTI detection combining multiple excitation/emission pairs. The fluorescence ratios are physically grounded in the different fluorophore compositions of bacteria vs human cells.

**Confidence:** **Medium for >10⁵ CFU/mL detection; low for quantification.** Scatter + fluorescence multi-feature models can achieve ~80–90% sensitivity for UTI screening (bacteriuria + pyuria combined). Pure spectral quantification of CFU/mL is unreliable without cell counting/flow cytometry.

#### 9.2.6 Creatinine — Expanded Analysis

**Spectral properties of pure creatinine:**

| Property | Value | Source |
|---|---|---|
| UV max 1 | 190 nm | NIST WebBook |
| UV max 2 | 234 nm | NIST WebBook, SIELC |
| ε @ 234 nm | ~6,500 M⁻¹cm⁻¹ (estimated) | Literature |
| ε @ 275 nm | **<100 M⁻¹cm⁻¹** (negligible) | — |
| NIR bands | 1550–1600 nm (N-H stretch), 2100–2200 nm (combination) | Shaw et al. (1996) |
| Raman | 680, 850 cm⁻¹ (ring breathing) | RSC Advances (2016) |

**The creatinine problem:** At 275 nm (the shortest Jimini LED), creatinine is essentially transparent. Its primary UV absorption at 234 nm falls below the device range. Normal urine creatinine concentration (3–30 mmol/L) is high, but without spectral access to 234 nm, direct Beer-Lambert quantification is not possible.

**Indirect estimation strategies (ranked by physical grounding):**

1. **NIR spectroscopy (PLS on C14 sensor):** Shaw et al. (1996, Clinical Biochemistry) and Koschack et al. (2001) demonstrated NIR PLS estimation of urine creatinine using the 1500–2200 nm region. The C14384MA sensor reaches only 1050 nm — **insufficient** for primary NIR creatinine bands. However, weak overtone features may exist in the 900–1050 nm region.

2. **EIS-based estimation:** Creatinine is a zwitterion that affects urine conductivity. EIS at 1–100 kHz can measure ionic strength, and creatinine contributes to the total dissolved solute load. Combined with osmolality proxy, an indirect creatinine estimate is feasible. **This is the most promising route for Jimini.**

3. **Spectral residual method:** If all other major UV absorbers (uric acid, protein, bilirubin, hemoglobin) are quantified and subtracted from the total UV spectrum, the residual carries information about creatinine + other unquantified analytes. This is physically grounded (mass balance) but sensitive to errors in the primary analyte models.

4. **Creatinine-to-SG ratio:** Creatinine correlates with specific gravity (both measure solute concentration). If osmolality/SG is estimated optically (Section 9.2.2), creatinine can be regressed from it. Approximate relationship: creatinine (mmol/L) ≈ f(SG, conductivity). Weak physical grounding — empirical correlation, not direct measurement.

5. **Jaffe reaction (requires reagent):** Creatinine + alkaline picrate → yellow-red complex absorbing at 492–520 nm. This is the clinical standard but **requires a reagent** — violates the reagentless constraint. Mentioned for completeness.

#### 9.2.7 Osmolality — Expanded Analysis

**Physical basis:** Osmolality (mOsm/kg) measures total dissolved solute particles per kg of water. It is not a single molecular species — it's a colligative property determined by all dissolved solutes (urea, NaCl, KCl, creatinine, glucose, etc.).

**Optical correlates:**

| Observable | Physical mechanism | λ range | Strength |
|---|---|---|---|
| **Refractive index** | Total dissolved solids increase RI (ΔRI ≈ 1.5×10⁻⁶ per mOsm/kg) | All | Strong but requires refractometer |
| **NIR water absorption** | O-H stretching bands (~970 nm, ~1200 nm, ~1450 nm) shift and broaden with solute concentration | 900–1500 nm | Medium |
| **Baseline absorbance** | Total dissolved solids increase baseline optical density across all wavelengths | 400–1070 nm | Weak-Medium |
| **EIS conductivity** | Ionic solutes dominate conductivity; osmolality ≈ 1.86 × conductivity (mS/cm) for dilute electrolytes | — | **Strong** |
| **Spectral slope** | Scatter from dissolved macromolecules (proteins, mucoproteins) increases with concentration | NIR | Weak |

**Suggested features:**
- **EIS conductivity at 10–100 kHz** — most direct physical correlate; conductivity is a colligative property like osmolality
- $A_{1070}$ — NIR baseline, sensitive to total dissolved solids + scatter
- $\int A(\lambda) d\lambda$ over 400–850 nm — total spectral area scales with total absorber/scatterer load
- $A_{970}$ from C12880MA sensor — water O-H overtone band; shape changes with osmolality (requires spectral resolution)
- $dA/d\lambda$ in 900–1050 nm — NIR slope encodes total dissolved solids

**Model architecture:** Multi-input regression combining EIS conductivity (primary) + spectral features (secondary):
$$\text{osmolality} \approx \beta_0 + \beta_1 \cdot \sigma_{10\text{kHz}} + \beta_2 \cdot A_{1070} + \beta_3 \cdot \int A \, d\lambda$$

This is physically grounded because conductivity IS a colligative property (like osmolality), and the spectral terms capture the non-ionic dissolved species that conductivity misses (e.g., glucose, urea which are osmotically active but poorly conducting).

#### 9.2.8 Porphobilinogen (PBG)

**Physical basis:** PBG is a pyrrole monomer and heme precursor. Elevated urinary PBG is the hallmark of acute porphyria attacks.

**Spectral properties:**

| Property | Value | Notes |
|---|---|---|
| UV absorption max | ~240 nm | Below Jimini's 275 nm range |
| ε @ 240 nm | ~2,800 M⁻¹cm⁻¹ | Weak in native form |
| Ehrlich reaction product (p-DMAB) | 555 nm (pink-red) | Requires reagent (p-dimethylaminobenzaldehyde) |
| **Conversion to uroporphyrin (by heating)** | Soret at ~405 nm, fluorescence at ~620 nm | PBG spontaneously polymerizes to uroporphyrinogen → uroporphyrin on standing/heating |

**The PBG opportunity for Jimini:** PBG itself is spectrally invisible at Jimini wavelengths. However, in urine samples from acute porphyria patients, PBG concentration is extremely high (10–200 mg/L vs normal <2 mg/L) and the sample **darkens on standing** as PBG auto-polymerizes to porphyrins. This means:

1. **Fresh urine:** PBG is invisible at 405 nm. Only indirect detection via its contribution to total UV absorption (weak).
2. **Aged urine (>1 hr):** PBG converts to uroporphyrin, which absorbs at 405 nm (Soret) and fluoresces at 620 nm. This is directly detectable.
3. **Forced conversion:** Acidification + heating (not reagentless but mild) accelerates PBG → uroporphyrin conversion. The JBO paper (Mateen et al., 2018) demonstrated rapid spectrophotometric PBG quantification via this conversion.

**Suggested features (aligned with V20 objectives: abs 405/480, R405 HDR VIDS VIS):**
- $A_{405}$ — Soret band of porphyrins formed from PBG polymerization
- $A_{405}/A_{480}$ — discriminates porphyrin (peak at 405) from bilirubin (broad 450–480)
- $A_{405}$ time-series if sequential measurements available — rate of darkening correlates with PBG concentration
- Fluorescence: ex405/em620 — porphyrin fluorescence is highly specific; PBG-derived uroporphyrin fluoresces at ~618–625 nm when excited at ~405 nm
- $A_{405}$ from **R405 HDR** (high dynamic range at 405 nm) — high-sensitivity Soret measurement

**Confidence:** **Medium for binary detection of acute porphyria** (PBG >20 mg/L typically detectable via porphyrin conversion products). Quantitative PBG estimation without reagents is difficult.

#### 9.2.9 Porphyrins (Coproporphyrin, Uroporphyrin)

**Physical basis:** Porphyrins are tetrapyrrole macrocycles with one of the most distinctive spectral signatures in biology: an intense Soret (B) band ~400–410 nm and weaker Q-bands at 500–630 nm. They are intensely fluorescent.

**Spectral properties (in acidic aqueous solution):**

| Porphyrin | Soret λ (nm) | ε Soret (M⁻¹cm⁻¹) | Q-bands (nm) | Fluorescence em (nm) | Normal urine |
|---|---|---|---|---|---|
| **Coproporphyrin III** | 401 | ~500,000 | 497, 531, 565, 621 | 596, 652 | 10–200 µg/day |
| **Uroporphyrin III** | 398–405 | ~500,000 | 501, 535, 568, 623 | 618, 675 | 4–46 µg/day |
| **Protoporphyrin IX** | 406 | ~420,000 | 505, 540, 576, 630 | 632, 695 | Trace |

**Key insight:** Porphyrins have **the highest molar absorptivity of any biological molecule** in the Soret region (~500,000 M⁻¹cm⁻¹ — 4× higher than hemoglobin). Even at µg/L concentrations in urine, they produce measurable Soret absorption and strong fluorescence. The 405 nm Jimini LED is an almost perfect match for porphyrin Soret excitation.

**Suggested features:**
- $A_{405}$ — direct Soret band (shared with hemoglobin — disambiguation needed)
- $A_{405}/A_{540}$ — porphyrins have Q-band at ~500–540 nm; hemoglobin also absorbs at 540 nm but with different ratio
- **Fluorescence: ex405/em620** — **highly specific for porphyrins**. Hemoglobin does NOT fluoresce (paramagnetic quenching). Bilirubin fluoresces weakly at ~520 nm, not 620 nm. A 620 nm emission upon 405 nm excitation is essentially pathognomonic for porphyrins.
- Fluorescence: ex405/em595 vs ex405/em620 — ratio distinguishes coproporphyrin (em 596 nm) from uroporphyrin (em 618 nm)
- Second-derivative spectroscopy: $d²A/d\lambda²$ at 398–410 nm resolves porphyrin Soret from hemoglobin Soret (slightly shifted peaks)

**Confidence:** **High for detection; medium for quantification.** Porphyrin fluorescence at ex405/em620 is one of the cleanest spectroscopic signatures available — if the Jimini device captures fluorescence at 620 nm (within C12880MA range at 340–850 nm), porphyrin detection is straightforward. Buttery et al. (1995, Clinical Chemistry) demonstrated quantitative uroporphyrin/coproporphyrin fractionation in urine by second-derivative spectroscopy in the Soret region.

#### 9.2.10 Epithelial Cells (epiCells)

**Physical basis:** Epithelial cells in urine (squamous, transitional/urothelial, renal tubular) are large cells (20–60 µm squamous, 12–30 µm transitional). They have no distinctive absorption chromophore.

**Optical signatures:**
1. **Scattering** — large cells cause significant Mie scattering, similar to WBCs but larger → different angular scatter pattern
2. **Autofluorescence** — epithelial cells contain NADH, FAD, keratin, and tryptophan. Multispectral autofluorescence imaging can distinguish renal from squamous epithelial cells (Banten et al., 2021, Nature Sci. Rep.).
3. **No unique absorption band** — unlike hemoglobin or porphyrins

**Suggested features (reagentless):**
- $A_{1070}$ — turbidity/scatter (contributes to total particulate signal along with WBCs, bacteria, crystals)
- Scatter slope: $A_{400}/A_{800}$ — large cells (~30–60 µm) produce a shallow scatter slope ($\alpha < 1$)
- Fluorescence: ex365/em460 (NADH), ex455/em525 (FAD) — similar to WBCs, not specific
- **Discrimination from WBC/bacteria/crystals is the main challenge** — epithelial cells are larger than all other particulates and may be separable by the wavelength dependence of scatter

**Confidence:** **Very low for standalone detection.** Epithelial cells cannot be reliably detected or quantified by bulk UV-Vis spectroscopy in urine. They contribute to total scatter signal but cannot be distinguished from WBCs, bacteria, or crystals without microscopy or flow cytometry. The V20 objectives note "no a priori specs" and "JC disagrees" — suggesting this is acknowledged as a stretch target. **Best treated as a scatter-correlated auxiliary feature**, not a primary spectroscopic target.

#### 9.2.11 Crystals

**Physical basis:** Urinary crystals (calcium oxalate monohydrate/dihydrate, uric acid, struvite, cystine, calcium phosphate) are solid particles of 10–100+ µm. They produce:

1. **Strong Mie scattering** — the dominant optical signature. Crystals are larger than cells and highly refractive.
2. **Birefringence** — many crystals are birefringent under polarized light (used in microscopy). Not exploitable with LEDs in transmission mode.
3. **Specific IR absorption** — calcium oxalate and uric acid crystals have distinct mid-IR and far-IR absorption bands (FEWS spectroscopy, RSC 2019), but these are outside Jimini's spectral range.
4. **UV absorption (uric acid crystals)** — uric acid crystals dissolving in the sample absorb at 275 nm, but this is indistinguishable from dissolved uric acid.

**Suggested features (reagentless):**
- $A_{1070}$ — primary indicator (large scatter contribution from solid particles)
- **Scatter wavelength dependence:** crystals (10–100 µm) produce essentially wavelength-independent scatter in the visible range (geometric optics regime: size >> λ), unlike cells or bacteria. The ratio $A_{800}/A_{400}$ approaching 1.0 suggests large particles (crystals).
- $A_{1070}$ vs $A_{275}$ — uric acid crystals contribute to both scatter AND UV absorption; calcium oxalate crystals contribute to scatter only. If $A_{1070}$ is high but $A_{275}$ is NOT elevated → calcium oxalate. If both high → uric acid crystals possible.
- **EIS features** — crystals do not conduct electricity; high crystal content may reduce conductivity at high frequencies

**Confidence:** **Low for crystal type identification; medium for binary presence detection (≥+).** Bulk spectroscopy can detect elevated turbidity from crystals but cannot distinguish crystal type without microscopy. Cross-reactivity with WBCs and bacteria makes isolated crystal detection unreliable. The V20 objective is binary (≥+), which is more feasible.

#### 9.2.12 Nitrites

**Physical basis:** Nitrites (NO₂⁻) in urine indicate bacterial reduction of dietary nitrate — a marker for Gram-negative UTI. Nitrite itself is a weak UV absorber.

**Spectral properties:**
- Nitrite ion absorbs in deep UV at ~210 nm and ~354 nm (weak, ε ~23 M⁻¹cm⁻¹ at 354 nm) — essentially invisible at Jimini concentrations
- **Griess reaction product:** azo dye at **540 nm** (ε ~40,000 M⁻¹cm⁻¹) — requires sulfanilamide + NED reagent, NOT reagentless
- In the absence of Griess reagent, nitrite is spectrally silent at Jimini wavelengths

**Suggested features (reagentless — indirect only):**
- **No direct spectral measurement possible.** Nitrite is a proxy for bacteriuria → approach via bacterial detection features instead (Section 9.2.5)
- Bacterial metabolic byproducts may alter the overall UV-Vis profile: increased bacterial load → nitrite presence, but this is a correlation, not a causal spectral feature
- **EIS features** — nitrite is an anion that contributes to ionic conductivity; however, at clinical concentrations (typically <1 mM), the EIS contribution is negligible vs NaCl, KCl, urea
- If Griess reagent is embedded in a disposable cuvette tip: $A_{540}$ from azo dye — highly specific, ε ~40,000

**Confidence:** **Very low for reagentless direct detection.** Nitrite detection without chemical reaction is not feasible by UV-Vis spectroscopy. The V20 results (Sensitivity 0.79, Specificity 0.92) likely use correlations with other spectral markers of bacteriuria rather than direct nitrite measurement. **Consider reframing as a derived feature of the bacterial detection model** rather than an independent spectral analyte.

#### 9.2.13 Sodium & Chloride

**Physical basis:** Na⁺ and Cl⁻ are simple inorganic ions. They have **no UV-Vis absorption** — they are spectrally transparent across the entire 200–2500 nm range. NaCl solutions do perturb the NIR water absorption bands slightly (hydration shell effects) and alter refractive index.

**Detection routes:**

| Method | Physical basis | Feasibility |
|---|---|---|
| **EIS conductivity** | Na⁺ and Cl⁻ are the dominant charge carriers in urine. Conductivity at 10–100 kHz is ~70% attributable to NaCl. | ★★★★ — primary route |
| **NIR water band perturbation** | Dissolved NaCl shifts O-H stretching bands at ~970 nm and ~1450 nm | ★★ — measurable but weak at urine concentrations |
| **Refractive index** | NaCl contributes ~50% of urine RI above water | ★★ — requires refractometer or interferometric measurement |
| **Osmolality proxy** | Na⁺ + Cl⁻ account for ~50% of urine osmolality | ★★★ — indirect, confounded by urea/K⁺/glucose |

**Suggested features:**
- **EIS multi-frequency impedance** — conductivity at 10 kHz (total ions); compare with higher frequencies to separate bulk from interfacial effects
- **EIS + osmolality model:** if osmolality is estimated (Section 9.2.7) and other major osmolytes (urea via NIR, creatinine via EIS) are subtracted, the residual is predominantly NaCl
- $A_{970}$ from C12880MA — water O-H overtone perturbation (very weak effect, likely below detection limit)
- $A_{1070}$ — weakly correlated with total dissolved solids

**Confidence:** **Low for spectral; medium-high for EIS.** Direct optical measurement of Na⁺ or Cl⁻ in urine is not physically possible without ion-selective reagents or electrodes. The ADuCM355 EIS frontend is the correct measurement modality. Multi-frequency EIS combined with temperature compensation can yield Na + Cl estimates within ±15–20 mmol/L (clinical utility questionable). Individual ion separation (Na from Cl from K) requires ion-selective electrodes, not bulk spectroscopy or EIS.

#### 9.2.14 Total Urinary Porphyrins (TUP)

**Note:** TUP = Total Urinary Porphyrins (sum of coproporphyrin + uroporphyrin + other porphyrin species). V20 objectives note "⚠ not working · MI · check R405 HDR VIDS VIS" and "partially working" for PBG with "optimise DSP · abs 405/480 · PHA: R405 HDR VIDS VIS".

TUP is closely related to the individual porphyrins in Section 9.2.9 and PBG in Section 9.2.8. The key distinction: TUP is the **sum of all fluorescent tetrapyrroles**, while PBG is a non-fluorescent monopyrrole precursor that only becomes detectable after polymerization to porphyrins.

**Why TUP is "not working":**

The most likely causes, given the V20 notes:

1. **Dynamic range at 405 nm:** Porphyrins have enormous ε (~500,000 M⁻¹cm⁻¹ at Soret) but are present at very low concentrations in normal urine (total porphyrins ~20–300 µg/L). This means $A_{405}$ from porphyrins is tiny (~0.001–0.01 AU) while hemoglobin and bilirubin produce much larger signals at the same wavelength. The "R405 HDR" note suggests the current dynamic range may be insufficient to resolve porphyrin signal from the Hb/bilirubin background.

2. **Spectral overlap at 405 nm:** Hemoglobin (Soret 415 nm), bilirubin (broad 400–500 nm), and porphyrins (Soret 398–406 nm) all absorb in the same region. Deconvolution is essential but challenging with LED-bandwidth resolution (~12 nm FWHM at 405 nm).

3. **Fluorescence is the correct modality for TUP:** Porphyrins fluoresce intensely at 595–625 nm when excited at 405 nm. Hemoglobin does NOT fluoresce (paramagnetic iron quenches fluorescence). Bilirubin fluoresces weakly at ~520 nm, not 620 nm. **Porphyrin fluorescence at ex405/em620 is the cleanest possible TUP measurement.**

**Improved feature set for TUP:**

| Feature | Physical basis | Why it helps |
|---|---|---|
| **Fluorescence: ex405 → em595–625 nm** | Porphyrin Q-band fluorescence | **Most specific measurement.** Hb doesn't fluoresce. This IS the TUP signal. |
| $A_{405}$ HDR (high sensitivity) | Soret band absorption | Needed for low concentrations; must subtract Hb contribution |
| $A_{405}/A_{480}$ | Soret peak shape | Porphyrins peak at 398–405 nm; bilirubin is broad and peaks ~453 nm. The 405/480 ratio resolves them. This is the exact ratio flagged in V20 objectives. |
| $A_{405} - f(A_{540}, A_{575})$ | Soret minus Q-band-estimated Hb | Use hemoglobin Q-bands (540/575 nm from white LED) to predict and subtract Hb contribution to 405 nm signal. Residual = porphyrins + other. |
| Second derivative: $d²A/d\lambda²$ at 398–415 nm | Peak deconvolution | Resolves uroporphyrin (398 nm), coproporphyrin (401 nm), and Hb (415 nm) Soret peaks |
| Fluorescence ratio: em595/em620 | Coproporphyrin vs uroporphyrin fractionation | Copro emits at 596 nm, uro at 618 nm; ratio gives fractionation without chromatography |

**Recommended approach:**
1. Measure fluorescence at ex405/em620 — this is the primary TUP signal
2. Use $A_{405}/A_{480}$ to separate porphyrin absorption from bilirubin
3. Use $A_{540}$/$A_{575}$ from white LED to model and subtract hemoglobin contribution to 405 nm
4. Apply second-derivative spectroscopy on the white-LED continuous spectrum around 395–420 nm for Soret deconvolution

**Confidence:** **High for elevated porphyrins (>300 µg/L) via fluorescence; medium for normal-range quantification.** The fluorescence route (ex405/em620) should work if the Jimini optical path captures emission at 620 nm — this falls within the C12880MA sensor range (340–850 nm). Buttery et al. (1995) demonstrated quantitative porphyrin fractionation in urine using second-derivative spectroscopy at the Soret region.

#### 9.2.15 Summary Table — All Analytes (V20 Targets + Extended)

| # | Analyte | V20 Priority | Direct spectral access | Primary physical mechanism | Best features | Confidence | Model type |
|---|---|---|---|---|---|---|---|
| 1 | **WBC** | Primary | ★★ | Scatter + autofluorescence | $A_{1070}$, scatter slope, ex365/em460, EIS | Low | bin (cat if possible) |
| 2 | **BAC (bacteria)** | Primary | ★★ | Scatter + UV + fluorescence | Turbidity, scatter slope, flavin ex455/em525 | Low-Medium | bin |
| 3 | **RBC (hemoglobin)** | Primary | ★★★★★ | Soret @ 405 nm + Q-bands | $A_{405}$, $A_{405}/A_{455}$, Q-band 540/575 | High | bin (cat if possible) |
| 4 | **epiCells** | Secondary | ★ | Scatter (large cells, 20–60 µm) | $A_{1070}$, shallow scatter slope | Very low | bin ≥+ |
| 5 | **Crystals** | Secondary | ★ | Scatter (large particles, λ-independent) | $A_{1070}$, $A_{800}/A_{400}$ → 1.0 | Low | bin ≥+ |
| 6 | **Creatinine** | Secondary | ★ | Absorbs at 234 nm (below range) | EIS conductivity, spectral residual | Low | cnt (regression) |
| 7 | **Osmolality** | Secondary | ★★ | Colligative (conductivity, RI) | EIS σ, $A_{1070}$, spectral integral | Medium | cnt (regression) |
| 8 | **TUP (total porphyrins)** | Tertiary | ★★★★ | Soret @ 398–405 nm + fluorescence @ 620 nm | **Fluor ex405/em620**, $A_{405}/A_{480}$, 2nd deriv | Medium-High | bin |
| 9 | **PBG** | Tertiary | ★★★ | PBG→porphyrin conversion; Soret + fluor | $A_{405}$, fluor ex405/em620, time-series | Medium | bin |
| 10 | **Porphyrins** | (extended) | ★★★★ | Soret ~400 nm; ε ~500,000; fluor 595–625 nm | Fluor ex405/em620, em595/em620 ratio | High (if elevated) | spectral unmixing |
| 11 | **Sodium** | Tertiary | ☆ | No UV-Vis absorption | **EIS only**: multi-freq conductivity | Low (optical) / Med (EIS) | EIS regression |
| 12 | **Chloride** | Tertiary | ☆ | No UV-Vis absorption | **EIS only**: multi-freq conductivity | Low (optical) / Med (EIS) | EIS regression |
| 13 | **Nitrites** | (in results) | ☆ | Transparent at Jimini λ; Griess → 540 nm | Indirect: bacterial model proxy | Very low (reagentless) | bin (proxy via BAC) |
| 14 | **Uric acid** | (extended) | ★★★★★ | Beer-Lambert @ 275 nm; ε ~11,300 | $A_{275}$, $A_{275}/A_{320}$ | High | CLS / band ratio |
| 15 | **Bilirubin** | (extended) | ★★★★★ | Beer-Lambert @ 453 nm; ε ~60,000 | $A_{455}$, $(A_{455}-A_{600})/(A_{455}+A_{600})$ | High | CLS / band ratio |
| 16 | **Protein (total)** | (extended) | ★★★★ | Trp/Tyr @ 280 nm; ε ~5,500 | $A_{275}$ proxy, fluor ex275/em340 | Medium | band ratio + scatter |
| 17 | **NADH** | (extended) | ★★★★ | Fluorescence ex340/em460 | ex365→em460 intensity | Medium-High | fluorescence ratio |

**Legend:** ★★★★★ = strong direct spectral signature; ☆ = spectrally invisible, EIS or indirect only.  
V20 priority from `objectives.md`. Items marked "(extended)" are analytically important but not explicitly in V20 target list.

### 9.3 Implementation Priority

1. **Start with CLS / band ratios** — direct Beer-Lambert at known wavelengths. Fastest to implement, easiest to validate. If $c = A / (\varepsilon \cdot l)$ works for a target analyte, you're done.

2. **Add scatter correction** — use $A_{1070}$ and NIR slope to correct for matrix effects (multiplicative scatter correction, SNV). This makes the Beer-Lambert model more robust.

3. **Upgrade to Enhanced BLL features + ridge** — the 56-feature approach from arXiv:2509.12253 adapted for your wavelength set. Likely the optimal complexity–performance tradeoff.

4. **Try symbolic regression (PySR)** — feed your physics features + concentrations and let SR discover the best closed-form equation. The discovered formula IS your model — fully interpretable, deployable on STM32 without a neural network runtime.

5. **If accuracy insufficient, add learnable BLL network** — a small MLP trained on Beer-Lambert simulations, fine-tuned on real data. Use SHAPCA to verify it stays physically grounded.

6. **Physics-constrained autoencoder for mixture decomposition** — if you need to handle unknown interferents (medications, dietary chromophores). The autoencoder can discover new endmembers without being told what they are.

---

## 10. Gaps & Open Questions

1. **No paper directly applies physics-constrained ML to LED-based urinalysis.** The learnable BLL work (arXiv:2309.16735) is for brain tissue NIR. The glucose PINN work (arXiv:2509.12253) is for transcutaneous NIR. Neither addresses the specific challenge of discrete-LED excitation with multi-channel detection in urine.

2. **Fluorescence features are underexplored.** Most papers focus on absorption spectroscopy. Urine fluorescence (NADH at 365/460 nm, riboflavin at 370/525 nm) is a major information source that physics-grounded models should exploit but few papers address systematically.

3. **Symbolic regression for spectroscopy is very new.** The PhySO/PySR applications to optical data (arXiv:2506.01862) are from 2025 — no papers yet apply SR specifically to biofluid UV-Vis data.

4. **Matrix effects in urine are severe.** Urine varies enormously in concentration (osmolality 50–1200 mOsm/kg), pH (4.5–8.0), and color. Physics-grounded models need to account for inner-filter effects, pH-dependent spectral shifts, and variable dilution — most papers assume well-controlled lab conditions.

5. **Calibration transfer with physics models.** If the model's features are truly physically grounded (based on extinction coefficients, not learned biases), calibration transfer between devices should be easier — but this hasn't been tested empirically for LED-based devices.

6. **SHAPCA** (arXiv:2603.19141) is from March 2026 — very recent, no independent replication yet.

---

## 11. Sources

### Primary Papers (Read / Queried)

| Paper | Year | ID | Category | Key contribution |
|---|---|---|---|---|
| Enhanced Beer-Lambert for glucose | 2025 | arXiv:2509.12253 | A | 56 physics features beat all PINNs |
| NN learning spectral indices | 2022 | arXiv:2207.10530 | A | NNs spontaneously learn NDVI-like indices |
| Physics-informed features (PIFs) | 2025 | arXiv:2504.17112 | A | Formal framework for PIFs via Buckingham π |
| Spectra-Scope toolkit | 2026 | arXiv:2603.06011 | A | AutoML for interpretable spectral features |
| Learnable Beer-Lambert for brain | 2023 | arXiv:2309.16735 | B | MLP on Beer-Lambert simulations, real-time inference |
| Physics-constrained AE for Raman | 2024 | arXiv:2403.04526 | B | Non-negativity + sum-to-one in autoencoder |
| Principles-driven UV prediction | 2026 | OpenReview ICLR sub. | B | PPA, CLIAS, SCL training constraints |
| PhISM for hyperspectral | 2025 | arXiv:2508.21618 | B | Continuous basis function decomposition |
| Physics-based AI for optical data | 2025 | arXiv:2503.08183 | D | Physics model + NN residual |
| Physics+data hyperspectral unmixing | 2022 | arXiv:2206.05508 | D | Decoder = physical mixing model |
| SR for optical properties | 2025 | arXiv:2506.01862 | C | PhySO discovers Cauchy-like equations |
| SR review | 2022 | arXiv:2211.10873 | C | Comprehensive survey |
| SHAPCA | 2026 | arXiv:2603.19141 | E | SHAP + PCA backprojection for spectra |
| SpecReX | 2025 | arXiv:2503.14567 | E | Causal XAI for Raman |
| Spectral-zone SHAP | 2024 | Contreras & Bocklitz | E | Grouped spectral explanations |
| Explainable spectral modeling | 2022 | arXiv:2202.04527 | A/E | Feature selection for limited spectral data |
| LIBS trustworthiness | 2022 | arXiv:2210.03762 | B | Simulation augmentation + multitask |
| OASIS framework | 2025 | arXiv:2509.11499 | B | Universal spectroscopic analysis via novel losses |
| Spectral unmixing for photoacoustics | 2026 | arXiv:2602.16357 | B/D | PINN for optical inversion |

### Web Sources

| Source | URL |
|---|---|
| Spectroscopy Online: Demystifying the Black Box | [spectroscopyonline.com](https://www.spectroscopyonline.com/view/demystifying-the-black-box-making-machine-learning-models-explainable-in-spectroscopy) |
| Beer-Lambert deviations (Nature Sci. Rep.) | [nature.com/s41598-021-92850-4](http://www.nature.com/articles/s41598-021-92850-4) |
| Physics-informed spectral calibration (Nature Sci. Rep.) | [nature.com/s41598-023-29371-9](https://www.nature.com/articles/s41598-023-29371-9) |
| Physics-guided ML for optical inversion (Nature Sci. Rep.) | [nature.com/s41598-024-59594-3](https://www.nature.com/articles/s41598-024-59594-3) |
| Chemometric UV-Vis quantification (Nature Sci. Rep.) | [nature.com/s41598-025-31003-3](http://www.nature.com/articles/s41598-025-31003-3) |
| FTIR biofluid spectral biomarker identification (RSC Analyst) | [pubs.rsc.org/an/c3an00337j](https://pubs.rsc.org/en/content/articlelanding/2013/an/c3an00337j) |
| Body-fluid spectroscopy group (RUB Bochum) | [pure.ruhr-uni-bochum.de](http://www.pure.ruhr-uni-bochum.de/projekte/bph/bodyfluid.html.en) |
| Optical absorption of hemoglobin (OMLC) | [omlc.org/spectra/hemoglobin](https://omlc.org/spectra/hemoglobin/) |
| Hemoglobin calibration by photoacoustic spectroscopy (2025) | [springer.com](https://link.springer.com/article/10.1007/s10765-025-03686-3) |
| Blood optical properties (Frontiers in Photonics, 2025) | [frontiersin.org](https://www.frontiersin.org/journals/photonics/articles/10.3389/fphot.2025.1636398/pdf) |
| Vis-NIR spectroscopy for WBC count (2022, 2024) | [mdpi.com/2079-6374/14/1/53](https://www.mdpi.com/2079-6374/14/1/53) |
| WBC quantification via spectral analysis (Spectroscopy Online) | [spectroscopyonline.com](https://spectroscopyonline.com/view/accurate-quantification-of-white-blood-cells-using-spectral-analysis) |
| Urine cell profiling by IR spectroscopy (2025) | [pubmed/39862788](https://pubmed.ncbi.nlm.nih.gov/39862788/) |
| Bacterial detection in urine by laser scattering (2022) | [PMC8941854](https://pmc.ncbi.nlm.nih.gov/articles/PMC8941854/) |
| Spectroscopic UTI detection methodology (2025) | [mdpi.com/1424-8220/25/2/400](https://www.mdpi.com/1424-8220/25/2/400) |
| Fluorescent signatures for body fluid ID (Nature Sci. Rep.) | [nature.com/s41598-023-30241-7](https://www.nature.com/articles/s41598-023-30241-7) |
| Creatinine UV-Vis spectrum (NIST WebBook) | [webbook.nist.gov](https://webbook.nist.gov/cgi/cbook.cgi?ID=C60275&Mask=400) |
| Creatinine UV-Vis spectrum (SIELC) | [sielc.com](https://sielc.com/uv-vis-spectrum-of-creatinine) |
| NIR creatinine in urine — Shaw et al. (1996) | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/000991209502011X) |
| NIR urea/creatinine/glucose — Koschack et al. (2001) | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0009912001001989) |
| Urine osmolality vs specific gravity — Voinescu et al. (2002) | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0002962915345262) |
| Osmolality from conductivity + SG (Ghent Univ.) | [biblio.ugent.be](https://backoffice.biblio.ugent.be/download/8609692/8609694) |
| Kuenert catheter spectroscopy for urine (2025) | [nature.com](https://www.nature.com/articles/s41598-025-92802-2.pdf) |
