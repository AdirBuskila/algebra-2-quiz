import sympy as sp
r2=sp.sqrt(2)
A=sp.Matrix([[1,0,2],[2,0,1]])
U=sp.Matrix([[r2/2,r2/2],[r2/2,-r2/2]]); V=sp.Matrix([[r2/2,-r2/2,0],[0,0,1],[r2/2,r2/2,0]]); S=sp.Matrix([[3,0,0],[0,1,0]])
print('4a recon',sp.simplify(U*S*V.T-A)==sp.zeros(2,3), sp.simplify(V.T*V)==sp.eye(3), sp.simplify(U.T*U)==sp.eye(2))
print('A^TA',A.T*A, 'A v1',(A*sp.Matrix([1,0,1])/r2).T)
print('4b', 3*56*1+40*3+6*35*3, 918%280, (56*1)%5,(40*3)%7,(35*3)%8)
# 1b n=4
import math; print(sum(range(1,5))*2, math.log(24))
# 3b step
print((4-1)*(5-3))
a,b=sp.symbols('a b')
print('5a steps', (-1)*1+0+2*1+0, 16+1+25+9, (-1+10, 5*2-3*1), sp.Rational(-7+2,17).evalf())
# 2c step
Am=sp.Matrix([[2,1],[1,2]]); v=sp.Matrix([1,-1]); print(((sp.eye(2)+Am)*v).dot(v), v.dot(v)+(Am*v).dot(v))
# 5b group test: Z2^3 and S3-free check; every x*x=e group abelian -> (a*b)*a = b
import itertools
G=list(itertools.product([0,1],repeat=3)); op=lambda p,q:tuple((x+y)%2 for x,y in zip(p,q))
print(all(op(op(x,y),x)==y for x in G for y in G))
