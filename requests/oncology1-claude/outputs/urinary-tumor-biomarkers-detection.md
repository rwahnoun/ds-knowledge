# Urinary Tumor Biomarkers Detectable via Optical and Electrochemical Methods: A Systematic Review

## Executive Summary

Urine represents an ideal biofluid for non-invasive cancer detection due to its ease of collection, patient compliance, and concentration of tumor-derived analytes—particularly for urological malignancies. This review systematically surveys urinary tumor biomarkers across four molecular classes (proteins, nucleic acids, extracellular vesicles, and metabolites) detectable via optical (fluorescence, absorbance/colorimetry, SERS, SPR) and electrochemical (voltammetry, amperometry, EIS) biosensor platforms. We synthesize evidence from reviews, original research, and meta-analyses published primarily between 2020 and 2026.

Key findings: (1) Electrochemical biosensors consistently achieve lower limits of detection (LODs) than conventional immunoassays, with nanomaterial-enhanced platforms reaching femtomolar to attomolar sensitivity for miRNAs and sub-pg/mL for protein markers. (2) Optical biosensors, particularly SERS-based platforms, enable label-free multiplexed analysis of urine directly. (3) Most urinary biomarker–sensor combinations remain at the small-sample validation stage; clinical translation is limited by reproducibility, standardization of urine processing, and regulatory approval. (4) The field is moving toward point-of-care testing (POCT) devices integrating microfluidics with biosensors for rapid urinary cancer screening.

## 1. Introduction

Cancer remains a leading cause of mortality globally, with approximately 19.3 million new cases and 10 million deaths in 2020. Early detection significantly improves survival, yet current screening methods rely heavily on invasive procedures (biopsies, cystoscopy) or blood-based biomarkers with limited specificity. Urine-based liquid biopsy offers a compelling alternative: it is entirely non-invasive, can be collected repeatedly, and directly contacts the urinary tract epithelium—making it particularly relevant for bladder, prostate, and kidney cancers.

Two major classes of biosensor transduction are relevant to urinary biomarker detection:

- **Optical methods:** Fluorescence (including FRET), absorbance/colorimetry, surface-enhanced Raman scattering (SERS), surface plasmon resonance (SPR), and localized SPR (LSPR).
- **Electrochemical methods:** Cyclic voltammetry (CV), differential pulse voltammetry (DPV), square wave voltammetry (SWV), amperometry, and electrochemical impedance spectroscopy (EIS).

This review organizes findings by biomarker class, provides a comparative table of biomarker–method pairs with LODs and clinical utility, and discusses technology comparisons and clinical readiness.

## 2. Protein Biomarkers

### 2.1 Prostate-Specific Antigen (PSA)

PSA is the most widely used serum marker for prostate cancer but has well-documented specificity limitations (17–50% overdiagnosis rate). Urinary PSA and PSA derivatives have been explored with both electrochemical and optical biosensors.

**Electrochemical detection:**
- Multiple platforms using DPV, SWV, and EIS with nanomaterial-enhanced electrodes (AuNPs, graphene composites, carbon nanotubes) have been reported. LODs typically range from **0.01–1 pg/mL** for sandwich immunoassays using signal amplification strategies.
- Dowlatshahi & Abdekhodaie (2021) reviewed electrochemical PSA biosensors based on electroconductive nanomaterials and polymers, reporting LODs in the fg/mL–pg/mL range for laboratory buffer, with clinical serum validation in small cohorts.
- Traynor et al. (2020) reviewed recent advances in electrochemical PSA detection in clinically relevant samples, noting that sample matrix effects remain a major challenge for urine-based detection.

**Optical detection:**
- Aptamer-based optical/electrochemical hybrid sensors for PSA have been reviewed comprehensively (Jolly et al., 2019), covering fluorescence, SPR, and colorimetric approaches. LODs range from **0.1 pg/mL to ng/mL** depending on the amplification strategy.
- SERS-based label-free urine analysis using 3D-stacked AgNW-glass fiber filters has been demonstrated for prostate cancer diagnosis (Phyo et al., 2021, Anal. Chem.), achieving classification of cancer vs. healthy urine samples rather than quantitative PSA measurement.

