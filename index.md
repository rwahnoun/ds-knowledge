# ds-knowledge index

Curated navigation hub for the Usense scientific and engineering vault. Every section, directory, and note has a one-line description and wikilink.

---

## biomarkers — urine biomarker science, optical detection, and compound reference sheets

- [[biomarker-panel]] — Reagent-free Jimini panel: LED-to-biomarker detection mapping
- [[feasibility-analysis]] — Feasibility of quantifying 20 urine biomarkers via UV-Vis/NIR/fluorescence/MALS
- [[jimini-signal-processing]] — Beer-Lambert pipeline, matrix corrections, cross-device calibration
- [[literature]] — Consolidated paper reference for LED spectroscopy and EIS biomarker prediction
- [[optical-signatures]] — Absorbance, fluorescence, and scattering properties, 275–1078 nm range
- [[pre-analytics]] — Urine sample handling, stability, and pre-analytical requirements

### compounds

- [[compendium]] — Cross-analyte synthesis of 31 single-biomarker literature reviews
- [[instructions]] — Prompt template for generating per-biomarker reference sheets

#### fluorophores

- [[fad]] — Flavin adenine dinucleotide; fluorescent metabolic coenzyme, oncology marker
- [[nadh]] — Reduced NAD; fluorescent pyridine coenzyme, metabolic and oncology marker
- [[riboflavin]] — Vitamin B2; strongly fluorescent nutritional biomarker
- [[tryptophan]] — Aromatic amino acid; UV-fluorescent oncology and nutrition marker

#### metabolites

- [[chloride]] — Major urinary electrolyte; kidney function and electrolyte balance
- [[citrate]] — Inhibitor of calcium stone formation; nephrolithiasis risk marker
- [[copper]] — Trace element elevated in Wilson's disease and copper overload
- [[creatinin]] — Muscle catabolism end-product; GFR proxy and normalization reference
- [[glucose]] — Glucosuria marker; diabetes screening and renal threshold assessment
- [[magnesium]] — Electrolyte with EIS detection; bone and electrolyte balance
- [[oxalate]] — Key lithogenic anion; primary hyperoxaluria and nephrolithiasis
- [[phosphate]] — Inorganic electrolyte; bone metabolism and electrolyte balance
- [[sodium]] — Primary urinary cation; hydration status and electrolyte balance
- [[urea]] — Nitrogen catabolism end-product; kidney function and dietary protein load
- [[uric-acid]] — Purine oxidation product; gout, nephrolithiasis, and tumor lysis

#### infection-inflammation

- [[bacteria]] — Bacteriuria detection via scattering, EIS, and fluorescence for UTI diagnosis
- [[haemoglobin]] — Heme protein in urine; haemoglobinuria and renal injury marker
- [[leukocytes]] — Leukocyte esterase activity; pyuria and UTI inflammation marker
- [[nitrites]] — Bacterial nitrate reduction product; UTI screening by UV/Vis
- [[red-blood-cells]] — Erythrocytes in urine; haematuria detection by scattering/Vis
- [[white-blood-cells]] — Leukocyturia; UTI and inflammation assessed by scattering/fluorescence/EIS

#### physico-chemical

- [[ketone]] — Ketone bodies (acetoacetate, BHB); ketonuria in diabetes and starvation
- [[osmolality]] — Total solute concentration; hydration and concentrating ability via NIR
- [[ph]] — Acid-base balance; nephrolithiasis risk stratification via Vis
- [[usg]] — Urine specific gravity; hydration proxy via NIR refractometry

#### pigments-porphyrins

- [[bilirubin]] — Conjugated bilirubin; hepatobiliary disease and liver function marker
- [[porphobilinogen]] — Pyrrole precursor elevated in acute porphyria attacks
- [[total-urinary-porphyrin]] — Porphyrin panel for porphyria diagnosis and lead toxicity screening

#### contaminants

- [[chlorotalonil]] — Chlorothalonil fungicide metabolite; agricultural exposure biomarker
- [[metolachlore]] — Metolachlor herbicide mercapturate; pesticide exposure marker
- [[pfas]] — Per- and polyfluoroalkyl substances; persistent environmental contaminants

