---
title: Urine Sample Pre-Analytics & Stability
aliases:
  - pre-analytics
  - urine pre-analytics
  - urine stability
  - pre-analytical requirements
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---
/sync
# Urine Sample Pre-Analytics & Stability

Jimini pen-sized LED spectrophotometer (275/365/405/455 nm + white + 1070 nm NIR + EIS) for reagent-free urinalysis.
Analyte panel: WBC, RBC, BAC, epiCells, crystals, creatinine, osmolality, TUP, PBG, bilirubin, uric acid, NADH, protein, nitrites, sodium, chloride. 20+ sources synthesized.
See also: [[biomarker-panel]] [[optical-signatures]] [[signal-processing]]

---

## The Core Problem: Urine Is Unstable

Urine is a biologically active matrix. After voiding it undergoes simultaneous degradation processes:
- **Bacterial metabolism** — growth, urease activity, pH shift
- **Oxidation** — light-driven and spontaneous oxidation of chromophores
- **Enzymatic activity** — cell autolysis, proteases
- **Physical-chemical equilibria** — crystal precipitation on cooling, pH-dependent solubility

The European urinalysis guidelines (ECLM, 2000) state:

> *"Particles should be examined < 1 hour after voiding at ambient temperature, or < 4 hours if refrigerated."*

CLSI GP16-A3 / PRE05 is slightly more permissive for chemical analytes: **< 2 hours at room temperature** without preservative.

For Jimini — which measures both cellular and chemical analytes — the more stringent **1-hour rule for particles** is the binding constraint.

---

## Analyte-by-Analyte Stability

### Red Blood Cells (RBC / Erythrocytes)

RBCs lyse progressively due to osmotic stress (hypotonic urine) and proteolysis. Lysis releases free hemoglobin: Soret peak shifts from ~415 nm (intact RBC oxyhemoglobin) toward ~405 nm (free hemoglobin/methemoglobin), and scatter decreases as cells dissolve.

**Stability:**
- RT (20–25°C): 1 h (hypotonic urine, pH > 7.5) to 24 h (hypertonic, pH < 6.5). Mean ~2–4 h.
- 4–8°C: 1–4 h.
- Lysis accelerators: pH > 7.5, osmolality < 200 mOsm/kg, delay > 2 h at RT.

**Spectroscopic consequence:** Delayed measurement shows reduced scatter (A_1070) and shifted Soret ratio (A_405/A_415). RBC models trained on fresh samples give false negatives on aged samples. Liberated hemoglobin absorbs at 405 nm — can falsely elevate TUP/porphyrin estimates.

---

### White Blood Cells (WBC / Leukocytes)

WBCs are more fragile than RBCs. Lysis driven by alkaline pH (>7.5 from bacterial urease), dilute urine (osmolality <200 mOsm/kg), or temperature >25°C.

**Stability:**
- RT: 1 h (pH > 7.5) to 24 h (pH < 6.5).
- 4–8°C: ~1 day.

**Spectroscopic consequence:** WBC lysis reduces turbidity (scatter ↓). NADH autofluorescence may transiently increase after lysis (intracellular contents released) then decay. Models must be trained on consistently-timed samples.

---

### Bacteria

Bacteria multiply exponentially at room temperature using urine nutrients (amino acids, glucose, urea).

**Growth rates:**
- UPEC (E. coli) doubling time: ~20–40 min at 37°C; ~60–90 min at ~22°C RT.
- At RT: bacteria can increase >10-fold in **2 hours** (e.g., 10³ → 10⁵ CFU/mL — crossing the "significant bacteriuria" threshold, producing a false-positive UTI result).
- At 4°C: ~10× slower; stable 24 h per most guidelines.

**Spectroscopic consequence:** Scatter (A_1070) increases over time from bacterial growth even in samples with no initial clinical bacteriuria. Flavin/NADH fluorescence also increases. **The bacterial scatter signal is more time-dependent than any other analyte.**

---

### Bilirubin

Bilirubin is highly photosensitive. UV and visible light (especially 420–500 nm) catalyze photoisomerization to lumirubin and oxidation to biliverdin and colorless products.

**Stability:**
- In serum at room lighting: ~50% loss in 1–2 hours. Urine bilirubin likely more photolabile (lower protein binding).
- Light wavelength dependency: Blue/green (420–520 nm) is most efficient — exactly the range of Jimini's 405 nm and 455 nm LEDs.
- In darkness at RT: ~8 h stable. At 4°C in dark: 24 h.

