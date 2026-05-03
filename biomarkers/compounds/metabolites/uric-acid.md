---
title: Uric Acid
aliases:
  - 2,6,8-Trihydroxypurine
  - Urate
  - Hyperuricosuria
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - class/metabolite
  - clinical/gout
  - clinical/nephrolithiasis
  - clinical/tumor-lysis
  - modality/uv
  - presence/normal
  - subclass/purine-end-product
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
clinical-use:
  - gout
  - nephrolithiasis
  - tumor-lysis
detection-modality:
  - uv
class: metabolite
subclass: purine-end-product
presence: normal
parent: "[[biomarkers/compounds/metabolites/index|metabolites]]"
---
# Uric Acid

End-product of purine catabolism in humans. Key marker for gout, [[uric-acid|uric acid]] nephrolithiasis, and tumour lysis syndrome. Strong UV absorption at 293 nm enables direct spectroscopic detection. See [[datascience/spectroscopy-biomarkers]], [[signatures]], and [[optical-properties]] for spectral reference.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Uric Acid |
| **Other names** | 2,6,8-Trihydroxypurine, urate (ionised form) |
| **Chemical formula** | C₅H₄N₄O₃ |
| **Molecular weight** | 168.11 g/mol |
| **CAS number** | 69-93-2 |
| **PubChem CID** | 1175 |
| **SMILES** | O=c1[nH]c(=O)c2[nH]c(=O)[nH]c2[nH]1 |
| **Appearance** | White crystalline powder |
| **pKa** | 5.4 (first dissociation) |
| **Solubility** | ~60 mg/L at pH 5; ~200 mg/L at pH 7 (very pH-dependent) |

[[uric-acid|Uric acid]] is the end-product of purine nucleotide metabolism in humans (lacking uricase, unlike most mammals). A weak diprotic acid (pKa1 5.4, pKa2 10.3). At urinary pH <5.5, exists predominantly as **undissociated [[uric-acid|uric acid]]** (poorly soluble, can crystallise and form stones). At pH >6, the more soluble **urate ion** predominates.

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **[[urea\|Urea]]** | CH₄N₂O | 60.06 | From amino acid catabolism ([[urea]] cycle), not purine metabolism |
| **Xanthine** | C₅H₄N₄O₂ | 152.11 | Purine precursor of [[uric-acid\|uric acid]]; substrate of xanthine oxidase |
| **Allantoin** | C₄H₆N₄O₃ | 158.12 | Product of uricase (absent in humans) |
| **[[creatinin\|Creatinine]]** | C₄H₇N₃O | 113.12 | From creatine metabolism; different pathway |

---

## Medical Information

### Origin — Purine Catabolism

**Endogenous:** Final product of purine degradation. Pathway: adenine/guanine nucleotides → hypoxanthine → xanthine → [[uric-acid|uric acid]] (catalysed by xanthine oxidase/dehydrogenase). Humans lack uricase (pseudogene). Production ~600–800 mg/day: ~2/3 from endogenous purine turnover, ~1/3 from dietary purines.

**Exogenous:** High-purine foods: organ meats (liver, kidney), anchovies, sardines, shellfish, red meat, beer (yeast purines). Fructose and alcohol increase [[uric-acid|uric acid]] production.

### Biological Roles

- **Primary:** Waste product — end-product of purine catabolism for excretion.
- **Antioxidant:** [[uric-acid|Uric acid]] accounts for ~50% of plasma antioxidant capacity; scavenges peroxynitrite and hydroxyl radicals.
- **Blood pressure modulation:** Elevated [[uric-acid|uric acid]] associated with hypertension (causality debated).

### Elimination Pathway

~70% eliminated by kidneys, ~30% by GI tract (intestinal uricolysis by [[bacteria]]). Renal handling: freely filtered → ~90% reabsorbed (URAT1 transporter) → ~50% secreted (OAT1/3) → ~40% post-secretory reabsorption. Net fractional excretion: ~8–12%.

