---
title: Red Blood Cells
aliases:
  - RBCs
  - Erythrocytes
  - Haematuria
  - Red cells
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

# Red Blood Cells

Cellular biomarker for haematuria. Presence in urine at >3–5/HPF is always abnormal and indicates bleeding in the urinary tract. RBC morphology (isomorphic vs dysmorphic) distinguishes glomerular from lower tract bleeding. See [[datascience/spectroscopy-biomarkers]] and [[optical-properties]] for haemoglobin spectral data.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Red Blood Cells (Erythrocytes) |
| **Other names** | RBCs, erythrocytes, red cells |
| **Nature** | Anucleate biconcave disc cells |
| **Diameter** | 6–8 µm |
| **Thickness** | ~2 µm (edge), ~1 µm (centre) |
| **Mean cell volume (MCV)** | 80–100 fL |
| **Main component** | Haemoglobin (~270 million molecules/cell, ~33% of cell mass) |
| **Lifespan** | ~120 days in circulation |

RBCs are the most abundant cells in blood (~4.5–5.5 million/µL). In urine, their presence (haematuria) is always abnormal above trace quantities. **Isomorphic** RBCs suggest lower urinary tract origin; **dysmorphic** (acanthocytes) suggest glomerular passage.

### Entities Not to Be Confused With

| Entity | Description | Key Difference |
|---|---|---|
| **Free haemoglobin** | Hb released from lysed RBCs | Dissolved protein; dipstick positive but no cells on microscopy |
| **Myoglobin** | Muscle protein (MW 17,800 Da) | Similar dipstick reaction; distinguished by serum colour and CK levels |
| **White blood cells** | Leukocytes, 10–15 µm, granular | Larger, nucleated |
| **Yeast cells** | *Candida*, 3–8 µm, budding | Oval, budding, no central pallor |

---

## Medical Information

### Origin

**Endogenous:** RBCs produced in **bone marrow** from HSCs via erythropoiesis, stimulated by EPO from kidneys. Rate ~200 billion/day. Requires iron, vitamin B12, folate, and EPO.

**Exogenous:** None under normal conditions. Transfusion introduces donor RBCs.

### Biological Roles

- **Oxygen transport:** Haemoglobin binds O₂ in lungs and delivers it to tissues.
- **CO₂ transport:** ~20% as carbaminohaemoglobin; carbonic anhydrase converts CO₂ to HCO₃⁻.
- **pH buffering:** Haemoglobin buffers via histidine residues.
- **Nitric oxide metabolism:** Deoxyhaemoglobin reduces nitrite to NO → vasodilation.

### Elimination Pathway

Aged/damaged RBCs removed by reticuloendothelial macrophages in spleen, liver, and bone marrow. Haemoglobin catabolised: globin → amino acids; heme → biliverdin → bilirubin (bile); iron → recycled via transferrin. **Should not be in urine** — normal glomerular filtration barrier (endothelium + basement membrane + podocytes) prevents RBC passage.

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Blood RBC count** | Male: 4.5–5.5 × 10¹²/L; Female: 4.0–5.0 × 10¹²/L |
| **Urine RBCs (microscopy)** | 0–2 RBC/HPF; <5 RBC/HPF considered normal |
| **Urine RBCs (flow cytometry)** | <25 RBC/µL (Sysmex UF) |
| **Dipstick blood** | Negative (trace may be acceptable) |

### Factors Influencing Levels

**Increased (haematuria):** UTI, nephrolithiasis, glomerulonephritis (IgA nephropathy), bladder/renal/prostate cancer, trauma, vigorous exercise, menstrual contamination, anticoagulant therapy, polycystic kidney disease.

### Associated Pathologies

| Condition | RBC Pattern | Key Symptoms |
|---|---|---|
| **IgA nephropathy** | Dysmorphic RBCs, RBC casts | Episodic gross haematuria with URI; most common GN worldwide |
| **Nephrolithiasis** | Isomorphic RBCs | Flank pain, colicky; ~10% lifetime prevalence |
| **Bladder cancer** | Isomorphic, painless gross haematuria | Risk factors: smoking, age >50; ~550,000 new cases/year globally |
| **UTI** | Isomorphic + bacteria + WBCs | Dysuria, frequency |
| **Glomerulonephritis** | Dysmorphic RBCs, acanthocytes >5%, RBC casts | Proteinuria, oedema, hypertension |
| **Exercise-induced haematuria** | Transient, resolves 24–72 h | Benign; ~20% of runners |

### Presence in Urine

**Should it be present?** No — only trace amounts (0–2/HPF). More than 3–5 RBC/HPF = microscopic haematuria. In hypotonic/alkaline urine, RBCs lyse → "ghost cells" releasing free haemoglobin.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | LOD | Notes |
|---|---|---|---|
| **Dipstick (TMB/peroxidase)** | Pseudoperoxidase activity of Hb catalyses TMB oxidation → green-blue | ~5–10 RBC/µL | Sensitivity ~91–100%; cannot distinguish Hb from myoglobin |
| **Microscopy (sediment)** | Centrifuged sediment at 400x; pale biconcave discs ~7 µm | ~1 RBC/HPF | Gold standard morphology; operator-dependent |
| **Phase-contrast microscopy** | Enhanced RBC morphology; acanthocytes >5% = glomerular | ~1 RBC/HPF | Sensitivity 52–72%, specificity ~98% for glomerular origin |
| **Automated flow cytometry (Sysmex UF-5000)** | Fluorescent nucleic acid dye + scatter; RBCs lack nuclei | ~5 RBC/µL | Rapid, reproducible; no morphology |

