# -*- coding: utf-8 -*-
"""Solver re-derivation of 23B-A Q5a (official final coefficient 5b-3a claimed wrong). ASCII output, exit 1 on fail.
Run: PYTHONUTF8=1 py -I tools/verify/23B-A/solve_Q5a.py"""
import sys
import sympy as sp

a, b = sp.symbols("a b", real=True)
ip = lambda X, Y: (Y.T * X).trace()
X = sp.Matrix([[0, a], [b, 0]])
V1 = sp.Matrix([[-1, 1], [1, 0]])
V2 = sp.Matrix([[1, 0], [2, 1]])
U1 = V1
U2 = V2 - ip(V2, U1) / ip(U1, U1) * U1
bad = []
def ok(n, c):
    print(("OK   " if c else "FAIL ") + n)
    if not c:
        bad.append(n)
ok("U2 = (4/3 -1/3; 5/3 1)", U2 == sp.Matrix([[sp.Rational(4, 3), -sp.Rational(1, 3)], [sp.Rational(5, 3), 1]]))
W2 = 3 * U2
ok("<X,U1> = a+b, |U1|^2 = 3", sp.expand(ip(X, U1) - (a + b)) == 0 and ip(U1, U1) == 3)
ok("<X,W2> = 5b-a (not 5b-3a)", sp.expand(ip(X, W2) - (5 * b - a)) == 0 and sp.expand(ip(X, W2) - (5 * b - 3 * a)) != 0)
ok("|W2|^2 = 51", ip(W2, W2) == 51)
P = sp.simplify((a + b) / 3 * U1 + (5 * b - a) / 51 * W2)
target = sp.Matrix([[-7 * a + b, 6 * a + 4 * b], [4 * a + 14 * b, -a + 5 * b]]) / 17
ok("Proj = [[-7a+b, 6a+4b],[4a+14b, -a+5b]]/17", sp.simplify(P - target) == sp.zeros(2))
ok("X - Proj orthogonal to V1, V2", sp.simplify(ip(X - P, V1)) == 0 and sp.simplify(ip(X - P, V2)) == 0)
Pw = sp.simplify((a + b) / 3 * U1 + (5 * b - 3 * a) / 51 * W2)
ok("official printed answer is NOT orthogonal residual", sp.simplify(ip(X - Pw, V2)) != 0)
sys.exit(1 if bad else 0)
