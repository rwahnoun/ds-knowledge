---
title: Optical Path Design for Pen-Form Spectrophotometry of Urine
aliases:
  - Optical Path Design
  - Jimini Optical Architecture
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Optical Path Design for Pen-Form Spectrophotometry of Urine

Design reference for the Jimini optical system. LEDs at 275/365/405/455 nm + white + 1070 nm NIR; detectors C12880MA (340–850 nm) and C14384MA (640–1050 nm). See [[leds]] and [[sensors]] for component specs; see [[datascience/spectroscopy-biomarkers]] for analyte context.

---

## Path Length Selection

Path length $l$ (cm) is the dominant design variable. It sets the dynamic range through Beer-Lambert: $A = \varepsilon \cdot c \cdot l$.

The critical constraint is that absorbance must stay **within the linear Beer-Lambert range**: typically $A < 1.5$ AU for reliable spectrophotometry (above 1.5 AU, stray light errors and detector non-linearity dominate). The **lower bound** is set by detector noise; for the C12880MA (1.3 mV readout noise, ~16-bit effective), absorbances of ~0.001 AU are measurable with good SNR, but practically $A > 0.01$ AU is reliable.

### Analyte-by-Analyte Analysis

#### Bilirubin (ε = 60,000 M⁻¹cm⁻¹ @ 453 nm)

| Path length | A @ 5 µmol/L (min pathological) | A @ 100 µmol/L (severe) | Assessment |
|---|---|---|---|
| 10 mm (1 cm) | 0.30 | 6.0 | Saturates at high bilirubin |
| 5 mm | 0.15 | 3.0 | Borderline at very high concentrations |
| **2 mm** | **0.06** | **1.2** | ✅ Good linear range across clinical range |
| 1 mm | 0.03 | 0.60 | ✅ Good for high range; low SNR at low end |

Normal urine bilirubin: <5 µmol/L (negative). Pathological: 5–100+ µmol/L. **Optimal path: 2–5 mm.**

#### Uric Acid (ε ≈ 8,000–9,000 M⁻¹cm⁻¹ @ 275 nm)

| Path length | A @ 100 µmol/L (low normal) | A @ 5,000 µmol/L (hyperuricuria) | Assessment |
|---|---|---|---|
| 10 mm | 0.80 | 40 | Saturated at normal concentrations |
| 5 mm | 0.40 | 20 | Saturated at high end |
| **2 mm** | **0.16** | **8** | Saturates at hyperuricuria |
| **1 mm** | **0.08** | **4** | Still saturates at max concentration |
| **0.5 mm** | **0.04** | **2** | ✅ Linear at physiological range; low SNR |

Urine [[uric-acid|uric acid]]: 250–750 µmol/L typical; up to 5,000 µmol/L in hyperuricuria. **This is the most constraining analyte. Optimal path: 0.5–2 mm, possibly with dual-path or HDR measurement.**

#### Hemoglobin / [[red-blood-cells|RBC]] (ε = 128,000 M⁻¹cm⁻¹ @ 415 nm for oxyHb)

Clinical hematuria threshold: ~5 [[red-blood-cells|RBC]]/µL. Free hemoglobin from lysed [[red-blood-cells|RBC]] at 5 [[red-blood-cells|RBC]]/µL ≈ ~0.009–0.019 µmol/L.

| Path length | A @ 0.01 µmol/L (threshold) | A @ 1 µmol/L (gross haematuria) | Assessment |
|---|---|---|---|
| 10 mm | 0.0013 | 0.13 | ✅ Detects threshold; good dynamic range |
| **5 mm** | **0.0006** | **0.064** | ✅ Detectable with HDR |
| 2 mm | 0.0003 | 0.026 | Threshold borderline even with HDR |

Hemoglobin is the **most demanding analyte for sensitivity**. **Path ≥ 5 mm preferred for hemoglobin sensitivity.**

### Summary Conflict

The analytes pull in **opposite directions**:

- [[uric-acid|Uric acid]] → short path (≤1 mm) to avoid saturation
- Hemoglobin at threshold → long path (≥5 mm) for sensitivity

