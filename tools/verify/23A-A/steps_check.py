# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided STEPS of sitting 23A-A (algebra-2).
Run after the generator: PYTHONUTF8=1 py -I tools/verify/23A-A/steps_check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import json
import pathlib
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "23A-A.json"
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


# ---- Q1a least squares
X = sp.Matrix([[1, 1], [2, 1], [3, 1], [4, 1]])
y = sp.Matrix([20, 24, 31, 32])
sol = (X.T * X).solve(X.T * y)
same((1, "א"), [(X.T * X)[0, 0], (X.T * y)[0], sol[0], sol[0] * 5 + sol[1]])

# ---- Q1b projection in M2(R), <A,B> = tr(B^T A)


def ip(A, B):
    return (B.T * A).trace()


w1, w2 = sp.Matrix([[1, 1], [0, 0]]), sp.Matrix([[1, 3], [1, 1]])
v = sp.Matrix([[1, 2], [3, 0]])
u1 = w1
u2 = w2 - ip(w2, u1) / ip(u1, u1) * u1
c1, c2 = ip(v, u1) / ip(u1, u1), ip(v, u2) / ip(u2, u2)
proj = c1 * u1 + c2 * u2
ok("Q1b u2 = [[-1,1],[1,1]] and proj = 1/2 [[1,5],[2,2]]", u2 == sp.Matrix([[-1, 1], [1, 1]]) and proj == sp.Rational(1, 2) * sp.Matrix([[1, 5], [2, 2]]))
same((1, "ב"), [ip(w1, w2), c1, c2, proj[0, 1]])

# ---- Q2a
t = sp.symbols("t")
same((2, "א"), [sp.integrate(sp.exp(t), (t, 0, 1)), sp.integrate(t * sp.exp(t), (t, 0, 1))])

# ---- Q2b orders in Z5*
def zord(g, n):
    return next(k for k in range(1, n) if pow(g, k, n) == 1)


ok("Q2b orders 2 and 4, lcm 4", zord(4, 5) == 2 and zord(3, 5) == 4)
D = sp.Matrix([[4, 0], [0, 3]])
Hord = next(k for k in range(1, 20) if (D ** k).applyfunc(lambda e: e % 5) == sp.eye(2))
same((2, "ב"), [zord(4, 5), zord(3, 5), Hord])

# ---- Q3a eigenvalues of [[a,0,1],[0,2a,0],[1,0,a]]
a = sp.symbols("a", real=True)
M = sp.Matrix([[a, 0, 1], [0, 2 * a, 0], [1, 0, a]])
ok("Q3a eigenvalues 2a, a-1, a+1", set(M.eigenvals()) == {2 * a, a - 1, a + 1})
grid = [sp.Rational(k, 8) for k in range(-40, 41)]


def eigs(g):
    return [e for e in M.subs(a, g).eigenvals()]


ok("Q3a strictly positive iff a>1", all((min(eigs(g)) > 0) == (g > 1) for g in grid))
ok("Q3a positive semidefinite iff a>=1", all((min(eigs(g)) >= 0) == (g >= 1) for g in grid))
ok("Q3a strictly negative iff a<-1", all((max(eigs(g)) < 0) == (g < -1) for g in grid))
ok("Q3a negative semidefinite iff a<=-1", all((max(eigs(g)) <= 0) == (g <= -1) for g in grid))
ok("Q3a wrong options fail (a=1/2 not pd; a=1 not strict; a=-1/2 not nd; a=-1 not strict)",
   min(eigs(sp.Rational(1, 2))) < 0 and min(eigs(1)) == 0 and max(eigs(-sp.Rational(1, 2))) > 0 and max(eigs(-1)) == 0 and min(eigs(0.5)) < 0)
pos0 = sum(1 for e in eigs(0) if e > 0)
same((3, "א"), [(a - 1).subs(a, 3), pos0])

