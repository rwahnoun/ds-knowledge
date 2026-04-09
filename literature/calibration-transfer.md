# Calibration Transfer & Device Harmonization for Portable Spectrometers

> **Context**: Jimini pen-like LED-based device — each unit has different LED spectra, detector response, and optical paths. Models trained on one device must work on others **without** requiring paired urine samples.

---

## Executive Summary

Calibration transfer between portable spectroscopic devices is a well-studied chemometrics problem with a toolbox spanning classical linear methods (DS, PDS), preprocessing-based approaches (EPO, SNV), and emerging ML/domain-adaptation methods (CORAL, adversarial networks, MVG augmentation). The key constraint for Jimini — **no paired urine samples** — rules out the classical gold-standard methods (DS, PDS) but opens three practical pathways: (1) unsupervised distribution alignment (CORAL, DTW), (2) reference-material calibration using water or known standards, and (3) pooled/augmented training designed to make models intrinsically device-agnostic. The recent 2025 blood IR paper demonstrates that just 17 paired reference measurements (not biological samples) enable effective domain adaptation via multivariate Gaussian augmentation — a highly applicable strategy for Jimini using simple reference solutions.

---

## 1. Sources of Inter-Device Variability in LED-Based Systems

LED-based multi-channel spectrometers (like Jimini, or AMS-OSRAM AS7341/AS7343 designs) have characteristic inter-unit variability from several hardware sources:

| Source | Type | Effect on Spectrum |
|--------|------|--------------------|
| LED peak wavelength shift | Additive wavelength offset | Channel response mismatch |
| LED spectral width (FWHM) variation | Convolution effect | Feature broadening/sharpening |
| LED intensity variation | Multiplicative scalar | Overall signal level shift |
| Detector quantum efficiency variation | Multiplicative per-channel | Channel-specific gain difference |
| Optical path length differences | Multiplicative + baseline | Absorption magnitude error |
| Temperature drift | Slow multiplicative drift | Gradual spectral shift |

For LED multi-channel photometers specifically, channel-to-channel **multiplicative gain** errors are dominant — each channel's effective sensitivity differs between units. This is fundamentally different from full-spectrum NIR where wavelength shift is the main concern. The **Beer-Lambert law** still holds for each channel, so multiplicative corrections are physically motivated.

**AMS-OSRAM AS7341/AS7343 specifics**: These 11/14-channel sensors have fixed photodiode arrays with on-chip interference filters. Inter-unit variation is primarily from:
- Filter bandpass variation (±5-10 nm center wavelength, ±2-3 nm FWHM)  
- Photodiode responsivity variation (2-5% inter-unit, per AMS datasheet DS001046 v6-00)
- LED driver current matching (affects absolute intensity, less so spectral shape)

---

## 2. Classical Calibration Transfer Methods

### 2.1 Direct Standardization (DS)
**Paired samples required: YES** (same physical samples on both devices)

DS assumes a global linear transformation from slave to master spectra:

```
X_master ≈ X_slave · F
```

Where `F` is a `p × p` transformation matrix (p = number of spectral channels) estimated via least squares using `n` transfer samples (typically n ≥ 6-12).

- **Math**: F = (X_slave^T X_slave)^(-1) X_slave^T X_master  
- **Requirements**: n ≥ p physically identical samples measured on both devices simultaneously
- **Strengths**: Simple, fast, well-understood
- **Weaknesses**: Requires paired samples; assumes globally linear relationship; fails if nonlinear distortions exist; ill-conditioned for p >> n
- **For LED systems**: Works well because inter-unit variation is primarily multiplicative (linear); with only 6-8 LED channels, the matrix is small and well-conditioned
- **Reference**: Wang et al., *Anal. Chem.* 1991, 63, 2750 (original DS paper); Workman, *Appl. Spectrosc.* 2018, 72(3), 340–365

### 2.2 Piecewise Direct Standardization (PDS)
**Paired samples required: YES**

Applies local linear transformations across the spectrum, where each wavelength channel is predicted from a window of neighboring channels:

```
x_master[i] = x_slave[i-w:i+w] · f_i
```

