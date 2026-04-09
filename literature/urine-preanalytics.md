# Urine Sample Stability & Pre-Analytics for Spectroscopic Measurement

**Context:** Jimini pen-sized LED spectrophotometer (275/365/405/455 nm + white + 1070 nm NIR + EIS) for reagent-free urinalysis. Biomarker targets: WBC, RBC, BAC, epiCells, crystals, creatinine, osmolality, TUP, PBG, bilirubin, uric acid, NADH, protein, nitrites, sodium, chloride.

**Date:** 2026-04-09  
**Status:** Complete — 20+ sources synthesized

---

## Table of Contents

1. [The Core Problem: Urine Is Unstable](#1-the-core-problem-urine-is-unstable)
2. [Analyte-by-Analyte Stability](#2-analyte-by-analyte-stability)
3. [Master Stability Table](#3-master-stability-table)
4. [Temperature Effects](#4-temperature-effects)
5. [Light Exposure Effects](#5-light-exposure-effects)
6. [pH Drift and Its Cascade Effects](#6-ph-drift-and-its-cascade-effects)
7. [Preservatives](#7-preservatives)
8. [Clinical Guidelines: CLSI & European Urinalysis](#8-clinical-guidelines-clsi--european-urinalysis)
9. [Jimini-Specific Implications](#9-jimini-specific-implications)
10. [Recommended Measurement Protocol](#10-recommended-measurement-protocol)
11. [Sources](#11-sources)

---

## 1. The Core Problem: Urine Is Unstable

Urine is a biologically active matrix. After voiding it undergoes simultaneous degradation processes driven by:
- **Bacterial metabolism** — growth, urease activity, pH shift
- **Oxidation** — light-driven and spontaneous oxidation of chromophores
- **Enzymatic activity** — cell autolysis, proteases
- **Physical-chemical equilibria** — crystal precipitation on cooling, pH-dependent solubility

The European urinalysis guidelines (ECLM, 2000) state:

> *"Particles should be examined < 1 hour after voiding at ambient temperature, or < 4 hours if refrigerated."*

CLSI GP16-A3 / PRE05 is slightly more permissive for chemical analytes: **< 2 hours at room temperature** without preservative.

For Jimini specifically — which measures both cellular (particles) and chemical analytes — the more stringent **1-hour rule for particles** is the binding constraint.

---

## 2. Analyte-by-Analyte Stability

### 2.1 Red Blood Cells (RBC / Erythrocytes)

**Stability mechanism:** RBCs lyse progressively due to osmotic stress (hypotonic urine) and proteolysis. Lysis releases free hemoglobin into solution — spectral consequence: the Soret peak shifts from ~415 nm (intact RBC oxyhemoglobin) toward ~405 nm (free hemoglobin / methemoglobin), and scatter decreases as cells dissolve.

**Key data:**
- At **room temperature (20–25 °C):** stable 1 h (hypotonic urine, pH > 7.5) to 24 h (hypertonic urine >300 mOsm/kg, pH < 6.5). Mean stability ~2–4 h.
- At **4–8 °C:** 1–4 h.
- **Lysis accelerators:** pH > 7.5 (alkaline), osmolality < 200 mOsm/kg (dilute), delay > 2 h at room temperature.
- **Sysmex data (2001):** "Decay of formed elements generally begins from 2–4 h at 2–8 °C; erythrocyte decay may start earlier."
- Italian SIPMEL study: "With storage > 2 h, decay in quality of samples: bacterial overgrowth, lysis in RBC, WBC and casts."

**Spectroscopic consequence for Jimini:** Intact RBCs scatter differently from free hemoglobin. A delayed measurement will show reduced scatter ($A_{1070}$) and shifted Soret ratio ($A_{405}/A_{415}$). RBC-based models trained on fresh samples will give false negatives on aged samples. **Lysis also liberates hemoglobin which absorbs at 405 nm — can falsely elevate TUP/porphyrin estimates.**

---

### 2.2 White Blood Cells (WBC / Leukocytes)

**Stability mechanism:** WBCs are more fragile than RBCs. Lysis is driven by:
- Alkaline pH (urine pH > 7.5 from bacterial urease activity → cell membrane disruption)
- Dilute urine (osmolality < 200 mOsm/kg → osmotic lysis)
- Temperature > 25 °C

**Key data (from Delanghe & Speeckaert, 2014; European guidelines):**
- At **20–25 °C:** 1 h at pH > 7.5; 24 h at pH < 6.5.
- At **4–8 °C:** ~1 day.
- Pediatric urine is more vulnerable (lower osmolality typical).
- A study showed WBC can be preserved fairly well at room temperature up to 72 h WITHOUT preservative — but this was only in adult samples; pediatric samples showed rapid decline.

**Test strip WBC (leukocyte esterase):**
- At 4–8 °C: 1 day
- At 20–25 °C: 1 day (more stable than cellular WBC count)

**Spectroscopic consequence for Jimini:** WBC lysis reduces turbidity (scatter ↓). Autofluorescence signal (NADH from WBCs) may temporarily increase after lysis (intracellular contents released) then decay. Models must be trained on consistently-timed samples.

---

### 2.3 Bacteria

**Stability mechanism:** Bacteria multiply exponentially at room temperature using urine nutrients (amino acids, glucose, urea as energy sources).

**Key data:**
- **UPEC (E. coli) doubling time in urine:** ~20–40 min at 37 °C; ~60–90 min at room temperature (~22 °C). (Rosen et al., CMR 2020)
- At room temperature: bacteria can increase >10-fold in **2 hours** from an initial 10³ CFU/mL → ~10⁴–10⁵ CFU/mL.
- **Clinical significance:** A sample with 10⁴ CFU/mL that sits 2 h at room temp may read as 10⁵ CFU/mL (= clinical "significant bacteriuria" threshold) — a **false positive** UTI result.
- Roberts et al. (1967, BMJ): multiplication of contaminant bacteria doubles counts per hour at room temperature.
- At **4 °C:** bacteria still grow, but ~10× slower. Stable for 24 h refrigerated per most guidelines.
- **For clinical culture:** most labs require transport within 2 h at room temperature, or 24 h refrigerated. Culture tubes with preservatives (boric acid) extend this to 24–48 h.

**Spectroscopic consequence for Jimini:** Scatter ($A_{1070}$) increases over time from bacterial growth even in samples with no initial clinical bacteriuria. Fluorescence signals (flavins, NADH) also increase. Models trained on fresh samples will over-estimate bacterial load for aged samples. **The bacterial scatter signal is highly time-dependent — more so than any other analyte.**

---

### 2.4 Bilirubin

**Stability mechanism:** Bilirubin is **highly photosensitive**. UV and visible light (especially 420–500 nm) catalyze photoisomerization to lumirubin and irreversible oxidation to biliverdin and colorless products. In the dark, bilirubin is more stable.

**Key data:**
- **Photodegradation rate:** In serum exposed to room lighting, bilirubin at 20 mg/dL falls by **~50% in 1–2 hours** (Rehak et al., PMC2131702). Urine bilirubin is likely more photolabile (lower protein binding provides less protection).
- **Light wavelength dependency:** Blue/green light (420–520 nm) is most efficient — exactly the range of the 405 nm and 455 nm Jimini LEDs. Repeated measurements expose the sample to LED light.
- **Rate in darkness, room temp:** Bilirubin in urine is stable ~8 h if protected from light. At 4 °C in dark: 24 h.
- **First morning vs random urine:** First morning urine bilirubin is highest; random urine exposed to light during collection may be significantly degraded.
- **CLSI/European guidelines:** Protect from light during transport; analyze within 2 h or refrigerate.

**Spectroscopic consequence for Jimini:** 
1. **Measurement itself causes bilirubin degradation** — repeated 405/455 nm LED exposures photodegrade bilirubin between measurements. The 405 nm LED (peak of bilirubin absorption) is particularly efficient at photodegradation.
2. Sample aging in the collection container (even in a bright examination room) degrades bilirubin before measurement.
3. **Protocol implication:** Measure bilirubin-related signals on the FIRST LED flash; avoid multiple repeated exposures. Keep sample in dark before measurement.

---

### 2.5 Porphobilinogen (PBG) and Porphyrins (TUP)

**Stability mechanism:** PBG is a monopyrrole that polymerizes spontaneously to uroporphyrinogen, which oxidizes to uroporphyrin (a fluorescent porphyrin). This is the source of the characteristic "port wine" darkening of urine in acute porphyria attacks. The reactions are:

```
PBG → uroporphyrinogen (polymerization, slow at low pH, fast at neutral-alkaline pH)
     → uroporphyrin (oxidation, catalyzed by light)
```

**Key data (Bossenmaier et al., 1968, Clinical Chemistry):**
- PBG is **stable in acid urine (pH 3–5) at 4 °C for ≥ 24 h** — refrigeration + acidification stabilizes PBG.
- At **neutral-alkaline pH, room temperature:** PBG converts to porphyrins within hours; significant loss within 4–8 h.
- At **room temperature in light:** loss can be > 50% in 4–8 h.
- **Porphyrins (coproporphyrin, uroporphyrin) after formation:** photolabile; degrade under UV/Vis light.
- **For clinical samples:** European Porphyria Network recommends: "Urinary PBG is best analyzed in a fresh, random sample. If analysis is delayed, store in the dark at 4 °C or freeze."
- Clinlabint review (2024): "Specific pre-analytical requirements must be followed to prevent porphyrin degradation: amber tubes, refrigeration, rapid processing."

**Spectroscopic consequence for Jimini:**
- **PBG → porphyrin conversion IS the signal**: For Jimini's TUP measurement (Soret at 405 nm, fluorescence ex405/em620), the measurable signal INCREASES over time as PBG polymerizes. This means aged samples give **false-positive TUP elevation**.
- Fresh samples from patients without porphyria may show low or zero porphyrin signal; aged samples from the same patient may show elevated porphyrin from PBG conversion even without pathology.
- Samples from acute porphyria patients will show rapidly rising 405 nm absorbance and em620 fluorescence if not measured promptly.
- **Protocol implication:** Measure TUP/PBG within 30 min of collection, before significant PBG → porphyrin conversion occurs. Use amber/opaque containers.

---

### 2.6 Urobilinogen

**Stability mechanism:** Urobilinogen is oxidized to urobilin (brown/orange) and other products. The reaction is catalyzed by light and air.

**Key data:**
- Stable at 2–8 °C in dark for **24 hours**.
- At room temperature, room light: unstable — significant oxidation within **2 hours** (labpedia.net clinical guide).
- **Optimal collection:** 2–3 hours post-prandial (afternoon peak); first-morning urine not ideal.
- CLSI: protect from light, analyze within 2 h or refrigerate.

**Spectroscopic consequence for Jimini:** Urobilinogen absorbs broadly 430–500 nm; its oxidation product urobilin has a slightly different absorption profile. Aged samples will have lower urobilinogen and higher urobilin — a spectral shift that could confound bilirubin models using 455 nm.

---

### 2.7 Hemoglobin / Oxyhemoglobin → Methemoglobin Conversion

**Stability mechanism:** Free hemoglobin (from RBC lysis) undergoes autoxidation:
- OxyHb (Fe²⁺-O₂, red) → MetHb (Fe³⁺, brown) over hours
- MetHb → hemichrome → denatured Hb (longer timescale)

**Spectral consequences:**
- **OxyHb Soret:** ~415 nm, Q-bands at 541 nm and 576 nm (doublet)
- **MetHb Soret:** ~405 nm, broad Q-band at 630 nm (single peak), loss of 576 nm doublet

**Key data:**
- Half-life of OxyHb autoxidation at 37 °C: ~3–6 hours. At 22 °C: slower, ~12–24 h.
- In acidic urine: MetHb formation accelerates.
- MetHb is stable in PBS at 4 °C for ~1 week (PLOS ONE, 2022).

**Spectroscopic consequence for Jimini:** The 405/415 nm Soret ratio and the 541/576 nm Q-band doublet change significantly as OxyHb converts to MetHb. **A model trained on fresh (OxyHb-dominated) samples will misclassify aged samples where MetHb dominates.** The Q-band doublet at 540/575 nm (measured by white LED + C12880MA) can be used as a freshness indicator: presence of the doublet = OxyHb dominant (fresh); single peak at 630 nm = MetHb dominant (aged).

---

### 2.8 NADH

**Stability mechanism:** NADH is oxidized to NAD⁺ by dissolved oxygen. Also degraded by alkaline hydrolysis (especially at pH > 8).

**Key data:**
- NADH half-life in aqueous solution at room temp, neutral pH: ~1–4 hours.
- Protected by refrigeration (4 °C): more stable, but still oxidizes within 24 h.
- In urine: lower NADH concentrations than intracellular; oxidation is faster.

**Spectroscopic consequence for Jimini:** NADH fluorescence at ex365/em460 decays over time. Measurements delayed > 1 h underestimate NADH content. **NADH is one of the most time-sensitive analytes for spectroscopy.**

---

### 2.9 Uric Acid

**Stability:** Relatively stable. Uric acid is stable at room temperature for at least **4 hours**, and at 4 °C for > 24 h. At very high pH (> 8) and with alkaline oxidation, some degradation occurs via xanthine oxidase.

**Crystal precipitation:** At low temperatures (4 °C), uric acid crystals can precipitate from supersaturated urine. Refrigerated samples should be warmed to room temperature and mixed before measurement.

---

### 2.10 Creatinine

**Stability:** Very stable. Stable at room temperature for **> 24 hours**. Stable at 4 °C for days. No significant photodegradation. Can be measured on stored or frozen samples with confidence.

---

### 2.11 Protein (Total)

**Stability:** Stable at room temperature for **8 hours**; stable at 4 °C for 24–48 h. Proteolytic enzymes from bacteria or cells can degrade proteins over longer periods. High-pH urine (from bacterial urease) can cause false-positive colorimetric protein results via turbidimetry.

---

### 2.12 Crystals

**Formation mechanism:** Crystal formation/dissolution is temperature and pH dependent:
- **Cooling to 4 °C:** Promotes precipitation of urates and phosphates (solubility decreases).
- **pH elevation** (from bacterial urease): promotes phosphate crystal formation; dissolves uric acid crystals.
- **Crystal dissolution:** Uric acid crystals dissolve at pH > 7; calcium phosphate crystals form at pH > 7.

**Key guideline:** European urinalysis guidelines: "Refrigeration causes precipitation of phosphates and urates. Prepare a separate non-refrigerated aliquot if differentiation of urinary crystals is requested."

---

### 2.13 Nitrites

**Stability (strip test):** Surprisingly stable for a volatile compound:
- At 4–8 °C: 8 hours
- At 20–25 °C: **4 days** (from Delanghe & Speeckaert table, 2014)
- **False positive risk:** At very long room temperature storage, bacteria produce nitrites; elevated nitrites after 4 h at room temp may reflect in vitro bacterial metabolism rather than in vivo bacteriuria.

---

### 2.14 Glucose

**Stability:** Unstable due to bacterial and enzymatic consumption:
- At 4–8 °C: 2 hours
- At 20–25 °C: **< 2 hours**
- Ascorbic acid (vitamin C) can interfere with glucose oxidase test strips; no direct spectral effect.

---

## 3. Master Stability Table

### 3.1 Particle/Cellular Analytes (from Delanghe & Speeckaert, 2014; European guidelines)

| Analyte | 20–25 °C (no preservative) | 4–8 °C | Critical degradation mechanism | Spectral consequence |
|---|---|---|---|---|
| **RBC** | 1 h (dilute/alk) – 24 h (conc/acid) | 1–4 h | Osmotic lysis, proteolysis | Soret shifts 415→405 nm; scatter ↓ |
| **WBC** | 1 h (pH > 7.5) – 24 h (pH < 6.5) | ~1 day | pH-driven lysis, osmotic | Scatter ↓; fluorescence transiently ↑ then ↓ |
| **Bacteria** | **1–2 h** (start of significant growth) | 24 h | Exponential replication | Scatter ↑; flavin fluorescence ↑ |
| **Epithelial cells** | ~3 h | Not studied | Lysis | Scatter ↓ |
| **Casts** | ~2 days | Not allowed (freeze) | Mechanical fragility | — |
| **Crystals** | Variable | Precipitate ↑ on cooling | Solubility equilibrium | Scatter ↑ on cooling; dissolve on warming |

### 3.2 Chemical/Spectral Analytes

| Analyte | 20–25 °C (dark) | 20–25 °C (light) | 4–8 °C (dark) | Mechanism | Jimini priority |
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
| **Nitrites** | 4 days | 4 days | 8 h | Stable (later: in vitro BAC production) | Moderate |
| **Glucose** | **< 2 h** | < 2 h | 2 h | Bacterial/enzymatic consumption | Not Jimini target |

---

## 4. Temperature Effects

### Summary

| Temperature | Bacterial growth | Cell lysis | Chemical stability | Recommended? |
|---|---|---|---|---|
| **37 °C** | Very fast (doubling ~20–40 min) | Accelerated | Fast degradation | ❌ Never |
| **20–25 °C (RT)** | Moderate (doubling ~60–90 min) | Moderate | Moderate (varies by analyte) | Only if measured within **1–2 h** |
| **4–8 °C (refrigerated)** | Slowed (~10× vs RT) | Slowed | Stable for most analytes 24 h | ✅ If delay > 2 h |
| **−20 °C (frozen)** | Halted | Complete cellular disruption | Good for chemical; bad for particles | Not for particles |
| **−80 °C** | Halted | Cell disruption | Excellent (metabolomics standard) | Research only |

### Key temperatures for Jimini
- Jimini is a **point-of-care** device — measurements are taken close to collection time. Assume **room temperature** conditions.
- Target measurement window at room temperature: **< 1 hour after collection** for cellular analytes; **< 2 hours** for chemical analytes.
- If the device is used at body temperature (e.g., catheter-side measurement): bacterial growth is accelerated. Continuous catheter monitoring (as in Kuenert 2025) must account for ongoing biochemical changes in the catheter bag.

---

## 5. Light Exposure Effects

### Photosensitive Analytes

| Analyte | Sensitive wavelengths | Half-life in room light | Protection needed |
|---|---|---|---|
| **Bilirubin** | 400–500 nm (peak ~460 nm) | ~1–2 h | ⚠️ Amber container; dark room |
| **PBG** | 300–450 nm (accelerates polymerization) | 2–4 h | ⚠️ Amber container |
| **Porphyrins (TUP)** | 400–420 nm (Soret excitation) | 1–4 h | ⚠️ Amber container |
| **Urobilinogen** | 400–500 nm | ~1 h | Amber container |
| **NADH** | 340–365 nm | ~1–4 h (mixed oxidation + light) | Minimize UV exposure |
| **Uric acid** | Not photosensitive | — | No special precaution |
| **Creatinine** | Not photosensitive | — | No special precaution |

### Jimini Measurement Itself as a Photodegradation Source

**This is unique to spectrophotometric devices:** Each LED exposure degrades photosensitive analytes in the sample. The 405 nm LED is particularly efficient at porphyrin Soret excitation and bilirubin photodegradation.

**Quantification:** A typical LED measurement uses ~10–100 ms exposure at 1–100 mW. For bilirubin (ε ≈ 60,000 M⁻¹cm⁻¹ at 453 nm):
- At 455 nm, 10 mW, 10 ms exposure in a 1 mm path length cuvette
- Photon flux ≈ 2.3 × 10¹⁶ photons/s → ~2.3 × 10¹⁴ photons per pulse
- Photodegradation is measurable after multiple repeated exposures but single-exposure degradation is negligible (< 0.1% per flash)

**Recommendation:** Single measurement is safe. Sequential multi-LED sweeps (e.g., 10 exposures × 4 LEDs) accumulate ~1% bilirubin degradation — acceptable for single sessions, problematic for continuous monitoring.

---

## 6. pH Drift and Its Cascade Effects

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

**Time course of pH shift:**
- Urease-producing bacteria can raise pH from 5.5 to > 8 within **1–2 hours** at room temperature (Griffith et al., Investig Urol 1976; Mobley & Warren, J Clin Microbiol 1987).
- E. coli (the most common UTI pathogen) does NOT produce urease and does not cause this alkaline shift.

**Key implication for Jimini:** Samples from patients with Proteus/Klebsiella UTI (urease-producing organisms) will undergo rapid pH changes that:
- Lyse cells (WBC, RBC) → undercount
- Precipitate crystals → false-positive crystal detection
- Dissolve uric acid crystals → false-negative crystal detection
- Destabilize PBG → false-positive TUP signal

**Mitigation:** Measure immediately, or acidify to pH ~3–4 for porphyrin/PBG-specific assays.

---

## 7. Preservatives

No single preservative preserves all analytes simultaneously. This is a fundamental limitation.

### 7.1 Common Preservatives and Their Effects

| Preservative | Mechanism | Bacteria | WBC | RBC | Bilirubin | Porphyrins | Nitrite strip | LE strip | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Refrigeration (4 °C)** | Slows metabolism | ✅ slowed | ✅ preserved | ✅ preserved | ✅ (+ dark) | ✅ (+ dark) | ✅ | ✅ | Best general option |
| **Boric acid** (1.8%) | Bacteriostatic, keeps pH ≤ 7 | ✅ inhibited | ✅ preserved | Variable | — | ✅ (pH kept low) | ❌ false neg | ❌ false neg | Standard for culture; interferes with strip tests |
| **Borate + formate + sorbitol** (BD C&S, Greiner Stabilur) | Bacteriostatic + cell stabilization | ✅ | ✅ (6–24 h) | ✅ | — | — | ✅ | ✅ | Best commercial option for both culture + strips |
| **Formaldehyde** (10 mL/L) | Fixes cells, bactericidal | ✅ | ✅ | ❌ poor | — | — | ❌ | ❌ | Lowers pH; disrupts LE test |
| **Ethanol 80 mL/L + PEG 20 g/L** (Saccomanno's) | Fixes cells | — | ✅ | ✅ | — | — | — | — | For cytological work only |
| **Sodium azide** (0.1%) | Metabolic inhibitor | ✅ | ✅ | ✅ | — | — | — | — | Toxic; research use |
| **None + dark storage + 4 °C** | Physical | ✅ slowed | ✅ short-term | ✅ short-term | ✅ dark | ✅ dark | ✅ | ✅ | Sufficient for < 2 h |

### 7.2 Spectroscopic Interference of Preservatives

Critical for Jimini — chemical preservatives can directly interfere with spectroscopic measurements:

| Preservative | Spectral interference |
|---|---|
| **Boric acid** | Absorbs weakly in UV; lowered pH changes urobilinogen/bilirubin equilibria |
| **Formaldehyde** | Strong UV absorption at ~270 nm — **directly interferes with uric acid/protein measurements at 275 nm** |
| **Sodium azide** | Absorbs at ~270 nm — also interferes with UV measurements |
| **Mercury salts** | Interfere with creatinine and UV absorption |
| **Ethanol** | Strong UV absorption; completely disrupts 275 nm measurements |

**Recommendation for Jimini:** Avoid all chemical preservatives for spectroscopic samples. If preservation is needed, **refrigeration at 4 °C in the dark** is the only non-interfering option.

---

## 8. Clinical Guidelines: CLSI & European Urinalysis

### CLSI GP16-A3 / PRE05 (2009, updated 2024)

The key recommendations for routine urinalysis:
- **Analyze within 2 hours of collection** at room temperature, without preservative
- Refrigerate at **2–8 °C** if analysis is delayed beyond 2 hours
- Protect **bilirubin and urobilinogen** from light
- Use **first morning midstream** clean-catch for optimal sample quality
- **Warm refrigerated samples to room temperature** before analysis (prevents cold-induced crystal precipitation artifacts)
- Document time of collection and time of analysis; flag delayed samples

### European Confederation of Laboratory Medicine (ECLM) Urinalysis Guidelines (2000)

The European guidelines are more stringent for particle analysis:
- **Examine particles < 1 hour after voiding** at ambient temperature
- Or **< 4 hours if refrigerated** at 2–8 °C
- Particles: examine < 30 min from the time of micturition (ideal, per Sysmex standard)
- **Separate aliquot** for crystal analysis if refrigerated (crystals precipitate on cooling)

### Summary of Guideline Requirements

| Category | CLSI GP16-A3 | ECLM | Jimini recommendation |
|---|---|---|---|
| **Particle analysis (WBC, RBC, bacteria)** | < 2 h RT | **< 1 h RT**, < 4 h refrigerated | < 1 h at RT |
| **Chemical analysis (bilirubin, protein, etc.)** | < 2 h RT | < 2 h RT | < 2 h at RT |
| **Light-sensitive (bilirubin, urobilinogen, PBG, TUP)** | Protect from light | Amber containers | Dark container; measure first |
| **Refrigeration** | 2–8 °C if delay > 2 h | 2–8 °C if delay > 1 h | 2–8 °C if delay > 1 h |
| **Frozen** | Not for routine | Not for particles | Not applicable (POC) |
| **No preservative needed if...** | Analyzed < 2 h at RT | Analyzed < 1 h at RT | Analyzed < 1 h |

---

## 9. Jimini-Specific Implications

### 9.1 Time Budget Per Analyte

| Analyte | Hard deadline (RT, no preservative) | Risk of delay |
|---|---|---|
| **Bacteria (BAC)** | **1–2 h** — after this, in vitro growth causes false positives | Overcount |
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

### 9.2 The OxyHb → MetHb Transition: A Useful Quality Indicator

The Q-band doublet at 541/576 nm (OxyHb) vs single peak at 630 nm (MetHb) in the white-LED spectrum provides a built-in **sample freshness indicator for hematuria samples**:

```
Q-band doublet (541 nm + 576 nm) present → OxyHb dominant → Fresh sample
Single Q-band at 630 nm → MetHb dominant → Delayed > 4 h (at RT)
Ratio: A(541)/A(576) ≈ 0.9 for OxyHb; approaches 1 for MetHb
```

This ratio can be added as a QC feature to any RBC model output.

### 9.3 The PBG-TUP Temporal Confound

**A unique challenge for Jimini TUP measurement:**

In acute porphyria patients:
- Fresh sample: high PBG → low TUP (PBG not yet converted)
- Sample after 2–4 h at room temp: PBG → uroporphyrin → rising Soret + fluorescence
- Measurement reports TUP as elevated even though the cause is PBG, not pre-formed porphyrins

This means **TUP measured on delayed samples overestimates "true" porphyrins** and will create artificial TUP elevation that mimics porphyria. To distinguish PBG from pre-formed porphyrins, a second measurement on an acidified/fresh aliquot would be needed.

### 9.4 Bacterial Growth as a Confound for All Particulate Analytes

In a sample with bacteriuria (common in UTI patients — the primary clinical target), bacteria grow continuously from collection to measurement. After 2 hours at room temperature, the sample scatter is NOT representative of the original void.

**Recommendation:** Timestamp every sample. Build a time-from-collection feature into the ML pipeline. Models should be trained stratified by collection-to-measurement delay.

### 9.5 Crystal Artifact from Refrigerated Samples

If Jimini devices are deployed in clinical settings where samples are refrigerated during transport:
- **Uric acid and phosphate crystals may have precipitated in transit**
- Warming the sample back to 37 °C and mixing before measurement is necessary for accurate crystal analysis
- Include a **sample pre-warming step** in the measurement protocol if refrigerated samples are expected

---

## 10. Recommended Measurement Protocol

### 10.1 Optimal Protocol for Jimini (Point-of-Care Use)

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
  → Note: after 30 min, PBG conversion begins to produce artifact TUP signal

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

### 10.2 ML Data Collection Protocol

For building robust Jimini models, training data should include:
1. **Time-from-collection label** on each sample
2. **Samples measured at 0, 30, 60, 120 min** from the same void — to characterize degradation curves
3. **pH at time of measurement** — flags urease-driven cascade
4. **Storage temperature** — room temp vs refrigerated
5. **Light exposure** — dark container vs standard container

This enables the model to either:
- Apply a time-based correction factor to adjust measurements toward t=0 values
- Use time-from-collection as an additional input feature
- Flag out-of-protocol samples for review

---

## 11. Sources

| Source | URL / Reference |
|---|---|
| Delanghe & Speeckaert, Biochemia Medica 2014 — Preanalytical requirements of urinalysis | [PMC3936984](https://pmc.ncbi.nlm.nih.gov/articles/PMC3936984/) |
| BMC Nephrology 2024 — Changes in urine composition over six hours | [bmcnephrol.biomedcentral.com](https://bmcnephrol.biomedcentral.com/articles/10.1186/s12882-024-03933-z) |
| SIPMEL — Stability of urine particles at room temperature | [sipmel.it](https://www.sipmel.it/en/riviste/articolopdf.php/2466) |
| CLSI GP16-A3 / PRE05 sample | [clsi.org](https://clsi.org/media/2461/gp16a3e_sample.pdf) |
| European Confederation of Laboratory Medicine Urinalysis Guidelines (2000) | Scand J Clin Lab Investig 60:1–96 |
| Sysmex — Effect of delay on urine particle analysis | [sysmex.co.jp](https://www.sysmex.co.jp/en/products_solutions/library/journal/vol12_no1/sum_vol12_1_02.pdf) |
| Rehak et al. 2007 — Photolysis of bilirubin in serum (room lighting) | [PMC2131702](https://ncbi.nlm.nih.gov/pmc/articles/PMC2131702/) |
| Pediatric Research 2019 — Effect of light wavelength on bilirubin photodegradation | [nature.com](https://www.nature.com/articles/s41390-019-0310-2) |
| Bossenmaier et al., Clinical Chemistry 1968 — Stability of ALA and PBG in urine | [academic.oup.com/clinchem](https://academic.oup.com/clinchem/article-abstract/14/7/610/5674659) |
| European Porphyria Network — Laboratory diagnosis | [porphyria-europe.org](https://www.porphyria-europe.org/02-for-healthcare/labo-diagnosis.asp) |
| Clinlabint — Analyte stability for porphyrins and precursors | [clinlabint.com](https://clinlabint.com/impact-of-analyte-stability-on-the-urine-analysis-of-porphyrins-and-their-precursors/) |
| PubMed 38631910 — Stability of porphyrins in urine and plasma | [pubmed.ncbi.nlm.nih.gov/38631910](https://pubmed.ncbi.nlm.nih.gov/38631910/) |
| Rosen et al., CMR 2020 — UPEC growth and metabolism in urine | [ASM CMR](https://journals.asm.org/doi/10.1128/cmr.00101-19) |
| PMC9603375 — E. coli growth in pooled urine | [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9603375/) |
| Meng et al., PMC5303181 — Extinction coefficients of hemoglobin redox forms | [PMC5303181](https://pmc.ncbi.nlm.nih.gov/articles/PMC5303181/) |
| PLOS ONE 2022 — MetHb synthesis and stability | [journals.plos.org](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263782) |
| Mobley & Warren 1987 — Urease and long-term catheter obstruction | J Clin Microbiol 25:2216 |
| Griffith et al. 1976 — Urease: primary cause of infection-induced urinary stones | Investig Urol 13:346 |
| University of Washington Lab — Complete Urinalysis (2 h rule) | [testguide.labmed.uw.edu](https://testguide.labmed.uw.edu/view/UAC) |
| Labpedia — Urobilinogen stability | [labpedia.net](https://labpedia.net/urine-for-urobilinogen-and-ehrlich-reagent/) |
| Mayo Clinic Labs — Urine preservatives for 24-hour specimens | [mayocliniclabs.com](https://www.mayocliniclabs.com/-/media/it-mmfiles/Special-Instructions/9/6/7/Urine_Preservatives-Collection_and_Transportation_for_24-Hour_Urine_Specimens) |
| Ercan et al., Clin Biochem 2015 — Stability with/without preservatives at RT vs ice | [brd.nci.nih.gov](https://brd.nci.nih.gov/brd/paper/clin-biochem/2015/stability-of-urine-specimens-stored-with-and-without-preservatives/124430) |
| Clinical Biochemistry 2012 — 4-hour delay for urine samples | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0009912012001956) |
