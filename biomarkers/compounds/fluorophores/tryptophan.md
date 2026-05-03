---
title: Tryptophan
aliases:
  - L-Tryptophan
  - Trp
  - W
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - class/amino-acid
  - clinical/oncology
  - clinical/nutrition
  - modality/fluorescence
  - modality/uv
  - presence/trace
  - subclass/aromatic
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
clinical-use:
  - oncology
  - nutrition
detection-modality:
  - fluorescence
  - uv
class: amino-acid
subclass: aromatic
presence: trace
parent: "[[biomarkers/compounds/fluorophores/index|fluorophores]]"
---
# [[tryptophan|Tryptophan]]

Essential aromatic amino acid with the dominant protein fluorescence signal at Ex 280 / Em 348 nm. In urine, [[tryptophan]] and its metabolites serve as markers of protein metabolism, gut microbiome activity, and renal function. The indole ring gives it unique Raman and fluorescence signatures. See [[optical-properties]], [[signatures]], and [[datascience/spectroscopy-biomarkers]] for spectral reference.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | [[tryptophan\|Tryptophan]] |
| **Other names** | L-[[tryptophan\|Tryptophan]], Trp, W |
| **Chemical formula** | C₁₁H₁₂N₂O₂ |
| **Molecular weight** | 204.23 g/mol |
| **CAS number** | 73-22-3 |
| **PubChem CID** | 6305 |
| **Appearance** | White crystalline powder |
| **pKa** | 2.38 (COOH), 9.39 (NH₃⁺) |
| **Solubility** | ~11.4 g/L at 25 °C |

[[tryptophan|Tryptophan]] is an essential aromatic amino acid and the only amino acid with an **indole ring**, giving it unique fluorescence properties (Ex 280 nm / Em 348 nm). It is a precursor to serotonin, melatonin, niacin (vitamin B3), and kynurenine. Its intrinsic fluorescence makes it the dominant fluorophore in protein UV fluorescence. In urine, [[tryptophan]] and its metabolites (indoxyl sulfate, kynurenine, indole-3-acetic acid) serve as markers of protein metabolism, gut microbiome activity, and various diseases.

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Serotonin (5-HT)** | C₁₀H₁₂N₂O | 176.21 | [[tryptophan\|Tryptophan]] metabolite; neurotransmitter |
| **Kynurenine** | C₁₀H₁₂N₂O₃ | 208.21 | Major [[tryptophan]] metabolite via IDO/TDO pathway |
| **Indoxyl sulfate** | C₈H₆NO₄S⁻ | 212.20 | Gut bacterial metabolite; uraemic toxin |
| **5-HIAA** | C₁₁H₁₁NO₃ | 191.18 | Serotonin metabolite; elevated in carcinoid tumours |
| **Tyrosine** | C₉H₁₁NO₃ | 181.19 | Another aromatic amino acid; Ex 275 / Em 303 nm |

---

## Medical Information

### Origin

**Endogenous:** Essential amino acid — must be obtained from diet. The least abundant amino acid in the body. Metabolised via three main pathways:
1. **Kynurenine pathway** (~95%): Trp → kynurenine → quinolinic acid → NAD⁺. Key enzymes: IDO (immune-activated), TDO (liver).
2. **Serotonin pathway** (~1–2%): Trp → 5-HTP → serotonin → melatonin.
3. **Gut microbial pathway** (~4–6%): Trp → indole → indoxyl → indoxyl sulfate (liver conjugation).

**Exogenous:** Turkey, chicken, milk, cheese, eggs, fish, nuts, seeds, tofu, chocolate. RDA: ~250–425 mg/day.

### Biological Roles

- **Protein synthesis:** Essential amino acid for all proteins.
- **NAD⁺ precursor:** Via kynurenine pathway (niacin equivalent).
- **Serotonin/melatonin precursor:** Neurotransmitter and sleep hormone synthesis.
- **Immune modulation:** IDO-mediated [[tryptophan]] depletion regulates T-cell responses.
- **Gut-brain axis:** Microbial [[tryptophan]] metabolites (indoles) signal via AhR receptor.
- **Autofluorescence marker:** Dominant protein fluorophore at 280/348 nm.

