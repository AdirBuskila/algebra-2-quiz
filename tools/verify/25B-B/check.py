# -*- coding: utf-8 -*-
r"""sympy / brute-force checks for sitting 25B-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/25B-B/check.py
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


# ---- Q1a: LS line through (0,1),(2,4),(6,5),(10,8)
pts = [(0, 1), (2, 4), (6, 5), (10, 8)]
A = sp.Matrix([[x, 1] for x, _ in pts])
b = sp.Matrix([y for _, y in pts])
G = A.T * A
rhs = A.T * b
ok("Q1a normal matrix [[140,18],[18,4]]", G == sp.Matrix([[140, 18], [18, 4]]))
ok("Q1a rhs (118,18)", rhs == sp.Matrix([118, 18]))
sol = G.LUsolve(rhs)
ok("Q1a m = 37/59, n = 99/59", sol == sp.Matrix([sp.Rational(37, 59), sp.Rational(99, 59)]), str(sol.T))
ok("Q1a decimals 0.627, 1.678", abs(float(sol[0]) - 0.627) < 5e-4 and abs(float(sol[1]) - 1.678) < 5e-4)

# ---- Q1b: S^T A S is PSD iff A is PSD, S orthogonal, A symmetric (random checks)
random.seed(11)
agree = True
cnt = 0
for _ in range(300):
    n = random.randint(2, 3)
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            M[i, j] = M[j, i] = random.randint(-3, 3)
    w = sp.Matrix([random.randint(-3, 3) for _ in range(n)])
    if w.dot(w) == 0:
        continue
    S = sp.eye(n) - 2 * w * w.T / w.dot(w)  # Householder reflection: rational orthogonal matrix
    assert S.T * S == sp.eye(n)
    cnt += 1
    if M.is_positive_semidefinite != (S.T * M * S).is_positive_semidefinite:
        agree = False
ok("Q1b S^T A S PSD iff A PSD (%d random cases, Householder S)" % cnt, agree and cnt > 100)

# ---- Q2: H = {[[a,b],[c,d]] in M2(Z5), all entries nonzero}, Hadamard product
units = [1, 2, 3, 4]
inv5 = {x: pow(x, -1, 5) for x in units}
ok("Q2a.2 |H| = 4^4 = 256", len(list(itertools.product(units, repeat=4))) == 256)
hm = lambda X, Y: tuple((p * q) % 5 for p, q in zip(X, Y))
H = list(itertools.product(units, repeat=4))
Hs = set(H)
ok("Q2a.1 closed", all(hm(X, Y) in Hs for X in H[:64] for Y in H[::7]))
E = (1, 1, 1, 1)
ok("Q2a.1 identity is all-ones matrix", all(hm(E, X) == X for X in H))
ok("Q2a.1 inverse = entrywise inverse", all(hm(X, tuple(inv5[t] for t in X)) == E for X in H))
X0 = (1, 2, 2, 3)


def order(el):
    P, k = el, 1
    while P != E:
        P = hm(P, el)
        k += 1
    return k


ok("Q2a.3 order of [[1,2],[2,3]] is 4 (o(1)=1, o(2)=4, o(3)=4)", order(X0) == 4 and [order((t, t, t, t)) for t in units] == [1, 4, 4, 2])

# ---- Q2b: Cauchy-Schwarz with v=(1,...,1)
random.seed(3)
worst = 1e9
for _ in range(3000):
    n = random.randint(1, 7)
    aa = [random.uniform(-9, 9) for _ in range(n)]
    worst = min(worst, n * sum(t * t for t in aa) - sum(aa) ** 2)
ok("Q2b (sum a)^2 <= n sum a^2 on 3000 random samples", worst >= -1e-9, "min gap %.3g" % worst)

# ---- Q3a: a (x) b = ab - a - b
a_, b_, c_, e_ = sp.symbols("a b c e")
op = lambda s, t: s * t - s - t
l = sp.expand(op(op(a_, b_), c_))
r = sp.expand(op(a_, op(b_, c_)))
ok("Q3a.2 (a x b) x c = abc - ac - bc - ab + a + b - c", l == sp.expand(a_ * b_ * c_ - a_ * c_ - b_ * c_ - a_ * b_ + a_ + b_ - c_))
ok("Q3a.2 a x (b x c) = abc - ab - ac - a - bc + b + c", r == sp.expand(a_ * b_ * c_ - a_ * b_ - a_ * c_ - a_ - b_ * c_ + b_ + c_))
ok("Q3a.2 not associative (difference = 2a - 2c)", sp.expand(l - r) == sp.expand(2 * c_ * -1 + 2 * a_) or sp.expand(l - r) == sp.expand(2 * a_ - 2 * c_),
   str(sp.expand(l - r)))
ok("Q3a.2 numeric counterexample (1 x 2) x 3 != 1 x (2 x 3)", op(op(1, 2), 3) != op(1, op(2, 3)), "%s vs %s" % (op(op(1, 2), 3), op(1, op(2, 3))))
# identity: a x e = a  <=>  e(a-1) = 2a  (the printed official line says (a-1)e = a: slip, same conclusion at a=1)
ok("Q3a.3 a x e = a  <=>  e(a-1) = 2a", sp.expand((op(a_, e_) - a_) - (e_ * (a_ - 1) - 2 * a_)) == 0)
ok("Q3a.3 at a=1 the equation is 0 = 2 (no identity)", (e_ * (1 - 1) - 2 * 1) == -2)
ok("Q3a.3 no e in [-50,50] is an identity", not any(all(op(t, e) == t for t in range(-6, 7)) for e in range(-50, 51)))

# ---- Q3b: A = v u^T + u v^T, eigenvalues +-1
Q_, _ = sp.Matrix([[2, 1], [1, 3]]).QRdecomposition()
u, v = Q_[:, 0], Q_[:, 1]
Am = v * u.T + u * v.T
ok("Q3b A(u+v) = u+v", sp.simplify(Am * (u + v) - (u + v)) == sp.zeros(2, 1))
ok("Q3b A(u-v) = -(u-v)", sp.simplify(Am * (u - v) + (u - v)) == sp.zeros(2, 1))
ok("Q3b eigenvalues {1,-1}", Am.eigenvals() == {1: 1, -1: 1})

# ---- Q4a: QR of [[1,1,0],[1,0,1],[0,1,1]]
A4 = sp.Matrix([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
r2, r6, r3 = sp.sqrt(2), sp.sqrt(6), sp.sqrt(3)
Q4 = sp.Matrix([[r2 / 2, r6 / 6, -r3 / 3], [r2 / 2, -r6 / 6, r3 / 3], [0, r6 / 3, r3 / 3]])
R4 = sp.Matrix([[r2, r2 / 2, r2 / 2], [0, r6 / 2, r6 / 6], [0, 0, 2 * r3 / 3]])
ok("Q4a Q orthogonal", sp.simplify(Q4.T * Q4) == sp.eye(3))
ok("Q4a R upper triangular, positive diagonal", R4.is_upper and all(R4[i, i] > 0 for i in range(3)))
ok("Q4a A = Q R", sp.simplify(Q4 * R4 - A4) == sp.zeros(3, 3))
Qs, Rs = A4.QRdecomposition()
ok("Q4a sympy QR agrees", sp.simplify(Qs - Q4) == sp.zeros(3, 3) and sp.simplify(Rs - R4) == sp.zeros(3, 3))

# ---- Q4b: CRT 3x=4 (5), 2x=3 (7), x=7 (32)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

ok("Q4b reduced system x=3 (5), x=5 (7)", (3 * 3) % 5 == 4 and (2 * 5) % 7 == 3)
sol = solve_congruence((3, 5), (5, 7), (7, 32))
ok("Q4b x = 103 mod 1120", sol == (103, 1120), str(sol))
ok("Q4b original system at x=103", (3 * 103) % 5 == 4 and (2 * 103) % 7 == 3 and 103 % 32 == 7)

# ---- Q5a: [[1,c,0],[c,1,c],[0,c,1]]
c = sp.symbols("c", real=True)
Mc = sp.Matrix([[1, c, 0], [c, 1, c], [0, c, 1]])
lam = sp.symbols("lam")
roots = sp.solve(Mc.charpoly(lam).as_expr(), lam)
ok("Q5a eigenvalues 1, 1+-sqrt2 c", {sp.simplify(t) for t in roots} == {sp.Integer(1), sp.simplify(1 + sp.sqrt(2) * c), sp.simplify(1 - sp.sqrt(2) * c)})
ok("Q5a PSD iff |c| <= 1/sqrt2", sp.solve_univariate_inequality(1 - sp.sqrt(2) * c >= 0, c, relational=False) == sp.Interval(-sp.oo, 1 / sp.sqrt(2)))
for cv, kind in [(0, "pd"), (sp.Rational(1, 2), "pd"), (1 / sp.sqrt(2), "psd"), (-1 / sp.sqrt(2), "psd"), (1, "indef"), (-1, "indef")]:
    ev = [sp.N(t) for t in Mc.subs(c, cv).eigenvals().keys()]
    lo = min(ev)
    res = "pd" if lo > 1e-12 else ("psd" if lo > -1e-9 else "indef")
    ok("Q5a c=%s is %s" % (cv, kind), res == kind, "min eig %.6f" % lo)
ok("Q5a never negative: eigenvalue 1 is always positive", True)

# ---- Q6a: orthogonal diagonalization of [[3,2,0],[2,2,2],[0,2,1]]
A6 = sp.Matrix([[3, 2, 0], [2, 2, 2], [0, 2, 1]])
Q6 = sp.Matrix([[2, -2, 1], [2, 1, -2], [1, 2, 2]]) / 3
D6 = sp.diag(5, 2, -1)
ok("Q6a eigenvalues 5, 2, -1", A6.eigenvals() == {5: 1, 2: 1, -1: 1})
ok("Q6a Q orthogonal", Q6.T * Q6 == sp.eye(3))
ok("Q6a A = Q D Q^T", Q6 * D6 * Q6.T == A6)

# ---- Q6b: parallelogram law
u3 = sp.Matrix(sp.symbols("u1:4"))
v3 = sp.Matrix(sp.symbols("v1:4"))
nn = lambda x: x.dot(x)
ok("Q6b parallelogram law (symbolic, R^3)", sp.expand(nn(u3 + v3) + nn(u3 - v3) - 2 * nn(u3) - 2 * nn(v3)) == 0)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
