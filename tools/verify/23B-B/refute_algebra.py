# Independent refuter recomputation for 23B-B. Run: PYTHONUTF8=1 py -I tools/verify/23B-B/refute_algebra.py
from sympy import *
from sympy.ntheory import n_order
from sympy.ntheory.modular import crt
a, x = symbols('a x', real=True)
pts = [(6,10),(2,2),(0,1),(-1,0),(-2,-3)]
A = Matrix([[p[0],1] for p in pts]); y = Matrix([p[1] for p in pts])
assert A.T*A == Matrix([[45,5],[5,5]]) and A.T*y == Matrix([70,10]) and (A.T*A).solve(A.T*y) == Matrix([Rational(3,2),Rational(1,2)])
assert integrate(1/x**2,(x,1,2)) == Rational(1,2)
assert (pow(2,-1,5),pow(3,-1,7)) == (3,5) and 4*6 == 24 and n_order(2,5) == 4 and n_order(3,7) == 6 and ilcm(4,6) == 12
M = Matrix([[a**2,0,1],[0,a,0],[1,0,a**2]]); assert M.eigenvals() == {a:1, a**2+1:1, a**2-1:1}
for av in (Rational(1),Rational(2),Rational(3,2)): assert all(e >= 0 for e in M.subs(a,av).eigenvals())
for av in (Rational(1,2),0,-1,-2): assert any(e < 0 for e in M.subs(a,av).eigenvals())
assert sorted(M.subs(a,1).eigenvals()) == [0,1,2] and sorted(M.subs(a,2).eigenvals()) == [2,3,5]
assert crt([4,3,5],[3,2,4])[0] == 59 and 135+80+144 == 359
K = Matrix([[5,0,0],[0,4,2],[0,2,1]])
assert K.eigenvals() == {0:1, 5:2}          # no eigenvalue 9; trace 10 = 0+5+5
assert (K-9*eye(3)).det() != 0
Q = Matrix([[0,2/sqrt(5),1],[0,0,0],[0,0,0]])
Q = Matrix([[0,0,1],[-1/sqrt(5),2/sqrt(5),0],[2/sqrt(5),1/sqrt(5),0]])
assert simplify(Q.T*Q - eye(3)) == zeros(3)
assert simplify(Q*diag(0,5,5)*Q.T - K) == zeros(3)       # D = diag(0,5,5) is right
assert simplify(Q*diag(5,5,0)*Q.T - K) != zeros(3)       # the printed diag(5,5,0) is wrong for this Q
Am = Matrix([[-1,3],[1,5]]); Qm,Rm = Am.QRdecomposition()
assert Qm*Rm == Am and Rm == Matrix([[sqrt(2),sqrt(2)],[0,4*sqrt(2)]])
v = Matrix([Rational(3,5),Rational(4,5)]); u = Matrix([1,2]); Pm = v*v.T
assert Pm*Pm == Pm and (u-Pm*u).dot(v) == 0 and (u-Pm*u)[0] == -Rational(8,25) and Pm[0,1] == Rational(12,25)
Ai = eye(2); Bm = Matrix([[1,1],[0,1]]); vv = Matrix([1,2]); assert (vv.T*(-Ai-Bm.T*Bm)*vv)[0] == -18
A2 = diag(2,1); w = Matrix([1,-1]); assert (w.T*Bm.T*A2*Bm*w)[0] == 1
print('23B-B refute OK')
