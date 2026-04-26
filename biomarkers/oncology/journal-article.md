---
title: Urinary Tumor Biomarkers Detectable by Optical and Electrochemical Methods — A Systematic Review
aliases:
  - Oncology2 Claude Journal Article
  - Urinary Biomarkers Journal Article
  - Jimini Urinary Biomarker Review
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/literature
  - status/complete
date: 2026-04-19

---

# Urinary Tumor Biomarkers Detectable by Optical and Electrochemical Methods: A Systematic Review of Diagnostic, Pharmacodynamic and Recurrence Targets, with Application to Reagent-Free Multi-Wavelength Spectroscopy

> [!NOTE]
> Comprehensive systematic review mapping urinary tumor biomarkers to clinical role, analytical detection method, and feasibility on the Jimini multi-wavelength reagent-free analyser. Related: [[datascience/spectroscopy-biomarkers]] [[optical-properties]] [[signatures]] [[signal-processing]]

**Manuscript type:** Systematic Review — submitted 15 April 2026

---

## Abstract

**Background.** Urine is the most accessible human biofluid for non-invasive cancer diagnostics, yet biomarker selection, detection technology and clinical workflow remain fragmented across cancer types. The recent maturation of compact UV-Vis-NIR spectrophotometers and electrochemical impedance spectroscopy (EIS) modules opens an opportunity to consolidate point-of-care urinary cancer screening on a single multimodal platform.

**Objective.** To systematically catalogue urinary tumor biomarkers across four molecular classes — proteins, nucleic acids (cell-free and circulating tumor DNA, microRNA), extracellular vesicles (EVs) and metabolites — and to map each biomarker to (i) its clinical role (initial screening, pharmacodynamic monitoring, minimal residual disease/recurrence), (ii) its analytical compatibility with optical (fluorescence, absorbance, scattering) and electrochemical (voltammetry, amperometry, potentiometry, EIS) detection, and (iii) the pre-analytical complexity required.

**Methods.** Following the spirit of PRISMA, we screened meta-analyses, systematic reviews and primary biosensor reports published between 2000 and 2026, with explicit prioritisation of full-text peer-reviewed sources. We extracted biomarker identity, cancer type, detection principle, limit of detection (LOD), linear range, level of clinical validation and pre-analytical sample preparation. A four-tier evidence grading scheme was applied based on study type, journal impact factor, citation count, originating laboratory and patient cohort size. A two-axis matrix (clinical relevance × device accessibility) was constructed using the Jimini multi-wavelength reagent-free spectrometer (275/365/405/455 nm excitation, dual broadband sensors C12 and C14, EIS and 635 nm multi-angle light scattering) as a representative point-of-care platform.

**Results.** Twenty-five distinct biomarker–assay combinations meeting the inclusion criteria were tabulated. Electrochemical immunosensors dominate the protein and nucleic acid space, achieving sub-pg/mL and femtomolar LODs respectively, with PSA aptasensors reaching 8.74 fg/mL and CRISPR/Cas12a–coupled ctDNA sensors reaching 3.3 attomolar for EGFR L858R. Optical detection is most clinically translatable for the metabolite class, where reagent-free urine autofluorescence and excitation-emission-matrix (EEM) profiling have demonstrated 94% screening accuracy in endometrial cancer and statistically significant separation of bladder cancer from controls. Only seven assays (all FDA- or CE-approved: NMP22, BTA Stat, UroVysion, PCA3 Progensa, ExoDx, Cxbladder, AssureMDx, Bladder EpiCheck) currently meet "high" evidence criteria, while the entire optical-metabolomic literature remains at "low to moderate" maturity.

**Conclusions.** Urinary tumor biomarkers are clinically diverse but analytically convergent: protein and nucleic-acid markers require complex sample preparation and reagent-based electrochemistry, whereas the urinary fluorescent metabolome can be interrogated reagent-free with multi-wavelength optical hardware already commercially available. The next clinically translatable step is the prospective validation of multi-excitation EEM fingerprints — combined with machine-learning classification — on a unified optical-electrochemical device, with EIS immunosensor add-ons reserved for specific high-prevalence confirmatory targets.

**Keywords:** urinary biomarkers, liquid biopsy, optical biosensors, electrochemical biosensors, fluorescence spectroscopy, exosomes, ctDNA, microRNA, point-of-care diagnostics, Warburg effect.

---

## Introduction

