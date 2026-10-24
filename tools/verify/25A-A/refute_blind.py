import sympy as sp, itertools
from sympy.ntheory.modular import crt
x,a,b,w=sp.symbols('x a b w',real=True)
# 1
print('ip',sp.integrate((a*x+b)*(a*x-b),(x,0,1)).expand(), sp.solve(sp.integrate((a*x+b)*(a*x-b),(x,0,1)),b))
print('norms',sp.integrate((a*x+b)**2,(x,0,1)).expand(),sp.integrate((a*x-b)**2,(x,0,1)).expand())
# 3a
M=sp.Matrix([[1,w,w],[w,1,w],[w,w,1]]); print('eig',M.eigenvals())
# 4
import numpy as np
p=5
J=sp.Matrix([[0,4],[1,0]])
P=sp.eye(2)
for k in range(1,10):
    P=(P*J).applyfunc(lambda v:v%5)
    if P==sp.eye(2): print('ordJ',k);break
print('detJ',J.det()%5,'|G|',(25-1)*(25-5))
# brute force order property
els=[sp.Matrix([[q,r],[s,t]]) for q,r,s,t in itertools.product(range(5),repeat=4) if (q*t-r*s)%5]
def order(A):
    P=A.copy();k=1
    while P.applyfunc(lambda v:v%5)!=sp.eye(2):
        P=(P*A).applyfunc(lambda v:v%5);k+=1
    return k
print(len(els), all(order(A)==order((J.T*A*J).applyfunc(lambda v:v%5)) for A in els))
print('JTJ',(J.T*J).applyfunc(lambda v:v%5))
print('crt',crt([5,7,11],[2,3,10]))
A=sp.Matrix([[1,1,1],[1,-2,1]])
print('svd',(A*A.T).eigenvects(), (A.T*A).eigenvects())
U,S,V=None,None,None
u1=sp.Matrix([0,1]);u2=sp.Matrix([1,0])
v1=sp.Matrix([1,-2,1])/sp.sqrt(6);v2=sp.Matrix([1,1,1])/sp.sqrt(3);v3=sp.Matrix([1,0,-1])/sp.sqrt(2)
U=sp.Matrix.hstack(u1,u2);Vm=sp.Matrix.hstack(v1,v2,v3);Sg=sp.Matrix([[sp.sqrt(6),0,0],[0,sp.sqrt(3),0]])
print('recon',sp.simplify(U*Sg*Vm.T-A))
# group
X,Y,Z,W,xx,yy=sp.symbols('X Y Z W xx yy')
print(sp.solve([2*xx+1-xx, yy**2/3-yy],[xx,yy]))
