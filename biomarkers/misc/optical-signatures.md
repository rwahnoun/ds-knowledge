---
title: Urine Biomarker Optical Signatures — Reference Tables
aliases:
  - optical signatures
  - urine optical signatures
  - spectral signatures
  - LED biomarker mapping
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# Urine Biomarker Optical Signatures — Reference Tables

Single reference for absorbance, fluorescence, and scattering properties of urine biomarkers in the Jimini measurement range (275–1078 nm). See also: [[biomarker-panel]] [[feasibility-analysis]] [[literature]]

> [!IMPORTANT]
> Reagent-free detection is only feasible for analytes with strong intrinsic absorbance, fluorescence, or scattering (e.g., uric acid, hemoglobin, porphyrins). Electrolytes and most small molecules are optically transparent and require EIS or NIR indirect methods.

---

## Jimini Hardware

| Component | Specification | Role |
|---|---|---|
| **275 nm LED** | UV emitter | Uric acid absorbance; tryptophan/protein fluorescence excitation |
| **365 nm LED** | Near-UV emitter | NADH, riboflavin, hippuric acid fluorescence excitation |
| **405 nm LED** | Violet emitter | Porphyrin Soret band; bilirubin absorbance |
| **455 nm LED** | Blue emitter | Bilirubin peak; FAD/flavin excitation |
| **VIS / VISD** | Broadband visible | Hemoglobin Q-bands; urobilinogen |
| **R405** | Red/NIR | Extended scattering measurements |
| **C12 detector** | 321–870 nm | UV-Vis absorbance + fluorescence emission |
| **C14 detector** | 570–1078 nm | Vis-NIR absorbance + water overtone band |
| **EIS** | Electrochemical impedance | Ionic strength, conductivity, protein binding |
| **IRM-1070** | IR matrix sensor | NIR molecular overtones |

---

## LED → Biomarker Mapping

| LED (nm) | Absorbance Targets | Fluorescence Targets |
|---|---|---|
| **275** | Uric acid (290–295 nm), Tryptophan (280 nm), Tyrosine (274 nm), DNA/RNA (260–280 nm) | Tryptophan Em 330–350 nm (protein proxy), Indoxyl sulfate Em ~330 nm (CKD) |
| **365** | NADH (340–365 nm), bilirubin near-UV tail | NADH Em 440–470 nm, Riboflavin Em 520 nm, Hippuric acid Em 420 nm |
| **405** | Porphyrin Soret (405–415 nm), Bilirubin (415–450 nm), Hemoglobin Soret | Porphyrin Em 620–640 nm |
| **455** | Bilirubin peak (430–460 nm), FAD/Flavins (450 nm) | FAD Em 525 nm, Riboflavin Em 520 nm |
| **VIS broadband** | Hemoglobin Q-bands (541, 555, 576, 630 nm), Urobilinogen (440–500 nm) | — |

---

## C12 / C14 Detector Coverage

### C12 (321–870 nm)

| Range | Signals |
|---|---|
| 321–400 nm | Tryptophan emission (330–360 nm), UV fluorescence |
| 400–500 nm | NADH emission (440–470 nm), Flavin emission, Porphyrin Soret absorbance |
| 500–600 nm | Bilirubin absorbance, Hemoglobin Q-bands (541–576 nm), Riboflavin emission (520 nm) |
| 600–700 nm | Porphyrin emission (620–640 nm), Hemoglobin 630 nm band |
| 700–870 nm | NIR tail; water/turbidity scatter baseline |

### C14 (570–1078 nm)

| Range | Signals |
|---|---|
| 570–780 nm | Overlap with C12; hemoglobin absorption tails |
| 780–970 nm | First NIR window; lipid/protein overtones |
| 970–1078 nm | Water first overtone (~970 nm) — sensitive to ionic concentration, osmolality, specific gravity |

---

## Core Jimini Panel — Optical Signatures (200–1200 nm)