**Solution: dual-path or variable-path design.** Two standard approaches:

1. **Dual-cell design:** UV cell (0.5–1 mm path, for 275/365 nm measurements) + Vis cell (5–10 mm path, for 405/455/white measurements).
2. **Single cell with HDR:** A 2 mm path cell with exposure time adjustment per LED. Short exposures for UV LEDs, long exposures for visible LEDs. The Kuenert 2025 paper used this approach: two exposure times (20 ms and 200/320 ms) per light path.

### Practical Recommendation for Jimini

**Single cell, 2 mm path length**, with HDR exposure (multiple integration times per LED):

- Optimizes the widest range of analytes simultaneously
- Keeps the device compact (pen form factor)
- Allows software selection of the non-saturated exposure for each LED
- 2 mm is a standard micro-cuvette dimension (Hellma, Starna)

**For UV-C (275 nm), consider 1 mm** if [[uric-acid|uric acid]] saturation is confirmed empirically.

---

## Measurement Geometry

Three primary configurations for liquid spectrophotometry:

### Direct Transmission (DT) — Collinear

```
LED → [collimating lens] → SAMPLE → [collection lens] → DETECTOR
```

Light travels straight through the sample along the optical axis.

Advantages: maximum signal throughput; well-defined Beer-Lambert path length; simplest optical alignment.
Disadvantages: scatter from particles ([[white-blood-cells|WBC]], [[bacteria]]) mixes with absorption signal.

Best for: Chemical analyte quantification (bilirubin, [[uric-acid|uric acid]], hemoglobin) where scatter is a correction, not the primary measurement.

### Angular Transmission (AT) — Off-Axis

Detector is placed at a non-zero angle from the LED axis (typically 20–60°).

Advantages: Directional forward scatter (Mie) is strongly angle-dependent; separates scatter information from pure absorption.
Best for: Distinguishing scatter contributions; sizing particles by angular dependence.

### Angular Reflection (AR) — Backscatter

Light source and detector are on the same side of the sample; detector captures reflected/backscattered light.

Best for: Turbidity estimation; highly scattering samples.

### Recommendation: Multi-Angle (DT + AT + AR) as in Kuenert 2025

The Kuenert 2025 group explicitly compared all three configurations and combined them into a 1728-feature dataset (3 paths × 2 exposures × 288 wavelengths):

- **DT** performed best for direct absorbers (bilirubin, hemoglobin)
- **AT** and **AR** added information for scatter-dominated parameters (specific gravity, particles)

For Jimini's pen form factor, a **single DT path with one off-axis angle** (e.g., 30–45°) is a practical compromise.

---

## Sample Chamber & Cuvette Materials

### Optical Transmission Requirements by LED

| LED | λ (nm) | Required transmissive range | Compatible materials |
|---|---|---|---|
| UV-C | 275 | 250–300 nm | **Quartz (fused silica), sapphire** |
| UV-A | 365 | 350–380 nm | Quartz, sapphire, UV-grade glass, fused silica |
| Violet | 405 | 390–420 nm | Quartz, borosilicate glass, UV-grade acrylic |
| Blue | 455 | 440–470 nm | Quartz, borosilicate glass, standard glass, acrylic |
| White | 400–700 | 390–720 nm | Quartz, borosilicate glass, standard glass, acrylic |
| NIR | 1070 | 1000–1100 nm | Quartz, borosilicate glass, N-BK7, sapphire |

### Material Comparison Table

| Material | UV-C transparent | UV-A transparent | Vis transparent | NIR (1070 nm) | Chemical resistance | Cost |
|---|---|---|---|---|---|---|
| **Fused silica (synthetic quartz)** | ✅ (>170 nm) | ✅ | ✅ | ✅ | High | High |
| **Sapphire** | ✅ (>150 nm) | ✅ | ✅ | ✅ | Very High | Very High |
| **UV-grade borosilicate** | ⚠️ (>300 nm) | ✅ | ✅ | ✅ | Medium | Low |
| **Standard borosilicate** | ❌ (<320 nm absorbs) | ⚠️ weak | ✅ | ✅ | Medium | Very Low |
| **Optical-grade PMMA (acrylic)** | ❌ | ❌ | ✅ (>380 nm) | ✅ | Low | Very Low |
| **COC/COP** | ⚠️ (>280 nm) | ✅ | ✅ | ✅ | High | Medium |

