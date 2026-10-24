import sympy as sp, itertools, math
# 1a LS
pts=[(6,8),(2,2),(0,0),(-1,0),(-2,4)]
X=sp.Matrix([[x,1] for x,y in pts]); y=sp.Matrix([p[1] for p in pts])
print('LS',((X.T*X).inv()*X.T*y).T, X.T*X, X.T*y)
# 1b numeric sanity
import random
for n in [1,2,3,5,10]:
    L=sum(math.sqrt(2*k*math.log(k)) for k in range(1,n+1)); R=math.sqrt(n*(n+1)*math.log(math.factorial(n))); print(n,L<=R+1e-12,L,R)
# 2a |G| 2b order H
def mm(A,B,p): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))
G=[((a,b),(0,c)) for a in range(3) for b in range(3) for c in range(3) if (a*c)%3!=0]; print('|G|',len(G))
M=((2,1),(0,2)); I=((1,0),(0,1)); P=M;k=1;pw=[I,M]
while P!=I: P=mm(P,M,3);k+=1;pw.append(P)
print('ord H',k,pw[:7])
# 3a
a=sp.symbols('a',real=True); A=sp.Matrix([[1,0,2*a],[0,4-a**2,0],[2*a,0,1]]); print('eig',A.eigenvals())
import numpy as np
for av in [-3,-2.5,-2,-1,-0.6,-0.5,0,0.5,0.6,2,2.5]:
    print(av,np.linalg.eigvalsh(np.array([[1,0,2*av],[0,4-av**2,0],[2*av,0,1]])).round(4))
# 4a SVD
A=sp.Matrix([[1,0,2],[2,0,1]]); print('AAt',(A*A.T).eigenvects()); print('AtA',(A.T*A).eigenvects())
# 4b CRT
print([x for x in range(280) if x%5==3 and x%7==1 and x%8==6])
# 5a projection
a,b=sp.symbols('a b')
ip=lambda A,B:(B.T*A).trace()
v=sp.Matrix([[0,a],[b,0]]); w1=sp.Matrix([[-1,1],[1,0]]); w2=sp.Matrix([[1,0],[2,1]])
G=sp.Matrix([[ip(w1,w1),ip(w2,w1)],[ip(w1,w2),ip(w2,w2)]]); r=sp.Matrix([ip(v,w1),ip(v,w2)])
c=G.solve(r); Pm=sp.simplify(c[0]*w1+c[1]*w2); print('proj',Pm, 'coefs',[sp.simplify(t) for t in c]); print(sp.simplify(ip(v-Pm,w1)),sp.simplify(ip(v-Pm,w2)))
print('<v,w2>',ip(v,w2),'<w1,w2>',ip(w1,w2),'|w2|^2',ip(w2,w2),'|w1|^2',ip(w1,w1))
# Gram-Schmidt style as official: u1=w1,u2=w2 - <w2,w1>/<w1,w1> w1
u1=w1; u2=w2-ip(w2,u1)/ip(u1,u1)*u1; print('u2',u2, ip(u2,u2), ip(v,u2))
# 5b brute: groups of exponent 2 e.g. (Z2)^3 test (a*b)*a = b
