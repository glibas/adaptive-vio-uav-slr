# Adaptive VIO for UAV Navigation — SLR audit trail

Data, code, and decision trail for the systematic literature review *Research gaps in adaptive visual-inertial odometry for UAV navigation: A systematic literature review*, from database export to synthesis.

Each folder corresponds to one stage of the PRISMA 2020 flow.

| Folder | Stage | Content |
|--------|-------|---------|
| `00_protocol/` | A-priori protocol | Protocol document: criteria, PICO, T-filters, QA scheme |
| `01_identification/` | Identification | Raw database exports and the deduplicated record list |
| `02_screening/` | Screening | Title/abstract decisions for all 624 unique records |
| `03_retrieval/` | Retrieval | Retrieval status for the 309 sought reports |
| `04_eligibility/` | Eligibility | Full-text triage worksheet (T-filters, relevance scores) |
| `05_quality_assessment/` | Quality assessment | QA1–QA5 scores per retained paper |
| `06_data_extraction/` | Data extraction | 20-field extraction table plus the coded synthesis columns for the 182 included studies |
| `07_synthesis/` | Synthesis | Parametric tables, figure generator, PRISMA flow, keyword probe |

Full-text PDFs and the manuscript are not redistributed here for copyright reasons. The included studies are identified by DOI in `07_synthesis/ref_id_matching.csv`, which also gives the reference number each study has in the paper.

## Review protocol, as implemented

**Research questions.** RQ1 publication trends. RQ2 fusion architectures and visual front-ends. RQ3 adaptive and robust strategies. RQ4 datasets, platforms and evaluation metrics. RQ5 limitations and open research directions.

**Search.** Scopus, Web of Science Core Collection and IEEE Xplore were queried in September 2026 with a PICO-derived expression combining visual-inertial odometry/navigation/fusion terms with the platform terms "unmanned aerial vehicle", "UAV" and "drone*", restricted to articles and conference papers published 2014 or later. The exact query strings per database are given in Section 4.2.2 of the paper and in `00_protocol/`. The exports returned 1021 records (Scopus 364, Web of Science 249, IEEE Xplore 408). Deduplication by DOI and normalised title left 624 unique records (397 duplicates removed).

**Screening.** Each record was screened on title and abstract against the five inclusion criteria of the protocol (visual-inertial fusion, UAV platform, peer-reviewed, English, 2014 or later) and its exclusion criteria (surveys, non-aerial platforms, pure GNSS work, vision-only or inertial-only pipelines, applications that consume VIO as a black box, and so on). 309 records were retained (280 clear includes and 29 uncertain records deferred to full text, following PRISMA guidance) and 315 were excluded, 17 of them under INC-4 for records whose venue and metadata show a non-English full text. The screening procedure is described in Section 4.4 of the paper. The decision recorded in `02_screening/screened.csv` is the final decision for each record.

**Retrieval.** Full texts of the 309 retained records were sought through institutional access, open-access repositories, publisher platforms and author requests. 283 were obtained. 26 could not be retrieved through any channel and were excluded (EXC-8). `03_retrieval/retrieval_status.csv` records the outcome per report.

**Eligibility.** The 283 retrieved reports were read in full and assessed against three hard filters: 
T-1, the paper makes an algorithmic contribution to VIO rather than consuming it, 
T-2, the method is validated on aerial data, 
T-3, a quantitative evaluation is reported. 
Six binary relevance dimensions (GNSS-denied operation, adaptive component, real-time embedded operation, filter-based fusion, feature front-end, auxiliary sensor) were scored alongside. 101 reports were excluded: 76 failed T-1 (25 of which also failed T-3), 13 failed T-2, 7 failed T-3 alone, 2 under the language criterion (INC-4), and 3 under EXC-9 (reports from institutions of the Russian Federation, a non-scientific criterion that follows bill No. 7633 of the Verkhovna Rada of Ukraine, adopted in the first reading on 1 December 2022, and is applied after the scientific filters). All three EXC-9 reports pass the scientific filters. Including them would raise the corpus to 185 and change seven counts by one to three studies each, without changing which cells of the taxonomy are populated (Section 4.5 of the paper). The final synthesis corpus is **182 studies** (2015–2026). T-1 is applied with its explicit definition (a new VIO algorithm, or a multi-sensor estimator whose VIO measurement model, weighting or auxiliary-sensor integration is the contribution). GNSS-denied operation and adaptivity are synthesis dimensions, not eligibility criteria: 125 of the 182 studies explicitly target GNSS-denied operation, 140 contain an adaptive or online component, and 96 have both.

**Quality assessment.** Each retained paper was scored on the five items of Dybå and Dingsøyr (clear objective, experimental setup described, baseline comparison, limitations discussed, conclusions supported), each at 0 / 0.5 / 1.0. Mean total 4.14, minimum 2.5, maximum 5.0. No paper fell below the 2.0 sensitivity threshold.

**Extraction and synthesis.** A 20-field template (identification, architecture, front-end, adaptation, platform, evaluation, analysis) was applied to every included study, together with the coded columns described in Section 10 of the protocol. The result is `06_data_extraction/extractions_full.csv`. The synthesis classifies the corpus along eight parametric dimensions: fusion architecture, visual front-end, auxiliary sensors, adaptive-strategy family, addressed conditions, platform type, validation regime, and evaluation metrics. The classification lives in `07_synthesis/parametric_tables.csv`, the single curated source for the paper's Tables 8, 9 and 11–16 and the parametric figures. Reference numbers in the data files are those of the paper, where references are numbered in order of first appearance.

**PRISMA flow.** 1021 identified → 397 duplicates removed → 624 screened → 315 excluded → 309 sought → 26 not retrieved → 283 assessed → 101 excluded → 182 included. The rendered diagram is in `07_synthesis/prisma/`.

## Reproducing the figures

```
pip install matplotlib numpy
cd 07_synthesis
python3 generate_figures.py            # rebuilds figures 2–6 and validates the data files
python3 keyword_probe.py               # Table 18 probe (needs ../papers/*.pdf or --textdir)
python3 prisma/build_prisma.py         # Fig. 1 (PRISMA flow) from the stage CSVs, rendered with Edge
```

## License

Code and data files are released under the MIT License (see `LICENSE`). The bibliographic records originate from Scopus, Web of Science and IEEE Xplore and remain subject to the providers' terms.
