# -*- coding: utf-8 -*-
"""sympy / brute-force check of every machine-checkable step value in tools/raw/23A-S.json.
Run: PYTHONUTF8=1 py -I tools/verify/23A-S/steps_check.py   (ASCII output, exit 1 on mismatch)"""
import json
import pathlib
import sys

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "23A-S.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
bad = []
AL, BE = "א", "ב"
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


# ---- Q1a
a = sp.symbols("a", real=True)
M = sp.Matrix([[a, 2, 0], [a + 1, a, 0], [0, 0, a]])
numeq(1, AL, 0, sp.solve(sp.Eq(M[0, 1], M[1, 0]), a)[0])
ev = M.subs(a, 1).eigenvals()
numeq(1, AL, 1, max(ev))
numeq(1, AL, 2, min(ev))
ok("Q1a eigenvalues {1,3,-1}: indefinite", set(ev) == {1, 3, -1})
# ---- Q1b
nv2 = sp.symbols("nv2")
v2 = sp.solve(sp.Eq(16 + 36, 2 * 9 + 2 * nv2), nv2)[0]
numeq(1, BE, 1, 16 + 36)
numeq(1, BE, 2, v2)
numeq(1, BE, 3, R(16 - 36, 4))
# parallelogram law options on u=(1,0), v=(0,1): LHS=4
u, v = sp.Matrix([1, 0]), sp.Matrix([0, 1])
lhs = (u + v).dot(u + v) + (u - v).dot(u - v)
vals = [2 * 1 + 2 * 1, 2 * 1 - 2 * 1, 1 + 1, 4 * u.dot(v)]
ok("Q1b step0 only option a equals LHS=4", [x == lhs for x in vals] == [True, False, False, False])
# ---- Q2a
pts = [(5, 7), (3, 5), (1, 4), (-2, 0), (-3, 2)]
A = sp.Matrix([[x, 1] for x, _ in pts]); b = sp.Matrix([y for _, y in pts])
numeq(2, AL, 0, (A.T * A)[0, 0])
numeq(2, AL, 1, (A.T * b)[0])
sol = (A.T * A).solve(A.T * b)
numeq(2, AL, 2, sol[0])
numeq(2, AL, 3, sol[1])
# ---- Q2b: random orthogonal symmetric Q (reflection / diag +-1 conjugated)
import random
random.seed(1)
for _ in range(5):
    w = sp.Matrix([random.randint(-3, 3) or 1 for _ in range(3)])
    Q = sp.eye(3) - 2 * w * w.T / (w.T * w)[0]
    P = sp.eye(3) + Q
    assert Q.T == Q and Q.T * Q == sp.eye(3)
    assert Q * Q == sp.eye(3) and P * P == 2 * P and (sp.eye(3) + Q) ** 2 != sp.eye(3) + Q + Q * Q
ok("Q2b Q^2=I, P^2=2P, bug (I+Q)^2 != I+Q+Q^2", True)
Qm = -sp.eye(2)
ok("Q2b distractors: Q=-I has Q^2=I != Q, !=0, !=2I", Qm ** 2 == sp.eye(2) and Qm ** 2 != Qm and Qm ** 2 != sp.zeros(2) and Qm ** 2 != 2 * sp.eye(2))
correct_is(2, BE, 0, 0)
# ---- Q3a
Am = sp.Matrix([[1, 1, 0], [0, 0, 1], [1, -1, 1]])
c1, c2, c3 = Am[:, 0], Am[:, 1], Am[:, 2]
Qm_, Rm = Am.QRdecomposition()
numeq(3, AL, 0, c2.dot(c1))
numeq(3, AL, 1, Rm[0, 0])
numeq(3, AL, 2, Rm[0, 2])
numeq(3, AL, 3, Rm[1, 2])
ok("Q3a sympy QR matches the solution", Qm_ * Rm == Am and Rm[2, 2] == 1 and Rm[1, 1] == sp.sqrt(2))
# ---- Q3b (student solution, rechecked)
x = sp.symbols("x")
numeq(3, BE, 1, sp.integrate(x ** 6, (x, 0, 1)))
ok("Q3b ||x^3||^2 = 1/7 not 1/6", sp.integrate(x ** 6, (x, 0, 1)) == R(1, 7) != R(1, 6))
for f in [x, x ** 2 + 1, sp.exp(x), sp.cos(3 * x), x ** 3]:
    lhs = sp.integrate(x ** 3 * f, (x, 0, 1)) ** 2
    rhs = R(1, 7) * sp.integrate(f ** 2, (x, 0, 1))
    assert sp.N(lhs - rhs) <= 1e-12, f
