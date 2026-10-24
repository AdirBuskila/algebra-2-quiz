# -*- coding: utf-8 -*-
"""Machine check of every numeric/choice step value of sitting 24A-A (rubric/steps phase).
Run: PYTHONUTF8=1 py -I tools/verify/24A-A/steps_check.py   (after tools/gen/gen_24A-A.py). ASCII output, exit 1 on mismatch."""
import json
import pathlib
import sys
from math import gcd

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
raw = json.loads((ROOT / "tools" / "raw" / "24A-A.json").read_text(encoding="utf-8"))
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
s3 = sp.sqrt(3)

# Q1a: u=(3,4), v=2u
u = sp.Matrix([3, 4]); v = 2 * u
same("1a", numeric_answers(1, "א"), [(u + v).norm()])
ok("1a equality case", (u + v).norm() == u.norm() + v.norm())
ok("1a opposite direction breaks equality", (u - v).norm() != u.norm() + v.norm())
ok("1a cos=1 <=> <u,v>=|u||v|", u.dot(v) == u.norm() * v.norm())

# Q1b: Frobenius inner product <A,B> = tr(B^T A)
ip = lambda A, B: (B.T * A).trace()
v_ = sp.Matrix([[1, 1], [1, 0]])
I2 = sp.eye(2)
w2 = sp.Matrix([[0, 1], [0, 1]])
u1 = I2
u2 = w2 - ip(w2, u1) / ip(u1, u1) * u1
ok("1b u2*2 = [[-1,2],[0,1]]", 2 * u2 == sp.Matrix([[-1, 2], [0, 1]]))
U2 = 2 * u2
proj = ip(v_, u1) / ip(u1, u1) * u1 + ip(v_, U2) / ip(U2, U2) * U2
ok("1b projection", proj == sp.Matrix([[R(1, 3), R(1, 3)], [0, R(2, 3)]]))
ok("1b <I,u2>=0", ip(u1, U2) == 0)
same("1b", numeric_answers(1, "ב"), [ip(U2, U2), ip(v_, U2), proj[0, 0], proj[1, 1]])

# Q2: a (.) b = ab/(a+b)
a, b, c = sp.symbols("a b c", positive=True)
od = lambda p, q: p * q / (p + q)
lhs = sp.simplify(od(od(a, b), c)); rhs = sp.simplify(od(a, od(b, c)))
ok("2a associative", sp.simplify(lhs - rhs) == 0 and sp.simplify(lhs - a * b * c / (a * b + a * c + b * c)) == 0)
same("2a", numeric_answers(2, "א"), [od(od(R(1), R(2)), R(3))])
sub = {a: 1, b: 2, c: 3}
for name, ex in (("abc/(a+b+c)", a * b * c / (a + b + c)), ("(ab+ac+bc)/abc", (a * b + a * c + b * c) / (a * b * c)), ("(a+b+c)/abc", (a + b + c) / (a * b * c))):
    ok(f"2a distractor {name} differs at (1,2,3)", ex.subs(sub) != R(6, 11), str(ex.subs(sub)))
ok("2a distractor values 1, 11/6, 1", [e.subs(sub) for e in (a * b * c / (a + b + c), (a * b + a * c + b * c) / (a * b * c), (a + b + c) / (a * b * c))] == [1, R(11, 6), 1])
e = sp.symbols("e", positive=True)
ok("2b a(.)e = a -> a^2 = 0", sp.simplify(sp.numer(sp.together(od(a, e) - a))) == -a ** 2 or sp.expand(sp.numer(sp.together(od(a, e) - a)) + a ** 2) == 0)
ok("2b no positive e for a=3", sp.solve(sp.Eq(od(3, e), 3), e) == [])
ok("2b commutative and closed", sp.simplify(od(a, b) - od(b, a)) == 0 and (od(a, b)).is_positive)
same("2b", numeric_answers(2, "ב"), [od(R(3), R(6))])
x = sp.symbols("x", positive=True)
xx = sp.simplify(od(x, x))
ok("2c x(.)x = x/2", sp.simplify(xx - x / 2) == 0)
ok("2c x/2=x has no positive solution", sp.solve(sp.Eq(x / 2, x), x) == [] or all(not s.is_positive for s in sp.solve(sp.Eq(x / 2, x), x)))
ok("2c distractors at x=6", od(R(6), R(6)) == 3 and 3 not in (12, 36, R(3, 2)))
same("2c", numeric_answers(2, "ג"), [0])
pw = lambda t, n: __import__("functools").reduce(od, [t] * n)
ok("2d x^n = x/n for n=1..8", all(sp.simplify(pw(x, n) - x / n) == 0 for n in range(1, 9)))
ok("2d distractor x/(2n) differs", sp.simplify(pw(x, 2) - x / 4) != 0)
same("2d", numeric_answers(2, "ד"), [pw(R(2), 3), 5])
ok("2d a=5 -> n=5", pw(R(5), 5) == 1 and all(pw(R(5), n) != 1 for n in range(1, 5)))

