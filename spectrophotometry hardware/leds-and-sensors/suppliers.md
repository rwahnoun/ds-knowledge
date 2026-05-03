---
title: Suppliers & Distributors for UV/Vis/NIR LEDs and Spectral Sensors
aliases:
  - LED Suppliers
  - Component Suppliers
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Suppliers & Distributors for UV/Vis/NIR LEDs and Spectral Sensors

Sourcing strategy for components needed on Jimini: UV LEDs (275 nm, 365 nm), visible LEDs (405 nm, 455 nm, white CRI>95), NIR LED (1070 nm), multi-channel spectral sensors, EIS IC. See [[leds]] for full LED specs and [[sensors]] for sensor specs.

---

## Major Distributors — Coverage Summary

| Distributor | Deep UV (275nm) | 365nm UV | Vis LEDs | AS7341 | Hamamatsu | AD5933 Eval | Notes |
|---|---|---|---|---|---|---|---|
| **Digi-Key** | Limited (via specialty brands) | ✅ Nichia NVSU233B | ✅ Full range | ✅ In stock | ✅ C12880MA | ✅ EVAL-AD5933EBZ | MOQ 1; best datasheet access |
| **Mouser** | Limited | ✅ Nichia | ✅ Full range | ✅ In stock + eval kit | Indirect | ✅ | MOQ 1; strong inventory for AMS-OSRAM |
| **RS Components** | ✅ Seoul Viosys CUD7GF1B | ✅ | ✅ | ✅ AS7341 Eval Kit | Indirect | ✅ | Good EU stock; Korean/Asian brands well-represented |
| **Farnell / Newark** | Indirect | ✅ | ✅ | Available | ✅ C14384MA-01 | ✅ | Best for Hamamatsu SMD spectrometers |
| **Arrow Electronics** | Indirect | ✅ | ✅ | ✅ | Contact required | ✅ | Best for high-volume; negotiated pricing |
| **Future Electronics** | ✅ Nichia NCSU334B (280nm) | ✅ | ✅ | ✅ | Contact required | ✅ | Nichia authorised distributor |
| **CDI (Component Distributors Inc.)** | ✅ Crystal IS Klaran & Optan | Limited | Limited | ❌ | ❌ | ❌ | **Specialist for Crystal IS** — only US stocking distributor |
| **Laser Components** | ✅ Bolb Inc. (exclusive EU/US) | ✅ | ❌ | ❌ | ❌ | ❌ | Exclusive Bolb distributor for US + Europe |

> [!IMPORTANT]
> No single distributor covers everything. CDI or Laser Components are required for deep UV; Digi-Key/Mouser for sensors and ICs; Hamamatsu's own shop for their spectrometers.

---

## Deep UV LEDs — 275 nm

These are specialty components requiring AlGaN or AlN semiconductor material. Available power and efficiency drop sharply below 300 nm.

### Crystal IS — Optan Series (Sensing-Optimized)

