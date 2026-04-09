# Research: Signal Processing & Chemometrics for Spectral Urine Analysis

**Context:** Portable LED-based spectrophotometer (275–1078 nm) for urine analysis  
**Date:** 2026-04-09  
**Status:** Complete — 30+ sources synthesized

---

## Summary

The optimal preprocessing pipeline for portable LED-based urine spectrophotometry combines **Standard Normal Variate (SNV)** normalization (proven in direct LED urine spectroscopy studies) with **Savitzky-Golay smoothing/derivatives**, followed by **arPLS/airPLS baseline correction** when fluorescence drift is present. For the 275–1078 nm range covering both UV absorption and NIR overtones, **PLS regression** remains the gold-standard chemometric workhorse for quantification, but **1D-CNN** and hybrid CNN-attention models now consistently outperform PLS on larger datasets (>200 samples). For small datasets typical of clinical urine studies (50–400 samples), ensemble approaches (SVR + RF) or PLS with wavelength selection (CARS, SPA) are more robust. Spectral data augmentation via WGAN or diffusion models is emerging as the key strategy to combat small-sample overfitting.

---

## Part 1: Spectral Preprocessing for Biological Fluid Analysis

### 1.1 Standard Normal Variate (SNV) — Primary Scatter Correction

SNV is the **most validated preprocessing method for LED-based urine spectrophotometry**. In the key 2025 Kuenert et al. study (n=401 urine samples, 340–850 nm, Hamamatsu mini-spectrometer), SNV preprocessing reduced spectral inter-sample standard deviation by nearly **4 orders of magnitude** — from 1097.62 to 0.24 average SD per wavelength. SNV centers each spectrum to zero mean and unit variance:

```
s̃ᵢ = (sᵢ - μ(s)) / σ(s)
```

**Why SNV works for urine:** Urine samples vary dramatically in turbidity, color, and dilution between patients. SNV corrects for both additive (baseline shifts) and multiplicative (path-length variation, turbidity) scatter effects on a **per-spectrum basis** without requiring a reference mean spectrum.

**Trade-off:** SNV can suppress genuine amplitude differences when analyte concentration affects overall spectrum intensity. In those cases, use **SNV + detrending** together.

