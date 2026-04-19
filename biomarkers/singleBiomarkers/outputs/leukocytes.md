---
title: Leukocytes (Leukocyte Esterase)
aliases:
  - Leukocytes
  - Leukocyte esterase
  - LE
  - WBC esterase
  - Pyuria marker
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# Leukocytes (Leukocyte Esterase)

Leukocytes is the medical synonym for **White Blood Cells (WBCs)**. This sheet focuses on the **leukocyte esterase (LE) enzyme** as the specific dipstick-detectable biomarker, while cellular aspects are covered in the White Blood Cells sheet. LE is an enzyme released from neutrophil granules during degranulation or cell lysis; it persists in urine even after WBC disintegration, making it more sensitive than microscopy in aged specimens. See [[datascience/spectroscopy-biomarkers]] for clinical urinalysis context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Leukocyte Esterase (LE) |
| **Other names** | WBC esterase, granulocyte esterase |
| **Nature** | Serine protease/esterase enzyme from neutrophil azurophilic granules |
| **Molecular weight** | ~25–30 kDa (human neutrophil elastase, a related esterase) |
| **EC number** | EC 3.1.1.- (esterases, broad class) |
| **Key cell source** | Neutrophils (polymorphonuclear leukocytes) |
| **Significance** | Indirect marker of pyuria — detected even after WBC lysis |

**Representation:**

