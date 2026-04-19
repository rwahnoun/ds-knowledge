---
title: PFAS
aliases:
  - Per- and Polyfluoroalkyl Substances
  - Forever chemicals
  - PFCs
  - PFOS
  - PFOA
  - GenX
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

# PFAS

Environmental contaminants detectable in urine as biomonitoring targets. Short-chain PFAS (PFBA, PFBS) are the primary urinary analytes; long-chain PFAS (PFOS, PFOA) are better measured in serum. See [[datascience/spectroscopy-biomarkers]] for optical detection context.

> [!NOTE]
> PFAS have no physiological role. Their presence in urine reflects ubiquitous environmental exposure. Urinary PFAS measurement is used in exposure assessment and epidemiology, not routine clinical care.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Per- and Polyfluoroalkyl Substances (PFAS) |
| **Other names** | Forever chemicals, PFCs, PFOS, PFOA, GenX |
| **Chemical formula** | Variable; general: CₙF₍₂ₙ₊₁₎-R |
| **Key species** | PFOS (C₈HF₁₇O₃S, MW 500.13); PFOA (C₈HF₁₅O₂, MW 414.07) |
| **CAS numbers** | PFOS: 1763-23-1; PFOA: 335-67-1 |
| **Nature** | Class of >12,000 synthetic fluorinated organic compounds |
| **Solubility** | Amphiphilic; PFOA ~3.4 g/L; PFOS ~0.57 g/L |

### Key PFAS Species

| Compound | Formula | MW (g/mol) | Notes |
|---|---|---|---|
| **PFOS** | C₈F₁₇SO₃⁻ | 499.12 | Long-chain; half-life ~5 years; legacy |
| **PFOA** | C₇F₁₅COOH | 414.07 | Long-chain; half-life ~3.5 years; IARC 2B carcinogen |
| **GenX (HFPO-DA)** | C₆HF₁₁O₃ | 330.05 | Short-chain replacement; shorter half-life |
| **PFBS** | C₄F₉SO₃⁻ | 299.09 | Short-chain sulfonate; faster renal excretion |
| **Fluoride (F⁻)** | F⁻ | 19.00 | Inorganic; entirely different from organofluorine PFAS |

---

## Medical Information

### Origin

Entirely **exogenous/anthropogenic**. Sources:
- **Drinking water:** Contaminated by industrial discharge, AFFF firefighting foam runoff. EPA MCL for PFOA and PFOS: 4 ng/L (2024 rule).
- **Food:** Migration from food packaging; bioaccumulation in fish, meat, dairy.
- **Consumer products:** Non-stick cookware, stain-resistant fabrics, cosmetics.
- **Occupational:** Manufacturing workers, firefighters (AFFF exposure).
- **Air/dust:** Indoor dust from treated textiles and carpets.

### Biological Roles and Toxicity

PFAS have **no physiological role**. They are xenobiotic persistent organic pollutants.

Known toxic effects (epidemiological evidence):
- Immunotoxicity (reduced vaccine response) — strong evidence; basis for EPA health advisory
- Thyroid disruption (PFOS)
- Hepatotoxicity (elevated liver enzymes)
- Dyslipidaemia (elevated cholesterol)
- Developmental toxicity
- Potential carcinogenicity: kidney, testicular cancer (PFOA: IARC Group 2B)

### Elimination Pathway

PFAS are **not metabolised** in humans (C-F bonds are among the strongest in organic chemistry). Long-chain PFAS (PFOS, PFOA): half-lives **3–8 years**; very slow urinary excretion; bind strongly to serum albumin. Short-chain PFAS (PFBS, PFHxA): half-lives of **days to weeks**; faster renal excretion; primary elimination via **urine**.

### Urinary Levels

| Compartment | Reference Range |
|---|---|
| **Serum PFOS (general population)** | 1–20 ng/mL (declining since phase-out) |
| **Serum PFOA** | 0.5–5 ng/mL |
| **Urine PFOS** | <LOD to ~0.1 ng/mL (long-chain: very low) |
| **Urine PFBA/PFBS (short-chain)** | 0.1–5 ng/mL |

Serum is the preferred matrix for long-chain PFAS; urine for short-chain.

### Factors Influencing Levels

**Increased:** Proximity to contaminated sites, occupation (firefighters), contaminated water/food, PFAS-containing consumer products.

**Decreased:** Avoidance of contaminated sources; time since last exposure.

### Associated Pathologies

| Condition | PFAS Association | Evidence Level |
|---|---|---|
| **Elevated cholesterol** | PFOA/PFOS dyslipidaemia | Strong epidemiological |
| **Thyroid disease** | PFOS thyroid disruption | Moderate |
| **Immune suppression** | Reduced vaccine antibody response | Strong (EPA basis) |
| **Kidney cancer** | PFOA: IARC Group 2B | Limited human evidence |
| **Testicular cancer** | PFOA elevated risk in workers | Limited |
| **Pre-eclampsia** | PFAS exposure in pregnancy | Emerging |

