# -*- coding: utf-8 -*-
"""Machine check of every numeric/choice step value of sitting 23B-B (rubric/steps phase).
Run: PYTHONUTF8=1 py -I tools/verify/23B-B/steps_check.py   (after tools/gen/gen_23B-B.py). ASCII output, exit 1 on mismatch."""
import itertools
import json
import pathlib
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "23B-B.json").read_text(encoding="utf-8"))
byid = {(q["num"], q.get("part")): q for q in raw["questions"]}
bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def numeric_answers(num, part):
    return [s["answer"] for s in byid[(num, part)]["steps"] if s["type"] == "numeric"]


def same(name, got, want, tol=1e-3):
    ok(name, len(got) == len(want) and all(abs(float(g) - float(w)) <= tol for g, w in zip(got, want)), f"{got} vs {[float(w) for w in want]}")


R = sp.Rational
x = sp.symbols("x", positive=True)

# Q1a: least squares through (6,10),(2,2),(0,1),(-1,0),(-2,-3)
pts = [(6, 10), (2, 2), (0, 1), (-1, 0), (-2, -3)]
A = sp.Matrix([[px, 1] for px, _ in pts])
b = sp.Matrix([py for _, py in pts])
sol = (A.T * A).LUsolve(A.T * b)
same("1a", numeric_answers(1, "א"), [(A.T * A)[0, 0], (A.T * b)[0], sol[0], sol[1]])
ok("1a normal matrix", A.T * A == sp.Matrix([[45, 5], [5, 5]]) and A.T * b == sp.Matrix([70, 10]))

# Q1b
same("1b", numeric_answers(1, "ב"), [sp.integrate(1 / x ** 2, (x, 1, 2))])
f = sp.Function("f")(x)
for name, g in (("1/x", 1 / x), ("x", x), ("1", sp.Integer(1)), ("ln x", sp.log(x))):
    same_integrand = sp.simplify(f * g - f / x) == 0
    ok(f"1b g={name} {'matches' if name == '1/x' else 'differs'}", same_integrand == (name == "1/x"))
ok("1b antiderivative of 1/x^2 is -1/x, integral != ln 2", sp.integrate(1 / x ** 2, (x, 1, 2)) != sp.log(2))

# Q2a: Z5* x Z7*
ok("2a identity", all(((1 * a) % 5, (1 * c) % 7) == (a, c) for a in range(1, 5) for c in range(1, 7)))
same("2a", numeric_answers(2, "א"), [(4 * 2) % 5])
ok("2a (4,6) not neutral", (4 * 2) % 5 != 2)
ok("2a (0,0) not in G", 0 not in range(1, 5))
same("2b", numeric_answers(2, "ב"), [sp.mod_inverse(2, 5), sp.mod_inverse(3, 7)])
ok("2b (2,3)*(3,5)=(1,1)", (2 * 3) % 5 == 1 and (3 * 5) % 7 == 1)
same("2c", numeric_answers(2, "ג"), [len([a for a in range(1, 5)]), len([a for a in range(1, 7)]), 4 * 6])
from math import gcd
order = lambda g, p: next(k for k in range(1, p) if pow(g, k, p) == 1)
lcm = lambda a, c: a * c // gcd(a, c)
G = [(a, c) for a in range(1, 5) for c in range(1, 7)]
ord_pair = next(k for k in range(1, 100) if (pow(2, k, 5), pow(3, k, 7)) == (1, 1))
same("2d", numeric_answers(2, "ד"), [order(2, 5), order(3, 7), ord_pair])
ok("2d lcm", lcm(order(2, 5), order(3, 7)) == ord_pair == 12)

# Q2e / 2f: numeric examples
I2 = sp.eye(2)
B = sp.Matrix([[1, 1], [0, 1]])
v = sp.Matrix([1, 2])
same("2e", numeric_answers(2, "ה"), [(v.T * (-I2 - B.T * B) * v)[0]])
A2 = sp.diag(2, 1)
v2 = sp.Matrix([1, -1])
same("2f", numeric_answers(2, "ו"), [(v2.T * B.T * A2 * B * v2)[0]])

# Q3a
a = sp.symbols("a", real=True)
M = sp.Matrix([[a ** 2, 0, 1], [0, a, 0], [1, 0, a ** 2]])
ev = sorted(M.eigenvals().keys(), key=str)
ok("3a eigenvalues a, a^2+1, a^2-1", sorted(ev, key=str) == sorted([a, a ** 2 + 1, a ** 2 - 1], key=str), str(ev))
for name, opt in (("a,a^2+2,a^2-2", [a, a ** 2 + 2, a ** 2 - 2]), ("a^2,a+1,a-1", [a ** 2, a + 1, a - 1]), ("a,2a^2,0", [a, 2 * a ** 2, 0])):
    ok(f"3a distractor {name} wrong at a=2", sorted(e.subs(a, 2) if hasattr(e, 'subs') else e for e in opt) != sorted(M.subs(a, 2).eigenvals().keys()))
ok("3a a=2 eigenvalues 2,3,5", sorted(M.subs(a, 2).eigenvals().keys()) == [2, 3, 5])


