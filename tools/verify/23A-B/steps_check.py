# -*- coding: utf-8 -*-
"""Machine check of every numeric/choice step value of sitting 23A-B (rubric/steps phase).
Run: PYTHONUTF8=1 py -I tools/verify/23A-B/steps_check.py   (after tools/gen/gen_23A-B.py). ASCII output, exit 1 on mismatch."""
import itertools
import json
import pathlib
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "23A-B.json").read_text(encoding="utf-8"))
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
x = sp.symbols("x", real=True)

# Q1a
A = sp.Matrix([[1, -2], [-1, 2], [0, 3], [2, 5]])
b = sp.Matrix([3, 1, -4, 2])
sol = (A.T * A).LUsolve(A.T * b)
same("1a", numeric_answers(1, "א"), [(A.T * A)[1, 1], (A.T * b)[1], sol[1], sol[0]])

# Q1b
n = 3
lhs = sum(sp.sqrt(sp.log(k) * sp.log(n - k + 1)) for k in range(1, n + 1))
same("1b", numeric_answers(1, "ב"), [sp.N(lhs), sp.N(sp.log(sp.factorial(3)))])
# choice distractors: the dot product with each option differs from the sum (n=3, and n=5 so no accidental tie)
for nn in (3, 5):
    L = sum(sp.sqrt(sp.log(k) * sp.log(nn - k + 1)) for k in range(1, nn + 1))
    u = [sp.sqrt(sp.log(k)) for k in range(1, nn + 1)]
    rev = u[::-1]
    opt = {"correct": sum(a * c for a, c in zip(u, rev)),
           "v=u": sum(a * a for a in u),
           "ln vs ln": sum(sp.log(k) * sp.log(nn - k + 1) for k in range(1, nn + 1)),
           "v=ones": sum(u)}
    ok(f"1b option correct n={nn}", abs(sp.N(opt["correct"] - L)) < 1e-12)
    for k_, v_ in opt.items():
        if k_ != "correct":
            ok(f"1b distractor {k_} n={nn} differs", abs(sp.N(v_ - L)) > 1e-6)

# Q2a: projection of x^2 onto Sp{1,|x|} on [-1,1]; integrals of even functions = 2 * int_0^1 (|x| = x there)
ip = lambda f, g: 2 * sp.integrate(f * g, (x, 0, 1))  # valid for even integrands (all ours are)
c0 = ip(sp.Integer(1), sp.Integer(1))
c1 = ip(x, sp.Integer(1)) / c0
nrm = ip(x - c1, x - c1)
proj_c = ip(x ** 2, sp.Integer(1)) / c0 + ip(x ** 2, x - c1) / nrm * (-c1)
same("2a", numeric_answers(2, "א"), [c0, c1, nrm, proj_c])
# full check that proj = |x| - 1/6: residual orthogonal to 1 and |x|
pr = ip(x ** 2, sp.Integer(1)) / c0 + ip(x ** 2, x - c1) / nrm * (x - c1)
ok("2a proj = x - 1/6 (x>=0)", sp.simplify(pr - (x - R(1, 6))) == 0)
ok("2a residual orthogonal", ip(x ** 2 - pr, sp.Integer(1)) == 0 and ip(x ** 2 - pr, x) == 0)

# Q2b: brute force |H|
p = 5
cnt_ab = sum(1 for a in range(p) for bb in range(p) if (a * bb) % p != 0)
H = sum(1 for a in range(p) for bb in range(p) for c in range(p) if (a * bb) % p != 0)
same("2b", numeric_answers(2, "ב"), [p, cnt_ab, H])

