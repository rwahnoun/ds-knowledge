---
title: Urine pH
aliases:
  - pH
  - Urinary pH
  - Hydrogen ion concentration
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

# Urine pH

Physical-chemical property reflecting renal acid-base handling. Measured on Jimini using optical indicator dyes and electrochemical sensors. See [[signal-processing]] and [[optical-properties]] for measurement context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Urine pH |
| **Other names** | Hydrogen ion concentration, acidity/alkalinity |
| **Definition** | pH = −log₁₀[H⁺]; measure of hydrogen ion activity |
| **Nature** | Physical-chemical property (not a single molecule) |
| **Normal range** | 4.5–8.0 (typical: 5.5–6.5) |
| **Units** | pH units (dimensionless logarithmic scale) |

Urine pH reflects the kidney's role in acid-base homeostasis — the net excretion of H⁺ ions (titratable acid + ammonium) vs HCO₃⁻. Normal urine is mildly acidic (pH ~6) on a typical Western diet due to protein metabolism. Urine pH influences solubility of many substances: [[uric-acid|uric acid]] stones at pH <5.5, calcium [[phosphate]] stones at pH >7, struvite at pH >7.5.

### Concepts Not to Be Confused With

| Measure | Definition | Key Difference |
|---|---|---|
| **Titratable acidity** | Buffered H⁺ (mainly H₂PO₄⁻) | Amount of acid, not just concentration |
| **Ammonium (NH₄⁺)** | Major urinary acid excretion vehicle | Quantitative acid excretion; not measured by pH alone |
| **Blood pH** | 7.35–7.45 | Much tighter regulation; urine pH compensates |

---

## Medical Information

### Origin

**Endogenous:** Determined by (1) dietary acid/alkali load, (2) renal tubular H⁺ secretion (proximal and distal), (3) NH₄⁺ production (proximal tubule glutaminase), (4) HCO₃⁻ reclamation, and (5) titratable acid buffering (mainly [[phosphate]]). Western meat-rich diet generates ~50–100 mEq/day net acid → acidic urine.

**Exogenous:** Diet is the primary determinant: animal protein → acidic urine; fruits/vegetables → alkaline urine. Potassium citrate alkalinises; ammonium [[chloride]] acidifies; [[sodium]] bicarbonate alkalinises.

### Biological Roles

- **Primary:** Renal acid-base homeostasis — kidneys regulate blood pH by adjusting urinary H⁺ excretion.
- **Stone chemistry:** Urine pH critically affects crystal formation ([[uric-acid|uric acid]], calcium [[phosphate]], struvite).
- **Drug excretion:** pH affects ionisation and tubular reabsorption of weak acids/bases.
- **Antimicrobial:** Acidic urine inhibits bacterial growth.

### Clinical Levels

| Condition | pH Range |
|---|---|
| **Random urine** | 4.5–8.0 |
| **Typical (Western diet)** | 5.5–6.5 |
| **After meat-heavy meal** | 4.5–5.5 |
| **Vegetarian diet** | 6.5–7.5 |
| **Blood pH (for comparison)** | 7.35–7.45 |

### Factors Influencing Levels

**Acidic urine (pH <5.5):** High animal protein diet, metabolic acidosis (DKA, lactic acidosis), respiratory acidosis, dehydration, cranberry juice, ammonium [[chloride]], [[uric-acid|uric acid]] stone formers.

**Alkaline urine (pH >7.0):** Vegetarian/vegan diet, distal RTA (type 1 — cannot acidify below 5.5), UTI with urease-producing organisms (*Proteus*: [[urea]] → NH₃ → alkaline), metabolic/respiratory alkalosis, citrate/bicarbonate therapy.

### Associated Pathologies

| Condition | pH Pattern | Key Symptoms |
|---|---|---|
| **[[uric-acid\|Uric acid]] stones** | Persistently acidic (<5.5) | Radiolucent stones; ~10% of all stones |
| **Distal RTA (Type 1)** | Cannot acidify <5.5 despite acidosis | CaPO₄ stones, nephrocalcinosis, metabolic acidosis |
| **UTI (Proteus)** | Alkaline >7.5 + struvite crystals | Staghorn calculi, recurrent UTI |
| **CaPO₄ stones** | Alkaline >6.5 | Brushite/apatite stones |

---

## Detection in Urine

### Clinical Assays

