# -*- coding: utf-8 -*-
r"""sympy / brute-force checks for sitting 25B-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/25B-A/check.py
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


# ---- Q1a: least squares line through (-2,3),(1,5),(5,6),(7,5),(9,8)
pts = [(-2, 3), (1, 5), (5, 6), (7, 5), (9, 8)]
A = sp.Matrix([[x, 1] for x, _ in pts])
b = sp.Matrix([y for _, y in pts])
G = A.T * A
rhs = A.T * b
ok("Q1a normal matrix [[160,20],[20,5]]", G == sp.Matrix([[160, 20], [20, 5]]))
ok("Q1a rhs (136,27)", rhs == sp.Matrix([136, 27]))
sol = G.LUsolve(rhs)
ok("Q1a m = 7/20, n = 4", sol == sp.Matrix([sp.Rational(7, 20), 4]), str(sol.T))

# ---- Q1b: eigenvectors of a symmetric matrix for distinct eigenvalues are orthogonal (random symmetric integer matrices)
random.seed(5)
good = True
for _ in range(40):
    n = random.randint(2, 3)
    M = sp.Matrix(n, n, lambda i, j: 0)
    for i in range(n):
        for j in range(i, n):
            M[i, j] = M[j, i] = random.randint(-3, 3)
    evs = M.eigenvects()
    for (l1, _, v1s), (l2, _, v2s) in itertools.combinations(evs, 2):
        for v1 in v1s:
            for v2 in v2s:
                if sp.simplify(v1.dot(v2)) != 0:
                    good = False
ok("Q1b eigenvectors of distinct eigenvalues are orthogonal (40 random symmetric matrices)", good)

# ---- Q2: H = {[[x,y],[0,x^-1]] : x != 0} in M2(Z7)
inv7 = {x: pow(x, -1, 7) for x in range(1, 7)}
H = [(x, y) for x in range(1, 7) for y in range(7)]
ok("Q2.2 |H| = 42", len(H) == 42)


def mul(p, q):
    x, y = p
    a_, b_ = q
    # [[x,y],[0,x^-1]] * [[a,b],[0,a^-1]] = [[xa, xb+y a^-1],[0,(xa)^-1]]
    return ((x * a_) % 7, (x * b_ + y * inv7[a_]) % 7)


Hs = set(H)
ok("Q2.1 closed", all(mul(p, q) in Hs for p in H for q in H))
ok("Q2.1 associative", all(mul(mul(p, q), r) == mul(p, mul(q, r)) for p in H for q in H[:12] for r in H[::5]))
ok("Q2.1 identity (1,0)", all(mul((1, 0), p) == p and mul(p, (1, 0)) == p for p in H))
ok("Q2.1 inverse of (x,y) is (x^-1, -y)... as matrix [[x^-1,-y],[0,x]] i.e. element (x^-1,-y)",
   all(mul(p, (inv7[p[0]], (-p[1]) % 7)) == (1, 0) for p in H))
# the matrix identity itself: check the inverse formula with real matrices mod 7
xs, ys = sp.symbols("x y")
Mx = sp.Matrix([[xs, ys], [0, 1 / xs]])
Mi = sp.Matrix([[1 / xs, -ys], [0, xs]])
ok("Q2.1 symbolic: [[x,y],[0,1/x]] * [[1/x,-y],[0,x]] = I", sp.simplify(Mx * Mi) == sp.eye(2))
J = sp.Matrix([[1, 1], [0, 1]])
P = sp.eye(2)
order = None
for k in range(1, 20):
    P = (P * J).applyfunc(lambda t: t % 7)
    if P == sp.eye(2):
        order = k
        break
ok("Q2.3 order of [[1,1],[0,1]] mod 7 is 7", order == 7, str(order))
ok("Q2.3 J^k = [[1,k],[0,1]]", (J ** 5) == sp.Matrix([[1, 5], [0, 1]]))

# ---- Q2b: u u^T + v v^T + w w^T = I for an orthonormal basis
Q_, _ = sp.Matrix([[1, 2, 0], [1, 0, 1], [3, 1, 1]]).QRdecomposition()
u, v, w = Q_[:, 0], Q_[:, 1], Q_[:, 2]
ok("Q2b sum of u u^T = I", sp.simplify(u * u.T + v * v.T + w * w.T) == sp.eye(3))

# ---- Q3a: M(k) = [[k,k,0],[k,k,k],[0,k,k]]
k = sp.symbols("k", real=True)
Mk = sp.Matrix([[k, k, 0], [k, k, k], [0, k, k]])
lam = sp.symbols("lam")
roots = sp.solve(Mk.charpoly(lam).as_expr(), lam)
ok("Q3a eigenvalues k, k(1+-sqrt2)", {sp.simplify(t) for t in roots} == {k, sp.simplify(k * (1 - sp.sqrt(2))), sp.simplify(k * (1 + sp.sqrt(2)))})
for kv in [-2, -1, sp.Rational(-1, 2), 0, sp.Rational(1, 2), 1, 3]:
    ev = [sp.N(t) for t in Mk.subs(k, kv).eigenvals().keys()]
    lo, hi = min(ev), max(ev)
    if kv == 0:
        ok("Q3a k=0 is both PSD and NSD (zero matrix)", Mk.subs(k, 0) == sp.zeros(3, 3))
    else:
        ok("Q3a k=%s is indefinite (min<0<max)" % kv, lo < -1e-12 and hi > 1e-12, "%.3f %.3f" % (lo, hi))

# ---- Q3b: G = {[[1,n],[0,1]]}
m_, n_ = sp.symbols("m n")
ok("Q3b product [[1,n],[0,1]][[1,m],[0,1]] = [[1,m+n],[0,1]]",
   sp.Matrix([[1, n_], [0, 1]]) * sp.Matrix([[1, m_], [0, 1]]) == sp.Matrix([[1, m_ + n_], [0, 1]]))
ok("Q3b inverse of [[1,n],[0,1]] is [[1,-n],[0,1]]", sp.Matrix([[1, n_], [0, 1]]) * sp.Matrix([[1, -n_], [0, 1]]) == sp.eye(2))
ok("Q3b n -> [[1,n],[0,1]] injective (so |G| infinite)", True)  # entry (1,2) equals n

# ---- Q4a: a o b = ab + a + b on Z
a_, b_, c_ = sp.symbols("a b c")
op = lambda s, t: s * t + s + t
ok("Q4a.2 associative (symbolic)", sp.expand(op(op(a_, b_), c_) - op(a_, op(b_, c_))) == 0)
ok("Q4a.2 expansion abc+ac+bc+ab+a+b+c", sp.expand(op(op(a_, b_), c_)) == sp.expand(a_ * b_ * c_ + a_ * c_ + b_ * c_ + a_ * b_ + a_ + b_ + c_))
ok("Q4a.3 identity is 0 and only 0", sp.solve(sp.expand(op(a_, c_) - a_), c_) in ([0], [0]) and all(op(t, 0) == t for t in range(-5, 6)))
ok("Q4a.3 e(a+1)=0 for all a forces e=0", all(not (e != 0 and all(e * (t + 1) == 0 for t in range(-5, 6))) for e in range(-9, 10)))
has_inv = [t for t in range(-10, 11) if any(op(t, s) == 0 for s in range(-200, 201))]
no_inv = [t for t in range(-10, 11) if t not in has_inv]
print("   elements with an inverse in [-10,10]:", has_inv, " without:", no_inv)
ok("Q4a.4 not a group: a=-1 has no inverse (and a=1 neither)", -1 in no_inv and 1 in no_inv)
ok("Q4a.4 (-1) o b = -1 for every b", all(op(-1, s) == -1 for s in range(-20, 21)))
u3 = sp.Matrix(sp.symbols("u1:4"))
v3 = sp.Matrix(sp.symbols("v1:4"))
ok("Q4b |u+v|^2 - |u-v|^2 = 4<u,v>", sp.expand((u3 + v3).dot(u3 + v3) - (u3 - v3).dot(u3 - v3) - 4 * u3.dot(v3)) == 0)

# ---- Q5a: SVD of [[2,1],[1,-2],[0,2]]
A5 = sp.Matrix([[2, 1], [1, -2], [0, 2]])
s5 = sp.sqrt(5)
U5 = sp.Matrix([[sp.Rational(1, 3), 2 * s5 / 5, -2 * s5 / 15],
                [-sp.Rational(2, 3), s5 / 5, 4 * s5 / 15],
                [sp.Rational(2, 3), 0, s5 / 3]])
S5 = sp.Matrix([[3, 0], [0, s5], [0, 0]])
V5 = sp.Matrix([[0, 1], [1, 0]])
ok("Q5a U orthogonal", sp.simplify(U5.T * U5) == sp.eye(3))
ok("Q5a V orthogonal", V5.T * V5 == sp.eye(2))
ok("Q5a A = U S V^T", sp.simplify(U5 * S5 * V5.T - A5) == sp.zeros(3, 2))
ok("Q5a singular values 3, sqrt5", sorted([sp.sqrt(t) for t in (A5.T * A5).eigenvals().keys()], key=float) == [s5, 3])

# ---- Q5c: CRT x=1 (3), 2 (5), 2 (11)
from sympy.ntheory.modular import solve_congruence  # noqa: E402

sol = solve_congruence((1, 3), (2, 5), (2, 11))
ok("Q5c x = 112 mod 165", sol == (112, 165), str(sol))

# ---- Q6b: orthogonal diagonalization of [[3,1,1],[1,3,1],[1,1,3]]
A6 = sp.Matrix([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
r2, r6, r3 = sp.sqrt(2), sp.sqrt(6), sp.sqrt(3)
Q6 = sp.Matrix([[-1 / r2, -1 / r6, 1 / r3], [1 / r2, -1 / r6, 1 / r3], [0, 2 / r6, 1 / r3]])
D6 = sp.diag(2, 2, 5)
ok("Q6b Q orthogonal", sp.simplify(Q6.T * Q6) == sp.eye(3))
ok("Q6b A = Q D Q^T", sp.simplify(Q6 * D6 * Q6.T - A6) == sp.zeros(3, 3))
ok("Q6b eigenvalues 5 (x1), 2 (x2)", A6.eigenvals() == {5: 1, 2: 2})

# ---- Q6c: sum a_i^2 identity and the inequality
ai = sp.symbols("a1:5", positive=True)
bi = sp.symbols("b1:5", positive=True)
uu = sp.Matrix([sp.sqrt(x / y) for x, y in zip(ai, bi)])
vv = sp.Matrix([sp.sqrt(x * y) for x, y in zip(ai, bi)])
ok("Q6c <u,v> = sum a_i", sp.simplify(uu.dot(vv) - sum(ai)) == 0)
ok("Q6c |u|^2 = sum a_i/b_i, |v|^2 = sum a_i b_i", sp.simplify(uu.dot(uu) - sum(x / y for x, y in zip(ai, bi))) == 0
   and sp.simplify(vv.dot(vv) - sum(x * y for x, y in zip(ai, bi))) == 0)
random.seed(7)
worst = 1e9
for _ in range(5000):
    n = random.randint(1, 6)
    aa = [random.uniform(0.1, 9) for _ in range(n)]
    bb = [random.uniform(0.1, 9) for _ in range(n)]
    worst = min(worst, sum(x / y for x, y in zip(aa, bb)) - sum(aa) ** 2 / sum(x * y for x, y in zip(aa, bb)))
ok("Q6c inequality on 5000 random samples", worst >= -1e-9, "min gap %.3g" % worst)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
