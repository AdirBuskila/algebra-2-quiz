# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json -- algebra-2 (20079), semester B 2023, moed B (13.07.2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23B-B.py

Source: exam 2 pp. + typed official solution 8 pp. (both read from the rendered pages). 5 printed questions
(solve 4 of 5, 25% each), 16 items, all shipped.

Part letters: the bank allows single-letter parts only, so numbered sub-parts get letters in order.
  Q2: items 1..4 of part A -> parts a..d; items 1,2 of part B -> parts e, f.
  Q4: a, then b.1 -> b, b.2 -> c.     Q5: a, then b.1 -> b, b.2 -> c.
Every question text starts with its printed label.

Typos in the official solution (checked with tools/verify/23B-B/check.py; no FINAL answer is wrong):
- Q4a: the eigenspace section is headed "lambda = 9" but the eigenvalue is 5 (relabelled). The official prints
  D = diag(5,5,0) next to Q whose columns are (v1 for 0, v2 for 5, v3 for 5), so A = Q D Q^T only holds with
  D = diag(0,5,5) (written so; same slip class as 26A-A Q1a).
- Q3a: "positive definite" in the official is the course's term for positive SEMIdefinite (a >= 1); "strictly" is a > 1.
- Q3b: the official's last value 359 (mod 60) is not reduced; 359 = 59 (mod 60). Kept as printed with the reduction added.
- Q5a: the official is a pasted calculator output (QR of the matrix); transcribed as the same Q, R plus the check Q R = A.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ------------------------------------------------------------------ contexts
CTX = {
    "c2a": {"kind": "text", "title": "שאלה 2 סעיף א",
            "text": r"נסתכל בחבורה (אין צורך להוכיח זאת) $G=\left\{(a,b)\ \middle|\ a\in\mathbb{Z}_5^*,\ b\in\mathbb{Z}_7^*\right\}$ עם פעולת הכפל המוגדרת בצורה הבאה: $(a,b)\cdot(c,d)=(a\cdot c,\ b\cdot d)$, כאשר באגף ימין הכפל הוא מודולו 5 ו-7 בהתאמה."},
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף ב",
            "text": r"תהיינה $A,B\in M_n(\mathbb{R})$, כאשר $A$ מוגדרת חיובית. הוכיחו כי:"},
    "c4b": {"kind": "text", "title": "שאלה 4 סעיף ב",
            "text": r"תהי $G$ חבורה בה כל איבר הופכי לעצמו. זאת אומרת לכל $x\in G$ מתקיים $x=x^{-1}$. הוכיחו כי:"},
    "c5b": {"kind": "text", "title": "שאלה 5 סעיף ב",
            "text": r"יהי $\vec v$ וקטור יחידה במרחב $\mathbb{R}^n$. נגדיר מטריצת $P=\vec v\cdot\vec v^T\in M_n(\mathbb{R})$."},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"נחפש את המודל הליניארי מהצורה $y=mx+n$ לפי שיטת הריבועים הפחותים:" "\n"
    r"$$\begin{pmatrix}-2&1\\-1&1\\0&1\\2&1\\6&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}\approx\begin{pmatrix}-3\\0\\1\\2\\10\end{pmatrix}\ \mapsto\ \begin{pmatrix}-2&-1&0&2&6\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}-2&1\\-1&1\\0&1\\2&1\\6&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}-2&-1&0&2&6\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}-3\\0\\1\\2\\10\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\ \begin{pmatrix}45&5\\5&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}70\\10\end{pmatrix}\ \Rightarrow\ m=1.5,\ \ n=0.5$$" "\n"
    r"נציב ונקבל: $y=1.5x+0.5$."
)

S1B = (
    r"נסתכל במרחב מכפלה פנימית $C_{[1,2]}$ עם המכפלה הפנימית האינטגרלית הרגילה: $\langle f,g\rangle=\displaystyle\int_1^2 f(x)g(x)\,dx$." "\n"
    r"נגדיר $g(x)=\dfrac1x$ וניעזר באי-שוויון קושי-שוורץ. נקבל:" "\n"
    r"$$\left\langle f,\frac1x\right\rangle\le\|f(x)\|\cdot\left\|\frac1x\right\|\ \Longleftrightarrow\ \left\langle f,\frac1x\right\rangle^2\le\|f(x)\|^2\cdot\left\|\frac1x\right\|^2$$" "\n"
    r"$$\left\langle f,\frac1x\right\rangle^2=\left(\int_1^2 f(x)\frac1x\,dx\right)^2$$" "\n"
    r"$$\left\|\frac1x\right\|^2=\int_1^2\frac1{x^2}\,dx=\left[-\frac1x\right]_1^2=\frac12$$" "\n"
    r"$$\left(\int_1^2\frac{f(x)}{x}\,dx\right)^2\le\frac12\int_1^2 f^2(x)\,dx$$"
)

S2A1 = (
    r"האיבר הניטרלי של $G$ הוא $(1,1)$. הרי לכל $(a,b)\in G$ מתקיים:" "\n"
    r"$$(1,1)\cdot(a,b)=(1\cdot a,\ 1\cdot b)=(a,b)$$"
)

S2A2 = (
    r"כיוון ש-$2\cdot3=1\pmod 5$ ו-$3\cdot5=1\pmod 7$, אנו מקבלים ש-$(2,3)^{-1}=(3,5)$."
)

S2A3 = (
    r"הסדר של $\mathbb{Z}_5^*$ הוא 4 והסדר של $\mathbb{Z}_7^*$ הוא 6. לכן הסדר של $G$ הוא $24$."
)

S2A4 = (
    r"הסדר של $2$ ב-$\mathbb{Z}_5^*$ הוא 4, מפני ש-$2^4=1\pmod 5$. הסדר של $3$ ב-$\mathbb{Z}_7^*$ הוא 6, מפני ש-$3^6=1\pmod 7$. הסדר של $(2,3)$ ב-$G$ שווה לכפולה משותפת מינימלית של 4 ו-6. כלומר הסדר של $(2,3)$ ב-$G$ הוא $12$."
)

