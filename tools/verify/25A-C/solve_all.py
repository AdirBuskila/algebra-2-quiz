# -*- coding: utf-8 -*-
"""Solver checks for sitting 25A-C (algebra-2, no key). Every number written in tools/gen/gen_25A-C.py is
recomputed here. Run: PYTHONUTF8=1 py -I tools/verify/25A-C/solve_all.py"""
import itertools
import random
import sys

import sympy as sp
from sympy.ntheory import n_order
from sympy.ntheory.modular import solve_congruence

bad = []
R = sp.Rational


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + str(info) if info != "" else ""))
    if not cond:
        bad.append(name)


# ---------------------------------------------------------------- Q1a least squares y = m x + n
pts = [(-4, -1), (-2, 0), (2, 4), (4, 5), (5, 6)]
Am = sp.Matrix([[p[0], 1] for p in pts])
yv = sp.Matrix([p[1] for p in pts])
N = Am.T * Am
rhs = Am.T * yv
ok("Q1a A^T A = [[65,5],[5,5]]", N == sp.Matrix([[65, 5], [5, 5]]), N.tolist())
ok("Q1a A^T y = [62,14]", rhs == sp.Matrix([62, 14]), rhs.T.tolist())
sol = N.LUsolve(rhs)
ok("Q1a m = 4/5, n = 2", sol == sp.Matrix([R(4, 5), 2]), sol.T.tolist())
ok("Q1a elimination: 60 m = 48", 65 * R(4, 5) + 5 * 2 == 62 and 60 * R(4, 5) == 48)

# ---------------------------------------------------------------- Q1b Cauchy-Schwarz on C[1,2]
x = sp.symbols("x")
ok("Q1b ||1/x||^2 = int_1^2 x^-2 = 1/2", sp.integrate(x ** -2, (x, 1, 2)) == R(1, 2))
for f in (x, x ** 2 - 3, sp.sin(x), sp.exp(x)):  # sanity: the inequality holds on samples
    lhs = sp.N(sp.integrate(f / x, (x, 1, 2)) ** 2)
    r = sp.N(R(1, 2) * sp.integrate(f ** 2, (x, 1, 2)))
    ok(f"Q1b sample f={f}", lhs <= r + 1e-12, f"{lhs:.6f} <= {r:.6f}")
ok("Q1b equality case f = 1/x", sp.integrate(1 / x ** 2, (x, 1, 2)) ** 2 == R(1, 2) * sp.integrate(1 / x ** 2, (x, 1, 2)))

# ---------------------------------------------------------------- Q2a G = Z5* x Z7*
G = list(itertools.product(range(1, 5), range(1, 7)))
mul = lambda p, q: ((p[0] * q[0]) % 5, (p[1] * q[1]) % 7)
ok("Q2a.1 neutral (1,1)", all(mul((1, 1), g) == g == mul(g, (1, 1)) for g in G))
ok("Q2a.2 inverse of (2,3) is (3,5)", mul((2, 3), (3, 5)) == (1, 1) and mul((3, 5), (2, 3)) == (1, 1))
ok("Q2a.2 2*3=6=1 mod 5, 3*5=15=1 mod 7", 6 % 5 == 1 and 15 % 7 == 1)
ok("Q2a.3 |G| = 4*6 = 24", len(G) == 24)
p, k = (2, 3), 1
while p != (1, 1):
    p, k = mul(p, (2, 3)), k + 1
ok("Q2a.4 o((2,3)) = 12 (brute force)", k == 12, k)
ok("Q2a.4 o(2 mod 5)=4, o(3 mod 7)=6, lcm=12", n_order(2, 5) == 4 and n_order(3, 7) == 6 and sp.ilcm(4, 6) == 12)
ok("Q2a.4 powers of 2 mod 5: 2,4,3,1", [pow(2, i, 5) for i in range(1, 5)] == [2, 4, 3, 1])
ok("Q2a.4 powers of 3 mod 7: 3,2,6,4,5,1", [pow(3, i, 7) for i in range(1, 7)] == [3, 2, 6, 4, 5, 1])
ok("Q2a.4 (2,3)^6 = (4,1) != (1,1), (2,3)^4 = (1,4) != (1,1)", (pow(2, 6, 5), pow(3, 6, 7)) == (4, 1) and (pow(2, 4, 5), pow(3, 4, 7)) == (1, 4))

# ---------------------------------------------------------------- Q2b PSD claims (course sense: v^T M v >= 0)
random.seed(1)


def rand_psd(n, rank):
    C = sp.Matrix(n, rank, lambda i, j: random.randint(-3, 3))
    return C * C.T


all1 = all2 = True
for _ in range(60):
    n = random.randint(1, 4)
    A = rand_psd(n, random.randint(1, n))
    B = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    M1, M2 = -A - B.T * B, B.T * A * B
    all1 &= bool(M1.is_symmetric() and M1.is_negative_semidefinite)
    all2 &= bool(M2.is_symmetric() and M2.is_positive_semidefinite)
