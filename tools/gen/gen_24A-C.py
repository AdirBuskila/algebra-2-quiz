# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-C.json -- algebra-2 (20079), semester A 2024, moed C (no date printed).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-C.py

Source: the file "moed C - solution" is 15 pages: exam page 1 (Q1-Q2), then a handwritten (digital pen) student
solution page by page, with exam page 2 (Q3-Q5) at page 7. The exam sheet exists only inside this file. The header
says semester A tashpad, moed C, no date. Code 24A-C (no header typo here).
The file also contains three pages that are NOT questions of this sitting and are skipped: a word-problem
forecasting question (p.4, "week 5 forecast", not on the exam sheet) and a copy of the sum-of-squares >= 1/n proof
(p.6, that is 24A-B Q5b).

Student solution only (official: false, solutionSource student-solution, labelled "פתרון סטודנט"; the file carries
no author name). It covers Q1a, Q1b, Q2a(1-3), Q2b, Q4a, Q4b. NO answer source for Q3a (SVD), Q3b (polarization
identity), Q5a (Heisenberg group), Q5b (x*x=e => abelian-type proof): were held "no-key"; now solved by the
solver (SOLVED below: solutionSource "solved", official false, confidence high, pending the refuter; checks in
tools/verify/24A-C/solve_24AC.py, all OK). Q3a: SVD via AA^T (2x2), sigma = sqrt3, 1, v3 from ker A.

Part letters (single letters only): Q2: a.1..a.3 -> a..c, printed b -> d.

Notes on the student solution (checked with tools/verify/24A-C/check.py, all OK):
- Q2a: the structure is not even closed ((1,0)*(1,0)=(0,0) is outside R^2 minus the origin); the student argues
  "no inverse for (a,0)", which already shows it is not a group. Written as the student has it.
- Q4b: the student's first attempt (page 10) wrote the residues of the 24A-A system; the corrected attempt
  (x=2 mod 3, 0 mod 2, 6 mod 7 -> x=20 mod 42) is the one transcribed. Q4a: the student draws the eigenvalue
  signs on number lines; summarised in words.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-C.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "high"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"נתון מבנה אלגברי $\left(\mathbb{R}^2\setminus\{(0,0)\},*\right)$, כאשר פעולת $*$ מוגדרת באופן הבא: $\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ay+bx\\by\end{pmatrix}$ לכל $\begin{pmatrix}a\\b\end{pmatrix},\begin{pmatrix}x\\y\end{pmatrix}\in\mathbb{R}^2\setminus\{(0,0)\}$."},
}

S1A = (
    r"$y=mx+n$" "\n"
    r"$$\begin{cases}-4m+n=-1\\-2m+n=0\\2m+n=4\\4m+n=5\\5m+n=6\end{cases}\Rightarrow\begin{pmatrix}-4&1\\-2&1\\2&1\\4&1\\5&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}-1\\0\\4\\5\\6\end{pmatrix}\qquad A\vec x=\vec b$$" "\n"
    "אם נפתור את המערכת, בסבירות גבוהה לא נמצא פתרון כי אין ישר שעובר דרך כל הנקודות. לכן פותרים את בעיית הריבועים הפחותים $A^TA\\vec x=A^T\\vec b$:\n"
    r"$$A^TA=\begin{pmatrix}65&5\\5&5\end{pmatrix},\qquad A^T\vec b=\begin{pmatrix}62\\14\end{pmatrix}$$" "\n"
    r"$$\begin{cases}65m+5n=62\\5m+5n=14\end{cases}\Rightarrow60m=48\Rightarrow m=\frac45,\qquad5\cdot\frac45+5n=14\Rightarrow n=2$$" "\n"
    r"$$y=\frac45x+2$$"
)

S1B = (
    r"לפי קושי-שוורץ $\langle u,v\rangle\le\|u\|\cdot\|v\|$; לפי הצורה של הביטוי, $\langle f,g\rangle\le\|f\|\cdot\|g\|$ עבור $g(x)=x^3$ ו-$f(x)=f(x)$, כאשר $\langle f,g\rangle=\int_0^1x^3f(x)\,dx$." "\n"
    r"$$\|f\|=\sqrt{\langle f,f\rangle}=\sqrt{\int_0^1f^2(x)\,dx},\qquad\|g\|=\|x^3\|=\sqrt{\langle x^3,x^3\rangle}=\sqrt{\int_0^1x^6\,dx}=\sqrt{\left.\frac{x^7}7\right|_0^1}=\sqrt{\frac17}$$" "\n"
    r"$$\int_0^1x^3f(x)\,dx\le\sqrt{\int_0^1f^2(x)\,dx}\cdot\sqrt{\frac17}$$" "\n"
    r"נעלה בריבוע: $$\left(\int_0^1x^3f(x)\,dx\right)^2\le\frac17\int_0^1f^2(x)\,dx$$"
)

S2A1 = (
    r"$$\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ay+bx\\by\end{pmatrix},\qquad\begin{pmatrix}x\\y\end{pmatrix}*\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}xb+ya\\yb\end{pmatrix}$$" "\n"
    "שני האגפים שווים, לכן הפעולה קומוטטיבית."
)

S2A2 = (
    r"נחפש $\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}e_1\\e_2\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}$:" "\n"
    r"$$\begin{pmatrix}ae_2+be_1\\be_2\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}\Rightarrow\begin{cases}ae_2+be_1=a\\be_2=b\end{cases}\Rightarrow e_2=1$$" "\n"
    r"$$a\cdot1+be_1=a\Rightarrow be_1=0\Rightarrow e_1=0$$" "\n"
    r"$$e=\begin{pmatrix}0\\1\end{pmatrix}$$"
)

