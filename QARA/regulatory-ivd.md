---
title: Regulatory Pathway for Spectroscopic IVD Devices
aliases:
  - Jimini Regulatory
  - IVD Regulatory Pathway
  - IVDR Pathway
tags:
  - topic/architecture
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# Regulatory Pathway for Spectroscopic IVD Devices

Regulatory landscape synthesis for Jimini — pen-sized reagentless urine analyzer (UV-Vis/NIR spectroscopy + EIS). Target markets: EU (primary), US (secondary). See [[device]] for the device description and [[api-architecture]] for the algorithm and software architecture relevant to SaMD requirements.

---

## Device Description for Regulatory Purposes

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

---

## EU IVDR Classification

The EU IVDR (Regulation 2017/746) uses a risk-based seven-rule classification system (Annex VIII). **All seven rules must be applied; the highest result wins.**

### Application of Classification Rules

| Rule | Application to Jimini | Classification |
|---|---|---|
| **Rule 1** | Jimini detects bacteria in urine (not blood supply screening) | Not applicable → Not Class D |
| **Rule 2** | No blood group or transplant markers | Not applicable |
| **Rule 3(a–l)** | **Key question: does porphyria screening trigger Rule 3(j)?** Porphyria is life-threatening — detecting PBG/TUP for acute attack identification *could* trigger Rule 3(j) | Borderline Class B/C — see below |
| **Rule 4** | Intended for professional use, not home self-testing | Not applicable |
| **Rule 5** | Jimini IS intended for a specific IVD purpose | Not a Class A instrument |

### Classification Determination

**Most biomarkers (WBC, RBC, BAC, creatinine, osmolality, bilirubin, uric acid, protein) → Class B**

General urinalysis falls under the **Class B default** for devices not meeting Rules 1–4. MDCG 2020-16 rev.3 explicitly lists clinical chemistry analyzers and general urinalysis systems as Class B examples.

**Porphyria markers (PBG, TUP) → potentially Class C**

If the device's intended purpose explicitly includes "detection of acute porphyria attacks" or "management of patients with porphyria," Rule 3(j) — "devices used in the management of patients suffering from life-threatening diseases or conditions" — may apply, elevating these analytes to **Class C**.

| Intended purpose option | Classification | Implication |
|---|---|---|
| **Option A:** Porphyria markers as "screening/informational only, not for acute management" | **Class B** | Lower burden; more defensible if sensitivity/specificity are modest |
| **Option B:** Claim management of porphyria patients | **Class C** | Higher burden; enables clearer clinical claim for porphyria use case |

**Recommendation for Jimini v1.0: classify as Class B** with a carefully scoped intended purpose that positions porphyria markers as screening/informational, not for acute management.

> [!CAUTION]
> Engage a regulatory consultant or Notified Body for a formal classification opinion early. The Rule 3(j) porphyria question is genuinely borderline and could affect the entire conformity assessment route.

### Classification Summary

| Analyte Group | Classification | Rule | Rationale |
|---|---|---|---|
| General urinalysis (WBC, RBC, BAC, epiCells, crystals, bilirubin, protein, uric acid, creatinine, osmolality, Na, Cl, nitrites) | **Class B** | Rule 5/default | General urinalysis — Class B default |
| TUP, PBG (scoped as screening) | **Class B** | Rule 5/default | Screening/informational claim |
| TUP, PBG (if acute management claimed) | **Class C** | Rule 3(j) | Life-threatening condition management |
| **Overall device (recommended)** | **Class B** | — | Conservative scoping; revisit for v2.0 |

---

## EU Conformity Assessment Route

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
| Expert panel | No | Possible for some devices |
| Typical NB time | 6–12 months | 9–18 months |
| Typical NB cost | €20,000–80,000 | €40,000–150,000+ |

### Notified Bodies for IVD

| Notified Body | Country | Notes |
|---|---|---|
| **BSI (British Standards Institution)** | UK/EU | Largest NB; strong IVD experience |
| **TÜV SÜD** | Germany | Strong medical device / IVD |
| **DEKRA** | Germany/EU | Growing IVD portfolio |
| **SGS SA** | Switzerland/EU | Strong in diagnostics |

> [!WARNING]
> As of 2025, wait times for initial NB engagement can be 3–12 months before the assessment even begins. Apply early.

---

## US FDA Pathway

### CFR Classification and Product Codes

