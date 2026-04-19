---
title: Nitrites
aliases:
  - Nitrite
  - NO2-
  - Nitrite ion
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

# Nitrites

Urinary biomarker for bacterial infection. Detected exclusively via the Griess reaction on clinical dipsticks. See [[datascience/spectroscopy-biomarkers]] for optical detection context and [[signatures]] for spectral reference data.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Nitrite |
| **Other names** | Nitrite ion, NO₂⁻ |
| **Chemical formula** | NO₂⁻ |
| **Molecular weight** | 46.01 g/mol |
| **CAS number** | 14797-65-0 |
| **PubChem CID** | 946 |
| **SMILES** | [N-]=O |
| **Appearance** | Colourless in solution |

Structural formula: `O=N-O(-)` (bent geometry, bond angle ~115°)

Nitrite (NO₂⁻) is an inorganic anion formed by bacterial reduction of nitrate (NO₃⁻) in urine. It is not a metabolic product of human cells but rather a **marker of bacterial presence** in the urinary tract. Nitrate is normally present in urine from dietary sources and is reduced to nitrite by Gram-negative bacteria possessing nitrate reductase (e.g., *E. coli*, *Klebsiella*, *Proteus*).

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Nitrate (NO₃⁻)** | NO₃⁻ | 62.00 | Precursor of nitrite; normally present in urine from diet; not indicative of infection |
| **Nitric oxide (NO)** | NO | 30.01 | Gaseous signalling molecule; not stable in aqueous solution |
| **Nitrogen dioxide (NO₂)** | NO₂ | 46.01 | Toxic gas (neutral molecule, not the ion); environmental pollutant |

---

## Medical Information

### Origin

**Endogenous:** Nitrite is **not endogenously produced** in the urinary tract. Nitrate reductase in Gram-negative bacteria (primarily Enterobacteriaceae: *E. coli*, *Klebsiella*, *Proteus*, *Citrobacter*, *Enterobacter*) reduces dietary urinary nitrate to nitrite. Requires bladder dwell time ≥ 4 hours.

**Exogenous:** Dietary nitrate (green leafy vegetables, cured meats) is the ultimate substrate. Direct dietary nitrite intake (cured meats, E249/E250) does not significantly affect urinary nitrite levels.

### Biological Roles

- **UTI diagnostic marker:** No physiological role in urine. Presence is an indirect indicator of bacteriuria, specifically Gram-negative organisms with nitrate reductase activity.
- **Systemic nitrate-nitrite-NO pathway:** In blood, nitrite serves as a NO reservoir under hypoxia. Unrelated to urinary testing.

### Elimination Pathway

Nitrate is freely filtered and ~60–70% excreted intact. Nitrite in urine is unstable and can be further reduced to N₂, NH₃, or NO. In acidic urine, decomposes to nitrous acid (HNO₂, pKa 3.3).

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Urine nitrite** | Absent (negative on dipstick) |
| **Urine nitrate** | 40–200 mg/day (diet-dependent) |
| **Blood nitrite** | ~0.1–0.5 µmol/L |

### Factors Influencing Levels

**Positive urinary nitrite:** UTI with Gram-negative bacteria, sufficient dietary nitrate, bladder dwell time ≥4 h, urine pH <6.0.

**Negative despite infection:** Gram-positive organisms (Enterococcus, Staphylococcus); short dwell time (<4 h); low dietary nitrate; dilute urine; ascorbic acid; yeast UTI.

### Associated Pathologies

| Condition | Nitrite Status | Key Symptoms |
|---|---|---|
| **Uncomplicated UTI (cystitis)** | Positive (~45–60% sensitivity) | Dysuria, frequency, urgency |
| **Pyelonephritis** | Often positive | Fever, flank pain, nausea |
| **Asymptomatic bacteriuria** | May be positive | No symptoms; screening in pregnancy |
| **Gram-positive UTI** | Negative despite infection | Varies by organism |

### Presence in Urine

Absent in uninfected urine. Presence always indicates bacterial conversion of nitrate. Form: **nitrite ion (NO₂⁻)** at typical urine pH 5–7; at pH <3.3, exists partly as nitrous acid.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **Dipstick Griess (screening)** | Azo dye formation | ~540 nm (visual) | ~11 µmol/L | Sensitivity 45–60%; specificity 85–98% |
| **Griess assay (quantitative)** | Same Griess reaction in solution | 540–548 nm | ~2 µmol/L | Spectrophotometer required |
| **Chemiluminescence (NOA)** | Nitrite → NO → ozone reaction | 600–900 nm | ~1 nM | Research only; Sievers NOA 280i |

