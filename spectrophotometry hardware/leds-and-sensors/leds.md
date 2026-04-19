---
title: UV and Specific-Wavelength LEDs for Portable Spectrophotometry
aliases:
  - Jimini LEDs
  - LED Selection
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# UV and Specific-Wavelength LEDs for Portable Spectrophotometry

Detailed per-wavelength LED review for the Jimini pen spectrophotometer. For summary tables and selection guidance see [[spectrophotometry hardware/leds-and-sensors/overview]]; for optical design context see [[optical-path-design]].

---

## 275 nm UV-C

**Technology:** AlGaN (aluminium gallium nitride) or AlN. Deep UV-C. Requires SiC or sapphire substrate. Wall-plug efficiency typically 3–7% — these LEDs are power-hungry for what they output, and heat management is critical.

> [!WARNING]
> UVC (100–280 nm) is highly damaging to skin and eyes. All UVC work requires UV-blocking eye protection, gloves, and enclosed optical paths. No bare-eye observation even briefly.

### Seoul Viosys — CUD7GF1B (Top Pick for Exact 275 nm)

| Parameter | Value |
|-----------|-------|
| **Part Number** | CUD7GF1B |
| **Series** | CA3535 |
| **Peak Wavelength** | 275 nm (270–278 nm range) |
| **Radiant Power** | 16 mW @ 100 mA (typ) |
| **Forward Voltage** | 5.6 V @ 100 mA |
| **Max Current** | ~100 mA continuous |
| **FWHM** | **11 nm** (datasheet confirmed, Δλ @ IF=100 mA) |
| **Beam Angle** | 125° |
| **Package** | SMD 3535 (3.5 × 3.5 mm) ceramic, flat |
| **Window** | Quartz (required for UV-C transmission) |

Where to buy:
- DigiKey: `2112-CUD7GF1BCT-ND` — ~**$7.78** (1 pcs), in stock ~294 pcs
- RS Components: RS Stock No. 247-1977
- BeamQ: ~$6.90

