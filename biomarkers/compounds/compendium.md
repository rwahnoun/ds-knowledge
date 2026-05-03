---
title: Urinary Biomarkers Compendium
date: 2026-04-17
---

# Urinary Biomarkers Compendium

**A cross-analyte synthesis of 31 single-biomarker literature reviews**

*Usense Healthcare — Data Science · 2026-04-17*

---

## Executive Summary

This compendium synthesises the thirty-one single-biomarker literature reviews produced in the `singleBiomarkers` knowledge-base project. Each review covers identity, physiology, clinical relevance, and the full spectrum of detection methodologies — from routine dipstick chemistry to state-of-the-art SERS and quantum-dot sensors. The present document distils that corpus into a cross-analyte view: classification, physicochemical range, detection-technology coverage, spectroscopic fingerprint atlas, and the sensitivity gap between clinical assays and emerging research methods.

Three headline findings emerge:

- **Urinalysis spans eight orders of magnitude in concentration**, from [[urea]] (~300 mM) down to PFAS (~1 nM). No single detection modality can cover this span alone — a hybrid sensing architecture is essential.
- **Spectrophotometry remains the most widely deployed clinical technique** (18 of 31 biomarkers), followed by electrochemistry (12) and HPLC/LC-MS (13). Fluorescence and SERS are the fastest-growing research frontiers, each covering 15+ biomarkers at the research stage.
- **Emerging methods deliver 10²–10⁴× sensitivity gains** over clinical gold standards. The largest gaps exist for [[urea]] (×17,606 with SERS), nitrites (×11,000), and [[glucose]] (×2,800) — suggesting where point-of-care miniaturisation could make the greatest clinical impact.

---

## 1. Scope and Methodology

Each biomarker sheet in `outputs/` was generated to a strict template (Identity · Medical · Detection), and rendered to PDF individually. Structured data extracted from these sheets include chemical identity, typical urinary concentration, presence/absence in healthy urine, detection-method applicability, spectroscopic wavelengths and vibrational bands, and limits of detection (LOD). All cross-analyte figures in this document were built from that extracted dataset — see `generate_summary.py` in the repository root for the full data tables and plot code.

The 31 biomarkers were selected to cover the full clinical value of urinalysis at Usense:

