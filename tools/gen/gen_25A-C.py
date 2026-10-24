# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-C.json -- algebra-2 (20079), semester A 2025, moed C (no date printed).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25A-C.py

Source: exam only, pp. 274-275 of the 275-page compilation (the solution of the preceding sitting sits on pp.
272-273 and is not this exam's). There is NO key: all 15 items are solved by the solver (solutionSource "solved",
official false, confidence high) and go to the refuter.
Part letters: Q2: a.1..a.4 -> a..d, b.1 -> e, b.2 -> f. Q5: a, b.1 -> b, b.2 -> c. Q1, Q3, Q4: a, b.

Solver notes (checks: tools/verify/25A-C/solve_all.py, sympy + brute force, all OK):
- Q2b.2 "B^T A B מוגדרת חיובית" with B any real matrix. In this course "מוגדרת חיובית" means v^T M v >= 0
  (eigenvalues >= 0) and "מוגדרת חיובית לחלוטין" is the strict version (Q4a of this very sheet lists both terms;
  same usage in 23B-B, 24A-A, 26A-A). In the course sense the claim holds for every B. In the strict sense it fails for
  singular B (A=I, B=diag(1,0)) and holds when A is strictly PD and B invertible. The solution proves the course sense
  and carries a visible "הערה:" on the strict reading. Q2b.1 gets the same kind of note.
- Q4b prints "x = 3 (mod 2)"; 3 = 1 (mod 2), the answer is the same either way (x = 67 mod 70).
- Partial evidence: sitting 23B-B (typed official) reuses Q1b, all of Q2 (a.1-a.4, b.1, b.2), Q4a (as its Q3a),
  Q5a (as its Q4a) and Q5b (as its Q4b). Every answer here was derived independently and agrees with 23B-B's:
  (1,1), (3,5), 24, 12; Q2b proved in the >= 0 sense there too; Q4a a>=1 / a>1 / never negative; Q5a eigenvalues
  0,5,5 with the same eigenvectors. Q1a, Q3a, Q3b, Q4b have no reused source.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-C.json"


def Q(num, part, kind, topic, question, points, solution, **kw):
    q = {"num": num, "part": part, "kind": kind, "topic": topic, "question": question, "points": points,
         "solution": solution, "solutionSource": "solved", "official": False, "confidence": "high"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"נסתכל בחבורה (אין צורך להוכיח זאת) $G=\left\{(a,b)\ \middle|\ a\in\mathbb{Z}_5^*,\ b\in\mathbb{Z}_7^*\right\}$ עם פעולת הכפל המוגדרת בצורה הבאה: $(a,b)\cdot(c,d)=(a\cdot c,\ b\cdot d)$, כאשר באגף ימין הכפל הוא מודולו 5 ו-7 בהתאמה."},
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף ב",
            "text": r"תהיינה $A,B\in M_n(\mathbb{R})$, כאשר $A$ מוגדרת חיובית. הוכיחו כי:"},
    "c5b": {"kind": "text", "title": "שאלה 5 סעיף ב",
            "text": r"תהי $G$ חבורה בה כל איבר הופכי לעצמו. זאת אומרת לכל $x\in G$ מתקיים $x=x^{-1}$. הוכיחו כי:"},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"נחפש ישר מהצורה $y=mx+n$ לפי שיטת הריבועים הפחותים. נרשום את המערכת $A\begin{pmatrix}m\\n\end{pmatrix}\approx\vec b$:" "\n"
    r"$$A=\begin{pmatrix}-4&1\\-2&1\\2&1\\4&1\\5&1\end{pmatrix},\qquad\vec b=\begin{pmatrix}-1\\0\\4\\5\\6\end{pmatrix}$$" "\n"
    r"משוואות נורמליות $A^TA\begin{pmatrix}m\\n\end{pmatrix}=A^T\vec b$:" "\n"
    r"$$A^TA=\begin{pmatrix}\sum x_i^2&\sum x_i\\\sum x_i&5\end{pmatrix}=\begin{pmatrix}65&5\\5&5\end{pmatrix},\qquad A^T\vec b=\begin{pmatrix}\sum x_iy_i\\\sum y_i\end{pmatrix}=\begin{pmatrix}62\\14\end{pmatrix}$$" "\n"
    r"($\sum x_i^2=16+4+4+16+25=65$, $\sum x_i=5$, $\sum x_iy_i=4+0+8+20+30=62$, $\sum y_i=14$.)" "\n"
    r"$$\begin{cases}65m+5n=62\\5m+5n=14\end{cases}\ \Rightarrow\ 60m=48\ \Rightarrow\ m=0.8,\qquad n=\frac{14-5\cdot0.8}{5}=2$$" "\n"
    r"**תשובה:** $y=0.8x+2$."
)

S1B = (
    r"נסתכל במרחב $C_{[1,2]}$ עם המכפלה הפנימית $\langle f,g\rangle=\displaystyle\int_1^2f(x)g(x)\,dx$." "\n"
    r"נבחר $g(x)=\dfrac1x$ (רציפה ב-$[1,2]$). לפי אי-שוויון קושי-שוורץ $\langle f,g\rangle^2\le\|f\|^2\cdot\|g\|^2$:" "\n"
    r"$$\langle f,g\rangle^2=\left(\int_1^2\frac{f(x)}x\,dx\right)^2,\qquad\|f\|^2=\int_1^2f^2(x)\,dx,\qquad\|g\|^2=\int_1^2\frac1{x^2}\,dx=\left[-\frac1x\right]_1^2=-\frac12+1=\frac12$$" "\n"
    "ולכן\n"
    r"$$\left(\int_1^2\frac{f(x)}x\,dx\right)^2\le\frac12\int_1^2f^2(x)\,dx$$"
)

S2A1 = (
    r"האיבר הניטרלי של $\mathbb{Z}_5^*$ הוא $1$ ושל $\mathbb{Z}_7^*$ הוא $1$. לכל $(a,b)\in G$:" "\n"
    r"$$(1,1)\cdot(a,b)=(1\cdot a,\ 1\cdot b)=(a,b)=(a,b)\cdot(1,1)$$" "\n"
    r"**תשובה:** האיבר הניטרלי הוא $e=(1,1)$."
)

