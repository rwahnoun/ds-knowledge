---
title: Literature — LED Spectroscopy & EIS for Urine Biomarker Prediction
aliases:
  - literature
  - urine spectroscopy literature
  - Jimini lit review
  - paper index
tags:
  - topic/spectroscopy
  - topic/ml
  - topic/biomarker
  - type/literature
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: literature
author: Usense Healthcare
---

# Literature — LED Spectroscopy & EIS for Urine Biomarker Prediction

Consolidated paper reference for reagent-free urine biomarker prediction from LED-based spectroscopy and EIS.
Compiled by: Feynman multi-agent research pipeline (4 parallel threads, 60+ sources, 2026-04-09).
See also: [[optical-signatures]] [[biomarker-panel]] [[signal-processing]] [[ml-models]]

---

## Executive Summary

### What Works (High Confidence)

| Biomarker | Method | Jimini LED | Best reported performance |
|---|---|---|---|
| **Uric acid** | UV absorbance ~293 nm | 275 nm | Beer-Lambert, R² > 0.95 |
| **Hemoglobin / hematuria** | Vis absorbance (Soret 415 nm + Q-bands) | 405, 455, VIS | R² = 0.99 (PLS) |
| **Bilirubin** | Vis absorbance 344–450 nm | 405, 455 | AUC = 0.92 |
| **Urobilinogen** | Vis absorbance ~490 nm | 455, VIS | AUC ~0.85 |
| **Porphyrins** | Fluorescence Ex 405→Em 620 nm | 405→C12 | Qualitative/semi-quant |
| **Protein (indirect)** | Tryptophan fluorescence Ex 275→Em 335 nm | 275→C12 | Semi-quantitative |
| **NADH** | Fluorescence Ex 365→Em 460 nm | 365→C12 | Metabolic index |
| **Riboflavin** | Fluorescence Ex 365/455→Em 520 nm | 365/455→C12 | Quantitative |
| **Specific gravity / pH** | Multi-wavelength spectral pattern | Broadband | AUC ~0.85–0.89 |

### What Partially Works

| Biomarker | Method | Jimini channels | Confidence |
|---|---|---|---|
| **WBC (leukocytes)** | Scatter + NADH autofluorescence + EIS | A₁₀₇₀, ex365/em460, EIS | Low (binary pyuria Y/N) |
| **Bacteria** | Scatter + flavin fluorescence + EIS | A₁₀₇₀, ex455/em525, EIS | Low-Medium (>10⁵ CFU/mL) |
| **PBG** | Via conversion to porphyrins → Soret + fluorescence | A₄₀₅, A₄₀₅/A₄₈₀, ex405/em620 | Medium (binary, acute attacks) |
| **TUP (total porphyrins)** | Soret absorption + fluorescence | ex405/em620, 2nd deriv | Medium-High |
| **Osmolality** | EIS conductivity + NIR scatter | EIS σ, A₁₀₇₀, spectral integral | Medium |
| **Crystals** | Scatter (wavelength-independent at large size) | A₁₀₇₀, A₈₀₀/A₄₀₀→1.0 | Low (binary ≥+) |

### What Does NOT Work Reagent-Free (Visible Range)

| Biomarker | Why | Workaround |
|---|---|---|
| **Glucose** | No chromophore in UV-Vis at physiological levels | NIR >1400 nm or EIS |
| **Albumin (quantitative)** | Colorless in visible | Fluorescence (275→335) or EIS |
| **Creatinine (precise)** | Absorbs at 234 nm (below 275 nm LED range) | NIR PLS or EIS |
| **Urea** | No UV-Vis chromophore | NIR >1400 nm |
| **Electrolytes (Na⁺, K⁺, Cl⁻)** | No optical signature | EIS conductivity — total ionic, not individual ions |
| **Nitrites** | Spectrally transparent; Griess requires reagent | Indirect via bacterial detection model |
| **Epithelial cells** | No unique chromophore; scatter only | Not separable from WBC/bacteria by bulk spectroscopy |

> [!NOTE]
> No published paper combines LED multi-wavelength spectroscopy + EIS for multi-biomarker urine analysis. This is Jimini's potential unique contribution.

---

## UV-Vis Spectroscopy Papers

### Paper 1.1 — Label-Free Uric Acid Estimation (UV Spectrophotometry)

