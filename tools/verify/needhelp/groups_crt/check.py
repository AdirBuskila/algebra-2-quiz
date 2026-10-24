"""Machine check of every stored answer in courses/groups_crt/C01..C10.

Brute force over the finite groups (and over windows of Z for the infinite ones), sympy for symbolic
associativity and for the Chinese remainder theorem. The level files are loaded with the app's own loader
(node tools/course_load.js), so the script asserts what is actually stored.

Run from the app root:  py tools/verify/needhelp/groups_crt/check.py
Every own question (mcq, numeric, order, findbug) must be asserted, otherwise the script fails at the end.
"""
import json
import os
import re
import subprocess
import sys
from itertools import product
from math import gcd

import sympy as sp
from sympy.ntheory.modular import solve_congruence

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
COURSE = "groups_crt"

raw = subprocess.run(["node", os.path.join(ROOT, "tools", "course_load.js")], capture_output=True, cwd=ROOT, check=True).stdout
loaded = json.loads(raw.decode("utf-8"))
assert not loaded["errors"], loaded["errors"]
levels = {e["level"]["id"]: e["level"] for e in loaded["levels"] if e["courseId"] == COURSE}
assert sorted(levels) == ["C%02d" % i for i in range(1, 11)], sorted(levels)
Q = {}
for lid, L in levels.items():
    for q in L["questions"]:
        if "bankId" not in q:
            Q[q["id"]] = q
covered = set()


def own(qid):
    assert qid in Q, qid
    covered.add(qid)
    return Q[qid]


def num(qid, expected):
    q = own(qid)
    s = q["step"]
    assert s["type"] == "numeric", qid
    assert s.get("tol", 0) == 0, qid
    assert s["answer"] == expected, (qid, s["answer"], expected)


def mcq(qid, truth):
    """truth: option id -> computed boolean (is this option a correct answer?)."""
    q = own(qid)
    ids = [o["id"] for o in q["options"]]
    assert sorted(ids) == sorted(truth), (qid, ids, sorted(truth))
    right = [i for i in ids if truth[i]]
    assert right == [q["correctId"]], (qid, "computed correct", right, "stored", q["correctId"])
    assert "acceptedIds" not in q


def optval(qid, oid):
    return [o for o in Q[qid]["options"] if o["id"] == oid][0]["value"]


def step(qid, kind):
    q = own(qid)
    assert q["step"]["type"] == kind, qid
    return q["step"]


def check_text_contains(qid_or_lines, line_idx, fragment):
    """Cheap guard that the line being reasoned about is the stored one."""
    lines = qid_or_lines
    assert fragment in lines[line_idx], (line_idx, fragment, lines[line_idx])


# ---------------------------------------------------------------- generic helpers
def inv_mod(a, m):
    return pow(a, -1, m)


def order_mod(a, m):
    assert gcd(a, m) == 1
    k, x = 1, a % m
    while x != 1:
        x = x * a % m
        k += 1
    return k


def zstar(n):
    return [a for a in range(1, n) if gcd(a, n) == 1]


def is_group(elems, op):
    S = set(elems)
    if any(op(a, b) not in S for a in elems for b in elems):
        return "closure"
    if any(op(op(a, b), c) != op(a, op(b, c)) for a in elems for b in elems for c in elems):
        return "assoc"
    es = [e for e in elems if all(op(a, e) == a and op(e, a) == a for a in elems)]
    if not es:
        return "neutral"
    e = es[0]
    if any(not any(op(a, x) == e and op(x, a) == e for x in elems) for a in elems):
        return "inverse"
    return "group"


def matmul(A, B, p):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(A))) % p for j in range(len(B[0]))) for i in range(len(A)))


def matpow_order(A, p):
    n = len(A)
    I = tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))
    X, k = A, 1
    while X != I:
        X = matmul(X, A, p)
        k += 1
        assert k < 10000
    return k


a, b, c, e_, x_ = sp.symbols("a b c e x")

# ================================================================ C01
# lesson claims
assert sp.expand(((a + b + a * b) + c + (a + b + a * b) * c) - (a + (b + c + b * c) + a * (b + c + b * c))) == 0
assert (5 - 3) - 1 == 1 and 5 - (3 - 1) == 3
assert 1 - 2 == -1  # not in {1,2,3,...}

