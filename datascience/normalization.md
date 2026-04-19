---
title: Signal Normalization in Photospectroscopy
aliases:
  - spectral normalization
  - cross-device normalization
  - scatter correction
tags:
  - topic/spectroscopy
  - topic/chemometrics
  - topic/signal-processing
  - type/concept
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: concept
author: Usense Healthcare
---

# Signal Normalization in Photospectroscopy

Two orthogonal normalization problems for the Jimini device: **(1) across urines** (sample matrix variability — dilution, color, turbidity, pH) and **(2) across devices** (sensor response variability — LED variation, detector gain, optical path). See [[matrix-correction]] for full urine matrix correction methods, [[calibration-transfer]] for device harmonization, and [[turbidity]] for turbidity-specific approaches.

---

## Part 1 — Normalizing Signals Across Urines

### Why It Matters

Urine is a highly variable matrix. The same biomarker concentration produces different spectra depending on:
- **Dilution** — hydration state shifts all concentrations
- **Color** — pigments (urobilin, bilirubin) add broad absorbing backgrounds
- **Turbidity** — particles scatter light multiplicatively, inflating all signals
- **Creatinine / osmolality** — proxies for overall concentration and renal output
- **pH and ionic strength** — shift peak positions and baseline

### Methods

#### 1. Creatinine Normalization

Divide analyte signal by urinary creatinine concentration. Creatinine is excreted at a roughly constant rate, making it a reliable dilution marker.

$$A_{\text{norm}} = \frac{A_{\text{analyte}}}{[\text{creatinine}]}$$

**Limitations:** Creatinine varies with muscle mass, age, and disease. Fails in extreme renal conditions. A Variable Power-Functional CRN Correction (V-PFCRC) improves on simple ratio normalization for nonlinear dilution effects. See [[matrix-correction]] for full V-PFCRC derivation.

#### 2. Specific Gravity / Osmolality Normalization

Refractometry or reagent strips measure specific gravity (SG); osmolality is more accurate but requires a separate instrument.

$$A_{\text{norm}} = \frac{A_{\text{raw}}}{\text{SG} - 1.000}$$

**Use when:** Creatinine measurement is unavailable. Prefer direct osmolality in pathological urines.

#### 3. Standard Normal Variate (SNV)

Per-spectrum transform: subtract spectrum mean, divide by spectrum standard deviation. Corrects both additive baseline offsets and multiplicative scatter differences without requiring a reference spectrum.

$$x_{\text{SNV}}(\lambda) = \frac{x(\lambda) - \bar{x}}{\sigma_x}$$

**Strengths:** Simple; no reference needed; handles particle size and turbidity scatter.
**Weaknesses:** Set-independent — cannot distinguish chemical change from scatter change.

> [!IMPORTANT]
> SNV is the **most validated preprocessing method for LED-based urine spectrophotometry**. In Kuenert et al. (2025), SNV reduced inter-sample spectral standard deviation by ~4 orders of magnitude (1097 → 0.24) for 401 clinical urine samples.

#### 4. Multiplicative Scatter Correction (MSC)

Regress each spectrum $x_i$ against a reference $\bar{x}$ (typically the calibration set mean) to estimate gain $a_i$ and offset $b_i$:

$$x_i(\lambda) \approx a_i \cdot \bar{x}(\lambda) + b_i \quad \text{(fit by OLS)}$$

$$x_{\text{MSC}}(\lambda) = \frac{x_i(\lambda) - b_i}{a_i}$$

**Strengths:** Interpretable parameters; removes turbidity-driven multiplicative and additive scatter.
**Weaknesses:** Set-dependent — the reference $\bar{x}$ must be stable and representative.

#### 5. Extended MSC (EMSC)

Extends MSC to include polynomial baselines, known interferent spectra, and fluorescence components:

$$x_i(\lambda) \approx a_i \cdot \bar{x}(\lambda) + b_i + c_i \cdot \lambda + d_i \cdot \lambda^2 + \sum_k e_{ik} \cdot f_k(\lambda)$$

Particularly powerful for biological fluids where broad fluorescence backgrounds (e.g., from urobilin) confound simple scatter correction. See [[matrix-correction]] for urine-specific EMSC implementation.

#### 6. Derivative Spectroscopy (Savitzky-Golay)

Apply first or second derivative via Savitzky-Golay smoothing:
- **1st derivative**: removes constant baseline offset
- **2nd derivative**: removes linear baseline; sharpens peaks (sign inverted)

**Use when:** Broad fluorescence background or color baseline dominates; sharp absorption features of interest.

#### 7. Water / Blank Reference Subtraction

The natural reference for Jimini: measure a water blank through the same optical path and divide (absorbance space):

$$A_{\text{urine}}(\lambda) = \log_{10}\!\left(\frac{I_{\text{water}}(\lambda)}{I_{\text{urine}}(\lambda)}\right)$$

Directly removes device-specific baselines AND water absorption background simultaneously. Device drift is handled per-measurement — no cross-device correction needed.

#### Recommended Pipeline for Jimini (Urine Normalization)

```
Raw signal
  → Dark subtraction
  → Water-reference normalization (log ratio → absorbance)
  → SNV or MSC (turbidity / color scatter)
  → SG derivative (optional, sharpen peaks)
  → Creatinine normalization (dilution, if creatinine available)
  → Feature extraction / model
```

