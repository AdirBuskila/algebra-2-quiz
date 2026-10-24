# -*- coding: utf-8 -*-
"""Machine check of every stored answer in courses/orthodiag (levels C01..C08; C09 is bank questions).

Run from the app root:   PYTHONUTF8=1 py -I tools/verify/needhelp/orthodiag/check.py
The level files are loaded through tools/course_load.js, so the check reads exactly what ships.
For every multiple-choice question each option is mapped to a python object and tested by sympy:
exactly the stored correct option must satisfy the predicate. Numeric answers are recomputed.
Output is ASCII only; exit 1 on any failure or if a question id has no check.
"""
import json
import os
import random
import subprocess
import sys

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
bad = []
checked = set()


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


raw = subprocess.run(["node", os.path.join(ROOT, "tools", "course_load.js")], cwd=ROOT, capture_output=True).stdout
loaded = json.loads(raw.decode("utf-8"))
assert not loaded["errors"], loaded["errors"]
LV = {e["level"]["id"]: e["level"] for e in loaded["levels"] if e["courseId"] == "orthodiag"}
Q = {}
for lid, L in LV.items():
    for q in L["questions"]:
        if "id" in q:
            Q[q["id"]] = q

S = sp.Matrix
R = sp.Rational
sq = sp.sqrt


def pm(rows):
    """latex of a pmatrix option value, exactly as written in the level files"""
    return "$\\begin{pmatrix}" + "\\\\".join("&".join(str(x) for x in r) for r in rows) + "\\end{pmatrix}$"


def is_sym(M):
    return M == M.T


def eigs(M):
    return M.eigenvals()


def flags(M):
    """course convention: positive = >=0, strict = >0. Needs symmetric M."""
    if not is_sym(M):
        return dict(pos=False, spos=False, neg=False, sneg=False)
    ev = list(M.eigenvals().keys())
    return dict(pos=all(e >= 0 for e in ev), spos=all(e > 0 for e in ev),
                neg=all(e <= 0 for e in ev), sneg=all(e < 0 for e in ev))


def orth_diagonalizable(M):
    """independent of the spectral theorem: real eigenvalues, full eigenbasis, eigenspaces mutually orthogonal"""
    n = M.shape[0]
    try:
        ev = M.eigenvects()
    except Exception:
        return False
    if any(sp.im(e[0]) != 0 for e in ev):
        return False
    if sum(len(e[2]) for e in ev) != n:
        return False
    for i in range(len(ev)):
        for j in range(i + 1, len(ev)):
            for u in ev[i][2]:
                for v in ev[j][2]:
                    if sp.simplify((u.T * v)[0]) != 0:
                        return False
    return True


def stored(qid):
    checked.add(qid)
    q = Q[qid]
    return q["step"] if "step" in q else q


def opts_of(q):
    return {o["value"]: o["id"] for o in q["options"]}


def mcq(qid, table, pred):
    """table: {option value string: python object}; pred(obj)->bool; exactly the stored correct option may satisfy it"""
    s = stored(qid)
    om = opts_of(s)
    ok(qid + " options match the check table", set(om) == set(table), "" if set(om) == set(table) else str(set(om) ^ set(table)).encode("ascii", "replace").decode())
    true_ids = sorted(om[v] for v, o in table.items() if v in om and pred(o))
    ok(qid + " exactly the stored option is correct", true_ids == [s["correctId"]], f"true={true_ids} stored={s['correctId']}")


def num(qid, expected):
    s = stored(qid)
    ok(qid + " numeric answer", sp.nsimplify(s["answer"]) == sp.nsimplify(expected) and s.get("tol", 0) == 0, f"stored={s['answer']} expected={expected}")


