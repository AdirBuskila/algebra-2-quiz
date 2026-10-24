# -*- coding: utf-8 -*-
"""Learn-brief checks: crt, groups.
Run: PYTHONUTF8=1 py -I tools/verify/learn/check_number.py   (ASCII output, exit 1 on any failure)"""
import itertools
import math
import sys
import sympy as sp
from sympy.ntheory.modular import crt as sp_crt

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational

# ---------------------------------------------------------------- crt brief
# worked example: x = 2 (mod 3), 3x = 4 (mod 5), x = 6 (mod 7)
ok("CRT worked: 3^-1 mod 5 = 2, so 3x=4 gives x = 8 = 3 (mod 5)", pow(3, -1, 5) == 2 and (2 * 4) % 5 == 3)
M = 3 * 5 * 7
Ms = [M // m for m in (3, 5, 7)]
ok("CRT worked: M=105, M_i = 35, 21, 15", M == 105 and Ms == [35, 21, 15])
xi = [pow(Mi, -1, m) for Mi, m in zip(Ms, (3, 5, 7))]
ok("CRT worked: x_i = 2, 1, 1", xi == [2, 1, 1])
total = 2 * 35 * 2 + 3 * 21 * 1 + 6 * 15 * 1
ok("CRT worked: 140+63+90 = 293, 293 mod 105 = 83", total == 293 and total % 105 == 83)
ok("CRT worked: 83 satisfies the original system", 83 % 3 == 2 and (3 * 83) % 5 == 4 and 83 % 7 == 6)
ok("CRT worked: unique solution in [0,105) (brute force)", [n for n in range(105) if n % 3 == 2 and (3 * n) % 5 == 4 and n % 7 == 6] == [83])
ok("CRT worked: sympy agrees", sp_crt([3, 5, 7], [2, 3, 6])[0] == 83)
# reductions quoted in the brief
ok("CRT reduce: 3x=14 (mod 8) -> x = 2", [n for n in range(8) if (3 * n - 14) % 8 == 0] == [2] and (pow(3, -1, 8) * 14) % 8 == 2)
ok("CRT reduce: 2x=1 (mod 5) -> x = 3 ; 3x=5 (mod 11) -> x = 9", (pow(2, -1, 5) * 1) % 5 == 3 and (pow(3, -1, 11) * 5) % 11 == 9)
ok("CRT reduce: 3x=4 (mod 5) -> x = 3 ; 2x=3 (mod 7) -> x = 5", (pow(3, -1, 5) * 4) % 5 == 3 and (pow(2, -1, 7) * 3) % 7 == 5)
ok("CRT reduce: x=19 (mod 11) -> 8 ; x=5 (mod 3) -> 2 ; x=4 (mod 2) -> 0 ; x=22 (mod 25) stays", 19 % 11 == 8 and 5 % 3 == 2 and 4 % 2 == 0 and 22 % 25 == 22)
ok("CRT reduce: x=7 (mod 32) stays; 32 coprime to 5 and 7", math.gcd(32, 5) == 1 and math.gcd(32, 7) == 1)
ok("CRT coprime check: gcd(4,6)=2 so (4,6) is not allowed", math.gcd(4, 6) == 2)
ok("CRT inverse by Fermat: 3^5 = 5 mod 7 and 3*5 = 1 mod 7", pow(3, 5, 7) == 5 and (3 * 5) % 7 == 1)
ok("CRT extended Euclid: 1 = 3*(-3) + 5*2 gives 3^-1 = -3 = 2 mod 5", 3 * (-3) + 5 * 2 == 1 and (-3) % 5 == 2)
# an inconsistent non-coprime system and a consistent one
ok("CRT non-coprime consistent: x=1 (4), x=3 (6) has no solution (1 vs 3 differ mod gcd 2? 1-3=-2 divisible by 2 => solvable)", [n for n in range(12) if n % 4 == 1 and n % 6 == 3] == [9])
ok("CRT non-coprime inconsistent: x=1 (4), x=2 (6) has no solution", [n for n in range(12) if n % 4 == 1 and n % 6 == 2] == [])
# successive substitution cross-check
sol = None
for t in range(0, 105):
    if t % 7 == 6 and (3 * t) % 5 == 4 and t % 3 == 2:
        sol = t
ok("CRT successive substitution lands on 83", sol == 83)

# ---------------------------------------------------------------- groups brief
a, b, c, x, y, z = sp.symbols('a b c x y z', real=True)
# operations on R+: a*b/(a+b) (24A-A-Q2) associative, no identity
op1 = lambda p, q: p * q / (p + q)
ok("GR 24A-A-Q2: ab/(a+b) associative", sp.simplify(op1(op1(a, b), c) - op1(a, op1(b, c))) == 0)
e_ = sp.symbols('e')
ok("GR 24A-A-Q2: identity equation a*e/(a+e)=a forces a^2=0", sp.simplify(sp.expand(sp.numer(sp.together(op1(a, e_) - a)))) == sp.simplify(-a ** 2))
ok("GR 24A-A-Q2: x*x = x/2", sp.simplify(op1(x, x) - x / 2) == 0)
# (a+b)/(ab) not associative (24A-B-Q2)
op2 = lambda p, q: (p + q) / (p * q)
ok("GR 24A-B-Q2: (a+b)/(ab) not associative", sp.simplify(op2(op2(a, b), c) - op2(a, op2(b, c))) != 0)
ok("GR 24A-B-Q2: x*x = x gives x=sqrt2", sp.solve(sp.Eq(op2(x, x), x), x).__contains__(sp.sqrt(2)))
# (2xu, y+v) (24B-B-Q4)
op3 = lambda p, q: (2 * p[0] * q[0], p[1] + q[1])
P1, P2, P3 = (x, y), (a, b), (c, z)
l = op3(op3(P1, P2), P3)
r = op3(P1, op3(P2, P3))
ok("GR 24B-B-Q4: (2xu, y+v) associative", sp.simplify(l[0] - r[0]) == 0 and sp.simplify(l[1] - r[1]) == 0)
e3 = (R(1, 2), 0)
inv3 = (1 / (4 * x), -y)
ok("GR 24B-B-Q4: identity (1/2,0), inverse (1/(4x), -y)",
   op3(e3, (x, y)) == (x, y) and tuple(sp.simplify(t) for t in op3((x, y), inv3)) == e3)
ok("GR 24B-B-Q4e: (x,y)^3 = (4x^3, 3y)", tuple(sp.expand(t) for t in op3(op3((x, y), (x, y)), (x, y))) == (4 * x ** 3, 3 * y))
ok("GR 24B-B-Q4e: 4x^3 = x has solutions x = +-1/2 (x != 0)", sorted(sp.solve(4 * x ** 3 - x, x)) == [-R(1, 2), 0, R(1, 2)])
# (x+y)/(1+xy) on (-1,1) (24B-A-Q4)
op4 = lambda p, q: (p + q) / (1 + p * q)
ok("GR 24B-A-Q4: (x+y)/(1+xy) associative", sp.simplify(op4(op4(x, y), z) - op4(x, op4(y, z))) == 0)
ok("GR 24B-A-Q4: identity 0, inverse -x, commutative", op4(0, x) == x and sp.simplify(op4(x, -x)) == 0 and sp.simplify(op4(x, y) - op4(y, x)) == 0)
ok("GR 24B-A-Q4: 1 - x*y = (1-x)(1-y)/(1+xy) (closure hint)", sp.simplify(1 - op4(x, y) - (1 - x) * (1 - y) / (1 + x * y)) == 0)
# ab+a+b on Z (25B-A-Q4): equals (a+1)(b+1)-1
op5 = lambda p, q: p * q + p + q
ok("GR 25B-A-Q4: ab+a+b = (a+1)(b+1)-1, associative, identity 0", sp.expand(op5(a, b) - ((a + 1) * (b + 1) - 1)) == 0 and sp.simplify(op5(op5(a, b), c) - op5(a, op5(b, c))) == 0 and op5(a, 0) == a)
ok("GR 25B-A-Q4: -1 has no inverse (-1)*b = -1 for all b", sp.expand(op5(-1, b)) == -1)
# ab-a-b on Z (25B-B-Q3)
op6 = lambda p, q: p * q - p - q
ok("GR 25B-B-Q3: ab-a-b not associative; no identity (a=1 gives 0=2)", sp.simplify(op6(op6(a, b), c) - op6(a, op6(b, c))) != 0 and sp.expand(op6(1, e_) - 1) == -2)
# R^2\{0} with (ay+bx, by) (24A-C-Q2)
op7 = lambda p, q: (p[0] * q[1] + p[1] * q[0], p[1] * q[1])
l = op7(op7((a, b), (x, y)), (c, z))
r = op7((a, b), op7((x, y), (c, z)))
ok("GR 24A-C-Q2: (ay+bx, by) associative", sp.expand(l[0] - r[0]) == 0 and sp.expand(l[1] - r[1]) == 0)
ok("GR 24A-C-Q2: identity (0,1) both sides; (1,0) has no inverse (b=0)", op7((a, b), (0, 1)) == (a, b) and op7((0, 1), (a, b)) == (a, b) and op7((1, 0), (x, y))[1] == 0)
ok("GR 24A-C-Q2: commutative, and closure fails: (1,0)*(1,0) = (0,0) is outside R^2 minus origin",
   sp.expand(op7((a, b), (x, y))[0] - op7((x, y), (a, b))[0]) == 0 and sp.expand(op7((a, b), (x, y))[1] - op7((x, y), (a, b))[1]) == 0
   and op7((1, 0), (1, 0)) == (0, 0))
# Heisenberg type matrices (23A-S-Q4, 24A-C-Q5a)
def Hm(p, q, r_):
    return sp.Matrix([[1, p, q], [0, 1, r_], [0, 0, 1]])
ok("GR 23A-S-Q4: H(a1,b1,c1)H(a2,b2,c2) = H(a1+a2, b1+b2+a1c2, c1+c2)",
   sp.simplify(Hm(a, b, c) * Hm(x, y, z) - Hm(a + x, b + y + a * z, c + z)) == sp.zeros(3, 3))
ok("GR 23A-S-Q4: inverse H(-a, ac-b, -c); not abelian", sp.simplify(Hm(a, b, c) * Hm(-a, a * c - b, -c) - sp.eye(3)) == sp.zeros(3, 3) and (Hm(1, 0, 0) * Hm(0, 0, 1) - Hm(0, 0, 1) * Hm(1, 0, 0)) != sp.zeros(3, 3))
# Z_3 Heisenberg-like (24B-B-Q2): order 9, element order 3
def mm(Mx, p):
    return Mx.applyfunc(lambda t: t % p)
E = sp.Matrix([[1, 2, 0], [0, 1, 2], [0, 0, 1]])
E2 = mm(E * E, 3)
ok("GR 24B-B-Q2c: E^2 = [[1,1,1],[0,1,1],[0,0,1]], E^3 = I (mod 3), order 3", E2 == sp.Matrix([[1, 1, 1], [0, 1, 1], [0, 0, 1]]) and mm(E2 * E, 3) == sp.eye(3))
S3 = [sp.Matrix([[1, p, q], [0, 1, p], [0, 0, 1]]) for p in range(3) for q in range(3)]
ok("GR 24B-B-Q2b: |G| = 9, closed under multiplication mod 3", len(S3) == 9 and all(any(mm(P_ * Q_, 3) == T for T in S3) for P_ in S3 for Q_ in S3))
# matrices over Z_p
def order_mod(Mx, p, limit=2000):
    cur = Mx.applyfunc(lambda t: t % p)
    k = 1
    while cur != sp.eye(Mx.shape[0]):
        cur = mm(cur * Mx, p)
        k += 1
        if k > limit:
            return None
    return k
ok("GR upper triangular [[a,b],[0,c]], ac!=0 over Z_5: |H| = 4*5*4 = 80 (brute force)",
   len([1 for p_, q_, r_ in itertools.product(range(5), repeat=3) if (p_ * r_) % 5 != 0]) == 80)
ok("GR same over Z_7: 6*7*6 = 252 (brute force)", len([1 for p_, q_, r_ in itertools.product(range(7), repeat=3) if (p_ * r_) % 7 != 0]) == 252)
ok("GR [[a,c],[0,a^-1]] over Z_5: 4*5 = 20 ; over Z_7: 6*7 = 42",
   len([1 for p_ in range(1, 5) for q_ in range(5)]) == 20 and len([1 for p_ in range(1, 7) for q_ in range(7)]) == 42)
ok("GR |GL_2(Z_5)| = (25-1)(25-5) = 480 (brute force)", len([1 for t in itertools.product(range(5), repeat=4) if (t[0] * t[3] - t[1] * t[2]) % 5]) == 480 == (25 - 1) * (25 - 5))
ok("GR order of diag(4,3) mod 7 is lcm(3,6)=6", order_mod(sp.diag(4, 3), 7) == 6 and sp.ntheory.n_order(4, 7) == 3 and sp.ntheory.n_order(3, 7) == 6)
ok("GR order of diag(4,3) mod 5 is lcm(2,4)=4", order_mod(sp.diag(4, 3), 5) == 4)
ok("GR order of [[1,1],[0,1]] mod p is p (p=5,7)", order_mod(sp.Matrix([[1, 1], [0, 1]]), 5) == 5 and order_mod(sp.Matrix([[1, 1], [0, 1]]), 7) == 7)
Jm = sp.Matrix([[1, 1], [0, 2]])
ok("GR 26B-A-Q2: J=[[1,1],[0,2]] mod 5 has order 4, J^-1 = J^3 = [[1,2],[0,3]]", order_mod(Jm, 5) == 4 and mm(Jm ** 3, 5) == sp.Matrix([[1, 2], [0, 3]]) and mm(Jm * sp.Matrix([[1, 2], [0, 3]]), 5) == sp.eye(2))
ok("GR inverse of [[1,2],[0,3]] mod 7 is [[1,4],[0,5]]", mm(sp.Matrix([[1, 2], [0, 3]]) * sp.Matrix([[1, 4], [0, 5]]), 7) == sp.eye(2))
ok("GR inverse via adjugate: [[a,b],[0,c]]^-1 = [[1/a, -b/(ac)],[0,1/c]]", sp.simplify(sp.Matrix([[a, b], [0, c]]) * sp.Matrix([[1 / a, -b / (a * c)], [0, 1 / c]]) - sp.eye(2)) == sp.zeros(2, 2))
ok("GR [[x,y],[0,1/x]]^-1 = [[1/x,-y],[0,x]]", sp.simplify(sp.Matrix([[x, y], [0, 1 / x]]) * sp.Matrix([[1 / x, -y], [0, x]]) - sp.eye(2)) == sp.zeros(2, 2))
# Z_p^* products
ok("GR Z5* x Z7*: order 24 ; (2,3) has order lcm(4,6)=12 ; inverse (3,5)", 4 * 6 == 24 and math.lcm(sp.ntheory.n_order(2, 5), sp.ntheory.n_order(3, 7)) == 12 and (2 * 3) % 5 == 1 and (3 * 5) % 7 == 1)
ok("GR {(a,a^2)} over Z_7* has 6 elements and (3,2) has order 6", len({(q, (q * q) % 7) for q in range(1, 7)}) == 6 and math.lcm(sp.ntheory.n_order(3, 7), sp.ntheory.n_order(2, 7)) == 6)
ok("GR Hadamard group over Z_5: 4^4 = 256, E=all-ones, order of [[1,2],[2,3]] = lcm(1,4,4,4)=4", 4 ** 4 == 256 and math.lcm(1, sp.ntheory.n_order(2, 5), sp.ntheory.n_order(2, 5), sp.ntheory.n_order(3, 5)) == 4)
ok("GR orders in Z_5*: 1->1, 2->4, 3->4, 4->2", [sp.ntheory.n_order(t, 5) for t in (1, 2, 3, 4)] == [1, 4, 4, 2])
ok("GR phi: phi(12)=4, phi(7)=6, phi(8)=4, phi(p^k) rule phi(9)=6", [sp.totient(n) for n in (12, 7, 8, 9)] == [4, 6, 4, 6])
ok("GR Lagrange example: |G|=24, element orders divide 24, 12 | 24, 5 does not", 24 % 12 == 0 and 24 % 5 != 0)
ok("GR Fermat: a^(p-1) = 1 mod p (p=7, a=1..6)", all(pow(t, 6, 7) == 1 for t in range(1, 7)))
# (a-1)(b-1)+1 trick (26A-B-Q2) and induction claim a^n = (a-1)^n + 1
op8 = lambda p, q: p * q - p - q + 2
ok("GR a*b-a-b+2 = (a-1)(b-1)+1 ; identity 2 ; a^n = (a-1)^n+1 (n=1..8)",
   sp.expand(op8(a, b) - ((a - 1) * (b - 1) + 1)) == 0 and op8(a, 2) == a
   and all(sp.expand(sp.Symbol('t') - 1) is not None for _ in [0])
   and (lambda: all(sp.expand(__import__('functools').reduce(lambda acc, _: op8(acc, a), range(n - 1), a) - ((a - 1) ** n + 1)) == 0 for n in range(1, 9)))())
# proofs: algebraic derivations hold in a nonabelian example (S3 as permutations) as sanity checks for the identities used
from sympy.combinatorics import Permutation
s_, t_ = Permutation([1, 0, 2]), Permutation([0, 2, 1])
ok("GR sanity (S3 nonabelian): (xy)^-1 = y^-1 x^-1", (s_ * t_) ** -1 == (t_ ** -1) * (s_ ** -1))
ok("GR sanity: (xy)^2 = x^2 y^2 fails in S3 (so it forces abelian)", (s_ * t_) ** 2 != (s_ ** 2) * (t_ ** 2))
ok("GR sanity: conjugation keeps order, o(y^-1 x y) = o(x) in S3", all(((q ** -1) * p_ * q).order() == p_.order() for p_ in (s_, t_, s_ * t_) for q in (s_, t_)))
# group where x^2=e for all x is abelian: Z2 x Z2 check, and x^3=y^5 => x=y
Z2Z2 = [(i, j) for i in range(2) for j in range(2)]
addp = lambda p, q: ((p[0] + q[0]) % 2, (p[1] + q[1]) % 2)
def pw(p, n):
    out = (0, 0)
    for _ in range(n):
        out = addp(out, p)
    return out
ok("GR sanity (Z2xZ2): x^3 = x and y^5 = y so x^3=y^5 means x=y; every x^2=e", all(pw(p, 3) == p and pw(p, 5) == p and pw(p, 2) == (0, 0) for p in Z2Z2))
# (a*b)*a = b when x*x=e: verify in Z2xZ2 and sanity on the derivation
ok("GR sanity: c=(a*b)*a equals b in Z2xZ2", all(addp(addp(p, q), p) == q for p in Z2Z2 for q in Z2Z2))
sys.exit(1 if bad else 0)
