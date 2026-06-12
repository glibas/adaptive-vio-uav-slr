#!/usr/bin/env python3
"""Generate the synthesis figures from the stage CSV files."""
from __future__ import annotations
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np


BASE = Path(__file__).parent.parent
FIG_DIR = Path(__file__).parent / 'figures'
FIG_DIR.mkdir(exist_ok=True)

REF_OFFSET = 0

# Fonts are scaled so labels render at body size after the figure is shrunk
# to column width; Times New Roman with a metric-identical serif fallback.
BODY_PT = 14          # target on-page text size (matches the manuscript body)
DISPLAY_W_IN = 6.69   # width each figure is displayed at in the .docx (column width)
_FS = BODY_PT         # current working size; updated per figure by _fit_fonts()
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'custom', 'mathtext.rm': 'Times New Roman',
    'figure.dpi': 150, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
})


def _fit_fonts(fig_width_in):
    """Scale fonts so text lands at BODY_PT after shrinking to column width."""
    global _FS
    _FS = BODY_PT * fig_width_in / DISPLAY_W_IN
    plt.rcParams.update({
        'font.size': _FS, 'axes.titlesize': _FS, 'axes.labelsize': _FS,
        'xtick.labelsize': _FS, 'ytick.labelsize': _FS, 'legend.fontsize': _FS,
        'figure.titlesize': _FS,
    })

# Okabe-Ito colour-blind-safe palette
OI_BLACK = '#000000'; OI_ORANGE = '#E69F00'; OI_SKYBLUE = '#56B4E9'
OI_GREEN = '#009E73'; OI_YELLOW = '#F0E442'; OI_BLUE = '#0072B2'
OI_VERMILLION = '#D55E00'; OI_PURPLE = '#CC79A7'; OI_GREY = '#999999'
QUAL = [OI_BLUE, OI_ORANGE, OI_GREEN, OI_PURPLE, OI_SKYBLUE, OI_VERMILLION]
SEQ_HEAT = ['white', '#cfe6f5', OI_SKYBLUE, OI_BLUE]
ACCENT = OI_BLUE
FILTER_C = OI_BLUE
FEATURE_C = OI_VERMILLION
FULL = OI_GREEN
PART = OI_ORANGE
NONE_C = OI_GREY
GAP = OI_VERMILLION


def load_csv(path):
    with open(BASE / path, encoding='utf-8') as f:
        return list(csv.DictReader(f))


retrieval = load_csv('03_retrieval/retrieval_status.csv')
CORPUS = {r['id'] for r in retrieval if r.get('in_final_corpus') == 'Y'}
N = len(CORPUS)

refnum = {r['id']: int(r['ref_number']) + REF_OFFSET
          for r in load_csv('07_synthesis/ref_id_matching.csv')
          if r['ref_number'].strip().isdigit()}

def _load_ext():
    rows = load_csv('06_data_extraction/extractions_full.csv')
    if rows:
        return {r['reference_id']: r for r in rows if r.get('reference_id') in CORPUS}
    # fall back to the triage worksheet when the extraction sheet is empty
    return {r['id']: {'year': r.get('year', ''), 'class_id': r.get('class_id', '')}
            for r in load_csv('04_eligibility/triage_worksheet.csv') if r.get('id') in CORPUS}

ext = _load_ext()

screened = load_csv('02_screening/screened.csv')


def load_parametric():
    tables = defaultdict(list)
    for row in load_csv('07_synthesis/parametric_tables.csv'):
        refs = sorted(int(x) for x in row['ref_numbers'].split())
        tables[row['table']].append({'label': row['category'], 'refs': refs,
                                     'n': len(refs), 'pct': 100 * len(refs) / N})
    return tables

PARAM = load_parametric()


def get(table_key, contains):
    """First curated row of a table whose label contains `contains`."""
    for r in PARAM[table_key]:
        if contains.lower() in r['label'].lower():
            return r
    return {'label': contains, 'refs': [], 'n': 0, 'pct': 0.0}


def compress(nums):
    nums = sorted(set(nums))
    if not nums:
        return '[—]'
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        # Dash only for runs of 3+ consecutive numbers; a pair is comma-separated.
        if j - i >= 2:
            out.append(f'{nums[i]}–{nums[j]}')
        else:
            out.extend(str(nums[k]) for k in range(i, j + 1))
        i = j + 1
    return '[' + ', '.join(out) + ']'


def refs_label(refs, cap=7):
    if not refs:
        return '[—]'
    return compress(refs[:cap])[:-1] + ', …]' if len(refs) > cap else compress(refs[:cap])


