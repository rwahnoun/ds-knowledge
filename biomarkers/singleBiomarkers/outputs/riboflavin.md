---
title: Riboflavin
aliases:
  - Vitamin B2
  - Lactoflavin
  - E101
  - B2
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

# Riboflavin

The dominant fluorescent compound in human urine (Ex 450 / Em 525 nm). Its bright yellow-green autofluorescence must be accounted for in any fluorescence-based urine analysis. See [[optical-properties]], [[signatures]], and [[datascience/spectroscopy-biomarkers]] for urine fluorescence context.

> [!IMPORTANT]
> Riboflavin is the primary contributor to urine autofluorescence at 450/525 nm. Any fluorescence measurement in urine must consider riboflavin as a potential interferent or co-analyte.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Riboflavin |
| **Other names** | Vitamin B2, lactoflavin, E101 |
| **Chemical formula** | C₁₇H₂₀N₄O₆ |
| **Molecular weight** | 376.36 g/mol |
| **CAS number** | 83-88-5 |
| **PubChem CID** | 493570 |
| **Appearance** | Yellow-orange crystalline powder |
| **Solubility** | ~100–130 mg/L at 25 °C (more soluble at alkaline pH) |
| **Melting point** | 290 °C (decomposes) |

Riboflavin is a water-soluble B vitamin and the direct precursor of FMN and FAD, the essential flavin coenzymes. It is one of the **most intensely fluorescent** natural compounds (Ex 450 nm / Em 525 nm, quantum yield ~25%), making it the dominant contributor to the yellow-green autofluorescence of urine. Excess riboflavin is rapidly excreted in urine.

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **FMN** | C₁₇H₂₁N₄O₉P | 456.34 | Phosphorylated riboflavin; similar fluorescence |
| **FAD** | C₂₇H₃₃N₉O₁₅P₂ | 785.55 | Adenylated FMN; lower quantum yield (quenched by adenine) |
| **Lumiflavin** | C₁₃H₁₂N₄O₂ | 256.26 | Photodegradation product; slightly different fluorescence |
| **Lumichrome** | C₁₂H₁₀N₄O₂ | 242.23 | Another photodegradation product |

---

## Medical Information

### Origin

**Endogenous:** Cannot be synthesised by humans — **essential vitamin** obtained from diet. Some production by intestinal bacteria, but colon absorption is minimal.

**Exogenous:** Dairy products (major source), eggs, lean meats, green leafy vegetables, fortified cereals and breads. RDA: 1.1 mg/day (women), 1.3 mg/day (men). Supplements often contain 25–100 mg.

### Biological Roles

- **Primary:** Coenzyme precursor. Converted to FMN and FAD, required by ~75 flavoproteins for redox reactions in energy metabolism, fatty acid oxidation, drug metabolism, and antioxidant defence (glutathione reductase).
- **Antioxidant:** Via glutathione reductase (FAD-dependent).
- **Migraine prophylaxis:** High-dose riboflavin (400 mg/day) reduces migraine frequency.

### Elimination Pathway

Absorbed in small intestine via RFVT transporter. Converted to FMN and FAD in cells. Excess free riboflavin and metabolites (7-alpha-hydroxyriboflavin, lumiflavin) excreted in urine. **Renal excretion** is the primary route; both glomerular filtration and active tubular secretion contribute. Urinary riboflavin increases proportionally with intake above tissue saturation.

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Plasma riboflavin** | 5–50 nmol/L (highly variable with intake) |
| **Erythrocyte FAD** | 300–600 nmol/L |
| **Urinary riboflavin (24-h)** | 120–400 µg/day at RDA intake; can exceed >10 mg/day with supplements |
| **EGRac (functional test)** | <1.2 normal; 1.2–1.4 marginal; >1.4 deficient |

### Factors Influencing Levels

**Increased urinary riboflavin:** High dietary intake or supplementation (bright yellow urine), energy drinks, B-complex vitamins, tissue catabolism.

**Decreased urinary riboflavin:** Riboflavin deficiency, malabsorption (celiac, IBD), alcoholism, hypothyroidism, pregnancy.

### Associated Pathologies

| Condition | Riboflavin Pattern | Key Symptoms |
|---|---|---|
| **Ariboflavinosis** | Low urinary riboflavin, high EGRac | Angular cheilitis, glossitis, seborrhoeic dermatitis, normocytic anaemia |
| **MADD (riboflavin-responsive)** | Low flavin levels | Hypoglycaemia, metabolic acidosis, myopathy |

### Presence in Urine