| Biomarker | λ (nm) / Type | EIS? | Notes |
|---|---|---|---|
| **Uric Acid** | 205, 230, 260, 293 (UV abs) | Yes (enzyme) | Strong π→π* transition; λ_max 292–294 nm; sits on complex UV background |
| **Creatinine** | 210, 235, 280 (UV abs) · 1600–2200 nm (NIR) | Interferent | 235 nm least interfered in UV; NIR preferred in complex matrix |
| **Urea** | 1400, 1800, 2000, 2200 nm (NIR) | Indirect | No UV chromophore; N-H/C=O vibrational overtones; water dominates NIR |
| **Glucose** | 210 (weak), 260–270 (weak UV) · full NIR | Yes (GOx) | No distinct chromophore; spectral fingerprinting + ML only |
| **Albumin** | 229, 280 (UV abs) · Ex 295→Em 340 (fluo) | Yes (immunosensor) | 229 nm distinct from creatinine at 249 nm; tryptophan fluorescence more sensitive |
| **Protein (Total)** | 220–230 (peptide bonds), 280 (aromatic) · Ex 280→Em 340 | Yes | Non-specific; multiple proteins contribute |
| **Porphyrins (TUP)** | 407 (Soret abs) · Ex 407→Em 620 (fluo) | — | High ε (~500,000 M⁻¹cm⁻¹); coproporphyrin Em 596/652, uroporphyrin Em 618/675 |
| **Porphobilinogen (PBG)** | Abs ~240 nm (out of range); 405 nm after heat conversion | — | Heat converts PBG → uroporphyrin (fluorescent); differential scan needed |
| **Bilirubin** | 450–460 (vis abs) | — | Liver disease; photolabile; ε ≈ 55,000 M⁻¹cm⁻¹ at 454 nm |
| **Red Blood Cells (RBC)** | 415/541/577 (oxyHb Soret+Q) · 660 (turbidity) | Yes | MetHb at 405 nm; hemolysis shifts spectrum; MALS for counting |
| **White Blood Cells (WBC)** | 660 (turbidity) · 260 (DNA, post-lysis) | Yes | Slightly larger than RBCs (~10–15 µm); MALS + ML for differentiation |
| **Bacteria** | 260 (DNA/RNA) · 660 (turbidity at >10⁵ CFU/mL) | Yes | Smaller particles (~1–5 µm) → more isotropic scatter |
| **Crystals** | 660 (turbidity; wavelength-independent scatter) | — | High RI → strong MALS signal; crystal type not distinguishable by bulk spectroscopy |
| **Cylinders (Casts)** | 660 (turbidity) · MALS (large cylindrical) | — | Tamm-Horsfall protein; cylindrical shape → anisotropic MALS profile |
| **Epithelial Cells** | 660 (scatter) · MALS | — | Large (>20 µm squamous); no unique spectral signature |
| **Oxalate** | 200, 220 (weak UV) | Yes (enzyme) | Direct optical challenging; indirect via crystal turbidity/MALS |
| **Osmolality** | Refractometry 589 nm proxy · NIR 970 nm (water overtone) | Yes (conductivity) | No direct chromophore; EIS conductivity is practical surrogate |
| **pH** | 434, 578 nm (indicator-based) · NIR water bands (indirect) | Yes (electrode) | NIR water-band shift with pH is very weak; indicator or electrode required |
| **Sodium** | 1450, 1940 nm (indirect NIR, exploratory) | Yes (ISE) | No direct chromophore; dominant urinary cation |
| **Potassium** | 1450, 1940 nm (indirect NIR, exploratory) | Yes (ISE) | No chromophore |
| **Chloride** | — | Yes (ISE) | Optically invisible |
| **Calcium** | 210–230 (very weak, as Ca-oxalate crystals) · 660 (turbidity) | Yes (ISE) | Dissolved Ca²⁺ optically transparent |
| **Magnesium** | — | Yes (ISE) | Optically invisible |
| **Phosphate** | — (820 nm with molybdate reagent) | Yes | Reagent required; inorganic phosphate UV-transparent |
| **NADH** | Ex 340–365→Em 440–470 (fluorescence) | — | Metabolic activity marker; oxidizes to NAD⁺ (non-fluorescent) over hours |
| **Riboflavin (B2)** | Ex 365/455→Em 520 (fluorescence) | — | Nutritional status; high quantum yield |

---

