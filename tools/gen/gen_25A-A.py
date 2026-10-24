# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-A.json -- algebra-2 (20079), semester A 2025, moed A (13.2.2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25A-A.py

Source: exam 2 pp.; the solution file (16 pp.) is a handwritten student solution, read from the rendered pages,
so every shipped item is solutionSource "student-solution", official false (the refuter checks all of them).
5 questions, 16 items, all shipped.
Q4b (CRT) and Q5b (the sum inequality) are not in the solution file: written by the solver (solutionSource "solved",
  official false, no partial evidence), checked in tools/verify/25A-A/solve_Q4b_Q5b.py. Pending the refuter.
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

S4B = (
    r"$\gcd(5,7)=\gcd(5,11)=\gcd(7,11)=1$ , לכן לפי משפט השאריות הסיני יש פתרון יחיד מודולו $M=5\cdot7\cdot11=385$." "\n"
    r"$a_1=2,\ a_2=3,\ a_3=10$ ; $\ m_1=5,\ m_2=7,\ m_3=11$" "\n"
    r"$$M_1=\frac{385}{5}=77,\qquad M_2=\frac{385}{7}=55,\qquad M_3=\frac{385}{11}=35$$" "\n"
    r"$$M_1x_1\equiv1\pmod 5:\quad77x_1\equiv2x_1\equiv1\pmod 5\ \Rightarrow\ x_1\equiv3\pmod 5$$" "\n"
    r"$$M_2x_2\equiv1\pmod 7:\quad55x_2\equiv6x_2\equiv1\pmod 7\ \Rightarrow\ x_2\equiv6\pmod 7$$" "\n"
    r"$$M_3x_3\equiv1\pmod{11}:\quad35x_3\equiv2x_3\equiv1\pmod{11}\ \Rightarrow\ x_3\equiv6\pmod{11}$$" "\n"
    r"$$x\equiv a_1M_1x_1+a_2M_2x_2+a_3M_3x_3=2\cdot77\cdot3+3\cdot55\cdot6+10\cdot35\cdot6=462+990+2100=3552\pmod{385}$$" "\n"
    r"$$3552=9\cdot385+87\ \Rightarrow\ x\equiv87\pmod{385}$$" "\n"
    r"בדיקה: $87=17\cdot5+2$ , $\ 87=12\cdot7+3$ , $\ 87=7\cdot11+10$."
)

S5B = (
    r"נסמן $a=\sqrt x,\ b=\sqrt y,\ c=\sqrt z$ (מספרים חיוביים), כך ש-$x+y+z=a^2+b^2+c^2$ ו-$\left(\sqrt x+\sqrt y+\sqrt z\right)^2=(a+b+c)^2$." "\n"
    r"**אי-השוויון השמאלי.** נפעיל את אי-שוויון קושי-שוורץ ב-$\mathbb{R}^3$ עם המכפלה הסטנדרטית על $\vec u=(a,b,c)$ ו-$\vec v=(1,1,1)$:" "\n"
    r"$$|\langle\vec u,\vec v\rangle|\le\|\vec u\|\cdot\|\vec v\|\ \Rightarrow\ a+b+c\le\sqrt{a^2+b^2+c^2}\cdot\sqrt3\ \Rightarrow\ (a+b+c)^2\le3\left(a^2+b^2+c^2\right)$$" "\n"
    r"מכיוון ש-$(a+b+c)^2>0$ , נחלק ונקבל $\dfrac{a^2+b^2+c^2}{(a+b+c)^2}\ge\dfrac13$ , כלומר $\dfrac13\le\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}$." "\n"
    r"**אי-השוויון הימני.** נפתח את הריבוע:" "\n"
    r"$$(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ac)>a^2+b^2+c^2$$" "\n"
    r"כי $a,b,c>0$ ולכן $2(ab+bc+ac)>0$. נחלק ב-$(a+b+c)^2>0$ ונקבל $\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}<1$." "\n"
    "מש\"ל"
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
    Q(4, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod5\\x\equiv3\pmod7\\x\equiv10\pmod{11}\end{cases}$. (8%)",
      S4B, part="ד", points=8, solutionSource="solved", official=False, confidence="high"),

    Q(5, "computation", "svd", r"סעיף א. מצאו פירוק $SVD$ עבור המטריצה $\begin{pmatrix}1&1&1\\1&-2&1\end{pmatrix}$. (15%)", S5A, part="א", points=15),
    Q(5, "proof", "cauchy_schwarz",
      r"סעיף ב. הוכיחו כי לכל שלושה מספרים ממשיים חיוביים $x,y,z$ מתקיים: $\dfrac13\le\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}<1$. (10%)",
      S5B, part="ב", points=10, solutionSource="solved", official=False, confidence="high"),
]

