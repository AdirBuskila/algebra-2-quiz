# -*- coding: utf-8 -*-
"""Learn-brief checks: orthogonality, projection, parseval_bessel, least_squares.
Run: PYTHONUTF8=1 py -I tools/verify/learn/check_geometry.py   (ASCII output, exit 1 on any failure)"""
import sys
import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational


def ip(A, B):
    """<A,B> = tr(B^T A) on M_2(R)"""
    return (B.T * A).trace()


def proj(v, basis, ipf=ip):
    """orthogonal projection of v onto Sp(basis) through the Gram matrix (works for dependent-free bases)"""
    G = sp.Matrix(len(basis), len(basis), lambda i, j: ipf(basis[i], basis[j]))
    r = sp.Matrix([ipf(v, b) for b in basis])
    c = G.LUsolve(r)
    out = sp.zeros(*v.shape)
    for ci, b in zip(c, basis):
        out += ci * b
    return out


# ---------------------------------------------------------------- orthogonality brief
ca = sp.Matrix([2, -1, 2])
cb = sp.Matrix([1, 2, 0])
ok("OR <alpha,beta>=0 for alpha=2u-v+2w, beta=u+2v (orthonormal u,v,w)", (ca.T * cb)[0] == 0)
ok("OR |alpha|^2=9, |beta|^2=5", (ca.T * ca)[0] == 9 and (cb.T * cb)[0] == 5)
A1 = sp.Matrix([[1, 1], [0, 0]])
B1 = sp.Matrix([[2, 0], [1, 1]])
U2 = B1 - ip(B1, A1) / ip(A1, A1) * A1
ok("OR GS in M2: u2 = [[1,-1],[1,1]]", U2 == sp.Matrix([[1, -1], [1, 1]]))
ok("OR GS: <u2,A1>=0, |A1|^2=2, |u2|^2=4", ip(U2, A1) == 0 and ip(A1, A1) == 2 and ip(U2, U2) == 4)
q1 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
q2 = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
q3 = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
ok("OR u u^T+v v^T+w w^T = I for an orthonormal basis of R^3",
   sp.simplify(q1 * q1.T + q2 * q2.T + q3 * q3.T - sp.eye(3)) == sp.zeros(3, 3))
Q = sp.Matrix.hstack(q1, q2, q3)
ok("OR Q^T Q = I and det Q = +-1", sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3) and abs(sp.simplify(Q.det())) == 1)
uu = sp.Matrix([1, 1]) / sp.sqrt(2)
vv = sp.Matrix([1, -1]) / sp.sqrt(2)
ok("OR v u^T + u v^T = diag(1,-1)", sp.simplify(vv * uu.T + uu * vv.T - sp.diag(1, -1)) == sp.zeros(2, 2))
ok("OR eigenvalues of 3 u u^T - 5 v v^T are 3 and -5",
   sorted(sp.simplify(3 * uu * uu.T + (-5) * vv * vv.T).eigenvals().keys()) == [-5, 3])
Qs = sp.Matrix([[0, 1], [1, 0]])
P = sp.eye(2) + Qs
ok("OR Q orthogonal+symmetric: Q^2=I and (I+Q)^2=2(I+Q) (example)", Qs * Qs == sp.eye(2) and P * P == 2 * P)
Hh = sp.eye(3) - 2 * sp.Matrix([1, 2, 2]) * sp.Matrix([1, 2, 2]).T / 9
ok("OR Householder H: orthogonal, symmetric, det -1", Hh.T * Hh == sp.eye(3) and Hh == Hh.T and Hh.det() == -1)
th = sp.symbols('theta', real=True)
Rot = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
ok("OR rotation: orthogonal, det 1", sp.simplify(Rot.T * Rot - sp.eye(2)) == sp.zeros(2, 2) and sp.simplify(Rot.det()) == 1)
a, b, x = sp.symbols('a b x', real=True)
ok("OR <ax+b, ax-b> on [0,1] = a^2/3 - b^2", sp.expand(sp.integrate((a * x + b) * (a * x - b), (x, 0, 1)) - (a ** 2 / 3 - b ** 2)) == 0)