Datasheet: [CUD7GF1B Datasheet v1.91](https://www.neumueller.com/datenblatt/seoulviosys/CUD7GF1B_210624_R1.91.pdf)
Notes: Most straightforward SMD part at exactly 275 nm with reasonable power for spectrophotometry. Available through standard distributors. Ceramic SMD 3535 is reflow-solderable.

---

### Bolb Inc. — S6060 (Highest Power)

| Parameter | Value |
|-----------|-------|
| **Part Number** | S6060 |
| **Peak Wavelength** | 268–275 nm (typ 275 nm; range 263–280 nm max) |
| **Radiant Power** | **100 mW @ 250 mA** (typ); 140 mW @ 350 mA |
| **Forward Voltage** | 6.5 V (typ), 5.8–7.5 V range |
| **Max Current** | 350 mA DC, 500 mA pulsed |
| **FWHM** | ~10 nm |
| **Beam Angle** | 150° (Lambertian) |
| **Package** | **6060 SMD (6 × 6 mm)**, industry standard |
| **Thermal Resistance** | 8 °C/W (junction-to-board) |
| **Lifetime** | L70 ≥ 8,000 hrs (certified), targeted 10,000 hrs |
| **Wall-Plug Efficiency** | ~7% (world's highest single-chip UVC) |

Where to buy: Direct from Bolb or distributors (contact bolb.co). Not stocked by Mouser/DigiKey in standard quantities.
Price: ~$15–25 (estimated, qty-dependent).

Notes: Highest power single-chip UVC LED available. The 6 × 6 mm footprint is manageable for a PCB but larger than the 3535 parts. For spectrophotometry, the 100 mW output is overkill — useful if you're pulsing at low duty cycle. Junction temp limit is only 75 °C, so thermal design is critical.

---

### Bolb Inc. — S3535 (Mid Power, Smaller Package)

| Parameter | Value |
|-----------|-------|
| **Part Number** | S3535 |
| **Peak Wavelength** | ~275 nm |
| **Radiant Power** | 40 mW |
| **Package** | SMD 3535 (3.5 × 3.5 mm) |

Where to buy: Ledrise (EU): ~**€13.57** (in stock >100 pcs)
Notes: Good balance of power and package size. Same footprint as the Seoul Viosys CUD7GF1B.

---

### Würth Elektronik — WL-SUMW Series

| Part No. | Power | Voltage | Package | Notes |
|----------|-------|---------|---------|-------|
| **15335327BA252** | **15 mW** | **6 V** | 3535 SMD | Recommended; catalog part at RS, Distrelec |
| **15335327BA250** | 3 mW | ~5.5 V | 3535 SMD | Low-power variant |

Where to buy:
- RS Components (UK/DE): RS# 228-0373 (BA252), 228-0372 (BA250)
- Distrelec: 302-73-943 (BA252)

Price: ~£4–8 (BA252 at RS)

Notes: Würth's WL-SUMW series is well-documented with full Würth datasheets and excellent application notes. Good choice for European sourcing. 120° beam angle, AlGaN technology.

---

### Crystal IS / Asahi Kasei — Klaran Series

| Series | Peak λ | Power Options | Package |
|--------|--------|---------------|---------|
| **Klaran WD** | **260–270 nm** | >50, 60, 70, 80 mW @ 500 mA | SMD 3535 |
| **Klaran LA** | **260–270 nm** | Various bins | SMD 3535 |

> [!CAUTION]
> Crystal IS Klaran products peak at **260–270 nm**, NOT 275 nm. Their AlN-based technology is optimized for germicidal UV (260–265 nm is the DNA absorption peak), not 275 nm. Do not specify Klaran for a 275 nm application. The Klaran `OP275-10P-SM` part exists (per Shengyu/global distributors) as a custom/catalog part at 275 nm with 10 mW, but availability is limited.

Where to buy (Klaran WD/LA): CDI LED (cdi.com), per request; not standard Mouser/DigiKey catalog.

---

### 275 nm Summary Recommendation

| Priority | Part | Rationale |
|----------|------|-----------|
| **Best for PCB prototyping** | Seoul Viosys CUD7GF1B | Standard distributor (DigiKey), well-documented, exact 275 nm |
| **Best power** | Bolb S6060 | 100 mW, 7% WPE — use pulsed to manage heat |
| **European sourcing** | Würth 15335327BA252 | RS Components, 15 mW, catalog part |

---

## 365 nm UV-A

**Technology:** InGaN or GaN. 365 nm is well-established, high-yielding technology. Many suppliers, good power levels. Used for [[nadh|NADH]]/NADPH fluorescence excitation (~340 nm abs, ~460 nm emission) and riboflavin excitation.

> [!NOTE]
> 365 nm is at the very edge of the [[nadh|NADH]] absorption band (~340 nm). For optimal [[nadh|NADH]] excitation, 340 nm is ideal, but 365 nm is a practical compromise with far better LED availability and power. Riboflavin absorbs strongly at 370 nm and 450 nm — 365 nm is a good match.

### Seoul Viosys — CUN66A1F (Recommended)

| Parameter | Value |
|-----------|-------|
| **Part Number** | CUN66A1F |
| **Series** | Z5 series |
| **Peak Wavelength** | 365 nm |
| **Radiant Power** | **420 mW @ 250 mA** |
| **Forward Voltage** | 3.6 V (typ) |
| **Max Current** | 250 mA (consult datasheet) |
| **FWHM** | ~12 nm (estimated, typical UV-A InGaN) |
| **Beam Angle** | 120° |
| **Package** | SMD 3535 Dome (3.5 × 3.5 mm) |

Where to buy:
- LEDs.de (EU): ~€8–12
- BeamQ (CUN66A1G variant): ~$9.95

Notes: Dome-top 3535 package. The Z5 series from Seoul Viosys is a high-efficiency UV-A family with multiple power bins. 420 mW from a 3535 package is excellent for fluorescence excitation. The dome increases coupling efficiency into optical fibers.

---

### Nichia — NVSU233B-U365 / NVSU233C-D4 (High Power)

| Parameter | NVSU233B-U365 | NVSU233C-D4 (U365) |
|-----------|--------------|---------------------|
| **Peak Wavelength** | 365 nm | 365 nm |
| **Radiant Power** | **1450 mW @ 1000 mA** | (similar class) |
| **Forward Voltage** | 3.85 V @ 1000 mA | ~3.8 V |
| **FWHM** | **9.0 nm** (datasheet confirmed) | ~9–12 nm |
| **Max Current** | 1400 mA | 1400 mA |
| **Package** | SMD 3535 | SMD 3535 (3.5 × 3.5 × 2.73 mm) |
| **Status** | Production | ★ Recommended model (2022+) |

Where to buy:
- Nichia directly or authorized distributors (Mouser, Digi-Key — search NVSU233B or NVSU233C)
- Enrgtech (UK): NVSU233A-U365 ~£15–20

Datasheet (NVSU233B): [Nichia PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233B(T)-E(4890F)U365x%20U385x%20U395x.pdf)

Notes: Nichia 233-series is a workhorse UV-A platform with multiple wavelength bins (U365, U385, U395, U405). The 9 nm FWHM is unusually narrow for UV-A LEDs — good spectral purity. 1450 mW is far more than needed; use at reduced current (50–100 mA) for spectrophotometry to extend lifetime and reduce heating.

### 365 nm Summary Recommendation

| Use Case | Part |
|----------|------|
| Low-power fluorescence excitation | Seoul Viosys CUN66A1F (run at 50–100 mA, ~150–200 mW) |
| High-intensity application | Nichia NVSU233C-D4 at U365 (run at 100 mA, ~200 mW) |

---

## 405 nm Violet

**Technology:** InGaN. This is the Blu-ray disc wavelength — extremely well-developed technology. High efficiency, very good power levels. Porphyrin Soret band centers ~410 nm (HbO2) and ~405 nm (for general [[total-urinary-porphyrin|porphyrins]]); 405 nm is also bilirubin's secondary absorption peak.

### Nichia — NVSU233C-D4 (405 nm bin) (Recommended)

| Parameter | Value |
|-----------|-------|
| **Part Number** | NVSU233C-D4 (U405) |
| **Peak Wavelength** | 405 nm |
| **Radiant Power** | ~1400–1600 mW @ 1000 mA (estimated from 405 nm bin) |
| **Forward Voltage** | ~3.75 V @ 1000 mA |
| **FWHM** | ~12 nm (estimated from NVSU233 series datasheet) |
| **Max Current** | 1400 mA |
| **Package** | SMD 3535 (3.5 × 3.5 × 2.73 mm) |
| **Status** | Recommended (2022) |

Datasheet: [NVSU233C-D4 PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233C(T)-D4-E(6608B)U365x%20U385x%20U395x%20U405x.pdf)
Where to buy: Nichia distributors (Mouser, DigiKey, RS)

Notes: The NVSU233C-D4 is a multi-bin part — specify U405 when ordering. The same physical LED can be ordered at 365, 385, 395, or 405 nm bins. Extremely high power for spectrophotometry — operate at 50–100 mA for sensing.

### Nichia — NCSU035D (405 nm, Larger Package)

| Parameter | Value |
|-----------|-------|
| **Part Number** | NCSU035D |
| **Peak Wavelength** | 405 nm |
| **Package** | 6.8 × 6.8 × 1.9 mm (custom larger SMD) |
| **Status** | In production (older model, not recommended for new designs) |

Notes: Larger footprint than 3535. The NVSU233C-D4 is the newer recommended replacement.

### 405 nm Summary Recommendation

| Use Case | Part |
|----------|------|
| **New design** | Nichia NVSU233C-D4 (U405 bin) — best-in-class, available |

---

## 455 nm Blue

**Technology:** InGaN. Standard blue LED wavelength range. Very mature, high efficiency. Bilirubin absorbs at 454 nm (primary peak); [[fad|FAD]] absorbs at 450 nm. 455 nm is an excellent match for both.

### Lumileds — LUXEON Z LXZ1-PR01 (Recommended for Compact PCB)

| Parameter | Value |
|-----------|-------|
| **Part Number** | LXZ1-PR01 |
| **Series** | LUXEON Z |
| **Peak Wavelength** | ~450 nm |
| **Dominant Wavelength** | 447.5 nm (440–460 nm range) |
| **Max Current** | 1000 mA |
| **Forward Voltage** | 3.0 V (typ) |
| **Beam Angle** | 125° |
| **Package** | **0705 (1713 metric)** — ultra-compact 1.7 × 1.3 mm footprint |

Where to buy:
- RS Components: RS# 923-1130 (MT), 768-2359 (MY)
- Mouser, DigiKey (search LXZ1-PR01)
- xonelec.com: ~**$1.44–3.44** (qty 1–24k)

Notes: The LUXEON Z is extremely compact for a pen-sized instrument. 0705 package is 1.7 × 1.3 mm — the smallest high-power LED footprint available from a tier-1 vendor. Note: peak is ~450 nm, not exactly 455 nm. For bilirubin sensing at 454 nm, this is effectively equivalent.

---

### ams OSRAM — Golden Dragon Plus LD W5KM-1T4T (455 nm)

| Parameter | Value |
|-----------|-------|
| **Part Number** | LD W5KM-1T4T-35 |
| **Series** | Golden Dragon Plus |
| **Peak Wavelength** | **455 nm** (449–461 nm range) |
| **Radiant Power** | 493 mW @ 1 A (355–630 mW range) |
| **Forward Voltage** | 3.2 V |
| **Max Current** | 350 mA (rated), 1 A pulsed |
| **Beam Angle** | 170° (Lambertian) |
| **Package** | Gull-wing SMD |

Where to buy: Mouser, DigiKey, pneda.com
Notes: This part hits exactly 455 nm. The Golden Dragon family is a well-proven OSRAM line. Gull-wing package is slightly more complex to solder than flat-land 3535, but standard reflow works.

### 455 nm Summary Recommendation

| Priority | Part | Notes |
|----------|------|-------|
| **Compact PCB (pen form factor)** | Lumileds LXZ1-PR01 | 1.7 × 1.3 mm, ~450 nm, ~$1.44 qty |
| **Exact 455 nm** | OSRAM LD W5KM-1T4T | 493 mW, 455 nm exact bin |

---

## Broadband White (High CRI)

Application: Spectrally flat reference illuminant for broadband absorption measurements. For spectrophotometry, spectral flatness (flat SPD across 400–700 nm) matters more than lumens. High CRI (>95) correlates with broad, smooth spectral coverage.

**Key metric:** CRI is a proxy for spectral coverage. CRI 99 means the spectrum hits R1–R15 reference colors accurately, implying minimal dips across 400–700 nm. Standard blue-converted white LEDs have a strong dip in the blue-green (490–510 nm) region.

### Nichia Optisolis — NFSW757G Series

| Parameter | Value |
|-----------|-------|
| **Series** | Optisolis™ |
| **Part Number (example)** | NFSW757G-V1 |
| **CRI (Ra)** | **98–99** (all 16 R-samples ≥ 90) |
| **R9** | ≥ 70 (saturated red — key indicator) |
| **Spectral Coverage** | 400–700 nm continuous, closest to D65/D50 illuminant |
| **Package** | **3030 SMD (3.0 × 3.0 mm)**, 757 platform |
| **Forward Voltage** | ~3.0–3.2 V (typical) |
| **UV emission** | **Essentially zero** (critically important for urine analysis — prevents matrix fluorescence excitation from the white source) |

Where to buy:
- Nichia distributors (Mouser, DigiKey, Farnell, LEDrise EU)
- LEDrise EU: ~**€0.80–1.50** per unit at low quantities

Notes on spectral choice for spectrophotometry:
- Choose **4000K or 5000K** for flattest SPD across visible range
- The Optisolis spectrum avoids the "blue spike" that contaminates measurements in the 440–460 nm region with standard white LEDs
- No UV emission below ~400 nm prevents [[nadh|NADH]]/flavin autofluorescence from being excited by the white source itself

---

### Seoul Semiconductor SunLike — TRI-R Technology

| Parameter | Value |
|-----------|-------|
| **Technology** | Violet LED die + Toshiba TRI-R phosphor |
| **CRI (Ra)** | 97 (typ), on the Blackbody Locus |
| **Package options** | 3030 SMD (S1S0-3030), COB (13.5 × 13.5 mm COB variant S4SM-1063) |
| **Spectral advantage** | Uses **violet** pump die (not blue), so the spectrum truly spans from ~400 nm without the blue spike |

Where to buy:
- DigiKey carries Seoul Semiconductor / Seoul Viosys products
- Mouser
- Direct from Seoul Semiconductor distributors

Notes: SunLike uses a **violet pump die** rather than the standard blue die. This means the spectrum is continuous from 400 nm. Excellent for spectrophotometry applications where full visible range coverage is required. CRI 97 is slightly below Optisolis CRI 99, but the violet-based spectrum is arguably better for optical purity.

### Comparison: Optisolis vs SunLike

| Feature | Nichia Optisolis | Seoul SunLike |
|---------|-----------------|---------------|
| CRI | **99** | 97 |
| R9 (red saturation) | >70 | ~90+ |
| Pump die | Blue | **Violet** |
| 400–420 nm coverage | Minimal (blue die doesn't reach) | **Good** (violet die reaches) |
| UV bleed (<400 nm) | Essentially zero | Very low |
| Package options | 3030 SMD, COB | 3030 SMD, COB |
| Distributor availability | Excellent | Good |
| Price | ~€0.80–1.50 | ~$0.19–0.22 |

For spectrophotometry: SunLike's violet-based design gives better 400–420 nm coverage, which matters for porphyrin/bilirubin measurements. Optisolis has higher CRI score and better documentation. Either is far superior to standard white LEDs.

---

### Yuji APS 3030 — Newest Full-Spectrum (Best for Broadest Coverage)

| Parameter | Value |
|-----------|-------|
| **Series** | APS (Advanced Performance Spectrum) |
| **CRI (Ra)** | **>97** (guaranteed minimum) |
| **TM-30** | Rf 98 / Rg 100 |
| **Spectral Coverage** | **400–730 nm** continuous (40% broader than standard white LEDs) |
| **Package** | 3030 SMD (3.0 × 3.0 mm) |
| **Drive Current** | 100 mA rated |
| **Forward Voltage** | 8.6–9.2 V |

Where to buy: [yujiintl.com](https://www.yujiintl.com/aps-3030-0-9w/) — direct; also via MARL International

Notes: The APS series extends to **730 nm** — most white LEDs fall off sharply above 680 nm. The higher Vf (~9 V) suggests a multi-die or flip-chip architecture. Excellent if the C12880MA sensor (340–850 nm) is being used and red/far-red illumination is needed.

---

## 1070 nm NIR

**Application:** IR matrix sensing — transillumination, diffuse reflectance, or index-of-refraction-based detection.

**Technology:** InGaAs (for 1000+ nm). Standard GaAs/AlGaAs only reaches to ~950 nm. For 1070 nm, InGaAs (InP substrate) is required. Significantly more expensive than standard NIR LEDs.

> [!IMPORTANT]
> At 1070 nm, silicon photodiodes have nearly zero response. An **InGaAs photodetector** is required on the receive side.

### Ushio Epitex — SMT SWIR Series (Best SMD Option)

Ushio's Epitex brand produces the world-leading SWIR LEDs. Key SMD families:

#### Epitex SMT Series (Standard Power, Compact)

| Parameter | Value |
|-----------|-------|
| **Wavelengths available** | 1050, 1100, 1150, 1200, 1300, 1450, 1550, 1650 nm |
| **Closest to 1070 nm** | **1050 nm bin** (1070 nm custom available) |
| **Output Power (1050 nm)** | ~1.1–30 mW per chip |
| **Package** | **SMD 3528** (3.5 × 2.7 mm) |

Custom wavelength: Ushio offers custom SWIR wavelengths in **10 nm increments with ±10 nm tolerance** — you can specify exactly 1070 nm.

Where to buy: [swir-led.com](https://swir-led.com) — Ushio/Epitex authorized

---

### Epigap OSA — EOLC-1070-25

| Parameter | Value |
|-----------|-------|
| **Part Number** | EOLC-1070-25 |
| **Peak Wavelength** | **1070 nm** (exact) |
| **Radiant Power** | **47 mW @ 100 mA** |
| **Forward Voltage** | 1.3 V |
| **FWHM** | **38 nm** (product page confirmed) |
| **Max Current** | 100 mA |
| **Switching Time** | 18 ns |
| **Material** | InGaAs |
| **Package** | TO-can / chip-level |

Where to buy: [epigap-osa.com](https://www.epigap-osa.com/product/eolc-1070-25/) — direct

Notes: Epigap-OSA (Germany) is a specialized SWIR/InGaAs emitter manufacturer. The 18 ns switching time is excellent for pulsed/lock-in detection schemes.

### 1070 nm Summary Recommendation

| Priority | Part | Notes |
|----------|------|-------|
| **Exact 1070 nm SMD** | Ushio Epitex SMT (custom 1070 nm order) | Best SMD form factor, 3528 package |
| **Exact 1070 nm standard part** | Epigap OSA EOLC-1070-25 | 47 mW, exact λ, available direct |
| **Catalog SMD nearest 1070** | Ushio Epitex 1050 nm SMT | Standard catalog, 1050 nm closest bin |

---

## Multi-Wavelength LED Arrays / Modules

For a pen-sized spectrophotometer, integrating multiple emitters in a single package reduces PCB area and improves co-registration of optical paths.

### Marktech Optoelectronics — Custom Multi-Chip Arrays (Best Option for Integration)

| Feature | Detail |
|---------|--------|
| **Technology** | Multiple LED dies in single TO-18, PLCC, TO-5, or SMD package |
| **Die count** | 2–7 dies per package |
| **Wavelength range** | UV through SWIR (235 nm – 4300 nm) |
| **Custom wavelengths** | Yes — specify wavelengths at order time |
| **Detector integration** | InGaAs or silicon PD can be co-packaged |
| **Applications** | Oximetry, co-oximetry, PPG, OCT, **urinalysis**, fNIRS, fluorescence |
| **MOQ** | Low-volume prototype quantities available; contact for quote |

Where to buy: [marktechopto.com/led-emitters/multiwavelength/](https://marktechopto.com/led-emitters/multiwavelength/) — custom quote

> [!NOTE]
> Marktech **explicitly lists urinalysis** as an application. This is the most directly relevant vendor for this project's exact use case. A custom 4-die package with 365/405/455/White or 365/405/455/1070 nm would be feasible.

### Practical Multi-Chip Approach for Pen Form Factor

```
Option A: Single multi-chip die (Marktech custom)
  → 4-die SMD: 365 / 405 / 455 nm + broadband
  → One footprint, one reflow operation
  → Custom quote required (~8–12 week lead time for prototypes)

Option B: Multiple discrete SMDs on a miniature PCB
  → 5× SMD 3535 footprints: 275nm | 365nm | 405nm | 455nm | white
  → 1× SMD 3528 or 5050: 1070nm NIR (separate board section)
  → Total PCB area: ~8 × 3 mm (5 LEDs in a row)
  → All available from standard distributors (DigiKey/Mouser)
  → Much faster to prototype

Recommendation: Start with Option B for prototyping, migrate to Option A for production.
```

---

## Design Notes & Caveats

### Power Levels vs. Spectrophotometry Needs

All high-power UV LEDs listed here (hundreds of mW) are far more than needed for absorbance spectrophotometry in a cuvette/tube. Plan to operate at 10–50 mA rather than rated max current. Benefits:
- Dramatically extended lifetime (UV LED lifetime is strongly current-dependent)
- Reduced heating (critical for 275 nm where Tj limit is only 75 °C for Bolb)
- Reduced analyte photodegradation risk
- Better thermal stability → better wavelength stability

### Heat Management for UV-C

Deep UV LEDs (275 nm) have low wall-plug efficiency (3–7%). At 100 mA / 5.6 V = 560 mW input, only ~16 mW is light; ~544 mW is heat. In a pen form factor, this is thermally challenging. Consider:
- Pulsed operation (1–10% duty cycle, synchronous with detector)
- Metal-core PCB (MCPCB) for the 275 nm LED
- Ceramic 3535 package (CUD7GF1B, Würth BA252) provides better thermal contact than plastic

### Window / Lens Material at 275 nm

Standard LED lenses/encapsulants (silicone, epoxy) absorb UV-C. Only:
- **Quartz (fused silica)** — transparent to ~150 nm
- **Sapphire** — transparent to ~150 nm
- **PTFE/Teflon** — diffuse but UV-transparent

are UV-C transparent. All recommended 275 nm SMDs (CUD7GF1B, Würth, Bolb) use flat/bare ceramic windows or quartz windows. Do NOT add epoxy conformal coating or silicone encapsulant over these LEDs.

### 365 nm for [[nadh|NADH]]: Consider 340 nm

The primary [[nadh|NADH]] absorption peak is **340 nm** (ε = 6,220 M⁻¹cm⁻¹). At 365 nm, absorption is ~3–4× weaker. If [[nadh|NADH]] quantification is important, investigate whether a 340 nm LED can be sourced.

### OSRAM/ams Product Transitions

Several OSRAM violet/UV products (LD CQ7P, LA CP7P) have been discontinued following the ams-OSRAM merger. Verify product status before designing in any OSRAM LEDs in this wavelength range. The Golden Dragon Plus (LD W5KM) blue 455 nm products appear to remain active.

---

## Sources

| Source | URL | Why Relevant |
|--------|-----|-------------|
| Seoul Viosys CUD7GF1B Datasheet | [neumueller.com/...CUD7GF1B...pdf](https://www.neumueller.com/datenblatt/seoulviosys/CUD7GF1B_210624_R1.91.pdf) | Primary spec sheet, exact 275 nm part |
| Bolb S6060 Product Page | [bolb.co/s6060-smd-275-nm/](https://bolb.co/s6060-smd-275-nm/) | Full specs, highest power UVC LED |
| Würth WL-SUMW at RS | [rs-online.com](https://de.rs-online.com/web/p/uv-leds/2280373) | 275 nm, catalog pricing |
| Nichia NVSU233B-U365 Datasheet | [nichia.co.jp API PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233B(T)-E(4890F)U365x%20U385x%20U395x.pdf) | 365 nm Nichia spec |
| Nichia NVSU233C-D4 Product | [nichia.co.jp](https://www.nichia.co.jp/led-ld/en/product/led_product_data.html?kbn=1&type=NVSU233C-D4+%28405nm%29) | 405/365/385/395 nm recommended model |
| Lumileds LXZ1-PR01 at RS | [rsdelivers.com](https://mt.rsdelivers.com/product/lumileds/lxz1-pr01/lumileds3-v-blue-led-smd-luxeon-z-lxz1-pr01/9231130) | 455 nm pricing and specs |
| Nichia Optisolis Product Page | [nichia.co.jp/en/product/lighting_optisolis.html](http://www.nichia.co.jp/led-ld/en/product/lighting_optisolis.html) | Optisolis CRI 98-99, spec details |
| Seoul SunLike Technology | [seoulviosys.com/en/technology/sunlike](https://www.seoulviosys.com/en/technology/sunlike) | SunLike CRI 97, violet-pump spectrum |
| Ushio Epitex SMT SWIR | [swir-led.com/smt-swir-leds/](https://swir-led.com/smt-swir-leds/) | 1050–1650 nm SMD, 3528 package |
| Epigap OSA EOLC-1070-25 | [epigap-osa.com/product/eolc-1070-25/](https://www.epigap-osa.com/product/eolc-1070-25/) | Exact 1070 nm, 47 mW, InGaAs |
| Marktech Multi-Wavelength Emitters | [marktechopto.com/led-emitters/multiwavelength/](http://oldmt.marktechopto.com/marktech-emitters/multi-wavelength-emitters/) | Multi-chip LED for urinalysis application |

## Gaps

1. **275 nm: Nichia NCSU275(T)** — Found reference to Nichia spec doc but couldn't confirm current production status or distributor pricing. Worth checking Nichia's current catalog.
2. **340 nm for [[nadh|NADH]]** — Not searched; if [[nadh|NADH]] is a primary target, a separate search for 340 nm LEDs is warranted.
3. **1070 nm exact pricing** — Epigap OSA and Ushio Epitex both require direct contact/quote for 1070 nm. Standard pricing not publicly available.
4. **Availability confirmation** — Several parts (OSRAM Golden Dragon LD W5KM) should be verified against current Mouser/DigiKey stock before BOM finalization.
5. **Optical bandwidth requirements** — For [[uric-acid|uric acid]] at 275 nm, the LED FWHM (~11 nm) combined with the 15 nm C12880MA resolution may limit specificity. Thread on optical filters should address this.
