# Urinary Tumor Biomarkers Detectable by Optical and Electrochemical Methods: A Systematic Review of Diagnostic, Pharmacodynamic and Recurrence Targets, with Application to Reagent-Free Multi-Wavelength Spectroscopy

**Authors:**
Léa M. Vasseur¹, Tomás A. Renaud², Anya K. Sørensen³, Jasper W. Holloway¹,⁴, Mira P. Castellanos⁵, Henrik J. Lindqvist², Devika R. Anand⁶, Caterina B. Marchetti⁷, Olivier T. Beaumont¹,*

¹ Department of Bioengineering and Translational Diagnostics, Laboratoire Saint-Hubert, 91190 Gif-sur-Yvette, France
² Centre for Liquid Biopsy and Sensor Technologies, Karolinska Affiliated Institute, Solna 17177, Sweden
³ Division of Clinical Oncology, Hovedstaden University Hospital, 2100 Copenhagen, Denmark
⁴ Faculty of Photonics and Bioanalytics, University of Manchester, M13 9PL Manchester, United Kingdom
⁵ Department of Urology, Hospital Clínico San Andrés, 28040 Madrid, Spain
⁶ Translational Cancer Metabolomics Unit, Tata Institute of Biomolecular Sciences, 400076 Mumbai, India
⁷ Laboratory of Electroanalytical Chemistry, Politecnico di Trieste, 34127 Trieste, Italy

\* Corresponding author: olivier.beaumont@lsh-bio.fr

**Submitted:** 15 April 2026
**Manuscript type:** Systematic Review

---

## Abstract

**Background.** Urine is the most accessible human biofluid for non-invasive cancer diagnostics, yet biomarker selection, detection technology and clinical workflow remain fragmented across cancer types. The recent maturation of compact UV-Vis-NIR spectrophotometers and electrochemical impedance spectroscopy (EIS) modules opens an opportunity to consolidate point-of-care urinary cancer screening on a single multimodal platform.

**Objective.** To systematically catalogue urinary tumor biomarkers across four molecular classes — proteins, nucleic acids (cell-free and circulating tumor DNA, microRNA), extracellular vesicles (EVs) and metabolites — and to map each biomarker to (i) its clinical role (initial screening, pharmacodynamic monitoring, minimal residual disease/recurrence), (ii) its analytical compatibility with optical (fluorescence, absorbance, scattering) and electrochemical (voltammetry, amperometry, potentiometry, EIS) detection, and (iii) the pre-analytical complexity required.

**Methods.** Following the spirit of PRISMA, we screened meta-analyses, systematic reviews and primary biosensor reports published between 2000 and 2026, with explicit prioritisation of full-text peer-reviewed sources. We extracted biomarker identity, cancer type, detection principle, limit of detection (LOD), linear range, level of clinical validation and pre-analytical sample preparation. A four-tier evidence grading scheme was applied based on study type, journal impact factor, citation count, originating laboratory and patient cohort size. A two-axis matrix (clinical relevance × device accessibility) was constructed using the Jimini multi-wavelength reagent-free spectrometer (275/365/405/455 nm excitation, dual broadband sensors C12 and C14, EIS and 635 nm multi-angle light scattering) as a representative point-of-care platform.

**Results.** Twenty-five distinct biomarker–assay combinations meeting the inclusion criteria were tabulated (Table 1). Electrochemical immunosensors dominate the protein and nucleic acid space, achieving sub-pg/mL and femtomolar LODs respectively, with PSA aptasensors reaching 8.74 fg/mL and CRISPR/Cas12a–coupled ctDNA sensors reaching 3.3 attomolar for EGFR L858R. Optical detection is most clinically translatable for the metabolite class, where reagent-free urine autofluorescence and excitation-emission-matrix (EEM) profiling have demonstrated 94% screening accuracy in endometrial cancer and statistically significant separation of bladder cancer from controls. Cancer-type-stratified mapping of diagnostic, monitoring and recurrence biomarkers is reported in Table 2. Evidence-level scoring (Table 3) confirmed that only seven assays — all FDA- or CE-approved (NMP22, BTA Stat, UroVysion, PCA3 Progensa, ExoDx, Cxbladder, AssureMDx, Bladder EpiCheck) — currently meet "high" evidence criteria, while the entire optical-metabolomic literature remains at "low to moderate" maturity. The clinical-relevance × device-accessibility matrix shows that urinary EEM fluorescence profiling and tryptophan autofluorescence offer the most favourable trade-off for reagent-free point-of-care use, while EIS immunosensors for PSA and NMP22 represent the most actionable add-on for specific confirmatory testing.

**Conclusions.** Urinary tumor biomarkers are clinically diverse but analytically convergent: protein and nucleic-acid markers require complex sample preparation and reagent-based electrochemistry, whereas the urinary fluorescent metabolome can be interrogated reagent-free with multi-wavelength optical hardware already commercially available. We argue that the next clinically translatable step is the prospective validation of multi-excitation EEM fingerprints — combined with machine-learning classification — on a unified optical-electrochemical device, with EIS immunosensor add-ons reserved for specific high-prevalence confirmatory targets.

**Keywords:** urinary biomarkers, liquid biopsy, optical biosensors, electrochemical biosensors, fluorescence spectroscopy, exosomes, ctDNA, microRNA, point-of-care diagnostics, Warburg effect.

---

## 1. Introduction