Gold standard for screening: **Griess dipstick**. For quantification: solution-phase Griess at 540 nm. For trace research levels: chemiluminescence.

Optimal specimen: **first morning urine** (dwell time ≥4 h). Analyse within 2 h (nitrite is unstable).

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Ascorbic acid (>25 mg/dL)** | False negative | Reduces diazonium salt |
| **Bacterial overgrowth (delay)** | False negative | Further reduction of nitrite |
| **Acidic urine pH (<5)** | Nitrite decomposition | HNO₂ → NO + H₂O |
| **Gram-positive organisms** | False negative | Lack nitrate reductase |
| **Phenazopyridine** | Colour interference | Orange dye obscures colour |

### Spectroscopic Detection

**UV-Vis:** Griess product absorbs at **540–548 nm** (azo dye, LOD ~2 µmol/L). Direct UV: nitrite absorbs at 354 nm (ε ~23 M⁻¹cm⁻¹) and 210 nm (ε ~5,300 M⁻¹cm⁻¹); severe matrix interference limits utility.

**Fluorescence:** DAN (2,3-diaminonaphthalene) assay — nitrite forms fluorescent naphthotriazole at **Ex 365 nm / Em 410 nm**; LOD ~10–50 nM. Rhodamine and quantum-dot probes also described.

**Raman:** Limited sensitivity. Key peaks: 1330 cm⁻¹ (NO₂ sym. stretch), 815 cm⁻¹ (N-O bend), 1240 cm⁻¹ (NO₂ asym. stretch). SERS with Ag nanoparticles improves LOD to ~1–10 µmol/L.

**FTIR:** Key bands at ~1330 cm⁻¹ (strongest), ~1275 cm⁻¹, ~830 cm⁻¹. Not practical for clinical urinary levels.

**Voltammetry:** Direct oxidation NO₂⁻ → NO₃⁻ at +0.7 to +0.9 V vs Ag/AgCl on nanostructured carbon electrodes. LOD ~0.1–1 µmol/L; ascorbic acid interference at similar potentials.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths | Limitations |
|---|---|---|---|---|---|
| **Dipstick Griess** | ~11 µmol/L | ~540 nm (visual) | None | Rapid, cheap, specific | Low sensitivity for UTI |
| **Griess assay (quantitative)** | ~2 µmol/L | 540–548 nm | Reagent addition | Quantitative | Spectrophotometer needed |
| **Chemiluminescence (NOA)** | ~1 nM | 600–900 nm | Reductive conversion | Ultra-sensitive | Complex, research only |
| **DAN fluorescence** | ~10–50 nM | Ex 365 / Em 410 nm | DAN + acid + NaOH | Very sensitive | Derivatisation needed |
| **SERS** | ~1–10 µmol/L | 1330 cm⁻¹; Ex 532/633 nm | Nanoparticles | Label-free | Marginal sensitivity |
| **Voltammetry** | ~0.1–1 µmol/L | +0.7–0.9 V | Buffer dilution | Sensitive, real-time | Ascorbic acid interference |
| **Ion chromatography** | ~0.1 µmol/L | Conductivity | Filtration | Accurate, multi-anion | Instrumentation required |

---

## Sources

| # | Reference |
|---|---|
| 1 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 2 | PMC — Sensitivity and Specificity of WBC and Nitrite in UTI. https://pmc.ncbi.nlm.nih.gov/articles/PMC8253458/ |
| 3 | AAFP — Dipstick Urinalysis for UTI. https://aafp.org/pubs/afp/issues/2013/0515/od2.html |
| 4 | NCBI Books — Urine Dipstick Meta-analysis. https://www.ncbi.nlm.nih.gov/books/NBK70576/ |
| 5 | PubChem — Nitrite ion, CID 946. https://pubchem.ncbi.nlm.nih.gov/compound/946 |
| 6 | Wikipedia — Griess test. https://en.wikipedia.org/wiki/Griess_test |
| 7 | Anal Chem — DAN fluorometric assay for nitrite (standard method reference) |

---

## Gaps

- SERS sensitivity for clinical nitrite detection not yet validated in real urine matrices
- No validated FTIR method for urinary nitrite quantification
- Fluorescent probe methods (DAN, rhodamine) not yet developed into point-of-care formats
- Gram-positive UTI remains undetectable by nitrite testing; alternative biomarkers needed
