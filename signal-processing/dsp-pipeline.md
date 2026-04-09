# **UV-Vis Urine Biomarker Extraction Pipeline**
Pipeline steps 


### **Dark Current Subtraction**
**Label**: `dark_correction`  
**Purpose**: Remove electronic noise and thermal effects
**Algorithm Options**:
- **Dark spectrum subtraction**: `I_corrected = I_raw - I_dark`
- **Per-pixel dark current correction** (for array detectors)
- **Temperature-compensated dark correction**

### **Reference/Blank Correction**
**Label**: `reference_correction`  
**Purpose**: Convert photon counts to transmittance
**Algorithm Options**:
- **Single-beam correction**: `T = (I_sample - I_dark) / (I_reference - I_dark)`
- **Double-beam correction** 
- **Stray light correction**

### **Absorbance Calculation**
**Label**: `absorbance_conversion`  
**Purpose**: Apply Beer-Lambert law transformation
**Formula**: `A = -log10(T) = -log10(I_sample/I_reference)`
**Algorithm Options**:
- reference to blank (same matrix without the compound)
- approximation using water
- approximation using white level

### **: Quality Control**
**Label**: `quality_control`  
**Purpose**: Remove corrupted measurements and outliers  
**Algorithm Options**:
- **Negative absorbance filtering** (indicates measurement issues)
- **Saturation detection** (photon counts at detector limits)
- **SNR thresholds**
- **Cosmic ray removal**
- **Outlier detection (isolation forest, Z-score)**
- **Bad pixel correction**
- **Spectral quality metrics (SNR thresholds)**

### **Baseline Correction**
**Label**: `baseline_correction`  
**Purpose**: Remove instrument drift and systematic backgrounds
**Algorithm Options**:
- **ArPLS** (Asymmetrically Reweighted Penalized Least Squares)
- **AirPLS** (Adaptive Iteratively Reweighted Penalized Least Squares)
- **RubberBand** (convex hull baseline)
- **Polynomial fitting** (1st-3rd order)
- **Whittaker smoothing**

### **Scatter Correction** 
**Label**: `scatter_correction`  
**Purpose**: Remove physical light scattering effects from urine particles
**Algorithm Options**:
- **MSC** (Multiplicative Scatter Correction)
- **EMSC** (Extended MSC) - best for multi-device[4]
- **SNV** (Standard Normal Variate)
- **De-trending** (remove wavelength-dependent scatter)

### **Spectral Derivatives**
**Label**: `derivative`  
**Purpose**: Remove overlapping backgrounds and enhance resolution
**Algorithm Options**:
- **First derivative** (Savitzky-Golay)
- **Second derivative** (removes linear baselines)
- **Continuous Wavelet Transform**

### **Smoothing/Filtering**
**Label**: `smoothing`  
**Purpose**: Reduce random noise while preserving peaks
**Algorithm Options**:
- **Savitzky-Golay** (5-17 window, 2-3 polynomial order)
- **Gaussian filtering**
- **Moving average**
- **Median filter**
- **Whittaker smoothing**

### **Orthogonal Signal Correction**
**Label**: `osc`  
**Purpose**: Remove biological/matrix variation orthogonal to biomarker[6]
**Algorithm Options**:
- **OSC** (Orthogonal Signal Correction)
- **OPLS** (Orthogonal PLS) - modern version
- **DSC** (Direct Orthogonalization)

### **Normalization/Scaling**
**Label**: `scaling`  
**Purpose**: Standardize intensities across samples/devices[7][2]
**Algorithm Options**:
- **StandardScaler** (zero mean, unit variance)
- **MinMaxScaler** (0-1 range)
- **RobustScaler** (median-based, outlier resistant)
- **Unit vector normalization**
- **Total Ion Current (TIC)** normalization

### **Feature Selection**
**Label**: `feature_selection`  
**Purpose**: Select wavelengths relevant to biomarker[8][7]
**Algorithm Options**:
- **SelectKBest** (univariate statistical tests)
- **Recursive Feature Elimination**
- **LASSO regularization**
- **Correlation-based** (remove redundant wavelengths)
- **Variable Importance in Projection (VIP)**

