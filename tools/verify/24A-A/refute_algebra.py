# Independent refuter recomputation for 24A-A. Run: PYTHONUTF8=1 py -I tools/verify/24A-A/refute_algebra.py
from sympy import *
from sympy.ntheory import n_order
from sympy.ntheory.modular import crt
a,b,c,x,k,t = symbols('a b c x k t', positive=True)
odot = lambda p,q: p*q/(p+q)
assert simplify(odot(odot(a,b),c) - odot(a,odot(b,c))) == 0 and simplify(odot(a,b)-odot(b,a)) == 0
assert solve(Eq(odot(a,x),a),x) == []                     # no identity: a*x = a*(a+x) -> a^2 = 0
assert simplify(odot(x,x) - x/2) == 0
p = x
for n_ in range(2,7): p = odot(p,x); assert simplify(p - x/n_) == 0   # x^n = x/n  -> a^a = 1
v = Matrix([[1,1],[1,0]]); e1 = eye(2); e2 = Matrix([[0,1],[0,1]]); ip = lambda P,Q: (Q.T*P).trace()
G = Matrix([[ip(e1,e1),ip(e2,e1)],[ip(e1,e2),ip(e2,e2)]]); cc = G.solve(Matrix([ip(v,e1),ip(v,e2)]))
assert cc[0]*e1+cc[1]*e2 == Matrix([[Rational(1,3),Rational(1,3)],[0,Rational(2,3)]])
# cI + A + A^2 with A sym PSD: v^T(...)v = c|v|^2 + <Av,v> + |Av|^2   (coefficient of |Av|^2 is 1, NOT c)
A = Matrix([[2,1],[1,2]]); vv = Matrix([1,0]); assert (vv.T*(1*eye(2)+A+A**2)*vv)[0] == 8
av = Matrix([2,1]); assert (vv.T*(eye(2)+A+A**2)*vv)[0] == 1 + (A*vv).dot(vv) + (A*vv).dot(A*vv)   # 1+2+5
assert (vv.T*(3*eye(2)+A+A**2)*vv)[0] != 3 + (A*vv).dot(vv) + 3*(A*vv).dot(A*vv)                 # c|Av|^2 form is wrong for c != 1
aa = symbols('aa', real=True)
M = Matrix([[1,0,aa**2],[0,3*aa-1,0],[aa**2,0,1]]); assert M.eigenvals() == {3*aa-1:1, 1+aa**2:1, 1-aa**2:1}
ev = lambda Mx: sorted(sum([[e]*m for e,m in Mx.eigenvals().items()],[]))
assert ev(M.subs(aa,Rational(1,2))) == [Rational(1,2),Rational(3,4),Rational(5,4)] and ev(M.subs(aa,2)) == [-3,5,5]
pts = [(1,3),(3,5),(-2,5),(2,2)]; Am = Matrix([[q[0],1] for q in pts]); y = Matrix([q[1] for q in pts])
assert Am.T*Am == Matrix([[18,4],[4,4]]) and Am.T*y == Matrix([12,15]) and (Am.T*Am).solve(Am.T*y) == Matrix([-Rational(3,14),Rational(111,28)])
assert 6*6*7 == 252 and ilcm(n_order(4,7),n_order(3,7)) == 6 and Matrix([[1,2],[0,3]]).inv_mod(7) == Matrix([[1,4],[0,5]])
for kk in range(1,5):
    for xx in range(-20,21): assert Rational((xx+kk)**2, xx**2+1) <= kk**2+1
S = Matrix([[2,0],[0,2],[1,sqrt(3)]]); assert (S.T*S).eigenvals() == {8:1, 4:1}
V = Matrix([[Rational(1,2),-sqrt(3)/2],[sqrt(3)/2,Rational(1,2)]])
U = Matrix([[sqrt(2)/4,-sqrt(3)/2,-sqrt(2)/4],[sqrt(6)/4,Rational(1,2),-sqrt(6)/4],[sqrt(2)/2,0,sqrt(2)/2]])
assert simplify(U.T*U - eye(3)) == zeros(3) and simplify(U*Matrix([[2*sqrt(2),0],[0,2],[0,0]])*V.T - S) == zeros(3,2)
assert crt([5,11,3],[3,9,2])[0] == 53 and 198+405+110 == 713 and 2*53%5 == 1 and 3*53%11 == 5
print('24A-A refute OK')
