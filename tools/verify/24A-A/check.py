# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 24A-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/24A-A/check.py
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


# ---- Q1a: ||u+v|| = ||u|| + ||v|| iff v = t u, t > 0 (numeric spot-check, both directions)
random.seed(1)
good = True
for _ in range(3000):
    u = sp.Matrix([random.randint(-4, 4) for _ in range(3)])
    v = sp.Matrix([random.randint(-4, 4) for _ in range(3)])
    if u.norm() == 0 or v.norm() == 0:
        continue
    eq = sp.simplify((u + v).norm() - u.norm() - v.norm()) == 0
    pos_multiple = (u.cross(v) == sp.zeros(3, 1)) and u.dot(v) > 0
    if eq != pos_multiple:
        good = False
ok("Q1a equality iff v = t u with t > 0 (3000 integer pairs)", good)

# ---- Q1b: projection in M2 with <A,B> = tr(B^T A)
def ip(A, B):
    return (B.T * A).trace()


W1 = sp.Matrix([[1, 0], [0, 1]])
W2 = sp.Matrix([[0, 1], [0, 1]])
v = sp.Matrix([[1, 1], [1, 0]])
u1 = W1
u2 = W2 - ip(W2, u1) / ip(u1, u1) * u1
ok("Q1b u2 = [[-1/2,1],[0,1/2]]", u2 == sp.Matrix([[-sp.Rational(1, 2), 1], [0, sp.Rational(1, 2)]]))
ok("Q1b u1 perp u2, |u1|^2=2, |u2'|^2 = 6 for [[-1,2],[0,1]]", ip(u1, u2) == 0 and ip(u1, u1) == 2
   and ip(sp.Matrix([[-1, 2], [0, 1]]), sp.Matrix([[-1, 2], [0, 1]])) == 6)
u2s = sp.Matrix([[-1, 2], [0, 1]])
proj = ip(v, u1) / ip(u1, u1) * u1 + ip(v, u2s) / ip(u2s, u2s) * u2s
ok("Q1b proj = [[1/3,1/3],[0,2/3]]", proj == sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 3)], [0, sp.Rational(2, 3)]]), str(proj))
# least squares check: v - proj must be orthogonal to both spanning matrices
ok("Q1b v - proj perp W1, W2", ip(v - proj, W1) == 0 and ip(v - proj, W2) == 0)

# ---- Q2a: a (.) b = ab/(a+b) on positive reals
a, b, c = sp.symbols("a b c", positive=True)
op = lambda x, y: x * y / (x + y)
ok("Q2a.1 associative: both sides abc/(ab+ac+bc)",
   sp.simplify(op(op(a, b), c) - a * b * c / (a * b + a * c + b * c)) == 0
   and sp.simplify(op(a, op(b, c)) - a * b * c / (a * b + a * c + b * c)) == 0)
e = sp.symbols("e", positive=True)
ok("Q2a.2 equation reduces to -a^2 = 0", sp.expand(sp.numer(sp.together(a * e / (a + e) - a))) == -a**2)
x = sp.symbols("x", positive=True)
ok("Q2a.3 x (.) x = x/2, never equal x for x > 0", sp.simplify(op(x, x) - x / 2) == 0 and sp.solve(sp.Eq(x / 2, x), x) == [])
# x^n = x/n (induction) checked for n up to 12
cur = x
okp = True
for n in range(2, 13):
    cur = op(cur, x)
    okp = okp and sp.simplify(cur - x / n) == 0
ok("Q2a.4 x^n = x/n for n=2..12", okp)
ok("Q2a.4 n^n = 1 for n=1..12", all(sp.Rational(n, n) == 1 for n in range(1, 13)))

# ---- Q2b: A PD => cI + A + A^2 PD (c>0): random PD matrices
random.seed(2)
alld = True
for _ in range(300):
    n = random.randint(1, 4)
    B = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
    A = B.T * B + sp.eye(n)
    cc = sp.Rational(random.randint(1, 9), 3)
    M = cc * sp.eye(n) + A + A * A
    alld = alld and M == M.T and all(M[:k, :k].det() > 0 for k in range(1, n + 1))
ok("Q2b cI + A + A^2 symmetric with positive leading minors (Sylvester) on 300 random PD A", alld)

# ---- Q3a: [[1,0,a^2],[0,3a-1,0],[a^2,b,1]] symmetric only if b = 0
aa = sp.symbols("aa", real=True)
M3 = sp.Matrix([[1, 0, aa**2], [0, 3 * aa - 1, 0], [aa**2, 0, 1]])
lam = sp.symbols("lam")
roots = sp.solve(M3.charpoly(lam).as_expr(), lam)
ok("Q3a eigenvalues 3a-1, 1+a^2, 1-a^2", {sp.simplify(r) for r in roots} == {3 * aa - 1, 1 + aa**2, 1 - aa**2})
for av, kind in [(sp.Rational(1, 2), "pd"), (1, "psd"), (sp.Rational(1, 3), "psd"), (sp.Rational(1, 4), "indef"),
                 (sp.Rational(3, 2), "indef"), (-1, "indef"), (2, "indef")]:
    evs = [sp.N(t) for t in M3.subs(aa, av).eigenvals(multiple=True)]
    lo = min(evs)
    res = "pd" if lo > 1e-12 else ("psd" if lo > -1e-12 else "indef")
    ok("Q3a a=%s is %s" % (av, kind), res == kind, "min eig %.5f" % lo)
