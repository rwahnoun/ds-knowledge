---
title: Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices
aliases:
  - spectroscopy biomarkers
  - urine biomarkers
  - Jimini biomarker targets
tags:
  - topic/spectroscopy
  - topic/biomarker
  - topic/ml
  - type/literature
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: literature
author: Usense Healthcare
---

# Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices

Literature synthesis of reagentless urine biomarker prediction by UV-Vis, NIR, and fluorescence spectroscopy using portable LED-based devices. Device context: Jimini with LEDs at 275/365/405/455 nm + broadband visible, photodetectors C12 (321–870 nm) and C14 (570–1078 nm), and EIS (electrochemical impedance). See [[signal-processing]] for preprocessing pipelines, [[physics-grounded-ml]] for architecture recommendations, [[matrix-correction]] for urine matrix effects, and [[multi-task-modeling]] for joint prediction strategies.

---

## Summary

Reagentless urine spectroscopy is feasible for a number of biomarkers across UV-Vis, NIR, and fluorescence domains. The most robustly accessible targets for Jimini's wavelength range are: **uric acid** (UV 290 nm absorption), **bilirubin** (~344–455 nm), **erythrocytes/hemoglobin** (Soret 415–420 nm, 541–555 nm, 630 nm), **urobilinogen** (~450–500 nm), and **protein/tryptophan autofluorescence** (Ex 275–295 nm → Em 330–350 nm). PLS regression dominates quantitative work; CNN/deep learning is emerging for classification. EIS adds complementary sensitivity for ionic/protein concentrations and UTI markers.

---

## Section 1: UV-Vis Spectroscopy for Urine Biomarkers

### Paper 1.1 — Label-Free Uric Acid Estimation (UV Spectrophotometry, 2022)

- **DOI:** 10.3390/s22083009
- **Wavelengths:** UV range; uric acid primary absorption at **~290–295 nm** (purine chromophore)
- **Model:** Beer-Lambert univariate calibration curve
- **Key finding:** First demonstration that portable UV spectrophotometry can measure uric acid in spot urine without reagents. Matrix interference from tyrosine and creatinine is the main challenge.
- **Jimini relevance:** The 275 nm LED directly excites uric acid. Single-wavelength or ratio-based approach at 275 nm can quantify uric acid.

### Paper 1.2 — Portable POC Uric Acid Device (Uricia, 2025)

- **DOI:** 10.3390/bios16020076
- **Wavelengths:** 295 nm primary; full UV-Vis profiling of glucose, ascorbic acid, albumin, creatinine, uric acid
- **Key finding:** 295 nm is optimal for uric acid detection. Spectral fingerprints of multiple analytes in the UV are characterized — directly applicable to Jimini's LED placement.

### Paper 1.3 — Spectrochip CCM for 12 Urine Parameters (2024)

- **DOI:** 10.1016/j.heliyon.2024.e37722 (PMC11425109)
- **Device:** MEMS spectrochip 340–1000 nm, 5 nm resolution; white LED
- **Model:** Calibration Curve Modeling; R² > 0.95 for all 12 parameters

**Characteristic wavelengths per biomarker:**

| Biomarker | Characteristic λ (nm) |
|-----------|----------------------|
| Leukocytes | 550 |
| Nitrite | 530 |
| Urobilinogen | 570 |
| Protein | 620 |
| pH | 615 |
| Occult Blood | 620 |
| Specific Gravity | 615 |
| Bilirubin | 540 |
| Glucose | 450 |
| Creatinine | 550 |

> [!NOTE]
> This study uses test strips — not fully reagent-free. The wavelength table is valid for understanding spectral regions but performance numbers reflect strip chemistry.

### Paper 1.4 — Continuous Spectroscopic Catheter Monitoring (Kuenert, 2025)

- **DOI:** 10.1038/s41598-025-92802-2
- **Device:** Hamamatsu C12880MA (340–850 nm); 3-LED hyperspectral (UV + NIR + FS LEDs); 3 optical paths
- **N:** 401 samples, 168 hospital patients; 5-fold CV

| Parameter | Model | AUC | BAC |
|-----------|-------|-----|-----|
| Bilirubin | LRRE | **0.921** | 0.711 |
| Erythrocytes | LRRE | ~0.88 | ~0.78 |
| pH (acidic/basic) | LRRE | good | good |
| Protein, SG, Urobilinogen | LRRE | good | good |
| Nitrite | LRRE | poor | poor |
| Glucose, Albumin | — | **no correlation** | — |

- **Key finding:** Glucose and albumin at physiological concentrations are **NOT detectable** by visible absorbance alone without reagents. Key bilirubin wavelengths: 344, 387, 427 nm.
- **Jimini relevance:** Most directly relevant study. Multi-LED catheter approach mirrors Jimini design.

