import sympy as sp, itertools
from sympy.ntheory.modular import solve_congruence
def ls(pts):
    x=sp.Matrix([[1,p[0]] for p in pts]);y=sp.Matrix([p[1] for p in pts])
    return ((x.T*x).inv()*x.T*y).T
print('1a',ls([(-2,3),(1,5),(5,6),(7,5),(9,8)]))
# H over Z7
H=[((x,y),(0,pow(x,-1,7))) for x in range(1,7) for y in range(7)]
def mul(A,B):
    (a,b),(c,d)=A;(p,q),(r,s)=B
    return (((a*p+b*r)%7,(a*q+b*s)%7),((c*p+d*r)%7,(c*q+d*s)%7))
Hs=set(((x,y),(0,pow(x,-1,7))) for x in range(1,7) for y in range(7))
assert all(mul(A,B) in Hs for A in Hs for B in Hs);print('H order',len(Hs))
M=((1,1),(0,1));P=M;n=1
while P!=((1,0),(0,1)):P=mul(P,M);n+=1
print('ord',n)
k=sp.symbols('k');K=sp.Matrix([[k,k,0],[k,k,k],[0,k,k]]);print('3a',K.eigenvals())
# odot
a,b,c=sp.symbols('a b c');o=lambda x,y:x*y+x+y
print('assoc',sp.expand(o(o(a,b),c)-o(a,o(b,c))))
print('ident', sp.solve(o(a,sp.Symbol('e'))-a,sp.Symbol('e')))
print('inv of a: b=',sp.solve(o(a,b),b), [ (x,o(x,y)) for x in range(-5,6) for y in range(-50,50) if o(x,y)==0])
S=sp.Matrix([[2,1],[1,-2],[0,2]]);print('5a',(S.T*S).eigenvects(),(S*S.T).eigenvects())
print('5c',solve_congruence((1,3),(2,5),(2,11)))
T=sp.Matrix([[3,1,1],[1,3,1],[1,1,3]]);print('6b',T.eigenvects())
import random
for _ in range(2000):
    n=random.randint(1,6);av=[random.random()+.01 for _ in range(n)];bv=[random.random()+.01 for _ in range(n)]
    assert sum(av)**2/sum(x*y for x,y in zip(av,bv))<=sum(x/y for x,y in zip(av,bv))+1e-9
print('6c ok')
