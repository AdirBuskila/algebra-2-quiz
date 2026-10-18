# -*- coding: utf-8 -*-
"""Generator for tools/raw/26A-A.json -- algebra-2 (20079), semester A 2026, moed A (5.02.2026), flagship sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_26A-A.py

Source: exam 2 pp. + typed official solution 13 pp. (both read from the rendered pages). The header says
"4 of 6" but the sheet has 5 questions (25% each); all 5 are transcribed, 17 items (16 shipped + 1 held).

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
HOLD: Q4c. The official answer "a even and x even" is wrong: x is the free variable, and b = 0 is missing. The
  elements commuting with everything are exactly (a, 0) with a even (brute force + algebra in check.py).
  Official answers are never fixed, so the item is held and listed in docs/ASK_ADIR.md.
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
    r"$$\forall\begin{pmatrix}a&b\\-b&a\end{pmatrix}\in K:\qquad\begin{pmatrix}a&b\\-b&a\end{pmatrix}^{-1}=\frac1{a^2+b^2}\begin{pmatrix}a&-b\\b&a\end{pmatrix}=\begin{pmatrix}a&-b\\b&a\end{pmatrix}\pmod 7\in K$$"
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
    {"num": 4, "part": "ג", "kind": "computation", "topic": "groups", "points": 5, "contextId": "c4",
     "question": r"סעיף ג. מצאו את כל האברים $(a,b)\in\mathbb{Z}^2$ המקיימים $(a,b)\circ(x,y)=(x,y)\circ(a,b)$ לכל $(x,y)\in\mathbb{Z}^2$. (5%)",
     "hold": "official answer wrong: it says \"a even and x even\" (x is the free variable, b=0 missing); the correct set is (a,0), a even"},

    Q(5, "proof", "orthogonality", r"סעיף א.1. הוכיחו כי $\vec u,\vec v,\vec w$ הם וקטורים עצמיים של $P$. (5%)", S5A1,
      part="א", points=5, contextId="c5"),
    Q(5, "proof", "pos_def", r"סעיף א.2. הראו כי $P$ מוגדרת חיובית. (5%)", S5A2, part="ב", points=5, contextId="c5"),
    Q(5, "computation", "orthodiag", r"סעיף א.3. מצאו את כל הווקטורים $\vec x\in\mathbb{R}^3$ המקיימים $P\vec x=\vec 0$. (5%)", S5A3,
      part="ג", points=5, contextId="c5"),
    Q(5, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}2x\equiv1\pmod 3\\3x\equiv1\pmod 4\\2x\equiv3\pmod 7\end{cases}$. (10%)",
      S5B, part="ד", points=10),
]

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
