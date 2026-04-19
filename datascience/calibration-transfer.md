---
title: Calibration Transfer & Device Harmonization for Portable Spectrometers
aliases:
  - calibration transfer
  - device harmonization
  - cross-device calibration
tags:
  - topic/spectroscopy
  - topic/chemometrics
  - type/concept
  - status/complete
  - device/jimini
date: 2026-04-19

---

# Calibration Transfer & Device Harmonization for Portable Spectrometers

Calibration transfer between Jimini pen-like LED-based devices — each unit has different LED spectra, detector response, and optical paths. Models trained on one device must work on others **without** requiring paired urine samples. See [[normalization]] for day-to-day signal correction, [[matrix-correction]] for urine matrix effects, and [[signal-processing]] for preprocessing pipeline integration.

---

## Executive Summary

Calibration transfer between portable spectroscopic devices is a well-studied chemometrics problem with a toolbox spanning classical linear methods (DS, PDS), preprocessing-based approaches (EPO, SNV), and emerging ML/domain-adaptation methods (CORAL, adversarial networks, MVG augmentation). The key constraint for Jimini — **no paired urine samples** — rules out the classical gold-standard methods (DS, PDS) but opens three practical pathways: (1) unsupervised distribution alignment (CORAL), (2) reference-material calibration using water or known standards, and (3) pooled/augmented training designed to make models intrinsically device-agnostic. The 2025 blood IR paper demonstrates that just 17 paired reference measurements (not biological samples) enable effective domain adaptation via multivariate Gaussian augmentation — a highly applicable strategy for Jimini.

---

## Sources of Inter-Device Variability in LED-Based Systems

| Source | Type | Effect on Spectrum |
|--------|------|--------------------|
| LED peak wavelength shift | Additive wavelength offset | Channel response mismatch |
| LED spectral width (FWHM) variation | Convolution effect | Feature broadening/sharpening |
| LED intensity variation | Multiplicative scalar | Overall signal level shift |
| Detector quantum efficiency variation | Multiplicative per-channel | Channel-specific gain difference |
| Optical path length differences | Multiplicative + baseline | Absorption magnitude error |
| Temperature drift | Slow multiplicative drift | Gradual spectral shift |

For LED multi-channel photometers, channel-to-channel **multiplicative gain** errors are dominant. The Beer-Lambert law still holds per channel, so multiplicative corrections are physically motivated.

**AMS-OSRAM AS7341/AS7343 specifics:**
- Filter bandpass variation ±5–10 nm center wavelength, ±2–3 nm FWHM
- Photodiode responsivity variation 2–5% inter-unit (DS001046 v6-00)
- LED driver current matching affects absolute intensity, less so spectral shape

---

## Classical Calibration Transfer Methods

### Direct Standardization (DS)

**Paired samples required: YES** (≥6 same physical samples on both devices)

```
X_master ≈ X_slave · F
```

- **Math:** F = (X_slave^T X_slave)^{-1} X_slave^T X_master
- **For LED systems:** Works well because inter-unit variation is primarily multiplicative (linear); with only 6–8 LED channels, the matrix is small and well-conditioned
- **Reference:** Wang et al., *Anal. Chem.* 1991, 63, 2750

### Piecewise Direct Standardization (PDS)

**Paired samples required: YES** (≥10)

Applies local linear transformations per wavelength channel from a window of neighboring channels. Less suited than DS for LED systems — with only 6–11 channels, the concept of neighboring wavelength windows degenerates.

### Slope-Bias Correction

**Paired samples required: YES (3–5 samples only)**

```
ŷ_corrected = a + b · ŷ_slave
```

Simplest transfer: correct predicted values (not spectra) by a linear relationship. Good first-line correction if inter-unit bias is consistent. With 5 reference solutions (known concentrations) on both units, this can close most practical performance gap.

### External Parameter Orthogonalization (EPO)

**Paired samples required: NO (uses water/blank references only)**

```python
X_corrected = X · (I - P · P.T)
```

Projects out variation directions associated with instrument identity using a nuisance subspace (PCA of spectral differences on reference materials). **Highly practical for Jimini** — water reference scans on all units during factory calibration define the instrument subspace.

---

## No-Paired-Sample Methods

### CORAL — CORrelation ALignment

**Paired samples required: NO**

Aligns second-order statistics (covariance matrices) of source and target feature distributions:

```python
X_source_aligned = X_source · C_source^(-1/2) · C_target^(1/2)
```

- **Requirements:** Unlabeled target-domain spectra only
- **For Jimini:** Align pooled spectra from a new device to the training device distribution using any urine measurements — no reference values needed
- **Implementation:** `from adapt.feature_based import CORAL`
- **Reference:** Sun et al., arXiv:1612.01939