S2B1 = (
    r"קודם כל, $(-A-B^TB)^T=-A^T-(B^TB)^T=-A-B^TB$. בנוסף לכל $\vec v\in\mathbb{R}^n$ מתקיים" "\n"
    r"$$\vec v^T(-A-B^TB)\vec v=-(\vec v^TA\vec v)-(\vec v^TB^TB\vec v)=-(\vec v^TA\vec v)-\|B\vec v\|^2\le0$$" "\n"
    r"משום ש-$A$ מוגדרת חיובית."
)

S2B2 = (
    r"באופן דומה: $\vec v^T\left(B^TAB\right)\vec v=\left(\vec v^TB^T\right)A\left(B\vec v\right)=(B\vec v)^TA(B\vec v)\ge0$, מפני ש-$A$ מוגדרת חיובית."
)

S3A = (
    r"נחשב את הערכים העצמיים של המטריצה:" "\n"
    r"$$\begin{vmatrix}a^2-\lambda&0&1\\0&a-\lambda&0\\1&0&a^2-\lambda\end{vmatrix}=(a-\lambda)\begin{vmatrix}a^2-\lambda&1\\1&a^2-\lambda\end{vmatrix}=(a-\lambda)\left(\lambda^2-2\lambda a^2+a^4-1\right)$$" "\n"
    r"לכן הערכים העצמיים הם: $\lambda=a$ , $\lambda=a^2+1$ , $\lambda=a^2-1$." "\n"
    r"המטריצה **מוגדרת חיובית** כאשר" "\n"
    r"$$\begin{cases}a\ge0\\a^2+1\ge0\\a^2-1\ge0\end{cases}\ \Rightarrow\ \begin{cases}a\ge0\\a^2\ge1\end{cases}\ \Rightarrow\ a\ge1$$" "\n"
    r"המטריצה **מוגדרת חיובית לחלוטין** כאשר $a>1$." "\n"
    r"המטריצה מוגדרת שלילית כאשר" "\n"
    r"$$\begin{cases}a\le0\\a^2+1\le0\\a^2-1\le0\end{cases}\ \Rightarrow\ a\in\emptyset$$" "\n"
    "סיכום:\n"
    r"המטריצה מוגדרת חיובית כאשר $a\ge1$." "\n"
    r"המטריצה מוגדרת חיובית לחלוטין כאשר $a>1$." "\n"
    "בשאר המקרים המטריצה אינה מוגדרת."
)

S3B = (
    r"נסמן: $q_1=3,\ q_2=2,\ q_3=4$ והם אכן זרים בזוגות. כמו כן נסמן: $m_1=4,\ m_2=3,\ m_3=5$ ולבסוף $m=m_1m_2m_3=4\cdot3\cdot5=60$, ולכן: $M_1=15,\ M_2=20,\ M_3=12$." "\n"
    "הפתרון למערכת הוא:\n"
    r"$$x=\left(q_1M_1x_1+q_2M_2x_2+q_3M_3x_3\right)\pmod m=\left(3\cdot15\cdot x_1+2\cdot20\cdot x_2+4\cdot12\cdot x_3\right)\pmod{60}$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$15x_1\equiv1\pmod 4\ \Rightarrow\ 3x_1\equiv1\pmod 4\ \Rightarrow\ x_1=3$$" "\n"
    r"$$20x_2\equiv1\pmod 3\ \Rightarrow\ 2x_2\equiv1\pmod 3\ \Rightarrow\ x_2=2$$" "\n"
    r"$$12x_3\equiv1\pmod 5\ \Rightarrow\ 2x_3\equiv1\pmod 5\ \Rightarrow\ x_3=3$$" "\n"
    "מכאן:\n"
    r"$$x=\left(3\cdot15\cdot3+2\cdot20\cdot2+4\cdot12\cdot3\right)\pmod{60}=359\pmod{60}$$" "\n"
    r"כלומר $x\equiv59\pmod{60}$."
)

S4A = (
    r"נחשב ערכים עצמיים:" "\n"
    r"$$|A-\lambda I|=\begin{vmatrix}5-\lambda&0&0\\0&4-\lambda&2\\0&2&1-\lambda\end{vmatrix}=(5-\lambda)\left[(4-\lambda)(1-\lambda)-4\right]=(5-\lambda)\left(\lambda^2-5\lambda\right)=-\lambda(\lambda-5)^2$$" "\n"
    r"ערכים עצמיים: $0,5,5$. נמצא את הוקטורים העצמיים המתאימים." "\n"
    r"**עבור $\lambda=0$:**" "\n"
    r"$$A-0I=\begin{pmatrix}5&0&0\\0&4&2\\0&2&1\end{pmatrix}\sim\begin{pmatrix}5&0&0\\0&2&1\\0&0&0\end{pmatrix}\ \to\ \begin{cases}x=0\\y=-0.5t\\z=t\end{cases}\ \to\ \vec v_1=\begin{pmatrix}0\\-1\\2\end{pmatrix}$$" "\n"
    r"**עבור $\lambda=5$:**" "\n"
    r"$$A-5I=\begin{pmatrix}0&0&0\\0&-1&2\\0&2&-4\end{pmatrix}\sim\begin{pmatrix}0&0&0\\0&1&-2\\0&0&0\end{pmatrix}\ \to\ \begin{cases}x=s\\y=2t\\z=t\end{cases}\ \to\ \vec v_2=\begin{pmatrix}0\\2\\1\end{pmatrix},\ \vec v_3=\begin{pmatrix}1\\0\\0\end{pmatrix}$$" "\n"
    r"אפשר לראות ששלושת הוקטורים שקיבלנו כבר מהווים בסיס אורתוגונלי. ננרמל אותם, נרשום כעמודות במטריצה ונקבל את המטריצה האורתוגונלית המלכסנת:" "\n"
    r"$$Q=\begin{pmatrix}0&0&1\\\frac{-1}{\sqrt5}&\frac2{\sqrt5}&0\\\frac2{\sqrt5}&\frac1{\sqrt5}&0\end{pmatrix}$$" "\n"
    r"נגדיר $D=\begin{pmatrix}0&0&0\\0&5&0\\0&0&5\end{pmatrix}$ (סדר הערכים העצמיים כסדר העמודות של $Q$). מתקיים: $A=QDQ^T$."
)

