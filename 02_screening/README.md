# 02_screening

Title and abstract screening of the 624 unique records against the protocol's inclusion and exclusion criteria.

`screened.csv` holds one row per record: bibliographic fields, the database of origin, the decision (INCLUDE / EXCLUDE / UNCERTAIN), the criteria that triggered an exclusion, and a short written justification.

| Column | Content |
|---|---|
| `id` | Record identifier (P0001 ...) |
| `pdf_present` | True when the full text was obtained (see `03_retrieval/retrieval_status.csv`) |
| `title`, `doi`, `year`, `source`, `authors`, `abstract`, `doc_type` | Bibliographic fields from the database export |
| `db`, `_also_in` | Database the record was taken from and the other databases that returned it |
| `decision`, `confidence` | Screening decision and the confidence in it |
| `triggered_criteria` | Criteria that triggered an exclusion. For retained records, the inclusion criteria confirmed from the abstract |
| `reasoning` | Written justification of the decision |
| `flag` | Concern noted at screening to be checked at full text (for example that VIO may be consumed as a black-box input) |

280 records were included and 29 uncertain records were deferred to full-text assessment (309 sought for retrieval in total). 315 were excluded, 17 of them with INC-4 as the first criterion (venue and metadata show a non-English full text).

## Screening procedure

The records were screened against the INC/EXC criteria of the protocol as described in Section 4.4 of the paper. The decision recorded in `screened.csv` is the final decision for each record.
