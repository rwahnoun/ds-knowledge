---
title: Vault Index
aliases: [index, home]
tags: [type/index, status/living]
date: 2026-04-26
status: living
type: index
author: claude
---

# Vault Index

Navigation hub for the ds-knowledge vault. Auto-generated — see [[updateIndex]] for regeneration instructions.

## biomarkers

- [[biomarkers/biomarker-panel|Urine Biomarker Panel — Jimini Reference]] — Reagent-free detection reference for the Jimini panel with LED-to-biomarker mapping and EIS support
- [[biomarkers/feasibility-analysis|Feasibility Analysis — Reagent-Free Multi-Modal Spectrophotometric Urinalysis]] — Comprehensive feasibility assessment for 20 key biomarkers across spectroscopy and electrochemical methods
- [[biomarkers/literature|Literature — LED Spectroscopy & EIS for Urine Biomarker Prediction]] — Consolidated paper reference for LED-based spectroscopy and EIS (60+ sources)
- [[biomarkers/optical-signatures|Urine Biomarker Optical Signatures — Reference Tables]] — Single reference for absorbance, fluorescence, and scattering properties across 275–1078 nm
- [[biomarkers/pre-analytics|Urine Sample Pre-Analytics & Stability]] — Pre-analytical requirements, analyte-by-analyte stability windows, and thermal management for Jimini
- [[biomarkers/signal-processing|Signal Processing & Matrix Correction for Jimini Urine Spectroscopy]] — Beer-Lambert pipeline: preprocessing, turbidity/dilution/color corrections, cross-device calibration

### oncology
- [[biomarkers/oncology/instructions|Objective]] — Objective for generating a systematic review of urinary tumor biomarkers via optical and electrochemical methods
- [[biomarkers/oncology/journal-article|Urinary Tumor Biomarkers Detectable by Optical and Electrochemical Methods — A Systematic Review]] — Systematic review mapping 25+ biomarker–assay combinations across proteins, nucleic acids, exosomes, and metabolites
- [[biomarkers/oncology/urinary-tumor-biomarkers-review|Systematic Review: Urinary Tumor Biomarkers]] — Review consolidating four biomarker classes with Jimini device compatibility assessment
- [[biomarkers/oncology/urinary-tumor-biomarkers-review.provenance|Provenance: Urinary Tumor Biomarkers Review]] — Search strategy and source documentation for the oncology systematic review

### singleBiomarkers
- [[compendium|Urinary Biomarkers Compendium]] — Cross-analyte synthesis of 31 single-biomarker reviews (identity, physiology, detection modalities, sensitivity)
- [[biomarkers/papers/singleBiomarkers/instructions|Generation of Biomarker Sheets]] — Template and guidelines for creating standardized biomarker reference sheets

### singleBiomarkers/sheets/contaminants
- [[chlorotalonil|Chlorotalonil]] — Fungicide as environmental urinary contaminant
- [[metolachlore|Metolachlore]] — Herbicide as environmental urinary contaminant
- [[pfas|PFAS (Per- and Polyfluoroalkyl Substances)]] — Fluorinated contaminants with environmental and bioaccumulation implications

### singleBiomarkers/sheets/fluorophores
- [[fad|FAD (Flavin Adenine Dinucleotide)]] — Fluorescent coenzyme (Ex 450/Em 525 nm) for metabolic redox state monitoring
- [[nadh|NADH]] — Intrinsically fluorescent electron carrier (Ex 340/Em 460 nm) as metabolic activity marker
- [[riboflavin|Riboflavin (Vitamin B2)]] — Fluorescent vitamin (Ex 365–455/Em 520 nm) for nutritional status
- [[tryptophan|Tryptophan]] — Intrinsic protein fluorophore (Ex 280/Em 340 nm) with cancer associations

### singleBiomarkers/sheets/infection-inflammation
- [[bacteria|Bacteria]] — Bacteriuria detection via turbidity, MALS, and nucleic acid methods
- [[haemoglobin|Haemoglobin]] — Oxygen-transport protein detected in hematuria via Soret and Q-band absorbance
- [[leukocytes|Leukocytes]] — Pyuria detection via scatter, enzyme activity, and nucleic acid methods
- [[nitrites|Nitrites]] — Bacterial metabolite indicating UTI; colorimetry and electrochemistry
- [[red-blood-cells|Red Blood Cells]] — Hematuria detection via scatter and hemoglobin absorbance
- [[white-blood-cells|White Blood Cells]] — Leukocyturia/pyuria reference sheet

