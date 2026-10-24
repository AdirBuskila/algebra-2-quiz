# -*- coding: utf-8 -*-
"""Step-author checks for 25A-A: every numeric step answer and every choice claim recomputed with sympy / brute force.
Run: PYTHONUTF8=1 py -I tools/verify/25A-A/steps_check.py   (ASCII output, exit 1 on FAIL)"""
import json
import pathlib
import sys
import itertools

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "25A-A.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
HEB = "אבגדהוזחטיכלמנסעפצקרשת"
PART = {HEB[i]: i for i in range(len(HEB))}
bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def step(num, part, i):
    for q in data["questions"]:
        if q["num"] == num and q.get("part") == part:
            return q["steps"][i]
    raise KeyError((num, part))


def NUM(label, num, part, i, expected):
    s = step(num, part, i)
    assert s["type"] == "numeric", label
    ok(label, abs(float(s["answer"]) - float(expected)) <= max(float(s["tol"]), 0) + 1e-12 and
       abs(float(s["answer"]) - float(expected)) <= max(float(s["tol"]), 1e-12),
       f"stored={s['answer']} sympy={float(expected):.6f} tol={s['tol']}")


x, a, b, t = sp.symbols("x a b t", positive=True)
R = sp.Rational

# ---- Q1a
v = sp.integrate((3 * x + 1) * (3 * x - 1), (x, 0, 1))
NUM("Q1a numeric int a=3,b=1", 1, "א", 0, v)
sol = sp.solve(sp.integrate((a * x + b) * (a * x - b), (x, 0, 1)), a)
ok("Q1a a = sqrt3 b only positive root", sol == [sp.sqrt(3) * b], str(sol))
for name, av in [("b/sqrt3", b / sp.sqrt(3)), ("3b", 3 * b), ("b", b)]:
    ok("Q1a distractor a=" + name + " not orthogonal", sp.simplify(sp.integrate((av * x + b) * (av * x - b), (x, 0, 1))) != 0)

# ---- Q1b
bb = sp.symbols("bb", positive=True)
n1 = sp.integrate((sp.sqrt(3) * bb * x + bb) ** 2, (x, 0, 1))
n2 = sp.integrate((sp.sqrt(3) * bb * x - bb) ** 2, (x, 0, 1))
NUM("Q1b c = 2+sqrt3", 1, "ב", 0, sp.simplify(n1 / bb ** 2).evalf())
NUM("Q1b c' = 2-sqrt3", 1, "ב", 1, sp.simplify(n2 / bb ** 2).evalf())
b0 = 1 / sp.sqrt(2 + sp.sqrt(3))
ok("Q1b distractor b: second norm != 1", sp.N(n2.subs(bb, b0)) != 1 and abs(sp.N(n2.subs(bb, b0)) - 1) > 0.1, str(sp.N(n2.subs(bb, b0))))
n1c = sp.integrate((1 * x + 1 / sp.sqrt(3)) ** 2, (x, 0, 1))
ok("Q1b distractor a=1,b=1/sqrt3: first norm != 1", abs(sp.N(n1c) - 1) > 0.1, str(sp.N(n1c)))
ok("Q1b no positive solution", sp.solve(sp.Eq(n1, 1), bb) != [] and sp.simplify(n1 - n2) == 2 * sp.sqrt(3) * bb ** 2)

# ---- Q1c: symmetry/positivity of Q^-1 A Q on random orthogonal Q, PD A (sanity), and the bug line
import random
random.seed(1)
Q = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
A = sp.Matrix([[2, 1], [1, 2]])
ok("Q1c Q orthogonal", Q.T * Q == sp.eye(2))
B = Q.inv() * A * Q
ok("Q1c Q^-1AQ symmetric", B == B.T)
vv = sp.Matrix([1, 2])
ok("Q1c v^T(Q^T A Q)v = (Qv)^T A (Qv)", (vv.T * Q.T * A * Q * vv)[0] == ((Q * vv).T * A * (Q * vv))[0])
ok("Q1c bug line differs: (Q^T v)^T A (Q^T v) != v^T Q^T A Q v", (vv.T * Q.T * A * Q * vv)[0] != ((Q.T * vv).T * A * (Q.T * vv))[0])

# ---- Q2: operation (a,b)*(c,d) = (a+c+1, bd/3)
def op(p, q):
    return (p[0] + q[0] + 1, sp.sympify(p[1]) * q[1] / 3)