# ---- Q3b orthonormal u,v,w -> coordinates
al, be = sp.Matrix([1, 2, 1]), sp.Matrix([1, 0, -1])
same((3, "ב"), [al.dot(be)])
same((3, "ג"), [al.dot(al), be.dot(be)])
ok("Q3c wrong norm formulas give 16, 4, 4 (not 6)", sum(al) ** 2 == 16 and sum(al) == 4 and sum(abs(e) for e in al) == 4)

# ---- Q4: (a,b)*(x,y) = (ay+bx, by)


def star(p, q):
    return (p[0] * q[1] + p[1] * q[0], p[1] * q[1])


import itertools

R = range(-4, 5)
ok("Q4a commutative", all(star(p, q) == star(q, p) for p in itertools.product(R, R) for q in itertools.product(R, R)))
ok("Q4a (1,2)*(3,4) = (10,8) = (3,4)*(1,2)", star((1, 2), (3, 4)) == (10, 8) == star((3, 4), (1, 2)))
same((4, "א"), [star((1, 2), (3, 4))[0]])
ok("Q4b e=(0,1) is identity", all(star(p, (0, 1)) == p for p in itertools.product(R, R)))
ok("Q4b unique identity among small integers", [e for e in itertools.product(R, R) if all(star(p, e) == p for p in itertools.product(R, R))] == [(0, 1)])
same((4, "ב"), [1, 0, star((5, 2), (0, 1))[0]])
ok("Q4c inverse of (1,2): (-1/4, 1/2)", star((1, 2), (sp.Rational(-1, 4), sp.Rational(1, 2))) == (0, 1))
ok("Q4c (5,0) has no inverse", all(star((5, 0), (x_, y_))[1] == 0 for x_ in R for y_ in R))
ok("Q4c (inverse formula x=-a/b^2, y=1/b) for generic a,b",
   sp.simplify(star((sp.Symbol("p"), sp.Symbol("q", nonzero=True)), (-sp.Symbol("p") / sp.Symbol("q", nonzero=True) ** 2, 1 / sp.Symbol("q", nonzero=True)))[0]) == 0)
same((4, "ג"), [sp.Rational(1, 2), sp.Rational(-1, 4)])

# ---- Q4d
ok("Q4d (a,b),(-b,a) orthogonal (inner 0); (a,a),(b,b) give 2ab <= 2|ab| only",
   (lambda aa, bb: aa * (-bb) + bb * aa == 0 and aa * bb + aa * bb <= 2 * abs(aa * bb))(3, 5))
same((4, "ד"), [1 * 2 + 2 * 1])
ok("Q4d (ab+ba)^2 <= (a^2+b^2)^2 brute", all((2 * p * q) ** 2 <= (p * p + q * q) ** 2 for p in range(-9, 10) for q in range(-9, 10)))

# ---- Q5a SVD of [[-1,1],[-1,1],[1,1]]
A = sp.Matrix([[-1, 1], [-1, 1], [1, 1]])
AtA = A.T * A
ok("Q5a A^T A = [[3,-1],[-1,3]], eigenvalues 4,2", AtA == sp.Matrix([[3, -1], [-1, 3]]) and set(AtA.eigenvals()) == {4, 2})
v1 = sp.Matrix([1, -1]) / sp.sqrt(2)
u1 = A * v1 / 2
ok("Q5a A v1 = 2 u1 with u1 = (-1,-1,0)/sqrt2", u1 == sp.Matrix([-1, -1, 0]) / sp.sqrt(2) and (AtA * v1 - 4 * v1) == sp.zeros(2, 1))
same((5, "א"), [AtA[0, 1], 4, sp.sqrt(2), u1[0]])

# ---- Q5b
res = solve_congruence((2, 3), (3, 5), (4, 7))
ok("Q5b x = 53 mod 105", res == (53, 105))
ok("Q5b a1=2 (2*2=1 mod 3), x1=2 (35*2=1 mod 3), sum 263", pow(2, -1, 3) == 2 and (35 * 2) % 3 == 1 and 2 * 35 * 2 + 3 * 21 + 4 * 15 == 263 and 263 % 105 == 53)
same((5, "ב"), [2, 2, 263, 53])

print("FAILED: " + ", ".join(bad) if bad else "ALL OK")
sys.exit(1 if bad else 0)