### singleBiomarkers/sheets/metabolites
- [[chloride|Chloride]] — Major urinary anion (55–200 mmol/day); ion-selective electrodes and conductivity
- [[citrate|Citrate]] — Stone-formation inhibitor; Raman and titration methods
- [[copper|Copper]] — Trace metal (5–50 µg/day) for Wilson disease screening
- [[creatinin|Creatinine]] — GFR marker and spot-urine normalization factor; Jaffe, enzymatic, NIR
- [[glucose|Glucose]] — Detected via enzyme strip chemistry and EIS when >140 mg/dL
- [[magnesium|Magnesium]] — Divalent cation (40–120 mmol/day); atomic absorption and ISE
- [[oxalate|Oxalate]] — Stone-forming anion (10–60 mg/day); chromatography and Raman
- [[phosphate|Phosphate]] — Electrolyte (20–40 mmol/day); molybdate colorimetry and electrochemistry
- [[sodium|Sodium]] — Major urinary cation (50–250 mmol/day) reflecting dietary intake
- [[urea|Urea]] — Nitrogen waste (300–500 mmol/day); enzymatic, NIR, SERS methods
- [[uric-acid|Uric Acid]] — Purine catabolite with UV chromophore (λmax 293 nm)

### singleBiomarkers/sheets/physico-chemical
- [[ketone|Ketone]] — Ketosis/starvation indicator; nitroprusside dipstick
- [[osmolality|Osmolality]] — Total solute concentration; refractometry, EIS conductivity, NIR water bands
- [[ph|pH]] — Acidity (4.5–8.0 range); glass electrode and indicator dyes
- [[usg|Urine Specific Gravity (USG)]] — Density-based hydration marker; refractometry and conductivity

### singleBiomarkers/sheets/pigments-porphyrins
- [[bilirubin|Bilirubin]] — Orange bile pigment with strong UV-Vis absorbance (454 nm); photosensitive
- [[porphobilinogen|Porphobilinogen]] — Porphyrin precursor; diagnostic for acute porphyria
- [[total-urinary-porphyrin|Total Urinary Porphyrin (TUP)]] — Soret-absorbing (407 nm) red-fluorescent (620 nm) heme precursor

## datascience

- [[datascience/calibration-transfer|Calibration Transfer & Device Harmonization for Portable Spectrometers]] — Cross-device spectral harmonization (DS, PDS, CORAL, MVG augmentation) without paired samples
- [[datascience/libraries|Python Libraries for UV-Vis Spectrophotometry in Biomarker Estimation]] (in-progress) — Reference guide to scipy, scikit-learn, pybaselines, spectral, and related libraries
- [[datascience/matrix-correction|Matrix Correction for Urine Variability in Spectroscopic Measurements]] — Layered pipeline: turbidity, dilution, color, fluorescence background, inner-filter effects, pH normalization
- [[datascience/ml-models|ML Models for Jimini Urine Spectroscopy]] — Model selection (PLS, 1D-CNN, PARAFAC), augmentation (WGAN, diffusion), validation by dataset size
- [[datascience/multi-task-modeling|Multi-Task & Multi-Output Prediction for Spectroscopic Biomarker Analysis]] — MTL architectures and loss functions for the 16-target biomarker panel
- [[datascience/normalization|Signal Normalization in Photospectroscopy]] — SNV, MSC, EMSC, Savitzky-Golay derivatives, cross-device transfer
- [[datascience/physics-grounded-ml|Physics-Grounded Machine Learning for Spectral Analysis]] — Six approach categories with Beer-Lambert grounding and classical chemometrics
- [[datascience/signal-processing|Signal Processing & Chemometrics for Spectral Urine Analysis]] — Full preprocessing pipeline for 275–1078 nm LED spectrophotometry
- [[datascience/spectroscopy-biomarkers|Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices]] — Synthesis of UV-Vis, NIR, fluorescence, and EIS for urine biomarkers
- [[datascience/turbidity|Turbidity Estimation in Urine Spectrophotometry]] — Single-wavelength turbidimetry (660 nm), CIE L*a*b* classification, Formazin calibration

## meta

- [[meta/tplMarkdown|Obsidian File Template & Conventions]] — Instructions for writing or editing notes in this vault
- [[meta/tplModule|Module Documentation Template]] — Template for documenting Python modules with index and reference sections

## QARA