- **Routine dipstick panel** — [[glucose]], ketones, bilirubin, blood ([[red-blood-cells|RBC]] / haemoglobin), nitrites, leukocyte esterase, pH, specific gravity, protein (via [[phosphate]]/osmolality context).
- **Electrolytes & renal function** — [[sodium]], [[chloride]], [[phosphate]], [[magnesium]], [[urea]], [[creatinin|creatinine]], [[uric-acid|uric acid]], osmolality.
- **Metabolic auto-fluorophores** — [[nadh|NADH]], [[fad|FAD]], riboflavin, [[tryptophan]] (intrinsic UV/blue fluorescence; probed by Usense's optical bench).
- **Porphyrin metabolites** — [[porphobilinogen]], total urinary porphyrin (red fluorescence signature).
- **Stone-risk and organic-acid markers** — oxalate, citrate.
- **Trace metal** — copper (Wilson disease).
- **Environmental contaminants** — metolachlor, PFAS, chlorothalonil.

---

## 2. Biomarker Landscape

### 2.1 Classification

![Figure 1 — Classification of 31 urinary biomarkers](fig1_classification.png){width=100%}

Metabolites (6) form the largest category, followed by cellular elements and electrolytes (4 each). Crucially, **19 of the 31 analytes are normally present in urine** and must therefore be quantified; the other **12 are normally absent** (or present at trace levels), so their detection often triggers a clinical flag.

### 2.2 Molecular-weight spectrum

![Figure 2 — Molecular weight spectrum of urinary biomarkers](fig2_molecular_weight.png){width=100%}

The analyte molecular weights span more than three orders of magnitude, from [[sodium]] (23 Da) to haemoglobin (64.5 kDa). This has direct consequences for method selection: small ions (Na⁺, Cl⁻, Mg²⁺) are ionically conductive but optically invisible in the UV–visible; medium-sized conjugated molecules (bilirubin, [[fad|FAD]], riboflavin, [[total-urinary-porphyrin|porphyrins]]) are the natural targets for absorbance and fluorescence; large proteins (haemoglobin, leukocyte esterase) are best addressed by immunoassay or activity-based chemistry.

### 2.3 Urinary concentration ranges

![Figure 4 — Urinary concentration ranges span eight orders of magnitude](fig4_concentration_ranges.png){width=100%}

The concentration landscape is the single most important design constraint for a multianalyte sensor. Major solutes ([[urea]], Na⁺, Cl⁻, [[phosphate]], [[creatinin|creatinine]]) sit in the 10–300 mM band, where tolerance to matrix effects outweighs raw LOD. Trace analytes (copper, [[total-urinary-porphyrin|porphyrins]], environmental contaminants) require sub-nanomolar sensitivity that only HPLC-MS, SERS, or targeted immunosensing can reach. The dynamic range of **eight orders of magnitude** rules out any single linear transducer; tiered chemistry (enzymatic amplification, sample dilution, preconcentration) is mandatory.

---

## 3. Detection Technology Landscape

### 3.1 Applicability matrix

![Figure 3 — Detection method applicability matrix](fig3_detection_heatmap.png){width=100%}

Each cell encodes whether a modality is **clinical / established (C)**, at **research stage (R)**, or **not applicable (—)** for a given biomarker. A few patterns stand out:

- **Spectrophotometry and electrochemistry** dominate the clinical column — they are the backbone of automated analysers and strip-based POC.
- **Fluorescence, Raman/SERS, and FTIR** are almost entirely in the research column. They promise reagent-free, multianalyte sensing but have yet to cross the clinical threshold for most targets.
- **HPLC/LC-MS** is clinically established for quantifying trace and regulatory-grade analytes ([[total-urinary-porphyrin|porphyrins]], PFAS, pesticides, [[nadh|NADH]]/[[fad|FAD]] in research contexts).
- **Flow cytometry and microscopy** are niche modalities restricted to cellular elements ([[red-blood-cells|RBC]], [[white-blood-cells|WBC]], [[bacteria]], leukocyte esterase).

### 3.2 Coverage by technology

![Figure 6 — Detection technology coverage across 31 biomarkers](fig6_method_coverage.png){width=100%}

Spectrophotometry covers the largest number of biomarkers at a clinical level (18), closely followed by HPLC/LC-MS (13) and electrochemistry (12). **Fluorescence and SERS** have the largest research-stage footprints (18 and 15 biomarkers respectively) — the most likely modalities to absorb new clinical targets in the next product cycle.

---

## 4. Spectroscopic Fingerprint Atlas

### 4.1 Optical landscape (UV-Vis & fluorescence)

![Figure 8 — Optical spectral landscape](fig8_wavelength_landscape.png){width=100%}

This is the single most operationally-relevant chart in the compendium. Each biomarker's primary **absorption maximum** (dark diamond) is plotted against the visible spectrum; fluorescent species additionally show **excitation (teal up-triangle)** and **emission (amber down-triangle)** markers linked by a coral Stokes-shift arrow. Dashed vertical lines mark common laser / LED excitation sources.

Key observations:

- **[[tryptophan|Tryptophan]]** (280 nm abs, 348 nm em) is the sole strong native UV fluorophore and drives any deep-UV optical design.
- **[[nadh|NADH]]** (340 nm → 460 nm) is a highly stoked biomarker that pairs naturally with a 365 nm UV-LED.
- **Flavins ([[fad|FAD]], riboflavin)** share a tight 450 → 525 nm excitation-emission pair — the classic green-autofluorescence channel. A single 450 nm laser diode excites both with ≥525 nm emission separation.
- **[[total-urinary-porphyrin|Porphyrins]]** have a characteristic large Stokes shift (405 → 620 nm) that cleanly separates them from flavins on the same violet-excitation platform.
- **Haemoglobin**'s Soret band at 415 nm with Q-bands at 542/577 nm is uniquely specific and non-fluorescent — a strong absorbance discriminator.
- **Bilirubin** (453 nm) and **[[glucose]]-POD product** (505 nm) sit in the blue-green absorbance window, enabling white-LED spectrometry.

### 4.2 Vibrational fingerprint atlas (Raman & FTIR)

![Figure 5 — Vibrational fingerprint atlas](fig5_spectroscopic_map.png){width=100%}

Raman (Panel A) and FTIR (Panel B) probe orthogonal selection rules but share the **1000–1700 cm⁻¹ biological fingerprint region** (shaded in teal). The most diagnostic bands are:

- **[[urea|Urea]]** — ν(C–N) at 1003 cm⁻¹ (Raman) and ν_as(C–N) at 1468 cm⁻¹ (FTIR). The Raman band is uniquely narrow and far from other urinary species, making it the most accessible target for Raman-based [[urea]] quantification.
- **[[creatinin|Creatinine]]** — 680 / 1490 cm⁻¹ (Raman) and 1492 cm⁻¹ (FTIR C=N) — complementary bands ideal for dual-modal detection.
- **[[uric-acid|Uric acid]]** — 630 cm⁻¹ ring-breathing mode is uniquely low and isolated, and 1680 cm⁻¹ C=O in FTIR provides secondary confirmation.
- **Nitrites, oxalate, citrate** — dominated by symmetric/asymmetric COO⁻ or NO₂ stretches that are strong in both Raman and FTIR, making ATR-FTIR a plausible multianalyte platform for organic-acid panels.
- **Flavins and [[total-urinary-porphyrin|porphyrins]]** — share isoalloxazine and Cβ-Cβ ring modes near 1350–1580 cm⁻¹ that enable SERS discrimination at picomolar sensitivity.

---

## 5. The Sensitivity Frontier

![Figure 7 — Clinical vs. research LOD: sensitivity gains from emerging technologies](fig7_lod_comparison.png){width=100%}

Figure 7 compares the best-of-class **clinical assay LOD** (teal) against the best-reported **research LOD** (amber) for ten representative biomarkers. The improvement factor (×, coral) reveals the sensitivity headroom available from next-generation chemistry.

- **[[urea|Urea]] (×17,606)** — SERS on Fe₃O₄@C@Ag nanostructures reaches 5.7 nM vs. ~0.1 mM for the urease-GLDH gold standard. This headroom is larger than typical urinary [[urea]] concentration, implying that SERS could enable drop-based quantification without dilution.
- **Nitrites (×11,000)** — SERS and fluorescence assays reach picomolar ranges vs. micromolar for Griess. Critical for early UTI detection before bacterial overgrowth.
- **[[glucose|Glucose]] (×2,800)** — fluorescence and SERS LODs of ~1 μM compare with ~2.8 mM for GOD-POD strips. Real-world gain is limited by urinary [[glucose]] variance, but meaningful for diabetic micro-urinary-[[glucose]] tracking.
- **Riboflavin (×1,000)** — LIF-CE reaches 100 pM; the physiological urinary baseline (~3 μM) is well above, so the gain translates directly into sub-second integration times.
- **[[creatinin|Creatinine]] (×18)** — the smallest gap: existing Jaffé and enzymatic assays are already excellent, and the research frontier is diminishing-returns territory.

**Strategic read:** The largest sensitivity gaps sit in biomarkers where **urinary concentration is close to the clinical assay LOD**. For those analytes ([[urea]] in dilute urine, [[glucose]] in early DM, nitrites in early UTI, riboflavin as a hydration / compliance marker), switching to a next-generation transducer unlocks clinically new information, not just a cleaner measurement.

---

## 6. Cross-Modality Design Implications for Usense

Synthesising the above figures and the underlying 31 sheets yields the following design principles for a multianalyte urinary panel:

1. **A dual optical-electrochemical platform is the minimum viable architecture.** Optical channels (UV-Vis 280–700 nm + fluorescence) cover ~20 of the 31 biomarkers natively; electrochemistry covers the remaining ionic / redox-active species (Na⁺, Cl⁻, [[phosphate]], pH, [[urea]], [[glucose]], [[uric-acid|uric acid]]).
2. **A 405 nm excitation source unlocks three orthogonal signals** — porphyrin emission at 620 nm, flavin emission at 525 nm, and haemoglobin Soret absorption. A single violet LED therefore pays for three biomarkers.
3. **A 365 nm source addresses [[nadh|NADH]] (em 460 nm)** for metabolic state and [[tryptophan]] (em 348 nm in near-UV). Combining 365 + 405 + 488 nm excitation yields a complete autofluorescence panel.
4. **ATR-FTIR is the most promising reagent-free multianalyte method** ([[urea]], [[creatinin|creatinine]], [[glucose]], [[uric-acid|uric acid]], ketones, nitrites, oxalate, citrate — all with >10⁻³ M bands). SERS gains sensitivity but loses throughput and reproducibility; FTIR wins for volume routine analysis.
5. **SERS should be reserved for ultra-trace targets** — pesticides, PFAS, sub-micromolar metabolites, early-infection nitrites. A SERS add-on channel maximises return on substrate cost.
6. **Dipstick chemistry remains irreplaceable** for rapid POC — leukocyte esterase, bilirubin, ketones, and blood are most reliably flagged by enzymatic strip reactions. The roadmap should augment, not replace, the paper strip.

---

## 7. Document Inventory

The full corpus of 31 single-biomarker sheets is available in `outputs/*.md` (source) and `papers/*.pdf` (rendered). Summary sheets are grouped below by category:

| Category | Biomarkers |
|---|---|
| **Metabolites** | [[glucose]], ketone, bilirubin, oxalate, citrate, [[uric-acid\|uric acid]] |
| **Cellular elements** | [[bacteria]], red blood cells, haemoglobin, white blood cells |
| **Electrolytes** | [[sodium]], [[chloride]], [[phosphate]], [[magnesium]] |
| **Physical properties** | pH, osmolality, USG (specific gravity) |
| **Coenzymes / vitamins** | [[nadh\|NADH]], [[fad\|FAD]], riboflavin |
| **Environmental contaminants** | metolachlor, PFAS, chlorothalonil |
| **Porphyrin metabolites** | [[porphobilinogen]], total urinary porphyrin |
| **Infection markers** | nitrites, leukocyte esterase |
| **Renal function** | [[urea]], [[creatinin\|creatinine]] |
| **Amino acid** | [[tryptophan]] |
| **Trace element** | copper |

Each sheet covers, at minimum: canonical identity (PubChem CID, SMILES, MW, structural formula); endogenous/exogenous origin; primary/secondary biological roles; catabolism and renal handling; normal serum and urinary reference ranges; factors modulating levels; associated pathologies; clinical assays with LOD and interferences; the current gold standard; and a research-methods inventory spanning UV-Vis, fluorescence, Raman/SERS, FTIR, voltammetry, and microfluidic / paper / MIP / thermal platforms. Every quantitative claim carries a peer-reviewed citation.

---

## 8. Key Take-Aways

- **Concentration is king.** The eight-order-of-magnitude urinary dynamic range forces any realistic panel to combine *amplifying* chemistries (enzymatic, SERS) with *high-capacity* linear transducers (spectrophotometry, electrochemistry).
- **Auto-fluorescence pays for itself.** [[nadh|NADH]], [[fad|FAD]], riboflavin, [[total-urinary-porphyrin|porphyrins]], and [[tryptophan]] form a self-consistent metabolic fluorescence panel from two UV-violet LEDs — no reagents, no consumables.
- **Raman-active fingerprint bands exist for every major organic solute.** A well-calibrated ATR-FTIR or SERS channel extracts [[urea]], [[creatinin|creatinine]], [[glucose]], [[uric-acid|uric acid]], ketones, nitrites, oxalate, and citrate from a single 5-μL droplet.
- **The research-stage LOD frontier offers ×10²–×10⁴ gains** — concentrated in trace-concentration analytes where sensitivity translates directly into new clinical utility (early infection, early dysglycaemia, environmental exposure).
- **Clinical dipstick chemistry is a floor, not a ceiling.** Every sheet identifies both the routine strip and a more sensitive research method; the roadmap is to preserve the former's speed while capturing the latter's sensitivity through integrated optical/electrochemical add-ons.

---

## Methods and Data Sources

All figures in this compendium were generated by `generate_summary.py` from structured data extracted verbatim from the 31 single-biomarker reviews in `outputs/`. The source literature for each data point is cited at the end of the corresponding biomarker sheet. All single-biomarker PDFs rendered by the `md2pdf` pipeline are archived in `papers/`.

Colour palette, typography, and branding follow the Usense navy / amber / teal design language. Plots were rendered with matplotlib 3.x (serif face: Cambria / Times New Roman). Wavelength-to-RGB mapping in Figure 8 follows a piecewise approximation of the CIE 1931 standard observer.

---

*End of compendium — 31 biomarkers, 8 figures, 1 view.*

[urea]: .plans/urea.md "Literature Review Plan — urea"
[glucose]: sheets/metabolites/glucose.md "Glucose"
[red-blood-cells|RBC]: sheets/infection-inflammation/red-blood-cells.md "Red Blood Cells"
[phosphate]: sheets/metabolites/phosphate.md "Phosphate"
[sodium]: sheets/metabolites/sodium.md "Sodium"
[chloride]: sheets/metabolites/chloride.md "Chloride"
[magnesium]: sheets/metabolites/magnesium.md "Magnesium"
[creatinin|creatinine]: sheets/metabolites/creatinin.md "Creatinine"
[uric-acid|uric acid]: sheets/metabolites/uric-acid.md "Uric Acid"
[nadh|NADH]: sheets/fluorophores/nadh.md "NADH (Reduced Nicotinamide Adenine Dinucleotide)"
[fad|FAD]: sheets/fluorophores/fad.md "FAD (Flavin Adenine Dinucleotide)"
[tryptophan]: sheets/fluorophores/tryptophan.md "Tryptophan"
[porphobilinogen]: sheets/pigments-porphyrins/porphobilinogen.md "Porphobilinogen"
[total-urinary-porphyrin|porphyrins]: sheets/pigments-porphyrins/total-urinary-porphyrin.md "Total Urinary Porphyrin"
[white-blood-cells|WBC]: sheets/infection-inflammation/white-blood-cells.md "White Blood Cells"
[bacteria]: sheets/infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[tryptophan|Tryptophan]: sheets/fluorophores/tryptophan.md "Tryptophan"
[total-urinary-porphyrin|Porphyrins]: sheets/pigments-porphyrins/total-urinary-porphyrin.md "Total Urinary Porphyrin"
[urea|Urea]: .plans/urea.md "Literature Review Plan — urea"
[creatinin|Creatinine]: sheets/metabolites/creatinin.md "Creatinine"
[uric-acid|Uric acid]: sheets/metabolites/uric-acid.md "Uric Acid"
[glucose|Glucose]: sheets/metabolites/glucose.md "Glucose"
[uric-acid\|uric acid]: sheets/metabolites/uric-acid.md "Uric Acid"
[nadh\|NADH]: sheets/fluorophores/nadh.md "NADH (Reduced Nicotinamide Adenine Dinucleotide)"
[fad\|FAD]: sheets/fluorophores/fad.md "FAD (Flavin Adenine Dinucleotide)"
[creatinin\|creatinine]: sheets/metabolites/creatinin.md "Creatinine"
