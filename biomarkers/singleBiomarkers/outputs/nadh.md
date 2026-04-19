---
title: NADH (Reduced Nicotinamide Adenine Dinucleotide)
aliases:
  - NADH
  - Reduced NAD
  - DPNH
  - Coenzyme I reduced
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

# NADH (Reduced Nicotinamide Adenine Dinucleotide)

NADH is the reduced form of NAD⁺, the central electron carrier in cellular metabolism. NADH is **intrinsically fluorescent** (Ex 340 nm / Em 460 nm), while NAD⁺ is not, making NADH a natural endogenous fluorophore. In the urinary context, NADH fluorescence has been explored as a marker of cellular metabolic activity and as a component of the overall urine autofluorescence spectrum. It is a research biomarker, not a routine clinical analyte. See [[optical-properties]] for fluorescence data and [[signatures]] for spectral assignments.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | NADH (Reduced Nicotinamide Adenine Dinucleotide) |
| **Other names** | DPNH, Coenzyme I (reduced form), NAD⁺ (oxidised form) |
| **Chemical formula** | C₂₁H₂₉N₇O₁₄P₂ |
| **Molecular weight** | 665.44 g/mol |
| **CAS number** | 58-68-4 |
| **PubChem CID** | 928 |
| **Appearance** | White to yellow powder; solutions fluorescent (NADH) or non-fluorescent (NAD⁺) |
| **Solubility** | Freely soluble in water |

**Structural formula:**