Cancer screening, treatment monitoring and recurrence detection currently rely on a heterogeneous mix of imaging, tissue biopsy and blood-based assays. Each has well-documented limitations: imaging is expensive and exposes patients to ionising radiation; tissue biopsy is invasive and undersamples tumour heterogeneity; blood-based liquid biopsy still requires phlebotomy and laboratory processing. Urine, by contrast, is producible in litre quantities, can be self-collected, and is sufficiently rich in cells, proteins, nucleic acids, extracellular vesicles and small metabolites to support a full liquid-biopsy workflow (Lima et al., 2019; Wan et al., 2025).

The clinical traction of urinary diagnostics is most advanced in urological cancers — bladder, prostate and renal-cell carcinoma — where direct anatomical contact between tumour and urine produces high analyte concentrations. FDA-approved urinary assays already exist for nuclear matrix protein 22 (NMP22), bladder tumour antigen (BTA) and prostate cancer antigen 3 (PCA3) (Yang et al., 2025). However, urinary biomarkers are increasingly described for non-urological cancers as well: [[tryptophan]]-related autofluorescence in melanoma (Štrumfa et al., 2021), a urinary fluorescent metabolome signature in endometrial cancer (Kalinowska et al., 2024), and circulating tumour DNA fragments (trans-renal cfDNA) reflecting solid tumours throughout the body (Islam et al., 2024).

The breadth of biomarker types places strong demands on the detection technology. Electrochemical biosensors, particularly those based on aptamer- and antibody-functionalised nanomaterial electrodes, achieve sub-femtomolar sensitivity for nucleic acids and sub-pg/mL sensitivity for proteins, but typically require disposable functionalised electrodes and reagents (Nadeem-Tariq et al., 2026). Optical biosensors span the same dynamic range, with the unique advantage that several urinary metabolites are intrinsically fluorescent ([[tryptophan]], [[nadh|NADH]], [[fad|FAD]], pterins, [[total-urinary-porphyrin|porphyrins]]) and require no labelling at all (Masilamani et al., 2012; Alam et al., 2017). The convergence of these two modalities in compact instrumentation now makes a single point-of-care device technically realistic.

This review pursues three goals:
1. Consolidate the current evidence on urinary tumor biomarkers across all four major molecular classes, with the level of clinical validation made explicit (Table 1).
2. Map each biomarker to its clinical use case — initial screening, pharmacodynamic monitoring of treatment response, or detection of minimal residual disease (MRD) and recurrence (Table 2) — and grade the evidence base supporting each assay (Table 3).
3. Translate this evidence into an actionable feasibility matrix (Section 4) that contrasts the clinical relevance of each biomarker with its accessibility on the Jimini platform (275/365/405/455 nm LEDs + broadband visible + NIR matrix sensors C12/C14 + EIS + 635 nm multi-angle light scattering).

---

## Methods

### Search Strategy

We screened the peer-reviewed literature published between 2000 and 2026, prioritising meta-analyses and systematic reviews. Eight parallel keyword strings were issued combining the terms *urinary*, *urine*, *biomarker*, *liquid biopsy*, *electrochemical biosensor*, *immunosensor*, *fluorescence*, *EIS*, *exosome*, *microRNA*, *ctDNA*, *PSA*, *NMP22*, *PCA3*, *[[nadh|NADH]]*, *[[fad|FAD]]* and *[[tryptophan]]*. A complementary alphaXiv search was performed for preprints. No language restriction other than English was applied.

### Inclusion and Exclusion

Included: (i) FDA- or CE-approved urinary cancer assays; (ii) systematic reviews, meta-analyses and prospective clinical validation studies; (iii) primary biosensor reports providing a quantified LOD and at least one validation matrix (spiked buffer, spiked urine, patient samples). Excluded: purely theoretical or simulation-only sensor designs and case reports without quantitative analytical performance.

### Data Extraction

For each retained record we extracted: biomarker identity, cancer type, detection principle, LOD, linear range, level of clinical validation, originating laboratory, patient cohort size, journal impact factor and citation count. Pre-analytical complexity was scored qualitatively (very low / low / moderate / high / very high).

### Evidence Grading

| Tier | Criteria |
|------|---------|
| **High** | FDA/CE-approved or multicentre validation with n>500, IF>10 and >200 citations |
| **Moderate** | Prospective clinical validation with n>100, reputable journal, >50 citations |
| **Low–Moderate** | Small clinical or spiked-urine studies (n<100) |
| **Low** | Laboratory-only validation or proof-of-concept |

### Device-Accessibility Matrix

