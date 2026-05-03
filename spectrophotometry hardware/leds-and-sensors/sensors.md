---
title: Spectral Sensors for Portable Spectrophotometry
aliases:
  - Jimini Sensors
  - Sensor Selection
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Spectral Sensors for Portable Spectrophotometry

STM32-compatible sensor selection for Jimini. Targets: Sensor 1 (C12-like, 321–870 nm UV-Vis), Sensor 2 (C14-like, 570–1078 nm Vis-NIR), IR matrix (~1070 nm), and EIS frontend. For component summary see [[spectrophotometry hardware/leds-and-sensors/overview]].

---

## Broadband / Multi-Channel Spectral Sensors (UV-Vis)

### AMS-OSRAM AS7341 — Best candidate for Sensor 1 (C12 replacement)

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | AMS-OSRAM |
| **Part Number** | AS7341-DLGM (LGA) / AS7341-DLGT (OLGA, newer) |
| **Spectral Range** | ~350–1000 nm (8 spectral + 3 aux channels) |
| **Channels** | 11 total: F1(415nm), F2(445nm), F3(480nm), F4(515nm), F5(555nm), F6(590nm), F7(630nm), F8(680nm), NIR(850nm), Clear, Flicker |
| **ADC Resolution** | 16-bit per channel |
| **Interface** | I²C (address 0x39) |
| **Package** | 8-TFLGA / OLGA-8 — **2.0 × 3.1 mm** |
| **Supply Voltage** | 1.7–2.0 V (IOVDD up to 3.6 V) |
| **Current (active)** | ~210 µA typical |
| **FWHM** | ~20–30 nm per channel |
| **Built-in LED driver** | Yes (up to 258 mA) |
| **Status** | AS7341-DLGM marked "Not for New Designs"; **AS7341-DLGT** is current version |
| **Price (1 qty)** | ~$5.86–7.66 USD (DigiKey/Xonelec) |
| **Where to buy** | DigiKey (`AS7341-DLGMTR-ND`), Mouser, Adafruit breakout ($12.50) |

STM32 notes: Standard I²C, 3.3 V logic compatible via IOVDD pin. Adafruit Arduino library is well-tested (Adafruit_AS7341). No official STM32 HAL driver, but the I²C register map is simple enough to port in ~200 lines. Multiple examples on GitHub for bare-metal STM32.

Vs. C12 (321–870 nm): Coverage is 350–1000 nm — slightly narrower at UV end (350 vs 321 nm) but extends further in NIR. With 8 narrow-band channels + clear + NIR + flicker it is far richer than a single-channel photodiode. Strong candidate for Sensor 1 slot.

---

### AMS-OSRAM AS7343 — Upgraded AS7341, More UV Channels

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
| **Price (1 qty)** | ~$8–12 USD |
| **Breakout** | SparkFun SEN-23220 (Qwiic) — **$21.95** |
| **Where to buy** | DigiKey, Mouser, LCSC (`AS7343-DLGM C19085986`), SparkFun |

STM32 notes: Drop-in upgrade from AS7341 — same I²C footprint, same register structure. SparkFun Arduino/Qwiic library available.

Vs. C12 (321–870 nm): Coverage starts at 380 nm (vs 321 nm needed). The UV gap below 380 nm may need supplemental UV photodiode if UV absorbance is required. Otherwise this is a better choice than AS7341 for the 14-channel coverage.

---

### AMS-OSRAM AS7265x (18-channel, 3-Chip Set)

| Parameter | Value |
|-----------|-------|
| **Chipset** | AS72651 (master, 600–870 nm) + AS72652 (560–940 nm) + AS72653 (410–535 nm) |
| **Spectral Range** | 410–940 nm combined |
| **Channels** | 18 channels across 3 ICs (6 each), ~35 nm spacing |
| **FWHM** | 20 nm per channel |
| **Interface** | UART (AT commands) or I²C to AS72651 master |
| **Package** | LGA-16 per IC, ~3.3 × 3.5 mm each |
| **Status** | "Ordering and shipping still possible" — **approaching EOL** |
| **Price (chips)** | ~$5–8 per IC × 3 = ~$15–25 total |
| **Breakout** | SparkFun Triad Spectroscopy Sensor SEN-15050 — ~**$80** |

STM32 notes: AT-command UART interface simplifies firmware — send ASCII commands, receive calibrated readings. Alternatively use I²C to AS72651. SparkFun has open-source Arduino library.

Limitation for Sensor 1: Does not reach below 410 nm (UV gap). 940 nm NIR edge.

