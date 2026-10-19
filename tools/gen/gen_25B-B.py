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
