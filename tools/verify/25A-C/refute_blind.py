import sympy as sp
from sympy.ntheory.modular import crt
a=sp.symbols('a',real=True)
pts=[(-4,-1),(-2,0),(2,4),(4,5),(5,6)]
A=sp.Matrix([[1,p[0]] for p in pts]);b=sp.Matrix([p[1] for p in pts])
print('line',(A.T*A).solve(A.T*b))
print('inv',pow(2,-1,5),pow(3,-1,7))
from sympy.ntheory import n_order
print('ords',n_order(2,5),n_order(3,7),sp.ilcm(n_order(2,5),n_order(3,7)))
M=sp.Matrix([[1,0,2],[2,0,1]])
print((M*M.T).eigenvects(),(M.T*M).eigenvects())
u1=sp.Matrix([1,1])/sp.sqrt(2);u2=sp.Matrix([1,-1])/sp.sqrt(2)
v1=sp.Matrix([1,0,1])/sp.sqrt(2);v2=sp.Matrix([-1,0,1])/sp.sqrt(2);v3=sp.Matrix([0,1,0])
U=sp.Matrix.hstack(u1,u2);V=sp.Matrix.hstack(v1,v2,v3);S=sp.Matrix([[3,0,0],[0,1,0]])
print(sp.simplify(U*S*V.T-M))
N=sp.Matrix([[a**2,0,1],[0,a,0],[1,0,a**2]]);print(N.eigenvals())
print('crt',crt([5,2,7],[2,3,4]))
O=sp.Matrix([[5,0,0],[0,4,2],[0,2,1]]);print(O.eigenvects())
