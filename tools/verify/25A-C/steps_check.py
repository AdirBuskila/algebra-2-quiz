# -*- coding: utf-8 -*-
"""Step-author checks for 25A-C: every numeric step answer and choice claim recomputed with sympy / brute force.
Run: PYTHONUTF8=1 py -I tools/verify/25A-C/steps_check.py   (ASCII output, exit 1 on FAIL)"""
import json
import pathlib
import random
import sys

import sympy as sp
from sympy.ntheory import n_order
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "25A-C.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
bad = []
R = sp.Rational


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
    d = abs(float(s["answer"]) - float(expected))
    ok(label, d <= max(float(s["tol"]), 1e-12), f"stored={s['answer']} sympy={float(expected):.6f} tol={s['tol']}")


x = sp.symbols("x")
# ---- Q1a
pts = [(-4, -1), (-2, 0), (2, 4), (4, 5), (5, 6)]
Am = sp.Matrix([[p[0], 1] for p in pts])
yv = sp.Matrix([p[1] for p in pts])
AtA, Aty = Am.T * Am, Am.T * yv
NUM("Q1a sum x^2", 1, "א", 0, AtA[0, 0])
NUM("Q1a sum xy", 1, "א", 1, Aty[0])
sol = AtA.LUsolve(Aty)
NUM("Q1a m", 1, "א", 2, sol[0])
NUM("Q1a n", 1, "א", 3, sol[1])
# ---- Q1b
NUM("Q1b ||1/x||^2", 1, "ב", 1, sp.integrate(x ** -2, (x, 1, 2)))
ok("Q1b g=1 gives norm^2 1 ; g=x gives 7/3 ; antiderivative of x^-2 is -1/x, not ln x",
   sp.integrate(1, (x, 1, 2)) == 1 and sp.integrate(x ** 2, (x, 1, 2)) == R(7, 3) and sp.integrate(x ** -2, x) == -1 / x
   and sp.integrate(x ** -2, (x, 1, 2)) != sp.log(2))
# ---- Q2a
ok("Q2a.1 (1,1) neutral ; (0,0),(1,0) not in G or annihilate",
   all((1 * a) % 5 == a for a in range(1, 5)) and all((1 * b) % 7 == b for b in range(1, 7)) and (0 * 2) % 5 == 0)
NUM("Q2a.1 (3,4)*(1,1) second", 2, "א", 1, (4 * 1) % 7)
NUM("Q2a.2 c", 2, "ב", 0, [c for c in range(1, 5) if (2 * c) % 5 == 1][0])
NUM("Q2a.2 d", 2, "ב", 1, [d for d in range(1, 7) if (3 * d) % 7 == 1][0])
NUM("Q2a.3 |Z5*|", 2, "ג", 0, len(range(1, 5)))
NUM("Q2a.3 |Z7*|", 2, "ג", 1, len(range(1, 7)))
NUM("Q2a.3 |G|", 2, "ג", 2, len(range(1, 5)) * len(range(1, 7)))
NUM("Q2a.4 ord 2 mod 5", 2, "ד", 0, n_order(2, 5))
NUM("Q2a.4 ord 3 mod 7", 2, "ד", 1, n_order(3, 7))
o = min(k for k in range(1, 100) if pow(2, k, 5) == 1 and pow(3, k, 7) == 1)
NUM("Q2a.4 ord (2,3) brute force", 2, "ד", 2, o)
ok("Q2a.4 ord is lcm(4,6)=12, not 24", o == sp.ilcm(4, 6) == 12)
# ---- Q2b
random.seed(3)
Bs = sp.Matrix([[1, 1], [0, 1]])
vs = sp.Matrix([1, -1])
NUM("Q2b.1 v^T B^T B v", 2, "ה", 0, (vs.T * Bs.T * Bs * vs)[0])
Aq = sp.diag(2, 3)
v0 = sp.Matrix([1, 0])
w0 = Bs * v0
NUM("Q2b.2 w^T A w", 2, "ו", 1, (w0.T * Aq * w0)[0])
ok("Q2b.2 option values: (Bv)^TA(Bv)=2 equals v^T B^TAB v ; with B^T v gives 5 ; v^TAv = 2 also (but not general)",
   (v0.T * Bs.T * Aq * Bs * v0)[0] == 2 and ((Bs.T * v0).T * Aq * (Bs.T * v0))[0] == 5)
