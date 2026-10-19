# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-C.json -- algebra-2 (20079), semester A 2025, moed C (no date printed).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25A-C.py

Source: exam only, pp. 274-275 of the 275-page compilation (the solution of the preceding sitting sits on pp.
272-273 and is not this exam's). There is NO key: all 15 items are held with reason "no-key" and go to the solver.
Part letters: Q2: a.1..a.4 -> a..d, b.1 -> e, b.2 -> f. Q5: a, b.1 -> b, b.2 -> c. Q1, Q3, Q4: a, b.
Facts found while transcribing (tools/verify/25A-C/check.py): Q2b.2 as printed says only B in M_n(R); B^T A B is
then positive SEMIdefinite, and positive definite only for invertible B (counterexample in check.py). The solver
should state the assumption. Q2a.3 / Q2a.4 are the order of Z5* x Z7* and of (2,3).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-C.json"
NOKEY = "no-key: the sitting is exam-only, no answer source exists"


def H(num, part, kind, topic, question, points, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "question": question, "points": points, "hold": NOKEY}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"נסתכל בחבורה (אין צורך להוכיח זאת) $G=\left\{(a,b)\ \middle|\ a\in\mathbb{Z}_5^*,\ b\in\mathbb{Z}_7^*\right\}$ עם פעולת הכפל המוגדרת בצורה הבאה: $(a,b)\cdot(c,d)=(a\cdot c,\ b\cdot d)$, כאשר באגף ימין הכפל הוא מודולו 5 ו-7 בהתאמה."},
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף ב",
            "text": r"תהיינה $A,B\in M_n(\mathbb{R})$, כאשר $A$ מוגדרת חיובית. הוכיחו כי:"},
    "c5b": {"kind": "text", "title": "שאלה 5 סעיף ב",
            "text": r"תהי $G$ חבורה בה כל איבר הופכי לעצמו. זאת אומרת לכל $x\in G$ מתקיים $x=x^{-1}$. הוכיחו כי:"},
}

questions = [
    H(1, "א", "computation", "least_squares",
      r"סעיף א. נתונות 5 הנקודות במישור $(-4,-1),(-2,0),(2,4),(4,5),(5,6)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים. (12%)", 12),
    H(1, "ב", "proof", "cauchy_schwarz",
      r"סעיף ב. הוכיחו כי $\left(\displaystyle\int_1^2\frac{f(x)}x\,dx\right)^2\le\frac12\int_1^2f^2(x)\,dx$ כאשר $f(x)\in C_{[1,2]}$. (13%)", 13),

    H(2, "א", "computation", "groups", r"סעיף א.1. מהו האיבר הניטרלי של $G$ ? (3%)", 3, contextId="c2"),
    H(2, "ב", "computation", "groups", r"סעיף א.2. מצאו את האיבר ההופכי של $(2,3)$ ? (4%)", 4, contextId="c2"),
    H(2, "ג", "computation", "groups", r"סעיף א.3. מהו הסדר של $G$ ? (5%)", 5, contextId="c2"),
    H(2, "ד", "computation", "groups", r"סעיף א.4. מהו הסדר של $(2,3)$ ? (5%)", 5, contextId="c2"),
    H(2, "ה", "proof", "pos_def", r"סעיף ב.1. $-A-B^TB$ מוגדרת שלילית. (4%)", 4, contextId="c2b"),
    H(2, "ו", "proof", "pos_def", r"סעיף ב.2. $B^TAB$ מוגדרת חיובית. (4%)", 4, contextId="c2b",
      hold=NOKEY + "; note: as printed B is any real matrix, so B^T A B is only positive semidefinite (B singular), the item needs B invertible"),

    H(3, "א", "computation", "svd", r"סעיף א. מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}$. (18%)", 18),
    H(3, "ב", "proof", "inner_product",
      r"סעיף ב. יהי $V$ מרחב מכפלה פנימית ממשי. הוכיחו כי עבור כל $\vec v,\vec u\in V$ מתקיים $\langle\vec u,\vec v\rangle=\dfrac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$. (7%)", 7),

    H(4, "א", "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}a^2&0&1\\0&a&0\\1&0&a^2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (17%)", 17),
    H(4, "ב", "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod5\\x\equiv3\pmod2\\x\equiv4\pmod7\end{cases}$. (8%)", 8),

    H(5, "א", "computation", "orthodiag",
      r"סעיף א. בצעו לכסון אורתוגונלי למטריצה $A=\begin{pmatrix}5&0&0\\0&4&2\\0&2&1\end{pmatrix}$. (15%)", 15),
    H(5, "ב", "proof", "groups", r"סעיף ב.1. $G$ חבורה אבלית, כלומר לכל $x,y\in G$ מתקיים $x\cdot y=y\cdot x$. (5%)", 5, contextId="c5b"),
    H(5, "ג", "proof", "groups", r"סעיף ב.2. אם $x,y\in G$ ו-$x^3=y^5$ אז $x=y$. (5%)", 5, contextId="c5b"),
]

exam = {
    "examCode": "25A-C",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ה מועד ג'",
    "year": 2025,
    "examDate": "",
    "sourceFile": "algebra-2-25A-C-exam",
    "solutionFile": "none",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
