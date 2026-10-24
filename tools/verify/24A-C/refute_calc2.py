from sympy import *
import itertools
A=Matrix([[0,-1,1],[1,1,0]])
s=sqrt
U=Matrix([[-1/s(2),1/s(2)],[1/s(2),1/s(2)]])
S=Matrix([[s(3),0,0],[0,1,0]])
V=Matrix([[1/s(6),1/s(2),-1/s(3)],[2/s(6),0,1/s(3)],[-1/s(6),1/s(2),1/s(3)]])
print(simplify(U*S*V.T-A), simplify(V.T*V), simplify(U.T*U))
# group op
a,b,x,y,p,q=symbols('a b x y p q')
op=lambda u,v:(u[0]*v[1]+u[1]*v[0],u[1]*v[1])
print(simplify(Matrix(op(op((a,b),(x,y)),(p,q)))-Matrix(op((a,b),op((x,y),(p,q))))))
print(op((1,0),(1,0)),op((a,b),(0,1)),op((0,1),(a,b)))
print(solve(list(Matrix(op((4,0),(x,y)))-Matrix([0,1])),[x,y]))
# G inverse
def M(a,b,c): return Matrix([[1,a,b],[0,1,c],[0,0,1]])
a,b,c,a2,b2,c2=symbols('a b c a2 b2 c2')
print(M(a,b,c)*M(a2,b2,c2)==M(a+a2,b+b2+a*c2,c+c2), simplify(M(a,b,c)*M(-a,a*c-b,-c)))
# brute: Z2xZ2 etc skip; CRT brute
print([n for n in range(70) if n%5==2 and n%2==1 and n%7==4],[n for n in range(42) if n%3==2 and n%2==0 and n%7==6])