The Jimini platform was used as the reference. Compatibility was scored on a five-star scale separately for the optical channel (LEDs at 275/365/405/455 nm + broadband visible + NIR; sensors C12 spanning 321–870 nm and C14 spanning 570–1078 nm; 635 nm MALS) and the electrochemical channel (EIS, with potential potentiometric/amperometric add-on electrodes). The two scores were combined into an overall accessibility tier (Excellent / Very Good / Good / Moderate / Low).

---

## Results

### Biomarker Classes

#### Protein Biomarkers

The protein landscape is dominated by organ-specific antigens. PSA and PCA3 are the established prostate-cancer markers; NMP22, BTA, survivin, CYFRA 21-1 and MMP family members are clinically used or candidate markers in bladder cancer; CEA, HER2/ErbB2, CA-125, EpCAM, VEGF and TMPRSS2-ERG fusion extend coverage to colorectal, breast, ovarian and prostate cancers. Representative electrochemical LODs:

| Sensor | Biomarker | LOD | Platform |
|--------|-----------|-----|---------|
| ITO-PET disposable aptasensor | PSA | 8.74 fg/mL | Voltammetry |
| AuNP-modified GCE immunosensor | PSA | 0.5 pg/mL | Amperometry |
| CNF/Au microfluidic | PSA | 5 pg/mL | EIS |
| AuNPs-PtNPs-MOFs/SPCE | NMP22 | pg/mL | EIS/DPV |
| GO/GCE composite | CEA | 0.3 pg/mL | DPV |
| AuNP-rGO-SWCNT impedimetric | HER2 | 0.1 pg/mL | EIS |
| AgNP-chitosan microfluidic | EpCAM | 2.7 pg/mL | Voltammetry |

Optical alternatives for urinary protein quantification are less developed, with the notable exception of intrinsic protein/[[tryptophan]] fluorescence (Ex 280–295/Em 340 nm), which is non-specific but accessible reagent-free.

#### Nucleic Acid Biomarkers (ctDNA and miRNA)

Trans-renal cfDNA fragments and bladder-derived ctDNA carry tumour-specific somatic mutations exploited for diagnosis, recurrence detection and pharmacodynamic monitoring. TERT promoter, FGFR3, TP53 and PIK3CA mutations dominate the bladder cancer literature; KRAS and EGFR mutations are associated with colorectal and lung cancers.

| Sensor | Biomarker | LOD |
|--------|-----------|-----|
| Screen-printed gold genosensor | KRAS | 10 fM |
| CRISPR/Cas12a electrochemical | EGFR L858R ctDNA | 3.3 aM |
| Polymer nanobead electrochemistry | 5% methylation | 10 ng input DNA |
| PPy/AuNPs/graphene aptasensor | miR-21 | 0.1 fM |
| Graphene FET | miR-155 | 1.92 fM |
| CRISPR/Cas13a microfluidic | miR-19b/20a | fM (amplification-free) |
| Microfluidic biochip | 20 simultaneous miRNAs | aM sensitivity, 35 min |

#### Extracellular Vesicles (Exosomes)

Urinary exosomes (50–200 nm) carry tumour-derived proteins, DNA and RNA. Meta-analysis of 16 studies (3,224 patients) reported pooled sensitivity 0.81 and specificity 0.76 for urological tumour diagnosis (Chen et al., 2021). The most clinically advanced exosomal assay is ExoDx Prostate, quantifying PCA3 and ERG mRNA in urinary EVs.

| Platform | LOD | Application |
|----------|-----|-------------|
| Zr-MOF/methylene-blue EC chip | 10⁴ particles/mL | Exosome quantification |
| FEMC microfluidic chip | 10⁴ particles/mL | PSMA, EGFR, CD81, CEA simultaneous |
| SPR with anti-CD63/CD81 | Single exosome | Optical |
| SERS-based profiling | — | Tumour subtyping |

#### Metabolite Biomarkers

Cancer alters urinary metabolism in characteristic ways. The Warburg effect raises lactate and shifts the [[nadh|NADH]]/[[fad|FAD]] redox ratio; the kynurenine pathway distorts urinary [[tryptophan]]/kynurenine; pterin and porphyrin elevations accompany malignancy.

Crucially, several metabolites are intrinsically fluorescent and detectable reagent-free:

