# 07_synthesis

Quantitative synthesis: the curated parametric classification, the figure generator, and the PRISMA and keyword-map assets.

| File | Content |
|------|---------|
| `parametric_tables.csv` | Curated category membership for the eight synthesis dimensions (`table`, `category`, `ref_numbers`, `count`). Single source for the paper's Tables 7–14 and the parametric figures; edit a row and re-run the generator to update everything consistently. |
| `ref_id_matching.csv` | Paper id → manuscript citation number (16–101) → DOI. This is also the DOI list of the 86 included studies. |
| `generate_figures.py` | Rebuilds all figures from the stage CSVs and validates corpus size and numbering on every run. `--audit` adds a keyword-classifier consistency check of the curated tables. |
| `keyword_map_section.md` | Narrative accompanying the keyword co-occurrence map. |
| `figures/` | Generated PNGs: `fig1` PRISMA flow, `fig2` publication trend, `fig3` class-by-year heatmap, `fig4` architecture distribution, `fig5` adaptive-strategy taxonomy, `fig6` maturity-to-gap matrix; VOSviewer keyword maps (Fig. 7 in the paper). |
| `prisma/` | PRISMA 2020 flow diagram (HTML source). |
| `vosviewer/` | VOSviewer project files for the keyword maps, including the thesaurus used for term consolidation. |

The trend and heatmap figures are computed directly from the stage CSVs. The architecture, taxonomy and gap-matrix figures are driven by `parametric_tables.csv`; percentages are recomputed against the live corpus size on every run.

Run:

```
python3 generate_figures.py
python3 generate_figures.py --audit
```
