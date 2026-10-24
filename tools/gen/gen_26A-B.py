# -*- coding: utf-8 -*-
"""Generator for tools/raw/26A-B.json -- algebra-2 (20079), semester A 2026, moed B (4.05.2026).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_26A-B.py

Source: exam 2 pp. (text PDF, exam-only copy). There is NO official solution. The only answer source is a partial
handwritten STUDENT solution (anonymised, labelled "student-solution-1"); it covers Q1a.1, Q1a.2, Q2.1, Q2.2, Q2.3, Q2.5,
Q3a, Q3b, Q5b. Those 9 items are shipped as solutionSource "student-solution", official false, confidence med, written out
cleanly in the student's method and every result recomputed (tools/verify/26A-B/check.py, sympy, all OK).
Q1b (item Q1c), Q2.4, Q4a, Q4b, Q4c, Q5a have no answer source: written by the solver (SV: solutionSource "solved",
official false; checked in tools/verify/26A-B/solve_held.py; the student scan was not consulted for them). Pending the
refuter. 15 items, all shipped.
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

S1B = (
    r"העמודות של $A$ בלתי תלויות (אינן פרופורציונליות), לכן $A^TA$ הפיכה ולמשוואות הנורמליות $A^TA\hat x=A^T\vec b$ יש פתרון יחיד." "\n"
    r"$$A^TA=\begin{pmatrix}1&-1&0&2\\-2&2&3&5\end{pmatrix}\begin{pmatrix}1&-2\\-1&2\\0&3\\2&5\end{pmatrix}=\begin{pmatrix}6&6\\6&42\end{pmatrix},\qquad A^T\vec b=\begin{pmatrix}1&-1&0&2\\-2&2&3&5\end{pmatrix}\begin{pmatrix}3\\1\\-4\\2\end{pmatrix}=\begin{pmatrix}6\\-6\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}6&6\\6&42\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}6\\-6\end{pmatrix}\ \Rightarrow\ \begin{cases}x_1+x_2=1\\x_1+7x_2=-1\end{cases}\ \Rightarrow\ 6x_2=-2\ \Rightarrow\ x_2=-\frac13,\ x_1=\frac43$$" "\n"
    r"$$\hat x=\begin{pmatrix}\frac43\\-\frac13\end{pmatrix}$$" "\n"
    r"בדיקה: $A\hat x=\begin{pmatrix}2\\-2\\-1\\1\end{pmatrix}$ ו-$\vec b-A\hat x=\begin{pmatrix}1\\3\\-3\\1\end{pmatrix}$ ניצב לשתי העמודות של $A$ ($1-3+0+2=0$ , $\ -2+6-9+5=0$)."
)

S2_4 = (
    "כן.\n"
    r"$$x\odot x=x\ \Longleftrightarrow\ x^2-x-x+2=x\ \Longleftrightarrow\ x^2-3x+2=0\ \Longleftrightarrow\ (x-1)(x-2)=0$$" "\n"
    r"$x=1\notin M$ , אבל $x=2\in M$ ומתקיים $2\odot2=4-2-2+2=2$. לכן קיים $x\in M$ כזה, והוא יחיד: $x=2$ (האיבר הניטרלי)."
)

S4A = (
    r"**סגירות:** לכל $\begin{pmatrix}a&b&c\\0&a&b\\0&0&a\end{pmatrix},\begin{pmatrix}d&e&f\\0&d&e\\0&0&d\end{pmatrix}\in G$:" "\n"
    r"$$\begin{pmatrix}a&b&c\\0&a&b\\0&0&a\end{pmatrix}\begin{pmatrix}d&e&f\\0&d&e\\0&0&d\end{pmatrix}=\begin{pmatrix}ad&ae+bd&af+be+cd\\0&ad&ae+bd\\0&0&ad\end{pmatrix}$$" "\n"
    r"המכפלה מאותה צורה (רכיבים מ-$\mathbb{Z}_5$), ו-$ad\not\equiv0\pmod 5$ כי $5$ ראשוני ו-$a,d\not\equiv0$. לכן המכפלה ב-$G$." "\n"
    "**אסוציאטיביות:** נובעת מאסוציאטיביות של כפל מטריצות (גם מודולו 5).\n"
    r"**איבר ניטרלי:** $I=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\in G$ ($a=1,\ b=c=0$)." "\n"
    r"**איבר הופכי:** נחפש $\begin{pmatrix}d&e&f\\0&d&e\\0&0&d\end{pmatrix}$ עם מכפלה $I$, כלומר" "\n"
    r"$$\begin{cases}ad\equiv1\\ae+bd\equiv0\\af+be+cd\equiv0\end{cases}\pmod 5\ \Rightarrow\ d=a^{-1},\quad e=-ba^{-2},\quad f=\left(b^2-ac\right)a^{-3}$$" "\n"
    r"($a^{-1}$ קיים מודולו $5$ כי $a\not\equiv0$ ו-$5$ ראשוני.) בדיקה של השוויון השלישי: $af+be+cd=\left(b^2-ac\right)a^{-2}-b^2a^{-2}+ca^{-1}=0$." "\n"
    r"ההופכי מאותה צורה ו-$d=a^{-1}\not\equiv0$ , לכן הוא ב-$G$ (ובמטריצות משולשיות מאותה צורה הכפל קומוטטיבי, כך שזה הופכי משני הצדדים)." "\n"
    r"לכן $G$ חבורה ביחס לכפל מטריצות."
)

S4B_ORD = (
    r"איבר של $G$ נקבע ביחידות על ידי $(a,b,c)$: יש $4$ אפשרויות ל-$a\in\{1,2,3,4\}$ (כי $a\not\equiv0$), ו-$5$ אפשרויות לכל אחד מ-$b,c\in\mathbb{Z}_5$." "\n"
    r"$$|G|=4\cdot5\cdot5=100$$"
)

S4C = (
    r"נכתוב $X=I+N$ כאשר $N=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$. מתקיים $N^2=0$ ו-$IN=NI$, ולכן באינדוקציה $X^n=I+nN=\begin{pmatrix}1&0&n\\0&1&0\\0&0&1\end{pmatrix}$." "\n"
    r"$$X^2=\begin{pmatrix}1&0&2\\0&1&0\\0&0&1\end{pmatrix},\ X^3=\begin{pmatrix}1&0&3\\0&1&0\\0&0&1\end{pmatrix},\ X^4=\begin{pmatrix}1&0&4\\0&1&0\\0&0&1\end{pmatrix},\ X^5=\begin{pmatrix}1&0&5\\0&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\pmod 5$$" "\n"
    r"$X^n=I$ אם ורק אם $n\equiv0\pmod 5$, לכן $o(X)=5$."
)

S5A = (
    r"$\gcd(3,5)=\gcd(3,8)=\gcd(5,8)=1$ , לכן יש פתרון יחיד מודולו $M=3\cdot5\cdot8=120$." "\n"
    r"$a_1=2,\ a_2=1,\ a_3=4$ ; $\ m_1=3,\ m_2=5,\ m_3=8$" "\n"
    r"$$M_1=\frac{120}{3}=40,\qquad M_2=\frac{120}{5}=24,\qquad M_3=\frac{120}{8}=15$$" "\n"
    r"$$40x_1\equiv1\pmod 3:\quad x_1\equiv1\pmod 3$$" "\n"
    r"$$24x_2\equiv1\pmod 5:\quad4x_2\equiv1\pmod 5\ \Rightarrow\ x_2\equiv4\pmod 5$$" "\n"
    r"$$15x_3\equiv1\pmod 8:\quad7x_3\equiv1\pmod 8\ \Rightarrow\ x_3\equiv7\pmod 8$$" "\n"
    r"$$x\equiv a_1M_1x_1+a_2M_2x_2+a_3M_3x_3=2\cdot40\cdot1+1\cdot24\cdot4+4\cdot15\cdot7=80+96+420=596\pmod{120}$$" "\n"
    r"$$596=4\cdot120+116\ \Rightarrow\ x\equiv116\pmod{120}$$" "\n"
    r"בדיקה: $116=38\cdot3+2$ , $\ 116=23\cdot5+1$ , $\ 116=14\cdot8+4$."
)


def SV(num, kind, topic, question, solution, **kw):
    """Solver-written item (no answer source): solved, official false, pending the refuter."""
    return Q(num, kind, topic, question, solution, solutionSource="solved", official=False, confidence="high", **kw)


questions = [
    Q(1, "proof", "inner_product", r"סעיף א.1. הוכיחו כי $\langle\cdot,\cdot\rangle_A$ היא מכפלה פנימית. (10%)", S1A1, part="א", points=10,
      contextId="c1"),
    Q(1, "computation", "orthogonality",
      r"סעיף א.2. מצאו את כל הערכים של $t\in\mathbb{R}$ עבורם $\vec u=\begin{pmatrix}1\\t\end{pmatrix}$ ו-$\vec v=\begin{pmatrix}t\\-1\end{pmatrix}$ הם וקטורים אורתוגונליים ביחס למכפלה $\langle\cdot,\cdot\rangle_A$. (5%)",
      S1A2, part="ב", points=5, contextId="c1"),
    SV(1, "computation", "least_squares",
      r"סעיף ב. פתרו את בעיית הריבועים הפחותים עבור $A\vec x=\vec b$ כאשר $A=\begin{pmatrix}1&-2\\-1&2\\0&3\\2&5\end{pmatrix}$ , $\vec b=\begin{pmatrix}3\\1\\-4\\2\end{pmatrix}$. (10%)",
      S1B, part="ג", points=10),

    Q(2, "truefalse", "groups", r"סעיף 1. האם הפעולה אסוציאטיבית? (5%)", S2_1, part="א", points=5, contextId="c2", verdict=True),
    Q(2, "truefalse", "groups", r"סעיף 2. האם ב-$(M,\odot)$ קיים איבר נייטרלי? (5%)", S2_2, part="ב", points=5, contextId="c2",
      verdict=True),
    Q(2, "truefalse", "groups", r"סעיף 3. האם המבנה $(M,\odot)$ הוא חבורה קומוטטיבית? (5%)", S2_3, part="ג", points=5, contextId="c2",
      verdict=True),
    SV(2, "truefalse", "groups", r"סעיף 4. האם קיים $x\in M$ כך ש: $x\odot x=x$ ? (5%)", S2_4, part="ד", points=5, contextId="c2",
       verdict=True),
    Q(2, "proof", "groups",
      r"סעיף 5. נגדיר $a^n=\underbrace{a\odot\cdots\odot a}_{n\ \text{times}}$. הוכיחו באינדוקציה כי $a^n=(a-1)^n+1$ לכל $n\in\mathbb{N}$. (5%)",
      S2_5, part="ה", points=5, contextId="c2"),

    Q(3, "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $x\in\mathbb{R}$ המטריצה $A=\begin{pmatrix}1&x&1\\x&1&1\\1&1&x+2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (17%)",
      S3A, part="א", points=17),
    Q(3, "proof", "pos_def",
      r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית לחלוטין. הוכיחו כי $A^2$ ו-$A^{-1}$ הן גם מוגדרות חיובית לחלוטין. (8%)",
      S3B, part="ב", points=8),

    SV(4, "proof", "groups",
      r"סעיף א. הוכיחו כי $G$ היא חבורה ביחס לכפל מטריצות. (הכפל והחיבור של רכיבי המטריצות הם מודולו 5). (15%)",
      S4A, part="א", points=15, contextId="c4"),
    SV(4, "computation", "groups", r"סעיף ב. מצאו את הסדר של $G$. (5%)", S4B_ORD, part="ב", points=5, contextId="c4"),
    SV(4, "computation", "groups", r"סעיף ג. מצאו את הסדר של $X=\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}$. (5%)", S4C, part="ג",
      points=5, contextId="c4"),

    SV(5, "computation", "crt",
      r"סעיף א. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod3\\x\equiv1\pmod5\\x\equiv4\pmod8\end{cases}$. (10%)",
      S5A, part="א", points=10),
    Q(5, "proof", "cauchy_schwarz",
      r"סעיף ב. הוכיחו כי לכל $n\in\mathbb{N}$ מתקיים אי-השוויון הבא: $\left(\displaystyle\sum_{k=1}^n\frac1{k^2}\right)^2\le\left(\displaystyle\sum_{k=1}^n\frac1k\right)\cdot\left(\displaystyle\sum_{k=1}^n\frac1{k^3}\right)$. (15%)",
      S5B, part="ב", points=15),
]

# ---------------------------------------------------------------- rubric / pitfalls / steps (step-author, ai-draft)
# Every numeric value is recomputed in tools/verify/26A-B/steps_check.py (sympy / brute force).
# Steps are derived from the stored solutions (partly student-written, partly solver-written), never from the scan.
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def num(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def ch(prompt, options, correct, explain):
    return {"type": "choice", "prompt": prompt, "options": opts(*options), "correctId": IDS[correct], "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def bug(prompt, lines, idx, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": idx, "explain": explain}


EXTRA = {
    (1, "א"): dict(
        rubric=rub(("אדיטיביות של $\\langle\\cdot,\\cdot\\rangle_A$ מליניאריות הכפל במטריצה", 2),
                   ("הומוגניות", 2),
                   (r"סימטריה: שימוש ב-$A^T=A$ ובכך שמספר שווה לשחלופו", 3),
                   (r"חיוביות: הערכים העצמיים $1,3$ חיוביים, ולכן $\vec u^TA\vec u>0$ לכל $\vec u\ne\vec0$", 3)),
        pitfalls=["לבדוק רק חיוביות ולהשמיט את הסימטריה או את הלינאריות.",
                  r"לטעון שהצורה חיובית רק כי איברי $A$ חיוביים (למשל $\begin{pmatrix}1&2\\2&1\end{pmatrix}$ חיובית באיברים ואינה מוגדרת חיובית).",
                  r"לשכוח שהסימטריה של הצורה נובעת מהסימטריה של המטריצה $A$."],
        steps=[num(r"מהו הערך העצמי הקטן של $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$?", 1, r"$(2-\lambda)^2-1=0$ נותן $\lambda=1,3$."),
               num(r"ומהו הערך העצמי הגדול?", 3, r"$\lambda=3$. שניהם חיוביים, ולכן $A$ מוגדרת חיובית לחלוטין."),
               ch(r"איזו תכונה של $A$ מבטיחה ש-$\langle\vec u,\vec v\rangle_A=\langle\vec v,\vec u\rangle_A$?",
                  [r"$A^T=A$", "$A$ הפיכה", "כל איברי $A$ חיוביים"], 0,
                  r"עבור $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ (הפיכה) מתקבל $\vec e_1^TA\vec e_2=2$ אבל $\vec e_2^TA\vec e_1=0$. עבור $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ (איברים חיוביים) מתקבלים $2$ ו-$3$."),
               order("סדרו את הוכחת הסימטריה.",
                     [r"$\langle\vec v,\vec u\rangle_A=\vec v^TA\vec u$",
                      r"$=\vec v^TA^T\vec u$ כי $A^T=A$",
                      r"$=(A\vec v)^T\vec u$",
                      r"$=\vec u^T(A\vec v)=\langle\vec u,\vec v\rangle_A$, כי מספר שווה לשחלופו"],
                     "כל שלב נשען על הקודם.")],
    ),
    (1, "ב"): dict(
        rubric=rub((r"כתיבת התנאי $\vec u^TA\vec v=0$ עבור הווקטורים הנתונים", 2),
                   (r"חישוב $2t-1+t(t-2)$", 2),
                   (r"פתרון $t^2-1=0$ ו-$t=\pm1$", 1)),
        pitfalls=["להשתמש במכפלה הסקלרית הרגילה במקום ב-$\\vec u^TA\\vec v$.",
                  r"להסתפק בשורש $t=1$ ולשכוח את $t=-1$."],
        steps=[num(r"עבור $t=2$ חשבו את $\langle\vec u,\vec v\rangle_A$ כאשר $\vec u=\begin{pmatrix}1\\2\end{pmatrix}$, $\vec v=\begin{pmatrix}2\\-1\end{pmatrix}$.", 3,
                   r"$A\vec v=\begin{pmatrix}3\\0\end{pmatrix}$ ולכן $\vec u^TA\vec v=3$."),
               num(r"לאחר הצבה כללית מתקבלת המשוואה $2t-1+t(t-2)=0$. מהו ערך הביטוי $2t-1+t(t-2)$ עבור $t=3$?", 8,
                   r"הביטוי שווה ל-$t^2-1=8$."),
               ch("מהי קבוצת הפתרונות?",
                  [r"$t=1$ או $t=-1$", r"$t=1$ בלבד", r"$t=0$ או $t=1$", r"$t=2$ או $t=-2$"], 0,
                  r"$t^2-1=0$. עבור $t=0$ מתקבל $-1\ne0$, עבור $t=2$ מתקבל $3\ne0$, ו-$t=-1$ אכן נותן $(1,-1)^TA(-1,-1)^T=0$.")],
    ),
    (1, "ג"): dict(
        rubric=rub(("כתיבת המשוואות הנורמליות $A^TA\\hat x=A^T\\vec b$ (העמודות בלתי תלויות)", 2),
                   (r"חישוב $A^TA$ ו-$A^T\vec b$", 3),
                   (r"פתרון המערכת: $x_2=-\frac13,\ x_1=\frac43$", 3),
                   (r"בדיקה שהשארית ניצבת לעמודות", 2)),
        pitfalls=[r"לחשב $AA^T$ במקום $A^TA$.",
                  r"לטעות בסימן של $A^T\vec b$ (שהשני בו שלילי).",
                  "לשכוח לוודא שהעמודות בלתי תלויות, כדי ש-$A^TA$ תהיה הפיכה."],
        steps=[num(r"מהו הרכיב השמאלי התחתון (שורה 2, עמודה 2) של $A^TA$?", 42, r"$(-2)^2+2^2+3^2+5^2=4+4+9+25=42$."),
               num(r"מהו הרכיב השני של $A^T\vec b$?", -6, r"$-2\cdot3+2\cdot1+3\cdot(-4)+5\cdot2=-6+2-12+10=-6$."),
               num(r"מהו $x_2$ (עיגול לשתי ספרות אחרי הנקודה)?", -0.33, r"מהמערכת $x_1+x_2=1,\ x_1+7x_2=-1$ מתקבל $x_2=-\frac13$.", tol=0.01),
               num(r"מהו $x_1$ (עיגול לשתי ספרות אחרי הנקודה)?", 1.33, r"$x_1=1-x_2=\frac43$.", tol=0.01)],
    ),
    (2, "א"): dict(
        rubric=rub((r"חישוב $(a\odot b)\odot c$", 2),
                   (r"חישוב $a\odot(b\odot c)$", 2),
                   ("השוואה: שני הביטויים שווים, ולכן אסוציאטיבית", 1)),
        pitfalls=["להסיק אסוציאטיביות מדוגמה מספרית בלבד.",
                  r"לשכוח את הקבוע $+2$ כשמציבים תוצאה של פעולה כאחד המשתנים."],
        steps=[num(r"חשבו $3\odot3$.", 5, r"$9-3-3+2=5$."),
               num(r"חשבו $(3\odot3)\odot3$.", 9, r"$5\odot3=15-5-3+2=9$."),
               ch(r"מהו הביטוי המשותף ל-$(a\odot b)\odot c$ ול-$a\odot(b\odot c)$?",
                  [r"$abc-ab-ac-bc+a+b+c$", r"$abc-ab-ac-bc+a+b+c+1$", r"$abc-ab-bc+a+b+c$"], 0,
                  r"עבור $a=b=c=3$ הביטוי $abc-ab-ac-bc+a+b+c$ נותן $9$ כבחישוב הישיר, הביטוי עם $+1$ נותן $10$, והביטוי ללא $-ac$ נותן $18$.")],
    ),
    (2, "ב"): dict(
        rubric=rub((r"הצבת התנאי $e\odot a=a$", 1),
                   (r"הגעה ל-$e(a-1)=2(a-1)$", 2),
                   (r"חילוק ב-$a-1\ne0$: $e=2$", 1),
                   (r"$2\in M$ והפעולה קומוטטיבית, ולכן ניטרלי דו-צדדי", 1)),
        pitfalls=[r"לחלק ב-$a-1$ בלי לציין ש-$a\ne1$.",
                  r"לשכוח לבדוק ש-$e=2$ שייך ל-$M$."],
        steps=[num(r"פתרו את $e(a-1)=2(a-1)$ עבור $a\ne1$. מהו $e$?", 2, r"מחלקים ב-$a-1$: $e=2$."),
               ch(r"מדוע מותר לחלק ב-$a-1$?",
                  [r"כי $a\in M$ ולכן $a\ne1$", r"כי $e\ne1$", r"כי $a>1$"], 0,
                  r"$M$ כוללת גם מספרים קטנים מ-$1$ (למשל $a=0$), ולכן $a>1$ אינו נכון; ההיתר לחלק מגיע רק מכך ש-$a\ne1$.")],
    ),
    (2, "ג"): dict(
        rubric=rub((r"סגירות: $a\odot b=1$ רק אם $a=1$ או $b=1$", 1),
                   (r"מציאת ההופכי $a^{-1}=\frac a{a-1}$", 2),
                   (r"ההופכי שייך ל-$M$", 1),
                   ("קומוטטיביות", 1)),
        pitfalls=[r"לשכוח לבדוק סגירות: שהתוצאה אינה $1$.",
                  r"לשכוח להראות שההופכי $\frac a{a-1}$ שונה מ-$1$."],
        steps=[ch(r"מתי $a\odot b=1$?",
                  [r"$(a-1)(b-1)=0$", r"$ab=1$", r"$(a-1)(b-1)=1$"], 0,
                  r"$a\odot b-1=ab-a-b+1=(a-1)(b-1)$. לדוגמה $2\odot\frac12=\frac12\ne1$ אף ש-$ab=1$, ו-$3\odot3=5\ne1$ כי $(3-1)(3-1)=4\ne0$."),
               num(r"מהו ההופכי של $3$ (עיגול לשתי ספרות)?", 1.5, r"$\frac a{a-1}=\frac32$. בדיקה: $3\odot1.5=2$.", tol=0.01),
               num(r"מהו ההופכי של $-1$?", 0.5, r"$\frac{-1}{-2}=0.5$. בדיקה: $-1\odot0.5=2$.", tol=0.01)],
    ),
    (2, "ד"): dict(
        rubric=rub((r"המשוואה $x^2-3x+2=0$", 2),
                   (r"פירוק $(x-1)(x-2)$", 1),
                   (r"$x=1\notin M$ ו-$x=2\in M$", 1),
                   ("מסקנה: כן, $x=2$", 1)),
        pitfalls=[r"לכלול את $x=1$ אף שאינו שייך ל-$M$.",
                  r"להסיק שאין פתרון כי אחד השורשים נפסל."],
        steps=[num(r"המשוואה $x\odot x=x$ שקולה ל-$(x-1)(x-2)=0$. איזה שורש שייך ל-$M$?", 2, r"$x=1\notin M$, ולכן הפתרון הוא $x=2$."),
               ch(r"מדוע $x=1$ נפסל?",
                  [r"כי $1\notin M$", r"כי $1\odot1\ne1$", r"כי $1$ אינו שורש"], 0,
                  r"$1\odot1=1-1-1+2=1$, כלומר $x=1$ כן שורש של המשוואה; הוא נפסל רק כי $M$ אינה כוללת את $1$."),
               num(r"חשבו $2\odot2$.", 2, r"$4-2-2+2=2$.")],
    ),
    (2, "ה"): dict(
        rubric=rub(("בסיס: $n=1$", 1), ("הנחת האינדוקציה", 1), (r"צעד: $a^{n+1}=a^n\odot a$ והשלמת החישוב", 3)),
        pitfalls=["לשכוח את בסיס האינדוקציה.",
                  r"לכתוב $a^{n+1}=a^n+a$ (פעולה רגילה) במקום $a^n\odot a$."],
        steps=[num(r"חשבו את $a^4$ עבור $a=3$ בעזרת הנוסחה $(a-1)^n+1$.", 17,
                   r"$2^4+1=17$, ובחישוב ישיר $3\odot3=5,\ 5\odot3=9,\ 9\odot3=17$."),
               order("סדרו את שלבי האינדוקציה.",
                     [r"בסיס: $a^1=a=(a-1)^1+1$.",
                      r"הנחה: $a^n=(a-1)^n+1$ לאיזשהו $n$.",
                      r"צעד: $a^{n+1}=a^n\odot a=\left((a-1)^n+1\right)\odot a$.",
                      r"לפי $x\odot y=(x-1)(y-1)+1$: $=(a-1)^n(a-1)+1=(a-1)^{n+1}+1$."],
                     "בסיס, הנחה, פתיחת הצעד, חישוב."),
               bug("באינדוקציה הבאה שורה אחת שגויה. מצאו אותה.",
                   [r"בסיס: $a^1=a=(a-1)^1+1$.",
                    r"הנחה: $a^n=(a-1)^n+1$ לאיזשהו $n$.",
                    r"צעד: $a^{n+1}=a^n\odot a=\left((a-1)^n+1\right)\odot a$.",
                    r"לפי $x\odot y=(x-1)(y-1)+1$: $=(a-1)^n\cdot a+1=(a-1)^{n+1}+1$."],
                   3, r"$x-1=(a-1)^n$ ו-$y-1=a-1$, ולכן המכפלה היא $(a-1)^n(a-1)$ ולא $(a-1)^n\cdot a$.")],
    ),
    (3, "א"): dict(
        rubric=rub((r"חישוב $\det(A-\lambda I)$ והגורם $1-x-\lambda$", 4),
                   (r"שורשי הריבועית: $x$ ו-$x+3$", 4),
                   (r"מוגדרת חיובית: $0\le x\le1$", 3),
                   (r"מוגדרת חיובית לחלוטין: $0<x<1$", 3),
                   ("מוגדרת שלילית ושלילית לחלוטין: אף ערך; אחרת אף אחת מהן", 3)),
        pitfalls=[r"להתבלבל בין $\ge0$ ל-$>0$ בקצוות $x=0$ ו-$x=1$.",
                  "להסיק שמוגדרת שלילית קיימת רק מכך שאחד הערכים העצמיים שלילי.",
                  r"לטעות בסימן של הערך העצמי $1-x$ (לא $x-1$)."],
        steps=[num(r"מהו העקבה (סכום האיברים באלכסון) של $A$ עבור $x=2$? (היא שווה לסכום הערכים העצמיים.)", 6, r"$1+1+(x+2)=6$."),
               ch("מהם הערכים העצמיים של $A$?",
                  [r"$1-x,\ x,\ x+3$", r"$x-1,\ x,\ x+3$", r"$1-x,\ x,\ x+2$", r"$1+x,\ x,\ x+3$"], 0,
                  r"סכום הערכים העצמיים חייב להיות העקבה $x+4$. הקבוצה $\{1-x,x,x+3\}$ נותנת $x+4$, הקבוצה עם $x-1$ נותנת $3x+2$, הקבוצה עם $x+2$ נותנת $x+3$, והקבוצה עם $1+x$ נותנת $3x+4$."),
               ch("עבור אילו $x$ המטריצה מוגדרת חיובית (לא בהכרח לחלוטין)?",
                  [r"$0\le x\le1$", r"$0<x<1$", r"$-3\le x\le1$", r"$x\ge0$"], 0,
                  r"נדרש $1-x\ge0$, $x\ge0$ ו-$x+3\ge0$. עבור $x=0$ מתקבלים $1,0,3$ (חיובית), עבור $x=-1$ יש ערך עצמי $-1$, ועבור $x=2$ יש ערך עצמי $-1$."),
               ch("עבור אילו $x$ המטריצה מוגדרת חיובית לחלוטין?",
                  [r"$0\le x\le1$", r"$0<x<1$", r"$x>0$"], 1,
                  r"כל הערכים העצמיים חייבים להיות חיוביים ממש: $0<x<1$.")],
    ),
    (3, "ב"): dict(
        rubric=rub((r"$A^2$ סימטרית", 1),
                   (r"חיוביות של $A^2$: $\vec u^TA^2\vec u=\|A\vec u\|^2>0$ כי $A\vec u\ne\vec0$", 3),
                   (r"$A^{-1}$ סימטרית", 1),
                   (r"הערכים העצמיים של $A^{-1}$ הם $\frac1\lambda>0$", 3)),
        pitfalls=[r"לשכוח לנמק ש-$A\vec u\ne\vec0$ (כי $A$ הפיכה).",
                  r"לטעון ש-$A^{-1}$ חיובית כי $A$ חיובית, בלי לטפל בערכים העצמיים.",
                  "לבדוק חיוביות בלבד ולשכוח סימטריה."],
        steps=[num(r"ל-$A$ ערכים עצמיים $2$ ו-$5$. מהו הערך העצמי הקטן של $A^{-1}$?", 0.2, r"הערכים העצמיים של $A^{-1}$ הם $\frac12$ ו-$\frac15$.", tol=0.001),
               ch(r"אם $A\vec v=\lambda\vec v$ ו-$\lambda\ne0$, מהו הערך העצמי של $A^{-1}$ עבור $\vec v$?",
                  [r"$\frac1\lambda$", r"$\lambda$", r"$-\lambda$", r"$\lambda^2$"], 0,
                  r"מכפילים ב-$A^{-1}$: $\vec v=\lambda A^{-1}\vec v$, כלומר $A^{-1}\vec v=\frac1\lambda\vec v$. עבור $A=\mathrm{diag}(2,5)$ הערכים של $A^{-1}$ הם $\frac12,\frac15$ ולא $2,5,-2,-5,4,25$."),
               order(r"סדרו את הוכחת החיוביות של $A^2$.",
                     [r"לכל $\vec u\ne\vec0$ נסמן $\vec v=A\vec u$; $\vec v\ne\vec0$ כי $A$ הפיכה.",
                      r"$\vec u^TA^2\vec u=\vec u^TA^TA\vec u=(A\vec u)^T(A\vec u)=\|\vec v\|^2$.",
                      r"$\|\vec v\|^2>0$, ולכן $A^2$ מוגדרת חיובית לחלוטין."],
                     "מגדירים $\\vec v$, מפרקים את הביטוי לנורמה, ומסיקים חיוביות.")],
    ),
    (4, "א"): dict(
        rubric=rub((r"סגירות: מכפלה מאותה צורה ו-$ad\not\equiv0$", 4),
                   ("אסוציאטיביות מכפל מטריצות", 2),
                   (r"איבר ניטרלי $I$", 2),
                   (r"הופכי: $d=a^{-1},\ e=-ba^{-2},\ f=\left(b^2-ac\right)a^{-3}$", 6),
                   ("מסקנה: חבורה", 1)),
        pitfalls=[r"לשכוח ש-$ad\not\equiv0\pmod5$ דורש ש-$5$ ראשוני.",
                  r"לשכוח לעבוד מודולו 5 כשמחשבים את $a^{-1}$.",
                  "לבדוק את ההופכי רק בשתי המשוואות הראשונות ולדלג על השלישית."],
        steps=[ch(r"מדוע $ad\not\equiv0\pmod5$ כשידוע ש-$a,d\not\equiv0$?",
                  [r"כי $5$ ראשוני, ולכן מכפלה של שני איברים שונים מאפס ב-$\mathbb{Z}_5$ שונה מאפס",
                   r"כי $ad$ מספר שלם חיובי, ולכן אינו מתחלק ב-$5$",
                   "כי המטריצה משולשית"], 0,
                  r"הטיעון על מספר שלם חיובי שגוי: $2\cdot5=10$ חיובי ומתחלק ב-$5$. הטיעון על משולשיות אינו קשור לשאלה."),
               num(r"עבור $a=2$ מהו $d=a^{-1}$ ב-$\mathbb{Z}_5$ (בין $0$ ל-$4$)?", 3, r"$2\cdot3=6\equiv1$."),
               num(r"עבור $a=2,\ b=1$ מהו $e=-ba^{-2}$ ב-$\mathbb{Z}_5$ (בין $0$ ל-$4$)?", 1, r"$a^{-2}=9\equiv4$ ו-$-4\equiv1$."),
               num(r"עבור $a=2,\ b=1,\ c=1$ מהו $f=\left(b^2-ac\right)a^{-3}$ ב-$\mathbb{Z}_5$ (בין $0$ ל-$4$)?", 3,
                   r"$b^2-ac=-1$, $a^{-3}=27\equiv2$ ולכן $f\equiv-2\equiv3$.")],
    ),
    (4, "ב"): dict(
        rubric=rub((r"$4$ אפשרויות ל-$a$ (כי $a\not\equiv0$)", 2),
                   (r"$5$ אפשרויות לכל אחד מ-$b,c$", 2),
                   (r"$|G|=100$", 1)),
        pitfalls=[r"לספור $5$ אפשרויות גם עבור $a$ ולקבל $125$.",
                  "לשכוח שאיבר ב-$G$ נקבע ביחידות על ידי שלושה פרמטרים בלבד."],
        steps=[num(r"כמה אפשרויות יש עבור $a$?", 4, r"$a\in\{1,2,3,4\}$."),
               num(r"מהו $|G|$?", 100, r"$4\cdot5\cdot5=100$.")],
    ),
    (4, "ג"): dict(
        rubric=rub((r"כתיבה $X=I+N$ עם $N^2=0$", 2),
                   (r"$X^n=I+nN$", 2),
                   (r"$o(X)=5$", 1)),
        pitfalls=[r"להסיק $o(X)=1$ כי $X$ 'כמעט' היחידה.",
                  r"לשכוח שהרכיב $n$ מחושב מודולו 5."],
        steps=[num(r"מהו הרכיב בשורה 1, עמודה 3 של $X^3$?", 3, r"$X^n=I+nN$ ולכן הרכיב הוא $n=3$."),
               num(r"מהו $o(X)$?", 5, r"$X^n=I$ אם ורק אם $n\equiv0\pmod5$.")],
    ),
    (5, "א"): dict(
        rubric=rub(("זרות המודולים וחישוב $M=120$", 2),
                   (r"$M_1,M_2,M_3=40,24,15$", 2),
                   (r"ההופכיים $x_1,x_2,x_3=1,4,7$", 3),
                   (r"הסכום והרדוקציה: $x\equiv116\pmod{120}$", 3)),
        pitfalls=[r"לשכוח לרדד את $M_i$ מודולו $m_i$ לפני חישוב ההופכי.",
                  r"לשכוח לרדד את הסכום $596$ מודולו $120$."],
        steps=[num(r"מהו $M=3\cdot5\cdot8$?", 120, r"$3\cdot5\cdot8=120$."),
               num(r"מהו $x_2$ (בין $0$ ל-$4$) המקיים $24x_2\equiv1\pmod5$?", 4, r"$24\equiv4$ ו-$4\cdot4=16\equiv1$."),
               num(r"מהו $x_3$ (בין $0$ ל-$7$) המקיים $15x_3\equiv1\pmod8$?", 7, r"$15\equiv7$ ו-$7\cdot7=49\equiv1$."),
               num(r"מהו הפתרון $x$ בין $0$ ל-$119$?", 116, r"$596=4\cdot120+116$.")],
    ),
    (5, "ב"): dict(
        rubric=rub((r"בחירת הווקטורים $\bar u_k=\frac1{\sqrt k}$ ו-$\bar v_k=\frac1{k^{3/2}}$", 5),
                   (r"חישוב $\|\bar u\|^2$, $\|\bar v\|^2$ ו-$\langle\bar u,\bar v\rangle$", 5),
                   ("הפעלת קושי-שוורץ", 3),
                   ("העלאה בריבוע של שני האגפים", 2)),
        pitfalls=[r"לבחור $\bar u_k=\bar v_k=\frac1k$, שמוביל לאי-שוויון טריוויאלי.",
                  "לשכוח שהנורמות כוללות שורש ולכן יש להעלות בריבוע."],
        steps=[ch("אילו וקטורים מפעילים בהם את קושי-שוורץ?",
                  [r"$\bar u_k=\frac1{\sqrt k},\ \bar v_k=\frac1{k^{3/2}}$", r"$\bar u_k=\frac1k,\ \bar v_k=\frac1k$",
                   r"$\bar u_k=\frac1{\sqrt k},\ \bar v_k=\frac1k$"], 0,
                  r"הבחירה $\frac1{\sqrt k},\frac1{k^{3/2}}$ נותנת $\langle\bar u,\bar v\rangle=\sum\frac1{k^2}$ ו-$\|\bar u\|^2\|\bar v\|^2=\sum\frac1k\cdot\sum\frac1{k^3}$. הבחירה $\frac1k,\frac1k$ נותנת $\sum\frac1{k^2}\le\sum\frac1{k^2}$, והבחירה $\frac1{\sqrt k},\frac1k$ נותנת מכפלה פנימית $\sum k^{-3/2}$."),
               num(r"עבור $n=2$ חשבו את $\langle\bar u,\bar v\rangle=\sum_{k=1}^2\frac1{k^2}$.", 1.25, r"$1+\frac14=1.25$."),
               num(r"עבור $n=2$ חשבו את $\left(\sum_{k=1}^2\frac1k\right)\left(\sum_{k=1}^2\frac1{k^3}\right)$.", 1.6875,
                   r"$\frac32\cdot\frac98=\frac{27}{16}=1.6875$, וזה גדול מ-$1.25^2=1.5625$.", tol=0.0001)],
    ),
}

for _q in questions:
    _e = EXTRA.pop((_q["num"], _q.get("part")))
    _q.update(_e)
    _q["rubricSource"] = "ai-draft"
    _q["stepsSource"] = "ai-draft"
    assert sum(r["points"] for r in _q["rubric"]) == _q["points"], (_q["num"], _q.get("part"))
assert not EXTRA, EXTRA

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
