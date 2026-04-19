---
title: Phosphate
aliases:
  - Inorganic phosphate
  - Orthophosphate
  - Pi
  - Urinary phosphate
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

# Phosphate

Essential mineral anion. The primary urinary buffer and the main regulatory mechanism for phosphate balance. Urinary phosphate measurement is used in stone workup and metabolic bone disease assessment. See [[datascience/spectroscopy-biomarkers]] and [[signatures]] for spectral context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Phosphate |
| **Other names** | Inorganic phosphate, orthophosphate, Pi |
| **Chemical formula** | PO₄³⁻ (fully deprotonated); H₂PO₄⁻ and HPO₄²⁻ at physiological pH |
| **Molecular weight** | 94.97 g/mol (PO₄³⁻) |
| **CAS number** | 14265-44-2 |
| **PubChem CID** | 1061 |
| **Appearance** | Colourless in solution |

Phosphate is an essential mineral anion. At urinary pH (4.5–8.0), it exists primarily as **H₂PO₄⁻** (dihydrogen phosphate, pKa₂ = 6.8) and **HPO₄²⁻** (monohydrogen phosphate). This buffering pair constitutes the major **titratable acid** system in urine.

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Pyrophosphate (PPi)** | P₂O₇⁴⁻ | 173.94 | Condensation dimer; inhibitor of calcification |
| **Organic phosphates (ATP, etc.)** | Variable | Variable | Phosphorylated organic molecules; not measured by Pi assays |
| **Phosphonate** | RPO₃²⁻ | Variable | C-P bond (not C-O-P); synthetic compounds |

---

## Medical Information

### Origin

**Endogenous:** Total body phosphorus ~700 g (85% in bone as hydroxyapatite, 14% soft tissue, 1% ECF). No endogenous synthesis — phosphorus is an element. Released from bone remodelling and intracellular stores.

**Exogenous:** Dietary phosphate from dairy, meat, fish, eggs, legumes, cola drinks. Typical intake: 800–1500 mg/day. Absorption 60–70% (enhanced by vitamin D; inhibited by calcium and aluminium).

### Biological Roles

- **Bone mineralisation:** Hydroxyapatite (Ca₁₀(PO₄)₆(OH)₂) is the structural mineral of bones and teeth.
- **Energy metabolism:** ATP, GTP, creatine phosphate — the energy currency bond.
- **Urinary buffer:** H₂PO₄⁻/HPO₄²⁻ system (pKa 6.8) is the primary titratable acid buffer in urine.
- **Nucleic acids and membranes:** DNA/RNA backbone; phospholipid bilayers.
- **Intracellular signalling:** Protein phosphorylation; second messengers (cAMP, IP₃).

### Elimination Pathway

Freely filtered at glomerulus (~6,500 mg/day). **80–90% reabsorbed** in proximal tubule via NaPi-IIa and NaPi-IIc transporters (regulated by PTH and FGF23, which reduce reabsorption). Remaining 10–20% excreted in urine.

**PTH** increases urinary phosphate (phosphaturic). **FGF23** also increases excretion. **Vitamin D** increases intestinal absorption.

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Serum phosphate** | 2.5–4.5 mg/dL (0.81–1.45 mmol/L) in adults |
| **Urinary phosphate (24-h)** | 400–1300 mg/day (13–42 mmol/day) |
| **TmP/GFR (tubular max reabsorption)** | 2.5–4.2 mg/dL |
| **FEPi (fractional excretion)** | 5–20% |

### Factors Influencing Levels

**Increased urinary phosphate:** Hyperparathyroidism, FGF23-producing tumours, Fanconi syndrome, high phosphate diet, metabolic acidosis, vitamin D excess.

**Decreased urinary phosphate:** Hypoparathyroidism, vitamin D deficiency, low phosphate diet, phosphate binders, growth/anabolism.

### Associated Pathologies

| Condition | Phosphate Pattern | Key Symptoms |
|---|---|---|
| **Primary hyperparathyroidism** | High urinary PO₄, low serum PO₄ | Hypercalcaemia, stones, bone pain |
| **CKD (advanced)** | Low urinary PO₄, high serum PO₄ | Renal osteodystrophy, vascular calcification |
| **Fanconi syndrome** | High urinary PO₄ + glucose + amino acids | Rickets/osteomalacia, growth failure |
| **Tumour-induced osteomalacia** | Very high FEPi, low serum PO₄ | Bone pain, fractures, muscle weakness |
| **Calcium phosphate nephrolithiasis** | Elevated urinary PO₄ + Ca | Kidney stones (brushite, apatite) |

### Presence in Urine

