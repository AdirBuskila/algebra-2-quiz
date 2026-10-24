# -*- coding: utf-8 -*-
"""Solver checks for the held items of 23A-S (algebra-2). No official key exists; these back the "solved" items.
Run: PYTHONUTF8=1 py -I tools/verify/23A-S/solve_23AS.py   ASCII output, exit 1 on any failure."""
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: definiteness is defined for symmetric matrices (course). M(a) symmetric iff a+1 = 2.
a = sp.symbols("a", real=True)
M = sp.Matrix([[a, 2, 0], [a + 1, a, 0], [0, 0, a]])
ok("Q1a symmetric iff a=1", sp.solve(sp.Eq(M[1, 0], M[0, 1]), a) == [1] and all(
    sp.simplify(M[i, j] - M[j, i]) == 0 for i in range(3) for j in range(3) if (i, j) not in [(0, 1), (1, 0)]))
M1 = M.subs(a, 1)
ok("Q1a M(1) eigenvalues {3,-1,1}", M1.eigenvals() == {3: 1, -1: 1, 1: 1})
lam = sp.symbols("lam")
ok("Q1a char poly of M(1) = (1-lam)((1-lam)^2-4)", sp.expand((M1 - lam * sp.eye(3)).det() - (1 - lam) * ((1 - lam) ** 2 - 4)) == 0)
v1, v2 = sp.Matrix([1, 1, 0]), sp.Matrix([1, -1, 0])
ok("Q1a witness v=(1,1,0): v^T M v = 6 > 0", (v1.T * M1 * v1)[0] == 6)
ok("Q1a witness v=(1,-1,0): v^T M v = -2 < 0", (v2.T * M1 * v2)[0] == -2)
# remark in the solution: the quadratic form v^T M v equals v^T S v, S = (M+M^T)/2, eigenvalues a, (3a+3)/2, (a-3)/2
Ssym = (M + M.T) / 2
ok("Q1a remark: S eigenvalues a, (3a+3)/2, (a-3)/2",
   sorted(map(sp.simplify, Ssym.eigenvals()), key=str) == sorted([a, (3 * a + 3) / 2, (a - 3) / 2], key=str))
ok("Q1a remark: form PD iff a>3, ND iff a<-1",
   sp.reduce_inequalities([a > 0, (3 * a + 3) / 2 > 0, (a - 3) / 2 > 0], a).as_set() == sp.Interval.open(3, sp.oo)
   and sp.reduce_inequalities([a < 0, (3 * a + 3) / 2 < 0, (a - 3) / 2 < 0], a).as_set() == sp.Interval.open(-sp.oo, -1))

# ---- Q1b: parallelogram law
nv2 = sp.symbols("nv2", positive=True)
sol = sp.solve(sp.Eq(4 ** 2 + 6 ** 2, 2 * (3 ** 2 + nv2)), nv2)
ok("Q1b ||v||^2 = 17", sol == [17])
# concrete realisation in R^2: u=(3,0), <u,v> = (16-36)/4 = -5, v = (-5/3, sqrt(17-25/9))
u = sp.Matrix([3, 0]); v = sp.Matrix([sp.Rational(-5, 3), sp.sqrt(17 - sp.Rational(25, 9))])
ok("Q1b realisable", sp.simplify((u + v).norm() - 4) == 0 and sp.simplify((u - v).norm() - 6) == 0 and sp.simplify(v.norm() - sp.sqrt(17)) == 0)

# ---- Q2a: least squares line
pts = [(5, 7), (3, 5), (1, 4), (-2, 0), (-3, 2)]
A = sp.Matrix([[x, 1] for x, _ in pts]); b = sp.Matrix([y for _, y in pts])
ok("Q2a A^T A = [[48,4],[4,5]]", A.T * A == sp.Matrix([[48, 4], [4, 5]]))
ok("Q2a A^T b = (48,18)", A.T * b == sp.Matrix([48, 18]))
ok("Q2a m=3/4, n=3", (A.T * A).solve(A.T * b) == sp.Matrix([sp.Rational(3, 4), 3]))
ok("Q2a det = 224", (A.T * A).det() == 224)

# ---- Q2b: Q orthogonal + symmetric -> Q^2 = I -> P^2 = 2P (spot check on reflections)
th = sp.symbols("th", real=True)
Qr = sp.Matrix([[sp.cos(th), sp.sin(th)], [sp.sin(th), -sp.cos(th)]])
P = sp.eye(2) + Qr
ok("Q2b reflection: Q^T Q = I, Q = Q^T, P^2 = 2P",
   sp.simplify(Qr.T * Qr - sp.eye(2)) == sp.zeros(2) and Qr == Qr.T and sp.simplify(P * P - 2 * P) == sp.zeros(2))
Hh = sp.eye(3) - 2 * sp.Matrix([1, 2, 2]) * sp.Matrix([1, 2, 2]).T / 9
ok("Q2b Householder 3x3: P^2 = 2P", (sp.eye(3) + Hh) ** 2 == 2 * (sp.eye(3) + Hh))