ok("Q2b.1 -A-B^TB symmetric, all eigenvalues <= 0 (60 random A PSD, B any)", all1)
ok("Q2b.2 B^TAB symmetric, all eigenvalues >= 0 (60 random A PSD, B any)", all2)
A, B = sp.eye(2), sp.Matrix([[1, 0], [0, 0]])
ok("Q2b.2 note: strict sense fails for singular B (A=I, B=diag(1,0) -> eigenvalue 0)", (B.T * A * B).eigenvals() == {1: 1, 0: 1})
A = sp.Matrix([[2, 1], [1, 2]])
B = sp.Matrix([[1, 2], [3, 4]])
ok("Q2b.2 note: strict sense holds for A PD and B invertible (sample)", all(ev > 0 for ev in (B.T * A * B).eigenvals()))

# ---------------------------------------------------------------- Q3a SVD of [[1,0,2],[2,0,1]]
A3 = sp.Matrix([[1, 0, 2], [2, 0, 1]])
AAt = A3 * A3.T
ok("Q3a A A^T = [[5,4],[4,5]]", AAt == sp.Matrix([[5, 4], [4, 5]]))
ok("Q3a eigenvalues of A A^T are 9, 1", AAt.eigenvals() == {9: 1, 1: 1})
ok("Q3a A^T A eigenvalues 9, 1, 0", (A3.T * A3).eigenvals() == {9: 1, 1: 1, 0: 1})
s2 = sp.sqrt(2)
U = sp.Matrix([[1, 1], [1, -1]]) / s2
S = sp.Matrix([[3, 0, 0], [0, 1, 0]])
v1 = A3.T * U[:, 0] / 3
v2 = A3.T * U[:, 1] / 1
ok("Q3a v1 = A^T u1 / 3 = (1,0,1)/sqrt2", sp.simplify(v1 - sp.Matrix([1, 0, 1]) / s2) == sp.zeros(3, 1))
ok("Q3a v2 = A^T u2 / 1 = (-1,0,1)/sqrt2", sp.simplify(v2 - sp.Matrix([-1, 0, 1]) / s2) == sp.zeros(3, 1))
ok("Q3a A^T u1 = (3,0,3)/sqrt2 and A^T u2 = (-1,0,1)/sqrt2",
   sp.simplify(A3.T * U[:, 0] - sp.Matrix([3, 0, 3]) / s2) == sp.zeros(3, 1) and sp.simplify(A3.T * U[:, 1] - sp.Matrix([-1, 0, 1]) / s2) == sp.zeros(3, 1))
V = sp.Matrix([[1, -1, 0], [0, 0, 1], [1, 1, 0]]) / s2
V[:, 2] = sp.Matrix([0, 1, 0])
ok("Q3a V = [v1 v2 (0,1,0)] orthogonal", sp.simplify(V.T * V) == sp.eye(3))
ok("Q3a U orthogonal", sp.simplify(U.T * U) == sp.eye(2))
ok("Q3a A = U Sigma V^T", sp.simplify(U * S * V.T - A3) == sp.zeros(2, 3))
ok("Q3a A^T A v3 = 0 for v3=(0,1,0)", A3.T * A3 * sp.Matrix([0, 1, 0]) == sp.zeros(3, 1))
ok("Q3a eigenvectors of AA^T: (1,1) for 9, (1,-1) for 1", AAt * sp.Matrix([1, 1]) == 9 * sp.Matrix([1, 1]) and AAt * sp.Matrix([1, -1]) == sp.Matrix([1, -1]))

# ---------------------------------------------------------------- Q3b polarization identity in R^n (sanity)
u = sp.Matrix(sp.symbols("u1:4"))
w = sp.Matrix(sp.symbols("w1:4"))
ok("Q3b <u,v> = (||u+v||^2 - ||u-v||^2)/4 (symbolic, R^3)",
   sp.expand(((u + w).dot(u + w) - (u - w).dot(u - w)) / 4 - u.dot(w)) == 0)