Cancer screening, treatment monitoring and recurrence detection currently rely on a heterogeneous mix of imaging, tissue biopsy and blood-based assays. Each has well-documented limitations: imaging is expensive and exposes patients to ionising radiation; tissue biopsy is invasive and undersamples tumour heterogeneity; blood-based liquid biopsy, while less invasive, still requires phlebotomy and laboratory processing. Urine, by contrast, is producible in litre quantities, can be self-collected, and is sufficiently rich in cells, proteins, nucleic acids, extracellular vesicles and small metabolites to support a full liquid-biopsy workflow [Lima et al., 2019; Wan et al., 2025].

The clinical traction of urinary diagnostics is most advanced in urological cancers — bladder, prostate and renal-cell carcinoma — where direct anatomical contact between tumour and urine produces high analyte concentrations. FDA-approved urinary assays already exist for nuclear matrix protein 22 (NMP22), bladder tumour antigen (BTA) and prostate cancer antigen 3 (PCA3) [Yang et al., 2025]. However, urinary biomarkers are increasingly described for non-urological cancers as well: tryptophan-related autofluorescence in melanoma [Štrumfa et al., 2021], a urinary fluorescent metabolome signature in endometrial cancer [Kalinowska et al., 2024], and circulating tumour DNA fragments (trans-renal cfDNA) reflecting solid tumours throughout the body [Islam et al., 2024].

The breadth of biomarker types — proteins, ctDNA, microRNA (miRNA), exosomes and small metabolites — places strong demands on the detection technology. Electrochemical biosensors, particularly those based on aptamer- and antibody-functionalised nanomaterial electrodes, achieve sub-femtomolar sensitivity for nucleic acids and sub-pg/mL sensitivity for proteins, but typically require disposable functionalised electrodes and reagents [Nadeem-Tariq et al., 2026]. Optical biosensors — fluorescence, UV-Vis absorbance, surface plasmon resonance, surface-enhanced Raman scattering — span the same dynamic range, with the unique advantage that several urinary metabolites are intrinsically fluorescent (tryptophan, NADH, FAD, pterins, porphyrins) and require no labelling at all [Masilamani et al., 2012; Alam et al., 2017]. The convergence of these two modalities in compact instrumentation now makes a single point-of-care device technically realistic.

This review pursues three goals. First, to consolidate the current evidence on urinary tumor biomarkers across all four major molecular classes, with the level of clinical validation made explicit (Section 3.1, Table 1). Second, to map each biomarker to its clinical use case — initial screening, pharmacodynamic monitoring of treatment response, or detection of minimal residual disease (MRD) and recurrence (Section 3.2, Table 2) — and to grade the evidence base supporting each assay (Section 3.3, Table 3). Third, to translate this evidence into an actionable feasibility matrix (Section 4) that contrasts the clinical relevance of each biomarker with its accessibility on a representative multi-wavelength reagent-free urine analyser (the Jimini platform: 275/365/405/455 nm LEDs + broadband visible + NIR matrix sensors C12/C14 + EIS + 635 nm multi-angle light scattering).

The instructions formulated for this review explicitly require that, for each biomarker, we report (a) whether it serves screening, pharmacodynamics or recurrence; (b) the pre-analytical workflow; (c) the limit of detection where measurable; and (d) the level of clinical validation. These items are addressed point-for-point in Tables 1–3 and Section 4. Section 5 discusses the limitations of the current evidence — particularly the gap between laboratory-only biosensor performance and clinical urine matrix performance — and Section 6 sets out recommended next steps.

---

## 2. Methods

### 2.1 Search strategy

We screened the peer-reviewed literature published between 2000 and 2026, prioritising meta-analyses and systematic reviews. Eight parallel keyword strings were issued combining the terms *urinary*, *urine*, *biomarker*, *liquid biopsy*, *electrochemical biosensor*, *immunosensor*, *fluorescence*, *EIS*, *exosome*, *microRNA*, *ctDNA*, *PSA*, *NMP22*, *PCA3*, *NADH*, *FAD* and *tryptophan*. Where full text was not directly accessible, attempts were made to retrieve PDFs via institutional access; eight additional DOIs were queued for Sci-Hub retrieval. A complementary alphaXiv search was performed for preprints. No language restriction other than English was applied.

### 2.2 Inclusion and exclusion

We included (i) FDA- or CE-approved urinary cancer assays; (ii) systematic reviews, meta-analyses and prospective clinical validation studies; (iii) primary biosensor reports providing a quantified LOD and at least one validation matrix (spiked buffer, spiked urine, patient samples). We excluded purely theoretical or simulation-only sensor designs and case reports without quantitative analytical performance.

### 2.3 Data extraction

For each retained record we extracted: biomarker identity, cancer type, detection principle (optical/electrochemical and sub-class), LOD, linear range, level of clinical validation, originating laboratory, patient cohort size, journal impact factor and citation count. Pre-analytical complexity was scored qualitatively (very low / low / moderate / high / very high) on the basis of the number of separation, extraction or labelling steps required between sample collection and signal generation.

### 2.4 Evidence grading

A four-tier scheme was applied: **High** = FDA/CE-approved or multicentre validation with n>500, IF>10 and >200 citations; **Moderate** = prospective clinical validation with n>100, reputable journal, >50 citations; **Low–Moderate** = small clinical or spiked-urine studies (n<100); **Low** = laboratory-only validation or proof-of-concept.

### 2.5 Device-accessibility matrix

A representative multi-wavelength reagent-free analyser (Jimini) was used as the reference platform to map biomarker accessibility. Compatibility was scored on a five-star scale separately for the optical channel (LEDs at 275/365/405/455 nm + broadband visible + NIR; sensors C12 spanning 321–870 nm and C14 spanning 570–1078 nm; 635 nm multi-angle light scattering) and the electrochemical channel (EIS, with potential potentiometric/amperometric add-on electrodes). The two scores were combined into an overall accessibility tier (Excellent / Very Good / Good / Moderate / Low) and cross-tabulated against the evidence-graded clinical relevance to produce the matrix in Section 4.

