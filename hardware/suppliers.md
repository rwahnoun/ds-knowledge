# Suppliers & Distributors for UV/Vis/NIR LEDs and Spectral Sensors

> **Device context:** Pen-sized portable spectrophotometer, STM32-based. Components needed: UV LEDs (275nm, 365nm), visible LEDs (405nm, 455nm, white CRI>95), NIR LED (1070nm), multi-channel spectral sensors, EIS IC.

---

## 1. Major Distributors — Coverage Summary

| Distributor                           | Deep UV (275nm)                | 365nm UV          | Vis LEDs     | AS7341                | Hamamatsu        | AD5933 Eval      | Notes                                                          |
| ------------------------------------- | ------------------------------ | ----------------- | ------------ | --------------------- | ---------------- | ---------------- | -------------------------------------------------------------- |
| **Digi-Key**                          | Limited (via specialty brands) | ✅ Nichia NVSU233B | ✅ Full range | ✅ In stock            | ✅ C12880MA       | ✅ EVAL-AD5933EBZ | MOQ 1; best datasheet access; full datasheets always available |
| **Mouser**                            | Limited                        | ✅ Nichia          | ✅ Full range | ✅ In stock + eval kit | Indirect         | ✅                | MOQ 1; strong inventory for AMS-OSRAM                          |
| **RS Components**                     | ✅ Seoul Viosys CUD7GF1B        | ✅                 | ✅            | ✅ AS7341 Eval Kit     | Indirect         | ✅                | Good EU stock; Korean/Asian brands well-represented            |
| **Farnell / Newark**                  | Indirect                       | ✅                 | ✅            | Available             | ✅ C14384MA-01    | ✅                | Best for Hamamatsu SMD spectrometers                           |
| **Arrow Electronics**                 | Indirect                       | ✅                 | ✅            | ✅                     | Contact required | ✅                | Best for high-volume; negotiated pricing                       |
| **Future Electronics**                | ✅ Nichia NCSU334B (280nm)      | ✅                 | ✅            | ✅                     | Contact required | ✅                | Nichia authorised distributor                                  |
| **CDI (Component Distributors Inc.)** | ✅ Crystal IS Klaran & Optan    | Limited           | Limited      | ❌                     | ❌                | ❌                | **Specialist for Crystal IS** — only US stocking distributor   |
| **LED Supply (ledsupply.com)**        | ✅ Seoul Viosys module          | ✅                 | ✅            | ❌                     | ❌                | ❌                | Module-level, not bare die                                     |
| **Laser Components**                  | ✅ Bolb Inc. (exclusive EU/US)  | ✅                 | ❌            | ❌                     | ❌                | ❌                | Exclusive Bolb distributor for US + Europe                     |
|                                       |                                |                   |              |                       |                  |                  |                                                                |

**Key takeaway:** No single distributor covers everything. You need CDI or Laser Components for deep UV, Digi-Key/Mouser for sensors and ICs, and Hamamatsu's own shop for their spectrometers.

---

## 2. Deep UV LEDs — 275nm

These are specialty components requiring AlGaN or AlN semiconductor material. Available power and efficiency drop sharply below 300nm.

### 2.1 Crystal IS — Optan Series (Sensing-Optimized)

