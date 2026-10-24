# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-B.json -- algebra-2 (20079), semester B 2025, moed B (7.08.2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25B-B.py

Source: exam 3 pp. (header misprints the semester as A; the date 07.08.25 and the file name make it semester B moed B)
+ handwritten solution 10 pp. (scan, read from the rendered pages). Sheet: 6 questions, "best 4", 25% each; all 6 are
transcribed, 17 items. Solutions are handwritten and carry no official typeset text, so solutionSource is
"student-solution" (unknown-author handwritten scan; not presented as the lecturer's) (the scan accompanying the exam; no author named).

Part letters: numbered sub-parts get letters in order (Q2: 1,2,3 -> a,b,c and printed b -> d; Q3 likewise).
Every question text starts with its printed label.

Slips in intermediate lines of the handwritten solution (fixed silently, logged in docs/ASK_ADIR.md; no final answer changes):
- Q3a.3: the identity equation is printed "(a-1)e = a"; a (x) e = a gives ae-a-e = a, i.e. e(a-1) = 2a. At a = 1 it reads 0 = 2
  (printed 0 = 1). Same conclusion (written correctly).
- Q5a: the range is printed with the letter lambda ("-1/sqrt2 <= lambda <= 1/sqrt2") but the parameter is c (written with c).
- Q1a: the official gives decimals m ~ 0.627, n ~ 1.678; exact values 37/59 and 99/59 are added.
Checks: tools/verify/25B-B/check.py (sympy + brute force), all OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"תהי $H=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb{Z}_5)\ \middle|\ a,b,c,d\neq0\right\}$. לכל $X=\begin{pmatrix}a&b\\c&d\end{pmatrix},\ Y=\begin{pmatrix}p&q\\s&t\end{pmatrix}\in H$ נגדיר את פעולת הכפל (Hadamard Product) רכיב-רכיב: $X\odot Y=\begin{pmatrix}ap&bq\\cs&dt\end{pmatrix}$. כמובן שכפל הרכיבים הוא מודולו 5."},
    "c3": {"kind": "text", "title": "שאלה 3 סעיף א",
           "text": r"לכל $a,b\in\mathbb{Z}$ נגדיר פעולה: $a\otimes b=ab-a-b$."},
}

S1A = (
    r"$$A=\begin{pmatrix}0&1\\2&1\\6&1\\10&1\end{pmatrix},\qquad \vec b=\begin{pmatrix}1\\4\\5\\8\end{pmatrix},\qquad A^TA\begin{pmatrix}m\\n\end{pmatrix}=A^T\vec b$$" "\n"
    r"$$\begin{pmatrix}140&18\\18&4\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}118\\18\end{pmatrix}\ \to\ \begin{pmatrix}70&9\\9&2\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}59\\9\end{pmatrix}$$" "\n"
    r"$$m=\frac{37}{59}\approx0.627,\qquad n=\frac{99}{59}\approx1.678$$" "\n"
    r"הישר: $y=\frac{37}{59}x+\frac{99}{59}\approx0.627x+1.678$"
)

S1B = (
    r"המטריצה $S^TAS$ סימטרית. לכל $\vec v\in\mathbb{R}^n$ מתקיים:" "\n"
    r"$$\langle S^TAS\vec v,\vec v\rangle\ge0\iff\vec v^TS^TAS\vec v\ge0\iff(S\vec v)^TA(S\vec v)\ge0\iff\vec u^TA\vec u\ge0$$" "\n"
    r"לכל $\vec u\in\mathbb{R}^n$, מכיוון ש-$S$ אורתוגונלית ולכן הפיכה (כל $\vec u$ הוא מהצורה $S\vec v$)." "\n"
    r"לכן $A$ מוגדרת חיובית אם ורק אם $S^TAS$ מוגדרת חיובית." "\n"
    "**דרך נוספת:** מכיוון ש-$A$ ו-$S^TAS=S^{-1}AS$ מטריצות דומות, יש להן בדיוק אותם ערכים עצמיים. לכן שתי המטריצות מוגדרות חיובית כאשר כל הערכים העצמיים שלהן אי-שליליים."
)

S2A1 = (
    r"**סגירות:** הכפל הוא מודולו 5 ו-$\mathbb{Z}_5^*$ סגורה לכפל, לכן $H$ סגורה ביחס לפעולה $\odot$." "\n"
    r"**אסוציאטיביות:** הפעולה $\odot$ אסוציאטיבית כי הכפל ב-$\mathbb{Z}_5^*$ אסוציאטיבי (הפעולה פועלת רכיב-רכיב)." "\n"
    r"**איבר ניטרלי:** $E=\begin{pmatrix}1&1\\1&1\end{pmatrix}\in H$." "\n"
    r"**איבר הופכי:** לכל $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ קיים איבר הופכי כי $a,b,c,d$ הפיכים ב-$\mathbb{Z}_5^*$ (ההופכי הוא המטריצה של ההופכיים של הרכיבים)."
)

S2A2 = (
    r"תהי $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ מטריצה מ-$H$. לכל רכיב יש בדיוק 4 ערכים אפשריים: $1,2,3,4$. לפי עקרון הכפל, הסדר של $H$ הוא" "\n"
    r"$$|H|=4^4=256$$"
)

S2A3 = (
    r"מתקיים $o(1)=1,\ o(2)=4,\ o(3)=4$ (בכפל מודולו 5, והפעולה רכיב-רכיב). לכן" "\n"
    r"$$o\left(\begin{pmatrix}1&2\\2&3\end{pmatrix}\right)=4$$"
)

