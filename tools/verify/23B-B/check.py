# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 23B-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/23B-B/check.py
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


# ---- Q1a: least squares line through 5 points
pts = [(6, 10), (2, 2), (0, 1), (-1, 0), (-2, -3)]
A = sp.Matrix([[x, 1] for x, y in pts])
b = sp.Matrix([y for x, y in pts])
sol = (A.T * A).LUsolve(A.T * b)
ok("Q1a A^T A = [[45,5],[5,5]]", A.T * A == sp.Matrix([[45, 5], [5, 5]]))
ok("Q1a A^T b = (70,10)", A.T * b == sp.Matrix([70, 10]))
ok("Q1a m=1.5 n=0.5", sol == sp.Matrix([sp.Rational(3, 2), sp.Rational(1, 2)]), str(list(sol)))

# ---- Q1b: (int f/x)^2 <= 1/2 int f^2 on [1,2]; ||1/x||^2 = 1/2 ; spot check with several f
x = sp.symbols("x", positive=True)
ok("Q1b int_1^2 1/x^2 = 1/2", sp.integrate(1 / x**2, (x, 1, 2)) == sp.Rational(1, 2))
for f in [x, x**2, sp.sin(x), sp.exp(x), 1 / x, 3 + x]:
    lhs = sp.integrate(f / x, (x, 1, 2)) ** 2
    rhs = sp.Rational(1, 2) * sp.integrate(f**2, (x, 1, 2))
    ok("Q1b spot f=%s" % f, sp.N(lhs - rhs) <= 1e-12, "gap %.4g" % sp.N(rhs - lhs))

# ---- Q2a: G = Z5* x Z7*
ok("Q2a.2 inverse of (2,3) is (3,5)", (2 * 3) % 5 == 1 and (3 * 5) % 7 == 1)
ok("Q2a.3 |G| = 24", 4 * 6 == 24)


def order(a, m):
    k, v = 1, a % m
    while v != 1:
        v = v * a % m
        k += 1
    return k


ok("Q2a.4 ord 2 mod 5 = 4, ord 3 mod 7 = 6, lcm = 12", order(2, 5) == 4 and order(3, 7) == 6 and sp.ilcm(4, 6) == 12)

# ---- Q2b: A pos. semidefinite symmetric => -A - B^T B is NSD, B^T A B is PSD (random check)
R = lambda t: float(sp.re(sp.N(t)))
random.seed(3)
worst1 = worst2 = 1e9
for _ in range(300):
    n = random.randint(1, 4)
    M = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    Aa = M.T * M
    B = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    e1 = max((-Aa - B.T * B).eigenvals(multiple=True), key=R)
    e2 = min((B.T * Aa * B).eigenvals(multiple=True), key=R)
    worst1 = min(worst1, -R(e1))
    worst2 = min(worst2, R(e2))
ok("Q2b.1 -A-B^TB has all eigenvalues <= 0 (300 random)", worst1 >= -1e-9)
ok("Q2b.2 B^TAB has all eigenvalues >= 0 (300 random)", worst2 >= -1e-9)

# ---- Q3a: [[a^2,0,1],[0,a,0],[1,0,a^2]]
a, lam = sp.symbols("a lambda", real=True)
M3 = sp.Matrix([[a**2, 0, 1], [0, a, 0], [1, 0, a**2]])
ev = M3.eigenvals()
ok("Q3a eigenvalues a, a^2+1, a^2-1", set(sp.simplify(k) for k in ev) == {a, a**2 + 1, a**2 - 1}, str(ev))
ok("Q3a PSD iff a>=1 (grid)", all((min(float(t.subs(a, v)) for t in ev) >= 0) == (v >= 1)
                                  for v in [sp.Rational(k, 4) for k in range(-12, 13)]))
ok("Q3a PD iff a>1 (grid)", all((min(float(t.subs(a, v)) for t in ev) > 0) == (v > 1)
                                for v in [sp.Rational(k, 4) for k in range(-12, 13)]))
