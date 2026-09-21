# SLR Protocol — Visual-Inertial Odometry for UAV Navigation

A-priori protocol for the systematic literature review (SLR) on adaptive VIO for UAV navigation in GNSS-denied environments. Follows Kitchenham & Charters (2007) and the PRISMA 2020 reporting guidelines (Sarkis-Onofre et al., 2021).

## 1. Objectives

1. Characterise the current state and publication trends in VIO research for UAVs.
2. Identify algorithmic approaches and sensor fusion architectures reported in the literature.
3. Assess methods used to improve navigation accuracy under challenging conditions.
4. Survey benchmark datasets, evaluation metrics, and experimental platforms.
5. Identify open challenges and directions for future research.

## 2. Research Questions

| ID | Research Question |
|----|-------------------|
| RQ1 | What is the current state and publication trend in VIO research targeted at UAV navigation? |
| RQ2 | What sensor fusion architectures (loosely coupled, tightly coupled, factor-graph, filter-based, learning-based) and visual front-ends (monocular, stereo, event camera) are used in UAV VIO systems? |
| RQ3 | What algorithmic strategies — adaptive parameter tuning, mode switching, outlier rejection, learning-based components, sensor quality assessment — are proposed to improve VIO robustness and accuracy under GNSS-denied, low-texture, high-dynamics, or sensor-degraded conditions on UAVs? |
| RQ4 | What benchmark datasets, experimental platforms, and evaluation metrics are used to assess VIO performance on UAVs? |
| RQ5 | What limitations, failure modes, and open research directions are identified for UAV VIO, particularly regarding real-time operation on resource-constrained platforms and GNSS-denied environments? |

## 3. Scope & Time Horizon

Covers peer-reviewed publications reporting VIO systems, algorithms, or components where UAVs (quadrotors, multirotors, fixed-wing drones, micro aerial vehicles) are the target platform or a directly stated application. Ground-only, underwater, and legged-robot papers are excluded unless they explicitly address aerial adaptation.

Publication window: **January 2014 to search-execution date.**

## 4. Search Strategy

### Databases

| Database | Coverage Strength |
|----------|-------------------|
| Scopus (Elsevier) | Engineering, CS, robotics. Broad interdisciplinary coverage, advanced TITLE-ABS-KEY search |
| Web of Science (Clarivate) | Engineering, CS, applied sciences. High citation quality, IEEE/ACM proceedings |
| IEEE Xplore | IEEE journals, conferences, standards. Primary robotics/aerospace/UAV venue |

### PICO

Search terms were structured with the PICO framework (Schardt et al., 2007):

| Element | Terms |
|---------|-------|
| P — Population (platform) | "unmanned aerial vehicle" OR "UAV" |
| I — Intervention (technique) | "visual-inertial odometry" OR "visual inertial odometry" OR "visual-inertial navigation" OR "visual inertial navigation" OR "visual-inertial fusion" OR "visual inertial fusion" |
| C — Comparison | N/A (addressed within RQ3) |
| O — Outcome | Navigation accuracy, pose estimation, trajectory estimation, odometry error |

### Final query strings

**Scopus**
```
TITLE-ABS-KEY ( ( "visual-inertial odometry" OR "visual inertial odometry" OR "visual-inertial navigation" OR "visual inertial navigation" OR "visual-inertial fusion" OR "visual inertial fusion" ) AND ( "unmanned aerial vehicle" OR "UAV" ) ) AND PUBYEAR > 2013 AND ( LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "ar" ) )
```

**Web of Science**
```
TS=( ("visual-inertial odometry" OR "visual inertial odometry" OR "visual-inertial navigation" OR "visual inertial navigation" OR "visual-inertial fusion" OR "visual inertial fusion") AND ("unmanned aerial vehicle" OR "UAV" ) )
```

**IEEE Xplore**
```
((("All Metadata":"visual-inertial odometry" OR "All Metadata":"visual inertial odometry" OR "All Metadata":"visual-inertial navigation" OR "All Metadata":"visual inertial navigation") AND ("All Metadata":"UAV" OR "All Metadata":"unmanned aerial vehicle")))
```

## 5. Inclusion / Exclusion Criteria

