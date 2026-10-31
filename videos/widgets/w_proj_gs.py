# -*- coding: utf-8 -*-
"""Widgets for the proj_gs videos (היטל וגרהם-שמידט): exact arithmetic (sympy), TeX for vectors and matrices,
spoken Hebrew for numbers, and SVG pictures computed in Python (a projection onto a line, a parallelogram, points
with a least-squares line, function plots with signed areas). Every picture is drawn from the same exact numbers
the script asserts, never by hand.

Ids (all hidden at start unless noted):
  proj2d(pfx, ...)  {pfx}-line  {pfx}-a  {pfx}-b  {pfx}-p  {pfx}-c  {pfx}-ra  {pfx}-w   (axes always visible)
  para(pfx, ...)    {pfx}-u  {pfx}-v  {pfx}-s (u+v)  {pfx}-d (u-v)  {pfx}-sides
  lsplot(pfx, ...)  {pfx}-pts (shown)  {pfx}-line  {pfx}-res  {pfx}-xbar  {pfx}-<key> for extra lines
  fplot(pfx, ...)   {pfx}-<id> per curve / area
  rows(pfx, items)  {pfx}-<i> per row
"""
import math
import sympy as sp

R = sp.Rational
X = sp.Symbol("x", real=True)


# ---------------------------------------------------------------- exact arithmetic
def V(*a):
    return sp.Matrix([sp.nsimplify(t) for t in a])


def M(rows):
    return sp.Matrix([[sp.nsimplify(t) for t in r] for r in rows])


def dot(u, v):
    return sp.simplify(sum(a * b for a, b in zip(u, v)))


def ip_m(A, B):
    """<A,B> = tr(B^T A) = sum of products of matching entries"""
    t = sp.simplify((B.T * A).trace())
    assert sp.simplify(t - sum(a * b for a, b in zip(A, B))) == 0
    return t


def ip_f(f, g, lo, hi, w=1):
    return sp.simplify(sp.integrate(w * f * g, (X, lo, hi)))


def coef(v, u, ip):
    return sp.simplify(ip(v, u) / ip(u, u))


def gram_schmidt(vs, ip):
    """plain Gram-Schmidt (no rescaling): [u_1, ...] and the coefficients {(m, i): <v_m,u_i>/|u_i|^2}"""
    us, cs = [], {}
    for m, v in enumerate(vs):
        u = v
        for i, w in enumerate(us):
            c = coef(v, w, ip)
            cs[(m, i)] = c
            u = u - c * w
        us.append(sp.simplify(u))
    for i in range(len(us)):
        for j in range(i):
            assert sp.simplify(ip(us[i], us[j])) == 0
    return us, cs


def proj(v, basis, ip):
    """projection on the span of an ORTHOGONAL basis (asserted)"""
    for i in range(len(basis)):
        for j in range(i):
            assert sp.simplify(ip(basis[i], basis[j])) == 0, "basis not orthogonal"
    p = 0 * v
    for u in basis:
        p = p + coef(v, u, ip) * u
    return sp.simplify(p)


# ---------------------------------------------------------------- TeX
def tx(r):
    r = sp.nsimplify(r)
    if r.is_Rational and not r.is_Integer:
        s = "-" if r < 0 else ""
        return f"{s}\\frac{{{abs(r.p)}}}{{{r.q}}}"
    return sp.latex(r)


def col(v):
    return "\\begin{pmatrix}" + "\\\\".join(tx(t) for t in v) + "\\end{pmatrix}"


def tup(v):
    return "(" + ",".join(tx(t) for t in v) + ")"


def mat(A):
    return "\\begin{pmatrix}" + "\\\\".join("&".join(tx(A[i, j]) for j in range(A.cols)) for i in range(A.rows)) \
        + "\\end{pmatrix}"