# ---------------------------------------------------------------- projection brief
W1 = sp.Matrix([[1, 1], [0, 0]])
W2 = sp.Matrix([[1, 3], [1, 1]])
V = sp.Matrix([[2, 0], [3, 1]])
P_ = proj(V, [W1, W2])
ok("PR worked: proj = [[1/2,3/2],[1/2,1/2]]", P_ == sp.Matrix([[R(1, 2), R(3, 2)], [R(1, 2), R(1, 2)]]), str(P_.tolist()))
Bb2 = W2 - ip(W2, W1) / ip(W1, W1) * W1
ok("PR worked: GS gives [[-1,1],[1,1]]", Bb2 == sp.Matrix([[-1, 1], [1, 1]]))
ok("PR worked: <V,B1>=2, <V,B2>=2, |B2|^2=4", ip(V, W1) == 2 and ip(V, Bb2) == 2 and ip(Bb2, Bb2) == 4)
res = V - P_
ok("PR worked: residual orthogonal to W1, W2, B2", ip(res, W1) == 0 and ip(res, W2) == 0 and ip(res, Bb2) == 0)
ok("PR worked: Pythagoras |V|^2 = |P|^2 + |res|^2", ip(V, V) == ip(P_, P_) + ip(res, res),
   "%s=%s+%s" % (ip(V, V), ip(P_, P_), ip(res, res)))


def fip(f, g):
    return sp.integrate(f * g, (x, -1, 1))


ok("PR worked: |V|^2=14, |P|^2=3, |res|^2=11", (ip(V, V), ip(P_, P_), ip(res, res)) == (14, 3, 11))
ok("PR C[-1,1]: proj of x^2 on Sp{1,x} = 1/3", fip(x ** 2, 1) / fip(1, 1) + fip(x ** 2, x) / fip(x, x) * x == R(1, 3))
# 23A-B-Q2a: W = Sp{1,|x|}, GS gives e2 = |x| - 1/2
n2 = sp.integrate((-x - R(1, 2)) ** 2, (x, -1, 0)) + sp.integrate((x - R(1, 2)) ** 2, (x, 0, 1))
i2 = sp.integrate(x ** 2 * (-x - R(1, 2)), (x, -1, 0)) + sp.integrate(x ** 2 * (x - R(1, 2)), (x, 0, 1))
ok("PR 23A-B-Q2a: <|x|,1>=1 so |x| - 1/2 is orthogonal to 1",
   sp.integrate(-x, (x, -1, 0)) + sp.integrate(x, (x, 0, 1)) == 1 and fip(1, 1) == 2)
ok("PR 23A-B-Q2a: |e2|^2 = 1/6, <x^2,e2> = 1/6, proj = |x| - 1/6", n2 == R(1, 6) and i2 == R(1, 6) and R(1, 3) - R(1, 2) * (i2 / n2) == -R(1, 6))
vv3 = sp.Matrix([1, 2, 2]) / 3
Pm = vv3 * vv3.T
uu3 = sp.Matrix(sp.symbols('s1:4', real=True))
ok("PR P = v v^T (unit v): P^2=P and <u-Pu, v>=0", Pm * Pm == Pm and sp.simplify(((uu3 - Pm * uu3).T * vv3)[0]) == 0)
ok("PR 24A-A-Q1b answer [[1/3,1/3],[0,2/3]]",
   proj(sp.Matrix([[1, 1], [1, 0]]), [sp.eye(2), sp.Matrix([[0, 1], [0, 1]])]) == sp.Matrix([[R(1, 3), R(1, 3)], [0, R(2, 3)]]))
ok("PR 24B-B-Q1c answer [[1,1],[0,2]]",
   proj(sp.Matrix([[1, 1], [1, 2]]), [sp.eye(2), sp.Matrix([[0, 1], [0, 1]])]) == sp.Matrix([[1, 1], [0, 2]]))
ok("PR 24A-B-Q1b answer (three spanning matrices)",
   proj(sp.Matrix([[2, 1], [1, 2]]), [sp.Matrix([[1, -1], [0, 1]]), sp.Matrix([[0, 1], [0, 1]]), sp.Matrix([[1, 1], [1, 1]])])
   == sp.Matrix([[R(9, 5), R(9, 10)], [R(6, 5), R(21, 10)]]))
ok("PR 24B-A-Q1b answer (three spanning matrices)",
   proj(sp.Matrix([[2, 2], [0, 2]]), [sp.Matrix([[1, 1], [-1, 1]]), sp.Matrix([[0, 1], [0, 1]]), sp.Matrix([[1, 1], [0, 0]])])
   == sp.Matrix([[R(3, 2), R(5, 2)], [-R(1, 2), R(3, 2)]]))