S2A3 = (
    "נבדוק את התנאים: הופכי, אסוציאטיביות, סגירות.\n"
    r"**הופכי:** נחפש $\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}a^{-1}\\b^{-1}\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix}$, כלומר $\begin{pmatrix}ab^{-1}+ba^{-1}\\bb^{-1}\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix}$. נדרש $bb^{-1}=1$, כלומר $b^{-1}=\dfrac1b$ ($b\ne0$). לוקטורים מהצורה $\begin{pmatrix}a\\0\end{pmatrix}$ אין הופכי." "\n"
    "לכן המבנה אינו חבורה."
)

S2B = (
    r"נוכיח ש-$I+A^2$ סימטרית, וש-$\langle(I+A^2)\vec v,\vec v\rangle>0$ לכל $\vec0\ne\vec v\in\mathbb{R}^n$." "\n"
    r"**(I)** $(I+A^2)^T=I^T+(A^2)^T=I+(A^T)^2=I+A^2$, כי $I^T=I$, $A^T=A$ ו-$(A^k)^T=(A^T)^k$." "\n"
    r"**(II)** $\langle(I+A^2)\vec v,\vec v\rangle=\vec v^T(I+A^2)\vec v=\vec v^TI\vec v+\vec v^TA^2\vec v>0$." "\n"
    r"ביאור $\vec v^TI\vec v$: $\vec v^TI\vec v=\vec v^T\vec v=\|\vec v\|^2>0$ לכל $\vec v\ne\vec0$ (דרך נוספת: $I$ מוגדרת חיובית לחלוטין כי $\lambda=1>0$)." "\n"
    r"ביאור $\vec v^TA^2\vec v$: $\vec v^TA\cdot A\vec v=\vec v^TA^TA\vec v=(A\vec v)^T(A\vec v)=\vec u^T\vec u=\|\vec u\|^2\ge0$, כאשר $A^T=A$, $(AB)^T=B^TA^T$ ו-$\vec u=A\vec v$." "\n"
    r"מכאן $\langle(I+A^2)\vec v,\vec v\rangle>0$, ולכן $I+A^2$ מוגדרת חיובית לחלוטין."
)

S4A = (
    r"$\lambda>0$ לכל $\lambda$: מוגדרת חיובית לחלוטין; $\lambda\ge0$ לכל $\lambda$: מוגדרת חיובית; $\lambda<0$: שלילית לחלוטין; $\lambda\le0$: שלילית." "\n"
    r"$$\begin{vmatrix}a^2-\lambda&0&1\\0&a-\lambda&0\\1&0&a^2-\lambda\end{vmatrix}=(a-\lambda)\left((a^2-\lambda)^2-1^2\right)=0$$" "\n"
    r"$$a-\lambda=0\Rightarrow\lambda=a,\qquad(a^2-\lambda)^2-1=0\Rightarrow\left((a^2-\lambda)-1\right)\left((a^2-\lambda)+1\right)=0\Rightarrow\lambda=a^2-1,\ \ \lambda=a^2+1$$" "\n"
    r"הערכים העצמיים הם $a$, $a^2-1$, $a^2+1$. (בדיקה נוספת של הפולינום: $\lambda^2-2a^2\lambda+a^4-1=0$ נותן $\lambda=\dfrac{2a^2\pm\sqrt4}2=a^2\pm1$.)" "\n"
    r"- $\lambda>0$ לכל ערך עצמי $\Leftarrow$ $a>1$: מוגדרת חיובית לחלוטין." "\n"
    r"- $\lambda\ge0$ לכל ערך עצמי $\Leftarrow$ $a\ge1$: מוגדרת חיובית." "\n"
    r"- עבור $a<1$ המטריצה אינה מוגדרת (לא שלילית: $a^2+1>0$ תמיד)."
)

S4B = (
    r"נסדר את המקדמים: $x\equiv2\pmod3$ (כי $5\equiv2$), $x\equiv0\pmod2$ (כי $4\equiv0$), $x\equiv6\pmod7$." "\n"
    r"$a_1=2,\ a_2=0,\ a_3=6$; $m_1=3,\ m_2=2,\ m_3=7$; $M_1=2\cdot7=14,\ M_2=21,\ M_3=6$; $x_1=2,\ x_2=1,\ x_3=6$." "\n"
    r"$$x_iM_i\equiv1\pmod{m_i}:\quad2\cdot14\equiv1\pmod3,\quad1\cdot21\equiv1\pmod2,\quad6\cdot6\equiv1\pmod7$$" "\n"
    r"$$x\equiv(a_1M_1x_1+\dots+a_kM_kx_k)\pmod{m_1m_2\cdots m_k}=(2\cdot14\cdot2+0\cdot21\cdot1+6\cdot6\cdot6)\pmod{3\cdot2\cdot7}=272\pmod{42}$$" "\n"
    r"$$x=20\pmod{42}$$" "\n"
    r"בדיקה: $20\equiv5\pmod3$, $20\equiv4\pmod2$, $20\equiv6\pmod7$."
)