### Key Material Decisions for Jimini

**For the 275 nm UV-C path:** The cuvette window(s) must be **fused silica (quartz)**. No exceptions. Standard glass, PMMA, and polycarbonate all absorb strongly at 275 nm. The Kuenert group used "UV quartz glass lenses" (Edmund Optics) in their prototype for this reason.

**For 365–1070 nm (all other LEDs):** UV-grade borosilicate glass is sufficient and cost-effective.

**Practical architecture:** A cuvette with a quartz optical window on the 275 nm axis and borosilicate glass elsewhere. Alternatively, an entirely fused-silica micro-cuvette (e.g., Hellma Analytics 105.200-QS, 1 mm path, 40 µL volume) serves all wavelengths.

### Standard Micro-Cuvette Suppliers

| Supplier | Product | Path (mm) | Volume (µL) | Material | UV-C compatible | Price (~) |
|---|---|---|---|---|---|---|
| **Hellma Analytics** | 105.200-QS | 1 | 40 | Quartz | ✅ | ~€150 |
| **Hellma Analytics** | 105.201-QS | 2 | 80 | Quartz | ✅ | ~€180 |
| **Starna Scientific** | 1-Q-1 | 1 | 40 | Quartz | ✅ | ~€120 |
| **Starna Scientific** | 18-Q-1 | 2 | 100 | Quartz | ✅ | ~€140 |
| **Custom SLA resin + quartz windows** | — | custom | custom | Resin frame + quartz | ✅ (windows) | <€20 |

---

## Optical Coupling: LED → Sample → Detector

### LED Collimation

Raw LEDs emit in a wide-angle Lambertian pattern (120–170° half-angle). Without collimation, only a fraction of this light reaches the sample.

| Method | Collimation quality | UV-C compatibility | Cost | Size |
|---|---|---|---|---|
| **Single aspherical lens (quartz)** | Good (±5–10°) | ✅ (quartz) | Medium | 5–15 mm diameter |
| **Reflective parabolic collimator** | Good | ✅ (Al mirror) | Medium | Larger |
| **Ball lens (quartz)** | Moderate | ✅ | Low | 2–6 mm diameter |
| **Fiber optic (quartz SMA)** | Excellent | ✅ (quartz fiber) | Medium-High | Flexible |
| **No collimation (bare LED + aperture)** | Poor | ✅ | Very Low | Minimal |

**Recommended for Jimini:** A small plano-convex quartz lens (e.g., Edmund Optics UV-grade fused silica, 5 mm diameter, 10 mm focal length) positioned at the LED's focal distance. Mechanically fixed in the 3D-printed chassis (SLA resin for sub-0.1 mm tolerance as shown by Kuenert 2025). For 365–1070 nm, standard glass or polymer lenses are acceptable.

### Collection Optics (Sample → Detector)

The C12880MA has a small entrance slit and accepts light within ~±15° of its optical axis.

**Option A: Free-space lens array** (used by Kuenert 2025) — Edmund Optics UV quartz glass lens array focuses light from sample exit to spectrometer entrance. Direct mechanical coupling; alignment must be precise.

**Option B: Fiber optic coupling** — Quartz-core fiber optic (e.g., Ocean Optics/Ocean Insight SMA-terminated QP200-2-UV-VIS) connects sample to spectrometer. Flexible; allows separation of optics and electronics.

**Recommendation:** For pen form factor with integrated design, **free-space collection using quartz lenses** gives highest transmission efficiency. For a bench prototype, **fiber optic coupling** is faster to implement.

---

## UV-C Specifics at 275 nm

### Material Constraints

At 275 nm, essentially all common optical materials absorb significantly:

| Material | Transmittance @ 275 nm (1 mm thick) |
|---|---|
| Fused silica (synthetic) | ~95% |
| Borosilicate glass (BK7) | ~5% |
| Standard glass | ~0% |
| PMMA (acrylic) | ~0% |
| Silicone / PDMS | ~0% (strong absorption) |
| PTFE | ~85% (diffuse, not clear) |
| Sapphire | ~90% |

