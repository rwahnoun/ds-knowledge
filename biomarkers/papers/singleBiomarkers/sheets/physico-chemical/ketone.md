---
title: Ketone Bodies
aliases:
  - Ketone
  - Ketone bodies
  - Ketonuria
  - Acetoacetate
  - Beta-hydroxybutyrate
  - BHB
  - Acetone
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

# Ketone Bodies

Ketone bodies are produced by hepatic fatty acid beta-oxidation when carbohydrate availability is limited. The three ketone bodies are: acetoacetate (AcAc), beta-hydroxybutyrate (BHB), and acetone. BHB is the predominant species in blood (~78%), AcAc (~20%), acetone (~2%). The dipstick **primarily detects acetoacetate, not BHB** — a critical limitation in DKA monitoring. See [[datascience/spectroscopy-biomarkers]] for clinical context and [[signatures]] for FTIR/Raman data.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Ketone bodies |
| **Other names** | Ketones, acetone, acetoacetate (AcAc), beta-hydroxybutyrate (BHB) |
| **Chemical formulas** | Acetoacetate: C₄H₅O₃⁻ (MW 101.08); BHB: C₄H₇O₃⁻ (MW 103.10); Acetone: C₃H₆O (MW 58.08) |
| **CAS numbers** | AcAc: 541-50-4; BHB: 300-85-6; Acetone: 67-64-1 |
| **Appearance** | Colourless in solution; acetone is volatile with fruity odour |

**Structural formulas:**

