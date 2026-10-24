# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-A.json -- algebra-2 (20079), semester B 2025, moed A (9.07.2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25B-A.py

Source: exam 3 pp. (header misprints the semester as A; the date 09.07.25 and the file name make it semester B moed A)
+ handwritten solution 12 pp. (scan, read from the rendered pages). Sheet: 6 questions, "best 4", 25% each; all 6 are
transcribed, 17 items. Solutions are handwritten without an author name, solutionSource "student-solution" (unknown-author handwritten scan; not presented as the lecturer's).
NOTE: the second file in the folder ("lecturers' solution", 11 pp.) belongs to a DIFFERENT exam (Q1 is an integral inner
product on C[0,1], Q2 a group on R x R*), so it is not used here.

Part letters: numbered sub-parts get letters in order (Q2: 1,2,3 -> a,b,c and printed b -> d; Q4: 1..4 -> a..d, printed b -> e).
Q5 is printed with parts "א" and "ג" and Q6 with "ב" and "ג" (the sheet skips letters); printed letters are kept.
Every question text starts with its printed label.

Official solution gaps / slips (no final answer is wrong):
- Q3b asks for the group proof AND the order of G; the handwritten solution stops after the group axioms. The order
  ("infinite") is added, so the item is shipped as solutionSource "solved", official false, with the Hebrew prefix.
  Logged in docs/ASK_ADIR.md.
- Q6c: the first line prints "[sum a_i^2]^2 <= ..."; the proof below proves (sum a_i)^2 <= (sum a_i/b_i)(sum a_i b_i)
  (written correctly). The closing line (square of the inner product bound) is stated in the solution; the last substitution is
  made explicit. Logged in docs/ASK_ADIR.md.
- Q5c prints only the final answer x = 112 mod 165 (kept, no steps invented). Q6b prints only D and Q (kept).
Checks: tools/verify/25B-A/check.py (sympy + brute force), all OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"תהי $H=\left\{\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix}\in M_2(\mathbb{Z}_7)\ \middle|\ x\neq0\right\}$ כאשר $x^{-1}$ מסמן את האיבר ההופכי של $x$ ב-$\mathbb{Z}_7$."},
    "c4": {"kind": "text", "title": "שאלה 4 סעיף א", "text": r"לכל $a,b\in\mathbb{Z}$ נגדיר פעולה: $a\odot b=ab+a+b$."},
}

S1A = (
    r"$$A=\begin{pmatrix}-2&1\\1&1\\5&1\\7&1\\9&1\end{pmatrix},\qquad\vec b=\begin{pmatrix}3\\5\\6\\5\\8\end{pmatrix},\qquad A^TA\begin{pmatrix}m\\n\end{pmatrix}=A^T\vec b$$" "\n"
    r"$$\begin{pmatrix}160&20\\20&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}136\\27\end{pmatrix}$$" "\n"
    r"$$m=0.35,\quad n=4\qquad\Rightarrow\qquad y=0.35x+4$$"
)

S1B = (
    r"נסמן ב-$\lambda$ וב-$\mu$ את הערכים העצמיים ($\lambda\ne\mu$) המתאימים ל-$\vec u$ ול-$\vec v$ בהתאמה: $A\bar u=\lambda\bar u$ , $A\bar v=\mu\bar v$." "\n"
    r"מצד אחד: $\ \bar v^TA\bar u=\bar v^T\lambda\bar u=\lambda\langle\bar u,\bar v\rangle$." "\n"
    r"מצד שני, מפני ש-$A$ סימטרית, נקבל: $\ \bar v^TA\bar u=\bar v^TA^T\bar u=(A\bar v)^T\bar u=\mu\bar v^T\bar u=\mu\langle\bar u,\bar v\rangle$." "\n"
    r"הוכחנו ש-$\lambda\langle\bar u,\bar v\rangle=\mu\langle\bar u,\bar v\rangle$. אבל $\lambda\ne\mu$, לכן $\langle\bar u,\bar v\rangle=0$, כלומר $\vec u\perp\vec v$."
)

S2A1 = (
    r"**סגירות:** יהיו $\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix},\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}\in H$. אז" "\n"
    r"$$\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix}\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}=\begin{pmatrix}xa&xb+ya^{-1}\\0&(xa)^{-1}\end{pmatrix}\in H$$" "\n"
    r"**אסוציאטיביות:** כל המטריצות פועלות בכפל מטריצות, שהוא אסוציאטיבי." "\n"
    r"**איבר ניטרלי:** $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}\in H$ הוא האיבר הניטרלי של $H$." "\n"
    r"**איבר הופכי:** נשים לב ש-$\begin{vmatrix}x&y\\0&x^{-1}\end{vmatrix}=1\neq0$, לכן המטריצה הפיכה. נמצא את ההופכית שלה:" "\n"
    r"$$\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix}\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$$" "\n"
    r"מכאן $a=x^{-1}$ , $xb+ya^{-1}=0\Rightarrow b=-y$. לכן" "\n"
    r"$$\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix}^{-1}=\begin{pmatrix}x^{-1}&-y\\0&x\end{pmatrix}\in H$$" "\n"
    "הוכחנו ש-$H$ חבורה."
)

S2A2 = (
    r"$x$ יכול להיות כל אחד מ-6 האיברים $(x\neq0)$ ו-$y$ כל אחד מ-7 האיברים של $\mathbb{Z}_7$. לכן" "\n"
    r"$$o(H)=6\cdot7=42$$"
)

S2A3 = (
    r"נסמן $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. נקבל:" "\n"
    r"$$A\neq I,\quad A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}\neq I,\quad A^3=\begin{pmatrix}1&3\\0&1\end{pmatrix}\neq I,\ \dots$$" "\n"
    r"$$A^7=\begin{pmatrix}1&7\\0&1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod7=I$$" "\n"
    r"לכן $o(A)=7$."
)

S2B = (
    r"נחשב: $A\bar u=\left(\bar u\bar u^T+\bar v\bar v^T+\bar w\bar w^T\right)\bar u=\bar u\cdot\bar u^T\bar u=\bar u$ כי $\|\bar u\|^2=1$ (שאר הגורמים מתאפסים בגלל האורתוגונליות)." "\n"
    r"$A\bar v=\bar v\cdot\bar v^T\bar v=\bar v$ , $\ A\bar w=\bar w\cdot\bar w^T\bar w=\bar w$." "\n"
    r"כלומר $A$ מקיימת $A\bar x=\bar x$ על שלושה וקטורים בלתי תלויים $\bar u,\bar v,\bar w$ (בסיס של $\mathbb{R}^3$), ולכן $A=I$. (ל-$A$ יש ערך עצמי $\lambda=1$ עם שלושה וקטורים עצמיים בלתי תלויים.)"
)