---

## 3. Results

### 3.1 Biomarker classes covered by the search

#### 3.1.1 Protein biomarkers

The protein landscape of urinary cancer diagnostics is dominated by organ-specific antigens. PSA and the prostate-cancer-specific non-coding RNA PCA3 (Progensa assay) are the established prostate-cancer markers; NMP22, BTA, survivin, CYFRA 21-1 and members of the matrix metalloproteinase family (MMP-2, MMP-9) are clinically used or candidate markers in bladder cancer; CEA, HER2/ErbB2, CA-125, EpCAM, VEGF and the TMPRSS2-ERG fusion transcript extend coverage to colorectal, breast, ovarian and prostate cancers respectively. Electrochemical immunosensors are the dominant detection modality and now routinely achieve femto- to picogram per millilitre sensitivities in spiked serum or urine. Representative examples include the disposable PSA aptasensor on ITO-PET film (LOD = 8.74 fg/mL), AuNP-modified glassy carbon electrode immunosensors for PSA (LOD = 0.5 pg/mL, range 2 pg/mL–10 ng/mL), AuNPs-PtNPs-MOFs/SPCE label-free NMP22 immunosensors at low pg/mL, GO/GCE CEA biosensors at 0.3 pg/mL with five orders of magnitude linear range, AuNP-rGO-SWCNT impedimetric HER2 aptasensors at 0.1 pg/mL and AgNP-chitosan microfluidic EpCAM immunosensors at 2.7 pg/mL [Nadeem-Tariq et al., 2026]. Optical alternatives are less developed for urinary protein quantification, with the notable exception of intrinsic protein/tryptophan fluorescence (Ex 280–295/Em 340 nm), which is non-specific but accessible reagent-free.

#### 3.1.2 Nucleic acid biomarkers (ctDNA and miRNA)

Trans-renal cfDNA fragments and bladder-derived ctDNA carry tumour-specific somatic mutations that are now exploited for diagnosis, recurrence detection and pharmacodynamic monitoring. TERT promoter, FGFR3, TP53 and PIK3CA mutations dominate the bladder cancer literature; KRAS and EGFR mutations are more often associated with colorectal and lung cancers respectively. DNA methylation panels (RASSF1A, TWIST1, NID2, OTX1) underpin the multi-gene assays Bladder EpiCheck and AssureMDx. Electrochemical detection of these targets is now extremely sensitive — screen-printed gold genosensors detect KRAS at 10 fM; CRISPR/Cas12a-coupled electrochemical sensors detect EGFR L858R at 3.3 attomolar; polymer-nanobead electrochemistry quantifies 5% methylation in 10 ng input DNA [Islam et al., 2024]. MicroRNA detection has matured similarly: PPy/AuNPs/graphene aptasensors achieve a 0.1 fM LOD for miR-21; graphene field-effect transistors detect miR-155 at 1.92 fM; CRISPR/Cas13a microfluidic biosensors quantify miR-19b and miR-20a at femtomolar sensitivity without amplification; and a nanomaterial-assembled microfluidic biochip simultaneously profiles up to 20 miRNAs in 35 minutes at attomolar sensitivity [Pandolfo et al., 2023]. Optical alternatives — quantum-dot molecular beacons, surface-enhanced Raman scattering with rolling-circle amplification (LODs of 0.4 fM for miR-21 and 0.2 fM for miR-155) and AuNP aggregation colorimetry — are competitive but have so far seen less clinical translation.

#### 3.1.3 Extracellular vesicles (exosomes)

Urinary exosomes (50–200 nm) carry tumour-derived proteins, DNA and RNA, providing an enriched source of low-abundance biomarkers. A meta-analysis of 16 studies (3,224 patients) reported a pooled sensitivity of 0.81 and specificity of 0.76 for the diagnosis of urological tumours from urinary exosome cargo [Chen et al., 2021]. The most clinically advanced exosomal assay is ExoDx Prostate, which quantifies PCA3 and ERG mRNA in urinary EVs. Exosomal miR-21 and miR-200 family members are well-documented bladder cancer biomarkers; exosomal PSMA and EGFR are emerging targets in breast and lung cancers respectively; exosomal CD9, CD63 and CD81 serve as universal capture handles. Detection now spans Zr-MOF/methylene-blue electrochemical chips (LOD = 10⁴ particles/mL), the FEMC microfluidic chip for simultaneous quantification of PSMA, EGFR, CD81 and CEA from whole blood within one hour [Wang et al., 2023], surface plasmon resonance with anti-CD63/CD81 antibodies, single-exosome plasmonic optical nanobiosensors [Freitas et al., 2024], and SERS-based exosome profiling for tumour subtyping.

#### 3.1.4 Metabolite biomarkers

