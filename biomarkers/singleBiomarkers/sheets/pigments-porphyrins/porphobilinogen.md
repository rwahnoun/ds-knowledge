---
title: Porphobilinogen
aliases:
  - PBG
  - 2-Aminomethyl-4-(2-carboxyethyl)-1H-pyrrole-3-propanoic acid
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

# Porphobilinogen

Second intermediate in the heme biosynthesis pathway. Urinary [[[[porphobilinogen]]|PBG]] is the primary diagnostic marker for acute porphyrias (AIP, VP, HCP). Closely related to [[total-urinary-porphyrin]]. See [[datascience/spectroscopy-biomarkers]] for fluorescence-based detection.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Porphobilinogen |
| **Other names** | [[[[porphobilinogen]]\|PBG]] |
| **Chemical formula** | C₁₀H₁₄N₂O₄ |
| **Molecular weight** | 226.23 g/mol |
| **CAS number** | 487-90-1 |
| **PubChem CID** | 1021 |
| **SMILES** | NCc1[nH]cc(CCC(=O)O)c1CC(=O)O |
| **Appearance** | White to off-white crystalline powder |
| **Melting point** | Decomposes before melting (~170 °C) |

[[[[porphobilinogen]]|PBG]] is a pyrrole derivative with an aminomethyl group, carboxymethyl (acetic acid) side chain, and 2-carboxyethyl (propionic acid) side chain. At physiological urinary pH, exists predominantly as a zwitterionic or anionic species. Highly water-soluble and photosensitive — polymerises and darkens in light and air, forming uroporphyrinogen-like pigments ("port-wine" urine discolouration).

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **δ-Aminolevulinic acid (ALA)** | C₅H₉NO₃ | 131.13 | Precursor to [[[[porphobilinogen]]\|PBG]] in heme pathway; also elevated in acute porphyrias |
| **Urobilinogen** | C₃₃H₄₄N₄O₆ | 592.73 | Bile pigment; also reacts with Ehrlich's reagent (false positive in Watson-Schwartz) |
| **Uroporphyrinogen** | C₄₀H₄₄N₄O₁₆ | 836.80 | Tetrapyrrole formed from 4 [[[[porphobilinogen]]\|PBG]] molecules; downstream in heme pathway |
| **Indican (indoxyl sulfate)** | C₈H₆NO₄SK | 251.30 | [[[[tryptophan]]\|Tryptophan]] metabolite; may interfere with colorimetric tests |

---

## Medical Information

### Origin

**Endogenous — heme biosynthesis:**
1. **ALA synthesis** (mitochondrial, rate-limiting): Glycine + Succinyl-CoA → δ-Aminolevulinic acid (ALA); catalysed by ALA synthase (ALAS1/liver, ALAS2/erythroid).
2. **[[[[porphobilinogen]]|PBG]] synthesis** (cytoplasmic): 2 ALA → Porphobilinogen; catalysed by **ALA dehydratase** (zinc-dependent).
3. [[[[porphobilinogen]]|PBG]] is then converted to hydroxymethylbilane by **[[[[porphobilinogen]]|PBG]] deaminase (PBGD)** — the enzyme deficient in acute intermittent porphyria.

**Exogenous:** None. [[[[porphobilinogen]]|PBG]] is exclusively an endogenous metabolic intermediate with no dietary sources.

### Biological Roles

- **Primary:** Obligatory intermediate in heme biosynthesis, required for haemoglobin, myoglobin, cytochromes, catalase.
- **Secondary:** None — no known receptor, signalling, or structural role. Accumulation of [[[[porphobilinogen]]|PBG]] (and ALA) is neurotoxic, causing neurological symptoms of acute porphyrias, possibly through GABAergic effects and oxidative stress.

### Elimination Pathway

Under normal conditions, rapidly consumed by [[[[porphobilinogen]]|PBG]] deaminase. Small amount excreted in urine by glomerular filtration (MW 226 Da; not reabsorbed). During acute attacks, bottleneck at [[[[porphobilinogen]]|PBG]] deaminase causes 10–100× increase in urinary excretion. **Unstable in urine** — polymerises and oxidises, especially in light and alkaline pH, darkening urine.

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Plasma [[[[porphobilinogen]]\|PBG]]** | <0.12 µmol/L |
| **Urinary [[[[porphobilinogen]]\|PBG]] (24-h)** | <8.8 µmol/day (<2 mg/day) |
| **Urinary [[[[porphobilinogen]]\|PBG]] (random, [[creatinin\|creatinine]]-corrected)** | <1.5 µmol/mmol [[creatinin\|creatinine]] |
| **Urinary [[[[porphobilinogen]]\|PBG]] (random)** | <8.8 µmol/L |