# ---------------------------------------------------------------- spoken numbers
FR = {(1, 2): "חצי", (1, 3): "שליש", (2, 3): "שני שליש", (1, 4): "רבע", (3, 4): "שלושה רבעים"}
NUM = {0: "אפס", 1: "אחת", 2: "שתיים", 3: "שלוש", 4: "ארבע", 5: "חמש", 6: "שש", 7: "שבע", 8: "שמונה", 9: "תשע",
       10: "עשר", 11: "אחת עשרה", 12: "שתים עשרה", 13: "שלוש עשרה", 14: "ארבע עשרה", 15: "חמש עשרה",
       16: "שש עשרה", 17: "שבע עשרה", 18: "שמונה עשרה", 19: "תשע עשרה", 20: "עשרים"}


def say_int(n):
    n = int(n)
    if n < 0:
        return "מינוס " + say_int(-n)
    return NUM.get(n, str(n))


def say_num(r):
    """exact rational in spoken Hebrew: 'מינוס שלוש חלקי שתיים', 'חצי', 'שתיים'"""
    r = sp.nsimplify(r)
    assert r.is_Rational, r
    if r.is_Integer:
        return say_int(r)
    s = "מינוס " if r < 0 else ""
    p, q = abs(r.p), r.q
    if (p, q) in FR:
        return s + FR[(p, q)]
    return f"{s}{say_int(p)} חלקי {say_int(q)}"


def say_vec(v):
    return ", ".join(say_num(t) for t in v)


# ---------------------------------------------------------------- HTML helpers
def rows(pfx, items, cls=""):
    """a column of rows revealed one by one: items = [html]; ids {pfx}-0, {pfx}-1, ..."""
    body = "".join(f'<div id="{pfx}-{i}" class="pg-row h">{h}</div>' for i, h in enumerate(items))
    return f'<div class="pg-rows {cls}">{body}</div>'


def big(id_, tex, cls="", hidden=True):
    return f'<div id="{id_}" class="pg-big{" h" if hidden else ""} {cls}">${tex}$</div>'


def stem(qid, html_):
    return f'<div class="qstem"><span class="qid">{qid}</span>{html_}</div>'


# ---------------------------------------------------------------- SVG
COL = {"a": "#38bdf8", "b": "#eaedff", "p": "#2dd4bf", "c": "#fbbf24", "w": "#fb7185", "g": "#9aa0cf", "v": "#c084fc"}


class Frame:
    def __init__(self, box, size):
        self.x0, self.x1, self.y0, self.y1 = [float(t) for t in box]
        self.W, self.H = size

    def X(self, x):
        return (float(x) - self.x0) / (self.x1 - self.x0) * self.W

    def Y(self, y):
        return self.H - (float(y) - self.y0) / (self.y1 - self.y0) * self.H

    def pt(self, v):
        return self.X(v[0]), self.Y(v[1])


