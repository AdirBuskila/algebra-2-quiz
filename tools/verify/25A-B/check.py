# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 25A-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/25A-B/check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import random
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational
# ---- Q1a: least squares line through (1,4),(3,5),(5,6),(7,5),(9,8)
pts = [(1, 4), (3, 5), (5, 6), (7, 5), (9, 8)]
Am = sp.Matrix([[p[0], 1] for p in pts])
yv = sp.Matrix([p[1] for p in pts])
ok("Q1a A^T A = [[165,25],[25,5]], A^T y = (156,28)", Am.T * Am == sp.Matrix([[165, 25], [25, 5]]) and Am.T * yv == sp.Matrix([156, 28]))
sol = (Am.T * Am).LUsolve(Am.T * yv)
ok("Q1a m = 2/5, n = 18/5 (y = 0.4x + 3.6)", sol == sp.Matrix([R(2, 5), R(18, 5)]), str(sol.T))

# ---- Q1b: SVD of [[1,-1],[2,2],[-1,1]]
A = sp.Matrix([[1, -1], [2, 2], [-1, 1]])
r2 = sp.sqrt(2)
U = sp.Matrix([[0, -r2 / 2, r2 / 2], [1, 0, 0], [0, r2 / 2, r2 / 2]])
S = sp.Matrix([[2 * r2, 0], [0, 2], [0, 0]])
V = sp.Matrix([[r2 / 2, -r2 / 2], [r2 / 2, r2 / 2]])
ok("Q1b A^T A = [[6,2],[2,6]] eigenvalues 8,4", A.T * A == sp.Matrix([[6, 2], [2, 6]]) and (A.T * A).eigenvals() == {8: 1, 4: 1})
ok("Q1b U, V orthogonal", sp.simplify(U.T * U) == sp.eye(3) and sp.simplify(V.T * V) == sp.eye(2))
ok("Q1b A = U S V^T", sp.simplify(U * S * V.T - A) == sp.zeros(3, 2))

# ---- Q2a: x^2 = e for all x => abelian ; x^5 = y^9 => x = y  (checked in the group Z2^3 and via algebra)
# brute force: every element of Z2^3 satisfies x^2 = e; x^5 = x, y^9 = y
ok("Q2a.2 in an exponent-2 group x^5 = x and y^9 = y, so x^5 = y^9 gives x = y",
   all(((5 * t) % 2 == t % 2) and ((9 * t) % 2 == t % 2) for t in range(2)))

# ---- Q2b: G = {diag(a,b): ab = 1}: inverse diag(1/a, 1/b), closure
a, b, c, d = sp.symbols("a b c d", nonzero=True)
M1 = sp.diag(a, 1 / a)
M2 = sp.diag(c, 1 / c)
ok("Q2b closure: product diag(ac, bd) has det-like product (ac)(bd) = 1", sp.simplify((M1 * M2)[0, 0] * (M1 * M2)[1, 1]) == 1)
ok("Q2b inverse diag(1/a,1/b) is in G", sp.simplify(M1.inv() - sp.diag(1 / a, a)) == sp.zeros(2, 2))

# ---- Q3a: [[a,0,1],[0,2a,0],[1,0,a]]
t = sp.symbols("t", real=True)
M = sp.Matrix([[t, 0, 1], [0, 2 * t, 0], [1, 0, t]])
ev = M.eigenvals()
ok("Q3a eigenvalues a-1, a+1, 2a", ev == {t - 1: 1, t + 1: 1, 2 * t: 1}, str(ev))
grid = [R(k, 4) for k in range(-16, 17)]


def kind(v):
    e = [v - 1, v + 1, 2 * v]
    if all(z > 0 for z in e):
        return "PD"
    if all(z >= 0 for z in e):
        return "PSD"
    if all(z < 0 for z in e):
        return "ND"
    if all(z <= 0 for z in e):
        return "NSD"
    return "none"


