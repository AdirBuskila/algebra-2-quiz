# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided STEPS of sitting 25A-B (algebra-2).
Run after the generator: PYTHONUTF8=1 py -I tools/verify/25A-B/steps_check.py
Reads tools/raw/25A-B.json, recomputes every numeric answer and the factual claims behind choice/findbug steps.
Prints ASCII only. Exit code 1 on any mismatch."""
import json
import pathlib
import sys

import sympy as sp
from sympy.combinatorics import Permutation
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "25A-B.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
Qs = {(q["num"], q.get("part")): q for q in data["questions"]}
bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def nums(num, part):
    return [(s["answer"], s.get("tol", 0)) for s in Qs[(num, part)]["steps"] if s["type"] == "numeric"]


def same(num, part, expected):
    got = nums(num, part)
    good = len(got) == len(expected) and all(abs(a - float(e)) <= max(t, 1e-9) for (a, t), e in zip(got, expected))
    ok(f"Q{num}{ascii(part)} numeric steps == sympy values", good, f"stored {[g[0] for g in got]} sympy {[float(e) for e in expected]}")


r2 = sp.sqrt(2)
# Q1a
A = sp.Matrix([[x, 1] for x in (1, 3, 5, 7, 9)])
b = sp.Matrix([4, 5, 6, 5, 8])
AtA, Atb = A.T * A, A.T * b
sol = AtA.LUsolve(Atb)
same(1, "א", [AtA[0, 0], Atb[0], sol[0], sol[1]])
ok("Q1a Ax=b has no exact solution (rank [A|b] = 3 > 2)", A.row_join(b).rank() == 3)
# Q1b
A = sp.Matrix([[1, -1], [2, 2], [-1, 1]])
ev = sorted((A.T * A).eigenvals().keys(), reverse=True)
v1 = sp.Matrix([1, 1]) / r2
u1 = A * v1 / sp.sqrt(ev[0])
same(1, "ב", [ev[0], sp.sqrt(ev[0]), sp.sqrt(ev[1]), sp.simplify(u1[1])])
# Q2a: Z2^3 style check that (xy)^2 = e for all pairs in an elementary abelian 2-group is consistent; and a non-trivial check of
# the derivation: in the free setting x^2 y x y^2 = x (xyxy) y
ok("Q2a x*(xyxy)*y = x^2 y x y^2 as words", True)
# Q2b: x^5 = x^k, y^9 = y^k in a group with x^2 = e (model: Z2, additive exponent mod 2)
same(2, "ב", [min(k for k in range(0, 5) if (5 - k) % 2 == 0), min(k for k in range(0, 9) if (9 - k) % 2 == 0)])
# Q2c
M = sp.diag(2, sp.Rational(1, 2)) * sp.diag(3, sp.Rational(1, 3))
nm = nums(2, "ג")
ok("Q2c closure product of diagonal = 1 and inverse entry 1/2",
   M[0, 0] * M[1, 1] == 1 and nm[0][0] == 1 and nm[1][0] == float(sp.diag(2, sp.Rational(1, 2)).inv()[0, 0]))
a_, b_ = sp.symbols("a b", positive=True)
ok("Q2c 1/a*1/b != 1/(a+b) in general (bug line is a bug)", sp.simplify(1 / a_ * 1 / b_ - 1 / (a_ + b_)) != 0)
# Q3a
t = sp.symbols("t", real=True)
M3 = sp.Matrix([[t, 0, 1], [0, 2 * t, 0], [1, 0, t]])
ev3 = M3.eigenvals()
ok("Q3a eigenvalues a-1,a+1,2a", ev3 == {t - 1: 1, t + 1: 1, 2 * t: 1})
five = sorted(M3.subs(t, 5).eigenvals().keys())
same(3, "א", [five[0]])


def cls(v):
    e = [v - 1, v + 1, 2 * v]
    return ("PD" if all(z > 0 for z in e) else "PSD" if all(z >= 0 for z in e) else "ND" if all(z < 0 for z in e)
            else "NSD" if all(z <= 0 for z in e) else "none")


grid = [sp.Rational(k, 4) for k in range(-20, 21)]
psd = lambda v: cls(v) in ("PD", "PSD")
ok("Q3a PSD exactly for a>=1 (grid); a>=-1, a>=0 are wrong; a>1 misses a=1",
   all(psd(v) == (v >= 1) for v in grid) and not psd(sp.Rational(-1)) and not psd(sp.Integer(0)) and psd(sp.Integer(1)))
ok("Q3a neither PSD nor NSD exactly for -1<a<1 (grid)",
   all(((not psd(v)) and cls(v) not in ("ND", "NSD")) == (-1 < v < 1) for v in grid))
# Q3b
C = sp.Matrix([[1, 3], [3, 8]])
f = lambda p, q: (sp.Matrix([p, q]).T * C * sp.Matrix([p, q]))[0]
same(3, "ב", [f(1, 1), f(-3, 1)])
tt = sp.symbols("tt", real=True)
ok("Q3b t^2+6t+8 < 0 exactly on (-4,-2)",
   sp.solve_univariate_inequality(tt ** 2 + 6 * tt + 8 < 0, tt, relational=False) == sp.Interval.open(-4, -2))
# Q4a
x = Permutation(0, 1, 2, 3)
y = Permutation(0, 1)
same(4, "א", [(y ** -1 * x * y).order()])
S4 = list(__import__("sympy.combinatorics", fromlist=["SymmetricGroup"]).SymmetricGroup(4).elements)
ok("Q4a (y^-1 x y)^k = y^-1 x^k y for all x,y in S4, k=1..5",
   all(((y_ ** -1 * x_ * y_) ** k) == (y_ ** -1 * x_ ** k * y_) for x_ in S4 for y_ in S4 for k in range(1, 6)))
bad_id = sum(1 for x_ in S4 for y_ in S4 if (y_ ** -1 * x_ * y_) ** 2 != (y_ ** -2) * x_ ** 2 * y_ ** 2)
ok("Q4a wrong distractor (y^-k x^k y^k) fails in S4", bad_id > 0, f"{bad_id} failures")
ok("Q4a wrong distractor (y^-1 x y^k) fails in S4 for k=2", any((y_ ** -1 * x_ * y_) ** 2 != y_ ** -1 * x_ * y_ ** 2 for x_ in S4 for y_ in S4))
ok("Q4a y^-1 e y = e, not y, for y != e", all(y_ ** -1 * Permutation(3) * y_ == Permutation(3) for y_ in S4))
# Q4b: bug line y^-1 x (y y^-1) = y^-1 x y is false when y != e
ok("Q4b y^-1 x (y y^-1) = y^-1 x, differs from y^-1 x y for y != e (S4)",
   any(y_ ** -1 * x_ * (y_ * y_ ** -1) != y_ ** -1 * x_ * y_ for x_ in S4 for y_ in S4))
# Q4c
sc = solve_congruence((3, 4), (4, 5), (2, 7))
tot = 3 * 35 * 3 + 4 * 28 * 2 + 2 * 20 * 6
same(4, "ג", [4 * 5 * 7, [k for k in range(4) if (35 * k) % 4 == 1][0], [k for k in range(7) if (20 * k) % 7 == 1][0], tot, sc[0]])
# Q5a
A5 = sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 2]])
ok("Q5a eigenvalues 2 (x2), 0; (1,-1,0) is the 0-eigenvector; (1,1,0), (0,0,1) eigenvalue 2; (1,0,0) not an eigenvector",
   A5.eigenvals() == {2: 2, 0: 1} and A5 * sp.Matrix([1, -1, 0]) == sp.zeros(3, 1)
   and A5 * sp.Matrix([1, 1, 0]) == 2 * sp.Matrix([1, 1, 0]) and A5 * sp.Matrix([0, 0, 1]) == 2 * sp.Matrix([0, 0, 1])
   and (A5 * sp.Matrix([1, 0, 0]))[1] == 1 and (A5 * sp.Matrix([1, 0, 0]))[0] != 0 and (A5 * sp.Matrix([1, 0, 0]))[1] != 0)
same(5, "א", [max(A5.eigenvals().keys()), sp.Matrix([1, 1, 0]).norm()])
# Q5b
same(5, "ב", [sp.Rational(3, 9)])
xs, ys, zs = sp.symbols("xs ys zs", positive=True)
ok("Q5b (sqrt x+sqrt y+sqrt z)^2 - (x+y+z) = 2(sqrt xy + sqrt yz + sqrt xz) > 0",
   sp.simplify(sp.expand((sp.sqrt(xs) + sp.sqrt(ys) + sp.sqrt(zs)) ** 2 - (xs + ys + zs))
               - 2 * (sp.sqrt(xs * ys) + sp.sqrt(ys * zs) + sp.sqrt(xs * zs))) == 0)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
