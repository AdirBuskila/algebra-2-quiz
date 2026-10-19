# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 24A-C (algebra-2); keys come from a handwritten student solution.
Run: PYTHONUTF8=1 py -I tools/verify/24A-C/check.py   Prints ASCII only. Exit code 1 on any mismatch."""
import random
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational

# ---- Q1a: least squares (-4,-1),(-2,0),(2,4),(4,5),(5,6)
pts = [(-4, -1), (-2, 0), (2, 4), (4, 5), (5, 6)]
A = sp.Matrix([[p[0], 1] for p in pts])
b = sp.Matrix([p[1] for p in pts])
ok("Q1a A^T A = [[65,5],[5,5]], A^T b = [[62],[14]]", A.T * A == sp.Matrix([[65, 5], [5, 5]]) and A.T * b == sp.Matrix([62, 14]))
sol = (A.T * A).solve(A.T * b)
ok("Q1a m = 4/5, n = 2", sol == sp.Matrix([R(4, 5), 2]), str(list(sol)))

# ---- Q1b: Cauchy-Schwarz in C[0,1]: ||x^3||^2 = 1/7; numeric spot check with polynomials
x = sp.symbols("x")
ok("Q1b integral of x^6 over [0,1] is 1/7", sp.integrate(x**6, (x, 0, 1)) == R(1, 7))
random.seed(3)
good = True
for _ in range(200):
    f = sum(random.randint(-3, 3) * x**k for k in range(4))
    lhs = sp.integrate(x**3 * f, (x, 0, 1)) ** 2
    rhs = R(1, 7) * sp.integrate(f**2, (x, 0, 1))
    good = good and lhs <= rhs
ok("Q1b (int x^3 f)^2 <= (1/7) int f^2 on 200 random cubics", good)

# ---- Q2a: (a,b)*(x,y) = (ay+bx, by) on R^2 minus the origin
a, b2, xx, y = sp.symbols("a b x y")
star = lambda p, q: (p[0] * q[1] + p[1] * q[0], p[1] * q[1])
ok("Q2a.1 commutative", all(sp.simplify(u - v) == 0 for u, v in zip(star((a, b2), (xx, y)), star((xx, y), (a, b2)))))
ok("Q2a.2 identity e = (0,1)", star((a, b2), (0, 1)) == (a, b2) and star((0, 1), (a, b2)) == (a, b2))
# identity uniqueness: solve (a,b)*(e1,e2) = (a,b) for all (a,b)
e1, e2 = sp.symbols("e1 e2")
eqs = [sp.expand(c - d) for c, d in zip(star((1, 1), (e1, e2)), (1, 1))] + [sp.expand(c - d) for c, d in zip(star((0, 1), (e1, e2)), (0, 1))]
ok("Q2a.2 identity is unique (0,1)", sp.solve(eqs, [e1, e2], dict=True) == [{e1: 0, e2: 1}])
ok("Q2a.3 (a,0)*(x,y) = (ay,0) is never the identity (0,1): no inverse", star((a, 0), (xx, y))[1] == 0)
ok("Q2a.3 the set is not even closed: (1,0)*(1,0) = (0,0), outside R^2 minus origin", star((1, 0), (1, 0)) == (0, 0))

# ---- Q2b: A PD => I + A^2 PD
random.seed(4)
allok = True
for _ in range(300):
    n = random.randint(1, 4)
    B = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    P = B.T * B + sp.eye(n)
    M = sp.eye(n) + P * P
    allok = allok and M == M.T and all(M[:k, :k].det() > 0 for k in range(1, n + 1))
ok("Q2b I + A^2 symmetric with positive leading minors on 300 random PD A", allok)

# ---- Q4a: [[a^2,0,1],[0,a,0],[1,0,a^2]]
aa = sp.symbols("aa", real=True)
M3 = sp.Matrix([[aa**2, 0, 1], [0, aa, 0], [1, 0, aa**2]])
lam = sp.symbols("lam")
roots = sp.solve(M3.charpoly(lam).as_expr(), lam)
ok("Q4a eigenvalues a, a^2-1, a^2+1", {sp.simplify(r) for r in roots} == {aa, aa**2 - 1, aa**2 + 1}, str(roots))
for av, kind in [(2, "pd"), (R(3, 2), "pd"), (1, "psd"), (R(1, 2), "indef"), (0, "indef"), (-2, "indef"), (-1, "indef")]:
    evs = [sp.N(t) for t in M3.subs(aa, av).eigenvals(multiple=True)]
    lo = min(evs)
    res = "pd" if lo > 1e-12 else ("psd" if lo > -1e-12 else "indef")
    ok("Q4a a=%s is %s" % (av, kind), res == kind, "min eig %.5f" % lo)
ok("Q4a never negative semidefinite: a^2+1 > 0", sp.solve_univariate_inequality(aa**2 + 1 <= 0, aa, relational=False) == sp.EmptySet)

# ---- Q4b: CRT x=5 (3), x=4 (2), x=6 (7)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

res = solve_congruence((5, 3), (4, 2), (6, 7))
ok("Q4b x = 20 mod 42 (solve_congruence)", res == (20, 42), str(res))
ok("Q4b reduced residues 2, 0, 6; M = 14, 21, 6; x_i = 2, 1, 6",
   (14 * 2) % 3 == 1 and (21 * 1) % 2 == 1 and (6 * 6) % 7 == 1 and 5 % 3 == 2 and 4 % 2 == 0)
ok("Q4b sum 5*14*2 + 4*21*1 + 6*6*6 = 440, 440 mod 42 = 20", 5 * 14 * 2 + 4 * 21 * 1 + 6 * 6 * 6 == 440 and 440 % 42 == 20)
ok("Q4b x=20 satisfies all three", 20 % 3 == 5 % 3 and 20 % 2 == 4 % 2 and 20 % 7 == 6)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