Allopurinol and febuxostat inhibit xanthine oxidase (reduce production). Probenecid and lesinurad are uricosurics (increase excretion).

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Serum [[uric-acid\|uric acid]]** | Male: 3.5–7.2 mg/dL; Female: 2.6–6.0 mg/dL |
| **Urinary [[uric-acid\|uric acid]] (24-h)** | 250–750 mg/day (1.5–4.5 mmol/day) on regular diet |
| **Urinary [[uric-acid\|uric acid]] (low-purine diet)** | <400 mg/day |

### Factors Influencing Levels

**Increased (hyperuricosuria):** High purine diet, gout with overproduction, tumour lysis syndrome, myeloproliferative disorders, uricosuric drugs (probenecid, losartan), Fanconi syndrome, Wilson disease.

**Decreased:** Xanthine oxidase inhibitors (allopurinol), CKD, lead nephropathy, dehydration.

### Associated Pathologies

| Condition | Uric Acid Pattern | Key Symptoms |
|---|---|---|
| **Gout** | Serum >6.8 mg/dL; variable urinary | Acute monoarthritis (podagra), tophi; ~4% adults |
| **[[uric-acid\|Uric acid]] nephrolithiasis** | High urinary [[uric-acid\|uric acid]] + acidic pH | Radiolucent stones; ~10% of all stones |
| **Tumour lysis syndrome** | Massive hyperuricosuria + hyperuricaemia | AKI, hyperK, hyperPO₄; oncology emergency |
| **Lesch-Nyhan syndrome** | Markedly elevated; HGPRT deficiency | Self-harm, dystonia, renal stones; X-linked |

### Presence in Urine

Normal excretory product (250–750 mg/day). Form: at pH <5.5 — **undissociated [[uric-acid|uric acid]]** (poorly soluble; crystallises as rhomboid or rosette yellow-brown crystals). At pH >6 — **urate anion** (more soluble). This pH-dependent solubility is the basis for [[uric-acid|uric acid]] stone formation in acidic urine.

| Urinary pH | Dominant Species | Solubility |
|---|---|---|
| pH 5.0 | [[uric-acid\|Uric acid]] (uncharged) | ~60 mg/L |
| pH 7.0 | Urate ion | ~200 mg/L |
| pH 8.0 | Urate ion | ~1580 mg/L |

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **Uricase-peroxidase (gold standard)** | Uricase: UA → allantoin + H₂O₂; peroxidase + chromogen (4-AAP + DHBS) → quinoneimine dye | 520 nm (Trinder) | ~0.1 mg/dL | Specific, automated; CV 2–4% |
| **UV differential (uricase)** | Absorbance at 293 nm before vs after uricase; difference = [[uric-acid\|uric acid]] | 293 nm | ~0.05 mg/dL | Reference method; very specific |
| **Phosphotungstic acid (historical)** | UA reduces phosphotungstate → tungsten blue | 680–700 nm | ~0.5 mg/dL | Non-specific; reacts with ascorbic acid |

Gold standard: **Uricase-UV differential** (293 nm) is the reference. **Uricase-peroxidase colorimetric** is the standard automated method.

Optimal specimen: **24-hour urine** acidified with HCl or alkaline preservative to dissolve [[uric-acid|uric acid]] crystals. Refrigerate; warm before analysis. Spot [[uric-acid|uric acid]]/[[creatinin|creatinine]] ratio available.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Ascorbic acid** | Positive bias (phosphotungstic); negative (enzymatic-Trinder) | Reducing agent; inhibits peroxidase |
| **Haemolysis** | Positive bias | Released purines |
| **Lipaemia** | Positive bias | Light scattering |
| **[[uric-acid\|Uric acid]] crystals** | Negative bias if not dissolved | Crystals settle; undercounting |

### Spectroscopic Detection

**UV-Vis:** [[uric-acid|Uric acid]] absorbs strongly at **293 nm** (ε ~12,500 M⁻¹cm⁻¹). LOD ~0.05 mg/dL. Combined with uricase differential (before/after treatment), this provides high specificity.