### Paper 1.5 — SpectraPhone Smartphone Spectrometer (2026)

- **DOI:** 10.1038/s41598-026-38307-y
- **Wavelengths:** 400–750 nm (~0.17 nm resolution, 2051 channels)

| Biomarker | Key Wavelengths | R² | RMSE |
|-----------|----------------|-----|------|
| Hematuria (RBC) | 419, 544, 555, 648 nm | **0.9913** | 61.6 RBC/µL |
| Albumin (reagent-free) | 586, 622, 705 nm | **0.9981** | 11.85 mg/dL |
| Albumin + BPB reagent | 556, 590 nm | **0.9997** | 4.26 mg/dL |

- **Key finding:** PLS on derivative/SNV-preprocessed spectra achieves near-perfect R² for hematuria and albuminuria. Hemoglobin key wavelengths align with Soret (419 nm) and Q-bands (541/555/630 nm). Model robust to downsampling to 20% of spectral resolution.

---

## Section 2: NIR Spectroscopy for Urine Analysis

| Study | Year | Analytes | Model | Key Finding |
|-------|------|---------|-------|-------------|
| Shaw et al. (*Clin. Biochem.*) | 1996 | Protein, creatinine, urea | PLS (NIR) | Foundational paper; NIR-PLS for 3 clinical markers without reagents |
| Pezzaniti et al. (*Clin. Biochem.*) | 2001 | Urea, creatinine, glucose, protein, ketone | PLS | Multi-analyte NIR feasibility; glucose detectable in NIR (invisible in visible) |
| Suzuki et al. (*Med. Biol. Eng. Comput.*) | 2020 | Multiple urine components | PLS (POC) | Direct spot urine measurement (no dilution/drying) feasible |
| Shaw et al. (*Clin. Chem.*) | 2000 | Urea, creatinine, total protein | PLS (Mid-IR, dried films) | Dried films eliminate water interference; highly accurate |

> [!IMPORTANT]
> NIR at 700–1078 nm (Jimini C14 range) is dominated by water overtones at ~970 nm. Creatinine and urea NIR bands require PLS on many wavelengths simultaneously. Main NIR creatinine bands (1500–2200 nm) fall outside C14 range.

---

## Section 3: Fluorescence-Based Urine Analysis

### Key Fluorophore Map

| Fluorophore | Excitation (nm) | Emission (nm) | Jimini LED | Relevance |
|-------------|----------------|---------------|-----------|-----------|
| Tryptophan | 275–295 | 330–360 | **275 nm** | Protein marker, metabolic disease |
| NADH/NAD(P)H | 340–365 | 440–470 | **365 nm** | Metabolic status, cellular energy |
| Riboflavin (B2) | 365–450 | 520–560 | **365/455 nm** | Nutritional status |
| Porphyrins | 405–420 | 620–640 | **405 nm** | Porphyria, heme metabolism |
| Indoxyl sulfate | ~280 | ~330 | 275 nm (proxy) | CKD uremic toxin |
| NADH/flavin | 360–370, 450 | 410–460 | **365/455 nm** | Melanoma-related metabolites |

### Notable Fluorescence Papers

**Bladder Cancer EEM + CNN (2025):** CNN on fluorescence EEMs achieved 72.1% accuracy for cancer classification — shows limits of fluorescence alone (multi-modal data fusion needed). DOI: 10.1038/s41598-025-15801-3

**Tryptophan & Melanoma (2021):** Autofluorescence at 295 nm significantly higher in melanoma patients; 275 nm LED excites tryptophan with emission at ~330–350 nm (within C12 range). DOI: 10.3390/ijms22041884

**Body Fluid Fluorescence Signatures (2023):** Precise excitation-emission peak maps for urine, validating 275 nm → 330–350 nm (tryptophan) and 365 nm → 400–500 nm (flavins, NADH) as dominant urine fluorescence channels. DOI: 10.1038/s41598-023-30241-7

---

## Section 4: LED-Based and Portable Spectrometer Papers

**LUMINA setup (Fantoni et al., UNINOVA):** Dedicated optoelectronic system for on-site urine spectral analysis — prototype most directly analogous to Jimini's form factor.

**Portable LED Nitrite Detector (IEEE 2020):** Native nitrite absorbs weakly at ~354 nm in UV; reagent-free sensitivity may be limited. Without Griess reaction reagent, Jimini's 365 nm LED provides marginal detection. DOI: IEEE Xplore 8980097

---

## Section 5: Machine Learning & Chemometric Models

### PLS Regression — Gold Standard for Quantification

**Best published results:**

