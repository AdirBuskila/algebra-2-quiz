# -*- coding: utf-8 -*-
"""Machine check of the guided SVD course (courses/svd/C01..C08.js).

Every stored answer is recomputed with sympy and asserted: numeric answers, the correct option of every
multiple-choice question (each option is evaluated as a claim, exactly one holds and it is correctId),
the key lines of order / findbug steps, the full-decomposition pipeline and the reconstruction U S V^T = A.

Run from the app root:  PYTHONUTF8=1 py -I tools/verify/needhelp/svd/check.py   (ASCII output, exit 1 on failure)
"""
import json
import os
import re
import subprocess
import sys

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
M = sp.Matrix
R = sp.Rational
sqrt = sp.sqrt
bad = []
n_ok = 0


def ok(name, cond, info=""):
    global n_ok
    if cond:
        n_ok += 1
    else:
        bad.append(name)
        print("FAIL " + name + (" " + info if info else ""))


def squash(s):
    return re.sub(r"\s+", "", s)


# ---------------------------------------------------------------- load the level files
raw = subprocess.run(["node", os.path.join(ROOT, "tools", "course_load.js")], capture_output=True, cwd=ROOT, check=True).stdout
loaded = json.loads(raw.decode("utf-8"))
assert not loaded["errors"], loaded["errors"]
LV = {d["level"]["id"]: d["level"] for d in loaded["levels"] if d["courseId"] == "svd"}
assert sorted(LV) == ["C%02d" % i for i in range(1, 9)], sorted(LV)
Q = {}
for lid, lv in LV.items():
    for q in lv["questions"]:
        if "bankId" not in q:
            Q[q["id"]] = q


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)


def step(qid):
    return Q[qid]["step"]


def num(qid, expected, tol=0):
    st = step(qid)
    diff = abs(float(sp.N(expected, 30)) - float(st["answer"]))
    ok(qid + " numeric answer", diff <= (tol if tol else 1e-9), "expected %s stored %s" % (expected, st["answer"]))
    ok(qid + " tol covers rounding", st.get("tol", 0) == tol)


def mcq(qid, claims):
    """claims: list of (signature substring, bool) in the stored option order. Exactly one claim holds: correctId."""
    q = Q[qid]
    opts = q["options"]
    ok(qid + " option count", len(opts) == len(claims), "%d vs %d" % (len(opts), len(claims)))
    true_ids = []
    for o, (sig, val) in zip(opts, claims):
        ok(qid + " option " + o["id"] + " matches its claim text", squash(sig) in squash(o["value"]), "sig=%s value=%s" % (sig, o["value"]))
        if val:
            true_ids.append(o["id"])
    ok(qid + " exactly one true option and it is correctId", true_ids == [q["correctId"]], "true=%s stored=%s" % (true_ids, q["correctId"]))


def tex(m):
    """pmatrix body of an integer / rational matrix, for matching the stored prompt text."""
    return "\\\\".join("&".join(str(x) for x in m.row(i)) for i in range(m.rows))


def in_text(qid, fragment):
    blob = " ".join(strings(Q[qid]))
    ok(qid + " text contains " + fragment[:30], squash(fragment) in squash(blob), fragment)


def unit(v):
    return sp.simplify(v.dot(v)) == 1


def is_orth(Mx):
    return sp.simplify(Mx.T * Mx - sp.eye(Mx.cols)) == sp.zeros(Mx.cols, Mx.cols)


def is_svd(U, S, V, A):
    try:
        return is_orth(U) and is_orth(V) and sp.simplify(U * S * V.T - A) == sp.zeros(*A.shape)
    except Exception:
        return False


def svd_exact(A):
    """The course recipe in exact arithmetic: A^T A -> sigma, V -> u_i = A v_i / sigma_i -> complete U by Gram-Schmidt."""
    m, n = A.shape
    if n > m:
        U_, S_, V_ = svd_exact(A.T)
        return V_, S_.T, U_
    ev = sorted(((e[0], x) for e in (A.T * A).eigenvects() for x in e[2]), key=lambda t: -float(t[0]))
    vs = []
    for lam, x in ev:
        for g in vs:
            x = x - (g.T * x)[0] * g
        vs.append((x / x.norm()).applyfunc(sp.simplify))
    sig = [sp.simplify(sqrt(l)) for l, _ in ev]
    us = [(A * vs[i] / sig[i]).applyfunc(sp.simplify) for i in range(n) if sig[i] != 0]
    for k in range(m):
        if len(us) == m:
            break
        w = sp.eye(m)[:, k]
        for g in us:
            w = w - (g.T * w)[0] * g
        w = w.applyfunc(sp.simplify)
        if w.norm() != 0:
            us.append((w / w.norm()).applyfunc(sp.simplify))
    S_ = sp.zeros(m, n)
    for i in range(n):
        S_[i, i] = sig[i]
    return M.hstack(*us), S_, M.hstack(*vs)


def vec(*c):
    return M(list(c))


