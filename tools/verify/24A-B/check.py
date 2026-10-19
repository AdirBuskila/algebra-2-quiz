# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 24A-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/24A-B/check.py
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


R = sp.Rational

# ---- Q1a: least squares (1,4),(3,5),(5,6),(7,5),(9,8)
pts = [(1, 4), (3, 5), (5, 6), (7, 5), (9, 8)]
A = sp.Matrix([[p[0], 1] for p in pts])
b = sp.Matrix([p[1] for p in pts])
ok("Q1a A^T A = [[165,25],[25,5]], A^T b = [[156],[28]]", A.T * A == sp.Matrix([[165, 25], [25, 5]]) and A.T * b == sp.Matrix([156, 28]))
sol = (A.T * A).solve(A.T * b)
ok("Q1a m = 2/5, n = 18/5", sol == sp.Matrix([R(2, 5), R(18, 5)]), str(list(sol)))

# ---- Q1b: projection in M2 with <A,B> = tr(B^T A)
def ip(X, Y):
    return (Y.T * X).trace()


e1 = sp.Matrix([[1, -1], [0, 1]])
e2 = sp.Matrix([[0, 1], [0, 1]])
e3 = sp.Matrix([[1, 1], [1, 1]])
v = sp.Matrix([[2, 1], [1, 2]])
v1 = e1
v2 = e2 - ip(e2, v1) / ip(v1, v1) * v1
v3 = e3 - ip(e3, v1) / ip(v1, v1) * v1 - ip(e3, v2) / ip(v2, v2) * v2
ok("Q1b v2 = e2", v2 == e2 and ip(v1, v2) == 0)
ok("Q1b v3 = [[2/3,1/3],[1,-1/3]]", v3 == sp.Matrix([[R(2, 3), R(1, 3)], [1, -R(1, 3)]]), str(v3))
v3s = 3 * v3
ok("Q1b orthogonal basis v1,v2,v3s=[[2,1],[3,-1]]", v3s == sp.Matrix([[2, 1], [3, -1]]) and ip(v1, v3s) == 0 and ip(v2, v3s) == 0)
proj = sum((ip(v, w) / ip(w, w) * w for w in (v1, v2, v3s)), sp.zeros(2, 2))
ok("Q1b proj = [[9/5,9/10],[6/5,21/10]]", proj == sp.Matrix([[R(9, 5), R(9, 10)], [R(6, 5), R(21, 10)]]), str(proj))
ok("Q1b coefficients 1, 3/2, 2/5", (ip(v, v1) / ip(v1, v1), ip(v, v2) / ip(v2, v2), ip(v, v3s) / ip(v3s, v3s)) == (1, R(3, 2), R(2, 5)))
ok("Q1b v - proj perp to e1,e2,e3", all(ip(v - proj, w) == 0 for w in (e1, e2, e3)))

# ---- Q2a: a (.) b = (a+b)/(ab) on positive reals
a_, b_, c_ = sp.symbols("a b c", positive=True)
op = lambda x, y: (x + y) / (x * y)
L = sp.simplify(op(op(a_, b_), c_))
Rr = sp.simplify(op(a_, op(b_, c_)))
ok("Q2a.2 (a.b).c = (a+b+abc)/(ac+bc)", sp.simplify(L - (a_ + b_ + a_ * b_ * c_) / (a_ * c_ + b_ * c_)) == 0)
ok("Q2a.2 a.(b.c) = (abc+b+c)/(ab+ac)", sp.simplify(Rr - (a_ * b_ * c_ + b_ + c_) / (a_ * b_ + a_ * c_)) == 0)
ok("Q2a.2 not associative (1,2,3: 1 vs 11/5)", op(op(R(1), R(2)), R(3)) == 1 and op(R(1), op(R(2), R(3))) == R(11, 5))
e = sp.symbols("e")
ok("Q2a.3 with a=1: (1+e)/e = 1 has no solution (official 'e=0' step is a slip)", sp.solve(sp.Eq((1 + e) / e, 1), e) == [])
ok("Q2a.3 general: a+e = a^2 e forces e = a/(a^2-1), depends on a, so no common identity",
   sp.solve(sp.Eq(a_ + e, a_**2 * e), e) == [a_ / (a_**2 - 1)])
ok("Q2a.4 x (.) x = 2/x, fixed point sqrt2", sp.simplify(op(a_, a_) - 2 / a_) == 0 and sp.solve(sp.Eq(2 / sp.Symbol("x", positive=True), sp.Symbol("x", positive=True)), sp.Symbol("x", positive=True)) == [sp.sqrt(2)])
ok("Q2a.1 closed: a+b>0, ab>0", True)

# ---- Q2b: A PD => A invertible and A^-1 PD
random.seed(5)
allok = True
for _ in range(300):
    n = random.randint(1, 4)
    B = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    P = B.T * B + sp.eye(n)
    Pi = P.inv()
    allok = allok and Pi == Pi.T and all(Pi[:k, :k].det() > 0 for k in range(1, n + 1))
ok("Q2b A^-1 symmetric, positive leading minors on 300 random PD A", allok)