# Q2e
A = sp.Matrix([[2, 1], [1, 2]])
cc = 1
M = cc * sp.eye(2) + A + A ** 2
same("2e", numeric_answers(2, "ה"), [(sp.Matrix([1, 0]).T * M * sp.Matrix([1, 0]))[0]])
A2 = sp.diag(1, 2); vv = sp.Matrix([1, 1])
q = (vv.T * A2 ** 2 * vv)[0]
ok("2e v^T A^2 v = |Av|^2", q == (A2 * vv).dot(A2 * vv) == 5)
ok("2e distractors 9, -5, 17", [(vv.T * A2 * vv)[0] ** 2, -(A2 * vv).dot(A2 * vv), (A2 ** 2 * vv).dot(A2 ** 2 * vv)] == [9, -5, 17])

# Q3a
aa, bb = sp.symbols("a b", real=True)
M3 = sp.Matrix([[1, 0, aa ** 2], [0, 3 * aa - 1, 0], [aa ** 2, 0, 1]])
ev = M3.eigenvals().keys()
ok("3a eigenvalues", set(ev) == {3 * aa - 1, 1 + aa ** 2, 1 - aa ** 2}, str(set(ev)))
ok("3a b=0 for symmetry", sp.Matrix([[1, 0, aa ** 2], [0, 3 * aa - 1, 0], [aa ** 2, bb, 1]]).is_symmetric() is False
   and sp.Matrix([[1, 0, aa ** 2], [0, 3 * aa - 1, 0], [aa ** 2, 0, 1]]).is_symmetric())
ok("3a distractor eigenvalue lists differ at a=2", [e_.subs(aa, 2) for e_ in (3 * aa - 1, aa ** 2 + 2, aa ** 2 - 2)] != sorted(M3.subs(aa, 2).eigenvals().keys()) and
   sorted(M3.subs(aa, 2).eigenvals().keys()) == [-3, 5])
grid = [R(k, 12) for k in range(-24, 25)]
ev_at = lambda t: list(M3.subs(aa, t).eigenvals().keys())
psd = [t for t in grid if all(e_ >= 0 for e_ in ev_at(t))]
pd = [t for t in grid if all(e_ > 0 for e_ in ev_at(t))]
nsd = [t for t in grid if all(e_ <= 0 for e_ in ev_at(t))]
ok("3a PSD exactly 1/3<=a<=1", psd == [t for t in grid if R(1, 3) <= t <= 1])
ok("3a PD exactly 1/3<a<1", pd == [t for t in grid if R(1, 3) < t < 1])
ok("3a NSD never", nsd == [])
ok("3a PSD distractors fail", R(1, 3) in psd and 2 not in psd and R(0) not in psd and R(-1) not in psd)
same("3a", numeric_answers(3, "א"), [0, min(ev_at(R(1, 2)))])

# Q3b
pts = [(1, 3), (3, 5), (-2, 5), (2, 2)]
Am = sp.Matrix([[px, 1] for px, _ in pts]); bm = sp.Matrix([py for _, py in pts])
sol = (Am.T * Am).LUsolve(Am.T * bm)
ok("3b normal matrix", Am.T * Am == sp.Matrix([[18, 4], [4, 4]]) and Am.T * bm == sp.Matrix([12, 15]))
same("3b", numeric_answers(3, "ב"), [(Am.T * Am)[0, 0], (Am.T * bm)[0], sol[0], sol[1]])
ok("3b m,n exact", sol == sp.Matrix([R(-3, 14), R(111, 28)]))