```
  Nicotinamide--Ribose--PO4--PO4--Ribose--Adenine
  (reduced nicotinamide ring carries extra H at C4)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **NAD⁺** | C₂₁H₂₇N₇O₁₄P₂ | 663.43 | Oxidised form; NOT fluorescent at 340/460 nm |
| **NADPH** | C₂₁H₃₀N₇O₁₇P₃ | 745.42 | Phosphorylated form; similar fluorescence; anabolic role |
| **FAD** | C₂₇H₃₃N₉O₁₅P₂ | 785.55 | Flavin-based coenzyme; fluorescent at 450/525 nm (different wavelength) |
| **Riboflavin (B2)** | C₁₇H₂₀N₄O₆ | 376.36 | FAD precursor; strong fluorescence at 450/525 nm |

---

## Medical Information

### Origin

#### Endogenous: Cellular Metabolism

NADH is produced in all cells via glycolysis (cytoplasm), pyruvate dehydrogenase, and the TCA cycle (mitochondria). It is the primary electron donor to Complex I of the electron transport chain. Intracellular NADH concentrations: ~100–400 µM. NADH is predominantly intracellular; extracellular/urinary levels reflect cell lysis, metabolic overflow, and renal tubular cell turnover.

#### Exogenous

NADH supplements are available commercially. Dietary NAD⁺ precursors include niacin (vitamin B3) and nicotinamide riboside (NR), but these do not directly contribute urinary NADH.

### Primary & Secondary Biological Roles

**Primary role:**
- **Electron carrier in catabolism:** NADH donates electrons to the mitochondrial ETC for ATP production (2.5 ATP per NADH).

**Secondary roles:**
- **Redox signalling:** NAD⁺/NADH ratio regulates sirtuins, PARPs, and metabolic gene expression.
- **Autofluorescence biomarker:** NADH fluorescence is used in tissue metabolic imaging (optical biopsy).

### Catabolism and Elimination Pathway

- NADH is rapidly oxidised to NAD⁺ in mitochondria (ETC) or cytoplasm (lactate dehydrogenase).
- Free NADH is unstable in acidic conditions (t½ ~30 min at pH 4).
- Urinary NADH derives from cellular debris, lysed cells, and renal tubular cell turnover.
- NAD⁺ and its metabolites (nicotinamide, NMN, ADPR) are also excreted.

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Intracellular NADH** | 100–400 µM |
| **Blood NAD⁺ total** | ~20–40 µM |
| **Urine NADH** | Trace (not routinely measured); detectable by fluorescence |

#### Factors Influencing Levels

**Increased urinary NADH fluorescence:**
- Increased cellular turnover or damage
- UTI (bacterial metabolic activity)
- Cancer cells (altered metabolism, Warburg effect)
- Mitochondrial disorders

**Decreased:**
- Not clinically significant in isolation.

#### Associated Pathologies

NADH itself is not a standalone clinical biomarker. Its fluorescence contributes to urinary autofluorescence patterns studied in research contexts.

| Condition | NADH Relevance | Notes |
|---|---|---|
| **Bladder cancer screening** | Altered NADH/FAD ratio in exfoliated cells | Research stage |
| **UTI** | Bacterial NADH fluorescence | Experimental |
| **Metabolic disorders** | Altered redox state | Research stage |

### Presence in Urine

**Should it be normally present?** In **trace amounts** — from normal cellular turnover. Not routinely measured.

**Normal urinary levels:** Not standardised. Detectable as fluorescence signal at Ex 340 / Em 460 nm.

**Form in urine:** Free NADH molecule (unstable, degrades in acidic urine).

**Solubility:** Freely soluble.

---

## Detection in Urine

> [!NOTE]
> No routine clinical assays measure urinary NADH. It is a research biomarker detected by autofluorescence methods.

### Optimal Urine Type for Measurement

- Fresh specimen required (NADH is unstable). Analyse immediately.
- Protect from light and heat.
- Neutral or slightly alkaline pH preserves NADH stability.

### Actual Gold Standard

No established clinical gold standard. **HPLC-UV at 340 nm** or **HPLC-fluorescence (Ex 340 / Em 460 nm)** are research reference methods.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Acidic pH** | Degradation | NADH decomposes at pH <6 |
| **Light** | Photodegradation | UV-sensitive |
| **Other fluorophores** | Spectral overlap | Riboflavin, FAD, proteins fluoresce at nearby wavelengths |
| **Oxidation** | Signal loss | NADH → NAD⁺ (non-fluorescent) |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- **UV absorption:** NADH absorbs at **340 nm** (ε ~6,220 M⁻¹cm⁻¹). NAD⁺ absorbs at 260 nm but not 340 nm. The 340 nm band is diagnostic for the reduced form.
  - LOD: ~1 µM by direct UV.
  - Sample prep: None (direct measurement of fresh urine).

#### Fluorescence Detection

This is the primary detection modality for NADH. See [[optical-properties]] for comparison with other urinary fluorophores.

- **Intrinsic fluorescence:** **Ex 340 nm / Em 460 nm** (blue fluorescence). Quantum yield ~2%.
  - LOD: ~0.1–1 µM in buffer; ~5–10 µM in urine (matrix quenching).
  - Lifetime: ~0.4 ns (free NADH), ~1–3 ns (protein-bound NADH).
- **Two-photon excitation:** Ex 720–740 nm (two-photon) / Em 460 nm. Used in tissue imaging.
- **FLIM (Fluorescence Lifetime Imaging):** Distinguishes free vs bound NADH by lifetime. Not applicable for bulk urine.

#### Raman Detection

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~1030** | Nicotinamide ring C-H stretch |
| **~1340** | Adenine ring |
| **~1580** | Nicotinamide ring C=C/C=N |
| **~1690** | C=O stretch (amide) |

- Conventional Raman: LOD ~1 mM (too high for urinary levels).
- SERS: Potentially LOD ~1–10 µM. Few studies on urinary NADH specifically.

#### FTIR Detection

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **~1690** | Amide C=O | Nicotinamide |
| **~1580** | Ring C=C | — |
| **~1080** | PO₄ stretch | Phosphodiester |

- Not practical for urinary NADH (too low concentration, overlapping bands).

#### Voltammetry Detection

- NADH is electrochemically oxidised: NADH → NAD⁺ + H⁺ + 2e⁻
- **Oxidation potential:** +0.5–0.7 V vs Ag/AgCl on bare carbon; reduced to +0.1–0.3 V on modified electrodes (Meldola Blue, carbon nanotubes, graphene).
- LOD: ~0.1–1 µM on nanostructured electrodes.
- **Interference:** Ascorbic acid, uric acid oxidise at similar potentials.

### Other Detection Technologies

1. **Enzymatic cycling assays:** NAD⁺/NADH quantified by lactate dehydrogenase cycling with colorimetric or fluorimetric endpoint. LOD: ~10 nM. Measures total NAD pool.
2. **LC-MS/MS:** Definitive identification and quantification. LOD: ~1 nM. Sample prep: protein precipitation, extraction.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **UV absorption** | ~1 µM | 340 nm | None | Direct, simple |
| **Fluorescence** | ~0.1–1 µM | Ex 340/Em 460 nm | None (fresh) | Primary method |
| **Electrochemical** | ~0.1–1 µM | +0.1–0.3 V (modified) | Buffer | Real-time |
| **Enzymatic cycling** | ~10 nM | Colorimetric/fluorimetric | Enzyme kit | Ultra-sensitive |
| **LC-MS/MS** | ~1 nM | m/z 664→514 | Extraction | Definitive |
| **Raman/FTIR** | >1 mM | — | — | Not practical |

---

## Sources

| # | Citation |
|---|---|
| 1 | PMC — Evaluating Cell Metabolism Through Autofluorescence of NAD(P)H and FAD. https://ncbi.nlm.nih.gov/pmc/articles/PMC6352511/ |
| 2 | PMC — NADH and NADPH Autofluorescence. https://ncbi.nlm.nih.gov/pmc/articles/PMC5145803/ |
| 3 | Wiley — NADH Autofluorescence as Bioenergetic Marker. https://onlinelibrary.wiley.com/doi/full/10.1002/cyto.a.23597 |
| 4 | PubChem — NADH, CID 928. https://pubchem.ncbi.nlm.nih.gov/compound/928 |

## Gaps

- Urinary NADH concentrations in health and disease have not been systematically characterised; reference ranges do not exist.
- EEM-based separation of NADH fluorescence from overlapping signals (tryptophan, tyrosine, FAD, riboflavin) in urine requires validated deconvolution algorithms.
- The NADH/FAD autofluorescence ratio as a urinary biomarker for cancer or metabolic disease has only been demonstrated in cell culture and ex vivo tissue, not in bulk urine.
- NADH instability in urine (acidic pH, light exposure) limits sample handling flexibility in clinical research.
