# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-A.json -- algebra-2 (20079), semester A 2025, moed A (13.2.2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25A-A.py

Source: exam 2 pp.; the solution file (16 pp.) is a handwritten student solution, read from the rendered pages,
so every shipped item is solutionSource "student-solution", official false (the refuter checks all of them).
5 questions, 16 items (14 shipped, 2 held):
HOLD (no-key): Q4b (CRT) and Q5b (the sum inequality) are not in the solution file. They go to the solver.
Part letters: Q1: a.1 -> a, a.2 -> b, b -> c. Q4: a.1 -> a, a.2 -> b, a.3 -> c, b -> d.

Checks: tools/verify/25A-A/check.py (sympy + brute force), all OK. Notes on the student solution:
- Q3b: the (=>) direction in the handwriting goes through "cos(alpha) = 1 so alpha = 0 so proportional", which
  is the claim itself; a direct argument is added in a labelled remark (the written proof is kept).
- Q4a.3: the side scribbles about o(ab)=o(a)o(b) are not part of the answer and are left out.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


CTX = {
    "c1": {"kind": "text", "title": "שאלה 1 סעיף א",
           "text": r"במרחב $C_{[0,1]}$ של כל הפונקציות הרציפות בקטע $[0,1]$ נגדיר את מכפלה הפנימית הבאה: $\langle f,g\rangle=\displaystyle\int_0^1f(x)\cdot g(x)\,dx$. עבור אילו ערכי $a>0,\ b>0$ המערכת $\{ax+b,\ ax-b\}$ היא:"},
    "c2": {"kind": "text", "title": "שאלה 2",
           "text": r"נסתכל ב-$(A,*)$ כאשר $A=\{(x,y)\mid x,y\in\mathbb{R}\ \wedge\ y\neq0\}$ והפעולה $*$ מוגדרת באופן הבא:" "\n"
                   r"$\forall (a,b),(c,d)\in A\ ,\quad (a,b)*(c,d)=\left(a+c+1,\ \dfrac{bd}3\right)$."},
    "c4": {"kind": "text", "title": "שאלה 4 סעיף א",
           "text": r"נסתכל בחבורה $G=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb{Z}_5)\ \middle|\ ad-cb\neq0\right\}$ עם כפל מטריצות (הכפל והחיבור של רכיבי המטריצות הם מודולו 5)."},
}

S1A1 = (
    r"בסיס אורתוגונלי הוא קבוצת איברים כך שכל זוג שונים מהם מקיים $\langle u,v\rangle=0$." "\n"
    r"$$\langle ax+b,\ ax-b\rangle=0\ \Longleftrightarrow\ \int_0^1(ax+b)(ax-b)\,dx=\int_0^1\left(a^2x^2-b^2\right)dx=\left.\frac{a^2x^3}3-b^2x\right|_0^1=\frac{a^2}3-b^2=0$$" "\n"
    r"$$\frac{a^2}3=b^2\ \Rightarrow\ a^2=3b^2\ \Rightarrow\ a=\sqrt3\,b$$"
)

S1A2 = (
    r"מערכת אורתונורמלית היא מערכת אורתוגונלית שבנוסף אורך כל איבר בה הוא 1, כלומר $\sqrt{\langle u,u\rangle}=1$, כלומר $\langle u,u\rangle=1$." "\n"
    r"נדרש $a=\sqrt3\,b$ (אורתוגונליות) וגם" "\n"
    r"$$\langle ax+b,ax+b\rangle=1,\qquad\langle ax-b,ax-b\rangle=1$$" "\n"
    r"נציב $a=\sqrt3\,b$ ונחשב את האינטגרלים:" "\n"
    r"$$\int_0^1\left(\sqrt3\,bx+b\right)^2dx=\int_0^1\left(3b^2x^2+2\sqrt3\,b^2x+b^2\right)dx=b^2+\sqrt3\,b^2+b^2=1$$" "\n"
    r"$$\int_0^1\left(\sqrt3\,bx-b\right)^2dx=\int_0^1\left(3b^2x^2-2\sqrt3\,b^2x+b^2\right)dx=b^2-\sqrt3\,b^2+b^2=1$$" "\n"
    r"נחסר את המשוואות: $2\sqrt3\,b^2=0\iff b=0$. אבל נתון $a,b>0$, ולכן לא קיימים $a,b>0$ כך שהמערכת אורתונורמלית."
)

