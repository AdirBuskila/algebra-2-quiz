import sympy as sp
r2=sp.sqrt(2)
# 23A-A Q5a claim
A=sp.Matrix([[-1,1],[-1,1],[1,1]])
U=sp.Matrix([[-1/r2,0,1/r2],[-1/r2,0,-1/r2],[0,1,0]]); S=sp.Matrix([[2,0],[0,r2],[0,0]]); V=sp.Matrix([[1/r2,1/r2],[-1/r2,1/r2]])
print('5a recon',sp.simplify(U*S*V.T-A)==sp.zeros(3,2),'U orth',sp.simplify(U.T*U)==sp.eye(3),'V orth',sp.simplify(V.T*V)==sp.eye(2))
# 1b claim
ip=lambda X,Y:(Y.T*X).trace()
v=sp.Matrix([[1,2],[3,0]]); P=sp.Rational(1,2)*sp.Matrix([[1,5],[2,2]])
w1=sp.Matrix([[1,1],[0,0]]); w2=sp.Matrix([[1,3],[1,1]]); print('1b resid',ip(v-P,w1),ip(v-P,w2), 'P in W', sp.Matrix([[1,1,P[0,0]],[1,3,P[0,1]],[0,1,P[1,0]],[0,1,P[1,1]]]).rank()==2)
u2=sp.Matrix([[-1,1],[1,1]]); print('u2',ip(u2,w1), ip(v,u2),ip(u2,u2), ip(v,w1))
print('1a',sum(x*x for x in [1,2,3,4]),sum(x*y for x,y in zip([1,2,3,4],[20,24,31,32])), sp.Rational(43,10)*5+16)
# step 2a
print(sp.integrate(sp.exp(sp.Symbol('x')),(sp.Symbol('x'),0,1)).evalf(), sp.integrate(sp.Symbol('x')*sp.exp(sp.Symbol('x')),(sp.Symbol('x'),0,1)))
# 4c steps
print(sp.Rational(1,2),-sp.Rational(1,4)); print((1*2+2*3, 3*2+4*1))
# 4d: inner products pairs
a,b=sp.symbols('a b'); print(sp.Matrix([a,b]).dot(sp.Matrix([-b,a])), sp.Matrix([a,a]).dot(sp.Matrix([b,b])))
# CRT
print((2*35*2+3*21*1+4*15*1), (2*35*2+3*21+60)%105)
# 5a u3 check
u3=sp.Matrix([1,-1,0])/r2; print('A^T u3',(A.T*u3).T)
