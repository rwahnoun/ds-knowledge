---
title: Datascience Architecture & API
aliases:
  - DS API
  - Datascience Architecture
  - Algorithms API
tags:
  - topic/architecture
  - type/architecture
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Datascience Architecture & API

Reference for the datascience code repositories, validation protocols, computing platform, and algorithm API. See [[database]] for the PostgreSQL data pipeline and [[device]] for the Jimini device and SLC naming conventions.

---

## Repositories

The data science code is hosted under the company GitHub account and is split into several repositories:

| Repository | URL | Contents |
|---|---|---|
| **datascience** | https://github.com/usense-projects/datascience | Code for data loaders, ETL, pipelines, signal processing, models, quality test protocols, and statistical tests |
| **ds-compute** | https://github.com/usense-projects/ds-compute | Code for the computing platform (Azure Functions) |
| **ds-scripts** | https://github.com/usense-projects/ds-scripts | Analysis scripts and Python notebooks |
| **knowledge** | https://github.com/usense-projects/knowledge | Production information on the company devices; ontology for normalization |

---

## Validation and Testing

Several test suites ensure performance and non-regression:

| Test Suite | Purpose | When Run |
|---|---|---|
| **unit tests** | Cover code exposed by the API. Test validity of API calls, ability to obtain and read Jimini records, and normal/abnormal responses. | Locally before deploying algorithms, and remotely in staging environment to validate deployment |
| **qtpAlgorithm** | Calculate standard ML metrics on one or more datasets to evaluate algorithm performance. | At end of development of a new algorithm |
| **qtpAnalyticPerformance** | Post-hoc test on a dataset unseen by the algorithm, to assess generalisation performance and estimate LoD, matrix interactions, etc. | After qtpAlgorithm, before production deployment |

---

## Data

The data science team handles two main types of data:

- **Device records** contain signals and associated data. These records can originate from Jiminis, spectrophotometers, and other external or research devices. All records are normalized through loaders into a universal format in the class `Records`. An ontology is used to resolve data heterogeneity.
- **Biomarkers** originate from columnar automatic exports from our partners, or CSV files written by our technicians. Similarly, they are normalized into a common format.

An ETL pipeline integrates and processes records and biomarkers to feed a mongo (records) and a SQL (biomarkers) database. See [[database]] for details.

---

## Computing Platform

The datascience algorithms are exposed using **Azure Functions**. This allows controlled access as well as scalability.

The Azure Functions can be called from a local computer, or from the cloud service after authentication. Examples of exposed functions include biomarker estimation from one or more Jimini records, or quality estimation of a given record.

The platform can be directly deployed from VS-Code, after validation of the related unit tests and QTPs. The platform is first deployed into a staging environment, then into a production environment once approved by the cloud team's integration tests.

---

## General API

To facilitate calls and the addition of new algorithms, the API exposes all algorithms on a single endpoint.

### API Call

The input is a dictionary containing:

- **`analysisType` (strList|str)** — algorithms to run.
  Examples: `'tup'`, `'pbg'`, `'redBloodCells'`, `'leukocytes'`, `'*'` (run everything possible), combinations like `['tup','pbg']` are accepted.

- **`records` (dict)** — records to analyse. Should contain `raw` (dict) for all algorithms and `raw` and `heated` for pbg. Record can follow several formats:
  - URL: `{"url": <signed url>}`
  - Blob storage: `{"blob": <blob>, "storageAccount": <"usense"|"research">}`
  - Raw JSON: `{"raw": <raw jimini record>}`

### Response

The output contains four fields:

| Field | Type | Description |
|---|---|---|
| **`request`** | dict | Contains the input information |
| **`items`** | list | Contains the items resulting from the analysis |
| **`status`** | str | `'pass'` if we managed to handle the request, `'fail'` if we failed |
| **`errors`** | list | Contains global error messages upon failure |

### Items Structure

Each item (dict) corresponds to a given analysis and can contain:

| Field | Type | Description |
|---|---|---|
| **`author`** | str | Algorithm name |
| **`version`** | str | Algorithm version |
| **`trainingDate`** | str | Algorithm training date |
| **`name`** | str | Biomarker name |
| **`unit`** | str | Biomarker unit |
| **`cat`** | str, optional | Result as a categorical string |
| **`cnt`** | float\|int, optional | Result as a continuous value |
| **`cntRng`** | str, optional | Result as a continuous value within a range |
| **`status`** | str | `'pass'`\|`'fail'` for this specific algorithm |
| **`errors`** | list | List of messages in case of error |

