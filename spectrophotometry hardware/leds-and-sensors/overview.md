---
title: LEDs & Sensors — Component Overview
aliases:
  - LED Sensor Overview
  - Jimini LEDs Sensors
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# LEDs & Sensors — Component Overview

Summary tables and selection guidance for all emitter and sensor components on the Jimini device. See [[leds]], [[sensors]], and [[suppliers]] for detailed per-component reviews.

---

## LED Master Table

All LEDs considered for the Jimini device, with confirmed specs from datasheets where available.

| λ (nm) | Type | Manufacturer | Part Number | Power (typ) | Vf (V) | FWHM (nm) | Beam (°) | Package | Price (1 pc) | Status | Notes |
|--------|------|-------------|-------------|-------------|--------|-----------|----------|---------|-------------|--------|-------|
| **275** | UV-C | Seoul Viosys | CUD7GF1B | 16 mW @ 100 mA | 5.6 | **11** ¹ | 125 | 3535 SMD ceramic | ~$7.78 | ★ Top pick | DigiKey in stock; exact 275 nm |
| **275** | UV-C | Bolb | S6060 | 100 mW @ 250 mA | 6.5 | ~12 ² | 150 | 6060 SMD | ~€12.52 | High power | Highest single-chip UVC; 263–280 nm bin |
| **275** | UV-C | Bolb | S3535 | 40 mW @ 100 mA | ~6.0 | ~12 ² | — | 3535 SMD | ~€13.57 | Mid power | Same tech as S6060, smaller package |
| **275** | UV-C | Würth Elektronik | 15335327BA252 | 15 mW | 6.0 | ~12 ² | 120 | 3535 SMD | ~£5–8 | EU sourcing | RS Components catalog part |
| **275** | UV-C | Crystal IS | OPTAN-275K-BL | 5 mW @ 100 mA | — | ~10–12 | 15 (ball) | Ball lens | Quote | ★ Spectroscopy | Sensing-optimized; tight ±5 nm bins |
| **365** | UV-A | Nichia | NVSU233B (U365) | 1450 mW @ 1 A | 3.85 | **9.0** ¹ | — | 3535 SMD glass | ~$15–20 | ★ Top pick | Narrowest FWHM; run at 50–100 mA |
| **365** | UV-A | Nichia | NVSU233C-D4 (U365) | ~1450 mW @ 1 A | 3.85 | **9.0** | — | 3535 SMD glass | ~$15–20 | Recommended | Newer variant of NVSU233B |
| **365** | UV-A | Seoul Viosys | CUN66A1F | 420 mW @ 250 mA | 3.6 | ~12 ² | 120 | 3535 Dome | ~€8–12 | Alternative | Dome top; Z5 series |
| **405** | Violet | Nichia | NVSU233C-D4 (U405) | ~1600 mW @ 1 A | 3.75 | **~12** ² | — | 3535 SMD glass | ~$15–20 | ★ Top pick | Multi-bin part; specify U405 |
| **405** | Violet | Nichia | NCSU035D | — | — | ~12 ² | — | 6.8×6.8 mm | ~$5–10 | Older model | Larger package; NVSU233C preferred |
| **450** | Blue | Lumileds | LXZ1-PR01 (LUXEON Z) | 575 mW @ 500 mA | 3.0 | **~20** ² | 125 | 0705/1713 | ~$1.44 | ★ Compact | Smallest high-power LED (1.7×1.3 mm) |
| **455** | Blue | ams-OSRAM | LD W5KM-1T4T-35 | 493 mW @ 1 A | 3.2 | **~20** ² | 170 | Gull-wing SMD | ~$2–5 | Exact 455 nm | Golden Dragon Plus; 449–461 nm bin |
| **455** | Blue | ams-OSRAM | LD W5SN-3T4U-35-Z | 365 mW @ 400 mA | 3.2 | ~20 ² | 160 | Gull-wing SMD | — | ARGUS ruggedized | Reliability-rated variant |
| **White** | Vis | Nichia | NF2W757G-F1 (Optisolis) | 23 lm @ 65 mA | 2.9 | **400–700** ³ | 120 | 3030 SMD | ~€0.80–1.50 | ★ CRI 98–99 | Near-D65; zero UV; blue pump ~420 nm |
| **White** | Vis | Seoul Semi | SunLike S1S0-3030 | 22 lm @ 65 mA | ~3.0 | **400–700** ³ | 120 | 3030 SMD | ~$0.19–0.22 | CRI ≥95 | **Violet pump** ~405 nm; smoothest blue |
| **White** | Vis | Yuji | APS 3030 (1 W) | 89–99 lm @ 100 mA | 8.6–9.2 | **400–730** ³ | — | 3030 SMD | Quote | CRI >97 | Newest; broadest coverage to 730 nm |
| **White** | Vis | Yuji | BC 3030 G03 (1 W) | 84–94 lm @ 300 mA | 3.0–3.4 | **400–700** ³ | — | 3030 SMD | Quote | CRI ≥95 typ 97 | Blue pump; cost-effective |
| **White** | Vis | Seoul Semi | SunLike COB S4SM-1063 | ~2000+ lm | — | **400–700** ³ | — | COB 13.5 mm | ~$10–15 | CRI 97 | Violet pump COB; too large for pen |
| **~1050** | SWIR | Ushio Epitex | SMT 1050 nm | ~1–30 mW | ~1.25 | **~80** ² | varies | 3528 SMD | Quote | Nearest catalog | Custom 1070 nm available in 10 nm steps |
| **1070** | SWIR | Epigap OSA | EOLC-1070-25 | 47 mW @ 100 mA | 1.3 | **38** ¹ | — | Chip/TO-can | Quote | ★ Exact 1070 nm | InGaAs; 18 ns switching; spectroscopy use |