### Elimination Pathway

~95% via kynurenine pathway. ~1–2% to serotonin. ~4–6% by gut [[bacteria]]. Urinary excretion: Trp itself (<50 mg/day) plus metabolites (kynurenine, kynurenic acid, xanthurenic acid, quinolinic acid, 5-HIAA, indoxyl sulfate). Free [[tryptophan]] is filtered and ~98% reabsorbed via neutral amino acid transporter.

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Plasma [[tryptophan]] (total)** | 50–80 µmol/L |
| **Plasma [[tryptophan]] (free)** | 5–15 µmol/L (~10% of total; rest albumin-bound) |
| **Urinary [[tryptophan]]** | <50 mg/day (~245 µmol/day) |
| **Urinary 5-HIAA** | 2–8 mg/day |

### Factors Influencing Levels

**Increased urinary [[tryptophan]]:** Hartnup disease (defective neutral amino acid transporter), [[tryptophan]] supplements, Fanconi syndrome.

**Decreased urinary [[tryptophan]]:** Low protein diet, increased IDO activity (infection, inflammation, cancer), vitamin B6 deficiency.

### Associated Pathologies

| Condition | [[tryptophan\|Tryptophan]] Pattern | Key Symptoms |
|---|---|---|
| **Hartnup disease** | Massive tryptophanuria + other neutral aminoacids | Pellagra-like rash, cerebellar ataxia; autosomal recessive |
| **Carcinoid syndrome** | Low plasma Trp (diverted to serotonin); high 5-HIAA | Flushing, diarrhoea, wheezing; ~2/100,000 |
| **CKD (uraemia)** | Elevated indoxyl sulfate (Trp metabolite) | Cardiovascular toxicity, CKD progression |
| **Depression** | Low plasma free Trp | Mood disorders (serotonin depletion hypothesis) |

### Presence in Urine

Small amounts normally (<50 mg/day free Trp). Metabolites (kynurenine, indoxyl sulfate, 5-HIAA) also normally excreted. Form: free **L-[[tryptophan]]** (zwitterionic at urine pH). Solubility ~11.4 g/L; no crystallisation issues.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **HPLC-fluorescence (gold standard)** | RP-C18 HPLC; direct indole fluorescence | Ex 280 / Em 348 nm | ~0.05 µmol/L | Specific; separates Trp from metabolites |
| **Amino acid analyser** | Ion-exchange + post-column ninhydrin | 570 nm (primary amines) | ~1 µmol/L | Full amino acid panel |
| **LC-MS/MS** | RP-HPLC + tandem MS | m/z 205→188 | ~0.01 µmol/L | Definitive; multiplex with metabolites |

Gold standard: **HPLC-fluorescence** (Ex 280 / Em 348 nm) or LC-MS/MS.

Optimal specimen: **24-hour urine** acidified with HCl (stabilises amino acids). Freeze at −20 °C if delayed.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Protein fluorescence** | Spectral overlap | [[tryptophan\|Tryptophan]] residues in urinary proteins |
| **Tyrosine** | Partial spectral overlap | Ex 275 / Em 303 nm |
| **Bacterial metabolism** | Decreased Trp | [[bacteria\|Bacteria]] convert Trp to indole |
| **Light** | Photodegradation | Indole ring photosensitive |

### Spectroscopic Detection

**UV-Vis:** [[tryptophan|Tryptophan]] absorbs at **280 nm** (ε ~5,500 M⁻¹cm⁻¹, indole ring) and 220 nm. LOD ~5 µmol/L by direct UV; interfered by proteins in urine.