- **Math**: Local least-squares fit per channel using a sliding window of width 2w+1
- **Requirements**: Fewer transfer samples than DS (n ~ 10); but spectral resolution matters — for AS7341 with only 6 channels, the concept of "neighboring wavelength windows" degenerates
- **Strengths**: Handles local nonlinearities, wavelength shift correction
- **Weaknesses**: Computationally intensive; loses physical meaning for very-low-channel sensors (e.g., 6-channel LED); can overfit noise
- **For LED systems**: Less suited than DS because LED channels are spectrally sparse — no meaningful window of neighboring channels. DS is preferable for ≤12-channel sensors.
- **Reference**: Feudale et al., *Chemom. Intell. Lab. Syst.* 2002, 64, 181 (review); Igne & Hurburgh, *JNIRS* 2008 (evaluation)

### 2.3 Shenk & Westerhaus / Slope-Bias Correction
**Paired samples required: YES (few samples, ~3-5)**

The simplest calibration transfer: correct predicted *values* (not spectra) by a linear relationship between predicted outputs of slave and master:

```
ŷ_corrected = a + b · ŷ_slave
```

- **Math**: Linear regression of slave predictions vs. master predictions on transfer samples
- **Requirements**: 3-5 samples with known reference values (or measured by master) on both devices
- **Strengths**: Extremely simple, requires almost no data; sufficient for systematic additive/multiplicative bias
- **Weaknesses**: Cannot correct spectral shape differences; only fixes output-level bias/slope
- **For LED systems**: Good first-line correction if inter-unit bias is consistent. With 5 reference solutions (known concentrations) measured on both units, this can close most practical performance gap.
- **Reference**: Shenk & Westerhaus, *Crop Sci.* 1991; Mark & Workman Jr., *Spectroscopy* 2017, 32(2) (bias/slope correction discussion)

### 2.4 External Parameter Orthogonalization (EPO)
**Paired samples required: NO (if instrument variation is characterizable)**

EPO projects out variation directions associated with "external parameters" (instrument identity, temperature) using a nuisance subspace:

```
X_corrected = X · (I - P · P^T)
```

Where P is a matrix of principal directions of instrument variation (PCA of spectral differences between instruments measured on reference standards like water, Spectralon).

- **Math**: Compute PCA of difference spectra between instruments on reference materials → remove those components from sample spectra
- **Requirements**: Reference material (water, blank) measured on both instruments — **does NOT need biological/target samples paired**
- **Strengths**: Can use non-biological references; physically motivated (removes specific sources of variation)
- **Weaknesses**: Requires good estimation of instrument nuisance subspace; may remove signal if analyte correlates with nuisance directions
- **For Jimini**: **Highly practical** — water reference scans (or blank urine simulant) measured on all units during factory calibration can define the instrument subspace. Very low overhead.
- **Reference**: Roger et al., *Chemom. Intell. Lab. Syst.* 2003, 66, 191; Workman, *Spectroscopy Online* 2025

---

## 3. No-Paired-Sample Methods

### 3.1 CORAL — CORrelation ALignment
**Paired samples required: NO**

CORAL aligns the second-order statistics (covariance matrices) of the source and target feature distributions:

```
X_source_aligned = X_source · C_source^(-1/2) · C_target^(1/2)
```

- **Math**: Whitens source features, then applies target covariance structure. Minimizes Frobenius norm between covariance matrices of source and target domains.
- **Requirements**: Unlabeled target-domain spectra only — no paired samples, no labels needed
- **Strengths**: Unsupervised; closed-form solution; works when distributions differ in second-order statistics; easy to implement
- **Weaknesses**: Only aligns up to 2nd-order statistics (misses higher-order nonlinear differences); may not capture multiplicative channel gain differences well
- **For Jimini**: Can align pooled spectra from a new device to the training device distribution using any urine measurements (no reference values needed). Very practical for field deployment.
- **Implementation**: `adapt` Python library: `from adapt.feature_based import CORAL`
- **Reference**: Sun et al., *arXiv* 1612.01939 (CORAL); Baochen Sun, Kate Saenko — also in *Domain Adaptation in Computer Vision Applications* (Springer 2017)

### 3.2 DTW — Dynamic Time Warping Without Standards
**Paired samples required: NO**

DTW aligns spectral features by non-linear warping of the wavelength axis, matching features across instruments without requiring paired samples. The warping path is found by minimizing the cumulative distance between spectral matrices.