---

## Detection in Urine

### Clinical Assays

| Method | Principle | LOD | Notes |
|---|---|---|---|
| **Online SPE-LC-MS/MS (gold standard)** | SPE + RP-HPLC + tandem MS (negative ESI) | 0.01–0.1 ng/mL | CDC/NHANES method; 20+ PFAS simultaneously |
| **UPLC-MS/MS** | Faster chromatography; same MS detection | ~0.01 ng/mL | High-throughput variant |

Gold standard: **Online SPE-LC-MS/MS** (CDC/NHANES). MRM transitions: PFOS m/z 499→80; PFOA m/z 413→369; PFBS m/z 299→80.

Optimal specimen: **spot urine** with [[creatinin|creatinine]]/SG correction for short-chain PFAS. Use **PFAS-free collection materials** (no PTFE/Teflon). Store frozen at −20 °C.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **PTFE labware contamination** | False positive | PFAS leaching from Teflon |
| **Matrix effects (ion suppression)** | Variable | Co-eluting phospholipids and salts |
| **Background lab contamination** | Elevated blank | Ubiquitous PFAS in solvents and tubing |
| **Branched isomers** | Multiple peaks | Linear vs branched PFOS separation required |

### Spectroscopic Detection

**UV-Vis:** Most PFAS have minimal UV-Vis absorption (no chromophore). Absorption <210 nm, not useful in urine.

**NIR:** No useful absorption.

**Fluorescence:** Most PFAS are non-fluorescent. Indirect competitive immunofluorescence (anti-PFOS + fluorescent tracer): LOD ~0.1–1 ng/mL; MIP-based fluorescence quenching: LOD ~1 ng/mL. Both still research stage.

**Raman:** Characteristic C-F stretch modes: ~730 cm⁻¹ (CF₂ sym. stretch), ~1220 cm⁻¹ (CF₂ asym. stretch), ~390 cm⁻¹ (CF₂ wagging). Conventional LOD >>1 µg/mL. SERS: potentially ~1–10 ng/mL on specialised substrates.

**FTIR:** Strong C-F stretching bands at ~1150–1250 cm⁻¹ and ~1320–1370 cm⁻¹. Detectable only at mg/L levels — not useful for ng/L biomonitoring.

**Voltammetry:** PFAS are electrochemically inert in the normal potential window. EIS-based MIP sensors: LOD ~0.1–10 ng/mL. Boron-doped diamond electrodes can reduce some PFAS at −2.5 V (research only).

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths | Limitations |
|---|---|---|---|---|---|
| **LC-MS/MS** | ~0.01–0.1 ng/mL | MRM (ESI⁻) | SPE/dilute | Gold standard, multi-PFAS | Instrument cost |
| **ELISA/immunofluorescence** | ~0.1–1 ng/mL | 450 nm or fluorescence | Plate assay | Screening | Limited multiplexing |
| **Total organic fluorine (EOF)** | ~2 ng/mL F | CIC or PIGE | Extraction | Total PFAS burden | No speciation |
| **EIS-MIP sensor** | ~0.1–10 ng/mL | Impedance | MIP electrode | Reagent-free | Research stage |
| **SERS** | ~1–10 ng/mL | 730 cm⁻¹ | Substrate | Research | Not validated |
| **FTIR** | >1 µg/mL | 1150–1250 cm⁻¹ | None | N/A | Inadequate sensitivity |

---

## Sources

| # | Reference |
|---|---|
| 1 | CDC — PFAS in Urine and Serum by Online SPE-LC-MS/MS. https://stacks.cdc.gov/view/cdc/103807 |
| 2 | Springer ABC — LC-MS for 56 PFAS in plasma. https://link.springer.com/article/10.1007/s00216-026-06486-2 |
| 3 | Academia — PFAS in human urine biomonitoring pilot. https://www.academia.edu/77039978/ |
| 4 | EPA — PFAS National Primary Drinking Water Regulation (2024) |
| 5 | IARC — PFOA and PFOS Monographs (2023) |

---

## Gaps

- No spectroscopic method (NIR/Raman/FTIR) approaches clinical sensitivity for urinary PFAS — LC-MS/MS is the only viable method
- Short-chain PFAS [[creatinin|creatinine]]-corrected spot urine norms not well-established in diverse populations
- SERS substrates for PFAS detection remain research prototypes without matrix validation in real urine
- Exposure attribution models (water vs food vs consumer products) remain uncertain for individual patients
