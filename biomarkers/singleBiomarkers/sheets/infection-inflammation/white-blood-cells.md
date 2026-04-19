---
title: White Blood Cells
aliases:
  - WBCs
  - Leukocytes
  - White cells
  - Pyuria
  - Leukocyturia
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

# White Blood Cells

Cellular marker for pyuria (urinary tract inflammation). Predominantly neutrophils (~95% of urinary [[white-blood-cells|WBC]]). [[white-blood-cells|WBC]] casts indicate renal parenchymal inflammation. Detection by dipstick (leukocyte esterase) or microscopy. See [[datascience/spectroscopy-biomarkers]] for optical detection context and [[red-blood-cells]] for comparative cellular biomarker context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | White Blood Cells (Leukocytes) |
| **Other names** | [[white-blood-cells\|WBC]], leukocytes, white cells |
| **Nature** | Nucleated immune cells |
| **Size** | 10–15 µm (neutrophils), 7–10 µm (lymphocytes), up to 20 µm (monocytes) |
| **Predominant type in urine** | Neutrophils (~95% of urinary [[white-blood-cells\|WBC]]) |
| **Normal blood count** | 4,000–11,000/µL |

[[white-blood-cells|WBC]] in urine (pyuria) indicate an inflammatory process in the urinary tract. Neutrophils are the dominant type, recruited by chemokines (IL-8, C5a) from blood vessels to the bladder wall, ureter, or renal parenchyma. [[white-blood-cells|WBC]] casts (tubular casts containing [[white-blood-cells|WBC]]) indicate renal parenchymal inflammation (pyelonephritis, interstitial nephritis).

### Entities Not to Be Confused With

| Entity | Description | Key Difference |
|---|---|---|
| **Red blood cells** | Anucleate, 6–8 µm, biconcave | Smaller, no nucleus, no granules |
| **Renal tubular epithelial cells** | 12–20 µm, round nucleus | Slightly larger; single large round nucleus |
| **Transitional epithelial cells** | 20–40 µm, variable shapes | Much larger |
| **[[[[bacteria]]\|Bacteria]]** | 0.5–3 µm | Much smaller; no internal structure by LM |

---

## Medical Information

### Origin

**Endogenous:** [[white-blood-cells|WBC]] produced in **bone marrow** from HSCs. Neutrophils mature over ~14 days, circulate for 6–10 hours. In urinary tract inflammation, neutrophils migrate through the urothelium into the urine.

**Exogenous:** None. [[white-blood-cells|WBC]] in urine originate exclusively from the patient's immune system.

### Biological Roles

- **Primary:** Immune defence — neutrophils phagocytose and kill pathogens through oxidative burst (ROS), degranulation (MPO, elastase), and NETs.
- **Inflammation mediators:** Release cytokines (TNF-α, IL-1β) and lipid mediators.
- **Tissue damage markers:** Eosinophils in urine suggest allergic interstitial nephritis or parasitic infection.

### Elimination Pathway

Neutrophils in urine undergo apoptosis and lysis within hours. Enzymes released during lysis (leukocyte esterase) can be detected by dipstick even after cells disintegrate. In the body, apoptotic neutrophils are cleared by macrophages (efferocytosis).

### Clinical Levels

| Compartment | Reference Range |
|---|---|
| **Blood [[white-blood-cells\|WBC]] count** | 4,000–11,000/µL |
| **Urine [[white-blood-cells\|WBC]] (microscopy)** | 0–5 [[white-blood-cells\|WBC]]/HPF |
| **Urine [[white-blood-cells\|WBC]] (flow cytometry)** | <25 [[white-blood-cells\|WBC]]/µL (Sysmex UF) |
| **Dipstick leukocyte esterase** | Negative |

### Factors Influencing Levels

**Increased [[white-blood-cells|WBC]] in urine (pyuria):** UTI (most common), pyelonephritis, interstitial nephritis, glomerulonephritis, renal transplant rejection, urolithiasis, bladder cancer, vaginal/cervical contamination, prostatitis.

### Associated Pathologies

