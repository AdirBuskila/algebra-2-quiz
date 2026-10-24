# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-S.json -- algebra-2 (20079), semester A 2023, special sitting (20.04.2023, 09:00-12:00).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-S.py

Source: the exam exists only inside the 275-page compilation (pp. 149-150, typed). There is NO official solution.
The pages that follow it (pp. 151-160) are a student's handwritten scans of selected questions, mixed with questions
from other sittings; of this sitting only Q1a (pp. 154-155) and Q3b (p. 151) appear. Per GATE1 this sitting is
non-official (official:false).
5 printed questions (solve 4 of 5, 25% each); 9 items: Q3b ships as the student solution (correct); the other 8
were held and are now solved by the solver (SOLVED below: solutionSource "solved", official false, confidence high,
pending the refuter; every computation in tools/verify/23A-S/solve_23AS.py, all OK).
Solver notes: Q1a answer "no such a" uses the course definition (definiteness is for symmetric matrices; the
matrix is symmetric only at a=1, where eigenvalues 3,-1,1 make it indefinite). A remark in the solution gives the
quadratic-form reading (symmetric part: PD iff a>3, ND iff a<-1) so a grader who reads it that way sees both.
The student's Q1a answer (PD for a >= 1+sqrt3) is NOT used. Q5a: 3 mod 2 is reduced to 1 mod 2; x = 67 mod 70.

Part letters: every question has printed parts a, b except Q4 (one part, no letter).
Every question text starts with its printed label.

Held (reason in the "hold" field; listed in docs/ASK_ADIR.md via the report; the orchestrator routes "no-key" to the solver):
- Q1a: the student's solution is WRONG (tools/verify/23A-S/check.py). The matrix [[a,2,0],[a+1,a,0],[0,0,a]] is not
  symmetric unless a = 1 (and at a = 1 it has eigenvalues 3, -1, 1, so it is indefinite); the student reads off the
  eigenvalues a, a +/- sqrt(2a+2) of a non-symmetric matrix and claims "positive for a >= 1+sqrt3".
- All other items: no solution in the source (no-key).
Q3b, the one shipped item: the student's argument (u = x^3, v = f, Cauchy-Schwarz, ||x^3||^2 = 1/7, square both sides)
is correct; checked with sympy. Source label is only "student solution"; no name appears in any field.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-S.json"

# ------------------------------------------------------------------ contexts
CTX = {
    "c5b": {"kind": "text", "title": "שאלה 5 סעיף ב",
            "text": r"במרחב הוקטורי $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע״י $\langle A,B\rangle=tr\left(B^TA\right)$ לכל $A,B\in M_2(\mathbb{R})$."},
}

S3B = (
    r"נסמן $\vec u=x^3$ ו-$\vec v=f(x)$ במרחב $C[0,1]$ עם המכפלה הפנימית $\langle f,g\rangle=\displaystyle\int_0^1f(x)g(x)\,dx$. לפי אי-שוויון קושי-שוורץ $|\langle\vec u,\vec v\rangle|\le\|\vec u\|\cdot\|\vec v\|$." "\n"
    r"$$\|\vec u\|=\sqrt{\langle x^3,x^3\rangle}=\sqrt{\int_0^1x^3\cdot x^3\,dx}=\sqrt{\left[\frac{x^7}7\right]_0^1}=\sqrt{\frac17},\qquad\|f(x)\|=\sqrt{\int_0^1f^2(x)\,dx}$$" "\n"
    r"$$\int_0^1x^3\cdot f(x)\,dx\le\sqrt{\frac17}\cdot\sqrt{\int_0^1f^2(x)\,dx}$$" "\n"
    r"נעלה בריבוע ונקבל: $\left(\displaystyle\int_0^1x^3f(x)\,dx\right)^2\le\dfrac17\displaystyle\int_0^1\left(f(x)\right)^2dx$."
)


def H(num, kind, topic, question, points, reason, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "points": points, "question": question, "hold": reason}
    if part:
        q["part"] = part
    q.update(kw)
    return q


