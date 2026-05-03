---
title: Bilirubin
aliases:
  - Bilirubin
  - Bilirubinuria
  - Conjugated bilirubin
  - Direct bilirubin
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - class/pigment
  - clinical/liver
  - clinical/hepatobiliary
  - modality/vis
  - modality/uv
  - presence/abnormal
  - subclass/tetrapyrrole
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
clinical-use:
  - liver
  - hepatobiliary
detection-modality:
  - vis
  - uv
class: pigment
subclass: tetrapyrrole
presence: abnormal
parent: "[[biomarkers/compounds/pigments-porphyrins/index|pigments-porphyrins]]"
---
# Bilirubin

Bilirubin is the yellow breakdown product of heme degradation. Only **conjugated (direct) bilirubin** appears in urine because unconjugated bilirubin is tightly bound to albumin and not filtered by the glomerulus. Bilirubinuria is an early sign of hepatobiliary disease. See [[optical-properties]] for UV-Vis absorption characteristics and [[datascience/spectroscopy-biomarkers]] for clinical context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Bilirubin |
| **Other names** | Unconjugated (indirect) bilirubin; Conjugated (direct) bilirubin = bilirubin diglucuronide |
| **Chemical formula** | C₃₃H₃₆N₄O₆ |
| **Molecular weight** | 584.66 g/mol |
| **CAS number** | 635-65-4 |
| **PubChem CID** | 5280352 |
| **Appearance** | Yellow-orange pigment |
| **Solubility** | Unconjugated: water-insoluble (bound to albumin); Conjugated: water-soluble |

**Structural formula:**

