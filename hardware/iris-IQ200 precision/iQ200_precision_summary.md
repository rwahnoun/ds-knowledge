# Iris / Beckman Coulter iQ200 — Precision & Accuracy Summary

Reference sources collected for WBC, RBC, and bacteria counting error
at low concentrations (~1e4 cells/mL ≈ 10 cells/µL ≈ 10 × 10⁶/L).

## Unit reminder

The iQ200 reports cells in **particles/µL** (equivalent to **× 10⁶/L**).
`1 × 10⁶ /L = 1 /µL = 1 000 /mL`.
So **1e4 /mL = 10 /µL = 10 × 10⁶/L** — this is the regime the user is asking about.
It sits right at / just below the clinical upper-limit-of-normal for WBC
(17–28 /µL depending on the reference), i.e. at the bottom of the analyzer's quantitative range.

## Headline numbers at ~10/µL (= 1e4 /mL)

| Particle | Within-run CV near 10–20/µL | Source |
| --- | --- | --- |
| **WBC** | **22–40 %** (reaches ~40 % at ~5/µL, ~12 % at ~30/µL) | Wah 2005 Fig 1B + Table 2 |
| RBC | 25–45 % (~45 % at ~5/µL, ~14 % at ~36/µL) | Wah 2005 Fig 1A + Table 2 |
| Epithelial | 18–35 % | Wah 2005 Table 2 |
| Bacteria | ~30 % at ~46 /µL | Linko 2006 Table 3 |

**Bottom line for the user's question** — at **1e4 WBC/mL (≈10/µL)** the iQ200
is close to its lower limit of quantitation. Expected within-run imprecision
is ≈ **25–40 % CV**. The manufacturer / literature–accepted lower detection
limit (defined as CV ≤ 20 %) is **~18 × 10⁶ WBC/L ≈ 18/µL ≈ 1.8e4 /mL**
(Wah 2005; Butch 2008).

---

## 1. Wah, Wises, Butch 2005 — AJCP (DOI 10.1309/VNGU9Q5V932D74NU)

`2005-Analytic-Performance-of-the-iQ200-Automated-Urine-Microscopy-Analyzer-and-Compar.pdf`

Within-run imprecision (n = 20 replicates, 5 samples per range):

| Cell | Mean (× 10⁶/L) | CV (%) |
| --- | --- | --- |
| RBC | 786 – 1 029 | 3.0 – 5.6 |
| RBC | 253 – 356 | 3.4 – 8.4 |
| RBC | 100 – 145 | 4.2 – 13.5 |
| RBC | 17 – 20 | 14.0 – 29.6 |
| **WBC** | 794 – 1 006 | 2.4 – 3.4 |
| **WBC** | 258 – 380 | 4.5 – 6.7 |
| **WBC** | 79 – 115 | 3.1 – 15.3 |
| **WBC** | **16 – 30** | **12.6 – 22.3** |
| Epithelial | 59 – 93 | 8.9 – 14.8 |
| Epithelial | 13 – 22 | 18.1 – 31.3 |

Further low-count dilution study (Fig 1): CV ≈ 40 % for WBC at ~5/µL,
approaching 45 % for RBC at the lowest dilution.
**"CVs of approximately 20 % were found at RBC, WBC and EC
concentrations of 25, 18 and 21 × 10⁶/L, respectively."**

Between-run (glutaraldehyde-fixed RBC, duplicate × 12 days):

| Mean (× 10⁶/L) | CV (%) |
| --- | --- |
| 1017 | 3.3 |
| 802 | 4.8 |
| 443 | 7.2 |
| 155 | 7.4 |
| 28 | 19.2 |

Correlation vs Fuchs-Rosenthal chamber (n = 166):
- RBC: y = 0.92 x – 2.94, r = 0.959
- WBC: y = 0.81 x – 3.20, r = 0.940 (iQ200 mean 24.7 % lower)
- EC : y = 0.94 x + 0.34, r = 0.951

Agreement above clinical cut-off (28 × 10⁶/L for WBC):
normal 96.7 %, abnormal 76.7 %.

Linearity: RBC to 1 000 × 10⁶/L, WBC to 900 × 10⁶/L. Carry-over ≤ 0.2 %.