S1B = (
    r"מטריצה מוגדרת חיובית לחלוטין: $A^T=A$ וגם $\langle A\vec u,\vec u\rangle>0$ לכל $\vec u\ne\vec 0$. מטריצה אורתוגונלית: $Q^T=Q^{-1}$." "\n"
    r"**סימטריה:** $$\left(Q^{-1}AQ\right)^T=Q^TA^T\left(Q^{-1}\right)^T=Q^{-1}AQ^{TT}=Q^{-1}AQ$$" "\n"
    r"**חיוביות:** לכל $\vec v\ne\vec 0$, תוך שימוש ב-$Q^{-1}=Q^T$:" "\n"
    r"$$\langle Q^{-1}AQ\vec v,\vec v\rangle=\vec v^TQ^TAQ\vec v=(Q\vec v)^TA(Q\vec v)$$" "\n"
    r"נסמן $\vec u=Q\vec v$ ($\vec u\ne\vec0$ כי $Q$ הפיכה): $\ \vec u^TA\vec u=\langle A\vec u,\vec u\rangle>0$." "\n"
    r"לכן $Q^{-1}AQ$ מוגדרת חיובית לחלוטין."
)

S2A = (
    r"$$\forall(a,b),(c,d)\in A:\quad(a,b)*(c,d)=\left(a+c+1,\frac{bd}3\right)\in A$$" "\n"
    r"מכיוון ש-$b,d\ne0$ מתקיים $b\cdot d\ne0$ ולכן $\frac{bd}3\ne0$. כל פעולה אריתמטית על מספרים ממשיים מחזירה מספר ממשי. לכן $A$ סגורה ביחס ל-$*$."
)

S2B = (
    r"$$\forall(a,b),(c,d),(x,y)\in A:\qquad\big((a,b)*(c,d)\big)*(x,y)=\left(a+c+1,\frac{bd}3\right)*(x,y)=\left(a+c+x+2,\ \frac{bdy}9\right)$$" "\n"
    r"$$(a,b)*\big((c,d)*(x,y)\big)=(a,b)*\left(c+x+1,\frac{dy}3\right)=\left(a+c+x+2,\ \frac{bdy}9\right)$$" "\n"
    "הפעולה אסוציאטיבית."
)

S2C = (
    r"$$\exists(e_1,e_2)\in A:\ \forall(a,b)\in A:\quad(e_1,e_2)*(a,b)=(a,b)=(a,b)*(e_1,e_2)$$" "\n"
    r"$$\left(e_1+a+1,\frac{e_2b}3\right)=(a,b)\ \Rightarrow\ \begin{cases}e_1+a+1=a\\\dfrac{e_2b}3=b\ \ (b\ne0)\end{cases}\ \Rightarrow\ \begin{cases}e_1=-1\\e_2=3\end{cases}\qquad e=(-1,3)$$" "\n"
    r"בדיקה: $(a,b)*(-1,3)=\left(a-1+1,\dfrac{3b}3\right)=(a,b)$."
)

S2D = (
    r"סגירות, אסוציאטיביות וקיום איבר ניטרלי הוכחו בסעיפים הקודמים. נשאר לבדוק הופכי:" "\n"
    r"$$\forall(a,b)\in A\ \exists\left(a^{-1},b^{-1}\right)\in A:\quad(a,b)*\left(a^{-1},b^{-1}\right)=(-1,3)$$" "\n"
    r"$$\left(a+a^{-1}+1,\frac{b\,b^{-1}}3\right)=(-1,3)\ \Rightarrow\ \begin{cases}a^{-1}=-2-a\\b^{-1}=\dfrac9b\end{cases}\qquad\left(a^{-1},b^{-1}\right)=\left(-2-a,\ \frac9b\right)\in A\ \ (b\ne0)$$" "\n"
    r"לכן $(A,*)$ היא חבורה."
)

S2E = (
    r"$$(x,y)*(x,y)=\left(2x+1,\frac{y^2}3\right)=(x,y)\qquad(y\ne0)$$" "\n"
    r"$$\begin{cases}2x+1=x\\\dfrac{y^2}3=y\end{cases}\ \to\ \begin{cases}x=-1\\y=3\end{cases}\qquad(-1,3)$$"
)

