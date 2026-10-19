# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-S.json -- algebra-2 (20079), semester A 2023, special sitting (20.04.2023, 09:00-12:00).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-S.py

Source: the exam exists only inside the 275-page compilation (pp. 149-150, typed). There is NO official solution.
The pages that follow it (pp. 151-160) are a student's handwritten scans of selected questions, mixed with questions
from other sittings; of this sitting only Q1a (pp. 154-155) and Q3b (p. 151) appear. Per GATE1 this sitting is
non-official (official:false).
5 printed questions (solve 4 of 5, 25% each); 9 items: 1 shipped (Q3b, student solution, correct) + 8 held.

Part letters: every question has printed parts a, b except Q4 (one part, no letter).
Every question text starts with its printed label.

Held (reason in the "hold" field; listed in docs/ASK_ADIR.md via the report; the orchestrator routes "no-key" to the solver):
- Q1a: the student's solution is WRONG (tools/verify/23A-S/check.py). The matrix [[a,2,0],[a+1,a,0],[0,0,a]] is not
  symmetric unless a = 1 (and at a = 1 it has eigenvalues 3, -1, 1, so it is indefinite); the student reads off the
  eigenvalues a, a +/- sqrt(2a+2) of a non-symmetric matrix and claims "positive for a >= 1+sqrt3".
- All other items: no solution in the source (no-key).
Q3b, the one shipped item: the student's argument (u = x^3, v = f, Cauchy-Schwarz, ||x^3||^2 = 1/7, square both sides)
is correct; checked with sympy. Source label is only "student solution"; no name appears in any field.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-S.json"

# ------------------------------------------------------------------ contexts
CTX = {
    "c5b": {"kind": "text", "title": "שאלה 5 סעיף ב",
            "text": r"במרחב הוקטורי $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע״י $\langle A,B\rangle=tr\left(B^TA\right)$ לכל $A,B\in M_2(\mathbb{R})$."},
}

S3B = (
    r"נסמן $\vec u=x^3$ ו-$\vec v=f(x)$ במרחב $C[0,1]$ עם המכפלה הפנימית $\langle f,g\rangle=\displaystyle\int_0^1f(x)g(x)\,dx$. לפי אי-שוויון קושי-שוורץ $|\langle\vec u,\vec v\rangle|\le\|\vec u\|\cdot\|\vec v\|$." "\n"
    r"$$\|\vec u\|=\sqrt{\langle x^3,x^3\rangle}=\sqrt{\int_0^1x^3\cdot x^3\,dx}=\sqrt{\left[\frac{x^7}7\right]_0^1}=\sqrt{\frac17},\qquad\|f(x)\|=\sqrt{\int_0^1f^2(x)\,dx}$$" "\n"
    r"$$\int_0^1x^3\cdot f(x)\,dx\le\sqrt{\frac17}\cdot\sqrt{\int_0^1f^2(x)\,dx}$$" "\n"
    r"נעלה בריבוע ונקבל: $\left(\displaystyle\int_0^1x^3f(x)\,dx\right)^2\le\dfrac17\displaystyle\int_0^1\left(f(x)\right)^2dx$."
)


def H(num, kind, topic, question, points, reason, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "points": points, "question": question, "hold": reason}
    if part:
        q["part"] = part
    q.update(kw)
    return q


NOKEY = "no-key"
questions = [
    H(1, "computation", "pos_def",
      r"(13 נק') האם קיימים ערכים ממשיים של הפרמטר $a$ עבור המטריצה $\begin{pmatrix}a&2&0\\a+1&a&0\\0&0&a\end{pmatrix}$ מוגדרת חיובית או מוגדרת שלילית? נמקו.",
      13, "the only solution in the source (a student's) is wrong: the matrix is not symmetric unless a=1 (then indefinite), the student used eigenvalues of a non-symmetric matrix; needs a solver", part="א"),
    H(1, "computation", "inner_product",
      r"(12 נק') יהי $V$ מרחב מכפלה פנימית ויהיו $\vec u,\vec v\in V$ וקטורים המקיימים: $\|\vec u\|=3$ , $\|\vec u+\vec v\|=4$ , $\|\vec u-\vec v\|=6$. מצאו את $\|\vec v\|$.",
      12, NOKEY, part="ב"),

    H(2, "computation", "least_squares",
      r"(15 נק') נתונות 5 הנקודות במישור $(5,7)$, $(3,5)$, $(1,4)$, $(-2,0)$, $(-3,2)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים.",
      15, NOKEY, part="א"),
    H(2, "proof", "orthogonality",
      r"(10 נק') תהי $Q\in M_n(\mathbb{R})$ אורתוגונלית וסימטרית בו זמנית. נגדיר $P=I+Q$. הוכיחו כי $P^2=2P$.",
      10, NOKEY, part="ב"),

    H(3, "computation", "qr", r"(15 נק') מצאו פירוק $QR$ עבור המטריצה $A=\begin{pmatrix}1&1&0\\0&0&1\\1&-1&1\end{pmatrix}$.",
      15, NOKEY, part="א"),
    {"num": 3, "part": "ב", "kind": "proof", "topic": "cauchy_schwarz", "points": 10,
     "question": r"(10 נק') הוכיחו את האי-השוויון הבא עבור כל פונקציה רציפה $f(x)$ על הקטע $[0,1]$: $\left(\displaystyle\int_0^1x^3f(x)\,dx\right)^2\le\dfrac17\displaystyle\int_0^1\left(f(x)\right)^2dx$.",
     "solution": S3B, "solutionSource": "student-solution", "official": False, "confidence": "med"},

    H(4, "proof", "groups",
      r"(25 נק') הוכיחו כי הקבוצה $G=\left\{A=\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}\in M_3(\mathbb{R})\ \middle|\ a,b,c\in\mathbb{R}\right\}$ יחד עם הפעולה של כפל מטריצות מהווה חבורה.",
      25, NOKEY),

    H(5, "computation", "crt",
      r"(13 נק') פתרו את המערכות הבאות באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod 5\\x\equiv3\pmod 2\\x\equiv4\pmod 7\end{cases}$.",
      13, NOKEY, part="א"),
    H(5, "computation", "projection",
      r"(12 נק') חשבו את ההיטל של $\begin{pmatrix}1&2\\3&0\end{pmatrix}$ על $Sp\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}1&3\\1&1\end{pmatrix}\right\}$.",
      12, NOKEY, part="ב", contextId="c5b"),
]

exam = {
    "examCode": "23A-S",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ג מועד מיוחד",
    "year": 2023,
    "examDate": "20.4.2023",
    "sourceFile": "algebra-2-23A-S-exam",
    "solutionFile": "student-solution-1",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
