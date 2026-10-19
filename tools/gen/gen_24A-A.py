# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-A.json -- algebra-2 (20079), semester A 2024, moed A (28.03.2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-A.py

Source: exam 2 pp. + typed official solution 8 pp. (both read from the rendered pages). Five questions, 25% each
("4 of 5"); all 5 are transcribed, 15 items, none held.

Part letters (single letters only): Q2: items 1..4 -> a..d, printed "b" -> e.  Q4: items 1..3 -> a..c, printed "b" -> d.
Every question text starts with its printed label.

Sitting code: header says semester A 2024, moed A, date 28.03.24 -> 24A-A (no header typo here; the cs24 copy has
no .pdf extension).

Typos / slips in the official solution (all checked with tools/verify/24A-A/check.py; no final answer is wrong):
- Q4a.1: the official line says "a=1,2,3,4,5,6 (mod 3)"; the modulus is 7 (written as mod 7).
- Q4a.2: the official line ends "o(H)=6"; it is the order of the element diag(4,3) that is 6 (written so).
- Q4a: the exam prints H with entries [[a,c],[0,b]], the solution writes [[a,b],[0,c]]; the inverse in 4a.3 is
  stated as a matrix to avoid the naming clash.
- Q2b: the last official line says "I+A^2" where cI+A+A^2 is meant (written correctly).
- Q3a: the official solution says b=0 is forced by symmetry; it calls positive SEMI-definiteness "positive
  definite" (the course's term). Kept as printed. Q2a.4 is stated for a in N and n in N; the official takes n=a.
Checks: tools/verify/24A-A/check.py (sympy + brute force), all OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ------------------------------------------------------------------ contexts
CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"נסמן $\mathbb{R}^*=\{x\in\mathbb{R}:x>0\}$. לכל $a,b\in\mathbb{R}^*$ נגדיר את הפעולה הבאה: $a\odot b=\dfrac{ab}{a+b}$."},
    "c4": {"kind": "text", "title": "שאלה 4 סעיף א",
           "text": r"נתבונן בחבורה $G=\left\{A\in M_2(\mathbb{Z}_7)\ \middle|\ \det(A)\ne0\right\}$ ביחס לכפל מטריצות (חבורת המטריצות ההפיכות מסדר 2x2 עם הרכיבים מ-$\mathbb{Z}_7$)." "\n"
                   r"תהי $H=\left\{\begin{pmatrix}a&c\\0&b\end{pmatrix}\in M_2(\mathbb{Z}_7)\ \middle|\ a\cdot b\ne0\right\}$ תת-חבורה של $G$."},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"**(⇒)** נתון $\vec v=t\vec u$ עם $t>0$. אז" "\n"
    r"$$\|\vec u+\vec v\|=\|\vec u+t\vec u\|=\|(1+t)\vec u\|\overset{t>0}{=}(1+t)\|\vec u\|$$" "\n"
    "מצד שני:\n"
    r"$$\|\vec u\|+\|\vec v\|=\|\vec u\|+\|t\vec u\|=\|\vec u\|+|t|\cdot\|\vec u\|\overset{t>0}{=}(1+t)\cdot\|\vec u\|$$" "\n"
    r"**(⇐)** נתון $\|\vec u+\vec v\|=\|\vec u\|+\|\vec v\|$, כלומר $\|\vec u+\vec v\|^2=\left(\|\vec u\|+\|\vec v\|\right)^2$." "\n"
    r"$$\|\vec u+\vec v\|^2=\langle\vec u+\vec v,\vec u+\vec v\rangle=\|\vec u\|^2+2\langle\vec u,\vec v\rangle+\|\vec v\|^2$$" "\n"
    r"$$\left(\|\vec u\|+\|\vec v\|\right)^2=\|\vec u\|^2+2\|\vec u\|\cdot\|\vec v\|+\|\vec v\|^2$$" "\n"
    r"$$\Rightarrow\ \langle\vec u,\vec v\rangle=\|\vec u\|\cdot\|\vec v\|\ \Rightarrow\ \frac{\langle\vec u,\vec v\rangle}{\|\vec u\|\cdot\|\vec v\|}=\cos\alpha=1$$" "\n"
    "מכאן נובע שהוקטורים מקבילים ויוצרים זווית 0 ביניהם. מסקנה: $t>0$, $\\vec v=t\\vec u$."
)