**Fluorescence (indirect):** [[uric-acid|Uric acid]] is weakly fluorescent (Ex 308 / Em 400 nm; very low quantum yield). Enzymatic H₂O₂ → Amplex Red: Ex 571 / Em 585 nm, LOD ~0.5 µM. Carbon dot quenching: LOD ~1 µM.

**Raman:** Key peaks:

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~630** | Ring deformation |
| **~1000–1010** | Ring breathing |
| **~1130** | C-N stretch |
| **~1370** | C=N stretch |
| **~1600–1640** | C=C/C=O stretch |

Conventional Raman: LOD ~1–5 mM; adequate for hyperuricosuric urine. SERS (Ag nanoparticles): LOD ~1–10 µM; Ex 532/785 nm.

**FTIR:** Key bands: ~1680 cm⁻¹ (C=O stretch, strong), ~1590 cm⁻¹ (C=C), ~1230 cm⁻¹ (C-N), ~740 cm⁻¹ (ring deformation). ATR-FTIR: LOD ~1–5 mM; detectable in concentrated urine.

**Voltammetry:** [[uric-acid|Uric acid]] easily oxidised at **+0.3–0.4 V vs Ag/AgCl** on carbon electrodes. LOD ~0.1–1 µM on modified electrodes (graphene, MWCNTs, BDD). Major interference: ascorbic acid oxidises at similar potential. Nafion membrane or DPV improves selectivity.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Uricase enzymatic** | ~0.1 mg/dL | 520 nm (Trinder) | None | Automated, specific |
| **UV differential (293 nm)** | ~0.05 mg/dL | 293 nm | Uricase treatment | Reference method |
| **SERS** | ~1–10 µM | Ex 532/785 nm | Nanoparticles | Ultra-sensitive |
| **Raman** | ~1–5 mM | 630+1370 cm⁻¹ | None | Non-destructive |
| **FTIR** | ~1–5 mM | 1680 cm⁻¹ | None | Reagent-free |
| **DPV (electrochemical)** | ~0.1 µM | +0.3 V | Buffer | Very sensitive, real-time |
| **Fluorescence (Amplex)** | ~0.5 µM | Ex 571 / Em 585 nm | Uricase | Sensitive |
| **HPLC-UV** | ~0.01 mg/dL | 293 nm | Inject | Research gold standard |

---

## Sources

| # | Reference |
|---|---|
| 1 | StatPearls — Hyperuricosuria. https://www.ncbi.nlm.nih.gov/books/NBK562201/ |
| 2 | PubChem — Uric Acid, CID 1175. https://pubchem.ncbi.nlm.nih.gov/compound/1175 |
| 3 | StatPearls — Gout. https://www.ncbi.nlm.nih.gov/books/NBK546606/ |
| 4 | Springer — Spectrophotometric Determination of Uric Acid. https://link.springer.com/article/10.2116/analsci.23.223 |

---

## Gaps

- Raman/SERS detection of [[uric-acid|uric acid]] at clinical concentrations in real urine matrix is not validated (crystal vs dissolved distinction unclear)
- Electrochemical (DPV) selectivity over ascorbic acid is not robust without membrane coatings or careful potential optimisation
- [[uric-acid|Uric acid]] as an antioxidant vs pathological marker creates interpretational complexity — no consensus on optimal urinary UA target range for stone prevention
- pH-dependent solubility means sampling conditions (temperature, pH at collection) significantly affect measured concentrations

[uric-acid|uric acid]: uric-acid.md "Uric Acid"
[datascience/spectroscopy-biomarkers]: ../../../../../datascience/spectroscopy-biomarkers.md "Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices"
[uric-acid|Uric acid]: uric-acid.md "Uric Acid"
[urea\|Urea]: ../../.plans/urea.md "Literature Review Plan — urea"
[urea]: ../../.plans/urea.md "Literature Review Plan — urea"
[uric-acid\|uric acid]: uric-acid.md "Uric Acid"
[creatinin\|Creatinine]: creatinin.md "Creatinine"
[bacteria]: ../infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[uric-acid\|Uric acid]: uric-acid.md "Uric Acid"
[creatinin|creatinine]: creatinin.md "Creatinine"