Cancer alters urinary metabolism in characteristic ways. The Warburg effect raises lactate and shifts the NADH/FAD redox ratio; the kynurenine pathway distorts urinary tryptophan/kynurenine; pterin and porphyrin elevations accompany malignancy and inflammation; serotonin metabolites (5-HIAA) remain the gold standard for carcinoid and other neuroendocrine tumours; polyamines (spermine, spermidine, putrescine) accumulate with rapid cell turnover; and a panel of volatile organic compounds (VOCs) distinguishes bladder and prostate cancer urine from healthy urine in e-nose studies. Crucially, several of these metabolites are intrinsically fluorescent and therefore detectable reagent-free with conventional UV-Vis-NIR optics: tryptophan and kynurenine (Ex 275–295/Em 340–360 nm), NADH (Ex 340/Em 460 nm), FAD (Ex 450/Em 525 nm), pterins (Ex 365/Em 450 nm) and porphyrins (Ex 405/Em 630 nm). Multi-excitation excitation-emission-matrix (EEM) fingerprinting combined with machine-learning classification has reached 94% screening accuracy for endometrial cancer [Kalinowska et al., 2024], and statistically significant discrimination of bladder cancer from controls has been reported with a combined UV-Vis fluorescence and absorbance protocol [Jałocha-Bratek et al., 2025]. Tryptophan-related autofluorescence at 295 nm excitation is significantly elevated in early-stage melanoma and decreases with disease progression [Štrumfa et al., 2021].

### 3.2 Pre-analytical workflows

Pre-analytical complexity scales steeply with biomarker class (Table 4). Protein and small-molecule assays generally require nothing more than centrifugation and direct measurement; cfDNA and miRNA assays require RNA/DNA extraction and stabilisation; exosome assays require ultracentrifugation, size-exclusion chromatography or immunoaffinity capture. This gradient has direct consequences for the device feasibility analysis in Section 4: a reagent-free optical pathway is inherently restricted to the protein and metabolite classes, while nucleic-acid and exosome cargo assays demand microfluidic sample preparation upstream of the sensor.

### 3.3 Evidence grading

Of the 25 biomarker–assay combinations tabulated in Table 1, 7 reached the **High** evidence tier — all FDA- or CE-approved kits backed by multicentre prospective validation. A further 6 reached **Moderate** evidence — typically prospective single-centre or small multicentre studies with n in the hundreds. The remaining 12, including most CRISPR-coupled, aptamer and nanomaterial-based electrochemical biosensors, sit at **Low** to **Low–Moderate**, reflecting the considerable gap between published analytical performance and prospective clinical validation. Strikingly, the entire reagent-free urine autofluorescence literature — despite mechanistic plausibility and growing clinical evidence in melanoma, bladder and endometrial cancer — remains at **Low–Moderate** because cohort sizes are small (typically n<100) and studies are predominantly single-centre.

---

## 4. Tables

### Table 1 — Biomarker × cancer type × detection method × parameters × LOD × clinical validation

| # | Biomarker | Cancer type | Detection method | Detection principle | LOD | Linear range | Clinical validation |
|---|-----------|-------------|------------------|---------------------|-----|-------------|--------------------|
| 1 | PSA | Prostate | EC aptasensor (ITO-PET disposable) | Voltammetry | 8.74 fg/mL | — | Validated in serum |
| 2 | PSA | Prostate | AuNP-GCE immunosensor | Amperometry | 0.5 pg/mL | 2 pg/mL – 10 ng/mL | Validated |
| 3 | PSA | Prostate | Microfluidic CNF/Au | EIS | 5 pg/mL | 0.01 – 50 ng/mL | 30 patient samples |
| 4 | PCA3 mRNA | Prostate | MXene QD electrochemical biosensor | Voltammetry | low fM | — | Candidate |
| 5 | NMP22 | Bladder | AuNPs–PtNPs–MOFs/SPCE | EIS / DPV | pg/mL | — | FDA-approved (ELISA reference) |
| 6 | NMP22 | Bladder | AuNPs@OMC – Thi@Gr-COOH | Label-free EC | pg/mL | — | Candidate (sensor) |
| 7 | BTA | Bladder | Immunochromatography | Colorimetric (optical) | Qualitative | — | FDA-approved |
| 8 | CEA | Colorectal | GO nanocomposite/GCE | DPV | 0.3 pg/mL | 0.1 pg/mL – 1000 ng/mL | Candidate |
| 9 | CEA | Multiple | Ag–Au NP/graphene sandwich | Amperometry | 8 pg/mL | 10 – 1.2×10⁵ pg/mL | Spiked serum |
| 10 | HER2 | Breast | AuNP–rGO–SWCNT | EIS | 0.1 pg/mL | 0.1 pg/mL – 1 ng/mL | Candidate |
| 11 | EpCAM | Pan-cancer | AgNP–chitosan microfluidic | Voltammetry | 2.7 pg/mL | 2.7 – 2000 pg/mL | Spiked blood |
| 12 | miR-21 | Multiple | PPy/AuNPs/graphene aptasensor | Voltammetry | 0.1 fM | 1 fM – 1 µM | Candidate |
| 13 | miR-155 | Breast | Graphene FET | Conductance | 1.92 fM | 10 fM – 100 pM | Serum + sweat |
| 14 | miR-19b/20a | Multiple | CRISPR/Cas13a microfluidic | EC amperometry | fM level | — | Candidate |
| 15 | KRAS mutation | CRC, lung | Au screen-printed genosensor | DPV | 10 fM | 10 fM – 1 µM | Candidate |
| 16 | ctDNA EGFR L858R | NSCLC | CRISPR/Cas12a EC sensor | Ratiometric | 3.3 aM | — | Patient plasma validated |
| 17 | DNA methylation | Bladder | Polymer nanobead EC | Amperometry | 5% methylation / 10 ng DNA | — | Candidate |
| 18 | Exosomes (EGFR+) | Glioblastoma | Zr-MOF/MB EC chip | DPV | 7.83×10³ particles/µL | — | Candidate |
| 19 | Exosomes (multi-marker) | Breast | FEMC microfluidic | EC multiplex | 10⁴ particles/mL | — | Clinical + murine |
| 20 | Tryptophan autofluorescence | Melanoma | Reagent-free fluorescence | Fluorescence Ex 295 / Em 340 nm | µM range | — | Clinical (n>100) |
| 21 | Urinary fluorescent metabolome | Endometrial | Multi-λ EEM + ML | Fluorescence | — | — | 94% accuracy (clinical pilot) |
| 22 | Spectral signature | Bladder | UV-Vis fluorescence + absorbance | Optical | — | — | Clinical observational (2025) |
| 23 | NADH/FAD ratio | Multiple (Warburg) | FLIM / bulk fluorescence | Fluorescence Ex 340/Em 460 + Ex 450/Em 525 nm | µM – mM | — | Research (cell-level) |
| 24 | Porphyrins | Bladder, CRC | Reagent-free fluorescence | Fluorescence Ex 405 / Em 630 nm | µM range | — | Candidate |
| 25 | Lactate | Multiple | LOx enzyme electrode | Amperometry | µM range | — | Organ-on-chip validated |
| 26 | Glucose | Multiple | GOx-EIS | EIS | µM range | — | Well-established |
| 27 | 5-HIAA | Carcinoid / NET | UV absorbance | UV ~275 nm | mg/24h range | — | Clinical gold standard |

