# -*- coding: utf-8 -*-
"""sympy / brute-force checks for sitting 23A-B (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/23A-B/check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import math
import random
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: least squares A x = b
A = sp.Matrix([[1, -2], [-1, 2], [0, 3], [2, 5]])
b = sp.Matrix([3, 1, -4, 2])
ok("Q1a A^T A = [[6,6],[6,42]]", A.T * A == sp.Matrix([[6, 6], [6, 42]]))
ok("Q1a A^T b = (6,-6)", A.T * b == sp.Matrix([6, -6]))
sol = (A.T * A).LUsolve(A.T * b)
ok("Q1a m=4/3 n=-1/3", sol == sp.Matrix([sp.Rational(4, 3), sp.Rational(-1, 3)]), str(list(sol)))

# ---- Q1b: sum sqrt(ln k ln(n-k+1)) <= ln(n!)
for n in range(1, 40):
    lhs = sum(math.sqrt(math.log(k) * math.log(n - k + 1)) for k in range(1, n + 1))
    rhs = math.log(math.factorial(n))
    if lhs > rhs + 1e-9:
        ok("Q1b n=%d" % n, False)
ok("Q1b inequality holds n=1..39", True)

# ---- Q2a: projection of x^2 onto Sp{1,|x|} in C[-1,1]
x = sp.symbols("x", real=True)
ip = lambda f, g: sp.integrate(f * g, (x, 0, 1)) + sp.integrate(f.subs(x, -x) * g.subs(x, -x), (x, 0, 1))
# work on [-1,1] by splitting: f(x) and g(x) given as expressions in x for x>=0, evaluated at -x for x<0
# |x| = x for x>=0 and also x after substituting -x -> |x| written as x on both halves
one = sp.Integer(1)
ab = x  # |x| on the positive half; on the negative half |(-x)| = x as well (even function)
h = x**2  # even
ip_even = lambda f, g: 2 * sp.integrate(f * g, (x, 0, 1))  # all functions here are even
n1 = ip_even(one, one)
ok("Q2a ||1||^2 = 2", n1 == 2)
c = ip_even(ab, one) / n1  # <|x|,1>/2
ok("Q2a <|x|,1>/||1||^2 = 1/2", c == sp.Rational(1, 2))
e2 = ab - c
ok("Q2a ||e2||^2 = 1/6", ip_even(e2, e2) == sp.Rational(1, 6))
proj = ip_even(h, one) / n1 + ip_even(h, e2) / ip_even(e2, e2) * e2
ok("Q2a proj = |x| - 1/6", sp.simplify(proj - (x - sp.Rational(1, 6))) == 0, str(sp.simplify(proj)))
# residual orthogonal to both spanning vectors
res = h - proj
ok("Q2a residual perp 1 and |x|", ip_even(res, one) == 0 and ip_even(res, ab) == 0)

# ---- Q2b: |H| for H = {[[a,c],[0,b]] over Z5, a b != 0}
H = [(a, c, bb) for a in range(5) for c in range(5) for bb in range(5) if (a * bb) % 5 != 0]
ok("Q2b |H| = 80", len(H) == 80, str(len(H)))
# H is closed under multiplication and inversion mod 5 (sanity: it is a subgroup of GL2(Z5))
def mul(p, q):
    a, c, b = p
    a2, c2, b2 = q
    return ((a * a2) % 5, (a * c2 + c * b2) % 5, (b * b2) % 5)


Hs = set(H)
ok("Q2b H closed under product", all(mul(p, q) in Hs for p in H for q in H))
GL = [(a, b_, c, d) for a in range(5) for b_ in range(5) for c in range(5) for d in range(5) if (a * d - b_ * c) % 5 != 0]
ok("Q2b |GL2(Z5)| = 480 (so [G:H] = 6)", len(GL) == 480)

# ---- Q3a: orthogonal diagonalization of [[3,1,1],[1,3,1],[1,1,3]]
A3 = sp.Matrix([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
ok("Q3a eigenvalues 5, 2, 2", A3.eigenvals() == {5: 1, 2: 2}, str(A3.eigenvals()))
s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
P = sp.Matrix([[1 / s3, -1 / s2, 1 / s6], [1 / s3, 1 / s2, 1 / s6], [1 / s3, 0, -2 / s6]])
D = sp.diag(5, 2, 2)
ok("Q3a P orthogonal", sp.simplify(P.T * P) == sp.eye(3))
ok("Q3a A = P D P^T", sp.simplify(P * D * P.T - A3) == sp.zeros(3, 3))
lam = sp.symbols("lambda")
ok("Q3a char poly (x-2)^2 (x-5)", sp.expand(A3.charpoly(lam).as_expr() - (lam - 2)**2 * (lam - 5)) == 0)

# ---- Q3b: polarization identity
u = sp.Matrix(sp.symbols("u1 u2 u3"))
v = sp.Matrix(sp.symbols("v1 v2 v3"))
nsq = lambda w: w.dot(w)
ok("Q3b <u,v> = 1/4(|u+v|^2-|u-v|^2) (R^3 instance)", sp.expand(sp.Rational(1, 4) * (nsq(u + v) - nsq(u - v)) - u.dot(v)) == 0)

# ---- Q4a: x*x=e, c=(a*b)*a  ->  c=b : brute force over small groups (Z2^k) and check chain of equalities symbolically n/a
# check on every element of Z2^3
els = list(itertools.product([0, 1], repeat=3))
op = lambda p, q: tuple((s + t) % 2 for s, t in zip(p, q))
ok("Q4a c=b on Z2^3", all(op(op(a_, b_), a_) == b_ for a_ in els for b_ in els))

# ---- Q4b: B=[[4,5],[5,6]] ; x^T B x < 0 at the point (-5,4)
B = sp.Matrix([[4, 5], [5, 6]])
xv = sp.Matrix([-5, 4])
ok("Q4b (-5,4): x^T B x = -4 < 0", (xv.T * B * xv)[0] == -4)
t = sp.symbols("t")
ok("Q4b 2t^2+5t+3 roots -3/2, -1", sp.solve(2 * t**2 + 5 * t + 3, t) == [-sp.Rational(3, 2), -1])
ok("Q4b B indefinite (det<0)", B.det() < 0)

# ---- Q5a: SVD of [[1,0],[0,3],[0,4]]
A5 = sp.Matrix([[1, 0], [0, 3], [0, 4]])
ok("Q5a A^T A eigenvalues 25, 1", A5.T * A5 == sp.diag(1, 25))
U = sp.Matrix([[0, 1, 0], [sp.Rational(3, 5), 0, -sp.Rational(4, 5)], [sp.Rational(4, 5), 0, sp.Rational(3, 5)]])
S = sp.Matrix([[5, 0], [0, 1], [0, 0]])
V = sp.Matrix([[0, 1], [1, 0]])
ok("Q5a U orthogonal", U.T * U == sp.eye(3))
ok("Q5a A = U S V^T", U * S * V.T == A5)

# ---- Q5b: CRT x=4(5), 3(7), 2(4)
sols = [v_ for v_ in range(140) if v_ % 5 == 4 and v_ % 7 == 3 and v_ % 4 == 2]
ok("Q5b unique solution 94 mod 140", sols == [94], str(sols))
ok("Q5b x1,x2,x3 = 2,6,3", (28 * 2) % 5 == 1 and (20 * 6) % 7 == 1 and (35 * 3) % 4 == 1)
ok("Q5b sum 4*28*2+3*20*6+2*35*3 = 794 = 94 mod 140", 4 * 28 * 2 + 3 * 20 * 6 + 2 * 35 * 3 == 794 and 794 % 140 == 94)

print("DONE", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
