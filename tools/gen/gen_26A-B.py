# -*- coding: utf-8 -*-
"""Generator for tools/raw/26A-B.json -- algebra-2 (20079), semester A 2026, moed B (4.05.2026).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_26A-B.py

Source: exam 2 pp. (text PDF, exam-only copy). There is NO official solution. The only answer source is a partial
handwritten STUDENT solution (anonymised, labelled "student-solution-1"); it covers Q1a.1, Q1a.2, Q2.1, Q2.2, Q2.3, Q2.5,
Q3a, Q3b, Q5b. Those 9 items are shipped as solutionSource "student-solution", official false, confidence med, written out
cleanly in the student's method and every result recomputed (tools/verify/26A-B/check.py, sympy, all OK).
Held ("no-key", routed to the solver): Q1b, Q2.4, Q4a, Q4b, Q4c, Q5a (no answer source). 15 items, 9 shipped + 6 held.
The sheet says "4 of 5", 25% each; all 5 questions are transcribed.
The scan also contains a student grade-report page (in another file); it is NOT used, quoted or shipped.

Part letters: numbered sub-parts get letters in order (Q1: a.1, a.2, b -> a, b, c; Q2: 1..5 -> a..e; Q4: a, b, c; Q5: a, b).
Every question text starts with its printed label.

Student-solution slips (fixed silently; logged in docs/ASK_ADIR.md):
- Q5b: the vector u is printed with last coordinate 1/sqrt2 (should be 1/sqrt n); written correctly.
- Q3a: the roots of the quadratic are given via the quadratic formula; written as the factorisation (x)(x+3).
- Q3a: "positive definite" in this course means positive SEMIdefinite (x in [0,1]); "strictly" is x in (0,1) (as in the
  flagship). The student's "neither" cases are x<0 or x>1; the negative (semi)definite answers follow from the same
  eigenvalues 1-x, x, x+3 (none exist) and are added.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26A-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


def H(num, kind, topic, question, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "hold": "no-key"}
    q.update(kw)
    return q


CTX = {
    "c1": {"kind": "text", "title": "שאלה 1 סעיף א",
           "text": r"לכל שני וקטורים $\vec u,\vec v\in\mathbb{R}^2$ נגדיר $\langle\vec u,\vec v\rangle_A=\vec u^TA\vec v$ כאשר $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$."},
    "c2": {"kind": "text", "title": "שאלה 2",
           "text": r"נסמן $M=\{x\in\mathbb{R}:x\neq1\}$. לכל $a,b\in M$ נגדיר את הפעולה הבאה: $a\odot b=ab-a-b+2$."},
    "c4": {"kind": "text", "title": "שאלה 4",
           "text": r"תהי $G=\left\{\begin{pmatrix}a&b&c\\0&a&b\\0&0&a\end{pmatrix}\ \middle|\ a,b,c\in\mathbb{Z}_5\ ,\ a\not\equiv0\pmod5\right\}$."},
}

S1A1 = (
    r"הצורה $\langle\vec u,\vec v\rangle_A=\vec u^TA\vec v$ מוגדרת לכל $\vec u,\vec v\in\mathbb{R}^2$ והערכים ממשיים. נבדוק את האקסיומות:" "\n"
    r"**אדיטיביות:** $\langle\vec u+\vec v,\vec w\rangle_A=(\vec u+\vec v)^TA\vec w=\vec u^TA\vec w+\vec v^TA\vec w=\langle\vec u,\vec w\rangle_A+\langle\vec v,\vec w\rangle_A$." "\n"
    r"**הומוגניות:** $\langle\alpha\vec u,\vec v\rangle_A=(\alpha\vec u)^TA\vec v=\alpha\vec u^TA\vec v=\alpha\langle\vec u,\vec v\rangle_A$." "\n"
    r"**סימטריה:** מכיוון ש-$A^T=A$ ומספר הוא שווה לשחלופו, $\langle\vec v,\vec u\rangle_A=\vec v^TA\vec u=\vec v^TA^T\vec u=(A\vec v)^T\vec u=\vec u^TA\vec v=\langle\vec u,\vec v\rangle_A$." "\n"
    r"**חיוביות:** $A$ סימטרית עם ערכים עצמיים $\lambda=1,3$ (מ-$(2-\lambda)^2-1=0$), שניהם חיוביים, לכן $A$ מוגדרת חיובית לחלוטין: $\langle\vec u,\vec u\rangle_A=\vec u^TA\vec u>0$ לכל $\vec u\neq\vec 0$. כמו כן $\langle\vec 0,\vec 0\rangle_A=0$, ואם $\langle\vec u,\vec u\rangle_A=0$ אז $\vec u=\vec 0$." "\n"
    "לכן $\\langle\\cdot,\\cdot\\rangle_A$ היא מכפלה פנימית."
)

S1A2 = (
    r"$$\left\langle\begin{pmatrix}1\\t\end{pmatrix},\begin{pmatrix}t\\-1\end{pmatrix}\right\rangle_A=(1,t)\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}t\\-1\end{pmatrix}=(1,t)\begin{pmatrix}2t-1\\t-2\end{pmatrix}=0$$" "\n"
    r"$$2t-1+t(t-2)=0\ \Rightarrow\ t^2-1=0\ \Rightarrow\ t=\pm1$$"
)

S2_1 = (
    r"$$(a\odot b)\odot c=(ab-a-b+2)c-(ab-a-b+2)-c+2=abc-ac-bc+2c-ab+a+b-2-c+2=abc-ab-ac-bc+a+b+c$$" "\n"
    r"$$a\odot(b\odot c)=a(bc-b-c+2)-a-(bc-b-c+2)+2=abc-ab-ac+2a-a-bc+b+c-2+2=abc-ab-ac-bc+a+b+c$$" "\n"
    "הביטויים שווים, לכן הפעולה אסוציאטיבית."
)

S2_2 = (
    r"נחפש $e\in M$ כך שלכל $a\in M$ מתקיים $e\odot a=a\odot e=a$:" "\n"
    r"$$ea-e-a+2=a\ \Rightarrow\ ea-e=2a-2\ \Rightarrow\ e(a-1)=2(a-1)\ \Rightarrow\ e=2$$" "\n"
    r"ו-$2\in M$ (כי $2\neq1$). הפעולה קומוטטיבית, לכן $2$ הוא איבר ניטרלי דו-צדדי. קיים איבר ניטרלי: $e=2$."
)

S2_3 = (
    r"**סגירות:** $a\odot b=1$ אם ורק אם $ab-a-b+1=0$, כלומר $(a-1)(b-1)=0$, כלומר $a=1$ או $b=1$, בסתירה ל-$a,b\in M$. לכן $a\odot b\in M$ ו-$\odot$ פעולה בינארית על $M$." "\n"
    r"**אסוציאטיביות:** הוכחה בסעיף 1. **איבר ניטרלי:** $e=2\in M$ (סעיף 2)." "\n"
    r"**איבר הופכי:** נחפש $a^{-1}\in M$ עם $a\odot a^{-1}=2$:" "\n"
    r"$$aa^{-1}-a-a^{-1}+2=2\ \Rightarrow\ a^{-1}(a-1)=a\ \Rightarrow\ a^{-1}=\frac{a}{a-1}\qquad(a\neq1)$$" "\n"
    r"וההופכי נמצא ב-$M$ כי $\dfrac{a}{a-1}\neq1$ (שוויון היה נותן $a=a-1$). בדיקה: $a\odot\dfrac a{a-1}=(a-1)\left(\dfrac a{a-1}-1\right)+1=2$." "\n"
    r"**קומוטטיביות:** $ab-a-b+2=ba-b-a+2$ לכל $a,b\in M$." "\n"
    "לכן $(M,\\odot)$ חבורה קומוטטיבית."
)

S2_5 = (
    r"נשים לב ש-$x\odot y=(x-1)(y-1)+1$. נוכיח באינדוקציה ש-$a^n=(a-1)^n+1$:" "\n"
    r"**בסיס:** $a^1=a=(a-1)^1+1$." "\n"
    r"**הנחה:** $a^n=(a-1)^n+1$ לאיזשהו $n\in\mathbb{N}$." "\n"
    r"**צעד:** $a^{n+1}=a^n\odot a=\left((a-1)^n+1\right)\odot a=\left((a-1)^n+1\right)a-\left((a-1)^n+1\right)-a+2$" "\n"
    r"$$=a(a-1)^n+a-(a-1)^n-1-a+2=a(a-1)^n-(a-1)^n+1=(a-1)^n(a-1)+1=(a-1)^{n+1}+1$$" "\n"
    "לכן הטענה נכונה לכל $n\\in\\mathbb{N}$."
)

S3A = (
    r"$$\det(A-\lambda I)=\begin{vmatrix}1-\lambda&x&1\\x&1-\lambda&1\\1&1&x+2-\lambda\end{vmatrix}=0\ \Rightarrow\ (1-x-\lambda)(x-\lambda)(x+3-\lambda)=0$$" "\n"
    r"(הגורם $\lambda=1-x$ נמצא על ידי חיסור שורות, והמשוואה הריבועית שנותרה היא $-\lambda^2+(2x+3)\lambda-x^2-3x=0$ ולפי נוסחת השורשים $\lambda=x,\ x+3$.)" "\n"
    r"$$\lambda_1=1-x,\qquad\lambda_2=x,\qquad\lambda_3=x+3$$" "\n"
    r"טבלת סימנים: $1-x\ge0$ כאשר $x\le1$, $\ x\ge0$ כאשר $x\ge0$, $\ x+3\ge0$ כאשר $x\ge-3$." "\n"
    "**תשובה סופית:**\n"
    r"מוגדרת חיובית: $0\le x\le1$" "\n"
    r"מוגדרת חיובית לחלוטין: $0<x<1$" "\n"
    "מוגדרת שלילית ומוגדרת שלילית לחלוטין: לא קיים $x$\n"
    r"לכל ערך אחר ($x<0$ או $x>1$) המטריצה אינה מוגדרת (אף אחת מהן)."
)

S3B = (
    r"**$A^2$:** $A$ סימטרית ($A^T=A$), לכן $\left(A^2\right)^T=(AA)^T=A^TA^T=AA=A^2$, כלומר $A^2$ סימטרית." "\n"
    r"לכל $\vec u\neq\vec0$, נסמן $\vec v=A\vec u$ (וזה $\neq\vec 0$ כי $A$ הפיכה, ערכיה העצמיים חיוביים):" "\n"
    r"$$\langle A^2\vec u,\vec u\rangle=\vec u^TA^2\vec u=\vec u^TA^TA\vec u=(A\vec u)^T(A\vec u)=\vec v^T\vec v=\|\vec v\|^2>0$$" "\n"
    r"לכן $A^2$ מוגדרת חיובית לחלוטין." "\n"
    r"**$A^{-1}$:** $\left(A^{-1}\right)^T=\left(A^T\right)^{-1}=A^{-1}$, כלומר $A^{-1}$ סימטרית." "\n"
    r"$A$ מוגדרת חיובית לחלוטין, לכן כל הערכים העצמיים שלה $\lambda_i>0$. אם $\vec v$ וקטור עצמי של $A$ עם ערך עצמי $\lambda$, אז $A\vec v=\lambda\vec v$, נכפול ב-$A^{-1}$: $\vec v=\lambda A^{-1}\vec v$, כלומר $A^{-1}\vec v=\dfrac1\lambda\vec v$." "\n"
    r"לכן $\dfrac1\lambda$ הוא ערך עצמי של $A^{-1}$, ו-$\dfrac1\lambda>0$ כי $\lambda>0$. כל הערכים העצמיים של $A^{-1}$ חיוביים ו-$A^{-1}$ סימטרית, לכן היא מוגדרת חיובית לחלוטין."
)

S5B = (
    r"נגדיר ב-$\mathbb{R}^n$ שני וקטורים: $\ \bar u=\left(\dfrac1{\sqrt1},\dfrac1{\sqrt2},\dots,\dfrac1{\sqrt n}\right)$ , $\ \bar v=\left(\dfrac1{1^{3/2}},\dfrac1{2^{3/2}},\dots,\dfrac1{n^{3/2}}\right)$. אז" "\n"
    r"$$\|\bar u\|^2=\sum_{k=1}^n\frac1k,\qquad\|\bar v\|^2=\sum_{k=1}^n\frac1{k^3},\qquad\langle\bar u,\bar v\rangle=\sum_{k=1}^n\frac1{\sqrt k}\cdot\frac1{k^{3/2}}=\sum_{k=1}^n\frac1{k^2}$$" "\n"
    r"לפי אי-שוויון קושי-שוורץ $|\langle\bar u,\bar v\rangle|\le\|\bar u\|\cdot\|\bar v\|$, כלומר" "\n"
    r"$$\left|\sum_{k=1}^n\frac1{k^2}\right|\le\sqrt{\sum_{k=1}^n\frac1k}\cdot\sqrt{\sum_{k=1}^n\frac1{k^3}}$$" "\n"
    r"ובהעלאה בריבוע (שני האגפים אי-שליליים):" "\n"
    r"$$\left(\sum_{k=1}^n\frac1{k^2}\right)^2\le\left(\sum_{k=1}^n\frac1k\right)\cdot\left(\sum_{k=1}^n\frac1{k^3}\right)$$"
)

questions = [
    Q(1, "proof", "inner_product", r"סעיף א.1. הוכיחו כי $\langle\cdot,\cdot\rangle_A$ היא מכפלה פנימית. (10%)", S1A1, part="א", points=10,
      contextId="c1"),
    Q(1, "computation", "orthogonality",
      r"סעיף א.2. מצאו את כל הערכים של $t\in\mathbb{R}$ עבורם $\vec u=\begin{pmatrix}1\\t\end{pmatrix}$ ו-$\vec v=\begin{pmatrix}t\\-1\end{pmatrix}$ הם וקטורים אורתוגונליים ביחס למכפלה $\langle\cdot,\cdot\rangle_A$. (5%)",
      S1A2, part="ב", points=5, contextId="c1"),
    H(1, "computation", "least_squares",
      r"סעיף ב. פתרו את בעיית הריבועים הפחותים עבור $A\vec x=\vec b$ כאשר $A=\begin{pmatrix}1&-2\\-1&2\\0&3\\2&5\end{pmatrix}$ , $\vec b=\begin{pmatrix}3\\1\\-4\\2\end{pmatrix}$. (10%)",
      part="ג", points=10),

    Q(2, "truefalse", "groups", r"סעיף 1. האם הפעולה אסוציאטיבית? (5%)", S2_1, part="א", points=5, contextId="c2", verdict=True),
    Q(2, "truefalse", "groups", r"סעיף 2. האם ב-$(M,\odot)$ קיים איבר נייטרלי? (5%)", S2_2, part="ב", points=5, contextId="c2",
      verdict=True),
    Q(2, "truefalse", "groups", r"סעיף 3. האם המבנה $(M,\odot)$ הוא חבורה קומוטטיבית? (5%)", S2_3, part="ג", points=5, contextId="c2",
      verdict=True),
    H(2, "truefalse", "groups", r"סעיף 4. האם קיים $x\in M$ כך ש: $x\odot x=x$ ? (5%)", part="ד", points=5, contextId="c2"),
    Q(2, "proof", "groups",
      r"סעיף 5. נגדיר $a^n=\underbrace{a\odot\cdots\odot a}_{n\ \text{times}}$. הוכיחו באינדוקציה כי $a^n=(a-1)^n+1$ לכל $n\in\mathbb{N}$. (5%)",
      S2_5, part="ה", points=5, contextId="c2"),

    Q(3, "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $x\in\mathbb{R}$ המטריצה $A=\begin{pmatrix}1&x&1\\x&1&1\\1&1&x+2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (17%)",
      S3A, part="א", points=17),
    Q(3, "proof", "pos_def",
      r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית לחלוטין. הוכיחו כי $A^2$ ו-$A^{-1}$ הן גם מוגדרות חיובית לחלוטין. (8%)",
      S3B, part="ב", points=8),

    H(4, "proof", "groups",
      r"סעיף א. הוכיחו כי $G$ היא חבורה ביחס לכפל מטריצות. (הכפל והחיבור של רכיבי המטריצות הם מודולו 5). (15%)",
      part="א", points=15, contextId="c4"),
    H(4, "computation", "groups", r"סעיף ב. מצאו את הסדר של $G$. (5%)", part="ב", points=5, contextId="c4"),
    H(4, "computation", "groups", r"סעיף ג. מצאו את הסדר של $X=\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}$. (5%)", part="ג", points=5,
      contextId="c4"),

    H(5, "computation", "crt",
      r"סעיף א. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod3\\x\equiv1\pmod5\\x\equiv4\pmod8\end{cases}$. (10%)",
      part="א", points=10),
    Q(5, "proof", "cauchy_schwarz",
      r"סעיף ב. הוכיחו כי לכל $n\in\mathbb{N}$ מתקיים אי-השוויון הבא: $\left(\displaystyle\sum_{k=1}^n\frac1{k^2}\right)^2\le\left(\displaystyle\sum_{k=1}^n\frac1k\right)\cdot\left(\displaystyle\sum_{k=1}^n\frac1{k^3}\right)$. (15%)",
      S5B, part="ב", points=15),
]

exam = {
    "examCode": "26A-B",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ו מועד ב'",
    "year": 2026,
    "examDate": "4.5.2026",
    "sourceFile": "algebra-2-26A-B-exam",
    "solutionFile": "student-solution-1",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