s2, s3, s5, s6 = sqrt(2), sqrt(3), sqrt(5), sqrt(6)

# ================================================================ C01
# the running 3x2 example: A = [[1,1],[0,1],[1,0]] from the lesson / brief
A0 = M([[1, 1], [0, 1], [1, 0]])
v1 = vec(1, 1) / s2
v2 = vec(1, -1) / s2
sig1, sig2 = s3, 1
u1 = A0 * v1 / sig1
u2 = A0 * v2 / sig2
u3 = vec(1, -1, -1) / s3
ok("example u1 = (2,1,1)/sqrt6", sp.simplify(u1 - vec(2, 1, 1) / s6) == sp.zeros(3, 1))
ok("example u2 = (0,-1,1)/sqrt2", sp.simplify(u2 - vec(0, -1, 1) / s2) == sp.zeros(3, 1))
ok("example cross product (2,1,1)x(0,-1,1) = (2,-2,-2)", vec(2, 1, 1).cross(vec(0, -1, 1)) == vec(2, -2, -2))
U0 = M.hstack(u1, u2, u3)
V0 = M.hstack(v1, v2)
S0 = M([[s3, 0], [0, 1], [0, 0]])
ok("example reconstruction U S V^T = A (3x2)", is_svd(U0, S0, V0, A0))
ok("example A^T A eigenvalues 3,1", (A0.T * A0).eigenvals() == {3: 1, 1: 1})
ok("example Av1 = sigma1 u1, Av2 = sigma2 u2", sp.simplify(A0 * v1 - sig1 * u1) == sp.zeros(3, 1) and sp.simplify(A0 * v2 - sig2 * u2) == sp.zeros(3, 1))
ok("example completion dot products 0", (u3.T * u1)[0] == 0 and (u3.T * u2)[0] == 0)


def dims_text(a, b, c, d, e, f):
    return "$U$ מסדר $%s\\times%s$, $S$ מסדר $%s\\times%s$, $V$ מסדר $%s\\times%s$" % (a, b, c, d, e, f)


m_, n_ = 4, 3
A4 = sp.zeros(m_, n_)
want = ((m_, m_), (m_, n_), (n_, n_))
cands = [((4, 4), (4, 3), (3, 3)), ((3, 3), (4, 3), (4, 4)), ((4, 4), (3, 3), (3, 3)), ((4, 3), (3, 3), (3, 3))]
mcq("C01-Q1", [(dims_text(*c[0], *c[1], *c[2]), c == want) for c in cands])
num("C01-Q2", 5)
in_text("C01-Q2", "2\\times5")
Sq3 = sp.diag(4, 2, 0)
in_text("C01-Q3", "4&0&0\\\\0&2&0\\\\0&0&0")
num("C01-Q3", Sq3.rank())

# Q4: which product equals A (A = A0, 3x2, with the exact SVD above)
# a generic 3x2 example whose V is not symmetric (so that V^T and V really differ)
Uc = M([[1, 0, 0], [0, R(3, 5), -R(4, 5)], [0, R(4, 5), R(3, 5)]])
Sc = M([[3, 0], [0, 1], [0, 0]])
Vc = M([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]])
A_q4 = Uc * Sc * Vc.T
ok("C01-Q4 generic example is a valid SVD with V != V^T", is_svd(Uc, Sc, Vc, A_q4) and Vc != Vc.T)
Ts = {
    "A=U^TSV": lambda: Uc.T * Sc * Vc,
    "A=USV^T": lambda: Uc * Sc * Vc.T,
    "A=VSU^T": lambda: Vc * Sc * Uc.T,
    "A=USV": lambda: Uc * Sc * Vc,
}


def prod_equals(f):
    try:
        P = f()
        return P.shape == A_q4.shape and sp.simplify(P - A_q4) == sp.zeros(*A_q4.shape)
    except Exception:
        return False


mcq("C01-Q4", [(k, prod_equals(f)) for k, f in Ts.items()])


def valid_S_for(S, m, n):
    if S.shape != (m, n):
        return False
    d = [S[i, i] for i in range(min(m, n))]
    off = all(S[i, j] == 0 for i in range(m) for j in range(n) if i != j)
    return off and all(x >= 0 for x in d) and all(d[i] >= d[i + 1] for i in range(len(d) - 1))


mcq("C01-Q5", [
    ("1&0&0\\\\0&\\sqrt5&0", valid_S_for(M([[1, 0, 0], [0, s5, 0]]), 2, 3)),
    ("\\sqrt5&0\\\\0&1", valid_S_for(M([[s5, 0], [0, 1]]), 2, 3)),
    ("\\sqrt5&0&0\\\\0&1&0", valid_S_for(M([[s5, 0, 0], [0, 1, 0]]), 2, 3)),
    ("\\sqrt5&0&0\\\\0&-1&0", valid_S_for(M([[s5, 0, 0], [0, -1, 0]]), 2, 3)),
])

# ================================================================ C02
A26 = sp.zeros(2, 6)
sizes = {"AA^T": (A26 * A26.T).shape, "A^TA": (A26.T * A26).shape}
small = min(sizes, key=lambda k: sizes[k][0])


