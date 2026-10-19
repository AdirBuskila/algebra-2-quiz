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