**Clinical utility:** Screening/diagnosis. PSA remains primarily a serum marker; urinary PSA detection via biosensors is at the research stage.

### 2.2 Nuclear Matrix Protein 22 (NMP22)

NMP22 is an FDA-approved urinary biomarker for bladder cancer surveillance (NMP22® BladderChek test), though it has limited sensitivity for low-grade tumors and high false-positive rates with inflammation.

**Fluorescent immunosensor:**
- Othman et al. (2020, RSC Advances) developed a fluorescent immunosensor for NMP22 using quantum dots (CdTe/CdS QDs) conjugated with anti-NMP22 antibodies. The sensor achieved a LOD of **0.05 pg/mL** with a linear range of 0.05–20 pg/mL, far exceeding the sensitivity of the commercial NMP22 BladderChek point-of-care test.

**Clinical utility:** Screening/diagnosis and surveillance (FDA-approved as adjunct to cystoscopy for surveillance of recurrent NMIBC).

### 2.3 Carcinoembryonic Antigen (CEA)

CEA is a glycoprotein biomarker elevated in colorectal, gastric, lung, and other cancers. While primarily a serum marker, CEA has been detected in urine.

**Electrochemical detection:**
- Three-dimensional PdAuCu nanocrystal-based immunosensors achieved LOD of **0.23 pg/mL** for CEA using DPV (Chen et al., 2019).
- MOF-based impedimetric aptasensors for CEA have been developed with LODs in the pg/mL range (He et al., 2023).
- Bio-functionalized carbon dots used as electrochemical signal probes for CEA detection achieved LOD of **0.54 pg/mL** (2024).

**Optical detection:**
- Fluorescent biosensors using mesoporous silica nanocontainers and quantum dots have demonstrated visual detection of CEA.

**Clinical utility:** Treatment monitoring and recurrence detection (primarily via serum; urinary CEA detection is experimental).

### 2.4 VEGF (Vascular Endothelial Growth Factor)

**Electrochemical detection:**
- Porous gold electrode-based EIS immunosensor using anti-VEGF VHH (nanobody) antibodies achieved LOD of **0.05 pg/mL** with a linear range of 0.1 pg/mL–0.1 µg/mL (Yarjoo et al., 2024).

**Clinical utility:** Prognostic marker; primarily research-stage for urinary detection.

### 2.5 Cytokeratin Fragment 19 (CYFRA 21-1)

CYFRA 21-1 is elevated in serum of lung cancer patients and detectable in urine.

**Fluorescent detection:**
- Carbon quantum dot/zinc oxide nanocomposite-based fluorescent immunosensor: LOD of **0.008 ng/mL** (Alarfaj et al., 2020).

**Clinical utility:** Screening/diagnosis for lung cancer (experimental for urine).

### 2.6 CA72-4

**Electrochemical detection:**
- MnO2 nanosheet/HNM-AuPtPd nanocomposite-based immunosensor: LOD of **1.78 × 10⁻⁵ U/mL** via amperometry (Yan et al., 2024).

**Clinical utility:** Diagnosis of gastric cancer (primarily serum).

### 2.7 Glypican-3 (GPC3)

**Electrochemical detection:**
- H-rGO-Pd NPs nanozyme with silver deposition strategy: LOD of **3.30 ng/mL** via DPV (Li et al., 2023).

**Clinical utility:** Hepatocellular carcinoma diagnosis.

## 3. Nucleic Acid Biomarkers

### 3.1 MicroRNA-21 (miR-21)

miR-21 is one of the most frequently overexpressed oncomiRs, implicated in prostate, bladder, breast, and colorectal cancers. Urinary miR-21 has been detected by multiple biosensor platforms.

**Electrochemical detection:**
- MOF@Pt@MOF nanozyme with cascade primer exchange reaction: LOD of **0.29 fM** (Li et al., 2020).
- Carboxylated graphene oxide/AuPt NPs on FTO: LOD of **1 fM** via DPV (Bharti et al., 2019).
- PCA-functionalized rGO probe: LOD of **5.4 fM** in 30 min (Zouari et al., 2020).
- AuNPs/GQDs/GO composite for simultaneous detection of miR-21, miR-155, and miR-210: LODs of **0.04 fM, 0.33 fM, and 0.28 fM** respectively via SWV (Pothipor et al., 2021).