S2B = (
    r"נגדיר ב-$\mathbb{R}^n$ שני וקטורים: $\bar u=\begin{pmatrix}a_1\\\vdots\\a_n\end{pmatrix}$ , $\bar v=\begin{pmatrix}1\\\vdots\\1\end{pmatrix}$." "\n"
    r"אז $|\langle\bar u,\bar v\rangle|^2=(a_1+\dots+a_n)^2$ , $\ \|\bar u\|^2=a_1^2+\dots+a_n^2$ , $\ \|\bar v\|^2=1^2+\dots+1^2=n$." "\n"
    r"לפי אי-שוויון קושי-שוורץ נקבל:" "\n"
    r"$$|\langle\bar u,\bar v\rangle|^2\le\|\bar u\|^2\cdot\|\bar v\|^2\ \Rightarrow\ (a_1+\dots+a_n)^2\le n\left(a_1^2+\dots+a_n^2\right)$$"
)

S3A1 = r"לכל $a,b\in\mathbb{Z}$ מתקיים $a\cdot b-a-b\in\mathbb{Z}$, לכן $\otimes$ פעולה בינארית על $\mathbb{Z}$."

S3A2 = (
    r"$$(a\otimes b)\otimes c=(ab-a-b)\otimes c=abc-ac-bc-ab+a+b-c$$" "\n"
    r"$$a\otimes(b\otimes c)=a\otimes(bc-b-c)=abc-ab-ac-a-bc+b+c$$" "\n"
    r"הביטויים שונים (למשל המקדם של $a$ הוא $+1$ בראשון ו-$-1$ בשני). הפעולה אינה אסוציאטיבית."
)

S3A3 = (
    r"נניח שקיים $e\in\mathbb{Z}$ כך שלכל $a\in\mathbb{Z}$ מתקיים $a\otimes e=a$. נקבל:" "\n"
    r"$$a\otimes e=ae-a-e=a\ \Rightarrow\ e(a-1)=2a\quad\forall a\in\mathbb{Z}$$" "\n"
    r"עבור $a=1$ נקבל $0=2$, סתירה. ב-$(\mathbb{Z},\otimes)$ לא קיים איבר ניטרלי."
)

S3A4 = r"מהסעיפים הקודמים נובע ש-$(\mathbb{Z},\otimes)$ אינה חבורה (הפעולה אינה אסוציאטיבית ואין איבר ניטרלי)."

S3B = (
    r"נסתכל בשני הווקטורים $\bar u+\bar v$ , $\bar u-\bar v$. מתקיים:" "\n"
    r"$$A(\bar u+\bar v)=\left(\bar v\bar u^T+\bar u\bar v^T\right)(\bar u+\bar v)=\bar v\underbrace{\bar u^T\bar u}_{1}+\bar u\underbrace{\bar v^T\bar u}_{0}+\bar v\underbrace{\bar u^T\bar v}_{0}+\bar u\underbrace{\bar v^T\bar v}_{1}=\bar v+\bar u$$" "\n"
    r"כלומר $A(\bar u+\bar v)=1\cdot(\bar u+\bar v)$, ולכן $\lambda=1$ הוא ערך עצמי של $A$." "\n"
    r"באופן דומה:" "\n"
    r"$$A(\bar u-\bar v)=\bar v\underbrace{\bar u^T\bar u}_{1}+\bar u\underbrace{\bar v^T\bar u}_{0}-\bar v\underbrace{\bar u^T\bar v}_{0}-\bar u\underbrace{\bar v^T\bar v}_{1}=\bar v-\bar u$$" "\n"
    r"כלומר $A(\bar u-\bar v)=-1\cdot(\bar u-\bar v)$, ולכן $\lambda=-1$ הוא גם ערך עצמי של $A$." "\n"
    r"$A$ מטריצה מסדר $2\times2$, לכן אין לה יותר ערכים עצמיים." "\n"
    r"**תשובה:** $\lambda=1,\ -1$"
)

S4A = (
    r"$$Q=\begin{pmatrix}\frac{\sqrt2}{2}&\frac{\sqrt6}{6}&-\frac{\sqrt3}{3}\\\frac{\sqrt2}{2}&-\frac{\sqrt6}{6}&\frac{\sqrt3}{3}\\0&\frac{\sqrt6}{3}&\frac{\sqrt3}{3}\end{pmatrix},\qquad R=\begin{pmatrix}\sqrt2&\frac{\sqrt2}{2}&\frac{\sqrt2}{2}\\0&\frac{\sqrt6}{2}&\frac{\sqrt6}{6}\\0&0&\frac{2\sqrt3}{3}\end{pmatrix}$$"
)

S4B = (
    r"$$\begin{cases}3x\equiv4\pmod5\\2x\equiv3\pmod7\\x\equiv7\pmod{32}\end{cases}\iff\begin{cases}x\equiv3\pmod5\\x\equiv5\pmod7\\x\equiv7\pmod{32}\end{cases}$$" "\n"
    r"$$x\equiv103\pmod{1120}$$"
)

S5A = (
    r"הערכים העצמיים: $\lambda_1=1\ ,\ \ \lambda_2=1+\sqrt2\,c\ ,\ \ \lambda_3=1-\sqrt2\,c$." "\n"
    r"מכיוון ש-$\lambda_1=1$, לא קיים $c$ שעבורו המטריצה מוגדרת שלילית, בפרט לחלוטין." "\n"
    r"נבדוק מתי היא מוגדרת חיובית:" "\n"
    r"$$\begin{cases}1\ge0\\1+\sqrt2\,c\ge0\\1-\sqrt2\,c\ge0\end{cases}\Rightarrow\begin{cases}c\ge-\frac1{\sqrt2}\\c\le\frac1{\sqrt2}\end{cases}$$" "\n"
    r"**תשובה סופית:**" "\n"
    r"מוגדרת חיובית: $-\dfrac1{\sqrt2}\le c\le\dfrac1{\sqrt2}$" "\n"
    r"מוגדרת חיובית לחלוטין: $-\dfrac1{\sqrt2}<c<\dfrac1{\sqrt2}$" "\n"
    "מוגדרת שלילית ומוגדרת שלילית לחלוטין: לא קיים $c$\n"
    "לשאר הערכים המטריצה אינה מוגדרת (אף אחת מהן)."
)