**Legend:**
¹ = confirmed from manufacturer datasheet
² = estimated from technology class / typical values
³ = broadband white LED — coverage range, not single-peak FWHM
★ = recommended pick for that wavelength

---

## Sensor Master Table

| Sensor | Type | Range (nm) | Channels | Resolution | Interface | Package | Price (1 pc) | Notes |
|--------|------|-----------|----------|------------|-----------|---------|-------------|-------|
| **Hamamatsu C12880MA** | Grating micro-spectrometer | 340–850 | 288 px | ~15 nm | Analog CLK | 20.1×12.5×10.1 mm | $286 | ★ Best Sensor 1 (C12 replacement) |
| **Hamamatsu C14384MA-01** | Grating NIR micro-spectrometer | 640–1050 | Multi-px | 17–25 nm | Analog CLK | 11.5×4.0×3.1 mm | ~$600 | ★ Best Sensor 2 (C14 replacement) |
| **ams-OSRAM AS7343** | Multi-channel spectral | 380–1000 | 14 | ~20–30 nm | I²C | 2.0×3.1 mm | ~$8–12 | ★ Budget Sensor 1; 14 channels |
| **ams-OSRAM AS7341** | Multi-channel spectral | 350–1000 | 11 | ~20–30 nm | I²C | 2.0×3.1 mm | ~$6–8 | NFND; use AS7343 instead |
| **ams-OSRAM AS7265x** | 3-chip spectral triad | 410–940 | 18 | ~20 nm | I²C / UART | 3× LGA-16 | ~$80 (kit) | Approaching EOL |
| **ams-OSRAM AS7263** | NIR multi-channel | 610–860 | 6 | ~20 nm | I²C / UART | LGA-16 | ~$8–10 | Companion to AS7341 |
| **TI OPT4048** | Tristimulus color | 400–900 | 4 (XYZ+W) | — | I²C | 2.0×1.35 mm | ~$3 | Colorimetric only, not spectrophotometry |

---

## EIS Frontend Table

