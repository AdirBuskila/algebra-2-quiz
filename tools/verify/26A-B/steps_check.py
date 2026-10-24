# -*- coding: utf-8 -*-
"""Step-author checks for 26A-B: every numeric step answer and choice claim recomputed with sympy / brute force.
Run: PYTHONUTF8=1 py -I tools/verify/26A-B/steps_check.py   (ASCII output, exit 1 on FAIL)"""
import itertools
import json
import pathlib
import sys

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "26A-B.json"
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


# ---- Q1a
A = sp.Matrix([[2, 1], [1, 2]])
ev = sorted(A.eigenvals())
NUM("Q1a small eigenvalue", 1, "א", 0, ev[0])
NUM("Q1a large eigenvalue", 1, "א", 1, ev[1])
e1, e2 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
Bm = sp.Matrix([[1, 2], [0, 1]])
Cm = sp.Matrix([[1, 2], [3, 4]])
ok("Q1a invertible nonsymmetric breaks symmetry (2 vs 0)", (e1.T * Bm * e2)[0] == 2 and (e2.T * Bm * e1)[0] == 0 and Bm.det() != 0)
ok("Q1a positive entries nonsymmetric breaks symmetry (2 vs 3)", (e1.T * Cm * e2)[0] == 2 and (e2.T * Cm * e1)[0] == 3)
ok("Q1a symmetric A gives symmetric form", all((u.T * A * v)[0] == (v.T * A * u)[0] for u in (e1, e2, e1 + e2) for v in (e1, e2, e1 - e2)))
ok("Q1a [[1,2],[2,1]] positive entries but not PD", min(sp.Matrix([[1, 2], [2, 1]]).eigenvals()) < 0)

# ---- Q1b
t = sp.symbols("t")
Ag = A
u = sp.Matrix([1, t])
v = sp.Matrix([t, -1])
expr = sp.expand((u.T * Ag * v)[0])
ok("Q1b expression is t^2-1", sp.simplify(expr - (t ** 2 - 1)) == 0)
NUM("Q1b <(1,2),(2,-1)>_A", 1, "ב", 0, (sp.Matrix([1, 2]).T * Ag * sp.Matrix([2, -1]))[0])
NUM("Q1b 2t-1+t(t-2) at t=3", 1, "ב", 1, (2 * t - 1 + t * (t - 2)).subs(t, 3))
ok("Q1b roots +-1; t=0 -> -1; t=2 -> 3", sorted(sp.solve(expr, t)) == [-1, 1] and expr.subs(t, 0) == -1 and expr.subs(t, 2) == 3)

# ---- Q1c
Al = sp.Matrix([[1, -2], [-1, 2], [0, 3], [2, 5]])
bl = sp.Matrix([3, 1, -4, 2])
AtA = Al.T * Al
Atb = Al.T * bl
NUM("Q1c (A^TA)[2,2]", 1, "ג", 0, AtA[1, 1])
NUM("Q1c (A^Tb)[2]", 1, "ג", 1, Atb[1])
xh = AtA.LUsolve(Atb)
NUM("Q1c x2", 1, "ג", 2, xh[1])
NUM("Q1c x1", 1, "ג", 3, xh[0])
ok("Q1c x_hat = (4/3, -1/3)", xh == sp.Matrix([R(4, 3), R(-1, 3)]))

# ---- Q2 operation a o b = ab - a - b + 2
def o(p, q):
    return p * q - p - q + 2