# ---- Q3a: QR
A = sp.Matrix([[1, 1, 0], [0, 0, 1], [1, -1, 1]])
s2 = sp.sqrt(2)
Qm = sp.Matrix([[1 / s2, 1 / s2, 0], [0, 0, 1], [1 / s2, -1 / s2, 0]])
Rm = sp.Matrix([[s2, 0, 1 / s2], [0, s2, -1 / s2], [0, 0, 1]])
ok("Q3a det A = 2", A.det() == 2)
ok("Q3a Q orthogonal", sp.simplify(Qm.T * Qm) == sp.eye(3))
ok("Q3a R = Q^T A", sp.simplify(Qm.T * A - Rm) == sp.zeros(3))
ok("Q3a QR = A", sp.simplify(Qm * Rm - A) == sp.zeros(3))
c1, c2, c3 = A.col(0), A.col(1), A.col(2)
u3 = c3 - (c3.dot(c1) / c1.dot(c1)) * c1 - (c3.dot(c2) / c2.dot(c2)) * c2
ok("Q3a GS: c1.c2 = 0, u3 = (0,1,0)", c1.dot(c2) == 0 and u3 == sp.Matrix([0, 1, 0]))

# ---- Q4: Heisenberg group closure / identity / inverse / associativity
a1, b1, c1_, a2, b2, c2_ = sp.symbols("a1 b1 c1 a2 b2 c2", real=True)
X = sp.Matrix([[1, a1, b1], [0, 1, c1_], [0, 0, 1]]); Y = sp.Matrix([[1, a2, b2], [0, 1, c2_], [0, 0, 1]])
ok("Q4 closure XY = [[1,a1+a2,b2+a1c2+b1],[0,1,c1+c2],[0,0,1]]",
   X * Y == sp.Matrix([[1, a1 + a2, b2 + a1 * c2_ + b1], [0, 1, c1_ + c2_], [0, 0, 1]]))
Xi = sp.Matrix([[1, -a1, a1 * c1_ - b1], [0, 1, -c1_], [0, 0, 1]])
ok("Q4 inverse", sp.expand(X * Xi) == sp.eye(3) and sp.expand(Xi * X) == sp.eye(3) and Xi == X.inv())
ok("Q4 det = 1", X.det() == 1)
ok("Q4 not abelian (XY != YX in general)", sp.expand(X * Y - Y * X) != sp.zeros(3))
Hm = lambda p, q, r: sp.Matrix([[1, p, q], [0, 1, r], [0, 0, 1]])
ok("Q4 example A(1,0,0)A(0,0,1)=A(1,1,1), reverse = A(1,0,1)",
   Hm(1, 0, 0) * Hm(0, 0, 1) == Hm(1, 1, 1) and Hm(0, 0, 1) * Hm(1, 0, 0) == Hm(1, 0, 1))

# ---- Q5a: CRT
ok("Q5a 3 = 1 mod 2", 3 % 2 == 1)
M1_, M2_, M3_ = 14, 35, 10
y1, y2, y3 = pow(14, -1, 5), pow(35, -1, 2), pow(10, -1, 7)
ok("Q5a inverses y1=4,y2=1,y3=5", (y1, y2, y3) == (4, 1, 5))
xs = (2 * 14 * 4 + 1 * 35 * 1 + 4 * 10 * 5) % 70
ok("Q5a sum 112+35+200 = 347 = 67 mod 70", 2 * 14 * 4 + 35 + 200 == 347 and xs == 67)
ok("Q5a 67 checks", 67 % 5 == 2 and 67 % 2 == 3 % 2 and 67 % 7 == 4)
ok("Q5a unique mod 70", [x for x in range(70) if x % 5 == 2 and x % 2 == 1 and x % 7 == 4] == [67])

# ---- Q5b: projection in M2 with tr(B^T A)
ip = lambda X_, Y_: (Y_.T * X_).trace()
A1 = sp.Matrix([[1, 1], [0, 0]]); A2 = sp.Matrix([[1, 3], [1, 1]]); C = sp.Matrix([[1, 2], [3, 0]])
ok("Q5b <A1,A1>=2 <A2,A1>=4", ip(A1, A1) == 2 and ip(A2, A1) == 4)
U2 = A2 - 2 * A1
ok("Q5b U2 = [[-1,1],[1,1]], <U2,U2>=4", U2 == sp.Matrix([[-1, 1], [1, 1]]) and ip(U2, U2) == 4 and ip(U2, A1) == 0)
ok("Q5b <C,A1>=3 <C,U2>=4", ip(C, A1) == 3 and ip(C, U2) == 4)
Pj = sp.Rational(3, 2) * A1 + 1 * U2
ok("Q5b proj = [[1/2,5/2],[1,1]]", Pj == sp.Matrix([[sp.Rational(1, 2), sp.Rational(5, 2)], [1, 1]]))
Rr = C - Pj
ok("Q5b residual orthogonal to A1, A2", ip(Rr, A1) == 0 and ip(Rr, A2) == 0)

print("ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