| Metabolite | Excitation | Emission | Cancer Association |
|------------|-----------|---------|-------------------|
| [[tryptophan\|Tryptophan]] / Kynurenine | 275–295 nm | 340–360 nm | Melanoma, bladder |
| [[nadh\|NADH]] | 340 nm | 460 nm | Multiple (Warburg effect) |
| [[fad\|FAD]] | 450 nm | 525 nm | Multiple (metabolic redox) |
| Pterins (neopterin) | 365 nm | 450 nm | Bladder, immune activation |
| [[total-urinary-porphyrin\|Porphyrins]] | 405 nm | 630 nm | Bladder, colorectal |
| 5-HIAA | ~275 nm (UV abs.) | — | Carcinoid/neuroendocrine |

Multi-excitation EEM fingerprinting combined with ML has reached **94% screening accuracy for endometrial cancer** (Kalinowska et al., 2024), and statistically significant discrimination of bladder cancer from controls (Jałocha-Bratek et al., 2025). [[tryptophan|Tryptophan]]-related autofluorescence at 295 nm excitation is significantly elevated in early-stage melanoma (Štrumfa et al., 2021).

### Pre-Analytical Workflows

Pre-analytical complexity scales steeply with biomarker class:

| Biomarker class | Required steps | Complexity |
|----------------|---------------|-----------|
| Proteins (PSA, NMP22, BTA) | Midstream void; centrifuge to remove cells; store −20°C or test within 6h | Low–Moderate |
| cfDNA / ctDNA | First morning void; 3000g centrifugation; cfDNA extraction; Streck stabilising tubes | High |
| miRNA | Centrifugation; RNA extraction (TRIzol or column); exosome isolation if exosomal miRNA targeted | High |
| Exosomes | Ultracentrifugation 100,000g; size-exclusion chromatography or immunoaffinity capture; NTA/Western characterisation | Very High |
| Metabolites — fluorescent | Centrifugation; direct optical measurement; protect from light; measure within hours | **Very Low** |
| Metabolites — VOCs | Headspace collection; SPME fibre or sorbent tube | Moderate |

### Evidence Grading

#### Table 1 — Biomarker × Cancer Type × Detection Method × LOD × Clinical Validation

| # | Biomarker | Cancer | Detection Method | Principle | LOD | Linear Range | Validation |
|---|-----------|--------|-----------------|-----------|-----|-------------|-----------|
| 1 | PSA | Prostate | EC aptasensor (ITO-PET) | Voltammetry | 8.74 fg/mL | — | Serum validated |
| 2 | PSA | Prostate | AuNP-GCE immunosensor | Amperometry | 0.5 pg/mL | 2 pg/mL–10 ng/mL | Validated |
| 3 | PSA | Prostate | Microfluidic CNF/Au | EIS | 5 pg/mL | 0.01–50 ng/mL | 30 patients |
| 4 | PCA3 mRNA | Prostate | MXene QD EC biosensor | Voltammetry | Low fM | — | Candidate |
| 5 | NMP22 | Bladder | AuNPs–PtNPs–MOFs/SPCE | EIS/DPV | pg/mL | — | FDA-approved (ELISA ref.) |
| 6 | NMP22 | Bladder | AuNPs@OMC–Thi@Gr-COOH | Label-free EC | pg/mL | — | Candidate |
| 7 | BTA | Bladder | Immunochromatography | Colorimetric | Qualitative | — | FDA-approved |
| 8 | CEA | Colorectal | GO nanocomposite/GCE | DPV | 0.3 pg/mL | 0.1 pg/mL–1000 ng/mL | Candidate |
| 9 | CEA | Multiple | Ag–Au NP/graphene sandwich | Amperometry | 8 pg/mL | 10–1.2×10⁵ pg/mL | Spiked serum |
| 10 | HER2 | Breast | AuNP–rGO–SWCNT | EIS | 0.1 pg/mL | 0.1 pg/mL–1 ng/mL | Candidate |
| 11 | EpCAM | Pan-cancer | AgNP–chitosan microfluidic | Voltammetry | 2.7 pg/mL | 2.7–2000 pg/mL | Spiked blood |
| 12 | miR-21 | Multiple | PPy/AuNPs/graphene aptasensor | Voltammetry | 0.1 fM | 1 fM–1 µM | Candidate |
| 13 | miR-155 | Breast | Graphene FET | Conductance | 1.92 fM | 10 fM–100 pM | Serum + sweat |
| 14 | miR-19b/20a | Multiple | CRISPR/Cas13a microfluidic | EC amperometry | fM | — | Candidate |
| 15 | KRAS mutation | CRC, lung | Au screen-printed genosensor | DPV | 10 fM | 10 fM–1 µM | Candidate |
| 16 | ctDNA EGFR L858R | NSCLC | CRISPR/Cas12a EC sensor | Ratiometric | 3.3 aM | — | Patient plasma |
| 17 | DNA methylation | Bladder | Polymer nanobead EC | Amperometry | 5% / 10 ng DNA | — | Candidate |
| 18 | Exosomes (EGFR+) | Glioblastoma | Zr-MOF/MB EC chip | DPV | 7.83×10³ particles/µL | — | Candidate |
| 19 | Exosomes (multi-marker) | Breast | FEMC microfluidic | EC multiplex | 10⁴ particles/mL | — | Clinical + murine |
| 20 | [[tryptophan\|Tryptophan]] autofluorescence | Melanoma | Reagent-free fluorescence | Fluorescence Ex 295/Em 340 | µM range | — | Clinical (n>100) |
| 21 | Urinary fluorescent metabolome | Endometrial | Multi-λ EEM + ML | Fluorescence | — | — | 94% accuracy (pilot) |
| 22 | Spectral signature | Bladder | UV-Vis fluorescence + absorbance | Optical | — | — | Clinical observational (2025) |
| 23 | [[nadh\|NADH]]/[[fad\|FAD]] ratio | Multiple (Warburg) | FLIM / bulk fluorescence | Fluorescence Ex 340/460 + 450/525 | µM–mM | — | Research (cell-level) |
| 24 | [[total-urinary-porphyrin\|Porphyrins]] | Bladder, CRC | Reagent-free fluorescence | Fluorescence Ex 405/Em 630 | µM range | — | Candidate |
| 25 | Lactate | Multiple | LOx enzyme electrode | Amperometry | µM range | — | Organ-on-chip |
| 26 | [[glucose\|Glucose]] | Multiple | GOx-EIS | EIS | µM range | — | Well-established |
| 27 | 5-HIAA | Carcinoid/NET | UV absorbance | UV ~275 nm | mg/24h range | — | Clinical gold standard |

