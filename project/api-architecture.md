# Datascience
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Datascience](#datascience)
- [Code](#code)
  - [Repositories](#repositories)
  - [Validation and testing.](#validation-and-testing)
- [Data](#data)
- [Computing platform](#computing-platform)
  - [Application programming interface](#application-programming-interface)
  - [General API](#general-api)
    - [API call](#api-call)
    - [Response](#response)
    - [Items structure](#items-structure)
    - [Errors structure](#errors-structure)
- [example installation with py312](#example-installation-with-py312)
- [Deployment](#deployment)
- [Algorithms Design documentation](#algorithms-design-documentation)
  - [Release notes](#release-notes)
  - [Versioning](#versioning)
  - [Code dependencies and safety](#code-dependencies-and-safety)
  - [Biomarker specific design](#biomarker-specific-design)
  - [Acute porphyria](#acute-porphyria)
    - [Total Urinary Porphyrin](#total-urinary-porphyrin)
    - [Porphobilinogen](#porphobilinogen)

<!-- /code_chunk_output -->


# Code
## Repositories
The data science code, consisting mainly of python classes, scripts and notebooks is hosted under the company github account and is split into several repositories, including:
- **datascience**, <https://github.com/usense-projects/datascience>: containing code for data loaders,ETL, pipelines, signal processing, models, quality test protocols, and statistical tests.
- **ds-compute**, <https://github.com/usense-projects/ds-compute>: containing the code for the computing platform.
- **ds-scripts**, <https://github.com/usense-projects/ds-scripts>: analysis scripts and python notebooks.
- **knowledge**, <https://github.com/usense-projects/knowledge>: production information on the company devices.

## Validation and testing.
As of today, several test suites are used to ensure performance and non regressions.
- **unit tests** cover the code exposed by the API. These include normal and corner cases testing the validity of API calls, ability to obtain and read jimini records, as well as normal and abnormal responses. The same tests are performed locally before deploying the algorithms, and remotely in the staging environment to validate the deployment.
- **qtpAlgorithm** are executed at the end of the devbelopment of a new algorithm. They calculate a series of standard machine learnng metrics on one or more dataset to evaluate an algorithm performance.
- **qtpAnaliticPerformance** correspond to a post hoc test on a dataset unseen by the algorithm, to assess its generalisation performance and estimate additional indices such as the limit of detection, interaction from other compounds etc.


# Data
The data science team handles two main types of data.
- **Device records** contain signals and associated data. These records can originate from jiminis, spectrophotometers and other external or research devices. To facilitate downstream analyses, all records are normalized through loader under an universal format in the class Records. The different sources and jimini versions lead to a wide variety of formats and nomenclature, so an ontology is used to resolve the data heterogeneity.
- **Biomarkers** originate from columnar automatic exports from our partners, or csv files written by our technicians. Similarly to records, they are normalized into a common format. Since the different partners have different nomenclatures, an ontology defined in the knowledge repository facilitates the normalization.

As the original data is not directly practical for analyses, an ETL pipeline integrates, and processes records and biomarkers to feed a mongo (records) and a SQL (biomarkers) database. This way, one can easily query records as well as associated meta into datasets. Those datasets can then be used for processing, algorithm training etc. and saved for later use. The ETL also contains functions to keep datasets up to date.

# Computing platform
The datascience algorithms are exposed using azure functions (Azure Functions Overview | Microsoft Learn). This allows controlled access as well as scalability.
The azure functions can be called from a local computer, or the cloud service after authentication. Examples of exposed functions include biomarker estimation from one or more jimini records, or quality estimation of a given record.
the computing platform can be directly deployed from vs-code, after validation of the related unit tests and QTPs. To allow for independant testing, the platform is first deployed into a staging environment, then into a production environment once approved by the cloud team's integration tests.

## Application programming interface
The application programming interface (API) allows external programs to interact with the exposed code. It can be used directly from the code to locally run a algorithm (ds.api) or remotely via the azure function.
The API can be easily deployed using vs-code and azure extensions by right clicking on the ds-compute repository and selecting "deploy to function app".

## General API
To facilitate calls and the addition of new algoritms, the API exposes all algorithms on a single endpoint.

### API call
The input consists of a dictionary containing the following fields:
- **analysisType (strList|str)** correspond to the algorithms to run.
    examples: 'tup','pbg','redBloodCells','leukocytes','*' (run everything possible), combinations ie ['tup','pbg'] are accepted

- **records (dict)** contains the records to analyse. it should contain raw (dict) for all algorithms and raw and heated for pbg
    record can follow several formats:
    - if url is provided, it will directly read the url:\
    ```<SRC> = {"url":<signed url>}```
    - if blob and container are provided, it will get the data from Azure Blob Storage:\
    ```<SRC> = {"blob":<blob>,"storageAccount":<"usense"|"research">}```\
    - if a raw json is provided, it will interpret it as a stringed jimini dictionary:\
    ```<SRC> = {"raw":<raw jimini record>}```

### Response
The output, common to every algorithm, resembles a simplified FHIR observation and contains four fields:
- **request (dict)** contains the input information
- **items (list)** contains the items resulting of the analysis
- **status (str)** is 'pass' if we managed to handle the request, and 'fail' if we failed
- **errors (list)** contains global error messages upon failure.

### Items structure
Each item (dict) corresponds to a given analysis, they can contain:
- **author (str)**: algorithm name
- **version (str)**: algorithm version
- **trainingDate (str)**: algorithm training date
- **name (str)**: biomarker name
- **unit (str)**: biomarker unit
- **cat (str,optional)**: result as a categorical string
- **cnt (float|int,optional)**: result as a continuous value
- **cntRng (str,optional)**: result as a continuous value within a range
- **status (str)** 'pass'|'fail' for this specific algorithm
- **errors (list)** list of messages in case of error

### Errors structure
The full list of possible error messages is available in the exceptions.py file in the datascience repository.

**name** corresponds to the error code, **domain** to the domain: e.g. signal, record, device. **message** contains a more detailed message, and the status corresponds to a pass/fail status of the analysis.
All possible messages are defined in the datascience.ds.dataio.exceptions.py file.

# example installation with py312
```
python -m pip install uv
.\datascience\docs\scripts\setupEnv.ps1
```
For more details on how to use:

```
Get-Help .\datascience\docs\scripts\setupEnv.ps1 -Detailed
```

# Deployment
Currently, the algorithms are stored as pickles in the ds.dataio repository and deployed with the API. A given API selects one or more algorithms according to the desired output.
The API can be simply deployed as an azure function from VS-Code simply by right clicking on the ds-compute folder and selecting 'deploy to function app'.
We can then select an existing azure function to deploy to. We currently have two azure functions; ds-functions (prod) and ds-function-staging (staging).

The following sequence is performed for the deployment of a novel algorithm, from the datascience stream POV:
1. Program and train the novel algorithm. This results in a QTR-Algorithm, stored in the datascience drive (ds-results/QTP).
2. Perform analytic performance if needed. This results in a QTR-AnalyticPerformance, stored in the datascience drive (ds-results/QTP).
3. Integrate the novel algorithm in the API.
4. Run locally the API unit tests.
5. Deploy to the staging environment.
6. Run remotely the API unit tests.
7. Wait for approval from the backend team to deploy to the prod environment.
8. Reproduce the deployment steps to the prod environment (steps 4-6)

# Algorithms Design documentation

## Release notes
Algorithm release notes are available at <https://github.com/usense-projects/datascience/blob/main/ds/models/readme.md>

## Versioning
Machine learning code cannot only consist of a code version, as algorithms are also dependant on training data.
For this reason, algorithm versions are defined as name-Vx.y.z where
- name is the algorithm name, chosen to be short but explanatory
- x: major version. A change of major version indicates a change in signal processing, or model
- y: minor version. A change of minor version indicates a bugfix, or minor change in the code
- z: data version. A change in the data version indicates a change in the training data
This will be improved onve we migrate all machine learning onto azure, were we will be able to have hash codes for code and data, enhancing traceability.
For better traceability, each algorithm sends its unique information with its output at each call.

## Code dependencies and safety
The datascience code is based on Python 3.11+ <https://www.python.org> and tries to minimize non standard libraries.
The full and up to date list of dependencies is available at <https://github.com/usense-projects/datascience/blob/main/pyproject.toml>
The biomarkers algorithms are mainly based on standard and well tested dependencies:
- data manipulation: numpy, scipy, pandas
- data access: microsoft azure libraries, requests, pyodbc
- machine learning: scikit-learn, statsmodels, lmfit
- code integrity: ruff, pydantic

The data exposed to this code includes signals extracted from the patients biofluids, sampleId, organization, technician account and date of the record.
Other patient metadata is not accessible by the code.

## Biomarker specific design
## Acute porphyria
### Total Urinary Porphyrin
The algorithm takes as an input a jimini scan of a urine sample and goes through the following steps:
1. We first asserts that the record is readable, well constructed and scanned with the following requirements:
- the record is performed with a jimini device, on a urine sample, untreated, with sufficient volume of biofluid.
- the spectra C12-405 and C12-275 are available.
2.

### Porphobilinogen
The algorithm takes as an input two jimini scans of a raw then heated urine sample, and goes through the following steps:
