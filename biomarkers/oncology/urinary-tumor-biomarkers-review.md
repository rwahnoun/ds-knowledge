---
title: Systematic Review — Urinary Tumor Biomarkers Detectable via Optical and Electrochemical Methods
aliases:
  - Urinary Biomarkers Review Oncology2
  - Jimini Biomarker Compatibility Review
  - Oncology2 Claude Systematic Review
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/literature
  - status/complete
date: 2026-04-19

---

# Systematic Review: Urinary Tumor Biomarkers Detectable via Optical and Electrochemical Methods

> [!NOTE]
> Comprehensive systematic review mapping urinary tumor biomarkers to optical and electrochemical detection feasibility, with Jimini device compatibility assessment. Date: 2026-04-15. Related: [[datascience/spectroscopy-biomarkers]] [[optical-properties]] [[signatures]] [[signal-processing]]

## Executive Summary

Urine represents a uniquely accessible biofluid for non-invasive cancer diagnostics. This review catalogs urinary tumor biomarkers across four classes — **proteins**, **nucleic acids** (ctDNA, microRNA), **extracellular vesicles** (exosomes), and **metabolites** (including fluorescent metabolites such as [[nadh|NADH]], [[fad|FAD]], and [[tryptophan]]) — and systematically maps their detection by optical and electrochemical biosensors. Meta-analyses and reviews published 2000–2026 are prioritised. Each biomarker's clinical utility (screening, treatment monitoring, recurrence detection) is assessed alongside compatibility with the Jimini device platform (UV-Vis-NIR spectrophotometry at 275/365/405/455 nm + broadband visible, NIR matrix, and EIS).

## Biomarker Classes and Detection Methods

### Protein Biomarkers

Protein tumor markers in urine include both organ-specific antigens and broadly secreted oncoproteins.

| Biomarker | Cancer Type | Normal Range | Clinical Use |
|-----------|-------------|-------------|--------------|
| PSA | Prostate | <4 ng/mL (serum); trace in urine | Screening, monitoring |
| PCA3 | Prostate | PCA3 score (mRNA ratio) | Diagnosis (FDA-approved Progensa) |
| NMP22 | Bladder | <10 U/mL | Screening, recurrence surveillance (FDA-approved) |
| BTA | Bladder | Negative (qualitative) | Screening (FDA-approved BTA Stat/TRAK) |
| Survivin | Bladder | Absent in normal | Diagnosis candidate |
| CYFRA 21-1 | Bladder, Lung | <3.3 ng/mL | Monitoring |
| CEA | Colorectal, Bladder | <2.5 ng/mL (serum) | Recurrence monitoring |
| HER2/ErbB2 | Breast, Bladder | Variable | Treatment response |
| CA-125 | Ovarian | <35 U/mL (serum) | Monitoring |
| EpCAM | Pan-carcinoma | Low in normal urine | CTC/exosome marker |
| VEGF | Multiple | Low pg/mL | Angiogenesis marker |
| MMP-2, MMP-9 | Bladder | Low | Invasion markers |
| TMPRSS2-ERG fusion | Prostate | Absent normally | Diagnosis (mRNA in urine) |

**Electrochemical immunosensors** are the dominant approach for urinary protein biomarkers:

| Biomarker | Sensor | LOD | Principle |
|-----------|--------|-----|---------|
| PSA | ITO-PET disposable aptasensor | 8.74 fg/mL | Voltammetry |
| PSA | AuNP-modified GCE | 0.5 pg/mL | Amperometry |
| PSA | Silicon nanowire aptasensor | — | Label-free |
| NMP22 | AuNPs-PtNPs-MOFs on SPCE | Low pg/mL | EIS |
| CEA | GO nanocomposite biosensor | 0.3 pg/mL | DPV |
| CEA | Ag/Au NP graphene sandwich | 8 pg/mL | Amperometry |
| HER2 | AuNP-rGO-SWCNT impedimetric aptasensor | 0.1 pg/mL | EIS |
| EpCAM | AgNP-chitosan microfluidic | 2.7 pg/mL | Voltammetry |