Normal excretion 400–1300 mg/day. Form: mixture of **H₂PO₄⁻** and **HPO₄²⁻** (ratio depends on urine pH; at pH 6.8, equal amounts). Calcium phosphate crystals (amorphous, brushite CaHPO₄) form in alkaline urine. Struvite (MgNH₄PO₄) forms in infected alkaline urine.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Detection | LOD | Notes |
|---|---|---|---|---|
| **Phosphomolybdate UV (gold standard)** | Phosphate + molybdate → phosphomolybdate complex | 340 nm (UV) or 660–700 nm (molybdenum blue, reduced) | ~0.1 mg/dL | Standard on automated platforms; CV 2–4% |
| **Enzymatic (PNP coupled)** | Pi + inosine → PNP → hypoxanthine → uric acid + H₂O₂ → Trinder | 546 nm | ~0.05 mg/dL | More specific, fewer interferences |

Gold standard: **Phosphomolybdate UV method** (340 nm) on automated platforms (Roche, Siemens).

Optimal specimen: **24-hour urine** for total phosphate; acidify with HCl to prevent crystal precipitation. Spot urine for TmP/GFR calculation (with simultaneous serum phosphate and creatinine).

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Haemolysis** | Positive bias | Intracellular phosphate release from RBCs |
| **Lipaemia** | Positive bias | Light scattering |
| **Bilirubin** | Variable | Absorbs near 340 nm |
| **Mannitol, dextran** | Positive bias | Complex with molybdate |
| **Precipitated Ca-PO₄** | Negative bias | Phosphate lost to crystals if urine not acidified |

### Spectroscopic Detection

**UV-Vis:** Phosphomolybdate blue at 660–700 nm (standard); vanadomolybdate yellow at 400–420 nm (alternative). NIR: no useful phosphate absorption.

**Fluorescence (indirect):** Europium(III) or terbium(III) complexes quenched by phosphate (Eu: Ex 340 / Em 615 nm, LOD ~1 µM). DPA-Zn fluorescent sensors for phosphate/pyrophosphate (Ex 340 / Em 460 nm).

**Raman:** Key peaks:

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~940** | P-O symmetric stretch (ν₁) — strongest |
| **~1020** | P-O asymmetric stretch (ν₃) |
| **~420** | O-P-O bending (ν₂) |

Conventional Raman detects phosphate at >10 mM; LOD ~5–10 mM (adequate for concentrated urine). Excitation: 532 or 785 nm.

**FTIR:** Bands at ~1080 cm⁻¹ (PO asym. stretch, ν₃), ~940 cm⁻¹ (PO sym. stretch, ν₁), ~560 cm⁻¹ (PO bending, ν₄). ATR-FTIR LOD ~5–10 mM in aqueous solution.

**Voltammetry:** Electrochemically inert in normal window. Indirect: phosphate precipitates with molybdate; DPV of phosphomolybdate gives LOD ~0.1 µM. Cobalt electrode method: Co²⁺ forms insoluble Co₃(PO₄)₂; stripping voltammetry LOD ~0.5 µM.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Phosphomolybdate UV** | ~0.1 mg/dL | 340 nm | None | Standard, automated |
| **Molybdenum blue** | ~0.05 mg/dL | 660–700 nm | Reagent | Sensitive |
| **Enzymatic** | ~0.05 mg/dL | 546 nm | None | Specific |
| **Raman** | ~5 mM | 940 cm⁻¹ | None | Reagent-free |
| **FTIR** | ~5 mM | 1080 cm⁻¹ | None | Non-destructive |
| **DPV (molybdate)** | ~0.1 µM | +0.2–0.4 V | Molybdate addition | Ultra-sensitive |
| **Eu fluorescence** | ~1 µM | Ex 340 / Em 615 nm | Probe | Sensitive |
| **ICP-OES** | ~0.001 mg/dL | 213.6 nm | Dilution | Ultimate reference |

---

## Sources

| # | Reference |
|---|---|
| 1 | PMC — Renal Phosphate Reabsorption Overview. https://pmc.ncbi.nlm.nih.gov/articles/PMC11083860/ |
| 2 | StatPearls — Hyperphosphatemia. https://www.ncbi.nlm.nih.gov/books/NBK551586/ |
| 3 | PubChem — Phosphate, CID 1061. https://pubchem.ncbi.nlm.nih.gov/compound/1061 |
| 4 | KDIGO Guidelines — CKD-MBD. https://kdigo.org/ |

---

## Gaps

- Raman phosphate detection (940 cm⁻¹) has adequate sensitivity for concentrated urine but is not yet validated in a Jimini-style flow-through system
- FGF23-mediated phosphaturia is clinically important but FGF23 itself is not measurable by standard urinary assays
- No validated SERS method for urinary phosphate; the 940 cm⁻¹ peak is a candidate but not demonstrated