- [[QARA/api-architecture|Datascience Architecture & API]] — Reference for ds code repositories, validation protocols, computing platform, and algorithm API
- [[QARA/database|Datascience ETL and Database (PostgreSQL)]] — DS-DB pipeline normalizing Jimini records and biomarkers into PostgreSQL
- [[QARA/device|Jimini Device Description]] — Pen-like device, signal naming convention (SLC), component specs, data model
- [[QARA/overview|Datascience Overview — ds-learn]] — ML models, training repository, data model, processing pipeline
- [[QARA/regulatory-ivd|Regulatory Pathway for Spectroscopic IVD Devices]] — Regulatory landscape: IVDR classification, FDA 510(k), CLIA, SaMD requirements

## spectrophotometry hardware

- [[spectrophotometry hardware/optical-path-design|Optical Path Design for Pen-Form Spectrophotometry of Urine]] — Path length, geometry, cuvette materials, UV-C, stray light, multi-angle strategies

### iris-IQ200 precision
- [[spectrophotometry hardware/iris-IQ200 precision/iQ200_precision_summary|Iris iQ200 Precision & Accuracy Summary]] — WBC/RBC/bacteria counting imprecision as comparator for Jimini detection thresholds

### leds-and-sensors
- [[spectrophotometry hardware/leds-and-sensors/leds|UV and Specific-Wavelength LEDs for Portable Spectrophotometry]] — Per-wavelength LED review (275/365/405/455 nm + white CRI>95 + 1070 nm NIR)
- [[spectrophotometry hardware/leds-and-sensors/overview|LEDs & Sensors — Component Overview]] — Summary tables and selection guidance; white LED deep-dive ranking
- [[spectrophotometry hardware/leds-and-sensors/sensors|Spectral Sensors for Portable Spectrophotometry]] — STM32-compatible sensor selection (C12/C14, AS7341/7343, AS7265x, EIS frontends)
- [[spectrophotometry hardware/leds-and-sensors/suppliers|Suppliers & Distributors for UV/Vis/NIR LEDs and Spectral Sensors]] — Distributor coverage, lead times, MOQ, BOM

## usense

- [[usense/branding|Usense Branding Assets & Workflow]] — Canonical PDF-generation workflow for Usense-branded deliverables via md2pdf
- [[usense/jiminiDevice|Jimini Device]] — Pen-like probe measuring urine biomarkers via optical, EIS, and SWV sensors

### code
- [[usense/code/conventions|Code Conventions — Usense Datascience Repos]] — Shared Python/ruff standards; camelCase, 3.11+, hatchling
- [[usense/code/projectDescription|ds-learn — Project Description & Data Model]] — ML training repo; Dataset–Record–Component hierarchy
- [[usense/code/workspace|Workspace Layout — datascience, ds-scripts, ds-learn]] — Three-repo workspace with shared venvs at `d:\code\venvs\`

### code/datascience
- [[usense/code/datascience/overview|datascience repo — Core ds Library]] — Loaders, ETL, signal processing, transformers, DB clients
- [[usense/code/datascience/metrics|ds.process.metrics — Signal & Record Quality Metrics]] — Per-component spectrum/impedance stats, time-series features (Hjorth, curve length, entropy), DataFrame resampling
- [[usense/code/datascience/prcPandas|ds.process.prcPandas — Low-Level Signal Processing]] — Functions on pandas Series/DataFrames: normalization, scatter correction, smoothing, baseline, peaks, EIS features
- [[usense/code/datascience/transformers|ds.process.transformers — Sklearn-Compatible Spectral Transformers]] — Pipeline-safe scikit-learn transformers wrapping the low-level functions

### code/ds-learn
- [[usense/code/ds-learn/overview|ds-learn repo — ML Models & Training]] (draft) — scikit-learn pipelines, joblib models, Azure ML deployment
- [[usense/code/ds-learn/explain|learn.explain — SHAP Model Explainability]] — SHAP for spectral data: wavelength importance, band extraction, per-sample explanations, publication plots

### code/ds-scripts
- [[usense/code/ds-scripts/overview|ds-scripts repo — Analysis Notebooks & Studies]] — Numbered studies (dsNNN), biomarker projects

## Sources

| Source | Note |
|---|---|
| Vault filesystem scan | Generated 2026-04-26 by `updateIndex.md` workflow with 8 parallel `Explore` agents |

## Gaps

- `biomarkers/papers/` holds PDF attachments referenced by sibling notes (no `.md` content).
- `biomarkers/singleBiomarkers/.plans/urea.md` (draft plan) excluded as a dotfile-directory entry per `updateIndex.md` rules.
