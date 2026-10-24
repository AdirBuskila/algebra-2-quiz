import sympy as sp
from sympy import Matrix, sqrt, Rational as R
A=Matrix([[2,1],[1,-2],[0,2]])
U=Matrix([[R(1,3),2/sqrt(5),-2/(3*sqrt(5))],[-R(2,3),1/sqrt(5),4/(3*sqrt(5))],[R(2,3),0,sqrt(5)/3]])
S=Matrix([[3,0],[0,sqrt(5)],[0,0]]); V=Matrix([[0,1],[1,0]])
print('corrected U orthogonal:',sp.simplify(U.T*U)==sp.eye(3),'  A==USV^T:',sp.simplify(U*S*V.T-A)==sp.zeros(3,2))
Ub=U.copy(); Ub[:,2]=Matrix([-2/sqrt(3),4/sqrt(3),sqrt(5)/3])
print('printed third col norm^2:',sp.nsimplify(sp.simplify((Ub[:,2].T*Ub[:,2])[0])),'  U^TU==I:',sp.simplify(Ub.T*Ub)==sp.eye(3))
print('dot printed col3 with col1:',sp.simplify((Ub[:,0].T*Ub[:,2])[0]))
print('cross(u1,u2)*3sqrt5:',sp.simplify(U[:,0].cross(U[:,1])*3*sqrt(5)).T)
# CRT 24B-B
print([134%5,134%8,134%9])
