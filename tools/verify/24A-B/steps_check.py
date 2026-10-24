# -*- coding: utf-8 -*-
"""sympy / brute-force check of every machine-checkable step value in tools/raw/24A-B.json.
Run: PYTHONUTF8=1 py -I tools/verify/24A-B/steps_check.py   (ASCII output, exit 1 on mismatch)"""
import json
import pathlib
import sys

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "24A-B.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
bad = []


def ok(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        bad.append(name)


def item(n, part):
    for q in data["questions"]:
        if q["num"] == n and q.get("part") == part:
            return q
    raise KeyError((n, part))


def ans(n, part, i):
    s = item(n, part)["steps"][i]
    assert s["type"] == "numeric", (n, part, i)
    return s["answer"], s["tol"]


def numeq(n, part, i, value):
    a, tol = ans(n, part, i)
    ok("Q%d%s step %d numeric = %s" % (n, part, i, sp.N(value, 8)), abs(float(a) - float(value)) <= max(tol, 0) + 1e-12)


R = sp.Rational
# Q1a least squares
A = sp.Matrix([[x, 1] for x in (1, 3, 5, 7, 9)])
b = sp.Matrix([4, 5, 6, 5, 8])
AtA, Atb = A.T * A, A.T * b
numeq(1, "א", 0, AtA[0, 0])
numeq(1, "א", 1, Atb[0])
sol = AtA.solve(Atb)
numeq(1, "א", 2, sol[0])
numeq(1, "א", 3, sol[1])


# Q1b
def ip(X, Y):
    return (Y.T * X).trace()


e1, e2, e3 = sp.Matrix([[1, -1], [0, 1]]), sp.Matrix([[0, 1], [0, 1]]), sp.Matrix([[1, 1], [1, 1]])
v = sp.Matrix([[2, 1], [1, 2]])
numeq(1, "ב", 0, ip(e2, e1))
numeq(1, "ב", 1, ip(e3, e1))
v3 = sp.Matrix([[2, 1], [3, -1]])
numeq(1, "ב", 2, ip(v, v3) / ip(v3, v3))
proj = ip(v, e1) / ip(e1, e1) * e1 + ip(v, e2) / ip(e2, e2) * e2 + ip(v, v3) / ip(v3, v3) * v3
numeq(1, "ב", 3, proj[0, 1])
ok("Q1b v3 orthogonal to e1,e2", ip(v3, e1) == 0 and ip(v3, e2) == 0)

# Q2a operation
a_, b_, c_, e_, x_ = sp.symbols("a b c e x", positive=True)
op = lambda p, q: (p + q) / (p * q)
sub = {a_: 1, b_: 2, c_: 3}
L = sp.simplify(op(op(a_, b_), c_))
Rr = sp.simplify(op(a_, op(b_, c_)))
ok("Q2a.2 L = (a+b+abc)/(ac+bc)", sp.simplify(L - (a_ + b_ + a_ * b_ * c_) / (a_ * c_ + b_ * c_)) == 0)
ok("Q2a.2 R = (abc+b+c)/(ab+ac)", sp.simplify(Rr - (a_ * b_ * c_ + b_ + c_) / (a_ * b_ + a_ * c_)) == 0)
numeq(2, "ב", 0, L.subs(sub))
numeq(2, "ב", 1, Rr.subs(sub))
bugR = (a_ * b_ * c_ + a_ + c_) / (a_ * b_ + a_ * c_)
ok("Q2a.2 findbug line differs from true value", sp.simplify(bugR - Rr) != 0)
ok("Q2a.3 a(.)e=a <=> a+e=a^2 e", sp.simplify(sp.together(op(a_, e_) - a_) - (a_ + e_ - a_**2 * e_) / (a_ * e_)) == 0)
for wrong in (a_ + e_ - a_ * e_, a_ + e_ - a_, 1 + e_ - a_ * e_):
    ok("Q2a.3 wrong distractor differs", sp.simplify(wrong - (a_ + e_ - a_**2 * e_)) != 0)
ok("Q2a.3 a=1: no solution", sp.solve(sp.Eq(1 + e_, e_), e_) == [])
numeq(2, "ג", 1, 0)
ok("Q2a.4 x(.)x = 2/x", sp.simplify(op(x_, x_) - 2 / x_) == 0)
for wrong in (2 * x_, x_ / 2, 1 / x_):
    ok("Q2a.4 distractor differs", sp.simplify(op(x_, x_) - wrong) != 0)
numeq(2, "ד", 1, sp.sqrt(2))
ok("Q2a.4 only positive root", sp.solve(sp.Eq(2 / x_, x_), x_) == [sp.sqrt(2)])

# Q2b distractors: trace>0 only, det>0 only are not enough; symmetric not enough for invertible
ok("Q2b trace>0 not PD: diag(3,-1)", sp.diag(3, -1).trace() > 0 and min(sp.diag(3, -1).eigenvals()) < 0)
ok("Q2b det>0 not PD: diag(-1,-1)", sp.diag(-1, -1).det() > 0 and min(sp.diag(-1, -1).eigenvals()) < 0)
ok("Q2b symmetric but singular: [[1,1],[1,1]]", sp.Matrix([[1, 1], [1, 1]]).det() == 0)
lam = sp.symbols("lam", nonzero=True)
ok("Q2b A v = lam^-1 v from v = lam A v", sp.simplify(1 / lam * lam - 1) == 0)

# Q3a
aa = sp.symbols("aa", real=True)
M3 = sp.Matrix([[2 * aa**2, aa, 0], [aa, 1, aa], [0, aa, 2 * aa**2]])
numeq(3, "א", 0, M3.subs(aa, 1).det())
numeq(3, "א", 1, (2 * aa**2 + 1).subs(aa, 2))
ok("Q3a eigenvalues", {sp.simplify(r) for r in sp.solve(M3.charpoly(sp.Symbol("l")).as_expr(), sp.Symbol("l"))} == {2 * aa**2, 2 * aa**2 + 1, 0})
ok("Q3a a=2 eigenvalue 9 present", 9 in M3.subs(aa, 2).eigenvals())

# Q3b expansion
t = sp.symbols("t", real=True)
u1, u2, w1, w2 = sp.symbols("u1 u2 w1 w2", real=True)
U = sp.Matrix([u1, u2])
W = sp.Matrix([w1, w2])
N2 = (U + t * W).dot(U + t * W)
good = U.dot(U) + 2 * t * U.dot(W) + t**2 * W.dot(W)
ok("Q3b expansion", sp.expand(N2 - good) == 0)
ok("Q3b distractor (no cross term) differs", sp.expand(N2 - (U.dot(U) + t**2 * W.dot(W))) != 0)
ok("Q3b distractor (norms product) differs", sp.expand(N2 - (U.dot(U) + 2 * t * sp.sqrt(U.dot(U)) * sp.sqrt(W.dot(W)) + t**2 * W.dot(W))) != 0)
ok("Q3b distractor (linear t) differs", sp.expand(N2 - (U.dot(U) + t * U.dot(W) + t * W.dot(W))) != 0)


# Q4a, mod 5 matrices
def mm(X, Y):
    return (X * Y).applyfunc(lambda z: z % 5)


Hs = [sp.Matrix([[a, c], [0, pow(a, -1, 5)]]) for a in range(1, 5) for c in range(5)]
ok("Q4a.2 |H| = 20 and a has 4 values", len(Hs) == 20 and len({H[0, 0] for H in Hs}) == 4)
numeq(4, "ב", 0, 4)
numeq(4, "ב", 1, 20)
a, c = 2, 1
bb, d = 2, 3
Xm = sp.Matrix([[a, c], [0, pow(a, -1, 5)]])
Ym = sp.Matrix([[bb, d], [0, pow(bb, -1, 5)]])
numeq(4, "א", 1, mm(Xm, Ym)[0, 1])
ok("Q4a.1 product stays in H", all(mm(X, Y) in Hs for X in Hs for Y in Hs))
ok("Q4a.1 true inverse formula", all(mm(X, sp.Matrix([[pow(X[0, 0], -1, 5), -X[0, 1]], [0, X[0, 0]]])) == sp.eye(2) for X in Hs))
cands = [lambda X: sp.Matrix([[pow(X[0, 0], -1, 5), X[0, 1]], [0, X[0, 0]]]),
         lambda X: sp.Matrix([[X[0, 0], -X[0, 1]], [0, pow(X[0, 0], -1, 5)]]),
         lambda X: sp.Matrix([[pow(X[0, 0], -1, 5), 0], [-X[0, 1], X[0, 0]]])]
for k, f in enumerate(cands):
    ok("Q4a.1 distractor %d fails for some X in H" % k, any(mm(X, f(X)) != sp.eye(2) for X in Hs))
bugX = sp.Matrix([[2, 1], [0, 3]])
ok("Q4a.1 findbug (+c) product is [[1,2ac],[0,1]] != I", mm(bugX, sp.Matrix([[3, 1], [0, 2]])) == sp.Matrix([[1, 4], [0, 1]]))
numeq(4, "ג", 0, pow(2, -1, 5))
inv = sp.Matrix([[2, 4], [0, 3]]).inv_mod(5)
ok("Q4a.3 inverse = [[3,1],[0,2]]", inv == sp.Matrix([[3, 1], [0, 2]]))
numeq(4, "ג", 1, inv[0, 1])
numeq(4, "ג", 2, inv[1, 1])

# Q4b CRT
from sympy.ntheory.modular import solve_congruence

xs = [t_ for t_ in range(8) if (3 * t_) % 8 == 14 % 8]
numeq(4, "ד", 0, xs[0])
ok("Q4b unique x mod 8", len(xs) == 1)
numeq(4, "ד", 1, 1800 // 9)
numeq(4, "ד", 2, pow(72, -1, 25))
numeq(4, "ד", 3, solve_congruence((2, 8), (4, 9), (22, 25))[0])

# Q5a
A5 = sp.Matrix([[3, -2, 4], [-2, 6, 2], [4, 2, 3]])
ev = A5.eigenvals()
numeq(5, "א", 0, min(ev))
numeq(5, "א", 1, ev[7])
vec = sp.Matrix([2, 1, -2])
ok("Q5a (2,1,-2) eigenvector of -2", A5 * vec == -2 * vec)
numeq(5, "א", 2, vec.norm())

# Q5b
nn = 4
numeq(5, "ב", 1, sp.sqrt(nn))
xsyms = sp.symbols("x1:5", positive=True)
ok("Q5b bound 1/n attained at x_i = 1/n", sum((R(1, nn)) ** 2 for _ in range(nn)) == R(1, nn))
ok("Q5b findbug line wrong: 1/n^1 vs 1/sqrt(n) for n=4", R(1, 4) != R(1, 2))

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