| IC | Type | Freq Range | Z Range | Interface | Package | Price (1 pc) | Notes |
|----|------|-----------|---------|-----------|---------|-------------|-------|
| **ADI ADuCM355** | Electrochemical AFE + MCU | 0.016 Hz – 200 kHz | <1 Ω – 10 MΩ | SPI/I²C/UART | LGA-72 (5×6 mm) | ~$11.58 | ★ Best for EIS; onboard Cortex-M3 + DFT |
| **ADI AD5933** | Impedance converter | 1 kHz – 100 kHz | 100 Ω – 10 MΩ | I²C | SSOP-16 | ~$11.45 | Simple; widely used |
| **ADI AD5934** | Impedance converter (low-cost) | 1 kHz – 100 kHz | 100 Ω – 10 MΩ | I²C | SSOP-16 | ~$6.13 | Budget AD5933 variant |
| **ADI MAX30001** | Bio-impedance + ECG AFE | 8 Hz – 131 kHz | ~10 Ω – 10 kΩ | SPI | WLP-30 | ~$8.79 | Bio-Z focus; tiny; hard to hand-solder |

---

## White LED Deep-Dive — Best for Spectrophotometry

The white LED is the most critical illumination component for broadband absorption measurements. The ideal source has:

1. **Flat SPD** across 400–700 nm (minimal peaks or dips)
2. **No UV leakage** below 400 nm (prevents autofluorescence of urine matrix)
3. **Tight chromaticity binning** (unit-to-unit consistency)
4. **Stability** over temperature and lifetime
5. **Small form factor** (3030 SMD or smaller for pen device)

### Ranking for Spectrophotometry

| Rank | LED | Architecture | CRI | SPD Flatness | UV Leakage | Package | Why |
|------|-----|-------------|-----|-------------|-----------|---------|-----|
| **1** | **Seoul SunLike S1S0-3030** | **Violet pump** (~405 nm) + TRI-R 3-phosphor | ≥95, typ 97 | ★★★★★ | Very low | 3030 SMD | Violet pump eliminates the 450 nm blue spike entirely; smoothest spectrum from 400–700 nm; available in 3030 SMD |
| **2** | **Yuji APS 3030** | Proprietary full-spectrum | >97 | ★★★★★ | Low | 3030 SMD | Broadest coverage (400–730 nm); CRI >97; TM-30 Rf 98/Rg 100; newest technology |
| **3** | **Nichia Optisolis NF2W757G-F1** | Blue pump (~420 nm) + multi-phosphor | ≥95, typ 98–99 | ★★★★ | **~Zero** (specified) | 3030 SMD | Highest CRI score; explicitly "zero UV emission"; residual blue bump at ~450 nm |
| **4** | **Yuji BC 3030 G03** | Blue pump (450 nm) + phosphor | ≥95, typ 97 | ★★★★ | Low | 3030 SMD | Cost-effective; TM-30 Rf 92/Rg 100 |
| **5** | **Luminus SST-20-W** | Blue pump + phosphor | >95 | ★★★★ | Low | 3030 SMD | High power (up to 3 A); CRI >95; well-documented |

### Recommendation

**For the Jimini pen spectrophotometer, the Seoul SunLike 3030 is the best white LED.**

Rationale:
- The **violet pump architecture** is fundamentally superior for spectrophotometry. Standard white LEDs use a ~450 nm blue die that creates a sharp emission peak overlapping with the bilirubin absorption band (454 nm). The SunLike uses a ~405 nm violet die, which sits below the measurement range and produces a genuinely smooth phosphor-emission spectrum from ~420 nm upward.
- The **TRI-R 3-phosphor system** (developed with Toshiba Materials) produces the closest match to a blackbody/daylight spectrum of any LED on the market.
- Available in **3030 SMD** — same footprint as Optisolis, compatible with pen form factor.
- **CRI ≥95 guaranteed**, R9 >85 (saturated red accuracy).
- Price is **very competitive** (~$0.19–0.22 qty from Accio/Alibaba), even lower than Optisolis.
- Available through **DigiKey, Mouser, Future Electronics** and the Seoul Semi distributor network.

> [!NOTE]
> If zero UV emission is the top priority (e.g., to completely suppress autofluorescence from the white source), Nichia Optisolis is the safer bet — Nichia explicitly specifies "UV emission essentially non-existent." The SunLike violet pump at ~405 nm does emit a small amount in the 400–420 nm near-UV range; whether this causes issues depends on the [[optical-path-design]] and detector sensitivity below 420 nm.

---

## Quick Selection Guide

### For Prototyping (Option B — Discrete SMDs)

