---
title: Datascience Overview — ds-learn
aliases:
  - DS Architecture
  - ds-learn Overview
  - Jimini Data Model
tags:
  - topic/architecture
  - type/architecture
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Datascience Overview — ds-learn

Overview of the ML models and training repository, data model, and processing pipeline for Jimini urine analysis. See [[api-architecture]] for the API and deployment, [[database]] for the ETL pipeline, and [[device]] for Jimini hardware and SLC naming conventions.

---

## Project Description

We are developing a device named Jimini allowing to measure urine biomarker concentrations in urine. This device has several sensors and LEDs. With it, we can scan a urine, water or air sample, and get a series of spectra, recorded using LED-sensor couples. We also have an EIS sensor, providing a complex output.

In the context of the `ds-learn` repository, we extract sensors from a dataset of records to obtain a pandas DataFrame where each row is a record and each column is a wavelength for optical signals, and frequency for the EIS signal.

> [!NOTE]
> Urines have different concentrations, color, and turbidity. Jimini devices may differ from each other — their spectra from the same sample can be different. This inter-device variability is a key challenge for [[calibration-transfer]] and robust model training.

---

## Data Model Structure

### Dataset

A Dataset is a container that holds collections of data records along with their associated metadata. Two main types:

| Type | Description |
|---|---|
| **DatasetRecords** | Contains an array of individual records (sensor readings) plus metadata about each record |
| **DatasetDF** | Contains feature data in DataFrame format alongside metadata |

Key characteristics:
- Each dataset has a collection of records and associated metadata
- Records can be selected, sorted, and filtered based on meta fields
- Datasets maintain consistency between the data, metadata, and biomarker information
- The structure allows for easy extraction of features from raw sensor measurements

File references:
- [Dataset class definitions](file:///D:/code/datascience/src/ds/dataio/dataset.py#L11-L325)
- [DatasetRecords implementation](file:///D:/code/datascience/src/ds/dataio/dataset.py#L98-L200)
- [DatasetDF implementation](file:///D:/code/datascience/src/ds/dataio/dataset.py#L223-L314)

### Record

A Record represents an individual measurement instance that contains:
- Sensor components (Spectrum, EISpectrum, etc.) stored in a dictionary format
- Metadata about the recording process including device info, sample details, and timing
- Biomarker information associated with this specific record
- The ability to process all contained sensor components

Key characteristics:
- Each record is an instance of the `Record` class from `ds.dataio.record`
- Contains multiple sensor components (Spectrum, EISpectrum, etc.)
- Has metadata describing the conditions under which data was collected
- Can be processed in-place or as a copy to clean/transform the contained data

File references:
- [Record base class](file:///D:/code/datascience/src/ds/dataio/record.py#L13-L86)

### Component

A Component represents individual sensor measurement types:

| Component | Description |
|---|---|
| **Spectrum** | Optical spectral measurements with wavelength and intensity values |
| **EISpectrum** | Electrochemical impedance spectroscopy data |
| **IRMatrix** | Infrared matrix data for absorbance measurements |
| **SquareWaveVoltamogram** | Voltamometric measurements (SWV) |
| **Spectrum3d** | 3D spectral data |

Key characteristics:
- Each component is a specialized class that inherits from the base Component class
- Contains structured data in pandas DataFrames with proper column/row naming conventions
- Has processing methods to clean and normalize raw sensor data
- Can be visualized using built-in plotting functions
- Supports operations like normalization, resampling, and data transformation

File references:
- [Component base classes](file:///D:/code/datascience/src/ds/dataio/component.py#L18-L200)
- [Spectrum component](file:///D:/code/datascience/src/ds/dataio/component.py#L64-L101)
- [EISpectrum component](file:///D:/code/datascience/src/ds/dataio/component.py#L173-L200)
- [IRMatrix component](file:///D:/code/datascience/src/ds/dataio/component.py#L103-L132)
- [SquareWaveVoltamogram component](file:///D:/code/datascience/src/ds/dataio/component.py#L202-L312)

---

## Transformers

Transformers process and extract features from the raw sensor data in Records and Datasets. They implement scikit-learn's `TransformerMixin` interface for compatibility with sklearn pipelines.

### ExtractComponent

The `ExtractComponent` transformer extracts and processes signal components from records or datasets. It operates on different types of signals (Spectrum, IRMatrix, EISpectrum) by applying specific transformations:

| Signal type | Transformations applied |
|---|---|
| **Spectrum** | Baseline removal, resampling, de-minimization, normalization based on integration time |
| **IRMatrix** | Normalization for zero and integration time |
| **EISpectrum** | Processes complex impedance data with rounding and clipping |

Key characteristics:
- Extracts components using a specified component identifier (cmp)
- Can use reference components for processing comparisons
- Supports different signal types with appropriate processing functions
- Returns processed data as pandas DataFrames suitable for ML modeling

File references:
- [ExtractComponent implementation](file:///D:/code/datascience/src/ds/process/transformers.py#L97-L188)
- [Component processing functions](file:///D:/code/datascience/src/ds/process/component.py#L7-L44)

### Other Transformers

| Transformer | Description |
|---|---|
| **DatasetExtractFeatures** | Extracts features from dataset records at stimulation peaks |
| **ScatterCorrection** | Applies [[signal-processing]] scatter correction methods (SNV, RNV) |
| **SavitzkyGolay** | Applies Savitzky-Golay smoothing filter with derivatives |
| **Scaler** | Scales data between specified ranges using various methods |
| **BaselineCorrection** | Removes baseline effects from spectral data |
| **Derive** | Computes numerical derivatives of spectral signals |
| **Trim** | Trims spectral data to a specified wavelength range |

File references:
- [Transformers module](file:///D:/code/datascience/src/ds/process/transformers.py#L36-L696)

---

## Summary

A Dataset contains multiple Records, each Record holds multiple Components (sensor measurements), and these components represent the actual measured data from different types of sensors on the Jimini device.

---

## Sources

| Source | Notes |
|---|---|
| [[api-architecture]] | Algorithm versioning, API endpoints, deployment |
| [[database]] | ETL pipeline and PostgreSQL schema |
| [[device]] | SLC naming conventions, sensor ranges |
| `datascience/src/ds/dataio/` | Dataset, Record, Component class implementations |
| `datascience/src/ds/process/transformers.py` | All transformer implementations |

## Gaps

1. The `Spectrum3d` and `SquareWaveVoltamogram` component types are listed but not described in detail — document their data structure and use cases.
2. No description of how the `knowledge` repository ontology maps raw SLC names to normalized component identifiers in the ETL step.
3. `DatasetExtractFeatures` and `ExtractComponent` distinction not fully explained — clarify when each is used in the training pipeline.

[api-architecture]: api-architecture.md "Datascience Architecture & API"
[database]: database.md "Datascience ETL and Database (PostgreSQL)"
[device]: device.md "Jimini Device Description"
[calibration-transfer]: ../datascience/calibration-transfer.md "Calibration Transfer & Device Harmonization for Portable Spectrometers"
[signal-processing]: ../biomarkers/signal-processing.md "Signal Processing & Matrix Correction for Jimini Urine Spectroscopy"
