# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided STEPS of sitting 23B-A (algebra-2).
Run after the generator: PYTHONUTF8=1 py -I tools/verify/23B-A/steps_check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import json
import pathlib
import sys

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "23B-A.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
Qs = {(q["num"], q.get("part")): q for q in data["questions"]}
bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def same(key, expected):
    got = [(s["answer"], s.get("tol", 0)) for s in Qs[key]["steps"] if s["type"] == "numeric"]
    good = len(got) == len(expected) and all(abs(a - float(e)) <= max(t, 1e-9) for (a, t), e in zip(got, expected))
    ok(f"Q{key[0]}{ascii(key[1])} numeric steps == sympy values", good, f"stored {[g[0] for g in got]} sympy {[float(e) for e in expected]}")


# ---- Q1a least squares through (6,8),(2,2),(0,0),(-1,0),(-2,4)
pts = [(6, 8), (2, 2), (0, 0), (-1, 0), (-2, 4)]
X = sp.Matrix([[p[0], 1] for p in pts])
y = sp.Matrix([p[1] for p in pts])
sol = (X.T * X).solve(X.T * y)
same((1, "א"), [(X.T * X)[0, 0], (X.T * y)[0], sol[0], sol[1]])
ok("Q1a m=3/4, n=41/20", sol[0] == sp.Rational(3, 4) and sol[1] == sp.Rational(41, 20))

# ---- Q1b
k, n = sp.symbols("k n", positive=True, integer=True)
ok("Q1b sum 2k = n(n+1)", sp.simplify(sp.summation(2 * k, (k, 1, n)) - n * (n + 1)) == 0)
ok("Q1b chosen vectors: sqrt(2k)*sqrt(ln k) = sqrt(2k ln k)", all(abs(sp.N(sp.sqrt(2 * j) * sp.sqrt(sp.log(j)) - sp.sqrt(2 * j * sp.log(j)))) < 1e-12 for j in range(1, 8)))
same((1, "ב"), [sum(2 * j for j in range(1, 5)), sp.log(24)])
ok("Q1b inequality holds n=1..40", all(sum(sp.N(sp.sqrt(2 * j * sp.log(j))) for j in range(1, m + 1)) <= sp.N(sp.sqrt(m * (m + 1) * sp.log(sp.factorial(m)))) + 1e-9 for m in range(1, 41)))
# wrong options: (sqrt k, sqrt ln k) -> inner sum sqrt(k ln k) != target; (2k, ln k) -> 2k ln k; (target, 1) -> norm^2 sum 2k ln k
ok("Q1b wrong options produce different inner products/norms",
   abs(sum(sp.N(sp.sqrt(j * sp.log(j))) for j in range(1, 5)) - sum(sp.N(sp.sqrt(2 * j * sp.log(j))) for j in range(1, 5))) > 0.1
   and sum(2 * j * sp.log(j) for j in range(1, 5)) != sum(2 * j for j in range(1, 5)) * sp.log(24))

# ---- Q2: G = {[[a,b],[0,c]]: ac != 0 mod 3}
G = [(a_, b_, c_) for a_ in range(3) for b_ in range(3) for c_ in range(3) if (a_ * c_) % 3]
ok("Q2a |G| = 12", len(G) == 12)
same((2, "א"), [2, 3, 12])
A = sp.Matrix([[2, 1], [0, 2]])
pw = {j: (A ** j).applyfunc(lambda e: e % 3) for j in range(1, 7)}
ordA = next(j for j in range(1, 20) if pw[j] == sp.eye(2) or (A ** j).applyfunc(lambda e: e % 3) == sp.eye(2))
ok("Q2b A^2=[[1,1],[0,1]], A^3=2I, A^4=[[1,2],[0,1]], order 6",
   pw[2] == sp.Matrix([[1, 1], [0, 1]]) and pw[3] == 2 * sp.eye(2) and pw[4] == sp.Matrix([[1, 2], [0, 1]]) and ordA == 6)
same((2, "ב"), [pw[2][0, 1], pw[3][0, 0], pw[4][0, 1], ordA])
Aq = sp.Matrix([[2, 1], [1, 2]])
vv = sp.Matrix([1, -1])
same((2, "ג"), [(vv.T * (sp.eye(2) + Aq) * vv)[0]])
ok("Q2c example: |v|^2 + <Av,v> = 2 + 2", vv.dot(vv) == 2 and (vv.T * Aq * vv)[0] == 2 and Aq.is_positive_definite)

# ---- Q3a
a = sp.symbols("a", real=True)
M = sp.Matrix([[1, 0, 2 * a], [0, 4 - a ** 2, 0], [2 * a, 0, 1]])
lam_ = sp.symbols("lam")
ok("Q3a eigenvalues 4-a^2, 1+2a, 1-2a", all(sp.expand(M.charpoly(lam_).as_expr().subs(lam_, e)) == 0 for e in (4 - a ** 2, 1 + 2 * a, 1 - 2 * a)))
grid = [sp.Rational(j, 8) for j in range(-32, 33)]


def eg(g):
    return list(M.subs(a, g).eigenvals())


ok("Q3a strict pos iff |a|<1/2", all((min(eg(g)) > 0) == (abs(g) < sp.Rational(1, 2)) for g in grid))
ok("Q3a pos semidef iff |a|<=1/2", all((min(eg(g)) >= 0) == (abs(g) <= sp.Rational(1, 2)) for g in grid))
ok("Q3a never negative semidefinite", all(not (max(eg(g)) <= 0) for g in grid))
ok("Q3a wrong options fail: a=1 has eig -1, a=1/2 has eig 0", min(eg(1)) < 0 and min(eg(sp.Rational(1, 2))) == 0 and min(eg(1)) < 0)
same((3, "א"), [(4 - a ** 2).subs(a, 1), (1 + 2 * a + 1 - 2 * a)])

