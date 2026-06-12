# 01_identification

Database search results. Searches were run on 15 May 2026 in Scopus, Web of Science Core Collection and IEEE Xplore, restricted to articles and conference papers from 2014 onwards. Query strings are documented in Section 2.2 of the paper.

| File | Content |
|------|---------|
| `scopus_export_15_05_2026.csv` | Scopus export, 253 records |
| `wos_export_15_05_2026.csv` | Web of Science export, 160 records |
| `ieee_export_15_05_2026.csv` | IEEE Xplore export, 235 records |
| `deduplicated_papers.csv` | 398 unique records after removing 250 duplicates (the `_also_in` column records cross-database overlap) |
| `deduplicated_papers_with_id.csv` | The same records with the P-number identifiers used throughout the later stages |