> [!WARNING]
> **Every optical element in the 275 nm path must be quartz (fused silica) or sapphire.** This includes: LED window, collimating lens, cuvette windows, any light guide, collection lens. Do not use conformal coatings, silicone adhesives, or epoxy near the UV-C path.

### Degradation and Solarization

UV-C radiation induces solarization in optical elements over time:
- PMMA: visible discoloration within hours of UV-C exposure
- Borosilicate glass: solarization above ~100 hours at high intensity
- Fused silica: minimal solarization (use UV-grade fused silica, JGS1 or better)
- Sapphire: immune to solarization

### Photobleaching Risk

UV-C at 275 nm can photobleach urine fluorophores ([[nadh|NADH]], [[total-urinary-porphyrin|porphyrins]]) and degrade analytes ([[uric-acid|uric acid]] partial photodestruction over extended exposure). Use pulsed LED (1–10 ms pulses) and minimize total UV dose per measurement.

---

## Stray Light Management

Stray light is out-of-band radiation reaching the detector without having passed through the sample — it reduces the effective dynamic range and causes systematic absorbance errors.

### Sources of Stray Light

1. **LED side lobes**: Even with collimation, LEDs emit some light at large angles
2. **Cuvette wall reflections**: Refractive index mismatch at glass-air and glass-water interfaces
3. **Spectrometer internal scatter**: The C12880MA MEMS grating has documented stray light at short wavelengths (confirmed by PMC11479284 — elevated signal below 400 nm)
4. **Fluorescence from optical elements**: Silicone adhesives, plastic holders, and PMMA fluoresce under UV excitation

### Mitigation Strategies

1. **Aperture baffles:** Place apertures between LED and cuvette to limit off-axis illumination. Use anodized black aluminum apertures.
2. **Dark enclosure:** Completely enclose the optical path in a light-tight housing. All internal surfaces should be matte black. Use black SLA resin for the mechanical chassis.
3. **Bandpass optical filter (recommended for 275 nm):** Place a narrow bandpass filter (e.g., 275 nm ± 5 nm) between the LED and cuvette. For UV-C, use interference filters on fused silica substrate (e.g., Semrock FF01-280/20-25).
4. **Dual-modulation (lock-in detection):** Pulse the LED at a known frequency (e.g., 1 kHz); use synchronous detection in firmware to reject ambient light and electronic noise.
5. **Detector-side filtering:** For fluorescence measurements (UV excitation → visible detection), a **long-pass filter** on the detector side eliminates the excitation wavelength from reaching the detector.

---

## Bubble Management

Air bubbles in the measurement path cause large absorbance spikes and scatter artifacts. This is one of the most common failure modes in portable liquid spectrophotometers.

### Mitigation Strategies

**Surface treatment (most effective):**
- **Plasma treatment (oxygen plasma):** Creates a highly hydrophilic surface on glass and silicone. Contact angle decreases from ~30° to <5°, strongly suppressing bubble nucleation.
- **PEG (polyethylene glycol) coating:** Chemical functionalization of glass surface with PEG creates a hydrophilic, non-fouling surface. More durable than plasma treatment.
- **Surfactant pre-rinse:** Rinse cuvette with dilute Tween-20 (0.01%) before measurement.

**Geometric design:**
- **Bottom-fill from below:** Sample enters from the bottom of the cuvette upward, displacing air outward from the top.
- **Vent at top:** Small vent hole at the top of the cuvette allows air to escape as sample fills from below.
- **Avoid sharp 90° turns:** Bubble-trapping geometry; use gentle curves in microfluidic channels.

**Detection and rejection:**
- **Bubble detection algorithm:** Large bubbles cause characteristic "spike" artifacts (sudden decrease in transmitted intensity across all wavelengths). Detect by monitoring the ratio of expected to measured total intensity; reject measurements that deviate >20% from baseline.

---

## Sample Introduction & Volume Requirements

### Volume Budget

