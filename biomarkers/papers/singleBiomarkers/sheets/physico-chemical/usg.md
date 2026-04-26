---
title: Urine Specific Gravity
aliases:
  - USG
  - Specific gravity
  - Relative density
  - SG
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

# Urine Specific Gravity

Physical property measuring the concentration of dissolved solutes as a ratio to water density. A rapid proxy for [[osmolality]]. Measured clinically by refractometry (gold standard) or dipstick (ionic SG). See [[signal-processing]] and [[optical-properties]] for NIR-based estimation context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Urine Specific Gravity |
| **Other names** | USG, relative density, SG |
| **Nature** | Physical property (not a single molecule) |
| **Definition** | Ratio of urine density to water density at same temperature |
| **Normal range** | 1.002–1.030 |
| **Typical value** | 1.015–1.025 |
| **Units** | Dimensionless (g/mL relative to water = 1.000) |

USG is a measure of the **concentration of dissolved solutes** in urine, reflecting the kidney's ability to concentrate or dilute urine. Major contributors: [[urea]] (~45%), NaCl (~25%), other electrolytes and organic molecules. USG is a surrogate for osmolality but is influenced by molecular weight — [[glucose]] and protein disproportionately raise USG relative to their osmotic contribution.

### Concepts Not to Be Confused With

| Measure | Definition | Key Difference |
|---|---|---|
| **Osmolality ([[osmolality]])** | Total solute particles per kg water (mOsm/kg) | True concentrating ability; independent of MW; more accurate |
| **Osmolarity** | Solute particles per litre solution | Slightly different from osmolality; rarely used clinically |
| **Total dissolved solids (TDS)** | Mass of all dissolved substances | Related; measured differently |

---

## Medical Information

### Origin

**Endogenous:** Reflects net effect of all dissolved solutes — products of metabolism ([[urea]], [[creatinin|creatinine]], [[uric-acid|uric acid]], electrolytes, organic acids, proteins). Controlled by countercurrent mechanism and ADH-mediated aquaporin-2 water reabsorption.

**Exogenous:** High water intake → low USG. High solute intake (protein, salt) → high USG. IV contrast media, mannitol, and dextran raise USG disproportionately.

### Biological Roles

- **Primary:** Indicator of hydration status and renal concentrating ability.
- **Specimen adequacy assessment:** USG <1.003 may indicate specimen too dilute for accurate analyte testing.
- **Drug testing:** Specimens with USG <1.003 considered dilute/invalid.

### Clinical Levels

| Condition | USG Range |
|---|---|
| **Normal (random)** | 1.002–1.030 |
| **First morning (concentrated)** | 1.015–1.030 |
| **After water loading** | 1.001–1.003 |
| **Maximum concentrating ability** | 1.030–1.040 |
| **Fixed (isosthenuria)** | ~1.010 (indicates renal concentrating defect) |

### Factors Influencing Levels

**Increased USG (concentrated):** Dehydration, SIADH, adrenal insufficiency, glycosuria (DM), proteinuria (nephrotic syndrome), IV contrast media, mannitol, high protein diet.

**Decreased USG (dilute):** Excessive water intake, DI (central or nephrogenic), diuretic use, CRF (loss of concentrating ability), hypercalcaemia, hypokalaemia.

### Associated Pathologies