```
  Linear tetrapyrrole (open-chain porphyrin derivative):
  Pyrrole-CH=Pyrrole-CH2-Pyrrole-CH=Pyrrole
  (with vinyl, methyl, propionic acid side chains)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Urobilinogen** | C₃₃H₄₄N₄O₆ | 592.73 | Reduced form of bilirubin by gut [[bacteria]]; colourless; normally in urine |
| **Biliverdin** | C₃₃H₃₄N₄O₆ | 582.65 | Green precursor of bilirubin; not found in urine |
| **Stercobilin** | C₃₃H₄₆N₄O₆ | 594.74 | Final faecal pigment; gives brown colour to stool |

---

## Medical Information

### Origin

#### Endogenous: Heme Degradation

Bilirubin is produced from heme catabolism (75–85% from senescent [[red-blood-cells|RBC]] haemoglobin, 15–25% from other haemoproteins). Pathway: Heme → biliverdin (heme oxygenase) → bilirubin (biliverdin reductase). Unconjugated bilirubin is transported bound to albumin to the liver, where UDP-glucuronosyltransferase (UGT1A1) conjugates it with glucuronic acid → conjugated bilirubin (water-soluble), excreted in bile.

Daily production: ~250–350 mg bilirubin.

#### Exogenous

No significant dietary source. Bilirubin is exclusively endogenous.

### Primary & Secondary Biological Roles

**Primary role:**
- **Waste product:** Bilirubin is an excretory end-product of heme metabolism.

**Secondary roles:**
- **Antioxidant:** Bilirubin is a potent scavenger of peroxyl radicals; mildly elevated levels may be cardioprotective (Gilbert syndrome).
- **Clinical marker:** Serum bilirubin levels indicate liver function, haemolysis, and biliary obstruction.

### Catabolism and Elimination Pathway

- Conjugated bilirubin is excreted in bile into the intestine.
- Gut [[bacteria]] reduce conjugated bilirubin → urobilinogen → stercobilin (faecal colour).
- ~10–15% of urobilinogen is reabsorbed (enterohepatic circulation), re-excreted in bile or filtered by kidneys into urine.
- Conjugated bilirubin can be filtered by the glomerulus if serum levels are elevated → bilirubinuria.
- Unconjugated bilirubin is not excreted in urine (albumin-bound).

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Total serum bilirubin** | 0.1–1.2 mg/dL (2–21 µmol/L) |
| **Direct (conjugated)** | 0–0.3 mg/dL |
| **Indirect (unconjugated)** | 0.1–0.8 mg/dL |
| **Urine bilirubin** | Negative (absent or <0.02 mg/dL) |
| **Urine urobilinogen** | 0.1–1.0 Ehrlich units (trace amounts normal) |

#### Factors Influencing Levels

**Bilirubinuria (positive urine bilirubin):**
- Obstructive jaundice (gallstones, pancreatic head tumour)
- Hepatocellular disease (hepatitis, cirrhosis)
- Drug-induced cholestasis
- Dubin-Johnson syndrome (rare conjugated hyperbilirubinaemia)

**Absent urine bilirubin (normal or haemolytic):**
- Normal state
- Haemolytic jaundice (unconjugated bilirubin elevated but not filtered)
- Gilbert syndrome (unconjugated; no bilirubinuria)

#### Associated Pathologies

| Condition | Bilirubin Pattern | Key Symptoms |
|---|---|---|
| **Obstructive jaundice** | Positive urine bilirubin + absent urobilinogen | Jaundice, dark urine, pale stools, pruritus |
| **Hepatitis** | Positive urine bilirubin + variable urobilinogen | Jaundice, RUQ pain, fatigue |
| **Haemolytic jaundice** | Negative urine bilirubin + increased urobilinogen | Anaemia, jaundice, splenomegaly |
| **Gilbert syndrome** | Negative urine bilirubin | Mild intermittent jaundice; benign; ~5% population |

### Presence in Urine

**Should it be normally present?** **No** — urine bilirubin should be absent. Its presence (bilirubinuria) always indicates pathology (conjugated hyperbilirubinaemia).

**Normal urinary levels:** Negative (<0.02 mg/dL).

**Form in urine:** **Conjugated bilirubin (bilirubin diglucuronide)**, water-soluble form.

**Pathological significance:**

| Urinary Bilirubin | Possible Causes | Prevalence |
|---|---|---|
| **Positive** | Obstructive or hepatocellular jaundice | Varies; gallstones ~10–15% adults |
| **Negative** | Normal; or haemolytic jaundice (unconjugated) | — |

**Solubility:** Conjugated bilirubin is water-soluble. Unconjugated is insoluble (albumin-bound).

---

## Detection in Urine

### Available Clinical Assays

1. **Dipstick diazo reaction:**
   - **Principle:** Conjugated bilirubin reacts with diazonium salt (2,4-dichloroaniline or similar) → azobilirubin (pink-tan colour).
   - **Detection:** Colour change on pad.
   - **LOD:** ~0.5 mg/dL (~8.5 µmol/L).
   - **Advantages:** Rapid, included on standard dipstick.
   - **Disadvantages:** Light degrades bilirubin → false negatives; insensitive.

2. **Ictotest (confirmatory tablet test):**
   - **Principle:** Bilirubin adsorbs onto special mat; diazo tablet reagent → blue-purple colour.
   - **Detection:** Visual colour on mat.
   - **LOD:** ~0.05–0.1 mg/dL (more sensitive than dipstick).
   - **Advantages:** Confirmatory; Siemens Ictotest tablets.

3. **Total bilirubin by diazo (Jendrassik-Grof, lab):**
   - **Principle:** Bilirubin + diazotised sulfanilic acid → azobilirubin.
   - **Detection:** Absorbance at **540–560 nm**.
   - **LOD:** ~0.1 mg/dL.

### Optimal Urine Type for Measurement

- **Fresh specimen** essential — bilirubin is photolabile (decomposes rapidly in light).
- Protect from light (foil-wrapped container).
- Analyse within **1 hour** of collection.
- Random specimen adequate.

### Actual Gold Standard

**Ictotest tablet** is the confirmatory urine bilirubin test. For serum, the **Jendrassik-Grof diazo method** at 540 nm is the reference.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Light exposure** | False negative | Photodecomposition of bilirubin |
| **Ascorbic acid** | False negative | Reduces diazo reaction |
| **Nitrite (high)** | False negative | Oxidises bilirubin |
| **Chlorpromazine** | False positive | Produces coloured metabolites |
| **Phenazopyridine** | Colour masking | Orange dye |
| **Elevated urobilinogen** | Minor interference | Slight colour contribution |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- **UV-Vis:** Bilirubin absorbs strongly at **453 nm** (ε ~55,000 M⁻¹cm⁻¹ in chloroform; shifts in aqueous solution). Direct spectrophotometry at 453 nm possible if concentrated enough.
  - LOD: ~0.05 mg/dL in clean solutions.
  - In urine matrix: interfered by other chromogens.
- **NIR:** No useful bilirubin absorption.

#### Fluorescence Detection

- Bilirubin has very weak native fluorescence (quantum yield <0.01%) due to rapid internal conversion.
- **Zinc bilirubin complex:** Zn-bilirubin fluoresces (Ex 430 / Em 530 nm). LOD: ~0.01 mg/dL.
- **Bilirubin oxidase + fluorescent product:** Enzymatic oxidation produces biliverdin (weakly fluorescent).
- Not commonly used for urine bilirubin.

#### Raman Detection

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~1615** | C=C stretching (vinyl groups) |
| **~1575** | Pyrrole ring stretching |
| **~1340** | C-N stretching |
| **~1270** | C-H bending |

- Bilirubin has characteristic Raman spectrum but concentrations in urine are too low for conventional Raman.
- SERS: Potential LOD ~0.01 mg/dL with Au nanoparticles. Limited studies.

#### FTIR Detection

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **~1690** | C=O stretch (lactam) | Strong |
| **~1620** | C=C stretch | — |
| **~1570** | Pyrrole ring | — |
| **~3300** | N-H stretch | Broad |

- ATR-FTIR: Not sensitive enough for normal or mildly elevated urinary bilirubin.

#### Voltammetry Detection

- Bilirubin is electrochemically oxidised at **+0.1–0.4 V vs Ag/AgCl** on carbon electrodes.
- LOD: ~0.01–0.1 mg/dL on modified electrodes (graphene, MWCNTs).
- Interference from ascorbic acid and [[uric-acid|uric acid]] (similar oxidation potentials).
- **MIP sensors:** Molecularly imprinted polymers for bilirubin. LOD: ~0.005 mg/dL.

### Other Detection Technologies

1. **Transcutaneous bilirubinometry:** Non-invasive skin reflectance at 460/550 nm for neonatal jaundice screening. Not for urine.
2. **Smartphone-based dipstick reading:** Camera analysis of diazo pad colour. LOD: similar to visual (~0.5 mg/dL).
3. **Paper-based diazo assay:** Low-cost diazo-impregnated paper with smartphone readout.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Dipstick (diazo)** | ~0.5 mg/dL | Pink-tan colour | None | Standard, rapid |
| **Ictotest** | ~0.05 mg/dL | Blue-purple | Mat adsorption | More sensitive |
| **Jendrassik-Grof** | ~0.1 mg/dL | 540–560 nm | Reagent | Quantitative |
| **UV-Vis (453 nm)** | ~0.05 mg/dL | 453 nm | None | Direct |
| **Zn-bilirubin fluorescence** | ~0.01 mg/dL | Ex 430/Em 530 nm | Zn addition | Sensitive |
| **Voltammetry** | ~0.01 mg/dL | +0.1–0.4 V | Buffer | Sensitive |
| **MIP electrochemical** | ~0.005 mg/dL | DPV | Buffer | Selective |
| **Raman/FTIR** | Not practical | — | — | Concentrations too low |

---

## Sources

| # | Citation |
|---|---|
| 1 | eClinpath — Bilirubin. https://eclinpath.com/chemistry/liver/cholestasis/bilirubin/ |
| 2 | Mayo Clinic — Bilirubin Test. https://www.mayoclinic.org/tests-procedures/bilirubin/about/pac-20393041 |
| 3 | Siemens — Ictotest Reagent Tablets. https://www.siemens-healthineers.com/en-us/poct-urinalysis/ictotest-reagent-tablets |
| 4 | FPnotebook — Urine Bilirubin. https://fpnotebook.com/Uro/Lab/UrnBlrbn.htm |
| 5 | RCPA — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 6 | PubChem — Bilirubin, CID 5280352. https://pubchem.ncbi.nlm.nih.gov/compound/5280352 |

## Gaps

- Native fluorescence of bilirubin in urine is poorly characterised; quantum yield values in aqueous/urine matrix are not well-established.
- Raman/SERS detection of bilirubin in urine has not been validated in patient samples.
- Differentiation of urinary bilirubin from urobilinogen by optical methods in complex urine matrix requires further study.
- No POC quantitative bilirubin assay with clinical-grade accuracy for urine exists.

[datascience/spectroscopy-biomarkers]: ../../../../../datascience/spectroscopy-biomarkers.md "Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices"
[bacteria]: ../infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[red-blood-cells|RBC]: ../infection-inflammation/red-blood-cells.md "Red Blood Cells"
[uric-acid|uric acid]: ../metabolites/uric-acid.md "Uric Acid"