- **Math**: Min-cost alignment path through DTW distance matrix; scales warped slave spectra to master axis
- **Requirements**: Representative unlabeled spectra from both devices
- **Strengths**: Handles wavelength shifts well; no paired samples
- **Weaknesses**: Primarily a wavelength-axis correction — less effective for intensity/gain differences; computationally expensive for real-time use; degenerate for very sparse LED channels
- **For LED systems**: Limited applicability — with only 6-11 channels, there is no continuous spectral axis to warp. Better for full-spectrum devices.
- **Reference**: Zhimin Zhang group, *Anal. Methods* 2019, c9ay01139k — scalable calibration transfer without standards via DTW

### 3.3 Affine Invariance Transfer (CTAI)
**Paired samples required: NO**

Exploits affine invariance of the spectral space: assumes differences between instruments are affine transformations (shift + scale), recoverable from unlabeled sample distributions.

- **Math**: Finds affine map A, b such that X_target ≈ A · X_source + b using distribution-matching (moment matching or OT)
- **Requirements**: Sufficient unlabeled samples from target domain
- **Strengths**: Directly models multiplicative+additive inter-device differences; no standards needed
- **Weaknesses**: Assumes affine relationship (may underfit complex nonlinear differences); needs reasonable sample coverage of chemical space in target domain
- **For Jimini**: Relevant since LED channel gain differences are well-modeled as per-channel affine transforms (Beer-Lambert)
- **Reference**: Molecules 2019, 24, 1802 — "Calibration transfer method based on affine invariance without transfer standards (CTAI)"

### 3.4 Filter Learning (Single Spectrum Transfer)
**Paired samples required: NO (needs only ONE spectrum from target)**

A 2024 method that learns a spectral filter from a **single reference spectrum** on the target instrument and uses it to transform all target spectra to the master instrument space.

- **Math**: Learns a convolutional filter mapping target → master using regularized least-squares on one representative spectrum
- **Requirements**: One reference spectrum on target device (e.g., water, blank)
- **Strengths**: Minimal requirements; very practical for deployment
- **Weaknesses**: Single-sample estimation may be noisy; performance with very sparse channels unclear
- **For Jimini**: **Potentially the most practical** — a single water reference scan at device registration could calibrate to master
- **Reference**: *Analytica Chimica Acta* 2024, 342404 — "Calibration transfer via filter learning"

---

## 4. Transfer Learning & Domain Adaptation (ML Methods)

### 4.1 MVG Augmentation (Model-Based Domain Adaptation)
**Paired samples required: FEW (calibration set, ~15-20 reference measurements)**

The most practically relevant approach from recent literature (Anal. Chem. 2025). Fits a Multivariate Gaussian to the **cross-device** covariance structure using a small calibration set of reference samples measured on both devices, then **synthetically augments training data** to include device-specific variation.

**Key finding (blood IR spectroscopy, 2025)**:
- 17 individuals with paired measurements on 2 FTIR devices were sufficient as calibration set
- Cross-device classification AUC improved from 0.81–0.86 → 0.90–0.92 (matching within-device performance)
- Model 3 (cross-device covariance augmentation) drastically outperformed generic augmentation

**Algorithm (Model 3)**:
```python
# For each individual i in calibration set:
mean_i = mean(spectra_device1[i], spectra_device2[i])
# Pooled cross-device covariance:
Sigma_cal = mean([cov(spectra[i]) for i in calibration_set])
# Generate synthetic spectra:
synthetic = multivariate_normal(mean=mean_i, cov=Sigma_cal, n=100)
# Add synthetic spectra to training set
```

**For Jimini**: Measure 15-20 reference solutions (known concentrations of creatinine, urea, etc.) on 2-3 devices. Use the cross-device covariance to augment training data. New devices in the field require NO paired measurements.

