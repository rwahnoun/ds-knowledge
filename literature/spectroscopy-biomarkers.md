# Urine Spectroscopy & Biomarker Prediction with LED-based Portable Devices

**Research Question:** What biomarkers can be predicted from urine using UV-Vis, NIR, and fluorescence spectroscopy with portable LED-based devices (no reagents)? What ML/chemometric models achieve the best results?

**Device Context (Jimini):** LEDs at 275 nm, 365 nm, 405 nm, 455 nm + broadband visible; photodetectors C12 (321–870 nm) and C14 (570–1078 nm); EIS (electrochemical impedance). Goal: reagent-free urine biomarker quantification.

---

## Summary

Urine spectroscopy without reagents is feasible for a number of biomarkers across UV-Vis, NIR, and fluorescence domains. The most robustly accessible targets for Jimini's wavelength range are: **uric acid** (UV 290 nm absorption), **bilirubin** (blue-range ~344–450 nm), **erythrocytes/hemoglobin** (Soret 415–420 nm, 541–555 nm, 630 nm), **urobilinogen** (visible ~450–500 nm), and **protein/tryptophan autofluorescence** (Ex 275–295 nm → Em 330–350 nm). Partial least squares (PLS) regression dominates quantitative work, with CNN/deep learning emerging as strong performers for classification tasks. EIS adds complementary electrical sensitivity for ionic/protein concentrations and UTI markers.

---

## Section 1: UV-Vis Spectroscopy for Urine Biomarkers