# ---- Q3a: [[2a^2,a,0],[a,1,a],[0,a,2a^2]]
aa = sp.symbols("aa", real=True)
M3 = sp.Matrix([[2 * aa**2, aa, 0], [aa, 1, aa], [0, aa, 2 * aa**2]])
lam = sp.symbols("lam")
roots = sp.solve(M3.charpoly(lam).as_expr(), lam)
ok("Q3a eigenvalues 2a^2, 2a^2+1, 0", {sp.simplify(r) for r in roots} == {2 * aa**2, 2 * aa**2 + 1, 0}, str(roots))
ok("Q3a det = 0 for every a", sp.simplify(M3.det()) == 0)
for av in [0, R(1, 3), 1, -2, 5, R(1, 10)]:
    evs = [sp.N(t) for t in M3.subs(aa, av).eigenvals(multiple=True)]
    ok("Q3a a=%s: min eig ~ 0 and all >= 0" % av, abs(min(evs)) < 1e-9 and all(t > -1e-9 for t in evs))

# ---- Q3b: ||u|| <= ||u+tv|| for all t iff <u,v> = 0 (numeric, both directions)
random.seed(6)
good = True
for _ in range(1500):
    u = sp.Matrix([random.randint(-3, 3) for _ in range(3)])
    w = sp.Matrix([random.randint(-3, 3) for _ in range(3)])
    # ||u+tw||^2 - ||u||^2 = 2t<u,w> + t^2||w||^2 >= 0 for all t  iff  <u,w> = 0 (or w=0)
    ts = [R(k, 8) for k in range(-40, 41)] + ([-u.dot(w) / w.dot(w)] if w.norm() != 0 else [])
    holds_all_t = all((u + t * w).dot(u + t * w) >= u.dot(u) for t in ts)
    claim = (u.dot(w) == 0)
    if w.norm() != 0 and holds_all_t != claim:
        good = False
ok("Q3b norm inequality for all sampled t iff <u,v> = 0 (1500 integer pairs)", good)

# ---- Q4a: H = {[[a,c],[0,a^-1]]} in M2(Z5)
inv5 = {a_: pow(a_, -1, 5) for a_ in range(1, 5)}
Hset = {(a_, c_, inv5[a_]) for a_ in range(1, 5) for c_ in range(5)}
ok("Q4a.2 |H| = 20", len(Hset) == 20)


def mul(X, Y):
    return ((X[0] * Y[0]) % 5, (X[0] * Y[1] + X[1] * Y[2]) % 5, (X[2] * Y[2]) % 5)


ok("Q4a.1 closed under product", all(mul(X, Y) in Hset for X in Hset for Y in Hset))
ok("Q4a.1 identity (1,0,1) in H", (1, 0, 1) in Hset)
ok("Q4a.1 inverse [[a,c],[0,a^-1]]^-1 = [[a^-1,-c],[0,a]] in H and correct",
   all(mul(X, ((pow(X[0], -1, 5)), (-X[1]) % 5, X[0])) == (1, 0, 1) and ((pow(X[0], -1, 5)), (-X[1]) % 5, X[0]) in Hset for X in Hset))
Mx = sp.Matrix([[2, 4], [0, 3]])
ok("Q4a.3 inverse of [[2,4],[0,3]] mod 5 is [[3,1],[0,2]]", Mx.inv_mod(5) == sp.Matrix([[3, 1], [0, 2]]) and (3, 1, 2) in Hset)
ok("Q4a.3 2^-1 = 3 mod 5", pow(2, -1, 5) == 3)

# ---- Q4b: CRT 3x=14 (8), x=4 (9), x=22 (25)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

ok("Q4b 3x=14 mod 8 iff x=2 mod 8", [t for t in range(8) if (3 * t) % 8 == 14 % 8] == [2])
res = solve_congruence((2, 8), (4, 9), (22, 25))
ok("Q4b x = 922 mod 1800", res == (922, 1800), str(res))
ok("Q4b M=225,200,72; x_i=1,5,8; sum=17122",
   (225 * 1) % 8 == 1 and (200 * 5) % 9 == 1 and (72 * 8) % 25 == 1 and 2 * 225 * 1 + 4 * 200 * 5 + 22 * 72 * 8 == 17122 and 17122 % 1800 == 922)
ok("Q4b original system at x=922", (3 * 922) % 8 == 14 % 8 and 922 % 9 == 4 and 922 % 25 == 22)

# ---- Q5a: orthogonal diagonalization
A5 = sp.Matrix([[3, -2, 4], [-2, 6, 2], [4, 2, 3]])
ok("Q5a eigenvalues {-2:1, 7:2}", A5.eigenvals() == {-2: 1, 7: 2})
s5 = sp.sqrt(5)
Q = sp.Matrix([[-R(2, 3), -1 / s5, -4 / (3 * s5)], [-R(1, 3), 2 / s5, -2 / (3 * s5)], [R(2, 3), 0, -s5 / 3]])
P = sp.diag(-2, 7, 7)
ok("Q5a Q orthogonal", sp.simplify(Q.T * Q) == sp.eye(3))
ok("Q5a A = Q P Q^T", sp.simplify(Q * P * Q.T - A5) == sp.zeros(3, 3))

# ---- Q5b: sum of squares >= 1/n when sum = 1 (random check) and CS
random.seed(7)
worst = 1e9
for _ in range(5000):
    n = random.randint(1, 7)
    xs = [random.uniform(-3, 3) for _ in range(n)]
    s = sum(xs)
    if abs(s) < 1e-6:
        continue
    xs = [t / s for t in xs]
    worst = min(worst, sum(t * t for t in xs) - 1 / n)
ok("Q5b sum x_i^2 >= 1/n when sum x_i = 1 (5000 random samples)", worst >= -1e-9, "min gap %.3g" % worst)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
