---
title: Oxalate
aliases:
  - Oxalic acid
  - Ethanedioic acid
  - C2O4(2-)
  - Urinary oxalate
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - class/metabolite
  - clinical/nephrolithiasis
  - modality/uv
  - modality/eis
  - presence/normal
  - subclass/organic-acid
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
clinical-use:
  - nephrolithiasis
detection-modality:
  - uv
  - eis
class: metabolite
subclass: organic-acid
presence: normal
parent: "[[biomarkers/compounds/metabolites/index|metabolites]]"
---
# Oxalate

Metabolic waste product; the dominant constituent of kidney stones (~75–80%). Clinically important for stone risk stratification. See [[datascience/spectroscopy-biomarkers]] and [[signatures]] for optical detection reference.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Oxalate |
| **Other names** | Oxalic acid, ethanedioic acid, C₂O₄²⁻ |
| **Chemical formula** | C₂H₂O₄ (acid); C₂O₄²⁻ (dianion) |
| **Molecular weight** | 90.03 g/mol |
| **CAS number** | 144-62-7 |
| **PubChem CID** | 971 |
| **pKa** | pKa1 = 1.25; pKa2 = 4.27 |
| **Solubility** | [[sodium\|Sodium]] oxalate: ~37 g/L; Calcium oxalate: 0.0067 g/L (very insoluble) |

Structural formula:

```
  O=C-C=O
  |     |
  OH   OH       (oxalic acid, fully protonated)
```

Oxalate is the simplest dicarboxylic acid. At urinary pH it exists primarily as the **oxalate dianion (C₂O₄²⁻)**. Its clinical importance lies in its propensity to form **calcium oxalate (CaOx) crystals** — the most common component of kidney stones (~75–80%). Even small increases in urinary oxalate dramatically raise CaOx supersaturation.

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Citrate** | C₆H₅O₇³⁻ | 189.10 | Stone inhibitor (chelates Ca); opposite role |
| **Glycolate** | C₂H₃O₃⁻ | 75.04 | Precursor of oxalate; elevated in primary hyperoxaluria type 1 |
| **Glyoxylate** | C₂HO₃⁻ | 73.03 | Key intermediate in oxalate synthesis; substrate of AGT enzyme |

---

## Medical Information

### Origin

**Endogenous (~50%):** Primarily liver. Pathways: glyoxylate → oxalate (via LDH or glycolate oxidase); ascorbic acid (vitamin C) → oxalate (non-enzymatic); hydroxyproline → oxalate.

**Exogenous (~40–50%):** Spinach, rhubarb, beetroot, nuts, chocolate, tea, sweet potatoes. Vitamin C supplements (>1 g/day) increase oxalate via non-enzymatic degradation.

### Biological Roles

- **Waste product:** No known physiological function. Purely a waste product of glyoxylate and ascorbate metabolism.
- **Stone formation:** CaOx precipitation is the basis of most kidney stones.

### Elimination Pathway

Humans cannot metabolise oxalate (no oxalate-degrading enzyme, unlike gut *Oxalobacter formigenes*). **Renal excretion** is the sole elimination route: filtered at glomerulus + secreted by proximal tubule (SLC26A6). Loss of *O. formigenes* (antibiotics) increases dietary oxalate absorption.

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Plasma oxalate** | 1–5 µmol/L |
| **Urinary oxalate (24-h)** | <40–45 mg/day (<0.5 mmol/day) |
| **Urinary oxalate concentration** | 10–40 mg/L |

### Factors Influencing Levels