NOKEY = "no-key"
questions = [
    H(1, "computation", "pos_def",
      r"(13 נק') האם קיימים ערכים ממשיים של הפרמטר $a$ עבור המטריצה $\begin{pmatrix}a&2&0\\a+1&a&0\\0&0&a\end{pmatrix}$ מוגדרת חיובית או מוגדרת שלילית? נמקו.",
      13, "the only solution in the source (a student's) is wrong: the matrix is not symmetric unless a=1 (then indefinite), the student used eigenvalues of a non-symmetric matrix; needs a solver", part="א"),
    H(1, "computation", "inner_product",
      r"(12 נק') יהי $V$ מרחב מכפלה פנימית ויהיו $\vec u,\vec v\in V$ וקטורים המקיימים: $\|\vec u\|=3$ , $\|\vec u+\vec v\|=4$ , $\|\vec u-\vec v\|=6$. מצאו את $\|\vec v\|$.",
      12, NOKEY, part="ב"),

    H(2, "computation", "least_squares",
      r"(15 נק') נתונות 5 הנקודות במישור $(5,7)$, $(3,5)$, $(1,4)$, $(-2,0)$, $(-3,2)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים.",
      15, NOKEY, part="א"),
    H(2, "proof", "orthogonality",
      r"(10 נק') תהי $Q\in M_n(\mathbb{R})$ אורתוגונלית וסימטרית בו זמנית. נגדיר $P=I+Q$. הוכיחו כי $P^2=2P$.",
      10, NOKEY, part="ב"),

    H(3, "computation", "qr", r"(15 נק') מצאו פירוק $QR$ עבור המטריצה $A=\begin{pmatrix}1&1&0\\0&0&1\\1&-1&1\end{pmatrix}$.",
      15, NOKEY, part="א"),
    {"num": 3, "part": "ב", "kind": "proof", "topic": "cauchy_schwarz", "points": 10,
     "question": r"(10 נק') הוכיחו את האי-השוויון הבא עבור כל פונקציה רציפה $f(x)$ על הקטע $[0,1]$: $\left(\displaystyle\int_0^1x^3f(x)\,dx\right)^2\le\dfrac17\displaystyle\int_0^1\left(f(x)\right)^2dx$.",
     "solution": S3B, "solutionSource": "student-solution", "official": False, "confidence": "med"},

    H(4, "proof", "groups",
      r"(25 נק') הוכיחו כי הקבוצה $G=\left\{A=\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}\in M_3(\mathbb{R})\ \middle|\ a,b,c\in\mathbb{R}\right\}$ יחד עם הפעולה של כפל מטריצות מהווה חבורה.",
      25, NOKEY),

    H(5, "computation", "crt",
      r"(13 נק') פתרו את המערכות הבאות באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod 5\\x\equiv3\pmod 2\\x\equiv4\pmod 7\end{cases}$.",
      13, NOKEY, part="א"),
    H(5, "computation", "projection",
      r"(12 נק') חשבו את ההיטל של $\begin{pmatrix}1&2\\3&0\end{pmatrix}$ על $Sp\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}1&3\\1&1\end{pmatrix}\right\}$.",
      12, NOKEY, part="ב", contextId="c5b"),
]