S2A2 = (
    r"מחפשים $(c,d)\in G$ כך ש-$(2,3)\cdot(c,d)=(2c,3d)=(1,1)$, כלומר $2c\equiv1\pmod5$ ו-$3d\equiv1\pmod7$." "\n"
    r"$$2\cdot3=6\equiv1\pmod5\ \Rightarrow\ c=3,\qquad 3\cdot5=15\equiv1\pmod7\ \Rightarrow\ d=5$$" "\n"
    r"**תשובה:** $(2,3)^{-1}=(3,5)$. בדיקה: $(2,3)\cdot(3,5)=(6\bmod5,\ 15\bmod7)=(1,1)$."
)

S2A3 = (
    r"$\mathbb{Z}_5^*=\{1,2,3,4\}$ ו-$\mathbb{Z}_7^*=\{1,2,3,4,5,6\}$ (כל השאריות השונות מ-0, כי 5 ו-7 ראשוניים). כל זוג $(a,b)$ עם $a\in\mathbb{Z}_5^*$, $b\in\mathbb{Z}_7^*$ הוא איבר של $G$, ולכן" "\n"
    r"$$|G|=|\mathbb{Z}_5^*|\cdot|\mathbb{Z}_7^*|=4\cdot6=24$$"
)

S2A4 = (
    r"$(2,3)^k=(2^k\bmod5,\ 3^k\bmod7)$, ולכן $(2,3)^k=(1,1)$ אם ורק אם $2^k\equiv1\pmod5$ וגם $3^k\equiv1\pmod7$." "\n"
    r"חזקות של $2$ מודולו 5: $2,4,3,1$, כלומר $o(2)=4$. חזקות של $3$ מודולו 7: $3,2,6,4,5,1$, כלומר $o(3)=6$." "\n"
    r"לכן $(2,3)^k=(1,1)$ אם ורק אם $4\mid k$ וגם $6\mid k$, כלומר $\mathrm{lcm}(4,6)=12\mid k$." "\n"
    r"(למשל $(2,3)^4=(1,4)\ne(1,1)$ ו-$(2,3)^6=(4,1)\ne(1,1)$.)" "\n"
    r"**תשובה:** הסדר של $(2,3)$ הוא $12$."
)

S2B1 = (
    r"בקורס, מטריצה $M$ מוגדרת חיובית אם היא סימטרית ו-$\vec v^TM\vec v\ge0$ לכל $\vec v$, ומוגדרת שלילית אם היא סימטרית ו-$\vec v^TM\vec v\le0$ לכל $\vec v$." "\n"
    r"**סימטריות:** $\left(-A-B^TB\right)^T=-A^T-B^T\left(B^T\right)^T=-A-B^TB$, כי $A$ סימטרית." "\n"
    r"**הסימן:** לכל $\vec v\in\mathbb{R}^n$:" "\n"
    r"$$\vec v^T\left(-A-B^TB\right)\vec v=-\vec v^TA\vec v-(B\vec v)^T(B\vec v)=-\underbrace{\vec v^TA\vec v}_{\ge0}-\underbrace{\|B\vec v\|^2}_{\ge0}\le0$$" "\n"
    r"לכן $-A-B^TB$ מוגדרת שלילית." "\n"
    r"הערה: אם $A$ מוגדרת חיובית לחלוטין, אז לכל $\vec v\ne\vec0$ מתקיים $\vec v^TA\vec v>0$, והביטוי שלמעלה קטן ממש מ-0. במקרה זה $-A-B^TB$ מוגדרת שלילית לחלוטין, לכל $B$."
)

S2B2 = (
    r"**סימטריות:** $\left(B^TAB\right)^T=B^TA^T\left(B^T\right)^T=B^TAB$, כי $A$ סימטרית." "\n"
    r"**הסימן:** לכל $\vec v\in\mathbb{R}^n$ נסמן $\vec w=B\vec v$. אז" "\n"
    r"$$\vec v^T\left(B^TAB\right)\vec v=\left(B\vec v\right)^TA\left(B\vec v\right)=\vec w^TA\vec w\ge0$$" "\n"
    r"כי $A$ מוגדרת חיובית. לכן $B^TAB$ מוגדרת חיובית, לכל $B\in M_n(\mathbb{R})$." "\n"
    r"הערה: הטענה נכונה במובן של הקורס, שבו \"מוגדרת חיובית\" פירושו $\vec v^TM\vec v\ge0$. במובן החזק (מוגדרת חיובית **לחלוטין**) הטענה אינה נכונה כפי שהיא מנוסחת, כי $B$ יכולה להיות סינגולרית. למשל $A=I$, $B=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ נותנות $B^TAB=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, שיש לה ערך עצמי $0$. אם מניחים בנוסף ש-$A$ מוגדרת חיובית לחלוטין ו-$B$ הפיכה, אז לכל $\vec v\ne\vec0$ גם $\vec w=B\vec v\ne\vec0$, ולכן $\vec w^TA\vec w>0$. במקרה זה $B^TAB$ מוגדרת חיובית לחלוטין."
)

S3A = (
    r"נחשב $AA^T$ (מסדר $2\times2$):" "\n"
    r"$$AA^T=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}\begin{pmatrix}1&2\\0&0\\2&1\end{pmatrix}=\begin{pmatrix}5&4\\4&5\end{pmatrix},\qquad|AA^T-\lambda I|=(5-\lambda)^2-16=0\ \Rightarrow\ \lambda_1=9,\ \lambda_2=1$$" "\n"
    r"הערכים הסינגולריים: $\sigma_1=\sqrt9=3$, $\sigma_2=\sqrt1=1$." "\n"
    r"**וקטורים עצמיים של $AA^T$ (העמודות של $U$):**" "\n"
    r"$$\lambda=9:\ \begin{pmatrix}-4&4\\4&-4\end{pmatrix}\vec u=\vec0\ \Rightarrow\ \vec u_1=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},\qquad\lambda=1:\ \begin{pmatrix}4&4\\4&4\end{pmatrix}\vec u=\vec0\ \Rightarrow\ \vec u_2=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$$" "\n"
    r"**העמודות של $V$:** $\vec v_i=\dfrac1{\sigma_i}A^T\vec u_i$:" "\n"
    r"$$\vec v_1=\frac13\begin{pmatrix}1&2\\0&0\\2&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}=\frac13\cdot\frac1{\sqrt2}\begin{pmatrix}3\\0\\3\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1\\0\\1\end{pmatrix},\qquad\vec v_2=\frac11\begin{pmatrix}1&2\\0&0\\2&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}-1\\0\\1\end{pmatrix}$$" "\n"
    r"את $\vec v_3$ נשלים לבסיס אורתונורמלי של $\mathbb{R}^3$: וקטור יחידה האורתוגונלי ל-$\vec v_1,\vec v_2$ (הוא וקטור עצמי של $A^TA$ עבור $\lambda=0$): $\vec v_3=\begin{pmatrix}0\\1\\0\end{pmatrix}$." "\n"
    "**הפירוק:**\n"
    r"$$A=U\Sigma V^T=\begin{pmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}\\\frac1{\sqrt2}&-\frac1{\sqrt2}\end{pmatrix}\cdot\begin{pmatrix}3&0&0\\0&1&0\end{pmatrix}\cdot\begin{pmatrix}\frac1{\sqrt2}&-\frac1{\sqrt2}&0\\0&0&1\\\frac1{\sqrt2}&\frac1{\sqrt2}&0\end{pmatrix}^T$$" "\n"
    r"(כאן $V=\begin{pmatrix}\vec v_1&\vec v_2&\vec v_3\end{pmatrix}$ כעמודות.)"
)

