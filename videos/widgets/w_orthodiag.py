# -*- coding: utf-8 -*-
"""Widgets for the orthodiag videos (orthogonal diagonalization and positive definiteness).

Everything shown is computed here with sympy, exactly (no floats):
  ent(x) / pm(M) / vec(v) / nvec(v)   TeX of exact entries in the course's spelling (1/sqrt5, not sqrt5/5)
  eig_pairs(A, pairs)                 asserts A v = lambda v for every (lambda, v)
  orth_diag(A, pairs)                 normalizes, asserts Q^T Q = I, Q^T A Q = D and Q D Q^T = A; returns (Q, D)
  classify(M)                         the course convention: positive = all eigenvalues >= 0, strict = > 0
Stage pieces (HTML/SVG with stable ids, class h = starts hidden):
  mat(pfx, M, ...)      a matrix as a grid: cell / row / column highlights {pfx}-c-i-j, {pfx}-row-i, {pfx}-col-j
  lines(pfx, items)     a stack of formula lines {pfx}-k
  table(pfx, head, rows) a small table whose cells appear one by one {pfx}-r-c
  numline(pfx, ...)     an SVG number line with bands (where an eigenvalue is >= 0, the final verdict rows)
  plane(pfx, vecs)      a small SVG plane with arrows (eigenvectors, a Gram-Schmidt projection)
CSS classes start with od- (all widget css files are merged into every video of the app).
"""
import html as _html
import sympy as sp

S = sp.Matrix
R = sp.Rational
sqrt = sp.sqrt

# colors of eigenpairs: the column of Q and its diagonal entry in D share one color
PAL = ["#2dd4bf", "#fbbf24", "#f472b6", "#a78bfa"]


# ----------------------------------------------------------------------------- exact algebra
def _split(x):
    """x = r * sqrt(m), r rational, m squarefree int (m = 1 for a rational x)"""
    x = sp.nsimplify(sp.simplify(x))
    if x.is_Rational:
        return sp.Rational(x), 1
    r, rest = x.as_coeff_Mul()
    if rest.is_Pow and rest.exp == sp.Rational(1, 2) and rest.base.is_Integer:
        return sp.Rational(r), int(rest.base)
    raise ValueError(f"not r*sqrt(m): {x}")


def _frac(p, q, root=None):
    """TeX of p/q (p, q > 0 ints), optional sqrt(root) in the denominator"""
    den = (str(q) if q != 1 else "") + (f"\\sqrt{{{root}}}" if root else "")
    return f"\\frac{{{p}}}{{{den}}}" if den else str(p)


def ent(x):
    """exact number -> TeX the way the course writes it: 2/3, -1/sqrt5, -4/(3 sqrt5), sqrt2; symbolic -> sp.latex"""
    if isinstance(x, str):
        return x
    if getattr(sp.sympify(x), "free_symbols", None):
        return sp.latex(x).replace(" ", "")
    r, m = _split(x)
    sign = "-" if r < 0 else ""
    r = abs(r)
    if m == 1:
        return sign + (_frac(r.p, r.q) if r.q != 1 else str(r.p))
    k = r * m                                   # r sqrt(m) = (r m) / sqrt(m)
    if k.q == 1 and r.q != 1:
        return sign + _frac(k.p, 1, m)
    if r.q == 1:
        return sign + ("" if r == 1 else str(r.p)) + f"\\sqrt{{{m}}}"
    return sign + _frac(k.p, k.q, m)


def pm(M, big=False):
    rows = "\\\\".join("&".join(ent(x) for x in M.row(i)) for i in range(M.rows))
    return f"\\begin{{pmatrix}}{rows}\\end{{pmatrix}}"


def vec(v):
    """integer/exact vector as a row tuple (a, b, c)"""
    return "(" + ",".join((lambda t: "{" + t + "}" if t.startswith("-") else t)(ent(x)) for x in v) + ")"


def nvec(v):
    """an integer vector v normalized, written as 1/sqrt(n) (a, b, c) or 1/k (a, b, c)"""
    n2 = sum(x * x for x in v)
    r, m = _split(sp.sqrt(n2))
    if m == 1 and r == 1:
        return vec(v)
    lead = _frac(1, r.p, m if m != 1 else None)
    return f"{lead}{vec(v)}"


def norm(v):
    return sp.sqrt(sum(x * x for x in v))


def eig_pairs(A, pairs):
    for lam, v in pairs:
        v = S(v)
        assert any(x != 0 for x in v), v
        assert sp.simplify(A * v - lam * v) == sp.zeros(A.rows, 1), (lam, list(v))
    return pairs