```
  Acetoacetate:         CH3-CO-CH2-COO(-)
  Beta-hydroxybutyrate: CH3-CHOH-CH2-COO(-)
  Acetone:              CH3-CO-CH3
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Lactate** | C₃H₅O₃⁻ | 89.07 | Product of anaerobic glycolysis, not ketogenesis |
| **Pyruvate** | C₃H₃O₃⁻ | 87.06 | Glycolysis intermediate |
| **Free fatty acids** | Variable | Variable | Precursors of ketones; not measured by ketone assays |

---

## Medical Information

### Origin

#### Endogenous: Ketogenesis

Ketone bodies are synthesised in **hepatocyte mitochondria** from acetyl-CoA derived from fatty acid beta-oxidation. Pathway: Acetyl-CoA → acetoacetyl-CoA → HMG-CoA (HMG-CoA synthase, rate-limiting) → acetoacetate (HMG-CoA lyase). AcAc is reduced to BHB or decarboxylated to acetone. Ketogenesis increases during fasting, starvation, low-carb diets, uncontrolled diabetes, and prolonged exercise.

#### Exogenous

Exogenous ketone supplements (BHB salts, ketone esters) are available as dietary supplements. Ketogenic diets (very low carbohydrate) also promote endogenous ketogenesis.

### Primary & Secondary Biological Roles

**Primary role:**
- **Alternative fuel:** BHB and AcAc are oxidised by extrahepatic tissues (brain, heart, skeletal muscle) during [[glucose]] scarcity. Brain can derive up to 75% of energy from ketones during prolonged fasting.

**Secondary roles:**
- **Signalling molecules:** BHB is a histone deacetylase (HDAC) inhibitor; anti-inflammatory signalling via HCAR2 receptor.
- **Acetone:** Volatile waste product; exhaled via lungs (fruity breath odour).

### Catabolism and Elimination Pathway

- BHB and AcAc are oxidised in peripheral tissues: BHB → AcAc (BHB dehydrogenase) → acetoacetyl-CoA (succinyl-CoA transferase) → 2 acetyl-CoA → TCA cycle.
- Acetone is exhaled via lungs or metabolised by CYP2E1.
- **Renal excretion:** Ketones are filtered and partially reabsorbed. At high plasma levels, reabsorption is saturated → ketonuria.
- Normal urinary ketones: <5 mg/dL.

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Blood BHB** | <0.6 mmol/L (fasting up to 0.5 mmol/L) |
| **Blood BHB (ketosis)** | 0.5–3.0 mmol/L (nutritional ketosis) |
| **Blood BHB (DKA)** | >3.0 mmol/L (often >5 mmol/L) |
| **Urine ketones (dipstick)** | Negative |
| **Urine AcAc** | <5 mg/dL |

#### Factors Influencing Levels

**Ketonuria (positive):**
- Diabetic ketoacidosis (DKA)
- Starvation / prolonged fasting
- Alcoholic ketoacidosis
- Ketogenic diet
- Prolonged vomiting (starvation + dehydration)
- Intense exercise
- Pregnancy (accelerated starvation)
- Glycogen storage diseases

**Absent ketonuria:**
- Fed state with adequate carbohydrate
- Well-controlled diabetes
- Early DKA (BHB predominates but dipstick detects AcAc)

#### Associated Pathologies

| Condition | Ketone Pattern | Key Symptoms |
|---|---|---|
| **DKA** | Strongly positive urine + blood BHB >3 mmol/L | Hyperglycaemia, acidosis, dehydration, Kussmaul breathing; ~5% of T1DM/year |
| **Starvation ketosis** | Mild-moderate ketonuria | Nausea, headache, fatigue |
| **Alcoholic ketoacidosis** | Moderate ketonuria + metabolic acidosis | Abdominal pain, vomiting after binge |
| **Hyperemesis gravidarum** | Ketonuria from starvation | Severe nausea/vomiting in pregnancy |

### Presence in Urine

**Should they be normally present?** **No** in fed state. Trace amounts may appear after overnight fasting or intense exercise.

**Normal urinary levels:** Negative (<5 mg/dL AcAc).

**Form in urine:** AcAc and BHB as their **anionic forms** at urine pH. Acetone is volatile and may evaporate.

**Pathological significance:**

| Urinary Ketones | Possible Causes | Prevalence |
|---|---|---|
| **Trace-small** | Fasting, exercise, morning specimen | Common (benign) |
| **Moderate-large** | DKA, starvation, alcoholic ketoacidosis | DKA: ~5% T1DM/year |

**Solubility:** All three ketone bodies are freely soluble in water. No crystallisation.

---

## Detection in Urine

### Available Clinical Assays

1. **Dipstick nitroprusside (Legal) test:**
   - **Principle:** [[sodium|Sodium]] nitroprusside (nitroferricyanide) reacts with AcAc in alkaline conditions → purple colour. Does **NOT detect BHB**.
   - **Detection:** Colour change from beige to purple.
   - **LOD:** ~5–10 mg/dL AcAc (~0.5–1 mmol/L).
   - **Advantages:** Rapid, inexpensive.
   - **Disadvantages:** Does not detect BHB (dominant species in DKA); underestimates true ketosis.

2. **Blood BHB meter (point-of-care, preferred for DKA):**
   - **Principle:** BHB dehydrogenase on electrochemical strip converts BHB → AcAc, generating electrons → current.
   - **Detection:** Amperometric at BHB dehydrogenase electrode.
   - **LOD:** ~0.1 mmol/L.
   - **Advantages:** Detects BHB (dominant species); quantitative; preferred for DKA monitoring.

3. **Enzymatic BHB assay (laboratory):**
   - **Principle:** BHB + NAD⁺ (BHB dehydrogenase) → AcAc + [[nadh|NADH]]. [[nadh|NADH]] measured at 340 nm.
   - **Detection:** 340 nm.
   - **LOD:** ~0.05 mmol/L.

### Optimal Urine Type for Measurement

- **First morning urine** or random specimen for screening.
- For DKA monitoring, **blood BHB** is superior to urine ketones.
- Fresh sample: acetone evaporates and AcAc decomposes at room temperature.
- Cap specimen tightly; test within 1 hour.

### Actual Gold Standard

**Blood BHB measurement** (enzymatic at 340 nm) is the gold standard for ketosis assessment. For urine, the **nitroprusside dipstick** remains the standard screening test, with the limitation of not detecting BHB.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Captopril, mesna** | False positive (dipstick) | Thiol groups react with nitroprusside |
| **L-DOPA metabolites** | False positive | Colour interference |
| **High specific gravity** | False positive | Concentrated specimen |
| **Ascorbic acid (high)** | False negative | Inhibits colour reaction |
| **Delayed testing** | False negative | AcAc decomposes; acetone evaporates |
| **BHB predominance** | False negative (dipstick) | Dipstick detects AcAc, not BHB |
| **Phenylketones (PKU)** | False positive | React with nitroprusside |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- **UV-Vis:** AcAc absorbs weakly at ~270 nm. Not useful in urine matrix.
- **Enzymatic [[nadh|NADH]] (340 nm):** See clinical assay. LOD: ~0.05 mmol/L.
- **NIR:** BHB and AcAc have C-H and C=O overtone bands (~1690–1730 nm region for C=O overtone). PLS calibration with NIR can estimate total ketones. LOD: ~0.5 mmol/L.

#### Fluorescence Detection

- **[[nadh|NADH]] fluorescence (enzymatic):** BHB dehydrogenase + NAD⁺ → [[nadh|NADH]] (Ex 340 / Em 460 nm). LOD: ~0.01 mmol/L.
- **Amplex Red (H₂O₂ detection):** AcAc oxidised enzymatically to generate H₂O₂ → resorufin (Ex 571 / Em 585 nm). LOD: ~0.005 mmol/L.

#### Raman Detection

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~1710** | C=O stretch (AcAc, acetone) |
| **~1365** | CH₃ symmetric deformation |
| **~790** | C-C stretch (acetone) |
| **~1060** | C-O stretch (BHB) |

- LOD: ~10 mM (conventional Raman). SERS can improve to ~0.1 mM.
- Excitation: 785 nm.

#### FTIR Detection

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **~1720** | C=O stretch (AcAc, acetone) | Distinguishable from [[urea]] C=O |
| **~1240** | C-O stretch (BHB) | — |
| **~1370** | CH₃ deformation | — |

- ATR-FTIR: LOD ~1–5 mM. Can detect ketonuria in DKA (levels often >5 mM).

#### Voltammetry Detection

- **BHB dehydrogenase biosensor:** Amperometric detection of [[nadh|NADH]] production at +0.3 V (mediator: Meldola Blue, prussian blue). LOD: ~10 µM.
- **Non-enzymatic AcAc reduction:** At Cu or Ni electrodes in alkaline media. LOD: ~50 µM.
- Linear range: 0.01–10 mM.

### Other Detection Technologies

1. **Breath acetone analysers:** Gas sensors (semiconductor, SIER, photoionisation) detect exhaled acetone. LOD: ~0.1 ppm (correlates with blood BHB). Non-invasive.
2. **Paper-based colorimetric BHB:** BHB-DH + NAD⁺ + tetrazolium salt (colour at 530 nm). LOD: ~0.5 mM. Low cost.
3. **Wearable sweat ketone sensors:** Electrochemical BHB detection in sweat. Prototype stage.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Dipstick (nitroprusside)** | ~5 mg/dL AcAc | Purple colour | None | Rapid, cheap |
| **Blood BHB meter** | ~0.1 mmol/L | Amperometric | Fingerstick | BHB-specific, POC |
| **Enzymatic BHB (lab)** | ~0.05 mmol/L | 340 nm ([[nadh\|NADH]]) | None | Quantitative |
| **[[nadh\|NADH]] fluorescence** | ~0.01 mmol/L | Ex 340/Em 460 nm | Enzyme | Very sensitive |
| **FTIR** | ~1–5 mM | 1720 cm⁻¹ | None | Reagent-free |
| **Raman** | ~10 mM | 1710 cm⁻¹ | None | Non-destructive |
| **Breath acetone** | ~0.1 ppm | Gas sensor | None | Non-invasive |
| **Voltammetry (BHB-DH)** | ~10 µM | +0.3 V mediator | Enzyme | Continuous |

---

## Sources

| # | Citation |
|---|---|
| 1 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 2 | Wikipedia — Urine Test Strip. https://en.wikipedia.org/wiki/Urine_test_strip |
| 3 | StatPearls — Diabetic Ketoacidosis. https://www.ncbi.nlm.nih.gov/books/NBK534848/ |
| 4 | StatPearls — Ketone Body Metabolism. https://www.ncbi.nlm.nih.gov/books/NBK493179/ |
| 5 | PubChem — Acetoacetic acid, CID 96. https://pubchem.ncbi.nlm.nih.gov/compound/96 |

## Gaps

- The dipstick's failure to detect BHB is a well-known clinical limitation; yet BHB-specific urine test strips are not widely deployed in practice.
- NIR multivariate models for urinary ketone quantification have not been validated across DKA severity levels.
- FTIR/Raman LOD (~1–10 mM) only covers severe ketonuria; mild-moderate ketonuria detection requires pre-concentration or alternative methods.
- The correlation between urine AcAc dipstick results and blood BHB levels is variable; no standardised conversion factor exists.