---

## Part 2 — Normalizing Signals Across Devices

### Why It Matters

Two Jimini units measuring the same urine sample produce different spectra because:
- LED emission spectra vary (peak wavelength shift ±2–5 nm, intensity ±10–20%)
- Photodetector spectral response varies (quantum efficiency curve differs unit to unit)
- Optical path differences — lens, geometry, fibre coupling
- Gain and offset drift — temperature, ageing, firmware differences

A model trained on device A will fail on device B unless calibration transfer is applied.

### Methods

| Method | Paired samples needed | Handles multiplicative | Handles additive | Notes |
|--------|-----------------------|----------------------|-----------------|-------|
| Dark/White reference | No (hardware) | Yes | Yes | Must be done first |
| Sensitivity calibration | Factory ref needed | Yes | No | Per-device factory step |
| CCA (water baseline) | No | No | Yes | Simplest, field-friendly |
| Regression / MSC transfer | No (water only) | Yes | Yes | Good for Jimini |
| DS | Yes (paired) | Yes | Yes | Needs transfer samples |
| PDS | Yes (paired) | Yes | Yes | Handles wavelength shifts |
| CORAL | No | Yes | Yes | Covariance alignment |
| PCA alignment | No | Yes | Yes | Also denoises |
| LED crosstalk correction | Factory | Yes | No | LED-specific |

#### 1. Dark + White Reference Normalization

The fundamental hardware-level correction — must be applied before any preprocessing:

$$R(\lambda) = \frac{I_{\text{sample}}(\lambda) - I_{\text{dark}}(\lambda)}{I_{\text{ref}}(\lambda) - I_{\text{dark}}(\lambda)}$$

Removes detector offset and light-source intensity variation simultaneously.

#### 2. Regression Calibration (MSC-Based Cross-Device Transfer)

For each device $d$, regress its mean water spectrum onto the reference device's mean water spectrum:

$$\bar{x}_{\text{water},d}(\lambda) \approx a_d \cdot \bar{x}_{\text{water,ref}}(\lambda) + b_d$$

Apply inverse correction to urine:

$$x_{\text{corr}}(\lambda) = \frac{x_{\text{urine}}(\lambda) - b_d}{a_d}$$

Corrects both multiplicative (LED intensity, detector gain) and additive (dark offset, background) differences. Requires only water scans — no paired urine samples.

#### 3. CORAL — Correlation Alignment (No Paired Samples)

Aligns second-order statistics (covariance matrices) of source and target device distributions:

$$x_{\text{corr},i}(\lambda) = \frac{x_{\text{urine},i}(\lambda) - \mu_d(\lambda)}{\sigma_d(\lambda)} \cdot \sigma_{\text{ref}}(\lambda) + \mu_{\text{ref}}(\lambda)$$

**Strengths:** No paired samples needed; robust to varying device populations. See [[calibration-transfer]] for full CORAL implementation and comparison with other methods.

#### 4. Direct Standardization (DS)

When paired transfer samples are available, a linear transformation matrix $\mathbf{F}$ maps slave to master spectra:

$$\mathbf{X}_{\text{master}} = \mathbf{X}_{\text{slave}} \cdot \mathbf{F}$$

See [[calibration-transfer]] for the full DS/PDS/EPO decision tree.

#### Recommended Pipeline for Jimini (Cross-Device)

```
Per measurement:
  → Dark subtraction + water reference normalization

Per device (from water scans collected in field):
  → Estimate mean water spectrum per device
  → Regression calibration (additive + multiplicative) OR CORAL
    (both require only water scans — no paired urine samples needed)

Optional (if paired transfer samples available):
  → PDS for fine wavelength alignment

Model:
  → Train on reference device spectra
  → Apply cross-device correction before inference on slave devices
```

---

## Sources

| Source | Key Contribution |
|--------|-----------------|
| Kuenert et al. *Sci. Reports* 2025 | SNV reduces urine spectral SD by 4 orders of magnitude; LED 340–850 nm, n=401 |
| NIRPy Research: SNV/MSC comparison | https://nirpyresearch.com/two-scatter-correction-techniques-nir-spectroscopy-python/ |
| Workman 2018, Calibration Transfer Review | DS/PDS/CORAL review; Spectroscopy Online |
| CORAL paper — Sun et al. 2016, arXiv:1612.01939 | Unsupervised covariance alignment |
| AMS-OSRAM AS7343/AS7352 calibration methods | Spectral sensor factory calibration |
| Carmine, *Sci Rep* 2025 (PMC11782553) | V-PFCRC nonlinear dilution correction |
| EMSC R package (Khliland) | Extended MSC implementation |

---

## Gaps

1. **V-PFCRC for spectroscopic analytes**: Validated for metals/iodine by ICP-MS; unclear if the same c/d coefficients transfer to spectroscopically-estimated biomarkers (e.g., creatinine by Raman).
2. **LED-specific SNV behavior**: Most SNV validation is for bench-top spectrometers. Whether SNV behaves differently for narrow-band LED excitation sources (e.g., 275 nm LED with sparse spectral coverage) has not been characterized.
3. **Optimal cross-device method for Jimini**: The empirical comparison of water-reference regression calibration vs. CORAL vs. per-channel gain correction on actual Jimini inter-unit data has not been published.