| Study | Biomarker | Model | R² | RMSE |
|-------|-----------|-------|-----|------|
| SpectraPhone 2026 | Hematuria (RBC) | PLS on 2nd-derivative | 0.9913 | 61.6 RBC/µL |
| SpectraPhone 2026 | Albumin (reagent-free) | PLS on SNV | 0.9981 | 11.85 mg/dL |
| SpectraPhone 2026 | Albumin + BPB | PLS on SNV | 0.9997 | 4.26 mg/dL |
| Shaw et al. 1996 | Protein, creatinine, urea | PLS (NIR) | High | Clinical range |

**Key preprocessing:** SNV normalization, 2nd derivative, mean centering, 10-fold CV, ~30 PCs typical.

### Logistic Regression with Random Effects (LRRE) — Best for Binary Classification

Best for repeated patient measurements. AUC 0.88–0.921 for bilirubin, erythrocytes, pH in Kuenert 2025. Random intercept handles within-patient correlation.

### CNN for Spectral Classification

- 1D-CNN outperforms MLP for spectral data
- Preprocessing (SNV, derivative) still required before CNN
- n > 200 needed for reliable training; augmentation essential for n < 200

See [[signal-processing]] for full architecture details and [[multi-task-modeling]] for multi-output CNN.

### PARAFAC for EEM Fluorescence Data

Decomposes three-way data (samples × excitation × emission) into independent fluorophore components. Jimini's 4 LEDs × C12 broadband creates a partial EEM — PARAFAC can separate contributions of tryptophan, NADH, riboflavin, and porphyrins simultaneously.

### Recommended ML Pipeline for Jimini

```
Raw spectra (4 LED × C12/C14 channels)
    ↓
Preprocessing: SNV normalization + 2nd derivative
    ↓
For quantitative regression: PLS-R (10–30 latent variables)
    ↓ (if N > 500 samples)
Upgrade to: 1D-CNN or XGBoost on PCA-reduced features
    ↓
Validation: 10-fold CV, report R², RMSE, MAE
    ↓
For binary classification: LRRE (small N) or RF/XGBoost (large N)
```

---

## Section 6: Electrochemical Impedance Spectroscopy (EIS) for Urine

| Study | Approach | Biomarker | Key Finding |
|-------|----------|-----------|-------------|
| Future Sci OA 2018 (PMC5961415) | Molybdenum electrodes; non-Faradaic EIS | Leukocyte esterase, protein | LOD = 1 pg/mL |
| Fraunhofer (label-free EIS) | 50 nm Ta₂O₅ IDE | Uromodulin | 15%/ng/mL impedance change; 0.5–8 ng/mL |
| RSC Advances 2022 | Non-enzymatic electrochemical | Creatinine | LOD ~30 µM; review of approaches |

**EIS combined with optical spectroscopy** (no published paper yet) is Jimini's potential unique contribution. See [[multi-task-modeling]] for fusion architectures.

---

## Section 7: Jimini LED Wavelengths Mapped to Urine Biomarkers

| LED (nm) | Absorption/Excitation Targets | Detectable Biomarkers |
|----------|------------------------------|----------------------|
| **275 nm** | Uric acid (~290–295 nm), Tryptophan (Ex 280 nm), Tyrosine (Ex 270 nm), DNA/RNA bases (260–280 nm) | Uric acid (Beer-Lambert), Protein/Tryptophan fluorescence (Em 330–350 nm), Indoxyl sulfate |
| **365 nm** | NADH (Ex 340–365 nm → Em 440–470 nm), Riboflavin (Ex 365 nm → Em 520 nm) | NADH metabolic index, Riboflavin (B2 status) |
| **405 nm** | Porphyrins (Soret ~405–415 nm → Em 620–640 nm), Bilirubin (weak, ~415–450 nm) | Porphyrins (porphyria, heme disease), Bilirubin (indirect) |
| **455 nm** | Bilirubin (absorption ~430–460 nm), FAD/flavins (Ex 450 nm → Em 525 nm) | Bilirubin (direct), FAD/flavin metabolites |
| **Broadband Visible** | Hemoglobin (Soret 415 nm, Q-bands 541, 555, 576, 630 nm), Urobilinogen (~440–500 nm) | Hematuria, Hemoglobinuria, Urobilinogen, Bilirubin |

---

## Section 8: What Is and Is Not Detectable Without Reagents

### Detectable Reagent-Free with Jimini

