---
title: Osmolality
aliases:
  - Urine osmolality
  - uOsm
  - Urinary osmolality
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

# Osmolality

Physical property measured on the Jimini platform as a proxy for hydration and renal concentrating ability. See [[signal-processing]] for NIR-based estimation approaches and [[optical-properties]] for spectral context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Osmolality |
| **Other names** | Urine osmolality, uOsm |
| **Nature** | Physical property (total solute concentration) |
| **Definition** | Number of osmoles of solute per kg of solvent (mOsm/kg H₂O) |
| **Normal range** | 50–1200 mOsm/kg (depends on hydration) |
| **Typical value** | 300–900 mOsm/kg |
| **Units** | mOsm/kg (milliosmoles per kilogram water) |

Osmolality measures the total concentration of dissolved particles in urine, regardless of size, charge, or nature. Major contributors:  [[urea]] (~50%), Na⁺/Cl⁻ (~25%), K⁺ (~15%), and other electrolytes/organic solutes. It is the truest measure of renal concentrating and diluting ability, superior to USG because it is unaffected by large molecules ([[glucose]], protein, contrast).

### Concepts Not to Be Confused With

| Measure | Definition | Key Difference |
|---|---|---|
| **Specific gravity ([[usg]])** | Density ratio to water | Affected by molecular weight; less accurate |
| **Osmolarity** | mOsm per litre solution | Slightly different; osmolality preferred clinically |

---

## Medical Information

### Origin

**Endogenous:** Reflects all solutes in urine — [[urea]] (from protein catabolism), electrolytes (Na, K, Cl, NH4⁺), [[creatinin|creatinine]], [[uric-acid|uric acid]], organic acids, and [[phosphate]]. The kidney regulates osmolality via ADH-mediated water reabsorption (collecting duct aquaporin-2) and the countercurrent mechanism.

**Exogenous:** Dietary water and solute intake directly determine urine osmolality. High water intake → dilute urine. High protein/salt intake → concentrated urine. Osmotically active substances (mannitol, sorbitol, contrast) increase uOsm.

### Biological Roles

- **Primary:** Indicator of renal concentrating/diluting ability and hydration status.
- **Secondary:** Differential diagnosis of hyponatraemia (SIADH vs psychogenic polydipsia), polyuria (DI vs osmotic diuresis), and AKI. ADH function assessment via water deprivation test.

### Clinical Levels

| Condition | Osmolality (mOsm/kg) |
|---|---|
| **Random urine** | 300–900 |
| **First morning (concentrated)** | 500–1200 |
| **After water loading** | 50–100 |
| **Maximum concentration** | 1200–1400 (young adults) |
| **Serum osmolality** | 275–295 |

### Factors Influencing Levels

**Increased uOsm:** Dehydration, SIADH, adrenal insufficiency, osmotic diuresis ([[glucose]]).

**Decreased uOsm:** Water intoxication, central DI, nephrogenic DI, CKD (loss of concentrating ability), compulsive water drinking.

### Associated Pathologies

| Condition | uOsm Pattern | Key Symptoms |
|---|---|---|
| **Central DI** | <300 despite dehydration; rises with desmopressin | Polyuria, polydipsia |
| **Nephrogenic DI** | <300 despite dehydration; no response to desmopressin | Polyuria, polydipsia |
| **SIADH** | >100 (often >300) with serum hyponatraemia | Confusion, seizures |
| **Psychogenic polydipsia** | <100 (appropriately dilute) | Polyuria, normal serum Na |

---

## Detection in Urine

### Clinical Assays

| Method | Principle | LOD | Notes |
|---|---|---|---|
| **FPD osmometry (gold standard)** | Freezing-point depression (1 Osm/kg = −1.86 °C) | ~1 mOsm/kg | Advanced Instruments, Gonotec; CV <1% |
| **Vapour pressure osmometry** | Dew-point temperature | ~5 mOsm/kg | Small volume (10 µL); affected by volatile solutes (ethanol) |
| **Calculated osmolality** | 2(Na + K) + [[[[urea]]\|Urea]] + [[[[glucose]]\|Glucose]] (mmol/L) | N/A | Only an estimate; misses unmeasured osmoles |

Gold standard: **Freezing-point depression osmometry**. Precision ±2 mOsm/kg.

Optimal specimen: first morning for concentrating ability; random with simultaneous serum osmolality for clinical context.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Volatile solutes (ethanol, methanol)** | Underestimation by VPO | Evaporate during measurement |
| **Very high protein** | Minor effect on FPD | Colligative property alteration |
| **Delayed analysis** | Bacterial alteration | Changes solute composition |

### Spectroscopic Detection

**NIR:** Water O-H bands (1450, 1940 nm) shift with solute concentration. PLS regression predicts osmolality; LOD ~10 mOsm/kg. No sample prep needed.

**Mid-IR (ATR-FTIR):** Overall spectral profile correlates with osmolality via PLS; similar approach to NIR.

**Fluorescence / Raman / Voltammetry:** Not directly applicable — osmolality is a bulk physical property, not a molecular analyte. Conductivity correlates with ionic osmolality but misses non-ionic solutes ([[urea]], [[glucose]]).

### Detection Methods Comparison

| Method | LOD/Resolution | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **FPD osmometry** | ~1 mOsm/kg | Freezing-point depression | None | Gold standard |
| **VPO** | ~5 mOsm/kg | Dew-point temperature | None | Small volume |
| **Calculated** | N/A | 2(Na+K)+[[[[urea]]\|Urea]]+Gluc | Blood/urine chem | No extra instrument |
| **NIR spectroscopy** | ~10 mOsm/kg | 1450, 1940 nm | None | Reagent-free |
| **Conductivity** | N/A | mS/cm | None | Real-time |
| **Refractometry (USG proxy)** | ~0.001 SG | Refractive index | None | Fast |

---

## Sources

| # | Reference |
|---|---|
| 1 | StatPearls — Urine Osmolality. https://www.ncbi.nlm.nih.gov/books/NBK567764/ |
| 2 | Mayo Clinic — Urinalysis. https://www.mayoclinic.org/tests-procedures/urinalysis/about/pac-20384907 |
| 3 | PMC — Urine Electrolytes and Osmolality. https://ncbi.nlm.nih.gov/pmc/articles/PMC8116912/ |
| 4 | Advanced Instruments — Osmometry technology |

---

## Gaps

- NIR-based osmolality prediction requires chemometric models trained on population-representative urine samples; no validated Jimini-specific model exists yet
- VPO underestimates in samples with ethanol/methanol — relevant if screening for alcohol use
- Multi-parameter ML models (conductivity + RI + pH) need prospective validation in clinical cohorts