Gold standard: **manual microscopy** of centrifuged sediment; phase-contrast at 400x for dysmorphic assessment.

Optimal specimen: **midstream clean-catch**; fresh within 1–2 hours. Avoid menstrual contamination.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Myoglobin** | False positive (dipstick) | Pseudoperoxidase activity similar to Hb |
| **Free haemoglobin (haemolysis)** | False positive for intact RBCs | Dipstick positive but no cells on microscopy |
| **Ascorbic acid** | False negative (dipstick) | Reduces chromogen, inhibiting colour development |
| **Oxidising agents (hypochlorite)** | False positive (dipstick) | Directly oxidise TMB |
| **Alkaline/dilute urine** | RBC lysis | Ghost cells missed on microscopy; Hb detected by dipstick |
| **Bacterial peroxidases** | False positive (dipstick, rare) | Peroxidase activity |

### Spectroscopic Detection

**UV-Vis:** Oxyhaemoglobin Soret band at **415 nm**; Q bands at **542 nm** and **577 nm**. Methaemoglobin at 405 nm and 630 nm. LOD ~0.5 mg/L free Hb (~10 RBC/µL if fully lysed). Sample prep: centrifuge to remove intact cells; measure supernatant.

**Fluorescence:** Mature RBCs lack nuclei → **no nucleic acid fluorescence** (how Sysmex UF differentiates RBCs from WBCs). Autofluorescence from porphyrin ring (Ex 405 / Em 635 nm) is quenched by iron — not practically useful.

**Raman (resonance):** Spectrum dominated by haemoglobin. Key peaks:

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~750** | Pyrrole breathing (porphyrin) |
| **~1003** | Phenylalanine |
| **~1375** | Oxidation state marker (ν₄) |
| **~1550–1580** | Spin state marker (ν₂, ν₁₉) |
| **~1620–1640** | Vinyl C=C stretch |

Resonance Raman with 532 nm excitation (Q-band resonance) strongly enhances porphyrin modes. Single-cell Raman feasible; LOD ~100 RBC/µL in bulk urine.

**FTIR:** Key bands: ~1650 cm⁻¹ (Amide I), ~1540 cm⁻¹ (Amide II), ~1080 cm⁻¹ (phospholipid PO₂⁻). ATR-FTIR on dried sediment detects RBCs at ~10³/µL; not routinely used.

**Voltammetry:** Direct Hb electron transfer at modified electrodes; heme Fe³⁺/Fe²⁺ redox at ~−0.35 V vs Ag/AgCl (pH 7). LOD ~0.1–1 mg/L free Hb. Detects free haemoglobin, not intact cells.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths | Limitations |
|---|---|---|---|---|---|
| **Dipstick (TMB)** | ~5–10 RBC/µL | Green-blue (visual) | None | Rapid, cheap, sensitive | Cannot distinguish Hb/myoglobin |
| **Microscopy** | ~1 RBC/HPF | 400x | Centrifugation | Morphology, casts | Operator-dependent |
| **Phase-contrast microscopy** | ~1 RBC/HPF | Phase optics | Centrifugation | Dysmorphic assessment | Specialised microscope |
| **Flow cytometry (Sysmex)** | ~5 RBC/µL | Ex 488 nm / scatter | None | Automated, fast | No morphology |
| **UV-Vis (Soret, free Hb)** | ~0.5 mg/L Hb | 415 nm | Centrifuge supernatant | Quantitative Hb | Misses intact RBCs |
| **Resonance Raman** | Single cell | Ex 532 nm; 750+1375 cm⁻¹ | Concentrate cells | Single-cell ID | Specialised |
| **FTIR** | ~10³ RBC/µL | 1650+1540 cm⁻¹ | Dry pellet | Multianalyte | Low sensitivity |
| **Electrochemical (Hb)** | ~0.1 mg/L Hb | −0.35 V vs Ag/AgCl | Cell lysis | Sensitive for free Hb | Destroys cells |
| **AI digital microscopy** | ~5 RBC/µL | Digital imaging | None/auto | Automated, morphology | Instrument cost |

---

## Sources

| # | Reference |
|---|---|
| 1 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 2 | StatPearls — Hematuria. https://www.ncbi.nlm.nih.gov/books/NBK534213/ |
| 3 | Harboe (1959) — Hemoglobin determination by Soret band. https://2024.sci-hub.se/2742/7725e4cf7e4ab51e68bcdefc1e17279a/harboe1959.pdf |
| 4 | MDPI Biomolecules (2024) — UV-Vis spectroscopy for hemoglobin quantification. https://www.mdpi.com/2218-273X/14/9/1046 |
| 5 | ACS Anal Chem (2020) — Heme detection methods review. https://pubs.acs.org/doi/10.1021/acs.analchem.0c00415 |
| 6 | Sysmex UF-5000 — Automated urine particle analyser. https://www.sysmex.com/ |
| 7 | BMJ JCP — Detection of myoglobin in urine. https://jcp.bmj.com/content/24/9/816 |

---

## Gaps

- Dysmorphic RBC assessment by automated imaging is not yet as reliable as expert phase-contrast microscopy
- Spectroscopic (Raman/FTIR) distinction between haematuria from different aetiologies not validated
- Haemoglobin vs myoglobin differentiation on dipstick cannot be done without supplemental serum CK — spectroscopic distinction at Soret band possible but requires clean-up step
- Microfluidic impedance cytometry for RBC counting is prototype-stage only