**Spectroscopic consequence:**
1. Repeated 405/455 nm LED exposures photodegrade bilirubin between measurements.
2. Sample aging in room light degrades bilirubin before measurement.
3. **Protocol implication:** Measure bilirubin-related signals on the FIRST LED flash; keep sample in dark before measurement.

---

### Porphobilinogen (PBG) and Porphyrins (TUP)

PBG spontaneously polymerizes to uroporphyrinogen, which oxidizes to uroporphyrin (fluorescent porphyrin):

```
PBG → uroporphyrinogen (polymerization; slow at low pH, fast at neutral-alkaline pH)
     → uroporphyrin (oxidation; catalyzed by light)
```

**Stability:**
- Stable in acid urine (pH 3–5) at 4°C for ≥ 24 h.
- At neutral-alkaline pH, RT: significant PBG loss within 4–8 h; in light, <2 h.
- Pre-formed porphyrins: photolabile, degrade in <2 h in light.

**Spectroscopic consequence:** PBG→porphyrin conversion IS the signal for the TUP measurement (Soret at 405 nm, fluorescence ex405/em620). Aged samples give **false-positive TUP elevation** from PBG conversion even without pathology. **Measure within 30 min of collection; use amber/opaque containers.**

---

### Urobilinogen

Urobilinogen oxidizes to urobilin (brown/orange) under light and air.

**Stability:**
- At 2–8°C in dark: 24 h.
- At RT in room light: significant oxidation within 2 h.

**Spectroscopic consequence:** Urobilinogen absorbs broadly 430–500 nm; oxidation product urobilin has a shifted absorption profile. Aged samples confound bilirubin models using 455 nm.

---

### Hemoglobin: OxyHb → MetHb Conversion

Free hemoglobin (from RBC lysis) undergoes autoxidation:
- OxyHb (Fe²⁺-O₂, red) → MetHb (Fe³⁺, brown) over hours

**Spectral shift:**
- OxyHb Soret: ~415 nm; Q-bands at 541 nm and 576 nm (doublet)
- MetHb Soret: ~405 nm; broad Q-band at 630 nm (single peak); loss of 576 nm doublet

**Half-life:** OxyHb autoxidation at 37°C ~3–6 h; at 22°C ~12–24 h.

**Spectroscopic consequence:** A model trained on fresh (OxyHb-dominated) samples will misclassify aged samples where MetHb dominates. **The 541/576 nm Q-band doublet can be used as a freshness quality indicator:**

```
Q-band doublet (541 nm + 576 nm) present → OxyHb dominant → Fresh sample
Single Q-band at 630 nm → MetHb dominant → Delayed > 4 h at RT
```

---

### NADH

NADH is oxidized to NAD⁺ by dissolved oxygen; degraded by alkaline hydrolysis (pH > 8).

**Stability:** Half-life in aqueous solution at RT ~1–4 h. Even less in urine. **NADH is one of the most time-sensitive analytes for spectroscopy.**

**Spectroscopic consequence:** NADH fluorescence ex365/em460 decays over time. Measurements delayed >1 h underestimate NADH content.

---

### Other Analytes — Stability Summary

| Analyte | RT stability | Notes |
|---|---|---|
| **Uric acid** | ≥ 4 h | Crystal precipitation at 4°C; warm and mix before measuring |
| **Creatinine** | > 24 h | Very stable; can use stored samples |
| **Protein** | ~8 h | Proteolysis by bacteria only at extended delay |
| **Nitrites** | 4 days at RT | False positive risk if bacteria produce nitrites in vitro |
| **Glucose** | < 2 h | Bacterial/enzymatic consumption |

---

## Master Stability Table

### Particle/Cellular Analytes

| Analyte | 20–25°C (no preservative) | 4–8°C | Critical mechanism | Spectral consequence |
|---|---|---|---|---|
| **RBC** | 1 h (dilute/alk) – 24 h (conc/acid) | 1–4 h | Osmotic lysis, proteolysis | Soret shifts 415→405 nm; scatter ↓ |
| **WBC** | 1 h (pH > 7.5) – 24 h (pH < 6.5) | ~1 day | pH-driven lysis, osmotic | Scatter ↓; fluorescence transiently ↑ then ↓ |
| **Bacteria** | **1–2 h** (start of significant growth) | 24 h | Exponential replication | Scatter ↑; flavin fluorescence ↑ |
| **Epithelial cells** | ~3 h | Not studied | Lysis | Scatter ↓ |
| **Casts** | ~2 days | Not allowed (freeze) | Mechanical fragility | — |
| **Crystals** | Variable | Precipitate ↑ on cooling | Solubility equilibrium | Scatter ↑ on cooling; dissolve on warming |

