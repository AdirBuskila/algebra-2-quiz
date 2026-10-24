import sympy as sp, itertools
# 1a LS
X=sp.Matrix([[1,1],[2,1],[3,1],[4,1]]); y=sp.Matrix([20,24,31,32])
b=(X.T*X).inv()*X.T*y; print('LS',b.T, 'pred5', b[0]*5+b[1])
# 1b projection (Gram-Schmidt, tr(B^T A))
ip=lambda A,B:(B.T*A).trace()
A=sp.Matrix([[1,2],[3,0]]); u1=sp.Matrix([[1,1],[0,0]]); u2=sp.Matrix([[1,3],[1,1]])
G=sp.Matrix([[ip(u1,u1),ip(u2,u1)],[ip(u1,u2),ip(u2,u2)]]); r=sp.Matrix([ip(A,u1),ip(A,u2)])
c=G.solve(r); P=c[0]*u1+c[1]*u2; print('proj',P, 'coef',c.T, 'resid orth', ip(A-P,u1),ip(A-P,u2))
# 2b order of diag(4,3) mod5
import numpy as np
M=sp.Matrix([[4,0],[0,3]]); k=1; N=M
while (N.applyfunc(lambda t:t%5))!=sp.eye(2): N=N*M; k+=1
print('order H',k)
# 3a
a=sp.symbols('a'); print('eig3a',sp.Matrix([[a,0,1],[0,2*a,0],[1,0,a]]).eigenvals())
# 3b
al=sp.Matrix([1,2,1]); be=sp.Matrix([1,0,-1]); print('3b',al.dot(be),al.norm(),be.norm())
# 4a brute: closure, commutativity, identity, inverse
import fractions
print('closure fail',(sp.Matrix([1,0]), ))
def op(p,q): a,b=p;x,y=q; return (a*y+b*x,b*y)
print(op((1,0),(1,0)), op((2,3),(5,7))==op((5,7),(2,3)))
# 5a SVD
A=sp.Matrix([[-1,1],[-1,1],[1,1]]); print('AtA eig',(A.T*A).eigenvects())
print('AAt eig',(A*A.T).eigenvects())
V=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2); S=[2,sp.sqrt(2)]
U=sp.Matrix.hstack(*[A*V[:,i]/S[i] for i in range(2)]); print('U cols',U.T)
# complete u3
u3=sp.Matrix(U[:,0]).cross(sp.Matrix(U[:,1])); print('u3',u3.T, u3.norm())
Ufull=sp.Matrix.hstack(U,u3/u3.norm()); Sig=sp.Matrix([[2,0],[0,sp.sqrt(2)],[0,0]])
print('recon',sp.simplify(Ufull*Sig*V.T-A))
# 5b
print([x for x in range(105) if (2*x)%3==1 and x%5==3 and x%7==4])
