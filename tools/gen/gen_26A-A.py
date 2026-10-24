# -*- coding: utf-8 -*-
"""Generator for tools/raw/26A-A.json -- algebra-2 (20079), semester A 2026, moed A (5.02.2026), flagship sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_26A-A.py

Source: exam 2 pp. + typed official solution 13 pp. (both read from the rendered pages). The header says
"4 of 6" but the sheet has 5 questions (25% each); all 5 are transcribed, 17 items, all shipped (Q4c with a typo correction).

Part letters: the bank allows single-letter parts only, so numbered sub-parts get letters in order.
  Q2: items 1..5 -> parts a..e.   Q3: a, g.1 -> g, g.2 -> d (the printed "b" is the shared setup, a context).
  Q5: a.1, a.2, a.3, b -> parts a, b, c, d. Every question text starts with its printed label.

Typos in the official solution (checked with tools/verify/26A-A/check.py; nothing below changes an answer):
- Q1a: the three eigenvector systems are all labelled "(A-3I)v=0" but the printed matrices are A-4I, A-2I, A-I
  (labels corrected). The final decomposition prints the third row of P^T as (1/sqrt2, 0, 1); the correct
  transpose of P has third row (0, 0, 1) (corrected; the printed product is not equal to A).
- Q1b: the printed ||v|| lacks the outer square root, and the printed last inequality has Sum a_i squared <=
  Sum(a_i^2/b_i) * sqrt(Sum b_i) (should be a plain product). Written correctly.
- Q2.4: the printed (1,2) entry of the product is 2y-2x; it is 2y+2x. The system that follows is right.
- Q3a: the determinant is printed as (lambda-1)(...) = 0; the sign is (1-lambda)(...). Equation unchanged.
  The official's "positive definite" is the course's term for positive SEMIdefinite (x in [-1,1]); "strictly"
  is x in (-1,1). Kept as printed.
- Q3g.2: "lcn p perp a" -- p is a multiple of a, so it is c perp p that is meant (written so).
- Q4 statement says "for all (a,b),(x,y) in A": A is never defined, it is Z^2 (kept as printed).
Q4c (FINAL ANSWER typo): the official answer "a even and x even" is wrong: x is the free variable, and b = 0 is
  missing. The elements commuting with everything are exactly (a, 0) with a even (check.py and the solver's
  tools/verify/26A-A/solve_Q4c.py). Per the typo ruling: solutionSource "solved", official false, prefix
  "הפתרון הרשמי עם תיקון". Logged in docs/ASK_ADIR.md.
Checks: tools/verify/26A-A/check.py (sympy + brute force), all OK apart from the Q4c official-answer finding.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26A-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ------------------------------------------------------------------ contexts
CTX = {
    "c2": {"kind": "text", "title": "שאלה 2", "text": r"תהי $K=\left\{\begin{pmatrix}a&b\\-b&a\end{pmatrix}\in M_2(\mathbb{Z}_7)\ \middle|\ a^2+b^2=1\pmod 7\right\}$."},
    "c3": {"kind": "text", "title": "שאלה 3 סעיף ב",
           "text": r"יהי $V$ מרחב מכפלה פנימית ויהיו $\vec a,\vec b\in V$. נגדיר שני וקטורים חדשים: $\vec p=\dfrac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\vec a$ , $\vec c=\vec b-\vec p$."},
    "c4": {"kind": "text", "title": "שאלה 4",
           "text": r"נסתכל ב-$(\mathbb{Z}^2,\circ)$ כאשר $\mathbb{Z}^2=\{(x,y)\mid x,y\in\mathbb{Z}\}$ והפעולה $\circ$ מוגדרת באופן הבא:" "\n"
                   r"$\forall (a,b),(x,y)\in A\ ,\quad (a,b)\circ(x,y)=\left(a+x,\ b+(-1)^a y\right)$."},
    "c5": {"kind": "text", "title": "שאלה 5 סעיף א",
           "text": r"יהי $\{\vec u,\vec v,\vec w\}$ בסיס **אורתונורמלי** במרחב $\mathbb{R}^3$. נגדיר את המטריצה $P=\vec u\cdot\vec u^T+\vec v\cdot\vec v^T\in M_3(\mathbb{R})$."},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"**ערכים עצמיים של $A$:**" "\n"
    r"$$|A-\lambda I|=\begin{vmatrix}3-\lambda&1&0\\1&3-\lambda&0\\0&0&1-\lambda\end{vmatrix}=(1-\lambda)\left((3-\lambda)^2-1\right)=0$$" "\n"
    r"$$\lambda_1=1,\qquad (3-\lambda)^2-1=0\Rightarrow(3-\lambda)^2=1\Rightarrow 3-\lambda=\pm1\qquad\lambda_2=2,\ \lambda_3=4$$" "\n"
    r"**וקטור עצמי עבור $\lambda=4$:** $(A-4I)\vec v_1=\vec 0$" "\n"
    r"$$\begin{pmatrix}-1&1&0\\1&-1&0\\0&0&-3\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0\ \to\ \begin{pmatrix}-1&1&0\\0&0&0\\0&0&-3\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0$$" "\n"
    r"$$\begin{cases}-x+y=0\\-3z=0\\y=t\end{cases}\qquad\begin{cases}x=t\\y=t\\z=0\end{cases}\qquad \vec v_1=\begin{pmatrix}\frac1{\sqrt2}\\\frac1{\sqrt2}\\0\end{pmatrix}$$" "\n"
    r"**וקטור עצמי עבור $\lambda=2$:** $(A-2I)\vec v_2=\vec 0$" "\n"
    r"$$\begin{pmatrix}1&1&0\\1&1&0\\0&0&-1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0\ \to\ \begin{pmatrix}1&1&0\\0&0&0\\0&0&-1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0$$" "\n"
    r"$$\begin{cases}x+y=0\\-z=0\\y=t\end{cases}\qquad\begin{cases}x=-t\\y=t\\z=0\end{cases}\qquad \vec v_2=\begin{pmatrix}-\frac1{\sqrt2}\\\frac1{\sqrt2}\\0\end{pmatrix}$$" "\n"
    r"**וקטור עצמי עבור $\lambda=1$:** $(A-I)\vec v_3=\vec 0$" "\n"
    r"$$\begin{pmatrix}2&1&0\\1&2&0\\0&0&0\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0\ \to\ \begin{pmatrix}1&2&0\\2&1&0\\0&0&0\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0\ \to\ \begin{pmatrix}1&2&0\\0&-3&0\\0&0&0\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=0$$" "\n"
    r"$$\begin{cases}x+2y=0\\-3y=0\\z=t\end{cases}\qquad\begin{cases}x=0\\y=0\\z=1\end{cases}\qquad \vec v_3=\begin{pmatrix}0\\0\\1\end{pmatrix}$$" "\n"
    r"**הלכסון האורתוגונלי:**" "\n"
    r"$$A=\begin{pmatrix}3&1&0\\1&3&0\\0&0&1\end{pmatrix}=\begin{pmatrix}\frac1{\sqrt2}&-\frac1{\sqrt2}&0\\\frac1{\sqrt2}&\frac1{\sqrt2}&0\\0&0&1\end{pmatrix}\cdot\begin{pmatrix}4&0&0\\0&2&0\\0&0&1\end{pmatrix}\cdot\begin{pmatrix}\frac1{\sqrt2}&-\frac1{\sqrt2}&0\\\frac1{\sqrt2}&\frac1{\sqrt2}&0\\0&0&1\end{pmatrix}^T$$"
)

S1B = (
    r"נגדיר את שני הווקטורים: $\bar u=\left(\dfrac{a_1}{\sqrt{b_1}},\dfrac{a_2}{\sqrt{b_2}},\dots,\dfrac{a_n}{\sqrt{b_n}}\right)$ , $\bar v=\left(\sqrt{b_1},\sqrt{b_2},\dots,\sqrt{b_n}\right)$." "\n"
    "לפי אי-שוויון קושי-שוורץ נקבל:" "\n"
    r"$$|(\bar u,\bar v)|\le\|\bar u\|\cdot\|\bar v\|$$" "\n"
    r"$$(\bar u,\bar v)=\sum_{i=1}^n\left(\frac{a_i}{\sqrt{b_i}}\cdot\sqrt{b_i}\right)=\sum_{i=1}^n a_i$$" "\n"
    r"$$\|\bar u\|=\sqrt{\sum_{i=1}^n\left(\frac{a_i}{\sqrt{b_i}}\right)^2}=\sqrt{\sum_{i=1}^n\frac{a_i^2}{b_i}}\qquad\|\bar v\|=\sqrt{\sum_{i=1}^n\left(\sqrt{b_i}\right)^2}=\sqrt{\sum_{i=1}^n b_i}$$" "\n"
    r"$$\left|\sum_{i=1}^n a_i\right|\le\sqrt{\sum_{i=1}^n\frac{a_i^2}{b_i}}\cdot\sqrt{\sum_{i=1}^n b_i}\ ,\qquad\left(\sum_{i=1}^n a_i\right)^2\le\sum_{i=1}^n\frac{a_i^2}{b_i}\cdot\sum_{i=1}^n b_i\ \Rightarrow$$" "\n"
    r"$$\sum_{i=1}^n\frac{a_i^2}{b_i}\ge\frac{\left(\sum_{i=1}^n a_i\right)^2}{\sum_{i=1}^n b_i}$$" "\n"
    "מש\"ל"
)

S2_1 = (
    "**סגירות:**\n"
    r"$$\begin{pmatrix}a&b\\-b&a\end{pmatrix}\begin{pmatrix}c&d\\-d&c\end{pmatrix}=\begin{pmatrix}ac-bd&ad+bc\\-ad-bc&ac-bd\end{pmatrix}\in K$$" "\n"
    "**אסוציאטיביות:** נובעת מאסוציאטיביות של כפל מטריצות.\n"
    "**איבר ניטרלי:** " r"$\begin{pmatrix}1&0\\0&1\end{pmatrix}$" "\n"
    "**איבר הופכי:**\n"
    r"$$\forall\begin{pmatrix}a&b\\-b&a\end{pmatrix}\in K:\qquad\begin{pmatrix}a&b\\-b&a\end{pmatrix}^{-1}=\frac1{a^2+b^2}\begin{pmatrix}a&-b\\b&a\end{pmatrix}=\begin{pmatrix}a&-b\\b&a\end{pmatrix}\pmod 7\in K$$" "\n"
    r"**הערה:** הפתרון הרשמי קובע ש-$K$ סגורה לכפל לפי הצורה בלבד. כדי שהמכפלה אכן תהיה ב-$K$ צריך לבדוק גם ש-$p^2+q^2=1$ עבור $p=ac-bd$ ו-$q=ad+bc$: $p^2+q^2=(a^2+b^2)(c^2+d^2)=1\cdot1=1\pmod 7$."
)

S2_2 = (
    r"$$a^2+b^2\equiv1\pmod 7\ \Longleftrightarrow$$" "\n"
    r"$$\begin{cases}a^2\equiv0\pmod 7\\b^2\equiv1\pmod 7\end{cases}$$" "\n"
    "או\n"
    r"$$\begin{cases}b^2\equiv0\pmod 7\\a^2\equiv1\pmod 7\end{cases}$$" "\n"
    "או\n"
    r"$$\begin{cases}a^2\equiv4\pmod 7\\b^2\equiv4\pmod 7\end{cases}\ \Longleftrightarrow$$" "\n"
    r"$$\begin{cases}a=0\\b=1,6\end{cases}$$" "\n"
    "או\n"
    r"$$\begin{cases}b=0\\a=1,6\end{cases}$$" "\n"
    "או\n"
    r"$$\begin{cases}a=2,5\\b=2,5\end{cases}\qquad\to\ |K|=2+2+4=8$$"
)

S2_3 = (
    r"$X=\begin{pmatrix}2&2\\5&2\end{pmatrix}$ ," "\n"
    r"$2+5\equiv0\pmod 7$ , $\ 2^2+5^2=29\equiv1\pmod 7\ \to\ \begin{pmatrix}2&2\\5&2\end{pmatrix}\in K$" "\n"
    r"$$\begin{pmatrix}a&b\\-b&a\end{pmatrix}^2=\begin{pmatrix}a^2-b^2&2ab\\-2ab&a^2-b^2\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}2&2\\5&2\end{pmatrix}=\begin{pmatrix}2&2\\-2&2\end{pmatrix}=2\begin{pmatrix}1&1\\-1&1\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}2&2\\5&2\end{pmatrix}^2=4\begin{pmatrix}1&1\\-1&1\end{pmatrix}^2=4\begin{pmatrix}0&2\\-2&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\pmod 7$$" "\n"
    r"$$\begin{pmatrix}2&2\\5&2\end{pmatrix}^4=\begin{pmatrix}0&1\\-1&0\end{pmatrix}^2\pmod 7=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}2&2\\5&2\end{pmatrix}^8=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}^2\pmod 7=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I$$" "\n"
    r"$$o\left(\begin{pmatrix}2&2\\5&2\end{pmatrix}\right)=8$$"
)

S2_4 = (
    r"$$\begin{pmatrix}2&2\\5&2\end{pmatrix}\begin{pmatrix}x&y\\-y&x\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}2&2\\-2&2\end{pmatrix}\begin{pmatrix}x&y\\-y&x\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod 7$$" "\n"
    r"$$\begin{pmatrix}2x-2y&2y+2x\\-2x-2y&2x-2y\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod 7$$" "\n"
    r"$$\begin{cases}2(x-y)\equiv1\pmod 7\\2(x+y)\equiv0\pmod 7\end{cases}\quad\begin{cases}x-y\equiv4\pmod 7\\x+y\equiv0\pmod 7\end{cases}\quad\begin{cases}x\equiv2\pmod 7\\y\equiv5\pmod 7\end{cases}$$" "\n"
    r"$$\begin{pmatrix}2&2\\-2&2\end{pmatrix}^{-1}=\begin{pmatrix}2&5\\-5&2\end{pmatrix}$$"
)

S2_5 = (
    r"$$o\left(\begin{pmatrix}2&2\\5&2\end{pmatrix}\right)=8=o(K)$$" "\n"
    "לכן חבורה $K$ ציקלית."
)

S3A = (
    r"$A=\begin{pmatrix}1&x&0\\x&2&x\\0&x&1\end{pmatrix}$ , $\ |A-\lambda I|=0$" "\n"
    r"$$\begin{vmatrix}1-\lambda&x&0\\x&2-\lambda&x\\0&x&1-\lambda\end{vmatrix}=(1-\lambda)\left(\lambda^2-3\lambda-2x^2+2\right)=0$$" "\n"
    r"$$\lambda=1,\qquad\lambda=\frac{3+\sqrt{8x^2+1}}{2},\qquad\lambda=\frac{3-\sqrt{8x^2+1}}{2}$$" "\n"
    "המטריצה מוגדרת חיובית כאשר\n"
    r"$$\begin{cases}1\ge0\\\dfrac{3+\sqrt{8x^2+1}}{2}\ge0\\\dfrac{3-\sqrt{8x^2+1}}{2}\ge0\end{cases}\ \Rightarrow\ \frac{3-\sqrt{8x^2+1}}{2}\ge0\ \Rightarrow\ -1\le x\le1$$" "\n"
    "תשובה סופית:\n"
    r"מוגדרת חיובית: $-1\le x\le1$" "\n"
    r"מוגדרת חיובית לחלוטין: $-1<x<1$" "\n"
    "מוגדרת שלילית: לא קיים\n"
    "מוגדרת שלילית לחלוטין: לא קיים"
)

S3G = (
    r"$$\vec p=\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\vec a\ ,\qquad\vec c=\vec b-\vec p$$" "\n"
    r"$$\langle\vec c,\vec a\rangle=\langle\vec b-\vec p,\vec a\rangle=\left\langle\vec b-\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\vec a,\ \vec a\right\rangle=$$" "\n"
    r"$$=\langle\vec b,\vec a\rangle-\left\langle\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\vec a,\ \vec a\right\rangle=\langle\vec b,\vec a\rangle-\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\langle\vec a,\vec a\rangle=$$" "\n"
    r"$$=\langle\vec b,\vec a\rangle-\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\|\vec a\|^2=0$$"
)

S3D = (
    r"הוכחנו ש-$\vec c\perp\vec a$. אבל $\vec p=\dfrac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\vec a$ , לכן $\vec c\perp\vec p$. מתקיים" "\n"
    r"$$\|\vec b\|^2=\|\vec c+\vec p\|^2=\langle\vec c+\vec p,\vec c+\vec p\rangle=\|\vec c\|^2+2\langle\vec c,\vec p\rangle+\|\vec p\|^2=\|\vec c\|^2+\|\vec p\|^2$$"
)

S4A = (
    "**סגירות:**\n"
    r"$$\forall(a,b),(x,y)\in A\ \to\ (a,b)\circ(x,y)=\left(a+x,\ b+(-1)^a y\right)\in A$$" "\n"
    "**אסוציאטיביות:**\n"
    r"$$\forall(a,b),(x,y),(u,v)\in A\ \to\ \big((a,b)\circ(x,y)\big)\circ(u,v)=\left(a+x,\ b+(-1)^a y\right)\circ(u,v)=$$" "\n"
    r"$$=\left(a+x+u,\ b+(-1)^a y+(-1)^{a+x}v\right)$$" "\n"
    r"$$(a,b)\circ\big((x,y)\circ(u,v)\big)=(a,b)\circ\left(x+u,\ y+(-1)^x v\right)=\left(a+x+u,\ b+(-1)^a\left(y+(-1)^x v\right)\right)=$$" "\n"
    r"$$=\left(a+x+u,\ b+(-1)^a y+(-1)^{a+x}v\right)\ \to$$" "\n"
    r"$$=\big((a,b)\circ(x,y)\big)\circ(u,v)=(a,b)\circ\big((x,y)\circ(u,v)\big)$$" "\n"
    "**יחידה:**\n"
    r"$$\forall(a,b)\in A\ \to\ (a,b)\circ(x,y)=\left(a+x,\ b+(-1)^a y\right)=(a,b)\ \to\ x=0,\ y=0\qquad(0,0)$$" "\n"
    "**הופכי:**\n"
    r"$$\forall(a,b),(x,y)\in A\ \to\ (a,b)\circ(x,y)=\left(a+x,\ b+(-1)^a y\right)=(0,0)\ \to$$" "\n"
    r"$$\begin{cases}a+x=0\\b+(-1)^a y=0\end{cases}\quad\begin{cases}x=-a\\b+(-1)^a y=-(-1)^{-a}b\end{cases}\qquad y=(-1)^{1-a}b$$" "\n"
    r"$$(a,b)^{-1}=\left(-a,\ (-1)^{1-a}b\right)$$"
)

S4B = (
    "לא. נביא דוגמה נגדית:\n"
    r"$$(1,1)\circ(1,0)=\left(2,\ 1+(-1)^1\cdot0\right)=(2,1)$$" "\n"
    r"$$(1,0)\circ(1,1)=\left(2,\ 0+(-1)^1\cdot1\right)=(2,-1)$$" "\n"
    r"$$(1,1)\circ(1,0)\ne(1,0)\circ(1,1)$$"
)

S4C = (
    r"**הפתרון הרשמי עם תיקון:** בפתרון הרשמי התשובה מודפסת כ-'$a$ זוגי ו-$x$ זוגי'. אבל $(x,y)$ הוא איבר כלשהו (המשתנה החופשי), ונוסף על כך חסר התנאי $b=0$. התשובה הנכונה: $(a,0)$ עם $a$ זוגי." "\n"
    r"$$\forall(a,b),(x,y)\in A\ ,\quad(a,b)\circ(x,y)=\left(a+x,\ b+(-1)^a y\right)$$" "\n"
    r"$$(x,y)\circ(a,b)=\left(x+a,\ y+(-1)^x b\right)$$" "\n"
    r"הרכיב הראשון שווה תמיד, לכן התנאי הוא $y+(-1)^x b=b+(-1)^a y$ לכל $x,y\in\mathbb{Z}$." "\n"
    r"נציב $x=0,\ y=1$: $\ 1+b=b+(-1)^a$, כלומר $(-1)^a=1$, ולכן $a$ זוגי." "\n"
    r"כעת ($a$ זוגי) התנאי הוא $y+(-1)^x b=b+y$, כלומר $(-1)^x b=b$ לכל $x$. נציב $x=1$: $\ -b=b$, ולכן $b=0$." "\n"
    r"להפך: אם $a$ זוגי ו-$b=0$ אז $(a,0)\circ(x,y)=(a+x,\ y)=(x+a,\ y+(-1)^x\cdot0)=(x,y)\circ(a,0)$ לכל $(x,y)$." "\n"
    r"**תשובה:** $\left\{(a,0)\ \middle|\ a\in2\mathbb{Z}\right\}$, כלומר $(a,b)$ עם $a$ זוגי ו-$b=0$."
)

S5A1 = (
    r"$$P=\vec u\cdot\vec u^T+\vec v\cdot\vec v^T\in M_3(\mathbb{R})$$" "\n"
    r"$$P\cdot\vec u=\left(\vec u\cdot\vec u^T+\vec v\cdot\vec v^T\right)\cdot\vec u=\left(\vec u\cdot\vec u^T\right)\cdot\vec u+\left(\vec v\cdot\vec v^T\right)\cdot\vec u=\vec u\cdot\left(\vec u^T\cdot\vec u\right)+\vec v\cdot\left(\vec v^T\cdot\vec u\right)=\left(\vec u^T\cdot\vec u\right)\cdot\vec u=\|\vec u\|^2\cdot\vec u$$" "\n"
    r"לכן $\vec u$ וקטור עצמי של $P$." "\n"
    r"$$P\cdot\vec v=\vec u\cdot\left(\vec u^T\cdot\vec v\right)+\vec v\cdot\left(\vec v^T\cdot\vec v\right)=\left(\vec v^T\cdot\vec v\right)\cdot\vec v=\|\vec v\|^2\cdot\vec v$$" "\n"
    r"לכן $\vec v$ וקטור עצמי של $P$." "\n"
    r"$$P\cdot\vec w=\vec u\cdot\left(\vec u^T\cdot\vec w\right)+\vec v\cdot\left(\vec v^T\cdot\vec w\right)=\vec 0=0\cdot\vec w$$" "\n"
    r"לכן $\vec w$ וקטור עצמי של $P$."
)

S5A2 = (
    r"$$P^T=\left(\vec u\cdot\vec u^T+\vec v\cdot\vec v^T\right)^T=\left(\vec u\cdot\vec u^T\right)^T+\left(\vec v\cdot\vec v^T\right)^T=\left(\vec u^T\right)^T\cdot\vec u^T+\left(\vec v^T\right)^T\cdot\vec v^T=\vec u\cdot\vec u^T+\vec v\cdot\vec v^T=P$$" "\n"
    r"לכן $P$ מטריצה סימטרית. הערכים העצמיים של $P$ הם" "\n"
    r"$$\lambda_1=\vec u^T\cdot\vec u=\|\vec u\|^2>0,\qquad\lambda_2=\vec v^T\cdot\vec v=\|\vec v\|^2>0,\qquad\lambda_3=0\ge0$$" "\n"
    "כלומר המטריצה סימטרית ובעלת ערכים עצמיים אי-שליליים. לכן היא מוגדרת חיובית."
)

S5A3 = (
    r"$$P\cdot\bar x=\bar 0\ ,\qquad\bar x=a\cdot\vec u+b\cdot\vec v+c\cdot\vec w\ ,\quad a,b,c\in\mathbb{R}$$" "\n"
    r"$$P\cdot\left(a\vec u+b\vec v+c\vec w\right)=a\cdot P\vec u+b\cdot P\vec v+c\cdot P\vec w=a\cdot\|\vec u\|^2\cdot\vec u+b\cdot\|\vec v\|^2\cdot\vec v=\bar 0\ \to\ a=b=0$$" "\n"
    "**תשובה:**\n"
    r"$$\bar x=c\cdot\vec w\ ,\qquad c\in\mathbb{R}$$"
)

S5B = (
    r"$$\begin{cases}2x\equiv1\pmod 3\\3x\equiv1\pmod 4\\2x\equiv3\pmod 7\end{cases}\qquad\begin{cases}x\equiv2\pmod 3\\x\equiv3\pmod 4\\x\equiv5\pmod 7\end{cases}$$" "\n"
    r"$\gcd(3,4)=\gcd(3,7)=\gcd(4,7)=1$" "\n"
    r"$a_1=2,\ a_2=3,\ a_3=5$ ; $\ m_1=3,\ m_2=4,\ m_3=7$ ; $\ M=m_1\cdot m_2\cdot m_3=3\cdot4\cdot7=84$" "\n"
    r"$$M_1=\frac{M}{m_1}=\frac{84}{3}=28,\qquad M_2=\frac{M}{m_2}=\frac{84}{4}=21,\qquad M_3=\frac{M}{m_3}=\frac{84}{7}=12$$" "\n"
    r"$$M_1x_1\equiv1\pmod 3,\quad28x_1\equiv1\pmod 3,\quad x_1\equiv1\pmod 3$$" "\n"
    r"$$M_2x_2\equiv1\pmod 4,\quad21x_2\equiv1\pmod 4,\quad x_2\equiv1\pmod 4$$" "\n"
    r"$$M_3x_3\equiv1\pmod 7,\quad12x_3\equiv1\pmod 7,\quad5x_3\equiv1\pmod 7,\quad x_3\equiv3\pmod 7$$" "\n"
    r"$$x\equiv\left(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3\right)\pmod{84}\equiv\left(2\cdot28\cdot1+3\cdot21\cdot1+5\cdot12\cdot3\right)\pmod{84}\equiv299\pmod{84}\equiv47\pmod{84}$$"
)

questions = [
    Q(1, "computation", "orthodiag", r"(15%) בצעו לכסון אורתוגונלי למטריצה הבאה: $A=\begin{pmatrix}3&1&0\\1&3&0\\0&0&1\end{pmatrix}$.",
      S1A, part="א", points=15),
    Q(1, "proof", "cauchy_schwarz",
      r"(10%) הוכיחו כי אם $b_1,b_2,\dots,b_n$ ו-$a_1,a_2,\dots,a_n$ הם מספרים חיוביים אז $\displaystyle\sum_{i=1}^n\frac{a_i^2}{b_i}\ge\frac{\left(\sum_{i=1}^n a_i\right)^2}{\sum_{i=1}^n b_i}$.",
      S1B, part="ב", points=10),

    Q(2, "proof", "groups",
      r"סעיף 1. הוכיחו כי $K$ היא חבורה ביחס לכפל מטריצות: סגירות, אסוציאטיביות, איבר ניטרלי, איבר הופכי. (הכפל והחיבור של רכיבי המטריצות הם מודולו 7). (9%)",
      S2_1, part="א", points=9, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף 2. מהו הסדר של $K$ ? (4%)", S2_2, part="ב", points=4, contextId="c2"),
    Q(2, "computation", "groups",
      r"סעיף 3. בדקו ש-$X=\begin{pmatrix}2&2\\5&2\end{pmatrix}\in K$ ומצאו את הסדר של $X$. (4%)",
      S2_3, part="ג", points=4, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף 4. חשבו את $X^{-1}$. (4%)", S2_4, part="ד", points=4, contextId="c2"),
    Q(2, "truefalse", "groups", r"סעיף 5. האם $K$ היא חבורה ציקלית? (4%)", S2_5, part="ה", points=4, contextId="c2",
      verdict=True),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $x\in\mathbb{R}$ המטריצה $\begin{pmatrix}1&x&0\\x&2&x\\0&x&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "proof", "projection", r"סעיף ג.1. הוכיחו כי $\vec c\perp\vec a$. (5%)", S3G, part="ג", points=5, contextId="c3"),
    Q(3, "proof", "projection", r"סעיף ג.2. הוכיחו כי $\|\vec b\|^2=\|\vec c\|^2+\|\vec p\|^2$. (5%)", S3D, part="ד", points=5,
      contextId="c3"),

    Q(4, "proof", "groups", r"סעיף א. הוכיחו ש-$(\mathbb{Z}^2,\circ)$ חבורה. (15%)", S4A, part="א", points=15, contextId="c4"),
    Q(4, "truefalse", "groups", r"סעיף ב. האם $(\mathbb{Z}^2,\circ)$ היא חבורה אבלית? (5%)", S4B, part="ב", points=5,
      contextId="c4", verdict=False),
    Q(4, "computation", "groups",
      r"סעיף ג. מצאו את כל האברים $(a,b)\in\mathbb{Z}^2$ המקיימים $(a,b)\circ(x,y)=(x,y)\circ(a,b)$ לכל $(x,y)\in\mathbb{Z}^2$. (5%)",
      S4C, part="ג", points=5, contextId="c4", solutionSource="solved", official=False),

    Q(5, "proof", "orthogonality", r"סעיף א.1. הוכיחו כי $\vec u,\vec v,\vec w$ הם וקטורים עצמיים של $P$. (5%)", S5A1,
      part="א", points=5, contextId="c5"),
    Q(5, "proof", "pos_def", r"סעיף א.2. הראו כי $P$ מוגדרת חיובית. (5%)", S5A2, part="ב", points=5, contextId="c5"),
    Q(5, "computation", "orthodiag", r"סעיף א.3. מצאו את כל הווקטורים $\vec x\in\mathbb{R}^3$ המקיימים $P\vec x=\vec 0$. (5%)", S5A3,
      part="ג", points=5, contextId="c5"),
    Q(5, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}2x\equiv1\pmod 3\\3x\equiv1\pmod 4\\2x\equiv3\pmod 7\end{cases}$. (10%)",
      S5B, part="ד", points=10),
]

# ---------------------------------------------------------------------------------------------------------
# Phase 4 (step author): rubric / pitfalls / guided steps, all derived from the stored solutions above.
# Numeric values and factual claims are re-checked by tools/verify/26A-A/steps_check.py (sympy / brute force).
IDS = "abcdef"


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def ch(prompt, right, wrongs, explain, pos=0):
    vals = list(wrongs)
    vals.insert(pos, right)
    return {"type": "choice", "prompt": prompt, "options": [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)],
            "correctId": IDS[pos], "explain": explain}


def num(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def bug(prompt, lines, i, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": i, "explain": explain}


S26AA = {
    (1, "א"): dict(
        rubric=rub((r"פולינום אופייני ומציאת הערכים העצמיים $1,2,4$", 5),
                   (r"וקטור עצמי לכל ערך עצמי (פתרון $(A-\lambda I)\vec v=\vec 0$)", 6),
                   (r"נרמול הווקטורים העצמיים", 2),
                   (r"כתיבת $A=PDP^T$ עם $P$ אורתוגונלית ו-$D$ אלכסונית", 2)),
        pitfalls=[r"לשכוח לנרמל את הווקטורים העצמיים: אז $P$ אינה אורתוגונלית ו-$P^{-1}\ne P^T$.",
                  r"לסדר את העמודות של $P$ בסדר שונה מסדר הערכים העצמיים על האלכסון של $D$."],
        steps=[
            num(r"מהי מכפלת הערכים העצמיים של $A$ (כלומר $\det A$)?", 8, r"הערכים העצמיים הם $4,2,1$, ומכפלתם $8$. אפשר לבדוק: $\det A=(9-1)\cdot1=8$."),
            ch(r"מה מאפשר לקבל את $P$ אורתוגונלית ישירות מהווקטורים העצמיים (אחרי נרמול)?",
               r"$A$ סימטרית, ולכן וקטורים עצמיים של ערכים עצמיים שונים ניצבים זה לזה",
               [r"$A$ אנטי-סימטרית", r"$A$ מטריצה אלכסונית", r"ל-$A$ ערך עצמי יחיד"],
               r"המטריצה $A$ סימטרית, ולכן הווקטורים העצמיים של ערכים עצמיים שונים ($1,2,4$) ניצבים. שאר האפשרויות שגויות: $A\ne-A^T$, $A$ אינה אלכסונית ולה שלושה ערכים עצמיים שונים.", 2),
            num(r"מהו הרכיב הראשון של הווקטור העצמי המנורמל עבור $\lambda=4$ (עיגול עד $0.001$)?", 0.70711,
                r"$\vec v_1=\frac1{\sqrt2}(1,1,0)^T$, ולכן הרכיב הראשון הוא $\frac1{\sqrt2}\approx0.7071$.", 0.001),
            num(r"מהו הרכיב השלישי של הווקטור העצמי עבור $\lambda=1$?", 1, r"$\vec v_3=(0,0,1)^T$, כי $A-I$ מאפסת את הציר $z$."),
        ]),
    (1, "ב"): dict(
        rubric=rub((r"בחירת הווקטורים $\bar u=\left(\frac{a_i}{\sqrt{b_i}}\right)$ ו-$\bar v=\left(\sqrt{b_i}\right)$", 4),
                   (r"חישוב $(\bar u,\bar v)=\sum a_i$ והנורמות", 2),
                   (r"הפעלת קושי-שוורץ", 2),
                   (r"העלאה בריבוע וחלוקה ב-$\sum b_i$ לקבלת הטענה", 2)),
        pitfalls=[r"לבחור $\bar u=\left(\frac{a_i}{b_i}\right)$ ו-$\bar v=(b_i)$: אז הנורמות הן $\sum\frac{a_i^2}{b_i^2}$ ו-$\sum b_i^2$ ולא מתקבל אי-השוויון הנדרש.",
                  r"לשכוח שקושי-שוורץ נותן אי-שוויון על ריבוע הסכום רק אחרי העלאה בריבוע של שני האגפים."],
        steps=[
            ch(r"איזה זוג וקטורים בוחר הפתרון הרשמי, כך שהמכפלה הפנימית היא $\sum a_i$ והנורמות בריבוע הן $\sum\frac{a_i^2}{b_i}$ ו-$\sum b_i$?",
               r"$\bar u=\left(\frac{a_i}{\sqrt{b_i}}\right)$ , $\bar v=\left(\sqrt{b_i}\right)$",
               [r"$\bar u=\left(\frac{a_i}{b_i}\right)$ , $\bar v=(b_i)$", r"$\bar u=\left(a_i\sqrt{b_i}\right)$ , $\bar v=\left(\sqrt{b_i}\right)$", r"$\bar u=(a_i)$ , $\bar v=\left(\frac1{\sqrt{b_i}}\right)$"],
               r"רק הזוג $\left(\frac{a_i}{\sqrt{b_i}}\right),\left(\sqrt{b_i}\right)$ נותן $(\bar u,\bar v)=\sum a_i$, $\|\bar u\|^2=\sum\frac{a_i^2}{b_i}$ ו-$\|\bar v\|^2=\sum b_i$. הזוג $\left(\frac{a_i}{b_i}\right),(b_i)$ נותן נורמות $\sum\frac{a_i^2}{b_i^2}$ ו-$\sum b_i^2$, הזוג $\left(a_i\sqrt{b_i}\right),\left(\sqrt{b_i}\right)$ נותן מכפלה $\sum a_ib_i$, והזוג $(a_i),\left(\frac1{\sqrt{b_i}}\right)$ נותן מכפלה $\sum\frac{a_i}{\sqrt{b_i}}$."),
            num(r"עבור $a=(1,3)$ ו-$b=(1,1)$, מהו $\sum\frac{a_i^2}{b_i}$ ?", 10, r"$1+9=10$."),
            num(r"באותה דוגמה, מהו האגף הימני $\dfrac{\left(\sum a_i\right)^2}{\sum b_i}$ ?", 8, r"$\frac{4^2}{2}=8\le10$."),
            order("סדרו את שלבי ההוכחה.",
                  [r"נגדיר $\bar u=\left(\frac{a_i}{\sqrt{b_i}}\right)$ , $\bar v=\left(\sqrt{b_i}\right)$",
                   r"נחשב $(\bar u,\bar v)=\sum a_i$ , $\|\bar u\|=\sqrt{\sum\frac{a_i^2}{b_i}}$ , $\|\bar v\|=\sqrt{\sum b_i}$",
                   r"לפי קושי-שוורץ $|(\bar u,\bar v)|\le\|\bar u\|\cdot\|\bar v\|$",
                   r"נעלה בריבוע ונחלק ב-$\sum b_i$ ונקבל $\sum\frac{a_i^2}{b_i}\ge\frac{\left(\sum a_i\right)^2}{\sum b_i}$"],
                  "הגדרת הווקטורים, חישוב המכפלה והנורמות, קושי-שוורץ, ואז העלאה בריבוע וחלוקה."),
        ]),
    (2, "א"): dict(
        rubric=rub((r"סגירות: המכפלה היא מהצורה $\begin{pmatrix}p&q\\-q&p\end{pmatrix}$", 1),
                   (r"סגירות: $p^2+q^2=(a^2+b^2)(c^2+d^2)=1$", 2),
                   ("אסוציאטיביות מכפל מטריצות", 1),
                   (r"איבר ניטרלי $I$", 2),
                   (r"הופכי: $\frac1{a^2+b^2}\begin{pmatrix}a&-b\\b&a\end{pmatrix}=\begin{pmatrix}a&-b\\b&a\end{pmatrix}\in K$", 3)),
        pitfalls=[r"לשכוח שהחישוב הוא מודולו $7$, ושהגורם $\frac1{a^2+b^2}$ שווה $1$ בזכות התנאי $a^2+b^2=1$.",
                  r"להסתפק בסגירות, אסוציאטיביות ואיבר ניטרלי, בלי להראות שההופכי עצמו שייך ל-$K$."],
        steps=[
            num(r"עבור $\begin{pmatrix}2&2\\5&2\end{pmatrix}\in K$ (כלומר $a=b=2$), מהו האיבר הימני-העליון בהופכי $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$ (בין $0$ ל-$6$)?", 5, r"$-b=-2\equiv5\pmod7$."),
            ch(r"מדוע ההופכי $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$ שייך ל-$K$?",
               r"הוא מהצורה הנדרשת, והסכום $a^2+(-b)^2=a^2+b^2=1$",
               [r"כי כל מטריצה הפיכה ב-$M_2(\mathbb{Z}_7)$ שייכת ל-$K$", r"כי $a^2+b^2=0$", r"כי $\det=-1$"],
               r"ההופכי הוא $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$, מהצורה הנדרשת וסכום ריבועי רכיביו $1$. לא כל מטריצה הפיכה שייכת ל-$K$ (למשל $2I$ הפיכה ו-$4\ne1$)."),
            order("סדרו את שלבי מציאת ההופכי.",
                  [r"ההופכי של $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ הוא $\frac1{a^2+b^2}\begin{pmatrix}a&-b\\b&a\end{pmatrix}$",
                   r"מכיוון ש-$a^2+b^2=1$, גורם הסקלר שווה $1$",
                   r"ההופכי הוא $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$",
                   r"הוא מהצורה הנדרשת וסכום ריבועי רכיביו $a^2+(-b)^2=1$, ולכן הוא שייך ל-$K$"],
                  "נוסחת ההופכי, פישוט הסקלר לפי התנאי, ואז בדיקה שהתוצאה שייכת ל-$K$."),
            bug("באיזו שורה יש טעות?",
                [r"סגירות: המכפלה היא $\begin{pmatrix}ac-bd&ad+bc\\-ad-bc&ac-bd\end{pmatrix}$, מאותה צורה",
                 r"אסוציאטיביות נובעת מכך שכפל מטריצות הוא חילופי",
                 r"איבר ניטרלי: מטריצת היחידה",
                 r"הופכי: $\begin{pmatrix}a&-b\\b&a\end{pmatrix}\in K$"],
                1, r"אסוציאטיביות נובעת מאסוציאטיביות של כפל מטריצות. כפל מטריצות אינו חילופי."),
        ]),
    (2, "ב"): dict(
        rubric=rub((r"המקרה $a^2\equiv0$ ו-$b^2\equiv1$: שני זוגות ($a=0$ , $b=1,6$)", 1),
                   (r"המקרה $b^2\equiv0$ ו-$a^2\equiv1$: שני זוגות", 1),
                   (r"המקרה $a^2\equiv b^2\equiv4$: ארבעה זוגות", 1),
                   (r"סכום המקרים $|K|=8$", 1)),
        pitfalls=[r"לשכוח את המקרה $a^2\equiv b^2\equiv4$ (כלומר $a,b\in\{2,5\}$), שבו שני הרכיבים שונים מאפס.",
                  r"לספור רק פתרון אחד לכל משוואה $x^2\equiv1$, כאשר יש שניים: $x=1,6$."],
        steps=[
            num(r"כמה זוגות $(a,b)$ מקיימים $a=0$ ו-$b^2\equiv1\pmod7$?", 2, r"$b=1,6$."),
            num(r"כמה זוגות מקיימים $a^2\equiv4$ ו-$b^2\equiv4\pmod7$?", 4, r"$a,b\in\{2,5\}$, ולכן $2\cdot2=4$ זוגות."),
            num("מהו הסדר של $K$?", 8, r"$2+2+4=8$."),
        ]),
    (2, "ג"): dict(
        rubric=rub((r"בדיקה ש-$X\in K$", 1), (r"חישוב $X^2$", 1), (r"חישוב $X^4=-I$", 1), (r"$X^8=I$ ולכן הסדר $8$", 1)),
        pitfalls=[r"להסיק שהסדר הוא $4$ כי $X^4$ ״כמעט״ יחידה: מתקבל $X^4=-I\ne I$.",
                  r"לשכוח לעבוד מודולו $7$: $-1\equiv6$."],
        steps=[
            num(r"מהו $2^2+2^2$ מודולו $7$ (הסכום $a^2+b^2$ של $X$)?", 1, r"$8\equiv1\pmod7$, ולכן $X\in K$."),
            num(r"מהו האיבר הימני-העליון ב-$X^2$ (מודולו $7$, בין $0$ ל-$6$)?", 1, r"$X^2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$."),
            num(r"מהו האיבר השמאלי-העליון ב-$X^4$ (מודולו $7$, בין $0$ ל-$6$)?", 6, r"$X^4=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$, כלומר $-1\equiv6$."),
            num(r"מהו הסדר של $X$?", 8, r"$X^4\ne I$ ו-$X^8=I$, ולכן הסדר מחלק את $8$ ואינו מחלק את $4$: $8$."),
        ]),
    (2, "ד"): dict(
        rubric=rub((r"הצבת $X\cdot\begin{pmatrix}x&y\\-y&x\end{pmatrix}=I$", 1), (r"כפל המטריצות ומערכת מודולו $7$", 1),
                   (r"פתרון המערכת $x=2$ , $y=5$", 1), (r"כתיבת ההופכי $\begin{pmatrix}2&5\\-5&2\end{pmatrix}$", 1)),
        pitfalls=[r"לפתור את המערכת ממש (בלי מודולו): $2(x-y)=1$ אין פתרון שלם.",
                  r"לטעות בסימן ב-$2(x+y)$: האיבר הימני-העליון במכפלה הוא $2y+2x$."],
        steps=[
            num(r"מהו ההופכי של $2$ ב-$\mathbb{Z}_7$?", 4, r"$2\cdot4=8\equiv1\pmod7$."),
            num(r"מהו $x$ (בין $0$ ל-$6$)?", 2, r"$x-y\equiv4$ ו-$x+y\equiv0$ נותנים $2x\equiv4$, כלומר $x=2$."),
            num(r"מהו $y$ (בין $0$ ל-$6$)?", 5, r"$y\equiv-x\equiv5\pmod7$."),
        ]),
    (2, "ה"): dict(
        rubric=rub((r"הסדר של $X$ הוא $8$", 2), (r"$|K|=8$", 1), (r"איבר מסדר $|K|$ יוצר את החבורה, ולכן היא ציקלית", 1)),
        pitfalls=[r"להסיק ציקליות רק מכך שהחבורה מסדר $8$ (חזקת $2$): ישנן חבורות מסדר $8$ שאינן ציקליות.",
                  r"לשכוח לבדוק שהסדר של $X$ הוא בדיוק $8$ ולא מחלק שלו."],
        steps=[
            num(r"מהו הסדר של $X=\begin{pmatrix}2&2\\5&2\end{pmatrix}$ ?", 8, r"$X^4=-I$ ו-$X^8=I$, ולכן הסדר $8$."),
            ch("איזו טענה מוכיחה ש-$K$ ציקלית?",
               r"אם קיים איבר שסדרו שווה לסדר החבורה, החבורה ציקלית",
               [r"כל חבורה מסדר זוגי היא ציקלית", r"כל חבורה אבלית היא ציקלית", r"כל חבורה מסדר חזקה של $2$ היא ציקלית"],
               r"איבר מסדר $|K|=8$ יוצר את $K$. שאר הטענות שגויות: $\mathbb{Z}_2\times\mathbb{Z}_2$ היא אבלית ומסדר זוגי וחזקת $2$ אך אינה ציקלית."),
        ]),
    (3, "א"): dict(
        rubric=rub((r"פולינום אופייני $(1-\lambda)\left(\lambda^2-3\lambda-2x^2+2\right)$", 5),
                   (r"ערכים עצמיים $1$ , $\frac{3\pm\sqrt{8x^2+1}}{2}$", 4),
                   (r"תנאי חיוביות: $\frac{3-\sqrt{8x^2+1}}{2}\ge0$ ולכן $-1\le x\le1$", 4),
                   (r"חיובית לחלוטין $-1<x<1$ ואין שלילית", 2)),
        pitfalls=[r"לבלבל בין ״חיובית״ (אי-שלילית, $-1\le x\le1$) ל״חיובית לחלוטין״ ($-1<x<1$).",
                  r"לשכוח שהערך העצמי $1$ תמיד חיובי, ולכן אין ערך $x$ שבו המטריצה שלילית."],
        steps=[
            num(r"עבור $x=1$, מהו הערך העצמי הקטן ביותר?", 0, r"$\frac{3-\sqrt{9}}{2}=0$."),
            ch("עבור אילו $x$ המטריצה מוגדרת חיובית לחלוטין?", r"$-1<x<1$", [r"$-1\le x\le1$", r"$0<x<1$", r"$x>1$"],
               r"נדרש $\frac{3-\sqrt{8x^2+1}}{2}>0$, כלומר $x^2<1$. עבור $x=\pm1$ הערך העצמי הקטן הוא $0$ (רק חיובית), ועבור $|x|>1$ הוא שלילי.", 0),
            ch("האם יש $x$ שעבורו המטריצה מוגדרת שלילית?", "לא, כי הערך העצמי $1$ חיובי לכל $x$",
               [r"כן, כאשר $x>1$", r"כן, כאשר $x<-1$", r"כן, כאשר $x=0$"],
               r"הערך העצמי $1$ אינו תלוי ב-$x$, ולכן תמיד יש ערך עצמי חיובי. עבור $|x|>1$ יש ערך עצמי שלילי וגם חיובי (מטריצה לא מוגדרת)."),
        ]),
    (3, "ג"): dict(
        rubric=rub((r"הצבת $\vec c=\vec b-\vec p$ ופירוק לפי לינאריות", 2), (r"$\langle\vec p,\vec a\rangle=\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\langle\vec a,\vec a\rangle$", 2),
                   (r"$\langle\vec a,\vec a\rangle=\|\vec a\|^2$ והצמצום, ולכן $\langle\vec c,\vec a\rangle=0$", 1)),
        pitfalls=[r"לכתוב $\langle\vec a,\vec a\rangle=\|\vec a\|$ במקום $\|\vec a\|^2$.",
                  r"להניח $\vec c\perp\vec a$ בלי לחשב את המכפלה הפנימית."],
        steps=[
            num(r"עבור $\vec a=(1,1)$ ו-$\vec b=(3,1)$, מהו המקדם $\dfrac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}$ ?", 2, r"$\frac{4}{2}=2$, ולכן $\vec p=(2,2)$ ו-$\vec c=(1,-1)$."),
            num(r"באותה דוגמה, מהו $\langle\vec c,\vec a\rangle$ ?", 0, r"$1\cdot1+(-1)\cdot1=0$."),
            order("סדרו את שלבי ההוכחה.",
                  [r"$\langle\vec c,\vec a\rangle=\langle\vec b-\vec p,\vec a\rangle=\langle\vec b,\vec a\rangle-\langle\vec p,\vec a\rangle$",
                   r"$\langle\vec p,\vec a\rangle=\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\langle\vec a,\vec a\rangle$",
                   r"$\langle\vec a,\vec a\rangle=\|\vec a\|^2$, ולכן $\langle\vec p,\vec a\rangle=\langle\vec b,\vec a\rangle$",
                   r"לכן $\langle\vec c,\vec a\rangle=\langle\vec b,\vec a\rangle-\langle\vec b,\vec a\rangle=0$"],
                  "פתיחה לפי לינאריות, חישוב המכפלה של $\\vec p$, צמצום, ואז התוצאה."),
            bug("באיזו שורה יש טעות?",
                [r"$\langle\vec c,\vec a\rangle=\langle\vec b,\vec a\rangle-\langle\vec p,\vec a\rangle$",
                 r"$\langle\vec p,\vec a\rangle=\frac{\langle\vec b,\vec a\rangle}{\|\vec a\|^2}\langle\vec a,\vec a\rangle$",
                 r"$\langle\vec a,\vec a\rangle=\|\vec a\|$",
                 r"לכן $\langle\vec c,\vec a\rangle=0$"],
                2, r"$\langle\vec a,\vec a\rangle=\|\vec a\|^2$ ולא $\|\vec a\|$."),
        ]),
    (3, "ד"): dict(
        rubric=rub((r"$\vec c\perp\vec p$ כי $\vec p$ כפולה של $\vec a$ ו-$\vec c\perp\vec a$", 2), (r"$\vec b=\vec c+\vec p$ ופתיחת $\|\vec c+\vec p\|^2$", 2), (r"האיבר המעורב מתאפס", 1)),
        pitfalls=[r"לפתוח $\|\vec c+\vec p\|^2=\|\vec c\|^2+\|\vec p\|^2$ בלי לנמק מדוע האיבר המעורב מתאפס.",
                  r"לשכוח את הגורם $2$ באיבר המעורב $2\langle\vec c,\vec p\rangle$."],
        steps=[
            ch(r"מדוע $\vec c\perp\vec p$ ?", r"$\vec p$ כפולה סקלרית של $\vec a$ ו-$\vec c\perp\vec a$",
               [r"כי $\vec p=\vec b$", r"כי $\|\vec p\|=\|\vec c\|$", r"כי $\vec p=\vec 0$"],
               r"$\vec p=t\vec a$ ולכן $\langle\vec c,\vec p\rangle=t\langle\vec c,\vec a\rangle=0$. בדוגמה $\vec a=(1,1),\vec b=(3,1)$: $\vec p=(2,2)\ne\vec b$, $\|\vec p\|=\sqrt8\ne\sqrt2=\|\vec c\|$ ו-$\vec p\ne\vec 0$."),
            num(r"עבור $\vec a=(1,1)$ ו-$\vec b=(3,1)$, מהו $\|\vec p\|^2$ ?", 8, r"$\vec p=(2,2)$, ולכן $4+4=8$ (ו-$\|\vec c\|^2=2$, $\|\vec b\|^2=10$)."),
            order("סדרו את שלבי ההוכחה.",
                  [r"$\vec b=\vec c+\vec p$ ולכן $\|\vec b\|^2=\langle\vec c+\vec p,\vec c+\vec p\rangle$",
                   r"$=\|\vec c\|^2+2\langle\vec c,\vec p\rangle+\|\vec p\|^2$",
                   r"$\langle\vec c,\vec p\rangle=0$ כי $\vec c\perp\vec p$",
                   r"לכן $\|\vec b\|^2=\|\vec c\|^2+\|\vec p\|^2$"],
                  "הצבה, פתיחה, אפס האיבר המעורב, ותוצאה."),
            bug("באיזו שורה יש טעות?",
                [r"$\vec b=\vec c+\vec p$ ולכן $\|\vec b\|^2=\langle\vec c+\vec p,\vec c+\vec p\rangle$",
                 r"$=\|\vec c\|^2+2\langle\vec c,\vec p\rangle+\|\vec p\|^2$",
                 r"מכיוון ש-$\vec c\perp\vec p$ מתקיים $\langle\vec c,\vec p\rangle=\|\vec c\|\cdot\|\vec p\|$",
                 r"לכן $\|\vec b\|^2=\|\vec c\|^2+\|\vec p\|^2$"],
                2, r"אם $\vec c\perp\vec p$ אז $\langle\vec c,\vec p\rangle=0$."),
        ]),
    (4, "א"): dict(
        rubric=rub(("סגירות", 3), ("אסוציאטיביות: חישוב שני האגפים והשוואתם", 5), (r"יחידה $(0,0)$", 3), (r"הופכי $(-a,(-1)^{1-a}b)$", 4)),
        pitfalls=[r"לשכוח את החזקה $(-1)^a$ בחישוב האסוציאטיביות: $(-1)^a(-1)^x=(-1)^{a+x}$.",
                  r"לבדוק רק יחידה מצד אחד ולא לבדוק שההופכי הוא גם הופכי מימין ומשמאל."],
        steps=[
            num(r"מהו הרכיב השני של $(1,2)\circ(3,4)$ ?", -2, r"$2+(-1)^1\cdot4=-2$ (והרכיב הראשון $4$)."),
            num(r"מהו הרכיב השני של ההופכי של $(1,3)$, לפי הנוסחה $(-a,(-1)^{1-a}b)$ ?", 3,
                r"$(-1)^{0}\cdot3=3$. בדיקה: $(1,3)\circ(-1,3)=(0,3-3)=(0,0)$."),
            num(r"מהו הרכיב השני של ההופכי של $(2,5)$ ?", -5, r"$(-1)^{-1}\cdot5=-5$. בדיקה: $(2,5)\circ(-2,-5)=(0,5-5)=(0,0)$."),
            bug("באיזו שורה בהוכחת האסוציאטיביות יש טעות?",
                [r"$\big((a,b)\circ(x,y)\big)\circ(u,v)=\left(a+x+u,\ b+(-1)^a y+(-1)^{a+x}v\right)$",
                 r"$(a,b)\circ\big((x,y)\circ(u,v)\big)=(a,b)\circ\left(x+u,\ y+(-1)^x v\right)=\left(a+x+u,\ b+(-1)^a y+(-1)^x v\right)$",
                 r"הרכיבים השניים שווים, ולכן הפעולה אסוציאטיבית"],
                1, r"הרכיב השני הוא $b+(-1)^a\left(y+(-1)^x v\right)=b+(-1)^a y+(-1)^{a+x}v$ ולא $(-1)^x v$."),
        ]),
    (4, "ב"): dict(
        rubric=rub(("תשובה: לא אבלית", 1), (r"חישוב $(1,1)\circ(1,0)=(2,1)$", 2), (r"חישוב $(1,0)\circ(1,1)=(2,-1)$ והשוואה", 2)),
        pitfalls=[r"לבדוק זוג שבו $a$ זוגי: אז $(-1)^a=1$ והאברים מתחלפים (למשל $(2,1)\circ(2,3)$).",
                  r"להסיק אבליות מכך שהרכיב הראשון קומוטטיבי."],
        steps=[
            num(r"מהו הרכיב השני של $(1,1)\circ(1,0)$ ?", 1, r"$1+(-1)^1\cdot0=1$."),
            num(r"מהו הרכיב השני של $(1,0)\circ(1,1)$ ?", -1, r"$0+(-1)^1\cdot1=-1\ne1$."),
            ch("מה מספיק כדי להוכיח שהחבורה אינה אבלית?", "זוג איברים אחד שאינם מתחלפים",
               [r"שהאיבר הניטרלי מתחלף עם כל איבר", r"שהחבורה אינסופית", r"שהאסוציאטיביות לא מתקיימת"],
               r"אי-אבליות פירושה קיום זוג שאינו מתחלף. האיבר הניטרלי תמיד מתחלף, אינסופיות אינה קשורה, והאסוציאטיביות כן מתקיימת."),
        ]),
    (4, "ג"): dict(
        rubric=rub((r"התנאי $y+(-1)^xb=b+(-1)^ay$ לכל $x,y$", 1), (r"הצבת $x=0,y=1$ ו-$a$ זוגי", 2), (r"הצבת $x=1$ ו-$b=0$", 1), (r"אימות והתשובה $\{(a,0):a\in2\mathbb{Z}\}$", 1)),
        pitfalls=[r"לכתוב את התשובה כ-״$a$ זוגי ו-$x$ זוגי״: $x$ הוא המשתנה החופשי, והתנאי החסר הוא $b=0$.",
                  r"לשכוח את התנאי $b=0$: האיבר $(2,1)$ אינו מתחלף עם $(1,1)$."],
        steps=[
            num(r"מהו $(-1)^a$ המתקבל מהצבת $x=0,y=1$ במשוואה $1+b=b+(-1)^a$ ?", 1, r"$(-1)^a=1$, ולכן $a$ זוגי."),
            num(r"כאשר $a$ זוגי והצבת $x=1$ נותנת $-b=b$, מהו $b$ ?", 0, r"$2b=0$ ולכן $b=0$."),
            ch("איזו קבוצה היא קבוצת כל האיברים המתחלפים עם כל איבר?", r"$\{(a,0)\mid a\in2\mathbb{Z}\}$",
               [r"$\{(a,b)\mid a\in2\mathbb{Z}\}$", r"$\{(a,0)\mid a\in\mathbb{Z}\}$", r"$\{(0,0)\}$"],
               r"למשל $(2,1)\circ(1,1)=(3,2)$ אך $(1,1)\circ(2,1)=(3,0)$, ו-$(1,0)\circ(0,1)=(1,-1)$ אך $(0,1)\circ(1,0)=(1,1)$. האיבר $(2,0)$ מתחלף עם כולם, ולכן הקבוצה אינה רק $\{(0,0)\}$."),
        ]),
    (5, "א"): dict(
        rubric=rub((r"חישוב $P\vec u=\|\vec u\|^2\vec u$", 2), (r"חישוב $P\vec v=\|\vec v\|^2\vec v$", 1), (r"חישוב $P\vec w=\vec 0=0\cdot\vec w$", 1), ("מסקנה: שלושתם וקטורים עצמיים", 1)),
        pitfalls=[r"לשכוח שהווקטור האפס אינו וקטור עצמי, אבל $\vec w\ne\vec 0$ ו-$P\vec w=0\cdot\vec w$ תקין.",
                  r"לא להשתמש באורתוגונליות: $\vec v^T\vec u=0$ היא שמאפסת את האיבר השני."],
        steps=[
            ch("אילו תכונות של הבסיס האורתונורמלי משתמשים בהן?",
               r"$\vec u^T\vec u=\vec v^T\vec v=1$ וכל מכפלה פנימית בין שני וקטורים שונים היא $0$",
               [r"$\vec u^T\vec u=0$", r"$\vec u^T\vec v=1$", r"$\vec w=\vec u+\vec v$"],
               r"בבסיס אורתונורמלי הנורמות $1$ והווקטורים השונים ניצבים. $\vec w$ בלתי תלוי ב-$\vec u,\vec v$, ולכן אינו סכומם."),
            num(r"מהו הערך העצמי של $P$ עבור $\vec w$ ?", 0, r"$P\vec w=\vec u(\vec u^T\vec w)+\vec v(\vec v^T\vec w)=\vec 0$."),
            num(r"מהו הערך העצמי של $P$ עבור $\vec u$ (כאשר $\|\vec u\|=1$) ?", 1, r"$P\vec u=\vec u(\vec u^T\vec u)+\vec v(\vec v^T\vec u)=\vec u$."),
            bug("באיזו שורה יש טעות?",
                [r"$P\vec u=\vec u\left(\vec u^T\vec u\right)+\vec v\left(\vec v^T\vec u\right)$",
                 r"$\vec u^T\vec u=1$ ו-$\vec v^T\vec u=1$, ולכן $P\vec u=\vec u+\vec v$",
                 r"לכן $\vec u$ הוא וקטור עצמי של $P$"],
                1, r"$\vec v^T\vec u=0$ בבסיס אורתונורמלי, ולכן $P\vec u=\vec u$."),
        ]),
    (5, "ב"): dict(
        rubric=rub((r"$P^T=P$ (סימטריה)", 2), (r"ערכים עצמיים $\|\vec u\|^2,\|\vec v\|^2,0$", 2), ("מסקנה: סימטרית עם ערכים עצמיים אי-שליליים, ולכן מוגדרת חיובית", 1)),
        pitfalls=[r"לדרוש ערכים עצמיים חיוביים ממש: ל-$P$ ערך עצמי $0$, והיא מוגדרת חיובית (אי-שלילית) בלבד.",
                  r"לשכוח לבדוק סימטריה, שהיא חלק מההגדרה."],
        steps=[
            ch("מה מראים כדי להוכיח ש-$P$ מוגדרת חיובית?", "ש-$P$ סימטרית וכל ערכיה העצמיים אי-שליליים",
               [r"ש-$P$ הפיכה", r"ש-$P$ אנטי-סימטרית", r"שכל ערכיה העצמיים שווים"],
               r"$P$ אינה הפיכה (הערך העצמי $0$), והיא סימטרית ולא אנטי-סימטרית, ויש לה ערכים עצמיים $\|\vec u\|^2,\|\vec v\|^2,0$ שאינם שווים."),
            num(r"מהי העקבה (trace) של $P$ כאשר $\|\vec u\|=\|\vec v\|=1$ ?", 2, r"סכום הערכים העצמיים $1+1+0=2$."),
            order("סדרו את שלבי ההוכחה.",
                  [r"$P^T=\left(\vec u\vec u^T\right)^T+\left(\vec v\vec v^T\right)^T$",
                   r"$\left(\vec u\vec u^T\right)^T=\vec u\vec u^T$ ובאופן דומה עבור $\vec v$, ולכן $P^T=P$",
                   r"הערכים העצמיים הם $\|\vec u\|^2>0$ , $\|\vec v\|^2>0$ , $0$",
                   r"$P$ סימטרית עם ערכים עצמיים אי-שליליים, לכן מוגדרת חיובית"],
                  "סימטריה, ערכים עצמיים, ואז מסקנה."),
        ]),
    (5, "ג"): dict(
        rubric=rub((r"כתיבת $\vec x=a\vec u+b\vec v+c\vec w$", 1), (r"הפעלת $P$ וקבלת $a\|\vec u\|^2\vec u+b\|\vec v\|^2\vec v$", 2), (r"אי-תלות לינארית נותנת $a=b=0$", 1), (r"התשובה $\vec x=c\vec w$", 1)),
        pitfalls=[r"לכלול את $\vec u$ או $\vec v$ בפתרון: $P\vec u=\|\vec u\|^2\vec u\ne\vec 0$.",
                  r"לשכוח שהפתרון הוא כל הכפולות של $\vec w$ ולא רק $\vec w$."],
        steps=[
            num(r"מהו המימד של קבוצת הפתרונות של $P\vec x=\vec 0$ ?", 1, r"הפתרונות הם $c\vec w$, כלומר ישר אחד."),
            ch(r"מהי קבוצת כל $\vec x$ המקיימים $P\vec x=\vec 0$ ?", r"כל הכפולות של $\vec w$", [r"$\mathrm{Sp}\{\vec u,\vec v\}$", r"$\{\vec 0\}$ בלבד", r"$\mathrm{Sp}\{\vec u,\vec w\}$"],
               r"$P\vec u=\|\vec u\|^2\vec u\ne\vec 0$ ו-$P\vec v\ne\vec 0$, ולכן אי אפשר לכלול אותם. $\vec w$ נמצא בגרעין."),
            order("סדרו את שלבי הפתרון.",
                  [r"נכתוב $\vec x=a\vec u+b\vec v+c\vec w$ (בסיס של $\mathbb{R}^3$)",
                   r"$P\vec x=aP\vec u+bP\vec v+cP\vec w=a\|\vec u\|^2\vec u+b\|\vec v\|^2\vec v$",
                   r"הווקטורים בלתי תלויים ולכן $a=b=0$",
                   r"לכן $\vec x=c\vec w$ , $c\in\mathbb{R}$"],
                  "הצגה בבסיס, הפעלת $P$, אי-תלות, ואז התשובה."),
        ]),
    (5, "ד"): dict(
        rubric=rub((r"צמצום המשוואות: $x\equiv2\pmod3$ , $x\equiv3\pmod4$ , $x\equiv5\pmod7$", 3), (r"$M=84$ ו-$M_1,M_2,M_3$", 2), (r"הפתרונות $x_1,x_2,x_3$ של $M_ix_i\equiv1$", 3), (r"הרכבה ל-$x\equiv47\pmod{84}$", 2)),
        pitfalls=[r"להציב את השאריות בלי לצמצם קודם: המשוואות הן $2x\equiv1$ ו-$3x\equiv1$ ולא $x\equiv1$.",
                  r"לשכוח את הצמצום מודולו $84$ בסוף: $299\equiv47$."],
        steps=[
            num(r"מהי השארית $a_1$ במערכת המצומצמת ($2x\equiv1\pmod3$) ?", 2, r"$2^{-1}\equiv2\pmod3$, ולכן $x\equiv2$."),
            num(r"מהי השארית $a_3$ במערכת המצומצמת ($2x\equiv3\pmod7$) ?", 5, r"$2^{-1}\equiv4\pmod7$, ולכן $x\equiv12\equiv5$."),
            num(r"מהו $x_3$ , הפתרון של $12x_3\equiv1\pmod7$ ?", 3, r"$12\equiv5$ ו-$5\cdot3=15\equiv1\pmod7$."),
            num(r"מהו הפתרון $x$ בין $0$ ל-$83$ ?", 47, r"$2\cdot28\cdot1+3\cdot21\cdot1+5\cdot12\cdot3=299\equiv47\pmod{84}$."),
        ]),
}
for _q in questions:
    _s = S26AA.get((_q["num"], _q.get("part")))
    assert _s is not None, ("no steps for", _q["num"], _q.get("part"))
    assert sum(r["points"] for r in _s["rubric"]) == _q["points"], ("rubric sum", _q["num"], _q.get("part"))
    _q["rubric"], _q["rubricSource"] = _s["rubric"], "ai-verified"
    _q["pitfalls"] = _s["pitfalls"]
    _q["steps"], _q["stepsSource"] = _s["steps"], "ai-verified"

exam = {
    "examCode": "26A-A",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ו מועד א'",
    "year": 2026,
    "examDate": "5.2.2026",
    "sourceFile": "algebra-2-26A-A-exam",
    "solutionFile": "algebra-2-26A-A-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
