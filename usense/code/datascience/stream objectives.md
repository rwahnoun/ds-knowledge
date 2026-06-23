# Datascience vision and scope
The datascience stream is involved in several steps of the development of the Jimini medical device.
1. Literature reviews
	- Understanding the optical and electrical signals, methods for preprocessing, processing and modeling towards biomarker estimation.
	- Scientific grounding of the biomarker estimation methods.
2. Device development support
	- Defining hardware specifications to obtain signals maximizing information on the target biomarkers.
	- Assessment of the signal quality, inter device variability, and conformity to specifications using notebooks and reports.
3. Data normalization and storage
	- creating and maintaining a normalized database of signals, metadata and biomarkers.
4. Algorithm development
	- Real time tracking of scientific studies, automatic estimation during internal trials.
	- Development of biomarker estimation algorithms from Jimini signals
5. Production
	- creating and managing biomarker estimation endpoints in production
	- validation of devices post production, assessing conformity to product specifications.
6. Tracking the performance of the deployed devices and algorithms.

# Datascience SDK
For this purpose, we developed a Software Development Kit (SDK) with:
- loaders for the different Jimini, gold standard devices and gold standard lab results  file formats.
- normalisation of any any source to a common internal format.
- sub repositories:
	- process spectral data and electroimpedance data
	- normalize samples and devices
	- statistical methods for continuous, categorical and binary variables.
	- wrapped models to estimate the relationship between data and biomarkers
These modules are used to create notebooks to, evaluate different devices, train algorithms, and gain information for device development and production tracking.

# Data
The data science team handles two main types of data:
- **Device records** contain signals and associated data. These records can originate from Jiminis, spectrophotometers, and other external or research devices. All records are normalized through loaders into a universal format in the class `Records`. An ontology is used to resolve data heterogeneity.
- **Biomarkers** originate from columnar automatic exports from our partners, or CSV files written by our technicians. Similarly, they are normalized into a common format.
An ETL pipeline integrates and processes records and biomarkers to feed a mongo (records) and a SQL (biomarkers) database.
To maximize the security of PHI, the data-science database contains the minimum necessary amount of information to estimate the biomarker concentration.

## ETL
Regarding the data pipelines, USense has several sources of information for Jimini data:
- An **indexing database**: maintains an index of the records from the devices.
- A **record blob storage**: stores raw records as JSON files in blob storage.
- A **biomarkers blob storage**: contains exports from our partners.
- **Google Sheets**: used to save information not present in the other databases for specific experiments, validations, etc.
- **Individual folders**: for records acquired with the HW-SDK.

These are the unique sources of persistent information and require careful handling. However, they contain raw, unprocessed data and are not directly queryable for batch processing. Additionally, the raw data has several formats, is not normalized, and lacks a common unique key between the biomarkers and the collected data.
The DS ETL: 
Processes biomarkers and data to create a common unique key for each record in the format `<organization><sampleId><year>`, avoiding conflicts among and within organizations.
- Normalizes the data, creating names for the SLCs, cleaning sample IDs, and reformatting SLCs to the v1 data model.
- Preprocesses the SLCs for faster access and resamples them to common wavelengths.
- Normalizes the biomarkers, cleaning values for numeric and categorical biomarkers.
- Stores the processed information into DS-DB, a PostgreSQL database.

The database contains three tables:

| Table          | Contents                                                      |
| -------------- | ------------------------------------------------------------- |
| **Records**    | Metadata for each record                                      |
| **Sensors**    | Sensor metadata, raw data, and processed data for all records |
| **Biomarkers** | Exported and cleaned biomarker values                         |
We can then use it to query records from a given study, filtering by device, date or the presence of a gold standard biomarker value.

## Available data 

# Biomarker Estimation
The Jimini device developed by Usense is a pen-like probe that can be dipped into a liquid sample (urine, water, or air). Via a companion app, it drives onboard emitters and reads signals from multiple sensors. The goal is to measure urine biomarker concentrations non-invasively.  From an algorithm development point of view, this converts to predicting a continuous, categorical, or binary concentration of a biomarker present in the urine from a matrix of electric and optic signals.

