# 04_eligibility

Full-text triage of the 124 retrieved reports. `triage_worksheet.csv` records, per report: the thematic class (C1–C7), the three hard filters (`t1` algorithmic contribution, `t2` aerial validation, `t3` quantitative evaluation), the six relevance dimensions (`r1`–`r6`), the reading tier, the decision and the exclusion code.

38 reports were excluded at this stage: 32 failed T-1 (12 of these also failed T-3), 3 under the language criterion (INC-4), and 3 under EXC-9 (research of russian origin). The remaining 86 reports form the final synthesis corpus. Rows with `pdf_present = False` carry the abstract-level filter assessments of the unretrieved reports and are not part of the triage denominator.
