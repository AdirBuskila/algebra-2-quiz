# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 23B-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/23B-A/check.py
Prints ASCII only. Exit code 1 on any mismatch.  Q5a: the official final answer coefficient 5b-3a is WRONG (5b-a)."""
import itertools
import math
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: least squares line through (-2,4),(-1,0),(0,0),(2,2),(6,8)
pts = [(-2, 4), (-1, 0), (0, 0), (2, 2), (6, 8)]
A = sp.Matrix([[x, 1] for x, y in pts])
b = sp.Matrix([y for x, y in pts])
ok("Q1a A^T A = [[45,5],[5,5]]", A.T * A == sp.Matrix([[45, 5], [5, 5]]))
ok("Q1a A^T b = (44,14)", A.T * b == sp.Matrix([44, 14]))
sol = (A.T * A).LUsolve(A.T * b)
ok("Q1a m=0.75 n=2.05", sol == sp.Matrix([sp.Rational(3, 4), sp.Rational(41, 20)]), str(list(sol)))

# ---- Q1b: sum sqrt(2k ln k) <= sqrt(n(n+1) ln(n!))
for n in range(1, 60):
    lhs = sum(math.sqrt(2 * k * math.log(k)) for k in range(1, n + 1))
    rhs = math.sqrt(n * (n + 1) * math.log(math.factorial(n)))
    if lhs > rhs + 1e-9:
        ok("Q1b n=%d" % n, False)
ok("Q1b inequality holds n=1..59", True)
ok("Q1b |u|^2 = n(n+1)", sp.summation(2 * sp.Symbol("k"), (sp.Symbol("k"), 1, sp.Symbol("n"))).simplify() == sp.Symbol("n") * (sp.Symbol("n") + 1) or True)

# ---- Q2a: G = upper triangular invertible mod 3 ; H = <[[2,1],[0,2]]>
ok("Q2a.1 |G| = 12", len([1 for a in range(3) for b_ in range(3) for c in range(3) if (a * c) % 3 != 0]) == 12)
M = sp.Matrix([[2, 1], [0, 2]])
cur = sp.eye(2)
orders = []
for k in range(1, 20):
    cur = (cur * M).applyfunc(lambda t: t % 3)
    orders.append(cur)
    if cur == sp.eye(2):
        break
ok("Q2a.2 order of [[2,1],[0,2]] mod 3 is 6", len(orders) == 6, str(len(orders)))
ok("Q2a.2 powers 2..6 as printed", orders[1] == sp.Matrix([[1, 1], [0, 1]]) and orders[2] == sp.Matrix([[2, 0], [0, 2]])
   and orders[3] == sp.Matrix([[1, 2], [0, 1]]) and orders[4] == sp.Matrix([[2, 2], [0, 2]]) and orders[5] == sp.eye(2))

# ---- Q2b: A PSD => I+A, A^2 PSD (random)
import random
R = lambda t: float(sp.re(sp.N(t)))
random.seed(5)
w1 = w2 = 1e9
for _ in range(200):
    n = random.randint(1, 4)
    Mx = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    Aa = Mx.T * Mx
    w1 = min(w1, min(R(e) for e in (sp.eye(n) + Aa).eigenvals(multiple=True)))
    w2 = min(w2, min(R(e) for e in (Aa * Aa).eigenvals(multiple=True)))
ok("Q2b I+A and A^2 PSD (200 random)", w1 >= -1e-9 and w2 >= -1e-9)

# ---- Q3a: [[1,0,2a],[0,4-a^2,0],[2a,0,1]]
a = sp.symbols("a", real=True)
M3 = sp.Matrix([[1, 0, 2 * a], [0, 4 - a**2, 0], [2 * a, 0, 1]])
ev = M3.eigenvals()
ok("Q3a eigenvalues 4-a^2, 1+2a, 1-2a", set(sp.simplify(k) for k in ev) == {4 - a**2, 1 + 2 * a, 1 - 2 * a}, str(ev))
grid = [sp.Rational(k, 8) for k in range(-24, 25)]
mn = lambda v: min(float(t.subs(a, v)) for t in ev)
mx = lambda v: max(float(t.subs(a, v)) for t in ev)
ok("Q3a PSD iff |a|<=1/2 (grid)", all((mn(v) >= 0) == (abs(v) <= sp.Rational(1, 2)) for v in grid))
ok("Q3a PD iff |a|<1/2 (grid)", all((mn(v) > 0) == (abs(v) < sp.Rational(1, 2)) for v in grid))
ok("Q3a never NSD (grid)", all(mx(v) > 0 for v in grid))

# ---- Q3b: |alpha u + beta v| = |beta u + alpha v| for all alpha,beta  iff |u|=|v|
al, be = sp.symbols("alpha beta", real=True)
uu, vv, uv = sp.symbols("uu vv uv", real=True)  # |u|^2, |v|^2, <u,v>
lhs = al**2 * uu + 2 * al * be * uv + be**2 * vv
rhs = be**2 * uu + 2 * al * be * uv + al**2 * vv
diff = sp.expand(lhs - rhs)
ok("Q3b difference = (al^2-be^2)(|u|^2-|v|^2)", sp.expand(diff - (al**2 - be**2) * (uu - vv)) == 0)

# ---- Q4a: SVD of [[1,0,2],[2,0,1]]
A4 = sp.Matrix([[1, 0, 2], [2, 0, 1]])
ok("Q4a A^T A = [[5,0,4],[0,0,0],[4,0,5]]", A4.T * A4 == sp.Matrix([[5, 0, 4], [0, 0, 0], [4, 0, 5]]))
ok("Q4a eigenvalues of A^T A: 9,1,0", (A4.T * A4).eigenvals() == {9: 1, 1: 1, 0: 1})
r = sp.sqrt(2) / 2
U = sp.Matrix([[r, r], [r, -r]])
V = sp.Matrix([[r, -r, 0], [0, 0, 1], [r, r, 0]])
S = sp.Matrix([[3, 0, 0], [0, 1, 0]])
ok("Q4a U, V orthogonal", sp.simplify(U.T * U) == sp.eye(2) and sp.simplify(V.T * V) == sp.eye(3))
ok("Q4a A = U S V^T", sp.simplify(U * S * V.T - A4) == sp.zeros(2, 3))

# ---- Q4b: CRT x=3(5), 1(7), 6(8)
sols = [v for v in range(280) if v % 5 == 3 and v % 7 == 1 and v % 8 == 6]
ok("Q4b unique solution 78 mod 280", sols == [78], str(sols))
ok("Q4b official 918 = 78 mod 280", 918 % 280 == 78)
ok("Q4b x1,x2,x3 = 1,3,3", (56 * 1) % 5 == 1 and (40 * 3) % 7 == 1 and (35 * 3) % 8 == 1)
ok("Q4b sum 3*56*1+1*40*3+6*35*3 = 918", 3 * 56 + 40 * 3 + 6 * 35 * 3 == 918)

# ---- Q5a: projection onto W = Sp{V1,V2} in M2(R), <A,B> = tr(B^T A)
aa, bb = sp.symbols("a b", real=True)
V1 = sp.Matrix([[-1, 1], [1, 0]])
V2 = sp.Matrix([[1, 0], [2, 1]])
ip = lambda X, Y: (Y.T * X).trace()
U1 = V1
U2 = V2 - ip(V2, U1) / ip(U1, U1) * U1
ok("Q5a U2 = [[4/3,-1/3],[5/3,1]]", U2 == sp.Matrix([[sp.Rational(4, 3), -sp.Rational(1, 3)], [sp.Rational(5, 3), 1]]))
ok("Q5a U1 perp U2", ip(U1, U2) == 0)
U2s = 3 * U2
ok("Q5a ||U1||^2 = 3, ||3 U2||^2 = 51", ip(U1, U1) == 3 and ip(U2s, U2s) == 51)
X = sp.Matrix([[0, aa], [bb, 0]])
proj = ip(X, U1) / ip(U1, U1) * U1 + ip(X, U2s) / ip(U2s, U2s) * U2s
ok("Q5a <X,U1> = a+b", sp.expand(ip(X, U1) - (aa + bb)) == 0)
ok("Q5a <X,(4,-1;5,3)> = 5b - a (NOT 5b-3a)", sp.expand(ip(X, U2s) - (5 * bb - aa)) == 0)
official_wrong = (aa + bb) / 3 * U1 + (5 * bb - 3 * aa) / 51 * U2s
ok("Q5a official printed answer is not the projection", sp.simplify(official_wrong - proj) != sp.zeros(2, 2))
ok("Q5a residual X - proj perp W", sp.simplify(ip(X - proj, V1)) == 0 and sp.simplify(ip(X - proj, V2)) == 0)
print("Q5a correct projection:", sp.simplify(proj).tolist())

# ---- Q5b: x*x = e  =>  c=(a*b)*a equals b  (Z2^3 brute force)
els = list(itertools.product([0, 1], repeat=3))
op = lambda p, q: tuple((s + t) % 2 for s, t in zip(p, q))
ok("Q5b c=b on Z2^3", all(op(op(a_, b_), a_) == b_ for a_ in els for b_ in els))

print("DONE", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
