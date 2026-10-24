import sympy as sp, itertools
# Q1a
A=sp.Matrix([[3,1,0],[1,3,0],[0,0,1]]); print('Q1a',A.eigenvects())
# Q2 K
K=[(a,b) for a in range(7) for b in range(7) if (a*a+b*b)%7==1]; print('|K|',len(K))
def mm(M,N): return tuple(tuple(sum(M[i][k]*N[k][j] for k in range(2))%7 for j in range(2)) for i in range(2))
mat=lambda a,b:((a,b),((-b)%7,a))
Ks={mat(a,b) for a,b in K}
print('closed',all(mm(x,y) in Ks for x in Ks for y in Ks))
X=((2,2),(5,2)); print('X in K',X in Ks)
I=((1,0),(0,1)); P=X;k=1
while P!=I: P=mm(P,X);k+=1
print('ord X',k)
inv=[y for y in Ks if mm(X,y)==I]; print('Xinv',inv)
def order(x):
    P=x;k=1
    while P!=I: P=mm(P,x);k+=1
    return k
print('orders',sorted(order(x) for x in Ks), 'cyclic', any(order(x)==8 for x in Ks))
# Q3a
x=sp.symbols('x',real=True); M=sp.Matrix([[1,x,0],[x,2,x],[0,x,1]]); print('det',sp.factor(M.det()),'minors',M[:2,:2].det())
print('charpoly roots',sp.solve(M.charpoly().as_expr(),sp.Symbol('lambda')))
import numpy as np
for xv in [0,0.5,0.99,1,1.01,2,-1,-1.5]:
    ev=np.linalg.eigvalsh(np.array([[1,xv,0],[xv,2,xv],[0,xv,1]],float)); print(xv,ev.round(4))
# Q4 brute: group axioms on small range, center
op=lambda p,q:(p[0]+q[0], p[1]+(-1)**p[0]*q[1])
R=range(-6,7)
pts=[(a,b) for a in R for b in R]
print('assoc',all(op(op(p,q),r)==op(p,op(q,r)) for p in pts[::7] for q in pts[::5] for r in pts[::11]))
print('noncomm',op((1,0),(0,1)),op((0,1),(1,0)))
cen=[p for p in pts if all(op(p,q)==op(q,p) for q in pts)]
print('center',cen)
# Q5 CRT
print([x for x in range(84) if (2*x)%3==1 and (3*x)%4==1 and (2*x)%7==3])
# Q5a P
import random
Q,_=np.linalg.qr(np.random.randn(3,3)); u,v,w=Q[:,0],Q[:,1],Q[:,2]; Pm=np.outer(u,u)+np.outer(v,v)
print(np.allclose(Pm@u,u),np.allclose(Pm@v,v),np.allclose(Pm@w,0), np.linalg.eigvalsh(Pm).round(6))
