import numpy as np, itertools
s2=2**.5;s5=5**.5
U=np.array([[0,-s2/2,s2/2],[1,0,0],[0,s2/2,s2/2]]);S=np.array([[2*s2,0],[0,2],[0,0]]);V=np.array([[s2/2,-s2/2],[s2/2,s2/2]])
A=np.array([[1,-1],[2,2],[-1,1]]);print('25A-B 1b',np.allclose(U@S@V.T,A),np.allclose(U.T@U,np.eye(3)),np.allclose(V.T@V,np.eye(2)))
P=np.array([[1/s2,0,-1/s2],[1/s2,0,1/s2],[0,1,0]]);D=np.diag([2,2,0]);B=np.array([[1,1,0],[1,1,0],[0,0,2]])
print('5a',np.allclose(P@D@P.T,B),np.allclose(P.T@P,np.eye(3)))
# S4 conjugation order
def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))  # p after q
def inv(p):
    r=[0]*len(p)
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
def order(p):
    e=tuple(range(len(p)));k=1;q=p
    while q!=e:q=comp(p,q);k+=1
    return k
x=(1,2,3,0);y=(1,0,2,3);print('S4 ord',order(comp(inv(y),comp(x,y))))
# 25B-A
s6=6**.5;s3=3**.5
U=np.array([[1/3,2*s5/5,-2*s5/15],[-2/3,s5/5,4*s5/15],[2/3,0,s5/3]]);S=np.array([[3,0],[0,s5],[0,0]]);V=np.array([[0,1],[1,0]])
A=np.array([[2,1],[1,-2],[0,2]]);print('25B-A 5a',np.allclose(U@S@V.T,A),np.allclose(U.T@U,np.eye(3)))
Q=np.array([[-1/s2,-1/s6,1/s3],[1/s2,-1/s6,1/s3],[0,2/s6,1/s3]]);D=np.diag([2,2,5]);T=np.array([[3,1,1],[1,3,1],[1,1,3]])
print('6b',np.allclose(Q@D@Q.T,T),np.allclose(Q.T@Q,np.eye(3)))
print('Q1b example',np.array([[2,1],[1,2]])@np.array([1,1]),np.array([[2,1],[1,2]])@np.array([1,-1]))
print('k=-3',sorted([-3,-3*(1-s2),-3*(1+s2)]))
# 25B-B
Q=np.array([[s2/2,s6/6,-s3/3],[s2/2,-s6/6,s3/3],[0,s6/3,s3/3]]);R=np.array([[s2,s2/2,s2/2],[0,s6/2,s6/6],[0,0,2*s3/3]])
M=np.array([[1,1,0],[1,0,1],[0,1,1]]);print('QR',np.allclose(Q@R,M),np.allclose(Q.T@Q,np.eye(3)),np.allclose(R,np.triu(R)))
Q=np.array([[2,-2,1],[2,1,-2],[1,2,2]])/3;D=np.diag([5,2,-1]);T=np.array([[3,2,0],[2,2,2],[0,2,1]])
print('6a',np.allclose(Q@D@Q.T,T),np.allclose(Q.T@Q,np.eye(3)))
# 25B-B 4b, CRT solutions unique
print([x for x in range(1120) if (3*x-4)%5==0 and (2*x-3)%7==0 and (x-7)%32==0])
print('Z12',sorted(set(range(0,12,2))&set(range(0,12,3))))
# lcm of Z5* orders matrix
import math
H=[1,2,3,4]
M2=(1,2,2,3);k=1;cur=M2
while any(c!=1 for c in cur):
    cur=tuple(c*m%5 for c,m in zip(cur,M2));k+=1
print('order',k)
# 25A-B group: Q2 x^5=y^9 sanity in Z2^3 and Q4a.2
print('c=0.5 eig',1-s2*0.5)