def orth_diag(A, pairs):
    """pairs [(lambda, integer vector)] in column order; returns exact (Q, D) after checking everything"""
    assert A == A.T
    eig_pairs(A, pairs)
    cols = [S(v) / norm(v) for _, v in pairs]
    Q = S.hstack(*cols)
    D = sp.diag(*[lam for lam, _ in pairs])
    assert sp.simplify(Q.T * Q) == sp.eye(A.rows)
    assert sp.simplify(Q.T * A * Q) == D
    assert sp.simplify(Q * D * Q.T) == A
    assert sorted(A.eigenvals(multiple=True)) == sorted(lam for lam, _ in pairs)
    return Q, D


def classify(M):
    """course flags (needs M symmetric): pos = all >= 0, spos = all > 0, neg, sneg"""
    assert M == M.T
    t = sp.Dummy("t")
    ev = sp.Poly((M - t * sp.eye(M.rows)).det(), t).real_roots()      # exact CRootOf: comparisons always decidable
    assert len(ev) == M.rows                                     # symmetric: every eigenvalue is real
    return dict(pos=all(e >= 0 for e in ev), spos=all(e > 0 for e in ev),
                neg=all(e <= 0 for e in ev), sneg=all(e < 0 for e in ev))


def lead_minors(M):
    return [sp.factor(M[:k, :k].det()) for k in range(1, M.rows + 1)]


# ----------------------------------------------------------------------------- stage pieces
def esc(s):
    return _html.escape(s, quote=True)