| Component | Dead volume | Measurement volume | Total minimum |
|---|---|---|---|
| 2 mm path cuvette (2×4 mm cross-section) | — | ~40 µL | — |
| Tubing/fill channel | 5–50 µL (design-dependent) | — | — |
| **Practical total minimum** | | | **50–200 µL** |

### Introduction Methods

**Option A: Dip-and-read** — Device is dipped directly into the urine sample. Volume: unlimited. Not recommended for quantitative transmission measurements.

**Option B: Pipette/manual fill** — User pipettes 100–200 µL into a cuvette slot. Recommended for clinical lab or near-patient settings.

**Option C: Capillary fill (passive)** — Disposable cuvette cartridge with a capillary channel; user touches the outlet to the urine sample. Recommended for true POC / pen form factor.

**Option D: Active pumping** — Small pump draws urine through a flow cell. Appropriate for catheter/continuous monitoring.

### Disposable vs Reusable Cuvette

| Aspect | Disposable | Reusable |
|---|---|---|
| Cross-contamination | None | Cleaning protocol required |
| Cost per test | Higher ($0.50–$2.00/test) | Lower (amortized) |
| Optical consistency | Varies (manufacturing tolerances) | High (precision optics, characterized) |
| Regulatory (IVD) | Registered as accessory | Must validate cleaning efficacy |

For **clinical use** (regulatory pathway): a **single-use disposable cuvette** is preferred.
For **development and research**: a **reusable quartz micro-cuvette** is most practical.

---

## Reference Measurement Strategy

Beer-Lambert requires a reference: $A = -\log_{10}(I_\text{sample} / I_\text{reference})$.

### Reference Options

**Option A: Water blank before each sample** — Fill cuvette with de-ionized water, measure $I_\text{water}$, then fill with sample. Pros: directly accounts for LED intensity drift and cuvette window variation. Recommended for development.

**Option B: Air reference** — Use empty cuvette (air). Not recommended for quantitative measurements without numerical correction — introduces ~0.04 AU systematic baseline offset at glass-air vs glass-water interfaces.

**Option C: Parallel reference channel** — A second detector monitors a beam-splitter continuously illuminated with the same LED. Compensates LED noise in real time.

**Option D: Stored reference from factory calibration** — Acceptable if LED is temperature-controlled and lifetime correction is applied.

**Recommendation for Jimini:**
- **Development:** Water blank before each measurement (Option A)
- **Clinical device:** Disposable cartridge pre-filled with deionized water, or factory calibration with LED monitor photodiode drift correction.

### Dark Current Correction

Essential for all measurements:

$$A = -\log_{10}\left(\frac{I_\text{sample} - I_\text{dark}}{I_\text{water} - I_\text{dark}}\right)$$

$I_\text{dark}$ is measured with LED off; take 5–10 dark measurements and average for stability.

---

## Multi-Angle Measurement for Scatter Discrimination

Scatter from cells and particles is angle-dependent, following Mie scattering theory.

### Mie Scattering Basics

For particles of radius $r$ and wavelength $\lambda$, the size parameter is $x = 2\pi r / \lambda$:

| Particle | Size | λ = 500 nm → x | Scattering regime |
|---|---|---|---|
| [[[[bacteria]]\|Bacteria]] (E. coli) | ~1 µm | ~6 | Mie |
| [[red-blood-cells\|RBC]] | ~7 µm disk | ~44 | Geometric optics |
| [[white-blood-cells\|WBC]] | ~12 µm | ~75 | Geometric optics |
| Crystals | 10–100 µm | ~63–630 | Geometric optics |
| Proteins (uromodulin) | ~100 nm | ~0.6 | Mie/Rayleigh |

### Angular Features for Particle Discrimination

The scatter slope $\alpha$ from a power-law fit $I_\text{scatter} \propto \lambda^{-\alpha}$:
- $\alpha \approx 4$: Rayleigh scattering (sub-wavelength particles)
- $\alpha \approx 1$–2: Mie scattering ([[bacteria]]-sized)
- $\alpha \approx 0$: Geometric optics (cells, crystals, large particles)

