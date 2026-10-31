# -*- coding: utf-8 -*-
"""Widgets for the groups_crt videos (groups, orders, modular inverses, the Chinese remainder theorem).

Every number a video shows comes from the helpers below, and each helper asserts its own result by brute force
(and against sympy where sympy has the same function):
  inv_mod(a, m)            modular inverse, asserted a*x = 1 (mod m)
  order_mod(a, m)          order of a in Z_m^*, asserted against sympy.n_order
  powers_mod(a, m)         a, a^2, ... up to the first 1
  zstar(n)                 the units mod n
  mmul / mpow / morder     2x2 / 3x3 matrices mod p (tuples of tuples)
  group_report(E, op)      closure / associativity / neutral / inverses / commutativity of a finite (E, op)
  euclid(a, m)             extended Euclid rows + the back-substitution, asserted
  crt(rems, mods)          the course recipe (M, M_i, M_i mod m_i, x_i, terms, sum, x), asserted with sympy and brute force
Stage pieces (HTML/SVG with stable ids; class h = starts hidden). CSS classes start with gc-.
  lines(pfx, items)        formula lines {pfx}-k revealed one by one
  cayley(pfx, E, op)       an operation table; {pfx}-row-i / {pfx}-col-j / {pfx}-c-i-j highlights, {pfx}-x-i-j red marks
  cycle(pfx, labels)       the powers g, g^2, ... on a circle: nodes {pfx}-n-k, arrows {pfx}-a-k (k -> k+1, last -> first)
  table(pfx, head, rows)   a table whose body cells {pfx}-r-c appear one by one
  strip(pfx, n, layers)    the numbers 0..n-1; each layer (a congruence) marks its members, {pfx}-L<k>
  chip / qstem
"""
import html as _html
import math
from functools import reduce
from itertools import product
from math import gcd

import sympy as sp
from sympy.ntheory import n_order
from sympy.ntheory.modular import solve_congruence

PAL = ["#2dd4bf", "#fbbf24", "#f472b6", "#a78bfa", "#38bdf8"]


# ----------------------------------------------------------------------------- arithmetic (asserted)
def inv_mod(a, m):
    assert gcd(a % m, m) == 1, (a, m)
    x = next(k for k in range(1, m) if (a * k) % m == 1) if m > 1 else 0
    assert x == pow(a, -1, m) and (a * x) % m == 1
    return x


def zstar(n):
    return [a for a in range(1, n) if gcd(a, n) == 1]


def powers_mod(a, m):
    """[a^1, a^2, ..., 1] (stops at the first 1)"""
    out, v = [], a % m
    while True:
        out.append(v)
        if v == 1:
            break
        v = (v * a) % m
        assert len(out) <= m
    return out


def order_mod(a, m):
    k = len(powers_mod(a, m))
    assert k == n_order(a, m)
    return k


def lcm(*xs):
    return reduce(lambda a, b: a * b // gcd(a, b), xs, 1)


def mmul(A, B, p):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(n)) for i in range(n))


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mpow(A, k, p):
    R = eye(len(A))
    for _ in range(k):
        R = mmul(R, A, p)
    return R


def morder(A, p):
    I = eye(len(A))
    R, k = A, 1
    while R != I:
        R, k = mmul(R, A, p), k + 1
        assert k < 10_000
    return k


def group_report(E, op):
    """brute force over a finite set: which group axioms hold. op(a, b) -> value (may leave E)."""
    E = list(E)
    S = set(E)
    closed = all(op(a, b) in S for a in E for b in E)
    assoc = closed and all(op(op(a, b), c) == op(a, op(b, c)) for a in E for b in E for c in E)
    neutral = [e for e in E if all(op(e, a) == a and op(a, e) == a for a in E)] if closed else []
    e = neutral[0] if neutral else None
    inv = {a: [x for x in E if op(a, x) == e and op(x, a) == e] for a in E} if e is not None else {}
    all_inv = e is not None and all(inv[a] for a in E)
    comm = all(op(a, b) == op(b, a) for a in E for b in E)
    return dict(closed=closed, assoc=assoc, neutral=e, inverses=inv, all_inv=all_inv, comm=comm,
                group=closed and assoc and e is not None and all_inv)


def euclid(a, m):
    """extended Euclid for a^{-1} mod m. Returns (divs, x) with divs = [(big, q, small, r)] meaning big = q*small + r,
    ending at r = 1; and x in [0, m) with a*x = 1 (mod m). Asserts the back-substitution s*a + t*m = 1."""
    divs, big, small = [], m, a
    while small != 1:
        q, r = divmod(big, small)
        divs.append((big, q, small, r))
        assert r != 0, "not coprime"
        big, small = small, r
    x = inv_mod(a, m)
    u, v, g = sp.gcdex(a, m)          # u*a + v*m = g
    assert u * a + v * m == g
    assert g == 1 and (int(u) - x) % m == 0
    return divs, x


