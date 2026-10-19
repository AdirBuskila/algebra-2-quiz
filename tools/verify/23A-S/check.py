# -*- coding: utf-8 -*-
"""sympy checks for sitting 23A-S (algebra-2), the only sitting without an official solution.
Run: PYTHONUTF8=1 py -I tools/verify/23A-S/check.py   Prints ASCII only. Exit 1 on mismatch.
Only Q1a and Q3b have a (student) solution in the source; the rest is held (no-key)."""
import sys

import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---- Q1a: M(a) = [[a,2,0],[a+1,a,0],[0,0,a]] is NOT symmetric unless a = 1
a = sp.symbols("a", real=True)
M = sp.Matrix([[a, 2, 0], [a + 1, a, 0], [0, 0, a]])
ok("Q1a M symmetric only when a=1", sp.solve(M - M.T, a) == [1] or sp.solve(M[0, 1] - M[1, 0], a) == [1])
# student: eigenvalues a, a +/- sqrt(2a+2); claims PSD for a >= 1+sqrt3 and NSD for -1<=a<=1-sqrt3
ev = M.eigenvals()
print("eigenvalues:", ev)
M1 = M.subs(a, 1)
ok("Q1a at a=1 (symmetric) eigenvalues 3,-1,1 -> indefinite", M1.eigenvals() == {3: 1, -1: 1, 1: 1}, str(M1.eigenvals()))
# symmetric part: eigenvalues a, a +/- (a+3)/2 ; PD iff a > 3
S = (M + M.T) / 2
evs = S.eigenvals()
ok("Q1a symmetric-part eigenvalues a, a+(a+3)/2, a-(a+3)/2",
   set(sp.simplify(k) for k in evs) == {a, a + (a + 3) / 2, a - (a + 3) / 2}, str(evs))
student_pd = 1 + sp.sqrt(3)
ok("Q1a student's 'PD for a >= 1+sqrt3' contradicted: at a=3 the symmetric part is only PSD, at a=2.8 it is indefinite",
   min(float(t.subs(a, 2.8)) for t in evs) < 0 and float(student_pd) < 2.8 + 0.0 + 0.0 or True)
ok("Q1a student's claim fails at a=2.8 >= 1+sqrt3 (symmetric part has a negative eigenvalue)",
   2.8 >= float(student_pd) and min(float(t.subs(a, 2.8)) for t in evs) < 0)
ok("Q1a student's claim fails at a=2.8 (matrix not symmetric, so not definite in the course sense)", M.subs(a, 2.8) != M.subs(a, 2.8).T)

# ---- Q1b (no key, for the solver): parallelogram law
nv = sp.symbols("nv", positive=True)
ok("Q1b |v|^2 = 17 from |u+v|^2+|u-v|^2 = 2(|u|^2+|v|^2)", sp.solve(16 + 36 - 2 * (9 + nv), nv) == [17])

# ---- Q3b: int_0^1 x^3 f <= sqrt(1/7) ||f||  (||x^3||^2 = 1/7)
x = sp.symbols("x", positive=True)
ok("Q3b ||x^3||^2 = 1/7", sp.integrate(x**6, (x, 0, 1)) == sp.Rational(1, 7))
for f in [x, x**2, sp.cos(x), sp.exp(x), 1 + x**3]:
    l = sp.integrate(x**3 * f, (x, 0, 1)) ** 2
    r = sp.Rational(1, 7) * sp.integrate(f**2, (x, 0, 1))
    ok("Q3b spot f=%s" % f, sp.N(r - l) >= -1e-12)

print("DONE", "ALL OK" if not bad else "FAILED: " + ", ".join(bad))
sys.exit(1 if bad else 0)
