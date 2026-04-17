# Literature Review Plan: Urinary Tumor Biomarkers — Optical & Electrochemical Detection

## Objective
Systematic review of tumor biomarkers detectable in human urine via optical and electrochemical methods, for diagnosis and treatment monitoring.

## Phases

### Phase 1: Literature Search
- [ ] Search for review papers on urinary tumor biomarkers (proteins, nucleic acids, EVs, metabolites)
- [ ] Search for optical biosensors for urinary cancer biomarkers
- [ ] Search for electrochemical biosensors for urinary cancer biomarkers
- [ ] Search for clinical validation studies

### Phase 2: Paper Acquisition
- [ ] Download key review papers via scihub
- [ ] Read and extract data from papers

### Phase 3: Data Extraction
- [ ] Extract biomarker data: name, cancer type, detection method, LOD, clinical validation
- [ ] Extract clinical context: screening vs monitoring vs recurrence
- [ ] Extract detection parameters and sample preparation
- [ ] Map to Jimini device capabilities

### Phase 4: Synthesis
- [ ] Build Table 1: Biomarker × Detection method × LOD × Validation
- [ ] Build Table 2: Cancer type × Biomarker type × Biomarker name
- [ ] Build Table 3: Evidence level assessment
- [ ] Build Jimini compatibility matrix
- [ ] Write final review document

## Status: COMPLETE

## Output
- `outputs/urinary-tumor-biomarkers-review.md` — Main review document (30KB)
- `outputs/urinary-tumor-biomarkers-review.provenance.md` — Source provenance

## Key Findings
- Urinary fluorescent metabolome profiling (EEM) is the most Jimini-compatible cancer screening approach
- Tryptophan fluorescence (Ex 275/Em 340) correlates with melanoma stage
- NADH/FAD redox ratio detectable with Jimini 365/455 nm LEDs
- EIS immunosensors for PSA/NMP22 are feasible add-ons
- Most EC biosensors remain lab-validated only; few tested in real urine