# ---------------------------------------------------------------- parseval_bessel brief
g1 = sp.Matrix([1, 1, 0]) / sp.sqrt(2)
g2 = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
g3 = sp.Matrix([0, 0, 1])
v3 = sp.Matrix([3, 1, 2])
cs = [sp.simplify((v3.T * g)[0]) for g in (g1, g2, g3)]
ok("PB coefficients 2*sqrt2, sqrt2, 2", cs == [2 * sp.sqrt(2), sp.sqrt(2), 2])
ok("PB Parseval: 8+2+4 = 14 = |v|^2", sum(c ** 2 for c in cs) == 14 == (v3.T * v3)[0])
ok("PB Bessel for {g1,g2}: 10 <= 14, gap 4 = 2^2", cs[0] ** 2 + cs[1] ** 2 == 10 and 14 - 10 == 4 == cs[2] ** 2)
Pv = cs[0] * g1 + cs[1] * g2
ok("PB |v - Pv|^2 = 4", sp.simplify(((v3 - Pv).T * (v3 - Pv))[0]) == 4)
h1 = 1 / sp.sqrt(2)
h2 = sp.sqrt(R(3, 2)) * x
ok("PB C[-1,1]: 1/sqrt2 and sqrt(3/2) x are orthonormal",
   sp.integrate(h1 ** 2, (x, -1, 1)) == 1 and sp.integrate(h2 ** 2, (x, -1, 1)) == 1 and sp.integrate(h1 * h2, (x, -1, 1)) == 0)
cc = [sp.integrate(x ** 2 * h, (x, -1, 1)) for h in (h1, h2)]
ok("PB x^2: coefficients sqrt2/3 and 0, squares sum 2/9 <= |x^2|^2 = 2/5",
   [sp.simplify(c) for c in cc] == [sp.sqrt(2) / 3, 0] and sum(c ** 2 for c in cc) == R(2, 9) and sp.integrate(x ** 4, (x, -1, 1)) == R(2, 5))

# ---------------------------------------------------------------- least_squares brief: points (0,1),(1,2),(2,2),(3,4)
pts = [(0, 1), (1, 2), (2, 2), (3, 4)]
A = sp.Matrix([[p[0], 1] for p in pts])
bvec = sp.Matrix([p[1] for p in pts])
ok("LS worked: sums 6, 14, 9, 18",
   (sum(p[0] for p in pts), sum(p[0] ** 2 for p in pts), sum(p[1] for p in pts), sum(p[0] * p[1] for p in pts)) == (6, 14, 9, 18))
ok("LS worked: A^T A = [[14,6],[6,4]], A^T b = (18,9), det 20",
   A.T * A == sp.Matrix([[14, 6], [6, 4]]) and A.T * bvec == sp.Matrix([18, 9]) and (A.T * A).det() == 20)
xs = (A.T * A).LUsolve(A.T * bvec)
ok("LS worked: y = 0.9 x + 0.9", xs == sp.Matrix([R(9, 10), R(9, 10)]))
r = bvec - A * xs
ok("LS worked: residual (0.1,0.2,-0.7,0.4) and A^T r = 0",
   r == sp.Matrix([R(1, 10), R(2, 10), -R(7, 10), R(4, 10)]) and A.T * r == sp.zeros(2, 1))
ok("LS worked: forecast at x=4 is 4.5", xs[0] * 4 + xs[1] == R(9, 2))
ok("LS worked: pseudo-inverse formula agrees", (A.T * A).inv() * A.T * bvec == xs)
A2 = sp.Matrix([[1, -2], [-1, 2], [0, 3], [2, 5]])
b2 = sp.Matrix([3, 1, -4, 2])
ok("LS 23A-B-Q1a: A^T A = [[6,6],[6,42]] and x = (4/3,-1/3)",
   A2.T * A2 == sp.Matrix([[6, 6], [6, 42]]) and (A2.T * A2).LUsolve(A2.T * b2) == sp.Matrix([R(4, 3), -R(1, 3)]))
ok("LS 23A-B-Q1a: columns independent (rank 2)", A2.rank() == 2)
ta, tb, tt = sp.symbols('ta tb tt', positive=True)
ok("LS linearization ln(a e^{bt}) = ln a + b t", sp.simplify(sp.expand_log(sp.log(ta * sp.exp(tb * tt)), force=True) - (sp.log(ta) + tb * tt)) == 0)
sys.exit(1 if bad else 0)
