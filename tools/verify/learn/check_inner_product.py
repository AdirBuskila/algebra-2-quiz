# -*- coding: utf-8 -*-
"""Learn-brief checks: inner_product + cauchy_schwarz. Run: PYTHONUTF8=1 py -I tools/verify/learn/check_inner_product.py"""
import math, random, sys
import sympy as sp
bad = []
def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond: bad.append(name)

# --- inner_product brief: worked example (parallelogram law), as in 23A-S-Q1b
v2, p = sp.symbols('v2 p', real=True)   # v2 = ||v||^2, p = <u,v>
sol = sp.solve([9 + 2*p + v2 - 16, 9 - 2*p + v2 - 36], [v2, p], dict=True)[0]
ok("PE ||v||^2=17, <u,v>=-5", sol[v2] == 17 and sol[p] == -5, str(sol))
ok("PE Cauchy-Schwarz consistent |-5|<=3*sqrt17", 5 <= 3*math.sqrt(17))
# parallelogram law shortcut: 16+36 = 2*9 + 2*||v||^2
ok("PE parallelogram shortcut", (16 + 36 - 18)//2 == 17)

# bilinear expansion + polarization + parallelogram, symbolic in R^3 with the standard product
u = sp.Matrix(sp.symbols('u1:4', real=True)); v = sp.Matrix(sp.symbols('v1:4', real=True))
dot = lambda a, b: (a.T*b)[0]
nsq = lambda a: dot(a, a)
ok("expand ||u+v||^2", sp.expand(nsq(u+v) - (nsq(u) + 2*dot(u, v) + nsq(v))) == 0)
ok("expand ||u-v||^2", sp.expand(nsq(u-v) - (nsq(u) - 2*dot(u, v) + nsq(v))) == 0)
ok("polarization", sp.expand(sp.Rational(1, 4)*(nsq(u+v) - nsq(u-v)) - dot(u, v)) == 0)
ok("parallelogram", sp.expand(nsq(u+v) + nsq(u-v) - 2*nsq(u) - 2*nsq(v)) == 0)

# <A,B> = tr(B^T A) = sum of entrywise products
A = sp.Matrix(2, 2, sp.symbols('a1:5', real=True)); B = sp.Matrix(2, 2, sp.symbols('b1:5', real=True))
ok("tr(B^T A)=sum a_ij b_ij", sp.expand((B.T*A).trace() - sum(A[i, j]*B[i, j] for i in range(2) for j in range(2))) == 0)

# u^T M v as a candidate inner product: M must be symmetric positive definite
M1 = sp.Matrix([[1, 2], [2, 1]]); M2 = sp.Matrix([[2, 1], [1, 2]])
ok("M1 eigenvalues 3,-1 (not an inner product)", sorted(M1.eigenvals().keys()) == [-1, 3])
x = sp.Matrix([1, -1]); ok("(1,-1)M1(1,-1)^T=-2", (x.T*M1*x)[0] == -2)
ok("M2 eigenvalues 1,3 (positive definite)", sorted(M2.eigenvals().keys()) == [1, 3])
# non-symmetric matrix: u^T N v is not symmetric
N = sp.Matrix([[1, 2], [0, 1]]); e1 = sp.Matrix([1, 0]); e2 = sp.Matrix([0, 1])
ok("N: <e1,e2>=2 but <e2,e1>=0", (e1.T*N*e2)[0] == 2 and (e2.T*N*e1)[0] == 0)

# bad integral products
t = sp.symbols('t', real=True)
ok("weight w=x on [-1,1]: <1,1>=0", sp.integrate(t, (t, -1, 1)) == 0)
ok("int f g^2 not homogeneous in g: f=1,g=1", sp.integrate(1*(2*1)**2, (t, 0, 1)) == 4 and 2*sp.integrate(1*1**2, (t, 0, 1)) == 2)
ok("e^x weight positive on [0,1]", all(math.exp(s/100) > 0 for s in range(101)))

# --- cauchy_schwarz brief
ok("int_0^1 x^6 = 1/7", sp.integrate(t**6, (t, 0, 1)) == sp.Rational(1, 7))
ok("int_1^2 1/x^2 = 1/2", sp.integrate(1/t**2, (t, 1, 2)) == sp.Rational(1, 2))
k, xx = sp.symbols('k xx', real=True)
ok("(k^2+1)(x^2+1)-(x+k)^2=(kx-1)^2", sp.expand((k**2+1)*(xx**2+1) - (xx+k)**2 - (k*xx-1)**2) == 0)
ok("||(2,1,3)||^2=14 < 16", 4+1+9 == 14 and 14 < 16)
n = 5; xs = sp.symbols('x1:%d' % (n+1), real=True)
ok("n*sum x^2-(sum x)^2 = sum_{i<j}(xi-xj)^2 (n=5)", sp.expand(n*sum(s**2 for s in xs) - sum(xs)**2 - sum((xs[i]-xs[j])**2 for i in range(n) for j in range(i+1, n))) == 0)
ok("ln(n!)=sum ln k (n=7)", abs(math.lgamma(8) - sum(math.log(i) for i in range(1, 8))) < 1e-12)
ok("sum_{k<=n}(2k)=n(n+1), sum(2k-1)=n^2", all(sum(2*i for i in range(1, m+1)) == m*(m+1) and sum(2*i-1 for i in range(1, m+1)) == m*m for m in range(1, 30)))
ok("sum_{k<=n} sqrt(k/n) <= sqrt((n^2+n)/2)", all(sum(math.sqrt(i/m) for i in range(1, m+1)) <= math.sqrt((m*m+m)/2)+1e-12 for m in range(1, 80)))
ok("sum sqrt(ln k ln(n-k+1)) <= ln n!", all(sum(math.sqrt(math.log(i)*math.log(m-i+1)) for i in range(1, m+1)) <= math.lgamma(m+1)+1e-12 for m in range(1, 60)))
ok("sum sqrt(2k ln k) <= sqrt(n(n+1) ln n!)", all(sum(math.sqrt(2*i*math.log(i)) for i in range(1, m+1)) <= math.sqrt(m*(m+1)*math.lgamma(m+1))+1e-9 for m in range(1, 60)))
ok("(sum sqrt((2k-1)ln k))^2 <= n^2 ln n!", all(sum(math.sqrt((2*i-1)*math.log(i)) for i in range(1, m+1))**2 <= m*m*math.lgamma(m+1)+1e-9 for m in range(1, 60)))
ok("(sum 1/k^2)^2 <= sum 1/k * sum 1/k^3", all(sum(1/i**2 for i in range(1, m+1))**2 <= sum(1/i for i in range(1, m+1))*sum(1/i**3 for i in range(1, m+1))+1e-12 for m in range(1, 80)))
random.seed(1)
def rnd(): return random.uniform(0.01, 50)
good = True
for _ in range(2000):
    a, b, c = rnd(), rnd(), rnd()
    r = (a+b+c)/(math.sqrt(a)+math.sqrt(b)+math.sqrt(c))**2
    good &= (1/3 - 1e-12 <= r < 1)
ok("1/3 <= (x+y+z)/(sx+sy+sz)^2 < 1 (random)", good)
good = True
for _ in range(500):
    m = random.randint(1, 8); a = [rnd() for _ in range(m)]; b = [rnd() for _ in range(m)]
    good &= sum(a)**2/sum(x*y for x, y in zip(a, b)) <= sum(x/y for x, y in zip(a, b)) + 1e-9
    good &= sum(a)**2 <= m*sum(x*x for x in a) + 1e-9
ok("(sum a)^2/sum ab <= sum a/b ; (sum a)^2 <= n sum a^2 (random)", good)
a1, a2, a3, b1, b2, b3 = sp.symbols('a1 a2 a3 b1 b2 b3', positive=True)
U = [sp.sqrt(a/b) for a, b in zip((a1, a2, a3), (b1, b2, b3))]; V = [sp.sqrt(a*b) for a, b in zip((a1, a2, a3), (b1, b2, b3))]
ok("Titu vectors: <U,V>=sum a", sp.simplify(sum(x*y for x, y in zip(U, V)) - (a1+a2+a3)) == 0)
ok("Titu vectors: |U|^2=sum a/b", sp.simplify(sum(x**2 for x in U) - sum(a/b for a, b in zip((a1, a2, a3), (b1, b2, b3)))) == 0)
tt = sp.symbols('tt', real=True); uv, vv = sp.symbols('uv vv', real=True)
ok("||u+tv||^2-||u||^2 = 2t<u,v>+t^2||v||^2", sp.expand((tt*vv*0) + 2*tt*uv + tt**2*vv - (2*tt*uv + tt**2*vv)) == 0)
ok("equality case ||u+tu||=(1+t)||u||", all(abs(math.hypot(*[(1+t0)*c for c in (3, 4)]) - (1+t0)*5) < 1e-9 for t0 in (0.5, 2, 7)))
sys.exit(1 if bad else 0)
