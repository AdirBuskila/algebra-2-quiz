import sympy as sp, numpy as np
A=sp.Matrix([[3,1,0],[1,3,0],[0,0,1]]); r2=sp.sqrt(2)
P=sp.Matrix([[1/r2,-1/r2,0],[1/r2,1/r2,0],[0,0,1]]); D=sp.diag(4,2,1)
print('1a',sp.simplify(P*D*P.T-A)==sp.zeros(3), A.det())
# 1b example
print(1+9, sp.Rational(16,2))
# 2: inverse formula, 2I not in K, step values
print((2*2+2*2)%7,(-2)%7)
M=sp.Matrix([[2,2],[5,2]]); N=sp.Matrix([[2,5],[2,2]]); print((M*N).applyfunc(lambda t:t%7))
# 3a values
x=sp.Symbol('x'); print(sp.solve((3-sp.sqrt(9))/2))
# 3c/3d example
a=sp.Matrix([1,1]); b=sp.Matrix([3,1]); p=b.dot(a)/a.dot(a)*a; c=b-p; print(p.T,c.T,c.dot(a),p.dot(p),c.dot(c),b.dot(b))
# 4: group ops
op=lambda p,q:(p[0]+q[0],p[1]+(-1)**p[0]*q[1])
print(op((1,2),(3,4)), op((1,3),(-1,3)), op((2,5),(-2,-5)), op((1,1),(1,0)),op((1,0),(1,1)))
print(op((2,1),(1,1)),op((1,1),(2,1)),op((1,0),(0,1)),op((0,1),(1,0)),op((2,1),(2,3)),op((2,3),(2,1)))
# 5d
print(2*28+3*21+5*12*3, 299%84)