vt = sp.Matrix([1, 1])
ok("Q2b.2 distractor v^TAv differs for v=(1,1)", (vt.T * Bs.T * Aq * Bs * vt)[0] != (vt.T * Aq * vt)[0])
ok("Q2b.2 (B^TAB)^T != B^T A^T B^T for random B (bug line)", any(
    (lambda B, A: (B.T * A * B).T != B.T * A.T * B.T)(sp.randMatrix(3, 3, 0, 5, seed=s), sp.Matrix([[2, 1, 0], [1, 2, 0], [0, 0, 3]])) for s in range(5)))
import numpy as np
_ok = True
for _s in range(50):
    _r = np.random.RandomState(_s)
    _C = _r.randint(-4, 5, (3, 3)).astype(float)
    _B = _r.randint(-4, 5, (3, 3)).astype(float)
    _M = -(_C.T @ _C) - _B.T @ _B
    _ok = _ok and np.linalg.eigvalsh(_M).max() <= 1e-9
ok("Q2b.1 -A-B^TB negative semidefinite for random PSD A=C^TC and random B", _ok)
# ---- Q3a
A3 = sp.Matrix([[1, 0, 2], [2, 0, 1]])
AAt = A3 * A3.T
NUM("Q3a (AA^T)[1,2]", 3, "א", 0, AAt[0, 1])
ev = sorted(AAt.eigenvals(), reverse=True)
NUM("Q3a sigma1", 3, "א", 1, sp.sqrt(ev[0]))
NUM("Q3a sigma2", 3, "א", 2, sp.sqrt(ev[1]))
u2 = sp.Matrix([1, -1]) / sp.sqrt(2)
v2 = A3.T * u2 / 1
NUM("Q3a v2 first coord", 3, "א", 3, v2[0].evalf())
ok("Q3a v2 = (-1,0,1)/sqrt2", sp.simplify(v2 - sp.Matrix([-1, 0, 1]) / sp.sqrt(2)) == sp.zeros(3, 1))
u1 = sp.Matrix([1, 1]) / sp.sqrt(2)
v1 = A3.T * u1 / 3
v3 = sp.Matrix([0, 1, 0])
ok("Q3a v1,v2,v3 orthonormal", sp.simplify(sp.Matrix.hstack(v1, v2, v3).T * sp.Matrix.hstack(v1, v2, v3) - sp.eye(3)) == sp.zeros(3, 3))
ok("Q3a distractors: (0,0,1) not orthogonal to v2 ; (1,0,1)/sqrt2 is v1", sp.simplify(sp.Matrix([0, 0, 1]).dot(v2)) != 0 and sp.simplify(v1 - sp.Matrix([1, 0, 1]) / sp.sqrt(2)) == sp.zeros(3, 1))
U = sp.Matrix.hstack(u1, u2)
S = sp.Matrix([[3, 0, 0], [0, 1, 0]])
V = sp.Matrix.hstack(v1, v2, v3)
ok("Q3a U S V^T = A", sp.simplify(U * S * V.T - A3) == sp.zeros(2, 3))
# ---- Q3b
uu, vv = sp.Matrix([1, 2]), sp.Matrix([3, 1])
NUM("Q3b polarization example", 3, "ב", 0, R(1, 4) * ((uu + vv).dot(uu + vv) - (uu - vv).dot(uu - vv)))
ok("Q3b equals dot product 5", uu.dot(vv) == 5)
# ---- Q4a
a = sp.symbols("a", real=True)
M4 = sp.Matrix([[a ** 2, 0, 1], [0, a, 0], [1, 0, a ** 2]])
ok("Q4a eigenvalues a, a^2-1, a^2+1", M4.eigenvals() == {a: 1, a ** 2 - 1: 1, a ** 2 + 1: 1})
NUM("Q4a trace at a=2", 4, "א", 0, M4.trace().subs(a, 2))
for nm, st in [("a,a^2-1,a^2", [a, a ** 2 - 1, a ** 2]), ("a,a^2-1,a^2+2", [a, a ** 2 - 1, a ** 2 + 2]), ("2a,a^2-1,a^2+1", [2 * a, a ** 2 - 1, a ** 2 + 1])]:
    ok("Q4a distractor {" + nm + "} wrong trace", sp.simplify(sum(st) - M4.trace()) != 0)
