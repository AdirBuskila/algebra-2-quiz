# -*- coding: utf-8 -*-
"""Learn-brief checks: orthodiag, pos_def, qr, svd.
Run: PYTHONUTF8=1 py -I tools/verify/learn/check_matrices.py   (ASCII output, exit 1 on any failure)"""
import random
import sys
import sympy as sp

bad = []


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


R = sp.Rational
lam = sp.symbols('lambda')
a, c, k = sp.symbols('a c k', real=True)


def eigset(M):
    return sorted(M.eigenvals().items(), key=lambda t: str(t[0]))


# ---------------------------------------------------------------- orthodiag brief
A = sp.Matrix([[4, 1, 1], [1, 4, 1], [1, 1, 4]])
ok("OD worked: eigenvalues 6 (x1), 3 (x2)", A.eigenvals() == {6: 1, 3: 2})
ok("OD worked: char poly = (6-l)(3-l)^2", sp.expand((A - lam * sp.eye(3)).det() - (6 - lam) * (3 - lam) ** 2) == 0)
v1 = sp.Matrix([1, 1, 1])
ok("OD worked: A(1,1,1) = 6(1,1,1)", A * v1 == 6 * v1)
w2 = sp.Matrix([1, -1, 0])
w3 = sp.Matrix([1, 0, -1])
ok("OD worked: w2,w3 in the eigenspace of 3, not orthogonal (<w2,w3>=1)",
   A * w2 == 3 * w2 and A * w3 == 3 * w3 and (w2.T * w3)[0] == 1)
w3p = w3 - (w3.T * w2)[0] / (w2.T * w2)[0] * w2
ok("OD worked: GS inside the eigenspace gives (1/2,1/2,-1)", w3p == sp.Matrix([R(1, 2), R(1, 2), -1]))
w3q = 2 * w3p
ok("OD worked: scaled (1,1,-2), orthogonal to both others", (w3q.T * w2)[0] == 0 and (w3q.T * v1)[0] == 0 and A * w3q == 3 * w3q)
Q = sp.Matrix.hstack(v1 / sp.sqrt(3), w2 / sp.sqrt(2), w3q / sp.sqrt(6))
D = sp.diag(6, 3, 3)
ok("OD worked: Q^T Q = I, Q D Q^T = A, Q^T A Q = D",
   sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(Q * D * Q.T - A) == sp.zeros(3, 3) and sp.simplify(Q.T * A * Q - D) == sp.zeros(3, 3))
ok("OD worked: trace 12 = 6+3+3, det 54 = 6*3*3", A.trace() == 12 and A.det() == 54)
# different eigenvalues -> orthogonal eigenvectors (symmetric); non-symmetric counterexample
Ns = sp.Matrix([[1, 1], [0, 2]])
ev = Ns.eigenvects()
vecs = [e[2][0] for e in ev]
ok("OD non-symmetric [[1,1],[0,2]]: eigenvectors for 1 and 2 are NOT orthogonal", (vecs[0].T * vecs[1])[0] != 0)
# exam-matrices eigenvalues quoted in the brief
for name, M, evs in (("23A-B-Q3a", sp.Matrix([[3, 1, 1], [1, 3, 1], [1, 1, 3]]), {5: 1, 2: 2}),
                     ("24B-A-Q5a", sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 2]]), {0: 1, 2: 2}),
                     ("23B-B-Q4a", sp.Matrix([[5, 0, 0], [0, 4, 2], [0, 2, 1]]), {5: 2, 0: 1}),
                     ("25B-B-Q6a", sp.Matrix([[3, 2, 0], [2, 2, 2], [0, 2, 1]]), {5: 1, 2: 1, -1: 1}),
                     ("24A-B-Q5a", sp.Matrix([[3, -2, 4], [-2, 6, 2], [4, 2, 3]]), {7: 2, -2: 1})):
    ok("OD %s eigenvalues" % name, M.eigenvals() == evs, str(M.eigenvals()))
# proof of orthogonality of eigenvectors: lambda<u,v> = <Au,v> = <u,Av> = mu<u,v>
ls_, ms_ = sp.symbols('ls ms', real=True)
ok("OD proof: (lambda-mu)<u,v>=0 forces <u,v>=0 when lambda != mu", sp.solve(sp.Eq((ls_ - ms_) * sp.Symbol('p'), 0), sp.Symbol('p')) == [0])