### **Model Training**
**Label**: `regressor`  
**Purpose**: Learn biomarker concentration from processed spectra  
**Algorithm Options**:
- **PLS Regression** (chemometrics standard)
- **Random Forest Regressor**
- **Support Vector Regression**
- **Ridge/LASSO Regression**
- **Neural Networks**

## **Why This Order is Critical**

### **Dark Current First**[1][2]
- **Must be first** because all subsequent calculations depend on accurate photon counts
- Electronic noise affects all wavelengths uniformly
- Temperature-dependent, so same conditions required for dark and sample

### **Reference Correction Before Absorbance**[3]
- **Beer-Lambert law requires transmittance calculation first**: `T = I_sample/I_reference`[4][6]
- Reference spectrum accounts for:
  - Light source intensity variations across wavelengths
  - Optical component transmission losses
  - Detector sensitivity variations

### **Absorbance Conversion**[5][7]
- **Must follow transmittance calculation**: `A = -log10(T)`
- Converts multiplicative effects (scattering) to additive effects
- Linearizes concentration relationship per Beer-Lambert law


### **Physical Processing First (Steps 1-3)**
**Baseline must come before scatter correction** because:[1]
- Baseline correction removes additive effects (instrumental drift)
- Scatter correction handles multiplicative effects (sample matrix)
- Wrong order can introduce artifacts

### **Chemical Enhancement (Steps 4-5)**
**Derivatives after scatter correction** because:[2][5]
- Scatter correction stabilizes the signal foundation
- Derivatives amplify noise, so clean signal is essential
- Smoothing after derivatives prevents noise amplification

### **Biological Correction (Step 6)**
**OSC after physical preprocessing** because:[1]
- Requires clean spectra to identify orthogonal variation correctly
- Physical artifacts would confound biological signal separation
- Must precede final scaling to maintain interpretability

### **Statistical Processing Last**
**Final scaling and modeling** because:[9][7]
- All spectral artifacts removed before standardization
- Feature selection on clean, processed spectra is more reliable
- Model training on properly preprocessed data prevents overfitting



def create_photon_count_biomarker_pipeline(reference_spectrum=None, dark_spectrum=None):
    """
    Complete pipeline from photon counts to biomarker concentration
    """
    return Pipeline([
        # Stage 0: Convert photon counts to absorbance
        ('dark_correction', DarkCurrentCorrection(dark_spectrum=dark_spectrum)),
        ('reference_correction', ReferenceCorrection(reference_spectrum=reference_spectrum)),
        ('absorbance_conversion', AbsorbanceConversion()),
        ('quality_control', PhotonCountQualityControl()),
        
        # Stage 1: Physical preprocessing (same as before)
        ('baseline_correction', ArPls(lam=1e5)),
        ('scatter_correction', ExtendedMultiplicativeScatterCorrection()),
        ('derivative', SecondDerivative()),
        ('smoothing', SavitzkyGolay(window_length=11, polyorder=2)),
        
        # Stage 2: Biological correction
        ('osc', OrthogonalSignalCorrection(n_components=2)),
        
        # Stage 3: Final processing
        ('scaling', StandardScaler()),
        ('feature_selection', SelectKBest(f_regression, k=100)),
        ('regressor', PLSRegression(n_components=5))
    ], memory='./cache')



# EXAMPLE

# Create pipeline with 3 steps
pipeline = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("pca", PCA()),
        ("regressor", RandomForestRegressor(random_state=42)),
    ]
)

# Parameter grid allowing bypass with 'passthrough'
# Option A: Direct replacement (simpler)

param_grid = {
    "scaler": [StandardScaler(), "passthrough"],
    "pca": [PCA(n_components=5), PCA(n_components=10), "passthrough"],
    "regressor__n_estimators": [50, 100],
}

# Option B: Parameter tuning (more flexible)
param_grid = {
    "scaler": [StandardScaler(), "passthrough"],
    "pca": [PCA(), "passthrough"],
    "pca__n_components": [5, 10, 15],  # Only applies when pca != 'passthrough'
    "regressor__n_estimators": [50, 100],
}


# Grid search
grid_search = GridSearchCV(
    pipeline, param_grid, cv=3, scoring="neg_mean_squared_error", n_jobs=-1
)

# Fit
grid_search.fit(X_train, y_train)
