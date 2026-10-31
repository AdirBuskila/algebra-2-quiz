# -*- coding: utf-8 -*-
"""SVD widgets for the algebra-2 videos (course svd): exact TeX for matrices and normalized vectors, the size diagram
A = U S V^T as proportional boxes, the U S V^T assembly row, and line stacks revealed one by one.

Everything numeric is sympy-exact. check_svd() asserts a decomposition the way the course checker does
(tools/verify/needhelp/svd/check.py is_svd: U, V orthogonal and U S V^T == A), plus descending non-negative sigmas.

Ids:
  line(id, tex)                    one hidden line of math (class sv-line)
  shapes(pfx, m, n)                {pfx}-A, {pfx}-eq, {pfx}-U, {pfx}-S, {pfx}-Vt   (boxes, hidden)
  assembly(pfx, A, U, S, Vt)       {pfx}-A, {pfx}-eq, {pfx}-U, {pfx}-S, {pfx}-Vt   (TeX terms with a label, hidden)
"""
import sympy as sp

M = sp.Matrix


# ---------------------------------------------------------------- exact algebra
def E(e):
    """TeX of an exact scalar: 0, -3, \\frac{1}{2}, \\sqrt{6}, 2\\sqrt{2}, \\frac{1}{\\sqrt{2}}"""
    e = sp.nsimplify(sp.simplify(e))
    if e == 0:
        return "0"
    s = "-" if e < 0 else ""
    a = abs(e)
    if a.is_Rational:
        return s + (str(a.p) if a.q == 1 else rf"\frac{{{a.p}}}{{{a.q}}}")
    r = sp.nsimplify(a ** 2)
    assert r.is_Rational, e
    p, q = r.p, r.q                           # a = sqrt(p/q)
    if q == 1:
        return s + sp.latex(sp.sqrt(p)).replace(r"\sqrt{", r"\sqrt{")
    if p == 1:
        return s + rf"\frac{{1}}{{{sp.latex(sp.sqrt(q))}}}"
    return s + sp.latex(a)


def sig(lam):
    """sigma = sqrt(lambda), exact"""
    return sp.sqrt(sp.nsimplify(lam))


def unit(x):
    x = M(x)
    return x / x.norm()


def _scale_tex(k):
    """1/sqrt(k) as TeX; k a positive integer"""
    r = sp.sqrt(k)
    if r.is_Integer:
        return "" if r == 1 else rf"\frac{{1}}{{{r}}}"
    return rf"\frac{{1}}{{\sqrt{{{k}}}}}"


def _num(t):
    """a tuple entry: a negative number braced, so TeX reads the minus as a sign and not as subtraction"""
    return f"{{{t}}}" if t < 0 else str(t)


def nvec(x, col=False):
    """an integer vector x normalized: TeX '\\frac{1}{\\sqrt{6}}(1,-2,1)' (col=True: a column pmatrix)"""
    x = [int(t) for t in x]
    k = sum(t * t for t in x)
    body = (r"\begin{pmatrix}" + r"\\".join(map(str, x)) + r"\end{pmatrix}") if col else "(" + ",".join(map(_num, x)) + ")"
    return _scale_tex(k) + body


def svec(x, k):
    """an integer vector x times 1/sqrt(k): '\\frac{1}{\\sqrt{2}}(3,3,0)'"""
    return _scale_tex(k) + "(" + ",".join(_num(int(t)) for t in x) + ")"


def ivec(x, col=False):
    x = [int(t) for t in x]
    return (r"\begin{pmatrix}" + r"\\".join(map(str, x)) + r"\end{pmatrix}") if col else "(" + ",".join(map(_num, x)) + ")"


def pm(Mx):
    """pmatrix of an exact sympy matrix"""
    Mx = M(Mx)
    rows = [" & ".join(E(Mx[i, j]) for j in range(Mx.cols)) for i in range(Mx.rows)]
    return r"\begin{pmatrix}" + r" \\ ".join(rows) + r"\end{pmatrix}"


def cols(*xs):
    """(TeX, sympy matrix) of the matrix whose columns are the integer vectors xs, each normalized.
    Entries are written x/sqrt(k) with the column's own k, the way the course writes them."""
    tex_cols, mats = [], []
    for x in xs:
        x = [int(t) for t in x]
        k = sum(t * t for t in x)
        r = sp.sqrt(k)
        cells = []
        for t in x:
            if t == 0:
                cells.append("0")
            elif r.is_Integer:
                cells.append(E(sp.Rational(t, int(r))))
            else:
                cells.append(("-" if t < 0 else "") + rf"\frac{{{abs(t)}}}{{\sqrt{{{k}}}}}")
        tex_cols.append(cells)
        mats.append(unit(x))
    n = len(xs[0])
    rows = [" & ".join(c[i] for c in tex_cols) for i in range(n)]
    return r"\begin{pmatrix}" + r" \\ ".join(rows) + r"\end{pmatrix}", M.hstack(*mats)


