# Signal Normalization in Photospectroscopy

> Context: Jimini device — urine biomarker estimation from LED-photodetector optical signals and EIS.
> Two orthogonal normalization problems: **(1) across urines** (sample matrix variability) and **(2) across devices** (sensor response variability).

---

## Part 1 — Normalizing Signals Across Urines

### Why it matters

Urine is a highly variable matrix. The same biomarker concentration will produce different spectra depending on:
- **Dilution** — hydration state shifts all concentrations
- **Color** — pigments (urobilin, bilirubin) add broad absorbing backgrounds
- **Turbidity** — particles scatter light multiplicatively, inflating all signals
- **Creatinine / osmolality** — proxies for overall concentration and renal output
- **pH and ionic strength** — shift peak positions and baseline

---

### Methods

#### 1. Creatinine Normalization (gold standard for dilution)

Divide analyte signal by urinary creatinine concentration. Creatinine is excreted at a roughly constant rate, making it a reliable dilution marker.

$$A_{\text{norm}} = \frac{A_{\text{analyte}}}{[\text{creatinine}]}$$

**Limitations:** creatinine itself varies with muscle mass, age, disease. Fails in extreme renal conditions. A variable-power functional correction (V-PFCRC) improves on simple ratio normalization for non-linear dilution effects.