- **Year:** 2022 | **Journal:** *Sensors* (MDPI) | **DOI:** [10.3390/s22083009](https://doi.org/10.3390/s22083009)
- **Wavelengths:** UV range; λ_max ~290–295 nm
- **Biomarkers:** Uric acid (reagent-free, spot urine)
- **Model:** Univariate Beer-Lambert calibration curve
- **Key finding:** First demonstration that portable UV spectrophotometry measures uric acid in spot urine without reagents. Characteristic π→π* transition at ~290 nm survives complex urine matrix.
- **Relevance:** 275 nm LED directly excites uric acid. Main challenge: matrix interference from tyrosine (274 nm), tryptophan (280 nm), creatinine (234 nm) requires derivative or PLS deconvolution.

### Paper 1.2 — Portable POC Uric Acid Device (Uricia)

- **Year:** 2025 | **Journal:** *Biosensors* (MDPI), 16(2):76 | **DOI:** [10.3390/bios16020076](https://doi.org/10.3390/bios16020076)
- **Wavelengths:** 295 nm primary; full UV-Vis profiling of glucose, ascorbic acid, albumin, creatinine, uric acid
- **Model:** Calibration curve; SD < 0.01
- **Key finding:** 295 nm is the optimal single wavelength for uric acid. Provides spectral library of UV-Vis fingerprints of multiple urine analytes — directly applicable to Jimini LED selection.

### Paper 1.3 — Spectrochip CCM for 12 Urine Parameters

- **Year:** 2024 | **Journal:** *Heliyon*, 10(18):e37722 | **DOI:** [10.1016/j.heliyon.2024.e37722](https://doi.org/10.1016/j.heliyon.2024.e37722)
- **Device:** MEMS spectrochip (340–1000 nm, 5 nm resolution), white LED source
- **Biomarkers / characteristic wavelengths:** Leukocytes 550, Nitrite 530, Urobilinogen 570, Protein 620, pH 615, Occult Blood 620, Specific Gravity 615, Ketone 530, Bilirubin 540, Glucose 450, Microalbumin 520 & 615, Creatinine 550 nm
- **Model:** Calibration Curve Modelling (CCM); R² > 0.95 for all 12 parameters

> [!NOTE]
> Spectrochip uses test strips (reagent-dependent). Characteristic wavelength table is the key contribution for understanding which spectral regions encode which biomarkers.

### Paper 1.4 — Continuous Spectroscopic Catheter Monitoring

- **Year:** 2025 | **Journal:** *Scientific Reports*, 15:8617 | **DOI:** [10.1038/s41598-025-92802-2](https://doi.org/10.1038/s41598-025-92802-2)
- **Device:** Hamamatsu C12880MA mini-spectrometer (340–850 nm, 288 channels); 3-LED source; N=401 samples, 168 hospital patients
- **Model:** LRRE (Logistic Regression with Random Effects); SNV normalisation; 5-fold CV

| Parameter | AUC | Notes |
|---|---|---|
| Bilirubin | **0.921** | Key wavelengths: 344, 387, 427 nm |
| Erythrocytes | ~0.88 | |
| Specific Gravity, pH, Protein, Urobilinogen | Good | |
| Glucose, Albumin | No correlation | Confirmed not detectable in 340–850 nm range |

- **Key finding:** Directly analogous 3-LED approach to Jimini. Confirms glucose and albumin are NOT detectable by visible absorbance alone at physiological concentrations.

### Paper 1.5 — SpectraPhone: Smartphone Spectrometer Urinalysis

- **Year:** 2026 | **Journal:** *Scientific Reports*, 16:8517 | **DOI:** [10.1038/s41598-026-38307-y](https://doi.org/10.1038/s41598-026-38307-y)
- **Device:** Smartphone camera + diffraction grating (400–750 nm, 2051 channels, ~0.17 nm resolution)
- **Model:** PLS on 2nd-derivative spectra

| Biomarker | Key Wavelengths | R² | RMSE |
|---|---|---|---|
| Hematuria (RBC) | 419, 544, 555, 648 nm | **0.9913** | 61.6 RBC/µL |
| Albumin (reagent-free) | 586, 622, 705 nm | **0.9981** | 11.85 mg/dL |

- **Key finding:** 405 nm and 455 nm LEDs perfectly cover the hemoglobin Soret and Q-band regions. Albumin detection mechanism in visible not explained (albumin is colourless) — may be indirect via light scattering.
- **Data:** [github.com/Uncommon-Sense-Lab/SpectraPhone](https://github.com/Uncommon-Sense-Lab/SpectraPhone.git)

---

## NIR Spectroscopy Papers

### Paper 2.1 — NIR Protein, Creatinine, Urea (Shaw 1996)

- **Year:** 1996 | **Journal:** *Clinical Biochemistry*, 29(1):11–19 | **DOI:** [10.1016/0009-9120(95)02011-X](https://doi.org/10.1016/0009-9120(95)02011-X)
- **Biomarkers:** Protein, creatinine, urea | **Model:** NIR-PLS (reagent-free)
- **Key finding:** Seminal paper establishing NIR-PLS for reagent-free quantification of three major urine clinical chemistry markers.

### Paper 2.2 — NIR Multi-Analyte (Pezzaniti 2001)

- **Year:** 2001 | **Journal:** *Clinical Biochemistry*, 34(3):239–246 | **DOI:** [10.1016/S0009-9120(01)00198-9](https://doi.org/10.1016/S0009-9120(01)00198-9)
- **Biomarkers:** Urea, creatinine, glucose, protein, ketone | **Model:** NIR-PLS
- **Key finding:** All 5 analytes quantifiable from the same spectral dataset. Glucose is detectable in NIR (not visible range) — rationale for extending Jimini into NIR.

### Paper 2.3 — Reagentless NIR Urea/Creatinine Ratio (2018)

- **Journal:** *Advanced Biomedical Engineering*, Vol. 7 | **Source:** J-Stage
- **Biomarkers:** Urea, creatinine (ratio = urea-to-creatinine, hydration/renal index)
- **Key finding:** Urea:creatinine ratio predicted reagent-free from NIR spectra of spot urine. Confirms C14 range (570–1078 nm) provides useful urea/creatinine information.

### Paper 2.4 — Suzuki NIR POC Spot Urine (2020)

- **Year:** 2020 | **Journal:** *Medical & Biological Engineering & Computing*, 58(1):67–74 | **DOI:** [10.1007/s11517-019-02063-1](https://doi.org/10.1007/s11517-019-02063-1)
- **Key finding:** Direct measurement of spot urine (no dilution, no reagents) in NIR is feasible — most directly relevant NIR-POC paper.

### Paper 2.5 — Mid-IR Reagent-free Urea/Creatinine/Protein (Shaw 2000)

- **Year:** 2000 | **Journal:** *Clinical Chemistry*, 46(9):1493–1495 | **DOI:** [10.1093/clinchem/46.9.1493](https://doi.org/10.1093/clinchem/46.9.1493)
- **Note for Jimini:** Mid-IR (2.5–25 µm) is outside Jimini's detector range. Dried film methodology may be applicable if sample prep is acceptable.

---

## Fluorescence Papers

### Paper 3.1 — Human Fluorescent Profile of Urine

- **Year:** 2020 | **Journal:** *Biomedical Signal Processing and Control*, 56:101693 | **DOI:** [10.1016/j.bspc.2019.101693](https://doi.org/10.1016/j.bspc.2019.101693)

| Fluorophore | Excitation (nm) | Emission (nm) | Jimini LED |
|---|---|---|---|
| Tryptophan | 275–295 | 330–360 | 275 nm |
| NADH/NAD(P)H | 340–365 | 440–470 | 365 nm |
| Riboflavin (B2) | 365–450 | 520–560 | 365/455 nm |
| Porphyrins | 405–420 | 620–640 | 405 nm |
| Hippuric acid | ~320 | ~420 | 365 nm |
| Indoxyl sulfate | ~280 | ~330 | 275 nm |

### Paper 3.2 — Cancer Detection by Native Fluorescence (405 nm)

- **Year:** 2012 | **Journal:** *Photochemistry and Photobiology* | **DOI:** [10.1111/j.1751-1097.2012.01239.x](https://doi.org/10.1111/j.1751-1097.2012.01239.x)
- **Key finding:** 405 nm excitation distinguishes cancer patients from normal subjects using porphyrin-region emissions (620–640 nm). 405 nm LED is perfectly positioned for this.

### Paper 3.3 — Tryptophan Fluorescence & Melanoma

- **Year:** 2021 | **Journal:** *International Journal of Molecular Sciences*, 22(4):1884 | **DOI:** [10.3390/ijms22041884](https://doi.org/10.3390/ijms22041884)
- **Wavelengths:** Ex 295 nm (selective for Trp over Tyr) → Em 330–350 nm
- **Key finding:** Significantly higher tryptophan fluorescence in melanoma patients; decreases with advancing stage (tryptophan catabolism via kynurenine pathway). 275 nm LED close enough.

### Paper 3.4 — Bladder Cancer EEM + CNN

- **Year:** 2025 | **Journal:** *Scientific Reports* | **DOI:** [10.1038/s41598-025-15801-3](https://doi.org/10.1038/s41598-025-15801-3)
- **Models:** LR, OPLS-DA, CNN. CNN achieved **72.1%** accuracy for bladder cancer classification on EEMs alone.
- **Key finding:** Fluorescence EEMs alone insufficient without chemical separation. Multi-modal fusion needed.

### Paper 3.5 — Body Fluid Fluorescence Signatures

- **Year:** 2023 | **Journal:** *Scientific Reports* | **DOI:** [10.1038/s41598-023-30241-7](https://doi.org/10.1038/s41598-023-30241-7)
- **Key finding:** Validates 275→330–350 nm (tryptophan) and 365→400–500 nm (flavins, NADH) as dominant urine fluorescence channels.

### Paper 3.6 — Melanoma Fluorescence Biomarkers (360/450 nm)

- **Year:** 2020 | **Journal:** *Open Chemistry* | **DOI:** [10.1515/chem-2020-0143](https://doi.org/10.1515/chem-2020-0143)
- **Key finding:** Excitation peaks at 360–370 nm and 450 nm; emission 410–460 nm. 365 nm and 455 nm LEDs cover both excitation peaks exactly.

---

## LED-Based / Portable Spectroscopy Papers

### Paper 4.1 — LUMINA: Light-Based Urine Monitoring and Analysis

- **Source:** NOVA Research Portal — UNINOVA/CTS/iNOVA4Health
- **Key finding:** Dedicated LED optoelectronic system for urine spectral analysis — most directly analogous existing device to Jimini's form factor.

### Paper 4.2 — Portable LED Nitrite Detector in Simulated Urine

- **Year:** 2020 | **Source:** IEEE Xplore 8980097
- **Key finding:** Low-cost LED spectrophotometer sufficient for nitrite detection. Native nitrite absorbs weakly at ~354 nm; reagent-free sensitivity limited.

---

## EIS Papers

### Paper 6.1 — Fully Electronic Urine Dipstick with EIS

- **Year:** 2018 | **Journal:** *Future Science OA*, 4(5):FSO301 | **PMC:** PMC5961415 | **DOI:** [10.4155/fsoa-2017-0142](https://doi.org/10.4155/fsoa-2017-0142)
- **Biomarkers:** Leukocyte esterase, protein | **LOD:** 1 pg/mL
- **Key finding:** Molybdenum electrodes on nanoporous polyamide; portable non-Faradaic EIS for inflammatory markers in urine.

### Paper 6.2 — Label-Free EIS for Uromodulin (Fraunhofer)

- **Source:** Fraunhofer Publications
- **Biomarker:** Uromodulin (kidney tubular damage) | **Range:** 0.5–8 ng/mL; 15%/ng·mL⁻¹ relative impedance change
- **Approach:** 50-nm Ta₂O₅ passivation layer on interdigitated electrodes

### Paper 6.3 — Electrochemical Creatinine Detection Review

- **Year:** 2022 | **Journal:** *RSC Advances* | **DOI:** [10.1039/D2RA04479J](https://doi.org/10.1039/D2RA04479J)
- **Key finding:** Non-enzymatic approaches (ZIF-8 nanoparticles, aptamers) achieve LOD ~30 µM in urine. EIS provides impedimetric creatinine sensing.

---

## Downloaded Papers (papers/ directory)

| File | Paper | Year | Key Topic |
|---|---|---|---|
| `spectraphone-urinalysis-2026.pdf` | SpectraPhone smartphone urinalysis | 2026 | PLS R²=0.99 hematuria, albumin |
| `kuenert-catheter-spectroscopy-2025.pdf` | Continuous catheter spectroscopic monitoring | 2025 | LED urine, SNV, LRRE, n=401 |
| `bladder-cancer-eem-cnn-2025.pdf` | Bladder cancer EEM + CNN | 2025 | Fluorescence EEM, CNN 72% |
| `body-fluid-fluorescence-2023.pdf` | Body fluid fluorescence signatures | 2023 | Precise Ex/Em peak maps for urine |
| `v-pfcrc-creatinine-normalization-2025.pdf` | V-PFCRC dilution correction | 2025 | Best-in-class creatinine normalisation |
| `1d-cnn-vs-chemometrics-2023.pdf` | 1D-CNN vs ML for spectral classification | 2023 | CNN outperforms PLS when n>500 |
| `electrochemical-creatinine-review-2022.pdf` | Electrochemical creatinine detection | 2022 | EIS creatinine sensing methods |
| `deep-spectral-cnn-libs-2020.pdf` | Deep Spectral CNN for LIBS | 2020 | 1D-CNN architecture for spectra |
| `1d-cnn-review-portable-raman-2020.pdf` | 1D-CNN review for portable Raman | 2020 | CNN architectures for spectral data |
| `dnn-mie-scatter-correction-2020.pdf` | DNN for Mie scatter correction in FTIR | 2020 | Neural net scatter correction |
| `data-augmentation-spectral-cnn-2017.pdf` | Data augmentation for spectral CNN | 2017 | Bjerrum augmentation strategies |
| `coral-original-2016.pdf` | CORAL domain adaptation | 2016 | Covariance alignment |
| `deep-coral-2016.pdf` | Deep CORAL | 2016 | Deep domain adaptation |
| `domain-adaptation-enose-drift-2015.pdf` | Domain adaptation for e-nose drift | 2015 | Sensor drift compensation |
| `benchmarking-dl-raman-2026.pdf` | Benchmarking DL for Raman | 2026 | Comprehensive DL vs chemometrics |

## Key Papers Not Yet Obtained

| Paper | DOI | Where |
|---|---|---|
| Tryptophan & Melanoma (2021) | 10.3390/ijms22041884 | MDPI |
| Uric Acid UV Portable (2022) | 10.3390/s22083009 | MDPI Sensors |
| Spectrochip CCM (2024) | 10.1016/j.heliyon.2024.e37722 | Heliyon |
| MVG Cross-Device Augmentation (2025) | PMC12096352 | PMC |
| Shaw NIR Urine (1996) | 10.1016/0009-9120(95)02011-X | Clinical Biochemistry |
| Human Fluorescent Profile (2020) | 10.1016/j.bspc.2019.101693 | Biomedical Signal Processing |
| EEM-PARAFAC cannabis metabolites (2023) | PMC10552475 | ACS Omega |
| Raman hematuria — Carswell (2022) | 10.1177/00037028211060853 | Applied Spectroscopy |

---

## Sources

| Reference | Notes |
|---|---|
| Fossati et al. *Clin Chem* 1980;26(2):227–231 | UV uric acid absorbance |
| Peters T. *Adv Clin Chem* 1970;13:37–111 | Protein UV absorption |
| Lim CK. *Methods Enzymol* 1986;123:383–405 | Porphyrin optical properties |
| Al-Awthan et al. *Spectrochim Acta A* 2020;229:117995 | NIR urea/creatinine PLS |
| Topham et al. *Clin Chem* 1978;24(9):1580–1583 | RBC turbidity |
| Watson & Schwartz. *Proc Soc Exp Biol Med* 1941;47(3):393–398 | PBG original test |
| Mateen et al. *J Biomed Optics* 2018;23(5):055006 | PBG heat conversion |
| Buttery et al. *Clin Chem* 1995;41(1):103 | TUP 2nd-derivative spectroscopy |
| Free AH et al. *Am J Clin Pathol* 1957;27(5):493–500 | WBC leukocyte assay |
| Carmine TC. *Sci Rep* 2025. PMC11782553 | V-PFCRC dilution correction |
| Leopold-Kerschbaumer et al. *Anal Chem* 2025. PMC12096352 | MVG cross-device augmentation |
| Ganin et al. *JMLR* 2016 | Domain-adversarial training |
| Xu & Liang. *J Chemometrics* 2004 | Monte Carlo Cross-Validation |
| Lemos et al. *arXiv* 2023. 2301.10746 | 1D-CNN vs chemometrics |
| Erzina et al. *Analyst* 2023. DOI: 10.1039/d3an00669g | WGAN spectral augmentation |

## Gaps

- Creatinine at 234 nm (below Jimini's 275 nm range): no reagent-free optical option in Jimini's LED set — NIR C14 range or EIS is the only path
- Glucose in visible range (confirmed not detectable by Kuenert 2025 and SpectraPhone 2026): NIR >1000 nm or EIS-GOx required
- Albumin detection mechanism in SpectraPhone R²=0.9981: albumin is colourless in visible — mechanistic explanation missing from that paper
- Specific gravity via NIR 970 nm (C14): theoretically linked to osmolality but not yet validated in a portable LED-based format
- EIS + optical fusion for multi-biomarker urinalysis: no published precedent as of 2026-04-19
- Priority literature to obtain: Suzuki 2020 (NIR POC full text), Shaw 1996 (NIR PLS full text), EEM-PARAFAC cannabis metabolites (ACS Omega 2023, PMC10552475)