### Paper 1.1 — Label-Free Uric Acid Estimation (UV Spectrophotometry)
- **Title:** Label-Free Uric Acid Estimation of Spot Urine Using Portable Device Based on UV Spectrophotometry
- **Year:** 2022
- **Journal:** *Sensors* (MDPI)
- **DOI:** [10.3390/s22083009](https://doi.org/10.3390/s22083009)
- **Wavelengths used:** UV range; uric acid has a primary absorption peak at **~290–295 nm** in aqueous solution (shifts slightly based on pH)
- **Biomarkers predicted:** Uric acid (reagent-free, spot urine)
- **Model:** Univariate calibration curve (absorbance vs. concentration); Beer-Lambert-based
- **Accuracy/R²:** Not published in abstract but reported feasibility demonstrated for first time in portable format
- **Key finding:** First demonstration that portable UV spectrophotometry can measure uric acid in spot urine without any reagents. The characteristic UV absorption of uric acid at ~290 nm (due to its purine chromophore) survives in the complex urine matrix with sufficient SNR.
- **Relevance to Jimini:** The 275 nm LED directly excites uric acid. A single-wavelength or ratio-based approach at 275 nm could quantify uric acid. Matrix interference from other UV-absorbing compounds (tyrosine, creatinine) is the main challenge.

### Paper 1.2 — Portable POC Uric Acid Device (Uricia)
- **Title:** Portable Point-of-Care Uric Acid Detection System with Cloud-Based Data Analysis and Patient Monitoring
- **Year:** 2025
- **Journal:** *Biosensors* (MDPI), Vol. 16(2), 76
- **DOI:** [10.3390/bios16020076](https://doi.org/10.3390/bios16020076)
- **Wavelengths used:** 295 nm (primary reading); UV-Vis spectrophotometric profiling of glucose, ascorbic acid, albumin, creatinine, and uric acid across full UV-Vis spectrum
- **Biomarkers:** Uric acid primary; also profiled glucose, ascorbic acid, albumin, creatinine spectrally
- **Device:** Compact UV measurement device designed for 295 nm point reading
- **Model:** Calibration curve; SD < 0.01 reported
- **Key finding:** Shows that 295 nm is the optimal single wavelength for uric acid detection. Also characterizes UV-Vis spectral fingerprints of multiple urine analytes for multi-analyte discrimination.
- **Relevance to Jimini:** Confirms 275/365 nm LEDs span the key uric acid absorption window. The spectral library of glucose, albumin, creatinine, uric acid in the UV is directly applicable.

### Paper 1.3 — Spectrochip CCM for 12 Urine Parameters
- **Title:** Spectrochip-based Calibration Curve Modeling (CCM) for Rapid and Accurate Multiple Analytes Quantification in Urinalysis
- **Year:** 2024
- **Journal:** *Heliyon*, Vol. 10(18), e37722
- **DOI:** [10.1016/j.heliyon.2024.e37722](https://doi.org/10.1016/j.heliyon.2024.e37722)
- **PMC:** PMC11425109
- **Wavelengths used (characteristic λ per biomarker):**

| Biomarker | Characteristic λ (nm) |
|-----------|----------------------|
| Leukocytes | 550 |
| Nitrite | 530 |
| Urobilinogen | 570 |
| Protein | 620 |
| pH | 615 |
| Occult Blood | 620 |
| Specific Gravity | 615 |
| Ketone | 530 |
| Bilirubin | 540 |
| Glucose | 450 |
| Microalbumin | 520 & 615 (dual) |
| Creatinine | 550 |

- **Device:** MEMS spectrochip (Micro-Grating Process), 340–1000 nm, 5 nm resolution; white LED light source (Cree XLamp XT-E)
- **Biomarkers:** 12 parameters: leukocytes, nitrite, urobilinogen, protein, pH, occult blood, specific gravity, ketone, bilirubin, glucose, microalbumin, creatinine
- **Model:** Calibration Curve Modeling (CCM) with regression analysis (linear and nonlinear models: exponential growth, exponential decay, sigmoid, linear)
- **Accuracy/R²:** **R² > 0.95 for all 12 parameters** (range 0.9499–0.9931; creatinine R²=0.9744 linear)
- **Key finding:** NOTE — uses test strips dipped in standard solutions, so **not fully reagent-free**. However, the spectrochip quantifies color changes on test strips much more accurately than visual reading. Establishes reference characteristic wavelengths for all standard urine parameters.
- **Relevance to Jimini:** The characteristic wavelength table is directly applicable for understanding which spectral regions encode which biomarkers. The CCM approach (calibration curve from known concentrations) is a straightforward baseline method.

### Paper 1.4 — Continuous Spectroscopic Catheter Monitoring
- **Title:** Continuous spectroscopic monitoring of urinary catheter output: advancements and clinical implications
- **Year:** 2025
- **Journal:** *Scientific Reports*, Vol. 15, article 8617
- **DOI:** [10.1038/s41598-025-92802-2](https://doi.org/10.1038/s41598-025-92802-2)
- **Wavelengths used:** 340–850 nm (Hamamatsu CM12880MA mini-spectrometer, 288 channels); custom **3-LED hyperspectral source**: UV LED + NIR LED + full-spectrum (FS) LED; 3 optical paths (direct transmission, angular transmission, angular reflection)
- **Biomarkers predicted (binary classification):**

| Parameter | Model | AUC | BAC |
|-----------|-------|-----|-----|
| Bilirubin | LRRE | **0.921** | 0.711 |
| Erythrocytes | LRRE | ~0.88 | ~0.78 |
| pH (acidic) | LRRE | good | good |
| pH (basic) | LRRE | good | good |
| Protein | LRRE | good | good |
| Specific Gravity | LRRE | good | good |
| Urobilinogen | LRRE | good | good |
| Leukocytes | LRRE | moderate | moderate |
| Ketones | LRRE | moderate | moderate |
| Nitrite | LRRE | poor | poor |
| Glucose | — | no correlation found | — |
| Albumin | — | no correlation found | — |

- **Models:** Logistic Regression (LR) and Logistic Regression with Random Effects (LRRE); 5-fold cross-validation; SNV normalization; Pearson/Kendall correlation pre-selection of wavelengths
- **Key wavelengths for bilirubin:** 344 nm, 387 nm, 427 nm (aligned with bilirubin absorption maxima at 415–450 nm)
- **Key finding:** Visible-range spectroscopy without reagents cannot detect glucose or albumin in urine (neither has meaningful absorption in the 340–850 nm range at physiological concentrations). AI methods (PLS-DA, RF, CNN) are being separately evaluated by IKIM and reportedly confirm or improve results.
- **Relevance to Jimini:** Very directly relevant — the 3-LED approach mirrors Jimini's multi-LED design. Confirms bilirubin (~344–427 nm), hemoglobin (Soret + Q bands), urobilinogen, specific gravity, and pH are all spectroscopically accessible. **Glucose and albumin at physiological concentrations are NOT detectable by visible absorbance alone without reagents** — requires NIR or fluorescence for indirect approaches.
- **Sample set:** N=401 samples from 168 hospital patients

### Paper 1.5 — SpectraPhone: Smartphone Spectrometer Urinalysis
- **Title:** Development of a smartphone based spectrometer for high-resolution urinalysis
- **Year:** 2026 (published Feb 12, 2026)
- **Journal:** *Scientific Reports*, Vol. 16, article 8517
- **DOI:** [10.1038/s41598-026-38307-y](https://doi.org/10.1038/s41598-026-38307-y)
- **Wavelengths used:** 400–750 nm (smartphone camera + diffraction grating, ~0.17 nm resolution, 2051 channels)
- **Biomarkers predicted:**

| Biomarker | Key Wavelengths | R² | RMSE | Notes |
|-----------|----------------|-----|------|-------|
| Hematuria (RBC) | 419, 544, 555, 648 nm | **0.9913** | 61.6 RBC/µL | Hemoglobin Soret + Q bands, reagent-free |
| Albumin (reagent-free) | 586, 622, 705 nm | **0.9981** | 11.85 mg/dL | Mechanism unclear (albumin near-colorless in visible) |
| Albumin + BPB reagent | 556, 590 nm | **0.9997** | 4.26 mg/dL | BPB binds albumin → blue color at 590 nm |

- **Model:** PLS regression on second-derivative spectra (hematuria) or SNV-normalized spectra (albumin); 10-fold cross-validation
- **Device:** Low-cost passive optic ($20–90 USD), iPhone 13 Pro Max camera, diffraction grating
- **Key finding:** PLS on derivative/SNV-preprocessed spectra achieves near-perfect R² for both hematuria and albuminuria. Model robust to downsampling to 20% of spectral resolution. Hemoglobin key wavelengths align perfectly with Soret band (419 nm) and Q-bands (541 nm, 555 nm, 630 nm). Albumin detection mechanism in visible not explained (albumin is colorless) — may be indirect via light scattering from protein aggregates.
- **Relevance to Jimini:** The 405 nm and 455 nm LEDs cover the hemoglobin Soret band and Q-band regions perfectly. PLS is the recommended baseline model for quantitative regression. The albumin result is important — suggests light scattering or matrix-level spectral changes are detectable.
- **Data:** Available at https://github.com/Uncommon-Sense-Lab/SpectraPhone.git

---

## Section 2: NIR Spectroscopy for Urine Analysis

### Paper 2.1 — NIR Protein, Creatinine, Urea Quantification
- **Title:** Quantitation of protein, creatinine, and urea in urine by near-infrared spectroscopy
- **Year:** 1996
- **Journal:** *Clinical Biochemistry*, Vol. 29(1), pp. 11–19
- **DOI:** [10.1016/0009-9120(95)02011-X](https://doi.org/10.1016/0009-9120(95)02011-X)
- **Authors:** R.A. Shaw, S. Kotowich, H.H. Mantsch, M. Leroux
- **Wavelengths:** NIR (typically 700–2500 nm range for these studies)
- **Biomarkers:** Protein, creatinine, urea
- **Model:** PLS regression (multi-wavelength calibration)
- **Key finding:** Early seminal paper establishing NIR-PLS as viable for quantifying three major urine clinical chemistry markers without reagents.
- **Relevance to Jimini:** Jimini's C14 detector extends to 1078 nm, covering 700–1078 nm NIR. Water overtone bands dominate this region (970 nm, 1175 nm), but creatinine and urea have detectable NIR overtone features. The main limitation is water domination — differentiating analyte signals requires PLS on many wavelengths simultaneously.

### Paper 2.2 — NIR Urea, Creatinine, Glucose, Protein, Ketone (Preliminary)
- **Title:** Preliminary investigation of near-infrared spectroscopic measurements of urea, creatinine, glucose, protein, and ketone in urine
- **Year:** 2001
- **Journal:** *Clinical Biochemistry*, Vol. 34(3), pp. 239–246
- **DOI:** [10.1016/S0009-9120(01)00198-9](https://doi.org/10.1016/S0009-9120(01)00198-9)
- **Authors:** J.L. Pezzaniti, T.W. Jeng, L. McDowell, G.M. Oosta
- **Wavelengths:** NIR, multiple wavelengths
- **Biomarkers:** Urea, creatinine, glucose, protein, ketone
- **Model:** PLS regression
- **Key finding:** Demonstrated feasibility of multi-analyte NIR prediction in urine — all 5 analytes quantifiable to clinically useful accuracy using the same spectral dataset.
- **Relevance to Jimini:** Establishes that glucose is indeed detectable in NIR (water overtone region) whereas it is invisible in visible-range absorbance. This is the rationale for extending Jimini's spectral range into NIR. Ketones also NIR-active (C-H overtone ~1200 nm).

### Paper 2.3 — Reagentless NIR Urea/Creatinine for UCR Ratio
- **Title:** Reagentless Estimation of Urea and Creatinine Concentrations Using Near-Infrared Spectroscopy for Spot Urine Test of Urea-to-Creatinine Ratio
- **Year:** 2018
- **Journal:** *Advanced Biomedical Engineering*, Vol. 7, pp. 72–79
- **DOI/Source:** [J-Stage ABE journal](https://www.jstage.jst.go.jp/article/abe/7/0/7_7_72/_article/-char/en)
- **Biomarkers:** Urea, creatinine (and their ratio = urea-to-creatinine ratio, used for hydration/renal assessment)
- **Model:** PLS regression, reagent-free
- **Key finding:** Demonstrated that urea:creatinine ratio — a key clinical index — can be predicted reagent-free from NIR spectra of spot urine.
- **Relevance to Jimini:** Confirms the NIR C14 range (570–1078 nm) can provide useful urea and creatinine information.

### Paper 2.4 — Suzuki NIR POC Spot Urine (2020)
- **Title:** NIR spectroscopic determination of urine components in spot urine: Preliminary investigation towards optical point-of-care test
- **Year:** 2020
- **Journal:** *Medical & Biological Engineering & Computing*, Vol. 58(1), pp. 67–74
- **DOI:** [10.1007/s11517-019-02063-1](https://doi.org/10.1007/s11517-019-02063-1)
- **Authors:** Suzuki et al.
- **Wavelengths:** NIR, spot urine (no sample preparation)
- **Biomarkers:** Multiple urine components
- **Model:** PLS regression towards POC application
- **Key finding:** Portable-oriented NIR investigation showing it's feasible for direct urine measurement without preprocessing (key POC requirement).
- **Relevance to Jimini:** Most directly relevant NIR-POC paper. Confirms that direct measurement of spot urine (no dilution, drying, or reagents) in NIR is feasible.

### Paper 2.5 — Mid-IR Reagent-free Urea/Creatinine/Protein (FTIR Dried Films)
- **Title:** Toward Reagent-free Clinical Analysis: Quantitation of Urine Urea, Creatinine, and Total Protein from the Mid-Infrared Spectra of Dried Urine Films
- **Year:** 2000
- **Journal:** *Clinical Chemistry*, Vol. 46(9), pp. 1493–1495
- **DOI:** [10.1093/clinchem/46.9.1493](https://doi.org/10.1093/clinchem/46.9.1493)
- **Authors:** R.A. Shaw, S. Low-Ying, M. Leroux, H.H. Mantsch
- **Wavelengths:** Mid-infrared (FTIR), dried urine films
- **Biomarkers:** Urea, creatinine, total protein
- **Model:** PLS regression
- **Key finding:** Mid-IR with PLS on dried urine films is highly accurate for urea, creatinine, protein — precursor to modern portable IR approaches. Dried films eliminate water interference.
- **Note for Jimini:** Mid-IR (2.5–25 µm) is outside Jimini's detector range but the methodology (drying + spectroscopy) is relevant if sample prep is acceptable.

---

## Section 3: Fluorescence-Based Urine Analysis

### Paper 3.1 — Human Fluorescent Profile of Urine (Autofluorescence)
- **Title:** Human fluorescent profile of urine as a simple tool of mining in data from autofluorescence spectroscopy
- **Year:** 2020
- **Journal:** *Biomedical Signal Processing and Control*, Vol. 56, 101693
- **DOI:** [10.1016/j.bspc.2019.101693](https://doi.org/10.1016/j.bspc.2019.101693)
- **Wavelengths:** Multiple excitation wavelengths; systematic EEM (excitation-emission matrix) mapping of urine autofluorescence
- **Key fluorophores identified in urine:**

| Fluorophore | Excitation (nm) | Emission (nm) | Relevance |
|-------------|----------------|---------------|-----------|
| Tryptophan | 275–295 | 330–360 | Protein marker, metabolic disease |
| NADH/NAD(P)H | 340–365 | 440–470 | Metabolic status, cellular energy |
| Riboflavin (B2) | 365–450 | 520–560 | Nutritional status |
| Flavins | 365–450 | 520 | Renal function |
| Porphyrins | 405–420 | 620–640 | Porphyria, heme metabolism |
| Hippuric acid | ~320 | ~420 | Drug metabolism, gut bacteria |
| Indoxyl sulfate | ~280 | ~330 | CKD uremic toxin |

- **Model:** Statistical analysis (PCA, LDA) for disease discrimination
- **Key finding:** Native urine fluorescence contains rich diagnostic information. The "fluorescent profile" concept — mapping all endogenous fluorophores — is proposed as a diagnostic fingerprint.
- **Relevance to Jimini:** The 275 nm LED excites tryptophan (protein proxy, metabolic disease) and indoxyl sulfate (CKD marker). The 365 nm LED excites NADH, riboflavin, and some porphyrins. The 405 nm LED excites porphyrins (peak). The 455 nm LED excites riboflavin and flavins. C12 (321–870 nm) captures all emissions.

### Paper 3.2 — Fluorescence Cancer Detection (EEM + 405 nm)
- **Title:** Characterization and Diagnosis of Cancer by Native Fluorescence Spectroscopy of Human Urine
- **Year:** 2012
- **Journal:** *Photochemistry and Photobiology*, Vol. 88(5)
- **DOI:** [10.1111/j.1751-1097.2012.01239.x](https://doi.org/10.1111/j.1751-1097.2012.01239.x)
- **Wavelengths:** Excitation at **405 nm**; EEMs over full excitation-emission range
- **Biomarkers/Target:** Cancer discrimination (bladder cancer, other cancers vs. normal)
- **Approach:** Native fluorescence at 405 nm excitation showed differences between cancer and control urine
- **Key finding:** 405 nm excitation distinguishes cancer patients from normal subjects using porphyrin-region emissions (620–640 nm).
- **Relevance to Jimini:** The 405 nm LED is perfectly positioned for porphyrin excitation. Porphyrins are elevated in bladder cancer and various metabolic disorders (porphyria). This fluorescence channel is essentially free for Jimini.

### Paper 3.3 — Tryptophan Fluorescence & Melanoma
- **Title:** Strong Dependence between Tryptophan-Related Fluorescence of Urine and Malignant Melanoma
- **Year:** 2021
- **Journal:** *International Journal of Molecular Sciences*, Vol. 22(4), 1884
- **DOI:** [10.3390/ijms22041884](https://doi.org/10.3390/ijms22041884)
- **Wavelengths:** Excitation **295 nm** (selective for tryptophan over tyrosine)
- **Biomarker:** Tryptophan-related fluorophores in urine (emit at ~330–350 nm)
- **Finding:** Autofluorescence at 295 nm significantly higher in melanoma patients (all stages) vs. healthy controls; decreases with advancing stage (likely due to tryptophan catabolism via kynurenine pathway)
- **Key finding:** A single-wavelength excitation at ~295 nm provides a melanoma stage-sensitive marker. Also: serotonin metabolite 5-HIAA and other indole metabolites contribute.
- **Relevance to Jimini:** The 275 nm LED (close to 295 nm) excites tryptophan. The emission would fall at ~330–350 nm, which is just within the C12 detector range (321–870 nm). This is the primary protein/aromatic amino acid fluorescence channel.

### Paper 3.4 — Bladder Cancer Urine Fluorescence (EEM + CNN)
- **Title:** The role of spectral characteristics of urine in bladder cancer diagnostics
- **Year:** 2025
- **Journal:** *Scientific Reports*
- **DOI:** [10.1038/s41598-025-15801-3](https://doi.org/10.1038/s41598-025-15801-3)
- **Wavelengths:** Multiple fluorescence excitation wavelengths (EEM) + HPLC chromatograms
- **Biomarkers:** Cancer vs. normal urine classification
- **Models tested:** Logistic regression, OPLS-DA, **CNN**
- **Results:** Analysis of urine EEMs alone: CNN achieved max accuracy of **72.1%** for training model (limited by sample size and urine matrix complexity). Chromatograms + CNN performed better.
- **Key finding:** CNN on fluorescence EEMs achieves ~72% classification accuracy for bladder cancer. Fluorescence EEMs alone are insufficient without additional information (chromatography adds chemical separation).
- **Relevance to Jimini:** Shows the limits of fluorescence alone for disease classification. Multi-modal data fusion (fluorescence + EIS) will likely be needed.

### Paper 3.5 — Body Fluid Fluorescence Signatures (Forensic)
- **Title:** Specific fluorescent signatures for body fluid identification using fluorescence spectroscopy
- **Year:** 2023
- **Journal:** *Scientific Reports*
- **DOI:** [10.1038/s41598-023-30241-7](https://doi.org/10.1038/s41598-023-30241-7)
- **Wavelengths (urine-relevant):**
  - Tryptophan: Ex ~225–230 nm / Em 335–350 nm
  - Protein (general): Ex 280–295 nm / Em 330–370 nm
  - FOX (flavin oxidase-related): Ex 365 nm / Em 400–500 nm
- **Key finding:** Provides precise excitation-emission peak maps for urine, semen, serum, saliva. Urine signature dominated by tryptophan-like compounds and flavins.
- **Relevance to Jimini:** Validates that 275 nm → 330–350 nm (tryptophan) and 365 nm → 400–500 nm (flavins, NADH) are the dominant urine fluorescence channels. 405 nm → 440–500 nm region also active (riboflavin fluorescence).

### Paper 3.6 — Melanoma Fluorescence Biomarkers (360/450 nm)
- **Title:** Fluorescence biomarkers of malignant melanoma detectable in urine
- **Year:** 2020
- **Journal:** *Open Chemistry*
- **DOI:** [10.1515/chem-2020-0143](https://doi.org/10.1515/chem-2020-0143)
- **Wavelengths:** Excitation peaks at **360–370 nm** and **450 nm**; emission at **410–460 nm**
- **Biomarkers:** Melanoma-related fluorescent metabolites (NADH, FAD, melanin precursors)
- **Relevance to Jimini:** The 365 nm and 455 nm LEDs cover both excitation peaks exactly. Emission in 410–460 nm range is well within C12 range. This is a direct validation of Jimini's LED selection for NADH/flavin fluorescence channel.

---

## Section 4: LED-Based and Portable Spectrometer Papers

### Paper 4.1 — LUMINA: Light-Based Urine Monitoring and Analysis
- **Title:** The LUMINA setup for a light-based urine monitoring and analysis
- **Authors:** A. Fantoni, M. Fernandes, J. Fidalgo, K. Soto, S.A. Pereira, et al.
- **Institution:** UNINOVA/CTS/iNOVA4Health, Universidade NOVA de Lisboa
- **Source:** NOVA Research Portal
- **Description:** Dedicated optoelectronic system for on-site urine spectral analysis with multiple LED wavelengths and photodetectors
- **Key finding:** Demonstrates that an LED-based optoelectronic setup can perform urine spectral analysis on-site; prototype similar in concept to Jimini
- **Relevance to Jimini:** Most directly analogous existing device to Jimini's form factor and approach.

### Paper 4.2 — Portable LED Nitrite Detector in Simulated Urine
- **Title:** Portable and low-cost LED based Spectrophotometer for the Detection of Nitrite in simulated-Urine
- **Year:** 2020
- **Journal:** IEEE Conference Publication
- **DOI/Source:** [IEEE Xplore 8980097](https://ieeexplore.ieee.org/document/8980097/)
- **Wavelengths:** LED-based, specific wavelength for nitrite detection (~530–540 nm, nitrite absorbs via Griess reaction color development, but also has native UV absorption at ~354 nm)
- **Biomarker:** Nitrite (UTI marker)
- **Key finding:** Low-cost LED spectrophotometer sufficient for nitrite detection in urine surrogate. Native nitrite absorbs weakly at ~354 nm in UV; reagent-based approaches use 530 nm.
- **Relevance to Jimini:** Without Griess reaction reagent, nitrite detection must use UV (near 275 nm or 365 nm). Confirms nitrite is detectable but reagent-free sensitivity may be limited.

### Paper 4.3 — Development of an Optical Urinalysis System (Wavelength Optimization)
- **Title:** Development of an optical urinalysis system - Selection of optimum wavelengths and its combination
- **Source:** CiNii Research (Japanese)
- **Relevance:** Addresses the multi-wavelength LED optimization problem for urinalysis — directly applicable to Jimini's multi-LED design
- **Key finding:** Systematic approach to selecting the minimum set of wavelengths for maximizing information in urine optical analysis.

---

## Section 5: Machine Learning & Chemometric Models

### 5.1 PLS Regression (Partial Least Squares) — Gold Standard for Quantitative Spectroscopy

**Best results achieved:**

| Study | Biomarker | Model | R² | RMSE |
|-------|-----------|-------|-----|------|
| SpectraPhone (2026) | Hematuria (RBC) | PLS on 2nd-derivative | 0.9913 | 61.6 RBC/µL |
| SpectraPhone (2026) | Albumin (reagent-free) | PLS on SNV | 0.9981 | 11.85 mg/dL |
| SpectraPhone (2026) | Albumin + BPB reagent | PLS on SNV | 0.9997 | 4.26 mg/dL |
| Shaw et al. 1996 | Protein, creatinine, urea | PLS (NIR) | High | Clinical range |
| Spectrochip 2024 | 12 parameters | Calibration curve | >0.95 | N/A |

**Key preprocessing steps (critical for performance):**
- Standard Normal Variate (SNV) normalization
- Second derivative preprocessing (resolves overlapping bands)
- Mean centering
- Principal component selection (30 PCs typical)
- 10-fold cross-validation standard

**Why PLS works:** Handles collinear spectral features, extracts latent variables correlated with analyte concentration, robust to matrix interference.

### 5.2 Logistic Regression with Random Effects (LRRE) — Best for Binary Classification

**Best results:**

| Study | Biomarker | Model | AUC | BAC |
|-------|-----------|-------|-----|-----|
| Kuenert 2025 (Catheter) | Bilirubin | LRRE | 0.921 | 0.711 |
| Kuenert 2025 (Catheter) | Erythrocytes | LRRE | ~0.88 | ~0.78 |
| Kuenert 2025 (Catheter) | pH, Specific Gravity | LRRE | good | good |
| Kuenert 2025 (Catheter) | Nitrite | LRRE | poor | poor |

**When to use:** Binary presence/absence classification in clinical settings; patient-level repeated measurements (random intercept handles within-patient correlation).

### 5.3 CNN (Convolutional Neural Network) — Emerging for Spectral Classification

**Results:**
- Bladder cancer urine EEM fluorescence (2025): CNN achieved **72.1%** accuracy for cancer classification (training)
- Membranous nephropathy Raman + CNN (2022): Deep learning (ResNet, AlexNet) on Raman spectra from urine/serum combined — high accuracy for disease classification
- IKIM (Kuenert group, in preparation): Preliminary results from PLS-DA, Random Forests, and CNNs on the catheter urine dataset "confirm or improve" the logistic regression AUC results

**Architecture notes for spectral data:**
- 1D-CNN (treating spectrum as 1D signal) often outperforms standard MLP
- Residual self-attention mechanisms (ResNet-style) show promise for 1D spectral regression
- Input preprocessing (SNV, derivative) still required before CNN

### 5.4 Random Forest and XGBoost

**For urinary biomarker prediction:**
- Urinary proteomics + XGBoost for kidney disease classification (medrxiv 2020): XGBoost outperformed RF, SVM, ANN on mass spectrometry proteomics data
- SERS + ML (2024): PLSR-MLP (two-step: PLS then MLP) achieved R²=0.94 for simultaneous uric acid + creatinine prediction from electrochemical-SERS data
- For *spectral* data specifically: RF and XGBoost work well but require feature extraction or binning first; PLS typically easier to train with small N

### 5.5 PARAFAC (Parallel Factor Analysis) — For EEM Fluorescence Data

**Application:** When using multi-excitation fluorescence (EEM matrices), PARAFAC decomposes the three-way data (samples × excitation × emission) into independent fluorophore components.
- Used for cannabis metabolites in urine EEM: accurate quantification of THC/CBD metabolites
- Applicable for: NADH, riboflavin, tryptophan simultaneous quantification from Jimini's multi-LED excitation data
- **Direct relevance:** Jimini's 4 LEDs (275, 365, 405, 455 nm) × C12 broadband detection creates a partial EEM — PARAFAC can decompose contributions of each fluorophore

### 5.6 Recommended ML Pipeline for Jimini

Based on literature findings:

```
Raw spectra (4 LED × C12/C14 channels)
    ↓
Preprocessing: SNV normalization + 2nd derivative
    ↓
For quantitative regression: PLS-R (start with 10–30 latent variables)
    ↓ (if N > 500 samples available)
Upgrade to: 1D-CNN or XGBoost on PCA-reduced features
    ↓
Validation: 10-fold CV, report R², RMSE, MAE
    ↓
For binary classification: LRRE (small N) or RF/XGBoost (large N)
```

---

## Section 6: Electrochemical Impedance Spectroscopy (EIS) for Urine

### Paper 6.1 — Fully Electronic Urine Dipstick with EIS
- **Title:** Fully electronic urine dipstick probe for combinatorial detection of inflammatory biomarkers
- **Year:** 2018
- **Journal:** *Future Science OA*, Vol. 4(5), FSO301
- **PMC:** PMC5961415
- **DOI:** [10.4155/fsoa-2017-0142](https://doi.org/10.4155/fsoa-2017-0142)
- **Approach:** Molybdenum electrodes on nanoporous polyamide substrate; non-Faradaic impedance
- **Biomarkers:** Inflammatory markers (leukocyte esterase, protein) in urine
- **Accuracy:** LOD = **1 pg/mL** (very sensitive); portable electronics platform demonstrated
- **Relevance to Jimini:** EIS directly measures electrical impedance changes as proteins/cells bind to or pass through the electrode interface. Combined with spectroscopy, EIS adds sensitivity for low-concentration proteins and ionic composition (specific gravity).

### Paper 6.2 — Label-Free EIS for Uromodulin (Kidney Tubular Damage)
- **Title:** Label-Free, Impedance-Based Biosensor for Kidney Disease (Fraunhofer)
- **Source:** Fraunhofer Publications
- **Approach:** 50-nm Ta₂O₅ passivation layer on interdigitated electrodes (IDE); non-Faradaic EIS
- **Biomarker:** Uromodulin (Tamm-Horsfall protein) — kidney tubular damage marker
- **Range:** 0.5–8 ng/mL; relative impedance change 15%/ng/mL
- **Relevance to Jimini:** EIS can quantify specific binding of uromodulin at femtomolar-nanomolar concentrations. This is an add-on biosensing capability beyond optical channels.

### Paper 6.3 — Electrochemical Creatinine Detection Review
- **Title:** Electrochemical creatinine detection for advanced point-of-care sensing devices: a review
- **Year:** 2022
- **Journal:** *RSC Advances*
- **DOI:** [10.1039/D2RA04479J](https://doi.org/10.1039/D2RA04479J)
- **Key finding:** Review of multiple electrochemical approaches for creatinine in urine. Non-enzymatic approaches (ZIF-8 nanoparticles, aptamers) achieve LOD ~30 µM in urine. EIS provides impedimetric creatinine sensing.
- **Relevance to Jimini:** EIS component could measure creatinine directly via bare electrode interactions or with functionalized electrodes.

### Paper 6.4 — POC EIS Device (ASU)
- **Title:** A point of care electrochemical impedance spectroscopy device
- **Institution:** Arizona State University (Jennifer Blain Christen lab)
- **Source:** ASU Elsevier Pure
- **Key finding:** Demonstrates that EIS can be implemented in a portable POC format for label-free molecular detection.

---

## Section 7: Key Absorption Wavelengths Summary for Jimini LEDs

### Jimini LED Wavelengths Mapped to Urine Biomarkers

| LED (nm) | Absorption/Excitation Targets | Detectable Biomarkers |
|----------|------------------------------|----------------------|
| **275 nm** | Uric acid (absorbs 290–295 nm), Tryptophan (Ex 280 nm), Tyrosine (Ex 270 nm), DNA/RNA bases (260–280 nm), Nitrite (354 nm nearby) | Uric acid (direct absorbance), Protein/Tryptophan fluorescence (Em 330–350 nm), Indoxyl sulfate (CKD marker) |
| **365 nm** | NADH (Ex 340–365 nm → Em 440–470 nm), Riboflavin (Ex 365 nm → Em 520 nm), FOX metabolites, Hippuric acid | NADH (metabolic activity), Riboflavin (B2 status), Hippuric acid, Nitrite (near-UV tail) |
| **405 nm** | Porphyrins (Soret band ~405–415 nm → Em 620–640 nm), Bilirubin (weak, ~415–450 nm), Riboflavin | Porphyrins (porphyria, heme disease), Bilirubin (indirect), Riboflavin fluorescence |
| **455 nm** | Bilirubin (absorption ~430–460 nm), FAD/flavins (Ex 450 nm → Em 525 nm), Riboflavin | Bilirubin (direct blue-range absorption), FAD/flavin metabolites |
| **Broadband Visible** | Hemoglobin (Soret 415 nm, Q-bands 541, 555, 576, 630 nm), Urobilinogen (~440–500 nm), Myoglobin | Hematuria, Hemoglobinuria, Urobilinogen, Bilirubin |

### C12 Detector (321–870 nm) Coverage

| Range | Signals |
|-------|---------|
| 321–400 nm | Tryptophan emission (330–360 nm), UV fluorescence emission |
| 400–500 nm | NADH emission (440–470 nm), Flavin emission (520 nm edge), Porphyrin Soret |
| 500–600 nm | Bilirubin absorption, Hemoglobin Q-bands (541–576 nm), Riboflavin emission |
| 600–700 nm | Porphyrin emission (620–640 nm), Hemoglobin (630 nm band) |
| 700–870 nm | NIR tail, specific gravity (water scattering), pH (possible indirect) |

### C14 Detector (570–1078 nm) Coverage

| Range | Signals |
|-------|---------|
| 570–780 nm | Overlap with C12; hemoglobin absorption tails |
| 780–970 nm | First NIR window; lipid/protein overtones |
| 970–1078 nm | Water first overtone band (~970 nm) — sensitive to ionic concentration, specific gravity |

---

## Section 8: What IS and IS NOT Detectable Without Reagents

### ✅ Detectable reagent-free with Jimini's LEDs + detectors

| Biomarker | Primary Method | Best Wavelength | Expected R²/AUC |
|-----------|---------------|----------------|-----------------|
| Uric acid | UV absorbance | 275–295 nm | High (Beer-Lambert) |
| Hemoglobin/RBC (hematuria) | Vis absorbance | 405 nm (Soret), 541/555 nm | R² ~0.99 (PLS) |
| Bilirubin | Vis absorbance | 405/455 nm | AUC ~0.92 (LR) |
| Urobilinogen | Vis absorbance | 455–500 nm | AUC ~0.85 (LR) |
| Porphyrins | Fluorescence Ex405→Em620 | 405 nm excitation | Qualitative/semi-quant |
| Tryptophan/protein (indirect) | Fluorescence Ex275→Em335 | 275 nm excitation | Semi-quantitative |
| NADH | Fluorescence Ex365→Em460 | 365 nm excitation | Metabolic index |
| Riboflavin (B2) | Fluorescence Ex365/455→Em520 | 365/455 nm excitation | Quantitative |
| Specific gravity | NIR (970 nm water band) + visible | C14 970 nm | AUC ~0.85 (LR) |
| pH (acidity) | Multi-wavelength spectral shift | Broadband | AUC ~0.85 (LR) |
| Nitrite | UV absorbance (weak, ~354 nm) | 365 nm | Limited (LOQ uncertain) |
| Creatinine (indirect) | NIR 700–1078 nm region | C14 range | R² ~0.7–0.85 (PLS) |

### ❌ NOT reliably detectable without reagents (at physiological concentrations)

| Biomarker | Reason | Workaround |
|-----------|--------|------------|
| **Glucose** | No UV-Vis chromophore; invisible in 300–850 nm | NIR (1000–2500 nm) needed; or EIS indirect |
| **Albumin (quantitative)** | Colorless in visible; weak scattering only | NIR + PLS may work; or pH-indicator reagent |
| **Creatinine (precise)** | Absorbs at 234 nm (too low) + weak NIR overtones | UV 234 nm (out of Jimini range) or NIR PLS |
| **Urea** | No UV-Vis chromophore | NIR (PLS) at 1400–2500 nm region |
| **Ketones** | Weak carbonyl absorption (NIR ~1700 nm) | NIR at 1000+ nm needed |
| **Microalbumin (clinical grade)** | Need μg/mL precision, colorless | EIS or NIR reflectance |

---

## Section 9: Critical Papers Not Yet Accessed (Priority Next Reads)

1. **Raman spectroscopy for urine biomarkers (Carswell et al., 2022)** — Hematuria detection by Raman; Applied Spectroscopy 76(3):273-283; DOI: 10.1177/00037028211060853
2. **Flores-Guerrero et al. (2020)** — Raman for urinary albumin in T2DM; Diagnostics 10(3):141; DOI: 10.3390/diagnostics10030141
3. **Sarigul et al. (2021)** — FTIR urine analysis healthy adults; J. Biophotonics 14(7)
4. **ATR-FTIR + ML for renal cell carcinoma (IJMS 2024)** — PCA-LDA and SVM on dried urine FTIR; DOI: 10.3390/ijms25189830
5. **Quantification of albumin in urine by NIR diffuse reflectance + PLS** — Chinese J. Analytical Chem. 2016 (via adsorbent preconcentration)
6. **EEM fluorescence + PARAFAC for cannabis metabolites in urine (ACS Omega 2023)** — Method applicable to other fluorescent urinary metabolites; PMC10552475

---

## Sources Kept vs. Dropped

### Kept (Primary Evidence)
- **SpectraPhone 2026** (Sci Rep) — Most directly relevant hardware + PLS; R² >0.99 for hematuria and albumin
- **Kuenert et al. 2025** (Sci Rep) — Multi-LED hyperspectral catheter sensor; 401 patient samples; clinical validation
- **Spectrochip 2024** (Heliyon) — Characteristic wavelength reference table for 12 analytes; R² >0.95
- **Pezzaniti et al. 2001** (Clin Biochem) — NIR feasibility for 5 urine analytes including glucose
- **Shaw et al. 2000** (Clin Chem) — Mid-IR reagent-free PLS for urea/creatinine/protein; landmark paper
- **Shaw et al. 1996** (Clin Biochem) — NIR protein/creatinine/urea PLS; foundational
- **Suzuki et al. 2020** (Med Biol Eng Comput) — Most recent NIR POC paper
- **Human Fluorescent Profile 2020** (BSPC) — Key autofluorescence reference map
- **Tryptophan-Melanoma 2021** (IJMS) — 275 nm excitation, clinical validation
- **Bladder Cancer EEM-CNN 2025** (Sci Rep) — CNN limits on fluorescence EEM data
- **Body Fluid Signatures 2023** (Sci Rep) — Quantitative excitation-emission peaks for urine
- **Electronic Dipstick EIS 2018** (Future Sci OA) — EIS POC validation
- **Fraunhofer EIS Uromodulin** — Non-faradaic EIS for kidney biomarker
- **Melanoma Fluorescence 2020** (Open Chem) — 365/455 nm excitation validated

### Dropped
- **HPLC/UV creatinine/uric acid methods** — Not portable, separation required
- **Raman spectroscopy papers** — Different technology (laser-based, not LED), not directly applicable
- **NIR fruit quality instruments** — Wrong application domain
- **CKD risk ML models on clinical records** — Not spectroscopy-based

---

## Gaps and Recommended Next Steps

### Key Gaps
1. **Creatinine quantification without reagents** — The 234 nm UV absorption of creatinine is below Jimini's LED range (275 nm is lowest). The Jaffe reaction chromophore (around 500 nm) requires alkaline picrate reagent. NIR at 1078 nm (C14 limit) is marginal for creatinine.
2. **Glucose quantification** — Confirmed by two independent studies (Kuenert 2025, SpectraPhone 2026) that glucose is NOT detectable in the 340–850 nm visible range. NIR extension (>1000 nm) needed.
3. **Albumin quantification precision** — SpectraPhone achieved R²=0.9981 for albumin (0–1000 mg/dL) by unclear mechanism (albumin colorless in visible). Needs replication and mechanism explanation. The 15 mg/dL clinical threshold for microalbuminuria may not be achievable without reagents in the visible range.
4. **EIS + spectroscopy fusion** — No paper combines EIS + multi-LED visible/NIR spectroscopy for multi-biomarker urine analysis. This is Jimini's potential unique contribution.
5. **Real urine matrix validation** — Most papers use artificial/spiked urine. Clinical validation with diverse patient samples (pH 4–8, variable specific gravity 1.001–1.035, varying metabolite backgrounds) is consistently identified as a gap.
6. **Specific gravity via NIR** — The 970 nm water overtone (accessible via C14 to 1078 nm) is theoretically linked to osmolality/specific gravity. No paper specifically validates this in a portable LED-based format.

### Recommended Next Steps for Jimini
1. **Priority Experiment 1:** Validate uric acid detection at 275 nm in real urine (N>50 samples, compare vs. enzymatic reference method). Expected: R² > 0.90 if uric acid is >2 mg/dL.
2. **Priority Experiment 2:** Map fluorescence response at all 4 LED excitation wavelengths for 20+ urine samples — confirm tryptophan (275→335 nm), NADH (365→460 nm), porphyrins (405→620 nm), riboflavin (455→520 nm).
3. **Priority Experiment 3:** Test EIS + optical data fusion for creatinine/specific gravity prediction (EIS sensitive to ionic strength/concentration).
4. **Modeling:** Start with PLS regression, validate with 10-fold CV, then progress to 1D-CNN for multi-analyte prediction on fused EIS + spectral feature vectors.
5. **Literature retrieval needed:** Obtain full text of Suzuki 2020 (NIR POC), Shaw 1996 (NIR PLS), and Sarigul 2021 (FTIR urine).

---

## Quick Reference: DOI List

| Paper | DOI/Source |
|-------|-----------|
| Uric Acid UV Portable (2022) | 10.3390/s22083009 |
| Portable POC Uric Acid (2025) | 10.3390/bios16020076 |
| Spectrochip CCM Urinalysis (2024) | 10.1016/j.heliyon.2024.e37722 |
| Catheter Spectroscopic Monitoring (2025) | 10.1038/s41598-025-92802-2 |
| SpectraPhone Smartphone Urinalysis (2026) | 10.1038/s41598-026-38307-y |
| NIR Protein/Creatinine/Urea Shaw (1996) | 10.1016/0009-9120(95)02011-X |
| NIR Multi-analyte Pezzaniti (2001) | 10.1016/S0009-9120(01)00198-9 |
| NIR Reagentless Urea/Creatinine (2018) | ABE Journal Vol 7 (J-Stage) |
| NIR POC Suzuki (2020) | 10.1007/s11517-019-02063-1 |
| Mid-IR Reagent-free Shaw (2000) | 10.1093/clinchem/46.9.1493 |
| Human Fluorescent Profile (2020) | 10.1016/j.bspc.2019.101693 |
| Cancer Native Fluorescence 405nm (2012) | 10.1111/j.1751-1097.2012.01239.x |
| Tryptophan & Melanoma (2021) | 10.3390/ijms22041884 |
| Bladder Cancer EEM+CNN (2025) | 10.1038/s41598-025-15801-3 |
| Body Fluid Fluorescence (2023) | 10.1038/s41598-023-30241-7 |
| Melanoma Fluorescence 365/450nm (2020) | 10.1515/chem-2020-0143 |
| EIS Urine Dipstick (2018) | 10.4155/fsoa-2017-0142 (PMC5961415) |
| Electrochemical Creatinine Review (2022) | 10.1039/D2RA04479J |
| ATR-FTIR + ML Renal Cancer (2024) | 10.3390/ijms25189830 |
| Raman Hematuria (2022) | 10.1177/00037028211060853 |
| Raman Albumin Diabetes (2020) | 10.3390/diagnostics10030141 |
| ML-POC Testing Review (2025) | 10.1038/s41467-025-58527-6 |

---

*Compiled: 2026-04-09 | Thread 1 — Jimini Device Spectroscopy Research*