---

### Hamamatsu C12880MA — Direct C12 Reference Module

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
| **Price** | **$286** (Hamamatsu shop) / ~$215 (eBay/GroupGets) |
| **Where to buy** | [shop.hamamatsu.com](https://shop.hamamatsu.com/products/micro-spectrometer-c12880ma), GroupGets, eBay |

STM32 notes: **No I²C or SPI** — uses custom clocked analog readout. STM32 drives CLK + ST digital signals; ADC samples the VIDEO analog pin synchronously. Requires a 12-bit (minimum) ADC on STM32 running at ~2–5 MHz. Use TIM + ADC DMA for efficient acquisition. Open-source STM32/Arduino drivers exist. Total acquisition time ~few ms for 288 pixels.

Best match for Sensor 1: Spectral range 340–850 nm is the closest available commercial module to the 321–870 nm requirement.

---

### Hamamatsu C14384MA-01 — Direct C14 Reference Module

| Parameter | Value |
|-----------|-------|
| **Manufacturer** | Hamamatsu Photonics |
| **Part Number** | C14384MA-01 |
| **Spectral Range** | **640–1050 nm** (covers 570–1078 nm target partially) |
| **Resolution** | 17–25 nm (FWHM) |
| **Interface** | **Analog** clocked readout (CLK, ST, VIDEO) — same as C12880MA |
| **Package** | **Ultra-compact: 11.5 × 4.0 × 3.1 mm**, 0.3 g |
| **Supply** | 4.75–5.25 V (Vs) |
| **Sensitivity** | 50× improvement at 1000 nm vs predecessor C11708MA |
| **Price** | ~$600–700 USD (quote-based) |
| **Where to buy** | Hamamatsu direct (quote), Farnell, Newark |

STM32 notes: Same analog clocked readout as C12880MA — STM32 drives CLK/ST, reads VIDEO via ADC + DMA. The 5 V supply requires level shifting for 3.3 V STM32 I/O. The lower edge starts at 640 nm (vs 570 nm needed) and the upper edge at 1050 nm (vs 1078 nm needed).

Best match for Sensor 2: Covers most of 570–1078 nm range. Gap at 570–640 nm can be bridged by AS7341/AS7343 red channels.

---

## NIR Spectral Sensors (570–1078 nm)

### AMS-OSRAM AS7263 (6-channel NIR)

| Parameter | Value |
|-----------|-------|
| **Spectral Range** | **610–860 nm** (6 channels: R@610, S@680, T@730, U@760, V@810, W@860 nm) |
| **FWHM** | 20 nm per channel |
| **Interface** | I²C or UART (AT commands) |
| **Package** | LGA-16 (~3.3 × 3.5 mm) |
| **Price** | ~$5–10 USD chip; SparkFun SEN-14351 breakout ~$16 |
| **Status** | Active |

Coverage gap: Only 610–860 nm — misses 570–610 nm lower end and >860 nm upper end of the 570–1078 nm target. Use alongside AS7341 for broader NIR.

---

### Hamamatsu InGaAs Photodiodes (G-series)

For **single-point or few-point NIR detection** in the 900–1700 nm range:

| Part Number | Range | Active Area | Package | Notes |
|-------------|-------|-------------|---------|-------|
| **G10899-01K** | 0.5–1.7 µm | 1 mm dia | TO-18 metal | Extended InGaAs, covers 570–1700 nm |
| **G10899-005K** | 0.5–1.7 µm | 0.5 mm dia | TO-18 | Smaller active area, lower capacitance |
| **G8370-01** | 0.9–1.7 µm | 1 mm dia | TO-18 | Standard InGaAs |

Price: ~$50–200 each (Hamamatsu direct, quote-based for volume)

Extended InGaAs (G10899 series) is the correct choice when sensitivity from **500–700 nm extending to 1700 nm** is needed — covers the full 570–1078 nm window in a single detector element, but without spectral discrimination.

---

## IR Matrix Sensors (~1070 nm Multi-Pixel)

> [!IMPORTANT]
> Most "IR matrix" sensors on the market are **thermal/far-IR** (8–14 µm range, e.g., Melexis MLX90640). For **near-IR at 1070 nm**, you need a photodetector, not a thermopile array.

### Melexis MLX90640 (Thermal Array — NOT 1070 nm)

| Parameter | Value |
|-----------|-------|
| **Type** | Far-infrared thermopile array |
| **Spectral range** | **8–14 µm** (thermal emission detection) |
| **Resolution** | 32×24 pixels |
| **Interface** | I²C |
| **Price** | ~$15–25 |

> [!CAUTION]
> MLX90640 detects thermal radiation (body heat, surface temperature). It cannot detect 1070 nm near-IR light. Do NOT use for near-IR spectrophotometry.

### Hamamatsu InGaAs Linear Arrays (Correct Choice)

For a **true multi-pixel NIR detector at ~1070 nm**:

| Part | Type | Pixels | Range | Interface | Notes |
|------|------|--------|-------|-----------|-------|
| **G9202-256W** | InGaAs linear array | 256 | 0.9–1.7 µm | Analog video out | $$$, lab grade |
| **G9204-512W** | InGaAs linear array | 512 | 0.9–1.7 µm | Analog video out | $$$$, research |
| **G6849-01** | Segmented InGaAs | 2 segments | 0.9–1.7 µm | Analog | Low cost, 2-pixel |

Price: Linear InGaAs arrays are expensive ($500–$5,000+). Mostly available direct from Hamamatsu; require dedicated driver circuitry.

### Recommended Path for 1070 nm Multi-Pixel

- **Option A (pragmatic):** The C14384MA-01 already provides a multi-pixel linear array at 640–1050 nm — treat the last pixels near 1050 nm as the "matrix" for that window.
- **Option B (dedicated):** 3–8 discrete extended-InGaAs photodiodes (G10899 series) in a custom spatial array, each with a ~1070 nm bandpass filter, read via STM32 ADC multiplexer.
- **Option C (expensive):** Hamamatsu InGaAs linear array module (quote required, $1,000+).

---

## EIS Frontend ICs

### Analog Devices AD5933 — Primary EIS IC

| Parameter | Value |
|-----------|-------|
| **Part Number** | AD5933YRSZ (SSOP-16) |
| **Function** | Impedance converter, network analyzer |
| **Frequency range** | 1 kHz – 100 kHz |
| **ADC** | 12-bit, 1 MSPS |
| **Impedance range** | **1 kΩ – 10 MΩ** (natively); **100 Ω – 1 kΩ** with external circuit |
| **System accuracy** | 0.5% |
| **Interface** | **I²C** (address 0x0D) |
| **Package** | SSOP-16 (5.3 × 6.2 mm) |
| **Supply** | 2.7–5.5 V (single supply) |
| **Price (1 qty)** | ~**$11.45** (ADI list) |
| **Where to buy** | DigiKey, Mouser, Arrow |

STM32 notes: Pure I²C interface — direct connection to STM32 I²C peripheral. The AD5933 requires a calibration resistor and current sense resistor for absolute impedance measurement. Key limitation: internal oscillator accuracy limits lowest useful frequency to ~1 kHz.

---

### Analog Devices AD5934 (Lower-Cost Variant)

| Parameter | Value |
|-----------|-------|
| **Part Number** | AD5934YRSZ |
| **Difference from AD5933** | 250 kSPS ADC (vs 1 MSPS), max freq ~100 kHz |
| **Interface** | I²C |
| **Package** | SSOP-16 |
| **Price (1 qty)** | ~**$6.13** |
| **Where to buy** | DigiKey, Mouser |

Use case: When cost is primary concern. Almost identical firmware to AD5933.

---

### Analog Devices ADuCM355 — Full Electrochemical AFE MCU

| Parameter | Value |
|-----------|-------|
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
| **Price (1ku)** | ~**$11.58** list |
| **Where to buy** | Mouser, DigiKey, LCSC (C660219) |

STM32 notes: The ADuCM355 is itself an ARM Cortex-M3 MCU — it can be used **standalone** for the EIS measurement, with results reported to the main STM32 via SPI/UART/I²C. The onboard DFT engine and programmable waveform generator mean the host STM32 can simply command a sweep and collect processed impedance data. **Best choice for a serious EIS application** — supports 3-electrode electrochemical cells directly.

---

### Analog Devices MAX30001 (BioZ / ECG)

| Parameter | Value |
|-----------|-------|
| **Part Number** | MAX30001CWV+T |
| **Type** | Biopotential (ECG) + Bioimpedance AFE |
| **BioZ frequency** | 8 Hz – 131 kHz AC excitation |
| **BioZ range** | Designed for body impedance (10 Ω – 10 kΩ range) |
| **Interface** | **SPI** (up to 10 MHz) |
| **Package** | WLP-30 (2.7 × 2.9 mm) — very small |
| **Price (1 qty)** | ~**$8.79** list |
| **Where to buy** | DigiKey, Mouser, LCSC (C2650384) |

Limitation for EIS: Optimized for **biological tissue impedance**. Less suitable for wide-range electrochemical EIS vs ADuCM355 or AD5933.

---

## Comparison Tables

### Broadband Spectral Sensors — Sensor 1 Candidates (321–870 nm)

| Sensor | Range | Channels | Interface | Package | Price | STM32 Ease | Notes |
|--------|-------|----------|-----------|---------|-------|------------|-------|
| **C12880MA** | 340–850 nm | 288 | Analog CLK | 20×12×10 mm | $286 | Medium | Grating spectrometer, 15 nm resolution |
| **AS7343** | 380–1000 nm | 14 | I²C | 2×3.1 mm | ~$10 | Easy | Best all-round chip; UV gap below 380 nm |
| **AS7341** | 350–1000 nm | 11 | I²C | 2×3.1 mm | ~$6–8 | Easy | NFND status; use AS7343 instead |
| **AS7265x** | 410–940 nm | 18 | I²C/UART | 3× LGA-16 | ~$80 (kit) | Easy | 3-chip system; UV gap below 410 nm |
| **OPT4048** | 400–900 nm | 4 (XYZ+W) | I²C | 2×1.35 mm | ~$3 | Very Easy | Colorimetric only, not spectrophotometry |

### NIR Sensors — Sensor 2 Candidates (570–1078 nm)

| Sensor | Range | Channels | Interface | Package | Price | STM32 Ease | Notes |
|--------|-------|----------|-----------|---------|-------|------------|-------|
| **C14384MA-01** | 640–1050 nm | Multi-pixel | Analog CLK | 11.5×4×3.1 mm | ~$600 | Medium | Grating NIR, 17–25 nm resolution |
| **AS7263** | 610–860 nm | 6 | I²C/UART | LGA-16 | ~$8–10 | Easy | Limited range; good companion to AS7341 |
| **G10899-01K** | 500–1700 nm | 1 (broadband) | Analog TIA | TO-18 | ~$80–150 | Hard | Single detector; needs external filter for spectroscopy |

### EIS Frontend ICs

| IC | Freq Range | Impedance Range | Interface | Package | Price | Notes |
|----|------------|-----------------|-----------|---------|-------|-------|
| **ADuCM355** | 0.016 Hz–200 kHz | <1 Ω–10 MΩ | SPI/I²C/UART | LGA-72 (5×6mm) | $11.58 | Full MCU, DFT onboard, potentiostat |
| **AD5933** | 1 kHz–100 kHz | 100 Ω–10 MΩ | I²C | SSOP-16 | $11.45 | Simple, widely used, 12-bit |
| **AD5934** | 1 kHz–100 kHz | 100 Ω–10 MΩ | I²C | SSOP-16 | $6.13 | Lower cost AD5933 variant |
| **MAX30001** | 8 Hz–131 kHz | ~10 Ω–10 kΩ | SPI | WLP-30 | $8.79 | Bio-impedance focus; tiny package |

---

## STM32 Integration Notes

### I²C Sensors (AS7341, AS7343, AS7263, AD5933, AD5934)

```c
// Standard STM32 HAL I2C pattern
HAL_I2C_Master_Transmit(&hi2c1, ADDR<<1, reg_buf, 2, 100);
HAL_I2C_Master_Receive(&hi2c1, ADDR<<1, data_buf, len, 100);
```

- AS7341/AS7343: address `0x39` fixed (pull INT pin for interrupt-driven reads)
- AD5933: address `0x0D` fixed; write to `0x80` (control reg), `0x82` (start freq), then poll status
- AS7265x (I²C mode): route through AS72651 master at `0x49`

### UART Sensors (AS7265x AT-Command Mode)

```c
// Example AT command to AS7265x
HAL_UART_Transmit(&huart2, "ATDATA\r\n", 8, 100);
HAL_UART_Receive_DMA(&huart2, rx_buf, 512);
```

AT-command mode returns calibrated float values as ASCII strings.

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
- C12880MA VIDEO signal: 0–3.3 V range, ~1 µs settling time per pixel

### Power / Voltage Considerations

| Sensor | VDD | STM32 3.3V? | Notes |
|--------|-----|-------------|-------|
| AS7341/AS7343 | 1.7–2.0 V | Via IOVDD pin (3.3 V ok) | Internal LDO; IOVDD level-shifts I²C |
| C12880MA | 3.3 V (Vdd) + 3.3 V input | ✅ | Analog output 0–3.3 V |
| C14384MA-01 | **5 V (Vs)** | Need 5 V rail | I/O may need level shift |
| AD5933 | 2.7–5.5 V | ✅ 3.3 V | I²C 3.3 V safe |
| ADuCM355 | 1.8 V + 3.3 V | ✅ | Dual supply; use LDO from STM32 board 3.3 V |
| MAX30001 | 1.1–1.8 V (core), 1.7–3.6 V IO | ✅ via 3.3 V IO | Tiny WLP package |

---

## Sensor Selection Guidance

### For Sensor 1 (321–870 nm, UV-Vis, "like C12")

**Recommended:** Hamamatsu **C12880MA** if full 288-channel spectral resolution is needed (grating spectrometer, ~15 nm resolution, $286).
**Budget alternative:** AMS-OSRAM **AS7343** — 14 channels, I²C, 8× cheaper, drop-in 2×3.1 mm chip. Limited to 380–1000 nm (UV gap below 380 nm).
**Extended UV:** If 321–380 nm is critical, add a **UV photodiode** (e.g., Hamamatsu S1226-8BQ, 190–1000 nm) + bandpass filter + TIA as a supplemental UV channel alongside the AS7343.

### For Sensor 2 (570–1078 nm, Vis-NIR, "like C14")

**Recommended:** Hamamatsu **C14384MA-01** — covers 640–1050 nm, ultra-compact module. Gap at 570–640 nm can be bridged by AS7341/AS7343 red channels (590–680 nm region). Gap above 1050 nm (to 1078 nm) is small and may be acceptable.
**Cheaper alternative:** **AS7265x** 3-chip system covers 410–940 nm at 18 channels.
**If 1078 nm is hard requirement:** Add a single InGaAs photodiode (G10899 series, 500–1700 nm) with a ~1070 nm bandpass filter.

### For EIS Frontend

**Recommended for broad EIS (electrochemical cell characterization):** **ADuCM355** — widest frequency range (0.016 Hz–200 kHz), best impedance range, onboard potentiostat and DFT engine.
**Simple/low-cost EIS:** **AD5933** or **AD5934** — minimal external components, I²C, $6–12, extensive community support, limited to 1 kHz–100 kHz.

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
| [Hamamatsu G10899-01K](https://www.hamamatsu.com/us/en/product/optical-sensors/infrared-detector/ingaas-photodiode/G10899-01K.html) | Extended InGaAs 0.5–1.7 µm |
| [PMC study on C12880MA + STM32](https://pmc.ncbi.nlm.nih.gov/articles/PMC11479284/) | Real-world STM32 + C12880MA implementation |
| [SparkFun AS7265x hookup guide](https://learn.sparkfun.com/tutorials/spectral-triad-as7265x-hookup-guide/) | Wiring, firmware, I²C/UART modes |
| [DigiKey AS7341 listing](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/AS7341-DLGM/9996230) | Price ~£5.86 / $7.66 |
| [SparkFun AS7343 breakout](https://www.sparkfun.com/sparkfun-spectral-sensor-as7343-qwiic.html) | $21.95, Qwiic/I²C |
| [GroupGets C12880MA](https://groupgets.com/products/hamamatsu-c12880ma-mems-u-spectrometer) | Community purchase ~$220 |
| [LCSC ADuCM355](https://www.lcsc.com/product-detail/microcontrollers-mcu-mpu-soc_analog-devices-aducm355bccz_C660219.html) | C660219, LGA-72 in stock |

## Gaps

1. **STM32 bare-metal AS7341 driver:** No complete STM32 HAL example found. Action: Port SparkFun Arduino library (Apache 2.0 license) to STM32; I²C register map is fully documented in AMS UG000400.
2. **EIS alternative to AD5933:** AD5941 (lower power, SPI) may be better for battery-powered pen device. Action: Compare AD5933 vs AD5941 datasheets for power budget and interface compatibility.
3. **C12880MA stray light below 400 nm:** Known issue (elevated baseline from MEMS grating design). Characterization against a calibrated reference spectrometer needed for the 275–400 nm range on Jimini prototypes.
4. **AS7343 UV gap (380–400 nm):** May need a supplemental UV photodiode channel if absorption at 280 nm (protein) or 293 nm ([[uric-acid|uric acid]] peak) is required independently of the C12880MA.

[spectrophotometry hardware/leds-and-sensors/overview]: overview.md "LEDs & Sensors — Component Overview"
[uric-acid|uric acid]: ../../biomarkers/papers/singleBiomarkers/sheets/metabolites/uric-acid.md "Uric Acid"
