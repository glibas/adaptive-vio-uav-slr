# 07_synthesis

Quantitative synthesis: the curated parametric classification, the figure generator, and the PRISMA and keyword-map assets.

| File | Content |
|------|---------|
| `parametric_tables.csv` | Curated category membership for the seven synthesis dimensions (`table`, `category`, `ref_numbers`, `count`). Single source for the paper's Tables 6–12 and the parametric figures; edit a row and re-run the generator to update everything consistently. |
| `ref_id_matching.csv` | Paper id → manuscript citation number (11–99) → DOI. This is also the DOI list of the 89 included studies. |
| `generate_figures.py` | Rebuilds all figures from the stage CSVs and validates corpus size and numbering on every run. `--audit` adds a keyword-classifier consistency check of the curated tables. |
| `palette.py` | Colour palettes used by the generator (greyscale- and CVD-safe). |
| `keyword_map_section.md` | Narrative accompanying the keyword co-occurrence map. |
| `figures/` | Generated PNGs. `fig1` publication trend, `fig2` architecture distribution, `fig3` class-by-year heatmap, `fig4` keyword maps (VOSviewer), `fig8` adaptive-strategy taxonomy, `fig9` maturity-to-gap matrix. |
| `prisma/` | PRISMA 2020 flow diagram (HTML source). |
| `vosviewer/` | VOSviewer project files for the keyword maps, including the thesaurus used for term consolidation. |

The trend and heatmap figures are computed directly from the stage CSVs. The architecture, taxonomy and gap-matrix figures are driven by `parametric_tables.csv`; percentages are recomputed against the live corpus size, and the gap-matrix exemplar cells are anchored by paper ids so that reference renumbering cannot corrupt them.

Run:

```
python3 generate_figures.py
python3 generate_figures.py --audit
```
