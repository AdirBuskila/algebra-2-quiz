# -*- coding: utf-8 -*-
"""sympy / brute-force check of every machine-checkable step value in tools/raw/24B-B.json.
Run: PYTHONUTF8=1 py -I tools/verify/24B-B/steps_check.py   (ASCII output, exit 1 on mismatch)"""
import json
import pathlib
import sys

import sympy as sp

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "24B-B.json"
data = json.loads(RAW.read_text(encoding="utf-8"))
bad = []
AL, BE, GI, DA, HE = "א", "ב", "ג", "ד", "ה"


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
nn = sp.symbols("nn", positive=True, integer=True)
# Q1a
ok("Q1a ||v||^2 = n * (1/n) = 1", sp.simplify(nn * (1 / sp.sqrt(nn)) ** 2) == 1)
numeq(1, AL, 0, sum(range(1, 5)))
numeq(1, AL, 1, sp.sqrt(4 * R(1, 4)))
ok("Q1a inequality holds for n=1..40", all(sum(sp.sqrt(R(k, n)) for k in range(1, n + 1)).evalf() <= sp.sqrt(R(n * n + n, 2)).evalf() + 1e-12 for n in range(1, 41)))
ok("Q1a findbug ||v|| = n is wrong for n=4", sp.sqrt(4 * R(1, 4)) != 4)


# Q1b, Q1c
def ip(X, Y):
    return (Y.T * X).trace()


I2 = sp.eye(2)
Bm = sp.Matrix([[0, 1], [0, 1]])
Cm = sp.Matrix([[1, 1], [1, 2]])
numeq(1, BE, 0, ip(Bm, I2))
numeq(1, BE, 1, ip(I2, I2))
u2 = Bm - ip(Bm, I2) / ip(I2, I2) * I2
numeq(1, BE, 2, u2[0, 0])
w = 2 * u2
ok("Q1b w = [[-1,2],[0,1]] orthogonal to I", w == sp.Matrix([[-1, 2], [0, 1]]) and ip(w, I2) == 0)
numeq(1, GI, 0, ip(Cm, I2))
numeq(1, GI, 1, ip(Cm, w) / ip(w, w))
proj = ip(Cm, I2) / ip(I2, I2) * I2 + ip(Cm, w) / ip(w, w) * w
ok("Q1c proj = [[1,1],[0,2]]", proj == sp.Matrix([[1, 1], [0, 2]]))
numeq(1, GI, 2, proj[1, 1])

# Q2: unitriangular mod 3
a, b, x, y = sp.symbols("a b x y")
M = lambda a_, b_: sp.Matrix([[1, a_, b_], [0, 1, a_], [0, 0, 1]])
prod = M(a, b) * M(x, y)
ok("Q2a AB top-right = y + a x + b", sp.expand(prod[0, 2] - (y + a * x + b)) == 0)
numeq(2, AL, 0, (1 + 1 * 2 + 2) % 3)
Mi = M(a, b)
true_inv = sp.Matrix([[1, -a, a**2 - b], [0, 1, -a], [0, 0, 1]])
ok("Q2a true inverse", sp.simplify(Mi * true_inv - sp.eye(3)) == sp.zeros(3, 3))
for k, cand in enumerate([sp.Matrix([[1, -a, -b], [0, 1, -a], [0, 0, 1]]), sp.Matrix([[1, -a, a**2 + b], [0, 1, -a], [0, 0, 1]]),
                          sp.Matrix([[1, a, -b], [0, 1, a], [0, 0, 1]])]):
    ok("Q2a inverse distractor %d wrong" % k, sp.simplify(Mi * cand - sp.eye(3)) != sp.zeros(3, 3))
ok("Q2a distractor 1 top-right = -a^2", sp.expand((Mi * sp.Matrix([[1, -a, -b], [0, 1, -a], [0, 0, 1]]))[0, 2] + a**2) == 0)
ok("Q2a findbug (+b) product top-right = 2b", sp.expand((Mi * sp.Matrix([[1, -a, a**2 + b], [0, 1, -a], [0, 0, 1]]))[0, 2] - 2 * b) == 0)
Gset = {(p, q) for p in range(3) for q in range(3)}
mm = lambda X, Y: (X * Y).applyfunc(lambda t: t % 3)
ok("Q2a group closed, 9 elements", len(Gset) == 9 and all(tuple(mm(M(*g1), M(*g2))[0, :].tolist()[0][1:]) in Gset for g1 in Gset for g2 in Gset))
numeq(2, BE, 0, 3)
numeq(2, BE, 1, len(Gset))
A = sp.Matrix([[1, 2, 0], [0, 1, 2], [0, 0, 1]])
A2, A3 = mm(A, A), mm(mm(A, A), A)
numeq(2, GI, 0, A2[0, 2])
numeq(2, GI, 1, A3[0, 1])
ok("Q2c A^3 = I, A^2 != I, A != I", A3 == sp.eye(3) and A2 != sp.eye(3) and A != sp.eye(3))
numeq(2, GI, 2, 3)

# Q3a
k = sp.symbols("k", real=True)
M3 = sp.Matrix([[k**2, 0, 2 * k], [0, k + 1, 0], [2 * k, 0, k**2]])
lam = sp.Symbol("l")
ok("Q3a eigenvalues", sp.expand(M3.charpoly(lam).as_expr() - (lam - (k + 1)) * (lam - (k**2 + 2 * k)) * (lam - (k**2 - 2 * k))) == 0)
numeq(3, AL, 0, (k**2 + 2 * k).subs(k, 3))
numeq(3, AL, 1, min(M3.subs(k, 1).eigenvals()))