# ---------------------------------------------------------------- pos_def brief
Mw = sp.Matrix([[2, a, 0], [a, 2, 0], [0, 0, a + 1]])
ev = Mw.eigenvals()
ok("PD worked: eigenvalues 2+a, 2-a, a+1", set(ev.keys()) == {2 + a, 2 - a, a + 1})
# classification of the worked example by scanning rational points (and the boundary points)
def classify(vals):
    if all(v > 0 for v in vals):
        return "pos_strict"
    if all(v >= 0 for v in vals):
        return "pos"
    if all(v < 0 for v in vals):
        return "neg_strict"
    if all(v <= 0 for v in vals):
        return "neg"
    return "none"
cls = {}
for t in [R(n, 4) for n in range(-16, 17)]:
    cls[t] = classify([2 + t, 2 - t, t + 1])
ok("PD worked: strict positive exactly on -1<a<2", all((cls[t] == "pos_strict") == (-1 < t < 2) for t in cls))
ok("PD worked: positive (not strict) exactly at a=-1 and a=2", all((cls[t] == "pos") == (t in (-1, 2)) for t in cls))
ok("PD worked: never negative", all(cls[t] not in ("neg", "neg_strict") for t in cls))
ok("PD worked: none otherwise (a<-1 or a>2)", all((cls[t] == "none") == (t < -1 or t > 2) for t in cls))
# non-symmetric trap (23A-S-Q1a)
Ms = sp.Matrix([[a, 2, 0], [a + 1, a, 0], [0, 0, a]])
ok("PD 23A-S-Q1a: symmetric only for a=1", sp.solve(sp.Eq(Ms[0, 1], Ms[1, 0]), a) == [1])
M1_ = Ms.subs(a, 1)
ok("PD 23A-S-Q1a: at a=1 eigenvalues 1,3,-1 (indefinite)", M1_.eigenvals() == {1: 1, 3: 1, -1: 1})
Mb = sp.Matrix([[1, 0, a ** 2], [0, 3 * a - 1, 0], [a ** 2, sp.Symbol('b'), 1]])
ok("PD 24A-A-Q3a: symmetric needs b=0", sp.solve(sp.Eq(Mb[1, 2], Mb[2, 1]), sp.Symbol('b')) == [0])
ok("PD 24A-A-Q3a: eigenvalues 3a-1, 1+a^2, 1-a^2", set(Mb.subs(sp.Symbol('b'), 0).eigenvals().keys()) == {3 * a - 1, 1 + a ** 2, 1 - a ** 2})
# quoted exam matrices
ok("PD 24B-A-Q3a: eigenvalues 1, 1+-sqrt2 c",
   set(sp.Matrix([[1, c, 0], [c, 1, c], [0, c, 1]]).eigenvals().keys()) == {1, 1 + sp.sqrt(2) * c, 1 - sp.sqrt(2) * c})
ok("PD 24A-C-Q4a / 23B-B-Q3a: eigenvalues a, a^2+-1",
   set(sp.Matrix([[a ** 2, 0, 1], [0, a, 0], [1, 0, a ** 2]]).eigenvals().keys()) == {a, a ** 2 + 1, a ** 2 - 1})
ok("PD 24B-B-Q3a: eigenvalues k+1, k^2+-2k",
   set(sp.Matrix([[k ** 2, 0, 2 * k], [0, k + 1, 0], [2 * k, 0, k ** 2]]).eigenvals().keys()) == {k + 1, k ** 2 + 2 * k, k ** 2 - 2 * k})
ok("PD 25A-B-Q3a: eigenvalues a-1, a+1, 2a",
   set(sp.Matrix([[a, 0, 1], [0, 2 * a, 0], [1, 0, a]]).eigenvals().keys()) == {a - 1, a + 1, 2 * a})
ok("PD 24A-B-Q3a: eigenvalues 0, 2a^2, 2a^2+1 (always PSD, never strict)",
   set(sp.Matrix([[2 * a ** 2, a, 0], [a, 1, a], [0, a, 2 * a ** 2]]).eigenvals().keys()) == {0, 2 * a ** 2, 2 * a ** 2 + 1})