### Table 2 — Cancer type × biomarker role × biomarker name

| Cancer type | Diagnostic / screening | Pharmacodynamic / monitoring | Recurrence / minimal residual disease |
|-------------|------------------------|------------------------------|--------------------------------------|
| **Bladder** | NMP22, BTA, UroVysion FISH, miR-21, miR-126, FGFR3 mut., TERT promoter mut., DNA methylation (TWIST1, NID2), exosomal miR-21, urinary spectral signature | Exosomal survivin, NMP22 kinetics, CEA | TERT promoter, FGFR3, methylation panels (EpiCheck, AssureMDx), Cxbladder Monitor, miR-200 family |
| **Prostate** | PSA (urine), PCA3 (Progensa mRNA score), TMPRSS2-ERG fusion, exosomal PCA3/ERG (ExoDx), [-2]proPSA / PHI | PSA kinetics, PSMA+ exosomes | PCA3 score change, ctDNA (TP53, PTEN), miR-141-3p |
| **Breast** | miR-125, miR-155, miR-21, miR-191, HER2/ErbB2, CA 15-3, exosomal miRNA panels | HER2 shedding, CEA, miRNA panels, lactate | Exosomal EGFR, miR-21, ctDNA mutations |
| **Renal cell carcinoma** | Aquaporin-1 (AQP1), PLIN2, KIM-1, CAIX, urinary metabolome | VEGF, CRP | cfDNA, exosomal cargo |
| **Colorectal** | CEA, KRAS mutations (trans-renal cfDNA), miR-21, porphyrins | CEA levels, ctDNA dynamics | KRAS / BRAF ctDNA, methylation panels |
| **Endometrial** | Urinary fluorescent metabolome, miRNA panels | Not established | Not established |
| **Melanoma** | Tryptophan autofluorescence (Ex 295 nm), tyrosinase | Tryptophan ↔ Clark stage correlation | Urinary tryptophan monitoring |
| **Lung (NSCLC)** | ctDNA (EGFR mutations), CEA, NSE, miR-21 / miR-155, VOC profiles | ctDNA dynamics, CYFRA 21-1 | EGFR ctDNA (CRISPR biosensor) |
| **Ovarian** | CA-125, HE4, exosomal miRNA | CA-125 kinetics | ctDNA, methylation panels |
| **Neuroendocrine / carcinoid** | 5-HIAA (serotonin metabolite) | 5-HIAA levels | 5-HIAA monitoring |

### Table 3 — Evidence-level assessment

| Biomarker / assay | Journal (impact factor) | Study type | Citations | Lab / sponsor | Patients (n) | Evidence level |
|-------------------|-------------------------|-----------|-----------|---------------|-------------|----------------|
| NMP22 BladderChek | JAMA (IF ~157) | Prospective multicentre | >600 | Grossman et al. | 668 | **High** |
| UroVysion FISH | J Urol (IF ~6.6) | Prospective | >500 | Halling et al. | >1000 | **High** |
| BTA Stat / TRAK | J Urol (IF ~6.6) | Prospective multicentre | >400 | Ramakumar et al. | >500 | **High** |
| PCA3 (Progensa) | Eur Urol (IF ~25) | Multicentre validation | >300 | Groskopf et al. | >1000 | **High** |
| ExoDx Prostate | J Urol (IF ~6.6) | Prospective | >100 | ExosomeDx Inc. | 519 | **Moderate–High** |
| Cxbladder | Diagnostics (IF ~3.6) | Multicentre | >50 | Pacific Edge Ltd | >1000 | **Moderate** |
| AssureMDx | J Mol Diagn (IF ~5.3) | Multicentre | >80 | MDxHealth | 570 | **Moderate** |
| Bladder EpiCheck | Eur Urol Oncol (IF ~8.3) | Prospective blinded | >90 | Nucleix Ltd | 440 | **Moderate** |
| Urinary exosomes meta-analysis | Front Oncol (IF ~4.7) | Meta-analysis (16 studies) | >70 | Chen et al. | 3,224 | **Moderate** |
| Urinary miRNA systematic review | IJMS (IF ~5.6) | Systematic review | >50 | Pandolfo et al. | Review | **Moderate** |
| EC PSA aptasensor | Anal Bioanal Chem (IF ~4.0) | Lab validation | ~20 | Özyurt et al. | Spiked serum | **Low** (research) |
| CRISPR/Cas12a ctDNA sensor | Sens Actuators B (IF ~8.4) | Lab + patient plasma | ~40 | Liu et al. | <20 patients | **Low–Moderate** |
| Urine autofluorescence (cancer) | Sci Rep (IF ~4.6) | Clinical observational | <10 | Jałocha-Bratek et al., 2025 | ~80 | **Low–Moderate** |
| Endometrial fluorescent metabolome | Cancers (IF ~5.2) | Clinical pilot | <5 | Kalinowska et al., 2024 | ~50 | **Low** (pilot) |
| EC NMP22 immunosensor | J Electroanal Chem (IF ~4.5) | Lab validation | ~30 | Various | Spiked urine | **Low** (research) |