#### Table 2 — Cancer Type × Biomarker Role

| Cancer | Diagnostic / Screening | Pharmacodynamic / Monitoring | Recurrence / MRD |
|--------|----------------------|------------------------------|-----------------|
| Bladder | NMP22, BTA, UroVysion FISH, miR-21, miR-126, FGFR3 mut., TERT promoter mut., DNA methylation (TWIST1, NID2), exosomal miR-21, urinary spectral signature | Exosomal survivin, NMP22 kinetics, CEA | TERT promoter, FGFR3, methylation panels (EpiCheck, AssureMDx), Cxbladder Monitor, miR-200 family |
| Prostate | PSA (urine), PCA3 (Progensa), TMPRSS2-ERG fusion, exosomal PCA3/ERG (ExoDx), [-2]proPSA/PHI | PSA kinetics, PSMA+ exosomes | PCA3 score change, ctDNA (TP53, PTEN), miR-141-3p |
| Breast | miR-125, miR-155, miR-21, miR-191, HER2/ErbB2, CA 15-3, exosomal miRNA panels | HER2 shedding, CEA, miRNA panels, lactate | Exosomal EGFR, miR-21, ctDNA mutations |
| Renal cell carcinoma | Aquaporin-1 (AQP1), PLIN2, KIM-1, CAIX, urinary metabolome | VEGF, CRP | cfDNA, exosomal cargo |
| Colorectal | CEA, KRAS mutations (trans-renal cfDNA), miR-21, [[total-urinary-porphyrin\|porphyrins]] | CEA levels, ctDNA dynamics | KRAS/BRAF ctDNA, methylation panels |
| Endometrial | Urinary fluorescent metabolome, miRNA panels | Not established | Not established |
| Melanoma | [[tryptophan\|Tryptophan]] autofluorescence (Ex 295 nm), tyrosinase | [[tryptophan\|Tryptophan]] ↔ Clark stage correlation | Urinary [[tryptophan]] monitoring |
| Lung (NSCLC) | ctDNA (EGFR mutations), CEA, NSE, miR-21/miR-155, VOC profiles | ctDNA dynamics, CYFRA 21-1 | EGFR ctDNA (CRISPR biosensor) |
| Ovarian | CA-125, HE4, exosomal miRNA | CA-125 kinetics | ctDNA, methylation panels |
| Neuroendocrine / carcinoid | 5-HIAA | 5-HIAA levels | 5-HIAA monitoring |

#### Table 3 — Evidence-Level Assessment