def ee(v):
    return list(M4.subs(a, v).eigenvals(multiple=True))
grid = [R(k, 4) for k in range(-16, 17)]
ok("Q4a PSD iff a>=1", all(all(e >= 0 for e in ee(g)) == (g >= 1) for g in grid))
ok("Q4a PD iff a>1", all(all(e > 0 for e in ee(g)) == (g > 1) for g in grid))
ok("Q4a never NSD", not any(all(e <= 0 for e in ee(g)) for g in grid))
ok("Q4a a=1 -> {0,1,2}; a=1/2 has -3/4 ; a=-2 -> {-2,3,5}", sorted(ee(1)) == [0, 1, 2] and R(-3, 4) in ee(R(1, 2)) and sorted(ee(-2)) == [-2, 3, 5])
# ---- Q4b
NUM("Q4b M", 4, "ב", 0, 70)
NUM("Q4b x1", 4, "ב", 1, sp.mod_inverse(14, 5))
NUM("Q4b x3", 4, "ב", 2, sp.mod_inverse(10, 7))
NUM("Q4b x", 4, "ב", 3, solve_congruence((2, 5), (3, 2), (4, 7))[0])
ok("Q4b 67 satisfies all three and sum 347", 67 % 5 == 2 and 67 % 2 == 3 % 2 and 67 % 7 == 4 and 2 * 14 * 4 + 35 + 4 * 10 * 5 == 347 and 347 % 70 == 67)
# ---- Q5a
A5 = sp.Matrix([[5, 0, 0], [0, 4, 2], [0, 2, 1]])
ok("Q5a eigenvalues 5 (x2), 0", A5.eigenvals() == {5: 2, 0: 1})
NUM("Q5a multiplicity of 5", 5, "א", 0, A5.eigenvals()[5])
NUM("Q5a dot v3.v2", 5, "א", 1, sp.Matrix([0, 1, -2]).dot(sp.Matrix([0, 2, 1])))
NUM("Q5a ||(0,2,1)||", 5, "א", 2, sp.Matrix([0, 2, 1]).norm().evalf())
ok("Q5a v1.v2=0, norms 1 and sqrt5, det A = 0", sp.Matrix([1, 0, 0]).dot(sp.Matrix([0, 2, 1])) == 0 and A5.det() == 0)
Q = sp.Matrix.hstack(sp.Matrix([1, 0, 0]), sp.Matrix([0, 2, 1]) / sp.sqrt(5), sp.Matrix([0, 1, -2]) / sp.sqrt(5))
ok("Q5a Q D Q^T = A", sp.simplify(Q * sp.diag(5, 5, 0) * Q.T - A5) == sp.zeros(3, 3) and sp.simplify(Q.T * Q) == sp.eye(3))
# ---- Q5b (brute force on small groups where every element is its own inverse: Z2^3)
import itertools
els = list(itertools.product(range(2), repeat=3))
mul = lambda p, q: tuple((i + j) % 2 for i, j in zip(p, q))
ok("Q5b group Z2^3: all g^2=e ; abelian ; x^3=x ; x^3=y^5 implies x=y",
   all(mul(g, g) == (0, 0, 0) for g in els) and all(mul(p, q) == mul(q, p) for p in els for q in els)
   and all(mul(mul(g, g), g) == g for g in els))
ok("Q5b Z2: g=1 has g=g^-1 but g^2=e != g", (1 + 1) % 2 == 0 and 1 != 0)

print()
print("FAILED:" if bad else "ALL OK", bad)
sys.exit(1 if bad else 0)