S3A = (
    r"נחשב את הערכים העצמיים של $A=\begin{pmatrix}1&w&w\\w&1&w\\w&w&1\end{pmatrix}$. אחרי הפחתת שורה $R_3-R_2$ ופיתוח הדטרמיננטה:" "\n"
    r"$$|A-\lambda I|=(1-\lambda-w)\left(\lambda^2+(-2-w)\lambda+\left(1+w-2w^2\right)\right)=0$$" "\n"
    r"אחד הפתרונות: $1-\lambda-w=0\Rightarrow\lambda=1-w$. את הגורם הריבועי פותרים עם הנוסחה:" "\n"
    r"$$\lambda_{1,2}=\frac{2+w\pm\sqrt{(2+w)^2-4\left(1+w-2w^2\right)}}2=\frac{2+w\pm\sqrt{9w^2}}2=\frac{2+w\pm3w}2$$" "\n"
    r"$$\lambda=\frac{2+4w}2=1+2w$$ או $$\lambda=\frac{2-2w}2=1-w$$" "\n"
    r"כלומר הערכים העצמיים הם $1+2w$ (פעם אחת) ו-$1-w$ (פעמיים)." "\n"
    r"טבלת סימנים: $1+2w>0\iff w>-\frac12$ ו-$1-w>0\iff w<1$." "\n"
    r"המטריצה מוגדרת חיובית לחלוטין כאשר $-\frac12<w<1$ (כל הערכים העצמיים $>0$)." "\n"
    r"המטריצה מוגדרת חיובית כאשר $-\frac12\le w\le1$ (כל הערכים העצמיים $\ge0$)." "\n"
    r"לא קיים $w$ שעבורו שני הערכים העצמיים שליליים ($w<-\frac12$ וגם $w>1$), ולכן המטריצה אינה מוגדרת שלילית ואינה מוגדרת שלילית לחלוטין לאף $w$." "\n"
    r"עבור $w<-\frac12$ או $w>1$ המטריצה אינה מוגדרת (לא חיובית ולא שלילית)."
)

S3B = (
    r"נניח $\vec v=t\vec u$ ונוכיח $\left|\langle\vec u,\vec v\rangle\right|=\|\vec u\|\cdot\|\vec v\|$ (כיוון ראשון)." "\n"
    r"$$|\langle\vec u,t\vec u\rangle|=\|\vec u\|\cdot\|t\vec u\|\ \Longleftrightarrow\ |t|\,\langle\vec u,\vec u\rangle=\|\vec u\|\cdot|t|\cdot\|\vec u\|\ \Longleftrightarrow\ |t|\,\|\vec u\|^2=\|\vec u\|^2|t|$$" "\n"
    r"וזה נכון. (בשימוש ב-$\|t\vec u\|=\sqrt{\langle t\vec u,t\vec u\rangle}=\sqrt{t^2\langle\vec u,\vec u\rangle}=|t|\,\|\vec u\|$.)" "\n"
    r"כיוון שני: נניח $|\langle\vec u,\vec v\rangle|=\|\vec u\|\cdot\|\vec v\|$. נחלק ב-$\|\vec u\|\|\vec v\|$ ונקבל $\dfrac{|\langle\vec u,\vec v\rangle|}{\|\vec u\|\|\vec v\|}=1=\cos\alpha$, ולכן $\alpha=0^\circ$, כלומר הווקטורים באותו כיוון ו-$\vec v=t\vec u$." "\n"
    r"**הערה:** הצעד האחרון נשען על המשמעות הגיאומטרית של הזווית. טיעון ישיר: נסמן $t=\dfrac{\langle\vec u,\vec v\rangle}{\|\vec u\|^2}$. אז $\|\vec v-t\vec u\|^2=\|\vec v\|^2-\dfrac{\langle\vec u,\vec v\rangle^2}{\|\vec u\|^2}=0$ כאשר מתקיים שוויון בקושי-שוורץ, ולכן $\vec v=t\vec u$."
)

S4A1 = (
    r"$\mathbb{Z}_5=\{0,1,2,3,4\}$. מתקיים $J=\begin{pmatrix}0&4\\1&0\end{pmatrix}\in G$ כי $0\cdot0-1\cdot4=-4\equiv1\pmod5\ne0$." "\n"
    r"הסדר $o(J)=n$ הוא המספר הטבעי המינימלי כך ש-$J^n=I$." "\n"
    r"$$n=2:\ \begin{pmatrix}0&4\\1&0\end{pmatrix}\begin{pmatrix}0&4\\1&0\end{pmatrix}=\begin{pmatrix}4&0\\0&4\end{pmatrix}\ne I$$" "\n"
    r"$$n=3:\ \begin{pmatrix}0&4\\1&0\end{pmatrix}\begin{pmatrix}4&0\\0&4\end{pmatrix}=\begin{pmatrix}0&16\\4&0\end{pmatrix}\equiv\begin{pmatrix}0&1\\4&0\end{pmatrix}\ne I$$" "\n"
    r"$$n=4:\ \begin{pmatrix}4&0\\0&4\end{pmatrix}\begin{pmatrix}4&0\\0&4\end{pmatrix}=\begin{pmatrix}16&0\\0&16\end{pmatrix}\equiv I\pmod5$$" "\n"
    r"$$o(J)=4$$"
)