def cols_T(*xs):
    """(TeX, matrix) of V^T: the normalized vectors xs written as ROWS"""
    _, Vm = cols(*xs)
    tex_rows = []
    for x in xs:
        x = [int(t) for t in x]
        k = sum(t * t for t in x)
        r = sp.sqrt(k)
        cells = []
        for t in x:
            if t == 0:
                cells.append("0")
            elif r.is_Integer:
                cells.append(E(sp.Rational(t, int(r))))
            else:
                cells.append(("-" if t < 0 else "") + rf"\frac{{{abs(t)}}}{{\sqrt{{{k}}}}}")
        tex_rows.append(" & ".join(cells))
    return r"\begin{pmatrix}" + r" \\ ".join(tex_rows) + r"\end{pmatrix}", Vm.T


def S_mat(m, n, sigmas):
    S = sp.zeros(m, n)
    for i, s in enumerate(sigmas):
        S[i, i] = s
    return S


def eig_desc(Mx):
    """eigenvalues with multiplicity, descending (exact)"""
    out = []
    for lam, k in M(Mx).eigenvals().items():
        out += [sp.nsimplify(lam)] * k
    return sorted(out, key=lambda t: -float(t))


def is_orth(Q):
    return sp.simplify(Q.T * Q - sp.eye(Q.cols)) == sp.zeros(Q.cols, Q.cols)


def check_svd(A, U, S, V):
    """asserts: U, V orthogonal, S the right size with descending non-negative diagonal, U S V^T == A"""
    A = M(A)
    m, n = A.shape
    assert U.shape == (m, m) and V.shape == (n, n) and S.shape == (m, n)
    assert is_orth(U) and is_orth(V)
    d = [S[i, i] for i in range(min(m, n))]
    assert all(x >= 0 for x in d) and all(d[i] >= d[i + 1] for i in range(len(d) - 1))
    assert all(S[i, j] == 0 for i in range(m) for j in range(n) if i != j)
    assert sp.simplify(U * S * V.T - A) == sp.zeros(m, n)
    return True


def is_eigvec(Mx, lam, x):
    x = M(x)
    return x != sp.zeros(*x.shape) and sp.simplify(M(Mx) * x - lam * x) == sp.zeros(*x.shape)


def same_dir(a, b):
    """b is a positive multiple of a"""
    a, b = M(a), M(b)
    return sp.simplify(unit(a) - unit(b)) == sp.zeros(*a.shape)


# ---------------------------------------------------------------- HTML
def line(id_, tex, cls="", hidden=True):
    return f'<div id="{id_}" class="sv-line {cls}{" h" if hidden else ""}">$\\displaystyle {tex}$</div>'


def lines(*items, cls=""):
    return f'<div class="sv-stack {cls}">' + "".join(items) + "</div>"


def row(*items, ltr=False):
    """items side by side (RTL like the text; ltr=True for math read left to right)"""
    return f'<div class="sv-row"{' dir="ltr" style="direction:ltr"' if ltr else ""}>' + "".join(items) + "</div>"


def note(id_, html, hidden=True):
    return f'<div id="{id_}" class="sv-note{" h" if hidden else ""}">{html}</div>'


def shapes(pfx, m, n, unit_px=54, hidden=True):
    """A (m x n) = U (m x m) S (m x n) V^T (n x n) as proportional boxes, S with its diagonal drawn"""
    h = " h" if hidden else ""

    def box(id_, name, r, c, cls, diag=False):
        w, ht = c * unit_px, r * unit_px
        d = ""
        if diag:
            k = min(r, c)
            d = "".join(f'<i class="sv-dot" style="left:{(i + .5) * unit_px - 9}px;top:{(i + .5) * unit_px - 9}px"></i>'
                        for i in range(k))
        return (f'<div id="{pfx}-{id_}" class="sv-term{h}"><div class="sv-box {cls}" style="width:{w}px;height:{ht}px">{d}'
                f'<span class="sv-bname">${name}$</span></div><div class="sv-blab">${r}\\times {c}$</div></div>')
    return (f'<div class="sv-shapes" dir="ltr">{box("A", "A", m, n, "a")}'
            f'<div id="{pfx}-eq" class="sv-op{h}">$=$</div>{box("U", "U", m, m, "u")}{box("S", "S", m, n, "s", True)}'
            f'{box("Vt", "V^T", n, n, "v")}</div>')


def assembly(pfx, A_tex, U_tex, S_tex, Vt_tex, hidden=True, labels=("U", "S", "V^T")):
    h = " h" if hidden else ""

    def term(id_, tex, lab):
        return (f'<div id="{pfx}-{id_}" class="sv-term{h}"><div class="sv-tm">$\\displaystyle {tex}$</div>'
                f'<div class="sv-blab">${lab}$</div></div>')
    a = term("A", A_tex, "A") if A_tex else ""
    eq = f'<div id="{pfx}-eq" class="sv-op{h}">$=$</div>' if A_tex else ""
    return (f'<div class="sv-asm" dir="ltr">{a}{eq}{term("U", U_tex, labels[0])}{term("S", S_tex, labels[1])}'
            f'{term("Vt", Vt_tex, labels[2])}</div>')