Normally present. The **primary yellow-green fluorescent compound** in urine. Normal excretion 120–400 µg/day. Form: free **riboflavin** molecule; minor metabolites: 7-alpha-hydroxyriboflavin, lumiflavin. Solubility ~100–130 mg/L; urinary concentrations typically well below saturation.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **HPLC-fluorescence (gold standard)** | C18 RP-HPLC separates riboflavin from FMN and FAD | Ex 450 / Em 520–525 nm | ~1–5 nmol/L | Specific; protect from light |
| **Microbiological assay (L. rhamnosus)** | Bacterial growth proportional to riboflavin | OD 600 nm | ~1 nmol/L | Slow, labour-intensive; historical |

Gold standard: **HPLC-fluorescence** (Ex 450 / Em 520 nm). EGRac for functional B2 status.

Optimal specimen: **24-hour urine** for total excretion. **Protect from light** (photolysis to lumiflavin/lumichrome). Store at −20 °C.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Light** | Degradation | Photolysis to lumiflavin/lumichrome |
| **FMN/FAD** | Spectral overlap | Same isoalloxazine fluorophore |
| **Tetracyclines** | Fluorescence quenching | Complexation |
| **Metal ions (Cu²⁺, Fe³⁺)** | Quenching | Heavy metal quenching |

### Spectroscopic Detection

**UV-Vis:** Riboflavin absorbs at **223, 267, 373, and 450 nm** (the 450 nm band, ε ~11,300 M⁻¹cm⁻¹, gives the yellow colour). LOD ~0.1 µM direct.

**Fluorescence:** Direct fluorescence at **Ex 450 / Em 525 nm**. LOD ~1 nM. Quantum yield ~25%. EEM fluorescence with chemometrics resolves riboflavin from FAD and other fluorophores (LOD ~5 nM). Time-resolved: riboflavin lifetime ~4.7 ns (vs FAD ~2.3 ns). Sample prep: dilution; protect from light.

**Raman:** Key peaks: ~1350 cm⁻¹ (CN stretch, isoalloxazine), ~1500 cm⁻¹ (C=N), ~1580 cm⁻¹ (C=C), ~1630 cm⁻¹ (C=O). Resonance Raman with Ex 458–514 nm enhances isoalloxazine peaks; LOD ~0.1–1 µM. SERS with Ag substrates: LOD ~1 nM.

**FTIR:** Isoalloxazine bands at 1650, 1580, 1540 cm⁻¹. Not practical for urinary concentrations.

**Voltammetry:** Reversible 2e⁻/2H⁺ reduction at ~−0.4 to −0.5 V vs Ag/AgCl (pH 7). LOD ~10 nM on modified electrodes (graphene, CNTs).

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **HPLC-fluorescence** | ~1 nM | Ex 450 / Em 520 nm | None | Gold standard |
| **Direct fluorescence** | ~1 nM | Ex 450 / Em 525 nm | None | Simple, fast |
| **UV-Vis** | ~0.1 µM | 450 nm | None | Direct |
| **Resonance Raman** | ~0.1 µM | Ex 458 nm | None | Specific |
| **SERS** | ~1 nM | 1350 cm⁻¹ | Ag NPs | Sensitive |
| **Voltammetry** | ~10 nM | −0.5 V | Buffer | Electrochemical |
| **LC-MS/MS** | ~0.1 nM | m/z 377→243 | Extraction | Definitive |

---

## Sources

| # | Reference |
|---|---|
| 1 | ScienceDirect — Riboflavin fluorescence in urine. https://www.sciencedirect.com/science/article/abs/pii/S0026265X16303721 |
| 2 | LWW JASN — Riboflavin Excretion as Tubular Secretion Biomarker. https://journals.lww.com/jasn/fulltext/2022/11001/riboflavin_excretion_as_a_functional_biomarker_of.3205.aspx |
| 3 | JCI — Urinary Excretion of Riboflavin. http://www.jci.org/articles/view/101118/files/pdf |
| 4 | PubChem — Riboflavin, CID 493570. https://pubchem.ncbi.nlm.nih.gov/compound/493570 |

---

## Gaps

- Riboflavin is a major interferent in EEM/fluorescence-based urinary analysis; spectral deconvolution from FAD, FMN, NADH, and tryptophan requires validated chemometric models
- Day-to-day variation from supplement use is high and unpredictable; needs normalisation strategy
- Riboflavin as a tubular secretion biomarker is an emerging application (JASN 2022) requiring further clinical validation
- No validated correction algorithm for riboflavin interference in multi-analyte urine fluorescence platforms