- **Website:** [cisuvc.com/products/optan](http://www.cisuvc.com/products/optan)
- **Subsidiary of Asahi Kasei** (Japan); fabricated on proprietary bulk AlN substrates in Green Island, NY
- **Optan BL Series** (Ball Lens): Peak wavelengths 250–275nm in **5nm bins**

| Part Number | Peak λ (bin) | Min Output | Max Output | @ Current | Application |
|---|---|---|---|---|---|
| OPTAN-275J-BL | 270–280nm | 1.0 mW | 3.0 mW | 100mA | Low-power sensing |
| OPTAN-275K-BL | 270–280nm | 5.0 mW | — | 100mA | Higher-power sensing |

- **FWHM:** ~10–12nm (very narrow — critical for spectroscopy)
- **Package:** Ball lens (tight 15° radiation pattern — ideal for coupling into fibers or cuvettes)
- **Where to buy:** [CDI (led.cdiweb.com)](https://led.cdiweb.com/manufacturer/crystal-is/uvc-led/optan-ball-lens) — primary US stocking distributor; also [Worldictown.com](https://worldictown.com/productdetail/OPTAN-275J-BL) for sourcing quotes
- **MOQ:** Contact CDI (typically 1–5 units for prototyping)
- **Lead time:** Some variants in stock; others 6–8 weeks
- **Datasheet quality:** ⭐⭐⭐⭐⭐ — Full spectral emission curves, FWHM, angular distribution, lifetime data

> **⚠ Spectroscopy note:** Optan is **explicitly designed for absorption and fluorescence measurement**, not just disinfection. Crystal IS provides application notes on cuvette coupling. This is the **preferred 275nm source for spectrophotometry**.

---

### 2.2 Seoul Viosys — Violeds CUD7GF1B

- **Website:** [seoulviosys.com](https://www.seoulviosys.com/en/product/violet)
- **Part:** CUD7GF1B — CA3535 ceramic package
- **Specs:** 275nm peak, **16mW** optical output, 5.6V@100mA, 125° viewing angle, 200mA max drive
- **Where to buy:**
  - RS Components: Stock No. 247-1977, ~£8–12/unit, **in stock**
  - LED Supply: Module version A00x-EGBF27508, ~$21.77 (board-mounted with heatsink)
  - Sanqianjia Technology (Chinese secondary market): [uv-disinfect.com](https://www.uv-disinfect.com/seoul-viosys-ultraviolet-uv-c-275nm-deep-uv-led-ca3535-cud7gf1b/)
- **MOQ:** 1 unit at RS; module version from LED Supply has no MOQ
- **Lead time:** Usually in stock at RS
- **Datasheet quality:** ⭐⭐⭐⭐ — Spectral emission graph provided, binning table included

> **Vs Crystal IS Optan:** Seoul Viosys offers ~3× higher power (16mW vs 3mW at 100mA) but does **not** bin as tightly on wavelength. For spectroscopy where exact λ matters, verify the emission peak with a reference spectrometer before use.

---

### 2.3 Bolb Inc. — S6060 SMD 275nm (High Power)

- **Website:** [bolb.co/s6060-smd-275-nm](https://bolb.co/s6060-smd-275-nm/)
- **Claims:** "World's highest-power single-chip UVC LED" and "World's most efficient high-power UVC LED"
- **Key specs:**
  - Peak: 263–273nm (note: below 275nm — check exact bin for absorption band alignment)
  - **100mW @ 250mA**, 140mW @ 350mA
  - Wall-plug efficiency: **7%** (best-in-class)
  - L70 lifetime: **8,000 hrs** (measured and certified)
  - 6×6mm SMD package (industry standard footprint)
  - Forward voltage: ~6–7V
- **Where to buy:**
  - **Laser Components USA, Inc.** — exclusive US distributor: [lasercomponents.com](https://www.lasercomponents.com/en/supplier/bolb-inc/)
  - **Laser Components GmbH** — exclusive European distributor
  - **WPG North America** — North American distribution
  - **Griot Group, Inc.** (US West Coast): +1 503 726-4445, dbutts@griotgroup.com
  - **Alltek** (China), **Prohubs** (Taiwan)
  - **Anglia Components** (UK)
- **MOQ:** Contact Laser Components; typically 5–25 units for prototyping
- **Datasheet quality:** ⭐⭐⭐⭐ — Emission spectrum provided, efficiency curves

> **For spectroscopy:** Bolb's peak at 263–273nm is slightly shifted from the 275nm absorption peak of many analytes. **Verify the exact bin** with the distributor before ordering.

---

### 2.4 Nichia — NCSU334B (280nm, closest production Nichia UVC)

- **Website:** [nichia.co.jp](https://led-ld.nichia.co.jp/en/product/uv_uvc.html)
- **Part:** NCSU334B — 280nm peak (not 275nm), 70mW, 1.8W drive, 3535 glass package
- **Where to buy:** Future Electronics (North America/Europe), Lumistrips (~$94.49/unit on PCB)
- **Note:** Nichia's deep UVC offerings are 280nm-centered, not 275nm. For 275nm specifically, Crystal IS or Seoul Viosys are better options.

---

### 2.5 Chinese / Shenzhen Suppliers — Assessment

| Supplier | Claimed λ | Power | Quality Assessment |
|---|---|---|---|
| **Zhuhai Tianhui** ([tianhuiuvled.com](https://www.tianhuiuvled.com/275nm-uv-led/)) | 275nm | Various | Mid-tier manufacturer; basic spectral data; no wavelength binning |
| **Anhui Zixin Semiconductor** ([ahuvc.cn](http://www.ahuvc.cn/en/)) | 255–315nm full range | Various | AlGaN MOCVD in-house; provides chip + package options; limited English docs |
| **Shenzhen Taoyuan Optoelectronics** ([ledwv.com](https://www.ledwv.com/-p-520.html)) | 275nm | 160–200mW@600mA | COB format; high power, but thermal management critical; specs unreliable without third-party test |

> **Chinese supplier quality reality:** Reputable Tier-2 Chinese UVC LED manufacturers (like Anhui Zixin) have made real progress with AlGaN MOCVD, but:
> - **Wavelength binning is typically ±10nm or wider**, vs ±5nm from Crystal IS/Seoul
> - **Spectral emission curves** are often absent or generic
> - **Lifetime data** is rarely measured or certified
> - **For spectrophotometry**: acceptable for exploratory builds if you characterize every unit yourself; **not acceptable** for calibrated instruments without individual characterization

---

## 3. UV-A and Visible LEDs

### 3.1 365nm UV-A

**Recommended: Nichia NVSU233B** — the current gold standard

- **Part:** NVSU233B (365nm) — 3535 glass package, 3.5×3.5×1.23mm
- **Specs:** 1450mW radiant flux @ 1000mA, 1400mA max IF, 3.85V typical VF
- **Status:** In production (Recommended model, released 2021/10)
- **Packaging:** 1400/reel
- **Downloads from Nichia:** Full spectral curve, Zemax/LightTools ray data files ✅
- **Where to buy:** Through Nichia authorised distributors (Future Electronics, select Digi-Key/Mouser listings)
- **Also in portfolio:**
  - NWSU333B: 4900mW high-power 365nm (larger package)
  - NVSU233C-D4: Narrow distribution variant

**Also available:**
- Broadcom AUV3-ST32-0SV0K: 395nm, 1460mW, 3-LED array — RS Components UK in stock (215-5752), ~£6.45/unit

---

### 3.2 405nm Violet LED

**Recommended: Nichia NCSU035D** (2022+ model)

- 6.8×6.8×1.9mm package
- Full spectral + Zemax ray data available from Nichia
- Packaging: 500/reel
- Status: In production (Recommended)
- **Where to buy:** Nichia distributor network; Digi-Key, Mouser

> **Application note for 405nm in spectrophotometry:** 405nm is the classic mercury lamp alternative for visible range spectrophotometry (matches the 405nm Hg line). Widely used for bilirubin, NADH, and protein assays.

---

### 3.3 455nm Royal Blue LED

- Wide availability; Cree XP-E2, Nichia, OSRAM OSLON all make 455nm emitters
- Available at Digi-Key, Mouser with no MOQ constraints
- Royal blue (440–460nm) is commonly used for fluorescence excitation (excites most GFP/FITC-like fluorophores) and visible-range turbidity measurements

---

## 4. White LEDs for Spectrophotometry (CRI > 95)

For broadband illumination in spectrophotometry, the LED must have a **smooth, continuous spectral emission** — spiky or uneven spectra create wavelength-dependent measurement errors that are hard to correct.

### 4.1 Nichia Optisolis NF2W757G-F1 — **Top Pick for Spectrophotometry**

- **Package:** 3×3×0.65mm (standard SMD)
- **Technology:** Blue LED pump + proprietary multi-phosphor blend
- **Key specs:** Ra≥95 (guaranteed), **Ra 98–99 typical**, R9≥85, 65mA IF, 2.9V VF, 23lm
- **Spectral properties:** Near-D65 daylight spectrum; near-zero UV emission (<380nm); essentially **no spectral gaps** in the visible range
- **Download:** Full spectral power distribution from Nichia portal (spectral curve data available)
- **Where to buy:** TDElektronik ([tdelektronik.com](https://www.tdelektronik.com/en/product/nf2w757g-f1)), specialty LED shops
- **Use in spectrophotometry:** Optimal for transmission/reflection measurements across 400–700nm; stable enough for colorimetry

> **⚠ Limitation:** Uses blue-pump LED at ~450nm — this causes a residual "blue bump" in the emission spectrum (see figure in datasheet). For critical spectroscopy needing smooth 440–470nm coverage, see SunLike below.

---

### 4.2 Seoul SunLike (TRI-R Technology) — Best for Smooth Blue Region

- **Technology:** **Violet LED pump** (not blue) + Toshiba TRI-R (Red-Green-Blue phosphor blend)
- **Key advantage:** Violet pump at ~405nm means the 440–470nm "blue bump" artifact is eliminated — spectrum is **much smoother** across 400–500nm
- **CRI:** Typ. **97** on the BBL (above the blackbody locus)
- **Available SKUs:** COB series S4SM-1063xx9736 (13.5×13.5mm, 9.8mm LES), MacAdam 3-step binning
- **Where to buy:** 
  - Digi-Key: Datasheet available ([Seoul Semi PDF via Digi-Key](https://media.digikey.com/pdf/Data%20Sheets/Seoul%20Semiconductor/S4SM-1063xx9736-0B000G3S-00001.pdf))
  - Seoul Semiconductor direct distribution network
  - JLCPCB parts library
- **CCT options:** 2700K, 3000K, 4000K, 5000K, 6500K

> **For spectrophotometry:** SunLike is arguably **better than Optisolis** in the 400–480nm range due to the violet pump architecture. However, it comes in larger COB formats — for pen-sized devices, the SMD Optisolis package may be more practical.

---

### 4.3 Lumileds LUXEON SunPlus — Not Recommended for Spectrophotometry

- **Designed for:** Horticulture (plant growth, PPF optimization)
- **Spectral optimization:** Tuned for photosynthetically active radiation (PAR) — heavy red and blue spikes designed to match plant chlorophyll absorption peaks
- **CRI:** Not specified (horticultural metric is µmol/J, not CRI)
- **Available at:** Mouser, Lumileds direct
- **Conclusion:** ❌ **Avoid for spectrophotometry** — designed for plants, not broad-spectrum illumination calibration

---

### White LED Comparison Table

| LED | Technology | Ra (min) | Ra (typ) | R9 | Blue Bump | Best Use |
|---|---|---|---|---|---|---|
| Nichia Optisolis NF2W757G-F1 | Blue pump + multi-phosphor | 95 | 98–99 | ≥85 | Yes (~450nm) | Colorimetry, CRI-critical |
| Seoul SunLike S4SM-1063 | **Violet pump** + TRI-R | 97 typ | 97 | High | **No** | Spectrophotometry 400–700nm |
| Nichia NF2W585AR | 405nm pump | 83–85 | — | — | Minimal | Germicidal dual-function only |
| Lumileds SunPlus | Horticulture | N/A | N/A | N/A | N/A | ❌ Not for spectrophotometry |

---

## 5. NIR LED — 1070nm

1070nm falls at the **boundary of standard NIR and SWIR** (Short-Wave IR). Standard Si photodiodes drop off above ~1100nm, so matched detector selection is critical.

### 5.1 Ushio Epitex — SWIR LED Series (Primary Supplier)

- **Website:** [ushio.co.jp/en/led/epitex](https://www.ushio.co.jp/en/led/epitex/wavelength/swir.html)
- **Coverage:** 1050nm–1900nm in **10nm increments** (including 1070nm specifically)
- **Key part (1050nm):** SMBB1050GD-1100-05
  - 1000µm × 1000µm GaAs chip, 1050nm typical
  - Peak wavelength accuracy: ±10nm
  - SMD package (PA9T resin, silicone lens)
  - Silver-plated copper lead frame
- **1070nm:** Available as custom/semi-custom order; Epitex explicitly lists 1070nm in their SWIR wavelength lineup
- **Where to buy:** 
  - Ushio Europe / Ushio America direct
  - Marubeni Solutions (traditional Epitex distributor for Asia/US)
  - Available to prototype quantities (contact required)
- **Datasheet quality:** ⭐⭐⭐⭐⭐ — Full spectral emission curves, efficiency plots

> **Note on 1070nm:** GaAs/InGaAs LED technology is needed. Epitex is the most practical source with a true 1070nm emission bin. OSRAM's OSLON Black series (SFH 4716S) tops out at **860nm** — too short. For 1070nm±10nm, Epitex is the recommended supplier.

### 5.2 Alternatives

| Supplier | Wavelength | Notes |
|---|---|---|
| OSRAM SFH 4716S | 860nm | ❌ Too short (850nm range, now discontinued) |
| Vishay TSAL | 950nm max | ❌ Too short for 1070nm |
| Marubeni Epitex | 1000–1900nm | ✅ Same as Ushio Epitex (rebranded) |
| Tech-LED.com | Custom SWIR | ✅ Specialist for 1050nm emitters |

---

## 6. Multi-Channel Spectral Sensors

### 6.1 AMS-OSRAM AS7341 — 11-Channel Spectral Sensor

- **Website:** [ams.com/AS7341](https://ams.com/AS7341)
- **Coverage:** ~350–1000nm, 11 channels:
  - 8 spectral (F1–F8): 415, 445, 480, 515, 555, 590, 630, 680nm
  - Clear (no filter), NIR (~910nm), Flicker detect
  - 6 channels processed in parallel by independent ADCs
- **Package:** OLGA-8 (2×2mm)
- **Interface:** I²C
- **Variants:** AS7341-DLGM (with glass lid), AS7341-DLGT

**Pricing (2024–2025):**

| Qty | Unit Price (USD) |
|---|---|
| 1 | $7.66 |
| 10 | $6.09 |
| 100 | $5.89 |
| 500 | $5.80 |
| 5,000 | $5.30 |

- **Where to buy:** Digi-Key, Mouser, Xon Electronics — **MOQ: 1 unit**
- **Lead time:** In stock (thousands of units at Digi-Key/Mouser)
- **Datasheet:** Full DS000504 v3 available from AMS-OSRAM and SparkFun CDN
- **Eval kit:** AS7341_EVM_SN_REFLECTION (reflection mode)
  - Available at: RS Components (Stock No. 232-9706, TWD 7,148 ≈ ~$220 USD)
  - Xon Electronics: [xonelec.com](https://www.xonelec.com/mpn/ams/as7341evalkit)
  - Connects to PC via USB; includes Windows GUI software
- **Breakout boards:**
  - Adafruit #4698: $18.95 (STEMMA QT/Qwiic)
  - SparkFun: available via Digi-Key

---

### 6.2 AMS-OSRAM AS7265x — 18-Channel Triad Spectroscopy Sensor

- **Coverage:** 410–940nm across 3 chips (18 channels total)
  - AS72651: 600–870nm (NIR master)
  - AS72652: 410–535nm (UV-VIS)
  - AS72653: 535–600nm (VIS)
- **Status:** Ordering and shipping still possible (but check lifecycle)
- **Interface:** UART/I²C (master chip controls the triad)
- **Where to buy:**
  - SparkFun Triad Spectroscopy Sensor SEN-15050 (Qwiic breakout): SparkFun Electronics
  - Bare IC via Digi-Key/Mouser
- **Use case:** When you need **410–940nm coverage in one module** without the complexity of the Hamamatsu spectrometer

---

### 6.3 Hamamatsu C12880MA — Mini-Spectrometer (Grating Type)

- **Website:** [hamamatsu.com](https://www.hamamatsu.com/us/en/product/optical-sensors/spectrometers/mini-spectrometer/C12880MA.html)
- **Specs:**
  - Form factor: **Fingertip-sized** — 20.1×12.5×10.1mm, 5g
  - Spectral range: **340–850nm**
  - Spectral resolution: **15nm max** (FWHM)
  - Technology: Reflective diffraction grating + CMOS linear image sensor
  - Hermetically sealed (improved humidity resistance)
  - Synchronized integration (electronic shutter)

**Pricing:**

| Item | Price | Where |
|---|---|---|
| C12880MA (sensor only) | **$286.00** | [shop.hamamatsu.com](https://shop.hamamatsu.com/products/micro-spectrometer-c12880ma) |
| C13016 Evaluation Circuit Board | **$952.00** | [shop.hamamatsu.com](https://shop.hamamatsu.com/products/evaluation-circuit-for-microspectrometer-c13016) |
| C12880MA from Shenzhen intermediaries | ~$280–296 | AliExpress (YIXIST Technology), Accio — check authenticity |
| C13053MA (improved variant) | Contact Hamamatsu | Farnell (0 stock per OEMSecrets) |

- **Eval board (C13016):** USB cable to PC + evaluation software — characterize the spectrometer and read spectral data. Complete getting-started kit.
- **MOQ:** 1 unit from Hamamatsu direct shop
- **Lead time:** Usually immediate from shop.hamamatsu.com

> **Critical for spectrophotometry:** Each C12880MA ships with **individual pixel-wavelength calibration data** on the body. This is essential — you use the calibration values to map pixel index to exact wavelength. Hamamatsu provides these calibration coefficients on each unit.

---

### 6.4 Hamamatsu C14384MA-01 — SMD NIR Mini-Spectrometer

- **Specs:**
  - 640–1050nm (NIR coverage)
  - Ultra-compact: **11.5×4.0×3.1mm**, 0.3g
  - Grating type, SMD package with flexible cable
- **Where to buy:** Farnell (listed, low stock), Newark (0 stock typically)
- **Price:** ~R$2,465 (BRL) from Farnell — roughly $500 USD
- **Note:** Very hard to source in small quantities. Contact Hamamatsu directly for samples.

---

### 6.5 Broadcom Qmini AFBR-S20M2xx — Research-Grade Mini-Spectrometer

- **Website:** [broadcom.com](https://www.broadcom.com/products/optical-sensors/spectrometers/)
- **Specs:**
  - Variants: DUV (185nm+), VIS, NIR (to 1100nm), extended NIR (to 1700nm via Qneo)
  - Focal length: 50mm; Grating: 300 or 600 lines/mm; Slit: 20µm
  - Detector: 2500-pixel linear CCD
  - Dynamic range: 1300:1; Stray light: <0.1%
  - Exposure: 3µs to 600s
- **Pricing:** RS Components (AFBR-S20N1N256 Qneo eval): ~**£3,598** ≈ $4,500 USD
- **Conclusion:** Industrial/research grade — overkill for a pen-sized device. Consider only if you need >850nm NIR coverage in a grating instrument.

---

## 7. EIS IC — AD5933

### Analog Devices AD5933

- **Description:** High-precision impedance converter — combines an on-board DDS frequency generator with 12-bit, 1 MSPS ADC, 1kΩ–10MΩ measurement range
- **Interface:** I²C
- **Eval board:** EVAL-AD5933EBZ
  - **Price:** ~$67.06 (Octopart aggregated; check Analog Devices direct)
  - **Where to buy:** Analog Devices webstore ([analog.com](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5933.html)), Digi-Key, Mouser
  - Includes PC-based evaluation software (Windows)
  - Application note AN-1053 provides step-by-step measurement guide
- **Lead time:** Usually in stock; MOQ 1
- **Status:** Production

> **Alternative:** AD5941 (Analog Devices) — newer, lower power, SPI interface, better suited for battery-powered applications than the AD5933 (which uses I²C with limited speed). Eval board: EVAL-AD5941BIOZ.

---

## 8. STM32 + Spectral Sensor Reference Designs

No official ST reference design exists specifically for STM32 + UV/Vis spectral sensor, but the following resources exist:

| Resource | Link | Notes |
|---|---|---|
| SparkFun AS7265x Hookup Guide | sparkfun.com | Arduino/I²C examples; easily ported to STM32 HAL |
| SparkFun AS7331 UV Sensor Hookup | sparkfun.github.io | Qwiic/I²C; 3-channel UV (UVA/B/C) |
| Open Colorimeter (IO Rodeo) | blog.iorodeo.com | Open-hardware design with AS7331; KiCad files available |
| Hamamatsu C13016 eval SW | shop.hamamatsu.com | PC-only evaluation; protocol reversible for STM32 |
| AMS AS7341 User Guide UG000400 | look.ams-osram.com | v6.00 (2022) — complete register map + timing for bare-metal drivers |
| MDPI Sensors 22-04852 | mdpi.com | Academic paper: STM32-based UV spectrum detector (UVA/B/C sensors) |

**Practical approach for STM32:**
1. Start with SparkFun breakout + Arduino to validate sensor
2. Port I²C driver to STM32 HAL using AMS register map from UG000400
3. AS7341 config: set SMUX table, set integration time, trigger measurement, read 6×ADC channels per bank

---

## 9. Spectral Data Quality — Who Provides Full Emission Spectra?

This is critical for spectrophotometry — you must know the **exact spectral shape**, not just peak wavelength.

| Manufacturer | Spectral Curve in Datasheet | Zemax/LightTools Ray Data | Wavelength Binning |
|---|---|---|---|
| **Nichia** | ✅ Yes (all LED products) | ✅ Yes (downloadable) | ✅ Per-bin specs |
| **Crystal IS (Optan)** | ✅ Yes + FWHM specified | Contact required | ✅ 5nm bins |
| **Seoul Viosys** | ✅ Yes | Limited | ✅ Per-model |
| **Seoul SunLike** | ✅ Yes (SPD curves in datasheet) | Contact required | CCT bins |
| **OSRAM/AMS-OSRAM** | ✅ Yes (all LED products) | ✅ Available | Standard |
| **Bolb Inc.** | ✅ Partial (FWHM noted) | No | Limited binning |
| **Tianhui / Shenzhen** | ⚠ Often generic/missing | ❌ No | Poor (±10nm typical) |
| **Anhui Zixin** | ⚠ Partial, request-based | ❌ No | Limited |

---

## 10. Ordering Summary — Bill of Materials Sourcing

| Component | Recommended Part | Supplier | Approx Price |
|---|---|---|---|
| 275nm UV LED | Crystal IS OPTAN-275K-BL | CDI (led.cdiweb.com) | $15–50/unit (request quote) |
| 275nm UV LED (alt) | Seoul Viosys CUD7GF1B | RS Components #247-1977 | ~£10/unit |
| 365nm UV LED | Nichia NVSU233B | Future Electronics / Digi-Key | ~$8–15/unit |
| 405nm violet LED | Nichia NCSU035D | Digi-Key / Mouser | ~$5–10/unit |
| 455nm royal blue LED | Nichia / Cree / OSRAM | Digi-Key / Mouser | $2–8/unit |
| White CRI>95 (SMD) | Nichia NF2W757G-F1 (Optisolis) | TDElektronik / specialist | ~$3–8/unit |
| White CRI>95 (COB, flat spectrum) | Seoul SunLike S4SM-1063xx | Digi-Key / Seoul Semi | ~$8–20/unit |
| 1070nm NIR LED | Ushio Epitex SWIR 1070nm | Ushio direct / Marubeni | Contact for quote |
| AS7341 11-ch sensor | AS7341-DLGT | Digi-Key / Mouser | **$7.66 @1, $5.30 @5k** |
| AS7341 Eval Kit | AS7341_EVM_SN_REFLECTION | RS Components #232-9706 | ~$220 USD |
| AS7265x 18-ch triad | AS7265x (bare IC) | Digi-Key / SparkFun breakout | ~$30–50 breakout |
| Hamamatsu mini-spectrometer | C12880MA | shop.hamamatsu.com | **$286** |
| Hamamatsu eval board | C13016 | shop.hamamatsu.com | **$952** |
| EIS IC | AD5933 | Digi-Key / Mouser | ~$8–12/unit |
| EIS Eval Board | EVAL-AD5933EBZ | analog.com / Digi-Key | **~$67** |

---

## 11. Key Purchasing Considerations

### Minimum Order Quantities
- **Digi-Key / Mouser:** MOQ = 1 for nearly all components listed above. Ideal for prototyping.
- **Crystal IS Optan:** Request-a-quote model via CDI; typically no minimum for samples.
- **Bolb Inc.:** Via Laser Components; contact for prototype quantities (5–25 units typical).
- **Hamamatsu:** shop.hamamatsu.com accepts single-unit orders with credit card.

### Lead Times (2024–2025)
- AS7341: **In stock** at Digi-Key and Mouser (thousands of units)
- Seoul Viosys CUD7GF1B: **In stock** at RS Components
- Crystal IS Optan: **Some variants in stock** at CDI; 6–8 weeks for others
- Bolb S6060: **Order required** — 2–6 weeks typical
- Hamamatsu C12880MA: **In stock** at their own shop ($286)
- Hamamatsu C13016 eval board: **In stock** at their own shop ($952)
- EVAL-AD5933EBZ: **In stock** at Digi-Key/Mouser

### Full Datasheet Availability
All major distributor platforms (Digi-Key, Mouser, RS, Farnell) provide full manufacturer datasheets as PDF downloads. AMS-OSRAM, Nichia, Hamamatsu, and Analog Devices also provide datasheets directly on their manufacturer websites without registration.

---

## Sources

### Kept
- Crystal IS Optan product page (cisuvc.com) — primary source for 275nm sensing LED specs
- Bolb Inc. S6060 product page + where-to-buy page (bolb.co) — distributor network confirmed
- RS Components CUD7GF1B listing (rs-online.com) — pricing and stock confirmed
- Hamamatsu shop (shop.hamamatsu.com) — C12880MA and C13016 pricing direct from manufacturer
- Xon Electronics AS7341 pricing (xonelec.com) — pricing table for AS7341 variants
- AMS-OSRAM AS7341 product page (ams-osram.com) — eval kit confirmed
- Nichia product pages (led-ld.nichia.co.jp) — NVSU233B, NCSU035D, NF2W757G-F1 specs
- Ushio Epitex SWIR lineup (ushio.co.jp) — 1070nm availability confirmed
- Analog Devices EVAL-AD5933 page — pricing and eval board confirmed
- Seoul SunLike datasheet (Digi-Key media CDN) — CRI 97 specs confirmed
- OEMSecrets C14384MA-01 listing — Hamamatsu NIR spectrometer pricing
- Lumistrips Optisolis blog — CRI 98–99 confirmed with spectral context

### Dropped
- Generic Alibaba/AliExpress UV LED listings — no spectral data, authenticity unverifiable
- LUXEON SunPlus (Lumileds) — confirmed horticulture product, not CRI-rated for spectrophotometry
- OSRAM SFH 4716S — 860nm, too short for 1070nm NIR requirement; also discontinued
- Broadcom Qmini AFBR-S20N1N256 eval module — £3,598 is too expensive for the application and research-grade overkill

---

## Gaps & Next Steps

1. **Exact 1070nm part number from Ushio Epitex:** Website confirms 1070nm is in the SWIR lineup, but no specific part number or datasheet link was found. **Action:** Contact Ushio directly (epitex@ushio.co.jp) or Marubeni Solutions for the exact part number and pricing for prototype quantities.

2. **Crystal IS Optan pricing:** CDI quotes required. No public per-unit pricing. **Action:** Submit request at led.cdiweb.com or contact CDI sales.

3. **AS7341 spectral response calibration data:** The sensor has channel sensitivity curves in the datasheet, but no individual calibration per-unit. **Action:** If absolute radiometric accuracy is needed, pair with a known-spectrum light source and calibrate each unit.

4. **455nm LED selection:** Not thoroughly researched — many options exist. **Action:** Thread D or follow-up search for Nichia NSSB119CT or similar royal blue emitters for STM32 PWM driving.

5. **STM32 bare-metal AS7341 driver:** No complete STM32 HAL example found. **Action:** Port SparkFun Arduino library (Apache 2.0 license) to STM32; the I²C register map is fully documented in AMS UG000400.

6. **EIS alternative to AD5933:** AD5941 (lower power, SPI) may be better for battery-powered pen device. **Action:** Compare AD5933 vs AD5941 datasheets for power budget and interface compatibility.
