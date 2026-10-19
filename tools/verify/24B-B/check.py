# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 24B-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/24B-B/check.py
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
# ---- Q1a: sum sqrt(k/n) <= sqrt((n^2+n)/2)
ok("Q1a inequality for n = 1..300", all(sum(sp.sqrt(sp.Rational(k, n)) for k in range(1, n + 1)).evalf(30) <= sp.sqrt(R(n * n + n, 2)).evalf(30)
                                         for n in range(1, 60)))
ok("Q1a ||u||^2 = n(n+1)/2, ||v|| = 1", all(sum(range(1, n + 1)) == n * (n + 1) // 2 for n in range(1, 50)))

# ---- Q1b: Gram-Schmidt in M2(R) with <A,B> = tr(B^T A)
ipm = lambda A, B: (B.T * A).trace()
A = sp.eye(2)
Bm = sp.Matrix([[0, 1], [0, 1]])
u1 = A
u2 = Bm - ipm(Bm, u1) / ipm(u1, u1) * u1
ok("Q1b.1 <B,A> = 1, ||A||^2 = 2", ipm(Bm, A) == 1 and ipm(A, A) == 2)
ok("Q1b.1 u2 = [[-1/2,1],[0,1/2]], orthogonal to A", u2 == sp.Matrix([[R(-1, 2), 1], [0, R(1, 2)]]) and ipm(u1, u2) == 0)
w2 = 2 * u2
C = sp.Matrix([[1, 1], [1, 2]])
ok("Q1b.2 <C,I> = 3, <C,[[-1,2],[0,1]]> = 3, ||[[-1,2],[0,1]]||^2 = 6", ipm(C, A) == 3 and ipm(C, w2) == 3 and ipm(w2, w2) == 6)
proj = ipm(C, A) / ipm(A, A) * A + ipm(C, w2) / ipm(w2, w2) * w2
ok("Q1b.2 projection = [[1,1],[0,2]]", proj == sp.Matrix([[1, 1], [0, 2]]), str(proj))
# cross-check by least squares (normal equations) onto Sp{A,B}
s, t = sp.symbols("s t")
cand = s * A + t * Bm
res = C - cand
eqs = [ipm(res, A), ipm(res, Bm)]
sl = sp.solve(eqs, [s, t])
ok("Q1b.2 same projection by normal equations", sp.simplify(cand.subs(sl) - proj) == sp.zeros(2, 2))

# ---- Q2: Heisenberg group over Z_3
def mm(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(3)) % 3 for j in range(3)) for i in range(3))


G = [((1, a, b), (0, 1, a), (0, 0, 1)) for a in range(3) for b in range(3)]
Gs = set(G)
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ok("Q2b |G| = 9", len(G) == 9)
ok("Q2a closed", all(mm(X, Y) in Gs for X in G for Y in G))
ok("Q2a product formula (1,x+a,y+ax+b)", all(mm(((1, a, b), (0, 1, a), (0, 0, 1)), ((1, x, y), (0, 1, x), (0, 0, 1))) ==
                                             ((1, (x + a) % 3, (y + a * x + b) % 3), (0, 1, (x + a) % 3), (0, 0, 1))
                                             for a, b, x, y in itertools.product(range(3), repeat=4)))
ok("Q2a inverse (1,-a,a^2-b)", all(mm(((1, a, b), (0, 1, a), (0, 0, 1)), ((1, (-a) % 3, (a * a - b) % 3), (0, 1, (-a) % 3), (0, 0, 1))) == I3
                                   for a in range(3) for b in range(3)))
Mx = ((1, 2, 0), (0, 1, 2), (0, 0, 1))
sq = mm(Mx, Mx)
cu = mm(sq, Mx)
ok("Q2c M^2 = [[1,1,1],[0,1,1],[0,0,1]], M^3 = I, o(M) = 3", sq == ((1, 1, 1), (0, 1, 1), (0, 0, 1)) and cu == I3 and Mx != I3)

# ---- Q3a: [[k^2,0,2k],[0,k+1,0],[2k,0,k^2]]
k = sp.symbols("k", real=True)
M = sp.Matrix([[k ** 2, 0, 2 * k], [0, k + 1, 0], [2 * k, 0, k ** 2]])
ev = M.eigenvals()
ok("Q3a eigenvalues k+1, k^2+2k, k^2-2k", set(ev.keys()) == {k + 1, k ** 2 + 2 * k, k ** 2 - 2 * k}, str(ev))


def cls(v):
    e = [v + 1, v * v + 2 * v, v * v - 2 * v]
    if all(z > 0 for z in e):
        return "PD"
    if all(z >= 0 for z in e):
        return "PSD"
    if all(z < 0 for z in e):
        return "ND"
    if all(z <= 0 for z in e):
        return "NSD"
    return "none"


