---
title: Jimini Device
aliases:
  - jimini
  - Jimini
  - jiminiDevice
  - SLC
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Jimini Device

The Jimini device is developed by Usense. It is a pen-like probe that can be dipped into a liquid sample (urine, water, or air). Via a companion app, it drives onboard emitters and reads signals from multiple sensors. The goal is to measure urine biomarker concentrations non-invasively. See [[datascience/spectroscopy-biomarkers]] for the optical measurement context.

## Sensors

| Sensor | Type | Range |
|--------|------|-------|
| C12 | Photodetector | 321–870 nm |
| C14 | Photodetector | 570–1078 nm |
| EIS | Electrochemical impedance | frequency domain (complex Z) |
| IRM | IR matrix | discrete IR wavelengths |
| SWV | Square wave voltamogram | current vs. voltage sweep |

## Emitters

| Emitter | Description | Geometry |
|---------|-------------|----------|
| `275`, `365`, `405`, `455` | UV/VIS LEDs (wavelength in nm) | opposite side from sensor |
| `VIS` | Broadband visible | opposite side from sensor |
| `VISD` | Broadband visible | same side as sensor |
| `R405` | 405 nm | same side as sensor |

Drive current (amplitude) is set in mA (e.g. `100.0mA`, `50.0mA`, `2.5mA`).

## Signals (SLCs)

SLCs (Sensor-LED Combinations) identify each acquired signal by its sensor, emitter, and drive amplitude.

**Naming convention:** `{sensor}-{emitter}-{amplitude}`

Examples: `C12-275-100.0mA`, `C14-VIS-50.0mA`

### SLC Suffixes

| Suffix | Meaning |
|--------|---------|
| `-hdrl` | High dynamic range — long integration exposure |
| `-hdrs` | High dynamic range — short integration exposure |
| `-ADS` | Analog-to-digital scaling applied |

> [!NOTE]
> HDR acquisitions (long + short) are merged during processing to extend the effective dynamic range of optical signals.

### Special SLCs

| SLC | Description |
|-----|-------------|
| `C12-off` / `C14-off` | Dark/reference (emitter off) |
| `EIS` | Electrochemical impedance spectrum |
| `IRM-{wavelength}-{amplitude}` | IR matrix (e.g. `IRM-1070-100.0mA`) |

### Signal Content by Type

| Signal | Index | Values |
|--------|-------|--------|
| Optical (C12, C14) | wavelength (nm) | intensity array |
| EIS | frequency (Hz) | complex impedance (real + imaginary) |
| IRM | 2D matrix | IR absorbance values |
| SWV | voltage (V) | current sweep |

## Sample Characteristics

Urine samples vary in color, turbidity, and analyte concentration — all of which affect optical signals. Water and air are used as blanks or controls. See [[turbidity]] for turbidity correction approaches.

> [!IMPORTANT]
> Device-to-device variability: individual Jimini units are not perfectly identical. The same sample scanned on two devices will yield slightly different spectra. ML models trained across devices must account for this via [[calibration-transfer]] or device-aware features.

## Data Model (Code)

Measurements are represented as structured Python objects in the `datascience` (`ds`) library:

| Class | Role |
|-------|------|
| `Record` | One acquisition session; contains sensor components + metadata (device MAC, sample ID, firmware) |
| `Component` | A single sensor signal within a record |
| `Spectrum` | Optical component (C12/C14) |
| `EISpectrum` | Electrochemical impedance component |
| `IRMatrix` | IR matrix component |
| `SquareWaveVoltamogram` | SWV component |
| `Spectrum3d` | 3D excitation-emission matrix |
| `DatasetRecords` | Ordered collection of Records with aligned metadata and biomarkers |
| `DatasetDF` | Flattened DataFrame (rows = records, columns = wavelengths/frequencies) |

**Files:**
- [`ds.dataio.record`](file:///D:/code/datascience/src/ds/dataio/record.py)
- [`ds.dataio.component`](file:///D:/code/datascience/src/ds/dataio/component.py)
- [`ds.dataio.dataset`](file:///D:/code/datascience/src/ds/dataio/dataset.py)

## Sources

| Source | Notes |
|--------|-------|
| Internal Usense hardware documentation | Sensor and emitter specifications |
| `d:\code\datascience\src\ds\dataio\` | Data model implementation |

## Gaps

- Exact frequency range for EIS sensor not specified here
- SWV voltage sweep range and step not documented
- HDR merge algorithm (long + short exposure combination) not described
- No documented calibration procedure for cross-device normalization of optical signals
