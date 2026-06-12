# Adaptive VIO for UAV Navigation — SLR audit trail

Supplementary materials for the systematic literature review *Adaptive Visual-Inertial Odometry Methods for UAV Navigation in GNSS-Denied Environments*. The repository contains the complete decision trail from database export to synthesis, so that every number, table and figure in the paper can be traced back to its source records and recomputed.

Each folder corresponds to one stage of the PRISMA 2020 flow.

| Folder | Stage | Content |
|--------|-------|---------|
| `00_protocol/` | A-priori protocol | Protocol document: criteria, PICO, T-filters, QA scheme |
| `01_identification/` | Identification | Raw database exports and the deduplicated record list |
| `02_screening/` | Screening | Title/abstract decisions for all 398 unique records |
| `03_retrieval/` | Retrieval | Retrieval status for the 232 sought reports |
| `04_eligibility/` | Eligibility | Full-text triage worksheet (T-filters, relevance scores) |
| `05_quality_assessment/` | Quality assessment | QA1–QA5 scores per retained paper |
| `06_data_extraction/` | Data extraction | 20-field extraction table for the 89 included studies |
| `07_synthesis/` | Synthesis | Parametric tables, figure generator, PRISMA flow, keyword maps |

Full-text PDFs and the manuscript are not redistributed here for copyright reasons. The included studies are identified by DOI in `07_synthesis/ref_id_matching.csv`.

## Review protocol, as implemented

**Research questions.** RQ1 publication trends; RQ2 fusion architectures and visual front-ends; RQ3 adaptive and robust strategies; RQ4 datasets, platforms and evaluation metrics; RQ5 limitations and open research directions.

**Search.** Scopus, Web of Science Core Collection and IEEE Xplore were queried on 15 May 2026 with a PICO-derived expression combining visual-inertial odometry/navigation/fusion terms with UAV terms, restricted to articles and conference papers published 2014 or later. The exact query strings per database are given in Section 2.2 of the paper. The exports returned 648 records (Scopus 253, Web of Science 160, IEEE Xplore 235); deduplication by DOI and normalised title left 398 unique records (250 duplicates removed).

**Screening.** Each record was screened on title and abstract against five inclusion criteria (UAV platform; VIO/VINS topic; algorithmic contribution; English; 2014 or later) and the exclusion criteria of the protocol (surveys, non-aerial platforms, pure GNSS work, vision-only or inertial-only pipelines, applications that consume VIO as a black box, and so on). 232 records were retained (228 clear includes and 4 uncertain records deferred to full text, following PRISMA guidance) and 166 were excluded. Screening was done by a single reviewer; a 10 % random sample was re-screened after a one-week delay, giving an inter-occasion agreement of κ = 0.84.

**Retrieval.** Full texts of the 232 retained records were sought through institutional access, open-access repositories, publisher platforms and author requests. 81 reports were obtained in the first pass and 43 more in a supplementary round; 108 reports could not be obtained through any channel and were excluded (EXC-8). `03_retrieval/retrieval_status.csv` records the outcome per report.

**Eligibility.** The 124 retrieved reports were read in full and assessed against three hard filters: T-1, the paper makes an algorithmic contribution to VIO rather than consuming it; T-2, the method is validated on aerial data; T-3, a quantitative evaluation is reported. Six binary relevance dimensions (GNSS-denied operation, adaptive component, real-time embedded operation, filter-based fusion, feature front-end, auxiliary sensor) were scored alongside. 35 reports were excluded: 32 failed T-1, 12 of which also failed T-3, and 3 were excluded under the language criterion on full-text inspection. This leaves the final corpus of **89 studies** (2015–2026).

**Quality assessment.** Each retained paper was scored on the five items of Dybå and Dingsøyr (clear objective; experimental setup described; baseline comparison; limitations discussed; conclusions supported), each at 0 / 0.5 / 1.0. Mean total 4.24, minimum 2.0, maximum 5.0; no paper fell below the 2.0 sensitivity threshold.

**Extraction and synthesis.** A 20-field template (identification, architecture, front-end, adaptation, platform, evaluation, analysis) was applied to every included study; the result is `06_data_extraction/extractions_full.csv`. The synthesis classifies the corpus along seven parametric dimensions: fusion architecture, visual front-end, auxiliary sensors, adaptive-strategy family, addressed conditions, platform and validation regime, and evaluation metrics. The classification lives in `07_synthesis/parametric_tables.csv`, which is the single curated source for the paper's Tables 6–12 and the parametric figures.

**PRISMA flow.** 648 identified → 250 duplicates removed → 398 screened → 166 excluded → 232 sought → 108 not retrieved → 124 assessed → 35 excluded → 89 included. The rendered diagram is in `07_synthesis/prisma/`.

## Reproducing the figures

```
pip install matplotlib numpy
cd 07_synthesis
python3 generate_figures.py            # rebuilds all figures and validates the corpus
python3 generate_figures.py --audit    # extra consistency check of the curated tables
```

The generator reads only the stage CSVs in this repository and validates that corpus size, reference numbering and table memberships agree before writing anything.

## License

Code and data files are released under the MIT License (see `LICENSE`). The bibliographic records originate from Scopus, Web of Science and IEEE Xplore and remain subject to the providers' terms.