# Q4a
cnt = sum(1 for p in range(7) for q_ in range(7) for r in range(7) if p % 7 and r % 7)
H = [(p, q_, r) for p in range(7) for q_ in range(7) for r in range(7) if p and r]
same("4a1", numeric_answers(4, "א"), [len([p for p in range(7) if p]), 7, len(H)])
ok("4a1 every such matrix invertible", all((p * r) % 7 for p, q_, r in H))
order = lambda g, m: next(k for k in range(1, m) if pow(g, k, m) == 1)
D = sp.Matrix([[4, 0], [0, 3]])
ordD = next(k for k in range(1, 50) if (D ** k).applyfunc(lambda t: t % 7) == sp.eye(2))
same("4a2", numeric_answers(4, "ב"), [order(3, 7), order(4, 7), ordD])
ok("4a2 lcm", order(3, 7) * order(4, 7) // gcd(order(3, 7), order(4, 7)) == ordD == 6)
Mx = sp.Matrix([[1, 2], [0, 3]])
inv = Mx.inv_mod(7)
ok("4a3 inverse", inv == sp.Matrix([[1, 4], [0, 5]]))
same("4a3", numeric_answers(4, "ג"), [Mx.det() % 7, inv[1, 1], inv[0, 1]])

# Q4b
xs, k = sp.symbols("x k", real=True)
u_ = sp.Matrix([xs, 1]); v_k = sp.Matrix([1, k])
ok("4b <u,v> = x+k", u_.dot(v_k) == xs + k)
ok("4b |u|^2|v|^2 - <u,v>^2 = (xk-1)^2 >= 0", sp.expand(u_.dot(u_) * v_k.dot(v_k) - u_.dot(v_k) ** 2) == sp.expand((xs * k - 1) ** 2))
target_rhs = sp.expand((k ** 2 + 1) * (xs ** 2 + 1))
d1 = sp.Matrix([xs, k]).dot(sp.Matrix([1, 1]))
ok("4b distractor (x,k),(1,1) gives different bound", sp.expand(sp.Matrix([xs, k]).dot(sp.Matrix([xs, k])) * 2) != target_rhs)
ok("4b distractor (x,1),(k,1) gives different inner product", sp.Matrix([xs, 1]).dot(sp.Matrix([k, 1])) != xs + k)
ok("4b distractor (x,x^2),(1,k) gives different norm", sp.Matrix([xs, xs ** 2]).dot(sp.Matrix([xs, xs ** 2])) != xs ** 2 + 1)
f = lambda t, kk: (t + kk) ** 2 / (t ** 2 + 1)
same("4b", numeric_answers(4, "ד"), [(2 ** 2 + 1) * (1 + 3 ** 2)])
ok("4b example f(2)=5 <= 10", f(R(2), 3) == 5 <= 3 ** 2 + 1)
ok("4b inequality holds on grid", all(f(R(t, 3), kk) <= kk ** 2 + 1 for t in range(-30, 31) for kk in range(1, 8)))

# Q5a
A5 = sp.Matrix([[2, 0], [0, 2], [1, s3]])
AtA = A5.T * A5
ok("5a A^T A", AtA == sp.Matrix([[5, s3], [s3, 7]]))
evs = sorted([sp.simplify(e_) for e_ in AtA.eigenvals()], reverse=True)
ok("5a eigenvalues 8, 4", evs == [8, 4], str(evs))
v1 = sp.Matrix([R(1, 2), s3 / 2])
ok("5a v1 eigenvector of A^T A for 8", sp.simplify(AtA * v1 - 8 * v1) == sp.zeros(2, 1))
u1_ = A5 * v1 / (2 * sp.sqrt(2))
same("5a", numeric_answers(5, "א"), [evs[0], sp.sqrt(evs[1]), sp.N(u1_[2])])
ok("5a official: U Sigma V^T = A (third matrix printed is V^T)", sp.simplify(
    sp.Matrix([[sp.sqrt(2) / 4, -s3 / 2, -sp.sqrt(2) / 4], [sp.sqrt(6) / 4, R(1, 2), -sp.sqrt(6) / 4], [sp.sqrt(2) / 2, 0, sp.sqrt(2) / 2]])
    * sp.Matrix([[2 * sp.sqrt(2), 0], [0, 2], [0, 0]]) * sp.Matrix([[R(1, 2), s3 / 2], [-s3 / 2, R(1, 2)]]) - A5) == sp.zeros(3, 2))
ok("5a dims: V is 2x2 from A^T A, U is 3x3 from A A^T", AtA.shape == (2, 2) and (A5 * A5.T).shape == (3, 3))

# Q5b
x_ = sp.symbols("x_")
a1 = sp.solve_congruence((2, 1, 5)) if hasattr(sp, "solve_congruence") else None
a1 = [t for t in range(5) if (2 * t) % 5 == 1][0]
a2 = [t for t in range(11) if (3 * t) % 11 == 5][0]
x2 = [t for t in range(11) if (15 * t) % 11 == 1][0]
x1 = [t for t in range(5) if (33 * t) % 5 == 1][0]
x3 = [t for t in range(3) if (55 * t) % 3 == 1][0]
total = a1 * 33 * x1 + a2 * 15 * x2 + 2 * 55 * x3
sol5, mod5 = sp.ntheory.modular.crt([5, 11, 3], [a1, a2, 2])
ok("5b total 713", total == 713 and (x1, x2, x3) == (2, 3, 1))
same("5b", numeric_answers(5, "ב"), [a1, a2, x2, sol5])
ok("5b solves original system", (2 * sol5) % 5 == 1 and (3 * sol5) % 11 == 5 and sol5 % 3 == 2 and mod5 == 165)

print("ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