## 2. Linko, Kouri, Toivonen, Ranta, Chapoulaud, Lalla 2006 — Clin Chim Acta (DOI 10.1016/j.cca.2006.03.015)

`2006-Analytical-performance-of-the-Iris-iQ200-automated-urine-microscopy-analyzer.pdf`

Within-run precision, Table 3:

| Particle | Mean (× 10⁶/L) | Observed CV (%) | Theoretical Poisson CV (%) |
| --- | --- | --- | --- |
| RBC-low | 12.25 | 32.6 | 20.2 |
| RBC-high | 1 246 | 6.2 | 2.0 |
| **WBC-low** | **114.9** | **10.4** | 6.6 |
| WBC-high | 464.6 | 4.0 | 3.3 |
| SQEP | 6.35 | 48.4 | 28.1 |
| NSE | 6.65 | 32.4 | 27.4 |
| **Bacteria** | **45.9** | **30.0** | 14.8 |
| Yeast | 32.7 | 25.1 | 12.4 |

Key statement: **"Lower limit of quantification with iQ200 was about
20 – 30 particles × 10⁶/L when using a criterion of between-day
repeatability CV < 30 %."**

Correlation vs phase-contrast Bürker chamber (after reclassification):
- RBC r = 0.948 (APR alone 0.894)
- WBC r = 0.978 (APR alone 0.885)
- SQEP r = 0.927
- Casts r = 0.856
- NSE r = 0.706
- Bacteria: sensitivity 42.9 % APR alone, 64.3 % after reclassification,
  specificity 96.4 → 97.0 %.

Linearity 0 – 1000 × 10⁶/L, R² = 0.9874 – 0.9987. No carry-over.

## 3. Butch, Wises, Wah, Gornet, Fritsche 2008 — AJCP (DOI 10.1309/WR1C5WNT6UFXNC6J)

`2008-A-Multicenter-Evaluation-of-the-Iris-iQ200-Automated-Urine-Microscopy-Analyzer-B.pdf`

Body-fluids module (CSF, serous fluid) — 350 specimens, 3 sites.

Within-run imprecision:
- RBC 2.6 – 5.9 % at 875 and 475 × 10⁶/L
- Nucleated cells 4.2 – 6.5 % at 820 and 590 × 10⁶/L

Between-run imprecision (10 days, body-fluid control):
- RBC 7.6 % (24 586 × 10⁶/L) and 4.6 % (49 766 × 10⁶/L)
- Nucleated 8.3 % (1 675 × 10⁶/L) and 10.3 % (2 787 × 10⁶/L)

**Lower detection limit (CV ≤ 20 %): 30 × 10⁶/L for RBC, 35 × 10⁶/L
for nucleated cells** (body fluid). Corresponding urine figures from
the 2005 study: 25 × 10⁶/L (RBC), 18 × 10⁶/L (WBC).

CSF agreement at clinical cut-offs (RBC 10, nucleated 5 × 10⁶/L):
- RBC: normal 93 %, abnormal 94.6 %
- Nucleated: normal 72 %, abnormal 82.4 %
  (poor at very low CSF counts — confirmed limitation for CSF).

## 4. Shayanfar, Tille, Sutton, Fritsche 2009 — CSF reliability (DOI 10.1309/AJCPCHHTZ6UDQ6WF)

`2009-The-Clinical-Reliability-of-Automated-Cerebrospinal-Fluid-Cell-Counts-on-the-Bec.pdf`

CSF comparison of LH750 vs iQ200 vs manual.
Reliability coefficient 0.84 for iQ200 nucleated-cell counts in CSF;
unacceptable error rates at counts < 50/µL — reinforces that the
iQ200 is not precise enough for CSF where normal nucleated count is
≤ 5/µL.

## 5. Bakan, Ozturk et al. 2016 — Biochemia Medica (DOI 10.11613/BM.2016.040)

`2016-BM-Cobas-vs-iQ200-Zaman.pdf` — open access, n = 540.

Diagnostic performance vs manual microscopy (clinical cut-offs):

| Parameter | Sensitivity | Specificity | PPV | NPV |
| --- | --- | --- | --- | --- |
| **WBC (iQ200)** | 92 % | 71 % | 83 % | 75 % |
| RBC (iQ200) | 90 % | 63 % | 65 % | 76 % |

Correlation with manual: WBC r = 0.81, RBC r = 0.65, SEC r = 0.70,
NEC r = 0.14 (NS), crystals r = 0.67.