```
  Neutrophil granule contents:
  - Leukocyte esterase (LE)
  - Myeloperoxidase (MPO)
  - Elastase
  - Lysozyme
  - Defensins
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW | Key Difference |
|---|---|---|---|
| **Myeloperoxidase (MPO)** | Protein | ~150 kDa | Another neutrophil enzyme; green colour; not detected by LE dipstick |
| **Neutrophil elastase** | Protein | ~29 kDa | Related serine protease; contributes to LE signal |
| **Bacterial esterases** | Various | Various | May cause minor false positives; different substrate specificity |

---

## Medical Information

### Origin

#### Endogenous

Leukocyte esterase is produced by **neutrophils** during granulopoiesis in the bone marrow. It is stored in **azurophilic (primary) granules** and released during:
- Degranulation at infection sites
- Cell death/lysis (necrosis or apoptosis in urine)
- NETosis (neutrophil extracellular trap formation)

LE in urine originates from neutrophils that have migrated into the urinary tract in response to infection, inflammation, or tissue injury.

#### Exogenous

No exogenous source. LE is exclusively an endogenous neutrophil product.

### Primary & Secondary Biological Roles

**Primary role:**
- **Antimicrobial defence:** Esterases and proteases degrade bacterial proteins and aid in phagocytic killing.
- **Diagnostic pyuria marker:** In urine, LE activity serves as an indirect indicator of WBC presence.

**Secondary roles:**
- **Tissue remodelling:** Neutrophil proteases contribute to extracellular matrix degradation during inflammation.
- **Inflammation amplification:** Enzyme release triggers further immune cell recruitment.

### Catabolism and Elimination Pathway

- LE is released into urine as WBCs degranulate or lyse.
- The enzyme remains active in urine for several hours, even after the parent cell has disintegrated.
- Eventually inactivated by urinary protease inhibitors and dilution.
- Eliminated by voiding.

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Urine LE (dipstick)** | Negative |
| **Urine WBC count** | <5 WBC/HPF; <25 WBC/µL |
| **Blood neutrophil count** | 2,000–7,500/µL |

#### Factors Influencing Levels

**Positive LE (increased):**
- UTI (cystitis, pyelonephritis)
- Interstitial nephritis
- Glomerulonephritis
- Urolithiasis
- Bladder cancer
- Vaginal contamination (common false positive)
- Trichomonas vaginalis infection
- Prostatitis

**Negative LE:**
- Healthy state
- Neutropenia (immunosuppression may reduce pyuria)
- Very early infection (WBCs not yet recruited)
- High glucose or albumin (assay inhibition)

#### Associated Pathologies

| Condition | LE Result | Key Symptoms |
|---|---|---|
| **UTI** | Positive (75–90% sensitivity) | Dysuria, frequency |
| **Sterile pyuria** | Positive but culture-negative | TB, interstitial nephritis, STI |
| **Contamination** | False positive | Asymptomatic, high squamous cells |

### Presence in Urine

**Should it be normally present?** **No** — negative LE indicates absence of significant pyuria.

**Normal urinary levels:** Undetectable by dipstick.

**Form in urine:** Dissolved **enzyme** (protein) released from WBCs.

**Pathological significance:**

| LE Result | Possible Causes | Prevalence |
|---|---|---|
| **Positive** | UTI, inflammation, contamination | UTI: most common bacterial infection |
| **Negative** | Normal; or false negative (drugs, high glucose) | — |

**Solubility:** Protein enzyme, soluble in urine.

---

## Detection in Urine

### Available Clinical Assays

1. **Dipstick leukocyte esterase (standard):**
   - **Principle:** LE cleaves indoxyl ester → indoxyl + acid. Indoxyl reacts with diazonium salt → violet azo dye.
   - **Detection:** Colour change: white → pink → violet, graded trace to 3+.
   - **LOD:** ~10–25 WBC/µL equivalent.
   - **Absorption:** ~550 nm (violet azo product).
   - **Read time:** 2 minutes (must not read early).
   - **Sensitivity for UTI:** 75–90%.
   - **Specificity:** 65–80%.

2. **Automated urine analysers with LE pad:**
   - **Principle:** Same chemistry; reflectance photometry for objective colour reading.
   - **Detection:** Reflectance at ~550 nm.
   - **Advantages:** Standardised reading, less operator variation.

3. **Flow cytometry (WBC counting, indirect):**
   - Counts intact WBCs, not LE activity. See White Blood Cells sheet for details.

### Optimal Urine Type for Measurement

- **Midstream clean-catch** — standard.
- LE remains positive **even in old specimens** (enzyme persists after WBC lysis) — advantage over microscopy.
- **Wait full 2 minutes** before reading dipstick (enzymatic reaction slower than other pads).
- Avoid contamination with vaginal secretions.

### Actual Gold Standard

For pyuria detection, **manual microscopy** remains the reference (WBC count/HPF). The LE dipstick is the primary **screening** tool. Combined LE + nitrite has better predictive value for UTI than either alone.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **High glucose** | False negative | Inhibits enzymatic reaction |
| **High albumin** | False negative | Protein inhibition |
| **Ascorbic acid** | Possible false negative | Antioxidant effect |
| **Antibiotics** | False negative | LE inhibition |
| **Formaldehyde** | False positive | Non-specific colour |
| **Oxidising agents** | False positive | Direct oxidation |
| **Vaginal contamination** | False positive | WBCs from vaginal secretions |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- LE itself has no unique UV-Vis chromophore. Detection relies on enzymatic activity assays with chromogenic substrates.
- **Chromogenic substrate assay:** p-nitrophenyl ester → p-nitrophenol (yellow, absorption at **405 nm**). LOD: ~0.1 U/L esterase activity.
- **NIR:** Not applicable.

#### Fluorescence Detection

- **Fluorogenic esterase substrates:** Non-fluorescent ester substrates (e.g., fluorescein diacetate, 4-methylumbelliferyl acetate) cleaved by LE to release fluorescent product.
  - Fluorescein: Ex 490 / Em 520 nm. LOD: ~1 WBC equivalent/µL.
  - 4-Methylumbelliferone: Ex 360 / Em 450 nm. LOD: ~0.5 WBC/µL.
- **Calcein-AM (live cell staining):** Intracellular esterases convert calcein-AM to fluorescent calcein (Ex 495 / Em 515 nm). Detects intact, viable WBCs only.

#### Raman Detection

No specific Raman detection methods for LE enzyme in urine. WBC cellular Raman spectra are discussed in the White Blood Cells sheet.

#### FTIR Detection

No specific FTIR methods for LE detection. Protein amide bands (1650, 1540 cm⁻¹) are non-specific and dominated by more abundant urinary proteins.

#### Voltammetry Detection

- **Electrochemical esterase assay:** LE cleaves electroactive ester substrates (e.g., indoxyl acetate → indoxyl, which is electrochemically oxidised at +0.3 to +0.5 V vs Ag/AgCl).
- LOD: ~5 WBC equivalent/µL.
- **Screen-printed electrodes:** Disposable, paper-based electrochemical LE sensors. LOD: ~10 WBC/µL.

### Other Detection Technologies

1. **Smartphone-based LE dipstick reading:** Camera + app analyses colour of LE pad. LOD: comparable to dipstick (~10–25 WBC/µL). Improved objectivity.

2. **Microfluidic LE sensors:** Integrated fluorogenic substrate reaction + optical detection. LOD: ~1–5 WBC/µL.

3. **Lateral flow immunoassay for neutrophil markers:** Anti-MPO or anti-elastase antibodies on strips. LOD: ~10 ng/mL MPO.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Dipstick LE** | ~10–25 WBC/µL | 550 nm violet dye | None | Rapid, cheap |
| **Automated reflectance** | ~10 WBC/µL | 550 nm | None | Objective |
| **Fluorogenic substrate** | ~0.5–1 WBC/µL | Ex 360–490/Em 450–520 nm | Substrate | More sensitive |
| **Chromogenic** | ~0.1 U/L | 405 nm | Substrate | Quantitative |
| **Electrochemical** | ~5–10 WBC/µL | +0.3–0.5 V | Substrate | Disposable |
| **Microscopy** | ~1 WBC/HPF | 400× | Centrifugation | Gold standard |

---

## Sources

| # | Citation |
|---|---|
| 1 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 2 | Wikipedia — Urine Test Strip. https://en.wikipedia.org/wiki/Urine_test_strip |
| 3 | PMC — WBC and Nitrite in UTI Diagnosis. https://pmc.ncbi.nlm.nih.gov/articles/PMC8253458/ |
| 4 | StatPearls — Pyuria. https://www.ncbi.nlm.nih.gov/books/NBK537089/ |
| 5 | AAFP — Dipstick Urinalysis for UTI. https://aafp.org/pubs/afp/issues/2013/0515/od2.html |
| 6 | LWW — Dipstick Reliability for UTI. https://journals.lww.com/jfmpc/fulltext/2015/04020/reliability_of_dipstick_assay_in_predicting.22.aspx |

## Gaps

- LE dipstick sensitivity for UTI (75–90%) leaves a substantial false-negative rate; improved enzymatic or immunological assays for pyuria are not yet in routine clinical use.
- The fluorogenic substrate approach (4-MU acetate) has not been validated in large clinical studies compared with standard dipstick.
- The combined LE + nitrite interpretation algorithm varies between guidelines and has not been prospectively optimised.
- LE persistence in aged specimens is an advantage but quantitative degradation kinetics in urine at different temperatures and pH are not standardised.
