# -*- coding: utf-8 -*-
"""Solver checks for 26A-B held items: Q1c (least squares), Q2d (x o x = x), Q4a-c (group G mod 5), Q5a (CRT).
ASCII output, exit 1 on fail.  Run: PYTHONUTF8=1 py -I tools/verify/26A-B/solve_held.py"""
import itertools
import sys
import sympy as sp
from sympy.ntheory.modular import crt

bad = []
def ok(n, c, info=""):
    print(("OK   " if c else "FAIL ") + n + (" " + info if info else ""))
    if not c:
        bad.append(n)

# ---- Q1c: least squares
A = sp.Matrix([[1, -2], [-1, 2], [0, 3], [2, 5]])
b = sp.Matrix([3, 1, -4, 2])
ok("rank A = 2", A.rank() == 2)
ok("A^T A = [[6,6],[6,42]]", A.T * A == sp.Matrix([[6, 6], [6, 42]]))
ok("A^T b = (6,-6)", A.T * b == sp.Matrix([6, -6]))
xh = (A.T * A).LUsolve(A.T * b)
ok("x_hat = (4/3, -1/3)", xh == sp.Matrix([sp.Rational(4, 3), -sp.Rational(1, 3)]), str(list(xh)))
ok("A x_hat = (2,-2,-1,1)", A * xh == sp.Matrix([2, -2, -1, 1]))
r = b - A * xh
ok("residual (1,3,-3,1) orthogonal to columns", r == sp.Matrix([1, 3, -3, 1]) and A.T * r == sp.zeros(2, 1))
ok("|residual|^2 = 20", r.dot(r) == 20)

# ---- Q2d: x o x = x in M = R \ {1}
x = sp.symbols("x")
sols = sp.solve(sp.Eq(x * x - x - x + 2, x), x)
ok("x^2-3x+2=0 -> {1,2}; only 2 in M", sorted(sols) == [1, 2])
ok("2 o 2 = 2", 2 * 2 - 2 - 2 + 2 == 2)

# ---- Q4: G = {[[a,b,c],[0,a,b],[0,0,a]] : a != 0 mod 5}
def mk(a, b_, c):
    return sp.Matrix([[a, b_, c], [0, a, b_], [0, 0, a]])
def md(M):
    return M.applyfunc(lambda t: t % 5)
G = [mk(a, b_, c) for a in range(1, 5) for b_ in range(5) for c in range(5)]
keys = {tuple(M) for M in G}
ok("|G| = 100", len(G) == 100 and len(keys) == 100)
a, b_, c, d, e, f = sp.symbols("a b c d e f")
P = mk(a, b_, c) * mk(d, e, f)
ok("product form [[ad, ae+bd, af+be+cd],...]", sp.expand(P - mk(a * d, a * e + b_ * d, a * f + b_ * e + c * d)) == sp.zeros(3))
closed = all(tuple(md(X * Y)) in keys for X in G[::7] for Y in G[::3])
ok("closure (sampled pairs)", closed)
ok("closure (all pairs, via a*d != 0 mod 5)", all((p * q) % 5 != 0 for p in range(1, 5) for q in range(1, 5)))
inv_ok = True
for (aa, bb, cc) in itertools.product(range(1, 5), range(5), range(5)):
    ai = pow(aa, -1, 5)
    Y = mk(ai, (-bb * ai * ai) % 5, ((bb * bb - aa * cc) * pow(ai, 3)) % 5)
    if md(mk(aa, bb, cc) * Y) != sp.eye(3) or md(Y * mk(aa, bb, cc)) != sp.eye(3):
        inv_ok = False
ok("inverse formula d=a^-1, e=-b a^-2, f=(b^2-ac) a^-3 works for all 100", inv_ok)
ok("identity in G (a=1,b=c=0)", tuple(sp.eye(3)) in keys)
X = mk(1, 0, 1)
pw = sp.eye(3); order = None
for n in range(1, 20):
    pw = md(pw * X)
    if pw == sp.eye(3):
        order = n
        break
ok("o(X) = 5", order == 5, str(order))
ok("X^n = I + nE13", all(md(X ** n) == md(sp.eye(3) + n * sp.Matrix([[0, 0, 1], [0, 0, 0], [0, 0, 0]])) for n in range(1, 8)))

# ---- Q5a: CRT
m = [3, 5, 8]; rr = [2, 1, 4]
Ms = [120 // k for k in m]
xs = [pow(Mi, -1, k) for Mi, k in zip(Ms, m)]
ok("M_i = 40,24,15 ; x_i = 1,4,7", Ms == [40, 24, 15] and xs == [1, 4, 7])
tot = sum(p * q * s for p, q, s in zip(rr, Ms, xs))
ok("sum = 80+96+420 = 596 ; 596 mod 120 = 116", tot == 596 and tot % 120 == 116)
ok("sympy crt agrees", crt(m, rr)[0] == 116)
ok("116 satisfies all three", 116 % 3 == 2 and 116 % 5 == 1 and 116 % 8 == 4)
sys.exit(1 if bad else 0)
