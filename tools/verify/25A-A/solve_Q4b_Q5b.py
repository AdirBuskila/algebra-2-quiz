# -*- coding: utf-8 -*-
"""Solver checks for 25A-A Q4b (CRT) and Q5b (1/3 <= (x+y+z)/(sqrt x+sqrt y+sqrt z)^2 < 1). ASCII, exit 1 on fail.
Run: PYTHONUTF8=1 py -I tools/verify/25A-A/solve_Q4b_Q5b.py"""
import random
import sys
import sympy as sp
from sympy.ntheory.modular import crt

bad = []
def ok(n, c, info=""):
    print(("OK   " if c else "FAIL ") + n + (" " + info if info else ""))
    if not c:
        bad.append(n)

# ---- Q4b
m = [5, 7, 11]; r = [2, 3, 10]
M = 5 * 7 * 11
Ms = [M // k for k in m]
ok("M = 385, M_i = 77,55,35", M == 385 and Ms == [77, 55, 35])
ok("M_i mod m_i = 2,6,2", [Mi % k for Mi, k in zip(Ms, m)] == [2, 6, 2])
xs = [pow(Mi, -1, k) for Mi, k in zip(Ms, m)]
ok("inverses x_i = 3,6,6", xs == [3, 6, 6], str(xs))
tot = sum(a * Mi * xi for a, Mi, xi in zip(r, Ms, xs))
ok("sum = 462+990+2100 = 3552", tot == 3552 and [2 * 77 * 3, 3 * 55 * 6, 10 * 35 * 6] == [462, 990, 2100])
ok("3552 mod 385 = 87", tot % M == 87)
ok("sympy crt agrees", crt(m, r)[0] == 87 and crt(m, r)[1] == 385)
ok("87 satisfies all three", 87 % 5 == 2 and 87 % 7 == 3 and 87 % 11 == 10)

# ---- Q5b
x, y, z = sp.symbols("x y z", positive=True)
a, b, c = sp.symbols("a b c", positive=True)  # a=sqrt x etc.
S = a + b + c
ok("CS form: 3(a^2+b^2+c^2) - (a+b+c)^2 = sum of squares",
   sp.expand(3 * (a**2 + b**2 + c**2) - S**2 - ((a - b)**2 + (b - c)**2 + (a - c)**2)) == 0)
ok("(a+b+c)^2 - (a^2+b^2+c^2) = 2(ab+bc+ca)", sp.expand(S**2 - (a**2 + b**2 + c**2) - 2 * (a * b + b * c + c * a)) == 0)
random.seed(1)
lo = 1e9; hi = -1e9
for _ in range(20000):
    v = [10 ** random.uniform(-6, 6) for _ in range(3)]
    q = sum(v) / sum(t ** 0.5 for t in v) ** 2
    lo = min(lo, q); hi = max(hi, q)
ok("random: 1/3 <= q < 1", lo >= 1 / 3 - 1e-12 and hi < 1, "min=%.6f max=%.6f" % (lo, hi))
ok("equality 1/3 at x=y=z", sp.simplify(3 * x / (3 * sp.sqrt(x))**2) == sp.Rational(1, 3))
sys.exit(1 if bad else 0)