**Hyperoxaluria (>45 mg/day):** Primary hyperoxaluria (types 1, 2, 3 — genetic, >100 mg/day); enteric hyperoxaluria (fat malabsorption: Crohn's, bariatric surgery); dietary hyperoxaluria; ethylene glycol poisoning.

**Low urinary oxalate:** Low dietary oxalate; pyridoxine (B6) supplementation (reduces glyoxylate → oxalate).

### Associated Pathologies

| Condition | Oxalate Pattern | Key Symptoms |
|---|---|---|
| **CaOx nephrolithiasis** | Mild hyperoxaluria (40–60 mg/day) | Renal colic, haematuria; 75–80% of all stones |
| **Primary hyperoxaluria type 1** | >100 mg/day; AGT deficiency | Recurrent stones, nephrocalcinosis, ESRD; ~1:120,000 |
| **Enteric hyperoxaluria** | 60–100 mg/day | Post-bariatric surgery, Crohn's |
| **Ethylene glycol poisoning** | Massive oxaluria + CaOx crystals | Metabolic acidosis, AKI, CNS depression |

### Presence in Urine

Normal urinary solute (<40–45 mg/day). Form: **oxalate dianion (C₂O₄²⁻)** at urinary pH >4.3. Forms insoluble CaOx crystals (monohydrate: whewellite; dihydrate: weddellite) when supersaturated. Calcium oxalate Ksp ~2.3 × 10⁻⁹.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **Oxalate oxidase enzymatic** | Oxalate + O₂ → 2CO₂ + H₂O₂; H₂O₂ + peroxidase + chromogen | 590 nm | ~5 µmol/L | Standard clinical; Trinity Biotech, Roche |
| **Ion chromatography** | Anion exchange + conductivity | Conductivity | ~0.5 µmol/L | Research reference; multi-anion |
| **Capillary electrophoresis** | Electrophoretic separation | UV 200 nm | ~1 µmol/L | Fast separation |

Gold standard: **Oxalate oxidase enzymatic assay**. IC is the research reference.

Optimal specimen: **24-hour urine acidified with 6N HCl** (~20 mL per container) to prevent CaOx crystallisation. Refrigerate during collection.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Ascorbic acid** | Positive bias | Non-enzymatic conversion to oxalate during storage |
| **CaOx crystal precipitation** | Negative bias | Oxalate lost to crystals if urine not acidified |
| **Glycolate (high)** | Minor cross-reactivity | Some oxalate oxidase preparations |

### Spectroscopic Detection

**UV-Vis:** Weak absorption <210 nm; direct UV not practical. Enzymatic colorimetric at 590 nm is standard. NIR: no useful absorption.

**Fluorescence (indirect):** Enzymatic H₂O₂ → Amplex Red (Ex 571 / Em 585 nm), LOD ~1 µmol/L. Ce(III) fluorescence quenching (Ex 256 / Em 360 nm), LOD ~5 µmol/L.

**Raman:** Key peaks: 1460 cm⁻¹ (C-O sym. stretch), 1620 cm⁻¹ (C=O asym. stretch), 890 cm⁻¹ (C-C stretch). Conventional LOD ~1 mM. CaOx crystals have distinct Raman signatures used for stone composition analysis.

**FTIR:** Bands at ~1620 cm⁻¹ (C=O asym.), ~1320 cm⁻¹ (C-O sym.), ~780 cm⁻¹ (O-C-O bending). ATR-FTIR can identify CaOx crystals in sediment; not practical for dissolved oxalate quantification.

**Voltammetry:** Oxalate oxidised at +0.8–1.2 V vs Ag/AgCl on carbon or Pt electrodes. LOD ~1–10 µmol/L on PbO₂ or boron-doped diamond. Ascorbic acid interference.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Oxalate oxidase** | ~5 µmol/L | 590 nm | Acidified urine | Standard clinical |
| **Ion chromatography** | ~0.5 µmol/L | Conductivity | Dilution | Reference |
| **Amplex Red fluorescence** | ~1 µmol/L | Ex 571 / Em 585 nm | Enzyme kit | Sensitive |
| **Voltammetry (BDD)** | ~1 µmol/L | +1.0 V | Buffer | Real-time |
| **Raman (CaOx crystals)** | N/A | 1460 cm⁻¹ | Crystal isolation | Stone analysis |
| **LC-MS/MS** | ~0.5 µmol/L | m/z 89→61 | Extraction | Definitive |

---

## Sources

| # | Reference |
|---|---|
| 1 | StatPearls — Hyperoxaluria. https://www.ncbi.nlm.nih.gov/books/NBK551653/ |
| 2 | KDIGO — Kidney Stone Guidelines |
| 3 | PubChem — Oxalic acid, CID 971. https://pubchem.ncbi.nlm.nih.gov/compound/971 |
| 4 | Trinity Biotech — Oxalate Assay Kit documentation |

---

## Gaps

- No validated spectroscopic (NIR/Raman) method for dissolved urinary oxalate quantification in complex matrix
- *Oxalobacter formigenes* gut microbiome influence on oxalate bioavailability not well-characterised for patient cohort stratification
- Raman stone analysis well-established; Raman for dissolved oxalate in urine not validated

[datascience/spectroscopy-biomarkers]: ../../../../../datascience/spectroscopy-biomarkers.md "Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices"
[sodium\|Sodium]: sodium.md "Sodium"