Authors' conclusion: **"still inadequate in the determination of WBC,
RBC and EC in highly-pathological samples; confirmation by manual
microscopy may be useful."**

---

## Practical implications at 1e4 cells/mL (= 10/µL) WBC

1. This concentration **sits below the analyzer's CV ≤ 20 % threshold**
   (~18/µL for WBC, Wah 2005; Butch 2008).
2. Expected **single-run error is 25 – 40 % CV**; duplicate averaging
   improves this by √2 only.
3. At this level the iQ200 tends to **under-count WBC by ~20–25 %**
   (slope 0.81 vs Fuchs-Rosenthal — Wah 2005).
4. Counts in this regime are **clinically close to the upper-limit-of-
   normal decision point** (17–28/µL), so error bars often straddle
   the cut-off → **manual confirmation is the literature-standard
   recommendation** (Bakan 2016, Butch 2008).
5. RBC at the same regime: CV ~ 25–45 %.
6. Bacteria: semiquantitative only; APR-alone sensitivity ≈ 43 %
   improves to ≈ 64 % after trained-tech reclassification (Linko 2006).

## If the user meant 1e4 /µL instead of 1e4 /mL

10 000 /µL = 10⁷ /µL — **beyond the documented linearity range**
(WBC linear to 900 × 10⁶/L = 900/µL; RBC to 1 000/µL).
Results above the upper linearity require sample dilution.

---

## Uncertainty window at a measured value of 1e4 WBC/mL (= 10/µL)

From the Wah 2005 low-count curve (Fig 1B), within-run CV ≈ 28–30 %
at mean WBC ≈ 10/µL (interpolating between ≈ 40 % at 5/µL and
≈ 22 % at 18/µL).

Using CV = 30 %, SD ≈ 3 /µL on a single read:

| Confidence | Window (cells/µL) | Window (cells/mL) |
| --- | --- | --- |
| ±1 σ (68 %) | 7 – 13 | 7 000 – 13 000 |
| **±2 σ (95 %)** | **4 – 16** | **4 000 – 16 000** |
| ±3 σ (99.7 %) | 1 – 19 | 1 000 – 19 000 |

Using the more conservative 40 % CV from the very-low-count dilution
series, the 95 % window widens to roughly **2 – 18 /µL
(2e3 – 1.8e4 /mL)**.

Plus a systematic bias: the iQ200 under-reads by ~20 % vs
Fuchs-Rosenthal (slope 0.81, Wah 2005). A displayed 10/µL is best
read as a *true* manual count of ~12 /µL, with the statistical
window above superimposed.

**Practical read**: at 1e4 /mL a single iQ200 run cannot distinguish
a true value between **~4 000 and ~16 000 /mL**. The window straddles
the upper-limit-of-normal decision point (17–28 /µL). Duplicate
averaging shrinks this by √2 only.

---

## Equivocal / indeterminate zone around the 1e4 /mL threshold

Turning the question around: for what range of *displayed* values
can we not decide whether the true concentration is above or below
10/µL?

A displayed value `X` is only confidently on one side of the threshold
when its 95 % CI (`X ± 1.96·CV·X`) clears 10/µL.

| CV used | Confidently **below** 1e4 /mL | Confidently **above** 1e4 /mL | Indeterminate zone |
| --- | --- | --- | --- |
| 20 % (optimistic, near LoQ) | < 7 200 /mL | > 16 400 /mL | 7 200 – 16 400 |
| **30 % (best estimate at 10/µL)** | **< 6 300 /mL** | **> 24 300 /mL** | **6 300 – 24 300** |
| 40 % (low-end dilution data) | < 5 600 /mL | > 46 300 /mL | 5 600 – 46 300 |

**Best single-number answer: the zone where a single iQ200 reading
cannot tell you whether the true value is above or below 1e4 /mL
is approximately 6 000 – 24 000 /mL.**

Outside that window (below ~6e3 or above ~2.4e4 /mL) the 95 % CI no
longer crosses the 1e4 line.

Caveat — add the systematic −20 % bias (slope 0.81 vs manual). If
your decision threshold refers to the *true* (manual-equivalent)
value, shift both bounds up by ~25 % → roughly
**7 500 – 30 000 /mL displayed**.