# ------------------------------------------------------------------ solver solutions (no key; checked by
# tools/verify/23A-S/solve_23AS.py, all OK). solutionSource "solved", official false, pending the refuter.
SOLVED = {
    (1, "א"): (
        r"לפי ההגדרה בקורס, סיווג מטריצה כמוגדרת (חיובית/שלילית, למחצה או לחלוטין) נעשה עבור מטריצה **סימטרית** $A^T=A$, ואז היא נקבעת לפי סימני הערכים העצמיים." "\n"
        r"**סימטריות:** $M^T=M$ דורש $M_{12}=M_{21}$, כלומר $2=a+1$, ושאר הרכיבים כבר סימטריים. לכן $M$ סימטרית אם ורק אם $a=1$. לכל $a\ne1$ המטריצה אינה סימטרית, ולכן אינה מוגדרת חיובית או שלילית (אין להסיק דבר מהערכים העצמיים של מטריצה לא סימטרית)." "\n"
        r"**המקרה $a=1$:** $M=\begin{pmatrix}1&2&0\\2&1&0\\0&0&1\end{pmatrix}$, ונפתח לפי השורה השלישית:" "\n"
        r"$$|M-\lambda I|=(1-\lambda)\left((1-\lambda)^2-4\right)=(1-\lambda)(3-\lambda)(-1-\lambda)=0\ \Rightarrow\ \lambda_1=1,\ \lambda_2=3,\ \lambda_3=-1$$" "\n"
        r"יש ערך עצמי חיובי ($3$) וגם ערך עצמי שלילי ($-1$), לכן המטריצה אינה מוגדרת. ניתן לראות זאת גם ישירות: עבור $\vec v=(1,1,0)^T$ מתקיים $\vec v^TM\vec v=6>0$, ועבור $\vec v=(1,-1,0)^T$ מתקיים $\vec v^TM\vec v=-2<0$." "\n"
        r"**תשובה:** לא קיימים ערכים ממשיים של $a$ עבורם המטריצה מוגדרת חיובית או מוגדרת שלילית." "\n"
        r"הערה: אין לקרוא את הערכים העצמיים $a,\ a\pm\sqrt{2a+2}$ של המטריצה הלא-סימטרית ולהסיק מהם. מי שבודק רק את התבנית הריבועית $\vec v^TM\vec v$ (בלי דרישת סימטריה) צריך לעבור לחלק הסימטרי $S=\frac12(M+M^T)$, שערכיו העצמיים $a,\ \frac{3a+3}2,\ \frac{a-3}2$. אז התבנית חיובית לחלוטין רק עבור $a>3$ ושלילית לחלוטין רק עבור $a<-1$. לפי הגדרת הקורס התשובה נשארת: אין ערכים כאלה."
    ),
    (1, "ב"): (
        r"נפתח את שני הריבועים בעזרת תכונות המכפלה הפנימית:" "\n"
        r"$$\|\vec u+\vec v\|^2=\|\vec u\|^2+2\langle\vec u,\vec v\rangle+\|\vec v\|^2,\qquad\|\vec u-\vec v\|^2=\|\vec u\|^2-2\langle\vec u,\vec v\rangle+\|\vec v\|^2$$" "\n"
        r"נחבר ונקבל את כלל המקבילית: $\|\vec u+\vec v\|^2+\|\vec u-\vec v\|^2=2\|\vec u\|^2+2\|\vec v\|^2$. נציב:" "\n"
        r"$$4^2+6^2=2\cdot3^2+2\|\vec v\|^2\ \Rightarrow\ 52=18+2\|\vec v\|^2\ \Rightarrow\ \|\vec v\|^2=17$$" "\n"
        r"$$\|\vec v\|=\sqrt{17}$$" "\n"
        r"(בדרך אגב, מחיסור שני השוויונות מתקבל $\langle\vec u,\vec v\rangle=\frac{16-36}4=-5$.)"
    ),
    (2, "א"): (
        r"נחפש ישר $y=mx+n$. הצבת הנקודות נותנת מערכת $A\vec x=\vec b$:" "\n"
        r"$$\begin{cases}5m+n=7\\3m+n=5\\m+n=4\\-2m+n=0\\-3m+n=2\end{cases}\Rightarrow\begin{pmatrix}5&1\\3&1\\1&1\\-2&1\\-3&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}7\\5\\4\\0\\2\end{pmatrix}$$" "\n"
        r"אין ישר שעובר דרך כל הנקודות, לכן פותרים את המשוואות הנורמליות $A^TA\vec x=A^T\vec b$:" "\n"
        r"$$A^TA=\begin{pmatrix}48&4\\4&5\end{pmatrix},\qquad A^T\vec b=\begin{pmatrix}48\\18\end{pmatrix}$$" "\n"
        r"$$\begin{cases}48m+4n=48\\4m+5n=18\end{cases}\Rightarrow n=12-12m\Rightarrow4m+60-60m=18\Rightarrow m=\frac34,\quad n=3$$" "\n"
        r"$$y=\frac34x+3$$"
    ),
    (2, "ב"): (
        r"$Q$ אורתוגונלית: $Q^TQ=I$. $Q$ סימטרית: $Q^T=Q$. לכן $Q^2=Q\cdot Q=Q^TQ=I$." "\n"
        r"$$P^2=(I+Q)(I+Q)=I^2+IQ+QI+Q^2=I+2Q+Q^2=I+2Q+I=2I+2Q=2(I+Q)=2P$$" "\n"
        r"ולכן $P^2=2P$. $\blacksquare$"
    ),
    (3, "א"): (
        r"נבצע גרם-שמידט על עמודות $A$: $\vec c_1=(1,0,1)^T$, $\vec c_2=(1,0,-1)^T$, $\vec c_3=(0,1,1)^T$ (העמודות בלתי תלויות, $\det A=2\ne0$)." "\n"
        r"$$\vec u_1=\vec c_1=(1,0,1)^T,\qquad\|\vec u_1\|=\sqrt2$$" "\n"
        r"$$\vec u_2=\vec c_2-\frac{\langle\vec c_2,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1=\vec c_2-0\cdot\vec u_1=(1,0,-1)^T,\qquad\|\vec u_2\|=\sqrt2$$" "\n"
        r"$$\vec u_3=\vec c_3-\frac{\langle\vec c_3,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1-\frac{\langle\vec c_3,\vec u_2\rangle}{\|\vec u_2\|^2}\vec u_2=(0,1,1)^T-\frac12(1,0,1)^T+\frac12(1,0,-1)^T=(0,1,0)^T,\qquad\|\vec u_3\|=1$$" "\n"
        r"נרמל ונקבל את עמודות $Q$, ואז $R=Q^TA$:" "\n"
        r"$$Q=\begin{pmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}&0\\0&0&1\\\frac1{\sqrt2}&-\frac1{\sqrt2}&0\end{pmatrix},\qquad R=Q^TA=\begin{pmatrix}\sqrt2&0&\frac1{\sqrt2}\\0&\sqrt2&-\frac1{\sqrt2}\\0&0&1\end{pmatrix}$$" "\n"
        r"בדיקה: $Q^TQ=I$, $R$ משולשית עליונה עם אלכסון חיובי, ו-$QR=A$."
    ),
    (4, None): (
        r"נסמן $A(a,b,c)=\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}$ ונבדוק את אקסיומות החבורה." "\n"
        r"**סגירות:** לכל $a_1,b_1,c_1,a_2,b_2,c_2\in\mathbb{R}$:" "\n"
        r"$$A(a_1,b_1,c_1)\cdot A(a_2,b_2,c_2)=\begin{pmatrix}1&a_1+a_2&b_2+a_1c_2+b_1\\0&1&c_1+c_2\\0&0&1\end{pmatrix}=A(a_1+a_2,\ b_1+b_2+a_1c_2,\ c_1+c_2)\in G$$" "\n"
        r"כי הרכיבים ממשיים והמבנה (אלכסון $1$, אפסים מתחת לאלכסון) נשמר." "\n"
        r"**אסוציאטיביות:** כפל מטריצות ב-$M_3(\mathbb{R})$ אסוציאטיבי, ובפרט על אברי $G$: $(XY)Z=X(YZ)$." "\n"
        r"**איבר ניטרלי:** $I=A(0,0,0)\in G$ ומתקיים $XI=IX=X$ לכל $X\in G$." "\n"
        r"**הופכי:** $\det A(a,b,c)=1\ne0$ (משולשית עם אלכסון $1$), ונמצא את ההופכי בתוך $G$: מהדרישה $A(a,b,c)A(x,y,z)=I$ לפי נוסחת הכפל: $a+x=0$, $c+z=0$, $b+y+az=0$, כלומר $x=-a$, $z=-c$, $y=ac-b$." "\n"
        r"$$A(a,b,c)^{-1}=\begin{pmatrix}1&-a&ac-b\\0&1&-c\\0&0&1\end{pmatrix}\in G$$" "\n"
        r"ובדיקה גם בכיוון השני: $A(-a,ac-b,-c)A(a,b,c)=A(0,\ ac-b+b-ac,\ 0)=I$." "\n"
        r"כל האקסיומות מתקיימות, לכן $(G,\cdot)$ חבורה. (היא אינה אבלית: למשל $A(1,0,0)A(0,0,1)=A(1,1,1)$ אבל $A(0,0,1)A(1,0,0)=A(1,0,1)$.) $\blacksquare$"
    ),
    (5, "א"): (
        r"קודם מביאים לצורה עם שארית קטנה מהמודולו: $x\equiv3\pmod2$ שקול ל-$x\equiv1\pmod2$. המודולים $5,2,7$ זרים בזוגות, לכן לפי משפט השאריות הסיני יש פתרון יחיד מודולו $M=5\cdot2\cdot7=70$." "\n"
        r"$a_1=2,\ a_2=1,\ a_3=4$; $m_1=5,\ m_2=2,\ m_3=7$; $M_1=14,\ M_2=35,\ M_3=10$." "\n"
        r"$$y_iM_i\equiv1\pmod{m_i}:\quad14y_1\equiv4y_1\equiv1\pmod5\Rightarrow y_1=4;\quad35y_2\equiv y_2\equiv1\pmod2\Rightarrow y_2=1;\quad10y_3\equiv3y_3\equiv1\pmod7\Rightarrow y_3=5$$" "\n"
        r"$$x\equiv a_1M_1y_1+a_2M_2y_2+a_3M_3y_3=2\cdot14\cdot4+1\cdot35\cdot1+4\cdot10\cdot5=112+35+200=347\equiv67\pmod{70}$$" "\n"
        r"$$x\equiv67\pmod{70}$$" "\n"
        r"בדיקה: $67=13\cdot5+2$, $67=33\cdot2+1$ ($\equiv3\pmod2$), $67=9\cdot7+4$."
    ),
    (5, "ב"): (
        r"נסמן $A_1=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, $A_2=\begin{pmatrix}1&3\\1&1\end{pmatrix}$, $C=\begin{pmatrix}1&2\\3&0\end{pmatrix}$. המכפלה $\langle A,B\rangle=tr\left(B^TA\right)$ היא סכום מכפלות הרכיבים המתאימים." "\n"
        r"**גרם-שמידט:** $B_1=A_1$, $\|B_1\|^2=1+1=2$. $\langle A_2,B_1\rangle=1+3=4$, לכן" "\n"
        r"$$B_2=A_2-\frac{\langle A_2,B_1\rangle}{\|B_1\|^2}B_1=\begin{pmatrix}1&3\\1&1\end{pmatrix}-2\begin{pmatrix}1&1\\0&0\end{pmatrix}=\begin{pmatrix}-1&1\\1&1\end{pmatrix},\qquad\|B_2\|^2=4$$" "\n"
        r"**ההיטל:** $\langle C,B_1\rangle=1+2=3$, $\langle C,B_2\rangle=-1+2+3+0=4$." "\n"
        r"$$P(C)=\frac{\langle C,B_1\rangle}{\|B_1\|^2}B_1+\frac{\langle C,B_2\rangle}{\|B_2\|^2}B_2=\frac32\begin{pmatrix}1&1\\0&0\end{pmatrix}+1\cdot\begin{pmatrix}-1&1\\1&1\end{pmatrix}=\begin{pmatrix}\frac12&\frac52\\1&1\end{pmatrix}$$" "\n"
        r"בדיקה: $C-P(C)=\begin{pmatrix}\frac12&-\frac12\\2&-1\end{pmatrix}$ אורתוגונלית ל-$A_1$ ($\frac12-\frac12=0$) ול-$A_2$ ($\frac12-\frac32+2-1=0$)."
    ),
}
for q in questions:
    key = (q["num"], q.get("part"))
    if key in SOLVED and "hold" in q:
        del q["hold"]
        q.update({"solution": SOLVED[key], "solutionSource": "solved", "official": False, "confidence": "high"})
assert all("hold" not in q for q in questions), "an item is still held"

exam = {
    "examCode": "23A-S",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ג מועד מיוחד",
    "year": 2023,
    "examDate": "20.4.2023",
    "sourceFile": "algebra-2-23A-S-exam",
    "solutionFile": "student-solution-1",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
