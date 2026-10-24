# -*- coding: utf-8 -*-
"""Solver checks for 26B-A (no official key). Run: py tools/verify/26B-A/solve_26B-A.py"""
import itertools, random
from sympy import Matrix, Rational, sqrt, symbols, simplify, eye, factor, solve, Symbol
from sympy.ntheory.modular import crt

ok = True
def check(name, cond):
    global ok
    print(("OK  " if cond else "FAIL") + " " + name)
    ok = ok and bool(cond)

ip = lambda X, Y: (Y.T * X).trace()

# Q1a Gram-Schmidt
A = Matrix([[1, 0], [0, -1]]); B = Matrix([[1, 1], [0, -1]])
u1 = A
u2 = B - ip(B, u1) / ip(u1, u1) * u1
check("Q1a <B,A>=2, ||A||^2=2", ip(B, A) == 2 and ip(A, A) == 2)
check("Q1a u2 = [[0,1],[0,0]]", u2 == Matrix([[0, 1], [0, 0]]))
check("Q1a orthogonal", ip(u1, u2) == 0 and ip(u2, u2) == 1)
# Q1b projection
C = Matrix([[2, 3], [1, 0]])
P = ip(C, u1) / ip(u1, u1) * u1 + ip(C, u2) / ip(u2, u2) * u2
check("Q1b proj = [[1,3],[0,-1]]", P == Matrix([[1, 3], [0, -1]]))
check("Q1b residual orthogonal to A,B", ip(C - P, A) == 0 and ip(C - P, B) == 0)

# Q1c random numeric sanity (the proof is algebraic)
for _ in range(20):
    M = Matrix(3, 3, lambda i, j: random.randint(-3, 3))
    S = M.T * M + eye(3)
    for T in (S + S**2, S + S.inv()):
        check_pd = T == T.T and all(T[:k, :k].det() > 0 for k in (1, 2, 3))
        if not check_pd:
            check("Q1c sample PD", False)
check("Q1c random samples PD (Sylvester)", True)

# Q2 group of invertible upper-triangular over Z5
G = [Matrix([[a, b], [0, c]]) for a in range(1, 5) for b in range(5) for c in range(1, 5)]
check("Q2.1 |G|=80", len(G) == 80)
md = lambda X: X.applyfunc(lambda t: t % 5)
J = Matrix([[1, 1], [0, 2]])
pw = [eye(2)]
while True:
    nx = md(pw[-1] * J)
    if nx == eye(2): break
    pw.append(nx)
check("Q2.2 H elements", pw == [eye(2), J, Matrix([[1, 3], [0, 4]]), Matrix([[1, 2], [0, 3]])])
check("Q2.4 |H|=4", len(pw) == 4)
Jinv = Matrix([[1, 2], [0, 3]])
check("Q2.3 J^-1", md(J * Jinv) == eye(2) and md(Jinv * J) == eye(2))
X = Matrix([[1, 1], [0, 1]]); Xinv = Matrix([[1, 4], [0, 1]])
check("Q2.5 X^-1", md(X * Xinv) == eye(2))
conj = md(X * J * Xinv)
check("Q2.5 XJX^-1 = [[1,2],[0,2]] not in H", conj == Matrix([[1, 2], [0, 2]]) and conj not in pw)
check("Q2.5 H = {[[1,c-1],[0,c]]}", all(h[0, 0] == 1 and (h[0, 1] - h[1, 1] + 1) % 5 == 0 for h in pw))

# Q3a
a, lam = symbols("a lambda", real=True)
M3 = Matrix([[1, 0, 2 * a], [0, 4 - a**2, 0], [2 * a, 0, 1]])
cp = factor(M3.charpoly(lam).as_expr())
print("   charpoly:", cp)
check("Q3a eigenvalues", __import__("sympy").expand((lam * eye(3) - M3).det() -(lam - (4 - a**2)) * (lam - (1 + 2*a)) * (lam - (1 - 2*a))) == 0)
def cls(av):
    e = [x.subs(a, av) for x in (4 - a**2, 1 + 2 * a, 1 - 2 * a)]
    if all(x > 0 for x in e): return "PD"
    if all(x >= 0 for x in e): return "PSD"
    if all(x < 0 for x in e): return "ND"
    if all(x <= 0 for x in e): return "NSD"
    return "none"
grid = [Rational(k, 8) for k in range(-40, 41)]
def expect(av):
    if abs(av) < Rational(1, 2): return "PD"
    if abs(av) == Rational(1, 2): return "PSD"
    return "none"
check("Q3a classification on grid", all(cls(v) == expect(v) for v in grid))

# Q3b
Ax = Matrix([[x, 1] for x in range(5)]); yv = Matrix([2, 2, 4, 8, 9])
N = Ax.T * Ax; r = Ax.T * yv
sol = N.solve(r)
check("Q3b normal eq [[30,10],[10,5]],[70,25]", N == Matrix([[30, 10], [10, 5]]) and r == Matrix([70, 25]))
check("Q3b y=2x+1", sol == Matrix([2, 1]))

# Q4: free-group style sanity on S3 for 4b (identity xyx^-1=y^2 => x^2yx^-2=y^4) by brute force in S_4
from sympy.combinatorics import Permutation
from sympy.combinatorics.named_groups import SymmetricGroup
S4 = list(SymmetricGroup(4).elements)
bad = 0
for x in S4:
    for y in S4:
        if x * y * x**-1 == y**2:
            if x**2 * y * x**-2 != y**4: bad += 1
check("Q4b brute force in S4", bad == 0)

# Q4c numeric for n=1..30
import math
check("Q4c numeric n<=30", all(sum(math.sqrt((2*k-1)*math.log(k)) for k in range(1, n+1))**2 <= n*n*math.log(math.factorial(n)) + 1e-9 for n in range(1, 31)))
check("Q4c sum(2k-1)=n^2", all(sum(2*k-1 for k in range(1, n+1)) == n*n for n in range(1, 50)))

# Q5c SVD
A5 = Matrix([[3, 2], [2, 3], [2, -2]])
check("Q5c A^TA", A5.T * A5 == Matrix([[17, 8], [8, 17]]))
U = Matrix([[1/sqrt(2), 1/(3*sqrt(2)), Rational(2, 3)],
            [1/sqrt(2), -1/(3*sqrt(2)), -Rational(2, 3)],
            [0, 4/(3*sqrt(2)), -Rational(1, 3)]])
S = Matrix([[5, 0], [0, 3], [0, 0]])
V = Matrix([[1, 1], [1, -1]]) / sqrt(2)
check("Q5c U orthogonal", simplify(U.T * U) == eye(3))
check("Q5c V orthogonal", simplify(V.T * V) == eye(2))
check("Q5c A = U S V^T", simplify(U * S * V.T - A5) == Matrix.zeros(3, 2))

# Q5d CRT
check("Q5d inverses", (72*3) % 5 == 1 and (45*5) % 8 == 1 and (40*7) % 9 == 1)
check("Q5d sum 2218", 3*72*3 + 2*45*5 + 4*40*7 == 2218 and 2218 % 360 == 58)
check("Q5d sympy crt", tuple(crt([5, 8, 9], [3, 2, 4])) == (58, 360))

print("ALL OK" if ok else "SOME FAILED")