**Optical biosensors** for urinary proteins include fluorescence immunoassays, SPR, and intrinsic protein fluorescence at Ex 280/Em 340 nm ([[tryptophan]], non-tumor-specific).

### Nucleic Acid Biomarkers (ctDNA, microRNA)

#### Cell-Free DNA / ctDNA

| Biomarker | Cancer | Clinical Use | Stage |
|-----------|--------|-------------|-------|
| TERT promoter mutations | Bladder (~55% cases) | Diagnosis, recurrence | Validated (multi-gene panels) |
| FGFR3 mutations | Bladder (30–50%) | Diagnosis, low-grade NMIBC | Validated |
| TP53 mutations | Bladder (24%), multiple | Monitoring, prognosis | Validated |
| PIK3CA mutations | Bladder (~35%) | Diagnosis | Research |
| KRAS mutations | Colorectal, lung, pancreatic | Monitoring | Research |
| DNA methylation (RASSF1A, TWIST1, NID2, OTX1) | Bladder | Diagnosis, recurrence | Validated (EpiCheck, AssureMDx) |
| Trans-renal cfDNA | Distant cancers | Screening | Research |

**Electrochemical DNA biosensors:**
- KRAS: screen-printed gold electrode, LOD = 10 fM (Garcia-Melo et al., 2022)
- CRISPR/Cas12a for EGFR L858R: LOD = 3.3 attomolar (Liu et al., 2022)
- DNA methylation: polymer nanobead electrochemical assay detects 5% methylation in 10 ng DNA

#### MicroRNA (miRNA)

| miRNA | Cancer | Clinical Use | Key Evidence |
|-------|--------|-------------|-------------|
| miR-21 | Bladder, prostate, breast | Diagnosis, prognosis | Pooled sensitivity 75%, specificity 76% (meta-analyses) |
| miR-155 | Breast, lung | Diagnosis | CRISPR/Cas13a biosensor: LOD = 0.2 fM |
| miR-200 family | Bladder | Prognosis | Exosomal; stable in urine |
| miR-126 | Bladder | Diagnosis, recurrence | Multiple validation studies |
| miR-141-3p | Prostate | Diagnosis | Candidate |
| miR-125 | Breast | Diagnosis | Multiplex biochip validated |
| miR-191 | Breast | Diagnosis | Multiplex biochip validated |
| miR-19b, miR-20a | Multiple | Diagnosis | CRISPR/Cas13a: fM sensitivity |

**Electrochemical biosensors for miRNA:**
- CRISPR/Cas13a microfluidic biosensor: amplification-free, fM-level sensitivity (Bruch et al., 2019)
- PPy/AuNPs/graphene aptasensor for miR-21: LOD = 0.1 fM
- Microfluidic biochip: simultaneous detection of 20 miRNAs in 35 min, attomolar sensitivity

**Optical biosensors for miRNA:**
- QD-molecular beacon fluorescence assays
- SERS with RCA for miR-21: LOD = 0.4 fM, miR-155: LOD = 0.2 fM
- Colorimetric AuNP aggregation assays

### Extracellular Vesicles (Exosomes)

Urinary exosomes (50–200 nm) carry tumor-derived proteins, DNA, and RNA. Meta-analysis of 16 studies (3,224 patients) showed pooled sensitivity 0.81 and specificity 0.76 for urological tumor diagnosis (Chen et al., Front Oncol, 2021).

| Exosome Cargo | Cancer | Clinical Use |
|---------------|--------|-------------|
| Exosomal miR-21 | Bladder | Diagnosis, prognosis (sensitivity 75–87%) |
| Exosomal miR-200 family | Bladder | Prognosis (stable in urine) |
| Exosomal PCA3 mRNA | Prostate | Diagnosis (ExoDx Prostate test — approved) |
| Exosomal PSMA | Prostate, breast | Subtyping |
| Exosomal EGFR | Glioblastoma, lung | Diagnosis |
| Exosomal CD81, CD63, CD9 | Pan-cancer | General EV markers (capture/quantification) |
| Exosomal survivin | Bladder | Diagnosis (high accuracy reported) |

