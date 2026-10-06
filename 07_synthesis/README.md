# 07_synthesis

Quantitative synthesis: the curated parametric classification, the figure generator, the PRISMA diagram source and the keyword probe behind Table 18.

| File | Content |
|------|---------|
| `parametric_tables.csv` | Curated category membership for the eight synthesis dimensions (`table`, `category`, `ref_numbers`). Counts and percentages are derived by the generator. Source of Tables 8, 9 and 11–16 of the paper. |
| `ref_id_matching.csv` | Paper id → manuscript citation number → DOI. The numbers are those printed in the paper, where references are numbered in order of first appearance, so the corpus numbers are not one contiguous block. |
| `prisma/build_prisma.py` | Writes `prisma/prisma_en.html` from the stage CSVs and renders `figures/fig1_prisma.png` (requires Playwright and Microsoft Edge) |
| `keyword_probe.py` | Full-text keyword probe for gaps G1 and G3 over the corpus PDFs. Writes `keyword_probe_results.csv`. |
| `generate_figures.py` | Rebuilds figures 2–6 from the stage CSVs and validates corpus size, reference numbering, class completeness and table coverage. |
| `figures/` | Generated PNGs: `fig1` PRISMA flow, `fig2` publication trend, `fig3` class-by-year heatmap, `fig4` architecture distribution, `fig5` adaptive-strategy taxonomy (horizontal bar chart of the six families), `fig6` corpus-to-gap map (G1-G5). |
| `prisma/` | PRISMA 2020 flow diagram. |

Run:

```
python3 generate_figures.py
```

The generator prints three notices that are expected: two studies fall under none of the three validation regimes, seven report none of the five tabulated metric categories, and two studies with an adaptive component fall in none of the six adaptive-strategy families.
