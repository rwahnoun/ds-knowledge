# UV and Specific-Wavelength LEDs for Portable Spectrophotometry
**Application:** Pen-sized spectrophotometer for liquid analysis (urine biomarkers)  
**Date:** 2026-04-09  

---

## Table of Contents
1. [275 nm UV-C — Uric acid, protein absorption](#1-275-nm-uv-c)
2. [365 nm UV-A — NADH, riboflavin excitation](#2-365-nm-uv-a)
3. [405 nm Violet — Porphyrin Soret band, bilirubin](#3-405-nm-violet)
4. [455 nm Blue — Bilirubin, FAD](#4-455-nm-blue)
5. [Broadband White (High CRI) — Flat reference illuminant](#5-broadband-white-high-cri)
6. [~1070 nm NIR — IR matrix sensing](#6-1070-nm-nir)
7. [Multi-Wavelength LED Arrays / Modules](#7-multi-wavelength-led-arrays--modules)
8. [Sourcing Summary Table](#8-sourcing-summary-table)
9. [Design Notes & Caveats](#9-design-notes--caveats)
10. [Sources](#10-sources)

---

## 1. 275 nm UV-C

**Technology:** AlGaN (aluminium gallium nitride) or AlN. Deep UV-C. Requires SiC or sapphire substrate. Wall-plug efficiency typically 3–7% — these LEDs are power-hungry for what they output, and heat management is critical.

**⚠️ Safety:** UVC (100–280 nm) is highly damaging to skin and eyes. All UVC work requires UV-blocking eye protection, gloves, and enclosed optical paths. No bare-eye observation even briefly.

---

### 1.1 Seoul Viosys — CUD7GF1B (★ Top Pick for Exact 275 nm)

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

**Where to Buy:**
- DigiKey: `2112-CUD7GF1BCT-ND` — ~**$7.78** (1 pcs), in stock ~294 pcs
- RS Components: RS Stock No. 247-1977
- BeamQ: ~$6.90

**Datasheet:** [CUD7GF1B Datasheet v1.91](https://www.neumueller.com/datenblatt/seoulviosys/CUD7GF1B_210624_R1.91.pdf)  
**Notes:** Most straightforward SMD part at exactly 275 nm with reasonable power for spectrophotometry. Available through standard distributors. Ceramic SMD 3535 is reflow-solderable.

---

### 1.2 Bolb Inc. — S6060 (Highest Power)

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
| **Certifications** | RoHS, REACH, UL tested |

**Where to Buy:** Direct from Bolb or distributors (contact bolb.co). Not stocked by Mouser/DigiKey in standard quantities.  
**Price:** ~$15–25 (estimated, qty-dependent).

**Notes:** Highest power single-chip UVC LED available. The 6 × 6 mm footprint is manageable for a PCB but larger than the 3535 parts. For spectrophotometry, the 100 mW output is overkill—useful if you're pulsing at low duty cycle. Junction temp limit is only 75 °C, so thermal design is critical.

---

### 1.3 Bolb Inc. — S3535 (Mid Power, Smaller Package)

| Parameter | Value |
|-----------|-------|
| **Part Number** | S3535 |
| **Peak Wavelength** | ~275 nm |
| **Radiant Power** | 40 mW |
| **Package** | SMD 3535 (3.5 × 3.5 mm) |

**Where to Buy:** Ledrise (EU): ~**€13.57** (in stock >100 pcs)  
**Notes:** Good balance of power and package size. Same footprint as the Seoul Viosys CUD7GF1B.

---

### 1.4 Würth Elektronik — WL-SUMW Series

| Part No. | Power | Voltage | Package | Notes |
|----------|-------|---------|---------|-------|
| **15335327BA252** | **15 mW** | **6 V** | 3535 SMD | Recommended; catalog part at RS, Distrelec |
| **15335327BA250** | 3 mW | ~5.5 V | 3535 SMD | Low-power variant |

**Where to Buy:**  
- RS Components (UK/DE): RS# 228-0373 (BA252), 228-0372 (BA250)  
- Distrelec: 302-73-943 (BA252)  
**Price:** ~£4–8 (BA252 at RS)

**Notes:** Würth's WL-SUMW series is well-documented with full Würth datasheets and excellent application notes. Good choice for European sourcing. 120° beam angle, AlGaN technology.

---

### 1.5 Crystal IS / Asahi Kasei — Klaran Series

| Series | Peak λ | Power Options | Package |
|--------|--------|---------------|---------|
| **Klaran WD** | **260–270 nm** | >50, 60, 70, 80 mW @ 500 mA | SMD 3535 |
| **Klaran LA** | **260–270 nm** | Various bins | SMD 3535 |

**⚠️ Important Note:** Crystal IS Klaran products peak at **260–270 nm**, NOT 275 nm. Their AlN-based technology is optimized for germicidal UV (260–265 nm is the DNA absorption peak), not 275 nm. **Do not specify Klaran for a 275 nm application.**  
The Klaran `OP275-10P-SM` part exists (per Shengyu/global distributors) as a custom/catalog part at 275 nm with 10 mW, but availability is limited.

**Where to Buy (Klaran WD/LA):** CDI LED (cdi.com), per request; not standard Mouser/DigiKey catalog.

---

### 1.6 International Light Technologies — E275-3

| Parameter | Value |
|-----------|-------|
| **Part Number** | E275-3 |
| **Peak Wavelength** | 275 nm |
| **Radiant Power** | 3–6 mW |
| **Forward Voltage** | 5–7 V |
| **Package** | Ceramic SMD 3535 |

**Notes:** Lower power, suitable for low-intensity reference applications. Reflow soldering max 170–180 °C (unusually low — check datasheet carefully for PCB design). Available from International Light Technologies directly.

---

### 275 nm Summary Recommendation

| Priority | Part | Rationale |
|----------|------|-----------|
| **Best for PCB prototyping** | Seoul Viosys CUD7GF1B | Standard distributor (DigiKey), well-documented, exact 275 nm |
| **Best power** | Bolb S6060 | 100 mW, 7% WPE — use pulsed to manage heat |
| **European sourcing** | Würth 15335327BA252 | RS Components, 15 mW, catalog part |

---

## 2. 365 nm UV-A

**Technology:** InGaN or GaN. 365 nm is well-established, high-yielding technology. Many suppliers, good power levels. Used for NADH/NADPH fluorescence excitation (~340 nm abs, ~460 nm emission) and riboflavin excitation.

**Note:** 365 nm is at the very edge of the NADH absorption band (~340 nm). For optimal NADH excitation, 340 nm is ideal, but 365 nm is a practical compromise with far better LED availability and power. Riboflavin absorbs strongly at 370 nm and 450 nm — 365 nm is a good match.

---

### 2.1 Seoul Viosys — CUN66A1F (★ Recommended)

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

**Where to Buy:**  
- LEDs.de (EU): ~€8–12  
- BeamQ (CUN66A1G variant): ~$9.95  

**Notes:** Dome-top 3535 package. The Z5 series from Seoul Viosys is a high-efficiency UV-A family with multiple power bins. 420 mW from a 3535 package is excellent for fluorescence excitation. The dome increases coupling efficiency into optical fibers.

---

### 2.2 Nichia — NVSU233B-U365 / NVSU233C-D4 (High Power)

| Parameter | NVSU233B-U365 | NVSU233C-D4 (U365) |
|-----------|--------------|---------------------|
| **Peak Wavelength** | 365 nm | 365 nm |
| **Radiant Power** | **1450 mW @ 1000 mA** | (similar class) |
| **Forward Voltage** | 3.85 V @ 1000 mA | ~3.8 V |
| **FWHM** | **9.0 nm** (datasheet confirmed) | ~9–12 nm |
| **Max Current** | 1400 mA | 1400 mA |
| **Package** | SMD 3535 | SMD 3535 (3.5 × 3.5 × 2.73 mm) |
| **ESD Protection** | Built-in | HBM Class 3B |
| **Status** | Production | ★ Recommended model (2022+) |

**Where to Buy:**  
- Nichia directly or authorized distributors (Mouser, Digi-Key — search NVSU233B or NVSU233C)
- Enrgtech (UK): NVSU233A-U365 ~£15–20

**Datasheet (NVSU233B):** [Nichia PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233B(T)-E(4890F)U365x%20U385x%20U395x.pdf)  
**Notes:** Nichia 233-series is a workhorse UV-A platform with multiple wavelength bins (U365, U385, U395, U405). The 9 nm FWHM is unusually narrow for UV-A LEDs — good spectral purity. 1450 mW is far more than needed; use at reduced current (50–100 mA) for spectrophotometry to extend lifetime and reduce heating.

---

### 2.3 Nichia NVSU233A-U365

| Parameter | Value |
|-----------|-------|
| **Part Number** | NVSU233A-U365 |
| **Radiant Power** | 1030 mW @ 1000 mA |
| **Forward Voltage** | ~3.85 V |
| **Package** | SMD 3535 |

**Where to Buy:** Enrgtech (UK), Mouser — ~£15–20  

---

### 365 nm Summary Recommendation

| Use Case | Part |
|----------|------|
| Low-power fluorescence excitation | Seoul Viosys CUN66A1F (run at 50–100 mA, ~150–200 mW) |
| High-intensity application | Nichia NVSU233C-D4 at U365 (run at 100 mA, ~200 mW) |

---

## 3. 405 nm Violet

**Technology:** InGaN. This is the Blu-ray disc wavelength — extremely well-developed technology. High efficiency, very good power levels. Porphyrin Soret band centers ~410 nm (HbO2) and ~405 nm (for general porphyrins); 405 nm is also bilirubin's secondary absorption peak.

---

### 3.1 Nichia — NVSU233C-D4 (405 nm bin) (★ Recommended)

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
| **Reel Qty** | 800/reel |

**Datasheet:** [NVSU233C-D4 PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233C(T)-D4-E(6608B)U365x%20U385x%20U395x%20U405x.pdf)  
**Where to Buy:** Nichia distributors (Mouser, DigiKey, RS)  
**Notes:** The NVSU233C-D4 is a multi-bin part — specify U405 when ordering. The same physical LED can be ordered at 365, 385, 395, or 405 nm bins. Extremely high power for spectrophotometry — operate at 50–100 mA for sensing.

---

### 3.2 Nichia — NCSU035D (405 nm, larger package)

| Parameter | Value |
|-----------|-------|
| **Part Number** | NCSU035D |
| **Peak Wavelength** | 405 nm |
| **Package** | 6.8 × 6.8 × 1.9 mm (custom larger SMD) |
| **Reel Qty** | 500/reel |
| **Status** | In production (older model, not recommended for new designs) |

**Where to Buy:** Nichia direct  
**Notes:** Larger footprint than 3535. The NVSU233C-D4 is the newer recommended replacement.

---

### 3.3 ams OSRAM — OSLON SSL 80 LD CQ7P / LT CP7P

| Parameter | Value |
|-----------|-------|
| **Part Number** | LD CQ7P (violet 405 nm), LT CP7P (violet) |
| **Peak Wavelength** | 405 nm |
| **Package** | OSLON SMD ceramic (compact) |
| **Status** | **DISCONTINUED** |

**Notes:** The OSRAM OSLON violet family at 405 nm has been discontinued as of the ams-OSRAM reorganization. Do not design these into new products. Use Nichia or Seoul Viosys alternatives.

---

### 3.4 VSM (via BoselEC) — VS5252C45L6-405

| Parameter | Value |
|-----------|-------|
| **Peak Wavelength** | 405 ± 5 nm |
| **Radiant Power** | mid-power: 1285 mW; high-power: 4900 mW |
| **Package** | SMD |
| **Beam Angle** | 60° (mid) / 90° (high) |

**Where to Buy:** boselec.com/shop  
**Notes:** Primarily for UV curing/disinfection applications. Useful if very high power at 405 nm is needed.

---

### 405 nm Summary Recommendation

| Use Case | Part |
|----------|------|
| **New design** | Nichia NVSU233C-D4 (U405 bin) — best-in-class, available |
| **If OSRAM needed** | LA CP7P (LA = 405 nm bin) — check stock, may be discontinued |

---

## 4. 455 nm Blue

**Technology:** InGaN. Standard blue LED wavelength range. Very mature, high efficiency. Bilirubin absorbs at 454 nm (primary peak); FAD absorbs at 450 nm. 455 nm is an excellent match for both.

---

### 4.1 Lumileds — LUXEON Z LXZ1-PR01 (★ Recommended for compact PCB)

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
| **Bin** | PR (Royal Blue, ~450 nm) |

**Where to Buy:**  
- RS Components: RS# 923-1130 (MT), 768-2359 (MY)  
- Mouser, DigiKey (search LXZ1-PR01)  
- xonelec.com: ~**$1.44–3.44** (qty 1–24k)

**Notes:** The LUXEON Z is extremely compact for a pen-sized instrument. 0705 package is 1.7 × 1.3 mm — the smallest high-power LED footprint available from a tier-1 vendor. Note: peak is ~450 nm, not exactly 455 nm. For bilirubin sensing at 454 nm, this is effectively equivalent.

---

### 4.2 ams OSRAM — Golden Dragon Plus LD W5KM-1T4T (455 nm)

| Parameter | Value |
|-----------|-------|
| **Part Number** | LD W5KM-1T4T-35 |
| **Series** | Golden Dragon Plus |
| **Peak Wavelength** | **455 nm** (449–461 nm range) |
| **Radiant Power** | 493 mW @ 1 A (355–630 mW range) |
| **Forward Voltage** | 3.2 V |
| **Max Current** | 350 mA (rated), 1 A pulsed |
| **Beam Angle** | 170° (Lambertian) |
| **Package** | Gull-wing SMD (through-hole alternate exists) |

**Where to Buy:** Mouser, DigiKey, pneda.com  
**Notes:** This part hits exactly 455 nm. The Golden Dragon family is a well-proven OSRAM line. Gull-wing package is slightly more complex to solder than flat-land 3535, but standard reflow works.

---

### 4.3 ams OSRAM — Golden Dragon ARGUS LD W5SN-3T4U

| Parameter | Value |
|-----------|-------|
| **Part Number** | LD W5SN-3T4U-35-Z |
| **Peak Wavelength** | **455 nm** (449–461 nm) |
| **Radiant Power** | 365 mW @ 400 mA (280–450 mW range) |
| **Forward Voltage** | 3.2 V |
| **Max Current** | 350 mA |
| **Beam Angle** | 160° |
| **Package** | Gull-wing SMD, 9.40 mm Dia |

**Notes:** ARGUS variant is ruggedized for reliability applications.

---

### 4.4 Samsung — Blue LEDs at 455 nm

Samsung's LM series (LM301B, LM561C etc.) are primarily phosphor-white, but Samsung offers single-color blue at 450–455 nm. Search Samsung LED builder or Mouser for "Samsung 455nm". Pricing is competitive but bin selection may be limited for spectroscopy use.

---

### 455 nm Summary Recommendation

| Priority | Part | Notes |
|----------|------|-------|
| **Compact PCB (pen form factor)** | Lumileds LXZ1-PR01 | 1.7 × 1.3 mm, ~450 nm, ~$1.44 qty |
| **Exact 455 nm** | OSRAM LD W5KM-1T4T | 493 mW, 455 nm exact bin |
| **Budget** | Generic 455 nm SMD from JLCPCB library | e.g., OSRAM LZ4-00UBH0 (405–410 nm range — check bins) |

---

## 5. Broadband White (High CRI)

**Application:** Spectrally flat reference illuminant for broadband absorption measurements. For spectrophotometry, spectral flatness (flat SPD across 400–700 nm) matters more than lumens. High CRI (>95) correlates with broad, smooth spectral coverage.

**Key metric:** CRI is a proxy for spectral coverage. CRI 99 means the spectrum hits R1–R15 reference colors accurately, implying minimal dips across 400–700 nm. Standard blue-converted white LEDs have a strong dip in the blue-green (490–510 nm) region.

---

### 5.1 Nichia Optisolis — NFSW757G series (★ Top Pick)

| Parameter | Value |
|-----------|-------|
| **Series** | Optisolis™ |
| **Part Number (example)** | NFSW757G-V1 |
| **CRI (Ra)** | **98–99** (all 16 R-samples ≥ 90) |
| **R9** | ≥ 70 (saturated red — key indicator) |
| **Spectral Coverage** | 400–700 nm continuous, closest to D65/D50 illuminant |
| **Package** | **3030 SMD (3.0 × 3.0 mm)**, 757 platform |
| **CCT options** | 2700K, 3000K, 4000K, 5000K, 6500K |
| **Forward Voltage** | ~3.0–3.2 V (typical) |
| **UV emission** | **Essentially zero** (critically important for urine analysis — prevents matrix fluorescence excitation from the white source) |
| **Notes** | COB versions also available |

**Where to Buy:**  
- Nichia distributors (Mouser, DigiKey, Farnell, LEDrise EU)  
- LEDrise EU: ~**€0.80–1.50** per unit at low quantities

**Datasheet:** Available on nichia.co.jp under Optisolis product page.  
**Website:** [nichia.co.jp/en/product/lighting_optisolis.html](http://www.nichia.co.jp/led-ld/en/product/lighting_optisolis.html)

**Notes on spectral choice for spectrophotometry:**  
- Choose **4000K or 5000K** for flattest SPD across visible range  
- The Optisolis spectrum avoids the "blue spike" that contaminates measurements in the 440–460 nm region with standard white LEDs  
- No UV emission below ~400 nm prevents NADH/flavin autofluorescence from being excited by the white source itself

---

### 5.2 Seoul Semiconductor SunLike — TRI-R Technology

| Parameter | Value |
|-----------|-------|
| **Technology** | Violet LED die + Toshiba TRI-R phosphor |
| **CRI (Ra)** | 97 (typ), on the Blackbody Locus |
| **Package options** | 3535, COB (13.5 × 13.5 mm COB variant S4SM-1063) |
| **COB Part No.** | S4SM-1063xx9736-0B000G3S-00001 |
| **LES** | 9.8 mm (COB) |
| **MacAdam step** | 3-step binning |
| **Spectral advantage** | Uses **violet** pump die (not blue), so the spectrum truly spans from ~400 nm without the blue spike |

**Where to Buy:**  
- DigiKey carries Seoul Semiconductor / Seoul Viosys products  
- Mouser  
- Direct from Seoul Semiconductor distributors  
**Datasheet:** [DigiKey PDF](https://media.digikey.com/pdf/Data%20Sheets/Seoul%20Semiconductor/S4SM-1063xx9736-0B000G3S-00001.pdf)

**Notes:** SunLike uses a **violet pump die** (like Soraa) rather than the standard blue die. This means the spectrum is continuous from 400 nm (no suppressed output in the 400–430 nm region). Excellent for spectrophotometry applications where you care about full visible range coverage. CRI 97 is slightly below Optisolis CRI 99, but the violet-based spectrum is arguably better for optical purity.

---

### 5.3 Comparison: Optisolis vs SunLike

| Feature | Nichia Optisolis | Seoul SunLike |
|---------|-----------------|---------------|
| CRI | **99** | 97 |
| R9 (red saturation) | >70 | ~90+ |
| Pump die | Blue | **Violet** |
| 400–420 nm coverage | Minimal (blue die doesn't reach) | **Good** (violet die reaches) |
| UV bleed (<400 nm) | Essentially zero | Very low |
| Package options | 3030 SMD, COB | 3535 SMD, COB |
| Distributor availability | Excellent | Good |
| Price | ~€0.80–1.50 | Similar |

**For spectrophotometry:** SunLike's violet-based design gives better 400–420 nm coverage, which matters for porphyrin/bilirubin measurements. Optisolis has higher CRI score and better documentation. Either is far superior to standard white LEDs.

---

### 5.4 Yuji APS 3030 — Newest Full-Spectrum (★ Best for Broadest Coverage)

| Parameter | Value |
|-----------|-------|
| **Series** | APS (Advanced Performance Spectrum) |
| **Part Number** | P3220008.xx (xx = CCT code) |
| **CRI (Ra)** | **>97** (guaranteed minimum) |
| **TM-30** | Rf 98 / Rg 100 |
| **TLCI** | 99 |
| **Spectral Coverage** | **400–730 nm** continuous (40% broader than standard white LEDs) |
| **Package** | 3030 SMD (3.0 × 3.0 mm) |
| **Drive Current** | 100 mA rated |
| **Forward Voltage** | 8.6–9.2 V |
| **Luminous Flux (5000K)** | 89–99 lm @ 100 mA |
| **CCT options** | 2700K, 3200K, 4000K, 5000K, 5700K, 6500K |

**Where to Buy:** [yujiintl.com](https://www.yujiintl.com/aps-3030-0-9w/) — direct; also via MARL International (leds.co.uk)  
**Notes:** The APS series is Yuji's newest (2024+) full-spectrum LED, explicitly designed for photographic, broadcast, and measurement applications. The coverage extending to **730 nm** is unique — most white LEDs fall off sharply above 680 nm. The higher Vf (~9 V) suggests a multi-die or flip-chip architecture. CRI >97 minimum is the tightest guaranteed CRI of any 3030 SMD LED currently available.

---

### 5.5 Yuji BC 3030 G03 — Cost-Effective High CRI

| Parameter | Value |
|-----------|-------|
| **Series** | BC (Broad Coverage) |
| **Part Number** | P3170001.xx |
| **CRI (Ra)** | ≥95 (guaranteed), typ 97 |
| **TM-30** | Rf 92 / Rg 100 |
| **Technology** | 450 nm blue die + Yuji phosphor |
| **Package** | 3030 SMD |
| **Drive Current** | 300 mA rated |
| **Forward Voltage** | 3.0–3.4 V |
| **Luminous Flux (5000K)** | 91–101 lm @ 300 mA |
| **CCT options** | 2700K, 3200K, 4000K, 5000K, 5700K, 6500K |

**Where to Buy:** [yujiintl.com](https://www.yujiintl.com/bc-3030-0-9w/); MARL International ([leds.co.uk](https://www.leds.co.uk/components/enhanced-cri-r9-tech/smd/bc-3030/))  
**Notes:** Budget-friendly alternative using standard blue-pump architecture. TM-30 Rf of 92 (vs 98 for APS) indicates slightly less spectral fidelity, but still far superior to generic white LEDs. The 3.0–3.4 V forward voltage is more standard and easier to drive than the APS series.

---

### 5.6 Luminus SST-20-W — High Power Alternative

| Parameter | Value |
|-----------|-------|
| **Part Number** | SST-20-WxH |
| **CRI (Ra)** | >95 |
| **Technology** | Blue die + phosphor |
| **Package** | 3030 SMD |
| **Max Drive Current** | 3000 mA |
| **Forward Voltage** | ~3.0 V |
| **Luminous Flux** | up to 853 lm @ 3 A |
| **CCT options** | 2700K, 3000K, 3500K, 4000K |
| **Thermal Resistance** | 1.6 °C/W |

**Datasheet:** [luminus.com PDF](https://download.luminus.com/datasheets/Luminus_SST-20-WxH_Datasheet.pdf)  
**Notes:** Very high power density if needed. Standard blue-pump architecture, so the blue spike is present. Less suitable for spectrophotometry than SunLike or APS but useful if high radiant power is the priority.

---

### 5.7 Other High-CRI Options

| Brand | Product | CRI | Notes |
|-------|---------|-----|-------|
| Lumileds LUXEON | 5750 series | 90–97 | High lumen, available at Mouser/DigiKey |
| Cree XLamp | XHP70.3 HI | 90–95 | High efficacy, standard distributors |
| Samsung | LM301H EVO | 90–98 | Very competitive; 3030 package |

---

### 5.8 White LED Selection for Spectrophotometry — Comparative Analysis

**Key metrics for spectrophotometry (not general lighting):**

| Feature | Seoul SunLike | Nichia Optisolis | Yuji APS 3030 | Yuji BC 3030 |
|---------|--------------|-----------------|---------------|-------------|
| **CRI (Ra)** | ≥95, typ 97 | ≥95, typ **98–99** | **>97** (guaranteed) | ≥95, typ 97 |
| **TM-30 Rf/Rg** | — | — | **98/100** | 92/100 |
| **Pump die** | **Violet (~405 nm)** | Blue (~420 nm) | Proprietary | Blue (~450 nm) |
| **Blue spike at 450 nm** | **None** | Small (~420 nm bump) | Low | Yes |
| **UV leakage <400 nm** | Very low | **~Zero** (specified) | Low | Low |
| **Spectral coverage** | 400–700 nm | 400–700 nm | **400–730 nm** | 400–700 nm |
| **Package** | 3030 SMD | 3030 SMD | 3030 SMD | 3030 SMD |
| **Vf** | ~3.0 V | 2.9 V | **8.6–9.2 V** | 3.0–3.4 V |
| **Price (1 pc)** | **~$0.19–0.22** | ~€0.80–1.50 | Quote | Quote |
| **Distributors** | DigiKey, Future | Mouser, DigiKey | Yuji direct | Yuji direct |

**★ Recommendation for spectrophotometry:** Seoul SunLike 3030 is preferred because:

1. **Violet pump eliminates the 450 nm blue spike** — critical for bilirubin measurements (454 nm absorption)
2. Smoothest SPD across 420–700 nm of any production LED
3. Cheapest option
4. Available through standard distributors (DigiKey, Future Electronics, Neumüller)
5. Same 3030 footprint as Optisolis — drop-in compatible

**If UV suppression is paramount:** Nichia Optisolis — the only LED that explicitly specifies "UV emission essentially non-existent"

**If coverage beyond 700 nm matters:** Yuji APS 3030 — extends to 730 nm, but higher Vf and contact-for-pricing

**Note:** For spectrophotometry specifically, CRI >95 with a known, smooth SPD is more important than CRI alone. Consider measuring the actual SPD of your chosen LED with a spectrometer reference if you need quantitative analysis.

---

## 6. 1070 nm NIR

**Application:** IR matrix sensing — likely transillumination, diffuse reflectance, or index-of-refraction-based detection.

**Technology:** InGaAs (for 1000+ nm). Standard GaAs/AlGaAs only reaches to ~950 nm. For 1070 nm, InGaAs (InP substrate) is required. These are significantly more expensive than standard NIR LEDs and require different forward voltage (~1.2–1.5 V vs ~1.8 V for GaAs).

**Important note on 1070 nm:** At this wavelength, you are between the silicon detector cutoff (~1100 nm edge) and well within InGaAs territory. If using a silicon photodiode detector, note it has nearly zero response at 1070 nm — you'll need an **InGaAs photodetector**.

---

### 6.1 Ushio Epitex — SMT SWIR Series (★ Best SMD Option)

**Platform overview:** Ushio's Epitex brand produces the world-leading SWIR LEDs. Two main SMD families:

#### Epitex SMT Series (Standard Power, Compact)

| Parameter | Value |
|-----------|-------|
| **Wavelengths available** | 1050, 1100, 1150, 1200, 1300, 1450, 1550, 1650 nm |
| **Closest to 1070 nm** | **1050 nm bin** (1070 nm custom available) |
| **Output Power (1050 nm)** | ~1.1–30 mW per chip |
| **Package** | **SMD 3528** (3.5 × 2.7 mm) |
| **Chips per package** | 1–3 |
| **Package material** | Plastic |
| **Lens options** | Flat, S1, 22, 25, 27, 29 (various angles) |
| **Photodetector option** | PD chip can be integrated into same package |

**Custom wavelength:** Ushio offers custom SWIR wavelengths in **10 nm increments with ±10 nm tolerance** — you can specify exactly 1070 nm.

#### Epitex D Series (High Power, 5050)

| Parameter | Value |
|-----------|-------|
| **Wavelengths** | 1050–1650 nm |
| **Output Power** | Up to **750 mW per chip** |
| **Package** | **SMD 5050** (5 × 5.2 mm) |
| **Chips** | 1–3 |

**Where to Buy:**  
- [swir-led.com](https://swir-led.com) — Ushio/Epitex authorized  
- Ushio America: ushio.com  
- Custom orders through Ushio Epitex with sample availability

**Datasheet library:** [swir-led.com/datasheets](https://swir-led.com/datasheets/)

**Notes:** For pen-sized form factor, the SMT 3528 series is ideal. For exactly 1070 nm, contact Ushio for custom order — standard catalog has 1050 nm and 1100 nm bins. The 1050 nm bin may be adequate depending on the matrix property you're measuring (check water absorption bands and target analyte absorption spectrum).

---

### 6.2 Epigap OSA — EOLC-1070-25

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
| **Chip Size** | 350 µm |
| **Package** | TO-can / chip-level |

**Where to Buy:** [epigap-osa.com](https://www.epigap-osa.com/product/eolc-1070-25/) — direct  
**Applications:** Gas sensing, proximity sensing, spectroscopy  
**Notes:** Epigap-OSA (Germany) is a specialized SWIR/InGaAs emitter manufacturer. The EOLC-1070-25 is an exact 1070 nm part with reasonable power. The 18 ns switching time is excellent for pulsed/lock-in detection schemes. Package type for the standard part may require a carrier PCB — contact for SMD options.

---

### 6.3 Marktech Optoelectronics — SWIR Series

| Parameter | Value |
|-----------|-------|
| **Wavelength range** | **1020–1900 nm** |
| **Package types** | PLCC, SMD, TO-can, hermetic metal SMD |
| **1200 nm example** | MTSM1200MT2-BK |
| **Custom wavelengths** | Available to order |
| **Distributors** | DigiKey, Mouser |

**Where to Buy:** [marktechopto.com/led-emitters/swir-and-mwir-leds/](https://marktechopto.com/led-emitters/swir-and-mwir-leds/) → DigiKey/Mouser links  
**Notes:** Marktech's SWIR catalog spans 1020–4300 nm with InGaAs and InGaAsP technology. Their 1070 nm products exist but may require a quote. Marktech is strong on custom multi-chip assemblies combining multiple SWIR wavelengths with InGaAs detectors in one package — see Section 7.

---

### 6.4 Hamamatsu — SWIR LEDs

Hamamatsu is primarily known for detectors but does offer SWIR LED sources. Their L13072 series targets 1200 nm (not 1070 nm). For 1070 nm specifically, Hamamatsu would require a custom order. **Not the primary recommendation for 1070 nm SMD**.

---

### 1070 nm Summary Recommendation

| Priority | Part | Notes |
|----------|------|-------|
| **Exact 1070 nm SMD** | Ushio Epitex SMT (custom 1070 nm order) | Best SMD form factor, 3528 package |
| **Exact 1070 nm standard part** | Epigap OSA EOLC-1070-25 | 47 mW, exact λ, available direct |
| **Catalog SMD nearest 1070** | Ushio Epitex 1050 nm SMT | Standard catalog, 1050 nm closest bin |
| **With multi-λ integration** | Marktech SWIR custom | Can combine 1070 nm emitter + InGaAs PD in one package |

---

## 7. Multi-Wavelength LED Arrays / Modules

For a pen-sized spectrophotometer, integrating multiple emitters in a single package reduces PCB area and improves co-registration of optical paths.

---

### 7.1 Marktech Optoelectronics — Custom Multi-Chip Arrays (★ Best Option for Integration)

| Feature | Detail |
|---------|--------|
| **Technology** | Multiple LED dies in single TO-18, PLCC, TO-5, or SMD package |
| **Die count** | 2–7 dies per package |
| **Wavelength range** | UV through SWIR (235 nm – 4300 nm) |
| **Polarization** | Polarized or non-polarized configurations |
| **Custom wavelengths** | Yes — specify wavelengths at order time |
| **Detector integration** | InGaAs or silicon PD can be co-packaged (LED + detector in one) |
| **Applications** | Oximetry, co-oximetry, PPG, OCT, **urinalysis**, fNIRS, fluorescence |
| **MOQ** | Low-volume prototype quantities available; contact for quote |

**Where to Buy:** [marktechopto.com/led-emitters/multiwavelength/](https://marktechopto.com/led-emitters/multiwavelength/) — custom quote  
**Distributors:** DigiKey, Mouser (for catalog multi-chip parts)

**Notes:** Marktech **explicitly lists urinalysis** as an application. This is the most directly relevant vendor for this project's exact use case. A custom 4-die package with 365/405/455/White or 365/405/455/1070 nm would be feasible. For prototyping, their standard multi-chip catalog may have close enough combinations.

---

### 7.2 Ushio Epitex — Custom Multi-Wavelength Solutions

| Feature | Detail |
|---------|--------|
| **Approach** | Standard packages with 2+ wavelengths; semi-custom orders |
| **Wavelength range** | Full NIR and SWIR with custom options |
| **Photodiode option** | PD chips can be co-integrated |
| **Package types** | SMD 3528 (SMT), SMD 5050 (D-series) |
| **Customization** | Wavelength, lens, chip count per package |

**Contact:** ushio.co.jp/en/led/epitex/custom/multi_wavelength.html

---

### 7.3 ProPhotonix — COBRA NX MultiSpec Line Light

For a bench-top or larger system (not pen-sized), the ProPhotonix COBRA NX MultiSpec offers factory-integrated multispectral LED line illumination. Not relevant for pen-sized but worth noting for benchtop validation.

---

### 7.4 Practical Multi-Chip Approach for Pen Form Factor

Given the pen form factor constraint, a practical approach:

```
Option A: Single multi-chip die (Marktech custom)
  → 4-die SMD: 365 / 405 / 455 nm (or 455nm substitute ~450nm) + broadband
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

## 8. Sourcing Summary Table

| λ (nm) | Target Analyte | Manufacturer | Part Number | Power (typ) | Vf (V) | FWHM | Package | Price (1 pc) | Buy At |
|--------|---------------|-------------|-------------|-------------|--------|------|---------|-------------|--------|
| **275** | Uric acid, protein | Seoul Viosys | CUD7GF1B | 16 mW @ 100mA | 5.6 | **11 nm** ¹ | 3535 SMD | ~$7.78 | DigiKey |
| **275** | Uric acid | Bolb | S6060 | 100 mW @ 250mA | 6.5 | ~12 nm ² | 6060 SMD | ~€12.52 | LEDs.de / Laser Components |
| **275** | Uric acid | Bolb | S3535 | 40 mW | ~6.0 | ~12 nm ² | 3535 SMD | ~€13.57 | Ledrise EU |
| **275** | Uric acid | Würth Elektronik | 15335327BA252 | 15 mW | 6.0 | ~12 nm ² | 3535 SMD | ~£5–8 | RS Components |
| **275** | Spectroscopy | Crystal IS | OPTAN-275K-BL | 5 mW @ 100mA | — | ~10–12 nm | Ball lens | Quote | CDI (led.cdiweb.com) |
| **365** | NADH, riboflavin | Seoul Viosys | CUN66A1F | 420 mW @ 250mA | 3.6 | ~12 nm ² | 3535 Dome | ~€8–12 | LEDs.de |
| **365** | NADH, riboflavin | Nichia | NVSU233C-D4 (U365) | ~1450 mW @ 1A | 3.85 | **9.0 nm** ¹ | 3535 SMD | ~$15–20 | Mouser/DigiKey |
| **405** | Porphyrin, bilirubin | Nichia | NVSU233C-D4 (U405) | ~1600 mW @ 1A | 3.75 | ~12 nm ² | 3535 SMD | ~$15–20 | Mouser/DigiKey |
| **450** | Bilirubin, FAD | Lumileds | LXZ1-PR01 | 575 mW @ 500mA | 3.0 | ~20 nm ² | 0705/1713 | ~$1.44 | Mouser/RS |
| **455** | Bilirubin, FAD | OSRAM | LD W5KM-1T4T-35 | 493 mW @ 1A | 3.2 | ~20 nm ² | Gull-wing SMD | ~$2–5 | Mouser/DigiKey |
| **White** | Broadband ref. | Seoul Semi | **SunLike S1S0-3030** | 22 lm @ 65mA | ~3.0 | 400–700 nm ³ | 3030 SMD | ~$0.19–0.22 | DigiKey/Future | 
| **White** | Broadband ref. | Nichia | NF2W757G-F1 (Optisolis) | 23 lm @ 65mA | 2.9 | 400–700 nm ³ | 3030 SMD | ~€0.80–1.50 | Mouser/DigiKey |
| **White** | Broadband ref. | Yuji | APS 3030 (1W) | 89–99 lm @ 100mA | 8.6–9.2 | 400–730 nm ³ | 3030 SMD | Quote | yujiintl.com |
| **~1070** | IR matrix | Ushio Epitex | SMT 1050nm (custom 1070) | ~30 mW | ~1.25 | ~80 nm ² | SMD 3528 | Quote | swir-led.com |
| **1070** | IR matrix | Epigap OSA | EOLC-1070-25 | 47 mW @ 100mA | 1.3 | **38 nm** ¹ | TO-can/chip | Quote | epigap-osa.com |

¹ = confirmed from manufacturer datasheet  
² = estimated from technology class / typical values for that material system  
³ = broadband white LED — spectral coverage range, not single-peak FWHM

---

## 9. Design Notes & Caveats

### 9.1 Crystal IS Klaran — NOT 275 nm
Crystal IS Klaran WD and LA series peak at **260–270 nm**, not 275 nm. The 260–265 nm band is optimal for DNA disinfection, not for uric acid/protein spectrophotometry. Do not use Klaran for a 275 nm spectrophotometer. (A special Klaran `OP275` part at 275 nm exists but has limited availability.)

### 9.2 Power Levels vs. Spectrophotometry Needs
All high-power UV LEDs listed here (hundreds of mW) are far more than needed for absorbance spectrophotometry in a cuvette/tube. Plan to operate at 10–50 mA rather than rated max current. Benefits:
- Dramatically extended lifetime (UV LED lifetime is strongly current-dependent)
- Reduced heating (critical for 275 nm where Tj limit is only 75°C for Bolb)
- Reduced analyte photodegradation risk
- Better thermal stability → better wavelength stability

### 9.3 Heat Management for UV-C
Deep UV LEDs (275 nm) have low wall-plug efficiency (3–7%). At 100 mA / 5.6 V = 560 mW input, only ~16 mW is light; ~544 mW is heat. In a pen form factor, this is thermally challenging. Consider:
- Pulsed operation (1–10% duty cycle, synchronous with detector)
- Metal-core PCB (MCPCB) for the 275 nm LED
- Ceramic 3535 package (CUD7GF1B, Würth BA252) provides better thermal contact than plastic

### 9.4 Window / Lens Material at 275 nm
Standard LED lenses/encapsulants (silicone, epoxy) absorb UV-C. Only:
- **Quartz (fused silica)** — transparent to ~150 nm
- **Sapphire** — transparent to ~150 nm  
- **PTFE/Teflon** — diffuse but UV-transparent  

are UV-C transparent. All recommended 275 nm SMDs (CUD7GF1B, Würth, Bolb) use flat/bare ceramic windows or quartz windows. Do NOT add epoxy conformal coating or silicone encapsulant over these LEDs.

### 9.5 Photodetector Matching for 1070 nm
Silicon photodiodes have essentially **zero** response above ~1100 nm. For 1070 nm:
- **Use InGaAs photodetector** (Hamamatsu G12183, Marktech MTC1070C, or similar)
- Alternatively: short-wave InGaAs arrays (e.g., Hamamatsu G11194)
- Cost implication: InGaAs photodetectors are ~$20–100 each vs. <$1 for silicon

### 9.6 365 nm for NADH: Consider 340 nm
The primary NADH absorption peak is **340 nm** (ε = 6,220 M⁻¹cm⁻¹). At 365 nm, absorption is ~3–4× weaker. If NADH quantification (not just detection) is important, investigate whether a 340 nm LED can be sourced. Seoul Viosys offers UV-A LEDs closer to 340–350 nm, but power and availability drop significantly below 365 nm.

### 9.7 Optisolis UV Content
Nichia Optisolis explicitly states "UV emission essentially non-existent." For urine analysis where NADH autofluorescence and porphyrin emission could contaminate broadband measurements, this is a significant advantage over standard white LEDs (which often leak some UV).

### 9.8 OSRAM/ams Product Transitions
Several OSRAM violet/UV products (LD CQ7P, LA CP7P) have been discontinued following the ams-OSRAM merger. Verify product status before designing in any OSRAM LEDs in this wavelength range. The Golden Dragon Plus (LD W5KM) blue 455 nm products appear to remain active.

---

## 10. Sources

### Kept (primary references)
| Source | URL | Why Relevant |
|--------|-----|-------------|
| Seoul Viosys CUD7GF1B Datasheet | [neumueller.com/...CUD7GF1B...pdf](https://www.neumueller.com/datenblatt/seoulviosys/CUD7GF1B_210624_R1.91.pdf) | Primary spec sheet, exact 275 nm part |
| Bolb S6060 Product Page | [bolb.co/s6060-smd-275-nm/](https://bolb.co/s6060-smd-275-nm/) | Full specs, highest power UVC LED |
| Würth WL-SUMW at RS | [rs-online.com](https://de.rs-online.com/web/p/uv-leds/2280373) | 275 nm, catalog pricing |
| Nichia NVSU233B-U365 Datasheet | [nichia.co.jp API PDF](https://led-ld.nichia.co.jp/api/data/spec/led/NVSU233B(T)-E(4890F)U365x%20U385x%20U395x.pdf) | 365 nm Nichia spec |
| Nichia NVSU233C-D4 Product | [nichia.co.jp](https://www.nichia.co.jp/led-ld/en/product/led_product_data.html?kbn=1&type=NVSU233C-D4+%28405nm%29) | 405/365/385/395 nm recommended model |
| Lumileds LXZ1-PR01 at RS | [rsdelivers.com](https://mt.rsdelivers.com/product/lumileds/lxz1-pr01/lumileds3-v-blue-led-smd-luxeon-z-lxz1-pr01/9231130) | 455 nm pricing and specs |
| OSRAM 455 nm Golden Dragon at PNEDA | [pneda.com](https://www.pneda.com/osram-opto-semiconductors-inc/optoelectronics/led-lighting/led-lighting-color/page-7) | 455 nm OSRAM spec confirmation |
| Nichia Optisolis Product Page | [nichia.co.jp/en/product/lighting_optisolis.html](http://www.nichia.co.jp/led-ld/en/product/lighting_optisolis.html) | Optisolis CRI 98-99, spec details |
| Seoul SunLike Technology | [seoulviosys.com/en/technology/sunlike](https://www.seoulviosys.com/en/technology/sunlike) | SunLike CRI 97, violet-pump spectrum |
| Ushio Epitex SMT SWIR | [swir-led.com/smt-swir-leds/](https://swir-led.com/smt-swir-leds/) | 1050–1650 nm SMD, 3528 package |
| Epigap OSA EOLC-1070-25 | [epigap-osa.com/product/eolc-1070-25/](https://www.epigap-osa.com/product/eolc-1070-25/) | Exact 1070 nm, 47 mW, InGaAs |
| Marktech Multi-Wavelength Emitters | [marktechopto.com/led-emitters/multiwavelength/](http://oldmt.marktechopto.com/marktech-emitters/multi-wavelength-emitters/) | Multi-chip LED for urinalysis application |
| Crystal IS CDI LED page | [led.cdiweb.com/manufacturer/crystal-is](https://led.cdiweb.com/manufacturer/crystal-is) | Klaran 260–270 nm clarification |
| Marktech SWIR Mouser page | [nz.mouser.com/new/marktech-optoelectronics/marktech-swir-emitters/](https://nz.mouser.com/new/marktech-optoelectronics/marktech-swir-emitters/) | SWIR 1020–1900 nm catalog |
| Seoul Viosys CUN66A1F | [leds.de](https://www.leds.de/products/seoul-viosys-uv-a-smd-led-cun66a1f-365nm) | 365 nm, 420 mW, 3535 specs |

### Dropped
| Source | Reason |
|--------|--------|
| Lumistrips LED strips | Strip product, not discrete SMDs for PCB |
| BeamQ (CUN66A1G) | Reseller site, limited spec detail |
| JLCPCB 405 nm part | Wavelength listed as 405–410 nm, bin uncertainty |
| Samsung general blue | Insufficient 455 nm bin documentation found |
| Hamamatsu L13072 (1.2 µm) | Target is 1070 nm, Hamamatsu part is 1200 nm |

---

## Gaps & Next Steps

1. **275 nm: Nichia NCSU275(T)** — Found reference to Nichia spec doc (NCSU275) but couldn't confirm current production status or distributor pricing. Worth checking Nichia's current catalog.

2. **340 nm for NADH** — Not searched; if NADH is a primary target, a separate thread on 340 nm LEDs would be warranted. Seoul Viosys and Nichia both offer UV-A down to ~340 nm but at lower efficiencies.

3. **1070 nm exact pricing** — Epigap OSA and Ushio Epitex both require direct contact/quote for 1070 nm. Standard pricing not publicly available.

4. **Availability confirmation** — Several parts (OSRAM Golden Dragon LD W5KM) should be verified against current Mouser/DigiKey stock before BOM finalization.

5. **Optical bandwidth requirements** — For uric acid at 275 nm, protein at 280 nm, and bilirubin at 450–455 nm, the LED FWHM (~10–20 nm) is potentially too broad for specific quantitation without an optical bandpass filter. Thread B (filters and optics) should address this.

6. **Lumileds LXZ1-PR01 exact peak** — Dominant wavelength 447.5 nm vs 455 nm target: confirm bilirubin absorption curve to verify 447.5 nm is adequate, or source an exact 455 nm part.