**Detection methods:**

| Platform | LOD | Application |
|----------|-----|-------------|
| Zr-MOF/MB electrochemical chip | 10⁴ particles/mL | Exosome quantification |
| FEMC microfluidic chip | 10⁴ particles/mL | PSMA, EGFR, CD81, CEA simultaneous |
| NTA | Size/concentration | Non-specific |
| SPR with anti-CD63/CD81 | Single exosome | Optical |
| SERS-based profiling | — | Tumour subtyping classification |
| Optical nanobiosensors | Single exosome | Plasmonic (Cancer Cell Int., 2024) |

### Metabolite Biomarkers

Cancer alters metabolic pathways, producing detectable changes in urinary metabolites:

| Metabolite | Cancer | Detection | Key Evidence |
|------------|--------|-----------|-------------|
| [[[[tryptophan]]\|Tryptophan]] / Kynurenine pathway | Melanoma, bladder, colorectal | Fluorescence Ex 275–295/Em 340–360 nm | Urine autofluorescence at 295 nm significantly higher in melanoma; decreases with stage (Štrumfa et al., 2021) |
| [[nadh\|NADH]] | Multiple (metabolic shift) | Fluorescence Ex 340/Em 460 nm | Warburg effect; detectable as bulk fluorescence in urine |
| [[fad\|FAD]] | Multiple | Fluorescence Ex 450/Em 525 nm | Metabolic redox indicator; [[nadh\|NADH]]/[[fad\|FAD]] ratio reflects mitochondrial function |
| Pterins (neopterin, biopterin) | Bladder, immune activation | Fluorescence Ex 365/Em 450 nm | Neopterin elevated in malignancy and inflammation |
| [[total-urinary-porphyrin\|Porphyrins]] | Bladder, colorectal | Fluorescence Ex 405/Em 630 nm | Coproporphyrin elevated in some cancers |
| 5-HIAA | Carcinoid/neuroendocrine | UV absorbance ~275 nm | Gold standard for carcinoid tumors |
| Polyamines (spermine, spermidine) | Multiple | Derivatization needed | Elevated in rapidly proliferating tumors |
| Lactate | Multiple | Electrochemical enzyme electrode (LOx) | Warburg effect marker |
| VOCs | Bladder, prostate | GC, e-nose | Urinary VOC profiles distinguish cancer vs. healthy |
| Urinary fluorescent metabolome | Endometrial, bladder | Multi-wavelength EEM + ML | Endometrial cancer: 94% accuracy (Cancers, 2024) |

**Urine Autofluorescence Spectroscopy (reagent-free cancer screening):**

| Cancer | Finding | Reference |
|--------|---------|-----------|
| Bladder | Statistically significant spectral differences vs. controls via UV-Vis fluorescence + absorbance | Jałocha-Bratek et al., Sci Rep 2025 |
| Melanoma | [[[[tryptophan]]\|Tryptophan]] autofluorescence (295 nm) significantly elevated in early-stage; decreases with advancing stage | Štrumfa et al., IJMS 2021 |
| Multi-cancer | EEMs at 280/330/365/405 nm excitation discriminate cancer from normal with >80% sensitivity in double-blind studies | Masilamani et al., 2010; Al-Shukri, 2021 |
| Endometrial | Urinary fluorescent metabolome profiling with ML: 94% screening accuracy | Kalinowska et al., Cancers 2024 |

## Comparative Tables

### Biomarker × Detection Method × LOD × Clinical Validation

