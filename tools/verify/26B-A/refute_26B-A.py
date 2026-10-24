import sympy as sp, itertools
A=sp.Matrix([[1,0],[0,-1]]);B=sp.Matrix([[1,1],[0,-1]]);C=sp.Matrix([[2,3],[1,0]])
ip=lambda X,Y:(Y.T*X).trace()
e1=A; e2=B-ip(B,A)/ip(A,A)*A
print('GS',e1,e2,ip(e1,e1),ip(e2,e2))
P=ip(C,e1)/ip(e1,e1)*e1+ip(C,e2)/ip(e2,e2)*e2; print('proj',P)
# groups
G=[(a,b,c) for a in range(1,5) for b in range(5) for c in range(1,5)];print('|G|',len(G))
J=sp.Matrix([[1,1],[0,2]]);M=sp.eye(2);H=[]
for n in range(6):
    H.append(M.applyfunc(lambda v:v%5));M=(M*J).applyfunc(lambda v:v%5)
print('H',H)
Jinv=H[3];print((J*Jinv).applyfunc(lambda v:v%5))
Hs={tuple(h) for h in H[:4]}
bad=[(a,b,c) for a,b,c in G if tuple(((sp.Matrix([[a,b],[0,c]])*J*sp.Matrix([[a,b],[0,c]]).inv_mod(5)).applyfunc(lambda v:v%5)))not in Hs]
print('bad count',len(bad), all(c!=(a+b)%5 for a,b,c in bad), len(bad)==len([1 for a,b,c in G if c!=(a+b)%5]))
a=sp.symbols('a');M3=sp.Matrix([[1,0,2*a],[0,4-a**2,0],[2*a,0,1]])
print(M3.eigenvals())
import numpy as np
print(np.polyfit([0,1,2,3,4],[2,2,4,8,9],1))
S=sp.Matrix([[3,2],[2,3],[2,-2]]);print(S.singular_values(),(S.T*S).eigenvects())
print(sp.Matrix([[3,2],[2,3],[2,-2]])*sp.Matrix([1,-1])/3)
print([x for x in range(360) if x%5==3 and x%8==2 and x%9==4])