| Condition | USG Pattern | Key Symptoms |
|---|---|---|
| **Diabetes insipidus** | Persistently low (<1.005) despite dehydration | Polyuria, polydipsia |
| **SIADH** | Inappropriately high (>1.020) with hyponatraemia | Confusion, seizures |
| **CKD (advanced)** | Fixed ~1.010 (isosthenuria) | Nocturia, polyuria |
| **Dehydration** | High (>1.025) | Thirst, tachycardia |
| **Water intoxication** | Very low (<1.003) | Hyponatraemia, confusion |

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Resolution | Notes |
|---|---|---|---|
| **Refractometry (gold standard)** | Refractive index proportional to total dissolved solutes; critical angle refractometer | ~0.001 SG | Temperature-compensated digital instruments (Reichert, Atago); affected by [[glucose]] and protein |
| **Dipstick (ionic SG)** | Polyelectrolyte releases H⁺ proportional to ionic strength → bromothymol blue colour change | ~0.005 (reads 1.000–1.030) | Measures ionic strength only; non-ionic solutes ([[glucose]], [[urea]]) not detected; alkaline pH → false low |
| **Urinometry/hydrometry (historical)** | Floating hydrometer; buoyancy proportional to density | ~0.001 | Large volume (15–20 mL); largely obsolete |
| **Oscillating U-tube densitometry** | Resonant frequency of U-tube filled with urine | ~0.0001 g/mL | Very precise; automated |

Gold standard: **Refractometry**. Precision ±0.001; temperature correction to 20 °C.

Optimal specimen: first morning for concentrating ability; random for routine hydration assessment. Temperature correction needed for refractometry.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **[[glucose\|Glucose]] (>1 g/dL)** | Falsely high SG (refractometer) | High-MW solute; dipstick unaffected (non-ionic) |
| **Protein (>1 g/dL)** | Falsely high SG (refractometer) | High-MW solute |
| **IV contrast media** | Very high SG (>1.040) | Dense iodinated molecules |
| **Alkaline pH (>8)** | Falsely low SG (dipstick) | Interferes with polyelectrolyte reaction |
| **Temperature** | Variable (refractometer) | Must correct to 20 °C standard |

### Spectroscopic Detection

**NIR:** Urine water content and solute concentration affect NIR O-H overtone bands (~1450, 1940 nm). PLS calibration predicts USG; LOD/resolution ~0.002 SG units. No sample prep.

**Raman:** Water O-H stretch (~3400 cm⁻¹) intensity inversely correlates with solute concentration. Potentially usable via chemometric models; not clinically validated.

**FTIR (ATR):** Balance of water vs solute bands correlates with USG. PLS calibration can estimate USG from overall spectral profile; LOD ~0.003 SG units. No sample prep.

**Voltammetry (conductivity):** Ionic strength partially correlates with USG. Conductivity electrodes give real-time measurement; does not capture non-ionic solutes. Equivalent to dipstick ionic SG.

**UV-Vis / Fluorescence:** Not applicable — USG is a bulk physical property.

### Detection Methods Comparison

| Method | Resolution | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Refractometry** | ~0.001 | Refractive index | None | Gold standard, fast |
| **Dipstick (ionic SG)** | ~0.005 | pH indicator colour | None | Included on dipstick |
| **Oscillating U-tube** | ~0.0001 | Resonant frequency | None | Very precise |
| **NIR spectroscopy** | ~0.002 | 1450+1940 nm | None | Reagent-free |
| **ATR-FTIR** | ~0.003 | Overall spectrum | None | Multianalyte |
| **Conductivity** | N/A | mS/cm | None | Real-time |
| **Acoustic densitometry** | ~0.0001 | Speed of sound | None | Non-contact |

---

## Sources

| # | Reference |
|---|---|
| 1 | Wikipedia — Urine Test Strip. https://en.wikipedia.org/wiki/Urine_test_strip |
| 2 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 3 | StatPearls — Urinalysis. https://www.ncbi.nlm.nih.gov/books/NBK557685/ |
| 4 | Mayo Clinic — Urinalysis. https://www.mayoclinic.org/tests-procedures/urinalysis/about/pac-20384907 |

---

## Gaps

- Dipstick ionic SG misses non-ionic solutes ([[glucose]], [[urea]]) — correlation with true osmolality deteriorates in diabetic or high-protein urine
- NIR/FTIR USG estimation requires per-population calibration; no validated Jimini-specific model
- Refractometry overestimates USG when [[glucose]] or contrast media are present — clinically important in ICU and oncology patients
- The relationship between USG and individual biomarker concentrations is nonlinear, complicating normalisation strategies