S3B = (
    r"נשתמש בתכונות המכפלה הפנימית הממשית: ליניאריות וסימטריות ($\langle\vec v,\vec u\rangle=\langle\vec u,\vec v\rangle$)." "\n"
    r"$$\|\vec u+\vec v\|^2=\langle\vec u+\vec v,\vec u+\vec v\rangle=\langle\vec u,\vec u\rangle+\langle\vec u,\vec v\rangle+\langle\vec v,\vec u\rangle+\langle\vec v,\vec v\rangle=\|\vec u\|^2+2\langle\vec u,\vec v\rangle+\|\vec v\|^2$$" "\n"
    r"$$\|\vec u-\vec v\|^2=\langle\vec u-\vec v,\vec u-\vec v\rangle=\langle\vec u,\vec u\rangle-\langle\vec u,\vec v\rangle-\langle\vec v,\vec u\rangle+\langle\vec v,\vec v\rangle=\|\vec u\|^2-2\langle\vec u,\vec v\rangle+\|\vec v\|^2$$" "\n"
    "נחסר את השוויון השני מהראשון:\n"
    r"$$\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2=4\langle\vec u,\vec v\rangle\ \Rightarrow\ \langle\vec u,\vec v\rangle=\frac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$$"
)

S4A = (
    r"המטריצה סימטרית. נחשב את הערכים העצמיים (פיתוח לפי השורה האמצעית):" "\n"
    r"$$\begin{vmatrix}a^2-\lambda&0&1\\0&a-\lambda&0\\1&0&a^2-\lambda\end{vmatrix}=(a-\lambda)\left[(a^2-\lambda)^2-1\right]=(a-\lambda)(a^2-1-\lambda)(a^2+1-\lambda)$$" "\n"
    r"הערכים העצמיים: $\lambda_1=a$, $\lambda_2=a^2-1$, $\lambda_3=a^2+1$." "\n"
    r"**מוגדרת חיובית** (כל הערכים העצמיים $\ge0$): $a\ge0$ וגם $a^2\ge1$ (ו-$a^2+1\ge0$ תמיד), כלומר $a\ge1$." "\n"
    r"**מוגדרת חיובית לחלוטין** (כולם $>0$): $a>0$ וגם $a^2>1$, כלומר $a>1$." "\n"
    r"**מוגדרת שלילית** (כולם $\le0$): דורש $a^2+1\le0$, וזה לא מתקיים לאף $a$. לכן אין ערכי $a$ עבורם המטריצה מוגדרת שלילית, ובפרט אין ערכים עבורם היא שלילית לחלוטין." "\n"
    "**סיכום:**\n"
    r"- $a>1$: מוגדרת חיובית לחלוטין (ובפרט מוגדרת חיובית)." "\n"
    r"- $a=1$: מוגדרת חיובית אך לא לחלוטין (הערכים העצמיים $1,0,2$)." "\n"
    r"- $a<1$: אף אחת מהן (יש ערך עצמי שלילי, $a<0$ או $a^2-1<0$, ותמיד יש ערך עצמי חיובי $a^2+1>0$)."
)

S4B = (
    r"נשים לב ש-$3\equiv1\pmod2$, כלומר המשוואה השנייה היא $x\equiv1\pmod2$. המודולים $5,2,7$ זרים בזוגות." "\n"
    r"$a_1=2,\ a_2=1,\ a_3=4$ ; $\ m_1=5,\ m_2=2,\ m_3=7$ ; $\ M=5\cdot2\cdot7=70$" "\n"
    r"$$M_1=\frac{70}5=14,\qquad M_2=\frac{70}2=35,\qquad M_3=\frac{70}7=10$$" "\n"
    r"$$14x_1\equiv1\pmod5\ \Rightarrow\ 4x_1\equiv1\pmod5\ \Rightarrow\ x_1=4$$" "\n"
    r"$$35x_2\equiv1\pmod2\ \Rightarrow\ x_2\equiv1\pmod2\ \Rightarrow\ x_2=1$$" "\n"
    r"$$10x_3\equiv1\pmod7\ \Rightarrow\ 3x_3\equiv1\pmod7\ \Rightarrow\ x_3=5$$" "\n"
    r"$$x\equiv a_1M_1x_1+a_2M_2x_2+a_3M_3x_3=2\cdot14\cdot4+1\cdot35\cdot1+4\cdot10\cdot5=112+35+200=347\equiv67\pmod{70}$$" "\n"
    r"**תשובה:** $x\equiv67\pmod{70}$. בדיקה: $67=13\cdot5+2$, $67$ אי-זוגי ($67\equiv3\pmod2$), $67=9\cdot7+4$."
)