# Figure 2: publication trend
def fig_trend():
    pool = [r for r in screened if r.get('decision') in ('INCLUDE', 'UNCERTAIN')]
    sy = Counter(r.get('year', '') for r in pool)
    ry = Counter(ext[i].get('year', '') for i in ext)
    years = sorted(y for y in (set(sy) | set(ry)) if y.isdigit())
    s = [sy.get(y, 0) for y in years]
    rc = [ry.get(y, 0) for y in years]
    x = np.arange(len(years)); w = 0.38
    _fit_fonts(9)
    fig, ax = plt.subplots(figsize=(9, 4.8))
    _seq_blue = [OI_SKYBLUE, OI_SKYBLUE, OI_BLUE]
    bs = ax.bar(x - w/2, s, w, color=_seq_blue[0], edgecolor='white',
                label=f'Screened pool (n = {len(pool)})')
    br = ax.bar(x + w/2, rc, w, color=ACCENT, edgecolor='white',
                label=f'Retained corpus (n = {N})')
    ax.set_xticks(x); ax.set_xticklabels(years, rotation=45, ha='right')
    ax.set_xlabel('Year of publication'); ax.set_ylabel('Number of articles per year')
    ax.set_ylim(0, max(max(s), max(rc)) * 1.2)
    ax.legend(loc='upper left', frameon=False)
    ax.grid(axis='y', linestyle=':', alpha=0.5)
    for bars, vals, col in [(bs, s, _seq_blue[2]), (br, rc, ACCENT)]:
        for b, c in zip(bars, vals):
            if c:
                ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.6, str(c),
                        ha='center', va='bottom', fontsize=_FS, color=col)
    fig.tight_layout(); fig.savefig(FIG_DIR / 'fig2_publication_trend.png'); plt.close(fig)
    print('Wrote fig2_publication_trend.png')


# Figure 4: architecture
def fig_architecture():
    rows = PARAM['architecture']
    short = ['Filter-based\n(EKF / ESKF / IEKF\n/ ESIKF / UKF / MSCKF)',
             'Optimisation-based\n(sliding window /\nfactor graph / iSAM)',
             'Learning-based /\nNeural-augmented',
             'Collaborative /\nDistributed multi-UAV']
    counts = [r['n'] for r in rows]; pcts = [r['pct'] for r in rows]
    _fit_fonts(8)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    colours = QUAL[:len(rows)]
    bars = ax.barh(short[:len(rows)], counts, color=colours, edgecolor='white')
    ax.set_xlabel('Number of articles'); ax.set_xlim(0, max(counts) * 1.45)
    for b, c, p in zip(bars, counts, pcts):
        ax.text(b.get_width() + 0.4, b.get_y() + b.get_height()/2, f'{c}   ({p:.1f} %)',
                va='center', fontsize=_FS)
    ax.invert_yaxis(); ax.grid(axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout(); fig.savefig(FIG_DIR / 'fig4_architecture.png'); plt.close(fig)
    print('Wrote fig4_architecture.png')


# Figure 3: class-by-year heatmap
def fig_class_year():
    classes = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
    labels = ['C1 Multi-sensor fusion', 'C2 Adaptive / robust', 'C3 Initialisation /\n    robustness',
              'C4 Survey / benchmark', 'C5 Auxiliary modality', 'C6 System / application',
              'C7 Front-end / feature']
    yc = defaultdict(lambda: defaultdict(int))
    for r in ext.values():
        y, c = r.get('year', ''), r.get('class_id', '')
        if y.isdigit() and c in classes:
            yc[y][c] += 1
    years = sorted(yc)
    M = np.array([[yc[y][c] for y in years] for c in classes])
    _fit_fonts(9)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    _stops = SEQ_HEAT
    from matplotlib.colors import LinearSegmentedColormap
    _cmap = LinearSegmentedColormap.from_list('seq_blue_w', _stops, N=256)
    im = ax.imshow(M, cmap=_cmap, aspect='auto', vmin=0)
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years, rotation=45, ha='right')
    ax.set_yticks(range(len(classes))); ax.set_yticklabels(labels)
    ax.set_xlabel('Year of publication')
    for i in range(len(classes)):
        for j in range(len(years)):
            v = M[i, j]
            if v:
                ax.text(j, i, int(v), ha='center', va='center', fontsize=_FS,
                        color='white' if v > M.max() * 0.55 else 'black')
    cb = plt.colorbar(im, ax=ax, shrink=0.8); cb.set_label('Articles per cell')
    fig.tight_layout(); fig.savefig(FIG_DIR / 'fig3_class_year_heatmap.png'); plt.close(fig)
    print('Wrote fig3_class_year_heatmap.png')