def mat(pfx, M, label="", cols=None, hidden=False, size=46, tex=None):
    """a matrix as a CSS grid with highlight overlays.
    M: sympy Matrix (entries via ent) or a list of lists of TeX strings (tex=True).
    cols: {j: color index} draws a permanent tint under column j (Q and D sharing colors).
    Ids: {pfx} the block, {pfx}-c-i-j cell, {pfx}-row-i, {pfx}-col-j, {pfx}-d-i (diagonal cell, = c-i-i)."""
    if isinstance(M, sp.MatrixBase):
        rows = [[ent(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]
    else:
        rows = M
    n, m = len(rows), len(rows[0])
    cells = []
    for j in range(m):
        cells.append(f'<i id="{pfx}-col-{j}" class="od-hi h" style="grid-row:1/{n + 1};grid-column:{j + 1}"></i>')
        if cols and j in cols:
            cells.append(f'<i class="od-tint" style="grid-row:1/{n + 1};grid-column:{j + 1};'
                         f'background:{PAL[cols[j]]}26;border-color:{PAL[cols[j]]}"></i>')
    for i in range(n):
        cells.append(f'<i id="{pfx}-row-{i}" class="od-hi h" style="grid-row:{i + 1};grid-column:1/{m + 1}"></i>')
    for i in range(n):
        for j in range(m):
            cells.append(f'<span class="od-cell" style="grid-row:{i + 1};grid-column:{j + 1}">'
                         f'<i id="{pfx}-c-{i}-{j}" class="od-chi h"></i><span>${rows[i][j]}$</span></span>')
    lab = f'<span class="od-mlab">${label}$</span>' if label else ""
    return (f'<div id="{pfx}" class="od-matw{" h" if hidden else ""}" dir="ltr" style="font-size:{size}px">{lab}'
            f'<div class="od-mat"><div class="od-grid" style="grid-template-columns:repeat({m},auto)">'
            f'{"".join(cells)}</div></div></div>')


def lines(pfx, items, size=44, cls="", start=0):
    """formula lines revealed one by one, ids {pfx}-{start}, {pfx}-{start+1}, ...
    items: list of TeX/HTML strings (TeX wrapped in $..$ by the caller)."""
    rows = "".join(f'<div id="{pfx}-{k}" class="od-line h">{t}</div>' for k, t in enumerate(items, start))
    return f'<div class="od-lines {cls}" dir="ltr" style="font-size:{size}px">{rows}</div>'


def table(pfx, head, rows, colors=None, size=36, shown_head=True):
    """head: [html]; rows: [[html]]; every body cell {pfx}-r-c hidden; colors: [color index per row] (a dot)."""
    th = "".join(f"<th>{h}</th>" for h in head)
    body = []
    for r, row in enumerate(rows):
        dot = (f'<span class="od-dot" style="background:{PAL[colors[r]]}"></span>' if colors else "")
        tds = "".join(f'<td><span id="{pfx}-{r}-{c}" class="h">{(dot if c == 0 else "")}{x}</span></td>'
                      for c, x in enumerate(row))
        body.append(f"<tr>{tds}</tr>")
    return (f'<table class="od-tab" id="{pfx}" dir="ltr" style="font-size:{size}px"><thead>'
            f'<tr{"" if shown_head else " class=h"}>{th}</tr></thead><tbody>{"".join(body)}</tbody></table>')


def numline(pfx, lo, hi, ticks, rows, w=1000, label_w=230, rh=64):
    """number line(s). ticks: [(value, text)] marked on the axis; rows: [(id, label, segments)] where segments are
    [(a, b, closed_a, closed_b, color)] with a/b numbers or None (= the end of the line, an arrow).
    Every row is hidden ({pfx}-{id}); the axis and ticks are shown. SVG text only (no TeX)."""
    pad = 40
    right = w - label_w                       # the axis ends here; row labels sit to its right
    X = lambda v: pad + (float(v) - lo) / (hi - lo) * (right - 2 * pad)
    h = 70 + rh * len(rows) + 20
    out = [f'<svg class="od-nl" id="{pfx}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" direction="ltr">']
    y0 = 40
    out.append(f'<line x1="{pad - 20}" y1="{y0}" x2="{right - pad + 20}" y2="{y0}" class="od-ax"/>')
    for v, t in ticks:
        x = X(v)
        out.append(f'<line x1="{x:.1f}" y1="{y0 - 12}" x2="{x:.1f}" y2="{y0 + 12}" class="od-ax"/>'
                   f'<text x="{x:.1f}" y="{y0 - 18}" class="od-tk">{esc(t)}</text>'
                   f'<line x1="{x:.1f}" y1="{y0 + 14}" x2="{x:.1f}" y2="{h - 10}" class="od-guide"/>')
    for k, (rid, label, segs) in enumerate(rows):
        y = 70 + rh * k + rh / 2
        g = [f'<g id="{pfx}-{rid}" class="h">']
        for a, b, ca, cb, col in segs:
            c = PAL[col] if isinstance(col, int) else col
            xa = X(a) if a is not None else pad - 20
            xb = X(b) if b is not None else right - pad + 20
            g.append(f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" stroke="{c}" stroke-width="12" '
                     f'stroke-linecap="butt"/>')
            for x, v, closed in ((xa, a, ca), (xb, b, cb)):
                if v is not None:
                    g.append(f'<circle cx="{x:.1f}" cy="{y}" r="11" stroke="{c}" stroke-width="5" '
                             f'fill="{c if closed else "#0a0c18"}"/>')
        if label:
            g.append(f'<text x="{w - 6}" y="{y + 10}" class="od-rl">{esc(label)}</text>')
        g.append("</g>")
        out += g
    out.append("</svg>")
    return "".join(out)


def plane(pfx, vecs, rng=3, size=430, dashed=()):
    """a 2D plane, x right / y up, from -rng to rng. vecs: [(id, (x, y), color index, text label)] arrows from 0
    (hidden, id {pfx}-{id}); dashed: [(id, (x1, y1), (x2, y2))] dashed segments (hidden)."""
    s = size / (2 * rng)
    C = lambda x, y: (size / 2 + float(x) * s, size / 2 - float(y) * s)
    o = [f'<svg class="od-pl" id="{pfx}" viewBox="-30 -30 {size + 60} {size + 60}" width="{size + 60}" '
         f'height="{size + 60}" direction="ltr"><defs>']
    for k, c in enumerate(PAL):
        o.append(f'<marker id="{pfx}-m{k}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
                 f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    o.append("</defs>")
    for t in range(-rng, rng + 1):
        x, _ = C(t, 0)
        o.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{size}" class="od-grd"/>'
                 f'<line x1="0" y1="{x}" x2="{size}" y2="{x}" class="od-grd"/>')
    o.append(f'<line x1="0" y1="{size / 2}" x2="{size}" y2="{size / 2}" class="od-ax"/>'
             f'<line x1="{size / 2}" y1="0" x2="{size / 2}" y2="{size}" class="od-ax"/>')
    for i, a, b in dashed:
        (x1, y1), (x2, y2) = C(*a), C(*b)
        o.append(f'<line id="{pfx}-{i}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="od-dash h"/>')
    for i, (x, y), col, lab in vecs:
        x0, y0 = C(0, 0)
        x1, y1 = C(x, y)
        L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        tx, ty = x1 + (x1 - x0) / L * 30, y1 + (y1 - y0) / L * 30
        o.append(f'<g id="{pfx}-{i}" class="h"><line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{PAL[col]}" '
                 f'stroke-width="7" marker-end="url(#{pfx}-m{col})"/>'
                 f'<text x="{tx:.1f}" y="{ty + (16 if (y1 - y0) / L > 0.3 else -14):.1f}" class="od-vl" fill="{PAL[col]}">{esc(lab)}</text></g>')
    o.append("</svg>")
    return "".join(o)


def chip(id_, html_, col=0, hidden=True):
    """a small colored pill (a verdict, an eigenvalue label)"""
    return (f'<span id="{id_}" class="od-chip{" h" if hidden else ""}" style="border-color:{PAL[col]};'
            f'color:{PAL[col]}">{html_}</span>')


def qstem(qid, html_):
    return f'<div class="qstem"><span class="qid">{qid}</span>{html_}</div>'


def qd(Q, D, size=30, extra=""):
    """Q and D side by side (LTR), for an answer card"""
    return (f'<div class="od-row" style="font-size:{size}px;gap:34px">$Q={pm(Q)}$<span>$D={pm(D)}$</span>'
            f'{extra}</div>')
