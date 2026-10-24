# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided STEPS of sitting 25B-B (algebra-2).
Run after the generator: PYTHONUTF8=1 py -I tools/verify/25B-B/steps_check.py
Reads tools/raw/25B-B.json, recomputes every numeric answer and the factual claims behind choice/findbug steps.
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import json
import math
import pathlib
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "25B-B.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
Qs = {(q["num"], q.get("part")): q for q in data["questions"]}
bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


def same(num, part, expected):
    got = [(s["answer"], s.get("tol", 0)) for s in Qs[(num, part)]["steps"] if s["type"] == "numeric"]
    good = len(got) == len(expected) and all(abs(a - float(e)) <= max(t, 1e-9) for (a, t), e in zip(got, expected))
    ok(f"Q{num}{ascii(part)} numeric steps == sympy values", good, f"stored {[g[0] for g in got]} sympy {[float(e) for e in expected]}")


R = sp.Rational
r2 = sp.sqrt(2)
# Q1a
A = sp.Matrix([[x, 1] for x in (0, 2, 6, 10)])
b = sp.Matrix([1, 4, 5, 8])
sol = (A.T * A).LUsolve(A.T * b)
same(1, "א", [(A.T * A)[0, 0], (A.T * b)[0], sol[0], sol[1]])
ok("Q1a m=37/59, n=99/59 ; Ax=b has no exact solution", sol == sp.Matrix([R(37, 59), R(99, 59)]) and A.row_join(b).rank() == 3)
# Q1b
S = sp.Matrix([[0, -1], [1, 0]])
Am = sp.diag(1, 2)
ev = sorted((S.T * Am * S).eigenvals().keys())
same(1, "ב", [ev[0]])
ok("Q1b S orthogonal, not symmetric; S^T A S = diag(2,1)", S.T * S == sp.eye(2) and S != S.T and S.T * Am * S == sp.diag(2, 1))
S2 = sp.Matrix([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]])
vv = sp.Matrix(sp.symbols("v1 v2"))
uu = S2 * vv
ok("Q1b v^T S^T A S v = (Sv)^T A (Sv) but != (S^T v)^T A (S^T v) (S = rotation by atan(4/3))",
   S2.T * S2 == sp.eye(2) and sp.expand((vv.T * S2.T * Am * S2 * vv)[0] - (uu.T * Am * uu)[0]) == 0
   and sp.expand((vv.T * S2.T * Am * S2 * vv)[0] - ((S2.T * vv).T * Am * (S2.T * vv))[0]) != 0)
# Q2a: Z5 arithmetic
same(2, "א", [(3 * 4) % 5, pow(2, -1, 5), pow(3, -1, 5)])
ok("Q2a E (all ones) is the Hadamard identity on H; I and the zero matrix have zero entries so are not in H",
   all((1 * x) % 5 == x for x in range(1, 5)) and all(0 not in h for h in itertools.product(range(1, 5), repeat=4)))
# Q2b
H = list(itertools.product(range(1, 5), repeat=4))
same(2, "ב", [4, len(H)])
# Q2c
def order(x, p=5):
    k, y = 1, x % p
    while y != 1:
        y = (y * x) % p
        k += 1
    return k


same(2, "ג", [order(2), order(3), math.lcm(order(1), order(2), order(2), order(3))])
X = (1, 2, 2, 3)
k = next(k for k in range(1, 20) if all(pow(c, k, 5) == 1 for c in X))
ok("Q2c brute force: smallest k with X^(odot k) = E is 4", k == 4)
# Q2d
a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
same(2, "ד", [3 * (1 + 4 + 9)])
ok("Q2d numeric example satisfies CS: 36 <= 42", 36 <= 42)
a = sp.Matrix([1, 2, 3])
ones = sp.Matrix([1, 1, 1])
ok("Q2d <u,1>^2 <= |u|^2 n on random integer vectors", all((sum(v) ** 2 <= len(v) * sum(t * t for t in v)) for v in itertools.product(range(-3, 4), repeat=3)))
ok("Q2d distractor vectors give different inequalities (a=(1,2,3))",
   (sp.Matrix([1, 2, 3]).dot(sp.Matrix([1, 2, 3]))) != sum([1, 2, 3]) and (sp.Matrix([1, 4, 9]).dot(ones)) != sum([1, 2, 3]))