| Condition | [[white-blood-cells\|WBC]] Pattern | Key Symptoms |
|---|---|---|
| **Uncomplicated cystitis** | >10 [[white-blood-cells\|WBC]]/HPF + [[bacteria]] | Dysuria, frequency, urgency |
| **Pyelonephritis** | [[white-blood-cells\|WBC]] + [[white-blood-cells\|WBC]] casts + [[bacteria]] | Fever, flank pain, nausea |
| **Sterile pyuria** | [[white-blood-cells\|WBC]] without [[bacteria]] on culture | TB, interstitial nephritis, STIs, nephrolithiasis |
| **Drug-induced interstitial nephritis** | [[white-blood-cells\|WBC]] + eosinophils + [[white-blood-cells\|WBC]] casts | AKI after drug exposure; eosinophiluria pathognomonic |
| **Renal transplant rejection** | [[white-blood-cells\|WBC]] + tubular epithelial cells | Rising [[creatinin\|creatinine]] post-transplant |

### Presence in Urine

Trace amounts (≤5 [[white-blood-cells|WBC]]/HPF) are normal. Greater numbers define pyuria. Form: **intact nucleated cells**, predominantly neutrophils. May degenerate into "glitter cells" (swollen neutrophils with brownian granular motion) in hypotonic urine. [[white-blood-cells|WBC]] casts indicate renal origin.

---

## Detection in Urine

### Clinical Assays

| Method | Principle | LOD | Notes |
|---|---|---|---|
| **Dipstick leukocyte esterase (LE)** | Esterase from lysed neutrophils hydrolyses indoxyl ester → indoxyl + diazonium salt → violet azo dye | ~10–25 [[white-blood-cells\|WBC]]/µL | ~550 nm (violet dye); sensitivity 75–90%, specificity 65–80%; detects lysed cells |
| **Urine sediment microscopy** | Centrifuged sediment at 400x; [[white-blood-cells\|WBC]] 12 µm, visible nucleus and granules | ~1 [[white-blood-cells\|WBC]]/HPF | Gold standard for count + morphology + casts; operator-dependent |
| **Automated flow cytometry (Sysmex UF-5000)** | Fluorescent nucleic acid dye + scatter; [[white-blood-cells\|WBC]] show strong fluorescence (nucleated) | ~5 [[white-blood-cells\|WBC]]/µL | Ex 488 nm; rapid, objective; no subtyping or cast ID |

Gold standard: **Manual microscopy** of centrifuged sediment at 400x. Automated analysers (Sysmex UF) used for screening with reflex to microscopy for abnormal results.

Optimal specimen: **midstream clean-catch**; analyse within 1–2 hours ([[white-blood-cells|WBC]] lyse rapidly in hypotonic/alkaline urine). Avoid vaginal contamination in women.

### Interferences

| Interference | Effect | Mechanism |
|---|---|---|
| **Vaginal contamination** | False positive | Vaginal leukocytes, epithelial cells |
| **Oxidising agents (hypochlorite)** | False positive (LE) | Chemical oxidation of substrate |
| **High [[glucose]] (>3 g/dL)** | False negative (LE) | Inhibits enzymatic reaction |
| **High albumin (>500 mg/dL)** | False negative (LE) | Enzyme inhibition |
| **Tetracycline, cephalexin** | False negative (LE) | Drug inhibition of esterase activity |
| **Delayed analysis** | Decreased [[white-blood-cells\|WBC]] count (microscopy) | Cell lysis in old specimen |

### Spectroscopic Detection

**UV-Vis:** No direct spectroscopic method for [[white-blood-cells|WBC]]. Myeloperoxidase (MPO) from neutrophils has a Soret-like absorption at **430 nm**, but concentrations in urine are too low for direct detection. Turbidimetry loosely correlates with high [[white-blood-cells|WBC]]/bacterial counts but is non-specific.

**Fluorescence:**
- **Nucleic acid staining (flow cytometry):** Polymethine/acridine orange dyes bind [[white-blood-cells|WBC]] DNA/RNA. Ex 488 nm / Em 520 nm (DNA), Em >600 nm (RNA). LOD ~5 [[white-blood-cells|WBC]]/µL.
- **Immunofluorescence (CD45-FITC):** Pan-leukocyte marker. Ex 490 / Em 520 nm. LOD ~1 [[white-blood-cells|WBC]]/µL. Specific but labour-intensive.
- **Calcein-AM viability staining:** Live [[white-blood-cells|WBC]] convert calcein-AM → fluorescent calcein. Ex 495 / Em 515 nm. LOD ~10 [[white-blood-cells|WBC]]/µL.

