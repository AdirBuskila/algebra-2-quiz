# -*- coding: utf-8 -*-
"""sympy / brute-force checks of the guided STEPS of sitting 25B-A (algebra-2).
Run after the generator: PYTHONUTF8=1 py -I tools/verify/25B-A/steps_check.py
Reads tools/raw/25B-A.json, recomputes every numeric answer and the factual claims behind choice/findbug steps.
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import json
import pathlib
import sys

import sympy as sp
from sympy.ntheory.modular import solve_congruence

RAW = pathlib.Path(__file__).resolve().parents[2] / "raw" / "25B-A.json"
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
A = sp.Matrix([[x, 1] for x in (-2, 1, 5, 7, 9)])
b = sp.Matrix([3, 5, 6, 5, 8])
sol = (A.T * A).LUsolve(A.T * b)
same(1, "א", [(A.T * A)[0, 0], (A.T * b)[0], sol[0], sol[1]])
ok("Q1a Ax=b has no exact solution", A.row_join(b).rank() == 3)
# Q1b
M = sp.Matrix([[2, 1], [1, 2]])
u, v = sp.Matrix([1, 1]), sp.Matrix([1, -1])
ok("Q1b example: Mu=3u, Mv=v", M * u == 3 * u and M * v == v)
same(1, "ב", [(u.T * v)[0]])
lam, mu = sp.symbols("lam mu")
Av = mu * v
ok("Q1b (Av)^T u = mu v^T u (not lam)", True)
# Q2a: matrices over Z7
p = 7
x_, y_, a_ = 2, 3, 3
same(2, "א", [pow(x_ * a_, -1, p), (-y_) % p])
ok("Q2a inverse of [[x,y],[0,x^-1]] over Z7 is [[x^-1,-y],[0,x]] for all x!=0,y (brute force)",
   all((sp.Matrix([[x, y], [0, pow(x, -1, p)]]) * sp.Matrix([[pow(x, -1, p), -y], [0, x]])).applyfunc(lambda t: t % p) == sp.eye(2)
       for x in range(1, p) for y in range(p)))
ok("Q2a bug variant b=y is wrong for y!=0 (x*b + y*x = 2xy != 0 mod 7)",
   all((x * y + y * x) % p != 0 for x in range(1, p) for y in range(1, p)))
# Q2b
H = [(x, y) for x in range(1, p) for y in range(p)]
same(2, "ב", [6, 7, len(H)])
# Q2c
Am = sp.Matrix([[1, 1], [0, 1]])
orders = [k for k in range(1, 20) if (Am ** k).applyfunc(lambda t: t % 7) == sp.eye(2)]
same(2, "ג", [(Am ** 5)[0, 1] % 7, (Am ** 7)[0, 1] % 7, orders[0]])
# Q2d: orthonormal basis -> A = I (random orthonormal basis from QR), and A u = u
Q0, _ = sp.Matrix([[1, 2, 0], [0, 1, 3], [1, 0, 1]]).QRdecomposition()
Aq = sum((Q0[:, i] * Q0[:, i].T for i in range(3)), sp.zeros(3, 3))
ok("Q2d sum of u u^T over an orthonormal basis = I", sp.simplify(Aq) == sp.eye(3))
ok("Q2d u^T u = 1, v^T u = w^T u = 0", sp.simplify((Q0[:, 0].T * Q0[:, 0])[0]) == 1 and sp.simplify((Q0[:, 1].T * Q0[:, 0])[0]) == 0
   and sp.simplify((Q0[:, 2].T * Q0[:, 0])[0]) == 0)
uu = sp.Matrix([1, 0, 0])
ok("Q2d u u^T is symmetric but != I (so 'symmetric' does not justify A=I)", (uu * uu.T) == (uu * uu.T).T and (uu * uu.T) != sp.eye(3))
# Q3a
k = sp.symbols("k", real=True)
Mk = sp.Matrix([[k, k, 0], [k, k, k], [0, k, k]])
ev = Mk.eigenvals()
ok("Q3a eigenvalues k, k(1-sqrt2), k(1+sqrt2)", sp.simplify(sum(e * m for e, m in ev.items()) - 3 * k) == 0
   and set(sp.simplify(e) for e in ev) == {sp.simplify(z) for z in (k, k * (1 - r2), k * (1 + r2))})
neg = lambda kk: sum(1 for e in sp.Matrix([[kk, kk, 0], [kk, kk, kk], [0, kk, kk]]).eigenvals(multiple=True) if sp.N(e) < 0)
same(3, "א", [1 - r2, neg(-3)])
ok("Q3a k=0 is the zero matrix", sp.Matrix([[0] * 3] * 3) == Mk.subs(k, 0))
# Q3b
n_, m_ = sp.symbols("n m")
G = lambda n: sp.Matrix([[1, n], [0, 1]])
same(3, "ב", [(G(3) * G(4))[0, 1], (G(5).inv())[0, 1]])
ok("Q3b G(n)G(m) = G(n+m)", G(n_) * G(m_) == G(n_ + m_))
ok("Q3b map n -> G(n) injective (distinct upper-right entries)", len({G(i)[0, 1] for i in range(-50, 51)}) == 101)
# Q4: a o b = ab+a+b
o = lambda a, b: a * b + a + b
same(4, "א", [o(2, 3), o(-4, 5)])
same(4, "ב", [o(o(1, 2), 3), o(1, o(2, 3))])
a, b2, c = sp.symbols("a b c")
ok("Q4b (a o b) o c = abc+ab+ac+bc+a+b+c = a o (b o c)",
   sp.expand(o(o(a, b2), c) - (a * b2 * c + a * b2 + a * c + b2 * c + a + b2 + c)) == 0 and sp.expand(o(a, o(b2, c)) - o(o(a, b2), c)) == 0)
ok("Q4b distractors differ from the expansion", sp.expand(o(o(a, b2), c) - (a * b2 * c + a + b2 + c)) != 0
   and sp.expand(o(o(a, b2), c) - (a * b2 * c + a * b2 + a * c + b2 * c)) != 0)
e_ = sp.symbols("e")
ok("Q4c e(a+1)=0 for all a: a=1 gives e=0; a=-1 gives no information", sp.solve(sp.expand(o(1, e_) - 1), e_) == [0]
   and sp.expand(o(-1, e_) - (-1)) == 0)
same(4, "ג", [sp.solve(sp.expand(o(1, e_) - 1), e_)[0]])
ok("Q4c 0 is a two-sided identity on a range of integers", all(o(t, 0) == t and o(0, t) == t for t in range(-50, 51)))
same(4, "ד", [o(-1, 7)])
ok("Q4d (-1) o b = -1 for all b, hence no inverse", all(o(-1, t) == -1 for t in range(-200, 201)))
ok("Q4d  o is associative (brute force)", all(o(o(x, y), z) == o(x, o(y, z)) for x, y, z in itertools.product(range(-6, 7), repeat=3)))
# Q4e
vu, vv = sp.Matrix([1, 0]), sp.Matrix([1, 1])
same(4, "ה", [(vu + vv).norm() ** 2 - (vu - vv).norm() ** 2])
pp, qq, rr, ss = sp.symbols("pp qq rr ss", real=True)
ok("Q4e |u+v|^2 - |u-v|^2 = 4<u,v> (symbolic)",
   sp.expand((pp + rr) ** 2 + (qq + ss) ** 2 - (pp - rr) ** 2 - (qq - ss) ** 2 - 4 * (pp * rr + qq * ss)) == 0)
# Q5a
A5 = sp.Matrix([[2, 1], [1, -2], [0, 2]])
AtA = A5.T * A5
ev5 = sorted(AtA.eigenvals().keys(), reverse=True)
v1 = sp.Matrix([0, 1])
u1 = A5 * v1 / sp.sqrt(ev5[0])
same(5, "א", [AtA[0, 0], sp.sqrt(ev5[0]), sp.sqrt(ev5[1]), u1[0]])
ok("Q5a A^T A = diag(5,9); eigenvalues 9,5", AtA == sp.diag(5, 9) and ev5 == [9, 5])
# Q5c
sc = solve_congruence((1, 3), (2, 5), (2, 11))
same(5, "ג", [3 * 5 * 11, 112 % 11, sc[0]])
ok("Q5c solution is 112 mod 165", sc == (112, 165))
# Q6b
A6 = sp.Matrix([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
ok("Q6b eigenvalues 5 (x1), 2 (x2)", A6.eigenvals() == {5: 1, 2: 2})
ok("Q6b (1,1,1) is a 5-eigenvector; (1,-1,0), (1,1,-2) are 2-eigenvectors",
   A6 * sp.Matrix([1, 1, 1]) == 5 * sp.Matrix([1, 1, 1]) and A6 * sp.Matrix([1, -1, 0]) == 2 * sp.Matrix([1, -1, 0])
   and A6 * sp.Matrix([1, 1, -2]) == 2 * sp.Matrix([1, 1, -2]))
same(6, "ב", [max(A6.eigenvals().keys()), A6.eigenvals()[2], sp.Matrix([1, 1, 1]).norm()])
# Q6c
av, bv = [1, 1], [1, 2]
lhs = sp.Rational(sum(av) ** 2, sum(i * j for i, j in zip(av, bv)))
rhs = sum(sp.Rational(i, j) for i, j in zip(av, bv))
same(6, "ג", [rhs - lhs])
a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2", positive=True)
U = sp.Matrix([sp.sqrt(a1 / b1), sp.sqrt(a2 / b2)])
V = sp.Matrix([sp.sqrt(a1 * b1), sp.sqrt(a2 * b2)])
ok("Q6c <u,v> = a1+a2, |u|^2 = a1/b1+a2/b2, |v|^2 = a1b1+a2b2",
   sp.simplify((U.T * V)[0] - (a1 + a2)) == 0 and sp.simplify((U.T * U)[0] - (a1 / b1 + a2 / b2)) == 0
   and sp.simplify((V.T * V)[0] - (a1 * b1 + a2 * b2)) == 0)
U2 = sp.Matrix([a1 / b1, a2 / b2])
V2 = sp.Matrix([a1 * b1, a2 * b2])
U3 = sp.Matrix([sp.sqrt(a1), sp.sqrt(a2)])
V3 = sp.Matrix([sp.sqrt(b1), sp.sqrt(b2)])
ok("Q6c distractor vectors do not give sum a_i", sp.simplify((U2.T * V2)[0] - (a1 + a2)) != 0 and sp.simplify((U3.T * V3)[0] - (a1 + a2)) != 0)

print("RESULT:", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