### Factors Influencing Levels

**Increased [[[[porphobilinogen]]|PBG]]:** Acute attacks of AIP, VP, HCP. Precipitating factors: fasting, barbiturates, sulfonamides, oral contraceptives, alcohol, infections, stress, menstrual cycle.

**Decreased [[[[porphobilinogen]]|PBG]]:** Very low ALA production (severe lead poisoning — ALA rises but [[[[porphobilinogen]]|PBG]] may fall). No clinical pathology from low [[[[porphobilinogen]]|PBG]].

### Associated Pathologies

| Condition | [[[[porphobilinogen]]\|PBG]] Level | Key Symptoms |
|---|---|---|
| **Acute intermittent porphyria (AIP)** | >10× ULN during attacks (>50 µmol/day, often >150) | Severe abdominal pain, tachycardia, hypertension, psychiatric symptoms, motor neuropathy, seizures |
| **Variegate porphyria (VP)** | Moderately elevated during attacks | Abdominal pain + photosensitive skin lesions |
| **Hereditary coproporphyria (HCP)** | Moderately elevated during attacks | Similar to AIP + occasional photosensitivity |
| **ALA dehydratase deficiency** | Very low [[[[porphobilinogen]]\|PBG]]; ALA elevated | Extremely rare; abdominal pain, neuropathy |
| **Lead poisoning** | Normal or slightly elevated (ALA markedly elevated) | Abdominal colic, anaemia, encephalopathy, wrist drop |

### Presence in Urine

Trace amounts normally present (<2 mg/day). Form: native molecular form, predominantly dianionic at typical urine pH. Unstable — wrap samples in foil.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **Ion-exchange + Ehrlich's (gold standard)** | Anion-exchange column removes interfering chromogens; Ehrlich's reagent (p-DMAB in HCl) forms red adduct | 553 nm | ~0.5 µmol/L | Mauzerall-Granick method; quantitative; ~30 min |
| **Watson-Schwartz test** | Ehrlich's + chloroform/butanol extraction; [[[[porphobilinogen]]\|PBG]] stays aqueous | Visual pink-red | ~50 µmol/L | Rapid screening; poor sensitivity; false positives |
| **Hoesch test** | Reverse Ehrlich's addition; immediate cherry-red = [[[[porphobilinogen]]\|PBG]] positive | Visual cherry-red | ~25–50 µmol/L | Simpler than Watson-Schwartz; bedside |
| **LC-MS/MS** | RP-HPLC + tandem MS | m/z specific | 0.01–0.1 µmol/L | Highest specificity; multiplexed with ALA; reference labs |

Gold standard: **ion-exchange column + Ehrlich's reagent** at 553 nm. LC-MS/MS increasingly used in reference laboratories.

Optimal specimen: **random spot urine** for emergency screening; 24-h for quantitative confirmation. **Protect from light** (wrap in foil); store at 2–8 °C (stable ~48 h) or −20 °C (≥1 month). Do not alkalinise. [[[[porphobilinogen]]|PBG]]/[[creatinin|creatinine]] ratio on random sample correlates with 24-h excretion.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Urobilinogen** | False positive (Watson-Schwartz) | Also reacts with Ehrlich's reagent; removed by column or chloroform extraction |
| **Indican/indoxyl sulfate** | False positive | Ehrlich's cross-reactivity |
| **Methyldopa, phenazopyridine** | False positive (colour) | Coloured compounds in acidic conditions |
| **Light exposure** | False decrease | [[[[porphobilinogen]]\|PBG]] polymerises to [[total-urinary-porphyrin\|porphyrins]] |
| **Alkaline pH** | False decrease | Accelerates [[[[porphobilinogen]]\|PBG]] degradation |
| **Bacterial contamination** | Variable | May degrade [[[[porphobilinogen]]\|PBG]] |

### Spectroscopic Detection

**UV-Vis:** [[[[porphobilinogen]]|PBG]] itself absorbs weakly at ~220–240 nm (pyrrole π→π*). Primary approach is indirect via **Ehrlich chromogen** at **553 nm** (ε ≈ 6.1 × 10⁴ M⁻¹cm⁻¹). LOD ~0.5 µmol/L after column cleanup. NIR: no reported methods.

**Fluorescence:**
- Native [[[[porphobilinogen]]|PBG]] fluorescence: weak (Ex ~280 / Em ~340 nm); insufficient for urine.
- Enzymatic conversion: [[[[porphobilinogen]]|PBG]] → uroporphyrinogen ([[[[porphobilinogen]]|PBG]] deaminase) → uroporphyrin (oxidant) → fluorescence at **Ex 405 nm / Em 596 and 620 nm** (Soret excitation, Q-band emission). LOD ~2 µmol/L.
- Hantzsch derivatisation: Acetylacetone + formaldehyde → fluorescent product; **Ex 360–410 nm / Em 470–510 nm**. LOD ~0.1 µmol/L.