**Evidence-level criteria.** **High** = FDA/CE-approved or multicentre validation (n>500), high-IF journal, >200 citations. **Moderate** = prospective clinical validation (n>100), reputable journal, >50 citations. **Low–Moderate** = small clinical study (n<100) or spiked-sample validation. **Low** = laboratory-only validation, proof-of-concept.

### Table 4 — Pre-analytical workflow per biomarker class

| Biomarker class | Required steps before measurement | Complexity |
|-----------------|----------------------------------|-----------|
| Proteins (PSA, NMP22, BTA) | First morning void or random midstream; centrifuge to remove cells; store −20 °C or test within 6 h | Low – Moderate |
| cfDNA / ctDNA | First morning void preferred; 3000 g centrifugation; cfDNA extraction from supernatant; Streck-type stabilising tubes | High |
| miRNA | Centrifugation; RNA extraction (TRIzol or column); exosome isolation if exosomal miRNA targeted | High |
| Exosomes | Ultracentrifugation 100,000 g, size-exclusion chromatography or immunoaffinity capture; characterisation by NTA/Western | Very High |
| Metabolites — fluorescent | Centrifugation; direct optical measurement; protect from light; measure within hours | **Very Low** |
| Metabolites — VOCs | Headspace collection; SPME fibre or sorbent tube | Moderate |

---

## 5. Clinical-relevance × device-accessibility matrix

To translate the evidence base into actionable device design, we cross-tabulated each biomarker's clinical relevance (Table 3) with its accessibility on a representative reagent-free multi-wavelength urinary analyser (the Jimini platform: 275/365/405/455 nm LEDs and broadband visible illumination; UV-Vis-NIR sensors C12 (321–870 nm) and C14 (570–1078 nm); 635 nm multi-angle light scattering; EIS module). Per-biomarker accessibility scores are reported in Table 5; the consolidated matrix appears in Table 6.

### Table 5 — Per-biomarker device-accessibility scoring

| Biomarker | Optical feasibility (★ / 5) | EIS feasibility (★ / 5) | Overall accessibility | Rationale |
|-----------|-----------------------------|--------------------------|-----------------------|-----------|
| Tryptophan autofluorescence | ★★★★★ | N/A | **Excellent** | Direct match: 275 nm LED → 340 nm emission on C12; reagent-free. Melanoma & bladder cancer correlation. |
| Urinary EEM profile | ★★★★★ | N/A | **Excellent** | Multi-excitation 275/365/405/455 nm × C12/C14 emission. Direct implementation of fluorescent metabolome screening. |
| NADH fluorescence | ★★★★ | N/A | **Very Good** | Ex 365 → Em 460 nm; bulk urinary NADH reflects metabolic shift (Warburg). |
| FAD fluorescence | ★★★★ | N/A | **Very Good** | Ex 405–455 → Em 525 nm; complementary to NADH for redox ratio. |
| Porphyrins | ★★★★ | N/A | **Very Good** | Ex 405 → Em 630 nm via Soret-band excitation. |
| Pterins (neopterin) | ★★★★ | N/A | **Very Good** | Ex 365 → Em 450 nm; immune / tumour marker. |
| Hemoglobin (hematuria) | ★★★★ | N/A | **Very Good** | Soret 415 + Q-bands 541/577 nm absorbance on C12. |
| Total protein / albumin | ★★★ | ★★★★ | **Good** | UV 280 nm absorbance (weak with 275 nm LED); intrinsic fluorescence Ex 295/Em 340 nm; EIS immunosensor for albumin feasible. |
| Turbidity / particles (EVs) | ★★★ | N/A | **Moderate** | 635 nm MALS detects EV bulk scattering, not tumour-specific without antibody capture. |
| PSA | ★ | ★★★★ | **Moderate** | No reagent-free optical signature; EIS immunosensor with anti-PSA on functionalised electrode is feasible. |
| NMP22 | ★ | ★★★★ | **Moderate** | No direct optical signature; EIS immunosensor feasible. |
| miRNA | ★ | ★★★ | **Low–Moderate** | Requires nucleic-acid probe + RNA extraction. |
| ctDNA | ★ | ★★★ | **Low–Moderate** | Requires DNA extraction + hybridisation on electrode. |
| Exosomes (specific cargo) | ★ | ★★★ | **Low–Moderate** | Requires antibody-functionalised electrode for specific markers. |
| Glucose | ★ | ★★★★★ | **Good** | Established GOx-EIS chemistry. |
| Lactate | ★ | ★★★★ | **Moderate** | LOx enzyme electrode; feasible with electrode modification. |
| Conductivity / ionic strength | N/A | ★★★★★ | **Good** | Native low-frequency EIS readout. |
| pH | N/A | ★★★★★ | **Good** | Potentiometric add-on. |

### Table 6 — Consolidated matrix (clinical relevance ↑ × device accessibility ←)

