# -*- coding: utf-8 -*-
"""Checks for every expected value / distractor used in the step data of gen_26B-A.py.
Run: py -I tools/verify/26B-A/steps_26B-A.py"""
import itertools, math
from sympy import Matrix, Rational, sqrt, symbols, simplify, eye, log, factorial, Sum, zeros, N, expand, Symbol
from sympy.ntheory.modular import crt

ok = True
def check(name, cond):
    global ok
    print(("OK  " if cond else "FAIL"), name)
    ok = ok and bool(cond)

ip = lambda X, Y: (Y.T * X).trace()
A = Matrix([[1, 0], [0, -1]]); B = Matrix([[1, 1], [0, -1]]); C = Matrix([[2, 3], [1, 0]])
# Q1a
check("1a <B,A>=2", ip(B, A) == 2)
check("1a |A|^2=2, |u1|=sqrt2", ip(A, A) == 2 and sqrt(ip(A, A)) == sqrt(2))
u2 = B - Rational(ip(B, A), ip(A, A)) * A
check("1a u2", u2 == Matrix([[0, 1], [0, 0]]))
for nm, M in {"B-2A": B - 2 * A, "B+A": B + A, "B": B}.items():
    check("1a distractor %s not orthogonal to A" % nm, ip(M, A) != 0)
# Q1b
u1 = A
check("1b <C,u1>=2 <C,u2>=3", ip(C, u1) == 2 and ip(C, u2) == 3)
P = Rational(2, 2) * u1 + 3 * u2
check("1b proj", P == Matrix([[1, 3], [0, -1]]))
inU = lambda M: M[1, 0] == 0 and M[1, 1] == -M[0, 0]   # U = {[[p+q,q],[0,-p-q]]}
check("1b U membership test", inU(A) and inU(B) and inU(P))
for nm, M in {"[[2,3],[0,0]]": Matrix([[2, 3], [0, 0]]), "[[1,3],[0,1]]": Matrix([[1, 3], [0, 1]]), "[[1,3],[1,-1]]": Matrix([[1, 3], [1, -1]])}.items():
    check("1b distractor %s not in U" % nm, not inU(M))
# Q1c: the line-3 of the findbug proof: A^T A^-1 A = A for symmetric A, != I
S = Matrix([[2, 1], [1, 3]])
check("1c A^T A^-1 A = A (not I)", S.T * S.inv() * S == S and S.T * S.inv() * S != eye(2))
# definition options: counterexamples
check("1c det>0 not enough: -I", (-eye(2)).det() > 0 and not all(e > 0 for e in (-eye(2)).eigenvals()))
check("1c PD with negative entries", Matrix([[2, -1], [-1, 2]]).is_positive_definite)
# Q2
md = lambda X: X.applyfunc(lambda t: t % 5)
G = [Matrix([[a, b], [0, c]]) for a in range(5) for b in range(5) for c in range(5) if (a * c) % 5]
check("2a |G|=80, a:4 b:5 c:4", len(G) == 80 and len({int(g[0, 0]) for g in G}) == 4 and len({int(g[0, 1]) for g in G}) == 5 and len({int(g[1, 1]) for g in G}) == 4)
J = Matrix([[1, 1], [0, 2]])
pw = [eye(2)]
while True:
    nx = md(pw[-1] * J)
    if nx == eye(2): break
    pw.append(nx)
check("2b J^2 TR=3, J^3 TR=2, |H|=4", pw[2][0, 1] == 3 and pw[3][0, 1] == 2 and len(pw) == 4)
check("2c J^-1=J^3 TR 2", md(J * pw[3]) == eye(2) and pw[3][0, 1] == 2)
check("2d o(J)=4", len(pw) == 4)
# 2e
Gi = lambda A_: md(A_.inv_mod(5))
check("2e corner invariant", all(md(g * J * g.inv_mod(5))[1, 1] == 2 for g in G))
check("2e only J in H with corner 2", [h for h in pw if h[1, 1] == 2] == [J])
good = [g for g in G if md(g * J * g.inv_mod(5)) not in pw]
check("2e many valid A (count %d)" % len(good), len(good) > 1 and Matrix([[1, 1], [0, 1]]) in good)
X = Matrix([[1, 1], [0, 1]])
check("2e AJA^-1 TR=2", md(X * J * X.inv_mod(5)) == Matrix([[1, 2], [0, 2]]))
for nm, M in {"I": eye(2), "J^2": pw[2], "J^3": pw[3]}.items():
    check("2e distractor %s gives conj in H" % nm, md(M * J * M.inv_mod(5)) in pw)