| ID | Type | Criterion |
|----|------|-----------|
| INC-1 | Include | Reports a VIO system/method/component fusing both visual (camera) and inertial (IMU) data for pose/motion estimation. VO-only or INS-only do not qualify. |
| INC-2 | Include | Target platform is explicitly or strongly implicitly a UAV / drone / quadrotor / MAV / fixed-wing drone or equivalent aerial robot. |
| INC-3 | Include | Peer-reviewed (journal or conference). |
| INC-4 | Include | Written in English. |
| INC-5 | Include | Publication year 2014 or later. |
| EXC-1 | Exclude | Duplicate across databases (version with more citation data retained). |
| EXC-2 | Exclude | Addresses only ground, underwater, or legged robots without aerial application. |
| EXC-3 | Exclude | Visual odometry only (no IMU/inertial component). |
| EXC-4 | Exclude | Secondary study (review, survey, meta-analysis) — tracked separately for context. |
| EXC-5 | Exclude | Dataset paper with no algorithmic VIO contribution. |
| EXC-6 | Exclude | Abstract-only records or extended abstracts under 4 pages. |
| EXC-7 | Exclude | Focuses only on hardware design, sensor calibration, or communications, with VIO as a cited downstream application and no algorithmic contribution to VIO itself. |
| EXC-8 | Exclude | Full text not retrievable through any access channel. |
| EXC-9 | Exclude | Reports originating from institutions of the Russian Federation, in compliance with the legislative restriction adopted by the Verkhovna Rada of Ukraine on 1 December 2022 (bill No. 7633), see https://doi.org/10.1007/s10993-024-09697-4. |

## 6. Full-Text Triage

All three hard filters must be satisfied for a paper to be retained in the final synthesis.

| ID | Label | Rule |
|----|-------|------|
| T-1 | Algorithmic contribution | Presents or significantly extends a VIO algorithm, **or** a multi-sensor state estimator in which the VIO measurement model, its weighting, or its integration with auxiliary sensors is the contribution. Applying an off-the-shelf system (e.g. VINS-Mono) unmodified inside an application pipeline fails this filter. Studies retained under the second clause are marked as T-1 borderline in `04_eligibility/triage_worksheet.csv` (notes column). |
| T-2 | Aerial validation | Validated on a UAV platform or aerial-collected dataset (EuRoC, TUM-VI MAV sequences, custom UAV flight). |
| T-3 | Quantitative evaluation | Reports ≥1 quantitative accuracy metric (ATE, RPE, RMSE, position error) against a prior method or baseline. Purely qualitative papers fail. |

**Relevance score** (0–1 per dimension, max 6) prioritises reading effort across: (1) GNSS-denied operation, (2) adaptive/online component, (3) real-time embedded/onboard execution, (4) EKF/filter-based fusion, (5) feature front-end (ORB, optical flow, keypoint quality), (6) auxiliary sensor fusion (barometer, rangefinder, UWB).

## 7. Study Selection Process

SALSA-aligned (Grant & Booth, 2009): **Search** (execute queries, export to Zotero) → **Deduplication** (by DOI and title, keeping the most complete metadata) → **Screening** (title/abstract against INC/EXC, borderline cases retained) → **Full-text appraisal** (apply criteria, record exclusion reasons, reconcile by consensus). A PRISMA flow diagram documents counts at each stage.

## 8. Quality Assessment

Each included paper scored on five dimensions (0 = No, 0.5 = Partial, 1 = Yes). Papers below 2.0/5.0 are flagged for sensitivity analysis, not auto-excluded. Scores are reported in aggregate.

| Item | Question |
|------|----------|
| QA1 | Is the research objective or hypothesis clearly stated? |
| QA2 | Is the experimental setup (platform, dataset, metrics) clearly described? |
| QA3 | Are results compared against ≥1 baseline or state-of-the-art method? |
| QA4 | Are the limitations of the proposed approach discussed? |
| QA5 | Are conclusions supported by the presented experimental evidence? |

## 9. Synthesis & Reporting

Narrative synthesis (primary), supplemented by frequency analysis and thematic mapping:

- **RQ1** — descriptive statistics and publication-trend charts.
- **RQ2** — taxonomy table of VIO architectures mapped to representative papers.
- **RQ3** — thematic analysis of robustness/accuracy strategies, classified into sensor-, algorithmic-, and system-level adaptations.
- **RQ4** — summary table of benchmarks, metrics, and platform configurations.
- **RQ5** — structured gap analysis linking limitations to future directions.

