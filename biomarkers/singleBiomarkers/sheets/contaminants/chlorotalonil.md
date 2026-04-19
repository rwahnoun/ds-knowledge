---
title: Chlorothalonil
aliases:
  - Chlorothalonil
  - Chlorotalonil
  - Tetrachloroisophthalonitrile
  - Daconil
  - Bravo
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

# Chlorothalonil

Chlorothalonil is a broad-spectrum **organochlorine fungicide** widely used on crops until its EU ban in 2019. In humans, exposure is assessed via urinary metabolites, primarily **4-hydroxy-2,5,6-trichloroisophthalonitrile (4-OH-chlorothalonil)** and its glutathione/mercapturate conjugates. It is a xenobiotic contaminant, not a physiological biomarker. See [[datascience/spectroscopy-biomarkers]] for pesticide detection context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Chlorothalonil |
| **Other names** | Tetrachloroisophthalonitrile, Daconil, Bravo (trade names) |
| **Chemical formula** | C₈Cl₄N₂ |
| **Molecular weight** | 265.91 g/mol |
| **CAS number** | 1897-45-6 |
| **PubChem CID** | 15910 |
| **Appearance** | Colourless to white crystalline solid |
| **Solubility in water** | ~0.81 mg/L at 25 °C (very poorly soluble) |
| **Log Kow** | 2.94 |
| **Melting point** | 250–251 °C |

**Structural formula:**

