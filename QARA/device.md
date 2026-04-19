---
title: Jimini Device Description
aliases:
  - Jimini Device
  - Jimini Hardware
tags:
  - topic/hardware
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# Jimini Device Description

The Jimini device is developed by Usense Healthcare. It consists of a pen-like device that can be plunged into a liquid sample (air, water, urine). With its companion app, we can generate signals from sensors or emitter-sensor couples. See [[optical-path-design]] for optical system details and [[overview]] (leds-and-sensors) for component specifications.

---

## Overview

| Property | Value |
|---|---|
| **Form factor** | Pen-like; plunged into liquid sample |
| **Sample types** | Air, water, urine |
| **Signal types** | Optical spectra (LED-sensor pairs), EIS |
| **Interface** | Companion app |

---

## Signal Naming Convention (SLC)

**SLC naming:** `{sensor}-{emitter}-{amplitude}`

### Emitters

| Identifier | Description |
|---|---|
| `275`, `365`, `405`, `455` | LED wavelength in nm |
| `VIS` | Broadband visible LED (opposite side to sensor) |
| `VISD` | Broadband visible LED (same side as sensor) |
| `R405` | 405 nm LED (same side as sensor) |
| `100.0mA`, `50.0mA`, `2.5mA` | Drive current suffix (amplitude) |
| `-hdrl` / `-hdrs` | High dynamic range long/short exposure suffix |
| `-ADS` | Analog-to-digital scaling suffix |

**Special SLCs:**

| SLC | Description |
|---|---|
| `C12-off` | Dark measurement (no emitter active) |
| `C14-off` | Dark measurement for C14 sensor |
| `EIS` | Electrochemical impedance spectroscopy |
| `IRM-{wavelength}-{amplitude}` | IR matrix, e.g., `IRM-1070-100.0mA` |

> [!NOTE]
> All sensors are on the **opposite side** of the emitter except VISD and R405, which are on the **same side** as the sensor.

### Sensors

| Sensor | Sensing Range | Notes |
|---|---|---|
| **C12** | 321–870 nm | UV-Vis; grating spectrometer (Hamamatsu C12880MA family) |
| **C14** | 570–1078 nm | Vis-NIR; grating spectrometer (Hamamatsu C14384MA family) |
| **EIS** | Electrochemical impedance | Complex output (real + imaginary) across frequency sweep |
| **IRM** | IR matrix (~1070 nm) | Multi-pixel matrix of IR sensors |

---

## Data Model

Records from Jimini devices are loaded as `Record` objects in the `ds` package. Each record contains:

- **Components** (`Spectrum`, `EISpectrum`, `IRMatrix`, etc.) keyed by SLC name
- **Metadata** (device MAC address, sample ID, organization, firmware version, timestamp)
- **Biomarker information** (if associated with a reference measurement)

SLC column names in the processed dataframe follow the format `{sensor}-{emitter}-{amplitude}`, e.g., `C12-275-100.0mA`, `C14-VIS-50.0mA`, `EIS`, `C12-off`.

---

## Sources

| Source | Notes |
|---|---|
| [[optical-path-design]] | Physical optical system design and LED/sensor specs |
| [[overview]] (leds-and-sensors) | LED and sensor selection tables |
| [[database]] | ETL pipeline and data storage |

## Gaps

1. Exact firmware version history and SLC naming changes across hardware generations not documented here — refer to the `knowledge` repository ontology for normalization mappings.
2. IRM sensor pixel layout and spatial correspondence to the 1070 nm IR matrix not specified — needs hardware documentation update.