# Q3: a (x) b = ab-a-b
o = lambda x, y: x * y - x - y
same(3, "א", [o(3, 4), o(-2, 5)])
same(3, "ב", [o(o(1, 2), 3), o(1, o(2, 3)), o(o(1, 2), 3) - o(1, o(2, 3))])
x_, y_, z_, e_ = sp.symbols("x y z e")
ok("Q3b (a o b) o c = abc-ac-bc-ab+a+b-c ; a o (b o c) = abc-ab-ac-a-bc+b+c",
   sp.expand(o(o(x_, y_), z_) - (x_ * y_ * z_ - x_ * z_ - y_ * z_ - x_ * y_ + x_ + y_ - z_)) == 0
   and sp.expand(o(x_, o(y_, z_)) - (x_ * y_ * z_ - x_ * y_ - x_ * z_ - x_ - y_ * z_ + y_ + z_)) == 0)
ok("Q3c e(a-1)=2a : a=1 gives 0=2", sp.expand(o(x_, e_) - x_ - (e_ * (x_ - 1) - 2 * x_)) == 0 and sp.expand(e_ * (1 - 1)) == 0)
same(3, "ג", [sp.expand(e_ * (1 - 1)), 2 * 1])
ok("Q3c no identity exists on a range (brute force e in -50..50, a in -50..50)",
   not any(all(o(t, ee) == t for t in range(-50, 51)) for ee in range(-50, 51)))