S5A = (
    "נחשב ערכים עצמיים:\n"
    r"$$|A-\lambda I|=\begin{vmatrix}5-\lambda&0&0\\0&4-\lambda&2\\0&2&1-\lambda\end{vmatrix}=(5-\lambda)\left[(4-\lambda)(1-\lambda)-4\right]=(5-\lambda)(\lambda^2-5\lambda)=-\lambda(\lambda-5)^2$$" "\n"
    r"הערכים העצמיים: $\lambda=5$ (ריבוי 2) ו-$\lambda=0$." "\n"
    r"**עבור $\lambda=5$:**" "\n"
    r"$$A-5I=\begin{pmatrix}0&0&0\\0&-1&2\\0&2&-4\end{pmatrix}\sim\begin{pmatrix}0&1&-2\\0&0&0\\0&0&0\end{pmatrix}\ \Rightarrow\ \begin{cases}x=s\\y=2t\\z=t\end{cases}\ \Rightarrow\ \vec v_1=\begin{pmatrix}1\\0\\0\end{pmatrix},\ \vec v_2=\begin{pmatrix}0\\2\\1\end{pmatrix}$$" "\n"
    r"$\vec v_1\perp\vec v_2$, לכן אין צורך בגרם-שמידט בתוך המרחב העצמי." "\n"
    r"**עבור $\lambda=0$:**" "\n"
    r"$$A-0I=\begin{pmatrix}5&0&0\\0&4&2\\0&2&1\end{pmatrix}\sim\begin{pmatrix}1&0&0\\0&2&1\\0&0&0\end{pmatrix}\ \Rightarrow\ \begin{cases}x=0\\z=-2y\end{cases}\ \Rightarrow\ \vec v_3=\begin{pmatrix}0\\1\\-2\end{pmatrix}$$" "\n"
    r"(וקטורים עצמיים של מטריצה סימטרית לערכים עצמיים שונים אורתוגונליים, ואכן $\vec v_3\perp\vec v_1,\vec v_2$.)" "\n"
    r"ננרמל: $\|\vec v_1\|=1$, $\|\vec v_2\|=\|\vec v_3\|=\sqrt5$. נרשום את הוקטורים המנורמלים כעמודות:" "\n"
    r"$$Q=\begin{pmatrix}1&0&0\\0&\frac2{\sqrt5}&\frac1{\sqrt5}\\0&\frac1{\sqrt5}&-\frac2{\sqrt5}\end{pmatrix},\qquad D=\begin{pmatrix}5&0&0\\0&5&0\\0&0&0\end{pmatrix},\qquad A=QDQ^T$$" "\n"
    r"($Q$ אורתוגונלית, $Q^{-1}=Q^T$, וסדר הערכים העצמיים ב-$D$ כסדר העמודות של $Q$.)"
)

S5B1 = (
    r"יהיו $x,y\in G$. גם $xy\in G$, ולכן גם הוא הופכי לעצמו: $xy=(xy)^{-1}$. לפי כלל ההופכי של מכפלה:" "\n"
    r"$$xy=(xy)^{-1}=y^{-1}x^{-1}=yx$$" "\n"
    r"(בשוויון האחרון: $y^{-1}=y$ ו-$x^{-1}=x$). לכן $G$ אבלית."
)

S5B2 = (
    r"לכל $g\in G$ מתקיים $g=g^{-1}$, ולכן $g^2=g\cdot g=g\cdot g^{-1}=e$." "\n"
    "לכן\n"
    r"$$x^3=x^2\cdot x=e\cdot x=x,\qquad y^5=y^2\cdot y^2\cdot y=e\cdot e\cdot y=y$$" "\n"
    r"מכאן, אם $x^3=y^5$ אז $x=y$."
)

questions = [
    Q(1, "א", "computation", "least_squares",
      r"סעיף א. נתונות 5 הנקודות במישור $(-4,-1),(-2,0),(2,4),(4,5),(5,6)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים. (12%)", 12,
      S1A),
    Q(1, "ב", "proof", "cauchy_schwarz",
      r"סעיף ב. הוכיחו כי $\left(\displaystyle\int_1^2\frac{f(x)}x\,dx\right)^2\le\frac12\int_1^2f^2(x)\,dx$ כאשר $f(x)\in C_{[1,2]}$. (13%)", 13,
      S1B),

    Q(2, "א", "computation", "groups", r"סעיף א.1. מהו האיבר הניטרלי של $G$ ? (3%)", 3, S2A1, contextId="c2"),
    Q(2, "ב", "computation", "groups", r"סעיף א.2. מצאו את האיבר ההופכי של $(2,3)$ ? (4%)", 4, S2A2, contextId="c2"),
    Q(2, "ג", "computation", "groups", r"סעיף א.3. מהו הסדר של $G$ ? (5%)", 5, S2A3, contextId="c2"),
    Q(2, "ד", "computation", "groups", r"סעיף א.4. מהו הסדר של $(2,3)$ ? (5%)", 5, S2A4, contextId="c2"),
    Q(2, "ה", "proof", "pos_def", r"סעיף ב.1. $-A-B^TB$ מוגדרת שלילית. (4%)", 4, S2B1, contextId="c2b"),
    Q(2, "ו", "proof", "pos_def", r"סעיף ב.2. $B^TAB$ מוגדרת חיובית. (4%)", 4, S2B2, contextId="c2b"),

    Q(3, "א", "computation", "svd", r"סעיף א. מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}$. (18%)", 18, S3A),
    Q(3, "ב", "proof", "inner_product",
      r"סעיף ב. יהי $V$ מרחב מכפלה פנימית ממשי. הוכיחו כי עבור כל $\vec v,\vec u\in V$ מתקיים $\langle\vec u,\vec v\rangle=\dfrac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$. (7%)", 7,
      S3B),

    Q(4, "א", "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}a^2&0&1\\0&a&0\\1&0&a^2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (17%)", 17,
      S4A),
    Q(4, "ב", "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod5\\x\equiv3\pmod2\\x\equiv4\pmod7\end{cases}$. (8%)", 8,
      S4B),

    Q(5, "א", "computation", "orthodiag",
      r"סעיף א. בצעו לכסון אורתוגונלי למטריצה $A=\begin{pmatrix}5&0&0\\0&4&2\\0&2&1\end{pmatrix}$. (15%)", 15, S5A),
    Q(5, "ב", "proof", "groups", r"סעיף ב.1. $G$ חבורה אבלית, כלומר לכל $x,y\in G$ מתקיים $x\cdot y=y\cdot x$. (5%)", 5, S5B1, contextId="c5b"),
    Q(5, "ג", "proof", "groups", r"סעיף ב.2. אם $x,y\in G$ ו-$x^3=y^5$ אז $x=y$. (5%)", 5, S5B2, contextId="c5b"),
]