def q1_claim(name, k):
    return name == small and k == sizes[name][0]


mcq("C02-Q1", [
    ("$A^TA$ מסדר $2\\times2$", q1_claim("A^TA", 2)),
    ("$AA^T$ מסדר $6\\times6$", q1_claim("AA^T", 6)),
    ("$AA^T$ מסדר $2\\times2$", q1_claim("AA^T", 2)),
    ("$A^TA$ מסדר $6\\times6$", q1_claim("A^TA", 6)),
])
A_w = M([[1, 1, 0], [0, 1, 1]])
in_text("C02-Q2", "1&1&0\\\\0&1&1")
ok("C02-Q2 AA^T = [[2,1],[1,2]]", A_w * A_w.T == M([[2, 1], [1, 2]]))
ok("C02-Q2 sum of eigenvalues = trace = sum of squares of entries", sum((A_w * A_w.T).eigenvals()) == (A_w * A_w.T).trace() == sum(x * x for x in A_w))
num("C02-Q2", (A_w * A_w.T).trace())


def ev_multiset(Mx):
    ev = []
    for k, mult in Mx.eigenvals().items():
        ev += [sp.nsimplify(k)] * mult
    return sorted(ev, key=lambda x: float(x), reverse=True)


ok("C02-Q3 A^TA of the example has eigenvalues 3,1", ev_multiset(A0.T * A0) == [3, 1])
true3 = ev_multiset(A0 * A0.T)
ok("C02-Q3 AA^T eigenvalues are 3,1,0", true3 == [3, 1, 0])
mcq("C02-Q3", [
    ("9,\\ 1,\\ 0", sorted([9, 1, 0], reverse=True) == true3),
    ("\\sqrt3,\\ 1,\\ 0", sorted([s3, 1, 0], key=float, reverse=True) == true3),
    ("3,\\ 1,\\ 1", [3, 1, 1] == true3),
    ("3,\\ 1,\\ 0", [3, 1, 0] == true3),
])

# Q4: the short route for a wide matrix really produces a valid SVD (A 2x4)
Aw = M([[1, 1, 0, 0], [0, 1, 1, 0]])
ok("C02-Q4 m<n so A A^T is the smaller matrix", (Aw * Aw.T).shape[0] < (Aw.T * Aw).shape[0])
AAT = Aw * Aw.T
ev = sorted(AAT.eigenvects(), key=lambda t: -float(t[0]))
sigs = [sqrt(e[0]) for e in ev]
Ucols = [(e[2][0] / e[2][0].norm()).applyfunc(sp.simplify) for e in ev]
Vcols = [(Aw.T * Ucols[i] / sigs[i]).applyfunc(sp.simplify) for i in range(2)]
ok("C02-Q4 v_i = A^T u_i / sigma_i are orthonormal", all(unit(v) for v in Vcols) and sp.simplify((Vcols[0].T * Vcols[1])[0]) == 0)
ker = Aw.nullspace()
G = list(Vcols)
for k in ker:
    w = k
    for g in G:
        w = w - (g.T * w)[0] / (g.T * g)[0] * g
    if sp.simplify(w.norm()) != 0:
        G.append((w / w.norm()).applyfunc(sp.simplify))
Vfull = M.hstack(*G[:4])
Sfull = sp.zeros(2, 4)
Sfull[0, 0], Sfull[1, 1] = sigs
ok("C02-Q4 completed V is 4x4 and U S V^T = A", Vfull.shape == (4, 4) and is_svd(M.hstack(*Ucols), Sfull, Vfull, Aw))
st = step("C02-Q4")
ok("C02-Q4 five lines", len(st["lines"]) == 5 and "AA^T" in st["lines"][0] and "A^Tu_i" in st["lines"][2])
Ae = M([[1, 0, 2], [2, 0, 1]])
in_text("C02-Q5", "1&0&2\\\\2&0&1")
ok("C02-Q5 AA^T = [[5,4],[4,5]] and A^TA = [[5,0,4],[0,0,0],[4,0,5]]", Ae * Ae.T == M([[5, 4], [4, 5]]) and Ae.T * Ae == M([[5, 0, 4], [0, 0, 0], [4, 0, 5]]))
ok("C02-Q5 eigenvalues of A^TA are 9,1,0", ev_multiset(Ae.T * Ae) == [9, 1, 0])
num("C02-Q5", max((Ae.T * Ae).eigenvals(), key=float))