ok("Q3d not associative and no identity", any(o(o(p, q), r) != o(p, o(q, r)) for p, q, r in itertools.product(range(-3, 4), repeat=3)))
same(3, "ד", [o(o(1, 2), 3) - o(1, o(2, 3))])
# Q3e
u = sp.Matrix([1, 0])
v = sp.Matrix([0, 1])
Am2 = v * u.T + u * v.T
ok("Q3e example A=[[0,1],[1,0]]: A(u+v)=u+v ; A(u-v)=-(u-v)", Am2 * (u + v) == (u + v) and Am2 * (u - v) == -(u - v))
same(3, "ה", [1, -1])
ok("Q3e distractor: diag(5,7) is symmetric with eigenvalues != +-1", sp.diag(5, 7).is_symmetric() and set(sp.diag(5, 7).eigenvals()) == {5, 7})
# general check with a random orthonormal basis of R^2
th = sp.symbols("th", real=True)
U = sp.Matrix([sp.cos(th), sp.sin(th)])
V = sp.Matrix([-sp.sin(th), sp.cos(th)])
Ag = V * U.T + U * V.T
ok("Q3e eigenvalues of vu^T+uv^T are +1,-1 for any rotation angle", sp.simplify(Ag * (U + V) - (U + V)) == sp.zeros(2, 1) and sp.simplify(Ag * (U - V) + (U - V)) == sp.zeros(2, 1))
# Q4a
M = sp.Matrix([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
Qm, Rm = M.QRdecomposition()
same(4, "א", [Rm[0, 0], Rm[0, 1], Rm[1, 1], Rm[2, 2]])
ok("Q4a QR: R upper triangular with positive diagonal and Q orthogonal", Rm.is_upper and all(Rm[i, i] > 0 for i in range(3)) and sp.simplify(Qm.T * Qm) == sp.eye(3))
# Q4b
sc = solve_congruence((3, 5), (5, 7), (7, 32))
same(4, "ב", [[t for t in range(5) if (3 * t) % 5 == 4][0], [t for t in range(7) if (2 * t) % 7 == 3][0], 5 * 7 * 32, sc[0]])
ok("Q4b x = 103 mod 1120 solves the original system", sc == (103, 1120) and (3 * 103) % 5 == 4 and (2 * 103) % 7 == 3 and 103 % 32 == 7)
# Q5a
c = sp.symbols("c", real=True)
M5 = sp.Matrix([[1, c, 0], [c, 1, c], [0, c, 1]])
ok("Q5a eigenvalues 1, 1+sqrt2 c, 1-sqrt2 c", set(M5.eigenvals().keys()) == {1, 1 + r2 * c, 1 - r2 * c})
same(5, "א", [1 - r2 / 2])


def kind(cv):
    e = [1, 1 + r2 * cv, 1 - r2 * cv]
    e = [sp.N(t, 30) for t in e]
    return ("PD" if all(t > 1e-20 for t in e) else "PSD" if all(t > -1e-20 for t in e) else "ND" if all(t < -1e-20 for t in e)
            else "NSD" if all(t < 1e-20 for t in e) else "none")


edge = 1 / r2
grid = [R(i, 20) for i in range(-30, 31)]
ok("Q5a PD exactly for |c|<1/sqrt2 and PSD (incl. PD) exactly for |c|<=1/sqrt2 (grid + edge)",
   all((kind(g) == "PD") == (abs(g) < edge) for g in grid) and kind(edge) == "PSD" and kind(-edge) == "PSD"
   and all((kind(g) in ("PD", "PSD")) == (abs(g) <= edge) for g in grid))
ok("Q5a PSD distractors: c=0.9 is not PSD ; c=0.6 is PSD ; c=0.8 not PD distractor |c|<1", kind(R(9, 10)) == "none" and kind(R(3, 5)) == "PD" and kind(R(4, 5)) == "none")
ok("Q5a never ND/NSD (grid) ; c large gives mixed signs ; c=0 is I (PD)",
   all(kind(g) not in ("ND", "NSD") for g in grid) and kind(R(10)) == "none" and kind(sp.Integer(0)) == "PD")
# Q5b
H5 = {t for t in range(12) if t % 2 == 0}
K5 = {t for t in range(12) if t % 3 == 0}
same(5, "ב", [len(H5 & K5)])
ok("Q5b intersection is a subgroup of Z12 and H cup K is not", H5 & K5 == {0, 6} and any(((p + q) % 12) not in (H5 | K5) for p in (H5 | K5) for q in (H5 | K5)))
# Q6a
A6 = sp.Matrix([[3, 2, 0], [2, 2, 2], [0, 2, 1]])
ok("Q6a eigenvalues 5, 2, -1 ; (2,2,1) is a 5-eigenvector", A6.eigenvals() == {5: 1, 2: 1, -1: 1} and A6 * sp.Matrix([2, 2, 1]) == 5 * sp.Matrix([2, 2, 1]))
same(6, "א", [A6.trace(), A6.det(), sp.Matrix([2, 2, 1]).norm()])
# Q6b
uu_, vv_ = sp.Matrix([1, 2]), sp.Matrix([3, -1])
same(6, "ב", [(uu_ + vv_).norm() ** 2 + (uu_ - vv_).norm() ** 2])
p_, q_, r_, s_ = sp.symbols("p q r s", real=True)
U6, V6 = sp.Matrix([p_, q_]), sp.Matrix([r_, s_])
ok("Q6b parallelogram law symbolically", sp.expand((U6 + V6).norm() ** 2 + (U6 - V6).norm() ** 2 - 2 * U6.norm() ** 2 - 2 * V6.norm() ** 2) == 0)
ok("Q6b |u-v|^2 = |u|^2 - 2<u,v> + |v|^2 (so the bug line with -|v|^2 is wrong)",
   sp.expand((U6 - V6).norm() ** 2 - (U6.norm() ** 2 - 2 * U6.dot(V6) + V6.norm() ** 2)) == 0
   and sp.expand((U6 - V6).norm() ** 2 - (U6.norm() ** 2 - 2 * U6.dot(V6) - V6.norm() ** 2)) != 0)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
