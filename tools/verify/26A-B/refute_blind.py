import sympy as sp
from sympy.ntheory.modular import crt
t,x=sp.symbols('t x',real=True)
A=sp.Matrix([[2,1],[1,2]])
u=sp.Matrix([1,t]);v=sp.Matrix([t,-1])
print('orth',sp.solve((u.T*A*v)[0],t))
Am=sp.Matrix([[1,-2],[-1,2],[0,3],[2,5]]);bv=sp.Matrix([3,1,-4,2])
print('rank',Am.rank(),'AtA',Am.T*Am,'Atb',Am.T*bv)
print('LS',(Am.T*Am).solve(Am.T*bv) if (Am.T*Am).det()!=0 else 'singular')
M=sp.Matrix([[1,x,1],[x,1,1],[1,1,x+2]])
print('minors',sp.factor(M[:1,:1].det()),sp.factor(M[:2,:2].det()),sp.factor(M.det()))
print('eig',M.charpoly().as_expr().factor())
import itertools
def psd(xv):
    ev=[sp.N(e) for e in M.subs(x,xv).eigenvals(multiple=True)]
    return ev
for xv in [-4,-3,-2,-1,-0.5,0,0.5,1,2,sp.Rational(-3)]:
    Mx=sp.Matrix(M.subs(x,xv)); print(xv,[round(float(sp.re(e)),4) for e in Mx.evalf().eigenvals(multiple=True)])
print('crt',crt([3,5,8],[2,1,4]))
# group 4
import numpy as np
els=[(a,b,c) for a in range(1,5) for b in range(5) for c in range(5)]
def mul(p,q):
    a,b,c=p;d,e,f=q
    return ((a*d)%5,(a*e+b*d)%5,(a*f+b*e+c*d)%5)
print(len(els), all(mul(p,q) in els for p in els for q in els))
X=sp.Matrix([[1,0,1],[0,1,0],[0,0,1]]);P=X;k=1
while P.applyfunc(lambda v:v%5)!=sp.eye(3): P=P*X;k+=1
print('ordX',k)
# noncommutative? check commutative
print('comm',all(mul(p,q)==mul(q,p) for p in els for q in els))
# M group: check
print(sp.simplify(sp.expand(sp.symbols('a')*sp.symbols('b')-sp.symbols('a')-sp.symbols('b')+2-((sp.symbols('a')-1)*(sp.symbols('b')-1)+1))))
print(sp.solve(sp.Eq((x-1)**2+1,x),x))
# CS check numeric
import random
for n in range(1,8):
    s1=sum(sp.Rational(1,k) for k in range(1,n+1));s2=sum(sp.Rational(1,k**2) for k in range(1,n+1));s3=sum(sp.Rational(1,k**3) for k in range(1,n+1))
    assert s2**2<=s1*s3