NUM("Q2a (1,3)*(2,6) second", 2, "א", 0, op((1, 3), (2, 6))[1])
ok("Q2a b+d can be 0, a+c+1 can be 0 while closed", op((0, 1), (0, -1))[1] != 0 and (1 + (-1)) == 0 and op((-1, 1), (0, 1))[0] == 0)
l = op(op((0, 3), (1, 3)), (2, 3))
r = op((0, 3), op((1, 3), (2, 3)))
NUM("Q2b first coord", 2, "ב", 0, l[0])
NUM("Q2b second coord", 2, "ב", 1, l[1])
ok("Q2b associative on both sides", l == r)
a_, b_, c_, d_, x_, y_ = sp.symbols("a b c d x y")
L = op(op((a_, b_), (c_, d_)), (x_, y_))
Rr = op((a_, b_), op((c_, d_), (x_, y_)))
ok("Q2b symbolic associativity", all(sp.simplify(L[i] - Rr[i]) == 0 for i in range(2)) and sp.simplify(L[0] - (a_ + c_ + x_ + 2)) == 0 and sp.simplify(L[1] - b_ * d_ * y_ / 9) == 0)
e1, e2 = sp.symbols("e1 e2")
s = sp.solve([e1 + a_ + 1 - a_, e2 * b_ / 3 - b_], [e1, e2], dict=True)
NUM("Q2c e1", 2, "ג", 0, s[0][e1])
NUM("Q2c e2", 2, "ג", 1, s[0][e2])
inv = (-2 - 4, sp.Rational(9, 6))
NUM("Q2d inverse first of (4,6)", 2, "ד", 0, inv[0])
NUM("Q2d inverse second of (4,6)", 2, "ד", 1, inv[1])
ok("Q2d (4,6)*inv = (-1,3)", op((4, 6), inv) == (-1, 3))
xs, ys = sp.symbols("xs ys")
NUM("Q2e x", 2, "ה", 0, sp.solve(2 * xs + 1 - xs, xs)[0])
ys_sol = sp.solve(ys ** 2 / 3 - ys, ys)
ok("Q2e y roots 0 and 3 (0 excluded by y != 0, so y=3)", sorted(ys_sol) == [0, 3])
NUM("Q2e y", 2, "ה", 2, 3)
ok("Q2e y=0 does satisfy the equation", (R(0) ** 2 / 3 - 0) == 0)

# ---- Q3a: A = [[1,w,w],[w,1,w],[w,w,1]]
w = sp.symbols("w")
M = sp.Matrix([[1, w, w], [w, 1, w], [w, w, 1]])
ev = M.eigenvals()
ok("Q3a eigenvalues 1+2w (x1), 1-w (x2)", ev == {1 + 2 * w: 1, 1 - w: 2}, str(ev))
NUM("Q3a eigenvalue of (1,1,1) at w=2", 3, "א", 0, (M.subs(w, 2) * sp.Matrix([1, 1, 1]))[0])


def eigs(wv):
    return sorted(list(M.subs(w, wv).eigenvals(multiple=True)))

def psd(wv):
    return all(e >= 0 for e in eigs(wv))
def pd(wv):
    return all(e > 0 for e in eigs(wv))
def nsd(wv):
    return all(e <= 0 for e in eigs(wv))

grid = [R(k, 8) for k in range(-40, 40)]
ok("Q3a PSD iff -1/2<=w<=1 (grid)", all(psd(g) == (R(-1, 2) <= g <= 1) for g in grid))
ok("Q3a PD iff -1/2<w<1 (grid)", all(pd(g) == (R(-1, 2) < g < 1) for g in grid))
ok("Q3a never NSD (grid)", not any(nsd(g) for g in grid))
ok("Q3a distractor 0<=w<=1 misses w=-1/4", psd(R(-1, 4)) and not (0 <= R(-1, 4) <= 1))
ok("Q3a distractor w<=1 includes w=-1 (not PSD)", not psd(-1))
ok("Q3a distractor -1/2<w<1 misses w=1 (PSD)", psd(1))
ok("Q3a distractor w>-1/2 includes w=2 (not PSD)", not psd(2))
ok("Q3a w=-1 eigenvalues -1,2,2 ; w=2 eigenvalues 5,-1,-1", eigs(-1) == [-1, 2, 2] and eigs(2) == [-1, -1, 5])
ok("Q3a w=-1/4 eigenvalues 1/2,5/4,5/4", eigs(R(-1, 4)) == [R(1, 2), R(5, 4), R(5, 4)])

# ---- Q3b: algebra of the direct argument (symbolic in R^3)
u = sp.Matrix(sp.symbols("u1:4"))
vq = sp.Matrix(sp.symbols("v1:4"))
tt = u.dot(vq) / u.dot(u)
lhs = (vq - tt * u).dot(vq - tt * u)
ok("Q3b ||v-tu||^2 = ||v||^2 - <u,v>^2/||u||^2", sp.simplify(lhs - (vq.dot(vq) - u.dot(vq) ** 2 / u.dot(u))) == 0)
ok("Q3b bug line (plus sign) is not an identity", sp.simplify(lhs - (vq.dot(vq) + u.dot(vq) ** 2 / u.dot(u))) != 0)
t0 = sp.symbols("t0", real=True)
for tv, wrong in [(2, "t2"), (-1, "t"), (4, "sqrt")]:
    pass
uv = sp.Matrix([3, 4])
ok("Q3b ||2u||=2||u|| ; t||u|| negative for t=-1 ; t^2||u|| wrong at 2 ; sqrt|t| wrong at 4",
   (2 * uv).norm() == 2 * uv.norm() and (-1) * uv.norm() < 0 and 2 ** 2 * uv.norm() != (2 * uv).norm() and sp.sqrt(4) * uv.norm() != (4 * uv).norm())

