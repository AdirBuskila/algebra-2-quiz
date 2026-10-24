import sympy as sp, itertools, random
from sympy.ntheory.modular import solve_congruence
def ls(pts):
    x=sp.Matrix([[1,p[0]] for p in pts]);y=sp.Matrix([p[1] for p in pts])
    return ((x.T*x).inv()*x.T*y).T
print('1a',ls([(0,1),(2,4),(6,5),(10,8)]))
print('2 order',4**4)
for v in (1,2,3):
    n=1
    while pow(v,n,5)!=1:n+=1
    print('ord',v,n)
a,b,c,e=sp.symbols('a b c e');o=lambda x,y:x*y-x-y
print('assoc',sp.expand(o(o(a,b),c)-o(a,o(b,c))),o(o(1,0),0),o(1,o(0,0)))
print('ident',sp.solve(o(a,e)-a,e))
print([ (x,y) for x in range(-5,6) for y in range(-30,30) if o(x,y)==0 and False])
u=sp.Matrix([1,0]);v=sp.Matrix([0,1]);print('3b',(v*u.T+u*v.T).eigenvals())
Q=sp.Matrix([[1,1,0],[1,0,1],[0,1,1]]);q,r=Q.QRdecomposition();print('4a',q,r,q*r==Q)
print('4b',[x for x in range(1000) if (3*x-4)%5==0 and (2*x-3)%7==0 and (x-7)%32==0][:3])
cc=sp.symbols('c');P=sp.Matrix([[1,cc,0],[cc,1,cc],[0,cc,1]]);print('5a',P.eigenvals())
T=sp.Matrix([[3,2,0],[2,2,2],[0,2,1]]);print('6a',T.eigenvects())