# ====================================================== C01
mcq("C01-Q1", {pm(m): S(m) for m in ([[2, 3], [1, 1]], [[2, 3], [3, 1]], [[1, 2], [-2, 1]], [[0, 1], [0, 0]])}, orth_diagonalizable)
t = sp.symbols("t")
num("C01-Q2", sp.solve(S([[1, t], [5, 2]]) [0, 1] - S([[1, t], [5, 2]])[1, 0], t)[0])
num("C01-Q3", max(eigs(S([[2, 1], [1, 2]]))))
mcq("C01-Q4", {"$3$ ו-$4$": (3, 4), "$1$ ו-$10$": (1, 10), "$-2$ ו-$-5$": (-2, -5), "$2$ ו-$5$": (2, 5)},
    lambda p: p[0] + p[1] == 7 and p[0] * p[1] == 10)
# the 2x2 shortcut: char poly roots are the eigenvalues, for a symmetric example
lam = sp.symbols("lam")
ok("C01 trace/det example", sp.Poly(lam ** 2 - 4 * lam + 3, lam).all_roots() == [1, 3] and sorted(eigs(S([[2, 1], [1, 2]]))) == [1, 3])
# theorem used in Q5, tested on examples (independent definition of orth. diagonalizability)
rnd = random.Random(7)
sym_ok = True
for _ in range(15):
    a, b, c = (rnd.randint(-4, 4) for _ in range(3))
    sym_ok &= orth_diagonalizable(S([[a, b], [b, c]]))
ok("C01 every sampled symmetric matrix is orthogonally diagonalizable", sym_ok)
ex = {
    "$A$ הפיכה": S([[1, 1], [0, 1]]),                    # invertible, not orthogonally diagonalizable
    "$A=A^T$": None,
    "כל הערכים העצמיים של $A$ שונים זה מזה": S([[1, 1], [0, 2]]),   # distinct eigenvalues, eigenvectors (1,0),(1,1)
    "$A$ אורתוגונלית": S([[0, -1], [1, 0]]),             # rotation
}
ok("C01-Q5 counterexamples: invertible / distinct eigenvalues / orthogonal matrices that are not orth. diagonalizable",
   S([[1, 1], [0, 1]]).det() != 0 and not orth_diagonalizable(S([[1, 1], [0, 1]]))
   and len(S([[1, 1], [0, 2]]).eigenvals()) == 2 and not orth_diagonalizable(S([[1, 1], [0, 2]]))
   and (S([[0, -1], [1, 0]]) * S([[0, -1], [1, 0]]).T == sp.eye(2)) and not orth_diagonalizable(S([[0, -1], [1, 0]])))
s = stored("C01-Q5")
ok("C01-Q5 stored correct option is the symmetry condition", {o["id"]: o["value"] for o in s["options"]}[s["correctId"]] == "$A=A^T$")
num("C01-Q6", S([[3, 1, 1], [1, 3, 1], [1, 1, 3]]).trace())

