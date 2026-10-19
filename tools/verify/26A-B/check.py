# -*- coding: utf-8 -*-
r"""sympy / brute-force checks for sitting 26A-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/26A-B/check.py
Covers the parts that have a (student) solution, plus reference values for the held parts (not shipped).
Prints ASCII only. Exit code 1 on any mismatch."""
import random
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: <u,v>_A = u^T A v, A = [[2,1],[1,2]]
A = sp.Matrix([[2, 1], [1, 2]])
ok("Q1a A symmetric, eigenvalues 1 and 3", A == A.T and A.eigenvals() == {1: 1, 3: 1})
t = sp.symbols("t", real=True)
u = sp.Matrix([1, t])
v = sp.Matrix([t, -1])
val = sp.expand((u.T * A * v)[0])
ok("Q1a.2 <u,v>_A = t^2 - 1", val == t**2 - 1, str(val))
ok("Q1a.2 solutions t = +-1", sorted(sp.solve(val, t)) == [-1, 1])
ok("Q1a.2 A v = (2t-1, t-2)", sp.expand(A * v - sp.Matrix([2 * t - 1, t - 2])) == sp.zeros(2, 1))
x1, x2 = sp.symbols("x1 x2", real=True)
qf = sp.expand((sp.Matrix([x1, x2]).T * A * sp.Matrix([x1, x2]))[0])
ok("Q1a.1 quadratic form 2x^2+2xy+2y^2 > 0 away from 0", qf == 2 * x1**2 + 2 * x1 * x2 + 2 * x2**2 and
   sp.expand(qf - (x1 + x2) ** 2 - x1**2 - x2**2) == 0)

# ---- Q1b (held, reference only): least squares for A x = b
A1 = sp.Matrix([[1, -2], [-1, 2], [0, 3], [2, 5]])
b1 = sp.Matrix([3, 1, -4, 2])
print("   Q1b reference: rank", A1.rank(), "solution", (A1.T * A1).LUsolve(A1.T * b1).T)

# ---- Q2: a o b = ab - a - b + 2 on M = R \ {1}
a, b, c, e = sp.symbols("a b c e")
op = lambda s, r: s * r - s - r + 2
ok("Q2.1 associative (symbolic)", sp.expand(op(op(a, b), c) - op(a, op(b, c))) == 0)
ok("Q2.1 both sides (a-1)(b-1)(c-1)+1", sp.expand(op(op(a, b), c) - ((a - 1) * (b - 1) * (c - 1) + 1)) == 0)
ok("Q2.1 student expansion abc-ac-bc+2c-ab+a+b-c = abc-ab-ac+2a-a-bc+b+c (both sides equal)",
   sp.expand((a * b - a - b + 2) * c - (a * b - a - b + 2) - c + 2) == sp.expand(a * (b * c - b - c + 2) - a - (b * c - b - c + 2) + 2))
ok("Q2.2 e = 2 is the identity and 2 is not 1", sp.solve(sp.expand(op(a, e) - a), e) == [2] and all(op(2, s) == s and op(s, 2) == s for s in range(-5, 6)))
ok("Q2.3 closure: a o b = 1 iff (a-1)(b-1) = 0", sp.expand(op(a, b) - 1 - (a - 1) * (b - 1)) == 0)
ok("Q2.3 inverse of a is a/(a-1), and a/(a-1) != 1", sp.simplify(op(a, a / (a - 1)) - 2) == 0 and sp.simplify(a / (a - 1) - 1) == 1 / (a - 1))
ok("Q2.3 commutative", sp.expand(op(a, b) - op(b, a)) == 0)
ok("Q2.4 (held, reference) x o x = x has the single solution x = 2 in M", [s for s in sp.solve(sp.expand(op(a, a) - a), a)] == [1, 2])
import functools  # noqa: E402

powers = {1: a}
for k in range(2, 9):
    powers[k] = op(powers[k - 1], a)
ok("Q2.5 a^n = (a-1)^n + 1 for n = 1..8", all(sp.expand(powers[k] - ((a - 1) ** k + 1)) == 0 for k in powers))
P = sp.Symbol("P")
ok("Q2.5 symbolic step: ((a-1)^n + 1) o a = (a-1)^n (a-1) + 1", sp.expand(op(P + 1, a) - (P * (a - 1) + 1)) == 0)