## Extended Analytes — Inflammation, Infection, Renal Injury

| Biomarker | Absorbance λ (nm) | Fluorescence λ (nm) | Notes |
|---|---|---|---|
| **Urobilinogen** | 490–500 | 500–520 | Product of bilirubin reduction; liver disease, hemolysis |
| **Hemoglobin / RBC** | 405–415, 540–580 | Non-fluorescent | Bleeding; see core panel above |
| **Myoglobin** | 405–410, 555–565 | Non-fluorescent | Muscle damage, rhabdomyolysis |
| **Leukocyte Esterase** | 490–510 (post-reaction) | 530–550 (post-reaction) | Enzyme from WBCs; dipstick wavelengths (reagent-dependent) |
| **Nitrite** | ~354 nm (weak native) · 540–550 (Griess reaction) | Non-fluorescent | Gram-negative bacteriuria; ε ~23 M⁻¹cm⁻¹ native — negligible at clinical conc. |
| **NAG** | 405–410 | 450–460 | Lysosomal enzyme; tubular cell damage |
| **Myeloperoxidase (MPO)** | 410–430 | Non-fluorescent | Neutrophil marker; inflammation |
| **Lactoferrin** | 280–295 | 320–360 | Iron-binding protein; elevated in infection |
| **NGAL** | 280–290 | 330–350 | Acute kidney injury marker |
| **Prostaglandin E2** | 230–240 | Non-fluorescent | Inflammatory mediator |
| **IL-6, IL-8, CRP** | Label-dependent (antibody conjugates) | Label-dependent | Require immunoassay; NOT detectable by direct spectroscopy |
| **Cortisol** | 247 | — | Cushing/Addison; stress |
| **Serotonin** | 220, 275, 299 | — | Carcinoid syndrome |
| **Dopamine / Norepinephrine / Epinephrine** | 218, 278 | — | Catecholamines; neuroblastoma, pheochromocytoma |
| **Indoxyl sulfate** | ~280 | ~330 | CKD uremic toxin; Ex 275→Em 330 |
| **Hippuric acid** | ~320 | ~420 | Gut bacteria, drug metabolism |

---

## Reagent-Free Detectability Summary

### What Works (High Confidence)

| Biomarker | Method | Jimini channel | Best reported |
|---|---|---|---|
| **Uric acid** | UV absorbance ~293 nm | 275 nm LED → C12 | R² > 0.95 (Beer-Lambert) |
| **Hemoglobin / hematuria** | Vis absorbance Soret + Q-bands | 405/VIS → C12 | R² = 0.99 (PLS 2nd deriv) |
| **Bilirubin** | Vis absorbance 344–450 nm | 405/455 → C12 | AUC = 0.92 (LRRE) |
| **Urobilinogen** | Vis absorbance ~490 nm | 455/VIS → C12 | AUC ~0.85 (LRRE) |
| **Porphyrins (TUP)** | Fluorescence Ex 405→Em 620 | 405 LED → C12 620 nm | Semi-quantitative |
| **Protein (indirect)** | Tryptophan fluorescence Ex 275→Em 335 | 275 LED → C12 330–360 nm | Semi-quantitative |
| **NADH** | Fluorescence Ex 365→Em 460 | 365 LED → C12 | Metabolic index |
| **Riboflavin** | Fluorescence Ex 365/455→Em 520 | 365/455 → C12 | Quantitative |
| **Specific gravity / osmolality** | Multi-wavelength + NIR water overtone | C14 970 nm + EIS | AUC ~0.85–0.89 |

### What Partially Works (Scatter / Fluorescence / EIS)

| Biomarker | Method | Jimini channels | Confidence |
|---|---|---|---|
| **WBC (pyuria)** | Mie scatter + NADH autofluorescence + EIS | A₁₀₇₀, ex365/em460, EIS | Low — binary Y/N |
| **Bacteria** | Scatter + flavin fluorescence + EIS | A₁₀₇₀, ex455/em525, EIS | Low-medium (>10⁵ CFU/mL) |
| **PBG** | Heat-induced conversion → Soret + fluorescence | A₄₀₅, A₄₀₅/A₄₈₀, ex405/em620 | Medium — binary acute attacks |
| **Crystals** | Scatter (wavelength-independent at large size) | A₁₀₇₀, A₈₀₀/A₄₀₀ → 1.0 | Low — binary |
| **Creatinine (NIR)** | NIR vibrational overtones | C14 900–1078 nm + PLS | R² ~0.7–0.85 |