- **Website:** [cisuvc.com/products/optan](http://www.cisuvc.com/products/optan)
- **Subsidiary of Asahi Kasei** (Japan); fabricated on proprietary bulk AlN substrates in Green Island, NY
- **Optan BL Series** (Ball Lens): Peak wavelengths 250–275 nm in **5 nm bins**

| Part Number | Peak λ (bin) | Min Output | Max Output | @ Current | Application |
|---|---|---|---|---|---|
| OPTAN-275J-BL | 270–280 nm | 1.0 mW | 3.0 mW | 100 mA | Low-power sensing |
| OPTAN-275K-BL | 270–280 nm | 5.0 mW | — | 100 mA | Higher-power sensing |

- **FWHM:** ~10–12 nm (very narrow — critical for spectroscopy)
- **Package:** Ball lens (tight 15° radiation pattern — ideal for coupling into fibers or cuvettes)
- **Where to buy:** [CDI (led.cdiweb.com)](https://led.cdiweb.com/manufacturer/crystal-is/uvc-led/optan-ball-lens) — primary US stocking distributor
- **MOQ:** Contact CDI (typically 1–5 units for prototyping)
- **Lead time:** Some variants in stock; others 6–8 weeks

> [!NOTE]
> Optan is **explicitly designed for absorption and fluorescence measurement**, not just disinfection. Crystal IS provides application notes on cuvette coupling. This is the **preferred 275 nm source for spectrophotometry**.

---

### Seoul Viosys — Violeds CUD7GF1B

- **Part:** CUD7GF1B — CA3535 ceramic package
- **Specs:** 275 nm peak, **16 mW** optical output, 5.6 V@100 mA, 125° viewing angle, 200 mA max drive
- **Where to buy:**
  - RS Components: Stock No. 247-1977, ~£8–12/unit, **in stock**
  - LED Supply: Module version A00x-EGBF27508, ~$21.77 (board-mounted with heatsink)
- **MOQ:** 1 unit at RS
- **Lead time:** Usually in stock at RS

Vs Crystal IS Optan: Seoul Viosys offers ~3× higher power (16 mW vs 3 mW at 100 mA) but does **not** bin as tightly on wavelength. For spectroscopy where exact λ matters, verify the emission peak with a reference spectrometer before use.

---

### Bolb Inc. — S6060 SMD 275 nm (High Power)

- **Website:** [bolb.co/s6060-smd-275-nm](https://bolb.co/s6060-smd-275-nm/)
- **Key specs:** 100 mW @ 250 mA, 140 mW @ 350 mA; wall-plug efficiency: **7%**; L70 lifetime: **8,000 hrs** (measured and certified); 6×6 mm SMD package; Forward voltage: ~6–7 V
- **Peak:** 263–273 nm (note: below 275 nm — check exact bin for absorption band alignment)
- **Where to buy:**
  - **Laser Components USA, Inc.** — exclusive US distributor: [lasercomponents.com](https://www.lasercomponents.com/en/supplier/bolb-inc/)
  - **Laser Components GmbH** — exclusive European distributor
- **MOQ:** Contact Laser Components; typically 5–25 units for prototyping

> [!CAUTION]
> Bolb's peak at 263–273 nm is slightly shifted from the 275 nm absorption peak of many analytes. **Verify the exact bin** with the distributor before ordering.

---

## UV-A and Visible LEDs

### 365 nm UV-A

**Recommended: Nichia NVSU233B** — the current gold standard

- **Part:** NVSU233B (365 nm) — 3535 glass package, 3.5×3.5×1.23 mm
- **Specs:** 1450 mW radiant flux @ 1000 mA, 1400 mA max IF, 3.85 V typical VF
- **Status:** In production (Recommended model, released 2021/10)
- **Downloads from Nichia:** Full spectral curve, Zemax/LightTools ray data files ✅
- **Where to buy:** Through Nichia authorised distributors (Future Electronics, select Digi-Key/Mouser listings)

---

### 405 nm Violet LED

**Recommended: Nichia NCSU035D** (2022+ model)

- 6.8×6.8×1.9 mm package
- Full spectral + Zemax ray data available from Nichia
- Status: In production (Recommended)
- **Where to buy:** Nichia distributor network; Digi-Key, Mouser

> [!NOTE]
> 405 nm is the classic mercury lamp alternative for visible range spectrophotometry (matches the 405 nm Hg line). Widely used for bilirubin, [[nadh|NADH]], and protein assays.

---

### 455 nm Royal Blue LED

- Wide availability; Cree XP-E2, Nichia, OSRAM OSLON all make 455 nm emitters
- Available at Digi-Key, Mouser with no MOQ constraints
- Royal blue (440–460 nm) is commonly used for fluorescence excitation and visible-range turbidity measurements

---

## White LEDs for Spectrophotometry (CRI > 95)

For broadband illumination in spectrophotometry, the LED must have a **smooth, continuous spectral emission** — spiky or uneven spectra create wavelength-dependent measurement errors that are hard to correct.

### Nichia Optisolis NF2W757G-F1 — Top Pick for Spectrophotometry

- **Package:** 3×3×0.65 mm (standard SMD)
- **Technology:** Blue LED pump + proprietary multi-phosphor blend
- **Key specs:** Ra≥95 (guaranteed), **Ra 98–99 typical**, R9≥85, 65 mA IF, 2.9 V VF, 23 lm
- **Spectral properties:** Near-D65 daylight spectrum; near-zero UV emission (<380 nm)
- **Where to buy:** TDElektronik ([tdelektronik.com](https://www.tdelektronik.com/en/product/nf2w757g-f1)), specialty LED shops

> [!CAUTION]
> Uses blue-pump LED at ~450 nm — this causes a residual "blue bump" in the emission spectrum. For critical spectroscopy needing smooth 440–470 nm coverage, use SunLike instead.

---

### Seoul SunLike (TRI-R Technology) — Best for Smooth Blue Region

- **Technology:** **Violet LED pump** (not blue) + Toshiba TRI-R (Red-Green-Blue phosphor blend)
- **Key advantage:** Violet pump at ~405 nm eliminates the 440–470 nm "blue bump" artifact — spectrum is **much smoother** across 400–500 nm
- **CRI:** Typ. **97** on the BBL
- **Where to buy:**
  - Digi-Key: Datasheet available ([Seoul Semi PDF via Digi-Key](https://media.digikey.com/pdf/Data%20Sheets/Seoul%20Semiconductor/S4SM-1063xx9736-0B000G3S-00001.pdf))
  - Seoul Semiconductor direct distribution network

For spectrophotometry: SunLike is arguably **better than Optisolis** in the 400–480 nm range due to the violet pump architecture.

### White LED Comparison Table

| LED | Technology | Ra (min) | Ra (typ) | Blue Bump | Best Use |
|---|---|---|---|---|---|
| Nichia Optisolis NF2W757G-F1 | Blue pump + multi-phosphor | 95 | 98–99 | Yes (~450 nm) | Colorimetry, CRI-critical |
| Seoul SunLike S1S0-3030 | **Violet pump** + TRI-R | 95 | 97 | **No** | Spectrophotometry 400–700 nm |
| Yuji APS 3030 | Proprietary | 97 (guaranteed min) | — | Low | Coverage to 730 nm |

---

## NIR LED — 1070 nm

1070 nm falls at the **boundary of standard NIR and SWIR** (Short-Wave IR). Standard Si photodiodes drop off above ~1100 nm, so matched detector selection is critical.

### Ushio Epitex — SWIR LED Series (Primary Supplier)

- **Website:** [ushio.co.jp/en/led/epitex](https://www.ushio.co.jp/en/led/epitex/wavelength/swir.html)
- **Coverage:** 1050 nm–1900 nm in **10 nm increments** (including 1070 nm specifically)
- **1070 nm:** Available as custom/semi-custom order; Epitex explicitly lists 1070 nm in their SWIR wavelength lineup
- **Where to buy:**
  - Ushio Europe / Ushio America direct
  - Marubeni Solutions (traditional Epitex distributor for Asia/US)

> [!NOTE]
> GaAs/InGaAs LED technology is needed. Epitex is the most practical source with a true 1070 nm emission bin. OSRAM's OSLON Black series (SFH 4716S) tops out at **860 nm** — too short for 1070 nm.

---

## Multi-Channel Spectral Sensors

### AMS-OSRAM AS7341 — 11-Channel Spectral Sensor

- **Coverage:** ~350–1000 nm, 11 channels
- **Package:** OLGA-8 (2×2 mm)
- **Interface:** I²C

Pricing (2024–2025):

| Qty | Unit Price (USD) |
|---|---|
| 1 | $7.66 |
| 10 | $6.09 |
| 100 | $5.89 |
| 5,000 | $5.30 |

- **Where to buy:** Digi-Key, Mouser, Xon Electronics — **MOQ: 1 unit**
- **Lead time:** In stock (thousands of units at Digi-Key/Mouser)

---

### Hamamatsu C12880MA — Mini-Spectrometer (Grating Type)

- **Form factor:** Fingertip-sized — 20.1×12.5×10.1 mm, 5 g
- **Spectral range:** **340–850 nm**
- **Spectral resolution:** **15 nm max** (FWHM)

Pricing:

| Item | Price | Where |
|---|---|---|
| C12880MA (sensor only) | **$286.00** | [shop.hamamatsu.com](https://shop.hamamatsu.com/products/micro-spectrometer-c12880ma) |
| C13016 Evaluation Circuit Board | **$952.00** | [shop.hamamatsu.com](https://shop.hamamatsu.com/products/evaluation-circuit-for-microspectrometer-c13016) |

- **MOQ:** 1 unit from Hamamatsu direct shop
- **Lead time:** Usually immediate from shop.hamamatsu.com

> [!IMPORTANT]
> Each C12880MA ships with **individual pixel-wavelength calibration data** on the body. This is essential — use the calibration values to map pixel index to exact wavelength. Hamamatsu provides these calibration coefficients on each unit.

---

### Hamamatsu C14384MA-01 — SMD NIR Mini-Spectrometer

- **Specs:** 640–1050 nm; ultra-compact: **11.5×4.0×3.1 mm**, 0.3 g; grating type, SMD package
- **Where to buy:** Farnell (listed, low stock), Newark (0 stock typically)
- **Price:** ~$500 USD
- **Note:** Very hard to source in small quantities. Contact Hamamatsu directly for samples.

---

## EIS IC — AD5933

### Analog Devices AD5933

- **Description:** High-precision impedance converter — combines DDS frequency generator with 12-bit, 1 MSPS ADC, 1 kΩ–10 MΩ measurement range
- **Interface:** I²C
- **Eval board:** EVAL-AD5933EBZ — **~$67** (DigiKey, Mouser, Analog Devices webstore)
- **Lead time:** Usually in stock; MOQ 1

---

## Spectral Data Quality — Who Provides Full Emission Spectra?

Critical for spectrophotometry — you must know the **exact spectral shape**, not just peak wavelength.

| Manufacturer | Spectral Curve in Datasheet | Zemax/LightTools Ray Data | Wavelength Binning |
|---|---|---|---|
| **Nichia** | ✅ Yes (all LED products) | ✅ Yes (downloadable) | ✅ Per-bin specs |
| **Crystal IS (Optan)** | ✅ Yes + FWHM specified | Contact required | ✅ 5 nm bins |
| **Seoul Viosys** | ✅ Yes | Limited | ✅ Per-model |
| **Seoul SunLike** | ✅ Yes (SPD curves in datasheet) | Contact required | CCT bins |
| **OSRAM/AMS-OSRAM** | ✅ Yes (all LED products) | ✅ Available | Standard |
| **Bolb Inc.** | ✅ Partial (FWHM noted) | No | Limited binning |
| **Tianhui / Shenzhen** | ⚠ Often generic/missing | ❌ No | Poor (±10 nm typical) |

---

## Ordering Summary — Bill of Materials Sourcing

| Component                   | Recommended Part               | Supplier                      | Approx Price                |
| --------------------------- | ------------------------------ | ----------------------------- | --------------------------- |
| 275 nm UV LED               | Crystal IS OPTAN-275K-BL       | CDI (led.cdiweb.com)          | $15–50/unit (request quote) |
| 275 nm UV LED (alt)         | Seoul Viosys CUD7GF1B          | RS Components  247-1977       | ~£10/unit                   |
| 365 nm UV LED               | Nichia NVSU233B                | Future Electronics / Digi-Key | ~$8–15/unit                 |
| 405 nm violet LED           | Nichia NCSU035D                | Digi-Key / Mouser             | ~$5–10/unit                 |
| 455 nm royal blue LED       | ams OSRAM LD W5KM-1T4T-35      | Digi-Key / Mouser             | $2–8/unit                   |
| White CRI>95 (SMD)          | Seoul SunLike S1S0-3030        | DigiKey / Future              | ~$0.20/unit                 |
| White CRI>95 (alt)          | Nichia NF2W757G-F1 (Optisolis) | TDElektronik / specialist     | ~$3–8/unit                  |
| 1070 nm NIR LED             | Ushio Epitex SWIR 1070 nm      | Ushio direct / Marubeni       | Contact for quote           |
| AS7343 14-ch sensor         | AS7343-DLGM                    | Digi-Key / Mouser             | ~$10 @1                     |
| Hamamatsu mini-spectrometer | C12880MA                       | shop.hamamatsu.com            | **$286**                    |
| Hamamatsu NIR spectrometer  | C14384MA-01                    | Farnell / Hamamatsu direct    | **~$500**                   |
| EIS IC                      | AD5933                         | Digi-Key / Mouser             | ~$11/unit                   |
| EIS Eval Board              | EVAL-AD5933EBZ                 | analog.com / Digi-Key         | **~$67**                    |

---

## Key Purchasing Considerations

### Minimum Order Quantities

- **Digi-Key / Mouser:** MOQ = 1 for nearly all components listed above. Ideal for prototyping.
- **Crystal IS Optan:** Request-a-quote model via CDI; typically no minimum for samples.
- **Bolb Inc.:** Via Laser Components; contact for prototype quantities (5–25 units typical).
- **Hamamatsu:** shop.hamamatsu.com accepts single-unit orders with credit card.

### Lead Times (2024–2025)

- AS7343: **In stock** at Digi-Key and Mouser
- Seoul Viosys CUD7GF1B: **In stock** at RS Components
- Crystal IS Optan: **Some variants in stock** at CDI; 6–8 weeks for others
- Bolb S6060: **Order required** — 2–6 weeks typical
- Hamamatsu C12880MA: **In stock** at their own shop ($286)
- EVAL-AD5933EBZ: **In stock** at Digi-Key/Mouser

---

## Sources

| Source | Relevance |
|--------|-----------|
| Crystal IS Optan product page (cisuvc.com) | Primary source for 275 nm sensing LED specs |
| Bolb Inc. S6060 product page + where-to-buy page (bolb.co) | Distributor network confirmed |
| RS Components CUD7GF1B listing (rs-online.com) | Pricing and stock confirmed |
| Hamamatsu shop (shop.hamamatsu.com) | C12880MA and C13016 pricing direct from manufacturer |
| AMS-OSRAM AS7341 product page (ams-osram.com) | Eval kit confirmed |
| Nichia product pages (led-ld.nichia.co.jp) | NVSU233B, NCSU035D, NF2W757G-F1 specs |
| Ushio Epitex SWIR lineup (ushio.co.jp) | 1070 nm availability confirmed |
| Analog Devices EVAL-AD5933 page | Pricing and eval board confirmed |
| Seoul SunLike datasheet (Digi-Key media CDN) | CRI 97 specs confirmed |

## Gaps

1. **Exact 1070 nm part number from Ushio Epitex:** Website confirms 1070 nm is in the SWIR lineup, but no specific part number or datasheet link was found. Action: Contact Ushio directly (epitex@ushio.co.jp) or Marubeni Solutions for the exact part number and pricing for prototype quantities.
2. **Crystal IS Optan pricing:** CDI quotes required. No public per-unit pricing.
3. **455 nm LED selection:** ams OSRAM LD W5KM-1T4T-35 is noted but not deeply researched. Action: verify current availability and stock at Mouser/DigiKey before BOM finalization.
4. **EIS alternative to AD5933:** AD5941 (lower power, SPI) may be better for battery-powered pen device. Action: Compare AD5933 vs AD5941 datasheets for power budget and interface compatibility.

[leds]: leds.md "UV and Specific-Wavelength LEDs for Portable Spectrophotometry"
[sensors]: sensors.md "Spectral Sensors for Portable Spectrophotometry"
[nadh|NADH]: ../../biomarkers/papers/singleBiomarkers/sheets/fluorophores/nadh.md "NADH (Reduced Nicotinamide Adenine Dinucleotide)"
