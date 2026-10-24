# -*- coding: utf-8 -*-
"""sympy / brute-force check of every machine-checkable step value in tools/raw/24B-A.json.
Run: PYTHONUTF8=1 py -I tools/verify/24B-A/steps_check.py   (ASCII output, exit 1 on mismatch)"""
import json
import pathlib
import sys

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "24B-A.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
bad = []
AL, BE, GI, DA, HE, VAV = "א", "ב", "ג", "ד", "ה", "ו"


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


R = sp.Rational
# Q1a Cauchy-Schwarz
al, be, ga = sp.symbols("al be ga", real=True)
v = sp.Matrix([2, 1, 3])
numeq(1, AL, 0, v.dot(v))
u = sp.Matrix([2, 1, 3])
numeq(1, AL, 1, (2 * u[0] + u[1] + 3 * u[2]) ** 2)
ok("Q1a 196 = 14 * |u|^2 (equality case)", 196 == 14 * u.dot(u))
# no solution: (2a+b+3c)^2 > 16(a^2+b^2+c^2) never, check by sampling and by the CS bound
import random

random.seed(1)
ok("Q1a no sample violates the bound", all((2 * x + y + 3 * z) ** 2 <= 14 * (x * x + y * y + z * z) + 1e-9
                                           for x, y, z in ((random.uniform(-9, 9), random.uniform(-9, 9), random.uniform(-9, 9)) for _ in range(20000))))


# Q1b projection in M2
def ip(X, Y):
    return (Y.T * X).trace()


e1, e2, e3 = sp.Matrix([[1, 1], [-1, 1]]), sp.Matrix([[0, 1], [0, 1]]), sp.Matrix([[1, 1], [0, 0]])
vv = sp.Matrix([[2, 2], [0, 2]])
u1 = e1
u2 = e2 - ip(e2, u1) / ip(u1, u1) * u1
u3 = e3 - ip(e3, u1) / ip(u1, u1) * u1 - ip(e3, u2) / ip(u2, u2) * u2
numeq(1, BE, 0, ip(e2, u1))
numeq(1, BE, 1, ip(e3, u2))
numeq(1, BE, 2, ip(vv, u1) / ip(u1, u1))
proj = sum((ip(vv, w) / ip(w, w) * w for w in (u1, u2, u3)), sp.zeros(2, 2))
ok("Q1b proj = [[3/2,5/2],[-1/2,3/2]]", proj == sp.Matrix([[R(3, 2), R(5, 2)], [-R(1, 2), R(3, 2)]]))
numeq(1, BE, 3, proj[0, 1])
ok("Q1b u2, u3 as in the solution", u2 == sp.Matrix([[-R(1, 2), R(1, 2)], [R(1, 2), R(1, 2)]]) and u3 == sp.Matrix([[R(1, 2), R(1, 2)], [R(1, 2), -R(1, 2)]]))

# Q2a: G = {(a, a^2)} in Z7* x Z7*
G = {(a, a * a % 7) for a in range(1, 7)}
mul = lambda p, q: (p[0] * q[0] % 7, p[1] * q[1] % 7)
ok("Q2a.1 (1,1) neutral in G", (1, 1) in G and all(mul((1, 1), g) == g for g in G))
for wrong in ((0, 0), (1, 0), (0, 1)):
    ok("Q2a.1 distractor %s not in G" % (wrong,), wrong not in G)
numeq(2, AL, 1, mul((1, 1), (3, 2))[1])
ok("Q2a.2 (2,4)^-1 = (4,2)", mul((2, 4), (4, 2)) == (1, 1))
numeq(2, BE, 0, pow(2, -1, 7))
numeq(2, BE, 1, pow(4, -1, 7))
ok("Q2a.3 |G| = 6 and map a -> (a,a^2) injective", len(G) == 6)
numeq(2, GI, 1, 6)
ok("Q2a.3 distractor sizes wrong: 7, 36, 49", len(G) not in (7, 36, 49))
ordz = lambda a: next(k for k in range(1, 7) if pow(a, k, 7) == 1)
numeq(2, DA, 0, ordz(3))
numeq(2, DA, 1, ordz(2))
g, k = (3, 2), 1
cur = g
while cur != (1, 1):
    cur = mul(cur, g)
    k += 1
numeq(2, DA, 2, k)
ok("Q2a.4 (3,2) in G", (3, 2) in G)
ok("Q2a.4 product of orders (18) is not the order", ordz(3) * ordz(2) != k)