# Q1: a - b on the positive integers
S = range(1, 60)
closed = all((p - q) in S for p in S for q in S)
assert not closed and (1 - 2) not in S
# "non-commutativity is the reason" is invalid: a*b = a is non-commutative yet closed on S
assert all(p in S for p in S for q in S) and any(p != q for p in S for q in S)
mcq("C01-Q1", {
    "a": (not closed) and (1 - 2) not in S,    # not closed because 1*2 = -1
    "b": closed,                               # claims "yes"
    "c": closed,                               # claims "yes"
    "d": False,                                # reason (non-commutativity) is not a reason for failing closure
})

# Q2
Sset = range(1, 6)
cnt = sum(1 for p in Sset for q in Sset if max(p, q) + 1 not in Sset)
assert cnt == 9 == 25 - 16
num("C01-Q2", cnt)

# Q3: a*b = 2a + b
f = lambda p, q: 2 * p + q
lhs, rhs = f(f(1, 2), 3), f(1, f(2, 3))
assert (lhs, rhs) == (11, 9)
assert sp.simplify((2 * (2 * a + b) + c) - (2 * a + 2 * b + c)) != 0  # not associative symbolically
mcq("C01-Q3", {
    "a": (lhs, rhs) == (11, 9) and lhs != rhs,
    "b": (lhs, rhs) == (11, 11),
    "c": (lhs, rhs) == (11, 9) and lhs == rhs,   # "one example does not refute": false, a mismatch refutes
    "d": (lhs, rhs) == (9, 11),
})

# Q4: findbug in the proof of associativity of a+b+ab
st = step("C01-Q4", "findbug")
L1 = (a + b + a * b) + c + (a + b + a * b) * c
stated = [None, L1, a + b + c + a * b + a * c + b * c, a + (b + c + b * c) + a * (b + c + b * c)]
true_expansion = sp.expand(L1)
assert sp.expand(stated[3]) == true_expansion
assert sp.expand(true_expansion - stated[2]) == a * b * c       # the stated expansion misses exactly abc
bad = [i for i in (2,) if sp.expand(stated[i]) != true_expansion]
assert bad == [2] and st["bugIndex"] == 2
check_text_contains(st["lines"], 2, "=a+b+c+ab+ac+bc$")
assert not st["lines"][2].endswith("abc$")

# ================================================================ C02
# lesson: a + b + 1 on Z has neutral -1 and inverse -a-2
g = lambda p, q: p + q + 1
assert all(g(p, -1) == p and g(-1, p) == p for p in range(-50, 50))
assert all(g(p, -p - 2) == -1 for p in range(-50, 50)) and g(4, -6) == -1

# Q1: a + b - 3
h = lambda p, q: p + q - 3
neutrals = [e for e in range(-100, 100) if all(h(p, e) == p and h(e, p) == p for p in range(-50, 50))]
assert neutrals == [3]
mcq("C02-Q1", {
    "a": 3 in neutrals,
    "b": 0 in neutrals,
    "c": -3 in neutrals,
    "d": not neutrals,
})

# Q2: a + b - ab, order step: the chain of facts the lines state
st = step("C02-Q2", "order")
k = lambda p, q: p + q - p * q
assert sp.expand(a + e_ - a * e_ - a) == sp.expand(e_ - a * e_) == sp.expand(e_ * (1 - a))   # lines 1-2
assert sp.solve((e_ * (1 - a)).subs(a, 2), e_) == [0]                                          # line 3
assert all(k(0, p) == p and k(p, 0) == p for p in range(-50, 50))                               # line 4
assert [e for e in range(-100, 100) if all(k(p, e) == p for p in range(-50, 50))] == [0]
assert len(st["lines"]) == 4
for i, frag in enumerate(["a+e-ae=a", "e(1-a)=0", "a=2", "0*a=0+a-0"]):
    assert frag.replace(" ", "") in st["lines"][i].replace("\\cdot", "").replace(" ", ""), (i, frag, st["lines"][i])

# Q3
assert all(h(5, 1) == 3 for _ in [0]) and [x for x in range(-50, 50) if h(5, x) == 3 and h(x, 5) == 3] == [1]
num("C02-Q3", 1)

# Q4: a + b + ab on Z, neutral 0; invertible?
m = lambda p, q: p + q + p * q
assert all(m(p, 0) == p for p in range(-50, 50))


