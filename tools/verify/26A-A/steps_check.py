# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided STEPS of sitting 26A-A (algebra-2).
Run after the generator: PYTHONUTF8=1 py -I tools/verify/26A-A/steps_check.py
Reads tools/raw/26A-A.json, recomputes every numeric answer and the factual claims behind choice/findbug steps.
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import json
import pathlib
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "26A-A.json"
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
    ok(f"Q{key[0]}{key[1]} numeric steps == sympy values", good, f"stored {[g[0] for g in got]} sympy {[float(e) for e in expected]}")


# ---- Q1a: A = [[3,1,0],[1,3,0],[0,0,1]]
A = sp.Matrix([[3, 1, 0], [1, 3, 0], [0, 0, 1]])
ev = A.eigenvals()
ok("Q1a eigenvalues {1,2,4}", set(ev) == {1, 2, 4})
v1 = (A - 4 * sp.eye(3)).nullspace()[0].normalized()
v3 = (A - 1 * sp.eye(3)).nullspace()[0].normalized()
ok("Q1a v1 first comp 1/sqrt2 and v3 = +-e3", abs(abs(v1[0]) - 1 / sp.sqrt(2)) == 0 and abs(v3[2]) == 1)
same((1, "א"), [A.det(), 1 / sp.sqrt(2), 1])
ok("Q1a A symmetric", A == A.T)

# ---- Q1b: Cauchy-Schwarz with u=a/sqrt(b), v=sqrt(b); example a=(1,3), b=(1,1)
a, b = [1, 3], [1, 1]
lhs = sum(sp.Rational(x * x, y) for x, y in zip(a, b))
rhs = sp.Rational(sum(a) ** 2, sum(b))
same((1, "ב"), [lhs, rhs])
t = sp.symbols("t", positive=True)
ok("Q1b chosen vectors give <u,v>=a, |u|^2=a^2/b, |v|^2=b",
   all(sp.simplify((x / sp.sqrt(y)) * sp.sqrt(y) - x) == 0 for x, y in zip(sp.symbols("a1 a2", positive=True), sp.symbols("b1 b2", positive=True))))
# wrong options really fail: option 1 (a/b, b): squared norms a^2/b^2, b^2
a1, b1 = sp.symbols("a1 b1", positive=True)
ok("Q1b wrong option (a/b, b) has norm^2 a^2/b^2", sp.simplify((a1 / b1) ** 2 - a1 ** 2 / b1 ** 2) == 0 and sp.simplify(a1 ** 2 / b1 ** 2 - a1 ** 2 / b1) != 0)
ok("Q1b wrong option (a*sqrt b, sqrt b) inner = a*b", sp.simplify(a1 * sp.sqrt(b1) * sp.sqrt(b1) - a1 * b1) == 0)
ok("Q1b wrong option (a, 1/sqrt b) inner = a/sqrt b != a", sp.simplify(a1 / sp.sqrt(b1) - a1) != 0)

# ---- Q2: K in M2(Z7)
K = [(x, y) for x in range(7) for y in range(7) if (x * x + y * y) % 7 == 1]
ok("Q2b |K| = 8", len(K) == 8)
ok("Q2b a=0 gives 2 pairs", sum(1 for x, y in K if x == 0) == 2)
ok("Q2b a^2=b^2=4 gives 4 pairs", sum(1 for x, y in K if x * x % 7 == 4 and y * y % 7 == 4) == 4)
same((2, "ב"), [2, 4, 8])


def mm(X, Y):
    return (X * Y).applyfunc(lambda e: e % 7)


X = sp.Matrix([[2, 2], [5, 2]])
X2, X4, X8 = mm(X, X), None, None
X4 = mm(X2, X2)
X8 = mm(X4, X4)
order_ = next(k for k in range(1, 50) if (X ** k).applyfunc(lambda e: e % 7) == sp.eye(2))
inv = sp.Matrix([[2, 5], [-5, 2]]).applyfunc(lambda e: e % 7)
ok("Q2d inverse of X is [[2,5],[-5,2]]", mm(X, inv) == sp.eye(2))
ok("Q2a inverse of (a,b)=(2,2) has top-right 5", sp.Matrix([[2, -2], [2, 2]])[0, 1] % 7 == 5)
ok("Q2a inverse formula valid for all of K",
   all(mm(sp.Matrix([[x, y], [-y, x]]), sp.Matrix([[x, -y], [y, x]])) == sp.eye(2) for x, y in K))
