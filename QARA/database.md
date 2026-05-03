---
title: Datascience ETL and Database (PostgreSQL)
aliases:
  - DS Database
  - DS-DB
  - ETL Pipeline
tags:
  - topic/architecture
  - type/reference
  - device/jimini
  - status/complete
date: 2026-04-19

---

# Datascience ETL and Database (PostgreSQL)

Technical reference for the DS-DB data pipeline that normalizes Jimini records and biomarkers into a queryable PostgreSQL database. See [[QARA/overview]] (QARA) for the broader datascience architecture and [[device]] for the Jimini device and SLC naming conventions.

---

## Rationale

### The USense Databases and Storage

Regarding the data pipelines, USense has several sources of information for Jimini data:

- An **indexing database**: maintains an index of the records from the devices.
- A **record blob storage**: stores raw records as JSON files in blob storage.
- A **biomarkers blob storage**: contains exports from our partners.
- **Google Sheets**: used to save information not present in the other databases for specific experiments, validations, etc.
- **Individual folders**: for records acquired with the HW-SDK.

These are the unique sources of persistent information and require careful handling. However, they contain raw, unprocessed data and are not directly queryable for batch processing. Additionally, the raw data has several formats, is not normalized, and lacks a common unique key between the biomarkers and the collected data.

Therefore, to utilize this data for data science purposes, reports, etc., an ETL ingesting, normalizing and cleaning step is required.

---

## The Datascience ETL and Database

The DS-DB creates processed and normalized copies of the available data. Any deletion or update in this database affects the company information stored in the USense databases.

### The DS ETL

- Processes biomarkers and data to create a common unique key for each record in the format `<organization><sampleId><year>`, avoiding conflicts among and within organizations.
- Normalizes the data, creating names for the SLCs, cleaning sample IDs, and reformatting SLCs to the v1 data model.
- Preprocesses the SLCs for faster access and resamples them to common wavelengths.
- Normalizes the biomarkers, cleaning values for numeric and categorical biomarkers.
- Stores the processed information into DS-DB, a PostgreSQL database.

### The DS Database

The database contains three tables:

| Table | Contents |
|---|---|
| **Records** | Metadata for each record |
| **Sensors** | Sensor metadata, raw data, and processed data for all records |
| **Biomarkers** | Exported and cleaned biomarker values |

### The DS Database Class `DbPostGreSql`

Class in the repository `datascience.dataio.remote.dbpg.DbPostGreSql`. Allows creating and updating the DS-DB with minimal code.

> [!NOTE]
> Updates are incremental. If changes are made to ingested information, the database needs to be reset.

---

## Stored Information

The DS-DB stores the signals from the Jimini devices, as well as the following information: sample ID, age, gender, organization, and biomarkers information available in the partner extracts. We do not know when the sample was provided by the patient, so tracing back to individuals would require access to the partners' servers, which we do not have.

---

## Setting Up the Database

1. Create a local PostgreSQL database.
2. Copy the `.env.template` from the DS repository into a `.env` file and fill in your credentials. Ensure that the `.env` file remains local and is not synced with Git.
3. Instantiate `db = DbPostGreSql()` and call `db.createTables()`.
4. Call `db.updateAll()` to populate the database.

```python
from ds.dataio.remote.dbpg import DbPostGreSql

db = DbPostGreSql()
db.updateAll()
```

### Querying the Database

Use `querySensors` or `queryRecords` after population. Both functions allow querying using filters on records (e.g., `macAddress`, `study`, `firmwareVersion`), on sensors (e.g., `c12-vis`), sensor metadata, or biomarker presence (e.g., `rbc`).

| Method | Returns | Best mode |
|---|---|---|
| `queryRecords` | Record objects | `"ds"` — returns a Dataset |
| `querySensors` | Sensor objects | `"ds"` — returns a Dataset |

Modes: `"ds"` (Dataset, most useful for ML), `"raw"` (raw records/sensors), `"dict"` (dictionary).

---

## Future Evolution

This database serves as a temporary solution to facilitate working with data. When the cloud side can provide:

- A single stable Jimini format, normalized, containing wavelengths, and all necessary information.
- Common keys to map with biomarkers, ideally de-identified.
- A method to map biomarkers with records in the cloud.
- The SDK records saved to a specific blob storage.

A USense storage service allowing direct saving and querying (including individual SLCs) of records and biomarkers would replace the DS-DB entirely. This requires significant effort on the cloud side, and is not prioritized at this time.

---

## Sources

| Source | Notes |
|---|---|
| `datascience.dataio.remote.dbpg.DbPostGreSql` | Primary class for DB creation and querying |
| [[QARA/overview]] (QARA) | Broader datascience architecture |
| [[device]] | SLC naming conventions and record structure |

## Gaps

1. No documentation of the specific PostgreSQL schema (column names, data types, foreign keys) — this should be extracted from `db.createTables()` and documented here.
2. Reset/migration procedure not documented — if changes are made to ingested information, the procedure for a full DB reset needs to be specified.
3. The `querySensors` and `queryRecords` filter parameter API not fully documented here — refer to the source code in `datascience.dataio.remote.dbpg`.

[QARA/overview]: overview.md "Datascience Overview — ds-learn"
[device]: device.md "Jimini Device Description"
