# 04_eligibility

Full-text triage of the 124 retrieved reports. `triage_worksheet.csv` records, per report: the thematic class (C1–C7), the three hard filters (`t1` algorithmic contribution, `t2` aerial validation, `t3` quantitative evaluation), the six relevance dimensions (`r1`–`r6`), the reading tier, the decision and the exclusion code.

35 reports were excluded at this stage: 32 failed T-1 (12 of these also failed T-3) and 3 were excluded under the language criterion (INC-4). The remaining 89 reports form the review corpus. Rows with `pdf_present = False` carry the abstract-level filter assessments of the unretrieved reports and are not part of the triage denominator.
