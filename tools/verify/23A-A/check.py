# -*- coding: utf-8 -*-
r"""sympy / brute-force checks for sitting 23A-A (algebra-2). Run: PYTHONUTF8=1 py -I tools/verify/23A-A/check.py
Prints ASCII only. Exit code 1 on any mismatch."""
import itertools
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: least squares line through (1,20),(2,24),(3,31),(4,32), forecast x=5
X = sp.Matrix([[1, 1], [2, 1], [3, 1], [4, 1]])
y = sp.Matrix([20, 24, 31, 32])
ok("Q1a X^T X = [[30,10],[10,4]]", X.T * X == sp.Matrix([[30, 10], [10, 4]]))
ok("Q1a X^T y = (289,107)", X.T * y == sp.Matrix([289, 107]))
sol = (X.T * X).solve(X.T * y)
ok("Q1a b = 16", sol[1] == 16, str(sol[1]))
# official prints a = 21.5 (slip; 21.5 is a*5); the correct slope is 43/10
ok("Q1a a = 43/10 (official prints 21.5: slip)", sol[0] == sp.Rational(43, 10), str(sol[0]))
ok("Q1a forecast y(5) = 37.5 (official final is right)", sol[0] * 5 + sol[1] == sp.Rational(75, 2))

# ---- Q1b: projection onto W = Sp{w1,w2} in M2(R) with <A,B> = tr(B^T A)
def ip(A, B):
    return (B.T * A).trace()


w1 = sp.Matrix([[1, 1], [0, 0]])
w2 = sp.Matrix([[1, 3], [1, 1]])
v = sp.Matrix([[1, 2], [3, 0]])
ok("Q1b <w1,w2> = 4", ip(w2, w1) == 4)
u1 = w1
u2 = w2 - ip(w2, u1) / ip(u1, u1) * u1
ok("Q1b u2 = [[-1,1],[1,1]]", u2 == sp.Matrix([[-1, 1], [1, 1]]), str(u2))
ok("Q1b <u1,u2> = 0", ip(u1, u2) == 0)
ok("Q1b <v,u1> = 3, ||u1||^2 = 2", ip(v, u1) == 3 and ip(u1, u1) == 2)
ok("Q1b <v,u2> = 4, ||u2||^2 = 4", ip(v, u2) == 4 and ip(u2, u2) == 4)
proj = ip(v, u1) / ip(u1, u1) * u1 + ip(v, u2) / ip(u2, u2) * u2
ok("Q1b proj = (1/2)[[1,5],[2,2]]", proj == sp.Rational(1, 2) * sp.Matrix([[1, 5], [2, 2]]), str(proj))
# cross-check by normal equations
a, b = sp.symbols("a b")
p = a * w1 + b * w2
res = v - p
s = sp.solve([ip(res, w1), ip(res, w2)], [a, b])
ok("Q1b proj via normal equations", sp.simplify(s[a] * w1 + s[b] * w2 - proj) == sp.zeros(2, 2))
# the printed middle matrix (2 -2; 3 2) is a slip: u2^T v = (2 -2; 4 2), trace 4 either way
ok("Q1b u2^T v = [[2,-2],[4,2]] (official prints 3: slip, trace same)", u2.T * v == sp.Matrix([[2, -2], [4, 2]]))

# ---- Q2a: <f,g> = int_0^1 e^x f g dx is an inner product on C[0,1]  (spot-check with sympy)
x = sp.symbols("x")
f, g = x ** 2 + 1, sp.cos(x)
I = lambda p_, q_: sp.integrate(sp.exp(x) * p_ * q_, (x, 0, 1))
ok("Q2a symmetric", sp.simplify(I(f, g) - I(g, f)) == 0)
ok("Q2a <f,f> > 0 on a sample", sp.N(I(f, f)) > 0)
ok("Q2a linear in 1st slot (alpha=3)", sp.simplify(I(3 * f, g) - 3 * I(f, g)) == 0)

# ---- Q2b: order of H = <diag(4,3)> in GL2(Z5)
M = sp.Matrix([[4, 0], [0, 3]])
pw = []
cur = sp.eye(2)
for n in range(1, 13):
    cur = (cur * M).applyfunc(lambda t: t % 5)
    pw.append(cur)
first = [i + 1 for i, m in enumerate(pw) if m == sp.eye(2)][0]
ok("Q2b order of diag(4,3) = 4", first == 4, str(first))
ok("Q2b powers 1..4", pw[0] == sp.Matrix([[4, 0], [0, 3]]) and pw[1] == sp.Matrix([[1, 0], [0, 4]])
   and pw[2] == sp.Matrix([[4, 0], [0, 2]]) and pw[3] == sp.eye(2))

