# Datascience ETL and Database (PostgreSQL)

## Rationale
### The USense Databases and Storage
Regarding the data pipelines, USense has several sources of information for Jimini data:
- An **indexing database**: maintains an index of the records from the devices.
- A **record blob storage**: stores raw records as JSON files in blob storage.
- A **biomarkers blob storage**: contains exports from our partners.
- **Google Sheets**: used to save information not present in the other databases for specific experiments, validations, etc.
- **Individual folders**: for records acquired with the HW-SDK.

These are the unique sources of persistent information and require careful handling. However, they contain raw, unprocessed data and are not directly queryable for batch processing. Additionally, the raw data has several formats, is not normalized, and lacks a common unique key between the biomarkers and the collected data.

Therefore, to utilize this data for data science purposes, reports, etc., an ETL, ingesting, normalizing and cleaning step is required.

## The Datascience ETL and Database

The DS-DB creates processed and normalized copies of the available data. Any deletion or update in this database affects the company information stored in the USense databases.

**The DS ETL**:
- Processes biomarkers and data to create a common unique key for each record in the format `<organization><sampleId><year>`, avoiding conflicts among and within organizations.
- Normalizes the data, creating names for the SLCs, cleaning sample IDs, and reformatting SLCs to the v1 data model.
- Preprocesses the SLCs for faster access and resamples them to common wavelengths.
- Normalizes the biomarkers, cleaning values for numeric and categorical biomarkers.
- Stores the processed information into DS-DB, a PostgreSQL database.

**The DS Database**:
The database contains three tables:
- **Records**: contains the metadata for each record.
- **Sensors**: contains the sensor metadata, data, and processed data for all records.
- **Biomarkers**: contains the exported and cleaned biomarkers.

**The DS Database Class `DbPostGreSql`**:\
This class in the repository `datascience.dataio.remote.dbpg.DbPostGreSql` allows for creating and updating the DS-DB with minimal code. Note: updates are incremental, so if changes are made to ingested information, the database needs to be reset.

## Stored Information
The DS-DB stores the signals from the Jimini devices, as well as the following information: sample ID, age, gender, organization, and biomarkers information available in the partner extracts. We do not know when the sample was provided by the patient, so tracing back to individuals would require access to the partners' servers, which we do not have.

## Setting Up the Database
- Create a local PostgreSQL database.
- Copy the `.env.template` from the DS repository into a `.env` file and fill in your credentials. Ensure that the `.env` file remains local and is not synced with Git.
- Instantiate `db = DbPostGreSql()` and call `db.createTables()`.
- Call `db.updateAll()` to populate the database. This will run the ETL and create all necessary information.

To update the database:
```python
from ds.dataio.remote.dbpg import DbPostGreSql
db = DbPostGreSql()
db.updateAll()
```
From then on, we can use the same class to query records using `querySensors` or `queryRecords`. Both functions allow querying using filters on records (e.g., `macAddress`, `study`, `firmwareVersion`), on sensors (e.g., `c12-vis`), sensor metadata, or biomarkers presence (e.g., `rbc`). `queryRecords` returns records, and `querySensors` returns sensors. There are several modes for returned information: "ds" provides a Dataset, "raw" provides raw records/sensors, and "dict" returns a dictionary. The most useful mode is the dataset, as this class allows sorting, plotting, selecting information, among other functionalities.

## Future Evolution
This database serves as a temporary solution to facilitate working with data. When we manage to establish on the cloud side:
- A single stable Jimini format, normalized, containing wavelengths, and all necessary information.
- Common keys to map with biomarkers, ideally de-identified.
- A method to map biomarkers with records in the cloud.
- The SDK records saved to a specific blob storage.

We could set up a USense storage service, allowing direct saving and querying (including individual SLCs) of records and biomarkers. At that point, there would be no need for this database, and we could have a unified data service. This requires significant effort on the cloud side, and is not prioritized at this time.