**Optical detection:**
- Silver nanoparticle (AgNP)-based colorimetric sensor for urinary miR-21 in prostate cancer: demonstrated concentration-dependent color changes, with clinical validation in patient urine samples (Biosensors, 2024).

**Clinical utility:** Screening/diagnosis (multi-cancer); treatment monitoring (emerging).

### 3.2 MicroRNA-155

miR-155 is overexpressed in breast, lung, and hematological malignancies.

**Electrochemical detection:**
- Simultaneous detection with miR-21 and miR-210 (see above): LOD of **0.33 fM** via SWV.

**Fluorescent detection:**
- Silver nanocluster-based platform with entropy-driven amplification: LOD of **8.7 pM** (Li et al., 2021).

**Clinical utility:** Diagnosis (breast cancer, lymphoma).

### 3.3 MicroRNA-210

miR-210 is a hypoxia-responsive miRNA elevated in renal cell carcinoma and other cancers.

**Electrochemical detection:**
- Co-detected with miR-21 and miR-155: LOD of **0.28 fM** (Pothipor et al., 2021).

**Clinical utility:** Diagnosis (renal cell carcinoma).

### 3.4 MicroRNA-141

miR-141 is part of the miR-200 family, overexpressed in prostate and ovarian cancers.

**Fluorescent detection:**
- Silver nanocluster platform: LOD of **6.1 pM** (Li et al., 2021).

**Clinical utility:** Diagnosis and prognosis (prostate cancer).

### 3.5 MicroRNA let-7a

**Electrochemical detection:**
- MnO2 nanosheet-based nanozyme: LOD of **0.25 nM** (Wu et al., 2021).
- MOF-based dual marker detection with miR-21: LOD of **3.6 fM** (Chang et al., 2019).

**LSPR-enhanced optical detection:**
- Ag@Au nanostructure ECL biosensor: LOD of **5.45 aM** (Meng et al., 2025).

**Clinical utility:** Diagnosis (various cancers, tumor suppressor miRNA).

### 3.6 PCA3 (Prostate Cancer Antigen 3, lncRNA)

PCA3 is a long non-coding RNA highly specific for prostate cancer, already FDA-approved as the Progensa PCA3 assay.

**Electrochemical detection:**
- ZnO/CuO/Au nanocomposite-based sensor: LOD of **1.37 fM (CV)** and **1.41 fM (EIS)** with linear range 100 nM–100 fM and hybridization time of 1 minute (Scientific Reports, 2025).

**Clinical utility:** Screening/diagnosis for prostate cancer (FDA-approved as RNA assay; biosensor format is experimental).

### 3.7 Cell-Free DNA / ctDNA in Urine

Urinary cell-free DNA (cfDNA) and circulating tumor DNA (ctDNA) are increasingly studied for bladder cancer management.

- A 2025 systematic review confirmed that urinary tumor DNA-based liquid biopsy shows promise for bladder cancer diagnosis, surveillance, and treatment response monitoring.
- Biosensor-based detection platforms for urinary ctDNA include electrochemical methods using carbon fiber multi-electrode arrays for nucleic acid hybridization detection.

**Clinical utility:** Diagnosis, surveillance, and recurrence detection for bladder cancer; treatment monitoring.

### 3.8 TMPRSS2:ERG Fusion Transcripts

TMPRSS2:ERG gene fusions detectable in urine are specific for prostate cancer.

**Electrochemical detection:**
- High-speed biosensing using alternating current electrohydrodynamic nanomixing: amplification-free detection of multiple fusion transcripts in urine (Koo et al., 2017, 2018).

**Clinical utility:** Diagnosis and risk stratification (prostate cancer).

## 4. Extracellular Vesicles (Exosomes)

### 4.1 Overview

Urinary exosomes (30–150 nm vesicles) carry tumor-derived proteins, nucleic acids, and lipids. They are particularly abundant in urine for prostate and bladder cancers. Key surface markers include CD63, CD9, CD81, EpCAM, and PSMA.

### 4.2 CD63 Detection