# ---- Q3b: random check of the identity |au+bv|^2-|bu+av|^2 = (a^2-b^2)(|u|^2-|v|^2)
uu, vv2, uv, al, be = sp.symbols("uu vv uv al be")
lhs = (al ** 2 * uu + 2 * al * be * uv + be ** 2 * vv2) - (be ** 2 * uu + 2 * al * be * uv + al ** 2 * vv2)
ok("Q3b identity", sp.expand(lhs - (al ** 2 - be ** 2) * (uu - vv2)) == 0)
same((3, "ב"), [lhs.subs({al: 2, be: 1, uu: 5, vv2: 3, uv: 1})])
ok("Q3b alpha=beta or alpha=-beta or 0,0 give no information (identity vanishes)", all(lhs.subs({al: p, be: q}) == 0 for p, q in [(1, 1), (0, 0), (1, -1)]) and lhs.subs({al: 1, be: 0}) == uu - vv2)

# ---- Q4a SVD of [[1,0,2],[2,0,1]]
Am = sp.Matrix([[1, 0, 2], [2, 0, 1]])
AtA = Am.T * Am
ok("Q4a A^T A = [[5,0,4],[0,0,0],[4,0,5]], eigenvalues 9,1,0", AtA == sp.Matrix([[5, 0, 4], [0, 0, 0], [4, 0, 5]]) and set(AtA.eigenvals()) == {9, 1, 0})
v1 = sp.Matrix([1, 0, 1]) / sp.sqrt(2)
u1 = Am * v1 / 3
ok("Q4a u1 = (1,1)/sqrt2", u1 == sp.Matrix([1, 1]) / sp.sqrt(2))
same((4, "א"), [AtA[0, 2], 9, 3, u1[0]])

# ---- Q4b CRT
from sympy.ntheory.modular import solve_congruence
ok("Q4b x = 78 mod 280", solve_congruence((3, 5), (1, 7), (6, 8)) == (78, 280))
ok("Q4b x2=3 (40*3=1 mod 7), x3=3 (35*3=1 mod 8)", (40 * 3) % 7 == 1 and (35 * 3) % 8 == 1 and 280 // 7 == 40 and 3 * 56 + 40 * 3 + 6 * 35 * 3 == 918 and 918 % 280 == 78)
same((4, "ב"), [40, 3, 3, 78])

# ---- Q5a projection onto W = Sp{V1, V2} in M2(R), <A,B> = tr(B^T A) = sum of products
def ip(P, Q_):
    return (Q_.T * P).trace()


a_, b_ = sp.symbols("a b")
V1, V2 = sp.Matrix([[-1, 1], [1, 0]]), sp.Matrix([[1, 0], [2, 1]])
U1 = V1
U2 = V2 - ip(V2, U1) / ip(U1, U1) * U1
ok("Q5a U2 = (1/3)[[4,-1],[5,3]]", U2 == sp.Rational(1, 3) * sp.Matrix([[4, -1], [5, 3]]))
W2 = sp.Matrix([[4, -1], [5, 3]])
Mx = sp.Matrix([[0, a_], [b_, 0]])
ok("Q5a <M,U1> = a+b, <M,W2> = 5b-a (NOT 5b-3a), norms 3 and 51", sp.expand(ip(Mx, U1) - (a_ + b_)) == 0 and sp.expand(ip(Mx, W2) - (5 * b_ - a_)) == 0 and ip(U1, U1) == 3 and ip(W2, W2) == 51)
pr = ip(Mx, U1) / ip(U1, U1) * U1 + ip(Mx, W2) / ip(W2, W2) * W2
ok("Q5a projection = 1/17 [[-7a+b, 6a+4b],[4a+14b, -a+5b]]", sp.simplify(pr - sp.Rational(1, 17) * sp.Matrix([[-7 * a_ + b_, 6 * a_ + 4 * b_], [4 * a_ + 14 * b_, -a_ + 5 * b_]])) == sp.zeros(2, 2))
ok("Q5a residual orthogonal to V1, V2", all(sp.simplify(ip(Mx - pr, V)) == 0 for V in (V1, V2)))
pr12 = pr.subs({a_: 1, b_: 2})
same((5, "א"), [ip(V2, U1), ip(W2, W2), ip(Mx.subs({a_: 1, b_: 2}), W2), pr12[0, 0]])
ok("Q5a printed 5b-3a would give 7 at a=1,b=2 (differs from 9)", 5 * 2 - 3 * 1 == 7 != 9)

# ---- Q5b: groups with x*x=e: brute force over Z2^3 and S3-free check (exponent 2 groups are abelian)
G2 = list(itertools.product([0, 1], repeat=3))


def op(p, q):
    return tuple((s + t) % 2 for s, t in zip(p, q))


ok("Q5b c=(a*b)*a equals b in Z2^3 (all a,b)", all(op(op(p, q), p) == q for p in G2 for q in G2))
# proof steps: ((a b) a) b = (a b)(a b) = e
ok("Q5b c*b = e in Z2^3", all(op(op(op(p, q), p), q) == (0, 0, 0) for p in G2 for q in G2))

print("FAILED: " + ", ".join(bad) if bad else "ALL OK")
sys.exit(1 if bad else 0)