### Errors Structure

The full list of possible error messages is available in `datascience/ds/dataio/exceptions.py`.

- **`name`** — error code
- **`domain`** — domain: e.g., signal, record, device
- **`message`** — more detailed message
- **`status`** — pass/fail status of the analysis

---

## Example Installation with py312

```bash
python -m pip install uv
.\datascience\docs\scripts\setupEnv.ps1
```

For more details on how to use:

```powershell
Get-Help .\datascience\docs\scripts\setupEnv.ps1 -Detailed
```

---

## Deployment

Currently, the algorithms are stored as pickles in the `ds.dataio` repository and deployed with the API. A given API selects one or more algorithms according to the desired output.

The API can be deployed as an Azure Function from VS-Code by right-clicking on the `ds-compute` folder and selecting 'deploy to function app'. We currently have two Azure Functions: `ds-functions` (prod) and `ds-function-staging` (staging).

### Deployment Sequence for a Novel Algorithm

1. Program and train the novel algorithm. This results in a QTR-Algorithm, stored in the datascience drive (`ds-results/QTP`).
2. Perform analytic performance if needed. This results in a QTR-AnalyticPerformance, stored in the datascience drive (`ds-results/QTP`).
3. Integrate the novel algorithm in the API.
4. Run locally the API unit tests.
5. Deploy to the staging environment.
6. Run remotely the API unit tests.
7. Wait for approval from the backend team to deploy to the prod environment.
8. Reproduce the deployment steps to the prod environment (steps 4–6).

---

## Algorithm Design Documentation

### Versioning

Machine learning code cannot only consist of a code version, as algorithms are also dependent on training data. Algorithm versions are defined as `name-Vx.y.z` where:

| Component | Description |
|---|---|
| `name` | Algorithm name — short but explanatory |
| `x` | Major version — change in signal processing or model |
| `y` | Minor version — bugfix or minor code change |
| `z` | Data version — change in training data |

For better traceability, each algorithm sends its unique information with its output at each call.

### Code Dependencies and Safety

The datascience code is based on Python 3.11+. The full and up-to-date list of dependencies is available at `https://github.com/usense-projects/datascience/blob/main/pyproject.toml`.

Key dependencies:

| Category | Libraries |
|---|---|
| Data manipulation | numpy, scipy, pandas |
| Data access | microsoft azure libraries, requests, pyodbc |
| Machine learning | scikit-learn, statsmodels, lmfit |
| Code integrity | ruff, pydantic |

The data exposed to this code includes signals extracted from the patient's biofluids, sampleId, organization, technician account and date of the record. Other patient metadata is not accessible by the code.

---

## Biomarker-Specific Design

### Acute Porphyria — Total Urinary Porphyrin (TUP)

The algorithm takes as input a Jimini scan of a urine sample and goes through the following steps:

1. Asserts that the record is readable, well-constructed and scanned with the following requirements:
   - The record is performed with a Jimini device, on a urine sample, untreated, with sufficient volume of biofluid.
   - The spectra `C12-405` and `C12-275` are available.
2. (Further steps to be documented as algorithm matures)

### Acute Porphyria — Porphobilinogen ([[porphobilinogen|PBG]])

The algorithm takes as input two Jimini scans of a raw then heated urine sample. (Further steps to be documented as algorithm matures)

---

## Sources

| Source | Notes |
|---|---|
| datascience GitHub repository | https://github.com/usense-projects/datascience |
| Algorithm release notes | https://github.com/usense-projects/datascience/blob/main/ds/models/readme.md |
| [[database]] | PostgreSQL ETL and data pipeline |
| [[device]] | Jimini device and SLC naming |

## Gaps

1. The TUP and [[porphobilinogen|PBG]] algorithm step-by-step design documentation is incomplete — algorithm-specific design docs should be added as algorithms are finalized.
2. The API endpoint URL and authentication method for external callers not documented here — refer to ds-compute repository.
3. Staging vs production environment configuration differences not documented.