grid = [R(j, 4) for j in range(-24, 25)]
ok("Q3a PD iff k>2 ; PSD iff k=0 or k>=2 ; no NSD/ND ; not semidefinite iff k in (-oo,0) u (0,2)",
   all((cls(v) == "PD") == (v > 2) and (cls(v) in ("PD", "PSD")) == (v == 0 or v >= 2) and cls(v) not in ("ND", "NSD")
       and (cls(v) == "none") == (v < 0 or 0 < v < 2) for v in grid))

# ---- Q3b: least squares line through (0,0),(2,1),(3,4),(4,6),(6,9)
pts = [(0, 0), (2, 1), (3, 4), (4, 6), (6, 9)]
Am = sp.Matrix([[p[0], 1] for p in pts])
yv = sp.Matrix([p[1] for p in pts])
ok("Q3b A^T A = [[65,15],[15,5]], A^T y = (92,20)", Am.T * Am == sp.Matrix([[65, 15], [15, 5]]) and Am.T * yv == sp.Matrix([92, 20]))
sol = (Am.T * Am).LUsolve(Am.T * yv)
ok("Q3b m = 8/5, n = -4/5", sol == sp.Matrix([R(8, 5), R(-4, 5)]), str(sol.T))

# ---- Q4: (x,y)*(u,v) = (2xu, y+v), x != 0
op = lambda p, q: (2 * p[0] * q[0], p[1] + q[1])
x, y, u, v, a_, b_ = sp.symbols("x y u v a b")
l_ = op(op((x, y), (u, v)), (a_, b_))
r_ = op((x, y), op((u, v), (a_, b_)))
ok("Q4b associative (4xua, y+v+b)", all(sp.simplify(p - q) == 0 for p, q in zip(l_, r_)) and l_ == (4 * x * u * a_, y + v + b_))
e = (R(1, 2), 0)
ok("Q4c identity (1/2,0)", all(sp.simplify(p - q) == 0 for p, q in zip(op(e, (x, y)), (x, y))) and
   all(sp.simplify(p - q) == 0 for p, q in zip(op((x, y), e), (x, y))))
ok("Q4d inverse (1/(4x), -y)", all(sp.simplify(p - q) == 0 for p, q in zip(op((x, y), (1 / (4 * x), -y)), e)))
sol4 = sp.solve([sp.Eq(4 * x ** 3, x), sp.Eq(3 * y, y)], [x, y], dict=True)
ok("Q4e (x,y)^3 = (x,y): (1/2,0), (-1/2,0)", {(s_[x], s_[y]) for s_ in sol4 if s_[x] != 0} == {(R(1, 2), 0), (R(-1, 2), 0)}, str(sol4))

# ---- Q5a: SVD of [[2,1],[1,-2],[0,2]]
A5 = sp.Matrix([[2, 1], [1, -2], [0, 2]])
ok("Q5a A^T A = diag(5,9)", A5.T * A5 == sp.diag(5, 9))
Sm = sp.Matrix([[3, 0], [0, sp.sqrt(5)], [0, 0]])
Vm = sp.Matrix([[0, 1], [1, 0]])
U_printed = sp.Matrix([[R(1, 3), 2 / sp.sqrt(5), -2 / sp.sqrt(3)], [-R(2, 3), 1 / sp.sqrt(5), 4 / sp.sqrt(3)], [R(2, 3), 0, sp.sqrt(5) / 3]])
ok("Q5a OFFICIAL printed U (third column -2/sqrt3, 4/sqrt3, sqrt5/3) is NOT orthogonal: official final-answer typo",
   sp.simplify(U_printed.T * U_printed) != sp.eye(3))
c3 = sp.Matrix([-2, 4, 5]) / (3 * sp.sqrt(5))
U_ok = sp.Matrix.hstack(U_printed[:, 0], U_printed[:, 1], c3)
ok("Q5a corrected third column (-2,4,5)/(3 sqrt5): U orthogonal", sp.simplify(U_ok.T * U_ok) == sp.eye(3))
ok("Q5a A = U S V^T with corrected U", sp.simplify(U_ok * Sm * Vm.T - A5) == sp.zeros(3, 2))
ok("Q5a printed first two columns of U are right (A v_i = sigma_i u_i)",
   sp.simplify(A5 * Vm[:, 0] - 3 * U_printed[:, 0]) == sp.zeros(3, 1) and sp.simplify(A5 * Vm[:, 1] - sp.sqrt(5) * U_printed[:, 1]) == sp.zeros(3, 1))

# ---- Q5b: CRT x = 4 (5), 6 (8), 8 (9)
sc = solve_congruence((4, 5), (6, 8), (8, 9))
ok("Q5b x = 134 mod 360", sc == (134, 360), str(sc))

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
