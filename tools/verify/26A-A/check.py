# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 26A-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/26A-A/check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import random
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: orthogonal diagonalization of A
A = sp.Matrix([[3, 1, 0], [1, 3, 0], [0, 0, 1]])
ev = A.eigenvals()
ok("Q1a eigenvalues {4,2,1}", ev == {4: 1, 2: 1, 1: 1}, str(ev))
r2 = sp.sqrt(2)
v1 = sp.Matrix([1 / r2, 1 / r2, 0])
v2 = sp.Matrix([-1 / r2, 1 / r2, 0])
v3 = sp.Matrix([0, 0, 1])
ok("Q1a A v1 = 4 v1", sp.simplify(A * v1 - 4 * v1) == sp.zeros(3, 1))
ok("Q1a A v2 = 2 v2", sp.simplify(A * v2 - 2 * v2) == sp.zeros(3, 1))
ok("Q1a A v3 = 1 v3", sp.simplify(A * v3 - v3) == sp.zeros(3, 1))
P = sp.Matrix.hstack(v1, v2, v3)
ok("Q1a P orthogonal", sp.simplify(P.T * P) == sp.eye(3))
D = sp.diag(4, 2, 1)
ok("Q1a A = P D P^T (correct P^T)", sp.simplify(P * D * P.T - A) == sp.zeros(3, 3))
# the PDF prints the third row of P^T as (1/sqrt2, 0, 1): that is NOT the transpose of P
Pbad = sp.Matrix([[1 / r2, -1 / r2, 0], [1 / r2, 1 / r2, 0], [1 / r2, 0, 1]])
ok("Q1a printed right factor is a typo (P D Pbad != A)", sp.simplify(P * D * Pbad - A) != sp.zeros(3, 3))
# the printed labels (A-3I) are typos for A-4I, A-2I, A-I
ok("Q1a A-4I matches printed matrix", A - 4 * sp.eye(3) == sp.Matrix([[-1, 1, 0], [1, -1, 0], [0, 0, -3]]))
ok("Q1a A-2I matches printed matrix", A - 2 * sp.eye(3) == sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, -1]]))
ok("Q1a A-I matches printed matrix", A - sp.eye(3) == sp.Matrix([[2, 1, 0], [1, 2, 0], [0, 0, 0]]))

# ---- Q1b: Cauchy-Schwarz (Engel / Titu) numeric spot-check, random positive reals
random.seed(1)
worst = 1e9
for _ in range(5000):
    n = random.randint(1, 6)
    a = [random.uniform(0.1, 9) for _ in range(n)]
    b = [random.uniform(0.1, 9) for _ in range(n)]
    lhs = sum(x * x / y for x, y in zip(a, b))
    rhs = sum(a) ** 2 / sum(b)
    worst = min(worst, lhs - rhs)
ok("Q1b inequality holds on 5000 random samples", worst >= -1e-9, "min gap %.3g" % worst)

# ---- Q2: K = {[[a,b],[-b,a]] : a^2+b^2 = 1 mod 7}
K = [(a, b) for a in range(7) for b in range(7) if (a * a + b * b) % 7 == 1]
ok("Q2.2 |K| = 8", len(K) == 8, str(K))
ok("Q2.2 split 2+2+4", sum(1 for a, b in K if a == 0) == 2 and sum(1 for a, b in K if b == 0) == 2
   and sum(1 for a, b in K if a and b) == 4)


def mat(a, b):
    return sp.Matrix([[a, b], [-b, a]])


def modm(M):
    return M.applyfunc(lambda t: t % 7)


Kset = {(a, b) for a, b in K}
closed = all(((a * c - b * d) % 7, (a * d + b * c) % 7) in Kset for (a, b) in K for (c, d) in K)
ok("Q2.1 closed under product", closed)
invs = all(((a) % 7, (-b) % 7) in Kset for (a, b) in K)  # inverse of (a,b) is (a,-b) since a^2+b^2=1
ok("Q2.1 inverse (a,-b) in K and correct", invs and all(
    modm(mat(a, b) * mat(a, -b)) == sp.eye(2) for (a, b) in K))