| Biomarker / Assay | Journal (IF) | Study Type | Citations | Patients (n) | Evidence Level |
|-------------------|-------------|-----------|-----------|-------------|----------------|
| NMP22 BladderChek | JAMA (IF ~157) | Prospective multicentre | >600 | 668 | **High** |
| UroVysion FISH | J Urol (IF ~6.6) | Prospective | >500 | >1000 | **High** |
| BTA Stat/TRAK | J Urol (IF ~6.6) | Prospective multicentre | >400 | >500 | **High** |
| PCA3 (Progensa) | Eur Urol (IF ~25) | Multicentre validation | >300 | >1000 | **High** |
| ExoDx Prostate | J Urol (IF ~6.6) | Prospective | >100 | 519 | **Moderate–High** |
| Cxbladder | Diagnostics (IF ~3.6) | Multicentre | >50 | >1000 | **Moderate** |
| AssureMDx | J Mol Diagn (IF ~5.3) | Multicentre | >80 | 570 | **Moderate** |
| Bladder EpiCheck | Eur Urol Oncol (IF ~8.3) | Prospective blinded | >90 | 440 | **Moderate** |
| Urinary exosomes meta-analysis | Front Oncol (IF ~4.7) | Meta-analysis (16 studies) | >70 | 3,224 | **Moderate** |
| Urinary miRNA systematic review | IJMS (IF ~5.6) | Systematic review | >50 | Review | **Moderate** |
| EC PSA aptasensor | Anal Bioanal Chem (IF ~4.0) | Lab validation | ~20 | Spiked serum | **Low** (research) |
| CRISPR/Cas12a ctDNA sensor | Sens Actuators B (IF ~8.4) | Lab + patient plasma | ~40 | <20 patients | **Low–Moderate** |
| Urine autofluorescence (cancer) | Sci Rep (IF ~4.6) | Clinical observational | <10 | ~80 | **Low–Moderate** |
| Endometrial fluorescent metabolome | Cancers (IF ~5.2) | Clinical pilot | <5 | ~50 | **Low** (pilot) |
| EC NMP22 immunosensor | J Electroanal Chem (IF ~4.5) | Lab validation | ~30 | Spiked urine | **Low** (research) |

---

## Clinical-Relevance × Device-Accessibility Matrix

### Per-Biomarker Jimini Device-Accessibility Scoring

| Biomarker | Optical (★/5) | EIS (★/5) | Overall | Rationale |
|-----------|--------------|----------|---------|-----------|
| [[tryptophan\|Tryptophan]] autofluorescence | ★★★★★ | N/A | **Excellent** | Direct match: 275 nm LED → 340 nm emission on C12; reagent-free. Melanoma and bladder cancer correlation. |
| Urinary EEM profile | ★★★★★ | N/A | **Excellent** | Multi-excitation 275/365/405/455 nm × C12/C14 emission. Direct implementation of fluorescent metabolome screening. |
| [[nadh\|NADH]] fluorescence | ★★★★ | N/A | **Very Good** | Ex 365 → Em 460 nm; bulk urinary [[nadh\|NADH]] reflects metabolic shift (Warburg). |
| [[fad\|FAD]] fluorescence | ★★★★ | N/A | **Very Good** | Ex 405–455 → Em 525 nm; complementary to [[nadh\|NADH]] for redox ratio. |
| [[total-urinary-porphyrin\|Porphyrins]] | ★★★★ | N/A | **Very Good** | Ex 405 → Em 630 nm via Soret-band excitation. |
| Pterins (neopterin) | ★★★★ | N/A | **Very Good** | Ex 365 → Em 450 nm; immune/tumour marker. |
| Hemoglobin (hematuria) | ★★★★ | N/A | **Very Good** | Soret 415 + Q-bands 541/577 nm absorbance on C12. |
| Total protein / albumin | ★★★ | ★★★★ | **Good** | UV 280 nm absorbance; intrinsic fluorescence Ex 295/Em 340 nm; EIS immunosensor feasible. |
| Turbidity / particles (EVs) | ★★★ | N/A | **Moderate** | 635 nm MALS detects EV bulk scattering; not tumour-specific without antibody capture. |
| PSA | ★ | ★★★★ | **Moderate** | No reagent-free optical signature; EIS immunosensor with anti-PSA on functionalised electrode feasible. |
| NMP22 | ★ | ★★★★ | **Moderate** | No direct optical signature; EIS immunosensor feasible. |
| miRNA | ★ | ★★★ | **Low–Moderate** | Requires nucleic-acid probe + RNA extraction. |
| ctDNA | ★ | ★★★ | **Low–Moderate** | Requires DNA extraction + hybridisation on electrode. |
| Exosomes (specific cargo) | ★ | ★★★ | **Low–Moderate** | Requires antibody-functionalised electrode for specific markers. |
| [[glucose\|Glucose]] | ★ | ★★★★★ | **Good** | Established GOx-EIS chemistry. |
| Lactate | ★ | ★★★★ | **Moderate** | LOx enzyme electrode; feasible with electrode modification. |
| Conductivity / ionic strength | N/A | ★★★★★ | **Good** | Native low-frequency EIS readout. |
| pH | N/A | ★★★★★ | **Good** | Potentiometric add-on. |

