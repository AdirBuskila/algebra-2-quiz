import sympy as sp
from sympy import Matrix, Rational as R, symbols
def ls(pts):
    A=Matrix([[1,x] for x,y in pts]); b=Matrix([y for x,y in pts])
    return (A.T*A).solve(A.T*b)
def proj(v,basis):
    # gram-based projection in trace inner product
    ip=lambda X,Y:(Y.T*X).trace()
    G=Matrix(len(basis),len(basis),lambda i,j:ip(basis[i],basis[j]))
    r=Matrix([ip(v,b) for b in basis])
    # handle dependence
    import sympy
    # use independent subset
    idx=[]
    M=Matrix([list(b) for b in basis])
    print('rank',M.rank())
    return G,r
print('24A-B LS',ls([(1,4),(3,5),(5,6),(7,5),(9,8)]).T)
print('24B-B LS',ls([(0,0),(2,1),(3,4),(4,6),(6,9)]).T)
print('24B-A LS',ls([(-3,-1),(0,1),(1,3),(3,3),(4,6)]).T)
def P(v,basis):
    M=Matrix([list(b) for b in basis]).T  # columns
    # orth proj onto colspace via standard dot (trace ip == frobenius dot)
    cols=M.columnspace()
    B=Matrix.hstack(*cols)
    p=B*(B.T*B).inv()*B.T*Matrix(list(v))
    return p.reshape(2,2), M.rank()
print('24A-B proj',P(Matrix([[2,1],[1,2]]),[Matrix([[1,-1],[0,1]]),Matrix([[0,1],[0,1]]),Matrix([[1,1],[1,1]])]))
print('24B-A proj',P(Matrix([[2,2],[0,2]]),[Matrix([[1,1],[-1,1]]),Matrix([[0,1],[0,1]]),Matrix([[1,1],[0,0]])]))
print('24B-B proj',P(Matrix([[1,1],[1,2]]),[Matrix([[1,0],[0,1]]),Matrix([[0,1],[0,1]])]))
# GS
A=Matrix([[1,0],[0,1]]);B=Matrix([[0,1],[0,1]])
ip=lambda X,Y:(Y.T*X).trace()
e1=A/sp.sqrt(ip(A,A)); w=B-ip(B,A)/ip(A,A)*A; print('GS',A,w,ip(w,w),w/sp.sqrt(ip(w,w)))
# CRT
from sympy.ntheory.modular import solve_congruence
print(solve_congruence((14*pow(3,-1,8)%8,8),(4,9),(22,25)))
print(solve_congruence((2,5),(3,7),(19,11)))
print(solve_congruence((4,5),(6,8),(8,9)))
# posdef
a,c,k=symbols('a c k',real=True)
for name,M,v in [('24A-B',Matrix([[2*a**2,a,0],[a,1,a],[0,a,2*a**2]]),a),('24B-A',Matrix([[1,c,0],[c,1,c],[0,c,1]]),c),('24B-B',Matrix([[k**2,0,2*k],[0,k+1,0],[2*k,0,k**2]]),k)]:
    print(name,'eig',M.eigenvals(),'minors',[sp.factor(M[:i,:i].det()) for i in (1,2,3)])
