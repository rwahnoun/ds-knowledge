# Docs Recommendations — Gaps & Improvements

Generated 2026-03-30. One section per document.

---

## projectDescription.md
- Missing hardware specs: sensor types, LED wavelengths, EIS output ranges
- No step-by-step preprocessing workflow (raw readings → final DataFrame)
- No ML model architecture or performance metrics
- Biomarker extraction logic (spectral/EIS → concentration) not explained
- `ExtractComponent` reference components: purpose and selection criteria undefined
- No file format / schema docs for raw sensor output
- Missing code examples or notebook links for typical workflows

---

## jiminiDevice.md
- No physical specs: dimensions, weight, power requirements, operating conditions
- R405 entry needs clarification (reflected 405nm? specify purpose)
- No calibration procedures, accuracy specs, or validation references
- Companion app undocumented: no UI description, workflow, or features
- No sample preparation guidance: volume requirements, handling procedures
- No data output format spec: how signals are recorded/exported
- No maintenance schedule, storage instructions, or troubleshooting

---

## biomarkers/summary.md
- No limits of detection (LOD/LOQ) for any biomarker
- Matrix interference specifics missing (e.g., ascorbate impact at 260nm quantified)
- No sample preparation protocols (centrifugation, filtration, dilution, storage)
- No cross-reactivity matrix between analytes and detection channels
- No reference standards or internal standards for QC
- ML/chemometric model details vague: no dataset sizes or validation metrics
- No EIS vs optical cost/complexity tradeoff guidance for POC deployment
- No instrumentation specs: electrode materials, optical path lengths, detection ranges
- No regulatory or clinical validation pathway noted
- No time-to-result or throughput estimates

---

## biomarkers/biomarkersSignatures.md
- Sections 3 and 5 are missing (document jumps 1→2→4→6)
- No detection limits or dynamic ranges
- References [15] and [17] duplicated/inconsistent numbering
- No ML guidance despite recommending ML-based indirect inference
- No pre-analytical stability data (storage, freeze-thaw)
- Heating protocols unspecified (temperature, duration) despite multiple references
- No interference prioritization / risk ranking
- ~6 of the 26 biomarkers incompletely described

---

## biomarkers/biomarkersSignatures2.md
- No cost/resource estimates for each development phase
- No competitive analysis vs existing POC urinalysis devices
- No regulatory/FDA pathway documentation
- No hardware supplier recommendations or component specs
- ML classifier details absent: algorithms, dataset sizes, validation metrics
- No clinical validation plan: patient population, sample size, power analysis
- No timeline, milestones, or go/no-go decision criteria
- No error bounds or accuracy targets (±%, LOD/LOQ)
- No UI/reporting format or HIS integration mention

---

## biomarkers/urine-biomarkers-photospectrometry.md
- No LOD/LOQ or quantitative detection thresholds for any biomarker
- No clinical reference ranges or diagnostic cutoff values
- No sample preparation or instrument requirements
- No specificity data or cross-reactivity information
- No validation against gold-standard clinical tests
- `image.png` reference is unresolved — spectral plots missing
- No temporal dynamics (how marker levels change over disease progression)

---

## codeImprovements/claudeSuggestions.md
- No justification for `name-Vx.y.z` versioning over alternatives
- No KPIs defined to measure post-refactoring impact
- Version pinning strategy for `ds-learn→datascience` unspecified (no requirements example)
- No cross-repo integration test plan post-consolidation
- `modelsV0/` migration decision tree missing (archive vs keep criteria)
- No list of the 9 specific bare `except:` locations to fix
- No rolled-up project timeline or effort estimate
- No rollback plan if consolidation breaks downstream code
- No definition of "done" / success criteria

---

## processing/dsp pipeline.md
- No actual implementation code for core algorithm classes (stubs only)
- Pipeline parameters (`lam=1e5`, `window_length=11`) lack tuning rationale
- No cross-validation strategy or performance metrics
- References [1]–[9] listed but no references section
- No failure mode or missing data handling
- No guidance on step skipping / reordering conditions
- No memory/runtime cost discussion
- GridSearchCV example at end is disconnected from the biomarker pipeline

---