S1B = (
    r"קודם כל נמצא בסיס אורתונורמלי עבור $W=\mathrm{Sp}\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\0&1\end{pmatrix}\right\}$ בעזרת תהליך גרם-שמידט:" "\n"
    r"$$\vec u_1=\begin{pmatrix}1&0\\0&1\end{pmatrix}$$" "\n"
    r"$$\vec u_2=\vec v_2-\frac{\langle\vec v_2,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1=\begin{pmatrix}0&1\\0&1\end{pmatrix}-\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}=\begin{pmatrix}-\frac12&1\\0&\frac12\end{pmatrix}\ \xrightarrow{\ \cdot2\ }\ \begin{pmatrix}-1&2\\0&1\end{pmatrix}$$" "\n"
    r"המערכת $\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}-1&2\\0&1\end{pmatrix}\right\}$ אורתוגונלית. ננרמל ונקבל את המערכת האורתונורמלית" "\n"
    r"$$\left\{\frac1{\sqrt2}\begin{pmatrix}1&0\\0&1\end{pmatrix},\ \frac1{\sqrt6}\begin{pmatrix}-1&2\\0&1\end{pmatrix}\right\}$$" "\n"
    r"כעת ניתן לחשב את ההיטל של $\vec v=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ על $W$:" "\n"
    r"$$\mathbf{proj}_W(\vec v)=\left\langle\vec v,\frac1{\sqrt2}\begin{pmatrix}1&0\\0&1\end{pmatrix}\right\rangle\frac1{\sqrt2}\begin{pmatrix}1&0\\0&1\end{pmatrix}+\left\langle\vec v,\frac1{\sqrt6}\begin{pmatrix}-1&2\\0&1\end{pmatrix}\right\rangle\frac1{\sqrt6}\begin{pmatrix}-1&2\\0&1\end{pmatrix}$$" "\n"
    r"$$=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}+\frac16\begin{pmatrix}-1&2\\0&1\end{pmatrix}=\begin{pmatrix}\frac13&\frac13\\0&\frac23\end{pmatrix}$$"
)

S2A = (
    r"נוכיח כי $(a\odot b)\odot c=a\odot(b\odot c)$." "\n"
    r"$$(a\odot b)\odot c=\frac{ab}{a+b}\odot c=\frac{\frac{ab}{a+b}\cdot c}{\frac{ab}{a+b}+c}=\frac{abc}{ab+ac+bc}$$" "\n"
    r"$$a\odot(b\odot c)=a\odot\frac{bc}{b+c}=\frac{a\cdot\frac{bc}{b+c}}{a+\frac{bc}{b+c}}=\frac{abc}{ab+ac+bc}$$" "\n"
    "הוכחנו כי הפעולה אסוציאטיבית."
)

S2B = (
    r"**סגירות:** עבור $a,b\in\mathbb{R}^*$ מתקיים $a+b,\ ab>0$ ולכן $a\odot b=\dfrac{ab}{a+b}\in\mathbb{R}^*$." "\n"
    "**אסוציאטיביות:** הוכחה בסעיף 1.\n"
    r"**קיום איבר ניטרלי:** נחפש אם קיים $e\in\mathbb{R}^*$ כך ש-$a\odot e=a$ וגם $e\odot a=a$. נקבל:" "\n"
    r"$$a\odot e=\frac{ae}{a+e}=a\ \Rightarrow\ ae=a(a+e)\ \Rightarrow\ a^2=0$$" "\n"
    "לא קיים איבר ניטרלי.\n"
    r"**מסקנה:** המבנה $(\mathbb{R}^*,\odot)$ אינו חבורה, קל וחומר שאינו חבורה אבלית."
)

S2C = (
    r"$$x\odot x=\frac{x^2}{2x}\overset{x\ne0}{=}\frac x2=x$$" "\n"
    r"למשוואה אין פתרון עבור $x\ne0$. **מסקנה:** לא קיים $x$ כזה."
)

S2D = (
    "נשים לב לחוקיות תחת הפעולה הנ\"ל:\n"
    r"$$x^1=x=\frac x1,\quad x^2=x\odot x=\frac x2,\quad x^3=x^2\odot x=\frac x2\odot x=\frac x3,\quad\dots,\quad x^n=\frac xn$$" "\n"
    r"לכן לכל $a=n\in\mathbb{N}$ מתקיים $n^n=\dfrac nn=1$. **מסקנה:** הטענה נכונה."
)

