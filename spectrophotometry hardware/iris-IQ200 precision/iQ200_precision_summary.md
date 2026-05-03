---
title: Iris iQ200 Precision & Accuracy Summary
aliases:
  - iQ200 Precision
  - Iris iQ200
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Iris iQ200 — Precision & Accuracy Summary

Reference data collected for [[white-blood-cells|WBC]], [[red-blood-cells|RBC]], and [[bacteria]] counting imprecision at low concentrations (~1×10⁴ cells/mL ≈ 10 cells/µL ≈ 10×10⁶/L). Relevant as a comparator for [[optical-path-design]] when setting detection thresholds for Jimini.

---

## Unit Reference

The iQ200 reports in **particles/µL** (equivalent to **×10⁶/L**).
`1×10⁶/L = 1/µL = 1000/mL`
So **1×10⁴/mL = 10/µL = 10×10⁶/L** — this sits right at/below the clinical upper-limit-of-normal for [[white-blood-cells|WBC]] (17–28/µL depending on reference), i.e. at the bottom of the analyzer's quantitative range.

---

## Headline Numbers at ~10/µL (= 1×10⁴/mL)

| Particle | Within-run CV near 10–20/µL | Source |
| --- | --- | --- |
| **[[white-blood-cells\|WBC]]** | **22–40%** (~40% at ~5/µL, ~12% at ~30/µL) | Wah 2005 Fig 1B + Table 2 |
| [[red-blood-cells\|RBC]] | 25–45% (~45% at ~5/µL, ~14% at ~36/µL) | Wah 2005 Fig 1A + Table 2 |
| Epithelial | 18–35% | Wah 2005 Table 2 |
| [[bacteria\|Bacteria]] | ~30% at ~46/µL | Linko 2006 Table 3 |

> [!IMPORTANT]
> At **1×10⁴ [[white-blood-cells|WBC]]/mL (≈10/µL)** the iQ200 is near its lower limit of quantitation. Expected within-run imprecision is **25–40% CV**. The CV ≤ 20% threshold corresponds to ~18×10⁶ [[white-blood-cells|WBC]]/L ≈ 18/µL ≈ 1.8×10⁴/mL (Wah 2005; Butch 2008).

---

## Source 1 — Wah, Wises, Butch 2005 (AJCP)

DOI: 10.1309/VNGU9Q5V932D74NU

Within-run imprecision (n = 20 replicates, 5 samples per range):

| Cell | Mean (×10⁶/L) | CV (%) |
| --- | --- | --- |
| [[red-blood-cells\|RBC]] | 786–1029 | 3.0–5.6 |
| [[red-blood-cells\|RBC]] | 253–356 | 3.4–8.4 |
| [[red-blood-cells\|RBC]] | 100–145 | 4.2–13.5 |
| [[red-blood-cells\|RBC]] | 17–20 | 14.0–29.6 |
| **[[white-blood-cells\|WBC]]** | 794–1006 | 2.4–3.4 |
| **[[white-blood-cells\|WBC]]** | 258–380 | 4.5–6.7 |
| **[[white-blood-cells\|WBC]]** | 79–115 | 3.1–15.3 |
| **[[white-blood-cells\|WBC]]** | **16–30** | **12.6–22.3** |
| Epithelial | 59–93 | 8.9–14.8 |
| Epithelial | 13–22 | 18.1–31.3 |

Low-count dilution study (Fig 1): CV ≈ 40% for [[white-blood-cells|WBC]] at ~5/µL, ~45% for [[red-blood-cells|RBC]] at lowest dilution.
"CVs of approximately 20% were found at [[red-blood-cells|RBC]], [[white-blood-cells|WBC]] and EC concentrations of 25, 18 and 21×10⁶/L, respectively."

Between-run imprecision (glutaraldehyde-fixed [[red-blood-cells|RBC]], duplicate × 12 days):

| Mean (×10⁶/L) | CV (%) |
| --- | --- |
| 1017 | 3.3 |
| 802 | 4.8 |
| 443 | 7.2 |
| 155 | 7.4 |
| 28 | 19.2 |

