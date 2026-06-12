# SLR Protocol — Visual-Inertial Odometry for UAV Navigation

**Adaptive Models, Methods, and Accuracy Improvement**

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

Publication window: **January 2014 to search-execution date.** The 2014 lower bound reflects three field-defining events: the EuRoC MAV benchmark (collected 2014; Burri et al., 2016), optimisation-based real-time VIO (OKVIS; Leutenegger et al., 2015), and MAV-targeted real-time VO (SVO; Forster et al., 2014). Foundational pre-2014 work (PTAM, Klein & Murray, 2007; MonoSLAM, Davison et al., 2007; original MSCKF, Mourikis & Roumeliotis, 2007) is covered narratively in the Background section, not subjected to systematic inclusion.

## 4. Search Strategy

### Databases

| Database | Coverage Strength |
|----------|-------------------|
| Scopus (Elsevier) | Engineering, CS, robotics; broad interdisciplinary, advanced TITLE-ABS-KEY search |
| Web of Science (Clarivate) | Engineering, CS, applied sciences; high citation quality, IEEE/ACM proceedings |
| IEEE Xplore | IEEE journals, conferences, standards; primary robotics/aerospace/UAV venue |

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
| EXC-8 | Exclude | Full text not retrievable through any access channel after initial and supplementary retrieval rounds. |

## 6. Full-Text Triage

All three hard filters must be satisfied for a paper to be retained in the final synthesis.

| ID | Label | Rule |
|----|-------|------|
| T-1 | Algorithmic contribution | Presents or significantly extends a VIO algorithm. Applying an off-the-shelf system (e.g. VINS-Mono) unmodified fails this filter. |
| T-2 | Aerial validation | Validated on a UAV platform or aerial-collected dataset (EuRoC, TUM-VI MAV sequences, custom UAV flight). |
| T-3 | Quantitative evaluation | Reports ≥1 quantitative accuracy metric (ATE, RPE, RMSE, position error) against a prior method or baseline. Purely qualitative papers fail. |

**Relevance score** (0–1 per dimension, max 6) prioritises reading effort across: (1) GNSS-denied operation, (2) adaptive/online component, (3) real-time embedded/onboard execution, (4) EKF/filter-based fusion, (5) feature front-end (ORB, optical flow, keypoint quality), (6) auxiliary sensor fusion (barometer, rangefinder, UWB). Scores 4–6 = core corpus (deep extraction); 2–3 = targeted extraction; 0–1 = skim for RQ-specific relevance only.

## 7. Study Selection Process

SALSA-aligned (Grant & Booth, 2009): **Search** (execute queries, export to Zotero) → **Deduplication** (by DOI + title; keep most complete metadata) → **Screening** (title/abstract against INC/EXC; borderline cases retained) → **Full-text appraisal** (apply criteria, record exclusion reasons, reconcile by consensus). A PRISMA flow diagram documents counts at each stage.

## 8. Quality Assessment

Each included paper scored on five dimensions (0 = No, 0.5 = Partial, 1 = Yes). Papers below 2.0/5.0 are flagged for sensitivity analysis, not auto-excluded; scores reported in aggregate.

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

Reporting structure: Abstract → Introduction → Background → Methodology → Results (RQ1–RQ5) → Discussion → Conclusion & Future Work.

## 10. Data Extraction Template

One sheet per included article; fields marked (*) are mandatory.

| Field | Description / Possible Values |
|-------|------------------------------|
| Reference ID * | Unique identifier (e.g., P001) |
| Full citation * | Authors, year |
| Year * | Publication year |
| Venue * | Journal / conference, publisher |
| Country / Institution | First-author affiliation |
| VIO Architecture * | Loosely / tightly / semi-tightly coupled |
| Fusion Method * | EKF, UKF, ESKF, factor graph / iSAM, sliding-window optimisation, learning-based, hybrid |
| Visual Front-end * | Monocular, stereo, RGB-D, event camera |
| Features / Representation * | Point (FAST, ORB, SIFT), line, direct/semi-direct, deep features |
| IMU Preintegration | Yes/No; approach (Forster, Shen, etc.) |
| Adaptive / Online Component | Yes/No/Partial — adaptation type, trigger condition, online vs offline execution |
| UAV Platform * | Type and commercial model if named |
| Benchmark / Dataset * | EuRoC, KITTI, TUM-VI, custom; sequence names |
| Evaluation Metrics * | ATE, RTE, RPE, RMSE, computational load |
| Challenging Conditions Addressed | Low texture, fast motion, lighting, vibration, GPS-denied |
| Key Contribution * | Main technical claim or improvement |
| Limitations Stated | Authors' own limitations |
| QA Score (0–5) | Aggregate quality score |
| Relevant RQs * | RQ1–RQ5 primarily addressed |
| Reviewer Notes | Free text |