# Figure 5: adaptive-strategy taxonomy
def fig_adaptive_taxonomy():
    rows = sorted(PARAM['adaptive'], key=lambda r: r['n'], reverse=True)
    _fit_fonts(11)
    fig, ax = plt.subplots(figsize=(11, 6.8))
    n = len(rows); ys = list(range(n))[::-1]
    maxc = max(r['n'] for r in rows) if rows else 1
    for y, r in zip(ys, rows):
        feature_level = 'feature-quality' in r['label'].lower()
        col = FEATURE_C if feature_level else FILTER_C
        ax.barh(y, r['n'], color=col, edgecolor='white', height=0.62, zorder=3)
        ax.text(r['n'] + 0.12, y, f"{r['n']}   {refs_label(r['refs'], cap=5)}", va='center',
                ha='left', fontsize=_FS, color='#222')
        short = r['label'].replace(' / ', ' /\n').replace(' tuning', '').replace(' assessment', '')
        ax.text(-0.15, y, short, va='center', ha='right', fontsize=_FS)
    ax.set_xlim(0, maxc + 11); ax.set_ylim(-0.6, n - 0.4)
    ax.set_yticks([]); ax.set_xlabel('Number of papers')
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    ax.grid(axis='x', linestyle=':', alpha=0.5)
    h1 = Rectangle((0, 0), 1, 1, color=FILTER_C); h2 = Rectangle((0, 0), 1, 1, color=FEATURE_C)
    ax.legend([h1, h2], ['Filter-/estimator-level adaptation',
                         'Feature-level adaptation'],
              loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False, fontsize=_FS)
    fig.tight_layout(); fig.savefig(FIG_DIR / 'fig5_adaptive_taxonomy.png'); plt.close(fig)
    print('Wrote fig5_adaptive_taxonomy.png')


# Figure 6: gap matrix
def fig_gap_matrix():
    # Established -> Intermediate -> Open gap, one row per capability dimension.
    matrix = [
        ('Visual-quality\nweighting',
         [('Point feat.\n+ RANSAC', 'full'), ('Frame IQA /\nmotion-state', 'part'),
          ('Per-keypoint\nscoring\nG1', 'gap')]),
        ('Learning\nhybrid',
         [('End-to-end\ndeep VIO', 'full'), ('Learned\nfront-ends', 'part'),
          ('On-autopilot\nML, no GPU\nG2', 'gap')]),
        ('Height /\naux fusion',
         [('IMU preint.\n+ scale', 'full'), ('Fixed-weight\nbaro / UWB', 'part'),
          ('Adaptive\nquality-wtd.\nG3', 'gap')]),
        ('Robustness /\nmode switching',
         [('M-estimator\n/ chi-sq.', 'full'), ('Temporal\ncalibration', 'part'),
          ('Multi-criterion\nswitching\nG4', 'gap')]),
        ('Evaluation\ncoverage',
         [('Handheld /\nKITTI, TUM', 'full'), ('EuRoC /\nVIODE sim.', 'part'),
          ('Long GNSS-\ndenied\nG5', 'gap')]),
        ('Fault\ntolerance',
         [('State\nstabilization', 'full'), ('Visual-degrade\nrobustness', 'part'),
          ('Actuator-fault\ntolerance\nG6', 'gap')]),
    ]
    head = ['Established', 'Intermediate', 'Open gap']
    scol = {'full': FULL, 'part': PART, 'none': NONE_C, 'gap': GAP}
    _fit_fonts(DISPLAY_W_IN)
    fig, ax = plt.subplots(figsize=(DISPLAY_W_IN, 6.5))
    nr = len(matrix); cw, ch, gx, gy = 2.05, 1.0, 0.12, 0.22
    px, py = cw + gx, ch + gy; top = nr * py
    for c in range(3):
        ax.text(c * px + cw/2, top + 0.12, head[c], ha='center', va='bottom',
                fontsize=_FS, color='#333')
    for ridx, (dim, cells) in enumerate(matrix):
        yrow = (nr - 1 - ridx) * py
        ax.text(-0.24, yrow + ch/2, dim, ha='right', va='center', fontsize=_FS)
        for c, (text, status) in enumerate(cells):
            x = c * px
            ax.add_patch(Rectangle((x, yrow), cw, ch,
                         linewidth=(1.4 if status == 'gap' else 0.6),
                         edgecolor=('#7d1f2b' if status == 'gap' else 'white'),
                         facecolor=scol[status], zorder=2))
            tcol = 'white' if status in ('full', 'gap') else ('black' if status == 'part' else '#9aa3ad')
            ax.text(x + cw/2, yrow + ch/2, text, ha='center', va='center',
                    fontsize=_FS, color=tcol, zorder=3, linespacing=1.2)
    ax.set_xlim(-2.25, 3 * px + 0.05); ax.set_ylim(-0.10, top + 0.85); ax.axis('off')
    leg = [mpatches.Patch(color=FULL, label='Established in corpus'),
           mpatches.Patch(color=PART, label='Current intermediate frontier'),
           mpatches.Patch(color=GAP, label='Open research gap (G1\u2013G6)')]
    ax.legend(handles=leg, loc='upper center', bbox_to_anchor=(0.5, -0.01), ncol=2,
              frameon=False, fontsize=_FS, handlelength=1.1)
    fig.tight_layout(); fig.savefig(FIG_DIR / 'fig6_gap_matrix.png'); plt.close(fig)
    print('Wrote fig6_gap_matrix.png')