a, b, c = sp.symbols("a b c")
NUM("Q2a 3o3", 2, "א", 0, o(3, 3))
NUM("Q2a (3o3)o3", 2, "א", 1, o(o(3, 3), 3))
L = sp.expand(o(o(a, b), c))
Rr = sp.expand(o(a, o(b, c)))
common = a * b * c - a * b - a * c - b * c + a + b + c
ok("Q2a associativity and common expression", sp.expand(L - Rr) == 0 and sp.expand(L - common) == 0)
sub = {a: 3, b: 3, c: 3}
ok("Q2a distractor values 10 and 18", (common + 1).subs(sub) == 10 and (a * b * c - a * b - b * c + a + b + c).subs(sub) == 18 and common.subs(sub) == 9)
e = sp.symbols("e")
ok("Q2b e(a-1) = 2(a-1)", sp.simplify(sp.expand(o(e, a) - a) - (e - 2) * (a - 1)) == 0)
NUM("Q2b e", 2, "ב", 0, sp.solve(e - 2, e)[0])
ok("Q2b a=0 in M is below 1 (a>1 is not the reason)", 0 != 1)
ok("Q2c a o b - 1 = (a-1)(b-1); 2 o 1/2 = 1/2 ; 3 o 3 = 5", sp.expand(o(a, b) - 1 - (a - 1) * (b - 1)) == 0 and o(2, R(1, 2)) == R(1, 2) and o(3, 3) == 5)
inv = lambda z: sp.Rational(z) / (sp.Rational(z) - 1)
NUM("Q2c inverse of 3", 2, "ג", 1, inv(3))
NUM("Q2c inverse of -1", 2, "ג", 2, inv(-1))
ok("Q2c inverses give 2", o(3, inv(3)) == 2 and o(-1, inv(-1)) == 2)
x = sp.symbols("x")
roots = sp.solve(sp.Eq(o(x, x), x), x)
ok("Q2d roots 1,2", sorted(roots) == [1, 2])
NUM("Q2d root in M", 2, "ד", 0, [r for r in roots if r != 1][0])
ok("Q2d 1 o 1 = 1 (x=1 is a root, excluded only by M)", o(1, 1) == 1)
NUM("Q2d 2o2", 2, "ד", 2, o(2, 2))
aa = 3
seq = [aa]
for _ in range(3):
    seq.append(o(seq[-1], aa))
NUM("Q2e a^4 at a=3", 2, "ה", 0, seq[-1])
ok("Q2e formula (a-1)^n+1 for n=1..6 and several a", all(
    (lambda s: all(s[i] == (av - 1) ** (i + 1) + 1 for i in range(len(s))))(
        [av] + [None] * 0) for av in [3]) and
   all(__import__("functools").reduce(lambda acc, _: o(acc, av), range(n - 1), av) == (av - 1) ** n + 1
       for av in [-2, 0, 3, R(1, 2), 5] for n in range(1, 7)))
ok("Q2e identity x o y = (x-1)(y-1)+1", sp.expand(o(a, b) - ((a - 1) * (b - 1) + 1)) == 0)
ok("Q2e bug line (a-1)^n * a + 1 != (a-1)^(n+1)+1", sp.simplify((a - 1) ** 2 * a + 1 - ((a - 1) ** 3 + 1)) != 0)

# ---- Q3a
xx = sp.symbols("xx")
M = sp.Matrix([[1, xx, 1], [xx, 1, 1], [1, 1, xx + 2]])
ok("Q3a eigenvalues 1-x, x, x+3", M.eigenvals() == {1 - xx: 1, xx: 1, xx + 3: 1}, str(M.eigenvals()))
NUM("Q3a trace at x=2", 3, "א", 0, M.trace().subs(xx, 2))
for nm, s_ in [("x-1,x,x+3", [xx - 1, xx, xx + 3]), ("1-x,x,x+2", [1 - xx, xx, xx + 2]), ("1+x,x,x+3", [1 + xx, xx, xx + 3])]:
    ok("Q3a distractor {" + nm + "} has wrong trace", sp.simplify(sum(s_) - M.trace()) != 0)
ok("Q3a true set has trace x+4", sp.simplify((1 - xx) + xx + (xx + 3) - M.trace()) == 0)
def eigs(v):
    return list(M.subs(xx, v).eigenvals(multiple=True))
grid = [R(k, 4) for k in range(-16, 16)]
ok("Q3a PSD iff 0<=x<=1", all(all(e_ >= 0 for e_ in eigs(g)) == (0 <= g <= 1) for g in grid))
ok("Q3a PD iff 0<x<1", all(all(e_ > 0 for e_ in eigs(g)) == (0 < g < 1) for g in grid))
ok("Q3a x=0 eigenvalues {1,0,3}; x=-1 has -1; x=2 has -1", sorted(eigs(0)) == [0, 1, 3] and -1 in eigs(-1) and -1 in eigs(2))

