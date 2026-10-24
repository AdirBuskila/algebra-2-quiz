# orthodiag / group / eigen facts (independent recompute)
import sympy as sp
from sympy import Matrix
for name,M in [('24A-B Q5a',Matrix([[3,-2,4],[-2,6,2],[4,2,3]])),('24B-A Q5a',Matrix([[1,1,0],[1,1,0],[0,0,2]]))]:
    print(name,M.eigenvals())
Q=Matrix([[-sp.Rational(2,3),-1/sp.sqrt(5),-4/(3*sp.sqrt(5))],[-sp.Rational(1,3),2/sp.sqrt(5),-2/(3*sp.sqrt(5))],[sp.Rational(2,3),0,-sp.sqrt(5)/3]])
M=Matrix([[3,-2,4],[-2,6,2],[4,2,3]])
print('24A-B Q5a claimed Q: orthogonal',sp.simplify(Q.T*Q)==sp.eye(3),'Q diag(-2,7,7) Q^T == M', sp.simplify(Q*sp.diag(-2,7,7)*Q.T-M)==sp.zeros(3))
s2=sp.sqrt(2)
Q2=Matrix([[1/s2,0,-1/s2],[1/s2,0,1/s2],[0,1,0]]);N=Matrix([[1,1,0],[1,1,0],[0,0,2]])
print('24B-A Q5a claimed',sp.simplify(Q2*sp.diag(2,2,0)*Q2.T-N)==sp.zeros(3))
print('24B-A G: inv of (2,4)=',(pow(2,-1,7),pow(4,-1,7)),' ord(3)=',[k for k in range(1,7) if pow(3,k,7)==1][0],' ord(2)=',[k for k in range(1,7) if pow(2,k,7)==1][0])
x=sp.symbols('x');print('24B-A c: 0.9 line check: ',sp.Rational(9,10),sp.Rational(3,2))
print('24B-A 1/2*1/3 =',(sp.Rational(1,2)+sp.Rational(1,3))/(1+sp.Rational(1,6)))
print('24B-A (0.5*0.2)*0.1 =',sp.nsimplify(((sp.Rational(1,2)+sp.Rational(1,5))/(1+sp.Rational(1,10)))))
