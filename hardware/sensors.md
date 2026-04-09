# Spectral Sensors for Portable Spectrophotometry (STM32 Compatible)

> **Project context:** Pen-sized spectrophotometer  
> **Date compiled:** 2026-04-09  
> **Targets:** Sensor 1 (C12-like, 321–870 nm UV-Vis), Sensor 2 (C14-like, 570–1078 nm Vis-NIR), IR matrix (~1070 nm), EIS frontend

---

## Table of Contents

1. [Broadband / Multi-Channel Spectral Sensors (UV-Vis)](#1-broadband--multi-channel-spectral-sensors-uv-vis)
2. [NIR Spectral Sensors (570–1078 nm)](#2-nir-spectral-sensors-5701078-nm)
3. [IR Matrix Sensors (~1070 nm multi-pixel)](#3-ir-matrix-sensors-1070-nm-multi-pixel)
4. [EIS Frontend ICs](#4-eis-frontend-ics)
5. [Comparison Tables](#5-comparison-tables)
6. [Evaluation Kits & Reference Designs](#6-evaluation-kits--reference-designs)
7. [STM32 Integration Notes](#7-stm32-integration-notes)
8. [Sensor Selection Guidance](#8-sensor-selection-guidance)

---

## 1. Broadband / Multi-Channel Spectral Sensors (UV-Vis)

### 1.1 AMS-OSRAM AS7341 ⭐ *Best candidate for Sensor 1 (C12 replacement)*

| Parameter               | Value                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Manufacturer**        | AMS-OSRAM                                                                                                                    |
| **Part Number**         | AS7341-DLGM (LGA) / AS7341-DLGT (OLGA, newer)                                                                                |
| **Spectral Range**      | ~350–1000 nm (8 spectral + 3 aux channels)                                                                                   |
| **Channels**            | 11 total: F1(415nm), F2(445nm), F3(480nm), F4(515nm), F5(555nm), F6(590nm), F7(630nm), F8(680nm), NIR(850nm), Clear, FLicker |
| **ADC Resolution**      | 16-bit per channel                                                                                                           |
| **Interface**           | I²C (address 0x39)                                                                                                           |
| **Package**             | 8-TFLGA / OLGA-8 — **2.0 × 3.1 mm**                                                                                          |
| **Supply Voltage**      | 1.7–2.0 V (IOVDD up to 3.6 V)                                                                                                |
| **Current (active)**    | ~210 µA typical                                                                                                              |
| **FWHM**                | ~20–30 nm per channel                                                                                                        |
| **Built-in LED driver** | Yes (up to 258 mA)                                                                                                           |
| **Status**              | AS7341-DLGM marked "Not for New Designs"; **AS7341-DLGT** is current version                                                 |
| **Price (1 qty)**       | ~$5.86–7.66 USD (DigiKey/Xonelec)                                                                                            |
| **Where to buy**        | DigiKey (`AS7341-DLGMTR-ND`), Mouser, Adafruit breakout ($12.50)                                                             |

**STM32 notes:** Standard I²C, 3.3 V logic compatible via IOVDD pin. Adafruit Arduino library is well-tested (Adafruit_AS7341). No official STM32 HAL driver, but the I²C register map is simple enough to port in ~200 lines. Multiple examples on GitHub for bare-metal STM32.  
**Vs. C12 (321–870 nm):** Coverage is 350–1000 nm — slightly narrower at UV end (350 vs 321 nm) but extends further in NIR. With 8 narrow-band channels + clear + NIR + flicker it is far richer than a single-channel photodiode. **Strong candidate for Sensor 1 slot.**

---

### 1.2 AMS-OSRAM AS7343 ⭐⭐ *Upgraded AS7341, more UV channels*

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | AMS-OSRAM |
| **Part Number** | AS7343-DLGM |
| **Spectral Range** | ~380–1000 nm |
| **Channels** | 14 total: 12 spectral (F1–F8 + 4 additional) + Clear + FD + NIR |
| **ADC Resolution** | 16-bit |
| **Interface** | I²C |
| **Package** | OLGA-8 — **2.0 × 3.1 mm** (same footprint as AS7341) |
| **Supply Voltage** | 1.7–1.98 V |
| **Built-in LED driver** | Yes |
| **Status** | Active production |
| **Price (1 qty)** | ~$8–12 USD (LCSC ~¥35–50; Mouser/DigiKey) |
| **Breakout** | SparkFun SEN-23220 (Qwiic) — **$21.95** |
| **Where to buy** | DigiKey, Mouser, LCSC (`AS7343-DLGM C19085986`), SparkFun |

**STM32 notes:** Drop-in upgrade from AS7341 — same I²C footprint, same register structure. SparkFun Arduino/Qwiic library available. I²C address configurable.  
**Vs. C12 (321–870 nm):** Coverage starts at 380 nm (vs 321 nm needed). The UV gap below 380 nm may need supplemental UV photodiode if UV absorbance is required. Otherwise this is a better choice than AS7341 for the 14-channel coverage.

---

### 1.3 AMS-OSRAM AS7265x (18-channel, 3-chip set)

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | AMS-OSRAM |
| **Chipset** | AS72651 (master, 600–870 nm) + AS72652 (560–940 nm) + AS72653 (410–535 nm) |
| **Spectral Range** | 410–940 nm combined |
| **Channels** | 18 channels across 3 ICs (6 each), ~35 nm spacing |
| **FWHM** | 20 nm per channel |
| **Interface** | UART (AT commands) or I²C to AS72651 master; AS72651 handles inter-chip comms via dedicated I²C |
| **Package** | LGA-16 per IC, ~3.3 × 3.5 mm each |
| **Supply** | 2.7–3.6 V |
| **Status** | "Ordering and shipping still possible" — **approaching EOL** |
| **Price (chips)** | ~$5–8 per IC × 3 = ~$15–25 total |
| **Breakout** | SparkFun Triad Spectroscopy Sensor SEN-15050 — ~**$80** |
| **Demo Kit** | AMS AS7265X_DEM_SN (Windows PC-hosted) |

**STM32 notes:** AT-command UART interface simplifies firmware — send ASCII commands, receive calibrated readings. Alternatively use I²C to AS72651. SparkFun has open-source Arduino library. UART mode especially convenient with STM32 HAL UART DMA.  
**Limitation for Sensor 1:** Does not reach below 410 nm (UV gap). 940 nm NIR edge. Good for color/food/agriculture but not deep UV applications.

---

### 1.4 Hamamatsu C12880MA ⭐⭐ *Direct C12 reference module*

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Hamamatsu Photonics |
| **Part Number** | C12880MA |
| **Spectral Range** | **340–850 nm** (closest match to 321–870 nm requirement) |
| **Channels** | 288 pixels (linear CMOS sensor array + grating) |
| **Resolution** | ~15 nm optical resolution (FWHM) |
| **Interface** | **Analog** — parallel clocked readout (CLK, ST, VIDEO pins) |
| **Package** | 20.1 × 12.5 × 10.1 mm module, 5 g |
| **Supply** | 3.3 V or 5 V (Vdd 3.3 V, external 3.3–5 V input) |
| **Integration time** | 20 µs to ~100 ms |
| **Dynamic range** | High (CMOS, 16-bit effective) |
| **Price** | **$286** (Hamamatsu shop) / ~$215 (eBay/GroupGets) |
| **Where to buy** | [shop.hamamatsu.com](https://shop.hamamatsu.com/products/micro-spectrometer-c12880ma), GroupGets, eBay |

**STM32 notes:** **No I²C or SPI** — uses custom clocked analog readout. STM32 drives CLK + ST digital signals; ADC samples the VIDEO analog pin synchronously. Requires a 12-bit (minimum) ADC on STM32 running at ~2–5 MHz. Use TIM + ADC DMA for efficient acquisition. Open-source STM32/Arduino drivers exist (github.com/groupgets/c12666ma is similar; multiple research papers implemented this on STM32F4). Total acquisition time ~few ms for 288 pixels.  
**Best match for Sensor 1:** Spectral range 340–850 nm is the closest available commercial module to the 321–870 nm requirement. The gap is only 19 nm at UV end and 20 nm at NIR end.

---

### 1.5 Hamamatsu C14384MA-01 ⭐⭐ *Direct C14 reference module*

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Hamamatsu Photonics |
| **Part Number** | C14384MA-01 |
| **Spectral Range** | **640–1050 nm** (covers 570–1078 nm target partially) |
| **Channels** | Linear CMOS + grating — multiple pixels (high resolution) |
| **Resolution** | 17–25 nm (FWHM) |
| **Interface** | **Analog** clocked readout (CLK, ST, VIDEO) — same as C12880MA |
| **Package** | **Ultra-compact: 11.5 × 4.0 × 3.1 mm**, 0.3 g |
| **Supply** | 4.75–5.25 V (Vs) |
| **Sensitivity** | 50× improvement at 1000 nm vs predecessor C11708MA |
| **Price** | ~$600–700 USD (quote-based; ₹54,840 India/Tanotis) |
| **Where to buy** | Hamamatsu direct (quote), Farnell, Newark, Tanotis (India) |

**STM32 notes:** Same analog clocked readout as C12880MA — STM32 drives CLK/ST, reads VIDEO via ADC + DMA. The 5 V supply requires level shifting for 3.3 V STM32 I/O, or use a 5 V-tolerant GPIO. Because it extends to 1050 nm and the target is 1078 nm, there's a ~28 nm gap at the NIR end — may need supplemental InGaAs detector for the 1050–1078 nm slice.  
**Best match for Sensor 2:** Covers most of 570–1078 nm range, but the lower edge starts at 640 nm (vs 570 nm needed). For full 570–1078 nm, consider pairing with an AS7341/AS7343 to cover 570–640 nm region.

---

### 1.6 Texas Instruments OPT4048 (Tristimulus — niche use)

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Texas Instruments |
| **Part Number** | OPT4048 |
| **Spectral Range** | 400–900 nm (XYZ CIE color match + ambient clear) |
| **Channels** | 4 (X, Y, Z, W/Clear) |
| **ADC** | 26-bit effective dynamic range |
| **Interface** | I²C (up to 1 MHz HS mode) |
| **Package** | SOT-5X3 (2 × 1.35 mm) |
| **Supply** | 1.7–3.6 V |
| **Speed** | 0.6–2400 ms integration, burst mode |
| **Price** | ~$2–3 USD |
| **Where to buy** | DigiKey, Mouser, TI store |

**STM32 notes:** Pure I²C, 3.3 V native. TI provides HAL driver code and reference design.  
**Limitation:** Only 4 channels, designed for color/CCT measurement. **Not a spectrometer replacement** — useful for colorimetric cross-check channels or a fast pre-screening step. Not a standalone solution for spectrophotometry.

---

### 1.7 Photodiode + TIA Custom Approach

For custom channel selection (e.g., exactly matching 321–870 nm or specific analyte wavelengths):

- **Silicon photodiodes** (Hamamatsu S1336 series, OSI Optoelectronics): ~200–1100 nm  
  with optical bandpass filters → custom spectral channels
- **Transimpedance amplifier ICs**: OPA2333 (zero-drift, low-noise), AD8615, TLV2333
- **Filter array**: custom thin-film filters or commercial bandpass filter sets
- **Cost:** Low (photodiode ~$2–5, TIA IC ~$1–3, filter ~$20–50/channel)
- **Tradeoff:** Complex PCB, filter alignment, many components; but ultimate flexibility

---

## 2. NIR Spectral Sensors (570–1078 nm)

### 2.1 AMS-OSRAM AS7263 (6-channel NIR)

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | AMS-OSRAM |
| **Part Number** | AS7263 |
| **Spectral Range** | **610–860 nm** (6 channels: R@610, S@680, T@730, U@760, V@810, W@860 nm) |
| **FWHM** | 20 nm per channel |
| **Interface** | I²C or UART (AT commands, same as AS7262) |
| **Package** | LGA-16 (~3.3 × 3.5 mm) |
| **Supply** | 2.7–3.6 V |
| **Price** | ~$5–10 USD chip; SparkFun SEN-14351 breakout ~$16 |
| **Status** | Active (SparkFun has Qwiic version) |

**STM32 notes:** I²C or AT-command UART — very easy STM32 integration. Good companion to AS7341 for extending NIR coverage beyond 680 nm.  
**Coverage gap:** Only 610–860 nm — misses 570–610 nm lower end and >860 nm upper end of the 570–1078 nm target. Use alongside AS7341 (which covers to 1000 nm NIR channel at 855 nm) for broader NIR.

---

### 2.2 Hamamatsu InGaAs Photodiodes (G-series)

For **single-point or few-point NIR detection** in the 900–1700 nm range:

| Part Number | Range | Active Area | Package | Notes |
|-------------|-------|-------------|---------|-------|
| **G10899-01K** | 0.5–1.7 µm | 1 mm dia | TO-18 metal | Extended InGaAs, covers 570–1700 nm |
| **G10899-005K** | 0.5–1.7 µm | 0.5 mm dia | TO-18 | Smaller active area, lower capacitance |
| **G8370-01** | 0.9–1.7 µm | 1 mm dia | TO-18 | Standard InGaAs |
| **G6849-01** | 0.9–1.7 µm | — | Ceramic | Segmented type |

**Price:** ~$50–200 each (Hamamatsu direct, quote-based for volume)  
**STM32 notes:** Requires external TIA circuit (e.g., OPA657 or AD8015 for high bandwidth). Connect TIA output to STM32 ADC. For spectroscopy, pair with a Fabry-Pérot tunable filter or wedge filter for wavelength selectivity.

**Extended InGaAs (G10899 series)** is the correct choice when you need sensitivity from **500–700 nm extending to 1700 nm** — this covers the full 570–1078 nm window in a single detector element, but without spectral discrimination (single broadband output). For spectral scanning, add a narrow bandpass filter wheel or tunable MEMS filter.

---

### 2.3 Hamamatsu C14384MA-01 (also in Sensor 2 candidate)

*(See Section 1.5 above)* — This is the **primary Sensor 2 candidate** as a grating-based mini-spectrometer module covering 640–1050 nm, analogous to how C12880MA serves Sensor 1.

---

### 2.4 AMS-OSRAM AS7265x NIR portion

The **AS72651** sub-chip covers **600–870 nm** and the **AS72652** extends to **940 nm** — combined, the 3-chip AS7265x system gives 410–940 nm at 18 channels. While not reaching 1078 nm, it provides excellent multi-channel NIR coverage and could substitute for a dedicated Sensor 2 if 1078 nm is not strictly required.

---

### 2.5 Silicon Extended-NIR Photodiodes

Standard silicon photodiodes (e.g., Hamamatsu S2386 series) have usable response to ~1000–1100 nm (R ~5–20% QE at 1000 nm) with depletion layer optimization. Above ~1050 nm, InGaAs is required.

- **Hamamatsu S2386-45K**: Enhanced NIR, 190–1100 nm, TO-18
- Response at 1000 nm: ~0.35 A/W typical for enhanced Si
- Price: ~$15–30

---

## 3. IR Matrix Sensors (~1070 nm Multi-Pixel)

> ⚠️ **Important distinction:** Most "IR matrix" sensors on the market are **thermal/far-IR** (8–14 µm range, e.g., Melexis MLX90640). For **near-IR at 1070 nm**, you need a photodetector, not a thermopile array.

### 3.1 Melexis MLX90640 (32×24 thermal array — NOT 1070 nm)

| Parameter | Value |
|-----------|-------|
| **Type** | Far-infrared thermopile array |
| **Spectral range** | **8–14 µm** (thermal emission detection) |
| **Resolution** | 32×24 pixels |
| **Interface** | I²C |
| **Package** | LCC-16 (4 × 3.1 mm) |
| **Price** | ~$15–25 |

**Verdict for your use case: ❌ WRONG SENSOR.** MLX90640 detects thermal radiation (body heat, surface temperature). It cannot detect 1070 nm near-IR light. Do NOT use for near-IR spectrophotometry.

---

### 3.2 Melexis MLX75305 (Single-pixel optical — not matrix)

- Single photodetector, not an array
- Spectral response: ~400–1000 nm (silicon-based)
- Not useful for multi-pixel NIR matrix at 1070 nm

---

### 3.3 Hamamatsu InGaAs Linear Arrays (Correct Choice)

For a **true multi-pixel NIR detector at ~1070 nm**:

| Part | Type | Pixels | Range | Interface | Notes |
|------|------|--------|-------|-----------|-------|
| **G9202-256W** | InGaAs linear array | 256 | 0.9–1.7 µm | Analog video out | $$$, lab grade |
| **G9204-512W** | InGaAs linear array | 512 | 0.9–1.7 µm | Analog video out | $$$$, research |
| **G6849-01** | Segmented InGaAs | 2 segments | 0.9–1.7 µm | Analog | Low cost, 2-pixel |

**Price:** Linear InGaAs arrays are expensive ($500–$5,000+). Mostly available direct from Hamamatsu; require dedicated driver circuitry.

---

### 3.4 ams-OSRAM TSL2591 / Other Si Arrays (Limited NIR)

Silicon-based pixel arrays with NIR enhancement (Vishay, Broadcom) typically cut off at ~1000–1100 nm. For 1070 nm, silicon QE is ~5–15% — marginal but detectable with gain.

---

### 3.5 Recommended Path for 1070 nm Multi-pixel

**Option A — Simple:** Use multiple discrete extended-InGaAs photodiodes (e.g., 3–8 × G10899 series) in a custom linear arrangement with a diffraction grating or prism. STM32 reads each via multiplexed ADC + TIA.

**Option B — Module:** Hamamatsu **C14384MA-01** extends to 1050 nm (close to 1070 nm) and provides a linear array implicitly through its CMOS sensor — if the upper wavelength cutoff at 1050 nm vs your 1078 nm target is acceptable.

**Option C — Expensive:** Hamamatsu InGaAs linear array module (quote required, $1,000+).

---

## 4. EIS Frontend ICs

### 4.1 Analog Devices AD5933 ⭐ *Primary EIS IC*

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Analog Devices (formerly ADI) |
| **Part Number** | AD5933YRSZ (SSOP-16) |
| **Function** | Impedance converter, network analyzer |
| **Frequency range** | 1 kHz – 100 kHz (internal clock-dependent) |
| **ADC** | 12-bit, 1 MSPS |
| **Impedance range** | **1 kΩ – 10 MΩ** (natively); **100 Ω – 1 kΩ** with external circuit |
| **System accuracy** | 0.5% |
| **Interface** | **I²C** (address 0x0D) |
| **Package** | SSOP-16 (5.3 × 6.2 mm) |
| **Supply** | 2.7–5.5 V (single supply) |
| **Output excitation** | Programmable sine wave, 2 Vpp max |
| **Price (1 qty)** | ~**$11.45** (ADI list); ~$10–15 on DigiKey/Mouser |
| **Eval board** | EVAL-AD5933EBZ (~$67–84) |
| **Where to buy** | DigiKey, Mouser, Arrow, Octopart |

**STM32 notes:** Pure I²C interface — direct connection to STM32 I²C peripheral. STM32 HAL I²C driver works out of the box. Open-source STM32 libraries and Arduino libraries widely available. The AD5933 requires a calibration resistor and current sense resistor for absolute impedance measurement. For EIS: sweep from 1 kHz to 100 kHz, read real + imaginary components, compute magnitude and phase. Typical STM32 implementation: configure DDS, read complex impedance via I²C after each frequency step, build Nyquist/Bode plot.

**Key limitation:** Internal oscillator accuracy limits lowest useful frequency to ~1 kHz. For sub-kHz EIS (important for some bioelectrochemical applications), an external clock or the AD5934 with divided-down MCLK is needed.

---

### 4.2 Analog Devices AD5934 (Lower-cost variant)

| Parameter | Value |
|-----------|-------|
| **Part Number** | AD5934YRSZ |
| **Difference from AD5933** | 250 kSPS ADC (vs 1 MSPS), max freq ~100 kHz |
| **Impedance range** | 1 kΩ – 10 MΩ |
| **Interface** | I²C |
| **Package** | SSOP-16 |
| **Price (1 qty)** | ~**$6.13** |
| **Where to buy** | DigiKey, Mouser |

**Use case:** When cost is primary concern and 250 kSPS ADC is sufficient. Almost identical firmware to AD5933.

---

### 4.3 Analog Devices ADuCM355 ⭐⭐ *Full electrochemical AFE MCU*

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Analog Devices |
| **Part Number** | ADuCM355BCCZ (LGA-72) |
| **Type** | Precision analog MCU with **integrated electrochemical sensor AFE** |
| **MCU core** | ARM Cortex-M3 @ 26 MHz |
| **Flash / RAM** | 128 kB / 64 kB |
| **EIS capability** | Digital waveform generator + DFT engine |
| **Impedance range** | **< 1 Ω to 10 MΩ**, **0.016 Hz to 200 kHz** |
| **ADC** | 16-bit, 400 kSPS |
| **Voltage DAC** | 2× dual-output (12-bit), ±2.2 V to sensor |
| **TIA amplifiers** | 2× potentiostat + TIA (ultra-low power 1 µA each) |
| **Interface** | I²C, SPI, UART, GPIO |
| **Package** | LGA-72 (5 × 6 mm) |
| **Supply** | 1.8 V + 3.3 V |
| **Price (1ku)** | ~**$11.58** list; LCSC ~$18–25 |
| **Eval board** | EVAL-ADuCM355 / EVAL-ADuCM355QSPZ |
| **Where to buy** | Mouser, DigiKey, LCSC (C660219) |

**STM32 notes:** The ADuCM355 is itself an ARM Cortex-M3 MCU — it can be used **standalone** for the EIS measurement, with results reported to the main STM32 via SPI/UART/I²C. Alternatively, use it purely as a slave EIS co-processor. ADI provides IAR/Keil support plus open-source examples. The onboard DFT engine and programmable waveform generator mean the host STM32 can simply command a sweep and collect processed impedance data without doing any DSP itself. **Best choice for a serious EIS application** — supports 3-electrode electrochemical cells directly.

---

### 4.4 Analog Devices MAX30001 (BioZ / ECG)

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Maxim/Analog Devices |
| **Part Number** | MAX30001CWV+T |
| **Type** | Biopotential (ECG) + Bioimpedance AFE |
| **BioZ frequency** | 8 Hz – 131 kHz AC excitation |
| **BioZ range** | Designed for body impedance (10 Ω – 10 kΩ range) |
| **ECG ADC** | 18-bit, 512 Hz |
| **Interface** | **SPI** (up to 10 MHz) |
| **Package** | WLP-30 (2.7 × 2.9 mm) — very small |
| **Supply** | 1.1–1.8 V core + 1.7–3.6 V IO |
| **Price (1 qty)** | ~**$8.79** list; LCSC ~$7–9 |
| **Where to buy** | DigiKey, Mouser, LCSC (C2650384), ProtoCentral breakout |

**STM32 notes:** SPI interface — connect to STM32 SPI peripheral. 3.3 V IO compatible. ProtoCentral makes an evaluation breakout with Arduino library. Footprint is WLP (solder bumps) — challenging for hand assembly; requires reflow.  
**Limitation for EIS:** Optimized for **biological tissue impedance** (body composition, ECG). Frequency range and impedance range biased toward kHz bioimpedance. Less suitable for wide-range electrochemical EIS vs ADuCM355 or AD5933.

---

### 4.5 Texas Instruments AFE4300 (Body composition / weight)

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Texas Instruments |
| **Part Number** | AFE4300 |
| **Type** | Dual AFE — weight scale + body composition impedance |
| **BIA** | 4-electrode tetra-polar impedance measurement |
| **ADC** | 16-bit, 860 SPS |
| **Interface** | SPI |
| **Package** | QFN-40 (6 × 6 mm) |
| **Frequency** | Single AC frequency (typ. 50 kHz) — NOT a swept-frequency EIS |
| **Price** | ~$5–8 |
| **Eval kit** | AFE4300EVM-PDK |

**Limitation:** Single-frequency BIA — not true impedance spectroscopy across a frequency sweep. Suitable for body fat percentage / hydration, not for electrochemical cell characterization. **Not recommended for EIS in a spectrophotometer context.**

---

## 5. Comparison Tables

### 5.1 Broadband Spectral Sensors — Sensor 1 Candidates (321–870 nm)

| Sensor | Range | Channels | Interface | Package | Price | STM32 Ease | Notes |
|--------|-------|----------|-----------|---------|-------|------------|-------|
| **C12880MA** | 340–850 nm | 288 | Analog CLK | 20×12×10 mm | $286 | Medium | Grating spectrometer, 15 nm resolution |
| **AS7343** | 380–1000 nm | 14 | I²C | 2×3.1 mm | ~$10 | Easy | Best all-round chip; UV gap below 380 nm |
| **AS7341** | 350–1000 nm | 11 | I²C | 2×3.1 mm | ~$6–8 | Easy | NFND status; use AS7343 instead |
| **AS7265x** | 410–940 nm | 18 | I²C/UART | 3× LGA-16 | ~$80 (kit) | Easy | 3-chip system; UV gap below 410 nm |
| **OPT4048** | 400–900 nm | 4 (XYZ+W) | I²C | 2×1.35 mm | ~$3 | Very Easy | Colorimetric only, not spectrophotometry |

### 5.2 NIR Sensors — Sensor 2 Candidates (570–1078 nm)

| Sensor | Range | Channels | Interface | Package | Price | STM32 Ease | Notes |
|--------|-------|----------|-----------|---------|-------|------------|-------|
| **C14384MA-01** | 640–1050 nm | Multi-pixel | Analog CLK | 11.5×4×3.1 mm | ~$600 | Medium | Grating NIR, 17–25 nm resolution; small gap at both ends |
| **AS7263** | 610–860 nm | 6 | I²C/UART | LGA-16 | ~$8–10 | Easy | Limited range; good companion to AS7341 |
| **AS7265x NIR** | 600–940 nm | 6 (AS72651) | I²C/UART | LGA-16 | part of 3-chip | Easy | Within the 3-chip package |
| **G10899-01K** | 500–1700 nm | 1 (broadband) | Analog TIA | TO-18 | ~$80–150 | Hard | Single detector; needs external filter for spectroscopy |
| **Si enhanced** | 200–1100 nm | 1 | Analog | TO-18 | ~$15–30 | Hard | Poor QE >1000 nm |

### 5.3 EIS Frontend ICs

| IC | Freq Range | Impedance Range | Interface | Package | Price | Notes |
|----|------------|-----------------|-----------|---------|-------|-------|
| **ADuCM355** | 0.016 Hz–200 kHz | <1 Ω–10 MΩ | SPI/I²C/UART | LGA-72 (5×6mm) | $11.58 | Full MCU, DFT onboard, potentiostat |
| **AD5933** | 1 kHz–100 kHz | 100 Ω–10 MΩ | I²C | SSOP-16 | $11.45 | Simple, widely used, 12-bit |
| **AD5934** | 1 kHz–100 kHz | 100 Ω–10 MΩ | I²C | SSOP-16 | $6.13 | Lower cost AD5933 variant |
| **MAX30001** | 8 Hz–131 kHz | ~10 Ω–10 kΩ | SPI | WLP-30 | $8.79 | Bio-impedance focus; tiny package |
| **AFE4300** | ~50 kHz fixed | Body fat range | SPI | QFN-40 | ~$6 | Single-freq BIA, NOT spectroscopy |

---

## 6. Evaluation Kits & Reference Designs

### Spectral Sensors

| Kit | Part | Price | Description |
|-----|------|-------|-------------|
| **Adafruit AS7341 breakout** | #4698 | $12.50 | STEMMA QT/Qwiic, 3.3 V ready |
| **SparkFun AS7343 (Qwiic)** | SEN-23220 | $21.95 | With I²C level shifting |
| **SparkFun AS7265x Triad** | SEN-15050 | ~$80 | 18-channel, 3-IC system, Qwiic |
| **AMS AS7265X_DEM_SN** | AS7265X_DEM_SN | ~€50–80 | Windows GUI, USB-UART dongle |
| **Hamamatsu C12880MA shop** | C12880MA | $286 | Ready-to-use module |
| **GroupGets C12880MA** | — | ~$220–250 | Community buy |
| **SparkFun AS7263 breakout** | SEN-14351 | ~$16 | NIR Qwiic breakout |

### EIS

| Kit | Part | Price | Description |
|-----|------|-------|-------------|
| **EVAL-AD5933EBZ** | EVAL-AD5933EBZ | ~$67–84 | AD5933 eval, USB to PC |
| **EVAL-ADuCM355** | EVAL-ADuCM355 | ~$100–150 | Full eval board, gas sensor cell inputs |
| **EVAL-ADuCM355QSPZ** | EVAL-ADuCM355QSPZ | ~$100 | With electrochemical sensor connections |
| **ProtoCentral MAX30001** | PC-MED-0307 | ~$60 | MAX30001 breakout with Arduino lib |
| **AFE4300EVM-PDK** | AFE4300EVM-PDK | ~$99 | TI eval, weight + BIA channels |

### Application Notes

- **AMS AS7341**: AN000580 "AS7341 Application Note for Spectral Sensing"
- **AMS AS7265x**: AS7265x datasheet + SparkFun hookup guide (fully worked Arduino + STM32 examples)
- **AD5933**: AN-1252 "Measuring a Loudspeaker Impedance Profile Using the AD5933"; AN-1053 "Measuring Sensor Impedance with the AD5933"
- **ADuCM355**: UG-1308 (EVAL-ADuCM355QSPZ User Guide) — full electrochemical cell interface guide
- **C12880MA**: Hamamatsu application note "Mini-spectrometer drive circuit" + multiple academic papers (PMC11479284, MDPI sensors/24/19/6445)

---

## 7. STM32 Integration Notes

### I²C Sensors (AS7341, AS7343, AS7263, AD5933, AD5934)

```c
// Standard STM32 HAL I2C pattern
HAL_I2C_Master_Transmit(&hi2c1, ADDR<<1, reg_buf, 2, 100);
HAL_I2C_Master_Receive(&hi2c1, ADDR<<1, data_buf, len, 100);
```

- AS7341/AS7343: address `0x39` fixed (pull INT pin for interrupt-driven reads)
- AD5933: address `0x0D` fixed; write to `0x80` (control reg), `0x82` (start freq), then poll status
- AS7265x (I²C mode): route through AS72651 master at `0x49`

### UART Sensors (AS7265x AT-command mode)

```c
// Example AT command to AS7265x
HAL_UART_Transmit(&huart2, "ATDATA\r\n", 8, 100);
HAL_UART_Receive_DMA(&huart2, rx_buf, 512);
```

AT-command mode returns calibrated float values as ASCII strings — easy to parse on STM32 without any register-level knowledge.

### Analog Clocked Sensors (C12880MA, C14384MA)

```c
// Pseudo-code for C12880MA readout on STM32
// TIM2 generates CLK; DMA triggers ADC at each CLK rising edge
// 1. Assert ST (start) for 1 CLK cycle
// 2. Run 288 CLK cycles while capturing VIDEO pin via ADC+DMA
// 3. Result: 288 uint16_t values in DMA buffer

HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_1);  // CLK output
HAL_ADC_Start_DMA(&hadc1, spectrum_buf, 288);
```

- Use `STM32F4` or `STM32H7` for best ADC speed (12-bit, 2–5 MHz sampling)
- Minimum viable: STM32F103 with bit-banged CLK + polling ADC (slower but functional)
- C12880MA VIDEO signal: 0–3.3 V range, ~1 µs settling time per pixel

### SPI Sensors (MAX30001, AFE4300, ADuCM355 slave mode)

```c
// MAX30001 SPI example (CPOL=0, CPHA=0, MSB first)
HAL_GPIO_WritePin(CS_GPIO, CS_PIN, GPIO_PIN_RESET);
HAL_SPI_TransmitReceive(&hspi1, tx_buf, rx_buf, len, 100);
HAL_GPIO_WritePin(CS_GPIO, CS_PIN, GPIO_PIN_SET);
```

### Power / Voltage Considerations

| Sensor | VDD | STM32 3.3V? | Notes |
|--------|-----|-------------|-------|
| AS7341/AS7343 | 1.7–2.0 V | Via IOVDD pin (3.3 V ok) | Internal LDO; IOVDD level-shifts I²C |
| C12880MA | 3.3 V (Vdd) + 3.3 V input | ✅ | Analog output 0–3.3 V |
| C14384MA-01 | **5 V (Vs)** | ⚠️ Need 5 V rail | I/O may need level shift |
| AD5933 | 2.7–5.5 V | ✅ 3.3 V | I²C 3.3 V safe |
| ADuCM355 | 1.8 V + 3.3 V | ✅ | Dual supply; use LDO from STM32 board 3.3 V |
| MAX30001 | 1.1–1.8 V (core), 1.7–3.6 V IO | ✅ via 3.3 V IO | Tiny WLP package |

---

## 8. Sensor Selection Guidance

### For Sensor 1 (321–870 nm, UV-Vis, "like C12")

**Recommended:** Hamamatsu **C12880MA** if full 288-channel spectral resolution is needed (grating spectrometer, ~15 nm resolution, $286).  
**Budget alternative:** AMS-OSRAM **AS7343** — 14 channels, I²C, 8× cheaper, drop-in 2×3.1 mm chip. Limited to 380–1000 nm (UV gap below 380 nm). Excellent for color matching, food analysis, LED characterization.  
**Extended UV:** If 321–380 nm is critical, add a **UV photodiode** (e.g., Hamamatsu S1226-8BQ, 190–1000 nm) + bandpass filter + TIA as a supplemental UV channel alongside the AS7343.

### For Sensor 2 (570–1078 nm, Vis-NIR, "like C14")

**Recommended:** Hamamatsu **C14384MA-01** — covers 640–1050 nm, ultra-compact module, analog grating spectrometer. Gap at 570–640 nm can be bridged by AS7341/AS7343 red channels (590–680 nm region). Gap above 1050 nm (to 1078 nm) is small and may be acceptable.  
**Cheaper alternative:** **AS7265x** 3-chip system covers 410–940 nm at 18 channels. Misses 940–1078 nm window.  
**If 1078 nm is hard requirement:** Add a single InGaAs photodiode (G10899 series, 500–1700 nm) with a ~1070 nm bandpass filter as a targeted detector for that specific wavelength.

### For IR Matrix Sensor (~1070 nm)

**Reality check:** No cheap I²C "IR matrix" sensor exists for 1070 nm near-IR (thermal cameras are 8–14 µm, completely different).  
**Option A (pragmatic):** The C14384MA-01 already provides a multi-pixel linear array at 640–1050 nm — treat the last pixels near 1050 nm as your "matrix" for that window.  
**Option B (dedicated):** 3–8 discrete InGaAs photodiodes (G10899 series) in a custom spatial array, each with a ~1070 nm bandpass filter (FWHM 10–20 nm), read via STM32 ADC multiplexer.  
**Option C (expensive):** Hamamatsu InGaAs linear array module (G9xxx series) — $1,000+ but true multi-pixel 1070 nm detection.

### For EIS Frontend

**Recommended for broad EIS (electrochemical cell characterization):** **ADuCM355** — it has the widest frequency range (0.016 Hz–200 kHz), best impedance range (<1 Ω–10 MΩ), onboard potentiostat and DFT engine, and is itself an ARM MCU. It can off-load all EIS computation from the main STM32.  
**Simple/low-cost EIS:** **AD5933** or **AD5934** — minimal external components, I²C, $6–12, extensive community support, limited to 1 kHz–100 kHz.  
**Bio-impedance only:** **MAX30001** — excellent for tissue impedance/body composition, tiny WLP package, but not a general electrochemical EIS solution.

---

## Sources

| Source | Relevance |
|--------|-----------|
| [AMS-OSRAM AS7341 product page](https://ams.com/en/as7341) | Specs, status, ordering |
| [AMS-OSRAM AS7343 product page](https://ams.com/as7343) | Specs, 14-channel details |
| [AMS AS7265x product page](https://ams.com/en/as7265x) | 18-channel chipset specs |
| [Hamamatsu C12880MA product page](https://www.hamamatsu.com/us/en/product/optical-sensors/spectrometers/mini-spectrometer/C12880MA.html) | Specs, 340–850 nm, $286 |
| [Hamamatsu C14384MA-01 datasheet (digchip)](https://www.digchip.com/datasheets/download_datasheet.php?id=174270&part-number=C14384MA-01) | 640–1050 nm specs, 11.5×4×3.1 mm |
| [Analog Devices AD5933](https://www.analog.com/en/products/ad5933.html) | EIS IC, $11.45, I²C |
| [Analog Devices ADuCM355](http://www.analog.com/ADuCM355) | Full electrochemical AFE MCU, $11.58 |
| [Analog Devices MAX30001](https://www.analog.com/en/products/max30001.html) | BioZ AFE, $8.79, SPI |
| [TI OPT4048 datasheet](https://www.ti.com/lit/ds/symlink/opt4048.pdf) | 4-channel XYZ, I²C |
| [TI AFE4300 product page](https://www.ti.com/tool/AFE4300EVM-PDK) | Body impedance, single-freq |
| [Hamamatsu G10899-01K](https://www.hamamatsu.com/us/en/product/optical-sensors/infrared-detector/ingaas-photodiode/G10899-01K.html) | Extended InGaAs 0.5–1.7 µm |
| [Melexis MLX90640](https://www.melexis.com/en/product/mlx90640/far-infrared-thermal-sensor-array) | Thermal array (NOT NIR spectroscopy) |
| [PMC study on C12880MA + STM32](https://pmc.ncbi.nlm.nih.gov/articles/PMC11479284/) | Real-world STM32 + C12880MA implementation |
| [SparkFun AS7265x hookup guide](https://learn.sparkfun.com/tutorials/spectral-triad-as7265x-hookup-guide/) | Wiring, firmware, I²C/UART modes |
| [DigiKey AS7341 listing](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/AS7341-DLGM/9996230) | Price ~£5.86 / $7.66 |
| [SparkFun AS7343 breakout](https://www.sparkfun.com/sparkfun-spectral-sensor-as7343-qwiic.html) | $21.95, Qwiic/I²C |
| [GroupGets C12880MA](https://groupgets.com/products/hamamatsu-c12880ma-mems-u-spectrometer) | Community purchase ~$220 |
| [LCSC ADuCM355](https://www.lcsc.com/product-detail/microcontrollers-mcu-mpu-soc_analog-devices-aducm355bccz_C660219.html) | C660219, LGA-72 in stock |

---

*Last updated: 2026-04-09*