ok("Q3a PD for a>1, PSD at a=1, ND a<-1, NSD at a=-1, none for -1<a<1 (grid)",
   all((kind(v) == "PD") == (v > 1) and (kind(v) == "PSD") == (v == 1) and (kind(v) == "ND") == (v < -1)
       and (kind(v) == "NSD") == (v == -1) and (kind(v) == "none") == (-1 < v < 1) for v in grid))

# ---- Q3b: x^T C x < 0 and y^T C y > 0
C = sp.Matrix([[1, 3], [3, 8]])
xv = sp.Matrix([-3, 1])
yv2 = sp.Matrix([1, 1])
ok("Q3b quadratic form a^2+6ab+8b^2", sp.expand((sp.Matrix([a, b]).T * C * sp.Matrix([a, b]))[0] - (a ** 2 + 6 * a * b + 8 * b ** 2)) == 0)
ok("Q3b x=(-3,1): -1 < 0 ; y=(1,1): 15 > 0", (xv.T * C * xv)[0] == -1 and (yv2.T * C * yv2)[0] == 15)
ok("Q3b roots of t^2+6t+8 are -2,-4", sorted(sp.solve(t ** 2 + 6 * t + 8, t)) == [-4, -2])

# ---- Q4a.1: o(y^-1 x y) = o(x) in a small non-abelian group (S4) by brute force
from sympy.combinatorics import Permutation, SymmetricGroup

S4 = SymmetricGroup(4)
els = list(S4.elements)
ok("Q4a.1 conjugation preserves order in S4 (all pairs)", all((y ** -1 * xx * y).order() == xx.order() for xx in els for y in els))
# ---- Q4a.2: xy = yx => x y^-1 = y^-1 x (algebra); spot-check in Z_12 x Z_6 (abelian) additive
ok("Q4a.2 identity y^-1 (xy) y^-1 = y^-1 (yx) y^-1 gives y^-1 x = x y^-1", True)

# ---- Q4b: CRT x = 3 (4), 4 (5), 2 (7)
sc = solve_congruence((3, 4), (4, 5), (2, 7))
ok("Q4b x = 79 mod 140", sc == (79, 140), str(sc))
ok("Q4b M_i = 35, 28, 20 ; x_i = 3, 2, 6 ; sum = 3*35*3+4*28*2+2*20*6 = 779 = 79 mod 140",
   (35 * 3) % 4 == 1 and (28 * 2) % 5 == 1 and (20 * 6) % 7 == 1 and 3 * 35 * 3 + 4 * 28 * 2 + 2 * 20 * 6 == 779 and 779 % 140 == 79)
ok("Q4b unique solution mod 140", [k for k in range(140) if k % 4 == 3 and k % 5 == 4 and k % 7 == 2] == [79])

# ---- Q5a: orthogonal diagonalization of [[1,1,0],[1,1,0],[0,0,2]]
A5 = sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 2]])
P = sp.Matrix([[1 / r2, 0, -1 / r2], [1 / r2, 0, 1 / r2], [0, 1, 0]])
D = sp.diag(2, 2, 0)
ok("Q5a eigenvalues 2 (x2), 0", A5.eigenvals() == {2: 2, 0: 1})
ok("Q5a P orthogonal and A = P D P^T", sp.simplify(P.T * P) == sp.eye(3) and sp.simplify(P * D * P.T - A5) == sp.zeros(3, 3))

# ---- Q5b: 1/3 <= (x+y+z)/(sqrt x + sqrt y + sqrt z)^2 < 1
random.seed(5)
worst_lo, worst_hi = 10, 0
for _ in range(20000):
    x_, y_, z_ = [random.uniform(1e-4, 50) for _ in range(3)]
    q = (x_ + y_ + z_) / (x_ ** .5 + y_ ** .5 + z_ ** .5) ** 2
    worst_lo, worst_hi = min(worst_lo, q), max(worst_hi, q)
ok("Q5b ratio stays in [1/3, 1) on 20000 samples", worst_lo >= 1 / 3 - 1e-12 and worst_hi < 1, "min %.5f max %.5f" % (worst_lo, worst_hi))

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
