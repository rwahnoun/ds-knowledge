# Regulatory Pathway for Spectroscopic IVD Devices

**Device:** Jimini — pen-sized reagentless urine analyzer (UV-Vis/NIR spectroscopy + EIS)  
**Target markets:** EU (primary), US (secondary)  
**Date:** 2026-04-09  
**Status:** First pass — regulatory landscape synthesis

---

## Table of Contents

1. [Device Description for Regulatory Purposes](#1-device-description-for-regulatory-purposes)
2. [EU IVDR Classification](#2-eu-ivdr-classification)
3. [EU Conformity Assessment Route](#3-eu-conformity-assessment-route)
4. [US FDA Pathway](#4-us-fda-pathway)
5. [CLIA Complexity Classification](#5-clia-complexity-classification)
6. [Clinical Performance Requirements](#6-clinical-performance-requirements)
7. [Software as a Medical Device (SaMD) & AI/ML](#7-software-as-a-medical-device-samd--aiml)
8. [Technical Documentation Requirements](#8-technical-documentation-requirements)
9. [Post-Market Surveillance](#9-post-market-surveillance)
10. [Timeline & Cost Estimates](#10-timeline--cost-estimates)
11. [Competitive Regulatory Landscape](#11-competitive-regulatory-landscape)
12. [Strategic Recommendations](#12-strategic-recommendations)
13. [Sources](#13-sources)

---

## 1. Device Description for Regulatory Purposes

Before any classification can be determined, the **intended purpose** must be precisely defined. Under IVDR Article 2(12) and FDA 21 CFR 801, the intended purpose governs classification, conformity assessment, and labeling.

### Proposed Intended Purpose Statement

> Jimini is a portable in vitro diagnostic device intended for the qualitative and semi-quantitative analysis of human urine in point-of-care or near-patient settings. The device uses multi-wavelength UV-Vis-NIR optical spectroscopy (275–1078 nm) and electrochemical impedance spectroscopy (EIS) to detect and estimate the following analytes in urine:
>
> **Cellular/particulate markers (binary classification):** white blood cells (WBC/leukocytes), red blood cells (RBC/erythrocytes), bacteria (BAC), epithelial cells, crystals  
> **Chemical analytes (quantitative/semi-quantitative):** creatinine, osmolality, total urinary porphyrins (TUP), porphobilinogen (PBG), bilirubin, uric acid, protein  
> **Supporting markers:** sodium, chloride, nitrites  
>
> Results are intended to assist healthcare professionals in screening for urinary tract infection, haematuria, metabolic disorders, and porphyria. They are not intended as a definitive diagnosis. Confirmation by laboratory testing is required when clinically indicated.

### Intended User

Healthcare professionals (nurses, physicians, point-of-care staff) in clinical settings. **Not** for self-testing/home use (this distinction critically affects EU classification under Rule 4).

### Specimen Type

Human urine (voided midstream, catheter, or indwelling catheter output).

---

## 2. EU IVDR Classification

The EU IVDR (Regulation 2017/746, applicable from 26 May 2022) uses a risk-based seven-rule classification system (Annex VIII). **All seven rules must be applied; the highest result wins.**

### Application of Classification Rules

| Rule | Description | Application to Jimini | Classification |
|---|---|---|---|
| **Rule 1** | Life-threatening transmissible agents in blood/tissue; blood supply screening | Jimini detects bacteria in urine (not blood supply). UTI detection does not involve life-threatening agents for blood supply screening. | Not applicable → **Not Class D** |
| **Rule 2** | Blood grouping / tissue typing | Not applicable — no blood group or transplant markers | Not applicable |
| **Rule 3(a–l)** | High individual risk — specific infectious agents, cancer screening, TDM | Rule 3(a): sexually transmitted agents — Jimini does not specifically detect Chlamydia/Gonorrhea. Rule 3(e): infectious agents likely fatal if untreated — UTI bacteria at standard POC screening level, not life-threatening agents requiring urgent treatment. Rule 3(i): monitoring medicine/substance levels — creatinine/osmolality for specimen dilution, not TDM. **Key question: does porphyria screening trigger Rule 3(j)?** Porphyria is a serious life-threatening condition — detecting PBG/TUP to identify acute porphyria attacks *could* trigger Rule 3(j). | **Borderline Class B/C — see below** |
| **Rule 4** | Self-testing devices | Intended for professional use, not home self-testing | Not applicable — does not elevate to Class C |
| **Rule 5** | General laboratory instruments | Jimini IS intended for a specific IVD purpose | Not a Class A instrument |
| **Rule 6** | Calibrators and control materials | Not applicable — Jimini is an analyzer, not calibrators | Not applicable |
| **Rule 7** | Specimen receptacles | Not applicable | Not applicable |

### Classification Determination

**Most biomarkers (WBC, RBC, BAC, creatinine, osmolality, bilirubin, uric acid, protein) → Class B**

General urinalysis falls under **Rule 7 (specimen) + Rule 5 default**, but the device generates IVD results → falls to the **Class B default** for devices not meeting Rules 1–4. The MDCG 2020-16 rev.3 guidance explicitly lists clinical chemistry analyzers and general urinalysis systems as Class B examples.

**Porphyria markers (PBG, TUP) → potentially Class C**

If the device's intended purpose explicitly includes "detection of acute porphyria attacks" or "management of patients with porphyria," Rule 3(j) — "devices used in the management of patients suffering from life-threatening diseases or conditions" — may apply, elevating these analytes to **Class C**. This is a critical strategic decision:

| Intended purpose option | Classification | Notified Body | Implication |
|---|---|---|---|
| **Option A:** Describe porphyria markers as "screening/informational only, not for acute management" | **Class B** | Yes | Lower burden; more defensible if sensitivity/specificity are modest |
| **Option B:** Claim management of porphyria patients | **Class C** | Yes + deeper clinical data review | Higher burden; enables clearer clinical claim for porphyria use case |

**Recommendation for Jimini v1.0: classify as Class B with a carefully scoped intended purpose that positions porphyria markers as screening/informational, not for acute management.**

> ⚠️ **Engage a regulatory consultant or Notified Body for a formal classification opinion early.** The Rule 3(j) porphyria question is genuinely borderline and could affect the entire conformity assessment route.

### Classification Summary

| Analyte Group | Classification | Rule | Rationale |
|---|---|---|---|
| General urinalysis (WBC, RBC, BAC, epiCells, crystals, bilirubin, protein, uric acid, creatinine, osmolality, Na, Cl, nitrites) | **Class B** | Rule 5/default | General urinalysis — Class B default |
| TUP, PBG (scoped as screening) | **Class B** | Rule 5/default | Screening/informational claim |
| TUP, PBG (if acute management claimed) | **Class C** | Rule 3(j) | Life-threatening condition management |
| **Overall device (recommended)** | **Class B** | — | Conservative scoping; revisit for v2.0 |

---

## 3. EU Conformity Assessment Route

### Class B Conformity Assessment

Under IVDR Article 48 and Annex IX, Class B devices require:

1. **Quality Management System (QMS) audit** by a Notified Body (EN ISO 13485:2016 certification)
2. **Technical documentation assessment** by the Notified Body
3. **Performance evaluation** review (analytical + clinical performance data)
4. **EU Declaration of Conformity** (manufacturer signs after NB certificate)
5. **CE marking** (affixed to device and labeling)
6. **EUDAMED registration** (UDI assignment, Basic UDI-DI, device registration)

### Class B vs Class C Difference

| Aspect | Class B | Class C |
|---|---|---|
| QMS audit | Yes (ISO 13485) | Yes (ISO 13485) |
| Technical documentation | Assessment by NB | Assessment by NB |
| Performance evaluation | NB reviews | NB reviews + deeper scrutiny |
| Expert panel | No | Possible for some devices |
| EURL batch verification | No | No (Class D only) |
| Typical NB time | 6–12 months | 9–18 months |
| Typical NB cost | €20,000–80,000 | €40,000–150,000+ |

### Technical Documentation (Annex II & III)

**Annex II** (full technical documentation) must include:
- Device description and specification (all components, algorithms, software)
- Reference to standards applied (EN ISO 13485, IEC 62304, IEC 62366, ISO 14971)
- Design and manufacturing information
- **Performance evaluation plan and report (PEPR)**
- Post-market surveillance plan
- Instructions for use (IFU)

**Annex III** (performance evaluation documentation):
- Analytical performance: precision (repeatability/reproducibility), accuracy, linearity, measuring range, detection limit, specificity, interference
- Clinical performance: sensitivity, specificity, PPV, NPV relative to reference standard
- Scientific validity: evidence that the analyte is associated with the claimed clinical condition

### Notified Bodies for IVD (Designated under IVDR)

As of 2025, 19 Notified Bodies are designated for IVDR. Key ones for IVD diagnostics:

| Notified Body | Country | Notes |
|---|---|---|
| **BSI (British Standards Institution)** | UK/EU | Largest NB; strong IVD experience; EU-designated (separate from UK UKCA) |
| **TÜV SÜD** | Germany | Strong medical device / IVD; German regulatory tradition |
| **DEKRA** | Germany/EU | Growing IVD portfolio |
| **SGS SA** | Switzerland/EU | Strong in diagnostics |
| **Eurofins** | Belgium/EU | Specialist in IVD conformity assessment |

> **Current bottleneck:** NB capacity is severely constrained. As of 2025, wait times for initial NB engagement can be 3–12 months before the assessment even begins. Apply early.

### Post-Market Surveillance (IVDR Articles 78–81)

For **Class B**:
- **Post-Market Surveillance (PMS) Plan** required (Annex III)
- **Post-Market Surveillance Report (PMSR)** — updated when significant findings
- **Vigilance reporting** — serious incidents reported to national competent authority within 15 days (Class B)
- **EUDAMED Post-Market Surveillance module** — once fully operational

For **Class C**:
- All the above, plus:
- **Periodic Safety Update Report (PSUR)** — mandatory, at least annually

---

## 4. US FDA Pathway

### CFR Classification and Product Codes

Urinalysis devices are classified under **21 CFR Part 864** (Hematology) and **21 CFR Part 862** (Clinical Chemistry). The relevant product codes are:

| Product Code | Device Type | CFR | Class | Pathway |
|---|---|---|---|---|
| **KQO** | Automated Urinalysis System (analyzer + sediment) | 21 CFR 864.6550 | II | 510(k) |
| **LKM** | Urine Particle Counter (flow cytometry type) | 21 CFR 864.6550 | II | 510(k) |
| **JIL** | Urinary Glucose (non-quantitative) | 21 CFR 862.1340 | II | 510(k) |
| **JIO** | Occult Blood Test / Hemoglobin (urine) | 21 CFR 864.7400 | II | 510(k) |
| **JJY** | Bilirubin (semi-quantitative) | 21 CFR 862.1095 | II | 510(k) |
| **MYN** | Urine Creatinine | 21 CFR 862.1145 | II | 510(k) |
| **LVA** | Clinical Chemistry Analyzer (multipurpose) | 21 CFR 862.2160 | II | 510(k) |

**Jimini will likely require multiple product codes** because it claims multiple analytes. The primary product code will be **KQO** (Automated Urinalysis System) given the combination of sediment markers (WBC, RBC, BAC) and chemistry (bilirubin, protein, creatinine). Additional product codes (JIO for blood, JJY for bilirubin, MYN for creatinine) will be listed as secondary.

### Primary Pathway: 510(k) — Substantial Equivalence

**510(k) requires:** (1) a predicate device with the same intended use, (2) same or equivalent technological characteristics, (3) no new safety/effectiveness questions.

**Predicate devices for Jimini:**

| Predicate | Manufacturer | 510(k) # | Technology | Notes |
|---|---|---|---|---|
| **Clinitek Novus** | Siemens Healthineers | K140717 | Optical reflectance strip + CMOS sediment | Gold standard urine chemistry + sediment |
| **iQ200 Elite** | Beckman Coulter (IRIS) | K093861 | Flow cytometry + digital imaging for sediment | Sediment + chemistry; complex predicate |
| **UF-5000** | Sysmex | K171883 | Flow cytometry (fluorescence) for sediment | Strongest predicate for cellular markers (WBC, RBC, BAC) |
| **cobas u 701** | Roche Diagnostics | — | Automated microscopy + reflectance chemistry | Combined sediment + chemistry |
| **Atellica UAS 800** | Siemens | — | Microscopy + AI-based morphology | Recent; includes AI image analysis |
| **SpectraPhone** | — | Not found | UV-Vis spectroscopy, 288 channels, 340–850 nm | Closest technology match; published in Nature 2026; no FDA clearance found |

**Best predicate strategy:** Use **UF-5000 (K171883)** as primary predicate for cellular markers (WBC, RBC, BAC classification) and **Clinitek Novus (K140717)** as secondary predicate for chemical analytes (bilirubin, creatinine, protein, etc.). Jimini's spectroscopic technology differs substantially from both flow cytometry and reflectance strip reading — this difference must be addressed in the substantial equivalence analysis.

**Key 510(k) question:** Can spectroscopy + ML achieve substantial equivalence to flow cytometry for WBC/RBC/bacteria counting? Answer depends on clinical performance data. If Jimini's sensitivity/specificity are comparable to the predicates, the FDA will likely accept the different technological approach (precedent: different technology can be equivalent if it achieves similar performance without new safety risks).

### Alternative Pathway: De Novo

If the spectroscopic approach is considered **novel** (no predicate with the same measurement principle), De Novo is appropriate. De Novo:
- Creates a new product code
- Establishes new special controls for the category
- Clears the device as Class II
- Subsequent similar devices can use Jimini as a predicate for 510(k)

**De Novo is appropriate if:** the FDA determines that spectroscopic multi-analyte urinalysis represents a novel device category for which no 510(k) predicate exists with similar intended use AND similar technology. Given that no reagentless multi-spectral urinalysis system appears to have received FDA clearance, De Novo is a realistic pathway.

**De Novo timeline:** 9–18 months; more resource-intensive than 510(k) but creates a defensible product code.

**Recommendation:** Prepare for **510(k) with UF-5000 + Clinitek as predicates** but have De Novo as backup. Conduct a **Pre-Submission (Q-Sub) meeting** with FDA CDRH to align on pathway before filing.

### FDA Submission Structure

A 510(k) for Jimini must include:

1. **Device description:** Hardware (LEDs, sensors, EIS), software (ML models, signal processing pipeline), intended use, indications for use
2. **Substantial equivalence comparison table:** Feature-by-feature comparison to predicates
3. **Performance testing:**
   - Analytical performance: precision, accuracy, linearity per CLSI guidance (EP5, EP6, EP7, EP9, EP15)
   - Interference testing (CLSI EP7-A3): hemolysis, lipemia, icterus, common medications
   - Clinical performance: sensitivity/specificity vs. reference standard (microscopy for cells, clinical chemistry for analytes)
4. **Software documentation (FDA SW guidance, June 2023):** IEC 62304 compliance, risk management (ISO 14971), cybersecurity (threat model, SBOM)
5. **AI/ML documentation** (if applicable): training data, test set performance, subgroup analysis, PCCP (if planned)
6. **Labeling:** Instructions for use, expected values tables, limitations
7. **Biocompatibility** (ISO 10993): if any patient-contacting components
8. **Electrical safety and EMC:** IEC 60601-1, IEC 60601-1-2

---

## 5. CLIA Complexity Classification

In the US, in vitro diagnostic tests used in clinical laboratories are also regulated under CLIA (Clinical Laboratory Improvement Amendments, 42 CFR Part 493). CLIA complexity determines which laboratories can use the device.

| CLIA Category | Requirements | Typical lab settings |
|---|---|---|
| **Waived** | Simple, minimal risk; FDA determines waiver eligibility | POC clinics, physician offices, pharmacies |
| **Moderate Complexity** | Qualified personnel; proficiency testing; QC requirements | Most hospital labs, outpatient labs |
| **High Complexity** | Most stringent; PhD/MD lab director required | Reference labs, academic medical centers |

**For Jimini, the target is CLIA Waiver**, enabling use in point-of-care settings without complex laboratory infrastructure. A CLIA Waiver application is submitted to FDA after 510(k) clearance and requires:

- Evidence that the test is simple (minimal operator training needed)
- Evidence that the risk of error is low (or consequence of error is manageable)
- Study demonstrating equivalence of results when used by lay operators vs. trained lab technicians (flex study)

**CLIA waiver comparator:** Siemens Clinitek Status+ (dipstick urinalysis) has CLIA waiver. Sysmex UF-5000 is **moderate complexity** (flow cytometry, trained operator required). Jimini's target classification depends on device design for simplicity.

---

## 6. Clinical Performance Requirements

### Reference Standards

| Analyte | Reference standard | Gold standard |
|---|---|---|
| **WBC (leukocytes)** | Manual phase-contrast microscopy, Fuchs-Rosenthal chamber | Urine culture (for UTI correlation) |
| **RBC (erythrocytes)** | Manual phase-contrast microscopy | Urine culture / histopathology |
| **Bacteria (BAC)** | Urine culture (>10⁵ CFU/mL) | Urine culture (gold standard) |
| **Creatinine** | Enzymatic creatinine assay (Roche Hitachi, Siemens) | Isotope dilution mass spectrometry (IDMS) |
| **Osmolality** | Freezing point depression osmometer | — |
| **Bilirubin** | Clinical chemistry analyzer | — |
| **Uric acid** | Enzymatic uricase assay | — |
| **Protein** | Pyrogallol red / biuret | 24-hr collection + quantitative assay |
| **TUP/PBG** | HPLC porphyrin quantification | — |

### Performance Benchmarks from Literature

From comparative studies of automated urine analyzers (Sysmex UF-5000, cobas u 701, Beckman iQ200) vs. manual microscopy:

**Cellular markers — target performance (per CLSI GP16-A3 and ISLH guidelines):**

| Analyte | Sensitivity target | Specificity target | Jimini v20 current | Gap |
|---|---|---|---|---|
| WBC (pyuria threshold ≥5/µL or ≥10/µL) | ≥0.80 | ≥0.90 | Sen 0.74, Spe 0.86 | Sen −0.06, Spe −0.04 |
| RBC (haematuria ≥5/µL) | ≥0.80 | ≥0.90 | Sen 0.64, Spe 0.72 | Sen −0.16, Spe −0.18 |
| BAC (>10⁵ CFU/mL by culture) | ≥0.85 | ≥0.70 | Sen 0.98, Spe 0.62 | Spe −0.08 |
| Nitrites | ≥0.75 | ≥0.90 | Sen 0.79, Spe 0.92 | ✅ Met |

> **V20 results from objectives.md:** WBC and RBC are both below specification on sensitivity AND specificity. BAC has high sensitivity but specificity gap. These gaps define the primary regulatory risk: if performance below targets at time of submission, FDA may not clear or may require additional studies.

**Reference: UF-5000 literature performance** (Comparative evaluation, PMC12818263, 2025):
- WBC: Sensitivity ~0.87, Specificity ~0.91 at standard thresholds
- RBC: Sensitivity ~0.82, Specificity ~0.89
- Bacteria: Sensitivity ~0.78, Specificity ~0.85

**FDA performance expectation:** The FDA will compare Jimini's clinical performance data to the predicate device (UF-5000). Jimini does not need to be better, but must not be substantially worse. Current V20 performance gaps represent a regulatory risk.

### Clinical Study Design Requirements

For a 510(k) with clinical data, the FDA typically expects:

| Parameter | Requirement | Notes |
|---|---|---|
| **Sample size** | ≥200 per analyte for binary; ≥100 for regression | Power calculation required; more for rare conditions |
| **Study sites** | ≥2 sites (multi-site validation) | Different patient populations, equipment |
| **Population** | Representative of intended use population | Age, sex, relevant comorbidities, disease prevalence |
| **Reference standard** | Pre-specified; performed independently | Blinded reading preferred |
| **Statistical analysis** | Pre-specified SAP; 95% CIs on all metrics | No post-hoc endpoint changes |
| **Subgroup analysis** | By relevant demographic/clinical subgroups | Required for AI/ML devices per Jan 2025 FDA guidance |
| **Interference testing** | Hemolysis (H), Lipemia (L), Icterus (I) per CLSI EP7 | Common interferences in urine |

**Total minimum clinical sample:** ~500–1000 urine samples for full panel validation, from ≥2 clinical sites, with complete reference standard testing.

---

## 7. Software as a Medical Device (SaMD) & AI/ML

Jimini's ML-based biomarker prediction models are **Software as a Medical Device (SaMD)** — software performing a medical function independently. This triggers specific regulatory requirements above and beyond hardware IVD requirements.

### IMDRF SaMD Risk Category

| Dimension | Jimini assessment |
|---|---|
| **Significance of information** | Drive/inform clinical management (WBC/RBC → UTI treatment decision; porphyrins → urgent workup) |
| **State of condition** | Serious (UTI, haematuria) to critical (acute porphyria) |
| **IMDRF Category** | **Category II–III** (serious condition + drive clinical management) |

### EU MDR Rule 11 (Software Classification)

The ML prediction models, as standalone software performing an IVD function, would be classified as **Class IIa** at minimum under MDR Rule 11. However, because they are embedded in and integral to a hardware IVD device, they are classified as part of the IVD under IVDR, not separately under MDR. **IVDR takes precedence for IVD software.** Key implication: the software classification follows the device classification (Class B), not MDR Rule 11.

### EU AI Act (Regulation 2024/1689)

The Jimini AI/ML prediction models qualify as **high-risk AI** under the EU AI Act (Annex I — AI intended to be used as a medical device or safety component of a medical device). Obligations:

- **Data governance:** Training data documentation, bias analysis, demographic representation
- **Transparency:** Algorithm description, limitations, performance characteristics in labeling
- **Human oversight:** Device must enable clinician override; output framed as clinical decision support
- **Accuracy, robustness, cybersecurity:** Ongoing validation requirements
- **Technical documentation:** Additional AI Act-specific documentation (Annex IV)
- **Conformity assessment:** Integrated into IVDR NB assessment (not separate)
- **Obligations apply from:** 2 August 2026

> Note: If Jimini CE marking is planned before August 2026, AI Act provisions apply on a transitional basis. If after August 2026, full compliance required at time of submission.

### FDA AI/ML Requirements

For a 510(k) with ML-based SaMD, FDA expects (per January 2025 draft guidance "AI-Enabled Device Software Functions"):

| Documentation element | Requirement |
|---|---|
| **Algorithm description** | Architecture, inputs, outputs, decision logic |
| **Training data** | Source, size, demographics, labeling methodology, partitioning (train/val/test independence) |
| **Test set performance** | Sensitivity, specificity, AUC + 95% CIs; independent test set never seen during training |
| **Subgroup analysis** | Performance by sex, age, disease severity, clinical site |
| **Failure mode analysis** | Common failure cases; edge cases; out-of-distribution inputs |
| **Human-AI workflow** | How clinician interacts with output; override capability |
| **Bias analysis** | Demographic representation in training data; performance disparities |
| **Cybersecurity** | Threat model, SBOM, adversarial robustness testing |

### Predetermined Change Control Plan (PCCP)

Given that Jimini's ML models will be iteratively improved (V20, V21, V22...), a **PCCP should be submitted with the initial 510(k)**. The PCCP authorizes pre-specified future modifications without requiring a new 510(k) for each update:

**PCCP scope for Jimini:**
1. **Retraining on expanded datasets** — same architecture, same intended use, same analytes; model retrained as more samples accumulate
2. **Threshold adjustments** — operating point adjustments within predefined performance bounds (e.g., moving WBC threshold ±20% to balance sensitivity/specificity)
3. **Addition of preprocessing variants** — new scatter correction methods; new derivative transforms within defined feature engineering bounds
4. **Performance improvement** — model updates that demonstrably improve sensitivity/specificity beyond current performance without degrading other analytes

**PCCP boundaries (what it CANNOT cover):**
- Adding new analytes not in original intended use
- Changing the fundamental model architecture (e.g., PLS → deep CNN)
- Modifying the hardware (LED wavelengths, sensors)
- Expanding intended use to self-testing or paediatric use

### IEC 62304 Compliance

All Jimini software must comply with **IEC 62304** (Medical Device Software — Software Life Cycle Processes). Safety class assignment:

| Software component | IEC 62304 Safety Class | Rationale |
|---|---|---|
| Spectral acquisition firmware (STM32) | Class B | Hardware failure could affect measurement accuracy |
| Signal processing pipeline | Class B | Errors could propagate to incorrect results |
| ML prediction models | **Class B–C** | Incorrect WBC/RBC/BAC result could delay treatment or cause unnecessary treatment |
| Porphyria detection (PBG/TUP) | **Class C** | Acute porphyria is life-threatening; missed detection has serious consequences |
| Result display and reporting | Class B | |

Class C software requires the most rigorous IEC 62304 documentation: detailed software requirements, architecture documentation, unit testing, integration testing, system testing with full traceability.

---

## 8. Technical Documentation Requirements

### EU IVDR Annex II/III Technical Documentation Outline

For a Class B IVD, the technical documentation (TD) must contain:

```
1. Device Description and Specification
   1.1 Device description (hardware, LEDs, sensors, EIS, optical path)
   1.2 Intended purpose and indications for use
   1.3 Variants / accessories / configurations
   1.4 General description of key functional elements
   1.5 Materials of biological origin (none expected)
   1.6 Single-use / sterilization (not applicable)
   
2. Reference to Previous and Similar Generations
   2.1 Previous generations of Jimini (if any)
   2.2 Similar CE-marked devices from other manufacturers
   
3. Design and Manufacturing Information
   3.1 Hardware design documentation
   3.2 Software architecture (IEC 62304 software development lifecycle documentation)
   3.3 Manufacturing process summary
   3.4 Quality management system documentation (EN ISO 13485:2016 certificate)
   
4. General Safety and Performance Requirements (Annex I GSPR Checklist)
   4.1 Chemical, physical, biological properties
   4.2 Infection and microbial contamination
   4.3 Electrical and electronic properties (IEC 60601-1, EMC IEC 60601-1-2)
   4.4 Software properties (IEC 62304, IEC 62366 usability)
   4.5 Protection against radiation (UV-C safety at 275nm)
   4.6 Mechanical properties
   
5. Benefit-Risk Analysis (ISO 14971:2019)
   5.1 Risk management file
   5.2 Risk-benefit analysis
   
6. Product Verification and Validation
   6.1 Pre-clinical testing (analytical performance)
   6.2 Clinical evidence (performance evaluation report)
   
7. Performance Evaluation Documentation (Annex III)
   7.1 Scientific validity (analyte-condition association evidence)
   7.2 Analytical performance:
       - Precision (within-run, between-run, between-day)
       - Accuracy (method comparison vs reference)
       - Analytical sensitivity / LoD / LoQ
       - Analytical specificity / interference testing
       - Linearity and measuring range
   7.3 Clinical performance:
       - Sensitivity / specificity per analyte
       - Multi-site clinical study report
       - Comparison to reference standard
       
8. Post-Market Surveillance Plan (Annex III, Part B)
   
9. Instructions for Use (Annex I, Chapter III)
```

### Standards Applied

| Standard | Domain |
|---|---|
| **EN ISO 13485:2016** | Quality management system |
| **IEC 62304:2006+AMD1:2015** | Medical device software lifecycle |
| **IEC 62366-1:2015** | Usability / human factors |
| **ISO 14971:2019** | Risk management |
| **IEC 60601-1** | Electrical safety (general) |
| **IEC 60601-1-2** | EMC |
| **ISO 15189** | Medical laboratory requirements (for clinical study labs) |
| **CLSI EP5-A3** | Precision evaluation |
| **CLSI EP6** | Linearity |
| **CLSI EP7-A3** | Interference testing |
| **CLSI EP9-A3** | Method comparison |
| **CLSI EP15-A3** | User verification of precision and accuracy |
| **CLSI GP16-A3 / PRE05** | Urinalysis procedures and sample collection |

---

## 9. Post-Market Surveillance

### EU IVDR Requirements

**For Class B (Jimini recommended classification):**

| Requirement | Frequency | Content |
|---|---|---|
| **PMS Plan** (Annex III) | At launch | Data sources, thresholds, feedback collection mechanisms |
| **Post-Market Surveillance Report (PMSR)** | Updated when triggered by significant findings | Summary of PMS data, safety conclusions, benefit-risk reconfirmation |
| **Vigilance reporting** | 15 days for serious incidents | Any serious incident or field safety corrective action (FSCA) |
| **EUDAMED reporting** | Ongoing | Device registration, incident reports (when EUDAMED modules active) |
| **Trend reporting** | When statistical increase in non-serious incidents | MDCG guidance on vigilance thresholds |

**For Class C (if porphyria management claimed):**
- All of the above, plus:
- **Periodic Safety Update Report (PSUR)** — annually throughout device lifetime
- PSUR summarizes clinical performance data, safety signal analysis, benefit-risk balance

### PMS Data Sources for Jimini

| Source | Data collected |
|---|---|
| Clinical complaint/feedback system | False positives/negatives reported by clinicians |
| Remote telemetry (if implemented) | Algorithm performance metrics, error logs, input distribution monitoring |
| Post-market clinical follow-up (PMCF) studies | Prospective real-world performance monitoring |
| Literature surveillance | Published studies on competing devices, reference standard evolution |
| Vigilance database monitoring | Cross-market incident signals |

### FDA Post-Market Requirements

| Requirement | Trigger | Content |
|---|---|---|
| **Medical Device Reports (MDR)** (21 CFR 803) | Serious injuries, deaths, malfunctions | Report to FDA within 30 days (non-urgent) or 5 days (urgent) |
| **Corrections and Removals** (21 CFR 806) | Any correction reducing risk of serious adverse health consequences | Report within 10 days |
| **Annual Report** (for 510(k) devices with conditions of approval) | Annually | Device performance data, complaints, changes |
| **PCCP reporting** (if authorized) | Each modification implemented | Notify FDA within 30 days of implementing a PCCP-authorized change |

### AI/ML Model Monitoring (Post-Market)

For Jimini's ML prediction models, ongoing performance monitoring is both a regulatory expectation (per FDA January 2025 guidance) and a safety requirement:

- Monitor prediction confidence score distributions for drift
- Track false positive / false negative rates in clinical deployments (requires ground truth collection)
- Implement statistical process control (SPC) on key performance metrics
- Report performance trends in PMSR/PSUR
- Document all algorithm updates in version control with performance comparison to previous version

---

## 10. Timeline & Cost Estimates

### EU Path to CE Mark (Class B)

| Phase | Activity | Duration | Cost (EUR) |
|---|---|---|---|
| **Pre-submission** | Device classification determination; regulatory consultant engagement | 1–3 months | €5,000–20,000 |
| **QMS implementation** | ISO 13485 QMS setup and certification | 6–18 months | €15,000–50,000 (consultant + NB audit) |
| **Technical documentation** | Prepare Annex II/III; write risk file, IFU, GSPR checklist | 6–12 months (parallel with QMS) | €20,000–50,000 (internal + consultant) |
| **Analytical performance studies** | Precision, accuracy, linearity, interference (CLSI panel) | 3–6 months | €30,000–80,000 (lab costs + reagents) |
| **Clinical study** | Multi-site clinical validation (n ≥ 500) | 12–24 months | €80,000–250,000 |
| **NB assessment** | NB review of QMS + TD | 6–18 months (after application) | **€20,000–80,000 (NB fees)** |
| **CE marking** | Declaration of Conformity; CE label; EUDAMED registration | 1–2 months | €2,000–5,000 |
| **TOTAL** | | **~24–48 months from start** | **€170,000–535,000** |

> **⚠️ NB capacity bottleneck:** As of 2025, initial NB engagement wait times are 6–18 months. Factor this into timeline.

### US FDA Path (510(k))

| Phase | Activity | Duration | Cost (USD) |
|---|---|---|---|
| **Pre-submission (Q-Sub)** | FDA meeting to align on classification, pathway, clinical study design | 3–4 months | $5,000–10,000 |
| **Analytical performance** | CLSI panel (precision, accuracy, interference) | 3–6 months | $50,000–100,000 |
| **Clinical study** | Multi-site validation, n ≥ 500 | 12–24 months | $150,000–400,000 |
| **Software documentation** | IEC 62304, cybersecurity, AI/ML documentation | 3–6 months (parallel) | $30,000–80,000 |
| **510(k) preparation** | Filing preparation, regulatory consultant | 3–6 months | $20,000–60,000 |
| **FDA review** | 90-day target; often 4–8 months with AI | 4–12 months | FDA user fee: **$22,248** (FY2025 small business fee) |
| **CLIA waiver (optional)** | Waiver application post-clearance | 6–12 months | $5,000–20,000 |
| **TOTAL** | | **~24–42 months from start** | **$260,000–670,000** |

### Combined EU + US Strategy (Typical for EU-first company)

1. **Year 1–2:** Complete analytical performance, design lock, ISO 13485 QMS, start clinical study, file Q-Sub with FDA
2. **Year 2–3:** Complete clinical study, prepare TD and 510(k), apply to EU NB
3. **Year 3–4:** EU NB assessment, 510(k) FDA review
4. **Year 4:** CE mark + FDA clearance (if parallel tracks successful)

**Total budget for dual clearance:** €500,000–€1,200,000 (highly variable; clinical study is the dominant cost driver)

---

## 11. Competitive Regulatory Landscape

### Cleared Urinalysis Analyzers (FDA)

| Device | Manufacturer | 510(k) # | Technology | Cleared | Notes |
|---|---|---|---|---|---|
| **Clinitek Novus** | Siemens | K140717 | Optical reflectance + CMOS sediment imaging | 2014 | Combined strip + sediment; product codes KQO, JIO, JJY |
| **iQ200 Elite** | Beckman Coulter (IRIS) | K093861 | Flow cytometry + digital imaging | 2009 | Sediment specialist; gold standard for cell counts |
| **UF-5000** | Sysmex | K171883 | Flow cytometry (laser + fluorescence) | 2017 | Most advanced automated sediment; moderate complexity |
| **Atellica UAS 800** | Siemens | K210127 | Automated microscopy + AI morphology | 2021 | AI-assisted particle classification |
| **cobas u 701** | Roche | — | Automated microscopy | ~2015 | Standard hospital lab device |

> **SpectraPhone (spectroscopic urinalysis, 2026):** Published as a research prototype in Nature Scientific Reports (2026) measuring 288 spectral channels (340–850 nm) on 401 clinical samples. No FDA 510(k) found. If Jimini files first, it could become the predicate for a new spectroscopic urinalysis product code.

### EU EUDAMED Status

No CE-marked reagentless spectroscopic urine analyzers were identified in EUDAMED as of early 2026. The closest CE-marked devices are conventional automated analyzers (Sysmex UF-5000, Siemens Clinitek Status+) using optical dipstick reading or flow cytometry — fundamentally different technologies from Jimini's multi-LED spectroscopy.

**Opportunity:** Jimini could be a **first-in-class CE-marked reagentless spectroscopic urine analyzer**, establishing the clinical and regulatory precedent for this category.

---

## 12. Strategic Recommendations

### Priority 1: Classification Decision (Month 1–3)

1. Engage a **regulatory consultant** (e.g., BSI Medical, TÜV SÜD, or specialist IVD consultant) for a formal IVDR classification opinion on the porphyria marker question (Class B vs C)
2. Scope intended purpose carefully: **initial Jimini v1.0 claim should be Class B** — general urinalysis including WBC/RBC/BAC/bilirubin/creatinine/osmolality, with porphyrins as "informational screening" only
3. Porphyria management claim reserved for **v2.0 after Class B clearance** and clinical validation

### Priority 2: Performance Gap Closure (Month 1–12, parallel)

The V20 results show WBC (Sen 0.74) and RBC (Sen 0.64, Spe 0.72) below regulatory targets. These gaps must be closed before a regulatory submission:

- WBC: target Sen ≥0.80, Spe ≥0.90 (V20: Sen 0.74, Spe 0.86) — **both below target**
- RBC: target Sen ≥0.80, Spe ≥0.90 (V20: Sen 0.64, Spe 0.72) — **both below target**
- BAC: target Sen ≥0.85 (V20: Sen 0.98 ✅), Spe ≥0.70 (V20: Spe 0.62) — **Spe below target**

Regulatory submissions require clinical data demonstrating performance AT OR ABOVE targets. Submitting with current performance will result in FDA deficiency letters or IVDR NB assessment failure.

### Priority 3: Quality Management System (Month 3–12)

- Implement **EN ISO 13485:2016 QMS** — this is prerequisite for any NB engagement
- ISO 13485 scope: design, development, manufacture, and distribution of Jimini
- Target certification from a recognized certification body (TÜV SÜD, BSI, DNV)
- Document all design history files, FMEA, and design verification activities under QMS

### Priority 4: Clinical Study Design (Month 6–18)

- Design a **prospective, multi-site clinical study** (minimum 2 sites, ideally 3)
- Target n ≥ 500 urine samples with complete reference panel
- Pre-register study in ClinicalTrials.gov or EU Clinical Trials Register
- Pre-specify all endpoints, thresholds, and statistical methods
- Include sufficient representation of: UTI-positive, haematuria, porphyria (if claiming), proteinuria

### Priority 5: FDA Pre-Submission (Month 6–9)

- Submit a **Q-Sub meeting request** to FDA CDRH
- Request feedback on: (1) primary predicate device selection, (2) clinical study design, (3) AI/ML documentation expectations, (4) PCCP scope
- FDA Q-Sub response takes ~70 days; meeting within 90 days
- This alignment reduces risk of deficiency letters during formal review

### Priority 6: PCCP Planning (Month 12–18)

- Design the PCCP to cover routine model retraining and threshold optimization
- Document training data governance procedures, acceptance criteria for model updates, and reporting procedures
- Submit PCCP as part of initial 510(k) — this enables rapid model improvement without new submissions after clearance

### Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Performance gaps in WBC/RBC not closed before submission | High | High | Prioritize ML improvements in v21/v22; do not file until targets met |
| NB capacity delays EU timeline by 12+ months | Medium | Medium | Apply to NB early; have multiple NB applications in parallel |
| FDA classifies spectroscopic approach as novel → De Novo required | Medium | Medium | Q-Sub meeting early; prepare for De Novo as backup |
| Rule 3(j) porphyria claim escalates to Class C | Low-Medium | Medium | Scope porphyria markers as informational screening only |
| AI Act compliance requires additional EU documentation by Aug 2026 | High | Low-Medium | Build AI Act documentation into TD preparation now |
| Clinical study underpowered for rare analytes (TUP, PBG) | High | Medium | Enrich study with porphyria/hepatic disease patients |

---

## 13. Sources

### EU Regulatory Sources

| Source | URL |
|---|---|
| IVDR Regulation (EU) 2017/746 full text | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?rid=6&uri=CELEX%3A32017R0746) |
| IVDR Classification Rules — MedDeviceGuide (comprehensive) | [meddeviceguide.com](https://meddeviceguide.com/blog/ivdr-classification-rules-guide) |
| MDCG 2020-16 rev.3 Guidance on IVD Classification Rules (July 2024) | [health.ec.europa.eu](https://health.ec.europa.eu/system/files/2023-02/md_mdcg_2020_guidance_classification_ivd-md_en.pdf) |
| BSI IVDR Conformity Assessment Routes Booklet | [bsigroup.com](https://www.bsigroup.com/globalassets/meddev/localfiles/en-us/brochures/bsi-md-ivdr-conformity-assessment-routes-booklet-us-en.pdf) |
| TEAM-NB IVDR Transition Timelines | [team-nb.org](https://www.team-nb.org/faq-items/what-are-the-timelines-for-obtaining-ce-certification-under-the-mdr-or-ivdr/) |
| NB Fees — Casus Consulting (Aug 2024) | [casusconsulting.com](https://casusconsulting.com/eu-commission-notified-body-list-fees-estimate-ce-marking-cost/) |
| IVDR Post-Market Surveillance Requirements | [euivdr.com/post-market-surveillance-reporting](https://euivdr.com/post-market-surveillance-reporting/) |
| PSUR requirements for IVD manufacturers | [qservegroup.com](https://www.qservegroup.com/eu/en/b1348/new-mdcg-guidance-on-periodic-safety-update-report--psur---whats-in-it-for-ivd-manufacturers) |
| MDCG 2025-10 PMS guidance | [health.ec.europa.eu](https://health.ec.europa.eu/document/download/a9ad86b7-1b8e-4bae-beb4-48b2b3ed2f05_en?filename=mdcg_2025-10_en.pdf) |
| EU AI Act (Regulation 2024/1689) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) |

### FDA Sources

| Source | URL |
|---|---|
| FDA AI/ML-Enabled Medical Devices Regulatory Guide | [meddeviceguide.com](https://meddeviceguide.com/blog/ai-ml-medical-device-regulatory-guide) |
| FDA 510(k) Database | [accessdata.fda.gov](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm) |
| Clinitek Novus 510(k) K140717 | [accessdata.fda.gov/cdrh_docs/pdf14/K140717.pdf](https://www.accessdata.fda.gov/cdrh_docs/pdf14/K140717.pdf) |
| Sysmex UF-5000 510(k) K171883 | [fda.report/PMN/K171883](https://fda.report/PMN/K171883) |
| FDA Product Code KQO (Automated Urinalysis) | [fda.innolitics.com](https://fda.innolitics.com/submissions/CH/subpart-c%E2%80%94clinical-laboratory-instruments/KQO/K946183) |
| FDA AI-Enabled Device Software Functions Draft Guidance (Jan 2025) | [hhs.gov](https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/FDA/guidance-ai-enabled-device-software-functions.pdf) |
| FDA PCCP Final Guidance (Dec 2024) | [innolitics.com](http://innolitics.com/articles/fda-guidance-2024-ai-pccp/) |
| FDA Premarket Submissions for Device Software Functions (June 2023) | [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket-submissions-device-software-functions) |
| FDA Artificial Intelligence in SaMD | [fda.gov](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device/) |
| CLIA Waiver regulations (42 CFR Part 493) | [govinfo.gov](https://www.govinfo.gov/content/pkg/CFR-2024-title42-vol5/pdf/CFR-2024-title42-vol5-part493.pdf) |
| FDA CLIA Waiver Decision Summaries | [fda.gov](https://www.fda.gov/about-fda/cdrh-transparency/clia-waiver-application-decision-summaries) |
| POCT Regulatory Guide | [meddeviceguide.com](https://meddeviceguide.com/blog/point-of-care-testing-poct-regulatory-guide) |

### Clinical Performance Standards

| Source | URL |
|---|---|
| CLSI GP16-A3 (urinalysis procedures) | [clsi.org](https://clsi.org/media/2461/gp16a3e_sample.pdf) |
| UF-5000 comparative performance evaluation (2025) | [PMC12818263](https://pmc.ncbi.nlm.nih.gov/articles/PMC12818263/) |
| cobas u 701 vs UF-1000i vs manual microscopy | [PMC6807231](https://pmc.ncbi.nlm.nih.gov/articles/PMC6807231/) |
| Automated urine sediment analyzer performance review | [De Gruyter CCLM](https://www.degruyterbrill.com/document/doi/10.1515/cclm-2019-0919/html?lang=en) |
| Preanalytical requirements of urinalysis | [PMC3936984](https://pmc.ncbi.nlm.nih.gov/articles/PMC3936984/) |
| SpectraPhone urinalysis spectroscopy (Nature Sci. Rep. 2026) | [nature.com](https://www.nature.com/articles/s41598-025-92802-2.pdf) |
| IEC 62304 guide | [intuitionlabs.ai](http://intuitionlabs.ai/articles/iec-62304-medical-device-software-guide) |