```
PCB layout (~8 × 3 mm LED row):

  [275nm]  [365nm]  [405nm]  [450nm]  [White]     [1070nm]
  CUD7GF1B NVSU233C NVSU233C LXZ1-PR01 SunLike   EOLC-1070
  3535     3535     3535     0705     3030         chip/TO
```

### For Production (Option A — Multi-Chip)

Contact **Marktech Optoelectronics** for a custom 4–5 die multi-chip LED package combining selected wavelengths. Marktech explicitly lists urinalysis as an application. Lead time ~8–12 weeks for prototypes.

---

## Files in This Folder

| File | Contents |
|------|----------|
| [[leds]] | Detailed LED review — all wavelengths with specs, sourcing, design notes |
| [[sensors]] | Spectral sensors, NIR detectors, EIS frontends — STM32 integration |
| [[suppliers]] | Distributor coverage, pricing, lead times, sourcing strategy |

---

## Sources

| Source | URL |
|--------|-----|
| Seoul Viosys CUD7GF1B Datasheet (Rev 1.91) | [neumueller.com PDF](https://www.neumueller.com/datenblatt/seoulviosys/CUD7GF1B_210624_R1.91.pdf) |
| Nichia NVSU233B Datasheet (U365/U385/U395) | [nichia.co.jp PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233B(T)-E(4890F)U365x%20U385x%20U395x.pdf) |
| Nichia Optisolis Product Page | [nichia.co.jp](http://www.nichia.co.jp/led-ld/en/product/lighting_optisolis.html) |
| Nichia NF2W757G-F1 Product Data | [nichia.co.jp](https://led-ld.nichia.co.jp/en/product/led_product_data.html?kbn=0&type=NF2W757G-F1+%28Optisolis%29) |
| Seoul SunLike 3030 Datasheet | [DigiKey PDF](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6638/S1S0-3030.pdf) |
| Seoul SunLike Technology | [seoulsemicon.com](https://www.seoulsemicon.com/en/technology/sunlike) |
| Seoul SunLike 3030S via Neumüller | [neumueller.com](https://www.neumueller.com/en/produktgruppe/full-spectrum-leds/3030s-sunlike-series) |
| Yuji APS 3030 Product Page | [yujiintl.com](https://www.yujiintl.com/aps-3030-0-9w/) |
| Yuji BC 3030 G03 Product Page | [yujiintl.com](https://www.yujiintl.com/bc-3030-0-9w/) |
| Yuji NormLite Standard Light Source | [store.yujiintl.com](https://store.yujiintl.com/products/normlite-iso-compliant-standard-light-source-full-spectrum-cri-99-professional-2700k-6500k-task-lamp) |
| Epigap OSA EOLC-1070-25 | [epigap-osa.com](https://www.epigap-osa.com/product/eolc-1070-25/) |
| Bolb S6060 Product Page | [bolb.co](https://bolb.co/s6060-smd-275-nm/) |
| Bolb S3535 Product Page | [bolb.co](https://bolb.co/smd3535/) |
| Crystal IS Optan Series | [cisuvc.com](http://www.cisuvc.com/products/optan) |
| Lumileds LXZ1-PR01 | [xonelec.com](https://www.xonelec.com/mpn/lumileds/lxz1pr01) |
| OSRAM LD W5KM-1T4T-35 | [microchipusa.com](https://www.microchipusa.com/product/ams-osram-usa-inc/led-color-lighting/LD-W5KM-1T4T-35) |
| Luminus SST-20-W Datasheet | [luminus.com PDF](https://download.luminus.com/datasheets/Luminus_SST-20-WxH_Datasheet.pdf) |
| Marktech Multi-Wavelength Emitters | [marktechopto.com](http://oldmt.marktechopto.com/marktech-emitters/multi-wavelength-emitters/) |

## Gaps

1. No evaluation of SunLike vs Optisolis in an actual Jimini prototype — recommendation is based on published SPD data, not measured spectrophotometric performance.
2. InGaAs detector pairing for 1070 nm not covered in this overview; see [[sensors]] for full NIR coverage discussion.
3. Multi-chip LED custom quote from Marktech not yet requested; lead time and prototype pricing unknown.