# ---- Q3a: A = [[a,0,1],[0,2a,0],[1,0,a]]
t = sp.symbols("t", real=True)
A = sp.Matrix([[t, 0, 1], [0, 2 * t, 0], [1, 0, t]])
ev = A.eigenvals()
ok("Q3a eigenvalues {2a, a-1, a+1}", set(ev.keys()) == {2 * t, t - 1, t + 1}, str(ev))
for tv, cls in [(2, "PD"), (1, "PSD"), (0, "none"), (sp.Rational(1, 2), "none"), (-1, "NSD"), (-2, "ND")]:
    Ev = list(A.subs(t, tv).eigenvals().keys())
    pd = all(e > 0 for e in Ev)
    psd = all(e >= 0 for e in Ev)
    nd = all(e < 0 for e in Ev)
    nsd = all(e <= 0 for e in Ev)
    got = "PD" if pd else "PSD" if psd else "ND" if nd else "NSD" if nsd else "none"
    ok("Q3a a=%s -> %s" % (tv, cls), got == cls, got)

# ---- Q3b: orthonormal u,v,w ; alpha = u+2v+w, beta = u-w
c_a = sp.Matrix([1, 2, 1])
c_b = sp.Matrix([1, 0, -1])
ok("Q3b1 <alpha,beta> = 0 (orthonormal coordinates)", (c_a.T * c_b)[0] == 0)
ok("Q3b2 ||alpha|| = sqrt6, ||beta|| = sqrt2", sp.sqrt((c_a.T * c_a)[0]) == sp.sqrt(6) and sp.sqrt((c_b.T * c_b)[0]) == sp.sqrt(2))

# ---- Q4: (a,b)*(x,y) = (ay+bx, by) on R^2 \ {0}
def star(p1, p2):
    return (p1[0] * p2[1] + p1[1] * p2[0], p1[1] * p2[1])


a_, b_, x_, y_ = sp.symbols("a b x y")
ok("Q4a1 commutative", all(sp.simplify(l - r) == 0 for l, r in zip(star((a_, b_), (x_, y_)), star((x_, y_), (a_, b_)))))
e = (0, 1)
ok("Q4a2 identity (0,1)", all(sp.simplify(l - r) == 0 for l, r in zip(star((a_, b_), e), (a_, b_))))
inv = sp.solve([sp.Eq(a_ * y_ + b_ * x_, 0), sp.Eq(b_ * y_, 1)], [x_, y_], dict=True)[0]
ok("Q4a3 inverse (-a/b^2, 1/b)", sp.simplify(inv[x_] + a_ / b_ ** 2) == 0 and sp.simplify(inv[y_] - 1 / b_) == 0)
ok("Q4a3 (5,0) has no inverse: (5,0)*(x,y) = (5y,0) != (0,1)", star((5, 0), (x_, y_))[1] == 0)
# extra (not in the official): closure fails, (1,0)*(1,0) = (0,0)
ok("Q4a3 closure also fails ((1,0)*(1,0) = (0,0))", star((1, 0), (1, 0)) == (0, 0))
# Q4b
ok("Q4b (ab+ba)^2 <= (a^2+b^2)^2 on grid", all((2 * p * q) ** 2 <= (p * p + q * q) ** 2 for p in range(-9, 10) for q in range(-9, 10)))

# ---- Q5b: CRT 2x=1 (3), x=3 (5), x=4 (7)
sol_crt = [n for n in range(105) if (2 * n) % 3 == 1 and n % 5 == 3 and n % 7 == 4]
ok("Q5b x = 53 mod 105 (unique)", sol_crt == [53], str(sol_crt))
ok("Q5b M_i = 35,21,15 ; x_i = 2,1,1", (35 * 2) % 3 == 1 and 21 % 5 == 1 and 15 % 7 == 1)
ok("Q5b 2*35*2+3*21*1+4*15*1 = 263 = 53 mod 105", 2 * 35 * 2 + 3 * 21 + 4 * 15 == 263 and 263 % 105 == 53)

# ---- Q5a (SVD of [[-1,1],[-1,1],[1,1]]): NO official key -> held; computed only to confirm it is well posed
S = sp.Matrix([[-1, 1], [-1, 1], [1, 1]])
print("INFO Q5a A^T A =", (S.T * S).tolist(), "eigs", (S.T * S).eigenvals())

print("RESULT", "FAIL " + ", ".join(bad) if bad else "all OK")
sys.exit(1 if bad else 0)