### oncology

- [[journal-article]] — Systematic review of urinary tumor biomarkers formatted as journal article
- [[urinary-tumor-biomarkers-review]] — Systematic review mapping tumor biomarkers to Jimini detection feasibility

---

## datascience — ML, signal processing, and chemometrics for Jimini urine spectroscopy

- [[calibration-transfer]] — Cross-device model harmonization for Jimini LED spectrometers
- [[libraries]] — Python ecosystem reference for UV-Vis spectrophotometry and biomarker pipelines
- [[matrix-correction]] — Correcting urine matrix variability (turbidity, dilution, pH, IFE)
- [[ml-models]] — Model selection, augmentation, and validation for Jimini spectral data
- [[multi-task-modeling]] — Joint multi-output prediction for spectroscopic biomarker analysis
- [[normalization]] — Cross-sample and cross-device signal normalization methods
- [[physics-grounded-ml]] — Beer-Lambert and domain-knowledge-constrained ML for spectroscopy
- [[signal-processing]] — DSP and chemometrics preprocessing pipeline for urine spectra
- [[spectroscopy-biomarkers]] — Literature synthesis of reagentless urine biomarker prediction
- [[turbidity]] — Spectrophotometric turbidity estimation as biomarker confound and proxy

---

## QARA — datascience architecture, device, and regulatory reference notes

- [[api-architecture]] — Repos, API schema, algorithm versioning, and Azure deployment
- [[database]] — PostgreSQL ETL pipeline normalizing Jimini records and biomarkers
- [[device]] — Jimini hardware, sensor specs, and SLC naming conventions
- [[overview]] — ds-learn data model: Dataset, Record, Component, and transformers
- [[regulatory-ivd]] — EU IVDR / FDA 510(k) pathway and SaMD requirements for Jimini

---

## spectrophotometry hardware — Jimini optical system: LEDs, sensors, path design, suppliers

- [[optical-path-design]] — Path length, geometry, materials, and optical architecture for pen-form urine spectrophotometry

### iris-IQ200 precision

- [[iQ200_precision_summary]] — Iris iQ200 cell-count imprecision data; comparator for Jimini detection thresholds

### leds-and-sensors

- [[leds]] — Per-wavelength LED specs and sourcing for 275/365/405/455 nm, white, and 1070 nm
- [[overview]] — Master tables for all Jimini LEDs, sensors, and EIS frontends with selection guidance
- [[sensors]] — STM32-compatible spectral sensor and EIS IC selection for UV-Vis and NIR
- [[suppliers]] — Distributor coverage, pricing, and lead times for UV/Vis/NIR LEDs and spectral sensors

---

## usense — Usense Healthcare device, repos, branding, and code conventions

- [[branding]] — PDF generation and brand assets for Usense deliverables
- [[jiminiDevice]] — Jimini pen probe: sensors, emitters, SLCs, data model

### code

- [[conventions]] — camelCase naming, ruff, uv, docstring, and style rules
- [[projectDescription]] — Dataset/Record/Component hierarchy and transformer overview
- [[workspace]] — Three-repo layout, dependency graph, shared venvs

### code/datascience

- [[metrics]] — Per-component quality metrics and Hjorth time-series features
- [[overview]] — Core `ds` package: loaders, ETL, signal processing, DB clients
- [[prcPandas]] — Low-level signal processing: SNV, MSC, S-G, baseline, EIS features
- [[remoteClients]] — PostgreSQL and Google Drive clients; sheet-to-dataset pattern
- [[transformers]] — Sklearn-compatible spectral transformers and `mkPipeline`

### code/ds-learn

- [[explain]] — SHAP explainability: wavelength importance, bands, spectral plots
- [[overview]] — ML training repo: sklearn pipelines, joblib models, Azure deployment

### code/ds-scripts

- [[overview]] — Numbered analysis studies (`dsNNN`), project folders, notebook patterns