ok("PD 25B-A-Q3a: eigenvalues k, k(1+-sqrt2)",
   set(sp.Matrix([[k, k, 0], [k, k, k], [0, k, k]]).eigenvals().keys()) == {k, k * (1 + sp.sqrt(2)), k * (1 - sp.sqrt(2))})
# vectors with x^T C x < 0
C = sp.Matrix([[1, 3], [3, 8]])
xq = lambda M, v: (v.T * M * v)[0]
ok("PD 25A-B-Q3b: C=[[1,3],[3,8]]: (-3,1) gives -1, (1,1) gives 15; completing the square (a+3b)^2 - b^2",
   xq(C, sp.Matrix([-3, 1])) == -1 and xq(C, sp.Matrix([1, 1])) == 15 and sp.expand(xq(C, sp.Matrix(sp.symbols('p q'))) - ((sp.Symbol('p') + 3 * sp.Symbol('q')) ** 2 - sp.Symbol('q') ** 2)) == 0)
B2 = sp.Matrix([[4, 5], [5, 6]])
ok("PD 23A-B-Q4b: B=[[4,5],[5,6]] eigenvalue signs differ (det -1 < 0), (-5,4) gives -4",
   B2.det() == -1 and xq(B2, sp.Matrix([-5, 4])) == -4)
# generic test vectors: e_i and e_i+e_j, e_i-e_j
Mt = sp.Matrix([[1, 2], [2, 1]])
ok("PD test vectors: [[1,2],[2,1]] e1 gives 1>0, (1,-1) gives -2<0", xq(Mt, sp.Matrix([1, 0])) == 1 and xq(Mt, sp.Matrix([1, -1])) == -2)
# proof facts, random numeric checks
import numpy as np
rng = np.random.default_rng(7)
def ev_(M):
    return np.linalg.eigvalsh(np.array(M, dtype=float))
good = True
for _ in range(200):
    n = 3
    B = rng.integers(-3, 4, (n, n)).astype(float)
    C_ = rng.integers(-3, 4, (n, n)).astype(float)
    I_ = np.eye(n)
    S = B.T @ B + I_                      # symmetric, strictly positive definite
    Sp_ = B.T @ B                         # symmetric, positive semidefinite
    tol = 1e-9
    good &= bool(np.all(ev_(S) > 0))
    good &= bool(np.all(ev_(C_.T @ Sp_ @ C_) >= -tol))                      # B^T A B psd
    good &= bool(np.all(ev_(np.linalg.inv(S)) > 0))                         # A^-1 strict
    good &= bool(np.all(ev_(S @ S) > 0))                                    # A^2 strict
    good &= bool(np.all(ev_(I_ + S @ S) > 0))                               # I + A^2
    good &= bool(np.all(ev_(S + np.linalg.inv(S)) > 0))                     # A + A^-1
    good &= bool(np.all(ev_(-Sp_ - C_.T @ C_) <= tol))                      # -A - B^T B
    cc_ = ev_(Sp_).max() + 1
    good &= bool(np.all(ev_(cc_ * I_ - Sp_) > 0))                           # cI - A
ok("PD proof facts (200 random symmetric matrices): A^-1, A^2, I+A^2, A+A^-1 strict; B^T A B psd; -A-B^T B nsd; cI-A strict", good)
Sing = sp.Matrix([[1, 0], [0, 0]])
Bsing = sp.Matrix([[1, 1], [0, 0]])
Aspd = sp.Matrix([[2, 0], [0, 1]])
ok("PD trap: B^T A B with B singular is only semi-definite (example det 0)", (Bsing.T * Aspd * Bsing).det() == 0 and Aspd.det() > 0)
v_ = sp.Matrix([1, -1])
ok("PD trap: (B^T A B) kills (1,-1) for singular B", (Bsing.T * Aspd * Bsing) * v_ == sp.zeros(2, 1))
ok("PD <A^2 v, v> = |A v|^2 for symmetric A", sp.simplify(((Mt * Mt * sp.Matrix([sp.Symbol('p'), sp.Symbol('q')])).T * sp.Matrix([sp.Symbol('p'), sp.Symbol('q')]))[0]
                                                      - ((Mt * sp.Matrix([sp.Symbol('p'), sp.Symbol('q')])).T * (Mt * sp.Matrix([sp.Symbol('p'), sp.Symbol('q')])))[0]) == 0)
