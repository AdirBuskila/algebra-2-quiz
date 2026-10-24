# -*- coding: utf-8 -*-
"""Solver re-derivation of 26A-A Q4c: center of (Z^2, o), (a,b)o(x,y) = (a+x, b+(-1)^a y). ASCII output.
Run: PYTHONUTF8=1 py -I tools/verify/26A-A/solve_Q4c.py"""
import sys

op = lambda p, q: (p[0] + q[0], p[1] + (-1) ** (p[0] % 2) * q[1])
R = range(-6, 7)
center = [(a, b) for a in R for b in R if all(op((a, b), (x, y)) == op((x, y), (a, b)) for x in R for y in R)]
expected = [(a, 0) for a in R if a % 2 == 0]
print("center in [-6,6]^2:", center)
good = center == expected
print(("OK   " if good else "FAIL ") + "center = {(a,0) : a even}")
# official "a even and x even" would include e.g. (2,1): check it fails for x=1
bad_official = op((2, 1), (1, 0)) != op((1, 0), (2, 1))
print(("OK   " if bad_official else "FAIL ") + "(2,1) (a even, b!=0) does not commute with (1,0)")
sys.exit(0 if good and bad_official else 1)