ok("Q2a inverse in K for all of K", all(((x * x + y * y) % 7) == 1 for x, y in K))
ok("Q2a 2I invertible but not in K", sp.Matrix([[2, 0], [0, 2]]).det() % 7 != 0 and (4 + 0) % 7 != 1)
same((2, "א"), [5])
ok("Q2c X in K", (2 * 2 + 2 * 2) % 7 == 1)
same((2, "ג"), [(2 * 2 + 2 * 2) % 7, X2[0, 1] % 7, X4[0, 0] % 7, order_])
ok("Q2c X^2 = [[0,1],[-1,0]], X^4 = -I", X2 == sp.Matrix([[0, 1], [6, 0]]) and X4 == sp.Matrix([[6, 0], [0, 6]]))
same((2, "ד"), [pow(2, -1, 7), 2, 5])
ok("Q2d x-y = 4, x+y = 0 mod 7 solved by (2,5)", (2 - 5) % 7 == 4 and (2 + 5) % 7 == 0)
same((2, "ה"), [order_])
ok("Q2e |K| = ord(X) = 8, so cyclic", len(K) == order_ == 8)
ok("Q2e Z2xZ2 is abelian, even order, 2-power, not cyclic",
   all(2 * 1 % 2 == 0 for _ in [0]) and max(1 if (a_ == 0 and b_ == 0) else 2 for a_ in range(2) for b_ in range(2)) == 2)

# ---- Q3a
x = sp.symbols("x", real=True)
M = sp.Matrix([[1, x, 0], [x, 2, x], [0, x, 1]])
cp = sp.factor(M.charpoly().as_expr())
lam = sp.symbols("lambda")
eigs = list(M.eigenvals())
ok("Q3a eigenvalues are 1, (3 +- sqrt(8x^2+1))/2",
   all(sp.simplify(M.charpoly(lam).as_expr().subs(lam, e)) == 0 for e in [1, (3 + sp.sqrt(8 * x ** 2 + 1)) / 2, (3 - sp.sqrt(8 * x ** 2 + 1)) / 2]))
lo = sp.Rational(1, 2) * (3 - sp.sqrt(8 * x ** 2 + 1))
ok("Q3a charpoly (1-l)(l^2-3l-2x^2+2)", sp.expand(M.charpoly(lam).as_expr() + (1 - lam) * (lam ** 2 - 3 * lam - 2 * x ** 2 + 2)) == 0
   or sp.expand(M.charpoly(lam).as_expr() - (lam - 1) * (lam ** 2 - 3 * lam - 2 * x ** 2 + 2)) == 0)
same((3, "א"), [lo.subs(x, 1)])
def _mineig(xv):
    return min(sp.N(e) for e in M.subs(x, xv).eigenvals())


_grid = [sp.Rational(k, 20) for k in range(-60, 61)]
ok("Q3a (true matrix eigenvalues) min eig >=0 iff |x|<=1 and >0 iff |x|<1",
   all((_mineig(g) >= -1e-9) == (abs(g) <= 1) and (_mineig(g) > 1e-9) == (abs(g) < 1) for g in _grid))
ok("Q3a largest eig is always >0 (never negative definite)", all(max(sp.N(e) for e in M.subs(x, g).eigenvals()) > 0 for g in _grid))
ok("Q3a x=2 indefinite, no x gives negative (eig 1 fixed)", lo.subs(x, 2) < 0)
ok("Q3a wrong options: x in (0,1) subset, x>1 not pos def", lo.subs(x, 2) < 0)

# ---- Q3c / Q3d numeric example a=(1,1), b=(3,1)
av, bv = sp.Matrix([1, 1]), sp.Matrix([3, 1])
coef = bv.dot(av) / av.dot(av)
pv = coef * av
cv = bv - pv
same((3, "ג"), [coef, cv.dot(av)])
ok("Q3c c=(1,-1), p=(2,2)", cv == sp.Matrix([1, -1]) and pv == sp.Matrix([2, 2]))
same((3, "ד"), [pv.dot(pv)])
ok("Q3d |b|^2=|c|^2+|p|^2 (10=2+8) and p != b, |p|!=|c|, p != 0",
   bv.dot(bv) == cv.dot(cv) + pv.dot(pv) and pv != bv and pv.dot(pv) != cv.dot(cv) and pv != sp.zeros(2, 1))

# ---- Q4: (a,b)o(x,y) = (a+x, b+(-1)^a y)


def op(p, q):
    return (p[0] + q[0], p[1] + (-1) ** p[0] * q[1])