S2E = (
    r"יהי $\vec0\ne\vec v\in\mathbb{R}^n$ כאשר $n$ הוא סדר המטריצה $A$. מתקיים $\left(cI+A+A^2\right)^T=cI+A+A^2$. בנוסף:" "\n"
    r"$$\left\langle\left(cI+A+A^2\right)\vec v,\vec v\right\rangle=\vec v^T\left(cI+A+A^2\right)\vec v=c\vec v^T\vec v+\vec v^TA\vec v+\vec v^TA^TA\vec v=c\|\vec v\|^2+\langle A\vec v,\vec v\rangle+c\|A\vec v\|^2$$" "\n"
    r"נתון כי $A$ מוגדרת חיובית, לכן $\langle A\vec v,\vec v\rangle\ge0$. בנוסף $c>0$ ו-$\vec v\ne\vec0$, לכן $c\|\vec v\|^2>0$. ברור ש-$c\|A\vec v\|^2\ge0$." "\n"
    r"מכאן נובע כי $c\|\vec v\|^2+\langle A\vec v,\vec v\rangle+c\|A\vec v\|^2>0$, כלומר $cI+A+A^2$ מוגדרת חיובית לחלוטין."
)

S3A = (
    r"על מנת שהמטריצה תהיה סימטרית חייב להתקיים $b=0$. נחשב את הערכים העצמיים של המטריצה:" "\n"
    r"$$\begin{vmatrix}1-\lambda&0&a^2\\0&3a-1-\lambda&0\\a^2&0&1-\lambda\end{vmatrix}=(3a-1-\lambda)\begin{vmatrix}1-\lambda&a^2\\a^2&1-\lambda\end{vmatrix}=(3a-1-\lambda)\left(\lambda^2-2\lambda+1-a^4\right)$$" "\n"
    r"לכן הערכים העצמיים הם $\lambda=3a-1$, $\lambda=a^2+1$, $\lambda=1-a^2$. המטריצה **מוגדרת חיובית** כאשר" "\n"
    r"$$\begin{cases}3a-1\ge0\\1+a^2\ge0\\1-a^2\ge0\end{cases}\Rightarrow\begin{cases}a\ge\frac13\\-1\le a\le1\end{cases}\Rightarrow\ \frac13\le a\le1$$" "\n"
    r"המטריצה **מוגדרת חיובית לחלוטין** כאשר $\dfrac13<a<1$." "\n"
    r"המטריצה **מוגדרת שלילית** כאשר $3a-1\le0,\ 1+a^2\le0,\ 1-a^2\le0$, כלומר $a\in\emptyset$. אין ערכי $a$ עבור המטריצה מוגדרת שלילית, בפרט שלילית לחלוטין." "\n"
    "**סיכום:**\n"
    r"- המטריצה מוגדרת חיובית כאשר $b=0$ ו-$\dfrac13\le a\le1$." "\n"
    r"- המטריצה מוגדרת חיובית לחלוטין כאשר $b=0$ ו-$\dfrac13<a<1$." "\n"
    "- בשאר המקרים המטריצה אינה מוגדרת."
)

S3B = (
    r"$y=mx+n$" "\n"
    r"$$\begin{cases}m+n=3\\3m+n=5\\-2m+n=5\\2m+n=2\end{cases}\Rightarrow\begin{pmatrix}1&1\\3&1\\-2&1\\2&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}3\\5\\5\\2\end{pmatrix}$$" "\n"
    r"$$A^TA\begin{pmatrix}m\\n\end{pmatrix}=A^T\vec b\ \Rightarrow\ \begin{pmatrix}18&4\\4&4\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}12\\15\end{pmatrix}\ \Rightarrow\ m=-\frac3{14},\ n=\frac{111}{28}$$" "\n"
    r"$$y=-\frac3{14}x+\frac{111}{28}$$"
)

S4A = (
    r"**1.** התנאי $a\cdot c\ne0\pmod7$ מתקיים אם ורק אם $a\ne0\pmod7\ \wedge\ c\ne0\pmod7$. לכן $\begin{pmatrix}a&b\\0&c\end{pmatrix}\in H$ כאשר $a=1,\dots,6\pmod7$ (6 אפשרויות), $c=1,\dots,6\pmod7$ (6 אפשרויות), ו-$b\in\mathbb{Z}_7$ (7 אפשרויות). לפי עקרון הכפל: $|H|=6\cdot6\cdot7=252$."
)

S4B = (
    r"מתקיימים $3^6\equiv1\pmod7$ ו-$4^3\equiv1\pmod7$. לכן סדר האיבר $\begin{pmatrix}4&0\\0&3\end{pmatrix}$ הוא 6."
)

