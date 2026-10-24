# -*- coding: utf-8 -*-
"""Solver check for 23A-A Q5a: SVD of A = [[-1,1],[-1,1],[1,1]]. ASCII output, exit 1 on fail.
Run: PYTHONUTF8=1 py -I tools/verify/23A-A/solve_Q5a.py"""
import sys
import sympy as sp

bad = []
def ok(n, c, info=""):
    print(("OK   " if c else "FAIL ") + n + (" " + info if info else ""))
    if not c:
        bad.append(n)

A = sp.Matrix([[-1, 1], [-1, 1], [1, 1]])
ATA = A.T * A
ok("A^T A = [[3,-1],[-1,3]]", ATA == sp.Matrix([[3, -1], [-1, 3]]))
lam = sp.symbols("lambda")
ok("char poly (3-l)^2-1 = (l-4)(l-2)", sp.expand(ATA.charpoly(lam).as_expr() - (lam - 4) * (lam - 2)) == 0)
s2 = sp.sqrt(2)
v1 = sp.Matrix([1, -1]) / s2
v2 = sp.Matrix([1, 1]) / s2
ok("A^T A v1 = 4 v1", ATA * v1 == 4 * v1)
ok("A^T A v2 = 2 v2", ATA * v2 == 2 * v2)
u1 = sp.simplify(A * v1 / 2)
u2 = sp.simplify(A * v2 / s2)
ok("u1 = (-1,-1,0)/sqrt2", sp.simplify(u1 - sp.Matrix([-1, -1, 0]) / s2) == sp.zeros(3, 1), str(list(u1)))
ok("u2 = (0,0,1)", u2 == sp.Matrix([0, 0, 1]), str(list(u2)))
u3 = sp.Matrix([1, -1, 0]) / s2
ok("u3 unit, orthogonal to u1,u2", sp.simplify(u3.dot(u3)) == 1 and sp.simplify(u3.dot(u1)) == 0 and u3.dot(u2) == 0)
ok("A A^T u3 = 0", sp.simplify(A * A.T * u3) == sp.zeros(3, 1))
U = sp.Matrix.hstack(u1, u2, u3)
S = sp.Matrix([[2, 0], [0, s2], [0, 0]])
V = sp.Matrix.hstack(v1, v2)
ok("U orthogonal", sp.simplify(U.T * U) == sp.eye(3))
ok("V orthogonal", sp.simplify(V.T * V) == sp.eye(2))
ok("A = U S V^T", sp.simplify(U * S * V.T - A) == sp.zeros(3, 2))
ok("singular values match sympy", sorted(sp.simplify(x) for x in A.singular_values()) == sorted([2, s2]))
sys.exit(1 if bad else 0)
