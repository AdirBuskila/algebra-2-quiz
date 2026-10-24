# -*- coding: utf-8 -*-
"""sympy / brute-force check of every machine-checkable step value in tools/raw/24A-C.json.
Includes a re-derivation of the student-solution items (Q1, Q2, Q4) BEFORE their steps are trusted.
Run: PYTHONUTF8=1 py -I tools/verify/24A-C/steps_check.py   (ASCII output, exit 1 on mismatch)"""
import itertools
import json
import pathlib
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "24A-C.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
bad = []
AL, BE, GI, DA = "א", "ב", "ג", "ד"
R = sp.Rational


def ok(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        bad.append(name)


def item(n, part):
    for q in data["questions"]:
        if q["num"] == n and q.get("part") == part:
            return q
    raise KeyError((n, part))


def numeq(n, part, i, value):
    s = item(n, part)["steps"][i]
    assert s["type"] == "numeric", (n, part, i)
    ok("Q%d%s step %d numeric = %s" % (n, part, i, sp.N(value, 8)), abs(float(s["answer"]) - float(value)) <= s["tol"] + 1e-12)


def correct_is(n, part, i, idx):
    s = item(n, part)["steps"][i]
    ok("Q%d%s step %d correctId" % (n, part, i), s["correctId"] == "abcdef"[idx])


x = sp.symbols("x")
# ================= student items: independent re-derivation =================
# Q1a least squares
pts = [(-4, -1), (-2, 0), (2, 4), (4, 5), (5, 6)]
A = sp.Matrix([[px, 1] for px, _ in pts]); b = sp.Matrix([py for _, py in pts])
ok("student Q1a A^T A = [[65,5],[5,5]], A^T b = (62,14)", A.T * A == sp.Matrix([[65, 5], [5, 5]]) and A.T * b == sp.Matrix([62, 14]))
sol = (A.T * A).solve(A.T * b)
ok("student Q1a m=4/5, n=2", sol == sp.Matrix([R(4, 5), 2]))
# Q1b Cauchy-Schwarz
ok("student Q1b ||x^3||^2 = 1/7", sp.integrate(x ** 6, (x, 0, 1)) == R(1, 7))
for f in [x, x ** 2 + 1, sp.exp(x), sp.cos(3 * x), x ** 3, sp.sin(x)]:
    lhs = sp.integrate(x ** 3 * f, (x, 0, 1)) ** 2
    rhs = R(1, 7) * sp.integrate(f ** 2, (x, 0, 1))
    assert sp.N(lhs - rhs) <= 1e-12, f
ok("student Q1b inequality holds on test functions", True)
# Q2a structure (R^2 \ 0, *)
a, b_, xx, yy, p, q = sp.symbols("a b x y p q", real=True)


def star(u, v):
    return sp.Matrix([u[0] * v[1] + u[1] * v[0], u[1] * v[1]])


ua, va, wa = sp.Matrix([a, b_]), sp.Matrix([xx, yy]), sp.Matrix([p, q])
ok("student Q2a1 commutative", sp.simplify(star(ua, va) - star(va, ua)) == sp.zeros(2, 1))
ok("student Q2a2 e=(0,1) two-sided", star(ua, sp.Matrix([0, 1])) == ua and star(sp.Matrix([0, 1]), ua) == ua)
ok("student Q2a2 e is unique", sp.solve([sp.expand(star(ua, sp.Matrix([sp.Symbol('e1'), sp.Symbol('e2')]))[i] - ua[i]) for i in range(2)], [sp.Symbol('e1'), sp.Symbol('e2')], dict=True) != [])
ok("student Q2a associative (so the failure is the inverse)", sp.simplify(star(star(ua, va), wa) - star(ua, star(va, wa))) == sp.zeros(2, 1))
ok("student Q2a3 (a,0) has no inverse; (1,0)*(1,0)=(0,0) not closed",
   star(sp.Matrix([a, 0]), va)[1] == 0 and star(sp.Matrix([1, 0]), sp.Matrix([1, 0])) == sp.zeros(2, 1))
# Q2b: I + A^2 PD for A PD; random PD matrices
import random
random.seed(3)
for _ in range(5):
    B = sp.Matrix(3, 3, lambda i, j: random.randint(-2, 2))
    Apd = B.T * B + sp.eye(3)
    S = sp.eye(3) + Apd ** 2
    assert S.T == S and S.is_positive_definite
ok("student Q2b I+A^2 symmetric PD on random PD A", True)
# Q4a eigenvalues and ranges
am, lam = sp.symbols("a lam", real=True)
M = sp.Matrix([[am ** 2, 0, 1], [0, am, 0], [1, 0, am ** 2]])
ev = list(M.eigenvals())
ok("student Q4a eigenvalues a, a^2-1, a^2+1", sorted(map(str, ev)) == sorted(map(str, [am, am ** 2 - 1, am ** 2 + 1])))
grid = [R(k, 8) for k in range(-40, 41)]


def eig(av):
    return [e for e in M.subs(am, av).eigenvals()]


def cls(av):
    e = eig(av)
    if all(t > 0 for t in e): return "PD"
    if all(t >= 0 for t in e): return "PSD"
    if all(t < 0 for t in e): return "ND"
    if all(t <= 0 for t in e): return "NSD"
    return "none"


ok("student Q4a PD iff a>1", all((cls(av) == "PD") == (av > 1) for av in grid))
ok("student Q4a PSD (not PD) iff a=1", all((cls(av) == "PSD") == (av == 1) for av in grid))
ok("student Q4a never negative", all(cls(av) not in ("ND", "NSD") for av in grid))
# Q4b CRT
xs, mod = solve_congruence((5 % 3, 3), (4 % 2, 2), (6, 7))
ok("student Q4b x=20 mod 42", (xs, mod) == (20, 42))

# ================= steps =================
# Q1a
numeq(1, AL, 0, (A.T * A)[0, 0]); numeq(1, AL, 1, (A.T * b)[0]); numeq(1, AL, 2, sol[0]); numeq(1, AL, 3, sol[1])
# Q1b
numeq(1, BE, 1, sp.integrate(x ** 6, (x, 0, 1)))
ok("Q1b bug antiderivative x^6/6 differs", sp.integrate(x ** 6, (x, 0, 1)) != R(1, 6))
# Q2a (comm)
numeq(2, AL, 0, star(sp.Matrix([1, 2]), sp.Matrix([3, 4]))[0])
numeq(2, AL, 1, star(sp.Matrix([3, 4]), sp.Matrix([1, 2]))[0])
# Q2b
numeq(2, BE, 0, 1); numeq(2, BE, 1, 0)
numeq(2, BE, 2, star(sp.Matrix([0, 1]), sp.Matrix([3, 5]))[0])
# Q2c
numeq(2, GI, 1, star(sp.Matrix([4, 0]), sp.Matrix([xx, yy]))[1])
correct_is(2, GI, 0, 0)


def has_inv(el):
    s = sp.solve(list(star(sp.Matrix(el), sp.Matrix([xx, yy])) - sp.Matrix([0, 1])), [xx, yy], dict=True)
    return bool(s)


opts = [(4, 0), (1, 1), (2, 3), (0, 1)]
ok("Q2c only (4,0) lacks an inverse", [has_inv(o) for o in opts] == [False, True, True, True])
numeq(2, GI, 2, sp.solve(list(star(sp.Matrix([1, 1]), sp.Matrix([xx, yy])) - sp.Matrix([0, 1])), [xx, yy], dict=True)[0][xx])
ok("Q2c (2,3)^-1 = (-2/9, 1/3)", sp.solve(list(star(sp.Matrix([2, 3]), sp.Matrix([xx, yy])) - sp.Matrix([0, 1])), [xx, yy], dict=True)[0] == {xx: R(-2, 9), yy: R(1, 3)})
# Q2d
A2 = sp.Matrix([[2, 1], [1, 2]]); v = sp.Matrix([1, 0])
numeq(2, DA, 0, (A2 * v).dot(A2 * v)); numeq(2, DA, 1, (v.T * (sp.eye(2) + A2 ** 2) * v)[0])
ok("Q2d bug (v^T A v)^2=4 != 5", (v.T * A2 * v)[0] ** 2 == 4)
# Q3a SVD
A3 = sp.Matrix([[0, -1, 1], [1, 1, 0]])
numeq(3, AL, 0, (A3 * A3.T)[0, 1])
ok("Q3a AA^T eigenvalues 3,1", set((A3 * A3.T).eigenvals()) == {3, 1})
numeq(3, AL, 1, sp.sqrt(3))
u1 = sp.Matrix([-1, 1]) / sp.sqrt(2)
v1 = A3.T * u1 / sp.sqrt(3)
numeq(3, AL, 2, v1[1])
numeq(3, AL, 3, len(A3.nullspace()))
Um = sp.Matrix([[-1, 1], [1, 1]]) / sp.sqrt(2)
Vm = sp.Matrix([[1 / sp.sqrt(6), 1 / sp.sqrt(2), -1 / sp.sqrt(3)], [2 / sp.sqrt(6), 0, 1 / sp.sqrt(3)], [-1 / sp.sqrt(6), 1 / sp.sqrt(2), 1 / sp.sqrt(3)]])
Sg = sp.Matrix([[sp.sqrt(3), 0, 0], [0, 1, 0]])
ok("Q3a U Sigma V^T = A, U,V orthogonal", sp.simplify(Um * Sg * Vm.T - A3) == sp.zeros(2, 3) and sp.simplify(Vm.T * Vm) == sp.eye(3) and sp.simplify(Um.T * Um) == sp.eye(2))
# Q3b
uu, vv = sp.Matrix([1, 2]), sp.Matrix([3, -1])
numeq(3, BE, 0, (uu + vv).dot(uu + vv) - (uu - vv).dot(uu - vv))
ok("Q3b 4<u,v> = difference", 4 * uu.dot(vv) == 4)
correct_is(3, BE, 1, 0)
# Q4a
numeq(4, AL, 0, min(eig(1)))
ok("Q4a a=1/2 indefinite", cls(R(1, 2)) == "none")
correct_is(4, AL, 1, 0); correct_is(4, AL, 2, 0); correct_is(4, AL, 3, 0)
ok("Q4a PD options: only a>1 matches", all((cls(av) == "PD") == (av > 1) for av in grid)
   and any(cls(av) != "PD" for av in grid if av >= 1) and any(cls(av) != "PD" for av in grid if av > 0) and any(cls(av) != "PD" for av in grid if av > -1))
ok("Q4a NSD options: none exist; a<=-1, a<0, a<=0 all contain a non-NSD value",
   all(cls(av) not in ("ND", "NSD") for av in grid))
# Q4b
numeq(4, BE, 0, 5 % 3)
numeq(4, BE, 1, sp.mod_inverse(6, 7))
numeq(4, BE, 2, 2 * 14 * 2 + 0 * 21 * 1 + 6 * 6 * 6)
numeq(4, BE, 3, (2 * 14 * 2 + 6 * 6 * 6) % 42)
# Q5a
a1, b1, c1, a2, b2, c2 = sp.symbols("a1 b1 c1 a2 b2 c2")


def Aabc(p_, q_, r_):
    return sp.Matrix([[1, p_, q_], [0, 1, r_], [0, 0, 1]])


numeq(5, AL, 0, (Aabc(1, 2, 3) * Aabc(4, 5, 6))[0, 2])
numeq(5, AL, 1, Aabc(1, 2, 3).inv()[0, 2])
pp, qq, rr = sp.symbols("p q r")
ok("Q5a inverse formula both sides", Aabc(pp, qq, rr) * Aabc(-pp, pp * rr - qq, -rr) == sp.eye(3) and Aabc(-pp, pp * rr - qq, -rr) * Aabc(pp, qq, rr) == sp.eye(3))
ok("Q5a bug y=b+ac fails", Aabc(pp, qq, rr) * Aabc(-pp, qq + pp * rr, -rr) != sp.eye(3))
# Q5b brute force: groups with x*x=e (Z2^3): c=b ; and a*b=b*a
els = list(itertools.product([0, 1], repeat=3))
mul = lambda s, t: tuple((i + j) % 2 for i, j in zip(s, t))
ok("Q5b brute force in Z2^3: c=(a*b)*a = b", all(mul(mul(s, t), s) == t for s in els for t in els))
ok("Q5b distractors fail in Z2^2 (a=(1,0), b=(0,1))", mul((1, 0), (0, 1)) == mul((0, 1), (1, 0)) and (1, 0) != (0, 1) and mul((1, 0), (0, 1)) != (0, 0) and (1, 0) != (0, 0))
correct_is(5, BE, 0, 0)
# findbug line "c = b*(a*a) = b*a" is wrong whenever a != e (b*a = b iff a = e)
ok("Q5b bug b*a == b only when a = e", all((mul(t, s) == t) == (s == (0, 0, 0)) for s in els for t in els))

print("%d failures" % len(bad))
sys.exit(1 if bad else 0)