# ---- Q3a: [[1,x,1],[x,1,1],[1,1,x+2]]
x = sp.symbols("x", real=True)
M3 = sp.Matrix([[1, x, 1], [x, 1, 1], [1, 1, x + 2]])
lam = sp.symbols("lam")
cp = sp.factor(M3.charpoly(lam).as_expr())
print("   charpoly:", cp)
roots = sp.solve(M3.charpoly(lam).as_expr(), lam)
ok("Q3a eigenvalues 1-x, x, x+3", {sp.simplify(r) for r in roots} == {1 - x, x, x + 3})
ok("Q3a PSD iff 0 <= x <= 1 (all of 1-x, x, x+3 >= 0)",
   sp.Intersection(sp.solve_univariate_inequality(1 - x >= 0, x, relational=False),
                   sp.solve_univariate_inequality(x >= 0, x, relational=False),
                   sp.solve_univariate_inequality(x + 3 >= 0, x, relational=False)) == sp.Interval(0, 1))
for xv, kind in [(sp.Rational(1, 2), "pd"), (0, "psd"), (1, "psd"), (sp.Rational(-1, 10), "indef"), (sp.Rational(11, 10), "indef"), (-3, "indef"), (-4, "indef"), (5, "indef")]:
    ev = [sp.N(r) for r in M3.subs(x, xv).eigenvals().keys()]
    lo, hi = min(ev), max(ev)
    res = "pd" if lo > 1e-12 else ("psd" if lo > -1e-12 else "indef")
    ok("Q3a x=%s is %s" % (xv, kind), res == kind, "eigs %.3f..%.3f" % (lo, hi))
ok("Q3a never negative semidefinite (largest eigenvalue > 0 on a grid of x)",
   all(not (max(sp.N(r) for r in M3.subs(x, xv).eigenvals().keys()) <= 1e-12) for xv in [sp.Rational(k, 2) for k in range(-40, 41)]))

# ---- Q3b: A PD symmetric => A^2 and A^-1 PD
random.seed(9)
good = True
for _ in range(150):
    k = random.randint(2, 4)
    B = sp.Matrix(k, k, lambda i, j: random.randint(-3, 3))
    Apd = B.T * B + sp.eye(k)
    for T in (Apd**2, Apd.inv()):
        if T != T.T or not T.is_positive_definite:
            good = False
ok("Q3b A^2 and A^-1 symmetric and positive on 150 random SPD matrices", good)

# ---- Q4 (held, reference only): G = upper triangular unipotent-ish over Z5 with a != 0
print("   Q4b reference: |G| =", 4 * 5 * 5)
Xm = sp.Matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
P_ = sp.eye(3)
for k in range(1, 12):
    P_ = (P_ * Xm).applyfunc(lambda s: s % 5)
    if P_ == sp.eye(3):
        print("   Q4c reference: order of X =", k)
        break

# ---- Q5a (held, reference only): CRT x=2 (3), 1 (5), 4 (8)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

print("   Q5a reference:", solve_congruence((2, 3), (1, 5), (4, 8)))

# ---- Q5b: Cauchy-Schwarz with u_k = 1/sqrt(k), v_k = 1/k^(3/2)
nmax = 6
uu = sp.Matrix([1 / sp.sqrt(kk) for kk in range(1, nmax + 1)])
vv = sp.Matrix([1 / sp.sqrt(kk**3) for kk in range(1, nmax + 1)])
ok("Q5b <u,v> = sum 1/k^2", sp.simplify(uu.dot(vv) - sum(sp.Rational(1, kk**2) for kk in range(1, nmax + 1))) == 0)
ok("Q5b |u|^2 = sum 1/k, |v|^2 = sum 1/k^3", sp.simplify(uu.dot(uu) - sum(sp.Rational(1, kk) for kk in range(1, nmax + 1))) == 0
   and sp.simplify(vv.dot(vv) - sum(sp.Rational(1, kk**3) for kk in range(1, nmax + 1))) == 0)
ok("Q5b inequality holds for n = 1..60", all(sum(sp.Rational(1, kk**2) for kk in range(1, m + 1)) ** 2 <=
                                           sum(sp.Rational(1, kk) for kk in range(1, m + 1)) * sum(sp.Rational(1, kk**3) for kk in range(1, m + 1))
                                           for m in range(1, 61)))

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