# ---------------------------------------------------------------- rubric / pitfalls / steps (step-author, ai-draft)
# Every numeric value is recomputed in tools/verify/25A-C/steps_check.py (sympy / brute force).
# The solutions are solver-written (no key exists), so the steps follow the stored solver solutions.
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
        rubric=rub((r"בניית $A$ (עם עמודת אחדות) ו-$\vec b$", 3),
                   (r"המשוואות הנורמליות: $A^TA=\begin{pmatrix}65&5\\5&5\end{pmatrix}$ ו-$A^T\vec b=\begin{pmatrix}62\\14\end{pmatrix}$", 4),
                   (r"פתרון המערכת: $m=0.8,\ n=2$", 4),
                   (r"התשובה $y=0.8x+2$", 1)),
        pitfalls=["לשכוח את עמודת האחדות ולחפש רק ישר דרך הראשית.",
                  r"לחשב $AA^T$ במקום $A^TA$.",
                  r"לטעות בחישוב $\sum x_iy_i$ (שיש בו איבר שלילי ראשון $4$ ולא $-4$)."],
        steps=[num(r"מהו $\sum x_i^2$ עבור הנקודות?", 65, r"$16+4+4+16+25=65$."),
               num(r"מהו $\sum x_iy_i$?", 62, r"$4+0+8+20+30=62$ (הנקודה הראשונה נותנת $(-4)(-1)=4$)."),
               num(r"מהו השיפוע $m$?", 0.8, r"מחסרים את המשוואות $65m+5n=62$ ו-$5m+5n=14$: $60m=48$.", tol=0.001),
               num(r"מהו $n$?", 2, r"$n=\frac{14-5\cdot0.8}5=2$.")],
    ),
    (1, "ב"): dict(
        rubric=rub((r"בחירת $g(x)=\frac1x$ והמכפלה $\int_1^2fg$", 4),
                   ("ניסוח קושי-שוורץ", 3),
                   (r"חישוב $\|g\|^2=\frac12$", 4),
                   ("הצבה ומסקנה", 2)),
        pitfalls=[r"לחשב $\int\frac1{x^2}$ כלוגריתם במקום $-\frac1x$.",
                  "לשכוח שקושי-שוורץ נותן אי-שוויון על הריבוע של האינטגרל.",
                  r"לבחור $g\equiv1$, שמוביל לאי-שוויון אחר."],
        steps=[ch("איזו פונקציה $g$ מציבים בקושי-שוורץ?",
                  [r"$g(x)=\frac1x$", r"$g(x)=1$", r"$g(x)=x$"], 0,
                  r"עבור $g=1$ מתקבל $\left(\int f\right)^2\le\int f^2$ ועבור $g=x$ מתקבל $\left(\int xf\right)^2\le\frac73\int f^2$: שניהם אי-שוויונות אחרים. רק $g=\frac1x$ נותן את האינטגרל $\int\frac fx$ ואת הקבוע $\frac12$."),
               num(r"מהו $\|g\|^2=\int_1^2\frac1{x^2}\,dx$?", 0.5, r"$\left[-\frac1x\right]_1^2=-\frac12+1=\frac12$.", tol=0.0001),
               bug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.",
                   [r"נבחר $g(x)=\frac1x$ ונשתמש במכפלה $\langle f,g\rangle=\int_1^2f(x)g(x)\,dx$.",
                    r"לפי קושי-שוורץ $\langle f,g\rangle^2\le\|f\|^2\|g\|^2$.",
                    r"$\|g\|^2=\int_1^2\frac1{x^2}\,dx=\left[\ln x\right]_1^2=\ln2$.",
                    r"לכן $\left(\int_1^2\frac{f(x)}x\,dx\right)^2\le\frac12\int_1^2f^2(x)\,dx$."],
                   2, r"הפונקציה הקדומה של $\frac1{x^2}$ היא $-\frac1x$ ולא $\ln x$, ולכן הערך הוא $\frac12$.")],
    ),
    (2, "א"): dict(
        rubric=rub(("הניטרלי של $\\mathbb{Z}_5^*$ ושל $\\mathbb{Z}_7^*$ הוא $1$", 1),
                   (r"בדיקה: $(1,1)\cdot(a,b)=(a,b)$", 1),
                   (r"תשובה: $e=(1,1)$", 1)),
        pitfalls=[r"לכתוב $(0,0)$ מתוך הרגל מחבורות חיבור; הכפל כאן ו-$0\notin G$."],
        steps=[ch("מהו האיבר הניטרלי של $G$?",
                  [r"$(1,1)$", r"$(0,0)$", r"$(1,0)$"], 0,
                  r"$(0,0)$ ו-$(1,0)$ אינם ב-$G$ (כי $0$ אינו ב-$\mathbb{Z}_5^*$ או ב-$\mathbb{Z}_7^*$), וגם מכפלה בהם מאפסת רכיב."),
               num(r"חשבו את הרכיב השני של $(3,4)\cdot(1,1)$.", 4, r"$4\cdot1=4$.")],
    ),
    (2, "ב"): dict(
        rubric=rub((r"המשוואות $2c\equiv1\pmod5$ ו-$3d\equiv1\pmod7$", 2),
                   (r"$c=3$", 1),
                   (r"$d=5$", 1)),
        pitfalls=["להפוך את הרכיבים כחיבור (למשל $-2$ ו-$-3$) במקום הופכי כפלי.",
                  r"לא לעבוד בכל רכיב במודולו שלו (5 ו-7)."],
        steps=[num(r"מהו $c\in\mathbb{Z}_5^*$ המקיים $2c\equiv1\pmod5$?", 3, r"$2\cdot3=6\equiv1$."),
               num(r"מהו $d\in\mathbb{Z}_7^*$ המקיים $3d\equiv1\pmod7$?", 5, r"$3\cdot5=15\equiv1$.")],
    ),
    (2, "ג"): dict(
        rubric=rub((r"$|\mathbb{Z}_5^*|=4$", 2), (r"$|\mathbb{Z}_7^*|=6$", 2), (r"$|G|=4\cdot6=24$", 1)),
        pitfalls=[r"לספור גם את $0$ ולקבל $5\cdot7=35$.",
                  "לחבר את הגדלים במקום להכפיל."],
        steps=[num(r"כמה איברים יש ב-$\mathbb{Z}_5^*$?", 4, r"$\{1,2,3,4\}$."),
               num(r"כמה איברים יש ב-$\mathbb{Z}_7^*$?", 6, r"$\{1,\dots,6\}$."),
               num(r"מהו $|G|$?", 24, r"$4\cdot6=24$.")],
    ),
    (2, "ד"): dict(
        rubric=rub((r"סדרי הרכיבים: $o(2)=4$ ו-$o(3)=6$", 3),
                   (r"הסדר הוא הכפולה המשותפת המינימלית: $\mathrm{lcm}(4,6)=12$", 2)),
        pitfalls=[r"לכתוב $4\cdot6=24$ במקום $\mathrm{lcm}$.",
                  r"לשכוח שחזקות של $2$ מודולו 5 חוזרות ל-$1$ רק אחרי $4$ צעדים."],
        steps=[num(r"מהו הסדר של $2$ ב-$\mathbb{Z}_5^*$?", 4, r"$2,4,3,1$."),
               num(r"מהו הסדר של $3$ ב-$\mathbb{Z}_7^*$?", 6, r"$3,2,6,4,5,1$."),
               num(r"מהו הסדר של $(2,3)$?", 12, r"$\mathrm{lcm}(4,6)=12$. הסדר אינו $24$, כי $(2,3)^{12}=(1,1)$ כבר.")],
    ),
    (2, "ה"): dict(
        rubric=rub(("סימטריה של $-A-B^TB$", 1),
                   (r"הצגה $\vec v^T(-A-B^TB)\vec v=-\vec v^TA\vec v-\|B\vec v\|^2$", 2),
                   ("שני המחוברים אי-שליליים, ולכן הסכום קטן או שווה לאפס", 1)),
        pitfalls=[r"לשכוח את הסימן המינוס לפני $B^TB$.",
                  r"לשכוח ש-$\vec v^TB^TB\vec v=\|B\vec v\|^2\ge0$."],
        steps=[num(r"עבור $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ ו-$\vec v=\begin{pmatrix}1\\-1\end{pmatrix}$ חשבו את $\vec v^TB^TB\vec v$.", 1,
                   r"$B\vec v=\begin{pmatrix}0\\-1\end{pmatrix}$ ולכן הערך הוא $\|B\vec v\|^2=1$."),
               bug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.",
                   [r"$\left(-A-B^TB\right)^T=-A^T-B^TB=-A-B^TB$, כי $A$ סימטרית.",
                    r"$\vec v^T\left(-A-B^TB\right)\vec v=-\vec v^TA\vec v+(B\vec v)^T(B\vec v)$.",
                    r"$\vec v^TA\vec v\ge0$ כי $A$ מוגדרת חיובית, וגם $(B\vec v)^T(B\vec v)=\|B\vec v\|^2\ge0$.",
                    r"לכן $\vec v^T\left(-A-B^TB\right)\vec v\le0$ והמטריצה מוגדרת שלילית."],
                   1, r"הסימן לפני $(B\vec v)^T(B\vec v)$ חייב להיות מינוס, כי מפזרים את המינוס שמול $B^TB$.")],
    ),
    (2, "ו"): dict(
        rubric=rub((r"סימטריה: $\left(B^TAB\right)^T=B^TAB$", 1),
                   (r"הצבה $\vec w=B\vec v$", 2),
                   (r"$\vec w^TA\vec w\ge0$ ולכן $B^TAB$ מוגדרת חיובית", 1)),
        pitfalls=[r"לכתוב $\left(B^TAB\right)^T=B^TA^TB^T$ (בשחלוף של מכפלה, $B$ הופך ל-$B^T$ ולהפך).",
                  r"לדרוש חיוביות לחלוטין: עבור $B$ סינגולרית הטענה לא נכונה במובן החזק."],
        steps=[ch(r"למה שווה $\vec v^T\left(B^TAB\right)\vec v$?",
                  [r"$(B\vec v)^TA(B\vec v)$", r"$\vec v^TA\vec v$", r"$(B^T\vec v)^TA(B^T\vec v)$"], 0,
                  r"$\vec v^TB^T=(B\vec v)^T$. עבור $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $A=\mathrm{diag}(2,3)$ ו-$\vec v=(1,0)^T$ הערך הוא $2$, כמו בביטוי עם $B\vec v$, ובביטוי עם $B^T\vec v=(1,1)^T$ מתקבל $5$."),
               num(r"עבור $A=\mathrm{diag}(2,3)$, $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ ו-$\vec v=\begin{pmatrix}1\\0\end{pmatrix}$ חשבו את $\vec w^TA\vec w$ כש-$\vec w=B\vec v$.", 2,
                   r"$\vec w=(1,0)^T$ ולכן $\vec w^TA\vec w=2$."),
               bug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.",
                   [r"$\left(B^TAB\right)^T=B^TA^TB^T=B^TAB$, כי $A$ סימטרית.",
                    r"לכל $\vec v$ נסמן $\vec w=B\vec v$.",
                    r"$\vec v^T\left(B^TAB\right)\vec v=(B\vec v)^TA(B\vec v)=\vec w^TA\vec w$.",
                    r"$\vec w^TA\vec w\ge0$ כי $A$ מוגדרת חיובית, ולכן $B^TAB$ מוגדרת חיובית."],
                   0, r"בשחלוף $(XYZ)^T=Z^TY^TX^T$, ולכן $\left(B^TAB\right)^T=B^TA^T\left(B^T\right)^T=B^TA^TB$ ולא $B^TA^TB^T$.")],
    ),
    (3, "א"): dict(
        rubric=rub((r"חישוב $AA^T=\begin{pmatrix}5&4\\4&5\end{pmatrix}$", 3),
                   (r"הערכים העצמיים $9,1$ והערכים הסינגולריים $3,1$", 3),
                   (r"העמודות של $U$: וקטורים עצמיים מנורמלים של $AA^T$", 4),
                   (r"העמודות $\vec v_1,\vec v_2$ של $V$ לפי $\frac1{\sigma_i}A^T\vec u_i$", 4),
                   (r"השלמה $\vec v_3=(0,1,0)^T$", 2),
                   (r"כתיבת $A=U\Sigma V^T$", 2)),
        pitfalls=[r"לרשום את $9,1$ כערכים הסינגולריים במקום $3,1$.",
                  r"לבחור את הסימנים של $\vec u_i$ ושל $\vec v_i$ בלי להקפיד על $A\vec v_i=\sigma_i\vec u_i$.",
                  r"לשכוח שהעמודה השלישית של $V$ חייבת להיות אורתוגונלית לשתיים הראשונות."],
        steps=[num(r"מהו הרכיב בשורה 1, עמודה 2 של $AA^T$?", 4, r"$1\cdot2+0\cdot0+2\cdot1=4$."),
               num(r"מהו $\sigma_1$ (הגדול)?", 3, r"$\lambda=9$ ולכן $\sigma_1=3$."),
               num(r"מהו $\sigma_2$?", 1, r"$\lambda=1$ ולכן $\sigma_2=1$."),
               num(r"אם $\vec u_2=\frac1{\sqrt2}(1,-1)^T$ אז $\vec v_2=\frac1{\sigma_2}A^T\vec u_2$. מהו הרכיב הראשון שלו (עיגול לארבע ספרות אחרי הנקודה)?", -0.7071,
                   r"$A^T\vec u_2=\frac1{\sqrt2}(-1,0,1)^T$, והרכיב הראשון הוא $-\frac1{\sqrt2}\approx-0.7071$.", tol=0.0001),
               ch(r"איזה וקטור (עד כדי סימן) משלים את $\vec v_1=\frac1{\sqrt2}(1,0,1)^T$ ו-$\vec v_2=\frac1{\sqrt2}(-1,0,1)^T$ לבסיס אורתונורמלי?",
                  [r"$(0,1,0)^T$", r"$(0,0,1)^T$", r"$\frac1{\sqrt2}(1,0,1)^T$"], 0,
                  r"$(0,0,1)^T$ אינו ניצב ל-$\vec v_2$ (המכפלה $\frac1{\sqrt2}$), והווקטור $\frac1{\sqrt2}(1,0,1)^T$ הוא $\vec v_1$ עצמו.")],
    ),
    (3, "ב"): dict(
        rubric=rub((r"פיתוח $\|\vec u\pm\vec v\|^2$ בעזרת ליניאריות וסימטריה", 4),
                   ("חיסור שני השוויונות", 2),
                   (r"חילוק ב-$4$ והמסקנה", 1)),
        pitfalls=[r"לשכוח את התכונה $\langle\vec v,\vec u\rangle=\langle\vec u,\vec v\rangle$ ולהישאר עם שני איברים נפרדים.",
                  r"לחבר במקום לחסר: החיבור נותן $2\|\vec u\|^2+2\|\vec v\|^2$."],
        steps=[num(r"עבור $\vec u=(1,2)$ ו-$\vec v=(3,1)$ במכפלה הסטנדרטית חשבו את $\frac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$.", 5,
                   r"$\|(4,3)\|^2=25$, $\|(-2,1)\|^2=5$, ו-$\frac{25-5}4=5=\langle\vec u,\vec v\rangle$."),
               ch(r"איזו תכונה של המכפלה הפנימית הממשית מאחדת את $\langle\vec u,\vec v\rangle$ ו-$\langle\vec v,\vec u\rangle$ בפיתוח?",
                  ["סימטריה", "אי-שוויון המשולש", "חיוביות"], 0,
                  r"רק הסימטריה $\langle\vec v,\vec u\rangle=\langle\vec u,\vec v\rangle$ מאפשרת לכתוב $2\langle\vec u,\vec v\rangle$. חיוביות ואי-שוויון המשולש אינם נותנים שוויון בין שני האיברים."),
               order("סדרו את שלבי ההוכחה.",
                     [r"$\|\vec u\pm\vec v\|^2=\|\vec u\|^2\pm2\langle\vec u,\vec v\rangle+\|\vec v\|^2$ (ליניאריות וסימטריה).",
                      r"מחסרים: $\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2=4\langle\vec u,\vec v\rangle$.",
                      r"מחלקים ב-$4$: $\langle\vec u,\vec v\rangle=\frac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$."],
                     "פיתוח, חיסור, חילוק.")],
    ),
    (4, "א"): dict(
        rubric=rub((r"חישוב הערכים העצמיים $a,\ a^2-1,\ a^2+1$", 6),
                   (r"מוגדרת חיובית: $a\ge1$", 3),
                   (r"מוגדרת חיובית לחלוטין: $a>1$", 3),
                   ("מוגדרת שלילית ושלילית לחלוטין: אף ערך", 3),
                   (r"סיכום: $a<1$ אף אחת מהן", 2)),
        pitfalls=[r"להתבלבל בין $a\ge1$ ל-$a>1$ בקצה $a=1$.",
                  r"לשכוח את התנאי $a\ge0$ על הערך העצמי $a$ ולפתור רק $a^2\ge1$ (שמאפשר $a\le-1$).",
                  r"לשכוח שהערך $a^2+1$ תמיד חיובי ולכן המטריצה אף פעם לא שלילית."],
        steps=[num(r"המטריצה היא $\begin{pmatrix}a^2&0&1\\0&a&0\\1&0&a^2\end{pmatrix}$. מהי העקבה שלה עבור $a=2$ (שווה לסכום הערכים העצמיים)?", 10, r"$4+2+4=10$."),
               ch("מהם הערכים העצמיים?",
                  [r"$a,\ a^2-1,\ a^2+1$", r"$a,\ a^2-1,\ a^2$", r"$a,\ a^2-1,\ a^2+2$", r"$2a,\ a^2-1,\ a^2+1$"], 0,
                  r"הסכום חייב להיות העקבה $2a^2+a$. הקבוצה הנכונה נותנת בדיוק זאת, ואילו הקבוצה עם $a^2$ נותנת $2a^2+a-1$, הקבוצה עם $a^2+2$ נותנת $2a^2+a+1$, והקבוצה עם $2a$ נותנת $2a^2+2a$."),
               ch("עבור אילו $a$ המטריצה מוגדרת חיובית (לא בהכרח לחלוטין)?",
                  [r"$a\ge1$", r"$a>1$", r"$a\ge0$"], 0,
                  r"נדרש $a\ge0$ וגם $a^2\ge1$. עבור $a=1$ הערכים הם $1,0,2$ (חיובית), ועבור $a=\frac12$ יש ערך עצמי $-\frac34$."),
               ch("עבור אילו $a$ המטריצה מוגדרת חיובית לחלוטין?",
                  [r"$a>1$", r"$a\ge1$", r"$a>0$"], 0,
                  r"עבור $a=1$ יש ערך עצמי $0$, ועבור $a=\frac12$ יש ערך עצמי שלילי."),
               ch("עבור אילו $a$ המטריצה מוגדרת שלילית?",
                  [r"עבור אף $a$", r"$a<0$", r"$|a|<1$"], 0,
                  r"הערך העצמי $a^2+1$ חיובי תמיד. עבור $a=-2$ הערכים הם $-2,3,5$, ועבור $a=\frac12$ הערכים הם $\frac12,-\frac34,\frac54$: בשני המקרים יש ערך עצמי חיובי.")],
    ),
    (4, "ב"): dict(
        rubric=rub((r"זרות המודולים ו-$M=70$", 1),
                   (r"$M_1,M_2,M_3=14,35,10$", 2),
                   (r"ההופכיים $x_1,x_2,x_3=4,1,5$", 3),
                   (r"הסכום $347$ והרדוקציה $67$", 2)),
        pitfalls=[r"לטעות בקריאת המשוואה $x\equiv3\pmod2$: היא שקולה ל-$x\equiv1\pmod2$.",
                  r"לשכוח לרדד את $M_i$ מודולו $m_i$ לפני מציאת ההופכי."],
        steps=[num(r"מהו $M=5\cdot2\cdot7$?", 70, r"$5\cdot2\cdot7=70$."),
               num(r"מהו $x_1$ (בין $0$ ל-$4$) המקיים $14x_1\equiv1\pmod5$?", 4, r"$14\equiv4$ ו-$4\cdot4=16\equiv1$."),
               num(r"מהו $x_3$ (בין $0$ ל-$6$) המקיים $10x_3\equiv1\pmod7$?", 5, r"$10\equiv3$ ו-$3\cdot5=15\equiv1$."),
               num(r"מהו הפתרון $x$ בין $0$ ל-$69$?", 67, r"$347=4\cdot70+67$.")],
    ),
    (5, "א"): dict(
        rubric=rub((r"הערכים העצמיים $5,5,0$", 4),
                   (r"בסיס למרחב העצמי של $5$: $(1,0,0)^T,\ (0,2,1)^T$ והבחנה שהם ניצבים", 4),
                   (r"וקטור עצמי של $0$: $(0,1,-2)^T$", 3),
                   (r"נרמול והרכבת $Q$ ו-$D$ (באותו סדר)", 4)),
        pitfalls=["לסדר את העמודות של $Q$ בסדר שונה מהערכים על אלכסון $D$.",
                  r"לשכוח לנרמל את $\vec v_2,\vec v_3$ (הנורמה היא $\sqrt5$).",
                  r"להפעיל גרם-שמידט שלא לצורך על וקטורים שכבר ניצבים."],
        steps=[num(r"מהו הריבוי של הערך העצמי $5$?", 2, r"$|A-\lambda I|=-\lambda(\lambda-5)^2$."),
               num(r"חשבו את המכפלה הסקלרית $(0,1,-2)\cdot(0,2,1)$.", 0, r"$2-2=0$, כלומר הווקטורים של ערכים עצמיים שונים ניצבים."),
               num(r"מהי הנורמה $\|(0,2,1)\|$ (עיגול לשלוש ספרות אחרי הנקודה)?", 2.236, r"$\sqrt5\approx2.236$.", tol=0.001),
               ch(r"מדוע אין צורך בגרם-שמידט בין $\vec v_1=(1,0,0)^T$ ל-$\vec v_2=(0,2,1)^T$?",
                  [r"כי הם כבר ניצבים: המכפלה הסקלרית שלהם $0$", "כי יש להם אותו אורך", "כי $A$ הפיכה"], 0,
                  r"אורכיהם $1$ ו-$\sqrt5$ (שונים), ו-$A$ אינה הפיכה (הערך $0$). מה שחשוב הוא רק שהמכפלה הסקלרית היא $0$.")],
    ),
    (5, "ב"): dict(
        rubric=rub((r"$xy\in G$ ולכן $xy=(xy)^{-1}$", 2),
                   (r"$(xy)^{-1}=y^{-1}x^{-1}$", 2),
                   (r"$y^{-1}x^{-1}=yx$ ולכן $xy=yx$", 1)),
        pitfalls=[r"להשתמש ב-$(xy)^{-1}=x^{-1}y^{-1}$ (נכון רק בחבורה אבלית).",
                  "להניח שהחבורה אבלית כדי להוכיח שהיא אבלית."],
        steps=[ch(r"מדוע מותר לכתוב $xy=(xy)^{-1}$?",
                  [r"כי $xy\in G$ והנתון חל על כל איבר של $G$", "כי $G$ אבלית", r"כי $x=y$"], 0,
                  r"הנימוק על אבליות הוא מעגלי (זו מה שמוכיחים), ו-$x=y$ אינו נתון."),
               order("סדרו את שלבי ההוכחה.",
                     [r"$xy\in G$, ולכן $xy=(xy)^{-1}$.",
                      r"$(xy)^{-1}=y^{-1}x^{-1}$.",
                      r"$y^{-1}=y$ ו-$x^{-1}=x$, ולכן $y^{-1}x^{-1}=yx$.",
                      r"לכן $xy=yx$ ו-$G$ אבלית."],
                     "כל שורה נשענת על הקודמת.")],
    ),
    (5, "ג"): dict(
        rubric=rub((r"$g=g^{-1}$ ולכן $g^2=e$ לכל $g$", 2),
                   (r"$x^3=x$ ו-$y^5=y$", 2),
                   (r"$x=x^3=y^5=y$", 1)),
        pitfalls=[r"לצמצם חזקות כמו בחשבון רגיל ($x^3=y^5\Rightarrow x=y$) בלי להשתמש ב-$g^2=e$.",
                  r"לטעות ב-$y^5=y^2y^2y$ ולקבל $y^2$."],
        steps=[ch(r"מה נובע מהנתון $g=g^{-1}$ לכל $g\in G$?",
                  [r"$g^2=e$", r"$g^2=g$", r"$g=e$"], 0,
                  r"$g\cdot g=g\cdot g^{-1}=e$. ב-$\mathbb{Z}_2$ למשל $g=1$ מקיים $g=g^{-1}$ אבל $g^2=0\ne g$ ו-$g\ne0$."),
               order("סדרו את שלבי ההוכחה.",
                     [r"$g=g^{-1}$ ולכן $g^2=e$ לכל $g\in G$.",
                      r"$x^3=x^2x=x$ ו-$y^5=y^2y^2y=y$.",
                      r"אם $x^3=y^5$ אז $x=x^3=y^5=y$."],
                     "קודם $g^2=e$, אחר כך מצמצמים את החזקות, ולבסוף משווים.")],
    ),
}

for _q in questions:
    _e = EXTRA.pop((_q["num"], _q.get("part")))
    _q.update(_e)
    _q["rubricSource"] = "ai-verified"
    _q["stepsSource"] = "ai-verified"
    assert sum(r["points"] for r in _q["rubric"]) == _q["points"], (_q["num"], _q.get("part"))
assert not EXTRA, EXTRA

exam = {
    "examCode": "25A-C",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ה מועד ג'",
    "year": 2025,
    "examDate": "",
    "sourceFile": "algebra-2-25A-C-exam",
    "solutionFile": "none",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
