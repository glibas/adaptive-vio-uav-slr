# 02_screening

Title and abstract screening of the 398 unique records against the protocol's inclusion and exclusion criteria.

`screened.csv` holds one row per record: bibliographic fields, the database of origin, the decision (INCLUDE / EXCLUDE / UNCERTAIN), the criteria that triggered an exclusion, and a short written justification.

| Column | Content |
|---|---|
| `id` | Record identifier (P0001 ...) |
| `pdf_present` | True when the full text was obtained (see `03_retrieval/retrieval_status.csv`) |
| `title`, `doi`, `year`, `source`, `authors`, `abstract`, `doc_type` | Bibliographic fields from the database export |
| `db`, `_also_in` | Database the record was taken from and the other databases that returned it |
| `decision`, `confidence` | Consensus screening decision and the screeners' confidence in it |
| `triggered_criteria` | Criteria that triggered an exclusion. For retained records, the inclusion criteria confirmed from the abstract |
| `reasoning` | Written justification of the decision |
| `flag` | Concern noted at screening to be checked at full text (for example that VIO may be consumed as a black-box input) |

224 records were included and 6 uncertain records were deferred to full-text assessment (230 sought for retrieval in total). 168 were excluded, 12 of them under INC-4 (venue and metadata show a non-English full text).

## Screening procedure

All 398 records were screened independently by three researchers against the INC/EXC criteria. Disagreements were resolved by discussion. The consensus decision is the one recorded in `screened.csv`.