# ================================================================ C03
A1 = M([[1, 2], [2, 1], [0, 0]])
in_text("C03-Q1", "1&2\\\\2&1\\\\0&0")
in_text("C03-Q1", "5&4\\\\4&5")
ok("C03-Q1 A^TA", A1.T * A1 == M([[5, 4], [4, 5]]))
sv1 = sorted([sp.simplify(x) for x in A1.singular_values()], key=float, reverse=True)
ok("C03-Q1 singular values 3,1", sv1 == [3, 1])
num("C03-Q1", sv1[0])
S1 = M([[3, 0], [0, 1], [0, 0]])
mcq("C03-Q2", [
    ("1&0\\\\0&3\\\\0&0", M([[1, 0], [0, 3], [0, 0]]) == S1),
    ("3&0&0\\\\0&1&0", M([[3, 0, 0], [0, 1, 0]]) == S1),
    ("9&0\\\\0&1\\\\0&0", M([[9, 0], [0, 1], [0, 0]]) == S1),
    ("3&0\\\\0&1\\\\0&0", M([[3, 0], [0, 1], [0, 0]]) == S1),
])
A2 = M([[1, 2], [2, 4]])
in_text("C03-Q3", "5&10\\\\10&20")
ok("C03-Q3 A^TA and its eigenvalues 25, 0", A2.T * A2 == M([[5, 10], [10, 20]]) and (A2.T * A2).eigenvals() == {25: 1, 0: 1})
num("C03-Q3", A2.rank())
ok("C03-Q3 rank equals number of nonzero singular values", A2.rank() == len([x for x in A2.singular_values() if sp.simplify(x) != 0]))
in_text("C03-Q4", "1&1&0\\\\0&1&1")
num("C03-Q4", max(A_w.singular_values(), key=float), 0.01)
# Q5: the recipe in the stored order, run on a sample, reproduces sympy's singular values
Asm = M([[1, 2], [2, 1], [0, 0]])
lam_s = sorted((Asm.T * Asm).eigenvals(), key=float, reverse=True)
ok("C03-Q5 recipe result = sympy singular values", [sqrt(x) for x in lam_s] == sorted(Asm.singular_values(), key=float, reverse=True))
ok("C03-Q5 four lines in the recipe order", len(step("C03-Q5")["lines"]) == 4)
# Q6: findbug
st = step("C03-Q6")
L = [squash(x) for x in st["lines"]]
ok("C03-Q6 lines 0..2 are right", "5&4\\\\4&5" in L[0] and "(5-\\lambda)^2-16=0" in L[1] and "\\lambda_1=9" in L[2] and "\\lambda_2=1" in L[2])
ok("C03-Q6 characteristic polynomial roots are 9 and 1", sp.solve((5 - sp.Symbol("l")) ** 2 - 16, sp.Symbol("l")) in ([1, 9], [9, 1]))
ok("C03-Q6 bug line claims sigma1=9 but sqrt(9)=3", "\\sigma_1=9" in L[3] and sqrt(9) == 3 and st["bugIndex"] == 3)

# ================================================================ C04
num("C04-Q1", vec(1, 2, 2).norm())
in_text("C04-Q1", "(1,2,2)")
T = M([[5, 4], [4, 5]])
Tvecs = [vec(1, -1) / s2, vec(1, 1), vec(1, 1) / s2, vec(4, 5) / sqrt(41)]


def eigvec_of(Mx, lam, v):
    return unit(v) and sp.simplify(Mx * v - lam * v) == sp.zeros(Mx.rows, 1)


mcq("C04-Q2", [
    ("\\frac{1}{\\sqrt2}(1,-1)", eigvec_of(T, 9, Tvecs[0])),
    ("(1,1)", eigvec_of(T, 9, Tvecs[1])),
    ("\\frac{1}{\\sqrt2}(1,1)", eigvec_of(T, 9, Tvecs[2])),
    ("\\frac{1}{\\sqrt{41}}(4,5)", eigvec_of(T, 9, Tvecs[3])),
])


def v_ok(Vm, lams):
    return all(eigvec_of(T, lams[i], Vm[:, i]) for i in range(Vm.cols))


mcq("C04-Q3", [
    ("\\frac1{\\sqrt2}\\begin{pmatrix}1&1\\\\-1&1\\end{pmatrix}", v_ok(M([[1, 1], [-1, 1]]) / s2, [9, 1])),
    ("\\frac1{\\sqrt2}\\begin{pmatrix}1&1\\\\1&1\\end{pmatrix}", v_ok(M([[1, 1], [1, 1]]) / s2, [9, 1])),
    ("\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}", v_ok(M([[1, 1], [1, -1]]), [9, 1])),
    ("\\frac1{\\sqrt2}\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}", v_ok(M([[1, 1], [1, -1]]) / s2, [9, 1])),
])
ok("C04-Q3 eigenvalues of A^TA are 9 and 1", T.eigenvals() == {9: 1, 1: 1})
ok("C04-Q3 the correct V is orthogonal", is_orth(M([[1, 1], [1, -1]]) / s2))
st = step("C04-Q4")
L = [squash(x) for x in st["lines"]]
ok("C04-Q4 line 0: A^TA - I", "4&4\\\\4&4" in L[0] and T - sp.eye(2) == M([[4, 4], [4, 4]]))
ok("C04-Q4 line 1: x1+x2=0 describes the kernel", sp.simplify((T - sp.eye(2)) * vec(1, -1)) == sp.zeros(2, 1) and "x_1+x_2=0" in L[1])
ok("C04-Q4 bug line 2: (1,1) is NOT in the kernel", (T - sp.eye(2)) * vec(1, 1) != sp.zeros(2, 1) and "(1,1)" in L[2] and st["bugIndex"] == 2)
ok("C04-Q4 line 3: v2 = (1,-1)/sqrt2 is a unit eigenvector for 1", eigvec_of(T, 1, vec(1, -1) / s2) and "(1,-1)" in L[3])
T3 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
in_text("C04-Q5", "2&1&1\\\\1&2&1\\\\1&1&2")
ok("C04-Q5 eigenvalues 4,1,1 and eigenspace of 1 is x1+x2+x3=0", T3.eigenvals() == {4: 1, 1: 2} and sp.simplify((T3 - sp.eye(3)) * vec(1, -1, 0)) == sp.zeros(3, 1))
vv1 = vec(1, 1, 1) / s3
ok("C04-Q5 v1 is a unit eigenvector for 4", eigvec_of(T3, 4, vv1))


