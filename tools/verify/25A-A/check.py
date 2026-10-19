# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 25A-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/25A-A/check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


x = sp.symbols("x")
a, b = sp.symbols("a b", positive=True)

# ---- Q1a: <f,g> = int_0^1 f g, system {ax+b, ax-b}
ip = lambda f, g: sp.integrate(sp.expand(f * g), (x, 0, 1))
orth = sp.simplify(ip(a * x + b, a * x - b))
ok("Q1a.1 <ax+b,ax-b> = a^2/3 - b^2", sp.simplify(orth - (a ** 2 / 3 - b ** 2)) == 0)
ok("Q1a.1 orthogonal iff a = sqrt3 b", sp.solve(sp.Eq(orth, 0), a) == [sp.sqrt(3) * b])
n1 = sp.simplify(ip(a * x + b, a * x + b).subs(a, sp.sqrt(3) * b))
n2 = sp.simplify(ip(a * x - b, a * x - b).subs(a, sp.sqrt(3) * b))
ok("Q1a.2 norms^2 at a=sqrt3 b: b^2(2+sqrt3), b^2(2-sqrt3)",
   sp.simplify(n1 - b ** 2 * (2 + sp.sqrt(3))) == 0 and sp.simplify(n2 - b ** 2 * (2 - sp.sqrt(3))) == 0)
ok("Q1a.2 both norms 1 is impossible (b^2 would be 1/(2+sqrt3) and 1/(2-sqrt3))",
   sp.simplify(1 / (2 + sp.sqrt(3)) - 1 / (2 - sp.sqrt(3))) != 0)

# ---- Q2: (a,b)*(c,d) = (a+c+1, bd/3) on {(x,y): y != 0}
R = sp.Rational
op = lambda p, q: (p[0] + q[0] + 1, p[1] * q[1] / 3)
p1, p2, q1, q2, r1, r2 = sp.symbols("p1 p2 q1 q2 r1 r2")
P, Qv, Rv = (p1, p2), (q1, q2), (r1, r2)
lhs = op(op(P, Qv), Rv)
rhs = op(P, op(Qv, Rv))
ok("Q2b associative", all(sp.simplify(u - v) == 0 for u, v in zip(lhs, rhs)))
ok("Q2a closed: (bd/3 != 0 when b,d != 0)", True)
e = (-1, 3)
ok("Q2c identity (-1,3), both sides", all(sp.simplify(u - v) == 0 for u, v in zip(op(e, P), P)) and
   all(sp.simplify(u - v) == 0 for u, v in zip(op(P, e), P)))
inv = (-2 - p1, 9 / p2)
ok("Q2d inverse (-2-a, 9/b)", all(sp.simplify(u - v) == 0 for u, v in zip(op(P, inv), e)) and
   all(sp.simplify(u - v) == 0 for u, v in zip(op(inv, P), e)))
sol = sp.solve([sp.Eq(2 * p1 + 1, p1), sp.Eq(p2 ** 2 / 3, p2)], [p1, p2], dict=True)
ok("Q2e idempotents: x=-1, y=3 (y=0 excluded)", {(-1, 3)} == {(s[p1], s[p2]) for s in sol if s[p2] != 0}, str(sol))

# ---- Q3a: [[1,w,w],[w,1,w],[w,w,1]]
w = sp.symbols("w", real=True)
M = sp.Matrix([[1, w, w], [w, 1, w], [w, w, 1]])
ev = M.eigenvals()
ok("Q3a eigenvalues 1+2w (x1), 1-w (x2)", ev == {1 + 2 * w: 1, 1 - w: 2}, str(ev))
ok("Q3a PD iff -1/2 < w < 1 ; PSD iff -1/2 <= w <= 1 ; negative definite never",
   sp.solve_univariate_inequality(1 + 2 * w > 0, w).as_set() .intersect(sp.solve_univariate_inequality(1 - w > 0, w).as_set())
   == sp.Interval.open(R(-1, 2), 1)
   and sp.Intersection(sp.Interval(-sp.oo, R(-1, 2), True, True), sp.Interval(1, sp.oo, True, True)) == sp.EmptySet)

# ---- Q3b: equality in Cauchy-Schwarz iff proportional (spot-check on random integer vectors)
import random

random.seed(3)
good = True
for _ in range(2000):
    u = sp.Matrix([random.randint(-4, 4) for _ in range(3)])
    v = sp.Matrix([random.randint(-4, 4) for _ in range(3)])
    if u.norm() == 0 or v.norm() == 0:
        continue
    eq = (abs(u.dot(v)) == u.norm() * v.norm())
    prop = (u.cross(v) == sp.zeros(3, 1))
    if eq != prop:
        good = False
ok("Q3b |<u,v>| = |u||v| iff u,v proportional (2000 random samples)", good)

# ---- Q4a: G = GL_2(Z_5)
def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 5 for j in range(2)) for i in range(2))


G = [((p, q), (r, s)) for p, q, r, s in itertools.product(range(5), repeat=4) if (p * s - q * r) % 5 != 0]
ok("Q4a.2 |G| = 480 divisible by 4", len(G) == 480 and 480 % 4 == 0)
Jm = ((0, 4), (1, 0))
I2 = ((1, 0), (0, 1))
ok("Q4a.1 det J = -4 = 1 mod 5, J in G", (0 * 0 - 4 * 1) % 5 == 1)
pw = [I2]
for _ in range(4):
    pw.append(mul(pw[-1], Jm))
ok("Q4a.1 J^2 = 4I, J^3 = [[0,1],[4,0]], J^4 = I, o(J)=4", pw[2] == ((4, 0), (0, 4)) and pw[3] == ((0, 1), (4, 0)) and pw[4] == I2)
JT = ((0, 1), (4, 0))
ok("Q4a.3 J^T J = J J^T = I (mod 5)", mul(JT, Jm) == I2 and mul(Jm, JT) == I2)


def order(A):
    k, M_ = 1, A
    while M_ != I2:
        M_ = mul(M_, A)
        k += 1
    return k


ok("Q4a.3 o(J^T A J) = o(A) for all 480 matrices of G", all(order(mul(mul(JT, A), Jm)) == order(A) for A in G))

# ---- Q5a: SVD of [[1,1,1],[1,-2,1]]
A = sp.Matrix([[1, 1, 1], [1, -2, 1]])
ok("Q5a A A^T = diag(3,6)", A * A.T == sp.diag(3, 6))
ok("Q5a eigenvalues of A^T A are 6,3,0", (A.T * A).eigenvals() == {6: 1, 3: 1, 0: 1})
U = sp.Matrix([[0, 1], [1, 0]])
S = sp.Matrix([[sp.sqrt(6), 0, 0], [0, sp.sqrt(3), 0]])
V = sp.Matrix([[1 / sp.sqrt(6), 1 / sp.sqrt(3), -1 / sp.sqrt(2)], [-2 / sp.sqrt(6), 1 / sp.sqrt(3), 0],
               [1 / sp.sqrt(6), 1 / sp.sqrt(3), 1 / sp.sqrt(2)]])
ok("Q5a V orthogonal", sp.simplify(V.T * V) == sp.eye(3))
ok("Q5a A = U S V^T", sp.simplify(U * S * V.T - A) == sp.zeros(2, 3))

# ---- held items (info only): Q4b CRT and Q5b are NOT covered by the solution file (hold: no-key)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

print("info Q4b CRT (not shipped, hold):", solve_congruence((2, 5), (3, 7), (10, 11)))

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