**Sources:**
- Kuenert et al. (2025) *Sci. Reports* — LED spectrometer urine (340–850 nm, 401 samples) [https://www.nature.com/articles/s41598-025-92802-2](https://www.nature.com/articles/s41598-025-92802-2)
- Barnes et al. (1989) *Appl. Spectrosc.* — SNV original paper, still canonical
- Yan et al. (2025) *PMC iScience* — comprehensive preprocessing review [https://pmc.ncbi.nlm.nih.gov/articles/PMC12221524/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12221524/)

---

### 1.2 Multiplicative Scatter Correction (MSC) and Extended MSC (EMSC)

**MSC** corrects per-sample spectra by regressing them against a mean reference spectrum, extracting additive (intercept) and multiplicative (slope) scatter coefficients. This is computationally heavier than SNV but preserves the relationship to a known reference state.

```
xᵢₖ = cᵢ + bᵢ·x̄ₖ + eᵢₖ
xᵢₖ* = (xᵢₖ - ĉᵢ) / b̂ᵢ
```

**EMSC (Extended MSC)** is more powerful for complex biological matrices. It adds:
- Polynomial baseline terms to remove fluorescence/broad background
- PCA-based interferent terms (e.g., water vapor, temperature effects)
- Explicit subtraction of known confounders (e.g., urine color compounds affecting baseline)

EMSC achieved **97% specificity** for Crohn's disease biomarkers in FTIR serum analysis and reduced temperature artifacts in NIR polymers from R²>95% to <1%. For urine, EMSC is valuable when:
- Strong fluorescence background exists (relevant in 275–400 nm UV range)  
- Known interferents (urobilin absorption at ~490 nm) contaminate analyte signals

**Recommendation for our system:** Use **SNV** as default for Vis-NIR (400–1078 nm). Use **EMSC with polynomial correction** in the UV range (275–400 nm) where fluorescence background from urinary compounds (porphyrins, NADH) is significant.

**Sources:**
- Afseth & Kohler (2012) *Chemom. Intell. Lab. Syst.* — EMSC tutorial
- Jochemsen et al. (2024) *Chemom. Intell. Lab. Syst.* — recent EMSC comparison [https://www.sciencedirect.com/science/article/pii/S0169743924001278](https://www.sciencedirect.com/science/article/pii/S0169743924001278)

---

### 1.3 Savitzky-Golay Filter and Derivatives — Signal Enhancement

**Savitzky-Golay (SG) filtering** applies local polynomial regression within a sliding window to smooth spectra while preserving peak shape. Unlike simple moving-average, SG preserves moments up to polynomial order N.

**Key parameters:**
- Window size (2M+1): typically 5–25 points; larger = more smoothing but peak broadening
- Polynomial order: 2nd or 3rd recommended; higher risks overfitting noise
- Derivative order: 0 = smoothing only; 1st = removes constant baseline; 2nd = removes linear baseline, enhances peak resolution

**SG 2nd derivatives** are particularly valuable for urine spectroscopy because:
1. They eliminate baseline offset and slope (critical for varying urine dilution)
2. They reveal overlapping peaks (e.g., discriminating creatinine vs. urea NIR bands)
3. Combined with SNV they provide excellent performance in NIRS food/biofluid studies

**Performance benchmark:** SG 1st derivative + SVM achieved 100% accuracy in NIR wood species identification. For NIR urea/creatinine prediction, SG 2nd derivative typically reduces RMSECV by 15–30% vs. raw spectra.

**Fractional-order SG derivatives (FOSGD):** Emerging technique using order α ∈ (0,2) to tune resolution-noise tradeoff. Showed +17% correlation improvement for chlorophyll estimation vs. integer derivatives. Worth exploring for dilute urine analytes.

**Sources:**
- Savitzky & Golay (1964) *Anal. Chem.* — original SG paper
- Rinnan et al. (2009) *TrAC Trends Anal. Chem.* — most common NIR preprocessing review
- Zhang & Mouazen (2023) *Infrared Phys. Technol.* — FOSGD for Vis-NIR

---

### 1.4 Baseline Correction: ArPLS, AirPLS, and Variants

For the UV range (275–380 nm) where urine autofluorescence is strongest and LED illumination may induce background, **iterative weighted least squares baseline methods** are essential.

**airPLS (Adaptive Iteratively Reweighted Penalized Least Squares):**
- Zhang et al. (2010) *Analyst* — most widely used
- Dynamically excludes spectral peaks, fits smooth baseline via asymmetric weights
- Iterates until residuals < 0.1% of total signal
- One hyperparameter: λ (smoothness penalty, typically 10²–10⁷ depending on spectral resolution)

**arPLS (Asymmetrically Reweighted PLS):**
- Baek et al. (2015) *Analyst*
- Uses logistic sigmoid weighting to adapt to local noise distribution
- More robust than airPLS in moderate-SNR conditions (UV-Vis range)
- Outperforms airPLS for Raman-like sharp peaks; comparable for broad NIR bands

**IairPLS (Improved airPLS):**
- Sigmoid transition replaces exponential decay at peak boundaries
- Reduced RMSE vs. airPLS (0.0187 vs. 0.0531 in XRF soil spectra)
- Better for complex urine fluorescence backgrounds

**BrPLS (Bayesian Reweighted PLS):**
- State-of-the-art; R²=0.9990 vs. 0.9985 (arPLS) for sinusoidal baselines
- Probabilistic weight adaptation, no manual threshold tuning
- **Recommended for 275–400 nm fluorescence correction** when computational cost is acceptable

**Recommended pipeline for our UV range:**
1. arPLS or IairPLS (λ = 10⁴–10⁵) for LED-excited fluorescence baseline
2. Verify baseline doesn't over-smooth near UV absorption peaks (280 nm aromatic amino acids, 340 nm NADH, 400–450 nm urobilinogen/bilirubin)

**Sources:**
- Zhang et al. (2010) *Analyst* — airPLS [DOI:10.1039/b922045c]
- Baek et al. (2015) *Analyst* — arPLS [DOI:10.1039/c4an01061b]
- Yan et al. (2025) *PMC iScience* — comprehensive baseline method comparison

---

### 1.5 Orthogonal Signal Correction (OSC) and OPLS

**OSC** removes spectral variation **orthogonal to the Y-variable** (target analyte) before modeling. This is fundamentally different from SNV/MSC: those correct for physical scatter, while OSC removes any latent structure in X that does not correlate with Y.

**Algorithm (Direct OSC, DOSC):**
1. Project Y into spectral space: Ŷ = X(XᵀX)⁻¹XᵀY
2. Isolate orthogonal spectral space: Z = (I - ŶŶ†)X
3. PCA/SVD of Z → extract noise subspace U
4. Remove from data: X_corrected = X - UPᵀ

**Impact on rice bran oil analysis:** OSC transformed R² from 0.50 to 0.987 by eliminating humidity-induced spectral variation.

**OPLS (Orthogonal PLS):** Integrates OSC directly into the PLS algorithm. Provides:
- Cleaner decomposition of X into predictive (correlated with Y) and orthogonal parts
- Better interpretability of loading plots — orthogonal loadings show *what is being removed*
- Particularly useful for urine: removes variation due to individual patient differences, dilution, and temperature

**When to use OSC/OPLS for urine:**
- When sample-to-sample matrix effects (different patients) dominate spectral variation
- When multiple analytes share spectral overlap and you want single-analyte OPLS models
- When a preprocessing step (prior to PLS) is preferred over model integration

**Caution:** OSC can over-correct if applied with too many components. Use **2-4 OSC components** maximum for urine spectra. Validate on held-out test set to confirm improvement.

**Sources:**
- Wold et al. (1998) *Chemom. Intell. Lab. Syst.* — OSC original
- Westerhuis et al. (2001) *Chemom. Intell. Lab. Syst.* — Direct OSC (DOSC)
- Yan et al. (2025) *PMC iScience* — OSC section

---

### 1.6 Complete Recommended Preprocessing Pipeline

```
Raw spectrum (275–1078 nm, N wavelength points)
    ↓
[1] Outlier/spike detection (arPLS residual Z-score > 4σ → flag sample)
    ↓
[2a] UV range (275–400 nm): arPLS/IairPLS baseline correction (λ=10⁴)
[2b] Vis-NIR range (400–1078 nm): apply SNV
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

**Alternative simplified pipeline (validated in Kuenert 2025):**
```
Raw → SNV → correlation-based wavelength selection → logistic regression
(AUC 0.921–0.981 on bilirubin, erythrocytes, pH, protein, specific gravity)
```

---

## Part 2: Feature Extraction and Wavelength Selection

### 2.1 Principal Component Analysis (PCA)

PCA is the standard exploratory step to:
- Identify spectral outliers (Hotelling T² and Q-residuals)
- Visualize sample clustering (useful: healthy vs. pathological urine)
- Determine effective dimensionality before building calibration models

**For urine spectra:** Typically 3–8 PCs explain >95% variance. The first PC often captures dilution (color depth), PC2-3 capture specific compound signatures.

---

### 2.2 Variable Importance in Projection (VIP) Scores

VIP scores from PLS quantify how much each wavelength contributes to the Y-variance across all PLS components. Standard threshold: **VIP > 1.0** selects wavelengths above average importance.

**Advantages:** Fast, directly tied to PLS model, easy to interpret  
**Disadvantages:** Collinear wavelengths may show inflated VIP; tends to select wide regions rather than specific peaks

---

### 2.3 Competitive Adaptive Reweighted Sampling (CARS)

CARS iteratively removes wavelengths with low PLS regression coefficients using adaptive weighting. It mimics "survival of the fittest" for wavelength selection:

1. Exponential decay removes a fraction of high-coefficient wavelengths each iteration
2. Competitive penalty reweights survivors
3. Monte Carlo cross-validation selects the optimal subset

**Performance:** CARS + PLSR achieved R²=0.927 for apple Brix values, and is widely used in agricultural NIR. For urine: particularly valuable for the 900–1100 nm NIR range where water overtones dominate but creatinine/urea have weak characteristic bands.

**Combined approach:** CARS-SPA (Successive Projections Algorithm after CARS) — SPA removes collinear wavelengths from the CARS-selected set, further reducing to a minimal non-collinear subset. Outperforms either method alone.

---

### 2.4 Successive Projections Algorithm (SPA)

SPA selects wavelengths by minimizing collinearity. Starting from a seed wavelength, it projects out the contribution of already-selected wavelengths and adds the one with maximum projection at each step.

**Advantages:** Produces small, non-redundant sets (5–15 wavelengths) ideal for miniature LED systems  
**Limitation:** Sensitive to initial seed wavelength

**For portable LED spectrophotometer (275–1078 nm):** SPA is ideal for reducing the ~800 wavelength channels to 5–20 key wavelengths that can guide future LED selection or filter placement.

---

### 2.5 Correlation-Based Wavelength Selection (Kuenert 2025 approach)

The Kuenert et al. 2025 urine study used a **literature-guided correlation analysis**:
1. Compute Pearson/Kendall-τ correlation between each wavelength channel and the clinical reference value
2. Plot correlation curves across the spectrum
3. Select wavelengths at significant correlation peaks (p < 0.05) that align with known absorption maxima

**Results for urine analytes:**
- **Bilirubin:** 344 nm, 387 nm, 426 nm (strong correlation, known absorption max ~440 nm)
- **Hemoglobin/erythrocytes:** Soret band ~414 nm, Q-bands 540/580 nm
- **Urobilinogen:** ~490 nm characteristic absorption
- **Protein:** Multiple wavelengths (broad, reflecting diverse protein types)
- **pH/specific gravity:** Broad spectral contributions, no sharp peaks
- **Glucose, albumin:** No significant correlations in 340–850 nm (confirmed absent in Vis range — need MIR or specific colorimetric reactions)

**Key insight for our 275–1078 nm system:** The UV extension to 275 nm is critical. Below 340 nm:
- Aromatic amino acids (tryptophan 280 nm, tyrosine 274 nm) absorb — useful for proteinuria
- Nucleobases absorb at ~260 nm (relevant for chronic kidney disease monitoring)
- Uric acid has absorption around 290 nm
- Nitrite absorbs at 354 nm

**Sources:**
- Kuenert et al. (2025) *Sci. Reports* [https://www.nature.com/articles/s41598-025-92802-2]
- Tang et al. (2014) *Analyst* — CARS-SPA combination [DOI:10.1039/c4an00837e]

---

## Part 3: Chemometric Modeling

### 3.1 PLS Regression — Gold Standard

**Partial Least Squares (PLS)** simultaneously decomposes X (spectra) and Y (analyte concentrations) into latent variables maximizing their covariance. PLS handles:
- Collinear wavelength variables (NIR spectra are almost never independent)
- More predictors (wavelengths) than samples
- Multiple targets simultaneously (PLS2)

**Key hyperparameter:** Number of latent variables (LVs) — typically selected by leave-one-out or 10-fold cross-validation minimizing RMSECV.

**Performance for urine NIR:**
- Creatinine: R² ≈ 0.85–0.95, RMSEP ≈ 0.5–1.5 mM (from classical studies)
- Urea: R² ≈ 0.80–0.90
- Total protein: R² ≈ 0.75–0.85 (harder due to diverse protein composition)

**When PLS is sufficient:** For small datasets (n < 200), PLS with proper cross-validation is typically more robust than ML methods which overfit.

---

### 3.2 OPLS — Interpretable Regression

**OPLS** separates PLS into a predictive component (1 LV per Y) and orthogonal components (removing Y-unrelated variation). Advantages:
- Cleaner loading plots showing only chemically relevant variation
- Better interpretability of which spectral regions drive prediction
- Equivalent prediction performance to PLS but with more interpretable models

**Recommended for clinical reporting** where regulatory bodies require interpretable models.

---

### 3.3 Machine Learning: SVR, Random Forest, XGBoost

**Support Vector Regression (SVR):**
- RBF kernel SVR consistently outperforms PLS for **nonlinear analyte-spectral relationships**
- Effective for small datasets (n = 50–300) with proper regularization (C, γ optimization via grid search)
- **Limitation:** Computationally expensive for full spectral input; use wavelength selection first

**Random Forest:**
- Excellent with wavelength selection pre-step; handles interactions between spectral features
- Built-in variable importance (Gini impurity) provides feature selection information
- Robust to outliers compared to PLS
- Typically requires n ≥ 100 for reliable performance

**XGBoost:**
- Gradient boosting ensemble; usually outperforms RF on structured spectral data when n ≥ 150
- Hyperparameter-sensitive: careful tuning of learning rate, depth, subsample
- Less studied for urine spectroscopy specifically; more common in general NIR literature

**Kuenert 2025 (preliminary mention):** PLS Discriminant Analysis, random forests, and CNNs were all tested; confirmed or improved upon logistic regression AUC results (full comparison to be published).

**Published comparison (NIR spectroscopy, food/agri contexts):**
- PLS vs. SVR vs. RF vs. CNN: CNN > SVR ≥ RF > PLS on datasets n > 300
- SVR ≈ CNN on datasets n < 150 (Zhang et al. 2022 *Sensors*)

---

### 3.4 Principal Components Regression (PCR)

PCR applies PCA to reduce spectral dimensionality, then regresses Y on scores. **Consistently underperforms PLS** because PCA compression ignores Y — some Y-relevant variation may be in lower PCs. Only useful when interpretability of PCA loadings is required.

---

## Part 4: Deep Learning on Spectroscopic Data

### 4.1 1D-Convolutional Neural Networks (1D-CNN) — State of the Art

1D-CNNs apply convolutional filters along the wavelength dimension, learning local spectral patterns without prior knowledge of peak positions. They are the dominant DL architecture for spectral regression.

**Architecture (typical):**
```
Input: (N_samples, N_wavelengths, 1)
→ Conv1D(32, kernel=7) + ReLU + BatchNorm
→ Conv1D(64, kernel=5) + ReLU + BatchNorm  
→ MaxPool1D(2)
→ Conv1D(128, kernel=3) + ReLU + BatchNorm
→ GlobalAvgPool1D
→ Dense(64) + Dropout(0.3)
→ Dense(1) [regression] or Dense(N_classes) + Softmax [classification]
```

**Performance benchmarks:**
- arxiv 2301.10746 (Lemos et al.): 1D-CNN outperformed PLS, SVR, RF, and MLP on 5 public spectral datasets; average R² improvement over PLS = +0.05–0.12
- CNN regression (Kiranyaz et al. survey): state-of-the-art for spectral quantification with n > 500
- MIR breast cancer classification: 95.09% accuracy with 1D-CNN (Shang et al. 2024)

**Limitations for small datasets:**
- n < 100: 1D-CNNs typically underperform PLS/SVR due to overfitting
- n = 100–300: 1D-CNN competitive with careful regularization (dropout, BatchNorm, data augmentation)
- n > 500: 1D-CNN consistently best

**Minimal 1D-CNN that works on small spectral datasets (~150-300 samples):**
```python
model = Sequential([
    Conv1D(32, 11, padding='same', activation='relu', 
           input_shape=(n_wavelengths, 1)),
    BatchNormalization(),
    Conv1D(16, 7, padding='same', activation='relu'),
    GlobalAveragePooling1D(),
    Dense(32, activation='relu'),
    Dropout(0.4),
    Dense(1)  # for regression
])
```

**Sources:**
- Kiranyaz et al. (2021) *Mech. Syst. Signal Process.* — 1D-CNN survey
- arxiv 2301.10746 (2023) — 1D-CNN vs. chemometrics comprehensive comparison
- arxiv 2005.07530 (Bjerrum 2020) — CNN classification and regression on spectral data

---

### 4.2 Transformer Models for Spectroscopy

**SpectraTr (Fu et al. 2022):** Transformer encoder for 1D spectral data. Multi-head self-attention learns long-range spectral dependencies. Published for qualitative NIR drug analysis, showing superior performance to 1D-CNN for identifying overlapping peaks.

**Transformer-based quantitative NIR (Li et al. 2024, SSRN preprint):** Outperforms 1D-CNN for quantitative NIR analysis on larger datasets (n > 500).

**SpectraViT (Li et al. 2024):** Combines CNN feature extraction with ViT (Vision Transformer) attention. Applied to UV spectroscopy for jade identification. The hybrid CNN+Transformer architecture outperforms pure CNN.

**Key consideration for our system:** Transformers require significantly more data than 1D-CNNs (typically n > 1000 for good generalization). For urine datasets of n = 150–500, **1D-CNN is preferred**; transformers should wait for larger datasets or use transfer learning.

---

### 4.3 Transfer Learning and Pre-training for Spectroscopy

**Cumulative learning (Bittremieux et al. 2020, *Nature Comm.*):** For mass spectrometry with small datasets, pre-training on large auxiliary spectral datasets then fine-tuning dramatically improves performance. The 1D-CNN approach with cumulative learning showed significant gains over direct training on small data.

**Practical approaches for our context:**
1. **Pre-train on large public spectral dataset** (e.g., Kew Garden NIR, LUCAS soil NIR — thousands of samples) then fine-tune on urine data
2. **Domain adaptation:** Pre-train on water/aqueous solution spectra (high spectral similarity to urine), fine-tune
3. **Source-task proxy:** Pre-train on blood serum spectra (compositionally similar), fine-tune on urine

**Key paper:** Towards CNN representations for small MS data classification (bioRxiv 2020) → *Nature Comm.* 2020 — demonstrated that cumulative learning reduces required dataset size by 5–10x for acceptable CNN accuracy.

---

### 4.4 Autoencoders for Feature Extraction and Denoising

**Denoising Autoencoder (DAE) for NIR:**
- Çataltaş (2025) *New Trends Comp. Sci.* — DAE pre-processing before PLSR significantly reduced noise, improved R² on NIR calibration
- Encode spectra into 16–32 dimensional latent space → reconstruct → residual is noise estimate
- Alternatively: use encoder output (bottleneck features) directly as input to PLS/SVR

**Attention-enhanced Residual Autoencoder (SpecFuseNet):**
- Kabiso & Ko (2025) *Sci. Reports* — NIR grain classification with attention-enhanced residual autoencoder
- PMC: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12460850/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12460850/)
- 97.8% classification accuracy; features from encoder outperformed raw spectra + PCA in downstream classification

**Variational Autoencoder (VAE) for denoising + generation:**
- Encodes spectra to probabilistic latent space
- Can generate synthetic spectra for augmentation
- TinyML-VAE achieved NRMSE 0.53–0.66 on embedded magnetometer data (edge deployment relevant for portable device)

---

## Part 5: Data Augmentation for Small Spectral Datasets

### 5.1 Why Augmentation is Critical for Clinical Spectroscopy

Clinical urine datasets are typically small (50–500 samples). The issue is not just total sample size but **class imbalance**: pathological samples (high protein, bilirubin, etc.) are rare. Augmentation addresses both.

**Rule of thumb from practice:**
- PLS models are reliable with n ≥ 30 samples per analyte range band
- 1D-CNN needs n ≥ 200 for training convergence without augmentation
- With augmentation: 1D-CNN can work at n_real ≈ 50–100 + augmented to 500–1000

---

### 5.2 Traditional Augmentation Methods

**Noise injection:** Add Gaussian noise (σ = 0.1–0.5% of signal) to existing spectra. Simple, fast, generally 20–30% improvement for DL models on small datasets.

**Spectral shifting:** Small wavelength shifts (±1–3 channels) simulate instrument calibration variations.

**Intensity scaling:** Multiply by scalar factor ∈ [0.9, 1.1] to simulate concentration variations.

**Baseline perturbation:** Add random low-frequency polynomial perturbation to simulate baseline drift.

**Limitation:** These methods don't generate genuinely new spectral features — they are transformations of existing spectra. Models trained on only these augmentations may still overfit.

---

### 5.3 GAN-Based Augmentation

**WGAN-based FTIR spectral augmentation (Erzina et al. 2023, *Analyst*):**
- Wasserstein GAN trained on cancer liquid biopsy FTIR spectra
- Generated realistic synthetic spectra that:
  - Passed visual similarity tests
  - Improved downstream classification accuracy by 8–15%
  - Were indistinguishable from real spectra in PCA space
- **Key insight:** Training GAN with gradient penalty (WGAN-GP) provides more stable training than vanilla GAN for spectral data

**GAN for Vis-NIR soil spectra (2023, *Sensors*):**
- Simultaneous augmentation of spectral and property data
- GAN-augmented training improved PLSR and RF R² by 0.05–0.12

**Adversarial Autoencoder (AAE) for NIR generation (Zhao et al. 2024):**
- AAE maps spectra to prior distribution, uses adversarial training
- Generated spectra maintain analyte property information
- Enhanced Gaussian Process Regression performance on small NIR datasets

---

### 5.4 Diffusion Model Augmentation (State-of-the-Art)

**Diffusion Probabilistic Models for NIR augmentation (2025):**
- Applied to precision agriculture NIR spectra
- Produces highest quality synthetic spectra (closest to real distribution)
- Significantly outperforms GANs for capturing inter-sample spectral variability
- **Main limitation:** Training requires significant compute (GPU, hours-days)

**Recommendation for our context:** Start with WGAN-GP (well-validated for FTIR/spectral data, reasonable compute). If dataset grows to n > 200, consider diffusion models.

---

### 5.5 Practical Augmentation Strategy for LED Urine Spectroscopy

```python
# Augmentation pipeline for small urine spectral dataset
def augment_spectrum(spectrum, label, n_augmented=5):
    """
    spectrum: (n_wavelengths,) array
    Returns: list of (augmented_spectrum, label) pairs
    """
    augmented = []
    for _ in range(n_augmented):
        s = spectrum.copy()
        
        # 1. Gaussian noise (simulate detector noise)
        noise_level = 0.002 * np.std(s)
        s += np.random.normal(0, noise_level, len(s))
        
        # 2. Multiplicative intensity scaling (dilution variation)
        scale = np.random.uniform(0.95, 1.05)
        s *= scale
        
        # 3. Baseline polynomial perturbation (LED drift)
        x = np.linspace(-1, 1, len(s))
        drift = np.random.normal(0, 0.001) * x + \
                np.random.normal(0, 0.0005) * x**2
        s += drift
        
        # 4. Spectral shift (±2 channels, wavelength calibration uncertainty)
        shift = np.random.randint(-2, 3)
        s = np.roll(s, shift)
        
        augmented.append((s, label))
    return augmented
```

---

## Part 6: Cross-Validation Strategies for Small Spectral Datasets

### 6.1 Key Pitfalls in Chemometric Cross-Validation

The main risk in spectral urine analysis is **overly optimistic performance estimation** due to:
1. **Data leakage:** Preprocessing (SNV, PCA) computed on entire dataset including test set
2. **Correlated samples:** Multiple measurements per patient (as in Kuenert 2025) → random splits may put same-patient samples in train and test
3. **Improper CV:** Performing preprocessing or wavelength selection on full dataset then CV

**Correct procedure:**
```
For each CV fold:
    1. Fit preprocessing parameters (SNV: mean/std per wavelength, 
       PCA: loadings, wavelength selector: CARS) on TRAINING set only
    2. Apply to test set using training parameters
    3. Evaluate
```

---

### 6.2 Recommended CV Strategies

**Leave-One-Patient-Out (LOPO):** If multiple samples per patient exist, hold out ALL samples from one patient for testing. This is the most clinically realistic estimate of generalization to new patients. Used by Kuenert et al. (correction via 5-fold CV with patient-level stratification).

**Monte Carlo Cross-Validation (MCCV, Xu & Liang 2004):**
- Randomly split 70–80% train / 20–30% test many times (100–1000 repeats)
- Average test error across all splits
- **Best for selecting number of PLS components** — less biased than LOO-CV for small datasets
- Published as better than K-fold for PLS model selection

**Venetian Blinds (Systematic K-fold):**
- Samples sorted by acquisition order, every K-th sample goes to test set
- Preserves distribution across all value ranges
- Preferred over random splits when measurement order correlates with analyte values (e.g., batch effects in hospital urine collection)

**Representative Splitting Cross-Validation (RSCV, 2018):**
- Kennard-Stone algorithm ensures training and test sets span the spectral space
- Avoids extreme values ending up only in training set
- Recommended for small urine datasets (n < 200)

**5-Fold with Patient Stratification (Kuenert 2025):**
- Stratify by patient to prevent data leakage
- n = 401 samples → 5 folds of ~80 samples, ~80/320 test/train split
- Compute correction term = mean(inner_perf - outer_perf) across folds
- Correct global model performance estimate by subtracting correction term

---

### 6.3 Systematic Validation Checklist (from Ezenarro 2025)

1. ✅ Preprocessing computed on training set only and applied to test
2. ✅ Wavelength/feature selection within cross-validation loop
3. ✅ Number of PLS components selected by MCCV, not LOO-CV
4. ✅ Separate validation set held out entirely (never used for tuning)
5. ✅ Report RMSECV and RMSEP separately (RMSECV ≈ RMSEP indicates no overfitting)
6. ✅ Check RMSEP/RMSECV ratio < 1.3 as threshold
7. ✅ External validation with n ≥ 20 independent test samples

---

## Part 7: Comparison Studies — Chemometrics vs. Deep Learning

### 7.1 Key Benchmark: Zhang et al. 2022 (Sensors) — Comprehensive Review

Zhang, Kasun et al. (2022) *Sensors* 22(24):9764 — reviewed 100+ papers on ML for NIR:

**Consensus findings:**
| Method | Dataset Size | Typical R² | Typical RMSEP | Notes |
|--------|-------------|-----------|---------------|-------|
| PCR | Any | Worst | Highest | Baseline only |
| PLS | n ≥ 30 | 0.80–0.95 | Reference | Gold standard |
| PLS + OSC | n ≥ 50 | 0.85–0.97 | 5–15% better | Matrix effects |
| SVR (RBF) | n ≥ 50 | 0.85–0.96 | ≈PLS | Better nonlinear |
| RF | n ≥ 100 | 0.82–0.95 | ≈PLS | Feature importance |
| 1D-CNN | n ≥ 200 | 0.87–0.98 | Best large N | Needs augmentation |
| Transformer | n ≥ 500 | 0.89–0.99 | Best very large | Interpretable attention |

**Key conclusion:** "For typical small NIR calibration datasets (30–200 samples), PLS with proper cross-validation remains competitive with or superior to deep learning methods."

---

### 7.2 1D-CNN vs. Chemometrics (arxiv 2301.10746, 2023)

Five spectral datasets tested. 1D-CNN outperformed PLS, SVR, RF, MLP on all datasets **when n > 500**. For smaller datasets (n < 200), SVM and PLS were competitive or better.

**Best practice conclusion:** Use **ensemble model** — average predictions from PLS + SVR + 1D-CNN (stacking) for robust performance across dataset size regimes.

---

### 7.3 Specific UV-Vis Urine Analysis Benchmarks

| Study | Modality | Range | n | Analyte | Best Method | R²/AUC |
|-------|----------|-------|---|---------|------------|--------|
| Kuenert 2025 | LED Vis (340–850nm) | 288ch | 401 | Bilirubin (class.) | LRRE (random intercept logistic) | AUC=0.921 |
| Kuenert 2025 | LED Vis | 288ch | 401 | Specific gravity | LRRE | AUC=0.890 |
| Kuenert 2025 | LED Vis | 288ch | 401 | Erythrocytes | LRRE | AUC=0.908 |
| Suzuki 2020 | NIR (900–1700nm) | — | small | Creatinine/urea | PLS | R²≈0.85 |
| ATR-FTIR 2024 | MIR | Full | 100+ | Glucose+albumin | PLS | RMSEP<0.5mg/dL |
| ATR-FTIR drug 2025 | MIR | Full | — | Drug metabolites | PLS-DA | >90% classif. |

**Critical observation for our 275–1078 nm range:** 
- UV (275–400 nm): Best for compounds with UV chromophores (aromatic aa, bilirubin, urobilinogen, nucleotides, nitrite)
- Vis (400–700 nm): Hemoglobin, erythrocytes, urobilin, bilirubin color bands
- NIR (700–1078 nm): Water overtones dominate; weak signals from C-H/N-H/O-H overtones of urea, creatinine, protein
- **SNV + PLS** on full range with CARS-selected wavelengths is a proven starting point

---

## Part 8: Practical Implementation Recommendations

### 8.1 Recommended Software Stack

**Python (recommended):**
```python
# Core libraries
import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, LeaveOneGroupOut

# Spectral preprocessing
from scipy.signal import savgol_filter  # Savitzky-Golay

# PyPI: spectral-process (Haque & Ghosh)
# pip install spectral-process
# Includes: SNV, MSC, SG, arPLS, airPLS

# Deep learning
import torch
import torch.nn as nn  # 1D-CNN

# Chemometrics-specific
# pip install chemometrics  # EMSC, PLS with EMSC pipeline
```

**R (alternative for classical chemometrics):**
```r
library(pls)      # PLS
library(prospectr) # SNV, MSC, SG, CARS, Kennard-Stone
library(mdatools)  # OPLS, OSC, validation tools
library(EMSC)     # Extended MSC
```

---

### 8.2 Minimum Viable Pipeline for 275–1078 nm LED Urine Spectroscopy

**Stage 1 (Baseline — < 1 week implementation):**
1. SNV preprocessing on full spectrum
2. Savitzky-Golay smoothing (window=9, poly=2, derivative=0)
3. PLS regression (leave-one-patient-out CV, MCCV for component selection)
4. Evaluate: RMSECV, RMSEP, R², correlation plots

**Stage 2 (Optimized — 2–4 weeks):**
1. Separate preprocessing: arPLS for UV (275–400nm), SNV for rest
2. CARS or SPA wavelength selection within CV loop
3. SVR and RF comparison against PLS
4. Report sensitivity analysis: which analytes are predicted well?

**Stage 3 (Advanced — ongoing):**
1. 1D-CNN with BatchNorm + Dropout + data augmentation
2. WGAN for generating synthetic spectra to balance classes
3. Stacking ensemble (PLS + SVR + CNN)
4. Patient-level random effects model (mixed model logistic regression like Kuenert 2025)
5. OPLS for interpretable single-analyte models

---

### 8.3 Analyte-Specific Preprocessing Notes

| Analyte | Expected UV-Vis Peaks | Key Preprocessing |
|---------|----------------------|------------------|
| Bilirubin | 344, 387, 426 nm | SNV; EMSC if icteric matrix interference |
| Hemoglobin/RBC | 414, 540, 576, 630 nm | SNV sufficient; Beer-Lambert holds well |
| Urobilinogen | ~490 nm | SNV; careful baseline at UV edge |
| Creatinine | No strong Vis abs.; 230 nm UV | UV: arPLS + SNV; SG 2nd derivative |
| Urea | No Vis abs.; 200 nm deep UV | NIR overtones 900–1000 nm; SG 2nd derivative |
| Protein | 280 nm (aromatic), broad Vis | SNV + SG derivative; VIP selection |
| Nitrite | 354 nm (UV) | arPLS baseline crucial; near LED noise floor |
| Ketones | Carbonyl >300 nm, weak | Challenging in Vis; may need UV |
| Glucose | No Vis/UV abs. in aqueous | Essentially invisible 275–1078 nm (confirmed Kuenert 2025) |
| pH | Indirect (multiple chromophores) | PLS on full spectrum; good (AUC>0.85) |
| Specific gravity | Refractive/multi-compound | PLS on full spectrum; good (AUC>0.89) |

---

## Sources

### Kept (Primary Sources)

| Source | URL | Relevance |
|--------|-----|-----------|
| Kuenert et al. 2025, Sci Reports — LED urine spectroscopy | https://www.nature.com/articles/s41598-025-92802-2 | Direct match: LED 340–850nm, 401 urine samples, SNV, LR, CNN planned |
| Yan et al. 2025, PMC iScience — Spectral preprocessing review | https://pmc.ncbi.nlm.nih.gov/articles/PMC12221524/ | Comprehensive reference for all preprocessing methods |
| Zhang et al. 2022, Sensors — ML for NIR review | https://www.mdpi.com/1424-8220/22/24/9764 | Best available ML-NIR comparison review |
| arxiv 2301.10746 — 1D-CNN vs chemometrics | https://arxiv.org/pdf/2301.10746 | Head-to-head 1D-CNN comparison on spectral data |
| Erzina et al. 2023, Analyst — WGAN spectral augmentation | https://pubs.rsc.org/en/content/articlehtml/2023/an/d3an00669g | WGAN for FTIR cancer liquid biopsies |
| Bittremieux et al. 2020, Nature Comm — Cumulative CNN | https://www.nature.com/articles/s41467-020-19354-z | Transfer/cumulative learning for small MS datasets |
| CARS-SPA, Tang et al. 2014, Analyst | https://pubs.rsc.org/en/content/articlepdf/2014/an/c4an00837e | Wavelength selection combination method |
| Ezenarro 2025, J. Chemometrics — Validation strategies | https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/cem.70036 | Systematic CV review for NIR food models |
| EMSC tutorial — Afseth & Kohler 2012 | Chemom. Intell. Lab. Syst. 117:92–99 | EMSC tutorial for vibrational spectroscopy |
| Wold et al. 1998 — OSC | Chemom. Intell. Lab. Syst. 44:175–185 | OSC original paper |
| MDPI 2023, Sensors — Spectral augmentation review | https://www.mdpi.com/1424-8220/23/20/8562 | Comprehensive augmentation review |
| Kabiso & Ko 2025, Sci Reports — Attention autoencoder NIR | https://pmc.ncbi.nlm.nih.gov/articles/PMC12460850/ | Feature extraction autoencoder for NIR |
| SpectraViT 2024 — CNN+Transformer for UV | https://discovery.researcher.life/article/jade-identification-using-ultraviolet-spectroscopy... | UV spectroscopy with CNN-Transformer hybrid |
| Xu & Liang 2004 — MCCV | J. Chemometrics — Monte Carlo CV for PLS |
| Baek et al. 2015 — arPLS | Analyst 140:250–257 | arPLS baseline correction |
| Zhang et al. 2010 — airPLS | Analyst 135:1138–1146 | airPLS baseline correction |
| ATR-FTIR glucose+albumin 2024 | https://pubs.rsc.org/en/content/articlelanding/2024/ay/d4ay01320d | Simultaneous glucose+albumin in urine |
| Suzuki et al. 2020 — NIR urine spot test | Med. Biol. Eng. Comput. 58:67–74 | NIR urea/creatinine reagentless |

### Dropped

- NMR spectroscopy papers — different modality (NMR vs photometry)
- Durian/food NIR papers — too domain-specific, no direct urine relevance  
- Soil/agriculture NIR preprocessing papers — used as method references only, not primary evidence

---

## Gaps and Open Questions

### Gap 1: LED-Specific Noise Characteristics Not Characterized
Most preprocessing literature is for bench-top spectrometers with halogen/deuterium sources. LED-based sources have specific noise characteristics:
- **Thermal drift** of LED emission wavelength (~0.1–0.3 nm/°C)
- **Intensity fluctuation** between LEDs (pulsed vs. continuous)
- **Narrow-band gaps** if LED coverage is incomplete between 275–1078 nm

**Recommendation:** Characterize noise statistics empirically. Use Kalman filter for real-time LED drift correction if continuous monitoring is planned.

### Gap 2: No Published 275–400 nm Preprocessing Specifically for Urine
All current LED urine studies start at ≥340 nm. The UV extension to 275 nm (our advantage) is uncharted territory for urine. Key unknowns:
- Fluorescence contribution from urinary porphyrins and pyridines at 275–320 nm
- Whether arPLS handles this adequately or requires specialized methods

**Next step:** Acquire urine spectra at 275–400 nm, compare arPLS vs. EMSC vs. polynomial correction for baseline quality.

### Gap 3: Multi-Patient Temporal Stability
The Kuenert 2025 study used frozen-thawed samples. Real-time analysis of fresh urine in catheters (our target use case) may show:
- Temperature-dependent spectral shifts
- Bacterial metabolism changing composition over time
- Foam/turbidity variations in continuous flow

**Next step:** Validate preprocessing pipeline on continuously collected catheter urine vs. spot samples.

### Gap 4: Quantification vs. Classification
Most recent urine spectroscopy studies focus on binary classification (healthy/pathological). Quantitative prediction (actual creatinine concentration in mg/dL) requires:
- More samples across full concentration range
- Concentration-balanced training set
- RMSEP < clinical decision threshold

**Recommended clinical thresholds:**
- Creatinine: RMSEP < 0.5 mM to be useful for GFR estimation
- Total protein: RMSEP < 30 mg/24h for proteinuria screening
- Specific gravity: RMSEP < 0.002 SG units

### Gap 5: Comparison with Strip-Based Systems
SpectraPhone (2026, *Sci. Reports*) compared spectroscopy + ML vs. traditional dipstick. No published comparison between pure spectroscopic methods and semi-quantitative strips for the 275–1078 nm range.

**Suggested next research:**
1. Systematic preprocessing comparison on same urine dataset
2. CARS vs. SPA vs. VIP for wavelength selection on urine analytes
3. Transfer learning study: pre-train on blood serum NIR → fine-tune on urine

---

*Research brief compiled from 30+ sources. Last updated: 2026-04-09*
