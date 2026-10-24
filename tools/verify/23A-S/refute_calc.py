from sympy import *
a=symbols('a',real=True)
# 23A-S 1b: |u|=3,|u+v|=4,|u-v|=6 : 16+36=2(9+|v|^2)
print('1b |v|^2=',(16+36)/2-9)
# LS
def ls(pts):
    x=symbols('x');n=len(pts)
    A=Matrix([[1,p[0]] for p in pts]);b=Matrix([p[1] for p in pts])
    return (A.T*A).inv()*A.T*b
print('LS 23A-S',ls([(5,7),(3,5),(1,4),(-2,0),(-3,2)]).T)
print('LS 24A-C',ls([(-4,-1),(-2,0),(2,4),(4,5),(5,6)]).T)
# QR
A=Matrix([[1,1,0],[0,0,1],[1,-1,1]])
Q,R=A.QRdecomposition();print(Q,R,Q*R==A)
# CRT
from sympy.ntheory.modular import solve_congruence
print(solve_congruence((2,5),(3,2),(4,7)),solve_congruence((5,3),(4,2),(6,7)))
# projection
B1=Matrix([1,1,0,0]);B2=Matrix([1,3,1,1]);v=Matrix([1,3,2,0]) # order (11,12,21,22): [[1,2],[3,0]] -> a11=1,a12=2,a21=3,a22=0
B1=Matrix([1,1,0,0]);B2=Matrix([1,3,1,1]);v=Matrix([1,2,3,0])
M=Matrix.hstack(B1,B2);print('proj',(M*(M.T*M).inv()*M.T*v).T)
# posdef
M=Matrix([[a,(a+3)/2,0],[(a+3)/2,a,0],[0,0,a]])
print(factor(M.det()),factor(M[:2,:2].det()))
print(solve_univariate_inequality(a>0,a))
print('sym part pd:',[ (a_) for a_ in [4,3.5,3,2,-0.5,-2,-1]])
for av in [4,3,2,0.5,-0.5,-1,-2,-5,1]:
    m=M.subs(a,av);print(av,[N(e) for e in m.eigenvals()])
# 24A-C
Mb=Matrix([[a**2,0,1],[0,a,0],[1,0,a**2]])
print(Mb.eigenvals())
for av in [-2,-1,-0.5,0,0.5,1,2]:
    print(av,[N(e) for e in Mb.subs(a,av).eigenvals()])
A=Matrix([[0,-1,1],[1,1,0]])
print((A*A.T).eigenvals(),(A.T*A).eigenvals())
print(A.singular_value_decomposition() if hasattr(A,'singular_value_decomposition') else '')
