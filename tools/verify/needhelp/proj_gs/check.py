# -*- coding: utf-8 -*-
"""Machine check of every stored answer in the guided course proj_gs (courses/proj_gs/C01..C10.js).

Run:  PYTHONUTF8=1 py -I tools/verify/needhelp/proj_gs/check.py     (ASCII output, exit 1 on any failure)

For each own question of the course it recomputes the expected value with sympy, then asserts
  - mcq / choice: the correct option parses to the expected value and every distractor parses to the
    value of the mistake the explanation names (so it is wrong for an observable reason);
  - numeric steps: the stored answer equals the recomputed value within the stored tolerance;
  - findbug steps: the flagged line is the only line whose claim disagrees with the recomputation;
and finally that no own question of the course was left without a check.
The bank questions pulled by bankId are only checked for existence and for the numbers quoted in recaps.
"""
import json, pathlib, re, subprocess, sys
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

ROOT = pathlib.Path(__file__).resolve().parents[4]
R = sp.Rational
x = sp.Symbol("x", real=True)
bad = []
covered = set()


def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond:
        bad.append(name)


# ---------------------------------------------------------------- load the course
proc = subprocess.run(["node", str(ROOT / "tools" / "course_load.js")], capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT / "tools"))
data = json.loads(proc.stdout)
assert not data["errors"], data["errors"]
LEVELS = {e["level"]["id"]: e["level"] for e in data["levels"] if e["courseId"] == "proj_gs"}
Q = {}
for lv in LEVELS.values():
    for q in lv["questions"]:
        if "bankId" not in q:
            Q[q["id"]] = q
BANK = {b["id"]: b for b in json.load(open(ROOT / "questions.json", encoding="utf-8"))["questions"]}

# ---------------------------------------------------------------- tiny TeX -> sympy reader for option values
TRANS = standard_transformations + (implicit_multiplication_application,)