### Affine Invariance Transfer (CTAI)

**Paired samples required: NO**

Assumes differences between instruments are affine (shift + scale), recoverable from unlabeled sample distributions. Relevant since LED channel gain differences are well-modeled as per-channel affine transforms (Beer-Lambert).

- **Reference:** *Molecules* 2019, 24, 1802

### Filter Learning (Single Spectrum Transfer)

**Paired samples required: NO (needs only ONE spectrum from target)**

Learns a convolutional filter from a single reference spectrum (e.g., water blank) on the target instrument to transform all target spectra to the master space. **Potentially the most practical for Jimini** — a single water reference scan at device registration.

- **Reference:** *Anal. Chim. Acta* 2024, 342404

---

## Transfer Learning & Domain Adaptation (ML Methods)

### MVG Augmentation — Most Practically Relevant

**Paired samples required: FEW (~15–20 reference measurements)**

The 2025 blood IR paper (Leopold-Kerschbaumer et al., Anal. Chem.) demonstrates: 17 individuals with paired measurements on 2 FTIR devices improved cross-device AUC from 0.81–0.86 → 0.90–0.92 (matching within-device performance).

```python
def mvg_augmentation(X_device1, X_device2, n_synthetic=100):
    """
    X_device1, X_device2: spectra from same samples on 2 devices
    Returns: augmented training spectra covering both device distributions
    """
    # Cross-device covariance from paired differences
    diff = X_device1 - X_device2
    Sigma_cross = np.cov(diff.T)
    
    augmented = []
    for x in X_device1:
        synth = np.random.multivariate_normal(mean=x, cov=Sigma_cross, size=n_synthetic)
        augmented.append(synth)
    return np.vstack(augmented)
```

**For Jimini:** Measure 15–20 reference solutions ([[creatinin|creatinine]], [[urea]], [[uric-acid|uric acid]], known concentrations) on 2–3 devices. New field devices require NO paired measurements.

### Domain Adversarial Neural Networks (DANN)

**Paired samples required: NO (domain labels only)**

Trains a feature extractor to be domain-invariant via gradient reversal:

```
Loss = L_task(predictions, labels) - λ · L_domain(device_labels)
```

**Caution:** "Worst scanner syndrome" (Moyer & Golland, arXiv:2101.06255) — forcing domain invariance can destroy information if target domain has lower SNR. More applicable at fleet scale (20+ devices). With only 6 channels, overkill.

### Deep Calibration Transfer

Pre-train CNN/MLP on master device → freeze early layers → fine-tune last 1–2 layers on few reference solutions from target device. Standard-free variants also exist.

---

## LED-to-LED Variability: Specific Corrections

### Per-Channel Gain Normalization with Water Reference

**Paired samples required: NO**

Beer-Lambert gives: A = −log(I_sample / I_reference). Inter-unit LED intensity differences cancel in this ratio **if water reference is measured on the same unit**.

**Correction strategy (diagonal DS matrix):**
1. Measure water/blank on new device → convert to absorbance (cancels LED intensity)
2. Apply per-channel gain factors (multiplicative) from 3–5 reference solutions
3. Store 6 gain values (AS7341 channels) in firmware

### Factory Calibration Protocol (Practical for Jimini)

```
1. Measure 3–5 known reference solutions (creatinine, urea, uric acid at known concentrations) on each new unit during manufacturing QC
2. Fit per-channel gain factors → store in device firmware
3. Apply gain correction to all measurements before model prediction
4. Per-channel gain correction alone reduces systematic inter-unit errors to <1–2%
```

---

## AMS-OSRAM Sensor Comparison

| Feature | AS7341 | AS7343 |
|---------|--------|--------|
| Channels | 11 (6 spectral + clear + NIR + flicker) | 14 (broader spectral coverage) |
| Spectral range | ~380–1000 nm | ~340–1000 nm |
| Useful for absorbance | 6 filtered channels (415–680 nm) | 10+ filtered channels |
| Inter-unit filter variation | ±5 nm center, ±5% sensitivity | Similar |
| Recommended calibration | ATIME + AGAIN + white LED gain | Same |

After gain normalization per AMS recommendations, inter-unit variation reduces to ~2–3% (from ~5–10% uncorrected).

---

## Multi-Device Model Robustness Strategies

### Pooled Training

Train a single model on data from 2–3 representative devices. Sun et al. 2019 (MicroNIR study) showed pooled training + SVM achieved 96–98% cross-unit classification accuracy without any calibration transfer step. 3 units generally sufficient to cover manufacturing variability.

### Robust Preprocessing

| Preprocessing | Removes | Useful for |
|---------------|---------|-----------|
| SNV | Multiplicative + additive baseline | Unit intensity differences |
| MSC | Baseline + slope vs. mean spectrum | Scatter/path length variation |
| 1st Derivative (SG) | Additive baseline offset | LED intensity drift |
| L2 Normalization | Overall scale | Concentration-independent features |