## Overall strategy
#### Explainability and simplicity
The strategy is to reach the simplest model that solves the problem. In the case of optical estimation of biomarker, we start from naive and science rooted methods, for example following the Beer Lambert law. We then try signal processing and normalisation techniques to circumvent sample and device variability. For the model, we start by using machine learning techniques (PCA for feature selection), Logistic Regression (model). If necessary, we switch to deep learning methods, when enough data is available. 
#### Science-backed algorithms
as mentioned earlier, algorithm development starts with understanding the expected impact of the target biomarker on the signals. In coordination with the science team, literature reviews drive the development of the device as well as the algorithms to target optical wavelengths in order to maximize biomarker responses. Algorithm development will first target expected signal changes. 
#### Determinism
All developed algorithms are deterministic, i.e. for a given input signal, the algorithm output will be the same. The hardware is designed to minimize variability between devices, and the datascience code contains several functions to reduce as much as possible inter and intra devices variations on the same sample.
#### Input validation
Algorithms are designed to accept specific input data. The models are wrapped to reject input signals when its requirements are not met.
This includes low signal level, metadata issues (wrong sample type), wrong hardware or firmware version, electroimpedance errors (when the device is not recording in urine, or with a low liquid level)
When algorithmic requirements are not met for a specific model, error codes are returned to the backend and mobile application. 
#### Tracability
Algorithm input and outputs are stored in our backend. We normally do not have gold standard biomarker levels when the device is in production, we therefore can not 

## Algorithm development
- Data are selected from the DS database for a given biomarker, and stored into a compact and reproductible format.
- The dataset is split into a training and testing dataset, ensuring that the same sample is not in the train and test dataset.
- We then implement descriptive overviews to better understand the problem, signals and distribution of biomarkers. This step helps choosing the development strategy for the models.
- Algorithms are trained, hyperparameter optimized and logged using a dedicated experiment tracking service (mlflow).  We then perform threshold optimization techniques to fit as much as possible to the product specifications.
- Once one or several candidate algorithms are in place. we run reports indicating the performance of the algorithms in prediction the biomarker concentration, and the potential confounders (i.e. other biomarkers that could increase the model error)
- The algorithm then undergoes the validation stage in collaboration with the science team.

## Compute service and ML-OPS
The data-science algorithms are exposed using **Azure Functions**. This allows controlled access as well as scalability. 
The Azure Functions can be called from a local computer, or from the cloud service after authentication. Examples of exposed functions include biomarker estimation from one or more Jimini records, or quality estimation of a given record.
The platform can be directly deployed from VS-Code, after validation of the related unit tests and QTPs. The platform is first deployed into a staging environment, then into a production environment once approved by the cloud team's integration tests.
A standardized **API** allows to call one or several biomarker estimation algorithms, providing the record(s) and requested analyses. The service responds in a format adapted from the FHIR standard.
The service is hosted by the Usense's cloud stream and inherits its firewall and security settings.
As of today,  a single endpoint for each biomarker is deployed, however, with this architecture, the system can easily evolve to add redundancy, and scale to any number of devices.

<STOP HERE>
------


# Vision Data Science
Expliquer précisément quel problème le développement d'algorithmes sur le Jimini résout, pour qui (patient, médecin, hôpital et payeur) et quel gain mesurable il apporte (diagnostic plus précoce etc.).
=> PRODUCT

# Taille et qualité des datasets
Présenter les datasets de données disponibles (nb échantillons/patients, campagnes de collecte...), leur représentativité et les éléments qui garantissent leur qualité (homme/femme, diversité, qualité des signaux, données longitudinales...).
Dataset Lisa / Dataset spectro / Dataset Jimini

# ~~Pipeline de données~~
~~Décrire comment les données sont collectées, transmises, stockées, transformées, en garantissant traçabilité, sécurité et conformité réglementaire.~~

# ~~Stratégie de validation~~
~~Expliquer comment les mesures de référence (gold standard) sont obtenues et intégrées.~~

# ~~Architecture ML~~
~~Présenter la stratégie, les types de modèles utilisés, les données d'entrée, les principales variables de suivi et les raisons qui justifient les choix technologiques effectués.~~

# Résultats de performance


# Montrer les métriques clés

# ~~Validation clinique~~
~~Création de dataset de validation analytiques~~
~~=> SCIENCE~~ 


# Monitoring et MLOps
Décrire les mécanismes permettant de surveiller la qualité des données et des modèles en production, détecter les dérives et assurer des mises à jour contrôlées.

Conformité réglementaire IAExpliquer comment les développements algorithmiques s'intègrent dans le système qualité, dans l'IA act et les règles de bonnes pratiques