questions = [
    Q(1, "computation", "least_squares",
      r"נתונות 5 הנקודות במישור $(-4,-1),(-2,0),(2,4),(4,5),(5,6)$ מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים. (12%)",
      S1A, part="א", points=12),
    Q(1, "proof", "cauchy_schwarz",
      r"הוכיחו כי $\left(\int_0^1x^3f(x)\,dx\right)^2\le\dfrac17\int_0^1f^2(x)\,dx$ כאשר $f(x)\in C_{[0,1]}$. (13%)",
      S1B, part="ב", points=13, confidence="med"),

    Q(2, "truefalse", "groups", r"סעיף א.1. האם הפעולה היא קומוטטיבית? (5%)", S2A1, part="א", points=5, contextId="c2", verdict=True),
    Q(2, "computation", "groups", r"סעיף א.2. מצאו את האיבר הניטרלי ביחס לפעולת $*$ (במידה וקיים). (6%)", S2A2, part="ב", points=6,
      contextId="c2"),
    Q(2, "truefalse", "groups", r"סעיף א.3. האם המבנה $\left(\mathbb{R}^2\setminus\{(0,0)\},*\right)$ הוא חבורה? (7%)", S2A3, part="ג",
      points=7, contextId="c2", verdict=False, confidence="med"),
    Q(2, "proof", "pos_def", r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית לחלוטין. הוכיחו כי $I+A^2$ מוגדרת חיובית לחלוטין. (7%)", S2B,
      part="ד", points=7, confidence="med"),

    {"num": 3, "part": "א", "kind": "computation", "topic": "svd", "points": 18,
     "question": r"מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}0&-1&1\\1&1&0\end{pmatrix}$. (18%)",
     "hold": "no-key: the file has no solution for this question"},
    {"num": 3, "part": "ב", "kind": "proof", "topic": "inner_product", "points": 7,
     "question": r"יהי $V$ מרחב מכפלה פנימית ממשי. הוכיחו כי עבור כל $\vec v,\vec u\in V$ מתקיים $\langle\vec u,\vec v\rangle=\dfrac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$. (7%)",
     "hold": "no-key: the file has no solution for this question"},

    Q(4, "computation", "pos_def",
      r"(17%) עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}a^2&0&1\\0&a&0\\1&0&a^2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S4A, part="א", points=17),
    Q(4, "computation", "crt",
      r"פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv5\pmod3\\x\equiv4\pmod2\\x\equiv6\pmod7\end{cases}$. (8%)",
      S4B, part="ב", points=8),

    {"num": 5, "part": "א", "kind": "proof", "topic": "groups", "points": 18,
     "question": r"הוכיחו כי הקבוצה $G=\left\{A=\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}\in M_3(\mathbb{R})\ \middle|\ a,b,c\in\mathbb{R}\right\}$ עם כפל מטריצות מהווה חבורה. (18%)",
     "hold": "no-key: the file has no solution for this question"},
    {"num": 5, "part": "ב", "kind": "proof", "topic": "groups", "points": 7,
     "question": r"תהי $(G,*)$ חבורה כך שלכל $x\in G$ מתקיים $x*x=e$, כלומר $x^{-1}=x$. יהיו $a,b\in G$. נסמן $c=(a*b)*a$. הוכיחו כי $c=b$. (7%)",
     "hold": "no-key: the file has no solution for this question"},
]

# ------------------------------------------------------------------ solver solutions (no key; checked by
# tools/verify/24A-C/solve_24AC.py, all OK). solutionSource "solved", official false, pending the refuter.
SOLVED = {
    (3, "א"): (
        r"$A$ מסדר $2\times3$, לכן נעבוד עם המטריצה הקטנה $AA^T$ ($2\times2$):" "\n"
        r"$$AA^T=\begin{pmatrix}0&-1&1\\1&1&0\end{pmatrix}\begin{pmatrix}0&1\\-1&1\\1&0\end{pmatrix}=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad|AA^T-\lambda I|=(2-\lambda)^2-1=0\Rightarrow\lambda_1=3,\ \lambda_2=1$$" "\n"
        r"הערכים הסינגולריים: $\sigma_1=\sqrt3$, $\sigma_2=1$, ולכן $\Sigma=\begin{pmatrix}\sqrt3&0&0\\0&1&0\end{pmatrix}$." "\n"
        r"**וקטורים עצמיים של $AA^T$ (עמודות $U$):** עבור $\lambda=3$: $\begin{pmatrix}-1&-1\\-1&-1\end{pmatrix}\vec u=\vec0\Rightarrow\vec u_1=\frac1{\sqrt2}\begin{pmatrix}-1\\1\end{pmatrix}$. עבור $\lambda=1$: $\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\vec u=\vec0\Rightarrow\vec u_2=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$." "\n"
        r"**עמודות $V$:** $\vec v_i=\frac1{\sigma_i}A^T\vec u_i$:" "\n"
        r"$$\vec v_1=\frac1{\sqrt3}\cdot\frac1{\sqrt2}\begin{pmatrix}0&1\\-1&1\\1&0\end{pmatrix}\begin{pmatrix}-1\\1\end{pmatrix}=\frac1{\sqrt6}\begin{pmatrix}1\\2\\-1\end{pmatrix},\qquad\vec v_2=\frac11\cdot\frac1{\sqrt2}\begin{pmatrix}0&1\\-1&1\\1&0\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1\\0\\1\end{pmatrix}$$" "\n"
        r"את $\vec v_3$ משלימים לבסיס אורתונורמלי של $\mathbb{R}^3$ מתוך $\ker A$ (ערך עצמי $0$ של $A^TA$): $A\vec x=\vec0\Rightarrow-x_2+x_3=0,\ x_1+x_2=0\Rightarrow\vec v_3=\frac1{\sqrt3}\begin{pmatrix}-1\\1\\1\end{pmatrix}$ (אורתוגונלי ל-$\vec v_1,\vec v_2$)." "\n"
        r"$$A=U\Sigma V^T,\qquad U=\begin{pmatrix}-\frac1{\sqrt2}&\frac1{\sqrt2}\\\frac1{\sqrt2}&\frac1{\sqrt2}\end{pmatrix},\quad\Sigma=\begin{pmatrix}\sqrt3&0&0\\0&1&0\end{pmatrix},\quad V=\begin{pmatrix}\frac1{\sqrt6}&\frac1{\sqrt2}&-\frac1{\sqrt3}\\\frac2{\sqrt6}&0&\frac1{\sqrt3}\\-\frac1{\sqrt6}&\frac1{\sqrt2}&\frac1{\sqrt3}\end{pmatrix}$$" "\n"
        r"בדיקה: $U^TU=I$, $V^TV=I$ ו-$U\Sigma V^T=A$. (הפירוק אינו יחיד: אפשר להחליף סימן של זוג $\vec u_i,\vec v_i$ יחד, ושל $\vec v_3$.)"
    ),
    (3, "ב"): (
        r"נפתח את שני הריבועים לפי לינאריות וסימטריה של המכפלה הפנימית הממשית ($\langle\vec v,\vec u\rangle=\langle\vec u,\vec v\rangle$):" "\n"
        r"$$\|\vec u+\vec v\|^2=\langle\vec u+\vec v,\vec u+\vec v\rangle=\langle\vec u,\vec u\rangle+\langle\vec u,\vec v\rangle+\langle\vec v,\vec u\rangle+\langle\vec v,\vec v\rangle=\|\vec u\|^2+2\langle\vec u,\vec v\rangle+\|\vec v\|^2$$" "\n"
        r"$$\|\vec u-\vec v\|^2=\langle\vec u-\vec v,\vec u-\vec v\rangle=\langle\vec u,\vec u\rangle-\langle\vec u,\vec v\rangle-\langle\vec v,\vec u\rangle+\langle\vec v,\vec v\rangle=\|\vec u\|^2-2\langle\vec u,\vec v\rangle+\|\vec v\|^2$$" "\n"
        r"נחסר את השוויון השני מהראשון:" "\n"
        r"$$\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2=4\langle\vec u,\vec v\rangle\ \Rightarrow\ \langle\vec u,\vec v\rangle=\frac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)\qquad\blacksquare$$" "\n"
        r"(הסימטריה היא המקום שבו משתמשים בכך שהמרחב ממשי: $\langle\vec u,\vec v\rangle+\langle\vec v,\vec u\rangle=2\langle\vec u,\vec v\rangle$.)"
    ),
    (5, "א"): (
        r"נסמן $A(a,b,c)=\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}$ ונבדוק את אקסיומות החבורה." "\n"
        r"**סגירות:** לכל $a_1,b_1,c_1,a_2,b_2,c_2\in\mathbb{R}$:" "\n"
        r"$$A(a_1,b_1,c_1)\cdot A(a_2,b_2,c_2)=\begin{pmatrix}1&a_1+a_2&b_2+a_1c_2+b_1\\0&1&c_1+c_2\\0&0&1\end{pmatrix}=A(a_1+a_2,\ b_1+b_2+a_1c_2,\ c_1+c_2)\in G$$" "\n"
        r"כי הרכיבים ממשיים והמבנה (אלכסון $1$, אפסים מתחת לאלכסון) נשמר." "\n"
        r"**אסוציאטיביות:** כפל מטריצות ב-$M_3(\mathbb{R})$ אסוציאטיבי, ובפרט על אברי $G$: $(XY)Z=X(YZ)$." "\n"
        r"**איבר ניטרלי:** $I=A(0,0,0)\in G$ ומתקיים $XI=IX=X$ לכל $X\in G$." "\n"
        r"**הופכי:** $\det A(a,b,c)=1\ne0$ (משולשית עם אלכסון $1$), ונמצא את ההופכי בתוך $G$: מהדרישה $A(a,b,c)A(x,y,z)=I$ לפי נוסחת הכפל: $a+x=0$, $c+z=0$, $b+y+az=0$, כלומר $x=-a$, $z=-c$, $y=ac-b$." "\n"
        r"$$A(a,b,c)^{-1}=\begin{pmatrix}1&-a&ac-b\\0&1&-c\\0&0&1\end{pmatrix}\in G$$" "\n"
        r"ובדיקה גם בכיוון השני: $A(-a,ac-b,-c)A(a,b,c)=A(0,\ ac-b+b-ac,\ 0)=I$." "\n"
        r"כל האקסיומות מתקיימות, לכן $G$ עם כפל מטריצות היא חבורה (לא אבלית). $\blacksquare$"
    ),
    (5, "ב"): (
        r"**שלב 1: $a*b=b*a$.** האיבר $a*b$ שייך ל-$G$, ולכן לפי הנתון $(a*b)^{-1}=a*b$. מצד שני, בכל חבורה $(a*b)^{-1}=b^{-1}*a^{-1}$, ולפי הנתון $a^{-1}=a$, $b^{-1}=b$. לכן" "\n"
        r"$$a*b=(a*b)^{-1}=b^{-1}*a^{-1}=b*a$$" "\n"
        r"**שלב 2:** נשתמש באסוציאטיביות ובנתון $a*a=e$:" "\n"
        r"$$c=(a*b)*a=(b*a)*a=b*(a*a)=b*e=b\qquad\blacksquare$$" "\n"
        r"(דרך שקולה: $(a*b)*(a*b)=e$; נכפול משמאל ב-$a$ ומימין ב-$b$ ונקבל $b*a=a*b$, ומשם כמו בשלב 2.)"
    ),
}
for q in questions:
    key = (q["num"], q.get("part"))
    if key in SOLVED and "hold" in q:
        del q["hold"]
        q.update({"solution": SOLVED[key], "solutionSource": "solved", "official": False, "confidence": "high"})
assert all("hold" not in q for q in questions), "an item is still held"

# ---- rubric / pitfalls / steps (ai-draft). Every expected value is recomputed by tools/verify/24A-C/steps_check.py ----
# Student-solution items (Q1, Q2, Q4) were re-derived with sympy first (steps_check.py section "student items").
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def num(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def choice(prompt, values, correct, explain):
    return {"type": "choice", "prompt": prompt, "options": opts(*values), "correctId": IDS[correct], "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def findbug(prompt, lines, idx, new, explain):
    bad = list(lines)
    bad[idx] = new
    return {"type": "findbug", "prompt": prompt, "lines": bad, "bugIndex": idx, "explain": explain}


def add(n, part, **kw):
    for q in questions:
        if q["num"] == n and q.get("part") == part:
            q.update(kw)
            q["rubricSource"] = "ai-draft"
            q["stepsSource"] = "ai-draft"
            assert sum(r["points"] for r in q["rubric"]) == q["points"], (n, part)
            return
    raise KeyError((n, part))


add(1, "א",
    rubric=rub((r"הצבת הנקודות וכתיבת המערכת $A\vec x=\vec b$", 3),
               (r"המעבר למשוואות הנורמליות $A^TA\vec x=A^T\vec b$ (אין פתרון מדויק)", 3),
               (r"$A^TA=\begin{pmatrix}65&5\\5&5\end{pmatrix}$ ו-$A^T\vec b=\begin{pmatrix}62\\14\end{pmatrix}$", 3),
               (r"הפתרון $m=\frac45,\ n=2$ והישר $y=\frac45x+2$", 3)),
    pitfalls=[r"לפתור את $A\vec x=\vec b$ ישירות (אין ישר שעובר דרך כל הנקודות).",
              r"לטעות בחישוב $\sum x_i^2$ (הערך הנכון $65$) או $\sum x_iy_i$ (הערך הנכון $62$)."],
    steps=[num(r"מהו $(A^TA)_{11}=\sum x_i^2$ עבור $x=-4,-2,2,4,5$?", 65, r"$16+4+4+16+25=65$."),
           num(r"מהו הרכיב הראשון של $A^T\vec b$, כלומר $\sum x_iy_i$?", 62, r"$4+0+8+20+30=62$."),
           num(r"מהו השיפוע $m$?", 0.8, r"מחיסור $5m+5n=14$ מ-$65m+5n=62$ מתקבל $60m=48$, כלומר $m=\frac45$.", tol=1e-9),
           num(r"מהו $n$?", 2, r"$5\cdot\frac45+5n=14$ ולכן $n=2$.")])

S1B_LINES = [r"נבחר $\langle f,g\rangle=\int_0^1fg\,dx$ ו-$g=x^3$, ולכן $\langle f,g\rangle=\int_0^1x^3f\,dx$",
             r"קושי-שוורץ: $\langle f,g\rangle\le\|f\|\|g\|$",
             r"$\|g\|^2=\int_0^1x^6\,dx=\left[\frac{x^7}7\right]_0^1=\frac17$",
             r"נעלה בריבוע: $\left(\int_0^1x^3f\,dx\right)^2\le\frac17\int_0^1f^2\,dx$"]
add(1, "ב",
    rubric=rub((r"זיהוי $\int_0^1x^3f$ כמכפלה פנימית של $f$ ו-$x^3$", 4),
               (r"הפעלת קושי-שוורץ", 2),
               (r"חישוב $\|x^3\|^2=\frac17$", 4),
               (r"העלאה בריבוע והמסקנה", 3)),
    pitfalls=[r"לחשב $\int_0^1x^6\,dx$ כ-$\frac16$.",
              r"להעלות בריבוע רק צד אחד של אי-השוויון."],
    steps=[choice(r"באיזו שיטה משתמש הפתרון?", [r"קושי-שוורץ עם $g(x)=x^3$", "אינדוקציה", "אי-שוויון המשולש", "נגזרת של $f$"], 0,
                  r"הביטוי $\int_0^1x^3f$ הוא מכפלה פנימית, והחסם עליה הוא קושי-שוורץ."),
           num(r"מהו $\int_0^1x^6\,dx$? (תשובה עשרונית)", 0.14285714, r"$\left[\frac{x^7}7\right]_0^1=\frac17\approx0.142857$.", tol=1e-6),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", S1B_LINES, 2,
                   r"$\|g\|^2=\int_0^1x^6\,dx=\left[\frac{x^6}6\right]_0^1=\frac16$",
                   r"האנטי-נגזרת של $x^6$ היא $\frac{x^7}7$, ולכן הערך הוא $\frac17$.")])

add(2, "א",
    rubric=rub((r"כתיבת $(a,b)*(x,y)$ ו-$(x,y)*(a,b)$", 3),
               (r"השוויון $ay+bx=xb+ya$ וכן $by=yb$ (חילופיות הכפל והחיבור הממשיים)", 2)),
    pitfalls=[r"לבדוק קומוטטיביות על זוג וקטורים אחד בלבד ולהסיק לכל הזוגות.",
              r"לבלבל קומוטטיביות עם אסוציאטיביות."],
    steps=[num(r"מהו הרכיב הראשון של $(1,2)*(3,4)$?", 10, r"$ay+bx=1\cdot4+2\cdot3=10$."),
           num(r"מהו הרכיב הראשון של $(3,4)*(1,2)$?", 10, r"$ay+bx=3\cdot2+4\cdot1=10$, זהה לתוצאה הקודמת."),
           choice("מה צריך להראות כדי להוכיח שהפעולה קומוטטיבית?",
                  [r"$(a,b)*(x,y)=(x,y)*(a,b)$ לכל זוג וקטורים", "שקיים איבר ניטרלי", "שלכל איבר יש הופכי", r"שוויון עבור זוג וקטורים אחד"], 0,
                  "בדיקה על זוג אחד אינה מוכיחה כלל, וקיום ניטרלי או הופכי אינם קשורים לסדר הפעולה.")])

add(2, "ב",
    rubric=rub((r"כתיבת המשוואה $(a,b)*(e_1,e_2)=(a,b)$", 2),
               (r"מהרכיב השני $be_2=b$ מתקבל $e_2=1$", 2),
               (r"מהרכיב הראשון $a+be_1=a$ מתקבל $e_1=0$, ולכן $e=(0,1)$", 2)),
    pitfalls=[r"לבחור $e=(1,1)$ או $(0,0)$; הוקטור $(0,0)$ אינו אפילו בקבוצה.",
              r"לבדוק רק מימין ולא לוודא ש-$e*(a,b)=(a,b)$."],
    steps=[num(r"מהו $e_2$ (מהרכיב השני $be_2=b$ כאשר $b\ne0$)?", 1, r"$be_2=b$ ולכן $e_2=1$."),
           num(r"מהו $e_1$ (מהרכיב הראשון $ae_2+be_1=a$ עם $e_2=1$)?", 0, r"$a+be_1=a$ ולכן $be_1=0$, כלומר $e_1=0$."),
           num(r"מהו הרכיב הראשון של $(0,1)*(3,5)$? (בדיקה משמאל)", 3, r"$ay+bx=0\cdot5+1\cdot3=3$, כלומר $(0,1)*(3,5)=(3,5)$.")])

add(2, "ג",
    rubric=rub((r"בדיקת האקסיומות (סגירות, אסוציאטיביות, ניטרלי, הופכי)", 2),
               (r"הוכחה שלאיברים מהצורה $(a,0)$ אין הופכי: הרכיב השני של $(a,0)*(x,y)$ הוא תמיד $0\ne1$", 3),
               (r"מסקנה: המבנה אינו חבורה", 2)),
    pitfalls=[r"לבדוק הופכי רק עבור איבר עם $b\ne0$, שיש לו הופכי.",
              r"לשכוח שהאיבר הניטרלי הוא $(0,1)$ ולא $(1,0)$ או $(0,0)$."],
    steps=[choice(r"איזה מהאיברים הבאים חסר הופכי?", [r"$(4,0)$", r"$(1,1)$", r"$(2,3)$", r"$(0,1)$"], 0,
                  r"הרכיב השני של $(4,0)*(x,y)$ הוא $0\cdot y=0\ne1$. לשאר יש הופכי: $(0,1)$ הוא הניטרלי, $(1,1)^{-1}=(-1,1)$ ו-$(2,3)^{-1}=(-\frac29,\frac13)$."),
           num(r"מהו הרכיב השני של $(4,0)*(x,y)$ לכל $(x,y)$?", 0, r"$by=0\cdot y=0$, בעוד שהאיבר הניטרלי הוא $(0,1)$ עם רכיב שני $1$."),
           num(r"מהו הרכיב הראשון של ההופכי של $(1,1)$? (מ-$(1,1)*(x,y)=(0,1)$)", -1, r"$y=1$ ו-$x+y=0$, ולכן $x=-1$.")])

S2B_LINES = [r"$(I+A^2)^T=I^T+(A^T)^2=I+A^2$, ולכן המטריצה סימטרית",
             r"$\vec v^T(I+A^2)\vec v=\vec v^T\vec v+\vec v^TA^2\vec v$",
             r"$\vec v^TA^2\vec v=\vec v^TA^TA\vec v=(A\vec v)^T(A\vec v)=\|A\vec v\|^2\ge0$",
             r"$\vec v^T\vec v=\|\vec v\|^2>0$, ולכן $\vec v^T(I+A^2)\vec v>0$"]
add(2, "ד",
    rubric=rub((r"סימטריה של $I+A^2$", 2),
               (r"פירוק הצורה הריבועית $\vec v^T\vec v+\vec v^TA^2\vec v$", 1),
               (r"$\vec v^TA^2\vec v=\|A\vec v\|^2\ge0$ (שימוש ב-$A^T=A$)", 2),
               (r"$\vec v^T\vec v>0$ ומסקנה: חיובית לחלוטין", 2)),
    pitfalls=[r"לשכוח לבדוק סימטריה: הגדרה של מוגדרת חיובית לחלוטין מחייבת מטריצה סימטרית.",
              r"לכתוב $\vec v^TA^2\vec v=(\vec v^TA\vec v)^2$ (שוויון שגוי)."],
    steps=[num(r"עבור $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ ו-$\vec v=(1,0)^T$: מהו $\|A\vec v\|^2=\vec v^TA^2\vec v$?", 5, r"$A\vec v=(2,1)^T$ ולכן $\|A\vec v\|^2=4+1=5$."),
           num(r"באותה דוגמה: מהו $\vec v^T(I+A^2)\vec v$?", 6, r"$\vec v^T\vec v+\vec v^TA^2\vec v=1+5=6>0$."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", S2B_LINES, 2,
                   r"$\vec v^TA^2\vec v=(\vec v^TA\vec v)^2\ge0$",
                   r"השוויון אינו נכון בדרך כלל: בדוגמה $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $\vec v=(1,0)^T$ מתקבל $5$ בצד אחד ו-$4$ בצד השני.")])

add(3, "א",
    rubric=rub((r"חישוב $AA^T=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$", 3),
               (r"הערכים העצמיים $3,1$", 3),
               (r"הערכים הסינגולריים $\sqrt3,1$ והמטריצה $\Sigma$", 2),
               (r"וקטורים עצמיים של $AA^T$ (עמודות $U$)", 3),
               (r"עמודות $V$ לפי $\vec v_i=\frac1{\sigma_i}A^T\vec u_i$", 4),
               (r"$\vec v_3$ מ-$\ker A$ ובדיקת הפירוק", 3)),
    pitfalls=[r"לחשב $A^TA$ ($3\times3$) במקום $AA^T$ ($2\times2$): העבודה קשה יותר.",
              r"לרשום את הערכים העצמיים במקום הערכים הסינגולריים (השורשים שלהם) ב-$\Sigma$."],
    steps=[num(r"מהו הרכיב $(AA^T)_{12}$ עבור $A=\begin{pmatrix}0&-1&1\\1&1&0\end{pmatrix}$?", -1, r"מכפלת שתי השורות: $0\cdot1+(-1)\cdot1+1\cdot0=-1$."),
           num(r"מהו הערך הסינגולרי הגדול $\sigma_1$? (תשובה עשרונית)", 1.7320508, r"הערכים העצמיים של $AA^T$ הם $3,1$, ולכן $\sigma_1=\sqrt3\approx1.7321$.", tol=1e-6),
           num(r"אם $\vec u_1=\frac1{\sqrt2}(-1,1)^T$: מהו הרכיב השני של $\vec v_1=\frac1{\sigma_1}A^T\vec u_1$? (תשובה עשרונית)", 0.81649658,
               r"$A^T\vec u_1=\frac1{\sqrt2}(1,2,-1)^T$, ואחרי חלוקה ב-$\sqrt3$: $\vec v_1=\frac1{\sqrt6}(1,2,-1)^T$, והרכיב השני הוא $\frac2{\sqrt6}\approx0.8165$.", tol=1e-6),
           num(r"מהו המימד של $\ker A$ (ממנו נבחר $\vec v_3$)?", 1, r"דרגת $A$ היא $2$ ו-$3-2=1$.")])

add(3, "ב",
    rubric=rub((r"פתיחת $\|\vec u+\vec v\|^2=\|\vec u\|^2+2\langle\vec u,\vec v\rangle+\|\vec v\|^2$", 2),
               (r"פתיחת $\|\vec u-\vec v\|^2=\|\vec u\|^2-2\langle\vec u,\vec v\rangle+\|\vec v\|^2$", 2),
               (r"חיסור הזהויות", 2),
               (r"חלוקה ב-$4$ והמסקנה", 1)),
    pitfalls=[r"לשכוח שהסימטריה $\langle\vec v,\vec u\rangle=\langle\vec u,\vec v\rangle$ נחוצה (מרחב ממשי).",
              r"לחבר את הזהויות במקום לחסר: החיבור מבטל את $\langle\vec u,\vec v\rangle$."],
    steps=[num(r"עבור $\vec u=(1,2)$ ו-$\vec v=(3,-1)$ ב-$\mathbb{R}^2$: מהו $\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2$?", 4, r"$\|(4,1)\|^2-\|(-2,3)\|^2=17-13=4$, כלומר $4\langle\vec u,\vec v\rangle$ עם $\langle\vec u,\vec v\rangle=1$."),
           choice(r"איזו תכונה של המכפלה הפנימית הממשית מאפשרת לאחד את $\langle\vec u,\vec v\rangle+\langle\vec v,\vec u\rangle$ ל-$2\langle\vec u,\vec v\rangle$?",
                  ["סימטריה", "חיוביות", "הומוגניות ברכיב הראשון", "אי-שוויון קושי-שוורץ"], 0,
                  r"רק הסימטריה אומרת ש-$\langle\vec v,\vec u\rangle=\langle\vec u,\vec v\rangle$; שאר התכונות אינן מקשרות בין שני הסדרים."),
           order("סדרו את שלבי ההוכחה.",
                 [r"$\|\vec u\pm\vec v\|^2=\|\vec u\|^2\pm2\langle\vec u,\vec v\rangle+\|\vec v\|^2$",
                  r"$\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2=4\langle\vec u,\vec v\rangle$",
                  r"$\langle\vec u,\vec v\rangle=\frac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$"],
                 "הפיתוח קודם לחיסור, והחלוקה ב-4 אחרונה.")])

add(4, "א",
    rubric=rub((r"חישוב הפולינום האופייני והערכים העצמיים $a,\ a^2-1,\ a^2+1$", 6),
               (r"מוגדרת חיובית לחלוטין: $a>1$", 4),
               (r"מוגדרת חיובית (למחצה): $a\ge1$", 3),
               (r"לא קיים ערך שלילי (כי $a^2+1>0$); עבור $a<1$ אינה מוגדרת", 4)),
    pitfalls=[r"לשכוח את התנאי $a^2-1>0$ ולהסיק $a>0$.",
              r"להחליף בין 'חיובית' ל'חיובית לחלוטין' בנקודה $a=1$ (שם יש ערך עצמי $0$)."],
    steps=[num(r"עבור $a=1$: מהו הערך העצמי הקטן ביותר?", 0, r"הערכים העצמיים הם $a=1,\ a^2-1=0,\ a^2+1=2$."),
           choice(r"מהו הסיווג עבור $a=\frac12$?", ["אינה מוגדרת (ערכים עצמיים חיוביים ושליליים)", "מוגדרת חיובית לחלוטין", "מוגדרת שלילית", "מוגדרת חיובית (למחצה)"], 0,
                  r"הערכים העצמיים הם $\frac12,\ -\frac34,\ \frac54$: יש שלילי וחיובי."),
           choice(r"עבור אילו $a$ המטריצה מוגדרת חיובית לחלוטין?", [r"$a>1$", r"$a\ge1$", r"$a>0$", r"$a>-1$"], 0,
                  r"צריך $a>0$ וגם $a^2-1>0$, כלומר $a>1$. עבור $a=1$ יש ערך עצמי $0$, ועבור $0<a<1$ מתקבל $a^2-1<0$."),
           choice(r"עבור אילו $a$ המטריצה מוגדרת שלילית (למחצה)?", ["אין ערך כזה", r"$a\le-1$", r"$a<0$", r"$a\le0$"], 0,
                  r"הערך העצמי $a^2+1$ חיובי תמיד.")])

add(4, "ב",
    rubric=rub((r"הבאת המשוואות לשאריות: $x\equiv2\pmod3$, $x\equiv0\pmod2$, $x\equiv6\pmod7$", 2),
               (r"$M=42$, $M_1=14,\ M_2=21,\ M_3=6$ והופכיים $2,1,6$", 3),
               (r"הצבה בנוסחה: $272$", 1),
               (r"הפחתה מודולו $42$: $x\equiv20$", 2)),
    pitfalls=[r"להשאיר $x\equiv5\pmod3$ ו-$x\equiv4\pmod2$ בלי להפחית.",
              r"לשכוח להפחית את הסכום $272$ מודולו $42$."],
    steps=[num(r"מהי השארית של $5$ מודולו $3$?", 2, r"$5=3+2$."),
           num(r"מהו $x_3$ המקיים $6x_3\equiv1\pmod7$ (ערך בין 0 ל-6)?", 6, r"$6\cdot6=36=35+1\equiv1$."),
           num(r"מהו הסכום $a_1M_1x_1+a_2M_2x_2+a_3M_3x_3$?", 272, r"$2\cdot14\cdot2+0+6\cdot6\cdot6=56+216=272$."),
           num(r"מהו הפתרון $x$ מודולו $42$ (ערך בין 0 ל-41)?", 20, r"$272=6\cdot42+20$.")])

G5_LINES = [r"נדרוש $A(a,b,c)A(x,y,z)=I$",
            r"לפי נוסחת הכפל: $a+x=0,\ c+z=0,\ b+y+az=0$",
            r"ולכן $x=-a,\ z=-c,\ y=ac-b$",
            r"$A(a,b,c)^{-1}=A(-a,ac-b,-c)\in G$"]
add(5, "א",
    rubric=rub((r"סגירות: $A(a_1,b_1,c_1)A(a_2,b_2,c_2)=A(a_1+a_2,\ b_1+b_2+a_1c_2,\ c_1+c_2)\in G$", 6),
               (r"אסוציאטיביות כפל מטריצות", 3),
               (r"איבר ניטרלי $I=A(0,0,0)$", 3),
               (r"הופכי: $A(-a,ac-b,-c)\in G$", 6)),
    pitfalls=[r"לשכוח את סגירות הכפל ולבדוק רק הופכי.",
              r"לכתוב את ההופכי כ-$A(-a,-b,-c)$: הרכיב העליון-ימני הוא $ac-b$."],
    steps=[num(r"עבור $A(1,2,3)\cdot A(4,5,6)$: מהו הרכיב בשורה 1 ובעמודה 3? (לפי $b_1+b_2+a_1c_2$)", 13, r"$2+5+1\cdot6=13$."),
           num(r"מהו הרכיב בשורה 1 ובעמודה 3 של ההופכי של $A(1,2,3)$?", 1, r"$ac-b=1\cdot3-2=1$."),
           order("סדרו את שלבי מציאת ההופכי.", G5_LINES, r"המשוואות נגזרות מנוסחת הכפל, והפתרון נגזר מהן."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G5_LINES, 2, r"ולכן $x=-a,\ z=-c,\ y=b+ac$",
                   r"מהמשוואה $b+y+az=0$ עם $z=-c$ מתקבל $y=ac-b$, לא $b+ac$.")])

G5B_LINES = [r"לפי הנתון $a*b\in G$ מקיים $(a*b)^{-1}=a*b$",
             r"בחבורה $(a*b)^{-1}=b^{-1}*a^{-1}=b*a$, ולכן $a*b=b*a$",
             r"$c=(a*b)*a=(b*a)*a$",
             r"$c=b*(a*a)=b*e=b$"]
add(5, "ב",
    rubric=rub((r"הוכחה ש-$a*b=b*a$ (באמצעות $(a*b)^{-1}=b^{-1}*a^{-1}$ והנתון $x^{-1}=x$)", 4),
               (r"הצבה $c=(b*a)*a$, אסוציאטיביות ו-$a*a=e$, וסיום $c=b$", 3)),
    pitfalls=[r"לכתוב $(a*b)^{-1}=a^{-1}*b^{-1}$ (נכון רק בחבורה אבלית).",
              r"לשכוח את האסוציאטיביות כשמזיזים סוגריים."],
    steps=[choice(r"מה מוכיחים תחילה, לפני חישוב $c$?", [r"$a*b=b*a$", r"$a=b$", r"$a*b=e$", r"$a=e$"], 0,
                  r"ב-$\mathbb{Z}_2\times\mathbb{Z}_2$ עם $a=(1,0)$, $b=(0,1)$ מתקיים $a*b=b*a$ אבל $a\ne b$, $a*b\ne e$, $a\ne e$."),
           order("סדרו את שלבי ההוכחה.", G5B_LINES, "כל שורה נשענת על הקודמת."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G5B_LINES, 3, r"$c=b*(a*a)=b*a$",
                   r"לפי הנתון $a*a=e$ ולכן $b*(a*a)=b*e=b$; הגרסה השגויה מדלגת על $a*a=e$ ואינה נותנת $b$.")])

exam = {
    "examCode": "24A-C",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ד מועד ג'",
    "year": 2024,
    "sourceFile": "algebra-2-24A-C-exam",
    "solutionFile": "student-solution-1",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
