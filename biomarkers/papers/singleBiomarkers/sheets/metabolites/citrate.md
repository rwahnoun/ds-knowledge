---
title: Citrate
aliases:
  - Citrate
  - Citric acid
  - Urinary citrate
  - Hypocitraturia
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---# Citrate

Citrate is a key intermediate in the TCA (Krebs) cycle and the most important **endogenous inhibitor of calcium stone formation** in urine. It chelates calcium, reduces CaOx and CaPO₄ supersaturation, and directly inhibits crystal growth and aggregation. Hypocitraturia is a major risk factor for nephrolithiasis. See [[datascience/spectroscopy-biomarkers]] for broader urinary analyte context.

***

## Identity Sheet

| Property             | Value                                                               |
| -------------------- | ------------------------------------------------------------------- |
| **Name**             | Citrate                                                             |
| **Other names**      | Citric acid (protonated), 2-hydroxypropane-1,2,3-tricarboxylic acid |
| **Chemical formula** | C₆H₈O₇ (acid); C₆H₅O₇³⁻ (trianion)                                  |
| **Molecular weight** | 192.12 g/mol                                                        |
| **CAS number**       | 77-92-9                                                             |
| **PubChem CID**      | 311                                                                 |
| **pKa values**       | pKa1=3.13, pKa2=4.76, pKa3=6.40                                     |
| **Solubility**       | Very soluble (~590 g/L at 20 °C for citric acid)                    |

**Structural formula:**

```text
  HOOC-CH2-C(OH)(COOH)-CH2-COOH
       (tricarboxylic acid with central hydroxyl)
```

### Molecules Not to Be Confused With

| Molecule       | Formula | MW (g/mol) | Key Difference                                    |
| -------------- | ------- | ---------- | ------------------------------------------------- |
| **Oxalate**    | C₂O₄²⁻  | 88.02      | Stone promoter (opposite role); forms CaOx stones |
| **Isocitrate** | C₆H₈O₇  | 192.12     | TCA cycle isomer; different biological role       |
| **Malate**     | C₄H₆O₅  | 134.09     | Another TCA intermediate; dicarboxylic acid       |

***

## Medical Information

### Origin

#### Endogenous: TCA Cycle

Citrate is synthesised in mitochondria by citrate synthase (acetyl-CoA + oxaloacetate → citrate). It is a central metabolite in the TCA cycle. Plasma citrate: ~100 µmol/L. Most urinary citrate derives from plasma filtration and tubular handling.

#### Exogenous

Dietary citrate from citrus fruits (lemons, oranges, grapefruit), berries, tomatoes. Potassium citrate supplements used therapeutically for stone prevention.

### Primary & Secondary Biological Roles

**Primary role:**

- **TCA cycle intermediate:** Central to aerobic energy metabolism.
- **Urinary stone inhibitor:** Chelates Ca²⁺ in urine, reducing CaOx and CaPO₄ supersaturation.

**Secondary roles:**

- **Fatty acid synthesis precursor:** Cytoplasmic citrate is cleaved by ATP-citrate lyase to oxaloacetate + acetyl-CoA (lipogenesis).
- **Acid-base metabolism:** Citrate is metabolised to HCO₃⁻; its excretion represents alkali loss.

### Catabolism and Elimination Pathway

- Citrate is freely filtered at glomerulus.
- ~65–90% reabsorbed in proximal tubule via NaDC-1 transporter ([[sodium]]-dicarboxylate cotransporter).
- Reabsorption is **increased by acidosis** (reduces urinary citrate — hypocitraturia).
- Reabsorption is **decreased by alkalosis** (increases urinary citrate).
- Remaining 10–35% excreted in urine.

### Expression in Humans

#### Normal Levels

| Compartment                  | Reference Range                        |
| ---------------------------- | -------------------------------------- |
| **Serum citrate**            | 50–130 µmol/L                          |
| **Urinary citrate (24-h)**   | Male: >250 mg/day; Female: >300 mg/day |
| **Hypocitraturia threshold** | Male: <250 mg/day; Female: <300 mg/day |

#### Factors Influencing Levels

**Hypocitraturia:**

- Metabolic acidosis (most common cause, including distal RTA)
- Chronic diarrhoea (alkali loss)
- High animal protein diet
- Hypokalaemia
- UTI ([[bacteria]] consume citrate)
- Acetazolamide
- Idiopathic (up to 40% of stone formers)

**Increased citrate:**

- Alkalosis
- Potassium citrate supplementation
- High fruit/vegetable diet
- Oestrogen (women have higher citrate than men)

#### Associated Pathologies

| Condition                            | Citrate Pattern                   | Key Symptoms                                          |
| ------------------------------------ | --------------------------------- | ----------------------------------------------------- |
| **Hypocitraturia + nephrolithiasis** | <250 mg/day (male)                | Recurrent CaOx/CaPO₄ stones; ~20–60% of stone formers |
| **Distal RTA**                       | Very low citrate + alkaline urine | CaPO₄ stones, nephrocalcinosis, metabolic acidosis    |
| **Chronic diarrhoea**                | Low citrate (metabolic acidosis)  | Dehydration, stone risk                               |

### Presence in Urine

**Should it be normally present?** **Yes** — citrate is a normal and important urinary solute.

**Normal urinary levels:** >250 mg/day (men); >300 mg/day (women).

**Form in urine:** At urinary pH 5–7, citrate exists as a mixture of **Hcit²⁻** and **cit³⁻** anions. These chelate Ca²⁺, forming soluble calcium-citrate complexes.

**Solubility:** Citric acid and its [[sodium]]/potassium salts are highly soluble. Calcium citrate is moderately soluble (~850 mg/L) — much more so than calcium oxalate.

