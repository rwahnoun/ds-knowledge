# Data Science Vision and Scope

The Jimini device generates complex optical and electrical signals that require rigorous data science to turn raw measurements into clinically meaningful biomarker estimates. The Data Science team underpins every stage of this process — from hardware specification to production deployment — ensuring that algorithms are scientifically grounded, reproducible, and ready for regulatory scrutiny.

The Data Science team is involved in the following steps of the development of the Jimini medical device:

1. Literature reviews
	- Understanding optical and electrical signals, and the methods for preprocessing, processing, and modeling towards biomarker estimation.
	- Scientific grounding of biomarker estimation methods.
2. Device development support
	- Defining hardware specifications to obtain signals that maximize information on target biomarkers.
	- Assessment of signal quality, inter-device variability, and conformity to specifications.
3. Data normalization and storage
	- Creating and maintaining a normalized database of signals, metadata, and biomarkers.
4. Algorithm development
	- Real-time tracking of scientific studies and automatic estimation during internal trials.
	- Development of biomarker estimation algorithms from Jimini signals.
5. Production
	- Creating and managing biomarker estimation endpoints in production.
	- Validation of devices post-production, assessing conformity to product specifications.
6. Post-market performance tracking
	- Continuous monitoring of deployed device and algorithm performance to detect drift and ensure sustained accuracy in the field.

# Data Science SDK

To support these activities, we developed a proprietary Software Development Kit (SDK) that standardizes data from all device types and formats into a single unified pipeline, enabling consistent algorithm development, reproducible experiments, and reliable quality assessment across all studies and production deployments.

# Data

The Data Science team handles two main types of data:

- **Device records** contain signals and associated data. These records can originate from Jiminis, spectrophotometers, and other external or research devices. All records are normalized through loaders into a universal format, with an ontology used to resolve data heterogeneity across sources.
- **Biomarkers** originate from automatic exports from our partners or from values recorded by our technicians. They are normalized into a common format for consistent processing.

An ETL (Extract, Transform, Load) pipeline integrates and processes records and biomarkers into a unified database.

To maximize the security of Protected Health Information (PHI), the Data Science database contains the minimum necessary amount of information required to estimate biomarker concentrations.
<The data minimization principle — collecting only the minimum necessary PHI — aligns with Article 10 of the EU AI Act, which mandates that training data for high-risk AI systems respect data protection and privacy requirements.>

## ETL

USense integrates data from multiple heterogeneous sources — device records, lab biomarker exports, and experiment-specific files — into a single, normalized, and queryable database. A custom ETL pipeline processes and harmonizes all incoming data, assigns unique identifiers to each record to avoid conflicts across organizations and studies, and stores the result in a structured PostgreSQL database. This ensures full consistency, traceability, and reproducibility across all algorithm development and production workflows.

The database contains three tables:

| Table          | Contents                                                      |
| -------------- | ------------------------------------------------------------- |
| **Records**    | Metadata for each record                                      |
| **Sensors**    | Sensor metadata, raw data, and processed data for all records |
| **Biomarkers** | Exported and cleaned biomarker values                         |

This structure allows querying records from a given study, filtering by device, date, or the presence of a gold-standard biomarker value.

# Biomarker Estimation

The Jimini device developed by USense is a pen-like probe that can be dipped into a liquid sample (urine, water, or air). Via a companion app, it drives onboard emitters and reads signals from multiple sensors. The goal is to measure urine biomarker concentrations non-invasively — enabling point-of-care diagnostics that could replace or complement laboratory testing, reducing time-to-result and improving access to care. From an algorithm development standpoint, this translates to predicting a continuous, categorical, or binary concentration of a biomarker from a matrix of electrical and optical signals.

## Overall Strategy

#### Explainability and Simplicity

The strategy is to reach the simplest model that solves the problem. For optical biomarker estimation, we start from naive, science-rooted methods — for example, following the Beer-Lambert law — and progressively apply signal processing and normalization techniques to address sample and device variability. For modeling, we begin with interpretable machine learning techniques (PCA for feature selection, Logistic Regression for classification). Deep learning methods are only adopted when simpler approaches are insufficient and enough data is available. This preference for simplicity means our models are more auditable, easier to validate with regulators, and faster to iterate on.
<This "simplest model first" philosophy directly supports the EU AI Act's requirement (Article 13) that high-risk AI systems be sufficiently transparent for users and notified bodies to understand and verify their outputs.>