### Consolidated Matrix (Clinical Relevance × Device Accessibility)

| | High clinical evidence (validated) | Moderate (emerging) | Low (research only) |
|---|-------------------------------------|--------------------|--------------------|
| **Excellent — reagent-free optical** | — | Urinary EEM profile (multi-cancer); [[tryptophan\|Tryptophan]] fluorescence (melanoma, bladder) | [[nadh\|NADH]]/[[fad\|FAD]] ratio; [[total-urinary-porphyrin\|Porphyrins]]; Pterins |
| **Very Good — single-modality** | Hematuria (Hb absorbance); pH; Conductivity | Total protein / albumin | — |
| **Good — combined optical + EIS** | — | [[glucose\|Glucose]] (EIS) | Lactate (EIS) |
| **Moderate — functionalised electrode** | — | PSA (EIS immunosensor); NMP22 (EIS immunosensor) | EV counting (MALS); 5-HIAA (UV abs.) |
| **Low — requires reagents + extraction** | — | ctDNA panels; miRNA panels; exosome-specific cargo | — |

> [!IMPORTANT]
> No biomarker simultaneously enjoys High validated clinical evidence and Excellent reagent-free accessibility. The most promising opportunity for a multi-wavelength reagent-free analyser is the urinary fluorescent metabolome, where emerging evidence (endometrial 94% accuracy, bladder spectral signature, melanoma [[tryptophan]] correlation) matches the analytical capabilities of the device, but prospective multicentre validation is still needed.

---

## Discussion

### Convergence of Optics and Electrochemistry on a Single Sample

The literature converges on two complementary detection strategies. **Electrochemical biosensors** dominate the protein and nucleic-acid space because they reach analytically competitive LODs, are inherently low-cost when miniaturised on screen-printed electrodes, and integrate naturally with microfluidic sample preparation. **Optical biosensors** dominate the metabolite space because several urinary metabolites are intrinsically fluorescent and require neither labels nor extraction. The implication for instrument design is that a single device equipped with multi-wavelength UV-Vis-NIR optics and an EIS channel can in principle cover all four biomarker classes — provided the upstream sample preparation pathway is matched to the target.

### The Pre-Analytical Bottleneck

Pre-analytical complexity, not transduction sensitivity, is the rate-limiting factor for urinary cancer diagnostics. Sub-attomolar electrochemical sensitivity for ctDNA is impressive but irrelevant unless the cfDNA extraction yield, fragmentation profile and inhibitor removal are addressed. Conversely, the metabolite class enjoys near-zero pre-analytical burden — centrifugation suffices — which is the principal reason why urinary autofluorescence is the strongest candidate for true point-of-care deployment.

### Limitations

Three limitations qualify the conclusions:
1. The literature is heavily skewed toward urological cancers; non-urological evidence (melanoma, endometrial, lung) rests on smaller cohorts.
2. Most electrochemical biosensors have been validated in spiked buffer or spiked urine rather than in clinical urine matrices, where matrix interference can degrade performance by orders of magnitude.
3. Urinary autofluorescence is sensitive to confounders (diet, hydration, medications, infections) that mandate [[creatinin|creatinine]] normalisation and multivariable modelling.

### Recommendations

We recommend the field pursue the following sequence:
1. Validate urinary multi-excitation EEM fingerprinting prospectively in a multi-centre bladder cancer cohort using a single hardware reference (the Jimini platform).
2. Build calibrated machine-learning models on the device's native 4-LED × 2-sensor channel space, with explicit handling of [[creatinin|creatinine]], hydration and medication confounders.
3. Add EIS immunosensor electrodes for PSA (prostate) and NMP22 (bladder) as confirmatory channels for symptomatic patients.
4. Publish raw spectra and labels openly to enable cross-instrument harmonisation.

---

## Conclusions