Measuring $\alpha$ from the ratio $A_{400}/A_{800}$ using the white LED continuous spectrum gives a **particle size proxy** and can **discriminate [[bacteria]] from [[white-blood-cells|WBC]] from crystals from dissolved protein** without imaging or flow cytometry.

---

## Prior Art: Published Portable Urine Spectrophotometer Designs

### SpectraPhone / Kuenert 2025 (Nat. Sci. Rep.)

**Reference:** Kuenert et al., "Continuous spectroscopic monitoring of urinary catheter output," Scientific Reports 15:8617 (2025).

Design summary:
- **Spectrometer:** Hamamatsu C12880MA (340–850 nm, 288 pixels)
- **Sample chamber:** Borosilicate glass (Hilgenberg) — **note: not UV-C compatible at 275 nm**
- **Collection optics:** Custom lens array, UV quartz glass lenses (Edmund Optics), SLA-printed chassis
- **Measurement geometry:** DT (0°), AT (angular transmission), AR (angular reflectance) — all three measured sequentially
- **Exposure times:** 2 per geometry (short + long HDR)
- **Data per sample:** 3 × 2 × 288 = 1,728 intensity values
- **Chassis:** SLA high-resolution 3D printing (Formlabs Form 3B+, Tough Resin 1500)

Key lessons:
1. SLA printing > FDM for optical precision (rigid resin, <0.1 mm tolerance)
2. Multi-geometry measurement captures both absorption and scatter information
3. HDR exposure prevents saturation
4. Borosilicate glass sufficient for 365–1070 nm; quartz needed for 275 nm

---

## Recommended Jimini Optical Architecture

### Physical Layout (Pen Form Factor ~15 mm Diameter × 80 mm)

```
[Cross-section, top view]

     UV-C (275nm)       Vis LEDs (365/405/455/white)     NIR (1070nm)
         ↓                        ↓                          ↓
    [Quartz lens]          [BK7/quartz lens]           [BK7 lens]
         ↓                        ↓                          ↓
    ←── [QUARTZ CUVETTE (2mm path, 100µL, capillary-fill)] ───→
         ↓
    [Collection lens array, UV quartz]
         ↓
    [C12880MA spectrometer head]   ←→  [C14384MA NIR spectrometer]

Geometry:
- DT: collinear LED → cuvette → detector
- AT: second LED at 30° angle to DT axis → same detector (time-multiplexed)
- Cuvette: vertical fill from below, vent at top

EIS electrodes:
- Integrated into cuvette side walls (Au or Pt thin film electrodes)
- Connected to ADuCM355 via PCB traces
```

### Bill of Materials (Optical)

| Component | Specification | Supplier | Estimated cost |
|---|---|---|---|
| UV-C cuvette window | Fused silica, 5×5 mm, 1 mm thick | Edmund Optics | ~€20 each (×2) |
| Cuvette body | Custom SLA resin (Formlabs Tough 1500) + quartz windows | In-house SLA | ~€5–10 per body |
| 275 nm collimating lens | Fused silica plano-convex, 5 mm dia, f=10 mm | Edmund Optics | ~€40 |
| 365–455 nm lenses | N-BK7 plano-convex, 5 mm dia, f=10 mm | Edmund Optics | ~€15 each |
| Collection lens (UV) | Fused silica achromat, 10 mm dia, f=20 mm | Edmund Optics | ~€60 |
| 275 nm bandpass filter | Fused silica, 275±10 nm, OD 4 blocking | Semrock | ~€200 |
| Emission LPF (fluorescence) | 450 nm long-pass, fused silica | Semrock | ~€80 |

### Operating Sequence

