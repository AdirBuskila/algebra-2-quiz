# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 24B-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/24B-A/check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import random
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational

# ---- Q1a: (2a+b+3c)^2 <= 14 (a^2+b^2+c^2) < 16 (...) unless all zero
al, be, ga = sp.symbols("al be ga", real=True)
ok("Q1a 14(a^2+b^2+c^2) - (2a+b+3c)^2 = (a-2b... Lagrange identity sum of squares",
   sp.expand(14 * (al**2 + be**2 + ga**2) - (2 * al + be + 3 * ga) ** 2
             - ((al * 1 - be * 2) ** 2 + (al * 3 - ga * 2) ** 2 + (be * 3 - ga * 1) ** 2)) == 0)
random.seed(1)
worst = -1e9
for _ in range(5000):
    t = [random.uniform(-5, 5) for _ in range(3)]
    n2 = sum(z * z for z in t)
    worst = max(worst, (2 * t[0] + t[1] + 3 * t[2]) ** 2 / n2)
ok("Q1a max of (2a+b+3c)^2 / (a^2+b^2+c^2) is at most 14 (never > 16)", worst <= 14 + 1e-9, "max ratio %.5f" % worst)

# ---- Q1b: projection in M2
def ip(X, Y):
    return (Y.T * X).trace()


e1 = sp.Matrix([[1, 1], [-1, 1]])
e2 = sp.Matrix([[0, 1], [0, 1]])
e3 = sp.Matrix([[1, 1], [0, 0]])
v = sp.Matrix([[2, 2], [0, 2]])
u1 = e1
u2 = e2 - ip(e2, u1) / ip(u1, u1) * u1
u3 = e3 - ip(e3, u1) / ip(u1, u1) * u1 - ip(e3, u2) / ip(u2, u2) * u2
ok("Q1b u2 = [[-1/2,1/2],[1/2,1/2]]", u2 == sp.Matrix([[-R(1, 2), R(1, 2)], [R(1, 2), R(1, 2)]]))
ok("Q1b u3 = [[1/2,1/2],[1/2,-1/2]]", u3 == sp.Matrix([[R(1, 2), R(1, 2)], [R(1, 2), -R(1, 2)]]))
ok("Q1b norms 4,1,1 and pairwise orthogonal", (ip(u1, u1), ip(u2, u2), ip(u3, u3)) == (4, 1, 1)
   and ip(u1, u2) == 0 and ip(u1, u3) == 0 and ip(u2, u3) == 0)
proj = sum((ip(v, w) / ip(w, w) * w for w in (u1, u2, u3)), sp.zeros(2, 2))
ok("Q1b proj = [[3/2,5/2],[-1/2,3/2]]", proj == sp.Matrix([[R(3, 2), R(5, 2)], [-R(1, 2), R(3, 2)]]), str(proj))
ok("Q1b coefficients 3/2, 1, 1", (ip(v, u1) / 4, ip(v, u2), ip(v, u3)) == (R(3, 2), 1, 1))
ok("Q1b v - proj perp e1,e2,e3", all(ip(v - proj, w) == 0 for w in (e1, e2, e3)))

# ---- Q2a: G = {(a,a^2) : a in Z7*}
G = {(a, (a * a) % 7) for a in range(1, 7)}
mulG = lambda p, q: ((p[0] * q[0]) % 7, (p[1] * q[1]) % 7)
ok("Q2a closed", all(mulG(p, q) in G for p in G for q in G))
ok("Q2a.1 identity (1,1)", all(mulG((1, 1), p) == p for p in G))
ok("Q2a.2 inverse of (2,4) is (4,2)", mulG((2, 4), (4, 2)) == (1, 1) and (4, 2) in G)
ok("Q2a.3 |G| = 6", len(G) == 6)
orders = None
cur2 = (3, 2)
for k in range(1, 20):
    if cur2 == (1, 1):
        orders = k
        break
    cur2 = mulG(cur2, (3, 2))
ok("Q2a.4 (3,2) in G and has order 6", (3, 2) in G and orders == 6, str(orders))
ok("Q2a.4 o(3)=6 and o(2)=3 in Z7*, lcm 6", min(k for k in range(1, 7) if pow(3, k, 7) == 1) == 6 and min(k for k in range(1, 7) if pow(2, k, 7) == 1) == 3)

# ---- Q2b: lambda eigenvalue of A iff c - lambda eigenvalue of cI - A; PD: choose c large
random.seed(2)
allok = True
for _ in range(300):
    n = random.randint(1, 4)
    B = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    A = B + B.T
    c = max(abs(sp.N(t)) for t in A.eigenvals(multiple=True)) + 1
    c = sp.nsimplify(sp.floor(c) + 1)
    M = c * sp.eye(n) - A
    allok = allok and all(M[:k, :k].det() > 0 for k in range(1, n + 1))
ok("Q2b.2 for a symmetric A, cI - A is PD once c exceeds the largest eigenvalue (300 random)", allok)
A2 = sp.Matrix([[2, 1], [1, 2]])
cc = sp.symbols("cc")
ok("Q2b.1 charpoly of cI-A at c-lambda matches A at lambda",
   sp.simplify((cc * sp.eye(2) - A2).charpoly(sp.Symbol("l")).as_expr().subs(sp.Symbol("l"), cc - sp.Symbol("m"))
               - A2.charpoly(sp.Symbol("m")).as_expr()) == 0)