After water-blank normalization (absorbance = −log(I/I₀)), residual preprocessing with SNV or L2 normalization handles remaining scale differences.

---

## Decision Matrix

| Method | Paired Samples | Reference Material | Computation | LED Suitability | Production-Ready |
|--------|---------------|-------------------|-------------|----------------|-----------------|
| DS | YES (≥6) | Same samples both devices | Low | Yes (with ref solutions) | Yes |
| PDS | YES (≥10) | Same samples both devices | Medium | No (too few channels) | Yes |
| Slope-Bias | YES (3–5) | Reference values sufficient | Trivial | Yes | Yes |
| EPO | NO | Water/blank on both | Medium | Yes | Yes |
| CORAL | NO | Unlabeled target spectra | Low | Yes | Yes |
| CTAI | NO | Unlabeled target spectra | Medium | Yes (affine model) | Conditional |
| Filter Learning | NO | 1 spectrum on target | Low | Yes | Yes |
| MVG Augmentation | FEW (~15–20) | Reference solutions | Medium | **Best option** | Yes |
| Deep Calibration Transfer | FEW | Target domain samples | High | Yes | Conditional |
| DANN | NO | Unlabeled target spectra | High | Yes | Future |
| Global Model | Multiple devices training | Any training data | Medium | Yes | Yes |
| Per-channel gain correction | NO | Reference solutions | Trivial | **Best option** | Yes (start here) |

---

## Practical Recommendations for Jimini

| Priority | Method | Pairs Needed | Expected Improvement | Effort |
|----------|--------|-------------|---------------------|--------|
| **1** | Water-reference normalization + SNV | 0 | Removes ~60–70% of inter-unit variation | Trivial |
| **2** | Per-channel gain correction with reference solutions | 0 (absolute concentrations known) | Reduces systematic gain errors to <1–2% | Low |
| **3** | MVG augmentation with cross-device covariance | 15–20 reference solution measurements across 2–3 units | Approaches within-device performance | Moderate |
| **4** | CORAL alignment (post-deployment) | 0 labeled pairs (unlabeled target spectra) | Moderate (2nd-order statistics) | Low |
| **5** | DANN (fleet-scale, future) | 0 in target domain | High if implemented correctly | High |

---

## Sources

| Source | Key Contribution |
|--------|-----------------|
| Leopold-Kerschbaumer et al., *Anal. Chem.* 2025, PMC12096352 | MVG augmentation for cross-device FTIR; 17 paired ref → AUC 0.81→0.92 |
| Surkova et al., *ACS Sensors* 2020, DOI:10.1021/acssensors.0c01018 | DS/PDS for LED multisensor systems — closest analog to Jimini |
| Sun et al., *Molecules* 2019, molecules-24-01997 | Pooled training + SVM; 96–98% cross-unit accuracy |
| Sun et al. (CORAL), arXiv:1612.01939 | Unsupervised covariance alignment |
| Mishra & Passos, *Infrared Phys. Technol.* 2021 | Deep calibration transfer; standard-free NIR transfer |
| *Anal. Chim. Acta* 2024, DOI:10.1016/j.aca.2024.342404 | Filter learning with single target spectrum |
| *Molecules* 2019, 24, 1802 | CTAI affine invariance without transfer standards |
| Moyer & Golland, arXiv:2101.06255 | Worst scanner syndrome warning for DANN |
| AMS-OSRAM DS001046 v6-00 | AS7343 datasheet; inter-unit sensitivity specs |
| Workman, *Spectroscopy Online* 2025, DOI:10.56530/spectroscopy.ie7568a1 | DS/PDS/EPO review; mathematical framework |

---

## Gaps

1. **LED spectral characterization**: Measure LED emission spectra of 5–10 Jimini units to quantify actual inter-unit variation (peak shift, FWHM). This determines which methods are sufficient.
2. **Reference solution design**: What reference solutions bracket Jimini's urine measurement space? Need: [[creatinin|creatinine]] (1–15 mM), [[urea]] (50–400 mM), [[uric-acid|uric acid]], pH range.
3. **Empirical comparison**: Run DS, slope-bias, CORAL, and MVG augmentation on actual Jimini inter-unit data. Theoretical preference is MVG + per-channel gain but empirical validation is needed.
4. **Temporal drift**: Methods above address unit-to-unit variation but not temporal drift (LED aging, detector degradation). EPO applied to water reference trends over time can address this separately.
5. **AS7343 vs AS7341 for urine**: AS7343's UV channel at ~340 nm could detect [[uric-acid|uric acid]] indirectly. AS7341 limited to 415+ nm.