def _defs(pfx):
    out = ["<defs>"]
    for k, c in COL.items():
        out.append(f'<marker id="{pfx}-m{k}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" '
                   f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    out.append("</defs>")
    return "".join(out)


def _axes(F, ticks=True, step=1):
    o = [f'<line class="pg-ax" x1="0" y1="{F.Y(0):.1f}" x2="{F.W}" y2="{F.Y(0):.1f}"/>',
         f'<line class="pg-ax" x1="{F.X(0):.1f}" y1="0" x2="{F.X(0):.1f}" y2="{F.H}"/>']
    if ticks:
        for i in range(math.ceil(F.x0), math.floor(F.x1) + 1, step):
            if i:
                o.append(f'<line class="pg-tk" x1="{F.X(i):.1f}" y1="{F.Y(0) - 6:.1f}" x2="{F.X(i):.1f}" y2="{F.Y(0) + 6:.1f}"/>'
                         f'<text class="pg-tl" x="{F.X(i):.1f}" y="{F.Y(0) + 30:.1f}">{i}</text>')
        for i in range(math.ceil(F.y0), math.floor(F.y1) + 1, step):
            if i:
                o.append(f'<line class="pg-tk" x1="{F.X(0) - 6:.1f}" y1="{F.Y(i):.1f}" x2="{F.X(0) + 6:.1f}" y2="{F.Y(i):.1f}"/>'
                         f'<text class="pg-tl" x="{F.X(0) - 14:.1f}" y="{F.Y(i) + 8:.1f}" text-anchor="end">{i}</text>')
    return "".join(o)


def _label(txt):
    """'u+v' -> italic letters; 'p_1' -> subscript"""
    if "_" in txt:
        a, b = txt.split("_", 1)
        return f'{a}<tspan dy="8" font-size="22">{b}</tspan>'
    return txt


def arrow(F, pfx, id_, a, b, k, label=None, lpos=None, hidden=True, dash=False):
    x1, y1 = F.pt(a)
    x2, y2 = F.pt(b)
    lab = ""
    if label:
        lx, ly = lpos if lpos else ((x1 + x2) / 2, (y1 + y2) / 2)
        lab = f'<text class="pg-vl" x="{lx:.1f}" y="{ly:.1f}" fill="{COL[k]}">{_label(label)}</text>'
    cls = "pg-vec" + (" pg-dash" if dash else "")
    return (f'<g id="{pfx}-{id_}"{" class=\"h\"" if hidden else ""}><line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" '
            f'x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COL[k]}" marker-end="url(#{pfx}-m{k})"/>{lab}</g>')


def _off(F, a, b, d=30, side=1, at=0.5):
    """a label spot: the point at fraction `at` of a->b pushed d px to one side (screen coords)"""
    x1, y1 = F.pt(a)
    x2, y2 = F.pt(b)
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy) or 1
    return x1 + at * dx + side * dy / n * d, y1 + at * dy - side * dx / n * d + 9


def proj2d(pfx, a, b, box, size=(620, 560), wrong=None, names=("a", "b", "p", "c"), sides=(1, -1, 1, 1), at=(0.5, 0.5, 0.5, 0.5)):
    """b projected on the line of a: p = <b,a>/|a|^2 a, c = b - p (asserted ⟂ a). wrong: a wrong 'projection' (red)."""
    a = [sp.nsimplify(t) for t in a]
    b = [sp.nsimplify(t) for t in b]
    k = (b[0] * a[0] + b[1] * a[1]) / (a[0] ** 2 + a[1] ** 2)
    p = [k * a[0], k * a[1]]
    c = [b[0] - p[0], b[1] - p[1]]
    assert sp.simplify(c[0] * a[0] + c[1] * a[1]) == 0
    F = Frame(box, size)
    o = [f'<svg class="pg-svg" id="{pfx}" viewBox="0 0 {size[0]} {size[1]}" width="{size[0]}" height="{size[1]}" '
         f'direction="ltr">', _defs(pfx), _axes(F)]
    # the line through a, across the whole box
    n = math.hypot(float(a[0]), float(a[1]))
    ux, uy = float(a[0]) / n, float(a[1]) / n
    tlo, thi = -1e9, 1e9                     # clip t·(ux,uy) to the box
    for d, lo_, hi_ in ((ux, F.x0, F.x1), (uy, F.y0, F.y1)):
        if abs(d) > 1e-12:
            t1, t2 = sorted((lo_ / d, hi_ / d))
            tlo, thi = max(tlo, t1), min(thi, t2)
    o.append(f'<line id="{pfx}-line" class="pg-line h" x1="{F.X(tlo * ux):.1f}" y1="{F.Y(tlo * uy):.1f}" '
             f'x2="{F.X(thi * ux):.1f}" y2="{F.Y(thi * uy):.1f}"/>')
    z = [0, 0]
    o.append(arrow(F, pfx, "a", z, a, "a", names[0], _off(F, z, a, 28, sides[0], at[0])))
    o.append(arrow(F, pfx, "b", z, b, "b", names[1], _off(F, z, b, 28, sides[1], at[1])))
    o.append(arrow(F, pfx, "p", z, p, "p", names[2], _off(F, z, p, 30, sides[2], at[2])))
    o.append(arrow(F, pfx, "c", p, b, "c", names[3], _off(F, p, b, 30, sides[3], at[3])))
    if wrong is not None:
        wv = [float(t) for t in wrong]
        o.append(arrow(F, pfx, "w", z, wv, "w", None))
    # right-angle mark at p, between the line (towards the origin side) and c
    s = 22
    px, py = F.pt(p)
    cx, cy = F.pt(b)
    dvx, dvy = cx - px, cy - py
    dn = math.hypot(dvx, dvy) or 1
    dvx, dvy = dvx / dn * s, dvy / dn * s
    lx, ly = F.X(float(p[0]) - ux) - px, F.Y(float(p[1]) - uy) - py
    ln = math.hypot(lx, ly) or 1
    lx, ly = lx / ln * s, ly / ln * s
    o.append(f'<path id="{pfx}-ra" class="pg-ra h" d="M{px + lx:.1f},{py + ly:.1f} L{px + lx + dvx:.1f},{py + ly + dvy:.1f} '
             f'L{px + dvx:.1f},{py + dvy:.1f}"/>')
    o.append("</svg>")
    return "".join(o), p, c


