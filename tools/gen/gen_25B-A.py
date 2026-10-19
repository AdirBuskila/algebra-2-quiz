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