| Method | Principle | Resolution | Notes |
|---|---|---|---|
| **Dipstick pH indicator** | Methyl red + bromothymol blue; colour range orange (pH 5) to blue (pH 9) | 0.5–1.0 pH units | Rapid; affected by buffer overflow |
| **Glass electrode pH meter (gold standard)** | Hydrogen-ion-selective glass membrane; Nernstian potential | 0.01 pH units | Two-point calibration (pH 4.0 and 7.0) |
| **ISFET pH sensor** | Ion-sensitive FET with H⁺-sensitive gate | 0.01–0.1 pH | Solid-state, miniaturisable |

Gold standard: **Glass electrode pH meter** with two-point calibration.

Optimal specimen: **fresh specimen** — measure within 1 hour (CO₂ loss and bacterial action alkalinise urine). First morning urine typically most acidic.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Delayed analysis** | Falsely alkaline | CO₂ loss; bacterial urease splits [[urea]] → NH₃ |
| **Bacterial contamination** | Falsely alkaline | Urease-producing organisms |
| **Protein overflow onto pH pad** | Falsely acidic (dipstick) | Protein buffer interference |
| **Formaldehyde preservative** | Acidifies | Formic acid generation |
| **Strong buffer capacity** | Dipstick inaccurate | Overcomes indicator capacity |

### Spectroscopic Detection

**UV-Vis (indicator dye spectrophotometry):** Phenol red (558 nm), bromothymol blue (616 nm), methyl orange (507 nm). Absorbance ratio at indicator vs reference wavelengths; LOD ~0.05 pH units. Fibre-optic pH sensors embed indicator on fibre tip.

**NIR:** Water O-H absorption bands shift slightly with pH; multivariate models can estimate pH; LOD ~0.3 pH units.

**Fluorescence (pH-sensitive fluorophores):**

| Probe | Ex / Em | pKa | Resolution |
|---|---|---|---|
| SNARF-1 (ratiometric) | Ex 514 / Em 580+640 nm | ~7.5 | 0.01 pH |
| BCECF (ratiometric) | Ex 440/490 / Em 535 nm | ~6.97 | 0.01 pH |
| Fluorescein | Ex 490 / Em 520 nm | ~6.4 | 0.05 pH |
| Oregon Green | Ex 496 / Em 524 nm | ~4.7 | 0.05 pH |

**Raman:** H₂PO₄⁻/HPO₄²⁻ ratio (peaks at 875 vs 990 cm⁻¹) is pH-dependent (pKa 6.8). Not routinely used.

**FTIR:** Protonation state of [[phosphate]] and carboxylate groups changes with pH. Multivariate FTIR models can estimate pH; LOD ~0.2 pH units.

**Voltammetry:** Glass electrode and ISFET are inherently electrochemical. Iridium oxide (IrO₂) electrode shows super-Nernstian response (−70 mV/pH); LOD 0.01 pH; chip-compatible.

### Detection Methods Comparison

| Method | Resolution | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **Glass electrode** | 0.01 pH | Potentiometric | None | Gold standard |
| **Dipstick indicator** | 0.5–1.0 pH | Visual colour | None | Rapid, cheap |
| **ISFET** | 0.01–0.1 pH | FET gate potential | None | Solid-state, miniature |
| **IrO₂ electrode** | 0.01 pH | −70 mV/pH | None | Robust, chip-compatible |
| **SNARF-1 fluorescence** | 0.01 pH | Ex 514 / Em 580+640 nm | Probe addition | Ratiometric |
| **Fibre-optic optode** | 0.01 pH | Absorbance/fluorescence | None | Remote sensing |
| **NIR chemometrics** | ~0.3 pH | 1450–1940 nm | None | Non-contact |

---

## Sources

| # | Reference |
|---|---|
| 1 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 2 | Wikipedia — Urine Test Strip. https://en.wikipedia.org/wiki/Urine_test_strip |
| 3 | StatPearls — Renal Tubular Acidosis. https://www.ncbi.nlm.nih.gov/books/NBK519044/ |
| 4 | StatPearls — Urinalysis. https://www.ncbi.nlm.nih.gov/books/NBK557685/ |

---

## Gaps

- NIR-based pH prediction in urine requires per-device calibration and is sensitive to matrix variability
- Dipstick resolution (0.5–1.0 pH) is insufficient for stone management protocols requiring 0.1-unit precision
- Smartphone-based indicator colour analysis needs standardised illumination for consistent readings
- Effect of buffer capacity ([[phosphate]]-rich urine) on dipstick accuracy is incompletely characterised
