---
title: Metolachlor
aliases:
  - Metolachlor
  - Metolachlore
  - S-Metolachlor
  - Metolachlor mercapturate
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

# Metolachlor

Metolachlor is a widely used **chloroacetamide herbicide** applied to control annual grasses and broadleaf weeds in corn, soybean, sorghum, and other crops. It is one of the most frequently detected pesticides in surface and groundwater. In urine, it is detected primarily as the **metolachlor mercapturate** metabolite, used as a biomarker of exposure. It is a xenobiotic contaminant, not a physiological biomarker. See [[datascience/spectroscopy-biomarkers]] for pesticide biomonitoring context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Metolachlor |
| **Other names** | S-Metolachlor (active enantiomer); Dual, Bicep (trade names) |
| **Chemical formula** | C₁₅H₂₂ClNO₂ |
| **Molecular weight** | 283.79 g/mol |
| **CAS number** | 51218-45-2 (racemic); 87392-12-9 (S-metolachlor) |
| **PubChem CID** | 4169 |
| **Appearance** | Colourless to light tan liquid |
| **Solubility in water** | ~530 mg/L at 25 °C |
| **Log Kow** | 3.13 (moderately lipophilic) |

**Structural formula:**

```
  Cl-CH2-CO-N(CH2-OCH3)-C6H3(CH3)(C2H5)
  (chloroacetamide herbicide)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Alachlor** | C₁₄H₂₀ClNO₂ | 269.77 | Related chloroacetamide herbicide; different substitution |
| **Acetochlor** | C₁₄H₂₀ClNO₂ | 269.77 | Another chloroacetamide; same class |
| **Atrazine** | C₈H₁₄ClN₅ | 215.68 | Triazine herbicide; different class; often co-applied |
| **Metolachlor mercapturate** | C₁₉H₂₈ClNO₅S | 421.95 | Primary urinary metabolite; biomarker of exposure |

---

## Medical Information

### Origin

#### Endogenous

Metolachlor is **not endogenous**. It is purely an anthropogenic environmental contaminant.

#### Exogenous

- **Agricultural application:** ~30–35 million kg/year in the USA alone.
- **Drinking water contamination:** Detected in surface and groundwater at 0.01–10 µg/L.
- **Dietary exposure:** Residues on crops (corn, soybeans).
- **Occupational:** Farmers, applicators (dermal and inhalation exposure).
- **EPA MCL:** Not established for metolachlor (lifetime health advisory: 525 µg/L).

### Primary & Secondary Biological Roles

Metolachlor has **no physiological role**. It is a xenobiotic contaminant.

**Mechanism of herbicidal action:** Inhibits biosynthesis of very-long-chain fatty acids (VLCFAs) in plants by inhibiting elongases. This disrupts cell membrane formation.

**Human toxicity:** Classified as Group C (possible human carcinogen) by EPA. Chronic exposure linked to potential endocrine disruption and liver effects in animal studies. Generally low acute toxicity in humans (oral LD50 rat: 2780 mg/kg).

### Catabolism and Elimination Pathway

In humans:
1. Metolachlor is metabolised primarily via **glutathione conjugation** (GST pathway): metolachlor-GSH conjugate → cysteine conjugate → **metolachlor mercapturate** (N-acetylcysteine conjugate) — the primary urinary metabolite.
2. Other minor metabolites: metolachlor oxanilic acid (MOA), metolachlor ethanesulfonic acid (MESA).
3. Half-life in humans: ~6–12 hours (rapid elimination).
4. Primary elimination: urine (as mercapturate and other conjugates).

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Urine metolachlor mercapturate (general population)** | <LOD to ~0.2 µg/L (NHANES CDC biomonitoring) |
| **Urine metolachlor mercapturate (farmers)** | 0.1–50 µg/L (exposure-dependent) |
| **Drinking water metolachlor** | Typically <1 µg/L |

#### Factors Influencing Levels

**Increased:**
- Agricultural work during application season (spring planting)
- Proximity to agricultural areas
- Contaminated drinking water
- Dietary exposure from treated crops

**Decreased:**
- No agricultural exposure
- Use of treated/filtered water
- Off-season sampling

#### Associated Pathologies

| Condition | Metolachlor Link | Evidence Level |
|---|---|---|
| **Potential endocrine disruption** | Some animal evidence | Weak; regulatory concern |
| **Liver toxicity** | Chronic high-dose animal studies | Not demonstrated in humans at environmental levels |
| **Cancer** | EPA Group C (possible) | Inconclusive epidemiological evidence |

### Presence in Urine

**Should it be normally present?** **No** in unexposed individuals. Low levels may be detectable in general population due to ubiquitous environmental presence.

**Normal urinary levels:** <LOD (typically <0.2 µg/L) in general population.

**Form in urine:** Primarily as **metolachlor mercapturate** (N-acetyl-L-cysteine-metolachlor conjugate); minor metabolites.

**Solubility:** Metabolites are water-soluble (mercapturate conjugation increases hydrophilicity).

---

## Detection in Urine

### Available Clinical Assays

1. **LC-MS/MS (gold standard for biomonitoring):**
   - **Principle:** Liquid chromatography + tandem mass spectrometry. Detects metolachlor mercapturate and other metabolites.
   - **Detection:** MRM transitions; metolachlor mercapturate m/z 422→130 or 422→192.
   - **LOD:** ~0.01–0.1 µg/L (10–100 ng/L).
   - **Advantages:** Definitive; ultra-sensitive; multiplex with other pesticide metabolites.
   - **Disadvantages:** Expensive instrumentation.

2. **HPLC-MS/MS (CDC NHANES method):**
   - **Principle:** Online SPE + HPLC-MS/MS.
   - **LOD:** ~0.02 µg/L.
   - **Reference:** CDC National Biomonitoring Program.

3. **ELISA (immunoassay):**
   - **Principle:** Antibody-based competitive ELISA for metolachlor mercapturate.
   - **Detection:** Absorbance at **450 nm** (HRP-TMB).
   - **LOD:** ~0.1–1 µg/L.
   - **Advantages:** Screening; lower cost than LC-MS/MS.
   - **Disadvantages:** Cross-reactivity with related chloroacetamides; semi-quantitative.

### Optimal Urine Type for Measurement

- **Spot urine** with creatinine correction is standard for biomonitoring.
- First morning urine preferred (more concentrated).
- Store frozen at -20 °C if not analysed immediately.
- No special preservatives.

### Actual Gold Standard

**LC-MS/MS** with online SPE (CDC method) is the reference for urinary metolachlor metabolite biomonitoring.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Other chloroacetamide metabolites** | Cross-reactivity (ELISA) | Structural similarity |
| **Matrix effects (ion suppression)** | Variable (LC-MS/MS) | Co-eluting urine components |
| **Isotopically labelled IS** | Corrects for matrix effects | Standard practice in LC-MS/MS |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- Metolachlor absorbs in the UV at **~220 nm** (aromatic ring + amide). Not specific enough for urine matrix.
- HPLC-UV at 220 nm: LOD ~1–10 µg/L. Less sensitive than MS detection.
- NIR: Not applicable (too low concentration).

#### Fluorescence Detection

- Metolachlor is weakly fluorescent (low quantum yield).
- **Fluorescence immunoassay (FPIA):** Fluorescein-labelled metolachlor + antibody. Ex 490 / Em 520 nm. LOD: ~0.5 µg/L.
- Not commonly used; LC-MS/MS preferred.

#### Raman Detection

- No published Raman methods for urinary metolachlor metabolites.
- SERS detection of parent metolachlor in water: LOD ~1–10 µg/L on Ag/Au substrates. Not validated for urine.

#### FTIR Detection

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **~1660** | C=O stretch (amide) | Chloroacetamide |
| **~1600** | Aromatic C=C | — |
| **~740** | C-Cl stretch | Characteristic |

- Not practical for urinary metabolites at ng/L to µg/L levels.

#### Voltammetry Detection

- Metolachlor can be reduced electrochemically (C-Cl bond reduction) at **-0.8 to -1.2 V vs Ag/AgCl** on mercury or bismuth electrodes.
- LOD: ~0.5–5 µg/L by adsorptive stripping voltammetry (AdSV) in water.
- Not validated for urine matrix (high organic content interferes).

### Other Detection Technologies

1. **GC-MS:** For parent metolachlor (volatile). LOD: ~0.01 µg/L in water. Requires extraction (LLE/SPE).
2. **Immunoassay rapid test strips:** Commercial RaPID Assay kits. LOD: ~0.1 µg/L. Field-deployable.
3. **Biosensors (acetolactate synthase inhibition):** Experimental. Not established for metolachlor.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **LC-MS/MS** | ~0.01 µg/L | MRM m/z 422→130 | SPE or dilute-shoot | Gold standard |
| **ELISA** | ~0.1–1 µg/L | 450 nm | Plate assay | Screening, cheaper |
| **HPLC-UV** | ~1–10 µg/L | 220 nm | SPE | Simpler |
| **GC-MS (parent)** | ~0.01 µg/L | EI-MS | LLE/SPE | Parent compound |
| **AdSV** | ~0.5 µg/L | -1.0 V | Buffer | Low-cost |
| **Raman/FTIR** | Not practical | — | — | Concentrations too low |

---

## Sources

| # | Citation |
|---|---|
| 1 | Nature JESEE — Immunoassay and HPLC-MS/MS for urinary metolachlor. https://preview-www.nature.com/articles/jes200915 |
| 2 | CDC — Biomonitoring of PFAS and Pesticide Metabolites. https://stacks.cdc.gov/view/cdc/187802/cdc_187802_DS1.pdf |
| 3 | ScienceDirect — ELISA for metolachlor mercapturate. https://www.sciencedirect.com/science/article/abs/pii/S0003267099005814 |
| 4 | ScienceDirect — Immunoassay biomonitoring of herbicides. https://www.sciencedirect.com/science/article/abs/pii/S0003267098004516 |
| 5 | PubChem — Metolachlor, CID 4169. https://pubchem.ncbi.nlm.nih.gov/compound/4169 |
| 6 | EPA — Metolachlor fact sheet. |

## Gaps

- Validated reference ranges for urinary metolachlor mercapturate in non-US general populations are limited.
- SERS/Raman detection of metolachlor mercapturate (not parent compound) in urine has not been demonstrated.
- Long-term health effects of chronic low-dose exposure in the general population (below occupational levels) are not well-characterised.
- No rapid POC test exists for field-based occupational exposure assessment.
- Enantioselective biomonitoring of S-metolachlor vs racemic metolachlor in urine is not routinely performed.