def psd(kv):
    return all(sp.N(e) >= -1e-12 for e in M3.subs(k, kv).eigenvals())


ok("Q3a k=0 PSD (k>=2 only is wrong)", psd(0))
ok("Q3a k=1 not PSD (k>=0 wrong)", not psd(1))
ok("Q3a k=2 PSD but not PD (k>2 wrong)", psd(2) and 0 in M3.subs(k, 2).eigenvals())
ok("Q3a PSD set on grid = {k>=2} u {0}", all(psd(R(t, 4)) == (R(t, 4) >= 2 or t == 0) for t in range(-24, 25)))

# Q3b
pts = [(0, 0), (2, 1), (3, 4), (4, 6), (6, 9)]
Am = sp.Matrix([[p, 1] for p, _ in pts])
bm = sp.Matrix([q for _, q in pts])
numeq(3, BE, 0, (Am.T * Am)[0, 0])
numeq(3, BE, 1, (Am.T * bm)[0])
sol = (Am.T * Am).solve(Am.T * bm)
numeq(3, BE, 2, sol[0])
numeq(3, BE, 3, sol[1])

# Q4: (x,y)*(u,v) = (2xu, y+v)
star = lambda p, q: (2 * p[0] * q[0], p[1] + q[1])
numeq(4, AL, 1, star((1, 2), (3, 4))[0])
ok("Q4a x=-1,u=1: 2xu<0 yet nonzero (positivity not needed)", star((-1, 0), (1, 0))[0] < 0)
ok("Q4b associativity symbolic", all(sp.simplify(l - r) == 0 for l, r in zip(star(star((x, y), (a, b)), (3, 5)), star((x, y), star((a, b), (3, 5))))))
numeq(4, BE, 0, star(star((1, 0), (2, 1)), (3, 2))[0])
numeq(4, BE, 1, star(star((1, 0), (2, 1)), (3, 2))[1])
ok("Q4b other side equals", star((1, 0), star((2, 1), (3, 2))) == (24, 3))
e1 = sp.symbols("e1")
numeq(4, GI, 0, sp.solve(sp.Eq(2 * e1 * x, x), e1)[0])
ok("Q4c e=(1/2,0) neutral, (1,0) not", star((R(1, 2), 0), (x, y)) == (x, y) and star((1, 0), (x, y)) != (x, y))
xs = sp.symbols("xs", nonzero=True)
inv = (1 / (4 * xs), -y)
ok("Q4d inverse (1/(4x), -y)", sp.simplify(star((xs, y), inv)[0] - R(1, 2)) == 0 and sp.simplify(star((xs, y), inv)[1]) == 0)
numeq(4, DA, 0, (1 / (4 * xs)).subs(xs, 2))
numeq(4, DA, 1, -3)
ok("Q4d (1/x,-y) is not the inverse", sp.simplify(star((xs, y), (1 / xs, -y))[0] - R(1, 2)) != 0)
sx, sy = sp.symbols("sx sy")
cube = star(star((sx, sy), (sx, sy)), (sx, sy))
ok("Q4e cube = (4x^3, 3y)", sp.expand(cube[0] - 4 * sx**3) == 0 and sp.expand(cube[1] - 3 * sy) == 0)
sols = sp.solve([sp.Eq(cube[0], sx), sp.Eq(cube[1], sy)], [sx, sy], dict=True)
nz = [s_ for s_ in sols if s_[sx] != 0]
ok("Q4e solutions (+-1/2, 0)", {(s_[sx], s_[sy]) for s_ in nz} == {(R(1, 2), 0), (-R(1, 2), 0)})
numeq(4, HE, 0, max(s_[sx] for s_ in nz))
numeq(4, HE, 1, nz[0][sy])
ok("Q4e count = 2", len(nz) == 2)

# Q5a SVD
A5 = sp.Matrix([[2, 1], [1, -2], [0, 2]])
ok("Q5a A^T A = diag(5,9)", A5.T * A5 == sp.diag(5, 9))
numeq(5, AL, 0, 9)
V = sp.Matrix([[0, 1], [1, 0]])
u1 = A5 * V[:, 0] / 3
ok("Q5a u1 = (1/3,-2/3,2/3)", u1 == sp.Matrix([R(1, 3), -R(2, 3), R(2, 3)]))
numeq(5, AL, 1, u1[0])
u3 = sp.Matrix([-2, 4, 5])
numeq(5, AL, 2, u3.norm())
u2 = A5 * V[:, 1] / sp.sqrt(5)
ok("Q5a u3 orthogonal to u1,u2", u3.dot(u1) == 0 and sp.simplify(u3.dot(u2)) == 0)
U = sp.Matrix.hstack(u1, u2, u3 / u3.norm())
S = sp.Matrix([[3, 0], [0, sp.sqrt(5)], [0, 0]])
ok("Q5a A = U S V^T", sp.simplify(U * S * V.T - A5) == sp.zeros(3, 2) and sp.simplify(U.T * U) == sp.eye(3))

# Q5b
from sympy.ntheory.modular import solve_congruence

res = solve_congruence((4, 5), (6, 8), (8, 9))
ok("Q5b CRT = 134 mod 360", res == (134, 360))
numeq(5, BE, 0, res[1])
numeq(5, BE, 1, 134 % 8)
numeq(5, BE, 2, 134 % 9)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