X = sp.Matrix([[2, 2], [5, 2]])
ok("Q2.3 X in K (2,2) with -b=5 mod 7", (X[1, 0] - (-2)) % 7 == 0 and (2 * 2 + 2 * 2) % 7 == 1 and (2 * 2 + 5 * 5) % 7 == 1)
pw = {}
M = sp.eye(2)
for k in range(1, 9):
    M = modm(M * X)
    pw[k] = M
ok("Q2.3 X^2 = [[0,1],[-1,0]]", pw[2] == sp.Matrix([[0, 1], [6, 0]]))
ok("Q2.3 X^4 = -I", pw[4] == sp.Matrix([[6, 0], [0, 6]]))
ok("Q2.3 X^8 = I and order 8", pw[8] == sp.eye(2) and all(pw[k] != sp.eye(2) for k in range(1, 8)))
ok("Q2.4 X^-1 = [[2,5],[-5,2]] mod 7", modm(X * sp.Matrix([[2, 5], [-5, 2]])) == sp.eye(2))
ok("Q2.4 sympy inv_mod agrees", X.inv_mod(7) == modm(sp.Matrix([[2, 5], [-5, 2]])))
ok("Q2.5 K cyclic: X has order 8 = |K|", len(K) == 8 and all(pw[k] != sp.eye(2) for k in range(1, 8)))

# ---- Q3a: positive (semi)definiteness for parameter x
x = sp.symbols("x", real=True)
M3 = sp.Matrix([[1, x, 0], [x, 2, x], [0, x, 1]])
lam = sp.symbols("lam")
cp = sp.factor(M3.charpoly(lam).as_expr())
print("charpoly:", cp)
roots = sp.solve(sp.Eq(M3.charpoly(lam).as_expr(), 0), lam)
rr = sorted([sp.simplify(t) for t in roots], key=lambda t: float(t.subs(x, 0.3)))
print("roots:", rr)
ok("Q3a eigenvalues 1 and (3 +- sqrt(8x^2+1))/2",
   {sp.simplify(t) for t in roots} == {sp.Integer(1), sp.simplify((3 + sp.sqrt(8 * x**2 + 1)) / 2),
                                       sp.simplify((3 - sp.sqrt(8 * x**2 + 1)) / 2)})
ok("Q3a smallest eigenvalue >= 0 iff x^2<=1",
   sp.solve_univariate_inequality((3 - sp.sqrt(8 * x**2 + 1)) / 2 >= 0, x, relational=False) == sp.Interval(-1, 1))
ok("Q3a strictly >0 iff -1<x<1",
   sp.solve_univariate_inequality((3 - sp.sqrt(8 * x**2 + 1)) / 2 > 0, x, relational=False) == sp.Interval.open(-1, 1))
# leading principal minors cross-check
m1 = M3[:1, :1].det()
m2 = M3[:2, :2].det()
m3 = M3.det()
print("minors:", m1, sp.expand(m2), sp.expand(m3))
ok("Q3a det = 2 - 2x^2, leading minors 1, 2-x^2", sp.expand(m3) == 2 - 2 * x**2 and m1 == 1 and sp.expand(m2) == 2 - x**2)
# boundary x=1 is PSD but singular, x=1.01 indefinite, x=0.5 PD, x=-1 PSD
for xv, kind in [(sp.Rational(1, 2), "pd"), (1, "psd"), (-1, "psd"), (sp.Rational(101, 100), "indef"), (0, "pd")]:
    ev_ = [sp.N(t) for t in M3.subs(x, xv).eigenvals().keys()]
    lo = min(ev_)
    res = "pd" if lo > 1e-12 else ("psd" if lo > -1e-12 else "indef")
    ok("Q3a x=%s is %s" % (xv, kind), res == kind, "min eig %.6f" % lo)

# ---- Q3b/c: projection identities, numeric on random vectors
random.seed(2)
worst = 0.0
for _ in range(2000):
    n = random.randint(2, 5)
    av = sp.Matrix([random.randint(-5, 5) for _ in range(n)])
    bv = sp.Matrix([random.randint(-5, 5) for _ in range(n)])
    if av.norm() == 0:
        continue
    p = (bv.dot(av) / av.dot(av)) * av
    c = bv - p
    assert c.dot(av) == 0
    assert c.dot(c) + p.dot(p) == bv.dot(bv)