```
     Cl    CN
      |    |
  Cl--C====C--CN
      |    |
  Cl--C====C
      |
      Cl
  (tetrachlorinated isophthalonitrile ring)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **4-Hydroxy-chlorothalonil (4-OH-CHT)** | C₈HCl₃N₂O | 247.47 | Primary metabolite (soil and biological); more water-soluble and toxic |
| **Chlorpyrifos** | C₉H₁₁Cl₃NO₃PS | 350.59 | Organophosphate insecticide; completely different class |
| **Mancozeb** | Polymer (Mn/Zn dithiocarbamate) | Variable | Another fungicide; different chemistry |

---

## Medical Information

### Origin

#### Endogenous

Chlorothalonil is **not endogenous**. It is a synthetic xenobiotic.

#### Exogenous

- **Agricultural application:** Used on >50 crop types worldwide.
- **Banned in EU since 2019** (groundwater contamination and classified as "likely carcinogenic" by EFSA); still registered in USA, Brazil, China.
- **Exposure routes:** Dietary residues on treated produce, contaminated drinking water (metabolite 4-OH-CHT commonly detected in groundwater), occupational (farmers, applicators).
- **Drinking water:** 4-OH-CHT frequently detected in European groundwater at >0.1 µg/L.

### Primary & Secondary Biological Roles

Chlorothalonil has **no physiological role**. It is a xenobiotic fungicide.

**Mechanism of fungicidal action:** Multi-site inhibition of glutathione and thiol-dependent enzymes in fungi (non-specific thiol alkylation). This multi-site activity reduces resistance development.

**Human toxicity:**
- **Acute:** Low oral toxicity (LD50 rat: >10,000 mg/kg); moderate eye and skin irritant.
- **Chronic/cancer:** Classified by US EPA as "likely to be carcinogenic" (renal tumours in rats). EU classified as carcinogen category 2 and banned for use.
- **Nephrotoxicity:** Animal studies show renal proximal tubular toxicity.

### Catabolism and Elimination Pathway

In humans:
1. **Glutathione conjugation** (primary Phase II metabolism): chlorothalonil reacts with GSH via GST → mono- and di-glutathione conjugates → mercapturic acid conjugates (N-acetylcysteine derivatives) excreted in urine.
2. **4-Hydroxylation:** Formation of 4-OH-chlorothalonil (also formed in the environment).
3. Half-life in mammals: relatively short (~hours); rapid urinary excretion of conjugated metabolites.

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Urine chlorothalonil metabolites (general population)** | Generally <LOD (~0.1 µg/L) in non-agricultural populations |
| **Urine chlorothalonil metabolites (occupational)** | 0.1–50 µg/L (exposure-dependent) |
| **Drinking water 4-OH-CHT (EU monitoring)** | Frequently >0.1 µg/L in groundwater near treated areas |

#### Factors Influencing Levels

**Increased:**
- Occupational exposure (fungicide applicators)
- Dietary intake from treated crops
- Contaminated drinking water (4-OH-CHT metabolite)
- Residential proximity to treated agricultural areas

**Decreased:**
- No agricultural exposure
- Consumption of organic produce
- Post-EU-ban: declining environmental levels in Europe

#### Associated Pathologies

| Condition | Chlorothalonil Link | Evidence |
|---|---|---|
| **Renal toxicity** | Proximal tubular damage (animal studies) | Strong in rodents at high doses |
| **Cancer (renal)** | Renal tumours in rats | Basis for EU ban and EPA classification |
| **Skin/eye irritation** | Occupational dermatitis | Common in applicators |
| **Endocrine disruption** | Some evidence of thyroid effects | Limited |

### Presence in Urine

**Should it be normally present?** **No** — it is a xenobiotic contaminant. However, low levels of metabolites may be detectable in populations with environmental exposure.

**Normal urinary levels:** <LOD in most individuals.

**Form in urine:** Glutathione and **mercapturate conjugates** of chlorothalonil; 4-OH-chlorothalonil conjugates.

**Solubility:** Metabolite conjugates are water-soluble (increased by glutathione/mercapturate conjugation).

---

## Detection in Urine

### Available Clinical Assays

1. **LC-MS/MS (gold standard):**
   - **Principle:** RP-HPLC + tandem MS for chlorothalonil metabolites (mercapturate conjugate, 4-OH-CHT).
   - **Detection:** MRM transitions in negative ESI mode.
   - **LOD:** ~0.01–0.1 µg/L.
   - **Advantages:** Definitive identification; multi-metabolite profiling.

2. **GC-MS (for parent compound in water):**
   - **Principle:** SPE or LLE extraction + GC-ECD or GC-MS.
   - **Detection:** ECD or EI-MS; m/z 266 (M+), 268, 270 (isotope pattern).
   - **LOD:** ~0.01 µg/L in water; higher in urine matrix.
   - **Advantages:** Parent compound detection.
   - **Disadvantages:** Urine contains metabolites, not parent; GC is less suitable.

### Optimal Urine Type for Measurement

- **Spot urine** with [[creatinin|creatinine]] correction.
- Store frozen at -20 °C.
- No PTFE or treated containers.
- Samples stable at -20 °C for months.

### Actual Gold Standard

**LC-MS/MS** for urinary mercapturate and glutathione conjugate metabolites of chlorothalonil.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Matrix effects** | Ion suppression (LC-MS/MS) | Urine salts, organic matter |
| **Isotope-labelled IS** | Corrects for matrix effects | Standard practice |
| **Cross-reactivity** | Possible with related chloronitriles | Minimal with MS detection |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- Chlorothalonil absorbs in the UV: **~232 nm** (strong, aromatic/nitrile conjugation, ε ~40,000 M⁻¹cm⁻¹) and **~320 nm** (weaker).
- HPLC-UV at 232 nm: LOD ~1–10 µg/L (parent in water). Not sufficient for urinary metabolites at trace levels.
- NIR: Not applicable.

#### Fluorescence Detection

- Chlorothalonil is **non-fluorescent** (nitrile groups are quenching).
- **Immunofluorescence:** Anti-chlorothalonil antibodies + fluorescent tracer. Ex/Em: probe-dependent. LOD: ~0.1–1 µg/L. Research stage.

#### Raman Detection

The nitrile peak at 2240 cm⁻¹ is highly characteristic and falls in a spectral region free from most biological interferences. See [[signatures]] for spectral context.

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~2240** | C≡N triple bond stretch (nitrile) — diagnostic |
| **~1580** | Aromatic C=C stretch |
| **~380** | C-Cl stretch |

- SERS: Potential LOD ~1–10 µg/L with Au/Ag substrates. Not validated for urine.

#### FTIR Detection

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **~2240** | C≡N stretch (nitrile) | Diagnostic, strong |
| **~1580** | Aromatic C=C | — |
| **~850** | C-Cl stretch | — |
| **~750** | Ring deformation | — |

- The nitrile band at 2240 cm⁻¹ is in a clear spectral region, making FTIR potentially useful for concentrated samples.
- Not practical for urinary metabolites at ng/L to µg/L levels.

#### Voltammetry Detection

- Chlorothalonil can be reduced at mercury or bismuth electrodes:
  - C-Cl bond reduction at **-0.6 to -1.0 V vs Ag/AgCl**.
  - CN reduction at more negative potentials.
- **Adsorptive stripping voltammetry (AdSV):** LOD ~0.1–1 µg/L for parent compound in water.
- Not established for urinary metabolites.

### Other Detection Technologies

1. **ELISA:** Commercial kits available for chlorothalonil in water/food. LOD: ~0.05–0.5 µg/L. Cross-reactivity with metabolites varies.
2. **GC-ECD:** Excellent sensitivity for chlorinated compounds. LOD: ~0.01 µg/L for parent. Requires extraction.
3. **Biomonitoring panels:** Some occupational health labs include chlorothalonil metabolites in multi-pesticide LC-MS/MS panels.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **LC-MS/MS (metabolites)** | ~0.01–0.1 µg/L | MRM (ESI-) | SPE | Gold standard for urine |
| **GC-MS (parent)** | ~0.01 µg/L | m/z 266 | LLE/SPE | Parent in water |
| **GC-ECD** | ~0.01 µg/L | ECD response | LLE/SPE | Sensitive for Cl compounds |
| **ELISA** | ~0.05–0.5 µg/L | 450 nm | Plate | Screening |
| **AdSV** | ~0.1–1 µg/L | -0.8 V | Adsorption | Low-cost |
| **Raman (nitrile)** | >10 µg/L | 2240 cm⁻¹ | None | Diagnostic peak |
| **FTIR (nitrile)** | >100 µg/L | 2240 cm⁻¹ | None | Characteristic |

---

## Sources

| # | Citation |
|---|---|
| 1 | PubChem — Chlorothalonil, CID 15910. https://pubchem.ncbi.nlm.nih.gov/compound/15910 |
| 2 | EFSA — Chlorothalonil peer review conclusion (2018). |
| 3 | US EPA — Chlorothalonil reregistration eligibility decision. |
| 4 | EU Commission — Regulation (EU) 2019/677 (non-renewal of chlorothalonil). |
| 5 | Environmental Health Perspectives — Chlorothalonil metabolites in groundwater. |

## Gaps

- Validated LC-MS/MS reference ranges for urinary chlorothalonil metabolites in the general population outside the US (NHANES) are lacking.
- Raman/SERS detection of metabolite conjugates (not parent) in urine has not been demonstrated.
- Long-term health effects of chronic low-level exposure (general population, drinking water route) remain incompletely characterised.
- No rapid POC test exists for chlorothalonil metabolite biomonitoring.
