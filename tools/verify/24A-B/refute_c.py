from sympy import Matrix, eye
def mat(a,b): return Matrix([[1,a,b],[0,1,a],[0,0,1]])
mods=lambda M:M.applyfunc(lambda t:t%3)
els=[mat(a,b) for a in range(3) for b in range(3)]
S={tuple(mods(e)) for e in els}
print('closed',all(tuple(mods(x*y)) in S for x in els for y in els),'abelian',all(mods(x*y)==mods(y*x) for x in els for y in els))
x=mat(2,0);P=x;k=1
while mods(P)!=eye(3): P=P*x;k+=1
print('order of given matrix? (a=2,b=0)',k)
# the exam matrix [[1,2,0],[0,1,2],[0,0,1]] is a=2,b=0