| Biomarker | Cancer | Detection Method | Principle | LOD | Linear Range | Validation |
|-----------|--------|-----------------|---------|-----|-------------|-----------|
| PSA | Prostate | EC aptasensor (ITO-PET) | Voltammetry | 8.74 fg/mL | — | Serum validated |
| PSA | Prostate | AuNP-GCE immunosensor | Amperometry | 0.5 pg/mL | 2 pg/mL–10 ng/mL | Validated |
| PSA | Prostate | Microfluidic CNF/Au | EIS | 5 pg/mL | 0.01–50 ng/mL | 30 patients |
| PCA3 mRNA | Prostate | MXene QD EC biosensor | Voltammetry | Low fM | — | Candidate |
| NMP22 | Bladder | AuNPs-PtNPs-MOFs/SPCE | EIS/DPV | pg/mL | — | FDA-approved (ELISA) |
| NMP22 | Bladder | AuNPs@OMC-Thi@Gr-COOH | Label-free EC | pg/mL | — | Candidate |
| BTA | Bladder | Immunochromatography | Colorimetric | Qualitative | — | FDA-approved |
| CEA | Colorectal | GO nanocomposite/GCE | DPV | 0.3 pg/mL | 0.1 pg/mL–1000 ng/mL | Candidate |
| CEA | Multiple | Ag-Au NP/graphene sandwich | Amperometry | 8 pg/mL | 10–1.2×10⁵ pg/mL | Spiked serum |
| HER2 | Breast | AuNP-rGO-SWCNT | EIS | 0.1 pg/mL | 0.1 pg/mL–1 ng/mL | Candidate |
| EpCAM | Pan-cancer | AgNP-chitosan microfluidic | Voltammetry | 2.7 pg/mL | 2.7–2000 pg/mL | Spiked blood |
| miR-21 | Multiple | PPy/AuNPs/graphene | Voltammetry | 0.1 fM | 1 fM–1 µM | Candidate |
| miR-155 | Breast | Graphene FET | Conductance | 1.92 fM | 10 fM–100 pM | Serum + sweat |
| miR-19b/20a | Multiple | CRISPR/Cas13a microfluidic | EC amperometry | fM | — | Candidate |
| KRAS mutation | CRC, lung | Au screen-printed genosensor | DPV | 10 fM | 10 fM–1 µM | Candidate |
| ctDNA EGFR L858R | NSCLC | CRISPR/Cas12a EC sensor | Ratiometric | 3.3 aM | — | Patient plasma |
| DNA methylation | Bladder | Polymer nanobead EC | Amperometry | 5% methylation/10 ng | — | Candidate |
| Exosomes (EGFR+) | Glioblastoma | Zr-MOF/MB EC | DPV | 7.83×10³ particles/µL | — | Candidate |
| Exosomes (multi-marker) | Breast | FEMC microfluidic | EC multiplex | 10⁴ particles/mL | — | Clinical + murine |
| [[[[tryptophan]]\|Tryptophan]] fluorescence | Melanoma | Autofluorescence | Fluorescence Ex 295/Em 340 | µM range | — | Clinical (n>100) |
| Urinary fluorescent metabolome | Endometrial | Multi-λ EEM + ML | Fluorescence | — | — | 94% accuracy |
| Spectral signature | Bladder | UV-Vis fluorescence + absorbance | Optical | — | — | Clinical (2025) |
| [[nadh\|NADH]]/[[fad\|FAD]] ratio | Multiple | FLIM / bulk fluorescence | Fluorescence | µM–mM | — | Research |
| [[total-urinary-porphyrin\|Porphyrins]] | Bladder, CRC | Fluorescence | Fluorescence Ex 405/Em 630 | µM range | — | Candidate |
| Lactate | Multiple | LOx enzyme electrode | Amperometry | µM range | — | Organ-on-chip |
| [[[[glucose]]\|Glucose]] | Multiple | GOx-EIS | EIS | µM range | — | Well-established |

### Cancer Type × Biomarker Role

