import sympy as sp
from sympy import Matrix
print('|H|',20)
Hm=Matrix([[2,4],[0,pow(2,-1,5)]]); print(Hm,'inv mod5',Hm.inv_mod(5))
a,b,c=sp.symbols('a b c',positive=True)
op=lambda x,y:(x+y)/(x*y)
print('assoc diff',sp.simplify(op(op(a,b),c)-op(a,op(b,c))))
print('x o x = x', sp.solve(sp.Eq(op(a,a),a),a))
print('identity? 1/a+1/e=a: e=',sp.solve(sp.Eq(op(a,b),a),b))
print('x^3=x',sp.solve(4*a**2-1,a))