ok("Q3a PSD iff 1/3<=a<=1: 3a-1>=0 and 1-a^2>=0",
   sp.solve_univariate_inequality(3 * aa - 1 >= 0, aa, relational=False).intersect(sp.Interval(-1, 1)) == sp.Interval(sp.Rational(1, 3), 1))
Mb = sp.Matrix([[1, 0, 4], [0, 2, 0], [4, 1, 1]])
ok("Q3a with b != 0 the matrix is not symmetric", Mb != Mb.T)

# ---- Q3b: least squares (1,3),(3,5),(-2,5),(2,2)
pts = [(1, 3), (3, 5), (-2, 5), (2, 2)]
A = sp.Matrix([[p[0], 1] for p in pts])
bb = sp.Matrix([p[1] for p in pts])
ok("Q3b A^T A = [[18,4],[4,4]], A^T b = [[12],[15]]", A.T * A == sp.Matrix([[18, 4], [4, 4]]) and A.T * bb == sp.Matrix([12, 15]))
sol = (A.T * A).solve(A.T * bb)
ok("Q3b m = -3/14, n = 111/28", sol == sp.Matrix([-sp.Rational(3, 14), sp.Rational(111, 28)]), str(list(sol)))

# ---- Q4a: H in GL2(Z7) upper triangular
count = 0
for aa_, bb_, cc_ in itertools.product(range(7), repeat=3):
    if (aa_ * cc_) % 7 != 0:
        count += 1
ok("Q4a.1 |H| = 252", count == 252, str(count))


def order_mod(M, p=7):
    cur = sp.eye(M.shape[0])
    for k in range(1, 100):
        cur = (cur * M).applyfunc(lambda t: t % p)
        if cur == sp.eye(M.shape[0]):
            return k
    return None


ok("Q4a.2 order of diag(4,3) mod 7 is 6", order_mod(sp.Matrix([[4, 0], [0, 3]])) == 6)
ok("Q4a.2 o(4)=3 and o(3)=6 in Z7*", pow(4, 3, 7) == 1 and pow(4, 1, 7) != 1 and pow(3, 6, 7) == 1 and pow(3, 3, 7) != 1 and pow(3, 2, 7) != 1)
Mx = sp.Matrix([[1, 2], [0, 3]])
inv = Mx.inv_mod(7)
ok("Q4a.3 inverse of [[1,2],[0,3]] mod 7 is [[1,4],[0,5]]", inv == sp.Matrix([[1, 4], [0, 5]]), str(inv))

# ---- Q4b: f(x) = (x+k)^2/(x^2+1) <= k^2+1  (equivalent to Cauchy-Schwarz)
xx, kk = sp.symbols("xx kk", real=True)
ok("Q4b (k^2+1)(x^2+1) - (x+k)^2 = (kx-1)^2",
   sp.expand((kk**2 + 1) * (xx**2 + 1) - (xx + kk) ** 2 - (kk * xx - 1) ** 2) == 0)

# ---- Q5a: SVD of A = [[2,0],[0,2],[1,sqrt3]]
r2, r3, r6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
A5 = sp.Matrix([[2, 0], [0, 2], [1, r3]])
U = sp.Matrix([[r2 / 4, -r3 / 2, -r2 / 4], [r6 / 4, sp.Rational(1, 2), -r6 / 4], [r2 / 2, 0, r2 / 2]])
S = sp.Matrix([[2 * r2, 0], [0, 2], [0, 0]])
Vt = sp.Matrix([[sp.Rational(1, 2), r3 / 2], [-r3 / 2, sp.Rational(1, 2)]])
ok("Q5a A^T A eigenvalues {8,4}", A5.T * A5 == sp.Matrix([[5, r3], [r3, 7]]) and A5.T.multiply(A5).eigenvals() == {8: 1, 4: 1})
ok("Q5a U orthogonal", sp.simplify(U.T * U) == sp.eye(3))
ok("Q5a V orthogonal", sp.simplify(Vt * Vt.T) == sp.eye(2))
ok("Q5a A = U S V^T", sp.simplify(U * S * Vt - A5) == sp.zeros(3, 2))
ok("Q5a sympy singular values 2sqrt2, 2", sorted([sp.simplify(s) for s in A5.singular_values()], key=float) == [2, 2 * r2])

# ---- Q5b: CRT 2x=1 (5), 3x=5 (11), x=2 (3)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

ok("Q5b reduced system x=3 (5), 9 (11), 2 (3)", (2 * 3) % 5 == 1 and (3 * 9) % 11 == 5)
res = solve_congruence((3, 5), (9, 11), (2, 3))
ok("Q5b x = 53 mod 165", res == (53, 165), str(res))
ok("Q5b M=33,15,55; x_i=2,3,1; sum=713", (33 * 2) % 5 == 1 and (15 * 3) % 11 == 1 and (55 * 1) % 3 == 1
   and 3 * 33 * 2 + 9 * 15 * 3 + 2 * 55 * 1 == 713 and 713 % 165 == 53)
ok("Q5b original system at x=53", (2 * 53) % 5 == 1 and (3 * 53) % 11 == 5 and 53 % 3 == 2)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