S4B1 = (
    r"נתון שלכל $x\in G$ מתקיים $x^{-1}=x$, כלומר $x^2=1$ כי כל איבר הפוך לעצמו." "\n"
    r"יהיו $x,y\in G$. מתקיים" "\n"
    r"$$x\cdot y=(x\cdot y)^{-1}=y^{-1}\cdot x^{-1}=y\cdot x$$"
)

S4B2 = (
    r"נניח כי $x^3=y^5$. אזי $x^3=x\cdot x^2=x$ ו-$y^5=y\cdot y^2\cdot y^2=y$ (כי $x^2=y^2=1$). לכן $x=y$."
)

S5A = (
    r"נמצא את פירוק ה-$QR$ של $A=\begin{pmatrix}-1&3\\1&5\end{pmatrix}$." "\n"
    r"נבצע אורתונורמליזציה לעמודות המטריצה. העמודות של $Q$ הן הוקטורים האורתונורמליים:" "\n"
    r"$$Q=\begin{pmatrix}-\frac{\sqrt2}2&\frac{\sqrt2}2\\\frac{\sqrt2}2&\frac{\sqrt2}2\end{pmatrix}$$" "\n"
    r"$$R=Q^TA=\begin{pmatrix}-\frac{\sqrt2}2&\frac{\sqrt2}2\\\frac{\sqrt2}2&\frac{\sqrt2}2\end{pmatrix}\begin{pmatrix}-1&3\\1&5\end{pmatrix}=\begin{pmatrix}\sqrt2&\sqrt2\\0&4\sqrt2\end{pmatrix}$$" "\n"
    r"כלומר $A=QR$ עם $Q$ ו-$R$ שלעיל."
)

S5B1 = (
    r"מתקיים $P^T=\left(\vec v\cdot\vec v^T\right)^T=\vec v\cdot\vec v^T=P$. בנוסף, $P^2=\vec v\cdot\underbrace{\left(\vec v^T\cdot\vec v\right)}_{\|\vec v\|^2=1}\cdot\vec v^T=P$." "\n"
    r"הראינו ש-$P$ סימטרית. לכל $\vec u$:" "\n"
    r"$$\vec u^T\cdot P\cdot\vec u=\vec u^T\cdot\left(\vec v\cdot\vec v^T\right)\cdot\vec u=\left(\vec u^T\cdot\vec v\right)\cdot\left(\vec v^T\cdot\vec u\right)=\left(\vec v^T\cdot\vec u\right)^T\cdot\left(\vec v^T\cdot\vec u\right)\ge0$$" "\n"
    r"לכן $P$ מוגדרת חיובית."
)

S5B2 = (
    r"$$\langle\vec u-P\vec u,\vec v\rangle=\vec v^T\left(\vec u-P\vec u\right)=\vec v^T\vec u-\vec v^TP\vec u=\vec v^T\vec u-\vec v^T\vec v\,\vec v^T\vec u=\vec v^T\vec u-\vec v^T\vec u=0$$" "\n"
    r"(השתמשנו ב-$\|\vec v\|=1$, כלומר $\vec v^T\vec v=1$)."
)

