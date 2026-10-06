# 01_identification

Database search results. Searches were run in September 2026 in Scopus, Web of Science Core Collection and IEEE Xplore, restricted to articles and conference papers from 2014 onwards. Query strings are documented in Section 4.2.2 of the paper and in `00_protocol/`.

| File | Content |
|------|---------|
| `scopus_export_09_2026.csv` | Scopus export, 364 records |
| `wos_export_09_2026.csv` | Web of Science export, 249 records |
| `ieee_export_09_2026.csv` | IEEE Xplore export, 408 records |
| `deduplicated_papers.csv` | 624 unique records after removing 397 duplicates by DOI and normalised title (the `_also_in` column records cross-database overlap) |
| `deduplicated_papers_with_id.csv` | The same records with the P-number identifiers used throughout the later stages |

The P-numbers are identifiers only. They are not consecutive and carry no meaning beyond linking the stage files.
