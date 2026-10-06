#!/usr/bin/env python3
"""Write prisma_en.html (PRISMA 2020 flow, Fig. 1) from the stage CSVs and render it to
../figures/fig1_prisma.png with the installed Edge (Playwright). The box texts are the
only part regenerated; the layout/CSS is the template below (unchanged from the
submitted figure). Usage: python build_prisma.py [--no-render]"""
from __future__ import annotations
import csv, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def load(rel):
    return list(csv.DictReader(open(ROOT / rel, encoding='utf-8-sig')))


scr = load('02_screening/screened.csv')
retr = load('03_retrieval/retrieval_status.csv')
tri = [r for r in load('04_eligibility/triage_worksheet.csv') if r['pdf_present'] == 'True']
n_screened = len(scr)
n_exc = sum(r['decision'] == 'EXCLUDE' for r in scr); n_inc4 = sum(r['decision'] == 'EXCLUDE' and r['triggered_criteria'].split('|')[0] == 'INC-4' for r in scr)   # primary criterion, as in the manuscript
n_sought = len(retr); n_miss = sum(r['pdf_retrieved'] != 'Y' for r in retr); n_assessed = n_sought - n_miss
exc = Counter(r['exclusion_code'] for r in tri if r['full_text_decision'] == 'EXCLUDE')
n_incl = sum(r['full_text_decision'] == 'INCLUDE' for r in tri)
pending = [r['id'] for r in tri if not r['full_text_decision']]
assert n_assessed == len(tri) and n_assessed - sum(exc.values()) == n_incl, f'triage incomplete: {len(pending)} retrieved reports without a decision {pending[:8]}'

html = (HERE / 'prisma_en.html').read_text(encoding='utf-8')


def setbox(old_pattern, new, count=1):
    global html
    html, k = re.subn(old_pattern, new, html, count=count, flags=re.S)
    assert k == count, old_pattern


# identification: the three database exports of the search
ident = {db_: len(load(f'01_identification/{db_}_export_09_2026.csv')) for db_ in ('scopus', 'wos', 'ieee')}
n_ident = sum(ident.values()); n_dup = n_ident - n_screened
LAB = {'scopus': 'Scopus', 'wos': 'Web of Science', 'ieee': 'IEEE Xplore'}
setbox(r'Scopus = \d+[^<]*<br>\s*Web of Science = \d+[^<]*<br>\s*IEEE Xplore = \d+[^<]*<br>\s*Total = \d+[^<]*',
       '<br>\n        '.join(f'{LAB[db_]} = {n}' for db_, n in ident.items()) + f'<br>\n        Total = {n_ident}')
setbox(r'Duplicate studies<br>\s*\(n = \d+\)', f'Duplicate studies<br> (n = {n_dup})')
setbox(r'Studies screened<br>\s*\(n = \d+\)', f'Studies screened<br>\n        (n = {n_screened})')
# the whole box is replaced (up to its </div>), so a re-run cannot append a second INC-4 line
setbox(r'Studies excluded<br>\s*\(n = \d+\).*?</div>', f'Studies excluded<br>\n        (n = {n_exc})<br>\n        of which INC-4 language (n = {n_inc4})</div>')
setbox(r'Studies sought for retrieval<br>\s*\(n = \d+\)', f'Studies sought for retrieval<br>\n        (n = {n_sought})')
setbox(r'Studies not retrieved<br>\s*EXC-8 \(n = \d+\)', f'Studies not retrieved<br>\n        EXC-8 (n = {n_miss})')
setbox(r'Studies assessed for eligibility<br>\s*\(n = \d+\)', f'Studies assessed for eligibility<br>\n        (n = {n_assessed})')
setbox(r'Studies excluded:<br>.*?</div>', 'Studies excluded:<br>\n        ' + '<br>\n        '.join(
    f'{lab} (n = {exc[code]})' for code, lab in [('T1', 'T-1'), ('T2', 'T-2'), ('T3', 'T-3'), ('INC-4', 'INC-4'), ('EXC-9', 'EXC-9')] if exc.get(code)) + '\n      </div>')
setbox(r'Studies included in review<br>\s*\(n = \d+\)', f'Studies included in review<br>\n        (n = {n_incl})')
(HERE / 'prisma_en.html').write_text(html, encoding='utf-8', newline='\n')
print(f'prisma_en.html: screened {n_screened}, excluded {n_exc} (INC-4 {n_inc4}), sought {n_sought}, not retrieved {n_miss}, assessed {n_assessed}, excluded {dict(exc)}, included {n_incl}')

if '--no-render' not in sys.argv:
    from playwright.sync_api import sync_playwright
    out = HERE.parent / 'figures' / 'fig1_prisma.png'
    with sync_playwright() as p:
        b = p.chromium.launch(channel='msedge')
        pg = b.new_page(viewport={'width': 620, 'height': 900}, device_scale_factor=2)
        pg.goto((HERE / 'prisma_en.html').as_uri())
        pg.locator('.prisma').screenshot(path=str(out))
        b.close()
    print('rendered', out)