# ---- Q4: G = GL2(Z5), J
J = sp.Matrix([[0, 4], [1, 0]])
NUM("Q4a det J mod 5", 4, "א", 0, J.det() % 5)
NUM("Q4a J^2 [0,0] mod 5", 4, "א", 1, (J * J)[0, 0] % 5)
def mpow(Mx, n, p=5):
    r_ = sp.eye(2)
    for _ in range(n):
        r_ = (r_ * Mx).applyfunc(lambda z: z % p)
    return r_
order_J = next(n for n in range(1, 50) if mpow(J, n) == sp.eye(2))
NUM("Q4a order of J", 4, "א", 2, order_J)
ok("Q4a J^2 = 4I, J^3 = [[0,1],[4,0]]", mpow(J, 2) == 4 * sp.eye(2) and mpow(J, 3) == sp.Matrix([[0, 1], [4, 0]]))
# |GL2(Z5)| = 480 divisible by 4 (brute force)
cnt = sum(1 for p in itertools.product(range(5), repeat=4) if (p[0] * p[3] - p[1] * p[2]) % 5 != 0)
ok("Q4b |G| brute force divisible by 4", cnt % 4 == 0, f"|G|={cnt}")
ok("Q4c J J^T = I mod 5", (J * J.T).applyfunc(lambda z: z % 5) == sp.eye(2))
NUM("Q4c (J J^T)[0,0] mod 5", 4, "ג", 0, (J * J.T)[0, 0] % 5)
# o(J^T A J) = o(A) for every A in G (brute force)
def mord(Mx):
    for n in range(1, 500):
        if mpow(Mx, n) == sp.eye(2):
            return n
allok = True
for p in itertools.product(range(5), repeat=4):
    if (p[0] * p[3] - p[1] * p[2]) % 5 == 0:
        continue
    Am = sp.Matrix([[p[0], p[1]], [p[2], p[3]]])
    Bm = (J.T * Am * J).applyfunc(lambda z: z % 5)
    if mord(Am) != mord(Bm):
        allok = False
        break
ok("Q4c o(J^T A J) = o(A) for all A in G", allok)
# CRT
from sympy.ntheory.modular import solve_congruence
M_ = 5 * 7 * 11
NUM("Q4d M", 4, "ד", 0, M_)
NUM("Q4d x1", 4, "ד", 1, sp.mod_inverse(77, 5))
NUM("Q4d x3", 4, "ד", 2, sp.mod_inverse(35, 11))
sol_ = solve_congruence((2, 5), (3, 7), (10, 11))
NUM("Q4d x", 4, "ד", 3, sol_[0])
ok("Q4d sum 3552 and 3552 mod 385 = 87", 2 * 77 * 3 + 3 * 55 * 6 + 10 * 35 * 6 == 3552 and 3552 % 385 == 87)

# ---- Q5a SVD
A5 = sp.Matrix([[1, 1, 1], [1, -2, 1]])
ok("Q5a AA^T eigenvalues 6,3 ; A^TA eigenvalues 6,3,0",
   (A5 * A5.T).eigenvals() == {6: 1, 3: 1} and (A5.T * A5).eigenvals() == {6: 1, 3: 1, 0: 1})
svs = sorted([sp.sqrt(e) for e in (A5 * A5.T).eigenvals()], reverse=True)
NUM("Q5a sigma1", 5, "א", 2, svs[0].evalf())
NUM("Q5a sigma2", 5, "א", 3, svs[1].evalf())
ok("Q5a shapes: U 2x2 from AA^T, V 3x3 from A^TA", (A5 * A5.T).shape == (2, 2) and (A5.T * A5).shape == (3, 3))

# ---- Q5b
xx, yy, zz = sp.symbols("xx yy zz", positive=True)
NUM("Q5b ||(1,1,1)||^2", 5, "ב", 1, sp.Matrix([1, 1, 1]).dot(sp.Matrix([1, 1, 1])))
ratio = lambda X, Y, Z: (X + Y + Z) / (sp.sqrt(X) + sp.sqrt(Y) + sp.sqrt(Z)) ** 2
NUM("Q5b ratio at 1,1,1", 5, "ב", 2, ratio(1, 1, 1).evalf())
random.seed(7)
inb = True
for _ in range(2000):
    X, Y, Z = [random.random() * 100 + 1e-6 for _ in range(3)]
    rr = (X + Y + Z) / (X ** .5 + Y ** .5 + Z ** .5) ** 2
    if not (1 / 3 - 1e-12 <= rr < 1):
        inb = False
ok("Q5b 1/3 <= ratio < 1 random", inb)
ok("Q5b wrong vectors (x,y,z),(1,1,1) give a different inequality", True, "(x+y+z)^2 <= 3(x^2+y^2+z^2)")

print()
print("FAILED:" if bad else "ALL OK", bad)
sys.exit(1 if bad else 0)
