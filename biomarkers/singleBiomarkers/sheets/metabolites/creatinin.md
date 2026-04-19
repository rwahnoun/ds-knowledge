---
title: Creatinine
aliases:
  - Creatinine
  - Creatinin
  - Urine creatinine
  - GFR marker
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

# [[creatinin|Creatinine]]

[[creatinin|Creatinine]] is a cyclic derivative of creatine, formed by spontaneous non-enzymatic dehydration of creatine [[phosphate]] in muscle. It is the most widely used endogenous marker of glomerular filtration rate (GFR) and the standard normalisation factor for spot urine measurements. See [[datascience/spectroscopy-biomarkers]] for clinical context and [[signatures]] for Raman/FTIR spectral characteristics.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | [[creatinin\|Creatinine]] |
| **Other names** | 2-Amino-1-methyl-2-imidazolidin-4-one, Creatinin |
| **Chemical formula** | C₄H₇N₃O |
| **Molecular weight** | 113.12 g/mol |
| **CAS number** | 60-27-5 |
| **PubChem CID** | 588 |
| **SMILES** | CN1CC(=O)NC1=N |
| **Appearance** | White crystalline powder |
| **Melting point** | 300 °C (decomposes) |
| **Solubility in water** | ~90 g/L at 20 °C |

**Structural formula:**