ok("Q3b c perp a and Pythagoras on 2000 random integer vectors", True)

# ---- Q4: group (Z^2, o), (a,b)o(x,y) = (a+x, b+(-1)^a y)


def op(p, q):
    return (p[0] + q[0], p[1] + (-1) ** (p[0] % 2) * q[1])


random.seed(3)
R = range(-6, 7)
assoc = all(op(op(p, q), r) == op(p, op(q, r)) for p in itertools.product(R, R) for q in itertools.product([-3, -2, -1, 0, 1, 2, 5], R)
            for r in [(0, 0), (1, 2), (-2, 3), (3, -5), (4, 4), (-1, 7)])
ok("Q4a associative (brute force)", assoc)
ok("Q4a (0,0) is two-sided identity", all(op((0, 0), p) == p and op(p, (0, 0)) == p for p in itertools.product(R, R)))
ok("Q4a inverse of (a,b) is (-a, (-1)^(1-a) b)",
   all(op(p, (-p[0], (-1) ** ((1 - p[0]) % 2) * p[1])) == (0, 0) and op((-p[0], (-1) ** ((1 - p[0]) % 2) * p[1]), p) == (0, 0)
       for p in itertools.product(R, R)))
ok("Q4b not abelian: (1,1)o(1,0)=(2,1), (1,0)o(1,1)=(2,-1)", op((1, 1), (1, 0)) == (2, 1) and op((1, 0), (1, 1)) == (2, -1))
center = [p for p in itertools.product(range(-8, 9), range(-8, 9))
          if all(op(p, q) == op(q, p) for q in itertools.product(range(-8, 9), range(-8, 9)))]
print("center within [-8,8]^2:", center[:6], "...", len(center))
ok("Q4c commuting elements are exactly a even AND b = 0 (NOT 'a even and x even')",
   all(p[0] % 2 == 0 and p[1] == 0 for p in center) and
   len(center) == len([a for a in range(-8, 9) if a % 2 == 0]))
ok("Q4c official answer 'a even, x even' is wrong/garbled: (2,1) does not commute with (1,0)",
   op((2, 1), (1, 0)) != op((1, 0), (2, 1)))

# ---- Q5a: P = u u^T + v v^T for an orthonormal basis; test on a concrete rotated basis
Q_, _ = sp.Matrix([[1, 1, 0], [1, -1, 1], [0, 1, 2]]).QRdecomposition()
u, v, w = Q_[:, 0], Q_[:, 1], Q_[:, 2]
Pm = u * u.T + v * v.T
ok("Q5a1 P u = u, P v = v, P w = 0", sp.simplify(Pm * u - u) == sp.zeros(3, 1) and sp.simplify(Pm * v - v) == sp.zeros(3, 1)
   and sp.simplify(Pm * w) == sp.zeros(3, 1))
ok("Q5a2 P symmetric with eigenvalues {1,1,0}", Pm == Pm.T and Pm.eigenvals() == {1: 2, 0: 1})
ok("Q5a3 kernel is Sp{w}", len(Pm.nullspace()) == 1 and sp.simplify(Pm.nullspace()[0].cross(w)) == sp.zeros(3, 1))

# ---- Q5b: CRT
from sympy.ntheory.modular import solve_congruence  # noqa: E402

sol = solve_congruence((2, 3), (3, 4), (5, 7))
ok("Q5b x = 47 mod 84 (solve_congruence)", sol == (47, 84), str(sol))
ok("Q5b original system 2x=1 (3), 3x=1 (4), 2x=3 (7) at x=47",
   (2 * 47) % 3 == 1 and (3 * 47) % 4 == 1 and (2 * 47) % 7 == 3)
ok("Q5b only solution mod 84", [t for t in range(84) if (2 * t) % 3 == 1 and (3 * t) % 4 == 1 and (2 * t) % 7 == 3] == [47])
ok("Q5b M1,M2,M3 = 28,21,12; x1,x2,x3 = 1,1,3",
   (28 * 1) % 3 == 1 and (21 * 1) % 4 == 1 and (12 * 3) % 7 == 1 and 2 * 28 * 1 + 3 * 21 * 1 + 5 * 12 * 3 == 299 and 299 % 84 == 47)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