S4C = (
    r"נסמן $\begin{pmatrix}1&2\\0&3\end{pmatrix}^{-1}=\begin{pmatrix}a&b\\0&c\end{pmatrix}$. מתקיים $\begin{pmatrix}1&2\\0&3\end{pmatrix}\cdot\begin{pmatrix}a&b\\0&c\end{pmatrix}=\begin{pmatrix}a&b+2c\\0&3c\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$. מכאן:" "\n"
    r"$$\begin{cases}a\equiv1\pmod7\\b+2c\equiv0\pmod7\\3c\equiv1\pmod7\end{cases}\Rightarrow\begin{cases}a\equiv1\pmod7\\b+2c\equiv0\pmod7\\c\equiv5\pmod7\end{cases}\Rightarrow\begin{cases}a\equiv1\pmod7\\b\equiv4\pmod7\\c\equiv5\pmod7\end{cases}$$" "\n"
    r"$$\begin{pmatrix}1&2\\0&3\end{pmatrix}^{-1}=\begin{pmatrix}1&4\\0&5\end{pmatrix}$$"
)

S4D = (
    r"עלינו להוכיח כי לכל $x\in\mathbb{R}$: $\dfrac{(x+k)^2}{x^2+1}\le k^2+1$, או $(x+k)^2\le(k^2+1)(x^2+1)$ לכל $x\in\mathbb{R}$." "\n"
    r"נגדיר 2 וקטורים ב-$\mathbb{R}^2$: $\vec u=\begin{pmatrix}x\\1\end{pmatrix}$, $\vec v=\begin{pmatrix}1\\k\end{pmatrix}$. לפי אי-שוויון קושי-שוורץ:" "\n"
    r"$$\left|\left\langle\begin{pmatrix}x\\1\end{pmatrix},\begin{pmatrix}1\\k\end{pmatrix}\right\rangle\right|\le\left\|\begin{pmatrix}x\\1\end{pmatrix}\right\|\cdot\left\|\begin{pmatrix}1\\k\end{pmatrix}\right\|$$" "\n"
    r"כלומר $|x+k|\le\sqrt{x^2+1}\cdot\sqrt{1+k^2}$. נעלה בריבוע את שני האגפים ונקבל $(x+k)^2\le(k^2+1)(x^2+1)$."
)

S5A = (
    r"$$\begin{pmatrix}2&0\\0&2\\1&\sqrt3\end{pmatrix}=\begin{pmatrix}\frac{\sqrt2}4&-\frac{\sqrt3}2&-\frac{\sqrt2}4\\\frac{\sqrt6}4&\frac12&-\frac{\sqrt6}4\\\frac{\sqrt2}2&0&\frac{\sqrt2}2\end{pmatrix}\cdot\begin{pmatrix}2\sqrt2&0\\0&2\\0&0\end{pmatrix}\cdot\begin{pmatrix}\frac12&\frac{\sqrt3}2\\-\frac{\sqrt3}2&\frac12\end{pmatrix}$$"
)

S5B = (
    r"נסדר את המקדמים במשוואות:" "\n"
    r"$$\begin{cases}x\equiv3\pmod5\\x\equiv9\pmod{11}\\x\equiv2\pmod3\end{cases}$$" "\n"
    r"נסמן: $m_1=5,\ m_2=11,\ m_3=3$ והם אכן זרים בזוגות. נסמן $m=m_1m_2m_3=5\cdot11\cdot3=165$, ולכן $M_1=33,\ M_2=15,\ M_3=55$. לכן הפתרון למערכת הוא:" "\n"
    r"$$x=(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3)\bmod m=(3\cdot33\cdot x_1+9\cdot15\cdot x_2+2\cdot55\cdot x_3)\bmod165$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$33x_1\equiv1\pmod5\Rightarrow3x_1\equiv1\pmod5\Rightarrow x_1=2$$" "\n"
    r"$$15x_2\equiv1\pmod{11}\Rightarrow4x_2\equiv1\pmod{11}\Rightarrow x_2=3$$" "\n"
    r"$$55x_3\equiv1\pmod3\Rightarrow x_3\equiv1\pmod3\Rightarrow x_3=1$$" "\n"
    r"מכאן: $x=(3\cdot33\cdot2+9\cdot15\cdot3+2\cdot55\cdot1)\bmod165=713\bmod165$, כלומר" "\n"
    r"$$x=53\pmod{165}$$" "\n"
    r"בדיקה: $2\cdot53\equiv1\pmod5$, $3\cdot53\equiv5\pmod{11}$, $53\equiv2\pmod3$."
)