S3A = (
    r"נחשב את הערכים העצמיים של המטריצה:" "\n"
    r"$$\begin{vmatrix}k-\lambda&k&0\\k&k-\lambda&k\\0&k&k-\lambda\end{vmatrix}=(\lambda-k)\left(-\lambda^2+2\lambda k+k^2\right)=0$$" "\n"
    r"$$\lambda_1=k,\qquad\lambda_2=k\left(1-\sqrt2\right),\qquad\lambda_3=k\left(1+\sqrt2\right)$$" "\n"
    r"מכיוון ש-$1+\sqrt2>0$ ו-$1-\sqrt2<0$, לכל $k\neq0$ יש ערך עצמי חיובי וערך עצמי שלילי, ולכן לא קיים $k\neq0$ עבורו המטריצה מוגדרת חיובית (לחלוטין) או שלילית (לחלוטין). עבור $k=0$ זו מטריצת האפס: מוגדרת חיובית ושלילית בו זמנית." "\n"
    "**סיכום:**\n"
    r"(1) המטריצה לא מוגדרת חיובית לחלוטין לכל $k$." "\n"
    r"(2) המטריצה לא מוגדרת שלילית לחלוטין לכל $k$." "\n"
    r"(3) המטריצה מוגדרת חיובית עבור $k=0$." "\n"
    r"(4) המטריצה מוגדרת שלילית עבור $k=0$." "\n"
    r"(לכל שאר ערכי $k$ אף אחת מהן.)"
)

S3B = (
    "השלמה לפתרון שבקובץ: הפתרון שבקובץ מוכיח שהמבנה חבורה אך לא כותב את הסדר של $G$, והסדר נוסף כאן.\n"
    r"**סגירות:** לכל $n,m\in\mathbb{Z}$ מתקיים" "\n"
    r"$$\begin{pmatrix}1&n\\0&1\end{pmatrix}\begin{pmatrix}1&m\\0&1\end{pmatrix}=\begin{pmatrix}1&m+n\\0&1\end{pmatrix}\in G$$" "\n"
    r"כי $m+n\in\mathbb{Z}$." "\n"
    r"**אסוציאטיביות:** כפל מטריצות אסוציאטיבי." "\n"
    r"**איבר ניטרלי:** $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}\in G$ (עבור $n=0$)." "\n"
    r"**איבר הופכי:** $\begin{vmatrix}1&n\\0&1\end{vmatrix}=1\neq0$, לכן המטריצה הפיכה. מתוך $m+n=0$ נקבל $m=-n$, כלומר" "\n"
    r"$$\begin{pmatrix}1&n\\0&1\end{pmatrix}^{-1}=\begin{pmatrix}1&-n\\0&1\end{pmatrix}\in G$$" "\n"
    r"כי $-n\in\mathbb{Z}$. הוכחנו ש-$G$ חבורה." "\n"
    r"**הסדר:** לכל $n\in\mathbb{Z}$ מתאימה מטריצה אחרת (הרכיב בפינה הימנית העליונה הוא $n$), לכן $G$ אינסופית: $|G|=\infty$."
)

S4A1 = r"לכל $a,b\in\mathbb{Z}$ מתקיים $a\odot b=ab+a+b\in\mathbb{Z}$, לכן $\odot$ פעולה בינארית על $\mathbb{Z}$."

S4A2 = (
    r"לכל $a,b,c\in\mathbb{Z}$ מתקיים:" "\n"
    r"$$(a\odot b)\odot c=(ab+a+b)\odot c=(ab+a+b)c+(ab+a+b)+c=abc+ac+bc+ab+a+b+c$$" "\n"
    r"$$a\odot(b\odot c)=a\odot(bc+b+c)=a(bc+b+c)+a+(bc+b+c)=abc+ab+ac+bc+a+b+c$$" "\n"
    "הפעולה אסוציאטיבית."
)

S4A3 = (
    r"נניח שקיים $e\in\mathbb{Z}$ כך שלכל $a\in\mathbb{Z}$ מתקיים $a\odot e=a$. אז" "\n"
    r"$$a\odot e=ae+a+e=a\ \Rightarrow\ e(a+1)=0\quad\forall a\in\mathbb{Z}\ \Rightarrow\ e=0$$" "\n"
    r"ב-$(\mathbb{Z},\odot)$ קיים איבר ניטרלי: $e=0$."
)

S4A4 = (
    r"עלינו לבדוק האם לכל $a\in\mathbb{Z}$ קיים איבר הופכי ביחס לפעולה $\odot$. נניח $a\odot b=0$. אז" "\n"
    r"$$a\cdot b+a+b=0\ ,\qquad b(a+1)=-a$$" "\n"
    r"אפשר לראות שלא קיים $b$ למשל עבור $a=-1$ (כמובן יש עוד דוגמאות): $(-1)\odot b=-b-1+b=-1\ne0$ לכל $b$. לכן $(\mathbb{Z},\odot)$ אינה חבורה."
)

S4B = (
    r"מתקיים" "\n"
    r"$$\|\bar u-\bar v\|=\|\bar u+\bar v\|\iff\|\bar u-\bar v\|^2=\|\bar u+\bar v\|^2\iff\langle\bar u-\bar v,\bar u-\bar v\rangle=\langle\bar u+\bar v,\bar u+\bar v\rangle$$" "\n"
    r"$$\iff\|\bar u\|^2-2\langle\bar u,\bar v\rangle+\|\bar v\|^2=\|\bar u\|^2+2\langle\bar u,\bar v\rangle+\|\bar v\|^2\iff-2\langle\bar u,\bar v\rangle=2\langle\bar u,\bar v\rangle$$" "\n"
    r"$$\iff\langle\bar u,\bar v\rangle=0\iff\bar u\perp\bar v$$"
)