**SERS-based detection:**
- MoS2-Au nanostar aptasensor with ROX-labeled aptamers: LOD of **17 particles/μL** for gastric cancer exosomes (Pan et al., 2022).

**Electrochemical detection:**
- DNA nanomachine-based separation-free EIS sensor for clinical exosome detection (Zeng et al., 2024).
- Hybridized chain reaction-amplified alkaline phosphatase-induced Ag-shell SERS immunoassay for exosomes (Cun et al., 2023).

### 4.3 Exosomal Proteins (General)

**Fluorescent detection:**
- Carbon nitride nanosheet nanozyme array with aptamer-based fluorescence: LOD of **2.5 × 10³ exosomes/mL** (Liu et al., 2021).

**Electrochemical biosensor advances (2025 review):**
- Chen et al. (Frontiers in Chemistry, 2025) comprehensively reviewed electrochemical biosensors for tumor-derived exosome detection, covering aptamer-based, antibody-based, and molecularly imprinted polymer approaches. EIS and DPV are the dominant techniques, with LODs reaching **10²–10⁴ particles/mL** in optimized systems.

### 4.4 Urinary Exosomal miRNAs

**Biosensor platform:**
- A highly sensitive urinary exosomal miRNA biosensor was developed for prostate cancer progression evaluation, detecting exosomal miR-21 and miR-141 in patient urine samples (Bioengineering, 2022).

**Optical nanobiosensors for exosome monitoring (2024 review):**
- A comprehensive review in Cancer Cell International (2024) surveyed optical nanobiosensors (fluorescence, SERS, SPR, colorimetric) for cancer-derived exosome detection, with an emphasis on sensitivity enhancement through nanomaterial functionalization.

### 4.5 SERS-Based Multiplex EV Biomarker Detection

**Recent advances (2025 review):**
- Duffield et al. (Nanoscale, 2025) reviewed SERS assays for multiplex EV biomarker detection in cancer diagnosis, covering simultaneous profiling of multiple surface proteins (CD63, CD9, EpCAM) using SERS nanotags.

### 4.6 Clinical Challenges

- Urinary EV isolation requires ultracentrifugation, size-exclusion chromatography, or immunoaffinity capture—adding pre-analytical complexity.
- Uromodulin (Tamm-Horsfall protein) co-precipitates with EVs from urine, introducing potential interference.
- Standardization of EV isolation and quantification protocols remains a major barrier to clinical adoption.

**Clinical utility:** Screening/diagnosis (prostate, bladder cancer); treatment monitoring (emerging); recurrence detection (research stage).

## 5. Metabolite Biomarkers

### 5.1 8-Hydroxy-2'-deoxyguanosine (8-OHdG)

8-OHdG is a marker of oxidative DNA damage elevated in urine of patients with various cancers (bladder, prostate, breast, gastric).

**Electrochemical detection:**
- A comprehensive review by Microchimica Acta (2021) surveyed nanostructured material-based electrochemical sensors for 8-oxoguanine and 8-OHdG, reporting LODs in the **nanomolar to sub-nanomolar range** using graphene, carbon nanotubes, and metal nanoparticle-modified electrodes.
- Exonuclease-mediated functional nucleic acid-based electrochemical analysis achieved enhanced sensitivity for 8-OHdG detection (Talanta, 2019).

**HPLC-ECD (electrochemical detection):**
- HPLC with electrochemical detection remains the gold-standard analytical method for 8-OHdG quantification in urine, achieving LODs in the **low nM range** (Molecules, 2022 review).

**Clinical utility:** Screening and risk assessment (oxidative stress across multiple cancers); treatment monitoring (assessment of oxidative damage response to therapy).

### 5.2 Spermine / Spermidine / Polyamines

Polyamines are essential for cell growth and are elevated in urine of prostate and other cancer patients.

- Spermine is highly expressed in the prostate and detectable in urine, expressed prostatic secretions, and tissue. Its clinical role in prostate cancer is emerging (IJMS, 2021, 2022 reviews).
- Diacetylated polyamine derivatives (N1,N12-diacetylspermine) in urine serve as markers for colorectal, breast, and other cancers.

