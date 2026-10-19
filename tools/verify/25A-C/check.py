# -*- coding: utf-8 -*-
"""Facts for sitting 25A-C (algebra-2). The sitting has NO key (all items held, reason no-key); this script only
records what was verified while transcribing, for the solver. Run: PYTHONUTF8=1 py -I tools/verify/25A-C/check.py"""
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational
# Q1a least squares
pts = [(-4, -1), (-2, 0), (2, 4), (4, 5), (5, 6)]
Am = sp.Matrix([[p[0], 1] for p in pts])
yv = sp.Matrix([p[1] for p in pts])
print("info Q1a normal equations:", (Am.T * Am).tolist(), (Am.T * yv).tolist(), "solution", (Am.T * Am).LUsolve(Am.T * yv).T)
# Q1b: (int f/x)^2 <= int f^2 * int x^-2 = (1/2) int f^2
x = sp.symbols("x")
ok("Q1b int_1^2 x^-2 dx = 1/2", sp.integrate(x ** -2, (x, 1, 2)) == R(1, 2))
# Q2a: G = Z5* x Z7*
ok("Q2a.3 |G| = 4*6 = 24 ; Q2a.2 inverse of (2,3) is (3,5)", (2 * 3) % 5 == 1 and (3 * 5) % 7 == 1)
from sympy.ntheory import n_order

ok("Q2a.4 o(2 mod 5)=4, o(3 mod 7)=6, o((2,3)) = lcm = 12", n_order(2, 5) == 4 and n_order(3, 7) == 6 and sp.ilcm(4, 6) == 12)
# Q2b.2: B^T A B is only semidefinite for singular B
A = sp.eye(2)
B = sp.Matrix([[1, 0], [0, 0]])
ok("Q2b.2 as printed (B any real matrix) B^T A B is NOT positive definite when B is singular", (B.T * A * B).eigenvals() == {1: 1, 0: 1})
# Q3a SVD of [[1,0,2],[2,0,1]]
A3 = sp.Matrix([[1, 0, 2], [2, 0, 1]])
print("info Q3a A A^T =", (A3 * A3.T).tolist(), "eigenvalues", (A3 * A3.T).eigenvals(), "A^T A", (A3.T * A3).eigenvals())
# Q4a PD parameter a: [[a^2,0,1],[0,a,0],[1,0,a^2]] -> eigenvalues a^2+1, a^2-1, a
a = sp.symbols("a", real=True)
M4 = sp.Matrix([[a ** 2, 0, 1], [0, a, 0], [1, 0, a ** 2]])
print("info Q4a eigenvalues", M4.eigenvals())
# Q4b CRT
print("info Q4b CRT x=2 (5), 3 (2), 4 (7):", solve_congruence((2, 5), (3, 2), (4, 7)))
# Q5a orthogonal diagonalization of [[5,0,0],[0,4,2],[0,2,1]]
A5 = sp.Matrix([[5, 0, 0], [0, 4, 2], [0, 2, 1]])
print("info Q5a eigenvalues", A5.eigenvals())
print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