# ---- Q3a: [[1,c,0],[c,1,c],[0,c,1]]
c = sp.symbols("c", real=True)
M3 = sp.Matrix([[1, c, 0], [c, 1, c], [0, c, 1]])
lam = sp.symbols("lam")
roots = sp.solve(M3.charpoly(lam).as_expr(), lam)
ok("Q3a eigenvalues 1, 1+-sqrt2 c", {sp.simplify(r) for r in roots} == {1, 1 + sp.sqrt(2) * c, 1 - sp.sqrt(2) * c}, str(roots))
r2 = sp.sqrt(2)
ok("Q3a PSD iff |c| <= 1/sqrt2", sp.solve_univariate_inequality(1 - r2 * sp.Abs(c) >= 0, c, relational=False) == sp.Interval(-1 / r2, 1 / r2))
for cv, kind in [(0, "pd"), (R(1, 2), "pd"), (-R(1, 2), "pd"), (1 / r2, "psd"), (-1 / r2, "psd"), (R(3, 4), "indef"), (-1, "indef")]:
    evs = [sp.N(t) for t in M3.subs(c, cv).eigenvals(multiple=True)]
    lo = min(evs)
    res = "pd" if lo > 1e-12 else ("psd" if lo > -1e-12 else "indef")
    ok("Q3a c=%s is %s" % (cv, kind), res == kind, "min eig %.5f" % lo)

# ---- Q3b: least squares (-3,-1),(0,1),(1,3),(3,3),(4,6)
pts = [(-3, -1), (0, 1), (1, 3), (3, 3), (4, 6)]
A = sp.Matrix([[p[0], 1] for p in pts])
bb = sp.Matrix([p[1] for p in pts])
ok("Q3b A^T A = [[35,5],[5,5]], A^T b = [[39],[12]]", A.T * A == sp.Matrix([[35, 5], [5, 5]]) and A.T * bb == sp.Matrix([39, 12]))
sol = (A.T * A).solve(A.T * bb)
ok("Q3b m = 9/10, n = 3/2", sol == sp.Matrix([R(9, 10), R(3, 2)]), str(list(sol)))

# ---- Q4: x*y = (x+y)/(1+xy) on (-1,1)
x, y, z = sp.symbols("x y z", real=True)
st = lambda p, q: (p + q) / (1 + p * q)
ok("Q4a closure: 1 +- x*y = (1 +- x)(1 +- y)/(1+xy)",
   sp.simplify(1 + st(x, y) - (1 + x) * (1 + y) / (1 + x * y)) == 0 and sp.simplify(1 - st(x, y) - (1 - x) * (1 - y) / (1 + x * y)) == 0)
ok("Q4a associative: both sides (x+y+z+xyz)/(1+xy+xz+yz)",
   sp.simplify(st(st(x, y), z) - (x + y + z + x * y * z) / (1 + x * y + x * z + y * z)) == 0
   and sp.simplify(st(x, st(y, z)) - (x + y + z + x * y * z) / (1 + x * y + x * z + y * z)) == 0)
ok("Q4a identity 0, inverse -x, commutative", sp.simplify(st(x, 0) - x) == 0 and sp.simplify(st(x, -x)) == 0 and sp.simplify(st(x, y) - st(y, x)) == 0)
random.seed(8)
good = True
for _ in range(2000):
    p = R(random.randint(-99, 99), 100)
    q = R(random.randint(-99, 99), 100)
    r_ = st(p, q)
    good = good and -1 < r_ < 1 and 1 + p * q > 0
ok("Q4a closure holds on 2000 random rationals in (-1,1); H = G cap Q closed (result rational)", good)

# ---- Q5a: orthogonal diagonalization of [[1,1,0],[1,1,0],[0,0,2]]
A5 = sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 2]])
ok("Q5a eigenvalues {2:2, 0:1}", A5.eigenvals() == {2: 2, 0: 1})
s2 = sp.sqrt(2)
Q = sp.Matrix([[1 / s2, 0, -1 / s2], [1 / s2, 0, 1 / s2], [0, 1, 0]])
D = sp.diag(2, 2, 0)
ok("Q5a Q orthogonal and A = Q D Q^T", sp.simplify(Q.T * Q) == sp.eye(3) and sp.simplify(Q * D * Q.T - A5) == sp.zeros(3, 3))

# ---- Q5b: CRT x=2 (5), x=3 (7), x=19 (11)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

res = solve_congruence((2, 5), (3, 7), (19, 11))
ok("Q5b x = 52 mod 385", res == (52, 385), str(res))
ok("Q5b 19 = 8 mod 11; M=77,55,35; x_i=3,6,6; sum=3132",
   19 % 11 == 8 and (77 * 3) % 5 == 1 and (55 * 6) % 7 == 1 and (35 * 6) % 11 == 1
   and 2 * 77 * 3 + 3 * 55 * 6 + 8 * 35 * 6 == 3132 and 3132 % 385 == 52)
ok("Q5b x=52 satisfies all", 52 % 5 == 2 and 52 % 7 == 3 and 52 % 11 == 19 % 11)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