def crt(rems, mods):
    """the course recipe; returns dict(M, rows=[(m, a, M_i, M_i mod m, x_i, a*M_i*x_i)], total, x)"""
    for i in range(len(mods)):
        for j in range(i + 1, len(mods)):
            assert gcd(mods[i], mods[j]) == 1, (mods[i], mods[j])
    M = math.prod(mods)
    rows = []
    for a, m in zip(rems, mods):
        assert 0 <= a < m
        Mi = M // m
        xi = inv_mod(Mi % m, m)
        assert (Mi * xi) % m == 1
        rows.append((m, a, Mi, Mi % m, xi, a * Mi * xi))
    total = sum(r[5] for r in rows)
    x = total % M
    assert solve_congruence(*zip(rems, mods)) == (x, M)
    assert [v for v in range(M) if all(v % m == a for a, m in zip(rems, mods))] == [x]
    return dict(M=M, rows=rows, total=total, x=x)


def solve_linear(a, b, m):
    """all x in [0, m) with a x = b (mod m), brute force"""
    return [x for x in range(m) if (a * x - b) % m == 0]


# ----------------------------------------------------------------------------- stage pieces
def esc(s):
    return _html.escape(s, quote=True)


def lines(pfx, items, size=40, cls="", start=0, shown=()):
    """formula lines {pfx}-{k}; items are HTML/TeX strings. shown: indexes that start visible."""
    rows = "".join(f'<div id="{pfx}-{k}" class="gc-line{"" if k in shown else " h"}">{t}</div>'
                   for k, t in enumerate(items, start))
    return f'<div class="gc-lines {cls}" dir="ltr" style="font-size:{size}px">{rows}</div>'


def cayley(pfx, E, op, sym="\\cdot", size=36, labels=None, inside=None):
    """operation table, LTR. labels: {value: text} (default str). inside: the set the results should land in
    (values outside it get a hidden red mark {pfx}-x-i-j). Ids: {pfx}-row-i, {pfx}-col-j, {pfx}-c-i-j."""
    lab = lambda v: (labels or {}).get(v, str(v))
    S = set(E if inside is None else inside)
    n = len(E)
    cells = [f'<span class="gc-ch gc-op" style="grid-row:1;grid-column:1">${sym}$</span>']
    for j, b in enumerate(E):
        cells.append(f'<span class="gc-ch" style="grid-row:1;grid-column:{j + 2}">{esc(lab(b))}</span>')
    for i, a in enumerate(E):
        cells.append(f'<i id="{pfx}-row-{i}" class="gc-hi h" style="grid-row:{i + 2}/{i + 3};grid-column:1/{n + 2}"></i>')
    for j in range(n):
        cells.append(f'<i id="{pfx}-col-{j}" class="gc-hi h" style="grid-row:1/{n + 2};grid-column:{j + 2}/{j + 3}"></i>')
    for i, a in enumerate(E):
        cells.append(f'<span class="gc-ch" style="grid-row:{i + 2};grid-column:1">{esc(lab(a))}</span>')
        for j, b in enumerate(E):
            v = op(a, b)
            mark = (f'<i id="{pfx}-x-{i}-{j}" class="gc-xm h"></i>' if v not in S else "")
            cells.append(f'<span class="gc-cell" style="grid-row:{i + 2};grid-column:{j + 2}">'
                         f'<i id="{pfx}-c-{i}-{j}" class="gc-chi h"></i>{mark}<span>{esc(lab(v))}</span></span>')
    return (f'<div id="{pfx}" class="gc-cay" dir="ltr" style="font-size:{size}px;'
            f'grid-template-columns:repeat({n + 1},auto)">{"".join(cells)}</div>')


