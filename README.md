# Adaptive VIO for UAV Navigation — SLR audit trail

Data, code, and decision trail for the systematic literature review *Adaptive Visual-Inertial Odometry Methods for UAV Navigation in GNSS-Denied Environments*, from database export to synthesis.

Each folder corresponds to one stage of the PRISMA 2020 flow.

| Folder | Stage | Content |
|--------|-------|---------|
| `00_protocol/` | A-priori protocol | Protocol document: criteria, PICO, T-filters, QA scheme |
| `01_identification/` | Identification | Raw database exports and the deduplicated record list |
| `02_screening/` | Screening | Title/abstract decisions for all 398 unique records |
| `03_retrieval/` | Retrieval | Retrieval status for the 230 sought reports |
| `04_eligibility/` | Eligibility | Full-text triage worksheet (T-filters, relevance scores) |
| `05_quality_assessment/` | Quality assessment | QA1–QA5 scores per retained paper |
| `06_data_extraction/` | Data extraction | 20-field extraction table plus recoded columns for the 123 included studies |
| `07_synthesis/` | Synthesis | Parametric tables, figure generator, PRISMA flow, keyword probe |

Full-text PDFs and the manuscript are not redistributed here for copyright reasons. The included studies are identified by DOI in `07_synthesis/ref_id_matching.csv`.

## Review protocol, as implemented

**Research questions.** RQ1 publication trends. RQ2 fusion architectures and visual front-ends. RQ3 adaptive and robust strategies. RQ4 datasets, platforms and evaluation metrics. RQ5 limitations and open research directions.

**Search.** Scopus, Web of Science Core Collection and IEEE Xplore were queried on 15 May 2026 with a PICO-derived expression combining visual-inertial odometry/navigation/fusion terms with UAV terms, restricted to articles and conference papers published 2014 or later. The exact query strings per database are given in Section 2.2 of the paper. The exports returned 648 records (Scopus 253, Web of Science 160, IEEE Xplore 235). Deduplication by DOI and normalised title left 398 unique records (250 duplicates removed).

**Screening.** Each record was screened on title and abstract against the five inclusion criteria of the protocol (visual-inertial fusion, UAV platform, peer-reviewed, English, 2014 or later) and its exclusion criteria (surveys, non-aerial platforms, pure GNSS work, vision-only or inertial-only pipelines, applications that consume VIO as a black box, and so on). 230 records were retained (224 clear includes and 6 uncertain records deferred to full text, following PRISMA guidance) and 168 were excluded, 12 of them under INC-4 for records whose venue and metadata show a non-English full text. Every record was screened independently by three researchers. Disagreements were resolved by discussion to a consensus decision, which is the decision recorded in `02_screening/screened.csv`.

**Retrieval.** Full texts of the 230 retained records were sought through institutional access, open-access repositories, publisher platforms and author requests in May 2026. 206 were obtained. 24 could not be retrieved through any channel and were excluded (EXC-8). `03_retrieval/retrieval_status.csv` records the outcome per report.

**Eligibility.** The 206 retrieved reports were read in full and assessed against three hard filters: 
T-1, the paper makes an algorithmic contribution to VIO rather than consuming it, 
T-2, the method is validated on aerial data, 
T-3, a quantitative evaluation is reported. 
Six binary relevance dimensions (GNSS-denied operation, adaptive component, real-time embedded operation, filter-based fusion, feature front-end, auxiliary sensor) were scored alongside. 83 reports were excluded: 66 failed T-1 (23 of which also failed T-3), 7 failed T-2, 5 failed T-3 alone, 2 under the language criterion (INC-4), and 3 under EXC-9 (reports from institutions of the Russian Federation, excluded in compliance with the Verkhovna Rada of Ukraine legislation of 1 December 2022, bill No. 7633). All three EXC-9 reports pass the scientific filters, and including them would raise the corpus to 126 without changing any conclusion of the review. The final synthesis corpus is **123 studies** (2015–2026). T-1 is applied with its explicit definition (a new VIO algorithm, or a multi-sensor estimator whose VIO measurement model, weighting or auxiliary-sensor integration is the contribution).

**Quality assessment.** Each retained paper was scored on the five items of Dybå and Dingsøyr (clear objective, experimental setup described, baseline comparison, limitations discussed, conclusions supported), each at 0 / 0.5 / 1.0. Mean total 4.12, minimum 2.5, maximum 5.0. No paper fell below the 2.0 sensitivity threshold.

**Extraction and synthesis.** A 20-field template (identification, architecture, front-end, adaptation, platform, evaluation, analysis) was applied to every included study, together with the recoded columns described in Section 10 of the protocol. The result is `06_data_extraction/extractions_full.csv`. The synthesis classifies the corpus along eight parametric dimensions: fusion architecture, visual front-end, auxiliary sensors, adaptive-strategy family, addressed conditions, platform type, validation regime, and evaluation metrics. The classification lives in `07_synthesis/parametric_tables.csv`, the single curated source for the paper's Tables 7–14 and the parametric figures.

**PRISMA flow.** 648 identified → 250 duplicates removed → 398 screened → 168 excluded → 230 sought → 24 not retrieved → 206 assessed → 83 excluded → 123 included. The rendered diagram is in `07_synthesis/prisma/`.

## Reproducing the figures

```
pip install matplotlib numpy
cd 07_synthesis
python3 generate_figures.py            # rebuilds all figures
python3 keyword_probe.py               # Table 16 probe (needs ../papers/*.pdf or --textdir)
python3 prisma/build_prisma.py         # Fig. 1 (PRISMA flow) from the stage CSVs, rendered with Edge
```

## License

Code and data files are released under the MIT License (see `LICENSE`). The bibliographic records originate from Scopus, Web of Science and IEEE Xplore and remain subject to the providers' terms.