- [Gold standard review — MDPI Biomolecules 2022](https://www.mdpi.com/2218-273X/12/7/903)
- [V-PFCRC method — Nature Scientific Reports 2024](https://www.nature.com/articles/s41598-024-84442-9)
- [Creatinine + MS signal combination — ACS Analytical Chemistry 2013](https://pubs.acs.org/doi/10.1021/ac401400b)

---

#### 2. Specific Gravity / Osmolality Normalization

Refractometry or reagent strips measure specific gravity (SG); osmolality is more accurate but requires a separate instrument. SG correlates linearly with osmolality for clean urines but diverges for pathological ones.

$$A_{\text{norm}} = \frac{A_{\text{raw}}}{\text{SG} - 1.000}$$

**Use when:** creatinine measurement is unavailable. Prefer direct osmolality in pathological urines.

- [SG vs osmolality comparison — PMC 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647580/)
- [Normalization to SG improves metabolomics — ACS Analytical Chemistry 2015](https://pubs.acs.org/doi/abs/10.1021/ac503190m)

---

#### 3. Standard Normal Variate (SNV)

A per-spectrum transform: subtract its mean, divide by its standard deviation. Corrects both additive baseline offsets and multiplicative scatter differences without needing a reference spectrum.

$$x_{\text{SNV}}(\lambda) = \frac{x(\lambda) - \bar{x}}{\sigma_x}$$

**Strengths:** simple, no reference needed, handles particle size / turbidity scatter.
**Weaknesses:** set-independent — applied to each spectrum individually, so it cannot distinguish chemical change from scatter change.

- [SNV vs MSC comparison — NIRPy Research](https://nirpyresearch.com/two-scatter-correction-techniques-nir-spectroscopy-python/)
- [SNV/MSC link — Academia.edu](https://www.academia.edu/35367842/The_link_between_Multiplicative_Scatter_Correction_MSC_and_Standard_Normal_Variate_SNV_transformations_of_NIR_spectra)

---

#### 4. Multiplicative Scatter Correction (MSC)

Regress each spectrum $x_i$ against a reference $\bar{x}$ (typically the mean spectrum of the calibration set) to estimate a gain $a_i$ and offset $b_i$:

$$x_i(\lambda) \approx a_i \cdot \bar{x}(\lambda) + b_i$$

Then correct:

$$x_{\text{MSC}}(\lambda) = \frac{x_i(\lambda) - b_i}{a_i}$$

**Strengths:** interpretable parameters; effectively removes turbidity-driven multiplicative and additive scatter.
**Weaknesses:** set-dependent — the reference $\bar{x}$ must be stable and representative.

- [NIRPy tutorial with Python code](https://nirpyresearch.com/two-scatter-correction-techniques-nir-spectroscopy-python/)

---

#### 5. Extended MSC (EMSC)

Extends the MSC model to include polynomial baselines, known interferent spectra, and fluorescence components in the regression:

$$x_i(\lambda) \approx a_i \cdot \bar{x}(\lambda) + b_i + c_i \cdot \lambda + d_i \cdot \lambda^2 + \sum_k e_{ik} \cdot f_k(\lambda)$$

Each term is subtracted before dividing by $a_i$. Particularly powerful for biological fluids where broad fluorescence backgrounds (e.g. from urobilin) confound simple scatter correction.

- [EMSC tutorial — ScienceDirect 2012](https://www.sciencedirect.com/science/article/abs/pii/S0169743912000494)
- [Physics-based EMSC — PubMed 2006](https://pubmed.ncbi.nlm.nih.gov/16608575/)
- [EMSC R package](https://cran.r-project.org/web/packages/EMSC/EMSC.pdf)

---

#### 6. Derivative Spectroscopy (Savitzky-Golay)

Apply first or second derivative via Savitzky-Golay smoothing. Derivatives suppress broad, slowly varying baselines and enhance narrow spectral features.

- 1st derivative: removes constant offset
- 2nd derivative: removes linear baseline, sharpens peaks (sign inverted)

**Use when:** broad fluorescence background or color baseline dominates; sharp absorption features of interest.

- [Preprocessing review — MDPI 2022](https://www.mdpi.com/1420-3049/27/6/1900)

---

#### 7. Water / Blank Reference Subtraction

Measure a water blank through the same optical path. Subtract (or divide in absorbance space) to isolate the sample contribution. This directly removes device-specific baselines AND the water absorption background simultaneously.

$$A_{\text{urine}}(\lambda) = \log_{10}\!\left(\frac{I_{\text{water}}(\lambda)}{I_{\text{urine}}(\lambda)}\right)$$

**This is the natural reference for Jimini:** the device scans water before urine, providing a per-device, per-measurement blank that handles both matrix and device drift.

---

#### 8. Turbidity Assessment and Correction

Turbidity correlates with nephelometric scatter (NTU) and can be estimated from the spectral baseline slope or a dedicated scatter wavelength (e.g. 800 nm where urine has no true absorbers). A turbidity-dependent correction factor can be applied before biomarker estimation.

- [Urine turbidity ↔ spectrophotometer color — PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12058184/)
- [Turbidity classification criteria — PLOS One 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0323351)

---

### Recommended Pipeline for Jimini

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

### Why it matters

Two Jimini units measuring the same urine sample will produce different spectra because:
- **LED emission spectra vary** (peak wavelength shift ±2–5 nm, intensity ±10–20%)
- **Photodetector spectral response varies** (quantum efficiency curve differs unit to unit)
- **Optical path differences** — lens, geometry, fibre coupling
- **Gain and offset drift** — temperature, ageing, firmware differences

A model trained on device A will fail on device B unless calibration transfer is applied.

---

### Methods

#### 1. Dark + White Reference Normalization (Radiometric Baseline)

The fundamental hardware-level correction. Every spectrometer measurement should begin here:

$$R(\lambda) = \frac{I_{\text{sample}}(\lambda) - I_{\text{dark}}(\lambda)}{I_{\text{ref}}(\lambda) - I_{\text{dark}}(\lambda)}$$

Where `dark` is measured with the light source off, and `ref` is a known reflectance standard or water blank. Removes detector offset and light-source intensity variation simultaneously.

- [Broadcom sensitivity calibration white paper](https://docs.broadcom.com/doc/sensitivity-calibration-with-broadcom-spectrometers-white-paper)
- [AMS-OSRAM AS7343/AS7352 calibration methods](https://look.ams-osram.com/m/3d28b734caad14b0/original/Spectral-Sensor-Calibration-Methods-AS7343-AS7352-Evaluation-Kit.pdf)

---

#### 2. Per-Wavelength Sensitivity Calibration

Characterise each device's spectral response function $S_d(\lambda)$ using a calibrated light source. Apply a per-wavelength gain correction:

$$x_{\text{corr}}(\lambda) = \frac{x_{\text{raw}}(\lambda)}{S_d(\lambda)}$$

**Requires:** factory calibration measurement per device. Stable for slow sensor drift; must be updated if LEDs age significantly.

- [NIST radiometric calibration guidelines](https://nvlpubs.nist.gov/nistpubs/hb/2015/NIST.HB.157.pdf)

---

#### 3. Additive Baseline Correction via Water Reference (CCA)

The simplest cross-device normalization that requires **no paired samples** of urine. Each device scans water; its mean water spectrum is treated as a device fingerprint. Correct urine by removing the device offset and adding back a reference:

$$x_{\text{corr},i} = x_{\text{urine},i} - \bar{x}_{\text{water},d} + \bar{x}_{\text{water},\text{ref}}$$

**Strengths:** no paired urine samples needed; directly uses water scans collected in the field.
**Limitations:** only corrects additive offset, not multiplicative gain differences.

---

#### 4. Regression Calibration (MSC-based Cross-Device Transfer)

For each device $d$, regress its mean water spectrum onto the reference device's mean water spectrum:

$$\bar{x}_{\text{water},d}(\lambda) \approx a_d \cdot \bar{x}_{\text{water,ref}}(\lambda) + b_d$$

Then apply the inverse to urine:

$$x_{\text{corr}}(\lambda) = \frac{x_{\text{urine}}(\lambda) - b_d}{a_d}$$

Corrects both **multiplicative** (LED intensity, detector gain) and **additive** (dark offset, background) differences simultaneously.

- [Calibration transfer Vis/NIR portable devices — ScienceDirect 2021](https://www.sciencedirect.com/science/article/abs/pii/S0925521421002593)

---

#### 5. Direct Standardization (DS)

When paired transfer samples (same sample measured on both master and slave device) are available, a linear transformation matrix $\mathbf{F}$ maps slave spectra to the master space:

$$\mathbf{X}_{\text{master}} = \mathbf{X}_{\text{slave}} \cdot \mathbf{F}$$

$\mathbf{F}$ is estimated by least squares from the paired transfer samples. The calibration model built on the master is then applied to transformed slave data.

- [Workman 2018 — Calibration Transfer Review, Spectroscopy](https://journals.sagepub.com/doi/10.1177/0003702817736064)
- [Calibration transfer by wavelength correspondence — ScienceDirect 2024](https://www.sciencedirect.com/science/article/pii/S0924203124000201)

---

#### 6. Piecewise Direct Standardization (PDS)

A windowed version of DS: for each wavelength of the master, only a local window of wavelengths on the slave is used in the regression. Handles wavelength shifts and local response differences better than global DS.

$$x_{\text{master}}(\lambda_j) = \sum_{k=j-w}^{j+w} x_{\text{slave}}(\lambda_k) \cdot f_{jk}$$

**Widely used in NIR calibration transfer** between instruments from different manufacturers.

- [PDS improvement — ScienceDirect 1996](https://www.sciencedirect.com/science/article/abs/pii/0169743995000747)
- [PDS for coffee origin ID — PMC 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9736488/)
- [Workman review Part II — Spectroscopy Online](https://www.spectroscopyonline.com/view/calibration-transfer-chemometrics-part-ii-review-subject)

---

#### 7. CORAL — Correlation Alignment (No Paired Samples)

Aligns the **second-order statistics (covariance matrix)** of the source device distribution to the target (reference) device distribution. Requires only unpaired spectra from each device — exactly the Jimini scenario.

$$C_{\text{target}} = A \cdot C_{\text{source}} \cdot A^T$$

where $A$ is learned to minimize $\| C_{\text{source}} - C_{\text{target}} \|_F^2$.

In the diagonal (per-wavelength) version: align mean and std per wavelength independently:

$$x_{\text{corr},i}(\lambda) = \frac{x_{\text{urine},i}(\lambda) - \mu_d(\lambda)}{\sigma_d(\lambda)} \cdot \sigma_{\text{ref}}(\lambda) + \mu_{\text{ref}}(\lambda)$$

**Strengths:** no paired samples; robust when device populations overlap; handles varying numbers of water records per device.

- [CORAL paper — arxiv 2016](https://arxiv.org/pdf/1612.01939)
- [Deep CORAL — Springer 2016](https://link.springer.com/chapter/10.1007/978-3-319-49409-8_35)
- [GitHub implementation](https://github.com/VisionLearningGroup/CORAL)

---

#### 8. PCA Latent-Space Alignment

Fit PCA on water spectra from all devices. Project each device's water spectra into the latent space, compute the mean projection per device. Shift urine projections to align with the reference device mean, then reconstruct.

$$z_{\text{urine},i} = P^T (x_{\text{urine},i} - \mu_{\text{global}})$$
$$z_{\text{corr},i} = z_{\text{urine},i} - \bar{z}_d + \bar{z}_{\text{ref}}$$
$$x_{\text{corr},i} = P \cdot z_{\text{corr},i} + \mu_{\text{global}}$$

The low-rank projection also acts as a **spectral noise filter**, suppressing high-frequency sensor noise.

- [Local-preserving PCA calibration transfer — ScienceDirect 2023](https://www.sciencedirect.com/science/article/abs/pii/S0924203123000450)

---

#### 9. LED Spectral Crosstalk Correction

Specific to LED-based narrowband devices like Jimini. Each LED has a finite bandwidth; adjacent LEDs overlap spectrally. A spectral correction matrix $\mathbf{C}$ (characterised per LED type at factory) deconvolves the crosstalk:

$$x_{\text{true}} = \mathbf{C}^{-1} \cdot x_{\text{measured}}$$

- [LED spectral correction for diffuse reflectance — PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10387445/)

---

### Method Comparison

| Method | Paired samples needed | Handles multiplicative | Handles additive | Notes |
|---|---|---|---|---|
| Dark/White reference | No (hardware) | ✅ | ✅ | Must be done first |
| Sensitivity calibration | Factory ref needed | ✅ | ❌ | Per-device factory step |
| CCA (water baseline) | No | ❌ | ✅ | Simplest, field-friendly |
| Regression / MSC transfer | No (water only) | ✅ | ✅ | Good for Jimini |
| DS | Yes (paired) | ✅ | ✅ | Needs transfer samples |
| PDS | Yes (paired) | ✅ | ✅ | Handles wavelength shifts |
| CORAL | No | ✅ | ✅ | Covariance alignment |
| PCA alignment | No | ✅ | ✅ | Also denoises |
| LED crosstalk correction | Factory | ✅ | ❌ | LED-specific |

---

### Recommended Pipeline for Jimini Cross-Device

```
Per measurement:
  → Dark subtraction + water reference normalization

Per device (from water scans collected in field):
  → Estimate mean water spectrum per device
  → Regression calibration (additive + multiplicative) OR CORAL
    (both require only water scans, no paired urine samples)

Optional (if paired transfer samples available):
  → PDS for fine wavelength alignment

Model:
  → Train on reference device spectra
  → Apply cross-device correction before inference on slave devices
```

---

## See Also

- [[comfyui/comfyui optimizations]] — signal processing references
- [[DATASCIENCE/MACHINE LEARNING/FeatureExtraction]] — feature extraction methods
- `d:/code/ds-learn/src/learn/projects/testHolyGrail/calibration.py` — CCA, MSC, CORAL, PCA implementations
- `d:/code/datascience/src/ds/process/transformers.py` — SNV, ScatterCorrection, SavitzkyGolay transformers