def pair_ok(a, b):
    return eigvec_of(T3, 1, a) and eigvec_of(T3, 1, b) and sp.simplify((a.T * b)[0]) == 0


mcq("C04-Q5", [
    ("\\frac1{\\sqrt2}(1,-1,0)$ ו-$\\frac1{\\sqrt2}(1,0,-1)", pair_ok(vec(1, -1, 0) / s2, vec(1, 0, -1) / s2)),
    ("\\frac1{\\sqrt2}(1,-1,0)$ ו-$\\frac1{\\sqrt3}(1,1,1)", pair_ok(vec(1, -1, 0) / s2, vec(1, 1, 1) / s3)),
    ("\\frac1{\\sqrt2}(1,-1,0)$ ו-$\\frac1{\\sqrt6}(1,1,-2)", pair_ok(vec(1, -1, 0) / s2, vec(1, 1, -2) / s6)),
    ("(1,-1,0)$ ו-$(1,1,-2)", pair_ok(vec(1, -1, 0), vec(1, 1, -2))),
])
ok("C04-Q5 (1,-1,0).(1,0,-1) = 1 so the first pair is not orthogonal", (vec(1, -1, 0).T * vec(1, 0, -1))[0] == 1)

# ================================================================ C05
V1 = vec(1, 1) / s2
V2 = vec(1, -1) / s2
sg1, sg2 = 3, 1
ok("C05 A^TA of [[1,2],[2,1],[0,0]]: v1, v2 eigenvectors for 9, 1", eigvec_of(A1.T * A1, 9, V1) and eigvec_of(A1.T * A1, 1, V2))
Av1 = A1 * V1
num("C05-Q1", sp.simplify(Av1.norm()))
in_text("C05-Q1", "1&2\\\\2&1\\\\0&0")
ok("C05-Q1 |A v1| = sigma1", sp.simplify(Av1.norm()) == sg1)
U1 = (A1 * V1 / sg1).applyfunc(sp.simplify)
U2 = (A1 * V2 / sg2).applyfunc(sp.simplify)
ok("C05 u1 = (1,1,0)/sqrt2 and u2 = (-1,1,0)/sqrt2", U1 == vec(1, 1, 0) / s2 and U2 == vec(-1, 1, 0) / s2)


def same(a, b):
    return sp.simplify(a - b) == sp.zeros(a.rows, 1)


mcq("C05-Q2", [
    ("\\frac1{\\sqrt2}(3,3,0)", same(vec(3, 3, 0) / s2, U1)),
    ("\\frac1{\\sqrt2}(1,-1,0)", same(vec(1, -1, 0) / s2, U1)),
    ("\\frac13(1,1,0)", same(vec(1, 1, 0) / 3, U1)),
    ("\\frac1{\\sqrt2}(1,1,0)", same(vec(1, 1, 0) / s2, U1)),
])
mcq("C05-Q3", [
    ("\\frac1{\\sqrt2}(1,-1,0)", same(vec(1, -1, 0) / s2, U2)),
    ("\\frac1{\\sqrt2}(-1,1,0)", same(vec(-1, 1, 0) / s2, U2)),
    ("\\frac1{\\sqrt2}(1,1,0)", same(vec(1, 1, 0) / s2, U2)),
    ("\\frac1{\\sqrt2}(-3,3,0)", same(vec(-3, 3, 0) / s2, U2)),
])
# Q4: the reasons, each evaluated
AAT1 = A1 * A1.T
w = -U1  # an equally good unit eigenvector of AA^T for 9
sign_issue = eigvec_of(AAT1, 9, w) and sp.simplify(A1 * V1 + sg1 * w) == sp.zeros(3, 1)
ok("C05-Q4 -u1 is a unit eigenvector of AA^T for 9 but gives A v1 = -sigma1 (-u1)", sign_issue)
mcq("C05-Q4", [
    ("ל-$AA^T$ אין וקטורים עצמיים", len(AAT1.eigenvects()) == 0),
    ("נקבעים עד כדי סימן", sign_issue),
    ("ערכים עצמיים שונים מאפס שונים זה מזה", set(ev_multiset(AAT1)) - {0} != set(ev_multiset(A1.T * A1)) - {0}),
    ("$u_i$ חייב להיות שווה ל-$v_i$", U1.shape == V1.shape),
])
# Q5: the recipe gives orthonormal u_i for a sample
ok("C05-Q5 u1, u2 are orthonormal", unit(U1) and unit(U2) and (U1.T * U2)[0] == 0)
ok("C05-Q5 four lines", len(step("C05-Q5")["lines"]) == 4)
A5 = M([[1, 0], [1, 1], [0, 1]])
in_text("C05-Q6", "1&0\\\\1&1\\\\0&1")
ok("C05-Q6 data: sigma1 = sqrt3, v1 = (1,1)/sqrt2", eigvec_of(A5.T * A5, 3, V1) and (A5.T * A5).eigenvals() == {3: 1, 1: 1})
u5 = (A5 * V1 / s3).applyfunc(sp.simplify)
ok("C05-Q6 u1 = (1,2,1)/sqrt6", u5 == vec(1, 2, 1) / s6)
num("C05-Q6", u5[1], 0.01)