# ====================================================== C02
A3 = S([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
w1, w2 = S([1, -1, 0]), S([1, 0, -1])
# Q1: symmetric A with eigenvalues 2 and 5, random orthonormal bases: eigenvectors are always orthogonal
ips = []
for (pa, pb, pc) in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (20, 21, 29), (7, 24, 25), (9, 40, 41), (12, 35, 37), (28, 45, 53)]:
    c_, s_ = R(pa, pc), R(pb, pc)
    Qm = S([[c_, -s_], [s_, c_]])
    Am = Qm * sp.diag(2, 5) * Qm.T
    assert is_sym(Am.applyfunc(sp.simplify))
    u, v = Qm[:, 0], Qm[:, 1]
    assert sp.simplify(Am * u - 2 * u) == sp.zeros(2, 1) and sp.simplify(Am * v - 5 * v) == sp.zeros(2, 1)
    ips.append(sp.simplify((u.T * v)[0]))
allzero = all(i == 0 for i in ips)
mcq("C02-Q1", {"$\\langle u,v\\rangle=0$": "zero", "$\\langle u,v\\rangle=10$": "ten", "$\\langle u,v\\rangle\\ne0$": "nonzero",
               "אי אפשר לדעת, צריך לחשב את הווקטורים": "unknown"},
    lambda k: {"zero": allzero, "ten": all(i == 10 for i in ips), "nonzero": all(i != 0 for i in ips),
               "unknown": not allzero and len(set(ips)) > 1}[k])
ok("C02 w1,w2 are eigenvectors of A3 for the eigenvalue 2", A3 * w1 == 2 * w1 and A3 * w2 == 2 * w2)
num("C02-Q2", (w1.T * w2)[0])
num("C02-Q3", (w2.T * w1)[0] / (w1.T * w1)[0])
w2p = w2 - (w2.T * w1)[0] / (w1.T * w1)[0] * w1
v3 = 2 * w2p
ok("C02 GS vector is (1,1,-2), eigen for 2, orthogonal to w1 and to (1,1,1)",
   v3 == S([1, 1, -2]) and A3 * v3 == 2 * v3 and (v3.T * w1)[0] == 0 and (v3.T * S([1, 1, 1]))[0] == 0 and A3 * S([1, 1, 1]) == 5 * S([1, 1, 1]))
num("C02-Q4", (v3.T * v3)[0])
mcq("C02-Q5", {"$\\frac{1}{6}(1,1,-2)$": v3 / 6, "$\\frac{1}{\\sqrt2}(1,1,-2)$": v3 / sq(2), "$\\frac{1}{\\sqrt6}(1,1,-2)$": v3 / sq(6),
               "$(1,1,-2)$, הוא כבר מנורמל": v3},
    lambda v: sp.simplify((v.T * v)[0]) == 1)
s = stored("C02-Q6")
exp_lines = [
    "נתון $Au=\\lambda u$ ו-$Av=\\mu v$, כאשר $\\lambda\\ne\\mu$.",
    "מחשבים $\\lambda\\langle u,v\\rangle=\\langle Au,v\\rangle$.",
    "מהסימטריה של $A$: $\\langle Au,v\\rangle=\\langle u,Av\\rangle$.",
    "ומכאן $\\langle u,Av\\rangle=\\mu\\langle u,v\\rangle$.",
    "לכן $(\\lambda-\\mu)\\langle u,v\\rangle=0$, ומכיוון ש-$\\lambda\\ne\\mu$ מתקבל $\\langle u,v\\rangle=0$.",
]
ok("C02-Q6 proof lines are the chain in the stored order", s["type"] == "order" and s["lines"] == exp_lines)
# identity behind the chain, on random symmetric matrices with distinct eigenvalues
import numpy as np
chain_ok = True
nrng = np.random.default_rng(3)
for _ in range(200):
    G = nrng.integers(-5, 6, size=(4, 4)).astype(float)
    Am = G + G.T
    w, V = np.linalg.eig(Am)          # general eig (not eigh): orthogonality must come from symmetry, not from the routine
    for i in range(4):
        for j in range(4):
            if abs(w[i] - w[j]) > 1e-6:
                u, v = V[:, i], V[:, j]
                chain_ok &= abs(w[i] * (u @ v) - (Am @ u) @ v) < 1e-8 and abs((u @ Am) @ v - w[j] * (u @ v)) < 1e-8 and abs(u @ v) < 1e-8
ok("C02 chain: lambda<u,v> = <Au,v> = <u,Av> = mu<u,v> and <u,v>=0 on random symmetric matrices", chain_ok)

# ====================================================== C03
A2 = S([[2, 1], [1, 2]])
Qa = S([[1, 1], [1, 1]]).copy()
Qa = S([[1, 1], [1, -1]]) / sq(2)           # columns: (1,1)/sqrt2 [eig 3], (1,-1)/sqrt2 [eig 1]
Qb = S([[1, 1], [-1, 1]]) / sq(2)           # columns: (1,-1)/sqrt2 [eig 1], (1,1)/sqrt2 [eig 3]
ok("C03 eigenpairs", A2 * Qa[:, 0] == 3 * Qa[:, 0] and A2 * Qa[:, 1] == Qa[:, 1] and Qa.T * Qa == sp.eye(2))
Dopts = {pm([[1, 0], [0, 3]]): S([[1, 0], [0, 3]]), pm([[3, 0], [0, 3]]): S([[3, 0], [0, 3]]),
         pm([[3, 0], [0, 1]]): S([[3, 0], [0, 1]]), pm([[3, 1], [1, 3]]): S([[3, 1], [1, 3]])}
mcq("C03-Q1", Dopts, lambda D: (Qa * D * Qa.T).applyfunc(sp.simplify) == A2)
Dopts2 = {pm([[1, 0], [0, 3]]): S([[1, 0], [0, 3]]), pm([[3, 0], [0, 1]]): S([[3, 0], [0, 1]]),
          pm([[-1, 0], [0, 1]]): S([[-1, 0], [0, 1]]), pm([[1, 0], [0, 1]]): S([[1, 0], [0, 1]])}
mcq("C03-Q2", Dopts2, lambda D: (Qb * D * Qb.T).applyfunc(sp.simplify) == A2)
Q3 = S([[1, 1], [1, -1]]) / sq(2)
A_ = (Q3 * sp.diag(5, 1) * Q3.T).applyfunc(sp.simplify)
ok("C03-Q3 A = [[3,2],[2,3]]", A_ == S([[3, 2], [2, 3]]))
num("C03-Q3", A_[0, 1])
Qg = S([[1, 2, 2], [2, 1, -2], [-2, 2, -1]]) / 3     # rational orthogonal, not symmetric
Dg = sp.diag(1, 2, 4)
Bm = (Qg * Dg * Qg.T)
ok("C03 generic example valid: Q orthogonal, not symmetric, columns are eigenvectors", Qg.T * Qg == sp.eye(3) and Qg != Qg.T and is_sym(Bm)
   and all(Bm * Qg[:, i] == Dg[i, i] * Qg[:, i] for i in range(3)) and Qg.T * Dg * Qg != Bm)
mcq("C03-Q4", {"$A=Q^TDQ$": lambda Q_, D: Q_.T * D * Q_, "$A=QDQ^T$": lambda Q_, D: Q_ * D * Q_.T,
               "$A=DQQ^T$": lambda Q_, D: D * Q_ * Q_.T, "$A=QQ^TD$": lambda Q_, D: Q_ * Q_.T * D},
    lambda f: f(Qg, Dg) == Bm)
# Q5: A=[[1,2],[2,1]]
A5 = S([[1, 2], [2, 1]])
v1_, v2_ = S([1, 1]) / sq(2), S([1, -1]) / sq(2)
ok("C03-Q5 lines 0-2 true", A5.trace() == 2 and A5.det() == -3 and A5 * v1_ == 3 * v1_ and A5 * v2_ == -v2_ and (v1_.T * v2_)[0] == 0)
Qbug = S.hstack(v2_, v1_)
bugM = (Qbug * sp.diag(3, -1) * Qbug.T).applyfunc(sp.simplify)
goodM = (Qbug * sp.diag(-1, 3) * Qbug.T).applyfunc(sp.simplify)
ok("C03-Q5 line 3 is the bug (mismatched order), the matched order works", bugM == S([[1, -2], [-2, 1]]) and bugM != A5 and goodM == A5)
s = stored("C03-Q5")
ok("C03-Q5 bugIndex", s["bugIndex"] == 3)
num("C03-Q6", (Qa[:, 0].T * A2 * Qa[:, 0])[0])

# ====================================================== C04
A4 = S([[5, 0, 0], [0, 4, 2], [0, 2, 1]])
e1 = S([1, 0, 0])
num("C04-Q1", (A4 * e1)[0])
ok("C04 A e1 = 5 e1", A4 * e1 == 5 * e1)
blk = S([[4, 2], [2, 1]])
ok("C04 block eigenvalues 0 and 5", blk.eigenvals() == {0: 1, 5: 1} and blk.det() == 0 and blk.trace() == 5)
num("C04-Q2", max(blk.eigenvals()))
mcq("C04-Q3", {"$(2,1)$": S([2, 1]), "$(1,2)$": S([1, 2]), "$(1,-2)$": S([1, -2]), "$(-2,-1)$": S([-2, -1])},
    lambda v: blk * v == sp.zeros(2, 1))
ok("C04 A4 eigenvalues {5:2, 0:1}", A4.eigenvals() == {5: 2, 0: 1})
num("C04-Q4", len((A4 - 5 * sp.eye(3)).nullspace()))
ok("C04 eigenvectors are mutually orthogonal as the lesson says",
   all((a.T * b)[0] == 0 for a, b in [(e1, S([0, 2, 1])), (e1, S([0, 1, -2])), (S([0, 2, 1]), S([0, 1, -2]))])
   and A4 * S([0, 2, 1]) == 5 * S([0, 2, 1]) and A4 * S([0, 1, -2]) == sp.zeros(3, 1))
Q4 = S.hstack(e1, S([0, 1, -2]) / sq(5), S([0, 2, 1]) / sq(5))
mcq("C04-Q5", {"$\\operatorname{diag}(5,5,0)$": sp.diag(5, 5, 0), "$\\operatorname{diag}(0,5,5)$": sp.diag(0, 5, 5),
               "$\\operatorname{diag}(5,0,5)$": sp.diag(5, 0, 5), "$\\operatorname{diag}(5,0,0)$": sp.diag(5, 0, 0)},
    lambda D: (Q4 * D * Q4.T).applyfunc(sp.simplify) == A4)
ok("C04 Q4 is orthogonal", sp.simplify(Q4.T * Q4) == sp.eye(3))
ok("C04-Q6 eigenvalues of A3 are 5,2,2", A3.eigenvals() == {5: 1, 2: 2})
num("C04-Q6", A3.det())

# ====================================================== C05
x1, x2 = sp.symbols("x1 x2", real=True)
X = S([x1, x2])
B1 = S([[1, 3], [3, 8]])
form1 = sp.expand((X.T * B1 * X)[0])
mcq("C05-Q1", {"$x_1^2+3x_1x_2+8x_2^2$": x1 ** 2 + 3 * x1 * x2 + 8 * x2 ** 2, "$x_1^2+9x_1x_2+8x_2^2$": x1 ** 2 + 9 * x1 * x2 + 8 * x2 ** 2,
               "$x_1^2+8x_2^2$": x1 ** 2 + 8 * x2 ** 2, "$x_1^2+6x_1x_2+8x_2^2$": x1 ** 2 + 6 * x1 * x2 + 8 * x2 ** 2},
    lambda e: sp.expand(e - form1) == 0)
num("C05-Q2", (S([-3, 1]).T * B1 * S([-3, 1]))[0])
ok("C05 completing the square", sp.expand((x1 + 3 * x2) ** 2 - x2 ** 2 - form1) == 0 and (S([1, 1]).T * B1 * S([1, 1]))[0] == 15)
q3 = 3 * x1 ** 2 - 4 * x1 * x2 + 2 * x2 ** 2
a12 = sp.Poly(q3, x1, x2).coeff_monomial(x1 * x2) / 2
num("C05-Q3", a12)
mcq("C05-Q4", {"$(1,1)$": S([1, 1]), "$(1,-1)$": S([1, -1]), "$(2,1)$": S([2, 1]), "$(1,0)$": S([1, 0])},
    lambda v: (v.T * S([[1, 2], [2, 1]]) * v)[0] < 0)
# Q5: symmetric matrix with eigenvalues 5 and -2 (non-diagonal)
Rm = S([[3, -4], [4, 3]]) / 5
A5s = (Rm * sp.diag(5, -2) * Rm.T).applyfunc(sp.simplify)
neg_exists = any((v.T * A5s * v)[0] < 0 for v in [Rm[:, 1], S([1, 1]), S([1, -1]), S([0, 1]), S([1, 0])])
neg_all_eig = all((v.T * A5s * v)[0] < 0 for v in (Rm[:, 1], 7 * Rm[:, 1], -3 * Rm[:, 1]))
mcq("C05-Q5", {"לא, כי הערך העצמי $5$ גדול ומאזן את $-2$": "a", "לא, כי העקבה $3$ חיובית": "b",
               "כן, כל וקטור עצמי של הערך $-2$ מתאים": "c", "כן, אבל רק אם $A$ אלכסונית": "d"},
    lambda k: {"a": not neg_exists, "b": not neg_exists, "c": neg_exists and neg_all_eig,
               "d": neg_exists and A5s == sp.diag(*[A5s[i, i] for i in range(2)])}[k])
ok("C05-Q5 example matrix is symmetric, non-diagonal, eigenvalues 5,-2", is_sym(A5s) and A5s.eigenvals() == {5: 1, -2: 1} and A5s[0, 1] != 0)
B6 = S([[1, 2], [2, 1]])
mcq("C05-Q6", {"כן, כי איברי האלכסון חיוביים": "a", "לא, כי $x=(1,-1)$ נותן ערך שלילי": "b", "כן, כי $A$ סימטרית": "c", "לא, כי $A$ אינה סימטרית": "d"},
    lambda k: {"a": flags(B6)["spos"], "b": (S([1, -1]).T * B6 * S([1, -1]))[0] < 0, "c": flags(B6)["spos"], "d": not is_sym(B6)}[k])

# ====================================================== C06
Z = sp.zeros(2)
J = S([[1, 1], [1, 1]])
ok("C06 J eigenvalues 2 and 0", J.eigenvals() == {2: 1, 0: 1})
fj = flags(J)
mcq("C06-Q1", {"מוגדרת חיובית לחלוטין": "spos", "מוגדרת חיובית אך לא לחלוטין": "pos_not_s", "אף אחת מהן": "none", "מוגדרת שלילית": "neg"},
    lambda k: {"spos": fj["spos"], "pos_not_s": fj["pos"] and not fj["spos"], "none": not any(fj.values()), "neg": fj["neg"]}[k])
fz = flags(Z)
mcq("C06-Q2", {"מוגדרת חיובית לחלוטין": "spos", "אף אחת מהן": "none", "מוגדרת חיובית וגם מוגדרת שלילית, אך לא לחלוטין": "both", "מוגדרת חיובית בלבד": "pos_only"},
    lambda k: {"spos": fz["spos"], "none": not any(fz.values()), "both": fz["pos"] and fz["neg"] and not fz["spos"] and not fz["sneg"],
               "pos_only": fz["pos"] and not fz["neg"]}[k])
fi = flags(sp.eye(2))
mcq("C06-Q3", {"היא מוגדרת חיובית לחלוטין, ולכן גם מוגדרת חיובית": "a", "היא מוגדרת חיובית לחלוטין, אך לא מוגדרת חיובית": "b",
               "היא מוגדרת חיובית אך לא לחלוטין": "c", "היא מוגדרת שלילית לחלוטין": "d"},
    lambda k: {"a": fi["spos"] and fi["pos"], "b": fi["spos"] and not fi["pos"], "c": fi["pos"] and not fi["spos"], "d": fi["sneg"]}[k])
a_ = sp.symbols("a", real=True)
ok("C06 [[2,a],[a,2]] eigenvalues 2+a, 2-a", set(S([[2, a_], [a_, 2]]).eigenvals()) == {2 + a_, 2 - a_})
cnt = sum(1 for a in range(-12, 13) if flags(S([[2, a], [a, 2]]))["pos"] and not flags(S([[2, a], [a, 2]]))["spos"])
num("C06-Q4", cnt)
ok("C06-Q5 lines 1 and 3 true, line 2 false at a=0", all(
    (flags(sp.diag(a, 4))["spos"] == (a > 0)) and (not flags(sp.diag(a, 4))["neg"]) for a in range(-5, 6))
   and flags(sp.diag(0, 4))["pos"] and not (0 > 0) and S([[0, 0], [0, 4]]).eigenvals() == {0: 1, 4: 1}
   and all(flags(sp.diag(a, 4))["pos"] == (a >= 0) for a in range(-5, 6)))
s = stored("C06-Q5")
ok("C06-Q5 bugIndex", s["bugIndex"] == 2)
spd = [S([[2, 1], [1, 2]]), S([[3, 0, 1], [0, 2, 0], [1, 0, 3]]), sp.eye(3), S([[5, 2], [2, 1]])]
ok("C06 sample strictly positive matrices", all(flags(m)["spos"] for m in spd))
mcq("C06-Q6", {"$A$ אינה הפיכה": lambda m: m.det() == 0, "$A$ גם מוגדרת חיובית": lambda m: flags(m)["pos"],
               "ל-$A$ יש ערך עצמי $0$": lambda m: 0 in m.eigenvals(), "$A$ אינה מוגדרת חיובית": lambda m: not flags(m)["pos"]},
    lambda f: all(f(m) for m in spd))

# ====================================================== C07
num("C07-Q1", S([[2, 1], [1, 3]]).det())


def lead(M):
    return [M[:k, :k].det() for k in range(1, M.shape[0] + 1)]


A7 = S([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
ok("C07-Q2 minors 2,3,4 and eigenvalues", lead(A7) == [2, 3, 4] and set(A7.eigenvals()) == {2, 2 + sq(2), 2 - sq(2)})
f7 = flags(A7)
mcq("C07-Q2", {"מוגדרת חיובית לחלוטין": "spos", "מוגדרת חיובית אך לא לחלוטין": "pos_not_s", "מוגדרת שלילית לחלוטין": "sneg", "אף אחת מהן": "none"},
    lambda k: {"spos": f7["spos"], "pos_not_s": f7["pos"] and not f7["spos"], "sneg": f7["sneg"], "none": not any(f7.values())}[k])
ok("C07 Sylvester agrees with eigenvalues on random symmetric matrices",
   all((all(m > 0 for m in lead(M)) == flags(M)["spos"]) for M in
       [S([[a, b], [b, c]]) for a in range(-3, 4) for b in range(-3, 4) for c in range(-3, 4)]))
# leading minors with a zero do not decide "positive" (3x3 pair with equal leading minors 1,0,0)
Pa, Pb = S([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), S([[1, 1, 0], [1, 1, 0], [0, 0, -1]])
ok("C07 same leading minors, different positivity", lead(Pa) == lead(Pb) == [1, 0, 0] and flags(Pa)["pos"] and not flags(Pb)["pos"])
A73 = J
f73 = flags(A73)
undecided = lead(Pa) == lead(Pb) and flags(Pa)["pos"] != flags(Pb)["pos"]
mcq("C07-Q3", {"היא מוגדרת חיובית לחלוטין, כי $\\Delta_1>0$": "a", "היא אינה מוגדרת חיובית כלל, כי $\\Delta_2=0$": "b",
               "היא אינה מוגדרת חיובית לחלוטין, והקריטריון אינו מכריע אם היא מוגדרת חיובית": "c", "היא מוגדרת שלילית": "d"},
    lambda k: {"a": f73["spos"], "b": not f73["pos"], "c": (not f73["spos"]) and undecided, "d": f73["neg"]}[k])
ok("C07-Q3 minors 1,0", lead(A73) == [1, 0])
M4 = S([[0, 0], [0, -1]])
ok("C07-Q4 minors 0,0 and eigenvalues 0,-1", lead(M4) == [0, 0] and M4.eigenvals() == {0: 1, -1: 1})
f4 = flags(M4)
mcq("C07-Q4", {"כן, כי כל המינורים המובילים אי-שליליים": "a", "כן, כי היא סימטרית": "b",
               "לא, כי $x=(0,1)$ נותן $x^TAx=-1<0$": "c", "כן, כי שני הערכים העצמיים אי-שליליים": "d"},
    lambda k: {"a": f4["pos"], "b": f4["pos"], "c": (not f4["pos"]) and (S([0, 1]).T * M4 * S([0, 1]))[0] == -1, "d": f4["pos"]}[k])
first = next(a for a in range(-10, 30) if flags(S([[1, 2], [2, a]]))["spos"])
num("C07-Q5", first)
ok("C07-Q5 a=4 gives minor 0", lead(S([[1, 2], [2, 4]])) == [1, 0] and not flags(S([[1, 2], [2, 4]]))["spos"])
A76 = S([[-2, 1], [1, -2]])
ok("C07-Q6 minors -2,3 and eigenvalues -1,-3", lead(A76) == [-2, 3] and A76.eigenvals() == {-1: 1, -3: 1})
f76 = flags(A76)
mcq("C07-Q6", {"מוגדרת חיובית לחלוטין": "spos", "מוגדרת שלילית לחלוטין": "sneg", "אף אחת מהן": "none", "מוגדרת חיובית אך לא לחלוטין": "pos_not_s"},
    lambda k: {"spos": f76["spos"], "sneg": f76["sneg"], "none": not any(f76.values()), "pos_not_s": f76["pos"] and not f76["spos"]}[k])

# ====================================================== C08
ok("C08 [[3,a],[a,3]] eigenvalues 3+a, 3-a", set(S([[3, a_], [a_, 3]]).eigenvals()) == {3 + a_, 3 - a_})
num("C08-Q1", max(a for a in range(-12, 13) if flags(S([[3, a], [a, 3]]))["spos"]))
num("C08-Q2", sum(1 for a in range(-12, 13) if flags(S([[3, a], [a, 3]]))["pos"]))
b_ = sp.symbols("b", real=True)
M3 = S([[1, 0, a_], [0, 2, 0], [a_, b_, 1]])
num("C08-Q3", sp.solve(M3[1, 2] - M3[2, 1], b_)[0])
Mp = S([[a_, 0, 2], [0, a_, 0], [2, 0, a_]])
ok("C08 M(a) eigenvalues a-2, a, a+2", set(Mp.eigenvals()) == {a_ - 2, a_, a_ + 2})
f84 = flags(Mp.subs(a_, 2))
mcq("C08-Q4", {"מוגדרת חיובית לחלוטין": "spos", "מוגדרת חיובית אך לא לחלוטין": "pos_not_s", "אף אחת מהן": "none", "מוגדרת שלילית": "neg"},
    lambda k: {"spos": f84["spos"], "pos_not_s": f84["pos"] and not f84["spos"], "none": not any(f84.values()), "neg": f84["neg"]}[k])
num("C08-Q5", sum(1 for a in range(-20, 21) if not flags(Mp.subs(a_, a))["pos"] and not flags(Mp.subs(a_, a))["neg"]))
grid = [R(i, 2) for i in range(-8, 9)]
strict_set = {a for a in grid if all(e > 0 for e in (a ** 2 + 1, 2 * a ** 2, 3))}
mcq("C08-Q6", {"$a>0$": lambda a: a > 0, "לכל $a$": lambda a: True, "$a\\ne0$": lambda a: a != 0, "$a\\ge0$": lambda a: a >= 0},
    lambda f: {a for a in grid if f(a)} == strict_set)

# ====================================================== C09 (boss): bank questions only
bank = json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf-8"))
bank = bank["questions"] if isinstance(bank, dict) else bank
bank_ids = {b["id"]: b for b in bank}
for q in LV["C09"]["questions"]:
    b = bank_ids.get(q.get("bankId"))
    ok(f"C09 {q.get('bankId')} is in the bank, official/verified, not held", b is not None and not b.get("hold") and b.get("topic") in ("orthodiag", "pos_def")
       and (b.get("official") or b.get("solutionSource")))

# ====================================================== coverage
own = {qid for qid in Q if not qid.startswith("C09")}
missing = sorted(own - checked)
ok("every own question id has a check", not missing, str(missing))
print("\n%d failures" % len(bad))
sys.exit(1 if bad else 0)