| Cancer | Diagnostic Biomarkers | Monitoring/Pharmacodynamic Biomarkers | Recurrence/MRD Biomarkers |
|--------|----------------------|--------------------------------------|--------------------------|
| Bladder | NMP22, BTA, UroVysion FISH, miR-21, miR-126, FGFR3 mut., TERT promoter mut., DNA methylation (TWIST1, NID2), exosomal miR-21, urinary spectral signature | Exosomal survivin, NMP22 kinetics, CEA | TERT promoter mutations, FGFR3, methylation panels (EpiCheck, AssureMDx), Cxbladder Monitor, miR-200 family |
| Prostate | PSA (urine), PCA3 (mRNA score), TMPRSS2-ERG fusion, exosomal PCA3/ERG (ExoDx), [-2]proPSA/PHI | PSA kinetics, PSMA+ exosomes | PCA3 score changes, ctDNA (TP53, PTEN), miR-141-3p |
| Breast | miR-125, miR-155, miR-21, miR-191, HER2/ErbB2, CA 15-3, exosomal miRNA panels | HER2 shedding, CEA, miRNA panels, metabolic markers (lactate) | Exosomal EGFR, miR-21, ctDNA mutations |
| Renal Cell Carcinoma | Aquaporin-1 (AQP1), PLIN2, KIM-1, CAIX, urinary metabolome | VEGF, CRP | cfDNA, exosomal cargo |
| Colorectal | CEA, KRAS mutations (trans-renal cfDNA), miR-21, [[total-urinary-porphyrin\|porphyrins]] | CEA levels, ctDNA dynamics | KRAS/BRAF ctDNA, DNA methylation |
| Endometrial | Urinary fluorescent metabolome, miRNA panels | Not established | Not established |
| Melanoma | [[[[tryptophan]]\|Tryptophan]] autofluorescence (Ex 295 nm), tyrosinase | [[[[tryptophan]]\|Tryptophan]]/Clark stage correlation | Urinary [[tryptophan]] monitoring |
| Lung (NSCLC) | ctDNA (EGFR mutations), CEA, NSE, miR-21/miR-155, VOC profiles | ctDNA dynamics, CYFRA 21-1 | EGFR ctDNA (CRISPR biosensor) |
| Ovarian | CA-125, HE4, exosomal miRNA | CA-125 kinetics | ctDNA, methylation panels |
| Neuroendocrine | 5-HIAA (serotonin metabolite) | 5-HIAA levels | 5-HIAA monitoring |

### Evidence Level Assessment

| Biomarker/Assay | Source (IF) | Study Type | Citations | Patients (n) | Evidence Level |
|----------------|-------------|-----------|-----------|-------------|---------------|
| NMP22 BladderChek | JAMA (IF ~157) | Prospective multicenter | >600 | 668 | **High** |
| UroVysion FISH | J Urol (IF ~6.6) | Prospective | >500 | >1000 | **High** |
| BTA Stat/TRAK | J Urol (IF ~6.6) | Prospective multicenter | >400 | >500 | **High** |
| PCA3 (Progensa) | Eur Urol (IF ~25) | Multicenter validation | >300 | >1000 | **High** |
| ExoDx Prostate | J Urol (IF ~6.6) | Prospective | >100 | 519 | **Moderate-High** |
| Cxbladder | Diagnostics (IF ~3.6) | Multicenter | >50 | >1000 | **Moderate** |
| AssureMDx | J Mol Diagn (IF ~5.3) | Multicenter | >80 | 570 | **Moderate** |
| Bladder EpiCheck | Eur Urol Oncol (IF ~8.3) | Prospective blinded | >90 | 440 | **Moderate** |
| Urinary exosomes meta-analysis | Front Oncol (IF ~4.7) | Meta-analysis (16 studies) | >70 | 3,224 | **Moderate** |
| Urinary miRNA (systematic review) | IJMS (IF ~5.6) | Systematic review | >50 | Review | **Moderate** |
| EC PSA aptasensor | Anal Bioanal Chem (IF ~4.0) | Lab validation | ~20 | Spiked serum | **Low** (research) |
| CRISPR/Cas12a ctDNA sensor | Sens Actuators B (IF ~8.4) | Lab + patient plasma | ~40 | <20 patients | **Low-Moderate** |
| Urine autofluorescence (cancer) | Sci Rep (IF ~4.6) | Clinical observational | <10 | ~80 | **Low-Moderate** |
| Endometrial fluorescent metabolome | Cancers (IF ~5.2) | Clinical pilot | <5 | ~50 | **Low** (pilot) |
| EC NMP22 immunosensor | J Electroanal Chem (IF ~4.5) | Lab validation | ~30 | Spiked urine | **Low** (research) |