S5B = (
    "**סגירות:** יהיו $x,y\\in H\\cap K$. אז $x,y\\in H$ וגם $x,y\\in K$. מכיוון ש-$H$ ו-$K$ תת-חבורות, $x*y\\in H$ וגם $x*y\\in K$, כלומר $x*y\\in H\\cap K$.\n"
    r"**אסוציאטיביות:** נובעת מהאסוציאטיביות של $*$ ב-$G$." "\n"
    r"**איבר ניטרלי:** יהי $e$ האיבר הניטרלי של $G$. מכיוון ש-$H$ ו-$K$ תת-חבורות, $e\in H$ וגם $e\in K$. לכן $e\in H\cap K$." "\n"
    r"**איבר הופכי:** יהי $x\in H\cap K$, כלומר $x\in H$ וגם $x\in K$. מכיוון ש-$H$ ו-$K$ תת-חבורות, $x^{-1}\in H$ וגם $x^{-1}\in K$. הוכחנו ש-$x^{-1}\in H\cap K$." "\n"
    "מש\"ל"
)

S6A = (
    r"הערכים העצמיים: $\lambda_1=5,\ \lambda_2=2,\ \lambda_3=-1$." "\n"
    r"$A=QDQ^T$ כאשר" "\n"
    r"$$D=\begin{pmatrix}5&0&0\\0&2&0\\0&0&-1\end{pmatrix},\qquad Q=\begin{pmatrix}\frac23&-\frac23&\frac13\\\frac23&\frac13&-\frac23\\\frac13&\frac23&\frac23\end{pmatrix}$$"
)

S6B = (
    r"$$\|\bar u+\bar v\|^2=\langle\bar u+\bar v,\bar u+\bar v\rangle=\|\bar u\|^2+2\langle\bar u,\bar v\rangle+\|\bar v\|^2$$" "\n"
    r"$$\|\bar u-\bar v\|^2=\|\bar u\|^2-2\langle\bar u,\bar v\rangle+\|\bar v\|^2$$" "\n"
    r"$$\|\bar u+\bar v\|^2+\|\bar u-\bar v\|^2=2\left(\|\bar u\|^2+\|\bar v\|^2\right)$$"
)

questions = [
    Q(1, "computation", "least_squares",
      r"(10%) נתונות 4 נקודות במישור: $(0,1),\ (2,4),\ (6,5),\ (10,8)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן של הריבועים הפחותים.",
      S1A, part="א", points=10),
    Q(1, "proof", "pos_def",
      r"(15%) תהיינה $A\in M_n(\mathbb{R})$ מטריצה סימטרית ו-$S\in M_n(\mathbb{R})$ מטריצה אורתוגונלית. הוכיחו כי $S^TAS$ מוגדרת חיובית אם ורק אם $A$ מוגדרת חיובית.",
      S1B, part="ב", points=15),

    Q(2, "proof", "groups", r"סעיף א.1. הוכיחו כי $(H,\odot)$ היא חבורה. (7%)", S2A1, part="א", points=7, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.2. מהו הסדר של $H$ ? (4%)", S2A2, part="ב", points=4, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.3. מצאו את הסדר של $\begin{pmatrix}1&2\\2&3\end{pmatrix}$ ? (4%)", S2A3, part="ג", points=4,
      contextId="c2"),
    Q(2, "proof", "cauchy_schwarz",
      r"סעיף ב. יהיו $a_1,a_2,\dots,a_n$ מספרים ממשיים. הוכיחו כי $(a_1+a_2+\dots+a_n)^2\le n\left(a_1^2+a_2^2+\dots+a_n^2\right)$. (10%)",
      S2B, part="ד", points=10),

    Q(3, "proof", "groups", r"סעיף א.1. הראו כי $\otimes$ היא פעולה בינארית על $\mathbb{Z}$. (3%)", S3A1, part="א", points=3, contextId="c3"),
    Q(3, "truefalse", "groups", r"סעיף א.2. האם הפעולה אסוציאטיבית? (4%)", S3A2, part="ב", points=4, contextId="c3", verdict=False),
    Q(3, "truefalse", "groups", r"סעיף א.3. האם במבנה $(\mathbb{Z},\otimes)$ קיים איבר ניטרלי? (4%)", S3A3, part="ג", points=4,
      contextId="c3", verdict=False),
    Q(3, "truefalse", "groups", r"סעיף א.4. האם $(\mathbb{Z},\otimes)$ זו חבורה? (4%)", S3A4, part="ד", points=4, contextId="c3",
      verdict=False),
    Q(3, "computation", "orthogonality",
      r"סעיף ב. יהי $\{\vec u,\vec v\}$ בסיס **אורתונורמלי** במרחב $\mathbb{R}^2$. נגדיר את המטריצה $A=\vec v\cdot\vec u^T+\vec u\cdot\vec v^T\in M_2(\mathbb{R})$. מצאו את הערכים העצמיים של $A$. (10%)",
      S3B, part="ה", points=10),

    Q(4, "computation", "qr", r"(15%) מצאו פירוק QR עבור המטריצה הבאה: $\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}$.", S4A, part="א", points=15),
    Q(4, "computation", "crt",
      r"(10%) פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}3x\equiv4\pmod5\\2x\equiv3\pmod7\\x\equiv7\pmod{32}\end{cases}$.",
      S4B, part="ב", points=10),

    Q(5, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $c$ המטריצה $\begin{pmatrix}1&c&0\\c&1&c\\0&c&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S5A, part="א", points=15),
    Q(5, "proof", "groups",
      r"(10%) תהי $(G,*)$ חבורה כלשהי ותהיינה $H$ ו-$K$ שתי תת-חבורות של $G$. הוכיחו כי $H\cap K$ היא גם תת-חבורה של $G$.",
      S5B, part="ב", points=10),

    Q(6, "computation", "orthodiag", r"(15%) בצעו לכסון אורתוגונלי למטריצה הבאה: $A=\begin{pmatrix}3&2&0\\2&2&2\\0&2&1\end{pmatrix}$.",
      S6A, part="א", points=15),
    Q(6, "proof", "cauchy_schwarz",
      r"(10%) הוכיחו כי בכל מרחב מכפלה פנימית $V$ מתקיים **כלל המקבילית**: $\|\vec u+\vec v\|^2+\|\vec u-\vec v\|^2=2\|\vec u\|^2+2\|\vec v\|^2$ לכל $\vec u,\vec v\in V$.",
      S6B, part="ב", points=10),
]

