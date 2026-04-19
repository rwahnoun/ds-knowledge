---
title: Magnesium
aliases:
  - Magnesium
  - Mg
  - Mg2+
  - Urinary magnesium
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

# Magnesium

Magnesium is the second most abundant intracellular cation and the fourth most abundant cation in the body. It is an essential cofactor for >300 enzymatic reactions, including all ATP-dependent processes. Only ~1% of total body Mg is in ECF; ~60% is in bone, ~39% in soft tissue. Urinary Mg measurement helps differentiate renal from extrarenal causes of hypomagnesaemia. Mg²⁺ is not detectable by [[optical-properties|optical spectroscopy]] methods directly. See [[datascience/spectroscopy-biomarkers]] for trace mineral context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Magnesium |
| **Other names** | Mg, Mg²⁺ |
| **Chemical formula** | Mg²⁺ (divalent cation) |
| **Atomic weight** | 24.31 g/mol |
| **CAS number** | 7439-95-4 |
| **PubChem CID** | 5462224 |
| **Appearance** | Colourless in solution |

**Structural formula:**

```
  Mg(2+)   (divalent cation, hydrated in solution)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Calcium (Ca²⁺)** | Ca²⁺ | 40.08 | Larger divalent cation; different metabolic roles; often co-measured |
| **Potassium (K⁺)** | K⁺ | 39.10 | Monovalent; primary intracellular cation; different renal handling |

---

## Medical Information

### Origin

#### Endogenous

Magnesium is not synthesised. Total body Mg: ~24 g (~1000 mmol) in adults. Bone stores act as a reservoir. Released during bone resorption.

#### Exogenous

Dietary sources: green leafy vegetables (chlorophyll contains Mg), nuts, seeds, whole grains, legumes, dark chocolate, mineral water. Typical intake: 300–400 mg/day. Intestinal absorption: 30–50% (small intestine, primarily jejunum and ileum via TRPM6 channels). Mg supplements and antacids are additional sources.

### Primary & Secondary Biological Roles

**Primary role:**
- **Enzymatic cofactor:** Required for all kinases (ATP-Mg as true substrate), DNA/RNA polymerases, and >300 other enzymes.

**Secondary roles:**
- **Neuromuscular function:** Modulates calcium channels and NMDA receptors; deficiency causes hyperexcitability, tetany, and seizures.
- **Bone structure:** ~60% of body Mg is in bone mineral.
- **Cardiac rhythm:** Mg stabilises cardiac cell membranes; deficiency promotes arrhythmias.
- **Glucose metabolism:** Insulin signalling requires Mg.

### Catabolism and Elimination Pathway

- Mg freely filtered at glomerulus (~2400 mg/day, ~80% of plasma Mg is filterable).
- **~95–97%** reabsorbed: 15% proximal tubule, 70% thick ascending loop of Henle (paracellular via claudin-16/19), 10% distal convoluted tubule (TRPM6, fine-tuning).
- 3–5% excreted in urine (~100 mg/day).
- Minor losses: GI, sweat.

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Serum Mg** | 1.7–2.2 mg/dL (0.70–0.95 mmol/L) |
| **Urinary Mg (24-h)** | 73–122 mg/day (3–5 mmol/day) |
| **Urinary Mg (spot)** | Variable; FEMg <4% normally |

#### Factors Influencing Levels

**Increased urinary Mg:**
- Diuretics (loop >> thiazide)
- Alcohol excess
- Diabetic ketoacidosis (osmotic diuresis)
- Cisplatin, aminoglycosides, amphotericin B (nephrotoxic)
- Gitelman syndrome, Bartter syndrome
- Hypercalcaemia (Ca competes for reabsorption)
- IV Mg administration

**Decreased urinary Mg:**
- Low Mg intake
- GI Mg losses (diarrhoea, malabsorption)
- Appropriate renal conservation in extrarenal hypomagnesaemia (FEMg <2%)
- Familial hypomagnesaemia with hypocalciuria

#### Associated Pathologies

| Condition | Mg Pattern | Key Symptoms |
|---|---|---|
| **Renal Mg wasting** | High urinary Mg (FEMg >4%), low serum Mg | Tetany, arrhythmias, seizures |
| **GI Mg loss** | Low urinary Mg (FEMg <2%), low serum Mg | Diarrhoea, malabsorption, cramps |
| **Alcoholism** | High urinary Mg + poor intake | Tremor, seizures, Wernicke |
| **Drug-induced (PPI, cisplatin)** | Variable urinary Mg | Muscle weakness, cramps |

### Presence in Urine

**Should it be normally present?** **Yes** — urinary Mg excretion is the primary regulatory mechanism. Normal: 3–5 mmol/day.

**Normal urinary levels:** 73–122 mg/day (3–5 mmol/day).

**Form in urine:** **Mg²⁺ ion**, hydrated. May complex with phosphate (struvite: MgNH₄PO₄) in infected alkaline urine.

**Pathological significance:**

| Urinary Mg | Possible Causes | Prevalence |
|---|---|---|
| **High (>5 mmol/day)** | Renal Mg wasting, drugs, DKA | Common with diuretics |
| **Low (<3 mmol/day)** | Extrarenal loss, low intake, renal conservation | Common |

**Solubility:** MgCl₂ and MgSO₄ are very soluble. MgNH₄PO₄ (struvite) is poorly soluble in alkaline conditions and can form stones.

---

## Detection in Urine

### Available Clinical Assays

1. **Colorimetric (xylidyl blue / calmagite):**
   - **Principle:** Mg²⁺ reacts with calmagite or xylidyl blue in alkaline pH → blue-violet complex.
   - **Detection:** Absorbance at **520–550 nm**.
   - **LOD:** ~0.1 mg/dL (~0.04 mmol/L).
   - **Advantages:** Automated, standard on clinical platforms.

2. **Atomic absorption spectroscopy (AAS, reference):**
   - **Principle:** Mg atoms in flame absorb **285.2 nm** light.
   - **Detection:** Absorption at **285.2 nm**.
   - **LOD:** ~0.001 mg/dL.
   - **Advantages:** Highly specific; reference method.

3. **Ion-selective electrode:**
   - **Principle:** Mg²⁺-selective ionophore membrane (ETH 7025 or similar).
   - **Detection:** Potentiometric.
   - **LOD:** ~0.1 mmol/L. Less common than for Na/K.

### Optimal Urine Type for Measurement

- **24-hour urine** for total excretion assessment.
- Spot urine for FEMg calculation (with serum Mg and creatinine).
- Acidify with HCl to prevent Mg salt precipitation.
- Refrigerate.

### Actual Gold Standard

**Flame AAS at 285.2 nm** is the reference method. Colorimetric methods (calmagite/xylidyl blue) on automated platforms are the standard clinical assay. CV: 3–5%.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Calcium (high)** | Positive bias (colorimetric) | Ca also reacts with dyes; EGTA chelation masks Ca |
| **Haemolysis** | Positive bias | Intracellular Mg release |
| **EDTA contamination** | Negative bias | Chelates Mg |
| **Lipaemia** | Positive bias | Light scattering |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- **AAS at 285.2 nm:** Reference method. LOD: ~0.001 mg/dL.
- **ICP-OES at 279.6 nm or 285.2 nm:** Multi-element. LOD: ~0.0001 mg/dL.
- **Colorimetric (calmagite, 520 nm):** See clinical assays.
- **NIR:** No useful Mg²⁺ absorption.

#### Fluorescence Detection

- **Mag-Fura-2 (furaptra):** Ratiometric Mg probe. Ex 340/380 nm, Em 510 nm. Kd ~1.5 mM. LOD: ~0.1 mM.
- **Mag-Indo-1:** Ex 349 nm, Em 390/480 nm. LOD: ~0.1 mM.
- **Mag-Fluo-4:** Ex 493 / Em 516 nm. Single wavelength. LOD: ~0.5 mM.
- Originally designed for intracellular Mg imaging; applicable to urine with calibration.

#### Raman Detection

Mg²⁺ (monatomic ion) has no Raman-active modes. Not detectable.

#### FTIR Detection

Mg²⁺ has no IR absorption. Not detectable by FTIR.

#### Voltammetry Detection

- Mg²⁺ cannot be reduced in aqueous media (E0 = -2.37 V vs SHE).
- **Potentiometric ISE** with Mg-selective ionophore is the main electrochemical approach.
- **Anodic stripping voltammetry** not applicable (too negative reduction potential).

### Other Detection Technologies

1. **ICP-MS:** LOD ~0.00001 mg/dL. Multi-element, ultimate sensitivity.
2. **Flame emission photometry:** Mg emission at 285 nm. Less common than AAS.
3. **Paper-based colorimetric:** Calmagite-impregnated strips. LOD: ~0.5 mmol/L.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Colorimetric (calmagite)** | ~0.04 mmol/L | 520–550 nm | None | Standard, automated |
| **Flame AAS** | ~0.001 mg/dL | 285.2 nm | Dilution | Reference, specific |
| **ICP-OES** | ~0.0001 mg/dL | 279.6 nm | Dilution | Multi-element |
| **Mag-Fura-2 fluorescence** | ~0.1 mM | Ex 340–380/Em 510 nm | Probe addition | Ratiometric |
| **ISE** | ~0.1 mmol/L | Potentiometric | None | Real-time |
| **Raman / FTIR** | N/A | N/A | N/A | Not applicable |

---

## Sources

| # | Citation |
|---|---|
| 1 | PMC — Interpreting Magnesium Status. https://ncbi.nlm.nih.gov/pmc/articles/PMC5812344/ |
| 2 | Mayo Clinic Labs — 24-h Urine Magnesium. https://www.mayocliniclabs.com/ |
| 3 | ACS Anal Chem (1961) — Ca and Mg in Urine by AAS. https://pubs.acs.org/doi/abs/10.1021/ac60172a021 |
| 4 | JCP — Ca and Mg by AAS in serum and urine. https://jcp.bmj.com/content/20/3/280 |
| 5 | StatPearls — Hypomagnesaemia. https://www.ncbi.nlm.nih.gov/books/NBK500003/ |

## Gaps

- No optical or Raman/FTIR method is applicable for Mg²⁺ detection in urine; all viable approaches are electrochemical or atomic spectroscopic.
- Fluorescent Mg probes (Mag-Fura-2) have not been validated at clinical urinary concentrations with adequate selectivity over Ca²⁺, Zn²⁺, and other cations.
- Spot urine FEMg thresholds (<2% vs >4%) for renal vs extrarenal wasting have not been validated in large prospective studies across diverse patient populations.
- Struvite stone formation risk prediction from urinary Mg levels alone is insufficient; co-measurement with ammonium and phosphate is required.