## processing/signalsProcessingAndNormalization.md
- Code references (`calibration.py`, `transformers.py`) lack links or snippets
- No normalization quality validation metrics (CV before/after, linearity)
- No device-specific parameters: LED spectral shift ranges, photodetector response for Jimini
- No decision tree for method selection given data constraints
- CORAL and PCA alignment: no sample size requirements or PCA component guidance
- No failure mode coverage (negative corrections, insufficient water scans)
- No guidance on method ordering/combination (SNV before/after MSC?)

---

## processing/deviceCalibration.md
- No clarity on which methods are implemented in current codebase
- No quantitative comparison of methods (SNV vs MSC vs EMSC) on Jimini data
- Cross-device section: no primary method recommendation; PDS sample count unspecified
- LED crosstalk correction (Section 9, Part 2) lacks implementation details
- No expected residual error bounds after normalization
- No sensitivity analysis for edge cases (extreme dilution, pathological samples)
- Creatinine measurement method/sensor not specified for Jimini hardware

---

## processing/turbidity.md
- No intra/inter-assay repeatability or reproducibility data
- No sample stability guidance (sit time, storage, freeze-thaw)
- ML classifier section: no dataset size, class balance, CV strategy, or threshold optimization
- References [^2357^], [^2356^], [^2359^] cited but not defined
- No troubleshooting (cuvette cleanliness, temperature artifacts, hemolysis interference)
- Python library list lacks version specs or install instructions

---

## processing/prcPandas.md
- No parameter types, defaults, or constraints for any function
- No return type documentation
- Function list incomplete: "extensive filtering" mentioned but only 3 filter functions documented
- No error/edge case handling documentation (NaN, empty data, dimension mismatch)
- No performance notes for large datasets
- No library version requirements
- Single usage example insufficient — each major function needs before/after example
- No workflow examples combining functions (e.g., baseline removal → peak detection)
- `findPeaks` `fpArgs` dict sub-parameters undocumented

---

## processing/transformers.md
- No parameter ranges, defaults, or validation rules per transformer
- Return types and shape changes undocumented
- No memory/computational complexity information
- No error handling for edge cases (empty data, NaN, dimension mismatches)
- Baseline and scatter correction methods (e.g., "rubberband") not explained
- No library version dependencies listed
- Only one example pipeline; no real-world scenarios or best practice workflows
- No guidance on when transformers are inappropriate (data requirements)

---

## statistics.md
- No code examples or usage snippets for either class
- Multiclass averaging strategies incomplete (only micro/weighted; macro/samples missing)
- No method signatures, required arguments, or return types
- Visualization methods unnamed and uncustomizable without reading source
- No edge case handling documented (zero denominators, NaN, single-class)
- `StatsBase` inheritance not explained
- No guidance on which metrics to combine or use together

---

## libraries.md
- No decision tree for library selection by task type
- No Python version / dependency compatibility info
- No maintenance status indicators (some libraries appear outdated/archived)
- No code snippets or workflow examples
- No pipeline recommendations for common scenarios
- No quality/performance comparisons between alternatives
- Duplicate entries across sections without cross-references
- No validation data for UV-Vis specific use cases
- No known compatibility conflict warnings

---

## qara/datascience.md
- "Total Urinary Porphyrin" section cuts off mid-step (line 168)
- "Porphobilinogen" section has no implementation details
- Azure deployment URLs and function app names not specified
- No security documentation (auth, rate limiting, encryption)
- No troubleshooting guide or error code interpretation
- No SLA / latency / throughput specs for API
- QTP terminology ("qtpAlgorithm", "qtpAnaliticPerformance") not formally defined
- No concrete version number examples or migration guidance
- No HIPAA/GDPR compliance statements

---

## qara/datascienceDatabase.md
- No authentication or access control documentation
- No detailed schema definitions or example data structures for the 3 tables
- No query performance, DB size, or indexing strategy
- ETL failure handling and rollback procedures missing
- Incremental update merge logic and conflict resolution not explained
- No concrete query usage examples beyond function signatures
- No data retention / archival policy
- No ETL monitoring, logging, or audit trail docs
- No Python package dependency list

---

## automationRecommendations.md
- No tested hook implementation snippets or validation patterns
- GitHub MCP authentication prerequisites not documented (PAT setup)
- SKILL.md templates empty — no command definitions, exit codes, or error handling
- No recovery steps if hooks break workflows
- No metrics for when each automation should/shouldn't be used
- `feature-dev:code-reviewer` invocation syntax not specified
- No testing/validation plan before deployment
- Azure/MongoDB credential management strategy missing beyond .env mention