| Product Code | Device Type | CFR | Class | Pathway |
|---|---|---|---|---|
| **KQO** | Automated Urinalysis System (analyzer + sediment) | 21 CFR 864.6550 | II | 510(k) |
| **JIO** | Occult Blood Test / Hemoglobin (urine) | 21 CFR 864.7400 | II | 510(k) |
| **JJY** | Bilirubin (semi-quantitative) | 21 CFR 862.1095 | II | 510(k) |
| **MYN** | Urine Creatinine | 21 CFR 862.1145 | II | 510(k) |

Jimini will likely require multiple product codes. The primary product code will be **KQO** (Automated Urinalysis System).

### Primary Pathway: 510(k) — Substantial Equivalence

**Predicate devices for Jimini:**

| Predicate | Manufacturer | 510(k) # | Technology | Notes |
|---|---|---|---|---|
| **Clinitek Novus** | Siemens Healthineers | K140717 | Optical reflectance strip + CMOS sediment | Gold standard urine chemistry + sediment |
| **UF-5000** | Sysmex | K171883 | Flow cytometry (fluorescence) for sediment | Strongest predicate for cellular markers (WBC, RBC, BAC) |

**Best predicate strategy:** Use **UF-5000 (K171883)** as primary predicate for cellular markers and **Clinitek Novus (K140717)** as secondary predicate for chemical analytes.

### Alternative Pathway: De Novo

If the spectroscopic approach is considered **novel** (no predicate with the same measurement principle), De Novo is appropriate. De Novo:
- Creates a new product code
- Establishes new special controls for the category
- Timeline: 9–18 months; more resource-intensive than 510(k)

**Recommendation:** Prepare for **510(k) with UF-5000 + Clinitek as predicates** but have De Novo as backup. Conduct a **Pre-Submission (Q-Sub) meeting** with FDA CDRH to align on pathway before filing.

---

## CLIA Complexity Classification

**Target: CLIA Waiver**, enabling use in point-of-care settings without complex laboratory infrastructure. A CLIA Waiver application is submitted to FDA after 510(k) clearance and requires:

- Evidence that the test is simple (minimal operator training needed)
- Evidence that the risk of error is low
- Flex study demonstrating equivalence of results when used by lay operators vs. trained lab technicians

---

## Clinical Performance Requirements

### Reference Standards

| Analyte | Reference standard |
|---|---|
| **WBC (leukocytes)** | Manual phase-contrast microscopy, Fuchs-Rosenthal chamber |
| **RBC (erythrocytes)** | Manual phase-contrast microscopy |
| **Bacteria (BAC)** | Urine culture (>10⁵ CFU/mL) |
| **Creatinine** | Enzymatic creatinine assay |
| **Bilirubin** | Clinical chemistry analyzer |
| **TUP/PBG** | HPLC porphyrin quantification |

### Performance Benchmarks

Cellular markers — target performance (per CLSI GP16-A3 and ISLH guidelines):

| Analyte | Sensitivity target | Specificity target | Jimini v20 current | Gap |
|---|---|---|---|---|
| WBC (pyuria threshold ≥5/µL or ≥10/µL) | ≥0.80 | ≥0.90 | Sen 0.74, Spe 0.86 | Sen −0.06, Spe −0.04 |
| RBC (haematuria ≥5/µL) | ≥0.80 | ≥0.90 | Sen 0.64, Spe 0.72 | Sen −0.16, Spe −0.18 |
| BAC (>10⁵ CFU/mL by culture) | ≥0.85 | ≥0.70 | Sen 0.98, Spe 0.62 | Spe −0.08 |
| Nitrites | ≥0.75 | ≥0.90 | Sen 0.79, Spe 0.92 | ✅ Met |

> [!WARNING]
> V20 results show WBC and RBC are both below specification on sensitivity AND specificity. BAC has high sensitivity but specificity gap. These gaps define the primary regulatory risk: performance below targets at time of submission will result in FDA deficiency letters or IVDR NB assessment failure.

---

## Software as a Medical Device (SaMD) & AI/ML

Jimini's ML-based biomarker prediction models are **Software as a Medical Device (SaMD)**. This triggers specific regulatory requirements above and beyond hardware IVD requirements.

### EU AI Act (Regulation 2024/1689)

The Jimini AI/ML prediction models qualify as **high-risk AI** under the EU AI Act (Annex I — AI intended to be used as a medical device). Obligations:

- **Data governance:** Training data documentation, bias analysis, demographic representation
- **Transparency:** Algorithm description, limitations, performance characteristics in labeling
- **Human oversight:** Device must enable clinician override; output framed as clinical decision support
- **Obligations apply from:** 2 August 2026