# ---------------------------------------------------------------------------------------------------------
# Phase 4 (step author): rubric / pitfalls / guided steps, all derived from the stored solutions above.
# Numeric values and factual claims are re-checked by tools/verify/25B-B/steps_check.py (sympy / brute force).
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


S25BB = {
    (1, "א"): dict(
        rubric=rub((r"הצבת $A$ ו-$\vec b$ (עמודת איקסים ועמודת אחדות)", 3),
                   (r"משוואות נורמליות $A^TA\binom mn=A^T\vec b$ וחישוב שני האגפים", 4),
                   (r"פתרון: $m=\frac{37}{59}$, $n=\frac{99}{59}$ והישר", 3)),
        pitfalls=[r"לפתור את $A\vec x=\vec b$ ישירות: ארבע הנקודות אינן על ישר אחד.",
                  r"לשכוח שהנקודה הראשונה היא $(0,1)$, כך שהאיבר $x=0$ תורם $0$ לסכומים."],
        steps=[
            ch("איזו מערכת פותרים בשיטת הריבועים הפחותים?", r"$A^TA\binom mn=A^T\vec b$",
               [r"$A\binom mn=\vec b$ (פתרון מדויק)", r"$AA^T\binom mn=\vec b$"],
               r"הפתרון כופל ב-$A^T$ משמאל. המערכת $A\vec x=\vec b$ אינה פתירה, ו-$AA^T$ היא מטריצה $4\times4$ ולא מתאימה.", 2),
            num(r"מהו האיבר הימני-העליון ב-$A^TA$, כלומר $\sum x_i^2$?", 140, r"$0+4+36+100=140$."),
            num(r"מהו האיבר הראשון ב-$A^T\vec b$, כלומר $\sum x_iy_i$?", 118, r"$0+8+30+80=118$."),
            num("מהו השיפוע $m$?", 0.6271186, r"$m=\frac{37}{59}\approx0.627$.", 0.001),
            num(r"מהו חיתוך הצירים $n$?", 1.6779661, r"$n=\frac{99}{59}\approx1.678$.", 0.001),
        ]),
    (1, "ב"): dict(
        rubric=rub((r"$S^TAS$ סימטרית", 2), (r"$\vec v^TS^TAS\vec v=(S\vec v)^TA(S\vec v)$ והשקילות לתנאי על $\vec u=S\vec v$", 7),
                   (r"כל $\vec u$ הוא מהצורה $S\vec v$ כי $S$ הפיכה", 4), ("מסקנה: אם ורק אם", 2)),
        pitfalls=[r"להוכיח רק כיוון אחד: צריך גם ש-$A$ חיובית גוררת ש-$S^TAS$ חיובית וגם להפך.",
                  r"לשכוח שיש להשתמש בהפיכות של $S$ כדי שה-$\vec u=S\vec v$ יעברו על כל $\mathbb{R}^n$."],
        steps=[
            order("סדרו את שלבי ההוכחה.",
                  [r"$\langle S^TAS\vec v,\vec v\rangle=\vec v^TS^TAS\vec v$",
                   r"$=(S\vec v)^TA(S\vec v)$",
                   r"$S$ הפיכה, ולכן $\vec u=S\vec v$ עובר על כל $\mathbb{R}^n$",
                   r"$S^TAS$ חיובית $\iff$ $\vec u^TA\vec u\ge0$ לכל $\vec u$ $\iff$ $A$ חיובית"],
                  "פותחים את המכפלה הפנימית, מקבצים, מסבירים שהמשתנה החדש עובר על כל המרחב, ואז מסיקים."),
            bug("באיזו שורה יש טעות?",
                [r"$\langle S^TAS\vec v,\vec v\rangle=\vec v^TS^TAS\vec v$",
                 r"$=\left(S^T\vec v\right)^TA\left(S^T\vec v\right)$",
                 r"$S$ הפיכה, ולכן הווקטורים עוברים על כל $\mathbb{R}^n$"],
                1, r"$\vec v^TS^T=(S\vec v)^T$ ו-$S\vec v$ ולא $S^T\vec v$."),
            ch(r"מדוע כל $\vec u\in\mathbb{R}^n$ הוא מהצורה $S\vec v$?", r"כי $S$ אורתוגונלית ולכן הפיכה ($\vec v=S^T\vec u$)",
               [r"כי $A$ סימטרית", r"כי $S$ סימטרית"],
               r"אורתוגונלית גוררת הפיכה. סימטריה של $A$ אינה קשורה, ו-$S$ אורתוגונלית אינה חייבת להיות סימטרית (סיבוב).", 0),
            num(r"$S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ ו-$A=\operatorname{diag}(1,2)$. מהו הערך העצמי הקטן של $S^TAS$?", 1,
                r"$S^TAS=\operatorname{diag}(2,1)$, בעל אותם ערכים עצמיים כמו $A$."),
        ]),
    (2, "א"): dict(
        rubric=rub(("סגירות: $\\mathbb{Z}_5^*$ סגורה לכפל", 2), ("אסוציאטיביות רכיב-רכיב", 1), (r"איבר ניטרלי $E$ (מטריצת האחדות)", 2),
                   ("הופכי רכיב-רכיב", 2)),
        pitfalls=[r"לחשוב שהאיבר הניטרלי הוא $I$: $I$ אינה ב-$H$ (יש בה אפסים), והפעולה רכיב-רכיב.",
                  r"לשכוח שכל הרכיבים שונים מאפס, ולכן הפיכים ב-$\mathbb{Z}_5$."],
        steps=[
            ch(r"מהו האיבר הניטרלי של $(H,\odot)$?", r"$E=\begin{pmatrix}1&1\\1&1\end{pmatrix}$",
               [r"$I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$", r"$\begin{pmatrix}0&0\\0&0\end{pmatrix}$"],
               r"$X\odot E=X$ רכיב-רכיב. $I$ ומטריצת האפס אינן ב-$H$ (יש בהן אפסים).", 0),
            num(r"מהו $3\cdot4$ ב-$\mathbb{Z}_5$?", 2, r"$12=2\cdot5+2$."),
            num(r"מהו ההופכי של $2$ ב-$\mathbb{Z}_5$?", 3, r"$2\cdot3=6\equiv1$."),
            num(r"מהו ההופכי של $3$ ב-$\mathbb{Z}_5$?", 2, r"$3\cdot2=6\equiv1$."),
        ]),
    (2, "ב"): dict(
        rubric=rub((r"לכל רכיב $4$ ערכים אפשריים ($1,2,3,4$)", 2), (r"עקרון הכפל: $4^4=256$", 2)),
        pitfalls=[r"לספור גם את הערך $0$ ולקבל $5^4$.",
                  r"לספור רק $4\cdot4$ (שני רכיבים בלבד)."],
        steps=[
            num(r"כמה ערכים אפשריים יש לכל רכיב?", 4, r"$\mathbb{Z}_5^*=\{1,2,3,4\}$."),
            num(r"מהו $|H|$?", 256, r"ארבעה רכיבים בלתי תלויים: $4^4=256$."),
        ]),
    (2, "ג"): dict(
        rubric=rub((r"סדרי הרכיבים: $o(1)=1$, $o(2)=o(3)=4$", 2), (r"הסדר של המטריצה הוא הכפולה המשותפת המינימלית: $4$", 2)),
        pitfalls=[r"לחשב סדר של המטריצה בכפל מטריצות רגיל ולא ברכיב-רכיב.",
                  r"לקחת את הסדר הגדול ביותר ולא את הכפולה המשותפת המינימלית (כאן הם זהים, אך זה אינו כלל)."],
        steps=[
            num(r"מהו הסדר של $2$ ב-$\mathbb{Z}_5^*$ (בכפל)?", 4, r"$2,4,3,1$: החזקה הרביעית היא הראשונה ששווה ל-$1$."),
            num(r"מהו הסדר של $3$ ב-$\mathbb{Z}_5^*$?", 4, r"$3,4,2,1$."),
            num(r"מהו הסדר של $\begin{pmatrix}1&2\\2&3\end{pmatrix}$?", 4, r"$\operatorname{lcm}(1,4,4,4)=4$."),
        ]),
    (2, "ד"): dict(
        rubric=rub((r"הגדרת $\bar u=(a_1,\dots,a_n)$ ו-$\bar v=(1,\dots,1)$", 3), (r"חישוב $\langle\bar u,\bar v\rangle$ והנורמות", 3),
                   ("קושי-שוורץ והצבה", 4)),
        pitfalls=[r"לשכוח ש-$\|\bar v\|^2=n$ ולכתוב $1$.",
                  r"לשכוח את הריבוע על הסכום: $\left(\sum a_i\right)^2$."],
        steps=[
            ch("לאילו וקטורים מיישמים את קושי-שוורץ?", r"$\bar u=(a_1,\dots,a_n)$ ו-$\bar v=(1,\dots,1)$",
               [r"$\bar u=(a_1,\dots,a_n)$ ו-$\bar v=\bar u$", r"$\bar u=\left(a_1^2,\dots,a_n^2\right)$ ו-$\bar v=(1,\dots,1)$"],
               r"רק עם $\bar u=(a_1,\dots,a_n)$ ו-$\bar v=(1,\dots,1)$ מתקבל $\langle\bar u,\bar v\rangle=\sum a_i$ ו-$\|\bar v\|^2=n$. הבחירה $\bar v=\bar u$ נותנת שוויון טריוויאלי והבחירה עם $a_i^2$ נותנת $\left(\sum a_i^2\right)^2\le n\sum a_i^4$.", 1),
            order("סדרו את שלבי ההוכחה.",
                  [r"נגדיר $\bar u=(a_1,\dots,a_n)^T$ ו-$\bar v=(1,\dots,1)^T$",
                   r"$\langle\bar u,\bar v\rangle=a_1+\dots+a_n$, $\|\bar u\|^2=\sum a_i^2$, $\|\bar v\|^2=n$",
                   r"קושי-שוורץ: $\langle\bar u,\bar v\rangle^2\le\|\bar u\|^2\|\bar v\|^2$",
                   r"$(a_1+\dots+a_n)^2\le n\left(a_1^2+\dots+a_n^2\right)$"],
                  "הגדרה, חישוב, אי-שוויון, והצבה."),
            num(r"עבור $a=(1,2,3)$, מהו $n\left(a_1^2+a_2^2+a_3^2\right)$?", 42, r"$3\cdot14=42\ge6^2=36$."),
        ]),
    (3, "א"): dict(
        rubric=rub((r"$a\cdot b-a-b$ שלם לכל $a,b\in\mathbb{Z}$", 2), ("לכן הפעולה בינארית", 1)),
        pitfalls=[r"לבדוק רק שהביטוי מוגדר, ולא שהתוצאה שייכת ל-$\mathbb{Z}$."],
        steps=[
            num(r"מהו $3\otimes4$?", 5, r"$12-3-4=5$."),
            num(r"מהו $(-2)\otimes5$?", -13, r"$-10+2-5=-13$, שלם."),
        ]),
    (3, "ב"): dict(
        rubric=rub((r"פיתוח $(a\otimes b)\otimes c$ ו-$a\otimes(b\otimes c)$", 2), (r"הביטויים שונים (למשל המקדם של $a$), ולכן אינה אסוציאטיבית", 2)),
        pitfalls=[r"להסיק אי-אסוציאטיביות מפיתוח בלי להראות במפורש שהביטויים שונים (דוגמה נגדית מספיקה).",
                  r"לטעות בסימנים בפיתוח $(ab-a-b)c-(ab-a-b)-c$."],
        steps=[
            num(r"מהו $(1\otimes2)\otimes3$?", -5, r"$1\otimes2=-1$ ו-$(-1)\otimes3=-3+1-3=-5$."),
            num(r"מהו $1\otimes(2\otimes3)$?", -1, r"$2\otimes3=1$ ו-$1\otimes1=1-1-1=-1$."),
            num(r"מהו הפרש שני הערכים, $(1\otimes2)\otimes3-1\otimes(2\otimes3)$?", -4, r"$-5-(-1)=-4\ne0$, ולכן אינה אסוציאטיבית."),
        ]),
    (3, "ג"): dict(
        rubric=rub((r"$a\otimes e=a$ נותן $e(a-1)=2a$ לכל $a$", 2), (r"עבור $a=1$: $0=2$, סתירה", 2)),
        pitfalls=[r"לבחור $a$ אחר מ-$1$: רק בו האגף השמאלי מתאפס ונוצרת הסתירה.",
                  r"לבדוק רק ערך אחד של $e$ במקום להראות שאף $e$ אינו מתאים."],
        steps=[
            num(r"מהו הערך של $e(a-1)$ עבור $a=1$ (לכל $e$)?", 0, r"$e\cdot0=0$."),
            num(r"מהו האגף הימני $2a$ עבור $a=1$?", 2, r"$2\cdot1=2$, ולכן $0=2$ ויש סתירה."),
        ]),
    (3, "ד"): dict(
        rubric=rub((r"הפעולה אינה אסוציאטיבית (סעיף א.2)", 2), (r"אין איבר ניטרלי (סעיף א.3)", 2)),
        pitfalls=[r"לבדוק רק את אקסיומת ההופכי, בלי לשים לב שכבר נכשלו אקסיומות קודמות.",
                  r"להסיק שזו חבורה רק כי הפעולה בינארית."],
        steps=[
            ch(r"אילו מאקסיומות החבורה נכשלות ב-$(\mathbb{Z},\otimes)$?", "גם האסוציאטיביות וגם קיום איבר ניטרלי",
               ["האסוציאטיביות בלבד", "קיום איבר ניטרלי בלבד", "אף אחת"],
               r"בסעיף א.2 יש דוגמה נגדית לאסוציאטיביות, ובסעיף א.3 מראים שאין איבר ניטרלי.", 1),
            num(r"מהו $(1\otimes2)\otimes3-1\otimes(2\otimes3)$ (עדות לכשל האסוציאטיביות)?", -4, r"$-5-(-1)=-4$."),
        ]),
    (3, "ה"): dict(
        rubric=rub((r"$A(\bar u+\bar v)=\bar u+\bar v$, לכן $\lambda=1$", 4), (r"$A(\bar u-\bar v)=-(\bar u-\bar v)$, לכן $\lambda=-1$", 4),
                   (r"מטריצה $2\times2$ ולכן אין ערכים עצמיים נוספים", 2)),
        pitfalls=[r"לשכוח את התנאי שהבסיס אורתונורמלי: $\bar u^T\bar v=0$ ו-$\bar u^T\bar u=\bar v^T\bar v=1$.",
                  r"להסיק שהערכים העצמיים הם $\pm1$ רק מכך שהווקטורים יחידה, בלי החישוב."],
        steps=[
            num(r"דוגמה: $\bar u=(1,0)^T$ ו-$\bar v=(0,1)^T$, ולכן $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. מהו הערך העצמי של $\bar u+\bar v$?", 1,
                r"$A(1,1)^T=(1,1)^T$."),
            num(r"באותה דוגמה, מהו הערך העצמי של $\bar u-\bar v$?", -1, r"$A(1,-1)^T=(-1,1)^T=-(1,-1)^T$."),
            ch("מדוע אין ערכים עצמיים נוספים?", r"כי $A$ מסדר $2\times2$ ויש לה כבר שני ערכים עצמיים שונים",
               [r"כי $A$ סימטרית ולכן כל הערכים העצמיים הם $\pm1$", r"כי הווקטורים $\bar u,\bar v$ הם יחידה"],
               r"למטריצה $2\times2$ יש לכל היותר שני ערכים עצמיים. סימטריה או נרמול לבדם אינם מגבילים את הערכים (למשל $\operatorname{diag}(5,7)$ סימטרית).", 0),
        ]),
    (4, "א"): dict(
        rubric=rub((r"גרם-שמידט: $\bar q_1=\bar a_1/\|\bar a_1\|$", 4), (r"$\bar q_2,\bar q_3$ מהורדת ההיטלים ונרמול", 4),
                   (r"$R=Q^TA$ העליונה המשולשת", 4), (r"בדיקה $A=QR$", 3)),
        pitfalls=[r"לשכוח לנרמל את $\bar q_i$ ולקבל $Q$ שאינה אורתוגונלית.",
                  r"לכתוב את $R$ תחתונה במקום עליונה."],
        steps=[
            num(r"מהו $r_{11}=\|\bar a_1\|$ עבור $\bar a_1=(1,1,0)^T$ (ערך מספרי)?", 1.4142136, r"$\sqrt2\approx1.414$.", 0.001),
            num(r"מהו $r_{12}=\bar q_1\cdot\bar a_2$ עבור $\bar a_2=(1,0,1)^T$ (ערך מספרי)?", 0.7071068, r"$\frac1{\sqrt2}(1,1,0)\cdot(1,0,1)=\frac{\sqrt2}2\approx0.707$.", 0.001),
            num(r"מהו $r_{22}$ (ערך מספרי)?", 1.2247449, r"$\frac{\sqrt6}2\approx1.225$.", 0.001),
            num(r"מהו $r_{33}$ (ערך מספרי)?", 1.1547005, r"$\frac{2\sqrt3}3\approx1.155$.", 0.001),
        ]),
    (4, "ב"): dict(
        rubric=rub((r"צמצום לצורה $x\equiv3\pmod5$ ו-$x\equiv5\pmod7$", 4), (r"מודולים זרים בזוגות ו-$m=1120$", 2), (r"פתרון $x\equiv103\pmod{1120}$", 4)),
        pitfalls=[r"לפתור את המערכת בלי לצמצם קודם את המקדמים ($3x$, $2x$) לצורה $x\equiv\cdot$.",
                  r"לשכוח ש-$32=2^5$ זר ל-$5$ ול-$7$, ולכן המשפט חל."],
        steps=[
            num(r"פתרו $3x\equiv4\pmod5$ ($0\le x<5$). מהו $x$?", 3, r"$3\cdot3=9\equiv4$."),
            num(r"פתרו $2x\equiv3\pmod7$ ($0\le x<7$). מהו $x$?", 5, r"$2\cdot5=10\equiv3$."),
            num(r"מהו $m=5\cdot7\cdot32$?", 1120, r"המודולים זרים בזוגות."),
            num(r"מהו הפתרון $x_0$ ($0\le x_0<1120$) של המערכת?", 103, r"$103\equiv3\pmod5$, $\equiv5\pmod7$, $\equiv7\pmod{32}$."),
        ]),
    (5, "א"): dict(
        rubric=rub((r"ערכים עצמיים $1,\ 1+\sqrt2c,\ 1-\sqrt2c$", 3), (r"חיובית: $|c|\le\frac1{\sqrt2}$", 3), (r"חיובית לחלוטין: $|c|<\frac1{\sqrt2}$", 3),
                   (r"אין $c$ שלילית (בגלל $\lambda_1=1>0$)", 3), ("בשאר הערכים אף אחת", 3)),
        pitfalls=[r"לשכוח שהערך העצמי $\lambda_1=1$ קבוע ואינו תלוי ב-$c$.",
                  r"לבלבל בין $\le$ (חיובית) ל-$<$ (חיובית לחלוטין)."],
        steps=[
            num(r"עבור $c=0.5$, מהו הערך העצמי $1-\sqrt2c$ (ערך מספרי)?", 0.2928932, r"$1-0.7071\approx0.293$.", 0.001),
            ch("עבור אילו $c$ המטריצה מוגדרת חיובית (לא בהכרח לחלוטין)?", r"$|c|\le\frac1{\sqrt2}$",
               [r"$|c|\le1$", r"$|c|\le\frac12$", r"$|c|<\frac1{\sqrt2}$"],
               r"צריך $1\pm\sqrt2c\ge0$, כלומר $|c|\le\frac1{\sqrt2}$. עבור $c=0.9$ הערך $1-\sqrt2c<0$; עבור $c=0.6$ התנאי מתקיים ולכן $\frac12$ קטן מדי; ובקצה $|c|=\frac1{\sqrt2}$ יש ערך עצמי $0$ שמותר בהגדרה החלשה.", 3),
            ch("עבור אילו $c$ המטריצה מוגדרת חיובית לחלוטין?", r"$|c|<\frac1{\sqrt2}$",
               [r"$|c|\le\frac1{\sqrt2}$", r"$|c|<1$"],
               r"צריכים כל הערכים העצמיים חיוביים ממש; ב-$|c|=\frac1{\sqrt2}$ יש ערך עצמי $0$.", 0),
            ch("האם יש $c$ שעבורו המטריצה מוגדרת שלילית?", r"לא, כי $\lambda_1=1>0$ לכל $c$",
               [r"כן, עבור $c$ גדול מספיק", r"כן, עבור $c=0$"],
               r"בשלילית כל הערכים העצמיים $\le0$, אך $\lambda_1=1$ תמיד. עבור $c$ גדול הערכים $1\pm\sqrt2c$ משני סימנים, ועבור $c=0$ המטריצה היא $I$.", 1),
        ]),
    (5, "ב"): dict(
        rubric=rub(("סגירות", 3), ("אסוציאטיביות מ-$G$", 1), (r"איבר ניטרלי $e\in H\cap K$", 3), (r"הופכי $x^{-1}\in H\cap K$", 3)),
        pitfalls=[r"לבדוק רק סגירות ולשכוח את הניטרלי וההופכי.",
                  r"לבלבל בין חיתוך לאיחוד: איחוד של תת-חבורות אינו בהכרח תת-חבורה."],
        steps=[
            order("סדרו את שלבי הוכחת הסגירות.",
                  [r"יהיו $x,y\in H\cap K$, כלומר $x,y\in H$ וגם $x,y\in K$",
                   r"$H$ ו-$K$ תת-חבורות, ולכן $x*y\in H$ וגם $x*y\in K$",
                   r"לכן $x*y\in H\cap K$"],
                  "הנחה, שימוש בסגירות כל תת-חבורה, ואז מסקנה."),
            bug("באיזו שורה בהוכחת ההופכי יש טעות?",
                [r"יהי $x\in H\cap K$",
                 r"$H$ תת-חבורה, ולכן $x^{-1}\in H$",
                 r"$K$ תת-חבורה, ולכן $x^{-1}\in K$",
                 r"לכן $x^{-1}\in H\cup K$"],
                3, r"צריך להסיק ש-$x^{-1}$ בשתי הקבוצות, כלומר ב-$H\cap K$ ולא ב-$H\cup K$."),
            num(r"ב-$\mathbb{Z}_{12}$ (חיבור) תהי $H=\langle2\rangle$ ו-$K=\langle3\rangle$. מהו $|H\cap K|$?", 2, r"$H=\{0,2,4,6,8,10\}$ ו-$K=\{0,3,6,9\}$; החיתוך $\{0,6\}$."),
        ]),
    (6, "א"): dict(
        rubric=rub((r"ערכים עצמיים $5,2,-1$", 5), ("וקטורים עצמיים בלתי תלויים (לכל ערך עצמי)", 5), ("נרמול ל-$Q$ אורתוגונלית", 3), (r"$A=QDQ^T$", 2)),
        pitfalls=[r"לשכוח לנרמל את הווקטורים העצמיים.",
                  r"לסדר את עמודות $Q$ בסדר שונה מסדר הערכים העצמיים ב-$D$."],
        steps=[
            num(r"מהי העקבה (trace) של $A$, והיא סכום הערכים העצמיים?", 6, r"$3+2+1=6=5+2+(-1)$."),
            num(r"מהי הדטרמיננטה של $A$, והיא מכפלת הערכים העצמיים?", -10, r"$5\cdot2\cdot(-1)=-10$."),
            num(r"מהו האורך של הווקטור העצמי $(2,2,1)^T$ (של $\lambda=5$) שמנרמלים?", 3, r"$\sqrt{4+4+1}=3$, ולכן הווקטור המנורמל הוא $\left(\frac23,\frac23,\frac13\right)^T$."),
        ]),
    (6, "ב"): dict(
        rubric=rub((r"פיתוח $\|\bar u+\bar v\|^2=\|\bar u\|^2+2\langle\bar u,\bar v\rangle+\|\bar v\|^2$", 3), (r"פיתוח $\|\bar u-\bar v\|^2$", 3),
                   ("חיבור: הגורמים המעורבים מצטמצמים", 4)),
        pitfalls=[r"לשכוח את הגורם $2$ במכפלה הפנימית.",
                  r"לכתוב $\|\bar u+\bar v\|^2=\|\bar u\|^2+\|\bar v\|^2$ (נכון רק כשהווקטורים אורתוגונליים)."],
        steps=[
            num(r"$\bar u=(1,2)$ ו-$\bar v=(3,-1)$. מהו $\|\bar u+\bar v\|^2+\|\bar u-\bar v\|^2$?", 30, r"$17+13=30=2(5+10)$."),
            ch("איזה גורם מצטמצם בחיבור שתי הזהויות?", r"$2\langle\bar u,\bar v\rangle$ (מופיע עם שני סימנים)",
               [r"$\|\bar u\|^2$", r"$\|\bar v\|^2$"],
               r"$\|\bar u\|^2$ ו-$\|\bar v\|^2$ מופיעים בשתי הזהויות באותו סימן ולכן מוכפלים ב-$2$; רק הגורם המעורב מתבטל.", 0),
            bug("באיזו שורה יש טעות?",
                [r"$\|\bar u+\bar v\|^2=\|\bar u\|^2+2\langle\bar u,\bar v\rangle+\|\bar v\|^2$",
                 r"$\|\bar u-\bar v\|^2=\|\bar u\|^2-2\langle\bar u,\bar v\rangle-\|\bar v\|^2$",
                 r"$\|\bar u+\bar v\|^2+\|\bar u-\bar v\|^2=2\left(\|\bar u\|^2+\|\bar v\|^2\right)$"],
                1, r"$\langle-\bar v,-\bar v\rangle=+\|\bar v\|^2$, ולכן הסימן של $\|\bar v\|^2$ חיובי."),
        ]),
}
for _q in questions:
    _s = S25BB.get((_q["num"], _q.get("part")))
    assert _s is not None, ("no steps for", _q["num"], _q.get("part"))
    assert sum(r["points"] for r in _s["rubric"]) == _q["points"], ("rubric sum", _q["num"], _q.get("part"))
    _q["rubric"], _q["rubricSource"] = _s["rubric"], "ai-verified"
    _q["pitfalls"] = _s["pitfalls"]
    _q["steps"], _q["stepsSource"] = _s["steps"], "ai-verified"

exam = {
    "examCode": "25B-B",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ה מועד ב'",
    "year": 2025,
    "examDate": "7.8.2025",
    "sourceFile": "algebra-2-25B-B-exam",
    "solutionFile": "algebra-2-25B-B-handwritten-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