**Fluorescence:** Intrinsic indole fluorescence at **Ex 280 nm / Em 348 nm** is [[tryptophan]]'s defining optical property. Quantum yield ~13% (free in water). LOD ~0.05 µmol/L in clean solutions; ~1–5 µmol/L in urine (matrix interference). EEM fluorescence with chemometrics resolves Trp from tyrosine, [[nadh|NADH]], and riboflavin (LOD ~1 µmol/L). FLIM: Trp lifetime ~3.1 ns (free).

**Raman:** Key peaks:

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~760** | Indole ring breathing |
| **~880** | Indole N-H deformation |
| **~1340** | Fermi resonance doublet |
| **~1550** | Indole C=C stretch (W3 mode) |
| **~1620** | Indole ring |

Resonance Raman (Ex 229 nm deep UV) selectively enhances aromatic amino acid modes; LOD ~10 µmol/L. SERS: LOD ~0.1–1 µmol/L with Ag substrates.

**FTIR:** Bands at ~1660 cm⁻¹ (C=O), ~1580 cm⁻¹ (indole C=C), ~740 cm⁻¹ (indole ring, more specific). Not practical for urinary Trp at typical concentrations.

**Voltammetry:** [[tryptophan|Tryptophan]] indole ring oxidised at **+0.7–0.9 V vs Ag/AgCl** on carbon electrodes. LOD ~0.1–1 µmol/L on modified electrodes (graphene, MIPs, BDD). Interference from [[uric-acid|uric acid]] and ascorbic acid; DPV provides best selectivity.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **HPLC-fluorescence** | ~0.05 µmol/L | Ex 280 / Em 348 nm | None | Gold standard |
| **LC-MS/MS** | ~0.01 µmol/L | m/z 205→188 | Extraction | Definitive, metabolite panel |
| **Direct fluorescence** | ~1–5 µmol/L | Ex 280 / Em 348 nm | Dilution | Simple |
| **UV Raman (229 nm)** | ~10 µmol/L | 760+1550 cm⁻¹ | None | Amino acid-specific |
| **SERS** | ~0.1 µmol/L | 760 cm⁻¹ | Ag NPs | Ultra-sensitive |
| **DPV** | ~0.1 µmol/L | +0.8 V | Buffer | Real-time |
| **CE-LIF** | ~0.01 µmol/L | Ex 266 nm | None | Separation + detection |

---

## Sources

| # | Reference |
|---|---|
| 1 | PubChem — L-[[tryptophan\|Tryptophan]], CID 6305. https://pubchem.ncbi.nlm.nih.gov/compound/6305 |
| 2 | StatPearls — Hartnup Disease. https://www.ncbi.nlm.nih.gov/books/NBK482220/ |
| 3 | StatPearls — Carcinoid Syndrome. https://www.ncbi.nlm.nih.gov/books/NBK448096/ |
| 4 | PMC — [[tryptophan\|Tryptophan]] metabolism in health and disease (kynurenine pathway) |

---

## Gaps

- EEM-based [[tryptophan]] quantification in complex urine requires spectral deconvolution from riboflavin, [[nadh|NADH]], tyrosine, and urinary proteins
- Indoxyl sulfate (uraemic toxin and key Trp metabolite) is a separate biomarker with distinct optical properties not yet characterised in full [[tryptophan]] metabolite panel
- 5-HIAA (carcinoid marker) requires separate 24-h urine test; no combined Trp/5-HIAA spectroscopic assay validated
- Deep UV Raman (229 nm) is not compatible with standard Raman platforms

[tryptophan|Tryptophan]: tryptophan.md "Tryptophan"
[tryptophan]: tryptophan.md "Tryptophan"
[datascience/spectroscopy-biomarkers]: ../../../../../datascience/spectroscopy-biomarkers.md "Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices"
[tryptophan\|Tryptophan]: tryptophan.md "Tryptophan"
[bacteria]: ../infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[bacteria\|Bacteria]: ../infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[nadh|NADH]: nadh.md "NADH (Reduced Nicotinamide Adenine Dinucleotide)"
[uric-acid|uric acid]: ../metabolites/uric-acid.md "Uric Acid"
