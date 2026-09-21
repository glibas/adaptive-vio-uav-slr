#!/usr/bin/env python3
"""Corpus-level keyword probe for the research gaps (manuscript Table 16).

Searches the full text of every included study for the defining terms of each
probed gap and writes keyword_probe_results.csv (one row per paper and gap,
with per-term hit counts) plus a summary to stdout.

Full texts are read from ../papers/<id>.pdf (not redistributed); pass
--textdir DIR to use pre-extracted <id>.txt files instead.
"""
from __future__ import annotations
import argparse, csv, re, sys
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent.parent
OUT = Path(__file__).parent / 'keyword_probe_results.csv'

PROBES = {
    'G1': ['descriptor quality', 'keypoint quality', 'per-keypoint', 'per keypoint', 'per-feature weight',
           'per-feature weighting', 'match confidence', 'descriptor uniqueness', 'keypoint confidence',
           'feature quality', 'feature reliability', 'feature confidence', 'feature score'],
    'G3': ['adaptive barometer', 'barometric covariance', 'quality-weighted', 'quality weighted',
           'adaptive altitude', 'barometer noise', 'adaptive height', 'barometer', 'barometric',
           'altimeter', 'height sensor', 'altitude sensor'],
}
# terms that indicate presence of the channel rather than adaptive weighting of it
PRESENCE = {'G3': ['barometer', 'barometric', 'altimeter', 'height sensor', 'altitude sensor'],
            'G1': ['feature quality', 'feature reliability', 'feature confidence', 'feature score']}


def read_text(pid, textdir):
    if textdir:
        p = Path(textdir) / f'{pid}.txt'
        return p.read_text(encoding='utf-8', errors='replace') if p.exists() else None
    p = BASE / 'papers' / f'{pid}.pdf'
    if not p.exists():
        return None
    import fitz
    return '\n'.join(pg.get_text() for pg in fitz.open(p))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--textdir'); a = ap.parse_args()
    refs = {r['id']: int(r['ref_number']) for r in csv.DictReader(open(BASE / '07_synthesis/ref_id_matching.csv'))}
    rows, missing = [], []
    summary = defaultdict(lambda: {'any': set(), 'presence': set(), 'adaptive_terms': set()})
    for pid, n in sorted(refs.items(), key=lambda x: x[1]):
        t = read_text(pid, a.textdir)
        if t is None:
            missing.append(pid); continue
        low = re.sub(r'\s+', ' ', t.lower())
        for gap, terms in PROBES.items():
            hits = {term: low.count(term) for term in terms}
            row = {'id': pid, 'ref_number': n, 'gap': gap}
            row.update({f'hit:{k}': v for k, v in hits.items()})
            row['total_hits'] = sum(hits.values())
            rows.append(row)
            if row['total_hits']:
                summary[gap]['any'].add(n)
            if any(hits[k] for k in PRESENCE[gap]):
                summary[gap]['presence'].add(n)
            spec = [k for k in terms if k not in PRESENCE[gap] and hits[k]]
            if spec:
                summary[gap]['adaptive_terms'].add(n)
    fields = ['id', 'ref_number', 'gap'] + sorted({k for r in rows for k in r if k.startswith('hit:')}) + ['total_hits']
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    N = len(refs) - len(missing)
    print(f'probed {N} of {len(refs)} studies; missing full text: {missing}')
    for gap in PROBES:
        s = summary[gap]
        print(f'\n{gap}: any term {len(s["any"])}/{N}; generic presence terms {len(s["presence"])}/{N} '
              f'{sorted(s["presence"])}; gap-specific terms {len(s["adaptive_terms"])}/{N} {sorted(s["adaptive_terms"])}')
    print(f'\nwrote {OUT}')


if __name__ == '__main__':
    main()