### What Does NOT Work Reagent-Free (Visible Range)

| Biomarker | Why | Workaround |
|---|---|---|
| **Glucose** | No UV-Vis chromophore at physiological concentrations | NIR >1400 nm or EIS (GOx electrode) |
| **Albumin (quantitative)** | Colorless in visible | Fluorescence Ex 275→Em 335; or EIS immunosensor |
| **Creatinine (precise)** | UV peak at 234 nm (below 275 nm LED range) | NIR PLS or EIS |
| **Urea** | No UV-Vis chromophore | NIR >1400 nm + PLS |
| **Electrolytes (Na⁺, K⁺, Cl⁻, Mg²⁺)** | No optical signature | EIS conductivity (total ionic) or ISE |
| **Nitrites** | ε ~23 M⁻¹cm⁻¹ at 354 nm — negligible | Griess reagent cuvette or bacterial detection model |
| **Epithelial cells** | No unique chromophore; scatter only | Not separable from WBC/bacteria by bulk spectroscopy |

---

## Interferences & Mitigation

| Source | Effect | Mitigation |
|---|---|---|
| Urochrome, urobilin | Broad 400–500 nm absorbance baseline | 2nd derivative + ML; EMSC with reference spectrum |
| Ascorbate, drugs | Overlap at 260 nm (uric acid region) | Multi-wavelength PLS regression |
| Crystal precipitation | Turbidity drift across wavelengths | Heating + turbidity subtraction; EMSC scatter correction |
| Hemoglobin (RBC lysis) | 415, 541, 577 nm peaks (oxyHb); 405, 630 nm (metHb) | Flag artifact; Q-band ratio as freshness indicator |
| Temperature drift | Baseline shift; fluorescence quantum yield change | Peltier-controlled cell, ±0.1°C tolerance |
| Diet pigments | Variable 400–600 nm background | Robust PCA outlier removal |
| Bilirubin | Strong 400–500 nm overlap | A(454 nm) proxy; subtract scaled reference spectrum |
| pH drift | Shifts urobilin peak (~50 nm across pH 5–8); alters PBG conversion | Include pH as model covariate; EMSC pH-state references |
| Inner filter effect | Non-linear fluorescence at high absorbance | IFE correction: F_corr = F_obs × 10^((A_ex + A_em)/2) |

---

## Sources

| Reference | Notes |
|---|---|
| Fossati et al. *Clin Chem* 1980;26(2):227–231 | UV uric acid absorbance |
| Peters T. *Adv Clin Chem* 1970;13:37–111 | Protein UV absorption |
| Lim CK. *Methods Enzymol* 1986;123:383–405 | Porphyrin optical properties |
| Al-Awthan et al. *Spectrochim Acta A* 2020;229:117995 | NIR urea/creatinine PLS |
| Kuenert et al. *Sci Rep* 2025 | LED urine spectroscopy, n=401 |
| SpectraPhone *Sci Rep* 2026 | PLS R²=0.99 hematuria, albumin |
| See [[literature]] | Full numbered citation list with per-paper details |

## Gaps

- Catecholamines (dopamine, norepinephrine, epinephrine) at 218/278 nm: clinical relevance confirmed, but Jimini 275 nm LED sensitivity at physiological urine concentrations not validated
- Leukocyte esterase and nitrite wavelengths listed here are reagent-dependent — native (reagent-free) sensitivity uncharacterised for Jimini
- Cytokines (IL-6, IL-8, CRP): require immunoassay; listed for completeness only
- NIR water-band indirect ion sensing (1450/1940 nm): spectral changes at urine concentrations may be below Jimini C14 noise floor — needs experimental characterisation
- Albumin at 229 nm: distinct from creatinine at 249 nm in literature, but Jimini's lowest LED is 275 nm — direct absorption not accessible; fluorescence route only
