import sympy as sp, itertools
from sympy.ntheory.modular import solve_congruence
def ls(pts):
    n=len(pts);x=sp.Matrix([[1,p[0]] for p in pts]);y=sp.Matrix([p[1] for p in pts])
    b=(x.T*x).inv()*x.T*y;return b.T
print('25A-B 1a',ls([(9,8),(7,5),(5,6),(3,5),(1,4)]))
A=sp.Matrix([[1,-1],[2,2],[-1,1]]);print('1b AtA eig',(A.T*A).eigenvects(),'AAt',(A*A.T).eigenvects())
a=sp.symbols('a');M=sp.Matrix([[a,0,1],[0,2*a,0],[1,0,a]]);print('3a eig',M.eigenvals())
C=sp.Matrix([[1,3],[3,8]]);print('3b',C.det(),(sp.Matrix([3,-1]).T*C*sp.Matrix([3,-1]))[0],(sp.Matrix([1,0]).T*C*sp.Matrix([1,0]))[0])
print('4c',solve_congruence((3,4),(4,5),(2,7)))
B=sp.Matrix([[1,1,0],[1,1,0],[0,0,2]]);print('5a',B.eigenvects())
import random
for _ in range(2000):
    x,y,z=[random.random()**3*10+1e-9 for _ in range(3)]
    r=(x+y+z)/(x**.5+y**.5+z**.5)**2
    assert 1/3-1e-12<=r<1
print('5b ok')
# a=1,-1 semidef
for av in (1,-1,0,2,-2,sp.Rational(1,2)):print(av,M.subs(a,av).eigenvals())
# group facts
for xv in range(1):pass