**Raman:** [[white-blood-cells|WBC]] spectra reflect biomolecular composition. Key peaks:

| Peak (cm⁻¹) | Assignment |
|---|---|
| **~720–730** | Adenine (DNA) |
| **~780** | Cytosine/uracil (nucleic acids) |
| **~1003** | Phenylalanine |
| **~1340** | CH₂ wagging (proteins) |
| **~1660** | Amide I |

Single-cell confocal Raman (Ex 532 or 785 nm) can distinguish neutrophils, lymphocytes, and monocytes by spectral differences. LOD: single cell. Sample prep: centrifuge, transfer to optical substrate.

**FTIR:** Key bands: ~1080 cm⁻¹ (PO₂⁻ sym., DNA; higher DNA content than [[red-blood-cells|RBC]]), ~1240 cm⁻¹ (PO₂⁻ asym., DNA), ~1540 cm⁻¹ (Amide II), ~1650 cm⁻¹ (Amide I). ATR-FTIR on dried sediment can detect [[white-blood-cells|WBC]] at high concentrations (>10⁴/µL); can potentially distinguish infected vs non-infected urine by spectral profile.

**Voltammetry:**
- **MPO electrochemistry:** MPO peroxidase activity detected on modified electrodes. LOD ~0.1 ng/mL MPO.
- **Impedance cytometry (microfluidic):** Single-cell counting and sizing. LOD ~10 cells/µL; prototype stage.

### Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths | Limitations |
|---|---|---|---|---|---|
| **Dipstick LE** | ~10–25 [[white-blood-cells\|WBC]]/µL | ~550 nm (violet dye) | None | Rapid, cheap, detects lysed cells | Non-specific, false positives |
| **Microscopy** | ~1 [[white-blood-cells\|WBC]]/HPF | 400x light microscopy | Centrifugation | Gold standard, morphology + casts | Operator-dependent |
| **Flow cytometry (Sysmex)** | ~5 [[white-blood-cells\|WBC]]/µL | Ex 488 nm / scatter | None | Automated, fast | No subtyping |
| **Immunofluorescence (CD45)** | ~1 [[white-blood-cells\|WBC]]/µL | Ex 490 / Em 520 nm | Fixation + antibody | Specific for [[white-blood-cells\|WBC]] | Labour-intensive |
| **Single-cell Raman** | Single cell | Ex 532/785 nm; 1003 cm⁻¹ | Concentrate | Cell-type identification | Specialised |
| **FTIR** | >10⁴/µL | 1080+1650 cm⁻¹ | Dry pellet | Multianalyte | Low sensitivity |
| **Impedance cytometry** | ~10/µL | Impedance | Microfluidic | Label-free, real-time | Prototype stage |
| **AI digital microscopy** | ~5 [[white-blood-cells\|WBC]]/µL | Digital imaging | None/auto | Automated, objective | Instrument cost |

---

## Sources

| # | Reference |
|---|---|
| 1 | RCPA Manual — Urine Dipstick. https://www.rcpa.edu.au/Manuals/RCPA-Manual/Pathology-Tests/U/Urine-dipstick |
| 2 | PMC — [[white-blood-cells\|WBC]] and Nitrite Sensitivity/Specificity. https://pmc.ncbi.nlm.nih.gov/articles/PMC8253458/ |
| 3 | StatPearls — Pyuria. https://www.ncbi.nlm.nih.gov/books/NBK537089/ |
| 4 | StatPearls — Urinalysis. https://www.ncbi.nlm.nih.gov/books/NBK557685/ |
| 5 | Sysmex — UF-5000 automated urine analyser. https://www.sysmex.com/ |
| 6 | AAFP — Dipstick Urinalysis for UTI. https://aafp.org/pubs/afp/issues/2013/0515/od2.html |

---

## Gaps

- Dipstick LE cannot quantify [[white-blood-cells|WBC]] or distinguish cell types — microscopy remains obligatory for cast identification and aetiology assessment
- Sterile pyuria workup (TB, interstitial nephritis) requires additional targeted tests not addressed by standard urinalysis
- Eosinophiluria (allergic interstitial nephritis marker) requires specialised staining (Hansel's or Wright's) not available on standard platforms
- FTIR spectral profiling of infected vs non-infected urine is promising but has not been validated in prospective clinical cohorts
- Single-cell Raman can subtype [[white-blood-cells|WBC]] but is far from a clinical-scale tool
