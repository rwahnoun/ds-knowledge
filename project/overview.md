# ds-learn — docs

Documentation for the `ds-learn` ML models and training repo.

## Project description
- we are developping a device named jimini allowing to measure urine biomarker concentrations in urine.
- this device has several sensors and leds.
- with it, we can scan a urine, water or air sample, and get a series of spectra, recorded using a couple led-sensor.
- we also have an EIS sensor, providing a complex output.

In the context of the ds-learn repository, we extract sensors from a dataset of records, to obtain a pandas dataframe where each row is a record and each column is a wavelength for optical signals, and frequency for the EIS signal.

Notes:
- urines have different concentrations, color, turbidity.
- jimini may differ from each other, their spectra in the same sample can be different.

## Data Model Structure

### Dataset
A Dataset is a container that holds collections of data records along with their associated metadata. In this system, there are two main types:
1. **DatasetRecords** - Contains an array of individual records (like sensor readings) plus metadata about each record
2. **DatasetDF** - Contains feature data in DataFrame format alongside metadata

Key characteristics:
- Each dataset has a collection of records and associated metadata
- Records can be selected, sorted, and filtered based on meta fields
- Datasets maintain consistency between the data, metadata, and biomarker information
- The structure allows for easy extraction of features from raw sensor measurements

**File references:**
- [Dataset class definitions](file:///D:/code/datascience/src/ds/dataio/dataset.py#L11-L325)
- [DatasetRecords implementation](file:///D:/code/datascience/src/ds/dataio/dataset.py#L98-L200)
- [DatasetDF implementation](file:///D:/code/datascience/src/ds/dataio/dataset.py#L223-L314)

### Record
A Record represents an individual measurement instance that contains:
- Sensor components (like spectra, EIS data, etc.) stored in a dictionary format
- Metadata about the recording process including device info, sample details, and timing
- Biomarker information associated with this specific record
- The ability to process all contained sensor components

Key characteristics:
- Each record is an instance of the Record class from `ds.dataio.record`
- Contains multiple sensor components (Spectrum, EISpectrum, etc.)
- Has metadata describing the conditions under which data was collected
- Can be processed in-place or as a copy to clean/transform the contained data

**File references:**
- [Record base class](file:///D:/code/datascience/src/ds/dataio/record.py#L13-L86)

### Component
A Component represents individual sensor measurement types:
1. **Spectrum** - Optical spectral measurements with wavelength and intensity values
2. **EISpectrum** - Electrochemical impedance spectroscopy data
3. **IRMatrix** - Infrared matrix data for absorbance measurements
4. **SquareVaveVoltamogram** - Voltamometric measurements (SWV)
5. **Spectrum3d** - 3D spectral data

Key characteristics:
- Each component is a specialized class that inherits from the base Component class
- Contains structured data in pandas DataFrames with proper column/row naming conventions
- Has processing methods to clean and normalize raw sensor data
- Can be visualized using built-in plotting functions
- Supports operations like normalization, resampling, and data transformation

**File references:**
- [Component base classes](file:///D:/code/datascience/src/ds/dataio/component.py#L18-L200)
- [Spectrum component](file:///D:/code/datascience/src/ds/dataio/component.py#L64-L101)
- [EISpectrum component](file:///D:/code/datascience/src/ds/dataio/component.py#L173-L200)
- [IRMatrix component](file:///D:/code/datascience/src/ds/dataio/component.py#L103-L132)
- [SquareVaveVoltamogram component](file:///D:/code/datascience/src/ds/dataio/component.py#L202-L312)

## Transformers

Transformers are used to process and extract features from the raw sensor data in Records and Datasets. They implement scikit-learn's TransformerMixin interface for compatibility with sklearn pipelines.

### ExtractComponent
The `ExtractComponent` transformer extracts and processes signal components from records or datasets. It operates on different types of signals (Spectrum, IRMatrix, EISpectrum) by applying specific transformations like:

- **Spectrum**: Applies baseline removal, resampling, de-minimization, and normalization based on integration time
- **IRMatrix**: Applies normalization for zero and integration time
- **EISpectrum**: Processes complex impedance data with rounding and clipping

Key characteristics:
- Extracts components using a specified component identifier (cmp)
- Can use reference components for processing comparisons
- Supports different signal types with appropriate processing functions
- Returns processed data as pandas DataFrames suitable for ML modeling

**File references:**
- [ExtractComponent implementation](file:///D:/code/datascience/src/ds/process/transformers.py#L97-L188)
- [Component processing functions](file:///D:/code/datascience/src/ds/process/component.py#L7-L44)

### Other Transformers
Additional transformers include:

- **DatasetExtractFeatures**: Extracts features from dataset records at stimulation peaks
- **ScatterCorrection**: Applies scatter correction methods (SNV, RNV)
- **SavitzkyGolay**: Applies Savitzky-Golay smoothing filter with derivatives
- **Scaler**: Scales data between specified ranges using various methods
- **BaselineCorrection**: Removes baseline effects from spectral data
- **Derive**: Computes numerical derivatives of spectral signals
- **Trim**: Trims spectral data to a specified wavelength range

**File references:**
- [Transformers module](file:///D:/code/datascience/src/ds/process/transformers.py#L36-L696)

In summary: A Dataset contains multiple Records, each Record holds multiple Components (sensor measurements), and these components represent the actual measured data from different types of sensors on the Jimini device.
