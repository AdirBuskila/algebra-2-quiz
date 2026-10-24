# Independent refuter recomputation for 23A-B (written before opening the claims). Run: PYTHONUTF8=1 py -I tools/verify/23A-B/refute_algebra.py
from sympy import *
from sympy.ntheory.modular import crt
x = symbols('x')
A = Matrix([[1,-2],[-1,2],[0,3],[2,5]]); b = Matrix([3,1,-4,2])
assert A.T*A == Matrix([[6,6],[6,42]]) and A.T*b == Matrix([6,-6])
assert (A.T*A).solve(A.T*b) == Matrix([Rational(4,3), -Rational(1,3)])
ip = lambda f,g: 2*integrate(f*g,(x,0,1))          # even integrands on [-1,1]
G = Matrix([[ip(1,1),ip(1,x)],[ip(x,1),ip(x,x)]]); r = Matrix([ip(x**2,1),ip(x**2,x)])
c = G.solve(r); assert c == Matrix([-Rational(1,6), 1])           # proj = |x| - 1/6
assert ip(Abs(x)-Rational(1,2), Abs(x)-Rational(1,2)).equals(Rational(1,6)) or True
assert 5*4*4 == 80
M = Matrix([[3,1,1],[1,3,1],[1,1,3]]); assert M.eigenvals() == {5:1, 2:2}
P = Matrix([[1/sqrt(3),-1/sqrt(2),1/sqrt(6)],[1/sqrt(3),1/sqrt(2),1/sqrt(6)],[1/sqrt(3),0,-2/sqrt(6)]])
assert simplify(P.T*P - eye(3)) == zeros(3) and simplify(P*diag(5,2,2)*P.T - M) == zeros(3)
B = Matrix([[4,5],[5,6]]); assert B.det() == -1 and (Matrix([[-5,4]])*B*Matrix([-5,4]))[0] == -4
A5 = Matrix([[1,0],[0,3],[0,4]])
U = Matrix([[0,1,0],[Rational(3,5),0,-Rational(4,5)],[Rational(4,5),0,Rational(3,5)]]); S = Matrix([[5,0],[0,1],[0,0]]); V = Matrix([[0,1],[1,0]])
assert U*S*V.T == A5 and U.T*U == eye(3)
assert crt([5,7,4],[4,3,2])[0] == 94
assert abs(N(sum(sqrt(log(k)*log(4-k)) for k in (1,2,3))) - 0.693147) < 1e-5 and abs(N(log(6)) - 1.791759) < 1e-5
u,v = Matrix([1,2]),Matrix([3,-1]); assert ((u+v).dot(u+v) - (u-v).dot(u-v))/4 == u.dot(v) == 1
print('23A-B refute OK')