ok("Q3a never NSD (grid)", all(max(float(t.subs(a, v)) for t in ev) > 0 for v in [sp.Rational(k, 4) for k in range(-12, 13)]))

# ---- Q3b: CRT x=3(4), 2(3), 4(5)
sols = [v for v in range(60) if v % 4 == 3 and v % 3 == 2 and v % 5 == 4]
ok("Q3b unique solution 59 mod 60", sols == [59], str(sols))
ok("Q3b official 359 = 59 mod 60", 359 % 60 == 59)
ok("Q3b x1,x2,x3 = 3,2,3", (15 * 3) % 4 == 1 and (20 * 2) % 3 == 1 and (12 * 3) % 5 == 1)

# ---- Q4a: orthogonal diagonalization of [[5,0,0],[0,4,2],[0,2,1]]
A4 = sp.Matrix([[5, 0, 0], [0, 4, 2], [0, 2, 1]])
ok("Q4a eigenvalues 0,5,5", A4.eigenvals() == {0: 1, 5: 2}, str(A4.eigenvals()))
s5 = sp.sqrt(5)
Q = sp.Matrix([[0, 0, 1], [-1 / s5, 2 / s5, 0], [2 / s5, 1 / s5, 0]])
ok("Q4a Q orthogonal", sp.simplify(Q.T * Q) == sp.eye(3))
Dprinted = sp.diag(5, 5, 0)
Dgood = sp.diag(0, 5, 5)
ok("Q4a A = Q diag(0,5,5) Q^T (correct order)", sp.simplify(Q * Dgood * Q.T - A4) == sp.zeros(3, 3))
ok("Q4a printed D=diag(5,5,0) does NOT match the printed Q (slip)", sp.simplify(Q * Dprinted * Q.T - A4) != sp.zeros(3, 3))

# ---- Q4b: x = x^-1 for all x  =>  abelian ; x^3=y^5 => x=y. Brute force over Z2^3 and Z2^2 x Z2
def check_elem_abelian(k):
    els = list(itertools.product([0, 1], repeat=k))
    op = lambda p, q: tuple((s + t) % 2 for s, t in zip(p, q))
    return all(op(p, q) == op(q, p) for p in els for q in els) and all(
        (p == q) for p in els for q in els if op(op(p, p), p) == op(op(op(op(q, q), q), q), q))


ok("Q4b sanity on Z2^k, k=1..4", all(check_elem_abelian(k) for k in range(1, 5)))

# ---- Q5a: QR of [[-1,3],[1,5]]
A5 = sp.Matrix([[-1, 3], [1, 5]])
Q5, R5 = A5.QRdecomposition()
r2 = sp.sqrt(2)
Qp = sp.Matrix([[-r2 / 2, r2 / 2], [r2 / 2, r2 / 2]])
Rp = sp.Matrix([[r2, r2], [0, 4 * r2]])
ok("Q5a official Q R = A", sp.simplify(Qp * Rp - A5) == sp.zeros(2, 2))
ok("Q5a official Q orthogonal", sp.simplify(Qp.T * Qp) == sp.eye(2))
ok("Q5a sympy QR equals official (R diag > 0)", sp.simplify(Q5 - Qp) == sp.zeros(2, 2) and sp.simplify(R5 - Rp) == sp.zeros(2, 2))

# ---- Q5b: P = v v^T, |v|=1 -> P^2=P, P symmetric PSD, u-Pu perp v
v = sp.Matrix(sp.symbols("v1 v2 v3"))
vv = v / sp.sqrt(v.dot(v))
P = vv * vv.T
ok("Q5b P^2 = P", sp.simplify(P * P - P) == sp.zeros(3, 3))
u = sp.Matrix(sp.symbols("u1 u2 u3"))
ok("Q5b <u-Pu, v> = 0", sp.simplify(vv.dot(u - P * u)) == 0)

print("DONE", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