def para(pfx, u, v, box, size=(620, 520)):
    """the parallelogram of u and v with both diagonals u+v and u-v (drawn from the tip of v)"""
    F = Frame(box, size)
    u = [float(t) for t in u]
    v = [float(t) for t in v]
    s = [u[0] + v[0], u[1] + v[1]]
    z = [0, 0]
    o = [f'<svg class="pg-svg" id="{pfx}" viewBox="0 0 {size[0]} {size[1]}" width="{size[0]}" height="{size[1]}" '
         f'direction="ltr">', _defs(pfx)]
    o.append(f'<g id="{pfx}-sides" class="h"><line class="pg-side" x1="{F.X(u[0]):.1f}" y1="{F.Y(u[1]):.1f}" '
             f'x2="{F.X(s[0]):.1f}" y2="{F.Y(s[1]):.1f}"/><line class="pg-side" x1="{F.X(v[0]):.1f}" y1="{F.Y(v[1]):.1f}" '
             f'x2="{F.X(s[0]):.1f}" y2="{F.Y(s[1]):.1f}"/></g>')
    o.append(arrow(F, pfx, "u", z, u, "a", "u", _off(F, z, u, 30, 1)))
    o.append(arrow(F, pfx, "v", z, v, "b", "v", _off(F, z, v, 30, 1)))
    o.append(arrow(F, pfx, "s", z, s, "p", "u+v", _off(F, z, s, 44, -1, 0.72)))
    o.append(arrow(F, pfx, "d", v, u, "c", "u−v", _off(F, v, u, 40, 1, 0.25)))
    o.append("</svg>")
    return "".join(o)