Correlation vs Fuchs-Rosenthal chamber (n = 166):
- [[red-blood-cells|RBC]]: y = 0.92x − 2.94, r = 0.959
- [[white-blood-cells|WBC]]: y = 0.81x − 3.20, r = 0.940 (iQ200 mean 24.7% lower)
- EC: y = 0.94x + 0.34, r = 0.951

Linearity: [[red-blood-cells|RBC]] to 1000×10⁶/L, [[white-blood-cells|WBC]] to 900×10⁶/L. Carry-over ≤ 0.2%.

---

## Source 2 — Linko et al. 2006 (Clin Chim Acta)

DOI: 10.1016/j.cca.2006.03.015

Within-run precision (Table 3):

| Particle | Mean (×10⁶/L) | Observed CV (%) | Theoretical Poisson CV (%) |
| --- | --- | --- | --- |
| [[red-blood-cells\|RBC]]-low | 12.25 | 32.6 | 20.2 |
| [[red-blood-cells\|RBC]]-high | 1246 | 6.2 | 2.0 |
| **[[white-blood-cells\|WBC]]-low** | **114.9** | **10.4** | 6.6 |
| [[white-blood-cells\|WBC]]-high | 464.6 | 4.0 | 3.3 |
| SQEP | 6.35 | 48.4 | 28.1 |
| NSE | 6.65 | 32.4 | 27.4 |
| **[[bacteria\|Bacteria]]** | **45.9** | **30.0** | 14.8 |
| Yeast | 32.7 | 25.1 | 12.4 |

Key: "Lower limit of quantification with iQ200 was about 20–30 particles×10⁶/L when using a criterion of between-day repeatability CV < 30%."

[[bacteria|Bacteria]] sensitivity: 42.9% APR alone, 64.3% after reclassification; specificity 96.4→97.0%.

Linearity 0–1000×10⁶/L, R² = 0.9874–0.9987. No carry-over.

---

## Source 3 — Butch et al. 2008 (AJCP)

DOI: 10.1309/WR1C5WNT6UFXNC6J

Body-fluids module (CSF, serous fluid) — 350 specimens, 3 sites.

Within-run imprecision:
- [[red-blood-cells|RBC]] 2.6–5.9% at 875 and 475×10⁶/L
- Nucleated cells 4.2–6.5% at 820 and 590×10⁶/L

**Lower detection limit (CV ≤ 20%): 30×10⁶/L for [[red-blood-cells|RBC]], 35×10⁶/L for nucleated cells** (body fluid).
Urine figures from Wah 2005: 25×10⁶/L ([[red-blood-cells|RBC]]), 18×10⁶/L ([[white-blood-cells|WBC]]).

CSF at clinical cut-offs ([[red-blood-cells|RBC]] 10, nucleated 5×10⁶/L):
- [[red-blood-cells|RBC]]: normal 93%, abnormal 94.6%
- Nucleated: normal 72%, abnormal 82.4% — poor at very low CSF counts, confirmed limitation.

---

## Source 4 — Shayanfar et al. 2009 (CSF Reliability)

DOI: 10.1309/AJCPCHHTZ6UDQ6WF

Reliability coefficient 0.84 for iQ200 nucleated-cell counts in CSF; unacceptable error rates at counts < 50/µL. Reinforces that iQ200 is not suitable for CSF where normal nucleated count is ≤ 5/µL.

---

## Source 5 — Bakan et al. 2016 (Biochemia Medica)

DOI: 10.11613/BM.2016.040 — open access, n = 540.

Diagnostic performance vs manual microscopy (clinical cut-offs):

| Parameter | Sensitivity | Specificity | PPV | NPV |
| --- | --- | --- | --- | --- |
| **[[white-blood-cells\|WBC]] (iQ200)** | 92% | 71% | 83% | 75% |
| [[red-blood-cells\|RBC]] (iQ200) | 90% | 63% | 65% | 76% |

Correlation: [[white-blood-cells|WBC]] r = 0.81, [[red-blood-cells|RBC]] r = 0.65, SEC r = 0.70, NEC r = 0.14 (NS), crystals r = 0.67.
Authors: "still inadequate in the determination of [[white-blood-cells|WBC]], [[red-blood-cells|RBC]] and EC in highly-pathological samples; confirmation by manual microscopy may be useful."

