# -*- coding: utf-8 -*-
"""Generator for tools/raw/26B-A.json -- algebra-2 (20079), semester B 2026, moed A (17.06.2026).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_26B-A.py

Source: exam 2 pp. (text PDF). There is NO official solution, so every item is held with reason "no-key"
(the orchestrator routes the sitting to the solver). The question texts are transcribed in full so the solver can use them.
The sheet says "4 of 5", 25% each; 5 questions, 15 items (the printed ע"י is written with a gershayim). Q5 is printed with parts "ג" and "ד" (letters kept as printed).
Part letters: numbered sub-parts get letters in order (Q1: a.1, a.2, b -> a, b, c; Q2: 1..5 -> a..e; Q4: a, b, c).
The unidentified 17-page scan "2026-B.PDF" is a handwritten student solution of THIS sitting (not a distinct sitting)
with a student grade-report page; it is personal data, not an official source, and is not used or quoted.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26B-A.json"


def H(num, kind, topic, question, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "hold": "no-key"}
    q.update(kw)
    return q


CTX = {
    "c1": {"kind": "text", "title": "שאלה 1 סעיף א",
           "text": r"במרחב וקטורי $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע״י $\langle A,B\rangle=tr\left(B^TA\right)$."},
    "c2": {"kind": "text", "title": "שאלה 2",
           "text": r"נסתכל בחבורה $G=\left\{\begin{pmatrix}a&b\\0&c\end{pmatrix}\in M_2(\mathbb{Z}_5)\ \middle|\ a\cdot c\neq0\pmod5\right\}$ ביחס לכפל מטריצות (חבורת המטריצות המשולשות העליונות ההפיכות מסדר $2\times2$ עם רכיבים מ-$\mathbb{Z}_5$). תהי $H=\{J^n\mid n\in\mathbb{Z}\}$ תת-חבורה ציקלית של $G$ כאשר $J=\begin{pmatrix}1&1\\0&2\end{pmatrix}$."},
}

questions = [
    H(1, "computation", "orthogonality",
      r"סעיף א.1. בצעו תהליך גרם-שמידט עבור המערכת $\left\{A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ B=\begin{pmatrix}1&1\\0&-1\end{pmatrix}\right\}$. (9%)",
      part="א", points=9, contextId="c1"),
    H(1, "computation", "projection",
      r"סעיף א.2. חשבו את ההיטל של $C=\begin{pmatrix}2&3\\1&0\end{pmatrix}$ על $U=\mathrm{Sp}\{A,B\}$. (6%)",
      part="ב", points=6, contextId="c1"),
    H(1, "proof", "pos_def",
      r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית לחלוטין. הוכיחו כי $A+A^2$ ו-$A+A^{-1}$ הן גם מוגדרות חיובית לחלוטין. (10%)",
      part="ג", points=10),

    H(2, "computation", "groups", r"סעיף 1. מהו הסדר של $G$ ? (6%)", part="א", points=6, contextId="c2"),
    H(2, "computation", "groups", r"סעיף 2. חשבו את כל האיברים של $H$. (6%)", part="ב", points=6, contextId="c2"),
    H(2, "computation", "groups", r"סעיף 3. מצאו את $J^{-1}$. (4%)", part="ג", points=4, contextId="c2"),
    H(2, "computation", "groups", r"סעיף 4. מהו הסדר של $H$ ? (3%)", part="ד", points=3, contextId="c2"),
    H(2, "computation", "groups", r"סעיף 5. מצאו $A\in G$ כך $AJA^{-1}\notin H$. (6%)", part="ה", points=6, contextId="c2"),

    H(3, "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}1&0&2a\\0&4-a^2&0\\2a&0&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (15%)",
      part="א", points=15),
    H(3, "computation", "least_squares",
      r"סעיף ב. נתונות 5 נקודות במישור: $(0,2),\ (1,2),\ (2,4),\ (3,8),\ (4,9)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו בעזרת שיטת הריבועים הפחותים. (10%)",
      part="ב", points=10),

    H(4, "proof", "groups",
      r"סעיף א. תהי $G$ חבורה בה לכל $x,y\in G$ מתקיים $(xy)^2=x^2y^2$. הוכיחו כי $G$ חבורה אבלית, כלומר לכל $x,y\in G$ מתקיים $x\cdot y=y\cdot x$. (7%)",
      part="א", points=7),
    H(4, "proof", "groups",
      r"סעיף ב. תהי $K$ חבורה ו-$x,y\in K$. הוכיחו כי אם $xyx^{-1}=y^2$, אז $x^2yx^{-2}=y^4$. (7%)",
      part="ב", points=7),
    H(4, "proof", "cauchy_schwarz",
      r"סעיף ג. הוכיחו את אי השוויון הבא: $\displaystyle\left(\sum_{k=1}^n\sqrt{(2k-1)\ln k}\right)^2\le n^2\ln(n!)$. (11%)",
      part="ג", points=11),

    H(5, "computation", "svd", r"סעיף ג. מצאו פירוק SVD עבור המטריצה $A=\begin{pmatrix}3&2\\2&3\\2&-2\end{pmatrix}$. (17%)", part="ג", points=17),
    H(5, "computation", "crt",
      r"סעיף ד. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv3\pmod5\\x\equiv2\pmod8\\x\equiv4\pmod9\end{cases}$. (8%)",
      part="ד", points=8),
]

exam = {
    "examCode": "26B-A",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ו מועד א'",
    "year": 2026,
    "examDate": "17.6.2026",
    "sourceFile": "algebra-2-26B-A-exam",
    "solutionFile": "none",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
