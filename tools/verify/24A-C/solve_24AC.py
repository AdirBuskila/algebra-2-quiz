# -*- coding: utf-8 -*-
"""Solver checks for the held items of 24A-C (algebra-2): Q3a SVD, Q3b polarization, Q5a Heisenberg group, Q5b.
Run: PYTHONUTF8=1 py -I tools/verify/24A-C/solve_24AC.py   ASCII output, exit 1 on any failure."""
import itertools
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q3a: SVD of A = [[0,-1,1],[1,1,0]]
A = sp.Matrix([[0, -1, 1], [1, 1, 0]])
ok("Q3a AA^T = [[2,-1],[-1,2]]", A * A.T == sp.Matrix([[2, -1], [-1, 2]]))
lam = sp.symbols("lam")
ok("Q3a char poly (2-lam)^2-1 -> 3, 1", sp.solve((A * A.T - lam * sp.eye(2)).det(), lam) == [1, 3])
ok("Q3a A^T A eigenvalues 3,1,0", (A.T * A).eigenvals() == {3: 1, 1: 1, 0: 1})
s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
U = sp.Matrix([[-1, 1], [1, 1]]) / s2
S = sp.Matrix([[s3, 0, 0], [0, 1, 0]])
v1 = sp.Matrix([1, 2, -1]) / s6; v2 = sp.Matrix([1, 0, 1]) / s2; v3 = sp.Matrix([-1, 1, 1]) / s3
V = sp.Matrix.hstack(v1, v2, v3)
ok("Q3a v1 = A^T u1 / sqrt3", sp.simplify(A.T * U.col(0) / s3 - v1) == sp.zeros(3, 1))
ok("Q3a v2 = A^T u2 / 1", sp.simplify(A.T * U.col(1) - v2) == sp.zeros(3, 1))
ok("Q3a A v3 = 0", sp.simplify(A * v3) == sp.zeros(2, 1))
ok("Q3a U orthogonal", sp.simplify(U.T * U) == sp.eye(2))
ok("Q3a V orthogonal", sp.simplify(V.T * V) == sp.eye(3))
ok("Q3a A = U S V^T", sp.simplify(U * S * V.T - A) == sp.zeros(2, 3))
ok("Q3a A^T A v_i = sigma_i^2 v_i", all(sp.simplify(A.T * A * v - k * v) == sp.zeros(3, 1) for v, k in [(v1, 3), (v2, 1), (v3, 0)]))

# ---- Q3b: polarization, spot check with a non-standard inner product <x,y> = x^T G y, G PD
G = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
ok("Q3b G positive definite", all(e > 0 for e in G.eigenvals()))
ipG = lambda x, y: (x.T * G * y)[0]
xs = sp.symbols("x1:4"); ys = sp.symbols("y1:4")
x = sp.Matrix(xs); y = sp.Matrix(ys)
ok("Q3b <u,v> = (|u+v|^2-|u-v|^2)/4 symbolically", sp.expand(ipG(x, y) - (ipG(x + y, x + y) - ipG(x - y, x - y)) / 4) == 0)

# ---- Q5a: Heisenberg group
a1, b1, c1, a2, b2, c2, a3, b3, c3 = sp.symbols("a1 b1 c1 a2 b2 c2 a3 b3 c3", real=True)
H = lambda a, b, c: sp.Matrix([[1, a, b], [0, 1, c], [0, 0, 1]])
X, Y, Z = H(a1, b1, c1), H(a2, b2, c2), H(a3, b3, c3)
ok("Q5a closure", sp.expand(X * Y - H(a1 + a2, b2 + a1 * c2 + b1, c1 + c2)) == sp.zeros(3))
ok("Q5a associativity (matrix product)", sp.expand((X * Y) * Z - X * (Y * Z)) == sp.zeros(3))
ok("Q5a identity is H(0,0,0)=I", H(0, 0, 0) == sp.eye(3) and X * sp.eye(3) == X)
Xi = H(-a1, a1 * c1 - b1, -c1)
ok("Q5a inverse H(-a, ac-b, -c)", sp.expand(X * Xi) == sp.eye(3) and sp.expand(Xi * X) == sp.eye(3))

# ---- Q5b: brute force over all groups with x*x=e we can build: (Z2)^k, k<=3
for k in range(1, 4):
    els = list(itertools.product([0, 1], repeat=k))
    op = lambda p, q: tuple((s + t) % 2 for s, t in zip(p, q))
    good = all(op(op(a, b), a) == b for a in els for b in els)
    ok("Q5b (Z2)^%d: (a*b)*a = b" % k, good)
# and the property fails without x*x=e: S3 (permutations) has (ab)a != b for some a, b
from sympy.combinatorics import Permutation
from sympy.combinatorics.named_groups import SymmetricGroup
S3e = list(SymmetricGroup(3).elements)
ok("Q5b hypothesis needed: in S3 some (ab)a != b", any((a * b) * a != b for a in S3e for b in S3e))

print("ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