---

## Practical Implications at 1×10⁴ cells/mL (= 10/µL) [[white-blood-cells|WBC]]

1. Concentration **sits below the CV ≤ 20% threshold** (~18/µL for [[white-blood-cells|WBC]])
2. Expected **single-run error is 25–40% CV**; duplicate averaging improves by √2 only
3. iQ200 tends to **under-count [[white-blood-cells|WBC]] by ~20–25%** (slope 0.81 vs Fuchs-Rosenthal)
4. Error bars often straddle the upper-limit-of-normal cut-off (17–28/µL) — **manual confirmation is the literature-standard recommendation** (Bakan 2016, Butch 2008)
5. [[red-blood-cells|RBC]] at same regime: CV ~25–45%
6. [[bacteria|Bacteria]]: semiquantitative only; APR-alone sensitivity ≈ 43%, improves to ≈ 64% after reclassification

### Uncertainty Window at 1×10⁴ [[white-blood-cells|WBC]]/mL Displayed

From Wah 2005 Fig 1B, within-run CV ≈ 28–30% at mean [[white-blood-cells|WBC]] ≈ 10/µL. Using CV = 30%, SD ≈ 3/µL:

| Confidence | Window (cells/µL) | Window (cells/mL) |
| --- | --- | --- |
| ±1σ (68%) | 7–13 | 7000–13000 |
| **±2σ (95%)** | **4–16** | **4000–16000** |
| ±3σ (99.7%) | 1–19 | 1000–19000 |

At a conservative 40% CV, the 95% window widens to roughly **2–18/µL (2×10³–1.8×10⁴/mL)**.

### Equivocal Zone Around the 1×10⁴/mL Threshold

| CV used | Confidently **below** 1×10⁴/mL | Confidently **above** 1×10⁴/mL | Indeterminate zone |
| --- | --- | --- | --- |
| 20% (near LoQ) | < 7200/mL | > 16400/mL | 7200–16400 |
| **30% (best estimate)** | **< 6300/mL** | **> 24300/mL** | **6300–24300** |
| 40% (low-end dilution) | < 5600/mL | > 46300/mL | 5600–46300 |

**Best single-number answer:** the indeterminate zone is approximately **6000–24000/mL**. Add systematic −20% bias → shift bounds up ~25% → roughly **7500–30000/mL displayed**.

---

## Sources

| Reference | DOI / URL |
| --- | --- |
| Wah, Wises, Butch 2005 — AJCP | 10.1309/VNGU9Q5V932D74NU |
| Linko et al. 2006 — Clin Chim Acta | 10.1016/j.cca.2006.03.015 |
| Butch et al. 2008 — AJCP | 10.1309/WR1C5WNT6UFXNC6J |
| Shayanfar et al. 2009 — AJCP | 10.1309/AJCPCHHTZ6UDQ6WF |
| Bakan et al. 2016 — Biochemia Medica | 10.11613/BM.2016.040 |

## Gaps

1. No data on iQ200 performance at [[uric-acid|uric acid]] or bilirubin concentrations (optical rather than cell-count analytes).
2. All studies use laboratory-grade instruments; POC performance may differ.
3. iQ200 uses flow cytometry; Jimini's optical spectroscopy approach requires separate precision characterization.

[white-blood-cells|WBC]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/white-blood-cells.md "White Blood Cells"
[red-blood-cells|RBC]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/red-blood-cells.md "Red Blood Cells"
[bacteria]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[optical-path-design]: ../optical-path-design.md "Optical Path Design for Pen-Form Spectrophotometry of Urine"
[white-blood-cells\|WBC]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/white-blood-cells.md "White Blood Cells"
[red-blood-cells\|RBC]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/red-blood-cells.md "Red Blood Cells"
[bacteria\|Bacteria]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[bacteria|Bacteria]: ../../biomarkers/papers/singleBiomarkers/sheets/infection-inflammation/bacteria.md "Bacteria (Bacteriuria)"
[uric-acid|uric acid]: ../../biomarkers/papers/singleBiomarkers/sheets/metabolites/uric-acid.md "Uric Acid"