S4A2 = (
    r"אם $G$ חבורה סופית אז הסדר של כל תת-חבורה של $G$ מחלק את $|G|$ (משפט לגרנז')." "\n"
    r"הסדר של איבר הוא גודל תת-החבורה הציקלית שהוא יוצר: $|\langle J\rangle|=o(J)$." "\n"
    r"לפי לגרנז' $|\langle J\rangle|\ \big|\ |G|$, ומכיוון ש-$o(J)=4$ (מהסעיף הקודם) נקבל $4\mid|G|$."
)

S4A3 = (
    r"נראה ש-$J$ אורתוגונלית: $J^T=\begin{pmatrix}0&1\\4&0\end{pmatrix}$ ו" "\n"
    r"$$\begin{pmatrix}0&4\\1&0\end{pmatrix}\begin{pmatrix}0&1\\4&0\end{pmatrix}=\begin{pmatrix}16&0\\0&1\end{pmatrix}\equiv\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad\begin{pmatrix}0&1\\4&0\end{pmatrix}\begin{pmatrix}0&4\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&16\end{pmatrix}\equiv\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod5$$" "\n"
    r"ולכן $J^T=J^{-1}$." "\n"
    r"נניח $o(A)=n$, כלומר $n$ הוא המספר הטבעי המינימלי עם $A^n=I$. נראה ש-$o\left(J^TAJ\right)=n$." "\n"
    r"$$\left(J^TAJ\right)^n=J^TAJ\,J^TAJ\cdots J^TAJ=J^TA^nJ=J^TIJ=J^TJ=I$$" "\n"
    r"(בגלל $JJ^T=I$ באמצע.) נראה שזה המינימלי: נניח בשלילה $\left(J^TAJ\right)^m=I$ עבור $m<n$. אז $J^TA^mJ=I$, נכפול ב-$J$ משמאל וב-$J^T$ מימין ונקבל $A^m=I$, בסתירה למינימליות של $n$. לכן $o\left(J^TAJ\right)=n=o(A)$."
)

S5A = (
    r"$A=U\Sigma V^T$ עם $A\in M_{2\times3}$: $U$ מסדר $2\times2$, $\Sigma$ מסדר $2\times3$, $V$ מסדר $3\times3$." "\n"
    r"$$AA^T=\begin{pmatrix}1&1&1\\1&-2&1\end{pmatrix}\begin{pmatrix}1&1\\1&-2\\1&1\end{pmatrix}=\begin{pmatrix}3&0\\0&6\end{pmatrix}\ \to\ \lambda_1=6,\ \lambda_2=3$$" "\n"
    r"וקטורים עצמיים: $\begin{pmatrix}0\\1\end{pmatrix}$ עבור $6$ ו-$\begin{pmatrix}1\\0\end{pmatrix}$ עבור $3$. לכן $U=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ ו-$\Sigma=\begin{pmatrix}\sqrt6&0&0\\0&\sqrt3&0\end{pmatrix}$." "\n"
    r"$$A^TA=\begin{pmatrix}2&-1&2\\-1&5&-1\\2&-1&2\end{pmatrix}$$ הערכים העצמיים: $6,3,0$." "\n"
    r"$\lambda=6$: $\ (A^TA-6I)\vec v=0\ \to\ \vec v=\begin{pmatrix}1\\-2\\1\end{pmatrix}\sim\dfrac1{\sqrt6}\begin{pmatrix}1\\-2\\1\end{pmatrix}$" "\n"
    r"$\lambda=3$: $\ \vec v=\begin{pmatrix}1\\1\\1\end{pmatrix}\sim\dfrac1{\sqrt3}\begin{pmatrix}1\\1\\1\end{pmatrix}$" "\n"
    r"$\lambda=0$: $\ \vec v=\begin{pmatrix}-1\\0\\1\end{pmatrix}\sim\dfrac1{\sqrt2}\begin{pmatrix}-1\\0\\1\end{pmatrix}$" "\n"
    r"$$V=\begin{pmatrix}\frac1{\sqrt6}&\frac1{\sqrt3}&-\frac1{\sqrt2}\\-\frac2{\sqrt6}&\frac1{\sqrt3}&0\\\frac1{\sqrt6}&\frac1{\sqrt3}&\frac1{\sqrt2}\end{pmatrix},\qquad V^T=\begin{pmatrix}\frac1{\sqrt6}&-\frac2{\sqrt6}&\frac1{\sqrt6}\\\frac1{\sqrt3}&\frac1{\sqrt3}&\frac1{\sqrt3}\\-\frac1{\sqrt2}&0&\frac1{\sqrt2}\end{pmatrix}$$"
)