**Reference**: Leopold-Kerschbaumer et al., *Anal. Chem.* 2025, 97(19), 10264 — "Bridging Spectral Gaps: Cross-Device Model Generalization in Blood-Based Infrared Spectroscopy" | [PMC12096352](https://pmc.ncbi.nlm.nih.gov/articles/PMC12096352/)

### 4.2 Deep Calibration Transfer
**Paired samples required: SOME (for fine-tuning)**

Transfer learning approach where a deep neural network trained on master device data is fine-tuned on a small dataset from the slave device:

- **Approach**: Pre-train CNN/MLP on master device → freeze early layers → fine-tune last layers on few target-device samples
- **Results (IR spectroscopy)**: Demonstrated for both FT-NIR benchtop and handheld NIR transfer; standard-free variant also tested
- **For Jimini**: If a neural network model exists (e.g., CNN on the 6-channel LED signal), fine-tuning the last 1-2 layers with even unlabeled target data (via self-supervised objectives) or few reference solutions can adapt it.
- **Reference**: Mishra & Passos, *Infrared Phys. Technol.* 2021, 117, 103863 — "Deep Calibration Transfer: Transferring Deep Learning Models Between Infrared Spectroscopy Instruments"

### 4.3 Domain Adversarial Neural Networks (DANN) / Adversarial DA
**Paired samples required: NO (domain labels only)**

DANN trains a feature extractor to be **domain-invariant** by adding a gradient-reversal layer that makes it impossible to distinguish which device a spectrum came from, while still predicting the analyte concentration:

```
Loss = L_task(predictions, labels) - λ · L_domain(device_labels)
```

- **Architecture**: Shared encoder → (a) task head (concentration predictor) + (b) domain discriminator with gradient reversal
- **Requirements**: Labeled data from source device + unlabeled data from target device (no paired samples, no labels on target)
- **Strengths**: Can learn device-invariant features; end-to-end trainable
- **Weaknesses**: Requires careful λ tuning; "worst scanner syndrome" — forcing domain invariance can destroy information if the domains have inherently different SNR; overkill for small datasets
- **For Jimini**: Feasible if enough unlabeled target-device spectra are available (e.g., from device validation scans). With only 6 channels, the encoder is very shallow — risk of overfitting. More applicable when collecting data at scale from deployed units.
- **Reference**: Ganin et al. (DANN original); Moyer & Golland, *arXiv* 2101.06255 (warns about "worst scanner syndrome" — domain invariance can hurt if target has less information than source)

### 4.4 CODI — Contextual Out-of-Distribution Integration
**Paired samples required: NO**

An approach related to MVG augmentation that integrates out-of-distribution variation (device-specific differences) into training using contextual information:

- Generates synthetic OOD samples by exploiting the structure of known distribution shifts
- Demonstrated in IR spectroscopy (blood plasma fingerprinting)
- **Reference**: Eissa et al., *PNAS nexus* 2024, 3(10), 449

---

## 5. LED-to-LED Variability: Specific Corrections

### 5.1 The Surkova 2020 ACS Sensors LED Multisensor Study (Most Directly Relevant)
**Paired samples required: YES (but only reference liquids)**

This is the closest literature analog to Jimini: calibration transfer **specifically for LED-based optical multisensor systems** (absorptiometric sensors with multiple LED light sources at different wavelengths).

**Key findings**:
- DS and PDS were successfully applied to transfer calibration models between LED multisensors and a full-scale laboratory spectrometer
- The LED multisensor had different LED emission spectra, detector responses, and optical geometries vs. lab reference
- Transfer was demonstrated for liquid sample analysis (dairy applications)
- Even with spectral mismatches between LED sources, DS captured the effective linear mapping between device responses

**Practical implications for Jimini**:
- A set of reference solutions (e.g., urine simulants with known creatinine/urea concentrations) measured on both master and slave units can support DS/PDS
- These reference solutions don't need to be actual patient urine — synthetic mixtures work
- **Reference**: Surkova et al., *ACS Sensors* 2020, DOI: 10.1021/acssensors.0c01018; correction DOI: 10.1021/acssensors.1c00659

### 5.2 Per-Channel Gain Normalization with Water Reference
**Paired samples required: NO**

For LED-based absorptiometric sensors, the Beer-Lambert relationship gives:

```
A = -log(I_sample / I_reference)
```

where `I_reference` is the incident light (water blank). Inter-unit LED intensity differences directly cancel in this ratio **if water reference is measured on the same unit**. This is built-in compensation.

**Residual inter-unit variation** after water normalization:
- Spectral width differences in LEDs → different effective molar absorptivity per channel
- Detector quantum efficiency differences → channel-specific gain offset

**Correction strategy**:
1. Measure water/blank on new device → normalize raw ADC to absorbance (cancels LED intensity)
2. Apply per-channel gain factors (multiplicative) estimated from a few reference solutions
3. This effectively reduces to a **diagonal DS matrix** — very robust with few transfer samples

**Practical protocol for Jimini factory calibration**:
- Measure 3-5 known reference solutions on each new unit during manufacturing QC
- Fit per-channel gain factors (6 values for AS7341) → store in device firmware
- Apply gain correction to all measurements from that unit before model prediction

---

## 6. AMS-OSRAM Sensor-Specific Considerations (AS7341, AS7343)

| Feature | AS7341 | AS7343 |
|---------|--------|--------|
| Channels | 11 (6 spectral + clear + NIR + flicker) | 14 (broader spectral coverage) |
| Spectral range | ~380–1000 nm | ~340–1000 nm |
| Useful for absorbance | 6 filtered channels (415-680 nm) | 10+ filtered channels |
| Inter-unit filter variation | ±5 nm center, ±5% sensitivity | Similar |
| Recommended calibration | ATIME + AGAIN + white LED gain | Same |

**AMS-recommended inter-unit correction approach** (from DS001046 datasheet):
- Factory calibration: measure Spectralon / white reference to normalize detector response
- GAIN registers set per-unit based on reference measurement
- After gain normalization, inter-unit variation reduces to ~2-3% (from ~5-10% uncorrected)

**Additional considerations for urine spectroscopy**:
- Urine is highly variable in baseline turbidity, color, and dilution
- This **within-sample** variation can mask inter-unit variation
- Ratiometric measurement (sample/water reference on same device) is essential first step
- Creatinine normalization can further reduce concentration-related variability

---

## 7. Multi-Device Model Robustness Strategies

### 7.1 Global Model / Pooled Training
Train a single model on data from 2-3 representative devices to span the inter-unit variation space:

- **Requirement**: Calibration data from at least 2-3 distinct units (same samples measured)
- **Performance**: Sun et al. 2019 (MicroNIR study) showed that pooled training + SVM/hier-SVM achieved 96-98% cross-unit classification accuracy without any calibration transfer step
- **Practical threshold**: 3 units generally sufficient to cover manufacturing variability if process is well-controlled

### 7.2 Robust Preprocessing (Preprocessing-Based Invariance)
Spectral preprocessing can make features intrinsically invariant to certain distortions:

| Preprocessing | Removes | Useful for |
|---------------|---------|-----------|
| Standard Normal Variate (SNV) | Multiplicative + additive baseline | Unit intensity differences |
| Multiplicative Signal Correction (MSC) | Baseline + slope vs. mean spectrum | Scatter/path length variation |
| 1st Derivative (Savitzky-Golay) | Additive baseline offset | LED intensity drift |
| 2nd Derivative | Additive + linear slope | Broader baseline variations |
| L2 Normalization | Overall scale | Concentration-independent features |

**Key finding** (Sun et al. 2019 MicroNIR): After SNV + SG-1st-derivative, spectra from different instruments became nearly identical for the same sample. Cross-unit model errors reduced from ~10-15% to <5% with preprocessing alone.

**For Jimini**: Since water-blank normalization already divides out most LED intensity variation (absorbance = -log(I/I₀)), the residual preprocessing needed is minimal. SNV or L2 normalization on the 6-channel absorbance vector handles remaining scale differences.

### 7.3 Tikhonov Regularization Model Transfer
Fine-tune a classical PLS/ridge regression model to a new device using Tikhonov regularization:

```
θ_new = argmin ||y - Xθ||² + λ||θ - θ_master||²
```

Pulls new model coefficients toward the master model, requiring only a few labeled samples on the new device. Related to EMSC-based model transfer.

### 7.4 Device ID as a Covariate
Encode device identity as a categorical variable in the model (device ID embedding), then train a model that learns device-specific offsets:

- **Approach**: Add device one-hot or embedding to feature vector; model learns per-device bias terms
- **Requirements**: Labeled data from each device, but inference works on known-ID devices
- **Limitation**: Requires re-training for every new device (not scalable)

---

## 8. Practical Recommendations for Jimini

### Priority 1 (Lowest Overhead): Water-Reference Normalization + SNV
- **What**: Divide all measurements by water reference (already computing absorbance), apply SNV
- **Pairs needed**: 0 (water measurement per reading)
- **Expected improvement**: Removes ~60-70% of inter-unit variation
- **Implementation effort**: Trivial (already in measurement protocol)

### Priority 2 (Factory Calibration): Per-Channel Gain Correction with Reference Solutions
- **What**: Measure 3-5 reference solutions (known [creatinine], [urea], [uric acid]) on each new unit during factory QC
- **Pairs needed**: 0 (absolute concentrations known; no master device needed)
- **Expected improvement**: Reduces systematic per-channel gain errors to <1-2%
- **Implementation effort**: Low (add to manufacturing test protocol)

### Priority 3 (Training-Time): MVG Augmentation with Cross-Device Covariance
- **What**: Measure 15-20 reference solutions on 2-3 representative units; use cross-device covariance to augment training data
- **Pairs needed**: 15-20 reference solution measurements across 2-3 units (NO patient urine needed)
- **Expected improvement**: Cross-device model performance approaches within-device (Anal. Chem. 2025 result)
- **Implementation effort**: Moderate (one-time calibration study; straightforward Python code)

### Priority 4 (Post-Deployment): CORAL Alignment
- **What**: Collect unlabeled spectra from deployed device; align distribution to training set using CORAL
- **Pairs needed**: 0 labeled pairs; just unlabeled target-device spectra
- **Expected improvement**: Moderate (aligns 2nd-order statistics); good for slow drift over time
- **Implementation effort**: Low (`adapt` Python library, 5 lines of code)

### Priority 5 (Advanced): DANN with Fleet-Scale Data
- **What**: Train domain-adversarial model once fleet reaches ~20+ devices with sufficient unlabeled data
- **Pairs needed**: 0 in target domain
- **Expected improvement**: High if implemented correctly (domain-invariant representations)
- **Implementation effort**: High (requires DL infrastructure, hyperparameter tuning, beware of worst-scanner-syndrome)

---

## 9. Decision Matrix

| Method | Paired Samples | Reference Material | Computation | Inter-Unit LED Suitability | Production-Ready |
|--------|---------------|-------------------|-------------|---------------------------|-----------------|
| DS | YES (≥6) | Same samples both devices | Low | ✓ (with reference solutions) | ✓ |
| PDS | YES (≥10) | Same samples both devices | Medium | ✗ (too few channels) | ✓ |
| Slope-Bias | YES (3-5) | Reference values sufficient | Trivial | ✓ | ✓ |
| EPO | NO | Water/blank on both | Medium | ✓ | ✓ |
| CORAL | NO | Unlabeled target spectra | Low | ✓ | ✓ |
| DTW | NO | Unlabeled spectra | Medium | ✗ (sparse channels) | Conditional |
| CTAI | NO | Unlabeled target spectra | Medium | ✓ (affine model) | Conditional |
| Filter Learning | NO | 1 spectrum on target | Low | ✓ | ✓ |
| MVG Augmentation | FEW (~15-20 ref meas.) | Reference solutions | Medium | ✓✓ (best option) | ✓ |
| Deep Calibration Transfer | FEW | Target domain samples | High | ✓ | Conditional |
| DANN | NO | Unlabeled target spectra | High | ✓ | Future |
| Global Model | Multiple devices training | Any training data | Medium | ✓✓ | ✓ |
| Per-channel gain correction | NO | Reference solutions | Trivial | ✓✓ | ✓ (start here) |

---

## 10. Mathematical Appendix

### DS Math
```
X_s: slave spectra matrix [n × p]
X_m: master spectra matrix [n × p]
F: transformation matrix [p × p]

Solve: min ||X_m - X_s · F||_F
Solution: F = (X_s^T X_s)^{-1} X_s^T X_m = pinv(X_s) · X_m

Apply: X_new_corrected = X_new · F
```

### CORAL Math
```
C_s: source covariance [p × p]
C_t: target covariance [p × p]

Transformation: A = C_s^{-1/2} · C_t^{1/2}
Apply: X_s_aligned = (X_s - μ_s) · A + μ_t

Sklearn-like:
coral = CORAL()
coral.fit(X_source, X_target)
X_adapted = coral.transform(X_source)
```

### MVG Augmentation (Cross-Device)
```python
import numpy as np

def mvg_augmentation(X_device1, X_device2, n_synthetic=100):
    """
    X_device1, X_device2: spectra from same samples on 2 devices
    Returns: augmented training spectra covering both device distributions
    """
    n_samples, n_channels = X_device1.shape
    
    # Cross-device covariance
    person_covs = []
    for i in range(n_samples):
        combined = np.vstack([X_device1[i:i+1], X_device2[i:i+1]])
        person_covs.append(np.cov(combined.T))  # Wrong for 2-sample case; use paired diff
    
    # Better: covariance of paired differences captures cross-device variation
    diff = X_device1 - X_device2
    Sigma_cross = np.cov(diff.T)
    
    # Augment: for each training sample, add synthetic variants
    augmented = []
    for x in X_device1:
        synth = np.random.multivariate_normal(mean=x, cov=Sigma_cross, size=n_synthetic)
        augmented.append(synth)
    
    return np.vstack(augmented)
```

---

## Sources

### Kept
- **Workman, Spectroscopy Online 2025** (doi:10.56530/spectroscopy.ie7568a1) — Comprehensive DS/PDS/EPO review, sources of inter-instrument variability, mathematical framework; highly relevant
- **Leopold-Kerschbaumer et al., Anal. Chem. 2025** (PMC12096352) — MVG augmentation for cross-device FTIR; directly applicable to Jimini paradigm
- **Sun et al., Molecules 2019** (molecules-24-01997) — Direct model transferability with miniature NIR; SVM vs PLS-DA; quantitative cross-unit error analysis; highly relevant for portable device design
- **Surkova et al., ACS Sensors 2020** (doi:10.1021/acssensors.0c01018) — **Calibration transfer for LED-based optical multisensor systems** — closest literature analog to Jimini
- **Sun et al. (CORAL), arXiv 1612.01939** — CORAL unsupervised domain adaptation; alignment of 2nd-order statistics
- **Mishra & Passos, Infrared Phys. Technol. 2021** — Deep calibration transfer; standard-free transfer between handheld NIR
- **Zhang et al., Anal. Methods 2019** (c9ay01139k) — DTW calibration without standards
- **Molecules 2019, 24, 1802** — CTAI affine invariance without transfer standards
- **ACS Anal. Chim. Acta 2024** (doi:10.1016/j.aca.2024.342404) — Filter learning with single target spectrum
- **AMS-OSRAM DS001046 v6-00** — AS7343 datasheet; inter-unit sensitivity specs; gain calibration registers
- **Feudale et al., Chemom. Intell. Lab. Syst. 2002, 64, 181** — Comprehensive calibration transfer review
- **Moyer & Golland, arXiv 2101.06255** — Worst scanner syndrome; important warning for DANN approaches

### Dropped
- DTW for LED systems (sparse channel structure makes warping meaningless)
- PDS for 6-channel sensors (window-based approach degenerates with <10 channels)
- Full-spectrum NIR papers without LED-specific components (useful for concepts but not directly applicable)
- EO/satellite sensor harmonization papers (Panopticon, DOFA — wrong domain)

---

## Gaps & Next Steps

1. **LED spectral characterization study**: Measure LED emission spectra of 5-10 Jimini units to quantify actual inter-unit variation (peak shift, FWHM). This determines which methods are sufficient.

2. **Reference solution design**: What reference solutions bracket Jimini's urine measurement space? Need: creatinine (1-15 mM), urea (50-400 mM), uric acid, pH range. These enable factory gain correction AND MVG augmentation.

3. **Empirical comparison**: Run DS, slope-bias, CORAL, and MVG augmentation on the actual Jimini inter-unit dataset (if available from early manufacturing). The theoretical preference is MVG + per-channel gain, but empirical validation needed.

4. **Temporal drift**: All methods above address unit-to-unit variation but not **temporal drift** (LED aging, detector degradation). EPO applied to water reference trends over time can address this separately.

5. **AS7343 vs AS7341 for urine**: AS7343's broader spectral coverage (340 nm UV channel) could detect uric acid directly. AS7341 limited to 415+ nm. Check if UV absorption matters for Jimini's analyte panel.

6. **Semi-supervised approaches**: Once Jimini has 10+ deployed units collecting data in the field, semi-supervised domain adaptation (e.g., pseudo-labeling + CORAL) could continuously improve cross-device performance without labels.