**Evidence Level Criteria:**
- **High:** FDA/CE-approved or multicenter validation (n>500), high-IF journal, >200 citations
- **Moderate:** Prospective clinical validation (n>100), reputable journal, >50 citations
- **Low-Moderate:** Small clinical studies (n<100) or spiked sample validation
- **Low:** Lab-only validation, proof-of-concept

## Pre-Analytical Considerations (Sample Preparation)

| Biomarker Class | Pre-Analytical Requirements | Complexity |
|----------------|---------------------------|------------|
| Proteins (PSA, NMP22, BTA) | First morning void or random midstream; centrifuge for cell removal; store -20°C or test within 6h | Low-Moderate |
| cfDNA / ctDNA | First morning void preferred; centrifuge 3000g; extract cfDNA; stabilizing tubes (Streck) recommended | High |
| miRNA | Centrifuge to remove cells; RNA extraction (TRIzol or kit); exosome isolation if exosomal miRNA targeted | High |
| Exosomes | Ultracentrifugation (100,000g); size-exclusion chromatography or immunoaffinity capture; characterize by NTA/Western | Very High |
| Metabolites (fluorescent) | Minimal preparation; centrifuge to remove particulates; measure within hours (light-sensitive) | **Very Low** |
| Metabolites (VOC) | Headspace collection; SPME fiber or sorbent tube | Moderate |

> [!IMPORTANT]
> Metabolite fluorescence profiling requires minimal sample preparation (centrifuge + direct measurement), making it the most compatible biomarker class for the Jimini device's reagent-free workflow.

## Jimini Device Compatibility Matrix

**Jimini device specifications:**
- Optical emitters: 275 nm, 365 nm, 405 nm, 455 nm, VIS broadband, NIR
- Optical sensors: C12 (321–870 nm), C14 (570–1078 nm)
- Electrochemical: EIS
- MALS: Multi-angle light scattering (635 nm laser)

| Biomarker | Optical (★/5) | EIS (★/5) | Overall | Notes |
|-----------|--------------|----------|---------|-------|
| [[[[tryptophan]]\|Tryptophan]] autofluorescence | ★★★★★ | N/A | **EXCELLENT** | Ex 275 nm → Em 340 nm. Direct match with 275 nm LED + C12 sensor. Reagent-free. |
| [[nadh\|NADH]] fluorescence | ★★★★ | N/A | **VERY GOOD** | Ex 365 nm → Em 460 nm. 365 nm LED + C12 sensor. |
| [[fad\|FAD]] fluorescence | ★★★★ | N/A | **VERY GOOD** | Ex 405–455 nm → Em 525 nm. 405/455 nm LEDs + C12 sensor. |
| [[total-urinary-porphyrin\|Porphyrins]] | ★★★★ | N/A | **VERY GOOD** | Ex 405 nm → Em 630 nm. Soret band excitation. |
| Pterins (neopterin) | ★★★★ | N/A | **VERY GOOD** | Ex 365 nm → Em 450 nm. |
| Urinary EEM profile | ★★★★★ | N/A | **EXCELLENT** | Multi-excitation (275/365/405/455 nm) + C12/C14 emission. Direct implementation of fluorescent metabolome screening. |
| Hemoglobin (hematuria) | ★★★★ | N/A | **VERY GOOD** | Soret band 415 nm (absorbance) + Q-bands 541/577 nm. |
| Total protein/albumin | ★★★ | ★★★★ | **GOOD** | UV absorbance 280 nm; intrinsic fluorescence Ex 295/Em 340 nm; EIS immunosensor feasible. |
| Turbidity/particles (EVs) | ★★★ | N/A | **MODERATE** | MALS at 635 nm detects bulk scattering; not specific without antibodies. |
| PSA (specific) | ★ | ★★★★ | **MODERATE** | No reagent-free optical detection; EIS immunosensor feasible. |
| NMP22 (specific) | ★ | ★★★★ | **MODERATE** | No direct optical signature; EIS immunosensor feasible. |
| miRNA (specific) | ★ | ★★★ | **LOW-MODERATE** | Requires nucleic acid probe on EIS electrode + sample extraction. |
| ctDNA (specific) | ★ | ★★★ | **LOW-MODERATE** | Requires DNA extraction + hybridization on EIS electrode. |
| Exosomes (specific cargo) | ★ | ★★★ | **LOW-MODERATE** | Requires antibody-functionalized EIS electrode. |
| [[[[glucose]]\|Glucose]] | ★ | ★★★★★ | **GOOD** | GOx-EIS well-established. |
| Lactate | ★ | ★★★★ | **MODERATE** | LOx enzyme electrode on EIS. |
| Conductivity/ionic | N/A | ★★★★★ | **GOOD** | Low-frequency EIS; native capability. |
| pH | N/A | ★★★★★ | **GOOD** | Potentiometric; electrode compatible. |

