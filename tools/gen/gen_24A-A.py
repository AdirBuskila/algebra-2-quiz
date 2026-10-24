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

# ---- rubric / pitfalls / steps (ai-draft). Every numeric value is recomputed in tools/verify/24A-A/steps_check.py ----
IDS = "abcdefgh"


def ch(prompt, right, wrong, explain, pos=0):
    vals = list(wrong)
    vals.insert(pos, right)
    return {"type": "choice", "prompt": prompt, "options": [{"id": IDS[i], "value": v} for i, v in enumerate(vals)],
            "correctId": IDS[pos], "explain": explain}


def nm(prompt, ans, explain, tol=0.001):
    return {"type": "numeric", "prompt": prompt, "answer": ans, "tol": tol, "explain": explain}


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def add(num, part, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            assert "steps" not in q
            q.update(kw)
            return
    raise KeyError((num, part))


add(1, "א",
    rubric=rub((r"כיוון (⇒): עבור $\vec v=t\vec u$ עם $t>0$ מראים ששני האגפים שווים ל-$(1+t)\|\vec u\|$", 4),
               (r"כיוון (⇐): העלאה בריבוע של $\|\vec u+\vec v\|=\|\vec u\|+\|\vec v\|$", 2),
               (r"פתיחת שני האגפים וקבלת $\langle\vec u,\vec v\rangle=\|\vec u\|\cdot\|\vec v\|$", 2),
               (r"$\cos\alpha=1$, ולכן הוקטורים מקבילים באותו כיוון ו-$\vec v=t\vec u$ עם $t>0$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"בכיוון (⇒) לכתוב $\|t\vec u\|=t\|\vec u\|$ בלי לציין $t>0$; עבור $t<0$ מתקבל $|t|\|\vec u\|$.",
              r"להסיק מ-$\cos\alpha=1$ ש-$\vec v=\vec u$ ולא $\vec v=t\vec u$ עם $t>0$.",
              r"להוכיח רק כיוון אחד של הטענה הדו-כיוונית."],
    steps=[
        nm(r"נבדוק את הכיוון (⇒) על $\vec u=(3,4)$ ו-$\vec v=2\vec u=(6,8)$. מהו $\|\vec u+\vec v\|$?", 15,
           r"$\vec u+\vec v=(9,12)$ ונורמתו $15$, כמו $\|\vec u\|+\|\vec v\|=5+10$.", 0),
        {"type": "order", "prompt": r"סדרו את שלבי הכיוון (⇐).",
         "lines": [r"מעלים בריבוע את $\|\vec u+\vec v\|=\|\vec u\|+\|\vec v\|$ ומקבלים $\|\vec u+\vec v\|^2=\left(\|\vec u\|+\|\vec v\|\right)^2$.",
                   r"פותחים את שני האגפים: $\|\vec u\|^2+2\langle\vec u,\vec v\rangle+\|\vec v\|^2=\|\vec u\|^2+2\|\vec u\|\|\vec v\|+\|\vec v\|^2$.",
                   r"לכן $\langle\vec u,\vec v\rangle=\|\vec u\|\|\vec v\|$, כלומר $\cos\alpha=1$.",
                   r"הזווית היא $0$, ולכן הוקטורים מקבילים בכיוון זהה: $\vec v=t\vec u$ עם $t>0$."],
         "explain": "כל שלב נשען על הקודם: ריבוע, פתיחה, צמצום והסקה גאומטרית."},
        ch(r"מה מסיקים מ-$\cos\alpha=1$ על הוקטורים השונים מאפס $\vec u,\vec v$?",
           r"$\vec v=t\vec u$ עבור $t>0$ כלשהו",
           [r"$\vec v=t\vec u$ עבור $t<0$ כלשהו", r"$\vec u\perp\vec v$", r"$\vec v=\vec u$ בדיוק"],
           r"זווית $0$ פירושה אותו כיוון, אך לא בהכרח אותו אורך. $t<0$ מתאים ל-$\cos\alpha=-1$, אורתוגונליות מתאימה ל-$\cos\alpha=0$, ו-$\vec v=\vec u$ הוא מקרה פרטי בלבד.", 0),
    ],
    stepsSource="ai-draft")

add(1, "ב",
    rubric=rub((r"גרם-שמידט: $\vec u_1=I$ ו-$\vec u_2=\begin{pmatrix}-1&2\\0&1\end{pmatrix}$ (אחרי הכפלה ב-$2$)", 5),
               (r"נרמול: $\|\vec u_1\|^2=2$ ו-$\|\vec u_2\|^2=6$", 2),
               (r"נוסחת ההיטל $\mathbf{proj}_W(\vec v)=\sum\langle\vec v,\vec e_i\rangle\vec e_i$", 3),
               (r"חישוב המקדמים $\frac12$ ו-$\frac16$ וסכימה", 3),
               (r"התוצאה $\begin{pmatrix}\frac13&\frac13\\0&\frac23\end{pmatrix}$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"להשתמש ב-$\begin{pmatrix}0&1\\0&1\end{pmatrix}$ כאילו הוא ניצב ל-$I$: $\langle I,\begin{pmatrix}0&1\\0&1\end{pmatrix}\rangle=1$.",
              r"לחשב את הנורמה כסכום האיברים ולא כ-$\sqrt{\mathrm{tr}(A^TA)}$.",
              "לשכוח לנרמל ולהשתמש בנוסחת ההיטל עם וקטורים שאינם יחידה."],
    steps=[
        nm(r"מהי $\|\vec u_2\|^2=\mathrm{tr}\left(\vec u_2^T\vec u_2\right)$ עבור $\vec u_2=\begin{pmatrix}-1&2\\0&1\end{pmatrix}$?", 6,
           r"במכפלה $\mathrm{tr}(B^TA)$ זהו סכום ריבועי האיברים: $1+4+0+1=6$.", 0),
        nm(r"מהי $\langle\vec v,\vec u_2\rangle$ עבור $\vec v=\begin{pmatrix}1&1\\1&0\end{pmatrix}$?", 1,
           r"$1\cdot(-1)+1\cdot2+1\cdot0+0\cdot1=1$.", 0),
        nm(r"מהו האיבר בשורה 1 ועמודה 1 של ההיטל $\frac12 I+\frac16\vec u_2$?", 1 / 3,
           r"$\frac12\cdot1+\frac16\cdot(-1)=\frac13$.", 0.0005),
        nm(r"מהו האיבר בשורה 2 ועמודה 2 של ההיטל?", 2 / 3,
           r"$\frac12\cdot1+\frac16\cdot1=\frac23$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(2, "א",
    rubric=rub((r"חישוב $(a\odot b)\odot c=\frac{abc}{ab+ac+bc}$", 1),
               (r"חישוב $a\odot(b\odot c)=\frac{abc}{ab+ac+bc}$", 1),
               (r"השוואת שני הערכים", 1),
               (r"מסקנה: הפעולה אסוציאטיבית", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לבדוק אסוציאטיביות רק עבור שלשה מספרית אחת; זו דוגמה ולא הוכחה.",
              r"טעות באלגברה של שברים מורכבים: $\frac{\frac{ab}{a+b}c}{\frac{ab}{a+b}+c}$ מצטמצם ל-$\frac{abc}{ab+ac+bc}$."],
    steps=[
        nm(r"חשבו $(1\odot2)\odot3$.", 6 / 11, r"$1\odot2=\frac23$ ואז $\frac23\odot3=\frac{2}{\frac23+3}=\frac6{11}$.", 0.0005),
        ch(r"מהו הערך המשותף של $(a\odot b)\odot c$ ו-$a\odot(b\odot c)$?",
           r"$\dfrac{abc}{ab+ac+bc}$", [r"$\dfrac{abc}{a+b+c}$", r"$\dfrac{ab+ac+bc}{abc}$", r"$\dfrac{a+b+c}{abc}$"],
           r"ב-$(a,b,c)=(1,2,3)$ הערך הוא $\frac6{11}$, ורק הביטוי הראשון נותן אותו (השלושה האחרים נותנים $1,\ \frac{11}6,\ 1$).", 2),
    ],
    stepsSource="ai-draft")

add(2, "ב",
    rubric=rub((r"סגירות: $a\odot b=\frac{ab}{a+b}>0$", 1),
               (r"אסוציאטיביות לפי הסעיף הקודם", 1),
               (r"חיפוש איבר ניטרלי: $a\odot e=a$ גורר $a^2=0$", 2),
               (r"אין ניטרלי, ולכן אין חבורה", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לבדוק רק קומוטטיביות ולהסיק שזו חבורה אבלית; חסר איבר ניטרלי.",
              r"להציב $e=1$ או $e=\infty$ ללא בדיקה; $e=1$ נותן $a\odot1=\frac a{a+1}\ne a$."],
    steps=[
        ch(r"איזו תכונה של חבורה אינה מתקיימת ב-$(\mathbb{R}^*,\odot)$?", r"קיום איבר ניטרלי",
           [r"סגירות", r"אסוציאטיביות", r"קומוטטיביות"],
           r"הפעולה סגורה (חיוביים נשארים חיוביים), אסוציאטיבית (הסעיף הקודם) וקומוטטיבית ($a\odot b=b\odot a$ מהסימטריה של הנוסחה). רק הניטרלי חסר.", 1),
        ch(r"איזו משוואה מתקבלת מהדרישה $a\odot e=a$ לכל $a\in\mathbb{R}^*$?", r"$a^2=0$",
           [r"$e=0$", r"$a=e$", r"$0=0$"],
           r"$\frac{ae}{a+e}=a$ גורר $ae=a^2+ae$, כלומר $a^2=0$, בסתירה ל-$a>0$.", 0),
        nm(r"חשבו $3\odot6$ (הפעולה קומוטטיבית, ולכן גם שווה ל-$6\odot3$).", 2, r"$\frac{18}{9}=2$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ג",
    rubric=rub((r"חישוב $x\odot x=\frac{x^2}{2x}=\frac x2$", 1),
               (r"המשוואה $\frac x2=x$", 1),
               (r"הפתרון היחיד הוא $x=0$", 1),
               (r"$0\notin\mathbb{R}^*$, ולכן אין פתרון", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לצמצם $x$ משני האגפים ולהסיק $\frac12=1$ בלי לבדוק את המקרה $x=0$; יש להסיק שאין פתרון חיובי.",
              r"לחשוב ש-$x\odot x=x$ מתקיים עבור האיבר הניטרלי; אין ניטרלי."],
    steps=[
        ch(r"מהו $x\odot x$ עבור $x\in\mathbb{R}^*$?", r"$\dfrac x2$", [r"$2x$", r"$x^2$", r"$\dfrac x4$"],
           r"$x\odot x=\frac{x\cdot x}{x+x}=\frac{x^2}{2x}=\frac x2$. בבדיקה ב-$x=6$: $3$, ולא $12,\ 36$ או $1.5$.", 0),
        nm(r"כמה פתרונות חיוביים יש למשוואה $\frac x2=x$?", 0, r"המשוואה גוררת $x=0$, שאינו ב-$\mathbb{R}^*$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ד",
    rubric=rub((r"חישוב $x^2=\frac x2$", 1),
               (r"חישוב $x^3=\frac x3$", 1),
               (r"הכללה $x^n=\frac xn$", 2),
               (r"הצבה $a=n$ נותנת $n^n=1$, ולכן הטענה נכונה", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לבלבל בין חזקה רגילה לחזקה לפי $\odot$; כאן $x^n$ הוא $x\odot\cdots\odot x$.",
              r"לא להוכיח את החוקיות באינדוקציה: $x^{n+1}=\frac xn\odot x=\frac x{n+1}$."],
    steps=[
        nm(r"חשבו $2\odot2\odot2$ (שלוש פעמים).", 2 / 3, r"$2\odot2=1$ ו-$1\odot2=\frac23$, כלומר $\frac x3$ עבור $x=2$.", 0.0005),
        ch(r"מהי החזקה $x^n=\underbrace{x\odot\cdots\odot x}_{n}$ לפי הפעולה?", r"$\dfrac xn$",
           [r"$\dfrac{x}{2n}$", r"$x^n$ (חזקה רגילה)", r"$nx$"],
           r"$x^1=x,\ x^2=\frac x2,\ x^3=\frac x3$, וההמשך באינדוקציה: $\frac xn\odot x=\frac{x^2/n}{x(n+1)/n}=\frac x{n+1}$.", 0),
        nm(r"עבור $a=5$, איזה $n$ מקיים $a^n=\dfrac an=1$?", 5, r"$\frac5n=1$ נותן $n=5$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ה",
    rubric=rub((r"סימטריה של $cI+A+A^2$", 1),
               (r"פתיחת התבנית $\vec v^T(cI+A+A^2)\vec v=c\|\vec v\|^2+\langle A\vec v,\vec v\rangle+\|A\vec v\|^2$", 2),
               (r"$c\|\vec v\|^2>0$ כי $c>0$ ו-$\vec v\ne\vec0$", 1),
               (r"$\langle A\vec v,\vec v\rangle\ge0$ ו-$\|A\vec v\|^2\ge0$", 1),
               (r"הסכום חיובי ממש, ולכן המטריצה מוגדרת חיובית לחלוטין", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"להסתפק ב-$\ge0$; כדי לקבל חיוביות לחלוטין צריך איבר אחד חיובי ממש, והוא $c\|\vec v\|^2$.",
              r"לשכוח ש-$\vec v^TA^2\vec v=\|A\vec v\|^2$ דורש ש-$A$ סימטרית.",
              r"לבדוק רק ערכים עצמיים של $A$ בלי להסביר איך הם קשורים ל-$A^2$."],
    steps=[
        nm(r"עבור $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $c=1$ ו-$\vec v=(1,0)^T$, מהו $\vec v^T(cI+A+A^2)\vec v$?", 8,
           r"$1+2+5=8$, כי $A^2=\begin{pmatrix}5&4\\4&5\end{pmatrix}$.", 0),
        ch(r"כש-$A$ סימטרית, למה שווה $\vec v^TA^2\vec v$?", r"$\|A\vec v\|^2$",
           [r"$\left(\vec v^TA\vec v\right)^2$", r"$-\|A\vec v\|^2$", r"$\|A^2\vec v\|^2$"],
           r"$\vec v^TA^TA\vec v=(A\vec v)^T(A\vec v)$. ב-$A=\mathrm{diag}(1,2)$ ו-$\vec v=(1,1)$ הערך הוא $5$, ואילו שלוש האחרות נותנות $9,\ -5,\ 17$.", 0),
        {"type": "findbug", "prompt": "בהוכחה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"$cI+A+A^2$ סימטרית, כי $A$ סימטרית.",
                   r"$\vec v^T(cI+A+A^2)\vec v=c\|\vec v\|^2+\langle A\vec v,\vec v\rangle+\|A\vec v\|^2$.",
                   r"$c\|\vec v\|^2>0$ כי $c>0$ ו-$\vec v\ne\vec0$.",
                   r"$A$ מוגדרת חיובית, ולכן $\langle A\vec v,\vec v\rangle<0$, וגם $\|A\vec v\|^2\ge0$.",
                   r"לכן הסכום חיובי ממש, והמטריצה מוגדרת חיובית לחלוטין."],
         "bugIndex": 3,
         "explain": r"$A$ מוגדרת חיובית ולכן $\langle A\vec v,\vec v\rangle\ge0$; עם $<0$ אי אפשר להסיק שהסכום חיובי."},
    ],
    stepsSource="ai-draft")

add(3, "א",
    rubric=rub((r"סימטריה גוררת $b=0$", 2),
               (r"פולינום אופייני $(3a-1-\lambda)\left(\lambda^2-2\lambda+1-a^4\right)$ וערכים עצמיים $3a-1,\ 1+a^2,\ 1-a^2$", 5),
               (r"מוגדרת חיובית כאשר $\frac13\le a\le1$", 4),
               (r"מוגדרת חיובית לחלוטין כאשר $\frac13<a<1$", 2),
               (r"אין ערך של $a$ שבו המטריצה מוגדרת שלילית, ובשאר המקרים אינה מוגדרת", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לשכוח את התנאי $b=0$ ולבדוק רק את הערכים העצמיים של מטריצה לא סימטרית.",
              r"לרשום $a^2-1$ במקום $1-a^2$, ולקבל תחום שגוי עבור $a$.",
              r"לשכוח את התנאי $3a-1\ge0$ ולהסתפק ב-$-1\le a\le1$."],
    steps=[
        nm(r"המטריצה $\begin{pmatrix}1&0&a^2\\0&3a-1&0\\a^2&b&1\end{pmatrix}$ סימטרית. מהו $b$?", 0,
           r"האיבר בשורה 2 ועמודה 3 הוא $0$, ולכן גם האיבר בשורה 3 ועמודה 2 חייב להיות $0$.", 0),
        ch(r"מהם הערכים העצמיים של המטריצה כש-$b=0$?", r"$3a-1,\ 1+a^2,\ 1-a^2$",
           [r"$3a-1,\ a^2+2,\ a^2-2$", r"$3a-1,\ 1+a,\ 1-a$", r"$a,\ 1+a^2,\ 1-a^2$"],
           r"האיבר $3a-1$ נפרד, והבלוק $\begin{pmatrix}1&a^2\\a^2&1\end{pmatrix}$ נותן $1\pm a^2$. ב-$a=2$ הערכים הם $5,\ 5,\ -3$, ורק האפשרות הראשונה מתאימה.", 0),
        ch(r"עבור אילו $a$ המטריצה מוגדרת חיובית (כל הערכים העצמיים $\ge0$)?", r"$\frac13\le a\le1$",
           [r"$\frac13<a<1$", r"$a\ge\frac13$", r"$-1\le a\le1$"],
           r"נדרש $3a-1\ge0$ וגם $1-a^2\ge0$. ב-$a=\frac13$ הערך $0$ מותר; ב-$a=2$ מתקבל ערך שלילי; ב-$a=0$ הערך $3a-1=-1$.", 0),
        nm(r"מהו הערך העצמי הקטן ביותר כאשר $a=\frac12$?", 0.5,
           r"הערכים הם $3a-1=0.5,\ 1+a^2=1.25,\ 1-a^2=0.75$, והקטן הוא $0.5$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(3, "ב",
    rubric=rub((r"בניית $A=\begin{pmatrix}1&1\\3&1\\-2&1\\2&1\end{pmatrix}$ ו-$\vec b=(3,5,5,2)^T$", 3),
               (r"חישוב $A^TA=\begin{pmatrix}18&4\\4&4\end{pmatrix}$", 2),
               (r"חישוב $A^T\vec b=\begin{pmatrix}12\\15\end{pmatrix}$ ופתרון המערכת הנורמלית", 3),
               (r"$y=-\frac3{14}x+\frac{111}{28}$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לפתור את $A\vec x=\vec b$ ישירות, אף שאין פתרון מדויק.",
              r"טעות סימן ב-$\sum xy=3+15-10+4=12$.",
              "להפוך בין $m$ ל-$n$ בפתרון המערכת."],
    steps=[
        nm(r"מהו $\sum x_i^2$ לנקודות $(1,3),(3,5),(-2,5),(2,2)$?", 18, r"$1+9+4+4=18$.", 0),
        nm(r"מהו $\sum x_iy_i$?", 12, r"$3+15-10+4=12$.", 0),
        nm(r"פתרו את $\begin{pmatrix}18&4\\4&4\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}12\\15\end{pmatrix}$. מהו $m$?", -3 / 14,
           r"חיסור המשוואות נותן $14m=-3$, כלומר $m=-\frac3{14}\approx-0.214$.", 0.0005),
        nm(r"מהו $n$?", 111 / 28, r"$4n=15-4m=15+\frac67=\frac{111}7$ ולכן $n=\frac{111}{28}\approx3.964$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(4, "א",
    rubric=rub((r"התנאי $ac\ne0$ בכתיבה של הסעיף נותן שני איברי אלכסון שונים מאפס", 2),
               (r"$6$ אפשרויות לכל איבר אלכסון ו-$7$ לאיבר שמעל האלכסון", 1),
               (r"עקרון הכפל: $6\cdot6\cdot7=252$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לספור $7^3=343$ ולשכוח את התנאי על האלכסון.",
              r"לדרוש גם שהאיבר מעל האלכסון שונה מאפס."],
    steps=[
        nm(r"כמה ערכים אפשריים יש לכל איבר אלכסון (שונה מאפס ב-$\mathbb{Z}_7$)?", 6, r"$\{1,\dots,6\}$.", 0),
        nm(r"כמה ערכים אפשריים יש לאיבר שמעל האלכסון?", 7, r"אין עליו תנאי: כל $\mathbb{Z}_7$.", 0),
        nm(r"מהו $|H|$?", 252, r"$6\cdot6\cdot7=252$.", 0),
    ],
    stepsSource="ai-draft")

add(4, "ב",
    rubric=rub((r"$3^6\equiv1\pmod7$ והסדר של $3$ ב-$\mathbb{Z}_7^*$ הוא $6$", 2),
               (r"$4^3\equiv1\pmod7$ והסדר של $4$ הוא $3$", 2),
               (r"הסדר של המטריצה האלכסונית הוא ה-$\mathrm{lcm}$: $6$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"להניח שהסדר הוא $6\cdot3=18$ במקום ה-$\mathrm{lcm}$.",
              r"לחשב חזקות של המטריצה כולה ולא של כל איבר אלכסון בנפרד."],
    steps=[
        nm(r"מהו הסדר של $3$ ב-$\mathbb{Z}_7^*$?", 6, r"$3,2,6,4,5,1$: החזקה הראשונה השווה ל-$1$ היא $3^6$.", 0),
        nm(r"מהו הסדר של $4$ ב-$\mathbb{Z}_7^*$?", 3, r"$4,2,1$: החזקה הראשונה השווה ל-$1$ היא $4^3$.", 0),
        nm(r"מהו הסדר של $\begin{pmatrix}4&0\\0&3\end{pmatrix}$?", 6, r"$\mathrm{lcm}(3,6)=6$.", 0),
    ],
    stepsSource="ai-draft")

add(4, "ג",
    rubric=rub((r"סימון ההופכי $\begin{pmatrix}a&b\\0&c\end{pmatrix}$ וכתיבת $\begin{pmatrix}1&2\\0&3\end{pmatrix}\begin{pmatrix}a&b\\0&c\end{pmatrix}=I$", 2),
               (r"המערכת $a\equiv1,\ b+2c\equiv0,\ 3c\equiv1\pmod7$", 2),
               (r"$c\equiv5$ ו-$b\equiv4$", 2),
               (r"התשובה $\begin{pmatrix}1&4\\0&5\end{pmatrix}$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"להפוך כל איבר בנפרד: ההופכי של $2$ אינו חלק מההופכי של המטריצה.",
              r"לחשב מודולו אחר ($\bmod 3$ או $\bmod 5$) במקום $\bmod 7$.",
              "לשכוח להקטין מספר שלילי ($b=-10$) מודולו $7$."],
    steps=[
        nm(r"מהי הדטרמיננטה של $\begin{pmatrix}1&2\\0&3\end{pmatrix}$ מודולו $7$?", 3, r"$1\cdot3-2\cdot0=3$.", 0),
        nm(r"מהו $c$ שמקיים $3c\equiv1\pmod7$ (בטווח $0$ עד $6$)?", 5, r"$3\cdot5=15\equiv1$.", 0),
        nm(r"מהו $b$ שמקיים $b+2c\equiv0\pmod7$ עבור $c=5$ (בטווח $0$ עד $6$)?", 4, r"$b\equiv-10\equiv4\pmod7$.", 0),
    ],
    stepsSource="ai-draft")

add(4, "ד",
    rubric=rub((r"ניסוח מחדש: $(x+k)^2\le(k^2+1)(x^2+1)$", 2),
               (r"בחירת הוקטורים $\vec u=(x,1)^T$ ו-$\vec v=(1,k)^T$", 2),
               (r"הפעלת קושי-שוורץ $|x+k|\le\sqrt{x^2+1}\sqrt{1+k^2}$", 2),
               (r"העלאה בריבוע וחלוקה ב-$x^2+1>0$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לבחור $\vec u=(x,k)$ ו-$\vec v=(1,1)$: מתקבל $(x+k)^2\le2(x^2+k^2)$, שאינה הטענה.",
              r"לשכוח שחלוקה ב-$x^2+1$ חוקית כי הוא חיובי.",
              "להעלות בריבוע בלי ערך מוחלט ולאבד את הסימן."],
    steps=[
        ch(r"איזה זוג וקטורים מניב דרך קושי-שוורץ את $(x+k)^2\le(k^2+1)(x^2+1)$?",
           r"$\vec u=(x,1)^T$ ו-$\vec v=(1,k)^T$",
           [r"$\vec u=(x,k)^T$ ו-$\vec v=(1,1)^T$", r"$\vec u=(x,1)^T$ ו-$\vec v=(k,1)^T$", r"$\vec u=(x,x^2)^T$ ו-$\vec v=(1,k)^T$"],
           r"המכפלה הפנימית חייבת להיות $x+k$ והנורמות בריבוע $x^2+1$ ו-$1+k^2$. הזוג השני נותן $2(x^2+k^2)$ באגף ימין, השלישי נותן מכפלה $kx+1$, והרביעי נותן נורמה $x^2+x^4$.", 0),
        nm(r"עבור $x=2,\ k=3$, מהו $\|\vec u\|^2\cdot\|\vec v\|^2=(x^2+1)(1+k^2)$?", 50,
           r"$5\cdot10=50\ge(x+k)^2=25$, והמנה $\frac{25}5=5\le k^2+1=10$.", 0),
        {"type": "findbug", "prompt": "בהוכחה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"צריך להוכיח $(x+k)^2\le(k^2+1)(x^2+1)$ לכל $x$.",
                   r"נבחר $\vec u=(x,1)^T$ ו-$\vec v=(1,k)^T$, ואז $\langle\vec u,\vec v\rangle=x+k$.",
                   r"לפי קושי-שוורץ $|x+k|\le\sqrt{x^2+1}\cdot\sqrt{1+k^2}$.",
                   r"מעלים בריבוע ומקבלים $(x+k)^2\ge(k^2+1)(x^2+1)$.",
                   r"מחלקים ב-$x^2+1>0$ ומקבלים $f(x)\le k^2+1$."],
         "bugIndex": 3,
         "explain": r"העלאה בריבוע של אי-שוויון בין מספרים אי-שליליים שומרת על כיוונו: $\le$ ולא $\ge$."},
    ],
    stepsSource="ai-draft")

add(5, "א",
    rubric=rub((r"חישוב $A^TA=\begin{pmatrix}5&\sqrt3\\\sqrt3&7\end{pmatrix}$", 3),
               (r"ערכים עצמיים $8,\ 4$ וערכים סינגולריים $2\sqrt2,\ 2$", 3),
               (r"וקטורים עצמיים מנורמלים של $A^TA$ ובניית $V$", 4),
               (r"כתיבת $\Sigma=\begin{pmatrix}2\sqrt2&0\\0&2\\0&0\end{pmatrix}$", 3),
               (r"חישוב $\vec u_i=\frac1{\sigma_i}A\vec v_i$ והשלמת $\vec u_3$ ל-$U$ אורתוגונלית", 5)),
    rubricSource="ai-draft",
    pitfalls=[r"לרשום את הערכים העצמיים $8,4$ במקום הערכים הסינגולריים $2\sqrt2,2$.",
              r"לבחור סימנים שרירותיים ל-$\vec u_i$ ולא לחשב אותם מ-$\vec u_i=\frac1{\sigma_i}A\vec v_i$.",
              r"להציג את $V^T$ במקום $V$: בתשובה הרשמית המטריצה השלישית היא $V^T$."],
    steps=[
        ch(r"באיזו מטריצה משתמשים כדי למצוא את העמודות של $V$ (ה-$2\times2$)?", r"$A^TA$",
           [r"$AA^T$", r"$A+A^T$", r"$A^{-1}$"],
           r"$A^TA$ היא $2\times2$ כמו $V$. $AA^T$ היא $3\times3$ (נותנת את $U$), ול-$A+A^T$ ול-$A^{-1}$ אין משמעות כי $A$ אינה ריבועית.", 0),
        nm(r"מהו הערך העצמי הגדול של $A^TA=\begin{pmatrix}5&\sqrt3\\\sqrt3&7\end{pmatrix}$?", 8,
           r"עקבה $12$ ודטרמיננטה $35-3=32$, ולכן $\lambda=8,\ 4$.", 0),
        nm(r"מהו הערך הסינגולרי השני $\sigma_2$?", 2, r"$\sigma_2=\sqrt4=2$.", 0),
        nm(r"נתון $\vec v_1=\left(\frac12,\frac{\sqrt3}2\right)^T$. מהו הרכיב השלישי של $\vec u_1=\frac1{\sigma_1}A\vec v_1$?", 0.707107,
           r"$A\vec v_1=(1,\sqrt3,2)^T$ ו-$\sigma_1=2\sqrt2$, ולכן הרכיב הוא $\frac2{2\sqrt2}=\frac{\sqrt2}2\approx0.707$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(5, "ב",
    rubric=rub((r"צמצום המשוואות לצורה $x\equiv a_i\pmod{m_i}$: $x\equiv3\pmod5,\ x\equiv9\pmod{11},\ x\equiv2\pmod3$", 2),
               (r"סימון $m=165$ וחישוב $M_1=33,\ M_2=15,\ M_3=55$", 1),
               (r"חישוב ההופכיים $x_1=2,\ x_2=3,\ x_3=1$", 2),
               (r"הצבה בנוסחה והקטנה מודולו $165$: $x\equiv53$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לא לחלק את $2x\equiv1$ ו-$3x\equiv5$ בהופכי של המקדם לפני שימוש בנוסחה.",
              r"לחשב את ההופכי מודולו $165$ ולא מודולו $m_i$.",
              "לשכוח להקטין את הסכום $713$ מודולו $165$."],
    steps=[
        nm(r"פתרו $2x\equiv1\pmod5$ (בטווח $0$ עד $4$).", 3, r"$2\cdot3=6\equiv1$.", 0),
        nm(r"פתרו $3x\equiv5\pmod{11}$ (בטווח $0$ עד $10$).", 9, r"$3\cdot9=27\equiv5\pmod{11}$.", 0),
        nm(r"מהו $x_2$ שמקיים $15x_2\equiv1\pmod{11}$ (בטווח $0$ עד $10$)?", 3, r"$15\equiv4$ ו-$4\cdot3=12\equiv1\pmod{11}$.", 0),
        nm(r"מהו הפתרון $x$ בטווח $0$ עד $164$?", 53,
           r"$3\cdot33\cdot2+9\cdot15\cdot3+2\cdot55\cdot1=198+405+110=713=4\cdot165+53$.", 0),
    ],
    stepsSource="ai-draft")

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