# ================================================================ C06
num("C06-Q1", 4 - M([[1, 0], [0, 1], [0, 0], [0, 0]]).rank())
in_text("C06-Q1", "4\\times2")
cr = vec(1, 1, 0).cross(vec(-1, 1, 0))
ok("C06-Q2 cross product is (0,0,2)", cr == vec(0, 0, 2))
num("C06-Q2", cr[2])
uu1, uu2 = vec(1, 1, 0) / s2, vec(-1, 1, 0) / s2


def completes(v, vs):
    return unit(v) and all(sp.simplify((v.T * x)[0]) == 0 for x in vs)


mcq("C06-Q3", [
    ("\\frac1{\\sqrt3}(1,1,1)", completes(vec(1, 1, 1) / s3, [uu1, uu2])),
    ("(0,0,2)", completes(vec(0, 0, 2), [uu1, uu2])),
    ("(1,0,0)", completes(vec(1, 0, 0), [uu1, uu2])),
    ("(0,0,1)", completes(vec(0, 0, 1), [uu1, uu2])),
])
ok("C06-Q3 u1, u2 orthonormal", unit(uu1) and unit(uu2) and (uu1.T * uu2)[0] == 0)
# Q4: A 2x3, v1, v2 given, v3 in ker A
ok("C06-Q4 A^TA and v1, v2 are eigenvectors for 9, 1", eigvec_of(Ae.T * Ae, 9, vec(1, 0, 1) / s2) and eigvec_of(Ae.T * Ae, 1, vec(-1, 0, 1) / s2))
ok("C06-Q4 u1 = Av1/3, u2 = Av2 are unit (sigma 3, 1)",
   unit(Ae * (vec(1, 0, 1) / s2) / 3) and unit(Ae * (vec(-1, 0, 1) / s2)))
in_text("C06-Q4", "1&0&2\\\\2&0&1")
vk = [vec(0, 1, 1) / s2, vec(1, 0, 0), vec(0, 0, 1), vec(0, 1, 0)]
mcq("C06-Q4", [
    ("\\frac1{\\sqrt2}(0,1,1)", sp.simplify(Ae * vk[0]) == sp.zeros(2, 1) and completes(vk[0], [vec(1, 0, 1) / s2, vec(-1, 0, 1) / s2])),
    ("(1,0,0)", sp.simplify(Ae * vk[1]) == sp.zeros(2, 1) and completes(vk[1], [vec(1, 0, 1) / s2, vec(-1, 0, 1) / s2])),
    ("(0,0,1)", sp.simplify(Ae * vk[2]) == sp.zeros(2, 1) and completes(vk[2], [vec(1, 0, 1) / s2, vec(-1, 0, 1) / s2])),
    ("(0,1,0)", sp.simplify(Ae * vk[3]) == sp.zeros(2, 1) and completes(vk[3], [vec(1, 0, 1) / s2, vec(-1, 0, 1) / s2])),
])
vfull = M.hstack(vec(1, 0, 1) / s2, vec(-1, 0, 1) / s2, vec(0, 1, 0))
Sw = M([[3, 0, 0], [0, 1, 0]])
Uw = M.hstack(Ae * (vec(1, 0, 1) / s2) / 3, Ae * (vec(-1, 0, 1) / s2))
ok("C06-Q4 full reconstruction with v3 = (0,1,0)", is_svd(Uw.applyfunc(sp.simplify), Sw, vfull, Ae))
# Q5: rank-1 matrix
vr1 = vec(1, 2) / s5
ok("C06-Q5 A^TA = [[5,10],[10,20]], v1 = (1,2)/sqrt5 eigenvector for 25, sigma = 5, 0",
   eigvec_of(A2.T * A2, 25, vr1) and (A2.T * A2).eigenvals() == {25: 1, 0: 1})