def lsplot(pfx, pts, box, size=(640, 560), line=None, extra=None, xbar=None, step=1, res=True):
    """points, the line y = m x + n (exact m, n), its residual segments; extra = {key: (m, n, color)}"""
    F = Frame(box, size)
    o = [f'<svg class="pg-svg" id="{pfx}" viewBox="0 0 {size[0]} {size[1]}" width="{size[0]}" height="{size[1]}" '
         f'direction="ltr">', _defs(pfx), _axes(F, step=step)]

    def seg(m, n):
        """the line y = m x + n clipped to the box"""
        m, n = float(m), float(n)
        a, b = F.x0, F.x1
        if abs(m) > 1e-12:
            t1, t2 = sorted(((F.y0 - n) / m, (F.y1 - n) / m))
            a, b = max(a, t1), min(b, t2)
        return F.X(a), F.Y(m * a + n), F.X(b), F.Y(m * b + n)
    if xbar is not None:
        o.append(f'<line id="{pfx}-xbar" class="pg-xbar h" x1="{F.X(xbar):.1f}" y1="0" x2="{F.X(xbar):.1f}" y2="{F.H}"/>')
    for key, (m, n, k) in (extra or {}).items():
        x1, y1, x2, y2 = seg(m, n)
        o.append(f'<line id="{pfx}-{key}" class="pg-fit h" stroke="{COL[k]}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    if line is not None:
        m, n = line
        x1, y1, x2, y2 = seg(m, n)
        o.append(f'<line id="{pfx}-line" class="pg-fit h" stroke="{COL["p"]}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
        if res:
            r = []
            for (x, y) in pts:
                yh = sp.nsimplify(m) * sp.nsimplify(x) + sp.nsimplify(n)
                r.append(f'<line class="pg-res" x1="{F.X(x):.1f}" y1="{F.Y(y):.1f}" x2="{F.X(x):.1f}" y2="{F.Y(yh):.1f}"/>')
            o.append(f'<g id="{pfx}-res" class="h">{"".join(r)}</g>')
    dots = "".join(f'<circle class="pg-pt" cx="{F.X(x):.1f}" cy="{F.Y(y):.1f}" r="9"/>' for x, y in pts)
    o.append(f'<g id="{pfx}-pts">{dots}</g>')
    o.append("</svg>")
    return "".join(o)


def fplot(pfx, curves, box, size=(640, 520), areas=(), step=1, n=240, dom=None):
    """curves = [(id, f (sympy in x), color key, label, (lx, ly) world label spot)];
    areas = [(id, f)]: the signed area between f and the x-axis, positive part green, negative part red.
    dom = (lo, hi): the interval of the inner product (areas and curves are drawn on it only). Everything is
    clipped to the box."""
    F = Frame(box, size)
    lo, hi = dom if dom else (F.x0, F.x1)
    o = [f'<svg class="pg-svg" id="{pfx}" viewBox="0 0 {size[0]} {size[1]}" width="{size[0]}" height="{size[1]}" '
         f'direction="ltr">', _defs(pfx)]
    xs = [lo + (hi - lo) * i / n for i in range(n + 1)]
    clip = lambda y: min(F.y1, max(F.y0, y))
    for ar in areas:
        id_, f = ar[0], ar[1]
        c = float(ar[2]) if len(ar) > 2 else 0.0          # shade between f and the level y = c
        fn = sp.lambdify(X, f, "math")
        ys = [fn(x) for x in xs]
        for sign, cls in ((1, "pg-apos"), (-1, "pg-aneg")):
            pts = [f"{F.X(xs[0]):.1f},{F.Y(c):.1f}"]
            for x, y in zip(xs, ys):
                pts.append(f"{F.X(x):.1f},{F.Y(clip(max(c, y) if sign > 0 else min(c, y))):.1f}")
            pts.append(f"{F.X(xs[-1]):.1f},{F.Y(c):.1f}")
            o.append(f'<polygon id="{pfx}-{id_}-{"p" if sign > 0 else "n"}" class="{cls} h" points="{" ".join(pts)}"/>')
    o.append(_axes(F, step=step))
    for id_, f, k, lab, lp in curves:
        fn = sp.lambdify(X, f, "math")
        d, pen = [], False
        for x in xs:
            y = fn(x)
            if F.y0 <= y <= F.y1:
                d.append(f"{'L' if pen else 'M'}{F.X(x):.1f},{F.Y(y):.1f}")
                pen = True
            else:
                pen = False
        lab_ = (f'<text class="pg-vl" x="{F.X(lp[0]):.1f}" y="{F.Y(lp[1]):.1f}" fill="{COL[k]}">{lab}</text>'
                if lab else "")
        o.append(f'<g id="{pfx}-{id_}" class="h"><path class="pg-curve" stroke="{COL[k]}" d="{" ".join(d)}"/>{lab_}</g>')
    o.append("</svg>")
    return "".join(o)