**Electrochemical detection:**
- Currently, most polyamine quantification in urine relies on HPLC or LC-MS/MS rather than biosensors. Dedicated electrochemical biosensors for urinary polyamines in cancer contexts are sparse.

**Clinical utility:** Screening/diagnosis (prostate, colorectal cancers); clinical evidence is accumulating.

### 5.3 Sarcosine

Sarcosine (N-methylglycine) was identified as a potential prostate cancer metabolite by Sreekumar et al. (Nature, 2009), though subsequent validation has been mixed.

**Electrochemical detection:**
- Amperometric biosensor based on cross-coupled chemical and electrochemical reactions: LOD of **~0.1 µM** (Li et al., 2019).

**Clinical utility:** Prostate cancer diagnosis (controversial; not widely adopted).

### 5.4 Volatile Organic Compounds (VOCs)

Urinary VOCs represent a metabolic fingerprint that can distinguish cancer patients from healthy controls.

**Optical/sensor detection:**
- E-nose platforms, gas chromatography coupled with sensor arrays, and SERS-based VOC detection have been reported for prostate, bladder, and pancreatic cancer.
- A urinary VOC biosensor platform (Scientific Reports, 2024) demonstrated cancer detection using targeted VOC analysis.

**Clinical utility:** Screening (various urological cancers); primarily research-stage.

### 5.5 Pteridines (Neopterin, Biopterin)

Urinary pteridines are elevated in various cancers and can be detected by fluorescence due to their intrinsic fluorescent properties.

**Optical detection:**
- Fluorescence-based detection of neopterin/biopterin in urine is straightforward due to their native fluorescence. Detection has been demonstrated in capillary electrophoresis and microfluidic platforms.

**Clinical utility:** Screening/diagnosis (limited clinical adoption; primarily research).

## 6. Technology Comparison: Optical vs. Electrochemical Platforms

| Feature | Electrochemical | Optical |
|---------|----------------|---------|
| **Typical LOD range** | fM–pM (nucleic acids); pg/mL (proteins) | pM–nM (fluorescence); aM possible (LSPR-enhanced ECL) |
| **Sensitivity** | Very high (nanomaterial-enhanced) | Very high (SERS, ECL) |
| **Selectivity** | Antibody/aptamer dependent | Antibody/aptamer dependent |
| **Multiplexing** | Limited (dual/triple markers demonstrated) | Strong (SERS nanotags, multi-wavelength FL) |
| **POCT readiness** | High (miniaturizable, low-cost electrodes) | Moderate (requires optical reader) |
| **Sample processing** | Minimal for some formats | Minimal for SERS; moderate for fluorescence |
| **Cost** | Low fabrication cost | Variable (SERS substrates expensive) |
| **Stability** | Moderate (electrode fouling in urine matrix) | Moderate (photobleaching, signal drift) |
| **Speed** | 10–60 min | 15–90 min |
| **Clinical validation** | Small-sample stage for most | Small-sample stage for most |
| **Key challenge** | Matrix interference from urine components | Background fluorescence from urine |

**Key insight:** Electrochemical sensors have advantages in POCT miniaturization and cost, while optical sensors (especially SERS) excel at multiplexed analysis and label-free detection. Both face the shared challenge of urine matrix interference—high salt, pH variability, and abundant interfering proteins (e.g., uromodulin).

## 7. Comparative Biomarker Table