# ---------------------------------------------------------------- Q4a parameter a
a, lam = sp.symbols("a lambda", real=True)
M4 = sp.Matrix([[a ** 2, 0, 1], [0, a, 0], [1, 0, a ** 2]])
cp = sp.factor((M4 - lam * sp.eye(3)).det())
ok("Q4a char poly = (a-l)((a^2-l)^2-1)", sp.expand(cp - (a - lam) * ((a ** 2 - lam) ** 2 - 1)) == 0, cp)
ok("Q4a eigenvalues a, a^2+1, a^2-1", sp.expand((a - lam) * (a ** 2 + 1 - lam) * (a ** 2 - 1 - lam) - (a - lam) * ((a ** 2 - lam) ** 2 - 1)) == 0)
ok("Q4a PSD set = [1,oo)", sp.solve_univariate_inequality(a ** 2 - 1 >= 0, a, relational=False).intersect(sp.Interval(0, sp.oo)) == sp.Interval(1, sp.oo))
ok("Q4a PD set = (1,oo)", sp.solve_univariate_inequality(a ** 2 - 1 > 0, a, relational=False).intersect(sp.Interval.open(0, sp.oo)) == sp.Interval.open(1, sp.oo))
ok("Q4a a^2+1 > 0 always -> never NSD", sp.solve_univariate_inequality(a ** 2 + 1 <= 0, a, relational=False) == sp.EmptySet)
ok("Q4a a=1: eigenvalues 1, 2, 0 (PSD not PD)", M4.subs(a, 1).eigenvals() == {1: 1, 2: 1, 0: 1})
ok("Q4a a=1/2: eigenvalues of mixed sign", sorted(M4.subs(a, R(1, 2)).eigenvals()) == [R(-3, 4), R(1, 2), R(5, 4)])
ok("Q4a a=-2: eigenvalues -2, 5, 3 (mixed)", M4.subs(a, -2).eigenvals() == {-2: 1, 5: 1, 3: 1})

# ---------------------------------------------------------------- Q4b CRT
ok("Q4b 3 mod 2 = 1", 3 % 2 == 1)
ok("Q4b M=70, M1=14, M2=35, M3=10", 5 * 2 * 7 == 70 and 70 // 5 == 14 and 70 // 2 == 35 and 70 // 7 == 10)
ok("Q4b 14*4=56=1 mod 5 ; 35*1=1 mod 2 ; 10*5=50=1 mod 7", (14 * 4) % 5 == 1 and 35 % 2 == 1 and (10 * 5) % 7 == 1)
ok("Q4b 14 = 4 mod 5 ; 10 = 3 mod 7", 14 % 5 == 4 and 10 % 7 == 3)
ok("Q4b sum 2*14*4 + 1*35*1 + 4*10*5 = 347 = 67 mod 70", 2 * 14 * 4 + 35 + 4 * 10 * 5 == 347 and 347 % 70 == 67)
ok("Q4b sympy: x = 67 mod 70", solve_congruence((2, 5), (3, 2), (4, 7)) == (67, 70))
ok("Q4b check 67: 2 mod 5, 1 mod 2, 4 mod 7", (67 % 5, 67 % 2, 67 % 7) == (2, 1, 4))

# ---------------------------------------------------------------- Q5a orthogonal diagonalization
A5 = sp.Matrix([[5, 0, 0], [0, 4, 2], [0, 2, 1]])
l = sp.symbols("lambda")
ok("Q5a char poly = (5-l)(l^2-5l) = -l(l-5)^2", sp.expand((A5 - l * sp.eye(3)).det() - (-(l) * (l - 5) ** 2)) == 0)
ok("Q5a eigenvalues 5 (x2), 0", A5.eigenvals() == {5: 2, 0: 1})
e1, e2, e3 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 2, 1]), sp.Matrix([0, 1, -2])
ok("Q5a A e1 = 5 e1, A (0,2,1) = 5 (0,2,1), A (0,1,-2) = 0", A5 * e1 == 5 * e1 and A5 * e2 == 5 * e2 and A5 * e3 == sp.zeros(3, 1))
ok("Q5a pairwise orthogonal", e1.dot(e2) == 0 and e1.dot(e3) == 0 and e2.dot(e3) == 0)
s5 = sp.sqrt(5)
Q = sp.Matrix([[1, 0, 0], [0, 2 / s5, 1 / s5], [0, 1 / s5, -2 / s5]])
D = sp.diag(5, 5, 0)
ok("Q5a Q orthogonal", sp.simplify(Q.T * Q) == sp.eye(3))
ok("Q5a A = Q D Q^T", sp.simplify(Q * D * Q.T - A5) == sp.zeros(3, 3))
ok("Q5a row reduction A-5I: rows (0,-1,2),(0,2,-4)", A5 - 5 * sp.eye(3) == sp.Matrix([[0, 0, 0], [0, -1, 2], [0, 2, -4]]))

# ---------------------------------------------------------------- Q5b groups with x = x^-1 (sanity on Z2^3)
G2 = list(itertools.product(range(2), repeat=3))
add = lambda p, q: tuple((s + t) % 2 for s, t in zip(p, q))
ok("Q5b.1 sanity: Z2^3 every element self-inverse and abelian", all(add(g, g) == (0, 0, 0) for g in G2))
pw = lambda g, k: tuple((k * c) % 2 for c in g)
ok("Q5b.2 sanity: x^3 = x and y^5 = y in Z2^3", all(pw(g, 3) == g and pw(g, 5) == g for g in G2))

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