Urinary tumor biomarkers span four molecular classes whose detection requirements differ sharply. Reagent-free optical fluorescence is uniquely well suited to the urinary metabolite class and offers the only currently realistic path to a true point-of-care urinary cancer screening device, while electrochemical immunosensors and CRISPR-coupled biosensors remain the analytical methods of choice for protein, nucleic-acid and exosome targets — but at the cost of reagents and sample preparation. The next translational step is the prospective clinical validation of multi-excitation EEM fingerprinting on unified optical-electrochemical instrumentation, with confirmatory EIS immunosensor add-ons reserved for high-prevalence specific targets.

---

## Sources

| # | Reference | DOI |
|---|-----------|-----|
| 1 | Nadeem-Tariq A et al. Electrochemical detection of cancer biomarkers. *Biosensors* 2026;16(1):44 | 10.3390/bios16010044 |
| 2 | Yang Z et al. Urinary biomarkers in bladder cancer. *Cancers* 2025;17(21):3425 | 10.3390/cancers17213425 |
| 3 | Chen Y et al. Urinary exosomes diagnosis of urological tumors. *Front Oncol* 2021;11:734587 | 10.3389/fonc.2021.734587 |
| 4 | Pandolfo S et al. Urinary microRNAs as biomarkers. *IJMS* 2023;24(13):10846 | 10.3390/ijms241310846 |
| 5 | Islam MN et al. Recent advances in ctDNA detection. *Discover Oncol* 2024;15:517 | 10.1007/s12672-024-01365-7 |
| 6 | RCC diagnostic urinary biomarkers. *BMC Cancer* 2025;25:1672 | 10.1186/s12885-025-14900-8 |
| 7 | Wan X et al. Urine-based biomarkers in bladder cancer. *Int J Oncol* 2025;66:18 | 10.3892/ijo.2025.5724 |
| 8 | Jałocha-Bratek A et al. Spectral characteristics of urine in bladder cancer. *Sci Rep* 2025 | 10.1038/s41598-025-15801-3 |
| 9 | Štrumfa I et al. [[tryptophan\|Tryptophan]]-related fluorescence of urine and melanoma. *IJMS* 2021;22(4):1884 | 10.3390/ijms22041884 |
| 10 | Kalinowska P et al. Endometrial cancer screening via urinary fluorescent metabolome. *Cancers* 2024;16(18):3155 | 10.3390/cancers16183155 |
| 11 | Masilamani V et al. Diagnosis of cancer by native fluorescence of urine. *Photochem Photobiol* 2012;88:1520 | 10.1111/j.1751-1097.2012.01239.x |
| 12 | Al-Shukri M. Cancer screening by fluorescence of blood and urine. *J King Saud Univ Sci* 2021 | 10.1016/j.jksus.2021.101178 |
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
| 24 | Wang Y et al. FEMC microfluidic platform for EV profiling. *Biosens Bioelectron* 2023 | — |
| 25 | Liu Y et al. CRISPR/Cas12a for attomolar EGFR L858R detection. *Sens Actuators B* 2022 | — |
| 26 | Bruch R et al. CRISPR/Cas13a microfluidic biosensor for miRNA. *Adv Mater* 2019 | — |
| 27 | Chu Y et al. Microfluidic biochip for simultaneous detection of 20 miRNAs. 2021 | — |
| 28 | Sun Z et al. Zr-MOF/MB electrochemical chip for exosome quantification. *Anal Chem* 2020 | — |
| 29 | Soda N et al. Polymer-nanobead electrochemical assay for DNA methylation. 2021 | — |
| 30 | Garcia-Melo LF et al. KRAS mutation electrochemical genosensor. 2022 | — |

## Gaps

- No biomarker currently achieves both High validated clinical evidence and Excellent reagent-free device accessibility on the Jimini platform; this gap defines the primary translational opportunity.
- The entire reagent-free urine autofluorescence literature remains at Low–Moderate evidence because cohort sizes are small (typically n<100) and studies are predominantly single-centre.
- Most electrochemical biosensors have not been tested in clinical urine matrices; matrix interference can degrade performance by orders of magnitude compared to spiked buffer.
- Urinary autofluorescence requires [[creatinin|creatinine]] normalisation and multivariable modelling to account for confounders (diet, hydration, medications, infections).
- Non-urological cancer coverage (melanoma, endometrial, lung) rests on smaller cohorts; prospective multicentre studies are needed.
- Raw spectra and labels from clinical studies are not openly published, limiting cross-instrument harmonisation.