| Biomarker | Type | Cancer | Detection Method | LOD | Clinical Utility | Ref. |
|-----------|------|--------|-------------------|-----|-----------------|------|
| PSA | Protein | Prostate | Electrochemical (DPV, EIS) | 0.01–1 pg/mL | Screening/Diagnosis | Dowlatshahi 2021; Traynor 2020 |
| PSA | Protein | Prostate | Optical (SPR, aptasensor) | 0.1 pg/mL–ng/mL | Screening/Diagnosis | Jolly 2019 |
| NMP22 | Protein | Bladder | Fluorescent immunosensor (QDs) | 0.05 pg/mL | Screening/Surveillance | Othman 2020 |
| CEA | Protein | Colorectal, various | Electrochemical (DPV) | 0.23 pg/mL | Monitoring/Recurrence | Chen 2019 |
| VEGF | Protein | Various | Electrochemical (EIS, VHH nanobody) | 0.05 pg/mL | Prognosis | Yarjoo 2024 |
| CYFRA 21-1 | Protein | Lung | Fluorescence (CQD/ZnO) | 0.008 ng/mL | Diagnosis | Alarfaj 2020 |
| CA72-4 | Protein | Gastric | Electrochemical (amperometry) | 1.78 × 10⁻⁵ U/mL | Diagnosis | Yan 2024 |
| GPC3 | Protein | Liver (HCC) | Electrochemical (DPV) | 3.30 ng/mL | Diagnosis | Li 2023 |
| miR-21 | miRNA | Prostate, bladder, breast | Electrochemical (DPV/SWV) | 0.04–5.4 fM | Diagnosis/Monitoring | Pothipor 2021; Zouari 2020 |
| miR-21 | miRNA | Prostate | Optical (AgNP colorimetric) | qualitative | Diagnosis | Biosensors 2024 |
| miR-155 | miRNA | Breast, lymphoma | Electrochemical (SWV) | 0.33 fM | Diagnosis | Pothipor 2021 |
| miR-155 | miRNA | Breast | Fluorescence (Ag nanoclusters) | 8.7 pM | Diagnosis | Li 2021 |
| miR-210 | miRNA | Renal cell carcinoma | Electrochemical (SWV) | 0.28 fM | Diagnosis | Pothipor 2021 |
| miR-141 | miRNA | Prostate, ovarian | Fluorescence (Ag nanoclusters) | 6.1 pM | Diagnosis/Prognosis | Li 2021 |
| miR-let-7a | miRNA | Various (tumor suppressor) | LSPR-enhanced ECL | 5.45 aM | Diagnosis | Meng 2025 |
| miR-let-7a | miRNA | Various | Electrochemical (DPV, MOF) | 3.6 fM | Diagnosis | Chang 2019 |
| PCA3 | lncRNA | Prostate | Electrochemical (CV/EIS) | 1.37/1.41 fM | Screening/Diagnosis | Sci. Rep. 2025 |
| ctDNA | cfDNA | Bladder | Electrochemical (various) | varies | Diagnosis/Surveillance/Recurrence | 2025 systematic review |
| TMPRSS2:ERG | Fusion RNA | Prostate | Electrochemical (nanomixing) | amplification-free | Diagnosis/Risk stratification | Koo 2017, 2018 |
| CD63 (exosomes) | EV marker | Gastric | SERS (MoS2-Au aptasensor) | 17 particles/μL | Diagnosis | Pan 2022 |
| Exosomal proteins | EV | Various | Fluorescence (nanozyme) | 2.5 × 10³/mL | Diagnosis | Liu 2021 |
| Exosomal miRNAs | EV cargo | Prostate | Electrochemical biosensor | validated in patient urine | Monitoring/Prognosis | Bioengineering 2022 |
| 8-OHdG | Metabolite | Various (oxidative stress) | Electrochemical (DPV) | nM range | Screening/Risk assessment | Microchim. Acta 2021 review |
| 8-OHdG | Metabolite | Various | HPLC-ECD | low nM | Screening/Monitoring | Molecules 2022 |
| Sarcosine | Metabolite | Prostate | Amperometric biosensor | ~0.1 µM | Diagnosis (controversial) | Li 2019 |
| Spermine | Metabolite | Prostate | LC-MS/MS (no dedicated biosensor) | — | Diagnosis (emerging) | IJMS 2021, 2022 |
| VOCs | Metabolite | Various urological | Sensor arrays, SERS | qualitative | Screening | Sci. Rep. 2024 |
| Urine SERS profile | Metabolic fingerprint | RCC, bladder | Label-free SERS + ML | qualitative | Diagnosis | IJMS 2024; Nanoscale 2025 |

## 8. Clinical Utility Mapping