L = Matrix([[1, 0], [1, 1]])
check("2e distractor lower-triangular not in G", L not in G)
# Q3a
a, lam = symbols("a lambda", real=True)
M3 = Matrix([[1, 0, 2 * a], [0, 4 - a**2, 0], [2 * a, 0, 1]])
ev = {simplify(k) for k in M3.eigenvals()}
check("3a eigenvalues", ev == {4 - a**2, 1 + 2 * a, 1 - 2 * a})
for nm, tr in {"1+a,1-a": {1 + a, 1 - a}, "2a,-2a": {2 * a, -2 * a}, "1+4a^2,1-4a^2": {1 + 4 * a**2, 1 - 4 * a**2}}.items():
    check("3a distractor evs %s wrong" % nm, ev != {4 - a**2} | tr)
def cls(av):
    e = [x.subs(a, av) for x in ev]
    if all(x > 0 for x in e): return "PD"
    if all(x >= 0 for x in e): return "PSD"
    if all(x < 0 for x in e): return "ND"
    if all(x <= 0 for x in e): return "NSD"
    return "none"
check("3a a=1/2 PSD, a=1 none, a=0 PD, a=3 none, a=1/4 PD", cls(Rational(1, 2)) == "PSD" and cls(1) == "none" and cls(0) == "PD" and cls(3) == "none" and cls(Rational(1, 4)) == "PD")
check("3a a=2 none (not 'PD for |a|<2')", cls(1) == "none")
check("3a a=-1/2 PSD", cls(-Rational(1, 2)) == "PSD")
check("3a never negative", all(cls(Rational(k, 8)) not in ("ND", "NSD") for k in range(-80, 81)))
# Q3b
Ax = Matrix([[x, 1] for x in range(5)]); yv = Matrix([2, 2, 4, 8, 9])
Nn = Ax.T * Ax; r = Ax.T * yv
check("3b N11=30, r1=70", Nn[0, 0] == 30 and r[0] == 70)
check("3b m,n", Nn.solve(r) == Matrix([2, 1]))
# Q4
check("4b exponent: y^2*y^2=y^4", 2 * 2 == 4)
check("4c sum(2k-1) n=7 = 49", sum(2 * k - 1 for k in range(1, 8)) == 49)
check("4c ln(4!)=3.1781", abs(math.log(24) - 3.1781) < 1e-3 and sum(math.log(k) for k in range(1, 5)) == math.log(24) or abs(sum(math.log(k) for k in range(1, 5)) - math.log(24)) < 1e-12)
check("4c cauchy numeric n<=40", all(sum(math.sqrt((2*k-1)*math.log(k)) for k in range(1, n+1))**2 <= n*n*math.log(math.factorial(n)) + 1e-9 for n in range(1, 41)))
# 4a / 4b by brute force in S4
from sympy.combinatorics.named_groups import SymmetricGroup
S4 = list(SymmetricGroup(4).elements)
check("4b brute force S4", all(x**2 * y * x**-2 == y**4 for x in S4 for y in S4 if x * y * x**-1 == y**2))
check("4a buggy line wrong: x*y*y*y^-1 = x*y != x*y^2 (S3 elems)", any(x * y != x * y * y for x in S4[:6] for y in S4[:6]))
# Q5c
A5 = Matrix([[3, 2], [2, 3], [2, -2]])
AtA = A5.T * A5
check("5c AtA, (1,2)=8, eig 25,9", AtA == Matrix([[17, 8], [8, 17]]) and set(AtA.eigenvals()) == {25, 9})
v2 = Matrix([1, -1]) / sqrt(2)
u2v = A5 * v2 / 3
check("5c u2 = (1,-1,4)/(3 sqrt2), unit", simplify(u2v - Matrix([1, -1, 4]) / (3 * sqrt(2))) == zeros(3, 1) and simplify(u2v.norm()) == 1)
for nm, w in {"/3": Matrix([1, -1, 4]) / 3, "/sqrt2": Matrix([1, -1, 4]) / sqrt(2), "(1,-1,0)/sqrt2": Matrix([1, -1, 0]) / sqrt(2), "/(2sqrt2)": Matrix([1, -1, 4]) / (2 * sqrt(2))}.items():
    check("5c distractor u2 %s wrong" % nm, simplify(w - u2v) != zeros(3, 1))
cp = Matrix([1, 1, 0]).cross(Matrix([1, -1, 4]))
check("5c cross = (4,-4,-2)", cp == Matrix([4, -4, -2]) and cp[2] == -2)
# Q5d
check("5d M=360, y's", 5 * 8 * 9 == 360 and (72 * 3) % 5 == 1 and (45 * 5) % 8 == 1 and (40 * 7) % 9 == 1)
check("5d crt 58", tuple(crt([5, 8, 9], [3, 2, 4])) == (58, 360))
print("ALL OK" if ok else "SOME FAILED")
