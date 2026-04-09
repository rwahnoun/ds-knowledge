# Optical Path Design & Microfluidics for Pen-Form Spectrophotometry

**Context:** Jimini pen-sized multi-LED spectrophotometer for urine analysis.  
LEDs: 275 / 365 / 405 / 455 nm + white + 1070 nm NIR.  
Detectors: C12880MA (340–850 nm), C14384MA (640–1050 nm).  
Additional: EIS frontend (ADuCM355).  
Sample matrix: urine — variable turbidity (0–2000 NTU), colour (pale yellow to dark brown), particulates (cells, bacteria, crystals), pH 4.5–8.5.

**Date:** 2026-04-09

---

## Table of Contents

1. [Path Length Selection](#1-path-length-selection)
2. [Optical Configuration: Transmission vs Reflectance vs Dip-Probe](#2-optical-configuration)
3. [Optical Window & Cuvette Materials](#3-optical-window--cuvette-materials)
4. [Sample Introduction & Fluid Handling](#4-sample-introduction--fluid-handling)
5. [Bubble Management](#5-bubble-management)
6. [LED-to-Sample Optical Coupling](#6-led-to-sample-optical-coupling)
7. [Stray Light Management](#7-stray-light-management)
8. [Multi-Angle Measurement: Separating Scatter from Absorption](#8-multi-angle-measurement)
9. [Reference Measurement Strategy](#9-reference-measurement-strategy)
10. [Cleaning & Cross-Contamination](#10-cleaning--cross-contamination)
11. [Prior Art: Pen & Portable Spectrophotometer Designs](#11-prior-art)
12. [Recommended Design for Jimini](#12-recommended-design-for-jimini)
13. [Sources](#13-sources)

---

## 1. Path Length Selection

### 1.1 The Beer-Lambert Constraint

Beer-Lambert law: $A = \varepsilon \cdot c \cdot l$

For a fixed detector dynamic range (typically 0.001–3.0 AU usable), the path length $l$ must be chosen so that the expected absorbance for the target analyte concentration range falls within this window. The critical challenge for urine is that analyte molar absorptivities span **five orders of magnitude**:

| Analyte | ε (M⁻¹cm⁻¹) | Normal urine conc. | A at 10 mm path |
|---|---|---|---|
| Bilirubin | 60,000 @ 453 nm | 0–340 µmol/L | 0–0.60 |
| Hemoglobin (Soret) | 128,000 @ 415 nm | 0–50 µmol/L (haematuria) | 0–0.64 |
| Porphyrins (Soret) | ~500,000 @ 405 nm | 0.02–0.5 µmol/L | 0.001–0.025 |
| Uric acid | 11,300 @ 293 nm | 1.5–7.0 mmol/L | 1.7–7.9 → **saturates** |
| NADH | 6,220 @ 340 nm | 0.01–0.05 mmol/L | 0.006–0.031 |
| Creatinine | ~6,500 @ 234 nm | 3–30 mmol/L | not accessible at 275 nm |

**At 10 mm:** uric acid immediately saturates. At **1 mm:** uric acid A = 0.17–0.79, which is in the linear range. But porphyrins at 1 mm: A = 0.0001–0.0025 — at the noise floor.

### 1.2 Path Length Recommendations Per Analyte

| Analyte class | Optimal path length | Reasoning |
|---|---|---|
| High-ε UV absorbers (uric acid, protein) | **0.5–2 mm** | Avoids saturation at 275 nm |
| Moderate-ε visible (bilirubin, hemoglobin) | **2–5 mm** | Good signal without saturation |
| Trace fluorophores (porphyrins, NADH) | **5–10 mm** | Maximise optical path for weak signal |
| Scatter/turbidity (WBC, bacteria, crystals) | **5–10 mm** | Longer path amplifies scatter contrast |

**Conclusion:** No single path length is optimal for all analytes simultaneously. Three strategies exist:

#### Strategy A: Fixed Short Path (1–2 mm) with Sensitivity Compensation
- Pros: Simple, compact, never saturates UV
- Cons: Porphyrins and NADH may be near noise floor; scatter from low cell counts undetectable
- Best for: Devices where UV analytes (uric acid, protein) are primary targets

#### Strategy B: Fixed Medium Path (5 mm)
- Pros: Reasonable compromise; ~3× more sensitive than 1 mm for trace analytes; uric acid A ~ 0.85–3.95 (partially saturating at high concentrations)
- Cons: High uric acid in concentrated urine still saturates at 275 nm
- Best for: Balanced multi-analyte measurement

#### Strategy C: Dual-Path / Slope Spectroscopy
The "slope spectroscopy" technique (ScienceDirect 2021; Zhao et al. Anal. Chem. 2025) measures absorbance at multiple path lengths and fits the slope of A vs. $l$ to extract $\varepsilon c$. This provides:
- **Ultra-broad dynamic range** (>5 orders of magnitude demonstrated)
- Self-calibrating (slope measurement is independent of baseline offset)
- Requires two measurement positions (e.g., 1 mm and 5 mm) — mechanically complex for pen form factor

**Recommended for Jimini:** A fixed **2 mm quartz path** as primary, with a second **5–10 mm fluorescence path** at 90° to the excitation axis. This gives:
- UV (275 nm): A_uric acid = 0.34–1.58 — linear to ~4 mmol/L, saturating only at very high concentrations
- Vis (405/455 nm): A_bilirubin at max = 0.41 — good signal
- Fluorescence (405→620 nm emission): collected at 90° with longer effective path

### 1.3 Micro-Volume Considerations

Commercial micro-volume systems (Eppendorf µCuvette G1.0, Hellma TrayCell 2.0) achieve 1 mm path lengths with 1.5–2 µL sample volumes. For urine, which is abundant, volume is not a constraint — but minimising dead volume for rapid sequential measurements is.

Hellma TrayCell 2.0 caps: 0.2 mm (50× dilution factor), 1 mm (10× dilution factor), 10 mm (standard). Commercial caps are interchangeable — a design inspiration for Jimini's disposable tip.

---

## 2. Optical Configuration

### 2.1 Transmission (In-Line)

```
LED → [collimating lens] → [sample cell] → [collecting lens] → detector
```

- Standard configuration for absorbance
- Path length is mechanically defined by the cell
- Both forward-scattered light and transmitted light reach the detector — in turbid samples, forward scatter adds to "transmitted" signal, **underestimating true absorbance** (apparent A lower than actual)
- For urine with WBCs (turbidity), this is a measurable error at 1070 nm

### 2.2 90° Fluorescence (Off-Axis)

```
LED → [sample cell] → [90° emission detector]
         ↑
    (incident beam continues to transmission detector)
```

- Standard fluorescence geometry — eliminates excitation leakage into emission detector
- For Jimini: ex405/em620 for porphyrins; ex365/em460 for NADH
- Requires a second detector port or optical fibre at 90° to excitation

### 2.3 Reflectance

- Used for opaque samples (concentrated pigmented urine)
- Not recommended as primary configuration for transparent/semi-transparent urine
- Useful for color/turbidity measurement via diffuse reflectance from the sample surface

### 2.4 Dip-Probe (Immersion)

- LED + detector housed in a probe that is dipped into the urine cup
- No cuvette required — sample volume is effectively infinite
- Path length defined by probe geometry
- **Advantages for Jimini:**
  - No capillary fill needed (gravity/surface tension not relied on)
  - No bubble risk
  - Easy cleaning between samples (wipe or rinse)
  - Path length variability possible by adjusting probe insertion depth
- **Disadvantages:** More difficult to maintain optical alignment; risk of contamination if not designed well; 90° fluorescence requires two optical fibres

**Commercial examples:** Ocean Insight UV-VIS Transmission Dip Probe (SMA 905, path length configurable), Edmund Optics UV-VIS Dip Probe ($1,339), Peek Dip Probes (Spectrecology, 300 µm fibres).

**Assessment for Jimini:** The dip-probe configuration eliminates the most difficult engineering challenges (capillary fill, bubble removal, cuvette alignment) at the cost of contamination risk and external optics bulk. For a pen device that is inserted into a urine cup, a dip-probe is architecturally natural.

### 2.5 Configuration Comparison

| Config | Absorbance | Fluorescence | Scatter | Bubble risk | Volume | Pen form? |
|---|---|---|---|---|---|---|
| Transmission | ★★★★★ | ✗ (needs 90°) | Poor (fwd scatter adds to T) | High | 10–100 µL | ★★★ |
| 90° Fluorescence | ✗ alone | ★★★★★ | ★★★ (90° = nephelometry) | Moderate | 10–100 µL | ★★★ |
| Dip-probe | ★★★★ | ★★★ (with 2nd fibre) | ★★★ | **None** | None (infinite) | ★★★★★ |
| Reflectance | ★★ | ★★ | ★★★ | None | ~1 µL | ★★★★ |

---

## 3. Optical Window & Cuvette Materials

### 3.1 The 275 nm Problem

At 275 nm (UV-C), most optical materials absorb significantly. Only a small set are UV-C transparent:

| Material | UV cutoff (nm) | Transparency at 275 nm | Notes |
|---|---|---|---|
| **UV-grade fused silica (Suprasil)** | ~150 nm | **Excellent (>90% T/mm)** | Standard for UV spectroscopy; low autofluorescence |
| **Crystal quartz** | ~150 nm | **Excellent** | Birefringent — avoid in polarized setups |
| **CaF₂** | ~120 nm | Excellent | Very low autofluorescence; expensive; fragile |
| **MgF₂** | ~110 nm | Excellent | Hard coating applications |
| **Sapphire (Al₂O₃)** | ~145 nm | Good | Very hard; expensive; slightly absorbs near 200 nm |
| **Borosilicate glass (Pyrex)** | ~310 nm | **Zero** | Completely opaque at 275 nm |
| **Soda-lime glass** | ~350 nm | **Zero** | Opaque at 275 nm |
| **PMMA (acrylic)** | ~300 nm | **Zero** | Common plastic — unusable at 275 nm |
| **PDMS** | ~250 nm | **Zero at 275 nm** | Silicone — absorbs UV-C |
| **COC (Zeonex/Topas)** | ~260–280 nm | **Borderline** | Some grades cut off at 260 nm; COC Zeonex E48R down to 260 nm |
| **COP (Zeonex)** | ~260 nm | Marginal | Grade-dependent |
| **PTFE** | ~170 nm | **Excellent (diffuse reflector)** | Cannot use in transmission; ideal for integrating sphere interior |

**Implication:** Any window or cuvette wall that the 275 nm beam passes through **must be UV-grade fused silica or quartz**. PMMA, borosilicate, PDMS, and most engineering plastics are completely opaque at 275 nm.

For the 365/405/455/white/1070 nm LEDs, borosilicate, PMMA, COC, and most plastics are acceptable.

### 3.2 Autofluorescence

A secondary material concern is autofluorescence — especially for the fluorescence channels (ex365/em460, ex405/em620):

| Material | Autofluorescence at ex365 nm | At ex405 nm | Verdict for Jimini |
|---|---|---|---|
| UV-grade fused silica | **Extremely low** | Extremely low | ★★★★★ |
| Borosilicate glass | Low | Low | ★★★★ |
| PMMA | **HIGH** | High | ✗ for fluorescence |
| PDMS | High | Moderate | ✗ for fluorescence |
| COC | **Low** | Low | ★★★ |
| COP | Low | Low | ★★★ |

Piruska et al. (Lab on a Chip, 2005) systematically measured autofluorescence of plastic microfluidic chips under laser excitation — PMMA and polycarbonate have unacceptably high background; COC is the best plastic option.

### 3.3 Practical Material Strategy for Jimini

- **275 nm optical window:** UV-grade fused silica (1–2 mm thick, AR-coated at 275 nm if possible)
- **365/405/455 nm windows:** Fused silica or borosilicate (cost-performance balance)
- **1070 nm window:** Any glass or plastic (all transparent at 1070 nm)
- **Sample channel walls:** COC or glass — low autofluorescence, UV-transparent to ~260 nm
- **Avoid:** PDMS, PMMA, standard plastics anywhere in the UV optical path

---

## 4. Sample Introduction & Fluid Handling

### 4.1 Volume Requirements

| Configuration | Typical volume | Comment |
|---|---|---|
| Standard 10 mm cuvette | 500–3,000 µL | Way too large for pen device |
| Micro-cuvette (1 mm path) | 50–100 µL | Feasible |
| Capillary channel (0.5 mm × 5 mm × 2 mm path) | ~5 µL | Excellent for pen device |
| Dip-probe | 0 µL (infinite pool) | No volume consumption |
| Dipstick/surface contact | ~1–2 µL | Minimal but poor optical path control |

For a pen device, **5–50 µL** is a practical target volume. Urine provides ample volume; the constraint is minimizing dead volume and measurement time.

### 4.2 Sample Introduction Modes

#### Capillary Fill
- Sample drawn by capillary action into a micro-channel when the tip is dipped in urine
- Passive — no pump needed
- Requires: hydrophilic channel walls (contact angle < 30°), vent hole for air escape, channel geometry optimised for fill time (<5 sec)
- Smith et al. (Lab on a Chip 2016) demonstrated a micro-volume slipping manifold for urinalysis using capillary fill with ~2 µL sample
- **Challenge:** Surface tension depends on urine pH, surfactants, and protein concentration — fill behaviour can be inconsistent with abnormal urines

#### Pipette-Fill / Press-to-Fill
- User pipettes or squeezes a defined volume into a chamber
- More consistent than capillary fill
- Requires slightly more user action

#### Dip-and-Read
- Pen tip is simply dipped into the urine cup; the optical path is within the tip
- Most natural for a pen form factor
- No fill mechanism needed
- Path length defined by the probe geometry
- Examples: Sysmex UF-5000 dip-tube, standard dip-probe spectrometers

#### Flow-Through Cell
- Urine is actively pumped through the optical cell (microperistaltic pump, electroosmotic flow)
- Most controllable; enables multiple sequential measurements with rinse cycles
- Adds complexity and power consumption — less suitable for pen form factor

**Recommended for Jimini:** Dip-and-read with a defined-geometry optical tip. The sample is measured in situ. Clean between samples with a water rinse dip followed by air dry.

### 4.3 Fill Speed Calculation (Capillary)

For a rectangular channel (width $w$, height $h$, contact angle $\theta$):

$$l(t) = \sqrt{\frac{\gamma \cos\theta \cdot h}{3\eta} \cdot t}$$

For urine (η ≈ 1.1 mPa·s, γ ≈ 70 mN/m), a 0.5 mm × 0.5 mm channel with θ = 20° (hydrophilic COC):
- Fill to 5 mm in ≈ 0.5 seconds ✓
- Fill to 10 mm in ≈ 2 seconds ✓

Bubble inclusion risk increases with fill speed and channel corner features. Wider channels (>1 mm) fill faster but risk bubble trapping at corners.

---

## 5. Bubble Management

Bubbles are the primary cause of measurement failure in miniature liquid spectrophotometers. A single 0.5 mm bubble in a 2 mm path cell creates a local absorbance artefact of ~1 AU.

### 5.1 Why Bubbles Form

1. **Dissolved gas coming out of solution:** Urine warmed from refrigerator to room temperature releases dissolved CO₂ and N₂
2. **Capillary fill air pockets:** Corners, surface defects, and sudden channel expansions trap air during fill
3. **Turbulent fill:** High fill speed causes air entrainment
4. **Bacterial gas production:** Urease-producing bacteria release CO₂/NH₃ in alkaline urine

### 5.2 Prevention Strategies

| Strategy | Implementation | Effectiveness |
|---|---|---|
| **Hydrophilic coating** | PEG coating, plasma O₂ treatment of COC/PDMS, layer-by-layer PDADMAC/PSS | ★★★★ — contact angle <10° prevents corner trapping |
| **Degassing channel** | PDMS membrane permeable to dissolved gas upstream of optical cell | ★★★ — removes dissolved gas but adds length |
| **Slow fill / wick** | Channel geometry slows fill; absorbent pad draws sample gently | ★★★ — prevents turbulence |
| **Vent hole position** | Place vent at highest point of channel (gas rises) | ★★★★ — allows trapped air to escape |
| **Tapered channel entry** | Conical inlet smooths flow convergence | ★★★ |
| **Pre-wet** | Wetting with water/buffer before urine fill | ★★★★ — eliminates dry-surface trapping |
| **Detection & rejection** | Detect bubbles optically (A spike) or by light transmission drop; flag measurement | ★★★★★ — quality check always needed |

### 5.3 Bubble Detection

A bubble passing through the optical path causes:
- Sharp spike in apparent absorbance (A → ∞ during bubble passage)
- Characteristic temporal signature: fast rise, plateau, fast fall
- Asymmetric effect: larger at long wavelengths where urine is more transparent (bubble appears as white space)

**Algorithm:** Monitor A(1070 nm) (urine is minimally absorbing here); any value > 2.5 AU or temporal spike > 0.5 AU/ms indicates a bubble. Flag and repeat measurement.

---

## 6. LED-to-Sample Optical Coupling

### 6.1 Free-Space vs Fibre-Optic

#### Free-Space Coupling
- Direct line-of-sight from LED to sample channel
- LED mounted on PCB, sample channel aligned mechanically to LED axis
- Simple, no fibre losses, preserves LED emission pattern
- Requires precise mechanical alignment (±0.1 mm for 1 mm channel)
- Challenging for 275 nm: stray UV from LED housing can reach detector via unwanted paths

#### Fibre-Optic Coupling
- LED coupled into SMA-connector optical fibre; fibre routes to sample port and detector
- Advantages: flexible routing, separates LED PCB from optical head thermally, allows swappable tips
- Disadvantages: fibre transmission loss (~0.5–3 dB at 275 nm for UV-grade silica), mode scrambling, fibre degradation under UV-C
- **UV-grade silica fibres** are required for 275 nm (polymer fibres absorb UV-C completely)
- The open-source fibre-based portable spectrometer (Tunens et al., HardwareX 2024) demonstrated SMA905 coupling with a C12880MA — a practical reference design

#### Collimating Lens
- A small plano-convex lens (f = 5–15 mm) collimates the LED emission into the sample
- Reduces divergence from ~±60° to <±5°, dramatically improving throughput into a 1–2 mm channel
- Material requirement: UV-grade fused silica or CaF₂ for 275 nm
- LBTEK and Ocean Insight both offer 5 mm diameter collimating lenses for SMA fibres (F240SMA-UV, etc.)

### 6.2 LED Placement Geometry

The multi-wavelength deep-UV absorbance detector (ScienceDirect 2023) demonstrated a flow cell design with pulsed LED multiplexing: each LED fires in sequence, allowing a single detector to measure all wavelengths sequentially without optical switching elements.

**Jimini architecture consideration:**
```
LED bank (275, 365, 405, 455, white, 1070 nm)
  → Individual collimating lenses
  → Dichroic combiner or time-multiplexing
  → Common entrance window
  → Sample cell (2–5 mm path)
  → Exit window
  → Fibre-coupled to C12880MA (340–850 nm) and C14384MA (640–1050 nm)

Perpendicular axis (90°):
  → Fluorescence collection lens
  → Longpass filter (>450 nm for ex365, >450 nm for ex405 blocks excitation leakage)
  → To C12880MA detector (broadband fluorescence emission)
```

### 6.3 Collimation Requirements

Poorly collimated light in a short path cell causes two problems:
1. **Non-uniform path length:** Light at oblique angles traverses more than the nominal path length $l$, giving apparent A > true A (apparent path length error is $(l / \cos\theta) - l \approx \theta^2 l/2$ for small angles)
2. **Stray light in cell:** Divergent beam reflects from cell walls, increasing background

For a 2 mm path cell with ±5° divergence, path length error = (2 / cos 5°) - 2 = 0.008 mm = 0.4% — negligible.
For ±20° divergence, error = 2% — significant for high-precision quantification.

---

## 7. Stray Light Management

Stray light is unwanted light reaching the detector that did not pass through the sample at the correct wavelength. It **limits the maximum measurable absorbance** (typically to 2–3 AU for well-designed systems, less for poor designs).

### 7.1 Sources of Stray Light

1. **LED fluorescence / phosphorescence:** High-power LEDs emit at their rated wavelength plus a broader background from the package, phosphor, or carrier substrate. UV-C LEDs (275 nm) have a significant visible tail from carrier luminescence.
2. **Reflections from cell walls:** Light bouncing inside the cell before reaching the detector
3. **Detector spectral leakage:** C12880MA has finite out-of-band rejection; strong 275 nm illumination can leak into visible channels
4. **Ambient light:** Not critical if device is enclosed, but relevant for dip-probe designs
5. **Cuvette autofluorescence:** Material fluorescence (see Section 3.2) adds broadband background

### 7.2 Mitigation Strategies

| Source | Mitigation |
|---|---|
| **LED off-wavelength emission** | Bandpass filter on LED output; spatial separation between LEDs; black baffles between LED channels |
| **275 nm visible tail** | UVC bandpass filter centred at 275 nm (Semrock or Edmund Optics custom); absorbs the 300–700 nm tail while passing 275 nm |
| **Wall reflections** | Black-coated internal surfaces (black anodised aluminium, or matte black polymer); V-groove baffles; absorbing black paint on interior |
| **Stray light from one LED into another** | Black baffles; time-multiplexed firing (only one LED active at a time) — ensures detector always sees light from one source only |
| **Detector spectral leakage** | Longpass filter on detector input (e.g., 300 nm longpass for visible channels); grating dispersion in C12880MA provides intrinsic wavelength discrimination |
| **Ambient light** | Fully enclosed optical head; differential measurement (LED on minus LED off) — standard practice |

### 7.3 Differential Measurement Protocol

```
A_net(λ) = A(LED_on) - A(LED_off)
```

By subtracting the "LED off" background, ambient light and dark current are removed. The C12880MA integration time should be kept short (<10 ms) to minimise dark current accumulation. Time-multiplexed LED firing at ~100 Hz with phase-locked detection (lock-in amplifier or software lock-in) can dramatically improve SNR for weak fluorescence signals.

---

## 8. Multi-Angle Measurement

### 8.1 Scatter vs Absorption Discrimination

In turbid urine (WBCs, bacteria, crystals), the apparent absorbance measured in transmission includes both true molecular absorption AND scatter-induced attenuation. These cannot be separated with a single transmission measurement.

Three measurement geometries provide complementary information:

| Geometry | What it measures | Physical process |
|---|---|---|
| **0° (transmission)** | Absorbed + scattered light (apparent extinction) | $\mu_t = \mu_a + \mu_s$ |
| **90° (nephelometry)** | Light scattered sideways by particles | Mie scatter intensity |
| **180° (backscatter)** | Backscattered light from particles/cells | Mie backscatter |

The relationship: $\mu_a = \mu_t - \mu_s$, so if scatter ($\mu_s$) is measured independently at 90°, true absorption can be extracted.

### 8.2 Mie Scatter Wavelength Dependence

Scattering coefficient scales with particle size and wavelength:
- **Rayleigh regime** (particle << λ): $\mu_s \propto \lambda^{-4}$ (very steep wavelength dependence)
- **Mie regime** (particle ~λ): oscillating dependence; for bacteria (~1 µm) at 500 nm, $\mu_s \propto \lambda^{-2}$ approximately
- **Geometric optics** (particle >> λ): $\mu_s$ nearly wavelength-independent ($\lambda^0$)

| Particle type | Size | Scatter regime at 500 nm | $\lambda$ dependence |
|---|---|---|---|
| Protein aggregates | ~10 nm | Rayleigh | $\lambda^{-4}$ (very steep) |
| Bacteria | ~1 µm | Mie | $\lambda^{-1}$ to $\lambda^{-2}$ |
| WBCs | ~12 µm | Geometric | $\lambda^{-0.2}$ to $\lambda^0$ |
| Crystals | 10–100 µm | Geometric | $\lambda^0$ |

**Feature derived from multi-wavelength scatter:** The exponent $\alpha$ in $\mu_s \propto \lambda^{-\alpha}$ (from $\log A_{400} - \log A_{800}$) encodes information about the dominant scatterer size. This is a physically grounded feature for discriminating particle types.

### 8.3 Practical Multi-Angle Implementation for Jimini

A 90° scatter detector can be implemented with:
- A second photodiode (e.g., silicon PIN diode) mounted perpendicular to the optical axis
- A side-viewing fibre port leading to C12880MA (for full spectral scatter profile)
- A dedicated nephelometer element using 850–1070 nm (outside the absorption bands of most urine chromophores)

**Minimum addition to Jimini:** A single silicon photodiode at 90° to the 1070 nm LED beam, measuring near-IR nephelometric scatter. This provides:
- Turbidity measurement in NTU (calibrated against formazin standards)
- Scatter decoupled from 1070 nm absorption
- Enables correction of 0° transmission measurements for scatter contribution

---

## 9. Reference Measurement Strategy

### 9.1 Why Reference Measurement is Critical

The Beer-Lambert law requires a reference ($I_0$) measurement:
$$A = -\log_{10}(I_\text{sample}/I_0)$$

In a pen device, LED intensity varies with temperature, age, and drive current. A reference taken at the start of a measurement session may be invalid if temperature changes between reference and sample.

### 9.2 Reference Strategies

#### Water Blank at Measurement Time
- Most accurate: measure deionised water in the same cuvette immediately before the sample
- Cancels LED drift, detector drift, path length variations
- Requires sample exchange — adds ~10–30 seconds to workflow
- Practical for clinical settings with cuvette tips

#### Internal Reference Channel
- Split a fraction of LED light to a reference photodiode before it enters the sample
- Monitor LED intensity continuously; normalise sample signal in real time
- Does NOT correct for cuvette-to-cuvette path length variation
- Standard in laboratory spectrophotometers (dual-beam design)
- Implementation: a beamsplitter or partially reflective surface before the sample cell

#### Air Reference + Water Calibration Factor
- Measure air transmission; apply a stored correction factor for water vs air
- Least accurate; correction factor drifts with temperature
- Only acceptable if device temperature is well-controlled

#### In-Situ Water Rinsing Reference
- After each sample, rinse the cell with deionised water; measure water as $I_0$ before ejecting
- Reference is taken just after sample, in the same optical configuration
- Most practical for dip-probe design: dip in water cup → measure → dip in urine → measure

### 9.3 Temperature Compensation

LED emission wavelength shifts with temperature (~0.06 nm/°C for InGaN, ~0.1 nm/°C for AlGaInP). For the 275 nm LED, this is:
- At ±10°C shift: ±0.6 nm wavelength shift
- At 275 nm, uric acid absorption slope: ~800 AU/(M·nm)
- Effect on A at 5 mmol/L uric acid: ±0.4 AU/°C × 0.06 ≈ ±0.025 AU/°C

This is detectable. Temperature monitoring (±1°C accuracy) with a lookup table correction for LED wavelength is recommended.

---

## 10. Cleaning & Cross-Contamination

### 10.1 Clinical Risk

Carryover is a known problem in automated urine analyzers. Vurgun et al. (2016) documented false-positive haematuria in consecutive urinalysis samples due to hemoglobin carryover in the flow cell. At 5 ppm carry-over and a hemoglobin sample at 50 µmol/L, the next sample sees 0.25 nmol/L — below detection threshold. But at 500 µmol/L (gross haematuria), carryover at 5 ppm gives 2.5 nmol/L — still detectable (above Soret LOD).

### 10.2 Disposable Tip Design (Preferred)

The cleanest approach: **disposable single-use optical tips** containing the sample chamber and optical windows. The pen body (LEDs, detectors, electronics) is reusable; the tip containing any contaminated surfaces is discarded.

- Cost target: <€0.50/tip (moulded COC/COP + fused silica windows press-fit)
- Precedents: HemoCue microcuvettes (capillary-fill disposable), Abaxis Piccolo cuvette rotors, BD FACS disposable sample chambers

### 10.3 Reusable Tip with Cleaning Protocol

If tips are reusable (cost or usability reasons):

1. **After each measurement:** Dip in deionised water × 2; dip in 70% ethanol × 1; air dry (5 seconds with warm air jet or passive evaporation)
2. **Weekly deep clean:** 1% Tergazyme enzymatic cleaner, 10 min soak; rinse ×3 DI water
3. **Carryover test:** Run DI water blank after a high-bilirubin sample; check $A_{453} < 0.005$ AU before next sample

### 10.4 Surface Chemistry

Quartz and fused silica surfaces adsorb proteins, haemoglobin, and bilirubin. Surface passivation with PEGylation (mPEG-silane, 2 kDa) reduces protein adsorption by >90% and extends the useful life of reusable cuvettes.

---

## 11. Prior Art

### 11.1 Published Designs with C12880MA

**SpectraPhone (2026, Nature Sci. Rep.):** Smartphone-integrated portable spectrometer for urinalysis. Custom lens array and hyperspectral illumination source. Multi-angle, multi-exposure acquisition. 288 channels at 340–850 nm. Key optical design detail: the illumination source is decoupled from the spectrometer (external LED + fibre to sample, separate collection fibre to C12880MA). This decoupling simplifies stray light management significantly.

**Hamamatsu Low-Cost Setup (2017, Gary Spingarn):** Arduino-based integration of C12880MA with a simple transmission flow cell. Demonstrates that C12880MA can be operated in bare-metal STM32/Arduino mode without a dedicated eval board. The optical design is a black-box Lego-style holder with an LED on one side and C12880MA on the other — minimal but functional.

**Sensors Paper (2024, MDPI Sensors 24/19/6445):** Full characterization of C12880MA for water surface reflectance; includes drive circuit analysis and calibration methodology for the analog CLK-based interface. Relevant for Jimini's STM32 integration.

### 11.2 Published Multi-LED Absorbance Detectors

**Multi-wavelength deep-UV detector (ScienceDirect 2023):** Multi-LED deep-UV detector (4 LEDs, 200–275 nm range) with a single fibre-optic flow cell. LEDs are pulsed sequentially by a RedPitaya controller. Demonstrates that time-multiplexed multi-LED absorbance detection with a single detector is practical and achieves sub-mAU sensitivity. The optical design uses individual collimating lenses per LED, combined into a single fibre.

**Portable micro-volume spectrophotometer (AIMS Bioengineering 2026):** ML-driven computational correction for a portable micro-volume spectrophotometer for biochemical analysis. Path length 0.5–2 mm, UV-Vis LEDs 260–700 nm. Demonstrates that computational correction (ML-based Beer-Lambert inversion) can compensate for optical imperfections in low-cost portable designs.

### 11.3 Portable Urinalysis Devices

**Urine Analyzer via Portable UV Spectrophotometry (Sensors 2022):** Label-free uric acid in spot urine using a portable UV spectrophotometer. 275 nm LED, quartz cuvette (1 cm path). Demonstrates reagent-free uric acid measurement. Key finding: the 1 cm path saturates at high uric acid concentrations in concentrated morning urines — argues for ≤2 mm path for UV channel.

**HemoCue Glucose 201:** Disposable microcuvette with integrated dry reagent. Capillary fill, ~5 µL sample. Demonstrates the disposable micro-cuvette model at scale. Path length: defined by the microcuvette cavity geometry (~0.5 mm effective optical path after accounting for reagent layer).

**Broadband Cavity-Enhanced UV-VIS for pL samples (RSC Analyst 2023):** Demonstrates optical cavity enhancement to increase effective path length in picolitre volumes. Relevant for extremely small sample volumes but not for pen-sized device architectures.

### 11.4 Key Patents

- **US8747779 (Micronics):** Microfluidic clinical analyzer with on-board dry reagents and spectrophotometric detection. Describes docking interface, pneumatic fill, and spectrophotometric flow cell geometry.
- **WO2005/066638:** Microfluidic cartridge for clinical analyte determination from µL samples, spectrophotometric monitoring.

---

## 12. Recommended Design for Jimini

Based on the literature synthesis, the following design is recommended:

### 12.1 Sample Interface: Dip-and-Read with Disposable Tip

```
┌─────────────────────────────────────────────────────┐
│                  JIMINI PEN BODY                     │
│  [LED PCB] [EIS electrodes] [STM32] [Battery]       │
│       │                                              │
│   [collimating optics assembly]                      │
│       │                                              │
│   ┌───┴───────────────────────────────────────┐     │
│   │         DISPOSABLE TIP (COC + quartz)      │     │
│   │                                            │     │
│   │  ┌──────────────┐   ┌──────────────────┐  │     │
│   │  │ UV window    │   │  Fluorescence    │  │     │
│   │  │ (fused SiO₂) │   │  window (SiO₂)  │  │     │
│   │  │  275 nm beam │   │  90° collection  │  │     │
│   │  └──────┬───────┘   └────────┬─────────┘  │     │
│   │         │  2 mm path         │            │     │
│   │      ┌──┴───────────────┐    │            │     │
│   │      │   SAMPLE ZONE   │    │            │     │
│   │      │  (COC channel,  │────┘            │     │
│   │      │   PEG-coated)   │                 │     │
│   │      └──────────────────┘                │     │
│   │  EIS electrodes embedded in channel walls │     │
│   └───────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
```

### 12.2 Optical Design Summary

| Parameter | Specification | Rationale |
|---|---|---|
| **Sample cell material** | COC (Zeonex E48R) channel, UV-grade fused silica windows | COC: low autofluorescence, UV to 260 nm, injection-mouldable. Quartz windows for 275 nm |
| **Path length (UV)** | **2 mm** | Beer-Lambert linear for uric acid up to ~4 mmol/L; avoids saturation |
| **Path length (Vis/NIR)** | **5 mm** (if separate chamber) | Better sensitivity for porphyrins, bilirubin at clinical levels |
| **90° fluorescence port** | Yes — fused silica window, longpass filter (>450 nm) | ex405/em620 porphyrin; ex365/em460 NADH |
| **Nephelometry (scatter)** | 90° silicon photodiode at 1070 nm | Independent turbidity measurement for WBC/bacteria/crystals |
| **LED coupling** | Collimating lens (f=5 mm, UV-grade SiO₂) per UV LED; fibre bundle for visible | Reduces divergence to <±5°; enables flexible routing |
| **Stray light control** | Black-anodised aluminium housing; time-multiplexed LED firing; BPF on 275 nm LED output | Eliminates cross-channel stray light |
| **Reference** | Water blank measured in same tip before sample (dip-in-water-first protocol) | Compensates LED drift and path length variation |
| **Bubble detection** | Monitor A(1070 nm) > 2.5 AU → flag and discard | Real-time quality check |
| **Sample volume** | ~5–20 µL drawn into channel, OR infinite (dip-probe mode) | No volume constraint with urine |
| **Tip design** | Disposable, moulded COC, press-fit fused silica windows, EIS electrodes patterned | <€0.50/tip target; eliminates carryover |
| **Temperature monitoring** | On-tip NTC thermistor | LED wavelength drift compensation |

### 12.3 Critical Design Trade-offs

1. **Single vs dual path length:** A dual-chamber tip (2 mm for UV, 5 mm for Vis/fluorescence) adds manufacturing complexity but solves the dynamic range problem cleanly. Start with 2 mm for prototyping; add 5 mm chamber when scatter/porphyrin performance needs improvement.

2. **Fibre bundle vs free-space:** Free-space is simpler and lower-loss but harder to align. Fibre bundles add flexibility and allow the LED PCB to be separated from the optical head thermally. For prototype, start free-space; move to fibre bundle for final product.

3. **Disposable vs reusable tip:** Disposable eliminates carryover and cleaning protocol but adds recurring cost. Given the clinical context (urine — biohazard) and the regulatory benefit of disposable tips, disposable is strongly preferred.

4. **90° fluorescence — single detector:** The C12880MA detector can capture both transmission (via beamsplitter) and 90° fluorescence (via separate collection port) if the optical head has two input ports — one for each optical axis. The C12880MA's internal diffraction grating then provides spectral discrimination of both signals.

---

## 13. Sources

| Source | URL |
|---|---|
| Beer-Lambert path length selection (Agilent) | [agilent.com](https://www.agilent.com/cs/library/technicaloverviews/public/te-cary-3500-uv-vis-variable-path-length-cell-holder-5994-5781en-agilent.pdf) |
| Hellma TrayCell 2.0 micro-volume cuvette | [hellma-worldwide.com](http://www.hellma-worldwide.com/en/cuvettes-laboratory-supplies/micro-volume-analysis-traycell-20/faq) |
| Eppendorf µCuvette G1.0 (1 mm, 1.5 µL) | [eppendorf.com](https://www.eppendorf.com/fi-en/Products/Photometry/Cuvettes/Eppendorf-Cuvette-G10-p-PF-56120) |
| Eppendorf µCuvette whitepaper | [news-medical.net](https://www.news-medical.net/whitepaper/20151120/Highly-Precise-Photometric-Measurements-of-Nucleic-Acids-or-Proteins-using-Eppendorf-c2b5Cuvette-G10.aspx) |
| Variable path length / slope spectroscopy (ScienceDirect 2021) | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0263224120308095) |
| Ultra-broad dynamic range slope method (Anal. Chem. 2025) | [pubmed.ncbi.nlm.nih.gov/40193700](https://pubmed.ncbi.nlm.nih.gov/40193700/) |
| Multi-LED deep-UV absorbance detector (ScienceDirect 2023) | [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0021967323006076) |
| Optical fibre portable spectrometer (HardwareX 2024) | [pmc.ncbi.nlm.nih.gov/articles/PMC11046214](https://pmc.ncbi.nlm.nih.gov/articles/PMC11046214/) |
| Portable micro-volume spectrophotometer ML (AIMS Bioengineer. 2026) | [aimspress.com](https://www.aimspress.com/article/doi/10.3934/bioeng.2026005?viewType=HTML) |
| SpectraPhone urinalysis (Nature Sci. Rep. 2026) | [nature.com](http://www.nature.com/articles/s41598-026-38307-y) |
| C12880MA characterisation for water spectroscopy (MDPI Sensors 2024) | [pubmed.ncbi.nlm.nih.gov/39409485](https://pubmed.ncbi.nlm.nih.gov/39409485/) |
| C12880MA low-cost setup (Hamamatsu 2017) | [hamamatsu.com](https://www.hamamatsu.com/eu/en/news/featured-products_and_technologies/2017/20170510045200.html) |
| C12880MA product page (Hamamatsu) | [hamamatsu.com](https://www.hamamatsu.com/eu/en/product/optical-sensors/spectrometers/mini-spectrometer/C12880MA.html) |
| Bilirubin optical assay in blood (arXiv 2024) | [ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu/abs/2024arXiv240614816N/abstract) |
| Portable UV uric acid in spot urine (Sensors 2022) | [mdpi-res.com](https://mdpi-res.com/d_attachment/sensors/sensors-22-03009/article_deploy/sensors-22-03009-v2.pdf) |
| Capillary-driven microfluidics review (RSC Analyst 2023) | [pubs.rsc.org](https://pubs.rsc.org/en/content/articlehtml/2023/an/d3an00115f) |
| PDMS-PEG hydrophilic capillary flow (MDPI Sensors 2025) | [mdpi.com/1424-8220/25/2/411](https://www.mdpi.com/1424-8220/25/2/411) |
| Plastic microfluidic chip autofluorescence (Lab on a Chip 2005) | [pubs.rsc.org](https://pubs.rsc.org/en/content/articlelanding/2005/lc/b508288a/unauth) |
| Microfluidic chip material comparison (Blacksheep Sciences) | [blacksheepsciences.com](https://www.blacksheepsciences.com/publications/choosing-materials-for-microfluidic-chips) |
| UV optical materials: fused silica, CaF₂ | [mirrorganize.com](https://www.mirrorganize.com/news/optical-materials-in-the-deep-ultraviolet-band.html) |
| CVI Melles Griot optical material properties | [idexot.com](https://www.idexot.com/media/wysiwyg/04_Material_Properties.pdf) |
| PTFE UV reflectance (Porex Corporation) | [porex.com](https://www.porex.com/wp-content/uploads/2020/04/Ultraviolet-Reflectance-of-Microporous-PTFE.pdf) |
| UV-VIS dip probe (Edmund Optics) | [edmundoptics.com](https://www.edmundoptics.com/p/uv-vis-transmission-dip-probe/56990/) |
| Micro-volume slipping manifold for urinalysis (Lab on a Chip 2016) | [pubs.rsc.org](http://pubs.rsc.org/en/content/articlelanding/2016/lc/c6lc00340k) |
| Carryover in urine analyzers (De Gruyter 2016) | [degruyter.com](https://www.degruyter.com/document/doi/10.1515/tjb-2016-0162/html) |
| Broadband cavity-enhanced UV-VIS for pL volumes (RSC Analyst 2023) | [pubs.rsc.org](https://pubs.rsc.org/en/content/articlehtml/2023/an/d3an00143a) |
| Microfluidic clinical analyzer patent US8747779 | [freepatentsonline.com](https://www.freepatentsonline.com/8747779.html) |