S5A = (
    r"$$A=\begin{pmatrix}2&1\\1&-2\\0&2\end{pmatrix}=U\Sigma V^T$$" "\n"
    r"$$U=\begin{pmatrix}\frac13&\frac{2\sqrt5}{5}&-\frac{2\sqrt5}{15}\\-\frac23&\frac{\sqrt5}{5}&\frac{4\sqrt5}{15}\\\frac23&0&\frac{\sqrt5}{3}\end{pmatrix},\qquad\Sigma=\begin{pmatrix}3&0\\0&\sqrt5\\0&0\end{pmatrix},\qquad V=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$"
)

S5C = r"$$x\equiv112\pmod{165}$$"

S6B = (
    r"$$D=\begin{pmatrix}2&0&0\\0&2&0\\0&0&5\end{pmatrix},\qquad Q=\begin{pmatrix}-\frac1{\sqrt2}&-\frac1{\sqrt6}&\frac1{\sqrt3}\\\frac1{\sqrt2}&-\frac1{\sqrt6}&\frac1{\sqrt3}\\0&\frac2{\sqrt6}&\frac1{\sqrt3}\end{pmatrix},\qquad A=QDQ^T$$"
)

S6C = (
    r"עלינו להוכיח כי $\displaystyle\left(\sum_{i=1}^na_i\right)^2\le\left(\sum_{i=1}^n\frac{a_i}{b_i}\right)\cdot\left(\sum_{i=1}^na_ib_i\right)$." "\n"
    r"נגדיר שני וקטורים ב-$\mathbb{R}^n$: $\ \bar u=\begin{pmatrix}\sqrt{a_1/b_1}\\\vdots\\\sqrt{a_n/b_n}\end{pmatrix}$ , $\ \bar v=\begin{pmatrix}\sqrt{a_1b_1}\\\vdots\\\sqrt{a_nb_n}\end{pmatrix}$. מתקיים:" "\n"
    r"$$\langle\bar u,\bar v\rangle=\sum_{i=1}^na_i,\qquad\|\bar u\|^2=\sum_{i=1}^n\frac{a_i}{b_i},\qquad\|\bar v\|^2=\sum_{i=1}^na_ib_i$$" "\n"
    r"לפי אי-שוויון קושי-שוורץ מתקיים $\langle\bar u,\bar v\rangle^2\le\|\bar u\|^2\cdot\|\bar v\|^2$, כלומר" "\n"
    r"$$\left(\sum_{i=1}^na_i\right)^2\le\left(\sum_{i=1}^n\frac{a_i}{b_i}\right)\left(\sum_{i=1}^na_ib_i\right)\ \Rightarrow\ \frac{\left(\sum_{i=1}^na_i\right)^2}{\sum_{i=1}^na_ib_i}\le\sum_{i=1}^n\frac{a_i}{b_i}$$"
)

questions = [
    Q(1, "computation", "least_squares",
      r"(10%) נתונות 5 נקודות במישור: $(-2,3),\ (1,5),\ (5,6),\ (7,5),\ (9,8)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן של הריבועים הפחותים.",
      S1A, part="א", points=10),
    Q(1, "proof", "orthodiag",
      r"(15%) תהי $A\in M_n(\mathbb{R})$ מטריצה סימטרית ויהיו $\vec u,\vec v\in\mathbb{R}^n$ וקטורים עצמיים של $A$ המתאימים לערכים עצמיים $\lambda$ ו-$\mu$ **שונים זה מזה**. הוכיחו כי $\vec u\perp\vec v$ (אורתוגונליים זה לזה).",
      S1B, part="ב", points=15),

    Q(2, "proof", "groups", r"סעיף א.1. הוכיחו כי $H$ היא חבורה ביחס לכפל מטריצות. (הכפל והחיבור של רכיבי המטריצות הם מודולו 7). (7%)",
      S2A1, part="א", points=7, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.2. מהו הסדר של $H$ ? (4%)", S2A2, part="ב", points=4, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.3. מצאו את הסדר של $\begin{pmatrix}1&1\\0&1\end{pmatrix}$. (4%)", S2A3, part="ג", points=4,
      contextId="c2"),
    Q(2, "proof", "orthogonality",
      r"סעיף ב. יהי $\{\vec u,\vec v,\vec w\}$ בסיס **אורתונורמלי** במרחב $\mathbb{R}^3$. נגדיר את המטריצה $A=\vec u\cdot\vec u^T+\vec v\cdot\vec v^T+\vec w\cdot\vec w^T\in M_3(\mathbb{R})$. הוכיחו כי $A=I$. (10%)",
      S2B, part="ד", points=10),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $k$ המטריצה $\begin{pmatrix}k&k&0\\k&k&k\\0&k&k\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "proof", "groups",
      r"(10%) הוכיחו כי $G=\left\{\begin{pmatrix}1&n\\0&1\end{pmatrix}\ \middle|\ n\in\mathbb{Z}\right\}$ היא חבורה ביחס לכפל מטריצות ומצאו את הסדר של $G$.",
      S3B, part="ב", points=10, solutionSource="solved", official=False, confidence="high"),

    Q(4, "proof", "groups", r"סעיף א.1. הראו כי $\odot$ היא פעולה בינארית על $\mathbb{Z}$. (3%)", S4A1, part="א", points=3, contextId="c4"),
    Q(4, "truefalse", "groups", r"סעיף א.2. האם הפעולה אסוציאטיבית? (4%)", S4A2, part="ב", points=4, contextId="c4", verdict=True),
    Q(4, "truefalse", "groups", r"סעיף א.3. האם במבנה $(\mathbb{Z},\odot)$ קיים איבר ניטרלי? (4%)", S4A3, part="ג", points=4,
      contextId="c4", verdict=True),
    Q(4, "truefalse", "groups", r"סעיף א.4. האם $(\mathbb{Z},\odot)$ זו חבורה? (4%)", S4A4, part="ד", points=4, contextId="c4",
      verdict=False),
    Q(4, "proof", "cauchy_schwarz",
      r"סעיף ב. יהיו $\vec u,\vec v\in V$ שני וקטורים במרחב מכפלה פנימית. הוכיחו כי הוקטורים אורתוגונליים **אם ורק אם** $\|\vec u-\vec v\|=\|\vec u+\vec v\|$. (10%)",
      S4B, part="ה", points=10),

    Q(5, "computation", "svd", r"סעיף א. מצאו פירוק SVD עבור המטריצה הבאה: $\begin{pmatrix}2&1\\1&-2\\0&2\end{pmatrix}$. (15%)", S5A, part="א",
      points=15),
    Q(5, "computation", "crt",
      r"סעיף ג. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv1\pmod3\\x\equiv2\pmod5\\x\equiv2\pmod{11}\end{cases}$. (10%)",
      S5C, part="ג", points=10),

    Q(6, "computation", "orthodiag",
      r"סעיף ב. בצעו לכסון אורתוגונלי למטריצה הבאה: $A=\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$. (15%)", S6B, part="ב", points=15),
    Q(6, "proof", "cauchy_schwarz",
      r"סעיף ג. הוכיחו כי אם $b_1,b_2,\dots,b_n$ ו-$a_1,a_2,\dots,a_n$ הם מספרים חיוביים אז $\displaystyle\frac{\left(\sum_{i=1}^na_i\right)^2}{\sum_{i=1}^na_i\cdot b_i}\le\sum_{i=1}^n\frac{a_i}{b_i}$. (10%)",
      S6C, part="ג", points=10),
]