ok("PD eigenvalues of cI-A are c-lambda (A=[[2,1],[1,2]], c=5)", (5 * sp.eye(2) - sp.Matrix([[2, 1], [1, 2]])).eigenvals() == {4: 1, 2: 1})
# Sylvester: strict case only
Sy = sp.Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
ok("PD Sylvester: minors 2, 3, 4 > 0 for [[2,-1,0],[-1,2,-1],[0,-1,2]]", [Sy[:i, :i].det() for i in (1, 2, 3)] == [2, 3, 4] and all(e > 0 for e in Sy.eigenvals()))
Sz = sp.Matrix([[1, 1], [1, 1]])
ok("PD Sylvester warning: [[1,1],[1,1]] has minors 1, 0 (psd, not strict)", [Sz[:i, :i].det() for i in (1, 2)] == [1, 0] and sorted(Sz.eigenvals().keys()) == [0, 2])
Zm = sp.zeros(2, 2)
ok("PD zero matrix is both psd and nsd (25B-A-Q3a, k=0)", all(e == 0 for e in Zm.eigenvals()))

# ---------------------------------------------------------------- qr brief
Aq = sp.Matrix([[2, 1], [0, 1], [1, 1]])
a1 = Aq[:, 0]
a2 = Aq[:, 1]
u2 = a2 - (a2.T * a1)[0] / (a1.T * a1)[0] * a1
ok("QR worked: u2 = (-1/5, 1, 2/5), |u2|^2 = 6/5", u2 == sp.Matrix([-R(1, 5), 1, R(2, 5)]) and (u2.T * u2)[0] == R(6, 5))
Qq = sp.Matrix.hstack(a1 / sp.sqrt(5), u2 / sp.sqrt(R(6, 5)))
Rq = sp.simplify(Qq.T * Aq)
ok("QR worked: Q^T Q = I2 and R = Q^T A upper triangular",
   sp.simplify(Qq.T * Qq - sp.eye(2)) == sp.zeros(2, 2) and sp.simplify(Rq[1, 0]) == 0)
ok("QR worked: r11=sqrt5, r12=3/sqrt5, r22=sqrt(6/5)",
   sp.simplify(Rq[0, 0] - sp.sqrt(5)) == 0 and sp.simplify(Rq[0, 1] - 3 / sp.sqrt(5)) == 0 and sp.simplify(Rq[1, 1] - sp.sqrt(R(6, 5))) == 0)