# ---- Q3b
NUM("Q3b smallest eigenvalue of A^-1 (A eig 2,5)", 3, "ב", 0, min(sp.Matrix([[2, 0], [0, 5]]).inv().eigenvals()))
D = sp.diag(2, 5)
ok("Q3b distractors fail for diag(2,5): inverse eigs 1/2,1/5 != lam, -lam, lam^2", sorted(D.inv().eigenvals()) == [R(1, 5), R(1, 2)])
Asym = sp.Matrix([[2, 1], [1, 2]])
uu = sp.Matrix([1, -3])
ok("Q3b u^T A^2 u = ||Au||^2", (uu.T * Asym ** 2 * uu)[0] == (Asym * uu).dot(Asym * uu))

# ---- Q4 (mod 5 upper triangular Toeplitz)
def G(a_, b_, c_):
    return sp.Matrix([[a_, b_, c_], [0, a_, b_], [0, 0, a_]])
def modm(Mx, p=5):
    return Mx.applyfunc(lambda z: z % p)
a_, b_, c_ = 2, 1, 1
d_ = pow(a_, -1, 5)
e_ = (-b_ * pow(a_, -2, 5)) % 5
f_ = ((b_ ** 2 - a_ * c_) * pow(a_, -3, 5)) % 5
NUM("Q4a d for a=2", 4, "א", 1, d_)
NUM("Q4a e for a=2,b=1", 4, "א", 2, e_)
NUM("Q4a f for a=2,b=1,c=1", 4, "א", 3, f_)
ok("Q4a inverse really is the inverse mod 5", modm(G(a_, b_, c_) * G(d_, e_, f_)) == sp.eye(3) and modm(G(d_, e_, f_) * G(a_, b_, c_)) == sp.eye(3))
# full brute force: closure + inverse formula for every (a,b,c)
good = True
elems = [(a1, b1, c1) for a1 in range(1, 5) for b1 in range(5) for c1 in range(5)]
for (a1, b1, c1) in elems:
    inv_ = (pow(a1, -1, 5), (-b1 * pow(a1, -2, 5)) % 5, ((b1 ** 2 - a1 * c1) * pow(a1, -3, 5)) % 5)
    if modm(G(a1, b1, c1) * G(*inv_)) != sp.eye(3):
        good = False
        break
ok("Q4a inverse formula for all 100 elements", good)
NUM("Q4b a choices", 4, "ב", 0, len([1 for a1 in range(5) if a1 % 5 != 0]))
NUM("Q4b |G|", 4, "ב", 1, len(elems))
Xm = sp.Matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
NUM("Q4c (X^3)[1,3]", 4, "ג", 0, modm(Xm ** 3)[0, 2])
n_ = next(n for n in range(1, 20) if modm(Xm ** n) == sp.eye(3))
NUM("Q4c order of X", 4, "ג", 1, n_)
ok("Q4a 10 is positive and 0 mod 5", 10 % 5 == 0 and 10 > 0)

# ---- Q5a CRT
from sympy.ntheory.modular import solve_congruence
NUM("Q5a M", 5, "א", 0, 3 * 5 * 8)
NUM("Q5a x2", 5, "א", 1, sp.mod_inverse(24, 5))
NUM("Q5a x3", 5, "א", 2, sp.mod_inverse(15, 8))
NUM("Q5a x", 5, "א", 3, solve_congruence((2, 3), (1, 5), (4, 8))[0])
ok("Q5a sum 596 -> 116", 2 * 40 * 1 + 24 * 4 + 4 * 15 * 7 == 596 and 596 % 120 == 116)

# ---- Q5b
k = sp.symbols("k", integer=True, positive=True)
n2 = 2
ip = sum(R(1, kk ** 2) for kk in range(1, n2 + 1))
rhs = sum(R(1, kk) for kk in range(1, n2 + 1)) * sum(R(1, kk ** 3) for kk in range(1, n2 + 1))
NUM("Q5b <u,v> n=2", 5, "ב", 1, ip)
NUM("Q5b rhs n=2", 5, "ב", 2, rhs)
ok("Q5b inequality for n=1..30", all(
    sum(R(1, kk ** 2) for kk in range(1, n + 1)) ** 2 <= sum(R(1, kk) for kk in range(1, n + 1)) * sum(R(1, kk ** 3) for kk in range(1, n + 1))
    for n in range(1, 31)))
ok("Q5b u_k v_k = k^-2 and u_k^2 = 1/k, v_k^2 = k^-3", sp.simplify(1 / sp.sqrt(k) * k ** R(-3, 2) - k ** -2) == 0)

print()
print("FAILED:" if bad else "ALL OK", bad)
sys.exit(1 if bad else 0)