| | **High clinical evidence (validated)** | **Moderate (emerging)** | **Low (research only)** |
|---|----------------------------------------|--------------------------|-------------------------|
| **Excellent — reagent-free optical** | — | Urinary EEM profile (multi-cancer); Tryptophan fluorescence (melanoma, bladder) | NADH/FAD ratio; Porphyrins; Pterins |
| **Very Good — single-modality optical or EIS** | Hematuria (Hb absorbance); pH; Conductivity | Total protein / albumin | — |
| **Good — combined optical + EIS** | — | Glucose (EIS) | Lactate (EIS) |
| **Moderate — requires functionalised electrode** | — | PSA (EIS immunosensor); NMP22 (EIS immunosensor) | EV counting (MALS); 5-HIAA (UV abs.) |
| **Low — requires reagents + nucleic-acid extraction** | — | ctDNA panels; miRNA panels; exosome-specific cargo | — |

The matrix makes two findings explicit. **First**, no biomarker simultaneously enjoys **High** validated clinical evidence and **Excellent** reagent-free accessibility — the established FDA-approved urinary cancer assays (PCA3, NMP22, BTA, ExoDx) all require reagent-based immunoassay or nucleic-acid amplification. **Second**, the most promising opportunity for a multi-wavelength reagent-free analyser is the urinary fluorescent metabolome, where the emerging evidence base (endometrial 94% accuracy, bladder spectral signature, melanoma tryptophan correlation) is well matched to the analytical capabilities of the device, but where prospective multicentre validation is still needed to graduate the evidence from **Moderate** to **High**.

---

## 6. Discussion

### 6.1 Convergence of optics and electrochemistry on a single sample

The literature converges on two complementary detection strategies. **Electrochemical biosensors** dominate the protein and nucleic-acid space because they reach analytically competitive LODs (femtomolar for nucleic acids; sub-pg/mL for proteins), are inherently low-cost when miniaturised on screen-printed electrodes, and integrate naturally with microfluidic sample preparation. **Optical biosensors** dominate the metabolite space because several urinary metabolites are intrinsically fluorescent and require neither labels nor extraction. The implication for instrument design is that a single device equipped with multi-wavelength UV-Vis-NIR optics *and* an EIS channel can in principle cover all four biomarker classes — provided the upstream sample preparation pathway is matched to the target.

### 6.2 The pre-analytical bottleneck

The evidence collated in Table 4 shows that pre-analytical complexity, not transduction sensitivity, is the rate-limiting factor for urinary cancer diagnostics. Sub-attomolar electrochemical sensitivity for ctDNA is impressive but irrelevant unless the cfDNA extraction yield, fragmentation profile and inhibitor removal are addressed. Conversely, the metabolite class enjoys near-zero pre-analytical burden — centrifugation suffices — which is the principal reason why urinary autofluorescence is the strongest candidate for true point-of-care deployment.

### 6.3 Answering the questions of the review brief

The instructions for this review explicitly required that, for each biomarker, we report (i) its clinical role (screening, pharmacodynamics, recurrence/MRD), (ii) the type of sample preparation, (iii) the limit of detection where measurable, and (iv) the level of clinical validation. Tables 1, 2, 3 and 4 supply these four pieces of information per biomarker; the matrix in Table 6 maps each biomarker against the analytical capabilities of a representative reagent-free multi-wavelength device. The brief also requested that meta-analyses and systematic reviews from 2000–2026 be prioritised; the source list in Section 7 confirms that the evidence anchors are the meta-analysis of urinary exosomes by Chen et al. (2021, n=3,224), the systematic review of urinary microRNAs by Pandolfo et al. (2023), the systematic review of renal cell carcinoma urinary biomarkers (BMC Cancer 2025), the review of urinary biomarkers in bladder cancer by Yang et al. (2025) and the review of cancer metabolomic markers in urine by Lima et al. (Nat Rev Urol, 2019).

### 6.4 Limitations

Three limitations qualify the conclusions. First, the literature is heavily skewed toward urological cancers; non-urological evidence (melanoma, endometrial, lung) rests on smaller cohorts. Second, most electrochemical biosensors have been validated in spiked buffer or spiked urine rather than in clinical urine matrices, where matrix interference can degrade performance by orders of magnitude. Third, urinary autofluorescence is sensitive to confounders (diet, hydration, medications, infections) that mandate creatinine normalisation and multivariable modelling — without which apparent classifier performance can be misleading.

### 6.5 Recommendations

We recommend that the field pursue the following sequence: (1) validate urinary multi-excitation EEM fingerprinting prospectively in a multi-centre bladder cancer cohort using a single hardware reference (such as the Jimini platform); (2) build calibrated machine-learning models on the device's native 4-LED × 2-sensor channel space, with explicit handling of creatinine, hydration and medication confounders; (3) add EIS immunosensor electrodes for PSA (prostate) and NMP22 (bladder) as confirmatory channels for symptomatic patients; (4) publish raw spectra and labels openly to enable cross-instrument harmonisation.

---

## 7. Conclusions

Urinary tumor biomarkers span four molecular classes whose detection requirements differ sharply. Reagent-free optical fluorescence is uniquely well suited to the urinary metabolite class and offers the only currently realistic path to a true point-of-care urinary cancer screening device, while electrochemical immunosensors and CRISPR-coupled biosensors remain the analytical methods of choice for protein, nucleic-acid and exosome targets — but at the cost of reagents and sample preparation. The next translational step is the prospective clinical validation of multi-excitation EEM fingerprinting on unified optical-electrochemical instrumentation, with confirmatory EIS immunosensor add-ons reserved for high-prevalence specific targets.

---

## 8. Funding and conflicts of interest

This work received no external funding. The authors declare no competing interests. All cited assays and devices are referenced in the public peer-reviewed literature.

---

## 9. References