# Q3a
M = sp.Matrix([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
ev = M.eigenvects()
dim2 = [len(v) for e, m, v in ev if e == 2][0]
v2 = sp.Matrix([-1, 1, 0])
z = sp.symbols("z")
zsol = sp.solve(list((M - 2 * sp.eye(3)) * sp.Matrix([1, 1, z])), z)[z]
ok("3a (1,1,z) orthogonal to (-1,1,0)", v2.dot(sp.Matrix([1, 1, zsol])) == 0)
ok("3a (1,1,z) in eigenspace lam=2", (M * sp.Matrix([1, 1, zsol]) - 2 * sp.Matrix([1, 1, zsol])) == sp.zeros(3, 1))
lam111 = (M * sp.Matrix([1, 1, 1]))[0]
same("3a", numeric_answers(3, "א"), [M.det(), lam111, dim2, zsol])

# Q3b: polarization identity, numeric example and symbolic expansion
u = sp.Matrix([1, 2]); v = sp.Matrix([3, -1])
val = R(1, 4) * ((u + v).dot(u + v) - (u - v).dot(u - v))
same("3b", numeric_answers(3, "ב"), [val])
ok("3b = u.v", val == u.dot(v))
uu, vv, uv = sp.symbols("uu vv uv")
ok("3b difference = 4 uv", sp.expand((uu + 2 * uv + vv) - (uu - 2 * uv + vv)) == 4 * uv)

# Q4a: brute force in every exponent-2 group Z2^k (k=1..3): c = (a*b)*a = b; distractor x*x=x fails
for k in (1, 2, 3):
    els = list(itertools.product((0, 1), repeat=k))
    mul = lambda s, t: tuple((i + j) % 2 for i, j in zip(s, t))
    e = tuple([0] * k)
    ok(f"4a Z2^{k} c=b", all(mul(mul(mul(a, bb), a), bb) == e and mul(mul(a, bb), a) == bb for a in els for bb in els))
    ok(f"4a Z2^{k} x*x=e", all(mul(t, t) == e for t in els))
els = list(itertools.product((0, 1), repeat=2))
ok("4a distractor x*x=x fails", any(tuple((i + j) % 2 for i, j in zip(t, t)) != t for t in els))

# Q4b
B = sp.Matrix([[4, 5], [5, 6]])
t = sp.symbols("t")
roots = sorted(sp.solve(2 * t ** 2 + 5 * t + 3, t))
a_, b_ = sp.symbols("a b")
form = sp.expand((sp.Matrix([[a_, b_]]) * B * sp.Matrix([a_, b_]))[0])
ok("4b form", form == 4 * a_ ** 2 + 10 * a_ * b_ + 6 * b_ ** 2)
same("4b", numeric_answers(4, "ב"), [B.det(), roots[0], form.subs({a_: -5, b_: 4})])
ok("4b interval is between roots", roots == [R(-3, 2), -1] and (2 * R(-5, 4) ** 2 + 5 * R(-5, 4) + 3) < 0)
f = lambda tv: 2 * tv ** 2 + 5 * tv + 3
ok("4b distractor t<-1.5 or t>-1 fails at t=-2 and t=0", f(-2) >= 0 and f(0) >= 0)
ok("4b distractor t>0 fails at t=1", f(1) >= 0)
ok("4b distractor (-1,1.5) fails at t=0", f(0) >= 0)

# Q5a
A5 = sp.Matrix([[1, 0], [0, 3], [0, 4]])
W = A5 * A5.T
eigs = sorted([k for k in W.eigenvals()], reverse=True)
ok("5a eigenvalues of AA^T", eigs == [25, 1, 0], str(eigs))
ok("5a A^T A is 2x2 and AA^T is 3x3", (A5.T * A5).shape == (2, 2) and W.shape == (3, 3))
u1 = A5 * sp.Matrix([0, 1]) / 5
same("5a", numeric_answers(5, "א"), [eigs[0], sp.sqrt(eigs[1]), u1[2]])
ok("5a U Sigma V^T = A", (sp.Matrix([[0, 1, 0], [R(3, 5), 0, R(-4, 5)], [R(4, 5), 0, R(3, 5)]]) * sp.Matrix([[5, 0], [0, 1], [0, 0]]) * sp.Matrix([[0, 1], [1, 0]]).T) == A5)

# Q5b
sol, mod = sp.ntheory.modular.crt([5, 7, 4], [4, 3, 2])
m1, m2, m3 = 5, 7, 4
M1, M2, M3 = 140 // 5, 140 // 7, 140 // 4
x1, x2, x3 = sp.mod_inverse(M1, 5), sp.mod_inverse(M2, 7), sp.mod_inverse(M3, 4)
total = 4 * M1 * x1 + 3 * M2 * x2 + 2 * M3 * x3
ok("5b total 794", total == 794)
same("5b", numeric_answers(5, "ב"), [M1, x1, x2, sol])
ok("5b solution satisfies", sol % 5 == 4 and sol % 7 == 3 and sol % 4 == 2 and (M3, x3) == (35, 3))

print("ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