questions = [
    Q(1, "proof", "cauchy_schwarz",
      r"(10%) יהיו $\vec u,\vec v\in\mathbb{R}^n$ שני וקטורים השונים מ-$\vec0$. הוכיחו כי $\|\vec u+\vec v\|=\|\vec u\|+\|\vec v\|$ אם ורק אם קיים סקלר $t>0$ כך ש-$\vec v=t\vec u$.",
      S1A, part="א", points=10),
    Q(1, "computation", "projection",
      r"(15%) במרחב $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע\"י $\langle A,B\rangle=\mathrm{tr}\left(B^TA\right)$ לכל $A,B\in M_2(\mathbb{R})$. חשבו את ההיטל של $\vec v=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ על $\mathrm{Sp}\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\0&1\end{pmatrix}\right\}$.",
      S1B, part="ב", points=15),

    Q(2, "truefalse", "groups", r"סעיף א.1. האם הפעולה אסוציאטיבית? (4%)", S2A, part="א", points=4, contextId="c2", verdict=True),
    Q(2, "truefalse", "groups", r"סעיף א.2. האם המבנה $(\mathbb{R}^*,\odot)$ הוא חבורה אבלית (קומוטטיבית)? (5%)", S2B, part="ב", points=5,
      contextId="c2", verdict=False),
    Q(2, "truefalse", "groups", r"סעיף א.3. האם קיים $x\in\mathbb{R}^*$ כך ש: $x\odot x=x$ ? (4%)", S2C, part="ג", points=4,
      contextId="c2", verdict=False),
    Q(2, "truefalse", "groups",
      r"סעיף א.4. הוכיחו או הפריכו: לכל $a\in\mathbb{N}$ קיים $n\in\mathbb{N}$ כך ש-$a^n=1$, כאשר $a^n=\underbrace{a\odot\cdots\odot a}_{n\ \text{times}}$. (6%)",
      S2D, part="ד", points=6, contextId="c2", verdict=True),
    Q(2, "proof", "pos_def", r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית ו-$c>0$. הוכיחו כי $cI+A+A^2$ מוגדרת חיובית לחלוטין. (6%)", S2E,
      part="ה", points=6),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטרים $a$ ו-$b$ המטריצה $\begin{pmatrix}1&0&a^2\\0&3a-1&0\\a^2&b&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "computation", "least_squares",
      r"(10%) נתונות 4 נקודות במישור: $(1,3),\ (3,5),\ (-2,5),\ (2,2)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים.",
      S3B, part="ב", points=10),

    Q(4, "computation", "groups", r"סעיף א.1. מהו הסדר של $H$ ? (5%)", S4A, part="א", points=5, contextId="c4"),
    Q(4, "computation", "groups", r"סעיף א.2. מהו הסדר של האיבר $\begin{pmatrix}4&0\\0&3\end{pmatrix}$ ? (5%)", S4B, part="ב", points=5,
      contextId="c4"),
    Q(4, "computation", "groups", r"סעיף א.3. מצאו את האיבר ההופכי של $\begin{pmatrix}1&2\\0&3\end{pmatrix}$ . (7%)", S4C, part="ג",
      points=7, contextId="c4"),
    Q(4, "proof", "cauchy_schwarz",
      r"סעיף ב. נתונה הפונקציה $f(x)=\dfrac{(x+k)^2}{x^2+1}$, $k\in\mathbb{N}$. הוכיחו שלכל $x\in\mathbb{R}$ מתקיים $f(x)\le k^2+1$. (8%)",
      S4D, part="ד", points=8),

    Q(5, "computation", "svd", r"סעיף א. מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}2&0\\0&2\\1&\sqrt3\end{pmatrix}$. (18%)", S5A,
      part="א", points=18),
    Q(5, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}2x\equiv1\pmod5\\3x\equiv5\pmod{11}\\x\equiv2\pmod3\end{cases}$. (7%)",
      S5B, part="ב", points=7),
]

exam = {
    "examCode": "24A-A",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ד מועד א'",
    "year": 2024,
    "examDate": "28.3.2024",
    "sourceFile": "algebra-2-24A-A-exam",
    "solutionFile": "algebra-2-24A-A-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