| Clinical Stage | Biomarkers | Evidence Level |
|---------------|-----------|----------------|
| **Screening / Initial Diagnosis** | PSA, NMP22 (FDA-approved for bladder), PCA3 (FDA-approved for prostate), miR-21, miR-210, CYFRA 21-1, CD63 exosomes, 8-OHdG, urinary SERS fingerprinting | Strong for NMP22, PCA3; moderate for others |
| **Treatment Monitoring (Pharmacodynamics)** | CEA, ctDNA, exosomal miRNAs, 8-OHdG | Moderate; clinical validation ongoing |
| **Minimal Residual Disease / Recurrence Detection** | NMP22, ctDNA (bladder cancer), TMPRSS2:ERG (prostate), exosomal AR-V7 (prostate, castration resistance) | Moderate for ctDNA-bladder; emerging for others |

## 9. Clinical Readiness and Translation Challenges

Despite remarkable analytical performance in laboratory settings, clinical translation of biosensor-based urinary cancer biomarker detection faces several key challenges:

1. **Urine matrix variability:** pH (4.5–8), osmolality, and interfering biomolecules (uromodulin, albumin, creatinine) vary significantly between patients and even between collections from the same patient.

2. **Pre-analytical standardization:** First-void vs. midstream vs. 24-hour urine; time from collection to processing; centrifugation and filtration protocols all affect biomarker recovery.

3. **Regulatory pathway:** Only NMP22 (BladderChek) and PCA3 (Progensa) have FDA approval among urinary cancer biomarkers. Biosensor-format detection has not yet received regulatory clearance for any cancer biomarker.

4. **Clinical trial status:** According to clinical trial registries (as compiled by Wang et al., 2025), electrochemical impedance-based sensors (NCT03929185, NCT04825002, ChiCTR2200058608) and fluorescence/SERS optical sensors (NCT06772376, NCT02957370) are in early-stage clinical trials for various cancers. None have completed Phase III trials.

5. **Reproducibility:** Batch-to-batch variability in nanomaterial synthesis affects sensor performance. Large-scale manufacturing with consistent quality control is needed.

6. **Multiplexing needs:** Single-biomarker tests lack the sensitivity and specificity needed for clinical decision-making. Multi-biomarker panels (e.g., combining PSA + PCA3 + TMPRSS2:ERG + exosomal markers) are likely required for adequate clinical performance.

## 10. Open Questions

1. **Urine processing standardization:** No consensus exists on optimal urine preparation for biosensor-based detection. Direct urine analysis would be ideal for POCT but is challenging due to matrix effects.

2. **LOD vs. clinical relevance:** Many reported LODs are orders of magnitude below clinically relevant concentrations. Whether ultra-low LODs translate to improved clinical sensitivity is unclear.

3. **Metabolite biosensors:** Dedicated electrochemical or optical biosensors for urinary metabolites (spermine, pteridines) in cancer are under-developed relative to protein and nucleic acid biomarkers.

4. **EV isolation dependency:** Most exosome biosensors require upstream EV isolation, adding cost and time. Direct-from-urine EV detection platforms are emerging but not yet robust.

5. **Head-to-head comparisons:** Very few studies directly compare optical and electrochemical approaches for the same biomarker in the same urine cohort. Technology selection is currently based on analytical rather than clinical performance data.

6. **Long-term monitoring:** The potential of repeated urinary biosensor testing for longitudinal cancer monitoring (recurrence detection, treatment response) is largely unexplored in clinical settings.

## Sources