# ---------------------------------------------------------------- rubric / pitfalls / steps (step-author, ai-draft)
# Every numeric value is recomputed in tools/verify/25A-A/steps_check.py (sympy / brute force).
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def num(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def ch(prompt, options, correct, explain):
    return {"type": "choice", "prompt": prompt, "options": opts(*options), "correctId": IDS[correct], "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def bug(prompt, lines, idx, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": idx, "explain": explain}


EXTRA = {
    (1, "א"): dict(
        rubric=rub((r"כתיבת התנאי $\langle ax+b,ax-b\rangle=\int_0^1(ax+b)(ax-b)\,dx=0$", 2),
                   (r"פתיחה ואינטגרציה: $\frac{a^2}3-b^2$", 3),
                   (r"פתרון $a=\sqrt3\,b$ (עם $a,b>0$)", 3)),
        pitfalls=["להשתמש במכפלה סקלרית רגילה במקום באינטגרל.",
                  r"לשכוח שהאינטגרל של הקבוע $b^2$ בקטע $[0,1]$ הוא $b^2$.",
                  r"לכתוב $a=\pm\sqrt3\,b$ אף שנתון $a,b>0$."],
        steps=[num(r"עבור $a=3$ ו-$b=1$ חשבו את $\int_0^1(ax+b)(ax-b)\,dx$.", 2,
                   r"$\int_0^1(9x^2-1)\,dx=3-1=2$."),
               order("סדרו את שלבי הפתרון.",
                     [r"$(ax+b)(ax-b)=a^2x^2-b^2$",
                      r"$\int_0^1\left(a^2x^2-b^2\right)dx=\frac{a^2}3-b^2$",
                      r"$\frac{a^2}3-b^2=0$",
                      r"$a=\sqrt3\,b$"],
                     "פותחים, מבצעים אינטגרציה, משווים לאפס ופותרים."),
               ch("איזה קשר בין $a$ ל-$b$ נותן מערכת אורתוגונלית?",
                  [r"$a=\sqrt3\,b$", r"$a=\frac{b}{\sqrt3}$", r"$a=3b$", r"$a=b$"], 0,
                  r"רק עבור $a=\sqrt3\,b$ מתקיים $\frac{a^2}3-b^2=0$. עבור $a=b$ מתקבל $-\frac23b^2\ne0$, עבור $a=3b$ מתקבל $2b^2\ne0$, ועבור $a=\frac b{\sqrt3}$ מתקבל $-\frac89b^2\ne0$.")],
    ),
    (1, "ב"): dict(
        rubric=rub((r"שימוש באורתוגונליות $a=\sqrt3\,b$", 2),
                   (r"כתיבת תנאי הנורמה $\langle u,u\rangle=1$ לשני האיברים", 2),
                   (r"חישוב האינטגרלים: $b^2(2\pm\sqrt3)$", 2),
                   (r"סתירה: אין $a,b>0$", 2)),
        pitfalls=["לדרוש רק $\\langle u,u\\rangle=1$ ולשכוח את האורתוגונליות.",
                  r"לשכוח את האיבר האמצעי $\pm2\sqrt3\,b^2x$ בפיתוח הריבוע.",
                  "לפתור רק את אחת משתי משוואות הנורמה ולהסיק שקיים פתרון."],
        steps=[num(r"אחרי הצבת $a=\sqrt3\,b$ מתקבל $\|ax+b\|^2=c\cdot b^2$. מהו $c$ (עיגול לשלוש ספרות אחרי הנקודה)?",
                   3.732, r"$\int_0^1(3x^2+2\sqrt3\,x+1)\,dx=1+\sqrt3+1=2+\sqrt3\approx3.732$.", tol=0.001),
               num(r"באותו אופן $\|ax-b\|^2=c'\cdot b^2$. מהו $c'$?",
                   0.268, r"$\int_0^1(3x^2-2\sqrt3\,x+1)\,dx=2-\sqrt3\approx0.268$.", tol=0.001),
               ch("מהי המסקנה?",
                  [r"אין $a,b>0$ כאלה: שתי הנורמות דורשות $b^2(2+\sqrt3)=1$ וגם $b^2(2-\sqrt3)=1$, וזה סותר",
                   r"$b=\frac1{\sqrt{2+\sqrt3}}$ ו-$a=\sqrt3\,b$",
                   r"$a=1,\ b=\frac1{\sqrt3}$"], 0,
                  r"עבור $b=\frac1{\sqrt{2+\sqrt3}}$ עם $a=\sqrt3\,b$ הנורמה בריבוע של $ax-b$ היא $\frac{2-\sqrt3}{2+\sqrt3}\ne1$, ועבור $a=1,\ b=\frac1{\sqrt3}$ הנורמה בריבוע של $ax+b$ היא $\frac{2+\sqrt3}3\ne1$.")],
    ),
    (1, "ג"): dict(
        rubric=rub((r"סימטריה: $\left(Q^{-1}AQ\right)^T=Q^{-1}AQ$", 3),
                   (r"הצבה $\vec u=Q\vec v$ והמעבר ל-$\vec u^TA\vec u$", 4),
                   (r"$\vec u\ne\vec0$ כי $Q$ הפיכה, ולכן החיוביות ממש", 2)),
        pitfalls=["לבדוק חיוביות בלבד ולשכוח לבדוק סימטריה.",
                  r"להסתמך על כך שהערכים העצמיים של $Q^{-1}AQ$ שווים לאלה של $A$, בלי להוכיח זאת.",
                  r"לשכוח לנמק ש-$\vec u=Q\vec v\ne\vec0$."],
        steps=[order("סדרו את שלבי ההוכחה.",
                     [r"$Q^{-1}=Q^T$ כי $Q$ אורתוגונלית, ולכן $\left(Q^TAQ\right)^T=Q^TA^TQ=Q^TAQ$ סימטרית.",
                      r"לכל $\vec v\ne\vec0$ נסמן $\vec u=Q\vec v$; $\vec u\ne\vec0$ כי $Q$ הפיכה.",
                      r"$\vec v^T\left(Q^TAQ\right)\vec v=(Q\vec v)^TA(Q\vec v)=\vec u^TA\vec u$",
                      r"$\vec u^TA\vec u>0$ כי $A$ מוגדרת חיובית לחלוטין, ולכן גם $Q^{-1}AQ$ מוגדרת חיובית לחלוטין."],
                     "סימטריה, הצבה, העברת $Q$ לתוך הביטוי, שימוש בנתון על $A$."),
               bug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.",
                   [r"$Q^{-1}=Q^T$ כי $Q$ אורתוגונלית, ולכן $\left(Q^TAQ\right)^T=Q^TA^TQ=Q^TAQ$ סימטרית.",
                    r"לכל $\vec v\ne\vec0$ נסמן $\vec u=Q\vec v$; $\vec u\ne\vec0$ כי $Q$ הפיכה.",
                    r"$\vec v^T\left(Q^TAQ\right)\vec v=\left(Q^T\vec v\right)^TA\left(Q^T\vec v\right)=\vec u^TA\vec u$",
                    r"$\vec u^TA\vec u>0$ כי $A$ מוגדרת חיובית לחלוטין, ולכן גם $Q^{-1}AQ$ מוגדרת חיובית לחלוטין."],
                   2, r"$\vec v^TQ^T=(Q\vec v)^T$, ולכן הביטוי הנכון הוא $(Q\vec v)^TA(Q\vec v)$ ולא עם $Q^T\vec v$.")],
    ),
    (2, "א"): dict(
        rubric=rub((r"כתיבת $(a,b)*(c,d)=\left(a+c+1,\frac{bd}3\right)$ ובדיקה שהרכיבים ממשיים", 1),
                   (r"הרכיב השני $\frac{bd}3\ne0$ כי $b,d\ne0$", 3),
                   ("מסקנה: $A$ סגורה ביחס ל-$*$", 1)),
        pitfalls=["לבדוק רק את הרכיב הראשון ולשכוח את התנאי $y\\ne0$ ב-$A$."],
        steps=[num(r"חשבו את הרכיב השני של $(1,3)*(2,6)$.", 6, r"$\frac{3\cdot6}3=6$."),
               ch("מדוע הרכיב השני של התוצאה שונה מאפס?",
                  [r"כי $b+d\ne0$", r"כי $b\ne0$ ו-$d\ne0$, ולכן $bd\ne0$",
                   r"כי $a+c+1\ne0$"], 1,
                  r"$b+d$ יכול להיות $0$ (למשל $1+(-1)$) ו-$a+c+1$ יכול להיות $0$ (למשל $a=-1,\,c=0$) והסגירות עדיין מתקיימת. מה שמבטיח את הטענה הוא ש-$bd\ne0$.")],
    ),
    (2, "ב"): dict(
        rubric=rub((r"חישוב $\big((a,b)*(c,d)\big)*(x,y)=\left(a+c+x+2,\frac{bdy}9\right)$", 2),
                   ("חישוב הצד השני והגעה לאותו ביטוי", 2),
                   ("מסקנה: הפעולה אסוציאטיבית", 1)),
        pitfalls=[r"לשכוח שהקבוע ברכיב הראשון הוא $+2$ (שני צירופי $+1$).",
                  "להסיק אסוציאטיביות מדוגמה מספרית אחת בלבד."],
        steps=[num(r"חשבו את הרכיב הראשון של $\big((0,3)*(1,3)\big)*(2,3)$.", 5,
                   r"$(0,3)*(1,3)=(2,3)$ ואז $(2,3)*(2,3)=(5,3)$."),
               num(r"ומהו הרכיב השני של אותו ביטוי?", 3, r"$\frac{3\cdot3}3=3$, ואז $\frac{3\cdot3}3=3$.")],
    ),
    (2, "ג"): dict(
        rubric=rub((r"כתיבת התנאי $(e_1,e_2)*(a,b)=(a,b)$", 1),
                   (r"פתרון הרכיב הראשון: $e_1=-1$", 2),
                   (r"פתרון הרכיב השני: $e_2=3$ (חלוקה ב-$b\ne0$)", 2)),
        pitfalls=[r"לנחש $e=(0,1)$ מתוך הרגל מחבורות רגילות במקום לפתור את המשוואות.",
                  r"לשכוח שחלוקה ב-$b$ מותרת רק כי $b\ne0$."],
        steps=[num(r"פתרו את $e_1+a+1=a$. מהו $e_1$?", -1, r"$e_1=-1$."),
               num(r"פתרו את $\frac{e_2b}3=b$ עבור $b\ne0$. מהו $e_2$?", 3, r"מכפילים ב-$3$ ומחלקים ב-$b$: $e_2=3$.")],
    ),
    (2, "ד"): dict(
        rubric=rub(("הפניה לסגירות, אסוציאטיביות ואיבר ניטרלי מהסעיפים הקודמים", 1),
                   (r"כתיבת $(a,b)*\left(a^{-1},b^{-1}\right)=(-1,3)$", 1),
                   (r"פתרון ההופכי $\left(-2-a,\frac9b\right)$", 2),
                   (r"ההופכי ב-$A$ כי $\frac9b\ne0$, ולכן $A$ חבורה", 1)),
        pitfalls=[r"לחפש הופכי ביחס ל-$(1,1)$ במקום ביחס לאיבר הניטרלי $(-1,3)$.",
                  r"לשכוח לוודא ש-$\frac9b\ne0$, כדי שההופכי יהיה ב-$A$."],
        steps=[num(r"מהו הרכיב הראשון של ההופכי של $(4,6)$?", -6, r"$-2-a=-2-4=-6$."),
               num(r"ומהו הרכיב השני של ההופכי של $(4,6)$?", 1.5, r"$\frac9b=\frac96=1.5$. בדיקה: $(4,6)*(-6,1.5)=(-1,3)$.", tol=0.001)],
    ),
    (2, "ה"): dict(
        rubric=rub((r"הצבה: $(x,y)*(x,y)=\left(2x+1,\frac{y^2}3\right)$", 1),
                   (r"פתרון $2x+1=x$: $x=-1$", 2),
                   (r"פתרון $\frac{y^2}3=y$ עם $y\ne0$: $y=3$", 2)),
        pitfalls=[r"לכלול את $y=0$ כפתרון, אף ש-$y\ne0$ ב-$A$.",
                  "להחליף בין שני הרכיבים כשמשווים את $(x,y)*(x,y)$ ל-$(x,y)$."],
        steps=[num(r"פתרו את $2x+1=x$. מהו $x$?", -1, r"$x=-1$."),
               ch(r"המשוואה $\frac{y^2}3=y$ מתקיימת גם עבור $y=0$. מדוע $y=0$ אינו פתרון של השאלה?",
                  [r"כי $y\ne0$ בהגדרת $A$", r"כי $0$ אינו מקיים את המשוואה", r"כי $y=0$ נותן $x\ne-1$"], 0,
                  r"$\frac{0^2}3=0$, ולכן $y=0$ כן מקיים את המשוואה, ו-$x$ ו-$y$ אינם תלויים זה בזה; הוא נפסל רק כי $(x,0)\notin A$."),
               num(r"פתרו את $\frac{y^2}3=y$ עם $y\ne0$. מהו $y$?", 3, r"מחלקים ב-$y$: $\frac y3=1$, כלומר $y=3$.")],
    ),
    (3, "א"): dict(
        rubric=rub((r"חישוב הערכים העצמיים $1+2w$ ו-$1-w$ (פעמיים)", 6),
                   (r"מוגדרת חיובית: $-\frac12\le w\le1$", 2),
                   (r"מוגדרת חיובית לחלוטין: $-\frac12<w<1$", 2),
                   ("מוגדרת שלילית ולחלוטין: אף ערך", 3),
                   (r"אף אחת מהן עבור $w<-\frac12$ או $w>1$", 2)),
        pitfalls=[r"להתבלבל בין $\ge0$ (מוגדרת חיובית) ל-$>0$ (לחלוטין) בקצוות $w=-\frac12$ ו-$w=1$.",
                  r"לשכוח שהערך העצמי $1-w$ מופיע פעמיים.",
                  "להסיק שהמטריצה מוגדרת שלילית רק מכך שחלק מהערכים העצמיים שליליים."],
        steps=[num(r"הווקטור $(1,1,1)^T$ הוא וקטור עצמי של המטריצה. עבור $w=2$ מהו הערך העצמי שלו?", 5,
                   r"כל שורה מסכמת ל-$1+2w=5$."),
               ch("עבור אילו $w$ המטריצה מוגדרת חיובית (לא בהכרח לחלוטין)?",
                  [r"$-\frac12\le w\le1$", r"$-\frac12<w<1$", r"$0\le w\le1$", r"$w\le1$"], 0,
                  r"הערכים העצמיים הם $1+2w,\,1-w,\,1-w$ וכולם $\ge0$ בדיוק כאשר $-\frac12\le w\le1$. עבור $w=1$ מתקבלים $3,0,0$ (חיובית), עבור $w=-\frac14$ מתקבלים $\frac12,\frac54,\frac54$, ועבור $w=-1$ יש ערך עצמי שלילי."),
               ch("עבור אילו $w$ המטריצה מוגדרת חיובית לחלוטין?",
                  [r"$-\frac12\le w\le1$", r"$-\frac12<w<1$", r"$w>-\frac12$"], 1,
                  r"נדרש $1+2w>0$ וגם $1-w>0$. בקצוות יש ערך עצמי $0$, ועבור $w=2$ יש ערך עצמי שלילי."),
               ch("עבור אילו $w$ המטריצה מוגדרת שלילית?",
                  [r"עבור אף $w$", r"$w<-\frac12$", r"$w>1$"], 0,
                  r"נדרש $1+2w\le0$ וגם $1-w\le0$, כלומר $w\le-\frac12$ וגם $w\ge1$. עבור $w=-1$ הערכים הם $-1,2,2$ ועבור $w=2$ הערכים הם $5,-1,-1$: בשני המקרים יש ערך עצמי חיובי.")],
    ),
    (3, "ב"): dict(
        rubric=rub((r"כיוון ⇐: $\langle u,tu\rangle=t\|u\|^2$ ו-$\|tu\|=|t|\,\|u\|$, ולכן שוויון", 4),
                   (r"כיוון ⇒: שוויון בקושי-שוורץ גורר $\|v-tu\|=0$ (או $\cos\alpha=1$)", 4),
                   (r"מסקנה $\vec v=t\vec u$", 2)),
        pitfalls=[r"לכתוב $\|t\vec u\|=t\|\vec u\|$ בלי ערך מוחלט.",
                  "בכיוון ⇒ לומר 'הזווית היא $0$' בלי לנמק, וזה בעצם הטענה עצמה.",
                  r"לשכוח ש-$\vec u,\vec v\ne\vec0$ כדי שמותר לחלק בנורמות."],
        steps=[ch(r"מהי $\|t\vec u\|$?",
                  [r"$t\,\|\vec u\|$", r"$|t|\,\|\vec u\|$", r"$t^2\|\vec u\|$", r"$\sqrt{|t|}\,\|\vec u\|$"], 1,
                  r"$\|t\vec u\|=\sqrt{t^2\langle u,u\rangle}=|t|\,\|u\|$. הביטוי $t\|u\|$ שלילי כש-$t<0$, $t^2\|u\|$ נותן $4\|u\|$ במקום $2\|u\|$ עבור $t=2$, ו-$\sqrt{|t|}\|u\|$ נותן $2\|u\|$ במקום $4\|u\|$ עבור $t=4$."),
               order(r"סדרו את הטיעון הישיר לכיוון ⇒ (נתון שוויון בקושי-שוורץ).",
                     [r"נסמן $t=\frac{\langle\vec u,\vec v\rangle}{\|\vec u\|^2}$.",
                      r"$\|\vec v-t\vec u\|^2=\|\vec v\|^2-\frac{\langle\vec u,\vec v\rangle^2}{\|\vec u\|^2}$.",
                      r"בשוויון קושי-שוורץ $\langle\vec u,\vec v\rangle^2=\|\vec u\|^2\|\vec v\|^2$, ולכן הביטוי שווה $0$.",
                      r"$\|\vec v-t\vec u\|=0$, כלומר $\vec v=t\vec u$."],
                     "מגדירים את $t$, מחשבים את הנורמה, מציבים את השוויון ומסיקים."),
               bug("בטיעון הבא שורה אחת שגויה. מצאו אותה.",
                   [r"נסמן $t=\frac{\langle\vec u,\vec v\rangle}{\|\vec u\|^2}$.",
                    r"$\|\vec v-t\vec u\|^2=\|\vec v\|^2+\frac{\langle\vec u,\vec v\rangle^2}{\|\vec u\|^2}$.",
                    r"בשוויון קושי-שוורץ $\langle\vec u,\vec v\rangle^2=\|\vec u\|^2\|\vec v\|^2$, ולכן הביטוי שווה $0$.",
                    r"$\|\vec v-t\vec u\|=0$, כלומר $\vec v=t\vec u$."],
                   1, r"$\|v-tu\|^2=\|v\|^2-2t\langle u,v\rangle+t^2\|u\|^2=\|v\|^2-\frac{\langle u,v\rangle^2}{\|u\|^2}$: הסימן מינוס, ולא פלוס.")],
    ),
    (4, "א"): dict(
        rubric=rub((r"בדיקה ש-$J\in G$: הדטרמיננטה $1\ne0$ מודולו 5", 1),
                   (r"חישוב $J^2=4I$ ו-$J^3$", 2),
                   (r"חישוב $J^4=I$", 1),
                   (r"מסקנה $o(J)=4$", 1)),
        pitfalls=[r"לשכוח לעבוד מודולו 5 (להשאיר $16$ במקום $1$).",
                  r"לעצור ב-$J^2=4I\ne I$ ולהסיק שהסדר $2$."],
        steps=[num(r"חשבו את $0\cdot0-1\cdot4$ מודולו 5 (שארית בין $0$ ל-$4$).", 1, r"$-4\equiv1\pmod5$, שונה מ-$0$, ולכן $J\in G$."),
               num(r"מהו הרכיב השמאלי העליון של $J^2$ (מודולו 5)?", 4, r"$0\cdot0+4\cdot1=4$."),
               num(r"מהו $o(J)$?", 4, r"$J^2=4I$, $J^3\equiv\begin{pmatrix}0&1\\4&0\end{pmatrix}$, $J^4=16I\equiv I$.")],
    ),
    (4, "ב"): dict(
        rubric=rub((r"$\left|\langle J\rangle\right|=o(J)=4$", 2),
                   ("שימוש במשפט לגרנז': סדר תת-חבורה מחלק את סדר החבורה", 2),
                   (r"מסקנה: $4$ מחלק את $|G|$", 1)),
        pitfalls=[r"להפוך את לגרנז' ולטעון ש-$|G|$ מחלק את הסדר של $J$.",
                  "לשכוח להזכיר שהסדר של איבר הוא גודל תת-החבורה הציקלית שהוא יוצר."],
        steps=[ch("באיזה משפט משתמש הפתרון?",
                  ["משפט לגרנז'", "משפט השאריות הסיני", "אי-שוויון קושי-שוורץ"], 0,
                  "הטענה היא על סדר תת-חבורה וסדר החבורה, וזה משפט לגרנז'. משפט השאריות הסיני עוסק במשוואות מודולריות, ואי-שוויון קושי-שוורץ במרחבי מכפלה פנימית."),
               order("סדרו את שלבי ההוכחה.",
                     [r"$o(J)=4$, ולכן תת-החבורה הציקלית $\langle J\rangle$ היא בגודל $4$.",
                      r"לפי משפט לגרנז', גודל תת-חבורה של חבורה סופית מחלק את $|G|$.",
                      r"לכן $4\mid|G|$."],
                     "מגדירים את תת-החבורה, מפעילים את לגרנז' ומסיקים.")],
    ),
    (4, "ג"): dict(
        rubric=rub((r"הראיה ש-$J^T=J^{-1}$ (בדיקת $JJ^T=I$ מודולו 5)", 2),
                   (r"$\left(J^TAJ\right)^n=J^TA^nJ=I$", 2),
                   (r"מינימליות: הנחה בשלילה $m<n$ וסתירה", 2),
                   ("סיכום השוויון בין הסדרים", 1)),
        pitfalls=[r"להראות רק ש-$\left(J^TAJ\right)^n=I$ ולא שהוא המינימלי.",
                  r"לשכוח לעבוד מודולו 5 בבדיקת $JJ^T=I$ (כי $16\equiv1$)."],
        steps=[num(r"במכפלה $JJ^T=\begin{pmatrix}16&0\\0&1\end{pmatrix}$ מהו הרכיב השמאלי העליון מודולו 5 (בין $0$ ל-$4$)?", 1,
                   r"$16\equiv1\pmod5$, ולכן $JJ^T=I$."),
               order(r"סדרו את שלבי ההוכחה ש-$o\left(J^TAJ\right)=o(A)$.",
                     [r"$JJ^T=I$, ולכן $\left(J^TAJ\right)^m=J^TA^mJ$ לכל $m$; עבור $m=o(A)=n$ מתקבל $J^TIJ=I$.",
                      r"נניח בשלילה $\left(J^TAJ\right)^m=I$ עבור $m<n$. אז $J^TA^mJ=I$.",
                      r"נכפול ב-$J$ משמאל וב-$J^T$ מימין ונקבל $A^m=I$, בסתירה למינימליות של $n$.",
                      r"לכן $o\left(J^TAJ\right)=n=o(A)$."],
                     "קודם מראים שהחזקה $n$ נותנת $I$, אחר כך שאין חזקה קטנה יותר.")],
    ),
    (4, "ד"): dict(
        rubric=rub(("זרות המודולים וחישוב $M=385$", 1),
                   (r"$M_1,M_2,M_3=77,55,35$", 2),
                   (r"ההופכיים $x_1,x_2,x_3=3,6,6$", 3),
                   (r"הסכום והרדוקציה: $x\equiv87\pmod{385}$", 2)),
        pitfalls=[r"לשכוח לרדד את $M_i$ מודולו $m_i$ לפני מציאת ההופכי.",
                  r"לשכוח לרדד את הסכום $3552$ מודולו $385$."],
        steps=[num(r"מהו $M=5\cdot7\cdot11$?", 385, r"$5\cdot77=385$."),
               num(r"מהו $x_1$ (בין $0$ ל-$4$) המקיים $77x_1\equiv1\pmod5$?", 3, r"$77\equiv2$ ו-$2\cdot3=6\equiv1$."),
               num(r"מהו $x_3$ (בין $0$ ל-$10$) המקיים $35x_3\equiv1\pmod{11}$?", 6, r"$35\equiv2$ ו-$2\cdot6=12\equiv1$."),
               num(r"מהו הפתרון $x$ בין $0$ ל-$384$?", 87, r"$3552=9\cdot385+87$.")],
    ),
    (5, "א"): dict(
        rubric=rub((r"המימדים: $U$ מסדר $2\times2$, $\Sigma$ מסדר $2\times3$, $V$ מסדר $3\times3$", 2),
                   (r"$AA^T$ והערכים העצמיים $6,3$", 3),
                   (r"$U$ ו-$\Sigma$ (הערכים הסינגולריים $\sqrt6,\sqrt3$)", 3),
                   (r"$A^TA$ והערכים העצמיים $6,3,0$", 3),
                   (r"וקטורים עצמיים מנורמלים והרכבת $V$", 4)),
        pitfalls=[r"לרשום את הערכים הסינגולריים $6,3$ במקום $\sqrt6,\sqrt3$.",
                  "לא לסדר את העמודות של $U$ ושל $V$ באותו סדר של הערכים הסינגולריים.",
                  "לשכוח לנרמל את הווקטורים העצמיים."],
        steps=[ch(r"$A$ מסדר $2\times3$. מהו הסדר של $\Sigma$ בפירוק $A=U\Sigma V^T$?",
                  [r"$2\times3$", r"$3\times3$", r"$2\times2$"], 0,
                  r"$U$ הוא $2\times2$ ו-$V$ הוא $3\times3$, ולכן $\Sigma$ חייבת להיות $2\times3$ כדי שהמכפלה תהיה $2\times3$."),
               ch("מאיזו מטריצה מקבלים את העמודות של $U$?",
                  [r"$A^TA$", r"$AA^T$"], 1,
                  r"$AA^T$ היא $2\times2$ כמו $U$. $A^TA$ היא $3\times3$, ולכן וקטוריה העצמיים שייכים ל-$V$."),
               num(r"מהו הערך הסינגולרי הגדול $\sigma_1$ (עיגול לשלוש ספרות אחרי הנקודה)?", 2.449,
                   r"$\lambda_1=6$ ולכן $\sigma_1=\sqrt6\approx2.449$.", tol=0.001),
               num(r"מהו הערך הסינגולרי השני $\sigma_2$?", 1.732, r"$\lambda_2=3$ ולכן $\sigma_2=\sqrt3\approx1.732$.", tol=0.001)],
    ),
    (5, "ב"): dict(
        rubric=rub((r"בחירת הווקטורים $(\sqrt x,\sqrt y,\sqrt z)$ ו-$(1,1,1)$ והפעלת קושי-שוורץ", 3),
                   (r"הגעה ל-$(a+b+c)^2\le3\left(a^2+b^2+c^2\right)$ וחלוקה", 2),
                   ("פתיחת הריבוע וחיוביות המכפלות המעורבות", 3),
                   ("חלוקה והסקת אי-השוויון הימני", 2)),
        pitfalls=[r"להפעיל קושי-שוורץ על $(x,y,z)$ במקום על $(\sqrt x,\sqrt y,\sqrt z)$.",
                  r"לכתוב $<$ בצד השמאלי: השוויון $\frac13$ מתקבל כש-$x=y=z$."],
        steps=[ch("על אילו שני וקטורים מפעילים את קושי-שוורץ בצד השמאלי?",
                  [r"$(\sqrt x,\sqrt y,\sqrt z)$ ו-$(1,1,1)$", r"$(x,y,z)$ ו-$(1,1,1)$"], 0,
                  r"הווקטורים $(\sqrt x,\sqrt y,\sqrt z)$ ו-$(1,1,1)$ נותנים $\left(\sqrt x+\sqrt y+\sqrt z\right)^2\le3(x+y+z)$. הווקטורים $(x,y,z)$ ו-$(1,1,1)$ נותנים $(x+y+z)^2\le3\left(x^2+y^2+z^2\right)$, שזו טענה אחרת."),
               num(r"מהו $\|(1,1,1)\|^2$?", 3, r"$1+1+1=3$."),
               num(r"עבור $x=y=z=1$ מהו הערך של $\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}$ (עיגול לארבע ספרות אחרי הנקודה)?", 0.3333,
                   r"$\frac39=\frac13$: האי-שוויון השמאלי הוא שוויון כאן.", tol=0.0001),
               order("סדרו את הוכחת אי-השוויון הימני.",
                     [r"$(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ac)$, והמכפלות המעורבות חיוביות כי $a,b,c>0$.",
                      r"לכן $(a+b+c)^2>a^2+b^2+c^2$.",
                      r"מחלקים ב-$(a+b+c)^2>0$ ומקבלים $\frac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}<1$."],
                     "פותחים, משווים, מחלקים.")],
    ),
}

for _q in questions:
    _e = EXTRA.pop((_q["num"], _q.get("part")))
    _q.update(_e)
    _q["rubricSource"] = "ai-draft"
    _q["stepsSource"] = "ai-draft"
    assert sum(r["points"] for r in _q["rubric"]) == _q["points"], (_q["num"], _q.get("part"))
assert not EXTRA, EXTRA

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