**Raman:** No published methods for [[[[porphobilinogen]]|PBG]] in urine. Expected pyrrole ring peaks: ~1370–1400 cm⁻¹ (C=C/C-N), ~1550–1580 cm⁻¹ (C=C), ~1000–1050 cm⁻¹ (C-C), ~2900–3000 cm⁻¹ (C-H). At normal urinary concentrations, not feasible with conventional Raman.

**FTIR:** Expected bands: ~3300–3500 cm⁻¹ (N-H/NH₂), ~1700–1720 cm⁻¹ (C=O, 2 COOH), ~1580–1600 cm⁻¹ (NH₂/COO⁻), ~1350–1400 cm⁻¹ (pyrrole). Even during acute attacks (50–500 µmol/L), concentrations are below typical ATR-FTIR sensitivity without preconcentration.

**Voltammetry:** Pyrrole ring can be oxidised at ~+0.8 to +1.0 V vs Ag/AgCl on carbon electrodes. No validated methods published.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths | Limitations |
|---|---|---|---|---|---|
| **Ion-exchange + Ehrlich's** | ~0.5 µmol/L | 553 nm | Column + reagent | Quantitative, specific | Labour-intensive, 30 min |
| **Watson-Schwartz** | ~50 µmol/L | Visual pink-red | Ehrlich's + extraction | Rapid, bedside | Poor sensitivity, false positives |
| **Hoesch test** | ~25–50 µmol/L | Visual cherry-red | Reverse Ehrlich's | Simpler | Semi-quantitative |
| **LC-MS/MS** | ~0.01–0.1 µmol/L | m/z specific | Dilute/SPE | Highest specificity, multiplex | Expensive, specialised |
| **Fluorescence (porphyrin conversion)** | ~2 µmol/L | Ex 405 / Em 596+620 nm | Enzyme + oxidant | Non-destructive | Requires [[[[porphobilinogen]]\|PBG]] deaminase |
| **Fluorescence (Hantzsch)** | ~0.1 µmol/L | Ex 360–410 / Em 470–510 nm | Derivatisation | Sensitive, simultaneous ALA+[[[[porphobilinogen]]\|PBG]] | Chemical derivatisation |
| **HPLC-UV** | ~0.1–0.5 µmol/L | 240 nm | Acidify, centrifuge | Quantitative | HPLC instrumentation |
| **Raman / FTIR / Voltammetry** | Not established | — | — | — | No published methods |

---

## Sources

| # | Reference |
|---|---|
| 1 | PubChem — Porphobilinogen, CID 1021. https://pubchem.ncbi.nlm.nih.gov/compound/1021 |
| 2 | StatPearls — Biochemistry, Heme Synthesis. https://www.ncbi.nlm.nih.gov/books/NBK537329/ |
| 3 | GeneReviews — Acute Intermittent Porphyria. https://www.ncbi.nlm.nih.gov/books/NBK1193/ |
| 4 | PMC — Acute Hepatic Porphyrias: Current Diagnosis & Management. https://pmc.ncbi.nlm.nih.gov/articles/PMC6911835/ |
| 5 | Pierach & Watson (1977) — Comparison of Hoesch and Watson-Schwartz tests. Clin Chem. |
| 6 | Lang et al. (2015) — Rapid screening for porphyria using fluorescence. SPIE Proc. |
| 7 | Frontiers in Chemistry (2022) — Synchronous spectrofluorimetry for ALA and [[[[porphobilinogen]]\|PBG]]. https://www.frontiersin.org/articles/10.3389/fchem.2022.920468/full |
| 8 | Jamani et al. (1989) — Liquid-chromatographic assay of urinary [[[[porphobilinogen]]\|PBG]]. Clin Chem. |

---

## Gaps

- No validated Raman or SERS method for [[[[porphobilinogen]]|PBG]] detection in urine
- FTIR detection not feasible at clinical concentrations without preconcentration; no published protocol
- Voltammetric detection of pyrrole ring oxidation not characterised in complex urine matrix
- Hantzsch fluorimetry (LOD ~0.1 µmol/L) is promising for simultaneous ALA+[[[[porphobilinogen]]|PBG]] but not yet validated as a clinical platform
- Point-of-care [[[[porphobilinogen]]|PBG]] test (below Watson-Schwartz LOD of ~50 µmol/L) remains an unmet need