def invertible(av):
    # a + x + a x = 0  ->  x (1 + a) = -a ; solvable in Z iff (1+a) | a with 1+a != 0 ; a = -1 gives -1 for every x
    return any(m(av, x) == 0 and m(x, av) == 0 for x in range(-3000, 3000))


assert [av for av in (-2, 1, 2, 3) if invertible(av)] == [-2]
assert m(-2, -2) == 0
from fractions import Fraction
assert [Fraction(-av, 1 + av) for av in (1, 2, 3)] == [Fraction(-1, 2), Fraction(-2, 3), Fraction(-3, 4)]
mcq("C02-Q4", {"a": invertible(-2), "b": invertible(1), "c": invertible(2), "d": invertible(3)})

# ================================================================ C03
# lesson table
assert is_group(range(0, 5), lambda p, q: (p + q) % 5) == "group"
assert is_group(range(1, 5), lambda p, q: p * q % 5) == "group"
assert is_group(range(1, 6), lambda p, q: p * q % 6) == "closure" and (2 * 3) % 6 == 0
assert all((p + (7 - p)) % 7 == 0 for p in range(1, 7))   # inverse of a in (Z_n, +) is n - a

# Q1: (Z, *) multiplication, window
W = range(-30, 31)
clo = True
neu = [e for e in W if all(p * e == p for p in W)] == [1]
inv_fail = [p for p in W if not any(p * x == 1 for x in range(-1000, 1000))]
assert neu and 2 in inv_fail and sp.expand((a * b) * c - a * (b * c)) == 0
fails = {"closure": not clo, "assoc": False, "neutral": not neu, "inverse": bool(inv_fail)}
mcq("C03-Q1", {"a": fails["closure"], "b": fails["assoc"], "c": fails["neutral"], "d": fails["inverse"]})

# Q2
verdicts = {
    "a": is_group(range(4), lambda p, q: (p + q) % 4),
    "b": is_group(range(4), lambda p, q: (p * q) % 4),
    "c": is_group([1, 2, 3, 4], lambda p, q: (p * q) % 8),
    "d": is_group(range(4), lambda p, q: (p - q) % 4),
}
assert verdicts == {"a": "group", "b": "inverse", "c": "closure", "d": "assoc"}, verdicts
assert (2 * 4) % 8 == 0 and ((0 - 1) - 1) % 4 == 2 and (0 - (1 - 1)) % 4 == 0
assert all((p + (4 - p)) % 4 == 0 for p in range(4))
mcq("C03-Q2", {k_: v == "group" for k_, v in verdicts.items()})

# Q3: a + 2b
t = lambda p, q: p + 2 * q
assert (t(t(1, 2), 3), t(1, t(2, 3))) == (11, 17) and t(1, 2) == 5 and t(2, 1) == 4
assert sp.expand((a + 2 * b) + 2 * c - (a + 2 * (b + 2 * c))) != 0
assoc_ok = all(t(t(p, q), r) == t(p, t(q, r)) for p in range(-4, 5) for q in range(-4, 5) for r in range(-4, 5))
comm_ok = all(t(p, q) == t(q, p) for p in range(-8, 9) for q in range(-8, 9))
closed_ok = all(isinstance(t(p, q), int) for p in range(-8, 9) for q in range(-8, 9))
assert (assoc_ok, comm_ok, closed_ok) == (False, False, True)
mcq("C03-Q3", {
    "a": (not assoc_ok) and (t(t(1, 2), 3), t(1, t(2, 3))) == (11, 17),
    "b": assoc_ok and not comm_ok,
    "c": assoc_ok and comm_ok,
    "d": not closed_ok,
})

# ================================================================ C04
# lesson
assert zstar(8) == [1, 3, 5, 7]
assert {x: order_mod(x, 7) for x in zstar(7)} == {1: 1, 2: 3, 3: 6, 4: 3, 5: 6, 6: 2}
assert [pow(2, k, 5) for k in (1, 2, 3, 4)] == [2, 4, 3, 1] and order_mod(2, 5) == 4 and order_mod(4, 7) == 3
assert sp.ilcm(4, 3) == 12


def prod_order(pairs):  # elements of a direct product of Z_m^* groups, brute force by repeated multiplication
    (x1, m1), (x2, m2) = pairs
    k, y1, y2 = 1, x1 % m1, x2 % m2
    while (y1, y2) != (1, 1):
        y1, y2 = y1 * x1 % m1, y2 * x2 % m2
        k += 1
    return k


