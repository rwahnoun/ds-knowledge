---
title: ds-learn — Project Description & Data Model
aliases:
  - ds-learn project
  - data model
  - Dataset Record Component
tags:
  - topic/ml
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# ds-learn — Project Description

Documentation for the `ds-learn` ML models and training repo (`d:\code\ds-learn`).

Usense is developing [[jiminiDevice|Jimini]], a pen-like probe that measures urine biomarker concentrations. The device has multiple sensors and LEDs. It can scan urine, water, or air samples and produces a series of spectra (one per LED-sensor pair) plus an EIS signal.

In the `ds-learn` context, sensor data from a dataset of records is extracted into a pandas DataFrame where each row is a record and each column is a wavelength (optical) or frequency (EIS). Models are then trained on this tabular representation.

> [!IMPORTANT]
> Urines vary in concentration, color, and turbidity — all of which affect optical signals. Individual Jimini units also differ from one another; spectra from the same sample on two devices can diverge. ML models must account for both sources of variability. See [[calibration-transfer]].

## Data Model

The `datascience` library (`ds`) provides a three-level hierarchy for raw measurements.

### Dataset

A Dataset is a container for collections of records plus aligned metadata.

| Type | Description |
|------|-------------|
| `DatasetRecords` | Array of `Record` objects + metadata DataFrame |
| `DatasetDF` | Flattened feature DataFrame (rows = records, columns = wavelengths/frequencies) + metadata |

Key behaviors:
- Records can be selected, sorted, and filtered on metadata fields
- The structure maintains consistency between data, metadata, and biomarker labels
- `DatasetRecords` is the starting point; `DatasetDF` is produced after feature extraction

**File:** [`ds.dataio.dataset`](file:///D:/code/datascience/src/ds/dataio/dataset.py)

### Record

A Record represents one acquisition session.

| Field | Description |
|-------|-------------|
| Components | Dict of named sensor components (`Spectrum`, `EISpectrum`, etc.) |
| Metadata | Device MAC address, sample ID, firmware version, timing |
| Biomarkers | Ground-truth analyte concentrations for this record |

**File:** [`ds.dataio.record`](file:///D:/code/datascience/src/ds/dataio/record.py)

### Component

A Component is a single sensor signal within a Record.

| Subtype | Sensor | Data shape |
|---------|--------|------------|
| `Spectrum` | Optical (C12, C14) | wavelength → intensity |
| `EISpectrum` | Electrochemical impedance | frequency → complex Z |
| `IRMatrix` | IR matrix | 2D IR absorbance |
| `SquareWaveVoltamogram` | SWV | voltage → current |
| `Spectrum3d` | 3D EEM | excitation × emission → intensity |

All component subtypes:
- Inherit from a base `Component` class
- Store data as pandas DataFrames with proper index/column naming
- Have processing methods for normalization, resampling, and transformation
- Support built-in visualization

**File:** [`ds.dataio.component`](file:///D:/code/datascience/src/ds/dataio/component.py)

## Transformers

Transformers implement `sklearn.TransformerMixin` and operate on Records/Datasets to extract tabular features. See [[transformers]] for the full reference.

### ExtractComponent

Extracts and processes a named signal component from records or datasets.

| Signal type | Processing applied |
|-------------|-------------------|
| `Spectrum` | Baseline removal, resampling, normalization by integration time |
| `IRMatrix` | Normalization for zero and integration time |
| `EISpectrum` | Impedance rounding and clipping |

- `cmp`: component identifier string
- `cmpRef`: optional reference component for differential processing
- Returns processed data as pandas DataFrame

**File:** [`ds.process.transformers — ExtractComponent`](file:///D:/code/datascience/src/ds/process/transformers.py)

### Other Key Transformers

| Transformer | Purpose |
|-------------|---------|
| `DatasetExtractFeatures` | Extract features at stimulation peaks across all components |
| `ScatterCorrection` | SNV, RNV, MSC, EMSC scatter correction |
| `SavitzkyGolay` | Smoothing + optional derivative |
| `Scaler` | Local min-max scaling to wavelength regions |
| `BaselineCorrection` | Rubberband, arPLS baseline removal |
| `Derive` | Numerical derivative via `np.gradient` |
| `Trim` | Clip to wavelength range |

## Summary

```
Dataset (DatasetRecords)
  └── Record[]
        └── Component{} (Spectrum, EISpectrum, IRMatrix, SWV, Spectrum3d)
                ↓  (via ExtractComponent / DatasetExtractFeatures)
Dataset (DatasetDF)
  └── DataFrame (rows = records, columns = wavelengths or frequencies)
                ↓  (via sklearn pipeline)
              Model
```

## Sources

| Source | Notes |
|--------|-------|
| `d:\code\datascience\src\ds\dataio\` | Dataset, Record, Component implementations |
| `d:\code\datascience\src\ds\process\transformers.py` | Transformer implementations |

## Gaps

- `Spectrum3d` (3D EEM) component is listed but not documented in detail
- `SquareWaveVoltamogram` processing pipeline is not described
- No documented strategy for handling failed component extraction in a batch pipeline