questions = [
    Q(1, "computation", "least_squares",
      r"(13%) נתונות 5 נקודות במישור $(6,10)$ , $(2,2)$ , $(0,1)$ , $(-1,0)$ , $(-2,-3)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים.",
      S1A, part="א", points=13),
    Q(1, "proof", "cauchy_schwarz",
      r"(12%) הוכיחו כי $\left(\displaystyle\int_1^2\frac{f(x)}{x}\,dx\right)^2\le\frac12\displaystyle\int_1^2 f^2(x)\,dx$ כאשר $f(x)\in C_{[1,2]}$.",
      S1B, part="ב", points=12),

    Q(2, "computation", "groups", r"סעיף א.1. מהו האיבר הניטרלי של $G$ ? (3%)", S2A1, part="א", points=3, contextId="c2a"),
    Q(2, "computation", "groups", r"סעיף א.2. מצאו את האיבר ההופכי של $(2,3)$ ? (4%)", S2A2, part="ב", points=4, contextId="c2a"),
    Q(2, "computation", "groups", r"סעיף א.3. מהו הסדר של $G$ ? (5%)", S2A3, part="ג", points=5, contextId="c2a"),
    Q(2, "computation", "groups", r"סעיף א.4. מהו הסדר של $(2,3)$ ? (5%)", S2A4, part="ד", points=5, contextId="c2a"),
    Q(2, "proof", "pos_def", r"סעיף ב.1. $-A-B^TB$ מוגדרת שלילית. (4%)", S2B1, part="ה", points=4, contextId="c2b"),
    Q(2, "proof", "pos_def", r"סעיף ב.2. $B^TAB$ מוגדרת חיובית. (4%)", S2B2, part="ו", points=4, contextId="c2b"),

    Q(3, "computation", "pos_def",
      r"(17%) עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}a^2&0&1\\0&a&0\\1&0&a^2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=17),
    Q(3, "computation", "crt",
      r"(8%) פתרו את המערכות הבאות באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv3\pmod 4\\x\equiv2\pmod 3\\x\equiv4\pmod 5\end{cases}$.",
      S3B, part="ב", points=8),

    Q(4, "computation", "orthodiag",
      r"(15%) בצעו לכסון אורתוגונלי עבור המטריצה $A=\begin{pmatrix}5&0&0\\0&4&2\\0&2&1\end{pmatrix}$.",
      S4A, part="א", points=15),
    Q(4, "proof", "groups", r"סעיף ב.1. $G$ חבורה אבלית, כלומר לכל $x,y\in G$ מתקיים $x\cdot y=y\cdot x$. (5%)", S4B1, part="ב", points=5,
      contextId="c4b"),
    Q(4, "proof", "groups", r"סעיף ב.2. אם $x,y\in G$ ו-$x^3=y^5$ אז $x=y$. (5%)", S4B2, part="ג", points=5, contextId="c4b"),

    Q(5, "computation", "qr", r"(15%) מצאו פירוק $QR$ עבור המטריצה $\begin{pmatrix}-1&3\\1&5\end{pmatrix}$.", S5A, part="א", points=15),
    Q(5, "proof", "pos_def", r"סעיף ב.1. הוכיחו כי $P$ מוגדרת חיובית ומתקיים: $P^2=P$. (5%)", S5B1, part="ב", points=5, contextId="c5b"),
    Q(5, "proof", "projection", r"סעיף ב.2. הוכיחו כי לכל וקטור $\vec u\in\mathbb{R}^n$ הוקטור $\vec u-P\vec u$ אורתוגונלי ל-$\vec v$. (5%)", S5B2,
      part="ג", points=5, contextId="c5b"),
]

# ---- rubric / pitfalls / steps (ai-draft). Every numeric value is recomputed in tools/verify/23B-B/steps_check.py ----
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
    rubric=rub((r"בחירת המודל $y=mx+n$ וכתיבת המערכת $A\vec x\approx\vec b$", 2),
               (r"חישוב $A^TA=\begin{pmatrix}45&5\\5&5\end{pmatrix}$", 4),
               (r"חישוב $A^T\vec b=\begin{pmatrix}70\\10\end{pmatrix}$", 4),
               (r"פתרון המערכת הנורמלית וקבלת $y=1.5x+0.5$", 3)),
    rubricSource="ai-draft",
    pitfalls=[r"לשים את הנקודות בסדר שונה בעמודות ולהחליף בין $x$ ל-$y$ ב-$A$ ו-$\vec b$.",
              r"לשכוח את עמודת האחדות ב-$A$ ולקבל ישר דרך הראשית.",
              r"טעות חישוב ב-$\sum xy=60+4+0+0+6=70$."],
    steps=[
        nm(r"מהו $\sum x_i^2$, כלומר האיבר בשורה 1 ועמודה 1 של $A^TA$?", 45,
           r"$36+4+0+1+4=45$.", 0),
        nm(r"מהו $\sum x_iy_i$, כלומר הרכיב הראשון של $A^T\vec b$?", 70,
           r"$6\cdot10+2\cdot2+0\cdot1+(-1)\cdot0+(-2)\cdot(-3)=60+4+0+0+6=70$.", 0),
        nm(r"פתרו את $\begin{pmatrix}45&5\\5&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}70\\10\end{pmatrix}$. מהו $m$?", 1.5,
           r"חיסור המשוואה $5m+5n=10$ מ-$45m+5n=70$ נותן $40m=60$, כלומר $m=1.5$.", 0.0005),
        nm(r"מהו $n$?", 0.5, r"$5n=10-5m=2.5$, כלומר $n=0.5$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(1, "ב",
    rubric=rub((r"בחירת המכפלה הפנימית האינטגרלית $\langle f,g\rangle=\int_1^2fg\,dx$ ו-$g(x)=\frac1x$", 3),
               (r"קושי-שוורץ בריבוע: $\langle f,g\rangle^2\le\|f\|^2\|g\|^2$", 3),
               (r"חישוב $\|g\|^2=\int_1^2\frac1{x^2}dx=\frac12$", 4),
               (r"הצבה וקבלת הטענה", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לבחור $g(x)=x$ או $g(x)=1$, ואז $\langle f,g\rangle$ אינו האינטגרל הנתון.",
              r"לחשב את $\int_1^2\frac1{x^2}dx$ כ-$\ln2$ (זה האינטגרל של $\frac1x$).",
              "לשכוח להעלות את שני האגפים בריבוע, כך שמתקבל אי-שוויון על האינטגרל בלי ריבוע."],
    steps=[
        ch(r"איזו פונקציה $g$ מקיימת $\langle f,g\rangle=\displaystyle\int_1^2\frac{f(x)}{x}\,dx$ במכפלה $\langle f,g\rangle=\int_1^2f(x)g(x)\,dx$?",
           r"$g(x)=\dfrac1x$", [r"$g(x)=x$", r"$g(x)=1$", r"$g(x)=\ln x$"],
           r"רק עבור $g(x)=\frac1x$ מתקבל הביטוי $f(x)\cdot\frac1x$. שאר האפשרויות נותנות $xf(x)$, $f(x)$ או $f(x)\ln x$.", 0),
        nm(r"מהו $\|g\|^2=\displaystyle\int_1^2\frac1{x^2}\,dx$?", 0.5, r"$\left[-\frac1x\right]_1^2=-\frac12+1=\frac12$.", 0.0005),
        {"type": "findbug", "prompt": "בהוכחה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"מגדירים $\langle f,g\rangle=\int_1^2f(x)g(x)\,dx$ ו-$g(x)=\frac1x$.",
                   r"לפי קושי-שוורץ $\langle f,g\rangle^2\le\|f\|^2\cdot\|g\|^2$.",
                   r"$\langle f,g\rangle^2=\left(\int_1^2\frac{f(x)}x\,dx\right)^2$.",
                   r"$\|g\|^2=\int_1^2\frac1{x^2}\,dx=\left[\ln x\right]_1^2=\ln2$.",
                   r"לכן $\left(\int_1^2\frac{f(x)}x\,dx\right)^2\le\frac12\int_1^2f^2(x)\,dx$."],
         "bugIndex": 3,
         "explain": r"הפונקציה הקדומה של $\frac1{x^2}$ היא $-\frac1x$ ולא $\ln x$, והערך הנכון הוא $\frac12$."},
    ],
    stepsSource="ai-draft")

add(2, "א",
    rubric=rub((r"בדיקה ש-$(1,1)$ אינו מתאפס ושייך ל-$G$", 1),
               (r"$(1,1)\cdot(a,b)=(a,b)$", 1),
               (r"מסקנה: $(1,1)$ הוא האיבר הניטרלי", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לבחור $(0,0)$ כמו בחיבור; הוא אינו ב-$G$ כי $0\notin\mathbb{Z}_5^*$."],
    steps=[
        ch(r"מהו האיבר הניטרלי של $G$ (הכפל מוגדר ברכיבים)?", r"$(1,1)$", [r"$(0,0)$", r"$(4,6)$", r"$(2,3)$"],
           r"ברכיבים הניטרלי הוא $1$ בכל קואורדינטה. $(0,0)$ אינו ב-$G$, ו-$(4,6)$ ו-$(2,3)$ משנים את הערכים.", 1),
        nm(r"מהו הרכיב הראשון (מודולו 5) של $(4,6)\cdot(2,3)$? הוא מראה ש-$(4,6)$ אינו ניטרלי.", 3,
           r"$4\cdot2=8\equiv3\pmod5$, ולא $2$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ב",
    rubric=rub((r"מציאת ההופכי של $2$ מודולו $5$: $3$", 1),
               (r"מציאת ההופכי של $3$ מודולו $7$: $5$", 1),
               (r"הרכבת הזוג $(3,5)$", 1),
               (r"בדיקה: $(2,3)\cdot(3,5)=(1,1)$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לחשב הופכי מודולו 7 עבור הרכיב הראשון, או מודולו 5 עבור השני.",
              r"לרשום $\left(\frac12,\frac13\right)$ במקום מספרים שלמים מודולו 5 ו-7."],
    steps=[
        nm(r"מהו ההופכי של $2$ ב-$\mathbb{Z}_5^*$ (בטווח $1$ עד $4$)?", 3, r"$2\cdot3=6\equiv1\pmod5$.", 0),
        nm(r"מהו ההופכי של $3$ ב-$\mathbb{Z}_7^*$ (בטווח $1$ עד $6$)?", 5, r"$3\cdot5=15\equiv1\pmod7$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ג",
    rubric=rub((r"$|\mathbb{Z}_5^*|=4$", 2), (r"$|\mathbb{Z}_7^*|=6$", 2), (r"עקרון הכפל: $|G|=4\cdot6=24$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לספור $5\cdot7=35$ ולשכוח שהאפס אינו ב-$\mathbb{Z}_n^*$.",
              r"לחבר את הסדרים במקום להכפיל: $4+6=10$."],
    steps=[
        nm(r"כמה איברים יש ב-$\mathbb{Z}_5^*$?", 4, r"$\{1,2,3,4\}$.", 0),
        nm(r"כמה איברים יש ב-$\mathbb{Z}_7^*$?", 6, r"$\{1,2,3,4,5,6\}$.", 0),
        nm(r"מהו $|G|$?", 24, r"$4\cdot6=24$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ד",
    rubric=rub((r"הסדר של $2$ ב-$\mathbb{Z}_5^*$ הוא $4$", 2),
               (r"הסדר של $3$ ב-$\mathbb{Z}_7^*$ הוא $6$", 2),
               (r"הסדר של הזוג הוא ה-$\mathrm{lcm}$ שלהם: $12$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לקחת את המכפלה $4\cdot6=24$ במקום המכפלה המשותפת המינימלית.",
              r"לקחת את המקסימום $6$ במקום ה-$\mathrm{lcm}$."],
    steps=[
        nm(r"מהו הסדר של $2$ ב-$\mathbb{Z}_5^*$?", 4, r"$2,4,3,1$: החזקה הראשונה ששווה ל-$1$ היא $2^4$.", 0),
        nm(r"מהו הסדר של $3$ ב-$\mathbb{Z}_7^*$?", 6, r"$3,2,6,4,5,1$: החזקה הראשונה ששווה ל-$1$ היא $3^6$.", 0),
        nm(r"מהו הסדר של $(2,3)$ ב-$G$?", 12, r"$\mathrm{lcm}(4,6)=12$.", 0),
    ],
    stepsSource="ai-draft")

add(2, "ה",
    rubric=rub((r"הסימטריה: $(-A-B^TB)^T=-A-B^TB$", 1),
               (r"פתיחת התבנית הריבועית: $-\vec v^TA\vec v-\vec v^TB^TB\vec v$", 1),
               (r"$\vec v^TB^TB\vec v=\|B\vec v\|^2\ge0$", 1),
               (r"$\vec v^TA\vec v\ge0$ ולכן הסכום $\le0$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לבדוק רק את הסימטריה ולא את סימן התבנית הריבועית.",
              r"לשכוח את הסימן המינוס, כלומר להראות ש-$A+B^TB$ חיובית ולא ש-$-A-B^TB$ שלילית."],
    steps=[
        nm(r"נבדוק על $A=I_2$, $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ ו-$\vec v=(1,2)^T$. מהו $\vec v^T(-A-B^TB)\vec v$?", -18,
           r"$-\vec v^TA\vec v=-5$ ו-$-\|B\vec v\|^2=-\|(3,2)\|^2=-13$, בסך הכול $-18\le0$.", 0),
        {"type": "findbug", "prompt": "בהוכחה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"$(-A-B^TB)^T=-A^T-(B^TB)^T=-A-B^TB$.",
                   r"$\vec v^T(-A-B^TB)\vec v=-(\vec v^TA\vec v)-(\vec v^TB^TB\vec v)$.",
                   r"$\vec v^TB^TB\vec v=\|B\vec v\|^2$.",
                   r"$A$ מוגדרת חיובית, ולכן $\vec v^TA\vec v\le0$.",
                   r"לכן $\vec v^T(-A-B^TB)\vec v\le0$."],
         "bugIndex": 3,
         "explain": r"$A$ מוגדרת חיובית ולכן $\vec v^TA\vec v\ge0$ (לא $\le0$)."},
    ],
    stepsSource="ai-draft")

add(2, "ו",
    rubric=rub((r"פירוק $\vec v^T\left(B^TAB\right)\vec v=\left(\vec v^TB^T\right)A(B\vec v)$", 1),
               (r"זיהוי $\left(\vec v^TB^T\right)=(B\vec v)^T$", 1),
               (r"$A$ מוגדרת חיובית ולכן $(B\vec v)^TA(B\vec v)\ge0$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"להשתמש בכך ש-$B$ הפיכה; היא לא נתונה, וההוכחה אינה זקוקה לכך.",
              r"לשכוח את $(B\vec v)^T=\vec v^TB^T$ ולחשב $B\vec v\,A\,B\vec v$."],
    steps=[
        ch(r"באיזו עובדה משתמשים כדי להסיק ש-$(B\vec v)^TA(B\vec v)\ge0$?",
           r"$A$ מוגדרת חיובית, והעובדה חלה על הוקטור $B\vec v$",
           [r"$B$ הפיכה", r"$A$ סימטרית בלבד", r"$B^TB=I$"],
           r"הטענה $\vec w^TA\vec w\ge0$ נכונה לכל $\vec w$, ובפרט $\vec w=B\vec v$. סימטריה לבדה אינה מבטיחה סימן, ו-$B$ אינה נתונה כהפיכה או כאורתוגונלית.", 0),
        nm(r"נבדוק על $A=\begin{pmatrix}2&0\\0&1\end{pmatrix}$, $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ ו-$\vec v=(1,-1)^T$. מהו $\vec v^TB^TAB\vec v$?", 1,
           r"$B\vec v=(0,-1)^T$ ו-$(0,-1)A(0,-1)^T=1\ge0$.", 0),
        {"type": "order", "prompt": "סדרו את שלבי ההוכחה.",
         "lines": [r"$\vec v^T\left(B^TAB\right)\vec v=\left(\vec v^TB^T\right)A\left(B\vec v\right)$.",
                   r"$\left(\vec v^TB^T\right)=(B\vec v)^T$, ולכן הביטוי שווה ל-$(B\vec v)^TA(B\vec v)$.",
                   r"$A$ מוגדרת חיובית, ולכן $(B\vec v)^TA(B\vec v)\ge0$."],
         "explain": "קודם מקבצים את המכפלה, אחר כך מזהים את הוקטור $B\\vec v$, ורק אז מפעילים את החיוביות של $A$."},
    ],
    stepsSource="ai-draft")

add(3, "א",
    rubric=rub((r"חישוב הדטרמיננטה ופירוקה: $(a-\lambda)\left(\lambda^2-2\lambda a^2+a^4-1\right)$", 6),
               (r"הערכים העצמיים $a,\ a^2+1,\ a^2-1$", 3),
               (r"מוגדרת חיובית כאשר $a\ge1$, ומוגדרת חיובית לחלוטין כאשר $a>1$", 4),
               (r"אין ערך $a$ למטריצה מוגדרת שלילית, ובשאר המקרים אינה מוגדרת", 4)),
    rubricSource="ai-draft",
    pitfalls=[r"לשכוח שהאי-שוויון $a^2\ge1$ נותן גם $a\le-1$, ולהוציא את זה בעזרת התנאי $a\ge0$.",
              r"לבלבל בין מוגדרת חיובית (ערכים עצמיים $\ge0$) למוגדרת חיובית לחלוטין (ערכים עצמיים $>0$).",
              "לקבוע אי-הגדרה בלי לבדוק את כל הערכים העצמיים."],
    steps=[
        ch(r"מהם הערכים העצמיים של המטריצה $\begin{pmatrix}a^2&0&1\\0&a&0\\1&0&a^2\end{pmatrix}$?",
           r"$a,\ a^2+1,\ a^2-1$",
           [r"$a,\ a^2+2,\ a^2-2$", r"$a^2,\ a+1,\ a-1$", r"$a,\ 2a^2,\ 0$"],
           r"המטריצה פוצלה לבלוק $\begin{pmatrix}a^2&1\\1&a^2\end{pmatrix}$ עם ערכים עצמיים $a^2\pm1$, ועוד הערך $a$. בבדיקה ב-$a=2$ מתקבלים $2,5,3$, ורק האפשרות הראשונה נותנת אותם.", 0),
        ch(r"לפי מינוח הקורס (מוגדרת חיובית אם כל הערכים העצמיים $\ge0$), עבור אילו $a$ המטריצה מוגדרת חיובית?",
           r"$a\ge1$", [r"$a>1$", r"$a\ge0$", r"$a\le-1$ או $a\ge1$"],
           r"נדרש $a\ge0$ וגם $a^2\ge1$, כלומר $a\ge1$. ב-$a=1$ הערכים הם $1,2,0$ ולכן עדיין חיובית; ב-$a=-1$ אחד הערכים הוא $-1$.", 0),
        nm(r"כמה ערכים עצמיים שווים ל-$0$ כאשר $a=1$?", 1, r"הערכים הם $1,\ 2,\ 0$, ולכן בדיוק אחד, ומכאן שהמטריצה אינה חיובית לחלוטין ב-$a=1$.", 0),
        ch(r"עבור אילו $a$ המטריצה מוגדרת שלילית (כל הערכים העצמיים $\le0$)?",
           r"אף ערך של $a$", [r"$a\le0$", r"$a\le-1$", r"$-1\le a\le0$"],
           r"הערך $a^2+1$ תמיד חיובי, ולכן אי אפשר שכולם $\le0$. למשל ב-$a=0$ הערכים הם $0,1,-1$.", 1),
    ],
    stepsSource="ai-draft")

add(3, "ב",
    rubric=rub((r"סימון $m=60$ וחישוב $M_1=15,\ M_2=20,\ M_3=12$", 2),
               (r"חישוב ההופכיים $x_1=3,\ x_2=2,\ x_3=3$", 3),
               (r"הצבה בנוסחה וקבלת הסכום $359$", 2),
               (r"הקטנה מודולו $60$: $x\equiv59$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לחשב את ההופכי מודולו $m$ במקום מודולו $m_i$.",
              "לשכוח להקטין את $359$ מודולו $60$.",
              r"לבלבל בין שאריות ל-$q_i$ והמודולים $m_i$ בנוסחה."],
    steps=[
        nm(r"מהו $x_1$ שמקיים $15x_1\equiv1\pmod4$ (בטווח $0$ עד $3$)?", 3, r"$15\equiv3\pmod4$ ו-$3\cdot3=9\equiv1$.", 0),
        nm(r"מהו $x_2$ שמקיים $20x_2\equiv1\pmod3$ (בטווח $0$ עד $2$)?", 2, r"$20\equiv2\pmod3$ ו-$2\cdot2=4\equiv1$.", 0),
        nm(r"מהו הסכום $3\cdot15\cdot x_1+2\cdot20\cdot x_2+4\cdot12\cdot x_3$ עם $x_3=3$?", 359,
           r"$135+80+144=359$.", 0),
        nm(r"מהו הפתרון $x$ בטווח $0$ עד $59$?", 59, r"$359=5\cdot60+59$.", 0),
    ],
    stepsSource="ai-draft")

add(4, "א",
    rubric=rub((r"פולינום אופייני $-\lambda(\lambda-5)^2$ והערכים העצמיים $0,5,5$", 4),
               (r"וקטור עצמי $(0,-1,2)$ עבור $\lambda=0$", 3),
               (r"וקטורים עצמיים $(0,2,1),\ (1,0,0)$ עבור $\lambda=5$", 3),
               (r"בדיקת אורתוגונליות ונרמול", 3),
               (r"כתיבת $Q$ אורתוגונלית ו-$D$ אלכסונית עם $A=QDQ^T$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לרשום את $D$ בסדר $5,5,0$ כשהעמודה הראשונה של $Q$ שייכת ל-$\lambda=0$.",
              "לשכוח לנרמל את העמודות של $Q$.",
              r"בניית $\vec v_2$ בלי לבדוק שהוא ניצב ל-$\vec v_1$ (המכפלה $(0,-1,2)\cdot(0,2,1)=0$)."],
    steps=[
        nm(r"מהו $\det A$ עבור $A=\begin{pmatrix}5&0&0\\0&4&2\\0&2&1\end{pmatrix}$ (המכפלה של הערכים העצמיים)?", 0,
           r"$5\cdot(4\cdot1-2\cdot2)=0$, ולכן $0$ הוא ערך עצמי.", 0),
        nm(r"מהו המימד של המרחב העצמי של $\lambda=5$?", 2,
           r"$A-5I$ היא ברמה $1$ (שורות $(0,-1,2)$ ו-$(0,2,-4)$ תלויות), ולכן הגרעין ממימד $2$.", 0),
        nm(r"מהי המכפלה הפנימית $\langle(0,-1,2),(0,2,1)\rangle$?", 0,
           r"$0-2+2=0$, ולכן הוקטורים העצמיים של $0$ ושל $5$ ניצבים זה לזה.", 0),
        nm(r"מהו הרכיב השלישי של $\vec v_1=(0,-1,2)$ אחרי נרמול?", 0.894427,
           r"$\|\vec v_1\|=\sqrt5$ ולכן $\frac2{\sqrt5}\approx0.894$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(4, "ב",
    rubric=rub((r"הנתון $x^2=1$ לכל $x$, כלומר $x=x^{-1}$", 1),
               (r"$xy=(xy)^{-1}$", 1),
               (r"$(xy)^{-1}=y^{-1}x^{-1}$", 2),
               (r"$y^{-1}x^{-1}=yx$ ולכן $xy=yx$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לכתוב $(xy)^{-1}=x^{-1}y^{-1}$; זה נכון רק בחבורה אבלית, שהיא מה שרוצים להוכיח.",
              "להניח קומוטטיביות ישירות במקום להסיק אותה."],
    steps=[
        ch(r"איזו זהות נכונה בכל חבורה ומשמשת בהוכחה?", r"$(xy)^{-1}=y^{-1}x^{-1}$",
           [r"$(xy)^{-1}=x^{-1}y^{-1}$", r"$(xy)^2=x^2y^2$", r"$xy=yx$"],
           r"רק הזהות הראשונה נכונה בכל חבורה. בחבורת התמורות $S_3$ שלוש האחרות נכשלות על זוג איברים מתאים.", 0),
        {"type": "order", "prompt": "סדרו את שלבי ההוכחה ש-$xy=yx$.",
         "lines": [r"$xy=(xy)^{-1}$, כי כל איבר הפוך לעצמו.",
                   r"$(xy)^{-1}=y^{-1}x^{-1}$, כי זו זהות בכל חבורה.",
                   r"$y^{-1}x^{-1}=yx$, כי $y^{-1}=y$ ו-$x^{-1}=x$."],
         "explain": "השוויון הראשון מחליף את המכפלה בהופכי שלה, השני פותח את ההופכי, והשלישי משתמש שוב בנתון."},
    ],
    stepsSource="ai-draft")

add(4, "ג",
    rubric=rub((r"מהנתון $x^2=1$ ו-$y^2=1$", 1),
               (r"$x^3=x\cdot x^2=x$", 2),
               (r"$y^5=y\cdot y^2\cdot y^2=y$", 1),
               (r"מ-$x^3=y^5$ מקבלים $x=y$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"להשתמש ב-$x^3=x^{-1}$ ולהיתקע; יש לצמצם את החזקה בעזרת $x^2=1$.",
              r"לצמצם את $y^5$ ל-$y^3$ במקום ל-$y$, כלומר לצמצם רק חזקה אחת של $y^2$."],
    steps=[
        ch(r"מה שווה $x^3$ בחבורה שבה $x^2=1$ לכל איבר?", r"$x$", [r"$1$", r"$x^2$"],
           r"$x^3=x\cdot x^2=x\cdot1=x$. האפשרויות האחרות שוות ל-$1$ (כי $x^2=1$), ואין זה נכון ש-$x=1$ בכל איבר.", 0),
        ch(r"מה שווה $y^5$ באותה חבורה?", r"$y$", [r"$1$", r"$y^2$"],
           r"$y^5=y\cdot y^2\cdot y^2=y$. הערכים $1$ ו-$y^2$ שווים זה לזה (כי $y^2=1$), אך $y$ אינו בהכרח $1$.", 1),
        nm(r"נכתוב $y^5=y^k$ עם $k\in\{0,1\}$ בעזרת $y^2=1$. מהו $k$?", 1,
           r"$5$ הוא אי-זוגי, ולכן $y^5=y^4\cdot y=y$.", 0),
    ],
    stepsSource="ai-draft")

add(5, "א",
    rubric=rub((r"אורתונורמליזציה של $\vec a_1=(-1,1)^T$: $\vec q_1=\frac1{\sqrt2}(-1,1)^T$", 4),
               (r"הוקטור $\vec a_2-\langle\vec a_2,\vec q_1\rangle\vec q_1=(4,4)^T$ ונרמולו $\vec q_2=\frac1{\sqrt2}(1,1)^T$", 4),
               (r"כתיבת $Q$ מהעמודות $\vec q_1,\vec q_2$", 2),
               (r"חישוב $R=Q^TA=\begin{pmatrix}\sqrt2&\sqrt2\\0&4\sqrt2\end{pmatrix}$", 3),
               (r"בדיקה $QR=A$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לפרק לפי השורות של $A$ במקום לפי העמודות.",
              r"לשכוח שהאלכסון של $R$ חיובי: $r_{11}=\|\vec a_1\|=\sqrt2$.",
              r"לחשב $R=QA$ במקום $R=Q^TA$."],
    steps=[
        nm(r"מהו $r_{11}=\|\vec a_1\|$ עבור העמודה הראשונה $(-1,1)^T$?", 1.414214, r"$\sqrt{1+1}=\sqrt2$.", 0.0005),
        nm(r"מהו $r_{12}=\langle\vec q_1,\vec a_2\rangle$ עבור $\vec q_1=\frac1{\sqrt2}(-1,1)^T$ ו-$\vec a_2=(3,5)^T$?", 1.414214,
           r"$\frac{-3+5}{\sqrt2}=\sqrt2$.", 0.0005),
        nm(r"מהו $r_{22}=\|\vec a_2-r_{12}\vec q_1\|$?", 5.656854,
           r"$\vec a_2-r_{12}\vec q_1=(3,5)-(-1,1)=(4,4)$, ונורמתו $4\sqrt2\approx5.657$.", 0.0005),
        nm(r"מהו הרכיב הראשון של $\vec q_2=\frac{(4,4)^T}{r_{22}}$?", 0.707107, r"$\frac4{4\sqrt2}=\frac{\sqrt2}2$.", 0.0005),
    ],
    stepsSource="ai-draft")

add(5, "ב",
    rubric=rub((r"סימטריה: $P^T=(\vec v\vec v^T)^T=P$", 1),
               (r"$P^2=\vec v\left(\vec v^T\vec v\right)\vec v^T=P$ כי $\vec v^T\vec v=1$", 2),
               (r"$\vec u^TP\vec u=\left(\vec v^T\vec u\right)^T\left(\vec v^T\vec u\right)\ge0$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לשכוח את $\vec v^T\vec v=\|\vec v\|^2=1$, התנאי שגורר $P^2=P$.",
              r"לבלבל בין $\vec v\vec v^T$ (מטריצה $n\times n$) ל-$\vec v^T\vec v$ (מספר)."],
    steps=[
        nm(r"עבור $\vec v=(0.6,0.8)^T$, מהו האיבר בשורה 1 ועמודה 2 של $P=\vec v\vec v^T$?", 0.48, r"$0.6\cdot0.8=0.48$.", 0.0005),
        nm(r"עבור אותו $\vec v$, מהו העקבה (סכום האלכסון) של $P$?", 1, r"$0.36+0.64=1=\|\vec v\|^2$.", 0.0005),
        {"type": "findbug", "prompt": "בהוכחה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"$P^T=\left(\vec v\vec v^T\right)^T=\vec v\vec v^T=P$.",
                   r"$P^2=\vec v\left(\vec v^T\vec v\right)\vec v^T$.",
                   r"$\vec v^T\vec v=\|\vec v\|^2=0$.",
                   r"לכן $P^2=P$.",
                   r"$\vec u^TP\vec u=\left(\vec v^T\vec u\right)^T\left(\vec v^T\vec u\right)\ge0$."],
         "bugIndex": 2,
         "explain": r"$\vec v$ וקטור יחידה, ולכן $\vec v^T\vec v=1$; עם $0$ היה מתקבל $P^2=0$."},
    ],
    stepsSource="ai-draft")

add(5, "ג",
    rubric=rub((r"$\langle\vec u-P\vec u,\vec v\rangle=\vec v^T(\vec u-P\vec u)$", 1),
               (r"פתיחה: $\vec v^T\vec u-\vec v^TP\vec u$", 1),
               (r"$\vec v^TP=\vec v^T\vec v\,\vec v^T=\vec v^T$ כי $\|\vec v\|=1$", 2),
               (r"התוצאה $0$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לשכוח ש-$\vec v^T\vec v=1$ ולהישאר עם $\vec v^T\vec v\,\vec v^T\vec u$.",
              r"להחליף את סדר המכפלה ולחשב $P\vec v$ במקום $\vec v^TP$."],
    steps=[
        nm(r"נבדוק על $\vec v=(0.6,0.8)^T$ ו-$\vec u=(1,2)^T$. מהו הרכיב הראשון של $\vec u-P\vec u$?", -0.32,
           r"$\vec v^T\vec u=2.2$, ולכן $P\vec u=2.2\vec v=(1.32,1.76)$ ו-$\vec u-P\vec u=(-0.32,0.24)$. המכפלה עם $\vec v$: $-0.192+0.192=0$.", 0.0005),
        {"type": "order", "prompt": "סדרו את שלבי החישוב.",
         "lines": [r"$\langle\vec u-P\vec u,\vec v\rangle=\vec v^T\left(\vec u-P\vec u\right)$.",
                   r"$=\vec v^T\vec u-\vec v^TP\vec u$.",
                   r"$=\vec v^T\vec u-\vec v^T\vec v\,\vec v^T\vec u=\vec v^T\vec u-\vec v^T\vec u$, כי $\vec v^T\vec v=1$.",
                   r"$=0$."],
         "explain": "כל שורה נובעת מהקודמת: כתיבת המכפלה הפנימית, פתיחה, הצבת $P=\\vec v\\vec v^T$ עם $\\|\\vec v\\|=1$, ותוצאה."},
    ],
    stepsSource="ai-draft")

exam = {
    "examCode": "23B-B",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ג מועד ב'",
    "year": 2023,
    "examDate": "13.7.2023",
    "sourceFile": "algebra-2-23B-B-exam",
    "solutionFile": "algebra-2-23B-B-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