### IEC 62304 Software Safety Classes

| Software component | IEC 62304 Safety Class | Rationale |
|---|---|---|
| Spectral acquisition firmware (STM32) | Class B | Hardware failure could affect measurement accuracy |
| Signal processing pipeline | Class B | Errors could propagate to incorrect results |
| ML prediction models | **Class B–C** | Incorrect WBC/RBC/BAC result could delay treatment |
| Porphyria detection (PBG/TUP) | **Class C** | Acute porphyria is life-threatening; missed detection has serious consequences |
| Result display and reporting | Class B | |

### Predetermined Change Control Plan (PCCP)

A **PCCP should be submitted with the initial 510(k)** to authorize pre-specified future algorithm modifications without requiring a new 510(k) for each update.

**PCCP scope for Jimini:**
1. Retraining on expanded datasets — same architecture, same intended use, same analytes
2. Threshold adjustments — operating point adjustments within predefined performance bounds
3. Addition of preprocessing variants — new scatter correction methods; new derivative transforms
4. Performance improvement — model updates that demonstrably improve sensitivity/specificity

**PCCP boundaries (what it CANNOT cover):**
- Adding new analytes not in original intended use
- Changing the fundamental model architecture (e.g., PLS → deep CNN)
- Modifying the hardware (LED wavelengths, sensors)

---

## Technical Documentation Requirements

### EU IVDR Annex II/III Technical Documentation Outline

For a Class B IVD, the technical documentation (TD) must contain:

```
1. Device Description and Specification
   1.1 Device description (hardware, LEDs, sensors, EIS, optical path)
   1.2 Intended purpose and indications for use
   1.3 Variants / accessories / configurations

2. Design and Manufacturing Information
   2.1 Hardware design documentation
   2.2 Software architecture (IEC 62304 software development lifecycle documentation)
   2.3 Quality management system documentation (EN ISO 13485:2016 certificate)

3. General Safety and Performance Requirements (Annex I GSPR Checklist)
   3.1 Electrical and electronic properties (IEC 60601-1, EMC IEC 60601-1-2)
   3.2 Software properties (IEC 62304, IEC 62366 usability)
   3.3 Protection against radiation (UV-C safety at 275nm)

4. Benefit-Risk Analysis (ISO 14971:2019)

5. Performance Evaluation Documentation (Annex III)
   5.1 Analytical performance: precision, accuracy, linearity, LoD/LoQ, specificity, interference
   5.2 Clinical performance: sensitivity / specificity per analyte; multi-site clinical study

6. Post-Market Surveillance Plan (Annex III, Part B)

7. Instructions for Use (Annex I, Chapter III)
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
| **CLSI EP5-A3** | Precision evaluation |
| **CLSI EP7-A3** | Interference testing |
| **CLSI EP9-A3** | Method comparison |
| **CLSI GP16-A3 / PRE05** | Urinalysis procedures and sample collection |

---

## Post-Market Surveillance

### EU IVDR Requirements (Class B)

| Requirement | Frequency | Content |
|---|---|---|
| **PMS Plan** (Annex III) | At launch | Data sources, thresholds, feedback collection mechanisms |
| **Post-Market Surveillance Report (PMSR)** | Updated when triggered by significant findings | Summary of PMS data, safety conclusions, benefit-risk reconfirmation |
| **Vigilance reporting** | 15 days for serious incidents | Any serious incident or field safety corrective action (FSCA) |

---

## Timeline & Cost Estimates

### EU Path to CE Mark (Class B)

| Phase | Activity | Duration | Cost (EUR) |
|---|---|---|---|
| **Pre-submission** | Device classification; regulatory consultant engagement | 1–3 months | €5,000–20,000 |
| **QMS implementation** | ISO 13485 QMS setup and certification | 6–18 months | €15,000–50,000 |
| **Technical documentation** | Prepare Annex II/III | 6–12 months (parallel with QMS) | €20,000–50,000 |
| **Analytical performance studies** | CLSI panel | 3–6 months | €30,000–80,000 |
| **Clinical study** | Multi-site clinical validation (n ≥ 500) | 12–24 months | €80,000–250,000 |
| **NB assessment** | NB review of QMS + TD | 6–18 months (after application) | €20,000–80,000 |
| **TOTAL** | | **~24–48 months from start** | **€170,000–535,000** |

### US FDA Path (510(k))

| Phase | Activity | Duration | Cost (USD) |
|---|---|---|---|
| **Pre-submission (Q-Sub)** | FDA meeting to align on classification and pathway | 3–4 months | $5,000–10,000 |
| **Analytical performance** | CLSI panel | 3–6 months | $50,000–100,000 |
| **Clinical study** | Multi-site validation, n ≥ 500 | 12–24 months | $150,000–400,000 |
| **Software documentation** | IEC 62304, cybersecurity, AI/ML documentation | 3–6 months (parallel) | $30,000–80,000 |
| **510(k) preparation** | Filing preparation | 3–6 months | $20,000–60,000 |
| **FDA review** | 90-day target; often 4–8 months with AI | 4–12 months | FDA user fee: **$22,248** (FY2025 small business fee) |
| **TOTAL** | | **~24–42 months from start** | **$260,000–670,000** |

---

## Strategic Recommendations

### Priority 1: Classification Decision (Month 1–3)

1. Engage a regulatory consultant for a formal IVDR classification opinion on the porphyria marker question.
2. Scope intended purpose: initial Jimini v1.0 claim should be **Class B** — general urinalysis including WBC/RBC/BAC/bilirubin/creatinine/osmolality, with porphyrins as "informational screening" only.

### Priority 2: Performance Gap Closure (Month 1–12)

The V20 results show WBC (Sen 0.74) and RBC (Sen 0.64, Spe 0.72) below regulatory targets. Regulatory submissions require performance AT OR ABOVE targets.

### Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Performance gaps in WBC/RBC not closed before submission | High | High | Prioritize ML improvements in v21/v22; do not file until targets met |
| NB capacity delays EU timeline by 12+ months | Medium | Medium | Apply to NB early; have multiple NB applications in parallel |
| FDA classifies spectroscopic approach as novel → De Novo required | Medium | Medium | Q-Sub meeting early; prepare for De Novo as backup |
| Rule 3(j) porphyria claim escalates to Class C | Low-Medium | Medium | Scope porphyria markers as informational screening only |
| AI Act compliance requires additional EU documentation by Aug 2026 | High | Low-Medium | Build AI Act documentation into TD preparation now |

---

## Sources

### EU Regulatory Sources

| Source | URL |
|---|---|
| IVDR Regulation (EU) 2017/746 full text | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?rid=6&uri=CELEX%3A32017R0746) |
| MDCG 2020-16 rev.3 Guidance on IVD Classification Rules (July 2024) | [health.ec.europa.eu](https://health.ec.europa.eu/system/files/2023-02/md_mdcg_2020_guidance_classification_ivd-md_en.pdf) |
| EU AI Act (Regulation 2024/1689) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) |

### FDA Sources

| Source | URL |
|---|---|
| FDA 510(k) Database | [accessdata.fda.gov](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm) |
| Clinitek Novus 510(k) K140717 | [accessdata.fda.gov/cdrh_docs/pdf14/K140717.pdf](https://www.accessdata.fda.gov/cdrh_docs/pdf14/K140717.pdf) |
| Sysmex UF-5000 510(k) K171883 | [fda.report/PMN/K171883](https://fda.report/PMN/K171883) |
| FDA AI-Enabled Device Software Functions Draft Guidance (Jan 2025) | [hhs.gov](https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/FDA/guidance-ai-enabled-device-software-functions.pdf) |
| FDA PCCP Final Guidance (Dec 2024) | [innolitics.com](http://innolitics.com/articles/fda-guidance-2024-ai-pccp/) |

### Clinical Performance Standards

| Source | URL |
|---|---|
| CLSI GP16-A3 (urinalysis procedures) | [clsi.org](https://clsi.org/media/2461/gp16a3e_sample.pdf) |
| UF-5000 comparative performance evaluation (2025) | [PMC12818263](https://pmc.ncbi.nlm.nih.gov/articles/PMC12818263/) |
| SpectraPhone urinalysis spectroscopy (Nature Sci. Rep. 2026) | [nature.com](https://www.nature.com/articles/s41598-025-92802-2.pdf) |

## Gaps

1. A formal IVDR classification opinion from a Notified Body or regulatory consultant has not yet been obtained — this is Priority 1.
2. The clinical study design (sites, n, reference standard protocols, pre-specified SAP) needs to be developed before any clinical data collection.
3. ISO 13485 QMS has not yet been implemented — prerequisite for any NB engagement.
4. PCCP scope has been outlined but not formally drafted as a regulatory document.