def kind(av):
    e = list(M.subs(a, av).eigenvals().keys())
    return all(t >= 0 for t in e), all(t > 0 for t in e), all(t <= 0 for t in e), all(t < 0 for t in e)


grid = [R(k, 4) for k in range(-16, 17)]
psd = [g for g in grid if kind(g)[0]]
pd = [g for g in grid if kind(g)[1]]
nsd = [g for g in grid if kind(g)[2]]
ok("3a PSD exactly a>=1 on grid", psd == [g for g in grid if g >= 1])
ok("3a PD exactly a>1 on grid", pd == [g for g in grid if g > 1])
ok("3a NSD for no a", nsd == [])
zero_count = sum(1 for e in M.subs(a, 1).eigenvals().items() if e[0] == 0)
same("3a", numeric_answers(3, "א"), [zero_count])
ok("3a a=-1 not PSD, a=0 not NSD", not kind(-1)[0] and not kind(0)[2])

# Q3b
sol3, mod3 = sp.ntheory.modular.crt([4, 3, 5], [3, 2, 4])
M1, M2, M3 = 15, 20, 12
x1, x2, x3 = sp.mod_inverse(M1, 4), sp.mod_inverse(M2, 3), sp.mod_inverse(M3, 5)
total = 3 * M1 * x1 + 2 * M2 * x2 + 4 * M3 * x3
same("3b", numeric_answers(3, "ב"), [x1, x2, total, sol3])
ok("3b x3=3 and mod 60", x3 == 3 and mod3 == 60 and total % 60 == sol3)

# Q4a
A4 = sp.Matrix([[5, 0, 0], [0, 4, 2], [0, 2, 1]])
dim5 = len([vec for e, m, vs in A4.eigenvects() if e == 5 for vec in vs])
v1 = sp.Matrix([0, -1, 2])
v2_ = sp.Matrix([0, 2, 1])
ok("4a v1 eigen 0, v2 eigen 5", A4 * v1 == sp.zeros(3, 1) and A4 * v2_ == 5 * v2_)
same("4a", numeric_answers(4, "א"), [A4.det(), dim5, v1.dot(v2_), (v1 / v1.norm())[2]])

# Q4b: group of exponent 2 (S3 as the general-group test for the distractors)
from itertools import permutations
S3 = list(permutations(range(3)))
mul = lambda p, q: tuple(p[q[i]] for i in range(3))
inv = lambda p: tuple(sorted(range(3), key=lambda i: p[i]))
ok("4b (xy)^-1 = y^-1 x^-1 in S3", all(inv(mul(p, q)) == mul(inv(q), inv(p)) for p in S3 for q in S3))
ok("4b distractor (xy)^-1 = x^-1 y^-1 fails in S3", any(inv(mul(p, q)) != mul(inv(p), inv(q)) for p in S3 for q in S3))
ok("4b distractor (xy)^2 = x^2 y^2 fails in S3", any(mul(mul(p, q), mul(p, q)) != mul(mul(p, p), mul(q, q)) for p in S3 for q in S3))
ok("4b distractor xy=yx fails in S3", any(mul(p, q) != mul(q, p) for p in S3 for q in S3))
for k in (1, 2, 3):
    els = list(itertools.product((0, 1), repeat=k))
    mm = lambda s, t: tuple((i + j) % 2 for i, j in zip(s, t))
    ok(f"4b Z2^{k} abelian", all(mm(s, t) == mm(t, s) for s in els for t in els))

# Q4c: exponent-2 groups
for k in (1, 2, 3):
    els = list(itertools.product((0, 1), repeat=k))
    mm = lambda s, t: tuple((i + j) % 2 for i, j in zip(s, t))
    pw = lambda s, n: next(iter([s])) if False else __import__("functools").reduce(mm, [s] * n)
    ok(f"4c Z2^{k} x^3=x and y^5=y", all(pw(s, 3) == s and pw(s, 5) == s for s in els))
    e = tuple([0] * k)
    ok(f"4c Z2^{k} x != 1 in general, x^2=1", any(s != e for s in els) and all(pw(s, 2) == e for s in els))
same("4c", numeric_answers(4, "ג"), [5 % 2])

# Q5a
A5 = sp.Matrix([[-1, 3], [1, 5]])
Q, Rm = A5.QRdecomposition()
same("5a", numeric_answers(5, "א"), [Rm[0, 0], Rm[0, 1], Rm[1, 1], Q[0, 1]])
ok("5a Q R = A and Q^T A = R", sp.simplify(Q * Rm - A5) == sp.zeros(2, 2) and sp.simplify(Q.T * A5 - Rm) == sp.zeros(2, 2))

# Q5b / 5c
vv = sp.Matrix([R(3, 5), R(4, 5)])
P = vv * vv.T
same("5b", numeric_answers(5, "ב"), [P[0, 1], P.trace()])
ok("5b P^2=P and P symmetric", P * P == P and P == P.T)
u = sp.Matrix([1, 2])
w = u - P * u
same("5c", numeric_answers(5, "ג"), [w[0]])
ok("5c orthogonal", w.dot(vv) == 0)

print("ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