Primary thematic classes: C1 multi-sensor fusion, C2 adaptive / robust estimation, C3 initialisation, scale and observability, C4 evaluation / benchmark studies (primary studies whose contribution is a comparison or evaluation, while secondary surveys remain excluded under EXC-4), C5 auxiliary modality (thermal, event, ToF, UWB, altimeter), C6 integrated system / application, C7 front-end / feature processing.

Classification policy: each study is assigned one primary thematic class (C1–C7) for the publication-trend and class-by-year analyses, whereas membership across the eight parametric dimensions is multi-label — a study may fall in several rows (e.g., a hybrid architecture, or a method addressing several flight conditions), so the parametric row shares need not sum to 100%. Treating publications as multi-level, multi-category objects follows the multi-level classification approach of Turkin et al. (2025).

Reporting structure: Abstract → Introduction → Background → Methodology → Results (RQ1–RQ5) → Discussion → Conclusion & Future Work.

## 10. Data Extraction Template

One row per included article in `06_data_extraction/extractions_full.csv`. Fields marked (*) are mandatory.

| Field (column) | Description / Possible Values |
|-------|------------------------------|
| Reference ID * (`reference_id`) | Unique identifier (P0001 ...) |
| Full citation * (`authors_year`) | Authors, year |
| Year * (`year`) | Publication year |
| Venue * (`venue`), DOI (`doi`) | Journal / conference, publisher, and the DOI |
| Country / Institution (`country_institution`) | First-author affiliation |
| Thematic class (`class_id`), relevance score (`relevance_score`), QA total (`qa_total`) | C1–C7 primary class, sum of R1–R6, QA1–QA5 total (0–5) |
| VIO Architecture * (`vio_architecture`) | Loosely / tightly / semi-tightly coupled |
| Fusion Method * (`fusion_method`) | EKF, UKF, ESKF, MSCKF, factor graph / iSAM, sliding-window optimisation, learning-based, hybrid |
| Visual Front-end * (`visual_frontend`) | Monocular, stereo, RGB-D / ToF, thermal, event camera |
| Features / Representation * (`features_representation`) | Point (FAST, ORB, SIFT), line, direct/semi-direct, dense, learned features |
| IMU Preintegration (`imu_preintegration`) | Yes/No and the approach (Forster, Shen, etc.) |
| Adaptive / Online Component (`adaptive_online`) | Yes/No/Partial — adaptation type, trigger condition, online vs offline execution |
| UAV Platform * (`uav_platform`) | Type and commercial model if named |
| Benchmark / Dataset * (`benchmark_dataset`) | EuRoC, KITTI, TUM-VI, custom, with sequence names |
| Evaluation Metrics * (`evaluation_metrics`) | ATE, RTE, RPE, RMSE, computational load |
| Challenging Conditions Addressed (`challenging_conditions`) | Low texture, fast motion, lighting, vibration, GNSS-denied |
| Key Contribution * (`key_contribution`) | Main technical claim or improvement |
| Limitations Stated (`limitations_stated`) | Authors' own limitations |
| Relevant RQs * (`relevant_rqs`) | RQ1–RQ5 primarily addressed |
| Reviewer Notes (`reviewer_notes`) | Free text |
| Auxiliary sensors (`aux_sensors`, `aux_measurement_models`, `aux_fusion_weight`, `aux_evidence`) | Sensors fused with the camera+IMU estimator, their measurement-model class (absolute pressure altitude, range to ground, range to anchor, absolute 3-D position, relative pose, heading) and fusion weight (fixed, adaptive with the driving signal named, threshold switch, not stated). Basis of Table 9 |
| Height channel (`height_channel`, `height_channel_weighting`) | yes/no, weighting as above. Basis of gap G3 |
| Front-end representation (`frontend_type`, `point_features`, `frontend_evidence`) | Multi-label: descriptor point features, optical-flow-tracked corners, point features (tracker not stated), direct / photometric, semi-direct, dense, point-line, learned end-to-end, event-based, consumed pose stream, not stated. `point_features` = yes for the first three and point-line |
| Per-keypoint quality scoring (`per_keypoint_quality_scoring`, `quality_scoring_evidence`) | yes / frame-level / motion-state / no. Basis of gap G1 |
| Limitation codes (`limitation_codes`, `limitation_evidence`) | L1 computational cost, L2 visual degradation, L3 long-term drift, L4 monocular scale, L5 dynamic scenes, or `none stated`. Counted only when stated by the authors as a limitation of their own method. Basis of Table 15 |
| Recoding notes (`recode_notes`) | Free text on the recoded columns |