def cycle(pfx, labels, sups, r=200, node=46, size=None, font=34, hidden=True):
    """powers on a circle. labels: text in each node (the value); sups: the power label next to it, e.g. ('3', '2')
    for 3 squared -> drawn base + superscript. Nodes {pfx}-n-k and arrows {pfx}-a-k (k -> k+1; the last one closes
    the cycle) start hidden."""
    n = len(labels)
    W = size or 2 * (r + node + 90)
    c = W / 2
    pos = [(c + r * math.sin(2 * math.pi * k / n), c - r * math.cos(2 * math.pi * k / n)) for k in range(n)]
    o = [f'<svg class="gc-cyc" id="{pfx}" viewBox="0 0 {W:.0f} {W:.0f}" width="{W:.0f}" height="{W:.0f}" direction="ltr">',
         f'<defs><marker id="{pfx}-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
         f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#c9cdf0"/></marker></defs>']
    hid = " h" if hidden else ""
    for k in range(n):
        (x1, y1), (x2, y2) = pos[k], pos[(k + 1) % n]
        if n == 1:
            continue
        a1 = math.atan2(y1 - c, x1 - c)
        a2 = math.atan2(y2 - c, x2 - c)
        if a2 <= a1:
            a2 += 2 * math.pi
        da = (node + 8) / r
        s = (c + r * math.cos(a1 + da), c + r * math.sin(a1 + da))
        e = (c + r * math.cos(a2 - da), c + r * math.sin(a2 - da))
        big = 1 if (a2 - a1 - 2 * da) > math.pi else 0
        o.append(f'<path id="{pfx}-a-{k}" class="gc-arc{hid}" d="M{s[0]:.1f},{s[1]:.1f} A{r},{r} 0 {big} 1 '
                 f'{e[0]:.1f},{e[1]:.1f}" marker-end="url(#{pfx}-ah)"/>')
    for k, ((x, y), lab, (b, p)) in enumerate(zip(pos, labels, sups)):
        dx, dy = (x - c) / r, (y - c) / r
        tx, ty = x + dx * (node + 46), y + dy * (node + 40) + 12
        o.append(f'<g id="{pfx}-n-{k}" class="{hid.strip()}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{node}" class="gc-node"/>'
                 f'<text x="{x:.1f}" y="{y + font * 0.36:.1f}" class="gc-nl" style="font-size:{font}px">{esc(lab)}</text>'
                 f'<text x="{tx:.1f}" y="{ty:.1f}" class="gc-pw">{esc(b)}<tspan dy="-14" font-size="20">{esc(p)}</tspan></text></g>')
    o.append("</svg>")
    return "".join(o)


def table(pfx, head, rows, size=34, hide_cells=True):
    """head: [html]; rows: [[html]]; body cells {pfx}-r-c (hidden unless hide_cells=False), rows {pfx}-row-r highlight"""
    th = "".join(f"<th>{h}</th>" for h in head)
    body = []
    for r, row in enumerate(rows):
        tds = "".join(f'<td><span id="{pfx}-{r}-{c}"{" class=h" if hide_cells else ""}>{x}</span></td>'
                      for c, x in enumerate(row))
        body.append(f'<tr>{tds}</tr>')
    return (f'<table class="gc-tab" id="{pfx}" dir="ltr" style="font-size:{size}px"><thead><tr>{th}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table>')


def strip(pfx, n, layers, cols=15, cell=58):
    """the numbers 0..n-1 in rows of `cols`. layers: [(members set, color index)] -> a hidden overlay {pfx}-L<k>
    marking the members; plus a hidden gold ring {pfx}-s-<v> for every v (to point at a solution)."""
    rows = (n + cols - 1) // cols
    gap = 8
    W, H = cols * cell + (cols - 1) * gap, rows * cell + (rows - 1) * gap
    pos = lambda v: ((v % cols) * (cell + gap), (v // cols) * (cell + gap))
    o = [f'<div class="gc-strip" id="{pfx}" dir="ltr" style="width:{W}px;height:{H}px">']
    for k, (mem, col) in enumerate(layers):
        o.append(f'<div id="{pfx}-L{k}" class="gc-layer h">')
        for v in sorted(mem):
            x, y = pos(v)
            d = 13                                   # one colored dot per layer along the bottom of the cell
            o.append(f'<i style="left:{x + 6 + k * (d + 4)}px;top:{y + cell - d - 4}px;width:{d}px;height:{d}px;'
                     f'background:{PAL[col]}"></i>')
        o.append("</div>")
    for v in range(n):
        x, y = pos(v)
        o.append(f'<span class="gc-num" style="left:{x}px;top:{y}px;width:{cell}px;height:{cell}px">{v}</span>'
                 f'<i id="{pfx}-s-{v}" class="gc-sol h" style="left:{x - 6}px;top:{y - 6}px;width:{cell + 12}px;'
                 f'height:{cell + 12}px"></i>')
    o.append("</div>")
    return "".join(o)


def chip(id_, html_, col=0, hidden=True):
    return (f'<span id="{id_}" class="gc-chip{" h" if hidden else ""}" style="border-color:{PAL[col]};'
            f'color:{PAL[col]}">{html_}</span>')


def qstem(qid, html_):
    return f'<div class="qstem"><span class="qid">{qid}</span>{html_}</div>'


def ctx_stem(qid, ctx_html, q_html):
    """an exam stem: the shared context (smaller) + the part's question"""
    return (f'<div class="qstem"><span class="qid">{qid}</span><div class="gc-ctx">{ctx_html}</div>'
            f'<div>{q_html}</div></div>')


def pm(rows):
    """TeX pmatrix from a tuple of tuples"""
    return "\\begin{pmatrix}" + "\\\\".join("&".join(str(x) for x in r) for r in rows) + "\\end{pmatrix}"