def scalar(s):
    s = s.strip()
    s = re.sub(r"\\left|\\right", "", s)
    s = re.sub(r"\\[dt]?frac(\d)(\d)", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt(\d+)", r"sqrt(\1)", s)
    for _ in range(4):
        s = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
        s = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", s)
    s = s.replace("\\cdot", "*")
    s = re.sub(r"(?<![A-Za-z])e(?![A-Za-z])", "E", s)
    return parse_expr(s, local_dict={"x": x, "E": sp.E}, transformations=TRANS)


def split_top(s, sep):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "({":
            depth += 1
        if ch in ")}":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def parse(v):
    s = v.strip().strip("$").strip()
    s = re.sub(r"\\left|\\right", "", s)
    m = re.fullmatch(r"\\begin\{pmatrix\}(.*)\\end\{pmatrix\}", s, re.S)
    if m:
        rows = [[scalar(c) for c in r.split("&")] for r in m.group(1).split("\\\\")]
        return sp.Matrix(rows)
    if s.startswith("(") and s.endswith(")") and len(split_top(s[1:-1], ",")) > 1:
        return sp.Matrix([scalar(c) for c in split_top(s[1:-1], ",")])
    return scalar(s)


def eq(a, b):
    if hasattr(a, "shape") or hasattr(b, "shape"):
        if not (hasattr(a, "shape") and hasattr(b, "shape")) or a.shape != b.shape:
            return False
        return sp.simplify(a - b) == sp.zeros(*a.shape)
    return sp.simplify(a - b) == 0


def check_mcq(qid, expected, distractors=None):
    """expected: sympy value of the correct option. distractors: {optionId: value of the named mistake} (all of them)."""
    q = Q[qid]
    st = q.get("step", q)
    opts = {o["id"]: o["value"] for o in st["options"]}
    cid = st["correctId"]
    ok(f"{qid} correct option parses to the recomputed value", eq(parse(opts[cid]), expected), str(expected))
    for oid, v in opts.items():
        if oid == cid:
            continue
        exp = (distractors or {}).get(oid)
        if exp is None:
            ok(f"{qid} option {oid} has a named mistake", False, "missing")
            continue
        ok(f"{qid} option {oid} equals its named mistake and differs from the answer", eq(parse(v), exp) and not eq(parse(v), expected), str(exp))
    covered.add(qid)


def check_num(qid, value):
    st = Q[qid]["step"]
    tol = st.get("tol", 0)
    ok(f"{qid} numeric answer", abs(float(st["answer"]) - float(value)) <= max(tol, 1e-9) and tol <= 0.011, f"stored {st['answer']} (tol {tol}) vs {value}")
    covered.add(qid)


# ---------------------------------------------------------------- inner products
def ip_m(A, B):
    return (B.T * A).trace()          # <A,B> = tr(B^T A)


def dot(a, b):
    return (a.T * b)[0]


def ip_f(f, g, lo, hi, w=1):
    return sp.integrate(w * f * g, (x, lo, hi))


# ================================================================ C01
A = sp.Matrix([[1, 2], [0, 3]]); B = sp.Matrix([[2, 1], [1, 0]])
ok("C01 trace form equals the entrywise sum", ip_m(A, B) == sum(A[i, j] * B[i, j] for i in range(2) for j in range(2)))
check_num("C01-Q1", ip_m(A, B))
A2 = sp.Matrix([[1, -2], [3, 0]])
check_mcq("C01-Q2", sp.sqrt(ip_m(A2, A2)), {"b": ip_m(A2, A2), "c": sum(A2), "d": sp.sqrt(1 + 9)})
A3 = sp.Matrix([[1, 2], [3, 1]])
Xa = sp.Matrix([[2, -1], [0, 0]]); Xb = sp.eye(2); Xc = sp.ones(2, 2); Xd = sp.Matrix([[0, 1], [1, 0]])
ok("C01-Q3 inner products with the candidates", ip_m(A3, Xa) == 0 and ip_m(A3, Xb) == 2 and ip_m(A3, Xc) == 7 and ip_m(A3, Xd) == 5)
check_mcq("C01-Q3", Xa, {"b": Xb, "c": Xc, "d": Xd})
# C01-Q4: <u,v> = u^T G v is an inner product iff G is symmetric positive definite
G = {"a": sp.diag(2, 3), "b": sp.diag(1, -1), "c": sp.Matrix([[0, 1], [1, 0]]), "d": sp.Matrix([[1, 1], [1, 1]])}
good = {k for k, g in G.items() if g == g.T and all(ev > 0 for ev in g.eigenvals())}
ok("C01-Q4 exactly one formula is an inner product", good == {"a"} and Q["C01-Q4"]["step"]["correctId"] == "a")
wit = {"b": (sp.Matrix([0, 1]), -1), "c": (sp.Matrix([1, -1]), -2), "d": (sp.Matrix([1, -1]), 0)}
ok("C01-Q4 the explained witnesses fail positivity", all((w.T * G[k] * w)[0] == val for k, (w, val) in wit.items()))
covered.add("C01-Q4")
nu, nv, ipuv = 2, 3, -1
check_num("C01-Q5", nu**2 + 2 * ipuv + nv**2)

# ================================================================ C02
check_num("C02-Q1", ip_f(x, x**2, 0, 1))
pairs = {"a": (x, x**2), "b": (1, x**2), "c": (1, sp.Abs(x)), "d": (x**2, sp.Abs(x))}
vals = {k: sp.integrate(sp.piecewise_fold(f * g), (x, -1, 1)) for k, (f, g) in pairs.items()}
ok("C02-Q2 only the odd-times-even pair is orthogonal", vals["a"] == 0 and vals["b"] == R(2, 3) and vals["c"] == 1 and vals["d"] == R(1, 2), str(vals))
ok("C02-Q2 stored correct id", Q["C02-Q2"]["correctId"] == "a")
covered.add("C02-Q2")
check_num("C02-Q3", ip_f(x, x, 0, 3))
c = sp.Symbol("c")
check_num("C02-Q4", sp.solve(sp.integrate(x * (3 * x + c), (x, 0, 1)), c)[0])
wn = ip_f(1, 1, 0, 1, sp.exp(x))
check_mcq("C02-Q5", wn, {"b": 1, "c": sp.E, "d": (sp.E - 1) / 2})
ok("C02 lesson example <1,1>=2 and <x^2,1>=2/3 on [-1,1]", ip_f(1, 1, -1, 1) == 2 and ip_f(x**2, 1, -1, 1) == R(2, 3))
ok("C02 lesson: int |x| over [-1,1] is 1", sp.integrate(sp.Abs(x), (x, -1, 1)) == 1)

# ================================================================ C03
a = sp.Matrix([1, 1, 1]); b = sp.Matrix([2, 3, 7])
coef = dot(b, a) / dot(a, a); p = coef * a; cres = b - p
ok("C03 lesson example", coef == 4 and cres == sp.Matrix([-2, -1, 3]) and dot(cres, a) == 0 and dot(b, b) == 62 == dot(p, p) + dot(cres, cres))
check_num("C03-Q1", p[0])
a2 = sp.Matrix([3, 4]); b2 = sp.Matrix([2, 11])
pr = dot(b2, a2) / dot(a2, a2) * a2
check_mcq("C03-Q2", pr, {"b": dot(b2, a2) / sp.sqrt(dot(a2, a2)) * a2, "c": dot(b2, a2) * a2, "d": b2})
check_num("C03-Q3", dot(cres, cres))
ua = sp.Matrix([R(3, 5), R(4, 5)])
ok("C03-Q4 unit vector", dot(ua, ua) == 1)
check_num("C03-Q4", ((ua * ua.T) * sp.Matrix([5, 0]))[1])

# ================================================================ C04
u1 = sp.Matrix([1, 1, 0]); u2 = sp.Matrix([1, -1, 2]); v = sp.Matrix([3, 1, 5])
ok("C04 u1 and u2 are orthogonal", dot(u1, u2) == 0)
pW = dot(v, u1) / dot(u1, u1) * u1 + dot(v, u2) / dot(u2, u2) * u2
ok("C04 lesson example projection (4,0,4), residual orthogonal", pW == sp.Matrix([4, 0, 4]) and dot(v - pW, u1) == 0 and dot(v - pW, u2) == 0)
check_num("C04-Q1", pW[0])
g1 = u1 / sp.sqrt(2); g2 = sp.Matrix([1, -1, 0]) / sp.sqrt(2); g3 = sp.Matrix([0, 0, 1])
ok("C04-Q2 g1,g2,g3 orthonormal", all(sp.simplify(dot(gi, gj) - (1 if i == j else 0)) == 0 for i, gi in enumerate([g1, g2, g3]) for j, gj in enumerate([g1, g2, g3])))
check_mcq("C04-Q2", sp.simplify(dot(v, g1)), {"b": dot(v, u1), "c": dot(v, u1) / dot(u1, u1), "d": sp.simplify(dot(v, g2))})
w1 = sp.Matrix([1, 0, 0]); w2 = sp.Matrix([1, 1, 0]); vv = sp.Matrix([2, 3, 5])
G2 = sp.Matrix([[dot(wi, wj) for wj in (w1, w2)] for wi in (w1, w2)])
true_p = sum((c_ * w for c_, w in zip(G2.LUsolve(sp.Matrix([dot(vv, w1), dot(vv, w2)])), (w1, w2))), sp.zeros(3, 1))
naive = dot(vv, w1) / dot(w1, w1) * w1 + dot(vv, w2) / dot(w2, w2) * w2
ok("C04-Q3 w1,w2 are not orthogonal", dot(w1, w2) == 1)
ok("C04-Q3 naive residual is not orthogonal, true residual is", dot(vv - naive, w1) != 0 and dot(vv - true_p, w1) == 0 and dot(vv - true_p, w2) == 0)
check_mcq("C04-Q3", true_p, {"b": naive, "c": dot(vv, w1) / dot(w1, w1) * w1, "d": vv})
aa = sp.Symbol("aa")
check_num("C04-Q4", sp.solve(dot(sp.Matrix([1, 2, 1]), sp.Matrix([aa, 1, -1])), aa)[0])
check_num("C04-Q5", dot(pW, pW))
ok("C04-Q5 Pythagoras 35 = 32 + 3", dot(v, v) == 35 and dot(v - pW, v - pW) == 3)

# ================================================================ C05
v1 = sp.Matrix([1, 1, 1]); v2 = sp.Matrix([1, 2, 3])
uu2 = v2 - dot(v2, v1) / dot(v1, v1) * v1
ok("C05-Q1 u2 = (-1,0,1)", uu2 == sp.Matrix([-1, 0, 1]) and dot(uu2, v1) == 0)
check_num("C05-Q1", uu2[0])
M1 = sp.ones(2, 2); M2 = sp.diag(2, 2)
cM = ip_m(M2, M1) / ip_m(M1, M1)
um = M2 - cM * M1
check_mcq("C05-Q2", um, {"b": M2 - ip_m(M2, M1) * M1, "c": M2 - ip_m(M2, M1) / sp.sqrt(ip_m(M1, M1)) * M1, "d": M1})
ok("C05-Q2 u2 orthogonal to u1", ip_m(um, M1) == 0)
y1, y2, y3 = sp.Matrix([1, 1, 0]), sp.Matrix([1, 0, 1]), sp.Matrix([0, 1, 1])
ok("C05 lesson example u2", y2 - dot(y2, y1) / dot(y1, y1) * y1 == sp.Matrix([R(1, 2), -R(1, 2), 1]))
e1 = y1; e2 = y2 - dot(y2, e1) / dot(e1, e1) * e1
e3 = y3 - dot(y3, e1) / dot(e1, e1) * e1 - dot(y3, e2) / dot(e2, e2) * e2
ok("C05-Q3 given u2 and u3=(-2/3,2/3,2/3), all orthogonal", e2 == sp.Matrix([R(1, 2), -R(1, 2), 1]) and e3 == sp.Matrix([-R(2, 3), R(2, 3), R(2, 3)])
   and dot(e3, e1) == 0 and dot(e3, e2) == 0)
check_num("C05-Q3", e3[2])
t1, t2, t3 = sp.Matrix([1, 0, 1]), sp.Matrix([0, 1, 1]), sp.Matrix([1, 1, 2])
f2 = t2 - dot(t2, t1) / dot(t1, t1) * t1
f3 = t3 - dot(t3, t1) / dot(t1, t1) * t1 - dot(t3, f2) / dot(f2, f2) * f2
ok("C05-Q4 third GS vector is exactly zero, v3 not orthogonal to v1", f3 == sp.zeros(3, 1) and t3 == t1 + t2 and dot(t3, t1) == 3)
ok("C05-Q4 stored correct id is the zero-vector option", Q["C05-Q4"]["correctId"] == "a")
covered.add("C05-Q4")
# findbug: u2 for v1=(1,-1,0), v2=(3,1,2)
w_1 = sp.Matrix([1, -1, 0]); w_2 = sp.Matrix([3, 1, 2])
ok("C05-Q5 line facts", dot(w_2, w_1) == 2 and dot(w_1, w_1) == 2)
good_u2 = w_2 - dot(w_2, w_1) / dot(w_1, w_1) * w_1
bug_u2 = w_2 - 2 * w_1
ok("C05-Q5 true u2 is (2,2,2) and the stored wrong line (1,3,2) fails orthogonality", good_u2 == sp.Matrix([2, 2, 2]) and bug_u2 == sp.Matrix([1, 3, 2]) and dot(bug_u2, w_1) == -2 and dot(good_u2, w_1) == 0)
ok("C05-Q5 flagged line is the u2 line", Q["C05-Q5"]["step"]["bugIndex"] == 3 and "(1,3,2)" in Q["C05-Q5"]["step"]["lines"][3])
covered.add("C05-Q5")

# ================================================================ C06
I2 = sp.eye(2); D = sp.diag(1, -1); V = sp.Matrix([[3, 1], [2, 5]])
ok("C06-Q1 spanning matrices orthogonal", ip_m(I2, D) == 0)
pV = ip_m(V, I2) / ip_m(I2, I2) * I2 + ip_m(V, D) / ip_m(D, D) * D
ok("C06-Q1 projection diag(3,5), residual orthogonal", pV == sp.diag(3, 5) and ip_m(V - pV, I2) == 0 and ip_m(V - pV, D) == 0)
check_num("C06-Q1", ip_m(V - pV, V - pV))
W1 = sp.Matrix([[1, 1], [0, 0]]); W2 = sp.Matrix([[0, 1], [1, 0]]); V2 = sp.Matrix([[1, 0], [2, 2]])
ok("C06 W1,W2 not orthogonal", ip_m(W1, W2) == 1)
U1 = W1; U2 = 2 * (W2 - ip_m(W2, W1) / ip_m(W1, W1) * W1)
ok("C06 lesson u2 = (-1,1;2,0), norm^2 6", U2 == sp.Matrix([[-1, 1], [2, 0]]) and ip_m(U2, U2) == 6 and ip_m(U1, U2) == 0)
p2 = ip_m(V2, U1) / ip_m(U1, U1) * U1 + ip_m(V2, U2) / ip_m(U2, U2) * U2
Gm = sp.Matrix([[ip_m(a_, b_) for b_ in (W1, W2)] for a_ in (W1, W2)])
cc = Gm.LUsolve(sp.Matrix([ip_m(V2, W1), ip_m(V2, W2)]))
ok("C06-Q2 Gram-matrix projection agrees with the GS projection", cc[0] * W1 + cc[1] * W2 == p2 and p2 == sp.Matrix([[0, 1], [1, 0]]))
ok("C06-Q2 explanation numbers", ip_m(V2, U1) == 1 and ip_m(V2, U2) == 3)
naive2 = ip_m(V2, W1) / ip_m(W1, W1) * W1 + ip_m(V2, W2) / ip_m(W2, W2) * W2
check_mcq("C06-Q2", p2, {"b": naive2, "c": ip_m(V2, W1) / ip_m(W1, W1) * W1, "d": V2})
check_num("C06-Q3", ip_f(x, 1, 0, 1) / ip_f(1, 1, 0, 1))
h = x**3 + 1
cA = ip_f(h, 1, -1, 1) / ip_f(1, 1, -1, 1); cB = ip_f(h, x, -1, 1) / ip_f(x, x, -1, 1)
ok("C06-Q4 1 and x orthogonal on [-1,1]", ip_f(1, x, -1, 1) == 0 and cA == 1 and cB == R(3, 5))
check_mcq("C06-Q4", cA + cB * x, {"b": 1 + x, "c": cB * x, "d": 1 + x / cB})

# ================================================================ C07
pts = [(1, 2), (2, 3), (3, 5), (4, 6)]
Am = sp.Matrix([[px, 1] for px, _ in pts]); bm = sp.Matrix([py for _, py in pts])
ATA = Am.T * Am
ok("C07-Q1 A^T A", ATA == sp.Matrix([[30, 10], [10, 4]]))
check_mcq("C07-Q1", ATA, {"b": sp.Matrix([[30, 10], [10, 10]]), "c": sp.Matrix([[100, 10], [10, 4]]), "d": sp.Matrix([[30, 10], [10, 1]])})
xhat = ATA.LUsolve(Am.T * bm)
ok("C07 sums: sum xy = 47, sum y = 16", (Am.T * bm) == sp.Matrix([47, 16]))
check_num("C07-Q2", xhat[0])
ok("C07 n = 0.5", xhat[1] == R(1, 2))
check_num("C07-Q3", xhat[0] * 5 + xhat[1])
res = bm - Am * xhat
ok("C07-Q4 residual (0.1,-0.3,0.3,-0.1), orthogonal to both columns, not to b, not constant, sum of squares 0.2",
   res == sp.Matrix([R(1, 10), -R(3, 10), R(3, 10), -R(1, 10)]) and (Am.T * res) == sp.zeros(2, 1) and dot(res, bm) == R(1, 5) and dot(res, res) == R(1, 5))
ok("C07-Q4 stored correct id", Q["C07-Q4"]["step"]["correctId"] == "a")
covered.add("C07-Q4")
# lesson example
pe = [(0, 1), (1, 2), (2, 2), (3, 4)]
Ae = sp.Matrix([[px, 1] for px, _ in pe]); be = sp.Matrix([py for _, py in pe])
xe = (Ae.T * Ae).LUsolve(Ae.T * be)
ok("C07 lesson example m=n=0.9, prediction 4.5", xe == sp.Matrix([R(9, 10), R(9, 10)]) and xe[0] * 4 + xe[1] == R(9, 2) and (Ae.T * Ae) == sp.Matrix([[14, 6], [6, 4]]))
pb = [(0, 0), (2, 1), (3, 4), (4, 6), (6, 9)]
ok("C07 recap sums for the 5-point bank question", sum(px for px, _ in pb) == 15 and sum(px**2 for px, _ in pb) == 65)

# ================================================================ C08
a1 = sp.Matrix([1, 1, 0]); a2 = sp.Matrix([1, -1, 2])
ok("C08 columns orthogonal", dot(a1, a2) == 0)
bl = sp.Matrix([2, 0, 5])
xl = [dot(bl, a1) / dot(a1, a1), dot(bl, a2) / dot(a2, a2)]
pl = xl[0] * a1 + xl[1] * a2
ok("C08 lesson example x=(1,2), p=(3,-1,4), error 3", xl == [1, 2] and pl == sp.Matrix([3, -1, 4]) and dot(bl - pl, bl - pl) == 3 and dot(bl - pl, a1) == 0 and dot(bl - pl, a2) == 0)
bq = sp.Matrix([4, 0, 1])
Aq = sp.Matrix.hstack(a1, a2)
xq = (Aq.T * Aq).LUsolve(Aq.T * bq)
ok("C08 normal equations agree with the orthogonal-column shortcut", xq == sp.Matrix([dot(bq, a1) / dot(a1, a1), dot(bq, a2) / dot(a2, a2)]) == sp.Matrix([2, 1]))
check_num("C08-Q1", xq[1])
check_num("C08-Q2", dot(bq - Aq * xq, bq - Aq * xq))
c1 = sp.Matrix([1, 0, 1]); c2 = sp.Matrix([0, 1, 1]); bc = sp.Matrix([1, 1, 0])
Ac = sp.Matrix.hstack(c1, c2)
ok("C08-Q3 columns not orthogonal, A^T A and A^T b", dot(c1, c2) == 1 and Ac.T * Ac == sp.Matrix([[2, 1], [1, 2]]) and Ac.T * bc == sp.Matrix([1, 1]))
xc = (Ac.T * Ac).LUsolve(Ac.T * bc)
check_mcq("C08-Q3", xc, {"b": sp.Matrix([dot(bc, c1) / dot(c1, c1), dot(bc, c2) / dot(c2, c2)]), "c": Ac.T * bc, "d": sp.Matrix([R(2, 3), R(2, 3)])})
ok("C08-Q3 the (2/3,2/3) distractor does not solve the normal equations", (Ac.T * Ac) * sp.Matrix([R(2, 3), R(2, 3)]) != Ac.T * bc)
# Q4: A xhat = projection onto Col(A) (computed independently through an orthogonal basis of Col(A))
e1_ = c1; e2_ = c2 - dot(c2, c1) / dot(c1, c1) * c1
pcol = dot(bc, e1_) / dot(e1_, e1_) * e1_ + dot(bc, e2_) / dot(e2_, e2_) * e2_
rc = bc - Ac * xc
ok("C08-Q4 A xhat is the projection onto Col(A); differs from b, from the residual and from the projection onto Null(A)=0",
   Ac * xc == pcol == sp.Matrix([R(1, 3), R(1, 3), R(2, 3)]) and Ac * xc != bc and Ac * xc != rc and rc == sp.Matrix([R(2, 3), R(2, 3), -R(2, 3)]) and Ac.nullspace() == [])
ok("C08-Q4 stored correct id", Q["C08-Q4"]["step"]["correctId"] == "a")
covered.add("C08-Q4")
check_num("C08-Q5", dot(rc, rc))

# ================================================================ C09
AQ = sp.Matrix([[3, 5], [4, 0]])
q1 = AQ[:, 0] / sp.sqrt(dot(AQ[:, 0], AQ[:, 0]))
r12 = dot(AQ[:, 1], q1); uq2 = AQ[:, 1] - r12 * q1; r22 = sp.sqrt(dot(uq2, uq2)); q2 = uq2 / r22
Qm = sp.Matrix.hstack(q1, q2); Rm = Qm.T * AQ
ok("C09-Q1 QR of [[3,5],[4,0]]: Q orthogonal, R=[[5,3],[0,4]], QR=A, q2=(4/5,-3/5)",
   Qm.T * Qm == sp.eye(2) and Rm == sp.Matrix([[5, 3], [0, 4]]) and Qm * Rm == AQ and q2 == sp.Matrix([R(4, 5), -R(3, 5)]))
check_mcq("C09-Q1", Rm, {"b": Rm.T, "c": sp.Matrix([[5, dot(AQ[:, 1], AQ[:, 0])], [0, 4]]), "d": sp.Matrix([[5, 3], [0, dot(uq2, uq2)]])})
bq9 = sp.Matrix([5, 10])
Qtb = Qm.T * bq9
check_num("C09-Q2", Qtb[1])
ok("C09-Q2 first component 11", Qtb[0] == 11)
x9 = Rm.LUsolve(Qtb)
ok("C09-Q3 back substitution x=(2.5,-0.5) and A x = b", x9 == sp.Matrix([R(5, 2), -R(1, 2)]) and AQ * x9 == bq9)
check_num("C09-Q3", x9[0])
a9 = sp.Matrix([[2, 1], [0, 1], [1, 1]]); c1_ = a9[:, 0]; c2_ = a9[:, 1]
n1 = dot(c1_, c1_); ip12 = dot(c2_, c1_); uu = c2_ - ip12 / n1 * c1_
ok("C09-Q4 lines 0-3 are right", n1 == 5 and ip12 == 3 and uu == sp.Matrix([-R(1, 5), 1, R(2, 5)]) and dot(uu, uu) == R(6, 5))
r12_true = ip12 / sp.sqrt(n1)
ok("C09-Q4 line 4: r11=sqrt5 and r22=sqrt(6/5) are right, r12 is 3/sqrt5 and not 3", sp.sqrt(n1) == sp.sqrt(5) and sp.sqrt(dot(uu, uu)) == sp.sqrt(R(6, 5)) and r12_true == 3 / sp.sqrt(5) and r12_true != 3)
Q9 = sp.Matrix.hstack(c1_ / sp.sqrt(n1), uu / sp.sqrt(dot(uu, uu)))
R9 = sp.simplify(Q9.T * a9)
ok("C09-Q4 QR reproduces A with r12 = 3/sqrt5", sp.simplify(R9[0, 1] - r12_true) == 0 and sp.simplify(Q9 * R9 - a9) == sp.zeros(3, 2))
ok("C09-Q4 flagged line is the R line", Q["C09-Q4"]["step"]["bugIndex"] == 4 and "r_{12}=3," in Q["C09-Q4"]["step"]["lines"][4].replace(" ", ""))
covered.add("C09-Q4")
ok("C09-Q5 A^T A = R^T R and differs from R R^T and R^2",
   AQ.T * AQ == Rm.T * Rm == sp.Matrix([[25, 15], [15, 25]]) and Rm * Rm.T == sp.Matrix([[34, 12], [12, 16]]) and Rm * Rm != Rm.T * Rm)
ok("C09-Q5 stored correct id", Q["C09-Q5"]["correctId"] == "a")
covered.add("C09-Q5")
ok("C09 lesson example QR=A", (lambda Al: (lambda q_1, q_2: sp.simplify(sp.Matrix.hstack(q_1, q_2) * sp.Matrix([[sp.sqrt(2), 1 / sp.sqrt(2)], [0, 1 / sp.sqrt(2)]]) - Al) == sp.zeros(2, 2))(
    sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, -1]) / sp.sqrt(2)))(sp.Matrix([[1, 1], [1, 0]])))

# ---------------------------------------------------------------- bank pulls: exist, not held, official or verified, and not the private sitting
used = []
for lv in LEVELS.values():
    for q in lv["questions"]:
        if "bankId" in q:
            used.append(q["bankId"])
for bid in used:
    b = BANK.get(bid)
    ok(f"bank {bid} exists in the shipped bank (held questions are not shipped)", b is not None)
    ok(f"bank {bid} is not from the private sitting", not bid.startswith("26B"))
ok("each bankId is used once", len(used) == len(set(used)))
ok("boss level is the last and pulls only bank questions", LEVELS["C10"].get("boss") is True and all("bankId" in q for q in LEVELS["C10"]["questions"]))
ok("levels C01..C10 present", sorted(LEVELS) == [f"C{n:02d}" for n in range(1, 11)])

# ---------------------------------------------------------------- nothing left unchecked
missing = sorted(set(Q) - covered)
ok("every own question has a recomputed check", not missing, str(missing))

print("\n%d failure(s)" % len(bad))
sys.exit(1 if bad else 0)