### Jimini Compatibility Summary Matrix

| Jimini Accessibility | High (validated) | Moderate (emerging) | Low (research) |
|---------------------|-----------------|--------------------|----|
| **Excellent** (reagent-free optical) | — | Urinary EEM profile, [[[[tryptophan]]\|Tryptophan]] fluorescence | [[nadh\|NADH]]/[[fad\|FAD]] ratio, [[total-urinary-porphyrin\|Porphyrins]], Pterins |
| **Good** (optical + EIS) | Hematuria (Hb), pH, Conductivity | Total protein/albumin | [[[[glucose]]\|Glucose]] (EIS) |
| **Moderate** (electrode modification) | — | PSA (EIS), NMP22 (EIS) | Exosome counting (MALS), Lactate (EIS) |
| **Low** (reagents + extraction) | — | ctDNA panels, miRNA panels, exosome-specific cargo | — |

## Key Findings and Recommendations

### Strongest Opportunities for Jimini

1. **Urinary fluorescent metabolome profiling** is the most promising application for Jimini in cancer screening:
   - Requires NO reagents, NO sample preparation beyond centrifugation
   - Multi-excitation EEM at 275/365/405/455 nm maps directly to Jimini's LED array
   - Clinical evidence: 94% accuracy for endometrial cancer (2024); significant discrimination for bladder cancer (2025); melanoma correlation (2021)
   - Immediately actionable with ML (Random Forest, SVM, XGBoost)

2. **[[[[tryptophan]]|Tryptophan]] fluorescence (Ex 275/Em 340)** correlates with melanoma stage and bladder cancer

3. **[[nadh|NADH]]/[[fad|FAD]] redox ratio (Ex 365→Em 460 / Ex 455→Em 525)** reflects cancer metabolic shift (Warburg effect)

4. **Porphyrin fluorescence (Ex 405/Em 630)** elevated in bladder and colorectal cancer

5. **EIS-based immunosensors** for PSA and NMP22 could be developed as add-on electrodes for the Jimini EIS module

### Recommended Next Steps

1. Validate urinary EEM fingerprinting on the Jimini device using the 4-LED + 2-sensor configuration against a bladder cancer patient cohort vs. controls
2. Build ML models from Jimini spectral signatures (275/365/405/455 nm excitation × C12/C14 emission) for cancer vs. healthy discrimination
3. Explore EIS immunosensor add-on for PSA (prostate) and NMP22 (bladder) as specific confirmatory tests
4. Combine metabolic fluorescence with existing Jimini urinalysis ([[creatinin|creatinine]], [[uric-acid|uric acid]], protein) for normalized cancer risk scores

## Sources