1. Wang X, Hei J, Zhao T, Liu X, Huang Y. "Nanomaterial-Mediated Electrochemical and Optical Biosensors and Their Application in Tumour Marker Detection." *Sensors* 2025;25(18):5902. DOI: 10.3390/s25185902
2. López Mujica MEJ, Ferapontova EE. "Electrochemical Biosensors for Cancer Diagnosis and Prognosis Using Protein Biomarkers." *Sensors* 2026;26(4):1139. DOI: 10.3390/s26041139
3. Dowlatshahi S, Abdekhodaie MJ. "Electrochemical prostate-specific antigen biosensors based on electroconductive nanomaterials and polymers." *Clinica Chimica Acta* 2021;516:111-135. DOI: 10.1016/S0009-8981(21)00034-6
4. Traynor SM et al. "Recent Advances in Electrochemical Detection of Prostate Specific Antigen (PSA) in Clinically-Relevant Samples." *J. Electrochem. Soc.* 2020;167:037551. DOI: 10.1149/1945-7111/ab69fd
5. Prostate cancer detection: a systematic review of urinary biosensors. *Prostate Cancer Prostatic Dis.* 2022;25:39-46. DOI: 10.1038/s41391-021-00480-8
6. Othman HO et al. "A highly sensitive fluorescent immunosensor for NMP22." *RSC Advances* 2020;10:38316. DOI: 10.1039/d0ra06191c
7. Electrochemical protein biosensors for disease marker detection. *Microsystems & Nanoengineering* 2024;10:65. DOI: 10.1038/s41378-024-00700-w
8. Chen J, Zhao Z et al. "Advances in electrochemical biosensors for the detection of tumor-derived exosomes." *Front. Chem.* 2025;13:1556595. DOI: 10.3389/fchem.2025.1556595
9. "Increasing the sensitivity and accuracy of detecting exosomes as biomarkers for cancer monitoring using optical nanobiosensors." *Cancer Cell Int.* 2024;24:189. DOI: 10.1186/s12935-024-03379-1
10. Duffield C et al. "Recent advances in SERS assays for detection of multiple extracellular vesicles biomarkers for cancer diagnosis." *Nanoscale* 2025;17:3635-3655. DOI: 10.1039/D4NR04014G
11. SERS biosensors for liquid biopsy towards cancer diagnosis. *Nano Convergence* 2024;11:22. DOI: 10.1186/s40580-024-00428-3
12. "Nanostructured material-based electrochemical sensing of 8-oxoguanine and 8-OHdG." *Microchimica Acta* 2021;188:58. DOI: 10.1007/s00604-020-04689-7
13. "The Emerging Clinical Role of Spermine in Prostate Cancer." *IJMS* 2021;22:4382. DOI: 10.3390/ijms22094382
14. Scientific Reports. "Affordable ultrasensitive electrochemical detection of PCA3." 2025. DOI: 10.1038/s41598-025-04852-1
15. Wan X et al. "Unleashing the power of urine-based biomarkers in diagnosis, prognosis and monitoring of bladder cancer." *Int. J. Oncol.* 2025;66:18. DOI: 10.3892/ijo.2025.5724
16. "Urinary Biomarkers in Bladder Cancer: FDA-Approved Tests and Emerging Tools." *Cancers* 2025;17(21):3425. DOI: 10.3390/cancers17213425
17. Kim H et al. "Noninvasive precision screening of prostate cancer by urinary multimarker sensor and AI." *ACS Nano* 2021;15:4054-4065. DOI: 10.1021/acsnano.0c06946
18. Phyo JB et al. "Label-free SERS analysis of urine using 3D-stacked AgNW sensor." *Anal. Chem.* 2021;93:3778-3785. DOI: 10.1021/acs.analchem.0c04200
19. "Urinary MicroRNA-21 for Prostate Cancer Detection Using AgNP Sensor." *Biosensors* 2024;14(12):599. DOI: 10.3390/bios14120599
20. "Label-Free SERS of Urine Components for Discriminating RCC." *IJMS* 2024;25(7):3891. DOI: 10.3390/ijms25073891
21. Lu Y et al. "Non-invasive diagnosis of low-grade bladder cancer via SERSomes of urine." *Nanoscale* 2025;17(12). DOI: 10.1039/d4nr05306k
22. Pan H et al. "Sensing gastric cancer exosomes with MoS2-based SERS aptasensor." *Biosens. Bioelectron.* 2022;215:114553. DOI: 10.1016/j.bios.2022.114553
23. Pothipor C et al. "Electrochemical biosensor for simultaneous detection of breast cancer miRNAs." *Analyst* 2021;146:4000. DOI: 10.1039/D1AN00436K
24. Chang J et al. "MOF-Based Electrochemical Biosensor for Simultaneous Detection of Multiple Tumor Biomarkers." *Anal. Chem.* 2019;91:3604. DOI: 10.1021/acs.analchem.8b05599
25. Jolly P et al. "Application of optical and electrochemical aptasensors for PSA." *Biosens. Bioelectron.* 2019;142:111484. DOI: 10.1016/j.bios.2019.111484