ur1 = (A2 * vr1 / 5).applyfunc(sp.simplify)
ok("C06-Q5 u1 = (1,2)/sqrt5", ur1 == vec(1, 2) / s5)
in_text("C06-Q5", "1&2\\\\2&4")
mcq("C06-Q5", [
    ("\\frac1{\\sqrt5}(2,1)", completes(vec(2, 1) / s5, [ur1])),
    ("\\frac1{\\sqrt5}(1,2)", completes(vec(1, 2) / s5, [ur1])),
    ("(-2,1)", completes(vec(-2, 1), [ur1])),
    ("\\frac1{\\sqrt5}(-2,1)", completes(vec(-2, 1) / s5, [ur1])),
])
ok("C06-Q5 full SVD with u2 = (-2,1)/sqrt5, v2 = (-2,1)/sqrt5 reconstructs A",
   is_svd(M.hstack(ur1, vec(-2, 1) / s5), M([[5, 0], [0, 0]]), M.hstack(vr1, vec(-2, 1) / s5), A2))
# Q6: sample 3x2 rank 2 pipeline (the lesson example) = cross product + normalise
cp = vec(2, 1, 1).cross(vec(0, -1, 1))
ok("C06-Q6 pipeline: cross product normalised is u3 = (1,-1,-1)/sqrt3 and U^T U = I", sp.simplify(cp / cp.norm() - u3) == sp.zeros(3, 1) and is_orth(U0) and cp != cp / cp.norm())
ok("C06-Q6 four lines", len(step("C06-Q6")["lines"]) == 4)

# ================================================================ C07
V1c, V2c = V1, V2
Uf = M.hstack(U1, U2, vec(0, 0, 1))
Sf = M([[3, 0], [0, 1], [0, 0]])
Vf = M.hstack(V1c, V2c)
ok("C07 base decomposition of [[1,2],[2,1],[0,0]] is valid", is_svd(Uf, Sf, Vf, A1))
dU_a = Uf.copy(); dU_a[:, 0] = -dU_a[:, 0]
Vb = Vf.copy(); Vb[:, 1] = 2 * Vb[:, 1]
dU_c = Uf.copy(); dU_c[:, 0] = -dU_c[:, 0]
Vc2 = Vf.copy(); Vc2[:, 0] = -Vc2[:, 0]
Sd = M([[1, 0], [0, 3], [0, 0]])
mcq("C07-Q1", [
    ("$u_1$ ב-$-u_1$ בלבד", is_svd(dU_a, Sf, Vf, A1)),
    ("$v_2$ ב-$2v_2$", is_svd(Uf, Sf, Vb, A1)),
    ("$u_1$ ב-$-u_1$ וגם את $v_1$ ב-$-v_1$", is_svd(dU_c, Sf, Vc2, A1)),
    ("$\\sigma_1$ ו-$\\sigma_2$ ב-$S$ בלבד", is_svd(Uf, Sd, Vf, A1)),
])
I2 = sp.eye(2)
P = M([[0, 1], [1, 0]])
Aq = M([[2, 0], [0, 1]])
in_text("C07-Q2", "2&0\\\\0&1")
mcq("C07-Q2", [
    ("U=I,\\ S=\\begin{pmatrix}1&0\\\\0&2\\end{pmatrix},\\ V=I", is_svd(I2, M([[1, 0], [0, 2]]), I2, Aq) and valid_S_for(M([[1, 0], [0, 2]]), 2, 2)),
    ("U=-I", is_svd(-I2, M([[2, 0], [0, 1]]), I2, Aq)),
    ("U=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}", is_svd(P, M([[2, 0], [0, 1]]), I2, Aq)),
    ("U=I,\\ S=\\begin{pmatrix}2&0\\\\0&1\\end{pmatrix},\\ V=I", is_svd(I2, M([[2, 0], [0, 1]]), I2, Aq) and valid_S_for(M([[2, 0], [0, 1]]), 2, 2)),
])
st = step("C07-Q3")
L = [squash(x) for x in st["lines"]]
for need in ("A=\\begin{pmatrix}1&1\\\\0&1\\\\1&0\\end{pmatrix}", "v_1=\\frac1{\\sqrt2}(1,1)", "v_2=\\frac1{\\sqrt2}(1,-1)", "\\sigma_1=\\sqrt3", "u_1=\\frac1{\\sqrt6}(2,1,1)", "u_2=\\frac1{\\sqrt2}(0,-1,1)"):
    ok("C07-Q3 prompt data " + need[:20], squash(need) in squash(st["prompt"]))