| # | Reference | DOI |
|---|-----------|-----|
| 1 | Nadeem-Tariq A et al. Electrochemical Detection of Cancer Biomarkers. *Biosensors* 2026;16(1):44 | 10.3390/bios16010044 |
| 2 | Yang Z et al. Urinary Biomarkers in Bladder Cancer. *Cancers* 2025;17(21):3425 | 10.3390/cancers17213425 |
| 3 | Chen Y et al. Urinary Exosomes Diagnosis of Urological Tumors. *Front Oncol* 2021;11:734587 | 10.3389/fonc.2021.734587 |
| 4 | Pandolfo S et al. Urinary MicroRNAs as Biomarkers. *IJMS* 2023;24(13):10846 | 10.3390/ijms24131084 |
| 5 | Islam MN et al. Recent advances in ctDNA detection. *Discover Oncol* 2024;15:517 | 10.1007/s12672-024-01365-7 |
| 6 | RCC urinary biomarkers systematic review. *BMC Cancer* 2025;25:1672 | 10.1186/s12885-025-14900-8 |
| 7 | Wan X et al. Urine-based biomarkers in bladder cancer. *Int J Oncol* 2025;66:18 | 10.3892/ijo.2025.5724 |
| 8 | Jałocha-Bratek A et al. Spectral characteristics of urine in bladder cancer. *Sci Rep* 2025 | 10.1038/s41598-025-15801-3 |
| 9 | Štrumfa I et al. [[[[tryptophan]]\|Tryptophan]]-related fluorescence of urine and melanoma. *IJMS* 2021;22(4):1884 | 10.3390/ijms22041884 |
| 10 | Kalinowska P et al. Non-Invasive Endometrial Cancer Screening. *Cancers* 2024;16(18):3155 | 10.3390/cancers16183155 |
| 11 | Masilamani V et al. Diagnosis of cancer by native fluorescence of urine. *Photochem Photobiol* 2012;88:1520 | 10.1111/j.1751-1097.2012.01239.x |
| 12 | Al-Shukri M. Cancer screening by fluorescence spectra. *J King Saud Univ Sci* 2021 | 10.1016/j.jksus.2021.101178 |
| 13 | Cui F et al. Cancer biomarkers based on electrochemical biosensors. *J Electrochem Soc* 2020;167:037525 | 10.1149/2.0252003JES |
| 14 | Erozenci L et al. Urinary exosomal proteins as pan-cancer biomarkers. *FEBS Lett* 2019;593:1580 | 10.1002/1873-3468.13487 |
| 15 | Amri C et al. Nanoparticle-based optical biosensors for cancer biomarkers. *Materials* 2021 | — |
| 16 | Brönimann S et al. Catalogue of urinary markers for prostate cancer. *Curr Opin Urol* 2020;30(5):659 | — |
| 17 | Truong M et al. Detection of prostate cancer in urine. *J Urol* 2013;189:422 | — |
| 18 | Raja N et al. Urinary markers for prostate cancer risk stratification. *Transl Androl Urol* 2018;7(S4):S436 | — |
| 19 | Freitas D et al. Optical nanobiosensors for exosome detection. *Cancer Cell Int* 2024;24:189 | 10.1186/s12935-024-03379-1 |
| 20 | Campuzano S et al. Electrochemical biosensing of cancer-related EVs. *Anal Bioanal Chem* 2023 | 10.1007/s00216-023-04530-z |
| 21 | Advanced technologies in EV biosensing. *Molecules* 2026;31(2):227 | 10.3390/molecules31020227 |
| 22 | Lima AR et al. Cancer metabolomic markers in urine. *Nat Rev Urol* 2019;16:339 | 10.1038/s41585-019-0185-3 |
| 23 | Alam SR et al. [[nadh\|NADH]], [[fad\|FAD]] and [[tryptophan]] FLIM in prostate cancer cells. *Sci Rep* 2017;7:10856 | 10.1038/s41598-017-10856-3 |

## Gaps

- No biomarker simultaneously achieves High validated clinical evidence and Excellent reagent-free Jimini accessibility; this gap is the primary translational opportunity.
- Most electrochemical biosensors remain lab-validated only — few tested in real clinical urine matrices where matrix interference can degrade performance by orders of magnitude.
- Exosome-specific detection requires antibody functionalization not currently available on Jimini.
- miRNA and ctDNA assays require nucleic acid extraction, making them incompatible with Jimini's reagent-free approach.
- Metabolic fluorescence is promising but needs larger prospective validation studies; urinary autofluorescence is affected by diet, hydration, medications, and infections — normalization to [[creatinin|creatinine]] and multi-parameter modeling is essential.
- Raw spectra and labels from clinical studies are not openly published, limiting cross-instrument harmonisation.