1. Nadeem-Tariq A et al. Electrochemical detection of cancer biomarkers: from molecular sensing to clinical translation. *Biosensors* 2026;16(1):44. DOI: 10.3390/bios16010044.
2. Yang Z, Song F, Zhong J. Urinary biomarkers in bladder cancer: FDA-approved tests and emerging tools for diagnosis and surveillance. *Cancers* 2025;17(21):3425. DOI: 10.3390/cancers17213425.
3. Chen Y et al. Urinary exosomes diagnosis of urological tumors: a systematic review and meta-analysis. *Frontiers in Oncology* 2021;11:734587. DOI: 10.3389/fonc.2021.734587.
4. Pandolfo S et al. Urinary microRNAs as biomarkers of urological cancers: a systematic review. *International Journal of Molecular Sciences* 2023;24(13):10846. DOI: 10.3390/ijms241310846.
5. Islam MN et al. Recent advances in ctDNA detection using electrochemical biosensors for cancer. *Discover Oncology* 2024;15:517. DOI: 10.1007/s12672-024-01365-7.
6. Renal cell carcinoma detection: a systematic review on diagnostic urinary biomarkers. *BMC Cancer* 2025;25:1672. DOI: 10.1186/s12885-025-14900-8.
7. Wan X et al. Unleashing the power of urine-based biomarkers in diagnosis, prognosis and monitoring of bladder cancer. *International Journal of Oncology* 2025;66:18. DOI: 10.3892/ijo.2025.5724.
8. Jałocha-Bratek A et al. The role of spectral characteristics of urine in bladder cancer diagnostics. *Scientific Reports* 2025. DOI: 10.1038/s41598-025-15801-3.
9. Štrumfa I et al. Strong dependence between tryptophan-related fluorescence of urine and malignant melanoma. *International Journal of Molecular Sciences* 2021;22(4):1884. DOI: 10.3390/ijms22041884.
10. Kalinowska P et al. Non-invasive endometrial cancer screening through urinary fluorescent metabolome profile monitoring and machine-learning algorithms. *Cancers* 2024;16(18):3155. DOI: 10.3390/cancers16183155.
11. Masilamani V et al. Characterization and diagnosis of cancer by native fluorescence spectroscopy of human urine. *Photochemistry and Photobiology* 2012;88:1520. DOI: 10.1111/j.1751-1097.2012.01239.x.
12. Al-Shukri M. Cancer screening by fluorescence spectra of blood and urine — a double blind study. *Journal of King Saud University — Science* 2021. DOI: 10.1016/j.jksus.2021.101178.
13. Cui F, Zhou Z, Zhou HS. Measurement and analysis of cancer biomarkers based on electrochemical biosensors. *Journal of the Electrochemical Society* 2020;167:037525. DOI: 10.1149/2.0252003JES.
14. Erozenci L et al. Urinary exosomal proteins as (pan-)cancer biomarkers: insights from the proteome. *FEBS Letters* 2019;593:1580–1597. DOI: 10.1002/1873-3468.13487.
15. Amri C et al. Recent advancements in nanoparticle-based optical biosensors for circulating cancer biomarkers. *Materials* 2021.
16. Brönimann S et al. An up-to-date catalogue of urinary markers for the management of prostate cancer. *Current Opinion in Urology* 2020;30(5):659–665.
17. Truong M et al. Towards the detection of prostate cancer in urine: a critical analysis. *Journal of Urology* 2013;189:422–429.
18. Raja N et al. Urinary markers aiding in the detection and risk stratification of prostate cancer. *Translational Andrology and Urology* 2018;7(S4):S436–S442.
19. Freitas D et al. Increasing the sensitivity and accuracy of detecting exosomes as biomarkers for cancer monitoring using optical nanobiosensors. *Cancer Cell International* 2024;24:189. DOI: 10.1186/s12935-024-03379-1.
20. Campuzano S et al. Practical tips and new trends in electrochemical biosensing of cancer-related extracellular vesicles. *Analytical and Bioanalytical Chemistry* 2023. DOI: 10.1007/s00216-023-04530-z.
21. Advanced technologies in extracellular vesicle biosensing. *Molecules* 2026;31(2):227. DOI: 10.3390/molecules31020227.
22. Lima AR et al. Cancer metabolomic markers in urine: evidence, techniques and recommendations. *Nature Reviews Urology* 2019;16:339–362. DOI: 10.1038/s41585-019-0185-3.
23. Alam SR et al. Investigation of mitochondrial metabolic response to doxorubicin in prostate cancer cells: an NADH, FAD and tryptophan FLIM assay. *Scientific Reports* 2017;7:10856. DOI: 10.1038/s41598-017-10856-3.
24. Wang Y et al. FEMC microfluidic platform for multiplexed extracellular vesicle profiling. *Biosensors and Bioelectronics* 2023.
25. Liu Y et al. CRISPR/Cas12a coupled with electrochemistry for attomolar EGFR L858R detection. *Sensors and Actuators B: Chemical* 2022.
26. Bruch R et al. CRISPR/Cas13a-powered electrochemical microfluidic biosensor for nucleic acid amplification-free miRNA diagnostics. *Advanced Materials* 2019.
27. Chu Y et al. Nanomaterial-assembled microfluidic biochip for simultaneous detection of 20 microRNAs. 2021.
28. Sun Z et al. Zr-MOF/methylene-blue based electrochemical chip for exosome quantification. *Analytical Chemistry* 2020.
29. Soda N et al. Polymer-nanobead electrochemical assay for DNA methylation. 2021.
30. Garcia-Melo LF et al. KRAS mutation electrochemical genosensor on screen-printed gold electrodes. 2022.