ok("QR worked: Q R = A", sp.simplify(Qq * Rq - Aq) == sp.zeros(3, 2))
ok("QR worked: r11 = |a1|, r22 = |u2|", sp.simplify(Rq[0, 0] - sp.sqrt((a1.T * a1)[0])) == 0 and sp.simplify(Rq[1, 1] - sp.sqrt((u2.T * u2)[0])) == 0)
bq = sp.Matrix([1, 2, 3])
x_normal = (Aq.T * Aq).LUsolve(Aq.T * bq)
x_qr = sp.simplify(Rq.LUsolve(Qq.T * bq))
ok("QR worked: least squares via R x = Q^T b equals the normal equations", sp.simplify(x_qr - x_normal) == sp.zeros(2, 1), str(list(x_normal)))
# square case: solve A x = b by back substitution
As_ = sp.Matrix([[1, 1], [1, -1]])
bs_ = sp.Matrix([3, 1])
Qs_ = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
Rs_ = sp.simplify(Qs_.T * As_)
ok("QR square: A=[[1,1],[1,-1]] gives R=sqrt2 I, x = R^-1 Q^T b = (2,1)", sp.simplify(Rs_ - sp.sqrt(2) * sp.eye(2)) == sp.zeros(2, 2) and sp.simplify(Rs_.LUsolve(Qs_.T * bs_)) == sp.Matrix([2, 1]))
# exam QR checks quoted
Aex = sp.Matrix([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
cols = [Aex[:, i] for i in range(3)]
us = []
for cv in cols:
    wv = cv
    for uq in us:
        wv = wv - (cv.T * uq)[0] / (uq.T * uq)[0] * uq
    us.append(wv)
ok("QR 25B-B-Q4a: |u_i| = sqrt2, sqrt(3/2), 2/sqrt3 (diagonal of R)",
   [sp.simplify((u_.T * u_)[0]) for u_ in us] == [2, R(3, 2), R(4, 3)])

# ---------------------------------------------------------------- svd brief
As = sp.Matrix([[1, 1], [0, 1], [1, 0]])
AtA = As.T * As
ok("SVD worked: A^T A = [[2,1],[1,2]], eigenvalues 3,1", AtA == sp.Matrix([[2, 1], [1, 2]]) and AtA.eigenvals() == {3: 1, 1: 1})
vv1 = sp.Matrix([1, 1]) / sp.sqrt(2)
vv2 = sp.Matrix([1, -1]) / sp.sqrt(2)
ok("SVD worked: AtA v1 = 3 v1, AtA v2 = v2", AtA * vv1 == 3 * vv1 and AtA * vv2 == vv2)
uu1 = sp.simplify(As * vv1 / sp.sqrt(3))
uu2 = sp.simplify(As * vv2 / 1)
ok("SVD worked: u1 = (2,1,1)/sqrt6, u2 = (0,-1,1)/sqrt2",
   sp.simplify(uu1 - sp.Matrix([2, 1, 1]) / sp.sqrt(6)) == sp.zeros(3, 1) and sp.simplify(uu2 - sp.Matrix([0, -1, 1]) / sp.sqrt(2)) == sp.zeros(3, 1))
cr = sp.Matrix([2, 1, 1]).cross(sp.Matrix([0, -1, 1]))
ok("SVD worked: cross product (2,-2,-2), u3 = (1,-1,-1)/sqrt3", cr == sp.Matrix([2, -2, -2]))
uu3 = sp.Matrix([1, -1, -1]) / sp.sqrt(3)
U = sp.Matrix.hstack(uu1, uu2, uu3)
V = sp.Matrix.hstack(vv1, vv2)
S = sp.Matrix([[sp.sqrt(3), 0], [0, 1], [0, 0]])
ok("SVD worked: U orthogonal, V orthogonal, U S V^T = A",
   sp.simplify(U.T * U - sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(V.T * V - sp.eye(2)) == sp.zeros(2, 2) and sp.simplify(U * S * V.T - As) == sp.zeros(3, 2))
ok("SVD worked: A v_i = sigma_i u_i", sp.simplify(As * vv1 - sp.sqrt(3) * uu1) == sp.zeros(3, 1) and sp.simplify(As * vv2 - uu2) == sp.zeros(3, 1))
ok("SVD worked: rank 2 = number of nonzero sigma; |A|_F^2 = 4 = sigma1^2+sigma2^2 = 3+1", As.rank() == 2 and sum(e * e for e in As) == 4)
ok("SVD A A^T has eigenvalues 3,1,0 (same nonzero as A^T A)", (As * As.T).eigenvals() == {3: 1, 1: 1, 0: 1})
# wide matrix: choose A^T A or A A^T, the smaller one
Aw = sp.Matrix([[0, -1, 1], [1, 1, 0]])
ok("SVD wide (24A-C-Q3a): A A^T = [[2,-1],[-1,2]], sigma = sqrt3, 1, rank 2", Aw * Aw.T == sp.Matrix([[2, -1], [-1, 2]]) and (Aw * Aw.T).eigenvals() == {3: 1, 1: 1})
# repeated singular value (orthogonal matrix): all sigma = 1
ok("SVD orthogonal matrix has all singular values 1", (sp.Matrix([[0, 1], [1, 0]]).T * sp.Matrix([[0, 1], [1, 0]])).eigenvals() == {1: 2})
# quoted exam spectra
Ae = sp.Matrix([[2, 1], [1, -2], [0, 2]])
ok("SVD 24B-B-Q5a / 25B-A-Q5a: A^T A = [[5,0],[0,9]], sigma = 3, sqrt5", Ae.T * Ae == sp.Matrix([[5, 0], [0, 9]]))
Ae2 = sp.Matrix([[2, 0], [0, 2], [1, sp.sqrt(3)]])
ok("SVD 24A-A-Q5a: A^T A = [[5,sqrt3],[sqrt3,7]], eigenvalues 8, 4", (Ae2.T * Ae2).eigenvals() == {8: 1, 4: 1})
Ae3 = sp.Matrix([[1, 0], [0, 3], [0, 4]])
ok("SVD 23A-B-Q5a: A^T A = diag(1,25), sigma = 5, 1", Ae3.T * Ae3 == sp.diag(1, 25))
sys.exit(1 if bad else 0)