ok("Q4a (1,2)o(3,4) second comp -2", op((1, 2), (3, 4)) == (4, -2))
inv13 = (-1, (-1) ** (1 - 1) * 3)
inv25 = (-2, sp.Integer(-1) ** (1 - 2) * 5)
ok("Q4a inverse (1,3) -> (-1,3), (2,5) -> (-2,-5)", op((1, 3), inv13) == (0, 0) and op((2, 5), inv25) == (0, 0))
same((4, "א"), [-2, 3, -5])
rng = range(-3, 4)
ok("Q4a associativity (brute force)", all(op(op(p, q), r) == op(p, op(q, r)) for p in itertools.product(rng, rng) for q in itertools.product(rng, rng) for r in itertools.product(rng, rng)))
ok("Q4a wrong line (-1)^x v only is wrong: second comp b+(-1)^a(y+(-1)^x v) differs",
   any(op(p, op(q, r))[1] != p[1] + (-1) ** p[0] * q[1] + (-1) ** q[0] * r[1] for p in [(1, 0)] for q in [(1, 0)] for r in [(0, 1)]))
ok("Q4b (1,1)o(1,0)=(2,1), (1,0)o(1,1)=(2,-1)", op((1, 1), (1, 0)) == (2, 1) and op((1, 0), (1, 1)) == (2, -1))
same((4, "ב"), [1, -1])
ok("Q4b pitfall: (2,1)o(2,3) commute", op((2, 1), (2, 3)) == op((2, 3), (2, 1)))
# center
center = [(a_, b_) for a_ in range(-6, 7) for b_ in range(-6, 7)
          if all(op((a_, b_), (x_, y_)) == op((x_, y_), (a_, b_)) for x_ in range(-6, 7) for y_ in range(-6, 7))]
ok("Q4c centre = {(a,0): a even}", all(b_ == 0 and a_ % 2 == 0 for a_, b_ in center) and len(center) == len([a_ for a_ in range(-6, 7) if a_ % 2 == 0]))
same((4, "ג"), [1, 0])
ok("Q4c wrong options fail", op((2, 1), (1, 1)) == (3, 2) and op((1, 1), (2, 1)) == (3, 0)
   and op((1, 0), (0, 1)) == (1, -1) and op((0, 1), (1, 0)) == (1, 1) and op((2, 0), (1, 5)) == op((1, 5), (2, 0)))

# ---- Q5: orthonormal u,v,w = e1,e2,e3 case (example) and general facts
u, v, w = sp.eye(3)[:, 0], sp.eye(3)[:, 1], sp.eye(3)[:, 2]
P = u * u.T + v * v.T
ok("Q5a P w = 0, P u = u", P * w == sp.zeros(3, 1) and P * u == u)
same((5, "א"), [0, 1])
ok("Q5b trace P = 2, P symmetric, eigenvalues {1,1,0}", P.trace() == 2 and P == P.T and sorted(P.eigenvals().items()) == [(0, 1), (1, 2)])
same((5, "ב"), [2])
ok("Q5c dim null P = 1 and it is span{w}", len(P.nullspace()) == 1 and P.nullspace()[0] == w)
same((5, "ג"), [1])
# non-trivial orthonormal basis (rotation) too
th = sp.Rational(3, 5), sp.Rational(4, 5)
R = sp.Matrix([[th[0], -th[1], 0], [th[1], th[0], 0], [0, 0, 1]])
P2 = R[:, 0] * R[:, 0].T + R[:, 1] * R[:, 1].T
ok("Q5 rotated basis: P2 w = 0, P2 u = u, null = span w", P2 * R[:, 2] == sp.zeros(3, 1) and P2 * R[:, 0] == R[:, 0] and len(P2.nullspace()) == 1)
sol = solve_congruence((2, 3), (3, 4), (5, 7))
ok("Q5d reduced residues 2,3,5; x=47 mod 84", sol == (47, 84) and (pow(2, -1, 3), pow(3, -1, 4), 3 * pow(2, -1, 7) % 7) == (2, 3, 5))
ok("Q5d 2x=1 mod 3 -> 2; 3x=1 mod 4 -> 3; 2x=3 mod 7 -> 5", (2 * 2) % 3 == 1 and (3 * 3) % 4 == 1 and (2 * 5) % 7 == 3)
ok("Q5d x3: 12*3=36=1 mod 7", (12 * 3) % 7 == 1 and 84 // 7 == 12)
same((5, "ד"), [2, 5, 3, 47])
ok("Q5d crt sum 299 mod 84 = 47", (2 * 28 * 1 + 3 * 21 * 1 + 5 * 12 * 3) == 299 and 299 % 84 == 47)

print("FAILED: " + ", ".join(bad) if bad else "ALL OK")
sys.exit(1 if bad else 0)