questions = [
    Q(1, "computation", "orthogonality", r"סעיף א.1. מערכת אורתוגונלית? (8%)", S1A1, part="א", points=8, contextId="c1"),
    Q(1, "computation", "orthogonality", r"סעיף א.2. מערכת אורתונורמלית? (8%)", S1A2, part="ב", points=8, contextId="c1"),
    Q(1, "proof", "pos_def",
      r"סעיף ב. תהיינה $A,Q\in M_n(\mathbb{R})$ כך ש-$A$ מוגדרת חיובית לחלוטין ו-$Q$ אורתוגונלית. הוכיחו כי $Q^{-1}AQ$ היא מטריצה מוגדרת חיובית לחלוטין. (9%)",
      S1B, part="ג", points=9),

    Q(2, "truefalse", "groups", r"סעיף א. האם $A$ סגורה ביחס לפעולה $*$ ? (5%)", S2A, part="א", points=5, contextId="c2", verdict=True),
    Q(2, "truefalse", "groups", r"סעיף ב. האם הפעולה $*$ היא פעולה אסוציאטיבית? (5%)", S2B, part="ב", points=5, contextId="c2", verdict=True),
    Q(2, "truefalse", "groups", r"סעיף ג. האם ב-$A$ קיים איבר ניטרלי ביחס לפעולה הנ\"ל? (5%)", S2C, part="ג", points=5, contextId="c2",
      verdict=True),
    Q(2, "truefalse", "groups", r"סעיף ד. האם $(A,*)$ היא חבורה? (5%)", S2D, part="ד", points=5, contextId="c2", verdict=True),
    Q(2, "computation", "groups", r"סעיף ה. מצאו את כל האברים $(x,y)\in A$ המקיימים $(x,y)*(x,y)=(x,y)$. (5%)", S2E, part="ה", points=5,
      contextId="c2"),

    Q(3, "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $w$ המטריצה $\begin{pmatrix}1&w&w\\w&1&w\\w&w&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (15%)",
      S3A, part="א", points=15),
    Q(3, "proof", "cauchy_schwarz",
      r"סעיף ב. יהיו $\vec u,\vec v\in\mathbb{R}^n$ וקטורים שונים מ-$\vec 0$. הוכיחו כי $\left|\langle\vec u,\vec v\rangle\right|=\|\vec u\|\cdot\|\vec v\|$ אם ורק אם קיים $t\in\mathbb{R}$ כך ש-$\vec v=t\vec u$. (10%)",
      S3B, part="ב", points=10),

    Q(4, "computation", "groups", r"סעיף א.1. בדקו ש-$J=\begin{pmatrix}0&4\\1&0\end{pmatrix}\in G$ ומצאו את $o(J)$ (הסדר של $J$). (5%)", S4A1,
      part="א", points=5, contextId="c4"),
    Q(4, "proof", "groups", r"סעיף א.2. הוכיחו כי הסדר של $G$ מתחלק ב-4. (5%)", S4A2, part="ב", points=5, contextId="c4"),
    Q(4, "proof", "groups",
      r"סעיף א.3. הראו ש-$J$ מטריצה אורתוגונלית, והוכיחו כי לכל מטריצה $A\in G$ מתקיים: $o(A)=o\left(J^TAJ\right)$. (7%)", S4A3,
      part="ג", points=7, contextId="c4"),
    {"num": 4, "part": "ד", "kind": "computation", "topic": "crt", "points": 8,
     "question": r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod5\\x\equiv3\pmod7\\x\equiv10\pmod{11}\end{cases}$. (8%)",
     "hold": "no-key: the solution file has no answer for this question"},

    Q(5, "computation", "svd", r"סעיף א. מצאו פירוק $SVD$ עבור המטריצה $\begin{pmatrix}1&1&1\\1&-2&1\end{pmatrix}$. (15%)", S5A, part="א", points=15),
    {"num": 5, "part": "ב", "kind": "proof", "topic": "cauchy_schwarz", "points": 10,
     "question": r"סעיף ב. הוכיחו כי לכל שלושה מספרים ממשיים חיוביים $x,y,z$ מתקיים: $\dfrac13\le\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}<1$. (10%)",
     "hold": "no-key: the solution file has no answer for this question"},
]

exam = {
    "examCode": "25A-A",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ה מועד א'",
    "year": 2025,
    "examDate": "13.2.2025",
    "sourceFile": "algebra-2-25A-A-exam",
    "solutionFile": "student-solution-1",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
