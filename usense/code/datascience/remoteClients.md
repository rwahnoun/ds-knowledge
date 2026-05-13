---
title: ds.dataio.remote — Remote Data Clients
aliases:
  - DbPostGreSql
  - GoogleDriveClient
  - dbpg
  - gdrive
tags:
  - topic/repo
  - type/reference
  - status/complete
date: 2026-05-05
status: complete
type: reference
author: claude
---

# ds.dataio.remote — Remote Data Clients

`d:\code\datascience\src\ds\dataio\remote\` | `from ds.dataio.remote.dbpg import DbPostGreSql`

Clients for external data sources: PostgreSQL records DB, Google Drive/Sheets, Azure Blob/FileShare, MongoDB, and SQLite. The two most-used in notebooks are `DbPostGreSql` and `GoogleDriveClient`.

## Index

| Name | Type | Purpose |
|------|------|---------|
| `DbPostGreSql` | class | Query and update the PostgreSQL records/biomarkers DB |
| `GoogleDriveClient` | class | Read/write Google Sheets and Drive files |

## Reference

### `DbPostGreSql`

`from ds.dataio.remote.dbpg import DbPostGreSql`

#### `updateAll(reset=False)`
Syncs the DB from Azure blob storage. Always call before querying when fresh data is needed. `reset=True` drops and recreates the tables first.

#### `queryRecords(recordMetaFilters, sensorMetaFilters, biomarkersFilters, sensorLabels, limit, mode, name) → DatasetRecords | list`
Returns records matching the given filters.
- `recordMetaFilters`: dot-notation dict, e.g. `{"sample.sampleId": [...], "sample.sampleType": "urine"}`. Lists are treated as `IN` clauses.
- `mode`: `"ds"` (default) returns a `DatasetRecords`; `"raw"` returns raw SQLAlchemy rows.
- `name`: label attached to the returned dataset.

---

### `GoogleDriveClient`

`from ds.dataio.remote.gdrive import GoogleDriveClient`

#### `readGoogleSheet(src, sheetName) → pd.DataFrame`
Returns the sheet as a DataFrame (first row = column headers, all values as strings).
- `src`: spreadsheet ID (not the full URL) — extract from `https://docs.google.com/spreadsheets/d/<ID>/...`
- `sheetName`: tab name (the label on the sheet tab, not the `gid=` number)

## Typical pattern — sheet → dataset → pickle

Standard ingest used across `ds6xx` notebooks: read a Google Sheet for the sample list, sync the DB, query, save.

```python
import pickle
from ds.dataio.remote.dbpg import DbPostGreSql
from ds.dataio.remote.gdrive import GoogleDriveClient

SHEET_ID = "1LKPFuST9Py9jmGg-poLCYU2Tk-EOJvpd4qacT4lpYXI"
SHEET_TAB = "meta"  # tab name, not gid

gd = GoogleDriveClient()
meta = gd.readGoogleSheet(SHEET_ID, SHEET_TAB)
lstSid = meta.sampleId.dropna().unique().tolist()

db = DbPostGreSql()
db.updateAll()

ds = db.queryRecords(
    recordMetaFilters={"sample.sampleId": lstSid},
    mode="ds",
    name="ds687",
)

with open(r"d:\tmp\ds687.pickle", "wb") as f:
    pickle.dump(ds, f)
```

> [!TIP]
> `sheetName` is the visible tab label in the spreadsheet, not the numeric `gid` in the URL. Open the sheet and read the tab name directly.

## Sources

| Source | Notes |
|--------|-------|
| [`d:\code\datascience\src\ds\dataio\remote\dbpg.py`](file:///D:/code/datascience/src/ds/dataio/remote/dbpg.py) | `DbPostGreSql` implementation |
| [`d:\code\datascience\src\ds\dataio\remote\gdrive.py`](file:///D:/code/datascience/src/ds/dataio/remote/gdrive.py) | `GoogleDriveClient` implementation |
| [`d:\code\ds-scripts\src\notebooks\ds600\ds687.py`](file:///D:/code/ds-scripts/src/notebooks/ds600/ds687.py) | Example usage |

## Gaps

- `azureUsense`, `dbMongo`, `dbSqlite`, and Azure FileShare clients are not documented here yet.