## 11. Limitations (threats to validity)

- **Language** — English-only, so non-English work may be missed.
- **Time restriction** — pre-2014 excluded.
- **Subjectivity in quality scoring** — mitigated by explicit criteria and researchers cross-checking.

## 12. Final Execution Summary

Final PRISMA 2020 cascade, as reported in the manuscript (searches executed 2026-05-15 in Scopus, Web of Science and IEEE Xplore):

| Stage | Count |
|-------|-------|
| Unique records after deduplication | 398 |
| Title/abstract screened | 398 |
| ├─ Retained for full-text retrieval | 230 |
| └─ Excluded at title/abstract | 168 (12 under INC-4) |
| Full text retrieved | 206 |
| Excluded — full text unretrievable (EXC-8) | 24 |
| Excluded at full-text triage (T-1/T-2/T-3, INC-4, EXC-9) | 83 |
| **Final synthesis corpus** | **123** |

Full-text triage detail: of the 83 excluded, 66 failed T-1 (algorithmic contribution, 23 of these also failed T-3), 7 failed T-2, 5 failed T-3 alone, 2 were excluded under INC-4 (language), and 3 under EXC-9 (institutional origin). All three EXC-9 reports pass T-1/T-2/T-3, and including them would raise the corpus to 126 without changing any conclusion of the review.

Quality assessment: QA1–QA5 scored from full text for the 123 synthesised papers, mean QA total 4.12/5.0 (min 2.5, max 5.0), and **zero** papers below the 2.0 sensitivity threshold.

## References

- Burri, M., et al. (2016). The EuRoC micro aerial vehicle datasets. *IJRR*, 35(10), 1157–1163. https://doi.org/10.1177/0278364915620033
- Davison, A. J., Reid, I. D., Molton, N. D., & Stasse, O. (2007). MonoSLAM: Real-time single camera SLAM. *IEEE TPAMI*, 29(6), 1052–1067. https://doi.org/10.1109/TPAMI.2007.1049
- Forster, C., Pizzoli, M., & Scaramuzza, D. (2014). SVO: Fast semi-direct monocular visual odometry. *ICRA 2014*, 15–22. https://doi.org/10.1109/ICRA.2014.6906584
- Grant, M. J., & Booth, A. (2009). A typology of reviews. *Health Info. & Libraries J.*, 26(2), 91–108. https://doi.org/10.1111/j.1471-1842.2009.00848.x
- Kitchenham, B., & Charters, S. (2007). Guidelines for performing systematic literature reviews in software engineering. EBSE Technical Report EBSE-2007-01.
- Klein, G., & Murray, D. (2007). Parallel tracking and mapping for small AR workspaces. *ISMAR 2007*, 225–234. https://doi.org/10.1109/ISMAR.2007.4538852
- Leutenegger, S., et al. (2015). Keyframe-based visual–inertial odometry using nonlinear optimization. *IJRR*, 34(3), 314–334. https://doi.org/10.1177/0278364914554813
- Liubimov, O., & Liubimov, M. (2023). Use of open-source COTS/MOTS hardware and software platforms for the build up of the CubeSat nanosatellites. *Journal of Rocket-Space Technology*, 31(4), 138–147. https://doi.org/10.15421/452318
- Liubimov, O., & Turkin, I. (2025). CubeSats and their on-board computers: A systematic literature review. *Space Science and Technology*, 31(6), 14–37. https://doi.org/10.15407/knit2025.06.014
- Mourikis, A. I., & Roumeliotis, S. I. (2007). A multi-state constraint Kalman filter for vision-aided inertial navigation. *ICRA 2007*, 3565–3572. https://doi.org/10.1109/ROBOT.2007.364024
- Sarkis-Onofre, R., et al. (2021). How to properly use the PRISMA statement. *Systematic Reviews*, 10(1), 1–3. https://doi.org/10.1186/s13643-021-01671-z
- Schardt, C., et al. (2007). Utilization of the PICO framework to improve searching PubMed for clinical questions. *BMC Med. Inform. Decis. Mak.*, 7(1), 1–6. https://doi.org/10.1186/1472-6947-7-16
- Turkin, I., Chukhray, A., Liubimov, O., & Volobuieva, L. (2025). A distance-metric approach to expert agreement in multi-level publications classification. *CEUR Workshop Proceedings*, 4164, paper 12. https://ceur-ws.org/Vol-4164/paper12.pdf