### Chemical/Spectral Analytes

| Analyte | 20–25°C (dark) | 20–25°C (light) | 4–8°C (dark) | Mechanism | Jimini priority |
|---|---|---|---|---|---|
| **Bilirubin** | ~8 h | **< 1–2 h** | 24 h | Photodegradation to lumirubin/biliverdin | ⚠️ Measure first, in dark |
| **PBG** | 4–8 h (neutral pH) | **< 2 h** | ≥ 24 h (acid, dark) | Polymerization to porphyrins; light oxidation | ⚠️ Amber tube; measure <30 min |
| **Porphyrins (TUP)** | 4–8 h | **< 2 h** | 24 h | Photodegradation | ⚠️ Amber tube; measure promptly |
| **Urobilinogen** | ~2 h | **< 1 h** | 24 h | Oxidation to urobilin | Protect from light |
| **NADH** | ~1–4 h | ~1 h | 8–12 h | Oxidation to NAD⁺ | Measure within 1 h |
| **OxyHb → MetHb** | 12–24 h | Faster | Stable days | Autoxidation | Relevant after 4+ h |
| **Uric acid** | ≥ 4 h | ≥ 4 h | > 24 h | Stable | Low urgency |
| **Creatinine** | > 24 h | > 24 h | Days | Very stable | Low urgency |
| **Protein** | ~8 h | ~8 h | 24–48 h | Proteolysis (late) | Low urgency |
| **Nitrites** | 4 days | 4 days | 8 h | Stable (in vitro BAC production later) | Moderate |
| **Glucose** | **< 2 h** | < 2 h | 2 h | Bacterial/enzymatic consumption | Not Jimini target |

---

## Temperature Effects

| Temperature | Bacterial growth | Cell lysis | Chemical stability | Recommended? |
|---|---|---|---|---|
| **37°C** | Very fast (doubling ~20–40 min) | Accelerated | Fast degradation | Never |
| **20–25°C (RT)** | Moderate (doubling ~60–90 min) | Moderate | Moderate (varies) | Only if measured within **1–2 h** |
| **4–8°C (refrigerated)** | Slowed (~10× vs RT) | Slowed | Stable for most analytes 24 h | If delay > 2 h |
| **−20°C (frozen)** | Halted | Complete cellular disruption | Good for chemical; bad for particles | Not for particles |

**Jimini-specific note:** Point-of-care device — assume room temperature conditions. Target measurement window: **< 1 hour for cellular analytes; < 2 hours for chemical analytes.**

Continuous catheter monitoring (as in Kuenert 2025): bacterial growth is ongoing at body temperature; measurements must account for biochemical changes in the catheter bag.

---

## Light Exposure Effects

| Analyte | Sensitive wavelengths | Half-life in room light | Protection needed |
|---|---|---|---|
| **Bilirubin** | 400–500 nm (peak ~460 nm) | ~1–2 h | Amber container; dark room |
| **PBG** | 300–450 nm (accelerates polymerization) | 2–4 h | Amber container |
| **Porphyrins (TUP)** | 400–420 nm (Soret excitation) | 1–4 h | Amber container |
| **Urobilinogen** | 400–500 nm | ~1 h | Amber container |
| **NADH** | 340–365 nm | ~1–4 h (mixed oxidation + light) | Minimize UV exposure |
| **Uric acid** | Not photosensitive | — | No special precaution |
| **Creatinine** | Not photosensitive | — | No special precaution |

### Jimini Measurement as a Photodegradation Source

Each LED exposure degrades photosensitive analytes. The 405 nm LED is particularly efficient at porphyrin Soret excitation and bilirubin photodegradation.

**Quantification:** Single-exposure degradation is negligible (<0.1% per flash at typical LED power). Sequential multi-LED sweeps (10 exposures × 4 LEDs) accumulate ~1% bilirubin degradation — acceptable for single sessions, problematic for continuous monitoring.

**Recommendation:** Single measurement sweep is safe. For bilirubin: measure on the FIRST 455 nm LED flash; avoid repeated exposures.

---

## pH Drift and Its Cascade Effects

**The urease cascade** is the most clinically important pre-analytical artifact:

```
Urease-producing bacteria (Proteus, Klebsiella, Pseudomonas)
  ↓ urease enzyme
  urea → NH₃ + CO₂
  ↓
  NH₃ dissolves: NH₄⁺ + OH⁻ → pH rises (5 → 7 → 8 → 9)
  ↓ consequences:
  1. WBC and RBC lysis (accelerated above pH 7.5)
  2. Phosphate crystal formation (struvite, triple phosphate)
  3. Uric acid crystals dissolve (uric acid soluble above pH 7)
  4. PBG polymerization accelerated (PBG more stable at low pH)
  5. Nitrite test false positive (in vitro nitrite production by bacteria)
  6. Protein test false positive (alkaline pH causes false-positive colorimetric protein)
```

Urease-producing bacteria can raise pH from 5.5 to >8 within **1–2 hours** at room temperature.

> [!WARNING]
> E. coli (most common UTI pathogen) does NOT produce urease. The alkaline shift occurs specifically with Proteus/Klebsiella/Pseudomonas infections and creates a cascade of simultaneous spectral artifacts.

---

## Preservatives

No single preservative preserves all analytes simultaneously.

| Preservative | Bacteria | WBC | RBC | Bilirubin | Porphyrins | Notes |
|---|---|---|---|---|---|---|
| **Refrigeration (4°C)** | Slowed | ✅ | ✅ | ✅ (+ dark) | ✅ (+ dark) | Best general option |
| **Boric acid (1.8%)** | Inhibited | ✅ | Variable | — | ✅ (pH kept low) | Interferes with LE/nitrite strip tests |
| **Borate + formate + sorbitol** (BD C&S, Stabilur) | ✅ | ✅ (6–24 h) | ✅ | — | — | Best commercial option |
| **Formaldehyde (10 mL/L)** | ✅ | ✅ | Poor | — | — | Lowers pH; disrupts LE test |
| **None + dark + 4°C** | Slowed | ✅ short-term | ✅ short-term | ✅ dark | ✅ dark | Sufficient for < 2 h |

### Spectroscopic Interference of Preservatives

| Preservative | Spectral interference |
|---|---|
| **Boric acid** | Weak UV absorption; pH-shifted urobilinogen/bilirubin equilibria |
| **Formaldehyde** | Strong UV absorption at ~270 nm — **directly interferes with uric acid/protein at 275 nm** |
| **Sodium azide** | Absorbs at ~270 nm — UV measurement interference |
| **Ethanol** | Strong UV absorption; completely disrupts 275 nm measurements |

> [!IMPORTANT]
> For Jimini spectroscopic samples: avoid all chemical preservatives. **Refrigeration at 4°C in the dark** is the only non-interfering option when delay is unavoidable.

---

## Clinical Guidelines Summary

| Category | CLSI GP16-A3 | ECLM | Jimini recommendation |
|---|---|---|---|
| **Particle analysis (WBC, RBC, bacteria)** | < 2 h RT | **< 1 h RT**, < 4 h refrigerated | < 1 h at RT |
| **Chemical analysis (bilirubin, protein, etc.)** | < 2 h RT | < 2 h RT | < 2 h at RT |
| **Light-sensitive (bilirubin, urobilinogen, PBG, TUP)** | Protect from light | Amber containers | Dark container; measure first |
| **Refrigeration** | 2–8°C if delay > 2 h | 2–8°C if delay > 1 h | 2–8°C if delay > 1 h |
| **No preservative needed if...** | Analyzed < 2 h at RT | Analyzed < 1 h at RT | Analyzed < 1 h |

---

## Jimini-Specific Implications

### Time Budget Per Analyte

| Analyte | Hard deadline (RT, no preservative) | Risk of delay |
|---|---|---|
| **Bacteria (BAC)** | **1–2 h** | Overcount — false positive UTI |
| **PBG / TUP** | **< 30 min** ideally; **< 1 h** maximum | False positive TUP from PBG conversion |
| **Bilirubin** | **< 1 h in room light** | Undercount |
| **NADH** | **< 1 h** | Undercount |
| **Urobilinogen** | **< 2 h** in light | Undercount |
| **RBC** | 1–4 h (urine-dependent) | False negative + MetHb spectral shift |
| **WBC** | 1–4 h (pH-dependent) | False negative |
| **epiCells** | ~3 h | False negative |
| **Crystals** | Variable; refrigeration causes artifacts | Overcounting after cooling |
| **Uric acid** | > 4 h | Low urgency |
| **Creatinine** | > 24 h | No concern |
| **Osmolality** | > 24 h (ionic strength stable) | No concern |
| **Protein** | ~8 h | Low urgency |

### The PBG-TUP Temporal Confound