#### Science-Backed Algorithms

Algorithm development starts with understanding the expected impact of the target biomarker on the signals. In coordination with the science team, literature reviews drive device development as well as algorithm design — targeting specific optical wavelengths to maximize biomarker response. This scientific grounding strengthens the defensibility of our IP and supports faster regulatory approval by aligning algorithmic choices with established biochemical mechanisms.

#### Determinism

All developed algorithms are deterministic: for a given input signal, the algorithm will always produce the same output. The hardware is designed to minimize variability between devices, and the Data Science codebase contains dedicated functions to reduce inter- and intra-device signal variation on the same sample. This reproducibility is essential for regulatory submissions and clinical validation.
<Deterministic algorithms satisfy the EU AI Act's requirement (Article 9) for risk management and consistent, predictable behavior in high-risk AI systems — a key criterion for CE marking and clinical validation.>

#### Input Validation

Algorithms are designed to accept only specific, well-defined input data. The models actively reject input signals that do not meet their requirements — including low signal levels, metadata issues (wrong sample type), incompatible hardware or firmware versions, and electroimpedance errors (e.g., the device not recording in urine, or insufficient liquid level). When requirements are not met, error codes are returned to the backend and mobile application rather than producing an unreliable result.
<This input validation mechanism aligns with the EU AI Act's Article 9 requirements for risk management: the system actively detects out-of-scope conditions and refuses to operate rather than producing potentially harmful outputs.>

#### Traceability

Algorithm inputs and outputs are stored in our backend for every production call. Since gold-standard biomarker values are not routinely available in production settings, direct accuracy monitoring is not always possible; instead, we track signal quality metrics, output distributions, and error rates to detect drift and flag anomalies. This traceability infrastructure enables post-market surveillance and supports regulatory audit requirements.
<Full traceability of algorithm inputs and outputs supports compliance with the EU AI Act's Article 12, which requires high-risk AI systems to automatically log events throughout their lifecycle to enable post-market monitoring and auditability.>

## Algorithm Development

- Data are selected from the Data Science database for a given biomarker and stored in a compact, reproducible format.
- The dataset is split into training and testing sets, ensuring that no sample appears in both.
- Descriptive overviews are implemented to better understand the problem, the signals, and the distribution of biomarkers — informing the development strategy.
- Algorithms are trained, hyperparameter-optimized, and logged using a dedicated experiment tracking service (MLflow). Threshold optimization techniques are applied to align performance with product specifications.
- Once candidate algorithms are identified, reports are generated indicating prediction performance and potential confounders (i.e., other biomarkers that could increase model error).
- The algorithm then undergoes a validation stage in collaboration with the science team.

## Compute Service and ML-OPS

The Data Science algorithms are exposed using **Azure Functions**, enabling controlled access and horizontal scalability. The Azure Functions can be called from a local computer or from the cloud service after authentication. Examples of exposed functions include biomarker estimation from one or more Jimini records and quality estimation of a given record.

The platform is deployed directly from VS Code, following successful unit tests and Qualification Test Protocols (QTPs). Deployment follows a controlled two-stage process: first into a staging environment, then into production after approval by cloud team integration tests — ensuring that no unvalidated changes reach clinical users.
<This staged deployment process supports the EU AI Act's Articles 9 and 17 requirements for quality management systems governing AI system updates and post-deployment control.>

A standardized **API** allows calling one or several biomarker estimation algorithms, providing the record(s) and requested analyses. The service responds in a format adapted from the Fast Healthcare Interoperability Resources (FHIR) standard, ensuring interoperability with clinical information systems.

The service is hosted by USense's cloud infrastructure and inherits its firewall and security settings. The current architecture supports a single endpoint per biomarker, with built-in capacity to add redundancy and scale to any number of devices.

Our architecture was designed from the ground up to meet the requirements of high-risk AI systems under the EU AI Act and the In Vitro Diagnostic Regulation (IVDR) — combining deterministic algorithms, input validation, full traceability, staged deployment, and PHI minimization into a cohesive, audit-ready system.

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