ok("C07-Q3 line 0: Av1 = (2,1,1)/sqrt2", same(A0 * v1, vec(2, 1, 1) / s2) and "\\frac1{\\sqrt2}(2,1,1)" in L[0])
ok("C07-Q3 line 1: sigma1 u1 = Av1", same(s3 * u1, vec(2, 1, 1) / s2) and "\\sqrt3\\cdot\\frac1{\\sqrt6}(2,1,1)" in L[1] and L[1].endswith("\\frac1{\\sqrt2}(2,1,1)$"))
ok("C07-Q3 line 2: Av2 = (0,-1,1)/sqrt2", same(A0 * v2, vec(0, -1, 1) / s2) and "(0,-1,1)" in L[2])
ok("C07-Q3 bug line 3: sigma2 u2 = (0,-1,1)/sqrt2, not (0,1,-1)/sqrt2", same(sig2 * u2, vec(0, -1, 1) / s2) and not same(sig2 * u2, vec(0, 1, -1) / s2) and "(0,1,-1)" in L[3] and st["bugIndex"] == 3)
# Q4: two valid decompositions of the same matrix
D1 = (Uf, Sf, Vf)
D2 = (dU_c, Sf, Vc2)
both = is_svd(*D1, A1) and is_svd(*D2, A1)
ok("C07-Q4 two different valid decompositions of one matrix", both and Uf != dU_c)
mcq("C07-Q4", [
    ("פירוק SVD יחיד", not both),
    ("אינו יחיד", both),
    ("חיוביות צודק", not (is_svd(*D1, A1) and is_svd(*D2, A1))),
    ("בהכרח שונים", Sf != Sf),
])
Asq = M([[3, 1], [1, 3], [0, 0]])
in_text("C07-Q5", "3&1\\\\1&3\\\\0&0")
ok("C07-Q5 sum sigma^2 = sum of squared entries = 20", sp.simplify(sum(x ** 2 for x in Asq.singular_values())) == sum(x * x for x in Asq) == 20)
num("C07-Q5", 20)

# ================================================================ bank pulls: exist, topic svd, not held, steps verified
bank = json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf-8"))
bank = bank if isinstance(bank, list) else bank["questions"]
byid = {b["id"]: b for b in bank}
pulls = [q["bankId"] for lv in LV.values() for q in lv["questions"] if "bankId" in q]
ok("bank pulls: at least 6", len(pulls) >= 6, str(pulls))
for pid in pulls:
    b = byid.get(pid)
    ok("bank %s exists, topic svd, not held" % pid, bool(b) and b.get("topic") == "svd" and not b.get("hold"))
boss_ids = [q["bankId"] for q in LV["C08"]["questions"]]
ok("boss is 5 bank pulls only", len(boss_ids) == 5 and all("bankId" in q for q in LV["C08"]["questions"]) and LV["C08"].get("boss") is True)
# the stored solutions of the boss questions: every claimed matrix in the brief-size set really reconstructs (spot check by sympy)
boss_mats = {
    "23A-B-Q5a": M([[1, 0], [0, 3], [0, 4]]),
    "23B-A-Q4a": M([[1, 0, 2], [2, 0, 1]]),
    "24A-A-Q5a": M([[2, 0], [0, 2], [1, s3]]),
    "24B-B-Q5a": M([[2, 1], [1, -2], [0, 2]]),
    "26B-A-Q5c": M([[3, 2], [2, 3], [2, -2]]),
}
for pid, Am in boss_mats.items():
    txt = squash(byid[pid]["question"])
    rows = [[str(x).replace("sqrt(3)", "\\sqrt3") for x in Am.row(i)] for i in range(Am.rows)]
    pm = "\\\\".join("&".join(r) for r in rows)
    ok("boss %s stem holds the matrix" % pid, squash(pm) in txt, pm)
    sv = sorted([sp.simplify(x) for x in Am.singular_values()], key=float, reverse=True)
    ok("boss %s SVD exists with sigma>=0 descending" % pid, all(float(x) >= 0 for x in sv))
    U_, S_, V_ = svd_exact(Am)
    ok("boss %s exact SVD by the course recipe reconstructs A" % pid, is_svd(U_, S_, V_, Am))
    ok("boss %s rank = number of nonzero sigma" % pid, Am.rank() == len([x for x in sv if x != 0]))

# ================================================================ lint-style scans over every authored string
FORBID = re.compile(r"האפשרות|התשובה ה(ראשונה|שנייה|שלישית|רביעית)|בזוג ה(ראשון|שני)|במטריצה ה(ראשונה|שנייה|שלישית|רביעית)|\([אבגד]\)|תשובות? [אבגד]\b|option [abcd]\b|the (first|second|third|fourth) option")


for lid, lv in LV.items():
    for s in strings(lv):
        ok(lid + " no positional citation: " + s[:40], not FORBID.search(s), s[:80])
        for mm in re.finditer(r"\$\$?([^$]+)\$\$?", s):
            ok(lid + " no Hebrew inside math: " + mm.group(1)[:30], not re.search(r"[֐-׿]", mm.group(1)), mm.group(1))
    ok(lid + " 4-6 questions or boss", 4 <= len(lv["questions"]) <= 6, str(len(lv["questions"])))
    ok(lid + " source ai-verified", lv["source"] == "ai-verified")

print("checks passed: %d, failed: %d" % (n_ok, len(bad)))
sys.exit(1 if bad else 0)