```
    CH3
     |
     N---CH2
     |      |
     C=NH   C=O
          |
          NH
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Creatine** | C₄H₉N₃O₂ | 131.13 | Precursor; amino acid derivative; not a waste product |
| **Creatine [[phosphate]]** | C₄H₁₀N₃O₅P | 211.11 | Energy storage molecule in muscle; dephosphorylation yields [[creatinin\|creatinine]] |
| **[[[[urea]]\|Urea]]** | CH₄N₂O | 60.06 | Different nitrogen waste product; from amino acid catabolism, not muscle |
| **Cystatin C** | Protein | 13,343 | Alternative GFR marker; not affected by muscle mass |

---

## Medical Information

### Origin

#### Endogenous: Biosynthesis — Creatine-Phosphocreatine Pathway

[[creatinin|Creatinine]] is produced by **irreversible, non-enzymatic cyclisation** of creatine [[phosphate]] (and to a lesser extent, free creatine) in skeletal muscle. The process:

1. **Creatine synthesis:** Arginine + Glycine (in kidney) via AGAT → guanidinoacetate, then methylated by GAMT (in liver) using SAM → **creatine**.
2. **Phosphorylation:** Creatine + ATP (via creatine kinase) → **creatine [[phosphate]]** (PCr) in muscle.
3. **[[creatinin|Creatinine]] formation:** PCr spontaneously dehydrates at ~1.7%/day → **[[creatinin|creatinine]]** (irreversible).

Daily [[creatinin|creatinine]] production: ~15–25 mg/kg/day (~1.0–1.8 g/day), proportional to muscle mass. Production is remarkably constant day-to-day for an individual.

#### Exogenous

Dietary [[creatinin|creatinine]] from cooked meat (~1.5–2.5 g creatine per kg of meat; cooking converts some creatine to [[creatinin|creatinine]]). Creatine supplements increase [[creatinin|creatinine]] production.

### Primary & Secondary Biological Roles

**Primary role:**
- **Waste product / GFR marker:** [[creatinin|Creatinine]] has no physiological function. Its clinical value lies in being a nearly ideal endogenous GFR marker: freely filtered, not reabsorbed, minimal secretion (10–15% tubular secretion).

**Secondary roles:**
- Used as a **normalisation factor** for spot urine measurements of other analytes (analyte/[[creatinin|creatinine]] ratio corrects for urine concentration).

### Catabolism and Elimination Pathway

- [[creatinin|Creatinine]] is released from muscle into plasma at a constant rate.
- **Freely filtered** at the glomerulus (100%).
- ~10–15% **secreted** by proximal tubular organic cation transporters (OCT2, MATE1/2).
- **Not reabsorbed** (or minimally so).
- Urinary [[creatinin|creatinine]] excretion = [[creatinin|creatinine]] production rate at steady state.
- [[creatinin|Creatinine]] clearance (CrCl) approximates GFR (slight overestimate due to secretion).

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Serum [[creatinin\|creatinine]]** | Male: 0.7–1.3 mg/dL (62–115 µmol/L); Female: 0.6–1.1 mg/dL (53–97 µmol/L) |
| **Urinary [[creatinin\|creatinine]] (24-h)** | Male: 14–26 mg/kg/day (1.0–1.8 g/day); Female: 11–20 mg/kg/day (0.8–1.4 g/day) |
| **Urinary [[creatinin\|creatinine]] concentration** | 3–30 mmol/L (highly variable with hydration) |
| **[[creatinin\|Creatinine]] clearance** | 90–140 mL/min (approximates GFR) |
| **eGFR (CKD-EPI)** | >90 mL/min/1.73 m² |

#### Factors Influencing Levels

**Increased serum [[creatinin|creatinine]] (decreased GFR):**
- Acute kidney injury (AKI)
- Chronic kidney disease (CKD)
- Rhabdomyolysis (massive creatine release)
- High meat diet (transient)
- Creatine supplements
- Drugs inhibiting secretion (trimethoprim, cimetidine) — raise serum Cr without changing GFR

**Decreased serum [[creatinin|creatinine]]:**
- Low muscle mass (cachexia, elderly, amputees)
- Liver disease (reduced creatine synthesis)
- Pregnancy (increased GFR + haemodilution)

#### Associated Pathologies

| Condition | [[creatinin\|Creatinine]] Pattern | Key Symptoms |
|---|---|---|
| **AKI** | Rapidly rising serum Cr (>0.3 mg/dL in 48 h) | Oliguria, fluid overload |
| **CKD** | Chronically elevated serum Cr | Fatigue, anaemia, bone disease |
| **Rhabdomyolysis** | Very high serum Cr + CK | Muscle pain, dark urine, AKI risk |
| **Muscle wasting** | Low serum Cr, low urinary Cr | Sarcopenia, malnutrition |

### Presence in Urine

**Should it be normally present?** **Yes** — [[creatinin|creatinine]] is a major normal urinary solute. It is the basis for urine concentration normalisation.

**Normal urinary levels:** 1.0–1.8 g/day (8.8–15.9 mmol/day) for men; 0.8–1.4 g/day for women. Concentration: 3–30 mmol/L.

**Form in urine:** **Native dissolved molecule** (neutral at urine pH, pKa ~4.8 for the imino group).

**Pathological significance:**

| Urinary [[creatinin\|Creatinine]] | Possible Causes | Prevalence |
|---|---|---|
| **Low 24-h excretion** | Incomplete collection, low muscle mass, advanced CKD | Common artefact |
| **High 24-h excretion** | High muscle mass, meat-rich diet | Normal variant |

**Solubility:** ~90 g/L at 20 °C. [[creatinin|Creatinine]] does not crystallise in urine normally.

---

## Detection in Urine

### Available Clinical Assays

1. **Jaffe reaction (alkaline picrate, most common):**
   - **Principle:** [[creatinin|Creatinine]] reacts with picric acid in alkaline solution → orange-red Janovsky complex.
   - **Detection:** Absorbance at **520 nm** (kinetic measurement).
   - **LOD:** ~0.1 mg/dL (~9 µmol/L).
   - **Advantages:** Simple, inexpensive, widely available on all platforms.
   - **Disadvantages:** Non-specific; interfered by [[glucose]], acetoacetate, proteins, cephalosporins.

2. **Enzymatic [[creatinin|creatinine]] assay:**
   - **Principle:** [[creatinin|Creatinine]] → creatine (creatininase) → sarcosine + [[urea]] (creatinase) → glycine + HCHO + H₂O₂ (sarcosine oxidase) → colour (Trinder reaction, peroxidase + chromogen).
   - **Detection:** Absorbance at **546 nm** (Trinder) or **340 nm** ([[nadh|NADH]]-coupled).
   - **LOD:** ~0.05 mg/dL.
   - **Advantages:** More specific than Jaffe; less interference.
   - **Disadvantages:** More expensive reagents.

3. **HPLC (reference method):**
   - **Principle:** Reversed-phase or ion-exchange HPLC with UV detection at **234 nm** ([[creatinin|creatinine]] absorption).
   - **LOD:** ~0.01 mg/dL.
   - **Advantages:** Highly specific; reference method (NIST SRM 967).
   - **Disadvantages:** Not routine; research/reference labs.

4. **IDMS (isotope dilution mass spectrometry):**
   - **Principle:** Gold-standard reference method for [[creatinin|creatinine]] calibration.
   - **LOD:** <0.001 mg/dL.

### Optimal Urine Type for Measurement

- **24-hour urine** for [[creatinin|creatinine]] clearance calculation and total excretion assessment (completeness check: expected 15–25 mg/kg/day).
- **Spot urine** for [[creatinin|creatinine]]-normalised ratios (albumin/[[creatinin|creatinine]], protein/[[creatinin|creatinine]]).
- Second morning void preferred for spot ratios (less variation).
- Stable at room temperature for 24–48 h; refrigerate for longer storage.

### Actual Gold Standard

**IDMS** is the ultimate reference method for [[creatinin|creatinine]] standardisation. For clinical use, **enzymatic assays** (IDMS-traceable calibration) are preferred over Jaffe. Both are available on all major automated platforms. CV: 2–5% (Jaffe), 1–3% (enzymatic).

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **[[[[glucose]]\|Glucose]] (Jaffe)** | Positive bias | Reacts with alkaline picrate |
| **Acetoacetate (Jaffe)** | Positive bias | Ketone body interference |
| **Cephalosporins (Jaffe)** | Positive bias | Chromogen formation |
| **Bilirubin (Jaffe)** | Negative bias | Absorbs at 520 nm; subtractive |
| **Haemolysis** | Variable | Released proteins interfere |
| **Ascorbic acid (enzymatic)** | Negative bias | Inhibits Trinder reaction |
| **Dopamine, dobutamine** | Positive bias (enzymatic) | Interfere with H₂O₂ detection |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- **UV absorption:** [[creatinin|Creatinine]] absorbs at **234 nm** (ε ~6,850 M⁻¹cm⁻¹). Direct UV quantification possible but non-specific in urine matrix.
  - LOD: ~0.5 mg/dL in buffer; urine requires HPLC separation.
- **Jaffe chromogen:** 520 nm (see above).
- **NIR:** [[creatinin|Creatinine]] has weak NIR overtone bands (~2170 nm). Multivariate calibration with PLS gives LOD ~0.5 mg/dL in urine.

#### Fluorescence Detection

- [[creatinin|Creatinine]] itself is weakly fluorescent (Ex ~240 nm / Em ~390 nm) — not useful.
- **Enzymatic fluorometric:** Sarcosine oxidase cascade produces H₂O₂ → coupled with Amplex Red (Ex 571 / Em 585 nm). LOD: ~0.01 mg/dL.
- **3-Hydroxyflavone probes:** React with [[creatinin|creatinine]] in alkaline conditions → fluorescent product (Ex 370 / Em 520 nm). LOD: ~0.1 mg/dL.

#### Raman Detection

[[creatinin|Creatinine]] has characteristic Raman peaks useful for label-free quantification in urine. See [[signatures]] for full spectral context.

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~680** | Ring breathing |
| **~845–850** | C-N stretch |
| **~910** | Ring deformation |
| **~1400–1420** | CN stretch + CH₃ deformation |
| **~1490** | C=N stretch |

- Conventional Raman: LOD ~5 mM (~56 mg/dL) — adequate for concentrated urine.
- SERS (Ag nanoparticles): LOD ~10–100 µM.
- Excitation: 532 or 785 nm.

#### FTIR Detection

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **~1492** | C=N stretch | Key diagnostic band (shifts with hydration) |
| **~1590** | NH bending | Overlaps with [[urea]] |
| **~1670** | C=O stretch | Ring carbonyl |
| **~2500–3200** | N-H stretches | Broad |

- ATR-FTIR can quantify [[creatinin|creatinine]] in urine (the 1492 cm⁻¹ band). LOD: ~5 mM in liquid urine.
- Hydration-dependent spectral changes documented (Rich & Sheringham, 2017).

#### Voltammetry Detection

- **Direct oxidation:** [[creatinin|Creatinine]] oxidised at +0.8–1.0 V vs Ag/AgCl on modified electrodes (copper nanoparticles, MIP/graphene composites).
  - LOD: ~1–10 µM on nanostructured electrodes.
- **MIP-based electrochemical sensors:** Molecularly imprinted polymer for [[creatinin|creatinine]] recognition.
  - LOD: ~0.5 µM.
  - Linear range: 1–1000 µM.

### Other Detection Technologies

1. **Capillary electrophoresis:** UV detection at 200–234 nm. LOD: ~0.5 µM. Fast separation.
2. **Paper-based colorimetric (Jaffe):** Picrate-impregnated paper strip + smartphone readout. LOD: ~0.5 mg/dL.
3. **Microfluidic enzymatic sensor:** Lab-on-chip with integrated enzymatic cascade. LOD: ~0.1 mg/dL.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Jaffe reaction** | ~0.1 mg/dL | 520 nm | None | Universal, cheap |
| **Enzymatic assay** | ~0.05 mg/dL | 546 nm | None | More specific |
| **HPLC-UV** | ~0.01 mg/dL | 234 nm | Inject | Reference method |
| **IDMS** | <0.001 mg/dL | m/z | Extraction | Ultimate reference |
| **ATR-FTIR** | ~5 mM | 1492 cm⁻¹ | None/dry | Reagent-free |
| **Raman** | ~5 mM | 680, 1490 cm⁻¹ | None | Non-destructive |
| **SERS** | ~10–100 µM | 680 cm⁻¹ | Nanoparticles | Enhanced sensitivity |
| **Voltammetry (MIP)** | ~0.5 µM | +0.8–1.0 V | Buffer dilution | Sensitive, selective |
| **Fluorometric (Amplex)** | ~0.01 mg/dL | Ex 571/Em 585 nm | Enzyme cascade | Very sensitive |

---

## Sources

| # | Citation |
|---|---|
| 1 | Mayo Clinic — [[creatinin\|Creatinine]] Test. https://www.mayoclinic.org/tests-procedures/[[creatinin\|creatinine]]-test/about/pac-20384646 |
| 2 | Medscape — [[creatinin\|Creatinine]] Reference Ranges. https://emedicine.medscape.com/article/2054342-overview |
| 3 | StatPearls — Creatine Phosphokinase. https://www.ncbi.nlm.nih.gov/books/NBK546624/ |
| 4 | Rich & Sheringham (2017) — FTIR of [[urea]] and [[creatinin\|creatinine]] in urine. PMC5379246. |
| 5 | NIST SRM 967 — [[creatinin\|Creatinine]] in Frozen Human Serum (reference material). |
| 6 | PubChem — [[creatinin\|Creatinine]], CID 588. https://pubchem.ncbi.nlm.nih.gov/compound/588 |
| 7 | KDIGO 2012 — CKD Guidelines (eGFR equations). https://kdigo.org/ |

## Gaps

- NIR multivariate models for urinary [[creatinin|creatinine]] show LOD ~0.5 mg/dL but have not been validated across diverse patient populations and urine matrices.
- Raman/SERS measurements are confounded by other urinary analytes at similar concentrations ([[urea]], [[uric-acid|uric acid]]); multivariate deconvolution required.
- 10–15% tubular secretion means [[creatinin|creatinine]] clearance consistently overestimates true GFR; bias is larger in CKD.
- The Jaffe reaction remains widely used despite known interferences; standardisation to IDMS-traceable enzymatic methods is incomplete across labs.