def validate():
    print('\n=== VALIDATION ===')
    ok = True
    valid_nums = set(refnum.values())
    missing = sorted(CORPUS - set(refnum))
    if missing:
        ok = False; print(f'  ERROR: corpus papers with no ref number: {missing}')
    extra = sorted(set(refnum) - CORPUS)
    if extra:
        ok = False; print(f'  ERROR: ref_id_matching has non-corpus ids: {extra}')
    nums = sorted(refnum.values())
    if len(nums) != len(set(nums)):
        ok = False; print('  ERROR: duplicate manuscript ref numbers')
    print(f'  corpus N = {N}; ref numbers {min(nums)}..{max(nums)} ({len(nums)} unique)')
    for key, rows in PARAM.items():
        for r in rows:
            bad = [x for x in r['refs'] if x not in valid_nums]
            if bad:
                ok = False
                print(f'  ERROR: {key}/{r["label"][:30]} cites non-corpus refs {bad}')
    print('  RESULT:', 'PASS' if ok else 'FAIL')
    return ok


def print_summary():
    print('\n=== PARAMETRIC TABLES (curated; pct vs live N=%d) ===' % N)
    for key, rows in PARAM.items():
        print(f'\n{key}')
        for r in rows:
            print(f'  {r["n"]:3d}  {r["pct"]:5.1f}%  {r["label"][:44]:46} {refs_label(r["refs"])}')


def audit():
    def blob(r, fields):
        return ' '.join(r.get(f, '') for f in fields).lower()

    def arch(r):
        t = blob(r, ['vio_architecture', 'fusion_method']); o = set()
        if re.search(r'\b(ekf|eskf|iekf|esikf|liekf|ukf|msckf|kalman|filter-based|error-state)\b', t):
            o.add('Filter-based')
        if any(k in t for k in ['optimi', 'sliding window', 'sliding-window', 'factor graph',
                                'factor-graph', 'bundle adjustment', 'smoother', 'isam', 'pose graph']):
            o.add('Optimization-based')
        if any(k in t for k in ['learning', 'neural', 'lstm', 'cnn', ' deep', 'gan', 'gru', 'network']):
            o.add('Learning-based')
        if any(k in t for k in ['collaborative', 'distributed', 'multi-agent', 'cooperative',
                                'swarm', 'decentralized']):
            o.add('Collaborative')
        return o
    keymap = {'Filter-based': 'Filter-based', 'Optimization-based': 'Optimization-based',
              'Learning-based': 'Learning-based', 'Collaborative': 'Collaborative'}
    print('\n=== AUDIT: keyword classifier vs curated architecture table ===')
    cls = defaultdict(set)
    for pid, r in ext.items():
        for c in arch(r):
            cls[c].add(refnum.get(pid))
    for row in PARAM['architecture']:
        short = next((v for k, v in keymap.items() if k.lower() in row['label'].lower()), None)
        cur = set(row['refs']); kw = {x for x in cls.get(short, set()) if x}
        only_cur = sorted(cur - kw); only_kw = sorted(kw - cur)
        print(f'  {short:20} curated={len(cur):2}  keyword={len(kw):2}  '
              f'curated-only={only_cur}  keyword-only={only_kw}')
    print('  (differences are expected: keyword matching is inclusive and cannot read '
          'auxiliary-sensor or curation context; the curated table is authoritative.)')


if __name__ == '__main__':
    fig_trend()
    fig_architecture()
    fig_class_year()
    fig_adaptive_taxonomy()
    fig_gap_matrix()
    print_summary()
    validate()
    if '--audit' in sys.argv:
        audit()
    print(f'\nFigures written to: {FIG_DIR}')