| Biomarker | Primary Method | Best Wavelength | Expected R²/AUC |
|-----------|---------------|----------------|-----------------|
| Uric acid | UV absorbance | 275–295 nm | High (Beer-Lambert) |
| Hemoglobin/RBC | Vis absorbance | 405 nm (Soret), 541/555 nm | R² ~0.99 (PLS) |
| Bilirubin | Vis absorbance | 405/455 nm | AUC ~0.92 (LR) |
| Urobilinogen | Vis absorbance | 455–500 nm | AUC ~0.85 (LR) |
| Porphyrins | Fluorescence Ex405→Em620 | 405 nm excitation | Medium–High (if elevated) |
| Tryptophan/protein | Fluorescence Ex275→Em335 | 275 nm excitation | Semi-quantitative |
| NADH | Fluorescence Ex365→Em460 | 365 nm excitation | Metabolic index |
| Specific gravity | NIR (970 nm water band) + visible | C14 970 nm | AUC ~0.85 (LR) |
| pH (acidity) | Multi-wavelength spectral shift | Broadband | AUC ~0.85 (LR) |
| Creatinine (indirect) | NIR 700–1078 nm region | C14 range | R² ~0.7–0.85 (PLS) |

### Not Reliably Detectable Without Reagents

| Biomarker | Reason | Workaround |
|-----------|--------|------------|
| **Glucose** | No UV-Vis chromophore; invisible in 300–850 nm | NIR (1000–2500 nm) needed; or EIS indirect |
| **Albumin (quantitative)** | Colorless in visible; weak scattering only | NIR + PLS; or pH-indicator reagent |
| **Creatinine (precise)** | Absorbs at 234 nm (too low) + weak NIR overtones | NIR PLS at 1400–2500 nm (out of range) |
| **Urea** | No UV-Vis chromophore | NIR at 1400–2500 nm |
| **Ketones** | Weak carbonyl absorption (~1700 nm) | NIR at 1000+ nm |
| **Nitrites** | Transparent at Jimini λ; Griess → 540 nm | Indirect proxy from BAC model |
| **Sodium/Chloride** | No UV-Vis absorption | EIS conductivity |

---

## Sources

| Source | Key Contribution | DOI/URL |
|--------|-----------------|---------|
| Kuenert et al. 2025 | Multi-LED hyperspectral catheter; 401 patient samples | 10.1038/s41598-025-92802-2 |
| SpectraPhone 2026 | R² > 0.99 for hematuria and albumin; PLS + SNV | 10.1038/s41598-026-38307-y |
| Spectrochip 2024 | Characteristic wavelength table for 12 analytes | 10.1016/j.heliyon.2024.e37722 |
| Uric Acid UV 2022 | First portable UV reagentless uric acid | 10.3390/s22083009 |
| Portable POC Uric Acid 2025 | 295 nm optimal; multi-analyte UV characterization | 10.3390/bios16020076 |
| Human Fluorescent Profile 2020 | Autofluorescence reference map for urine | 10.1016/j.bspc.2019.101693 |
| Tryptophan & Melanoma 2021 | 275 nm excitation validated clinically | 10.3390/ijms22041884 |
| Body Fluid Signatures 2023 | Quantitative Ex/Em peaks for urine fluorophores | 10.1038/s41598-023-30241-7 |
| Bladder Cancer EEM+CNN 2025 | CNN limits on EEM alone; 72% accuracy | 10.1038/s41598-025-15801-3 |
| Shaw et al. 1996 | NIR protein/creatinine/urea PLS; foundational | 10.1016/0009-9120(95)02011-X |
| Electronic Dipstick EIS 2018 | EIS POC; LOD 1 pg/mL | 10.4155/fsoa-2017-0142 |
| Electrochemical Creatinine Review 2022 | EIS creatinine approaches | 10.1039/D2RA04479J |

---

## Gaps

1. **Creatinine without reagents**: 234 nm UV absorption is below Jimini's 275 nm range. NIR at 1078 nm (C14 limit) is marginal. EIS conductivity is the most promising route.
2. **Glucose quantification**: Confirmed absent in 340–850 nm by two independent studies (Kuenert 2025, SpectraPhone 2026). NIR extension beyond 1000 nm needed.
3. **Albumin quantification mechanism**: SpectraPhone achieved R²=0.9981 for albumin in visible range but albumin is colorless — mechanism unexplained. May be indirect via light scattering from protein aggregates.
4. **EIS + spectroscopy fusion**: No published paper jointly trains UV-Vis + multi-frequency EIS for multi-biomarker urine analysis. This is Jimini's potential unique contribution.
5. **Specific gravity via NIR**: The 970 nm water overtone accessible via C14 is theoretically linked to osmolality/SG but has not been validated in a portable LED format.
6. **Real urine matrix validation**: Most papers use artificial/spiked urine. Clinical validation with diverse patient samples (pH 4–8, SG 1.001–1.035) is consistently identified as a gap.