In acute porphyria patients:
- Fresh sample: high PBG → low TUP (PBG not yet converted)
- Sample after 2–4 h at RT: PBG → uroporphyrin → rising Soret + fluorescence

TUP measured on delayed samples overestimates "true" porphyrins, artificially mimicking porphyria. To distinguish PBG from pre-formed porphyrins, a second measurement on an acidified/fresh aliquot is required.

### Bacterial Growth as a Confound for All Particulate Analytes

In a sample with bacteriuria, bacteria grow continuously from collection to measurement. After 2 h at RT, scatter is NOT representative of the original void.

**Recommendation:** Timestamp every sample. Build time-from-collection as a feature in the ML pipeline. Stratify training data by collection-to-measurement delay.

### Crystal Artifact from Refrigerated Samples

If samples are refrigerated during transport, uric acid and phosphate crystals may precipitate. Warming to 37°C and mixing before measurement is necessary for accurate crystal analysis.

---

## Recommended Measurement Protocol

### Optimal Protocol for Jimini (Point-of-Care Use)

```
Collection:
  → Midstream clean-catch, first morning urine preferred for WBC/RBC
  → Use opaque/amber container for PBG/TUP/bilirubin-critical tests
  → Record collection time

Within 10 minutes:
  → Begin Jimini measurement
  → Measure light-sensitive analytes on FIRST exposure (bilirubin → 455 nm)
  → Perform all LEDs in a single sweep; minimize repeated exposures

Within 30 minutes:
  → Complete all measurements for PBG/TUP
  → After 30 min, PBG conversion begins producing artifact TUP signal

Within 1 hour:
  → All particle-based measurements (WBC, RBC, bacteria, crystals) valid
  → Chemical analytes (bilirubin, NADH, urobilinogen) still reliable

1–2 hours:
  → Chemical analytes still usable with caution
  → Bacteria count beginning to increase; flag if > 1 h

> 2 hours at room temperature:
  → WBC/RBC counts unreliable (lysis in alkaline/dilute urine)
  → Bacteria count unreliable (10× or more overgrowth)
  → Flag measurement as out-of-protocol; report with caveat
  → Only creatinine/osmolality/uric acid remain reliable
```

### ML Data Collection Protocol

For building robust Jimini models, training data should include:
1. **Time-from-collection label** on each sample
2. **Samples measured at 0, 30, 60, 120 min** from the same void — to characterize degradation curves
3. **pH at time of measurement** — flags urease-driven cascade
4. **Storage temperature** — room temp vs refrigerated
5. **Light exposure** — dark container vs standard container

This enables the model to apply time-based correction factors, use time-from-collection as an input feature, or flag out-of-protocol samples for review.

---

## Sources

| Source | Reference |
|---|---|
| Delanghe & Speeckaert, *Biochemia Medica* 2014 — Preanalytical requirements of urinalysis | PMC3936984 |
| BMC Nephrology 2024 — Changes in urine composition over six hours | bmcnephrol.biomedcentral.com |
| SIPMEL — Stability of urine particles at room temperature | sipmel.it |
| CLSI GP16-A3 / PRE05 | clsi.org |
| European Confederation of Laboratory Medicine Urinalysis Guidelines (2000) | Scand J Clin Lab Investig 60:1–96 |
| Sysmex — Effect of delay on urine particle analysis | sysmex.co.jp |
| Rehak et al. 2007 — Photolysis of bilirubin in serum | PMC2131702 |
| Bossenmaier et al., *Clinical Chemistry* 1968 — Stability of ALA and PBG in urine | academic.oup.com/clinchem |
| European Porphyria Network — Laboratory diagnosis | porphyria-europe.org |
| Clinlabint — Analyte stability for porphyrins and precursors | clinlabint.com |
| Rosen et al., CMR 2020 — UPEC growth and metabolism in urine | ASM CMR DOI: 10.1128/cmr.00101-19 |
| Meng et al., PMC5303181 — Extinction coefficients of hemoglobin redox forms | PMC5303181 |
| Mobley & Warren 1987 — Urease and long-term catheter obstruction | J Clin Microbiol 25:2216 |
| Griffith et al. 1976 — Urease: primary cause of infection-induced urinary stones | Investig Urol 13:346 |

## Gaps

- Exact Jimini LED exposure dose per measurement not characterized (needed for photodegradation risk quantification)
- Pediatric sample stability data sparse; adult thresholds used throughout
- Crystal dissolution kinetics on warming from refrigeration not quantified for Jimini sample protocol
- NADH concentration levels in normal urine before/after cell lysis not well characterized in the literature