# Q2b
numeq(2, HE, 0, 5 - 3)
numeq(2, VAV, 1, 6)
A = sp.diag(0, 2, 5)
ok("Q2b c=6 makes cI-A PD, c=5 does not", all(x > 0 for x in (6 * sp.eye(3) - A).eigenvals()) and not all(x > 0 for x in (5 * sp.eye(3) - A).eigenvals()))
cc = sp.symbols("cc", real=True)
M = sp.Matrix([[1, 2], [2, 1]])
ok("Q2b eig(cI-A) = c - eig(A) (example)", sorted((3 * sp.eye(2) - M).eigenvals()) == sorted(3 - x for x in M.eigenvals()))
ok("Q2b c = lambda_max gives eigenvalue 0 (not strict)", 0 in (3 * sp.eye(2) - M).eigenvals())
ok("Q2b c = 0 gives non-positive eigenvalues", all(x <= 0 for x in (0 * sp.eye(3) - A).eigenvals()))
ok("Q2b c below lambda_min makes all eigenvalues negative", all(x < 0 for x in (-1 * sp.eye(3) - A).eigenvals()))

# Q3a
c = sp.symbols("c", real=True)
M3 = sp.Matrix([[1, c, 0], [c, 1, c], [0, c, 1]])
lam = sp.Symbol("l")
roots = sp.solve(M3.charpoly(lam).as_expr(), lam)
ok("Q3a eigenvalues 1, 1+-sqrt2 c", {sp.simplify(r) for r in roots} == {1, 1 + sp.sqrt(2) * c, 1 - sp.sqrt(2) * c})
numeq(3, AL, 0, sp.solve(1 - sp.sqrt(2) * c, c)[0])
numeq(3, AL, 1, min(M3.subs(c, 1).eigenvals()))
ok("Q3a endpoint c=1/sqrt2 has eigenvalue 0", 0 in {sp.simplify(x) for x in M3.subs(c, 1 / sp.sqrt(2)).eigenvals()})
ok("Q3a c=2 indefinite", min(sp.N(x) for x in M3.subs(c, 2).eigenvals()) < 0 < max(sp.N(x) for x in M3.subs(c, 2).eigenvals()))

# Q3b
pts = [(-3, -1), (0, 1), (1, 3), (3, 3), (4, 6)]
Am = sp.Matrix([[x, 1] for x, _ in pts])
bm = sp.Matrix([y for _, y in pts])
numeq(3, BE, 0, (Am.T * Am)[0, 0])
numeq(3, BE, 1, (Am.T * bm)[0])
sol = (Am.T * Am).solve(Am.T * bm)
numeq(3, BE, 2, sol[0])
numeq(3, BE, 3, sol[1])

# Q4a: x*y = (x+y)/(1+xy) on (-1,1)
x, y, z = sp.symbols("x y z", real=True)
st = lambda p, q: (p + q) / (1 + p * q)
ok("Q4a 1+x*y = (1+x)(1+y)/(1+xy)", sp.simplify(1 + st(x, y) - (1 + x) * (1 + y) / (1 + x * y)) == 0)
ok("Q4a 1-x*y = (1-x)(1-y)/(1+xy)", sp.simplify(1 - st(x, y) - (1 - x) * (1 - y) / (1 + x * y)) == 0)
ok("Q4a findbug factor (1+x)(1-y) differs", sp.simplify((1 + x) * (1 - y) - (1 + x) * (1 + y)) != 0)
ok("Q4a associative", sp.simplify(st(st(x, y), z) - st(x, st(y, z))) == 0)
numeq(4, AL, 2, st(st(R(1, 2), R(1, 5)), R(1, 10)))
ok("Q4a identity 0, inverse -x", sp.simplify(st(x, 0) - x) == 0 and sp.simplify(st(x, -x)) == 0)
for wrong in (1 / x, -1 / x, 1 - x):
    ok("Q4a inverse distractor wrong", sp.simplify(st(x, wrong)) != 0)
ok("Q4a commutative", sp.simplify(st(x, y) - st(y, x)) == 0)
numeq(4, BE, 1, st(R(1, 2), R(1, 3)))

# Q5a
A5 = sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 2]])
ev = A5.eigenvals()
ok("Q5a eigenvalues {2:2, 0:1}", ev == {2: 2, 0: 1})
numeq(5, AL, 0, 4 - 2 - 2)
numeq(5, AL, 1, ev[2])
numeq(5, AL, 2, sp.Matrix([1, 1, 0]).dot(sp.Matrix([-1, 1, 0])))
numeq(5, AL, 3, sp.Matrix([-1, 1, 0]).norm())
ok("Q5a eigenvectors", A5 * sp.Matrix([1, 1, 0]) == 2 * sp.Matrix([1, 1, 0]) and A5 * sp.Matrix([0, 0, 1]) == 2 * sp.Matrix([0, 0, 1])
   and A5 * sp.Matrix([-1, 1, 0]) == sp.zeros(3, 1))

# Q5b CRT
from sympy.ntheory.modular import solve_congruence

numeq(5, BE, 0, 19 % 11)
numeq(5, BE, 1, pow(77, -1, 5))
numeq(5, BE, 2, pow(35, -1, 11))
numeq(5, BE, 3, solve_congruence((2, 5), (3, 7), (19, 11))[0])

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
