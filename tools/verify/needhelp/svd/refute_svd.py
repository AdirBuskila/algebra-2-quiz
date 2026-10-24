# Blind derivations (by hand first), sympy check.
from sympy import *
M=Matrix
A=M([[1,1,0],[0,1,1]]);print((A*A.T).eigenvals(),(A*A.T).trace())
A=M([[1,0,2],[2,0,1]]);print((A.T*A).eigenvals())
A=M([[1,2],[2,1],[0,0]]);print((A.T*A).eigenvals(),A*M([1,1])/sqrt(2),A*M([1,-1])/sqrt(2))
print(M([[1,2],[2,4]]).rank())
print(M([[5,4],[4,5]]).eigenvects())
A=M([[1,0],[1,1],[0,1]]);print((A*M([1,1])/sqrt(2)/sqrt(3)).T.evalf(3))
print(M([1,1,0]).cross(M([-1,1,0])).T)
A=M([[1,1],[0,1],[1,0]]);print((A*M([1,-1])/sqrt(2)).T)
print((M([[3,1],[1,3],[0,0]]).T*M([[3,1],[1,3],[0,0]])).trace())
print(M([[2,1,1],[1,2,1],[1,1,2]]).eigenvals())