## 11. Limitations (threats to validity)

- **Search coverage** — three databases may miss grey literature, arXiv preprints, and workshops; mitigated by supplementary hand-search of ICRA, IROS, RAL.
- **Language** — English-only; non-English work may be missed.
- **Time restriction** — pre-2014 excluded; foundational work covered narratively.
- **Subjectivity in quality scoring** — mitigated by explicit criteria and researcher/supervisor cross-checking.

## 12. Final Execution Summary

Final PRISMA 2020 cascade, as reported in the manuscript (searches executed 2026-05-15; Scopus, Web of Science, IEEE Xplore):

| Stage | Count |
|-------|-------|
| Unique records after deduplication | 398 |
| Title/abstract screened | 398 |
| ├─ Retained for full-text retrieval | 232 |
| └─ Excluded at title/abstract | 166 |
| Full text retrieved (81 initial + 43 supplementary) | 124 |
| Excluded — full text unretrievable (EXC-8) | 108 |
| Excluded at full-text triage (T-1/T-2/T-3, INC-4) | 35 |
| **Final synthesis corpus** | **89** |

Full-text triage detail: of the 35 excluded, 32 failed T-1 (algorithmic contribution; 12 of these also failed T-3) and 3 were excluded under INC-4 (language) on full-text review.

Quality assessment: QA1–QA5 scored from full text for all 89 retained papers; mean QA total 4.24/5.0 (min 2.0, max 5.0); **zero** papers below the 2.0 sensitivity threshold.

> Note: the earlier protocol-stage snapshots (228-paper INCLUDE pool, C1–C7 thematic classes, interim 191/194 corpus figures) reflect the title/abstract-screening pipeline and were superseded by the full-text retrieval and triage reported in the final manuscript. The numbers above are authoritative.

## References

- Burri, M., et al. (2016). The EuRoC micro aerial vehicle datasets. *IJRR*, 35(10), 1157–1163. https://doi.org/10.1177/0278364915620033
- Davison, A. J., Reid, I. D., Molton, N. D., & Stasse, O. (2007). MonoSLAM: Real-time single camera SLAM. *IEEE TPAMI*, 29(6), 1052–1067. https://doi.org/10.1109/TPAMI.2007.1049
- Forster, C., Pizzoli, M., & Scaramuzza, D. (2014). SVO: Fast semi-direct monocular visual odometry. *ICRA 2014*, 15–22. https://doi.org/10.1109/ICRA.2014.6906584
- Grant, M. J., & Booth, A. (2009). A typology of reviews. *Health Info. & Libraries J.*, 26(2), 91–108. https://doi.org/10.1111/j.1471-1842.2009.00848.x
- Kitchenham, B., & Charters, S. (2007). Guidelines for performing systematic literature reviews in software engineering. EBSE Technical Report EBSE-2007-01.
- Klein, G., & Murray, D. (2007). Parallel tracking and mapping for small AR workspaces. *ISMAR 2007*, 225–234. https://doi.org/10.1109/ISMAR.2007.4538852
- Leutenegger, S., et al. (2015). Keyframe-based visual–inertial odometry using nonlinear optimization. *IJRR*, 34(3), 314–334. https://doi.org/10.1177/0278364914554813
- Mourikis, A. I., & Roumeliotis, S. I. (2007). A multi-state constraint Kalman filter for vision-aided inertial navigation. *ICRA 2007*, 3565–3572. https://doi.org/10.1109/ROBOT.2007.364024
- Sarkis-Onofre, R., et al. (2021). How to properly use the PRISMA statement. *Systematic Reviews*, 10(1), 1–3. https://doi.org/10.1186/s13643-021-01671-z
- Schardt, C., et al. (2007). Utilization of the PICO framework to improve searching PubMed for clinical questions. *BMC Med. Inform. Decis. Mak.*, 7(1), 1–6. https://doi.org/10.1186/1472-6947-7-16
