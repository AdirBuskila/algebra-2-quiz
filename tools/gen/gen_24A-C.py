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
identity), Q5a (Heisenberg group), Q5b (x*x=e => abelian-type proof): held "no-key" (the orchestrator routes them
to the solver); their texts are transcribed in full.

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