***

## Detection in Urine

### Available Clinical Assays

1. **Citrate lyase enzymatic assay:**
   - **Principle:** Citrate lyase cleaves citrate → oxaloacetate + acetate. OAA + [[nadh|NADH]] (MDH) → malate + NAD⁺. [[nadh|NADH]] consumption measured.
   - **Detection:** Absorbance decrease at **340 nm**.
   - **LOD:** ~0.5 mg/dL (~25 µmol/L).
   - **Advantages:** Specific, automated (Roche, Beckman).
2. **Ion chromatography:**
   - **Principle:** Anion exchange + conductivity.
   - **LOD:** ~1 µmol/L.
3. **Capillary electrophoresis:**
   - **Principle:** Electrophoretic separation + UV at 210 nm.
   - **LOD:** ~5 µmol/L.

### Optimal Urine Type for Measurement

- **24-hour urine** for stone metabolic workup.
- No special preservatives needed (citrate is stable).
- Refrigerate during collection.
- Report as mg/day or mmol/day.

### Actual Gold Standard

**Citrate lyase enzymatic assay** ([[nadh|NADH]] at 340 nm) on automated platforms. CV: 3–5%.

### Interferences in Measurement

| Interference                | Effect                      | Mechanism                                       |
| --------------------------- | --------------------------- | ----------------------------------------------- |
| **Fluorocitrate**           | Inhibition of citrate lyase | Rare; from fluoroacetate poisoning              |
| **Bacterial contamination** | Falsely low                 | ‹WIKILINK:bacteria|Bacteria› metabolise citrate |
| **Very low pH**             | Affects enzyme activity     | Assay requires buffered conditions              |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- Citrate has weak UV absorption (<210 nm). Not practical for direct UV detection in urine.
- Enzymatic [[nadh|NADH]] consumption at 340 nm (see above).
- NIR: Citrate has C-H/C-O overtones but too low concentration for direct NIR.

#### Fluorescence Detection

- Citrate is non-fluorescent. Indirect:
- [[nadh|NADH]] **consumption fluorescence:** Decrease in [[nadh|NADH]] fluorescence (Ex 340 / Em 460 nm) after citrate lyase + MDH. LOD: ~10 µmol/L.
- **Eu(III) or Tb(III) complexes:** Citrate enhances lanthanide fluorescence via antenna effect. Ex 278 / Em 545 nm (Tb). LOD: ~1 µmol/L.

#### Raman Detection

| Peak (cm⁻¹) | Assignment              |
| ----------- | ----------------------- |
| **~840**    | C-C stretch             |
| **~960**    | C-OH stretch            |
| **~1390**   | COO⁻ symmetric stretch  |
| **~1580**   | COO⁻ asymmetric stretch |

- Conventional Raman: LOD ~10 mM. SERS: LOD ~10–100 µmol/L.

#### FTIR Detection

| Band (cm⁻¹) | Assignment              | Notes                                   |
| ----------- | ----------------------- | --------------------------------------- |
| **~1580**   | COO⁻ asymmetric stretch | Overlaps with ‹WIKILINK:urea›, proteins |
| **~1390**   | COO⁻ symmetric stretch  | More specific                           |
| **~1080**   | C-O stretch             | —                                       |

- ATR-FTIR: LOD ~5–10 mM. Marginal for urinary concentrations.

#### Voltammetry Detection

- Citrate is electrochemically inert in the normal potential window.
- **Indirect:** Citrate complexes Cu²⁺ or Fe³⁺ → shifts their redox potentials. LOD: ~10–50 µmol/L.
- **Potentiometric membrane electrode:** Citrate-selective ionophore. LOD: ~1 µmol/L.

### Other Detection Technologies

1. **LC-MS/MS:** LOD ~0.1 µmol/L. Definitive.
2. **Biosensor (citrate lyase on electrode):** Amperometric [[nadh|NADH]] detection. LOD: ~5 µmol/L.

***

## Detection Methods Comparison

| Method                                 | LOD         | Key Parameter    | Sample Prep | Strengths         |
| -------------------------------------- | ----------- | ---------------- | ----------- | ----------------- |
| **Citrate lyase/‹WIKILINK:nadh|NADH›** | ~25 µmol/L  | 340 nm           | None        | Standard clinical |
| **Ion chromatography**                 | ~1 µmol/L   | Conductivity     | Dilution    | Multi-anion       |
| **Tb(III) fluorescence**               | ~1 µmol/L   | Ex 278/Em 545 nm | Probe       | Sensitive         |
| **SERS**                               | ~10 µmol/L  | 1390 cm⁻¹        | Ag NPs      | Label-free        |
| **LC-MS/MS**                           | ~0.1 µmol/L | m/z 191→111      | Extraction  | Definitive        |

***

## Sources

| # | Citation                                                                        |
| - | ------------------------------------------------------------------------------- |
| 1 | StatPearls — Nephrolithiasis. <https://www.ncbi.nlm.nih.gov/books/NBK442014/>   |
| 2 | AUA/EAU Guidelines — Metabolic Stone Workup.                                    |
| 3 | PubChem — Citric acid, CID 311. <https://pubchem.ncbi.nlm.nih.gov/compound/311> |

## Gaps

- Raman/SERS quantification of citrate in urine matrix at clinical concentrations (sub-mM) has not been validated in patient cohorts.
- Direct NIR detection of urinary citrate has not been demonstrated; multivariate models are needed.
- Reference ranges for citrate vary between guidelines; sex-specific thresholds are not universally standardised.
- The interaction between urinary citrate and other stone inhibitors (pyrophosphate, [[magnesium]]) is not fully captured by current assays.