```
1. Insert sample cuvette (pre-wet with water)
2. Dark measurement: all LEDs off → I_dark
3. Reference: fill with DI water (or use stored calibration)
   Water measurement: 275nm on → I_ref_275; 365nm on → I_ref_365; ...
4. Sample: draw urine by capillary; wait 3s for bubbles to clear
5. Measure sequence (time-multiplexed):
   - 275nm on (10ms): I_DT_275 (short exposure; uric acid)
   - 275nm on (100ms): I_DT_275_HDR (long exposure; proteins, fluorescence)
   - 365nm on (50ms): I_DT_365; I_AT_365
   - 405nm on (20ms, 200ms): I_DT_405 (Soret); I_AT_405
   - 455nm on (50ms): I_DT_455 (bilirubin); I_AT_455
   - White on (20ms, 200ms): I_DT_white; I_AT_white (Q-bands, scatter)
   - 1070nm on (50ms): I_DT_1070 (NIR scatter, osmolality)
   Total measurement time: ~2–3 seconds
6. Compute absorbance: A(λ) = -log10((I_sample - I_dark)/(I_ref - I_dark))
7. Apply SNV normalization (see [[signal-processing]])
8. Run ML prediction models
9. Display results
```

---

## Sources

| Source | URL | Key contribution |
|---|---|---|
| Kuenert et al. (2025) — SpectraPhone, urine catheter spectroscopy | [nature.com/s41598-025-92802-2](https://www.nature.com/articles/s41598-025-92802-2) | DT/AT/AR multi-geometry design; lens array; SLA chassis; 401 clinical samples |
| Jechow et al. (2024) — C12880MA characterization | [PMC11479284](https://pmc.ncbi.nlm.nih.gov/articles/PMC11479284/) | Angular acceptance ±13°; stray light at <400nm; 11–12nm FWHM; open-source STM32 firmware |
| Prahl — Optical Absorption of Hemoglobin (OMLC) | [omlc.org/spectra/hemoglobin](https://omlc.org/spectra/hemoglobin/) | Hemoglobin extinction coefficients; Beer-Lambert path-length calculations |
| Seoul Viosys CUD7GF1B Datasheet | [neumueller.com PDF](https://www.neumueller.com/datenblatt/seoulviosys/CUD7GF1B_210624_R1.91.pdf) | 275nm LED spectral shift vs current; flat ceramic package; quartz window |
| Hamamatsu C12880MA Product Page | [hamamatsu.com](https://www.hamamatsu.com/us/en/product/optical-sensors/spectrometers/mini-spectrometer/C12880MA.html) | 340–850nm, 288 pixels, 15nm resolution, 20×12×10mm |
| Hellma Analytics Micro-cuvettes | [hellma-analytics.com](https://www.hellma-analytics.com) | Quartz micro-cuvettes: 1mm path (40µL), 2mm path (100µL) |
| Starna Scientific Cuvettes | [starna.com](https://www.starna.com) | UV-transparent quartz cuvettes; path length options |
| Edmund Optics UV Optics | [edmundoptics.com](https://www.edmundoptics.com/c/uv-fused-silica-optics/758/) | UV fused silica lenses; ball lenses; quartz rod light guides |
| Semrock UV bandpass filters | [semrock.com](https://semrock.com) | Interference filters on fused silica substrate; 275±10nm bandpass |
| Mie Scattering Tutorial (OMLC) | [omlc.org/calc/mie_calc.html](https://omlc.org/calc/mie_calc.html) | Mie scattering cross-sections; wavelength-dependent scatter for particle sizing |
| Open-source C12880MA firmware | [github.com/Helmholtz-UFZ/MiniSpecFirmware](https://github.com/Helmholtz-UFZ/MiniSpecFirmware) | STM32 firmware for C12880MA readout (EUPL 1.2 license) |

## Gaps

1. **Zemax simulation not yet performed** for the Jimini pen geometry. Kuenert 2025 used Ansys Zemax OpticStudio 2023 to optimize lens positions — this should be replicated for Jimini to minimize wall interactions and validate the 2 mm path length choice.
2. **[[uric-acid|Uric acid]] saturation at 1 mm path length not empirically confirmed** — path length selection for the 275 nm channel should be validated with known [[uric-acid|uric acid]] standards.
3. **Bubble rejection algorithm not designed** — the operating sequence specifies a 3 s wait, but a quantitative bubble detection check (intensity ratio threshold) has not been specified or validated.
4. **Capillary fill surface treatment protocol** — PEG coating vs plasma treatment vs surfactant pre-rinse have not been evaluated for the Jimini cuvette material (SLA resin + quartz windows).