ok("Q3b inequality holds on test functions (equality for f=x^3)", sp.simplify(sp.integrate(x ** 6, (x, 0, 1)) ** 2 - R(1, 7) * sp.integrate(x ** 6, (x, 0, 1))) == 0)
# ---- Q4 group G
a1, b1, c1_, a2, b2, c2_ = sp.symbols("a1 b1 c1 a2 b2 c2")


def Aabc(p, q, r):
    return sp.Matrix([[1, p, q], [0, 1, r], [0, 0, 1]])


prod = Aabc(a1, b1, c1_) * Aabc(a2, b2, c2_)
ok("Q4 product = A(a1+a2, b1+b2+a1c2, c1+c2)", prod == Aabc(a1 + a2, b1 + b2 + a1 * c2_, c1_ + c2_))
numeq(4, None, 0, (Aabc(1, 2, 3) * Aabc(4, 5, 6))[0, 2])
inv = Aabc(1, 2, 3).inv()
numeq(4, None, 1, inv[0, 2])
p, q, r = sp.symbols("p q r")
ok("Q4 inverse A(-a, ac-b, -c) both sides", Aabc(p, q, r) * Aabc(-p, p * r - q, -r) == sp.eye(3) and Aabc(-p, p * r - q, -r) * Aabc(p, q, r) == sp.eye(3))
ok("Q4 bug y=b+ac is not an inverse", Aabc(p, q, r) * Aabc(-p, q + p * r, -r) != sp.eye(3))
# associativity (symbolic)
a3, b3, c3_ = sp.symbols("a3 b3 c3")
ok("Q4 associativity", sp.expand((Aabc(a1, b1, c1_) * Aabc(a2, b2, c2_)) * Aabc(a3, b3, c3_) - Aabc(a1, b1, c1_) * (Aabc(a2, b2, c2_) * Aabc(a3, b3, c3_))) == sp.zeros(3))
# ---- Q5a CRT
numeq(5, AL, 0, 3 % 2)
numeq(5, AL, 1, sp.mod_inverse(14, 5))
numeq(5, AL, 2, sp.mod_inverse(10, 7))
from sympy.ntheory.modular import solve_congruence
xs, mod = solve_congruence((2, 5), (3, 2), (4, 7))
numeq(5, AL, 3, xs)
ok("Q5a mod 70", mod == 70)
# ---- Q5b projection
A1 = sp.Matrix([[1, 1], [0, 0]]); A2 = sp.Matrix([[1, 3], [1, 1]]); C = sp.Matrix([[1, 2], [3, 0]])


def ip(X, Y):
    return (Y.T * X).trace()


B1 = A1
B2 = A2 - ip(A2, B1) / ip(B1, B1) * B1
numeq(5, BE, 0, ip(A2, B1))
numeq(5, BE, 1, ip(B2, B2))
numeq(5, BE, 2, ip(C, B2))
Pc = ip(C, B1) / ip(B1, B1) * B1 + ip(C, B2) / ip(B2, B2) * B2
numeq(5, BE, 3, Pc[0, 1])
ok("Q5b P(C) residual orthogonal to A1, A2", ip(C - Pc, A1) == 0 and ip(C - Pc, A2) == 0)

print("%d failures" % len(bad))
sys.exit(1 if bad else 0)
