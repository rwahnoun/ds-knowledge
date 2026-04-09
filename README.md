# ds-knowledge

Knowledge base for the Jimini urine biomarker device and the `datascience` / `ds-learn` / `ds-scripts` repositories.

## Structure

### [project/](project/) — Project & Device

| Doc | Description |
|-----|-------------|
| [overview.md](project/overview.md) | Project description, data model, Dataset/Record structures |
| [device.md](project/device.md) | Jimini device architecture, LED wavelengths, sensors, EIS |
| [database.md](project/database.md) | PostgreSQL schema (3 tables), ETL pipeline, Azure/MongoDB integration |
| [api-architecture.md](project/api-architecture.md) | Azure Functions API, QTP protocol, algorithm versioning |

### [biomarkers/](biomarkers/) — Biomarker Detection

| Doc | Description |
|-----|-------------|
| [summary.md](biomarkers/summary.md) | Quick reference table of 30+ urine biomarkers with detection wavelengths |
| [signatures.md](biomarkers/signatures.md) | Feasibility table: 26 biomarkers with spectrophotometric signatures |
| [signatures-deep-dive.md](biomarkers/signatures-deep-dive.md) | Deep-dive feasibility: high/moderate/high-risk categories, phased strategy |
| [optical-properties.md](biomarkers/optical-properties.md) | Absorbance/fluorescence wavelengths per analyte |

### [signal-processing/](signal-processing/) — DSP & Calibration

| Doc | Description |
|-----|-------------|
| [dsp-pipeline.md](signal-processing/dsp-pipeline.md) | Full 13-step UV-Vis extraction pipeline |
| [normalization.md](signal-processing/normalization.md) | Within-urine and cross-device normalization (SNV, MSC, CORAL) |
| [device-calibration.md](signal-processing/device-calibration.md) | Per-device calibration methods |
| [turbidity.md](signal-processing/turbidity.md) | Turbidity measurement: turbidimetry, CIE L*a*b*, multi-angle scatter |

### [hardware/](hardware/) — LEDs, Sensors & Optics

| Doc | Description |
|-----|-------------|
| [overview.md](hardware/overview.md) | Component survey for pen-sized spectrophotometer |
| [leds.md](hardware/leds.md) | LED specs: 275/365/405/455 nm, white broadband, 1070 nm NIR |
| [sensors.md](hardware/sensors.md) | Spectral sensor evaluation: AS7341, NIR, IR, EIS frontend ICs |
| [optical-path-design.md](hardware/optical-path-design.md) | Optical path design considerations |
| [suppliers.md](hardware/suppliers.md) | Sourcing and datasheet links |
| [datasheets/](hardware/datasheets/) | Component datasheets (PDFs) |

### [literature/](literature/) — Literature Reviews

| Doc | Topic |
|-----|-------|
| [urine-biomarkers-review.md](literature/urine-biomarkers-review.md) | Comprehensive 60+ source review: detection physics, models, validation |
| [spectroscopy-biomarkers.md](literature/spectroscopy-biomarkers.md) | Paper summaries: label-free uric acid, POC devices, EEM-CNN |
| [signal-processing.md](literature/signal-processing.md) | SNV validation, Savitzky-Golay, arPLS, PLS vs 1D-CNN |
| [matrix-correction.md](literature/matrix-correction.md) | Turbidity, dilution, urochrome, inner filter effects, pH correction |
| [calibration-transfer.md](literature/calibration-transfer.md) | DS, PDS, CORAL, MVG augmentation for device harmonization |
| [deep-learning-spectral.md](literature/deep-learning-spectral.md) | Model selection by dataset size, data augmentation (WGAN-GP, diffusion) |
| [physics-grounded-ml.md](literature/physics-grounded-ml.md) | Physics-informed ML taxonomy: Beer-Lambert constraints, symbolic regression |
| [eis-electrochemical.md](literature/eis-electrochemical.md) | EIS for creatinine, glucose, ionic strength, albumin, bacteria |
| [multi-task-modeling.md](literature/multi-task-modeling.md) | Multi-task learning for spectral data |
| [urine-preanalytics.md](literature/urine-preanalytics.md) | Pre-analytical variability in urine samples |
| [regulatory-ivd.md](literature/regulatory-ivd.md) | IVD regulatory pathway |
| [papers/](literature/papers/) | 15 reference PDFs |

### [modules/](modules/) — Python API Documentation

| Doc | Module |
|-----|--------|
| [transformers.md](modules/transformers.md) | `ds.process.transformers` — DSP pipeline transformers |
| [prcPandas.md](modules/prcPandas.md) | `ds.process.prcPandas` — Low-level signal processing |
| [metrics.md](modules/metrics.md) | `ds.process.metrics` — Spectrum quality & time-series features |
| [explain.md](modules/explain.md) | `learn.explain.ExploreShap` — SHAP-based model explainability |

### [meta/](meta/) — Quality & Tooling

| Doc | Description |
|-----|-------------|
| [gap-analysis.md](meta/gap-analysis.md) | Scientific content gaps: missing LOD/LOQ, methodology, validation |
| [libraries.md](meta/libraries.md) | Python library catalog (90+ libs by domain) |
| [docs-recommendations.md](meta/docs-recommendations.md) | Documentation improvement notes |