# ---------------------------------------------------------------------------------------------------------
# Phase 4 (step author): rubric / pitfalls / guided steps, all derived from the stored solutions above.
# Numeric values and factual claims are re-checked by tools/verify/25B-A/steps_check.py (sympy / brute force).
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


S25BA = {
    (1, "א"): dict(
        rubric=rub((r"הצבת $A$ ו-$\vec b$ (עמודת איקסים ועמודת אחדות)", 3),
                   (r"משוואות נורמליות $A^TA\binom mn=A^T\vec b$ וחישוב שני האגפים", 4),
                   (r"פתרון: $m=0.35$, $n=4$ והישר", 3)),
        pitfalls=[r"לפתור את $A\vec x=\vec b$ ישירות: חמש הנקודות אינן על ישר אחד.",
                  r"לשכוח שאחת הנקודות היא עם $x=-2$ ולכן הסכומים $\sum x_i$ ו-$\sum x_i^2$ שונים מהרגיל."],
        steps=[
            ch("איזו מערכת פותרים בשיטת הריבועים הפחותים?", r"$A^TA\binom mn=A^T\vec b$",
               [r"$A\binom mn=\vec b$ (פתרון מדויק)", r"$AA^T\binom mn=\vec b$"],
               r"הפתרון כופל ב-$A^T$ משמאל. המערכת $A\vec x=\vec b$ אינה פתירה, ו-$AA^T$ היא מטריצה $5\times5$ ולא מתאימה.", 1),
            num(r"מהו האיבר הימני-העליון ב-$A^TA$, כלומר $\sum x_i^2$?", 160, r"$4+1+25+49+81=160$."),
            num(r"מהו האיבר הראשון ב-$A^T\vec b$, כלומר $\sum x_iy_i$?", 136, r"$-6+5+30+35+72=136$."),
            num("מהו השיפוע $m$?", 0.35, r"פתרון $\begin{pmatrix}160&20\\20&5\end{pmatrix}\binom mn=\binom{136}{27}$ נותן $m=0.35$.", 0.001),
            num(r"מהו חיתוך הצירים $n$?", 4, r"מאותה מערכת $n=4$.", 0.001),
        ]),
    (1, "ב"): dict(
        rubric=rub((r"סימון $A\bar u=\lambda\bar u$ ו-$A\bar v=\mu\bar v$", 3), (r"$\bar v^TA\bar u=\lambda\langle\bar u,\bar v\rangle$", 4),
                   (r"שימוש בסימטריה $A=A^T$: $\bar v^TA\bar u=(A\bar v)^T\bar u=\mu\langle\bar u,\bar v\rangle$", 5),
                   (r"$\lambda\ne\mu$ ולכן $\langle\bar u,\bar v\rangle=0$", 3)),
        pitfalls=[r"לא להשתמש בסימטריה של $A$: ללא $A=A^T$ הטענה שגויה.",
                  r"להסיק $\lambda=\mu$ במקום לחלק ב-$\lambda-\mu\ne0$."],
        steps=[
            num(r"דוגמה: $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $\bar u=(1,1)^T$ (ערך עצמי $3$) ו-$\bar v=(1,-1)^T$ (ערך עצמי $1$). מהו $\langle\bar u,\bar v\rangle$?", 0,
                r"$1\cdot1+1\cdot(-1)=0$, כפי שהטענה מבטיחה."),
            order("סדרו את שלבי ההוכחה.",
                  [r"$A\bar u=\lambda\bar u$ ו-$A\bar v=\mu\bar v$ עם $\lambda\ne\mu$",
                   r"נחשב את $\bar v^TA\bar u$ בשתי דרכים: $\lambda\langle\bar u,\bar v\rangle$, ומצד שני (כי $A=A^T$) $(A\bar v)^T\bar u=\mu\langle\bar u,\bar v\rangle$",
                   r"לכן $(\lambda-\mu)\langle\bar u,\bar v\rangle=0$",
                   r"מכיוון ש-$\lambda\ne\mu$ מתקיים $\langle\bar u,\bar v\rangle=0$"],
                  "הנחות, שתי דרכי חישוב, חיסור, ואז חלוקה ב-$\\lambda-\\mu$."),
            bug("באיזו שורה יש טעות?",
                [r"$\bar v^TA\bar u=\bar v^T\lambda\bar u=\lambda\langle\bar u,\bar v\rangle$",
                 r"$\bar v^TA\bar u=\bar v^TA^T\bar u=(A\bar v)^T\bar u=\lambda\,\bar v^T\bar u$",
                 r"לכן $\lambda\langle\bar u,\bar v\rangle=\mu\langle\bar u,\bar v\rangle$"],
                1, r"$A\bar v=\mu\bar v$, ולכן $(A\bar v)^T\bar u=\mu\,\bar v^T\bar u$ ולא $\lambda$."),
        ]),
    (2, "א"): dict(
        rubric=rub(("סגירות: מכפלה מהצורה הנדרשת", 2), ("אסוציאטיביות כפל מטריצות", 1), (r"איבר ניטרלי $I\in H$", 1),
                   (r"הופכי: $a=x^{-1}$, $b=-y$ ו-$\begin{pmatrix}x^{-1}&-y\\0&x\end{pmatrix}\in H$", 3)),
        pitfalls=[r"לשכוח שהחישוב מודולו $7$ ושה-$x^{-1}$ הוא הופכי ב-$\mathbb{Z}_7$.",
                  r"לשכוח לבדוק שהמטריצה ההופכית עצמה שייכת ל-$H$ (האלכסון $x^{-1},x$ וההפכי של $x^{-1}$ הוא $x$)."],
        steps=[
            num(r"$x=2$ ו-$a=3$ ב-$\mathbb{Z}_7$. מהו $(xa)^{-1}$, האיבר הימני-התחתון במכפלה?", 6,
                r"$xa=6$ ו-$6\cdot6=36\equiv1\pmod7$, ולכן $(xa)^{-1}=6$."),
            order("סדרו את שלבי מציאת ההופכי.",
                  [r"נדרוש $\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix}\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}=I$",
                   r"מהאלכסון: $xa=1$, ולכן $a=x^{-1}$",
                   r"מהפינה הימנית העליונה: $xb+ya^{-1}=0$, ולכן $b=-y$",
                   r"ההופכית היא $\begin{pmatrix}x^{-1}&-y\\0&x\end{pmatrix}\in H$"],
                  r"קודם מוצאים את $a$, ורק אחר כך אפשר להציב $a^{-1}=x$ בחישוב $b$."),
            bug("באיזו שורה יש טעות?",
                [r"נדרוש $\begin{pmatrix}x&y\\0&x^{-1}\end{pmatrix}\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}=I$",
                 r"מהאלכסון: $xa=1$, ולכן $a=x^{-1}$",
                 r"מהפינה הימנית העליונה: $xb+ya^{-1}=0$, ולכן $b=y$",
                 r"ההופכית היא $\begin{pmatrix}x^{-1}&y\\0&x\end{pmatrix}\in H$"],
                2, r"$a^{-1}=x$, ולכן $xb+yx=0$ ו-$b=-y$ ולא $y$."),
            num(r"נתון $y=3$ ב-$\mathbb{Z}_7$. מהו הערך של $b=-y$ בין $0$ ל-$6$?", 4, r"$-3\equiv4\pmod7$."),
        ]),
    (2, "ב"): dict(
        rubric=rub((r"מספר האפשרויות ל-$x$: $6$ (כל $x\ne0$)", 1), (r"מספר האפשרויות ל-$y$: $7$", 1), (r"הסדר $6\cdot7=42$", 2)),
        pitfalls=[r"לספור גם $x=0$: אז המטריצה אינה בעלת $x^{-1}$.",
                  r"לספור את $x^{-1}$ כבחירה נוספת: הוא נקבע לפי $x$."],
        steps=[
            num(r"כמה אפשרויות יש ל-$x$ ב-$\mathbb{Z}_7$ ($x\ne0$)?", 6, r"האיברים $1,\dots,6$."),
            num(r"כמה אפשרויות יש ל-$y$ ב-$\mathbb{Z}_7$?", 7, r"$y$ חופשי: $0,\dots,6$."),
            num(r"מהו $|H|$?", 42, r"לפי עקרון הכפל $6\cdot7=42$."),
        ]),
    (2, "ג"): dict(
        rubric=rub((r"$A^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}$", 2), (r"$k\equiv0\pmod7$ לראשונה ב-$k=7$, ולכן $o(A)=7$", 2)),
        pitfalls=[r"לשכוח שהחישוב מודולו $7$ ולהסיק שהסדר אינסופי.",
                  r"לעצור לפני $k=7$: $A^k\ne I$ לכל $1\le k\le6$."],
        steps=[
            num(r"מהו האיבר הימני-העליון ב-$A^5$ (מודולו $7$)?", 5, r"$A^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}$, ולכן $5$."),
            num(r"מהו האיבר הימני-העליון ב-$A^7$ מודולו $7$?", 0, r"$7\equiv0\pmod7$, ולכן $A^7=I$."),
            num(r"מהו הסדר של $A$?", 7, r"$k=7$ הוא החזקה החיובית הקטנה ביותר עם $A^k=I$."),
        ]),
    (2, "ד"): dict(
        rubric=rub((r"חישוב $A\bar u=\bar u\left(\bar u^T\bar u\right)=\bar u$ בעזרת אורתונורמליות", 4),
                   (r"אותו דבר ל-$\bar v$ ול-$\bar w$", 2), (r"$A$ קבועה על בסיס, ולכן $A=I$", 4)),
        pitfalls=[r"לשכוח ש-$\bar u^T\bar v=0$ (האורתוגונליות) מאפסת את שאר המחוברים.",
                  r"להסיק $A=I$ מכך ש-$A\bar u=\bar u$ לווקטור אחד בלבד."],
        steps=[
            order("סדרו את שלבי ההוכחה.",
                  [r"$A\bar u=\left(\bar u\bar u^T+\bar v\bar v^T+\bar w\bar w^T\right)\bar u$",
                   r"$=\bar u\left(\bar u^T\bar u\right)+\bar v\left(\bar v^T\bar u\right)+\bar w\left(\bar w^T\bar u\right)$",
                   r"$=\bar u\cdot1+\bar v\cdot0+\bar w\cdot0=\bar u$ (אורתונורמליות)",
                   r"באותו אופן $A\bar v=\bar v$ ו-$A\bar w=\bar w$",
                   r"$A\bar x=\bar x$ על בסיס, ולכן $A=I$"],
                  "הצבה, הוצאת הסקלרים, אורתונורמליות, הכללה לשאר הווקטורים, וסיכום."),
            bug("באיזו שורה יש טעות?",
                [r"$A\bar u=\left(\bar u\bar u^T+\bar v\bar v^T+\bar w\bar w^T\right)\bar u$",
                 r"$=\bar u\left(\bar u^T\bar u\right)+\bar v\left(\bar v^T\bar u\right)+\bar w\left(\bar w^T\bar u\right)$",
                 r"$=\bar u\cdot0+\bar v\cdot1+\bar w\cdot0=\bar u$"],
                2, r"$\bar u^T\bar u=\|\bar u\|^2=1$ ו-$\bar v^T\bar u=\bar w^T\bar u=0$, כלומר $\bar u\cdot1+\bar v\cdot0+\bar w\cdot0$."),
            ch(r"מדוע $A\bar x=\bar x$ על $\bar u,\bar v,\bar w$ גוררת $A=I$?", "כי העתקה לינארית נקבעת לפי פעולתה על בסיס",
               [r"כי $\bar u$ הוא וקטור יחידה", r"כי $A$ סימטרית"],
               r"$A$ ו-$I$ מתלכדות על בסיס של $\mathbb{R}^3$. סימטריה או נרמול של וקטור אחד אינם מספיקים (למשל $\bar u\bar u^T$ סימטרית ואינה $I$).", 2),
        ]),
    (3, "א"): dict(
        rubric=rub((r"חישוב הפולינום האופייני: $(\lambda-k)\left(-\lambda^2+2k\lambda+k^2\right)$", 5),
                   (r"ערכים עצמיים $k,\ k(1-\sqrt2),\ k(1+\sqrt2)$", 3),
                   (r"לכל $k\ne0$ סימנים מעורבים: לא חיובית/שלילית (לחלוטין)", 4),
                   (r"המקרה $k=0$: מטריצת האפס", 3)),
        pitfalls=[r"לשכוח את המקרה $k=0$, שבו כל הערכים העצמיים אפס.",
                  r"לשכוח ש-$1-\sqrt2<0$: הסימן של $k(1-\sqrt2)$ הפוך לסימן של $k$."],
        steps=[
            num(r"עבור $k=1$, מהו הערך העצמי $k(1-\sqrt2)$ (ערך מספרי)?", -0.4142136, r"$1-\sqrt2\approx-0.414$.", 0.001),
            num(r"עבור $k=-3$, כמה ערכים עצמיים שליליים יש למטריצה?", 2,
                r"הערכים: $-3$, $-3(1-\sqrt2)\approx1.24$, $-3(1+\sqrt2)\approx-7.24$. שניים שליליים."),
            ch(r"מהי המטריצה עבור $k=0$?", "מטריצת האפס: מוגדרת חיובית וגם מוגדרת שלילית (לא לחלוטין)",
               ["מוגדרת חיובית לחלוטין", "מוגדרת שלילית לחלוטין", "לא מוגדרת"],
               r"כל הערכים העצמיים הם $0$: $\bar v^TA\bar v=0\ge0$ וגם $\le0$, אבל לא $>0$ ולא $<0$.", 1),
        ]),
    (3, "ב"): dict(
        rubric=rub((r"סגירות: $\begin{pmatrix}1&n\\0&1\end{pmatrix}\begin{pmatrix}1&m\\0&1\end{pmatrix}=\begin{pmatrix}1&m+n\\0&1\end{pmatrix}$", 3),
                   ("אסוציאטיביות כפל מטריצות", 1), (r"איבר ניטרלי ($n=0$)", 2), (r"הופכי: $n\mapsto-n$", 2),
                   ("הסדר אינסופי", 2)),
        pitfalls=[r"לשכוח למצוא את הסדר של $G$ (השאלה מבקשת גם אותו).",
                  r"לסמן את ההופכי $1/n$: בחבורה זו החיבור בפינה, ולכן ההופכי הוא $-n$."],
        steps=[
            num(r"מהו האיבר הימני-העליון במכפלת $\begin{pmatrix}1&3\\0&1\end{pmatrix}\begin{pmatrix}1&4\\0&1\end{pmatrix}$?", 7, r"$n+m=3+4=7$."),
            num(r"מהו האיבר הימני-העליון בהופכי של $\begin{pmatrix}1&5\\0&1\end{pmatrix}$?", -5, r"ההופכי הוא $\begin{pmatrix}1&-5\\0&1\end{pmatrix}$."),
            ch(r"מהו הסדר של $G$?", r"אינסופי, כי לכל $n\in\mathbb{Z}$ מתאימה מטריצה שונה",
               [r"$7$", r"$1$"],
               r"ה-$n$ בפינה מזהה את המטריצה, ו-$\mathbb{Z}$ אינסופית; לכן אין סדר סופי.", 1),
        ]),
    (4, "א"): dict(
        rubric=rub((r"$a\odot b=ab+a+b$ מכפלה וסכום של שלמים", 2), (r"התוצאה שייכת ל-$\mathbb{Z}$, ולכן $\odot$ פעולה בינארית", 1)),
        pitfalls=[r"לבדוק רק שהביטוי מוגדר ולא שהתוצאה נשארת ב-$\mathbb{Z}$."],
        steps=[
            num(r"מהו $2\odot3$?", 11, r"$2\cdot3+2+3=11$."),
            num(r"מהו $(-4)\odot5$?", -19, r"$-20-4+5=-19$, שלם."),
        ]),
    (4, "ב"): dict(
        rubric=rub((r"פיתוח $(a\odot b)\odot c=abc+ab+ac+bc+a+b+c$", 2), (r"פיתוח $a\odot(b\odot c)$ לאותו ביטוי והמסקנה שהפעולה אסוציאטיבית", 2)),
        pitfalls=[r"לבדוק אסוציאטיביות על דוגמה אחת בלבד: דוגמה מראה אי-אסוציאטיביות, אך לא מוכיחה אסוציאטיביות."],
        steps=[
            num(r"מהו $(1\odot2)\odot3$?", 23, r"$1\odot2=5$ ו-$5\odot3=15+5+3=23$."),
            num(r"מהו $1\odot(2\odot3)$?", 23, r"$2\odot3=11$ ו-$1\odot11=11+1+11=23$."),
            ch(r"מהו הפיתוח המשותף של $(a\odot b)\odot c$ ו-$a\odot(b\odot c)$?", r"$abc+ab+ac+bc+a+b+c$",
               [r"$abc+a+b+c$", r"$abc+ab+ac+bc$"],
               r"פתיחת הסוגריים נותנת את כל המכפלות הזוגיות ואת $a+b+c$. הבחירות האחרות מחסירות מחוברים.", 0),
        ]),
    (4, "ג"): dict(
        rubric=rub((r"נדרוש $a\odot e=a$ לכל $a$: $e(a+1)=0$", 2), (r"בחירת $a=1$ נותנת $e=0$, והוא ניטרלי", 2)),
        pitfalls=[r"לבדוק רק $a\odot e=a$ ולא את $e\odot a=a$ (כאן הפעולה חילופית, ולכן זה מספיק).",
                  r"לבחור $a=-1$, שנותן $0=0$ ואינו חושף מידע על $e$."],
        steps=[
            ch(r"מ-$e(a+1)=0$ לכל $a\in\mathbb{Z}$: איזה ערך של $a$ מוביל ישירות ל-$e$?", r"$a=1$, ואז $2e=0$",
               [r"$a=-1$, ואז $0\cdot e=0$"],
               r"עבור $a=-1$ המשוואה אינה תלויה ב-$e$. עבור $a=1$ מקבלים $2e=0$.", 0),
            num(r"מהו האיבר הניטרלי $e$?", 0, r"$2e=0$ ולכן $e=0$; ואכן $a\odot0=a$."),
        ]),
    (4, "ד"): dict(
        rubric=rub((r"הניטרלי הוא $0$, ולכן הופכי של $a$ הוא $b$ עם $a\odot b=0$", 1), (r"עבור $a=-1$: $(-1)\odot b=-1\ne0$ לכל $b$", 2),
                   ("מסקנה: אין הופכי ולכן אינה חבורה", 1)),
        pitfalls=[r"לחפש הופכי ביחס ל-$1$ (הכפל הרגיל) ולא ביחס לניטרלי $0$ של $\odot$.",
                  r"להסיק שאין חבורה בלי להצביע על איבר אחד ספציפי ללא הופכי."],
        steps=[
            num(r"מהו $(-1)\odot7$?", -1, r"$-7-1+7=-1$."),
            ch(r"מדוע $(\mathbb{Z},\odot)$ אינה חבורה?", r"ל-$-1$ אין הופכי: $(-1)\odot b=-1\ne0$ לכל $b$",
               [r"הפעולה אינה אסוציאטיבית", r"אין איבר ניטרלי"],
               r"סעיפים ב-ג הראו שהפעולה אסוציאטיבית ושהניטרלי הוא $0$, ולכן הכשל הוא בהופכי.", 0),
        ]),
    (4, "ה"): dict(
        rubric=rub((r"שוויון הנורמות שקול לשוויון ריבועי הנורמות", 2), (r"פיתוח $\|\bar u\pm\bar v\|^2$", 4),
                   (r"צמצום והסקת $\langle\bar u,\bar v\rangle=0$", 2), ("הכיוון ההפוך (שקילות)", 2)),
        pitfalls=[r"להוכיח רק כיוון אחד: צריך ״אם ורק אם״ (או שרשרת שקילויות).",
                  r"לשכוח את הגורם $2$ במכפלה הפנימית: $\|\bar u\pm\bar v\|^2=\|\bar u\|^2\pm2\langle\bar u,\bar v\rangle+\|\bar v\|^2$."],
        steps=[
            order("סדרו את שרשרת השקילויות.",
                  [r"$\|\bar u-\bar v\|=\|\bar u+\bar v\|\iff\|\bar u-\bar v\|^2=\|\bar u+\bar v\|^2$ (נורמות אי-שליליות)",
                   r"$\iff\|\bar u\|^2-2\langle\bar u,\bar v\rangle+\|\bar v\|^2=\|\bar u\|^2+2\langle\bar u,\bar v\rangle+\|\bar v\|^2$",
                   r"$\iff-2\langle\bar u,\bar v\rangle=2\langle\bar u,\bar v\rangle\iff\langle\bar u,\bar v\rangle=0$",
                   r"$\iff\bar u\perp\bar v$"],
                  "ריבוע, פיתוח, צמצום, ואז הגדרת האורתוגונליות."),
            bug("באיזו שורה יש טעות?",
                [r"$\|\bar u-\bar v\|=\|\bar u+\bar v\|\iff\|\bar u-\bar v\|^2=\|\bar u+\bar v\|^2$",
                 r"$\iff\|\bar u\|^2-2\langle\bar u,\bar v\rangle+\|\bar v\|^2=\|\bar u\|^2-2\langle\bar u,\bar v\rangle+\|\bar v\|^2$",
                 r"$\iff\langle\bar u,\bar v\rangle=0$"],
                1, r"ב-$\|\bar u+\bar v\|^2$ הסימן של $2\langle\bar u,\bar v\rangle$ הוא פלוס."),
            num(r"$\bar u=(1,0)$ ו-$\bar v=(1,1)$. מהו $\|\bar u+\bar v\|^2-\|\bar u-\bar v\|^2$?", 4,
                r"$\|\bar u+\bar v\|^2=5$, $\|\bar u-\bar v\|^2=1$, והפרשם $4\langle\bar u,\bar v\rangle=4$."),
        ]),
    (5, "א"): dict(
        rubric=rub((r"$A^TA=\begin{pmatrix}5&0\\0&9\end{pmatrix}$", 3), (r"ערכים סינגולריים $3,\sqrt5$", 4), (r"$V$ מווקטורים עצמיים של $A^TA$", 3),
                   (r"$U$: $u_i=Av_i/\sigma_i$ והשלמה לבסיס אורתונורמלי", 5)),
        pitfalls=[r"לסדר את הערכים הסינגולריים בסדר עולה: ב-$\Sigma$ הם בסדר יורד ($3\ge\sqrt5$).",
                  r"לשכוח להתאים את סדר עמודות $V$ לסדר $\sigma_i$."],
        steps=[
            num(r"מהו האיבר הראשון (השמאלי-עליון) ב-$A^TA$?", 5, r"$2^2+1^2+0^2=5$."),
            num(r"מהו הערך הסינגולרי הגדול $\sigma_1$?", 3, r"$A^TA=\operatorname{diag}(5,9)$, והגדול $\sqrt9=3$."),
            num(r"מהו הערך הסינגולרי $\sigma_2$ (ערך מספרי)?", 2.236068, r"$\sqrt5\approx2.236$.", 0.001),
            num(r"$v_1=(0,1)^T$. מהו הרכיב הראשון של $u_1=Av_1/\sigma_1$ (ערך מספרי)?", 0.3333333,
                r"$Av_1=(1,-2,2)^T$ ו-$u_1=\frac13(1,-2,2)^T$.", 0.001),
        ]),
    (5, "ג"): dict(
        rubric=rub((r"שימוש במשפט השאריות הסיני (מודולים $3,5,11$ זרים, $m=165$)", 4), (r"התשובה $x\equiv112\pmod{165}$", 6)),
        pitfalls=[r"לשכוח לצמצם את התשובה מודולו $165$.",
                  r"להשתמש במודולים שאינם זרים בזוגות."],
        steps=[
            num(r"מהו $m=3\cdot5\cdot11$?", 165, r"המודולים זרים בזוגות."),
            num(r"מהי השארית של $112$ בחלוקה ב-$11$?", 2, r"$112=10\cdot11+2$, כנדרש."),
            num(r"מהו הפתרון $x$ בין $0$ ל-$164$?", 112, r"$112\equiv1\pmod3$, $\equiv2\pmod5$, $\equiv2\pmod{11}$."),
        ]),
    (6, "ב"): dict(
        rubric=rub((r"ערכים עצמיים $5,2,2$", 4), ("וקטורים עצמיים: $(1,1,1)$ ובסיס למרחב $x+y+z=0$", 4),
                   ("אורתונורמליזציה (גרם-שמידט במרחב העצמי של $2$)", 4), (r"$A=QDQ^T$", 3)),
        pitfalls=[r"לשכוח שבתוך המרחב העצמי של הערך הכפול צריך בסיס אורתוגונלי (לא רק בלתי תלוי).",
                  r"לשכוח לנרמל ולכן לקבל $Q$ שאינה אורתוגונלית."],
        steps=[
            num(r"מהו הערך העצמי הגדול של $A$?", 5, r"$A(1,1,1)^T=5(1,1,1)^T$."),
            num(r"מהו הריבוי האלגברי של הערך העצמי $2$?", 2, r"הערכים העצמיים: $5,2,2$."),
            ch(r"איזה וקטור הוא וקטור עצמי של $A$ עבור $5$?", r"$(1,1,1)^T$", [r"$(1,-1,0)^T$", r"$(1,1,-2)^T$"],
               r"$A(1,-1,0)^T=2(1,-1,0)^T$ ו-$A(1,1,-2)^T=2(1,1,-2)^T$: אלה וקטורים עצמיים של $2$.", 0),
            num(r"מהו האורך של $(1,1,1)^T$ שמנרמלים (ערך מספרי)?", 1.7320508, r"$\sqrt3\approx1.732$.", 0.001),
        ]),
    (6, "ג"): dict(
        rubric=rub((r"הגדרת $\bar u=\left(\sqrt{a_i/b_i}\right)$ ו-$\bar v=\left(\sqrt{a_ib_i}\right)$", 4), (r"חישוב $\langle\bar u,\bar v\rangle=\sum a_i$ והנורמות", 3),
                   (r"קושי-שוורץ וחלוקה ב-$\sum a_ib_i$", 3)),
        pitfalls=[r"לבחור וקטורים שהמכפלה הפנימית שלהם אינה $\sum a_i$.",
                  r"לשכוח ש-$a_i,b_i>0$ (נדרש לשורשים ולחלוקה)."],
        steps=[
            ch(r"לאילו וקטורים מיישמים את קושי-שוורץ?", r"$\bar u=\left(\sqrt{a_i/b_i}\right)_i$ ו-$\bar v=\left(\sqrt{a_ib_i}\right)_i$",
               [r"$\bar u=\left(a_i/b_i\right)_i$ ו-$\bar v=\left(a_ib_i\right)_i$", r"$\bar u=\left(\sqrt{a_i}\right)_i$ ו-$\bar v=\left(\sqrt{b_i}\right)_i$"],
               r"רק בבחירה הראשונה $\langle\bar u,\bar v\rangle=\sum a_i$. בשתי האחרות מקבלים $\sum a_i^2$ או $\sum\sqrt{a_ib_i}$.", 1),
            order("סדרו את שלבי ההוכחה.",
                  [r"נגדיר $\bar u=\left(\sqrt{a_i/b_i}\right)_i$ ו-$\bar v=\left(\sqrt{a_ib_i}\right)_i$",
                   r"$\langle\bar u,\bar v\rangle=\sum a_i$, $\|\bar u\|^2=\sum\frac{a_i}{b_i}$, $\|\bar v\|^2=\sum a_ib_i$",
                   r"קושי-שוורץ: $\langle\bar u,\bar v\rangle^2\le\|\bar u\|^2\|\bar v\|^2$",
                   r"נחלק ב-$\sum a_ib_i>0$: $\dfrac{\left(\sum a_i\right)^2}{\sum a_ib_i}\le\sum\dfrac{a_i}{b_i}$"],
                  "הגדרה, חישוב, אי-שוויון, חלוקה."),
            bug("באיזו שורה יש טעות?",
                [r"נגדיר $\bar u=\left(\sqrt{a_i/b_i}\right)_i$ ו-$\bar v=\left(\sqrt{a_ib_i}\right)_i$",
                 r"$\langle\bar u,\bar v\rangle=\sum a_i^2$, $\|\bar u\|^2=\sum\frac{a_i}{b_i}$, $\|\bar v\|^2=\sum a_ib_i$",
                 r"קושי-שוורץ: $\langle\bar u,\bar v\rangle^2\le\|\bar u\|^2\|\bar v\|^2$"],
                1, r"$\sqrt{a_i/b_i}\cdot\sqrt{a_ib_i}=a_i$, ולכן המכפלה הפנימית היא $\sum a_i$."),
            num(r"עבור $a=(1,1)$ ו-$b=(1,2)$, מהו הפרש האגפים $\sum\frac{a_i}{b_i}-\frac{\left(\sum a_i\right)^2}{\sum a_ib_i}$ (ערך מספרי)?", 0.1666667,
                r"$1.5-\frac43=\frac16\ge0$.", 0.001),
        ]),
}
for _q in questions:
    _s = S25BA.get((_q["num"], _q.get("part")))
    assert _s is not None, ("no steps for", _q["num"], _q.get("part"))
    assert sum(r["points"] for r in _s["rubric"]) == _q["points"], ("rubric sum", _q["num"], _q.get("part"))
    _q["rubric"], _q["rubricSource"] = _s["rubric"], "ai-draft"
    _q["pitfalls"] = _s["pitfalls"]
    _q["steps"], _q["stepsSource"] = _s["steps"], "ai-draft"

exam = {
    "examCode": "25B-A",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ה מועד א'",
    "year": 2025,
    "examDate": "9.7.2025",
    "sourceFile": "algebra-2-25B-A-exam",
    "solutionFile": "algebra-2-25B-A-handwritten-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