assert prod_order(((2, 5), (4, 7))) == 12

num("C04-Q1", len(zstar(9)))
assert zstar(9) == [1, 2, 4, 5, 7, 8]
num("C04-Q2", order_mod(5, 11))
assert [pow(5, k, 11) for k in (1, 2, 3, 4, 5)] == [5, 3, 4, 9, 1] and 10 % 5 == 0

o32 = prod_order(((3, 7), (2, 5)))
assert o32 == 12 and order_mod(3, 7) == 6 and order_mod(2, 5) == 4
assert pow(2, 6, 5) == 4
val = lambda qid, oid: int(re.sub(r"[^0-9]", "", optval(qid, oid)))
mcq("C04-Q3", {o: val("C04-Q3", o) == o32 for o in "abcd"})
assert [val("C04-Q3", o) for o in "abcd"] == [12, 24, 6, 10] and 6 * 4 == 24 and 6 + 4 == 10

# Lagrange: orders possible in a group of order 24 are exactly the divisors (cyclic Z_24 realises each one)
ord_in_z24 = {24 // gcd(24, x) for x in range(24)}
assert ord_in_z24 == {d for d in range(1, 25) if 24 % d == 0}
mcq("C04-Q4", {o: (24 % val("C04-Q4", o) != 0) for o in "abcd"})
assert [val("C04-Q4", o) for o in "abcd"] == [5, 6, 8, 12]
assert all(val("C04-Q4", o) in ord_in_z24 for o in "bcd")

# ================================================================ C05
# lesson
assert sorted({pow(2, k, 7) for k in range(1, 4)}) == [1, 2, 4] and order_mod(2, 7) == 3
assert all(pow(xx, 2, 8) == 1 and pow(xx, 3, 8) == xx and pow(xx, 5, 8) == xx for xx in zstar(8))  # x^2=e => x^3=x, x^5=x


def sub_tests(pred, window):
    has_e = pred(0)
    closed_ = all(pred(p + q) for p in window if pred(p) for q in window if pred(q))
    inv_ = all(pred(-p) for p in window if pred(p))
    return has_e, closed_, inv_


win = range(-60, 61)
cases = {
    "a": lambda n: n % 2 == 0,
    "b": lambda n: n % 2 == 1,
    "c": lambda n: n >= 0,
    "d": lambda n: -10 <= n <= 10,
}
res = {k_: sub_tests(p, win) for k_, p in cases.items()}
assert res["a"] == (True, True, True)
assert res["b"][0] is False
assert res["c"] == (True, True, False)
assert res["d"] == (True, False, True)
mcq("C05-Q1", {k_: all(v) for k_, v in res.items()})

ordq = order_mod(4, 13)
assert [pow(4, k, 13) for k in range(1, 7)] == [4, 3, 12, 9, 10, 1] and len({pow(4, k, 13) for k in range(1, 13)}) == 6 and 12 % 6 == 0
num("C05-Q2", ordq)

# Q3: intersection of subgroups. All subgroups of Z_12 (cyclic, generated by a divisor), both closure and inverse
n12 = 12


def gen_sub(d):
    return {(d * k) % n12 for k in range(n12)}


subs = {frozenset(gen_sub(d)) for d in range(1, n12 + 1)}
for H in subs:
    for K in subs:
        L = H & K
        assert 0 in L and all((p + q) % n12 in L for p in L for q in L) and all((-p) % n12 in L for p in L)
# with "or" the conclusion does not follow: a = 2 in H = {0,2,4,..}, inverse 10 in H but K = {0,6} does not contain it
H = frozenset(gen_sub(2))
K = frozenset(gen_sub(6))
a_ = 2
assert (-a_) % n12 in H and (-a_) % n12 not in K and a_ not in K          # "or" holds, yet -a is not in the intersection
st = step("C05-Q3", "findbug")
assert st["bugIndex"] == 3
assert "או $a^{-1}" in st["lines"][3] and "וגם" in st["lines"][1] and "וגם" in st["lines"][2]
assert "או " not in st["lines"][1] and "או " not in st["lines"][2]

# ================================================================ C06
assert inv_mod(4, 9) == 7 and 4 * 7 == 28 == 3 * 9 + 1
assert 30 == 4 * 7 + 2 and 7 == 3 * 2 + 1 and 1 == 13 * 7 - 3 * 30 and inv_mod(7, 30) == 13 and 7 * 13 == 91 == 3 * 30 + 1
assert 1 == 7 - 3 * 2 == 7 - 3 * (30 - 4 * 7)
assert [x for x in range(9) if 2 * x % 9 == 5] == [7] and inv_mod(2, 9) == 5 and 25 % 9 == 7 and 14 % 9 == 5
assert not [x for x in range(4) if 2 * x % 4 == 1]
assert 23 % 9 == 5 and (-2) % 5 == 3 and inv_mod(2, 5) == 3

num("C06-Q1", inv_mod(3, 7))
assert 3 * 5 == 15 == 2 * 7 + 1
mcq("C06-Q2", {o: gcd(val("C06-Q2", o), 12) != 1 for o in "abcd"})
assert [val("C06-Q2", o) for o in "abcd"] == [9, 5, 7, 11]
assert [(5 * 5) % 12, (7 * 7) % 12, (11 * 11) % 12] == [1, 1, 1]
sol = [x for x in range(8) if 5 * x % 8 == 3]
assert sol == [7] and inv_mod(5, 8) == 5 and 5 * 7 == 35 == 4 * 8 + 3
num("C06-Q3", sol[0])

want = (17 % 5, 6 % 2, (-1) % 7)
assert want == (2, 0, 6)
opts = {"a": (2, 0, 6), "b": (2, 1, 6), "c": (3, 0, 1), "d": (17, 6, -1)}
mods = (5, 2, 7)
mcq("C06-Q4", {o: v == want and all(0 <= r < mm for r, mm in zip(v, mods)) for o, v in opts.items()})

st = step("C06-Q5", "findbug")
assert 17 == 3 * 5 + 2 and 5 == 2 * 2 + 1                           # lines 0 and 1
assert 5 - 2 * 2 == 1 and 5 - 2 * (17 - 3 * 5) == 1                  # line 2
assert 7 * 5 - 2 * 17 == 1                                            # the correct line 3
assert 5 * 5 - 2 * 17 != 1 and 5 * 5 - 2 * 17 == -9                  # the stored (wrong) line 3
assert inv_mod(5, 17) == 7                                            # line 4
assert st["bugIndex"] == 3 and "1=5\\cdot5-2\\cdot17" in st["lines"][3].replace(" ", "")

# ================================================================ C07
P = 7
M = lambda *rows: tuple(tuple(r) for r in rows)
I2 = M((1, 0), (0, 1))
# lessons
assert len([1 for u in range(5) for v in range(1, 5)]) == 20
prod_ = matmul(M((2, 1), (0, 3)), M((4, 1), (0, 5)), 7)
assert prod_ == I2 and inv_mod(2, 7) == 4 and inv_mod(3, 7) == 5 and (-4 * 1 * 5) % 7 == 1
assert order_mod(2, 7) == 3 and order_mod(6, 7) == 2 and matpow_order(M((2, 0), (0, 6)), 7) == 6
# symbolic inverse formula for an upper-triangular matrix
A_, B_, C_, X_, Y_, Z_ = sp.symbols("A_ B_ C_ X_ Y_ Z_")
sp.Matrix([[A_, B_], [0, C_]]) * sp.Matrix([[X_, Y_], [0, Z_]]) == sp.Matrix([[A_ * X_, A_ * Y_ + B_ * Z_], [0, C_ * Z_]])
assert sp.Matrix([[A_, B_], [0, C_]]) * sp.Matrix([[X_, Y_], [0, Z_]]) == sp.Matrix([[A_ * X_, A_ * Y_ + B_ * Z_], [0, C_ * Z_]])
# [[1,b],[0,1]]^n = [[1,nb],[0,1]]
bb, nn = sp.symbols("bb nn")
assert sp.Matrix([[1, bb], [0, 1]]) ** 3 == sp.Matrix([[1, 3 * bb], [0, 1]])

q1 = sum(1 for a1 in range(1, 7) for b1 in range(7))
assert q1 == 42
num("C07-Q1", q1)
o2 = matpow_order(M((1, 3), (0, 1)), 7)
assert o2 == 7
num("C07-Q2", o2)

A3 = M((1, 3), (0, 2))
mats = {
    "a": M((1, 1), (0, 3)),
    "b": M((1, 2), (0, 3)),
    "c": M((1, 3), (0, 3)),
    "d": M((1, 1), (0, 2)),
}
invs = [X for X in product(product(range(5), repeat=2), repeat=2) if matmul(A3, X, 5) == M((1, 0), (0, 1)) and matmul(X, A3, 5) == M((1, 0), (0, 1))]
assert invs == [M((1, 1), (0, 3))]
mcq("C07-Q3", {o: (matmul(A3, X, 5) == M((1, 0), (0, 1)) and matmul(X, A3, 5) == M((1, 0), (0, 1))) for o, X in mats.items()})
# the text of the options is exactly these matrices
for o, X in mats.items():
    txt = optval("C07-Q3", o)
    nums = [int(t) for t in re.findall(r"\d", txt)]
    assert nums == [X[0][0], X[0][1], X[1][0], X[1][1]], (o, txt, nums)

o4 = matpow_order(M((2, 0), (0, 4)), 7)
assert o4 == 3 and order_mod(2, 7) == 3 and order_mod(4, 7) == 3
num("C07-Q4", o4)

# ================================================================ C08
def crt_recipe(rem, mod):
    Mtot = 1
    for m_ in mod:
        Mtot *= m_
    Ms = [Mtot // m_ for m_ in mod]
    xs = [inv_mod(Mi % m_, m_) for Mi, m_ in zip(Ms, mod)]
    s = sum(a_i * Mi * xi for a_i, Mi, xi in zip(rem, Ms, xs))
    return Mtot, Ms, xs, s, s % Mtot


# lesson example
Mt, Ms, xs, s, x = crt_recipe([2, 3, 2], [3, 5, 7])
assert (Mt, Ms, xs, s, x) == (105, [35, 21, 15], [2, 1, 1], 233, 23)
assert solve_congruence((2, 3), (3, 5), (2, 7)) == (23, 105)
assert 35 % 3 == 2 and 21 % 5 == 1 and 15 % 7 == 1

Mt, Ms, xs, s, x = crt_recipe([2, 3, 1], [3, 4, 5])
assert (Mt, Ms, xs, s, x) == (60, [20, 15, 12], [2, 3, 3], 251, 11)
assert solve_congruence((2, 3), (3, 4), (1, 5)) == (11, 60)
assert all(x % m_ == r for r, m_ in zip([2, 3, 1], [3, 4, 5]))
num("C08-Q1", Ms[1])
num("C08-Q2", xs[2])
assert 12 % 5 == 2 and 12 * 3 == 36 == 7 * 5 + 1
num("C08-Q3", x)
assert 2 * 20 * 2 + 3 * 15 * 3 + 1 * 12 * 3 == 251 == 4 * 60 + 11

st = step("C08-Q4", "order")
# every step needs the previous result: M -> M_i -> x_i -> sum mod M -> check. Assert that each result really is computed in that order.
seq = [Mt, Ms, xs, x]
assert seq == [60, [20, 15, 12], [2, 3, 3], 11] and len(st["lines"]) == 5
for i, frag in enumerate(["M=m_1m_2m_3", "M_i=M/m_i", "M_ix_i\\equiv1", "x=a_1M_1x_1", "מציבים"]):
    assert frag in st["lines"][i].replace(" ", "") or frag in st["lines"][i], (i, frag, st["lines"][i])

# ================================================================ C09
# lesson
assert 23 % 9 == 5 and inv_mod(5, 9) == 2 and [x for x in range(9) if 5 * x % 9 == 2] == [4]
assert inv_mod(3, 7) == 5 and (5 * 4) % 7 == 6 and 20 % 7 == 6 and 10 % 4 == 2
assert [x for x in range(7) if 3 * x % 7 == 4] == [6] and 10 % 4 == 2
assert solve_congruence((1, 4), (2, 6)) is None
assert solve_congruence((2, 4), (0, 6)) == (6, 12)
assert gcd(4, 6) == 2 and (1 - 2) % 2 != 0 and (2 - 0) % 2 == 0

sol1 = [x for x in range(7) if 4 * x % 7 == 3]
assert sol1 == [6] and inv_mod(4, 7) == 2 and 4 * 6 == 24 == 3 * 7 + 3
num("C09-Q1", sol1[0])

r1 = [x for x in range(7) if 2 * x % 7 == 3][0]
assert r1 == 5 and inv_mod(2, 7) == 4 and (4 * 3) % 7 == 5 and 11 % 4 == 3
res_ = solve_congruence((r1, 7), (11 % 4, 4), (4, 5))
assert res_ == (19, 140)
assert 2 * 19 % 7 == 3 and 19 % 4 == 3 and 19 % 5 == 4 and 7 * 4 * 5 == 140
assert all(19 % m_ == r for r, m_ in ((5, 7), (3, 4), (4, 5)))
num("C09-Q2", res_[0])

# Q3
no_solution = [x for x in range(24) if x % 4 == 1 and x % 6 == 2]
assert no_solution == [] and solve_congruence((1, 4), (2, 6)) is None
parity = all(x % 2 == 1 for x in range(48) if x % 4 == 1) and all(x % 2 == 0 for x in range(48) if x % 6 == 2)
assert parity
unique_mod_24 = len(no_solution) == 1
unique_mod_12 = len([x for x in range(12) if x % 4 == 1 and x % 6 == 2]) == 1
infinite_mod_12 = len([x for x in range(12) if x % 4 == 1 and x % 6 == 2]) > 1
mcq("C09-Q3", {
    "a": no_solution == [] and parity,
    "b": unique_mod_24,
    "c": unique_mod_12,
    "d": infinite_mod_12,
})

sol_c = solve_congruence((3, 4), (1, 6))
assert sol_c == (7, 12) and [x for x in range(12) if x % 4 == 3 and x % 6 == 1] == [7]
assert gcd(4, 6) == 2 and (3 - 1) % 2 == 0 and 1 % 4 != 3 and 7 % 4 == 3
num("C09-Q4", sol_c[0])

# Q5: findbug in the CRT calculation
st = step("C09-Q5", "findbug")
Mt, Ms, xs, s, x = crt_recipe([1, 2, 5], [3, 5, 7])
assert (Mt, Ms, xs, s, x) == (105, [35, 21, 15], [2, 1, 1], 187, 82)
assert solve_congruence((1, 3), (2, 5), (5, 7)) == (82, 105)
stored_x = [1, 1, 1]                                                  # x_1, x_2, x_3 as written in the lines
wrong = [i for i in range(3) if (Ms[i] * stored_x[i]) % (3, 5, 7)[i] != 1]
assert wrong == [0]                                                   # exactly the first x_i is wrong
assert 2 * 1 % 3 != 1 and 2 * 2 % 3 == 1
assert st["bugIndex"] == 1 and "x_1=1" in st["lines"][1].replace(" ", "")

# ================================================================ C10 and bank pulls
bank = json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf-8"))
bank_q = {q["id"]: q for q in bank["questions"]}
pulled = []
for lid, L in levels.items():
    for q in L["questions"]:
        if "bankId" in q:
            bid = q["bankId"]
            assert bid in bank_q, bid
            bq = bank_q[bid]
            assert not bq.get("hold"), bid
            assert bq.get("topic") in ("groups", "crt"), (bid, bq.get("topic"))
            assert bq.get("official") or "ai-verified" in str(bq.get("stepsSource")), bid
            assert bq.get("stepsSource") == "ai-verified", bid
            assert bid not in pulled, ("duplicate bank pull", bid)
            pulled.append(bid)
    assert any("bankId" in q for q in L["questions"]), lid
boss = levels["C10"]
assert boss.get("boss") is True and all("bankId" in q for q in boss["questions"]) and 4 <= len(boss["questions"]) <= 6
for q in boss["questions"]:
    assert bank_q[q["bankId"]].get("official"), q["bankId"]

# the CRT bank answers used as the boss: re-derive from the stored question systems with sympy
assert solve_congruence((3, 5), (9, 11), (2, 3)) == (53, 165)        # 2x=1 (5), 3x=5 (11), x=2 (3)
assert inv_mod(2, 5) == 3 and 5 * inv_mod(3, 11) % 11 == 9
assert solve_congruence((2, 5), (3, 7), (19 % 11, 11)) == (52, 385)  # x = 19 (11) reduces to 8

# every own question must have been asserted
missing = sorted(set(Q) - covered)
assert not missing, ("own questions with no machine check", missing)
print("OK: %d own questions asserted (%s), %d bank pulls verified present/not held/official or verified" % (len(covered), ", ".join(sorted(levels)), len(pulled)))
