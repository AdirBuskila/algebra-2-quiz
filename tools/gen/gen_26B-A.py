# -*- coding: utf-8 -*-
"""Generator for tools/raw/26B-A.json -- algebra-2 (20079), semester B 2026, moed A (17.06.2026).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_26B-A.py

Source: exam 2 pp. (text PDF, read from the rendered pages). There is NO official solution: every item was solved
from the exam text by the solver (solutionSource "solved", official false, confidence high), pending the refuter.
The sheet says "4 of 5", 25% each; 5 questions, 15 items (the printed ע"י is written with a gershayim). Q5 is printed with parts "ג" and "ד" (letters kept as printed).
Part letters: numbered sub-parts get letters in order (Q1: a.1, a.2, b -> a, b, c; Q2: 1..5 -> a..e; Q4: a, b, c).
The unidentified 17-page scan "2026-B.PDF" is a handwritten student solution of THIS sitting (not a distinct sitting)
with a student grade-report page; it is personal data, not an official source, and was NOT used, read or quoted
by the solver (no partial evidence was consulted).

Solver notes:
- Q1c: "מוגדרת חיובית לחלוטין" is taken in the course sense (symmetric with x^T A x > 0 for x != 0). Proof via the
  quadratic form; the eigenvalue argument (lambda+lambda^2, lambda+1/lambda) is given as a second line.
- Q2e: many answers exist; the solution gives one (A = [[1,1],[0,1]]) and the reason H misses the conjugate.
- Q3a: course terms: "מוגדרת חיובית" = semi-definite, "לחלוטין" = definite.
Checks: tools/verify/26B-A/solve_26B-A.py (sympy + brute force), ALL OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26B-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "solved", "official": False, "confidence": "high"}
    q.update(kw)
    return q


CTX = {
    "c1": {"kind": "text", "title": "שאלה 1 סעיף א",
           "text": r"במרחב וקטורי $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע״י $\langle A,B\rangle=tr\left(B^TA\right)$."},
    "c2": {"kind": "text", "title": "שאלה 2",
           "text": r"נסתכל בחבורה $G=\left\{\begin{pmatrix}a&b\\0&c\end{pmatrix}\in M_2(\mathbb{Z}_5)\ \middle|\ a\cdot c\neq0\pmod5\right\}$ ביחס לכפל מטריצות (חבורת המטריצות המשולשות העליונות ההפיכות מסדר $2\times2$ עם רכיבים מ-$\mathbb{Z}_5$). תהי $H=\{J^n\mid n\in\mathbb{Z}\}$ תת-חבורה ציקלית של $G$ כאשר $J=\begin{pmatrix}1&1\\0&2\end{pmatrix}$."},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"נסמן $\vec e_1=A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $\vec e_2=B=\begin{pmatrix}1&1\\0&-1\end{pmatrix}$. מתקיים" "\n"
    r"$$\langle B,A\rangle=tr\left(A^TB\right)=1\cdot1+0\cdot1+0\cdot0+(-1)(-1)=2,\qquad\|A\|^2=1+0+0+1=2$$" "\n"
    r"$$\vec u_1=\vec e_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$" "\n"
    r"$$\vec u_2=\vec e_2-\frac{\langle\vec e_2,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1=\begin{pmatrix}1&1\\0&-1\end{pmatrix}-\frac22\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$" "\n"
    r"בדיקה: $\langle\vec u_2,\vec u_1\rangle=0$. לכן $\left\{\begin{pmatrix}1&0\\0&-1\end{pmatrix},\begin{pmatrix}0&1\\0&0\end{pmatrix}\right\}$ בסיס אורתוגונלי של $\mathrm{Sp}\{A,B\}$." "\n"
    r"מאחר ש-$\|\vec u_1\|=\sqrt2$ ו-$\|\vec u_2\|=1$, הבסיס האורתונורמלי הוא" "\n"
    r"$$\left\{\frac1{\sqrt2}\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ \begin{pmatrix}0&1\\0&0\end{pmatrix}\right\}$$"
)

S1B = (
    r"נשתמש בבסיס האורתוגונלי מסעיף 1: $\vec u_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $\vec u_2=\begin{pmatrix}0&1\\0&0\end{pmatrix}$." "\n"
    r"$$\langle C,\vec u_1\rangle=2\cdot1+3\cdot0+1\cdot0+0\cdot(-1)=2,\qquad\langle C,\vec u_2\rangle=3$$" "\n"
    r"$$\mathrm{proj}_U(C)=\frac{\langle C,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1+\frac{\langle C,\vec u_2\rangle}{\|\vec u_2\|^2}\vec u_2=\frac22\begin{pmatrix}1&0\\0&-1\end{pmatrix}+\frac31\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}1&3\\0&-1\end{pmatrix}$$" "\n"
    r"בדיקה: $C-\mathrm{proj}_U(C)=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ אורתוגונלית ל-$A$ ול-$B$ (המכפלות הפנימיות הן $1-1=0$ ו-$1+0-1=0$)."
)

S1C = (
    r"$A$ מוגדרת חיובית לחלוטין, כלומר $A$ סימטרית ו-$x^TAx>0$ לכל $x\neq0$. בפרט $A$ הפיכה (אם $Ax=0$ עם $x\neq0$ אז $x^TAx=0$)." "\n"
    r"**סימטריות:** $\left(A^2\right)^T=\left(A^T\right)^2=A^2$ ו-$\left(A^{-1}\right)^T=\left(A^T\right)^{-1}=A^{-1}$, ולכן $A+A^2$ ו-$A+A^{-1}$ סימטריות." "\n"
    r"**$A+A^2$:** לכל $x\neq0$" "\n"
    r"$$x^T\left(A+A^2\right)x=x^TAx+x^TA^TAx=\underbrace{x^TAx}_{>0}+\underbrace{\|Ax\|^2}_{\ge0}>0$$" "\n"
    r"**$A+A^{-1}$:** לכל $x\neq0$ נסמן $y=A^{-1}x$; אז $y\neq0$ (כי $x=Ay$) ו-" "\n"
    r"$$x^TA^{-1}x=(Ay)^TA^{-1}(Ay)=y^TA^TA^{-1}Ay=y^TAy>0$$" "\n"
    r"$$\Rightarrow\ x^T\left(A+A^{-1}\right)x=x^TAx+x^TA^{-1}x>0$$" "\n"
    r"לכן שתי המטריצות מוגדרות חיובית לחלוטין." "\n"
    r"**דרך נוספת:** $A=PDP^T$ עם $P$ אורתוגונלית ו-$D=\mathrm{diag}(\lambda_i)$, $\lambda_i>0$. אז $A+A^2=P\left(D+D^2\right)P^T$ ו-$A+A^{-1}=P\left(D+D^{-1}\right)P^T$, והערכים העצמיים $\lambda_i+\lambda_i^2>0$ ו-$\lambda_i+\frac1{\lambda_i}>0$."
)

S2A = (
    r"איבר של $G$ נקבע ע״י $a,c\in\mathbb{Z}_5\setminus\{0\}$ (4 אפשרויות לכל אחד, כי $a\cdot c\neq0$ במודולו 5 ראשוני אם״ם $a\neq0$ וגם $c\neq0$) ו-$b\in\mathbb{Z}_5$ (5 אפשרויות)." "\n"
    r"$$|G|=4\cdot5\cdot4=80$$"
)

S2B = (
    r"לכל $b,c$ מתקיים $\begin{pmatrix}1&b\\0&c\end{pmatrix}\begin{pmatrix}1&1\\0&2\end{pmatrix}=\begin{pmatrix}1&1+2b\\0&2c\end{pmatrix}$. נחשב חזקות (מודולו 5):" "\n"
    r"$$J=\begin{pmatrix}1&1\\0&2\end{pmatrix},\quad J^2=\begin{pmatrix}1&3\\0&4\end{pmatrix},\quad J^3=\begin{pmatrix}1&7\\0&8\end{pmatrix}\equiv\begin{pmatrix}1&2\\0&3\end{pmatrix},\quad J^4=\begin{pmatrix}1&5\\0&6\end{pmatrix}\equiv\begin{pmatrix}1&0\\0&1\end{pmatrix}=I$$" "\n"
    r"מאחר ש-$J^4=I$, כל חזקה $J^n$ (גם עבור $n$ שלילי) שווה ל-$J^{n\bmod 4}$. לכן" "\n"
    r"$$H=\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\ \begin{pmatrix}1&1\\0&2\end{pmatrix},\ \begin{pmatrix}1&3\\0&4\end{pmatrix},\ \begin{pmatrix}1&2\\0&3\end{pmatrix}\right\}$$"
)

S2C = (
    r"מסעיף 2, $J^4=I$ ולכן $J^{-1}=J^3$:" "\n"
    r"$$J^{-1}=\begin{pmatrix}1&2\\0&3\end{pmatrix}$$" "\n"
    r"בדיקה: $\begin{pmatrix}1&1\\0&2\end{pmatrix}\begin{pmatrix}1&2\\0&3\end{pmatrix}=\begin{pmatrix}1&5\\0&6\end{pmatrix}\equiv\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod5$."
)

S2D = (
    r"$H$ היא החבורה הציקלית הנוצרת ע״י $J$, ולכן $|H|=o(J)$. מסעיף 2: $J,J^2,J^3\neq I$ ו-$J^4=I$, לכן $o(J)=4$ ו-" "\n"
    r"$$|H|=4$$"
)

S2E = (
    r"נשים לב שכל ארבעת האיברים של $H$ הם מהצורה $\begin{pmatrix}1&c-1\\0&c\end{pmatrix}$; בפרט האיבר היחיד ב-$H$ שבפינה הימנית התחתונה שלו $2$ הוא $J$ עצמו." "\n"
    r"ניקח $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}\in G$. אז $A^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}=\begin{pmatrix}1&4\\0&1\end{pmatrix}$ ו-" "\n"
    r"$$AJ=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&2\end{pmatrix}=\begin{pmatrix}1&3\\0&2\end{pmatrix},\qquad AJA^{-1}=\begin{pmatrix}1&3\\0&2\end{pmatrix}\begin{pmatrix}1&4\\0&1\end{pmatrix}=\begin{pmatrix}1&7\\0&2\end{pmatrix}\equiv\begin{pmatrix}1&2\\0&2\end{pmatrix}$$" "\n"
    r"הפינה התחתונה היא $2$ אבל $AJA^{-1}\neq J$, ולכן $AJA^{-1}\notin H$. (יש תשובות נוספות, למשל $A=\begin{pmatrix}2&0\\0&1\end{pmatrix}$ נותנת את אותה מטריצה.)"
)

S3A = (
    r"המטריצה סימטרית. נחשב את הערכים העצמיים (פיתוח לפי השורה האמצעית):" "\n"
    r"$$\begin{vmatrix}1-\lambda&0&2a\\0&4-a^2-\lambda&0\\2a&0&1-\lambda\end{vmatrix}=\left(4-a^2-\lambda\right)\left((1-\lambda)^2-4a^2\right)=\left(4-a^2-\lambda\right)(1-2a-\lambda)(1+2a-\lambda)$$" "\n"
    r"לכן הערכים העצמיים הם: $\lambda_1=4-a^2,\ \lambda_2=1+2a,\ \lambda_3=1-2a$." "\n"
    r"$\lambda_1\ge0\iff|a|\le2$, $\lambda_2\ge0\iff a\ge-\frac12$, $\lambda_3\ge0\iff a\le\frac12$ (ובאי-שוויון חזק בהתאמה)." "\n"
    "**סיכום:**\n"
    r"המטריצה **מוגדרת חיובית לחלוטין** כאשר כל הערכים העצמיים חיוביים: $-\frac12<a<\frac12$ (ואז גם $|a|<2$)." "\n"
    r"המטריצה **מוגדרת חיובית** כאשר כל הערכים העצמיים אי-שליליים: $-\frac12\le a\le\frac12$ (עבור $a=\pm\frac12$ אחד הערכים העצמיים הוא $0$)." "\n"
    r"**מוגדרת שלילית** דורשת $1+2a\le0$ וגם $1-2a\le0$, כלומר $a\le-\frac12$ וגם $a\ge\frac12$, וזה בלתי אפשרי. לכן לא קיים $a$ עבורו המטריצה מוגדרת שלילית, ובפרט אין $a$ עבורו היא **מוגדרת שלילית לחלוטין**." "\n"
    r"המטריצה **אינה אף אחת מהן** כאשר $|a|>\frac12$ (אז $1+2a$ ו-$1-2a$ בעלי סימנים מנוגדים)."
)

S3B = (
    r"$y=mx+n$" "\n"
    r"$$\begin{cases}0m+n=2\\1m+n=2\\2m+n=4\\3m+n=8\\4m+n=9\end{cases}\ \Rightarrow\ \begin{pmatrix}0&1\\1&1\\2&1\\3&1\\4&1\end{pmatrix}\cdot\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}2\\2\\4\\8\\9\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\begin{pmatrix}0&1&2&3&4\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}0&1\\1&1\\2&1\\3&1\\4&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}0&1&2&3&4\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}2\\2\\4\\8\\9\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\begin{pmatrix}30&10\\10&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}70\\25\end{pmatrix}\ \Rightarrow\ m=2\ ,\ n=1\ \Rightarrow\ y=2x+1$$"
)

S4A = (
    r"יהיו $x,y\in G$. לפי הנתון $(xy)^2=x^2y^2$, כלומר" "\n"
    r"$$xyxy=xxyy$$" "\n"
    r"נכפול משמאל ב-$x^{-1}$ ומימין ב-$y^{-1}$ (צמצום בחבורה):" "\n"
    r"$$x^{-1}(xyxy)y^{-1}=x^{-1}(xxyy)y^{-1}\ \Rightarrow\ yx=xy$$" "\n"
    r"לכן $G$ אבלית."
)

S4B = (
    r"נשתמש פעמיים בנתון $xyx^{-1}=y^2$:" "\n"
    r"$$x^2yx^{-2}=x\left(xyx^{-1}\right)x^{-1}=xy^2x^{-1}=xy\left(x^{-1}x\right)yx^{-1}=\left(xyx^{-1}\right)\left(xyx^{-1}\right)=y^2\cdot y^2=y^4$$"
)

S4C = (
    r"לכל $k\ge1$ מתקיים $2k-1>0$ ו-$\ln k\ge0$, ולכן השורשים מוגדרים. נעזר באי שוויון קושי-שוורץ ב-$\mathbb{R}^n$ עם המכפלה הפנימית הסטנדרטית, עבור" "\n"
    r"$$\vec u=\left(\sqrt1,\sqrt3,\dots,\sqrt{2n-1}\right),\qquad\vec v=\left(\sqrt{\ln1},\sqrt{\ln2},\dots,\sqrt{\ln n}\right)$$" "\n"
    r"$$\langle\vec u,\vec v\rangle=\sum_{k=1}^n\sqrt{2k-1}\sqrt{\ln k}=\sum_{k=1}^n\sqrt{(2k-1)\ln k}$$" "\n"
    r"$$\|\vec u\|^2=\sum_{k=1}^n(2k-1)=2\cdot\frac{n(n+1)}2-n=n^2$$" "\n"
    r"$$\|\vec v\|^2=\sum_{k=1}^n\ln k=\ln(1\cdot2\cdots n)=\ln(n!)$$" "\n"
    r"לפי קושי-שוורץ $\langle\vec u,\vec v\rangle^2\le\|\vec u\|^2\cdot\|\vec v\|^2$, כלומר" "\n"
    r"$$\left(\sum_{k=1}^n\sqrt{(2k-1)\ln k}\right)^2\le n^2\ln(n!)$$"
)

S5C = (
    r"$$A^TA=\begin{pmatrix}3&2&2\\2&3&-2\end{pmatrix}\begin{pmatrix}3&2\\2&3\\2&-2\end{pmatrix}=\begin{pmatrix}17&8\\8&17\end{pmatrix}$$" "\n"
    r"$$\left|A^TA-\lambda I\right|=(17-\lambda)^2-64=(\lambda-25)(\lambda-9)\ \Rightarrow\ \lambda_1=25,\ \lambda_2=9$$" "\n"
    r"הערכים הסינגולריים: $\sigma_1=5,\ \sigma_2=3$." "\n"
    r"וקטורים עצמיים מנורמלים של $A^TA$: עבור $\lambda=25$: $\vec v_1=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$; עבור $\lambda=9$: $\vec v_2=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$." "\n"
    r"$$\vec u_1=\frac1{\sigma_1}A\vec v_1=\frac1{5\sqrt2}\begin{pmatrix}5\\5\\0\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1\\1\\0\end{pmatrix},\qquad\vec u_2=\frac1{\sigma_2}A\vec v_2=\frac1{3\sqrt2}\begin{pmatrix}1\\-1\\4\end{pmatrix}$$" "\n"
    r"את $\vec u_3$ נשלים כוקטור יחידה האורתוגונלי ל-$\vec u_1,\vec u_2$ (פתרון של $x_1+x_2=0,\ x_1-x_2+4x_3=0$, או מכפלה וקטורית):" "\n"
    r"$$\begin{pmatrix}1\\1\\0\end{pmatrix}\times\begin{pmatrix}1\\-1\\4\end{pmatrix}=\begin{pmatrix}4\\-4\\-2\end{pmatrix}\ \Rightarrow\ \vec u_3=\frac13\begin{pmatrix}2\\-2\\-1\end{pmatrix}$$" "\n"
    r"ולכן $A=USV^T$ עם" "\n"
    r"$$U=\begin{pmatrix}\frac1{\sqrt2}&\frac1{3\sqrt2}&\frac23\\\frac1{\sqrt2}&-\frac1{3\sqrt2}&-\frac23\\0&\frac4{3\sqrt2}&-\frac13\end{pmatrix},\qquad S=\begin{pmatrix}5&0\\0&3\\0&0\end{pmatrix},\qquad V=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$"
)

S5D = (
    r"המודולים $5,8,9$ זרים בזוגות, ולכן לפי משפט השאריות הסיני יש פתרון יחיד מודולו $M=5\cdot8\cdot9=360$." "\n"
    r"$$M_1=\frac{360}5=72\equiv2\pmod5,\quad 2y_1\equiv1\pmod5\Rightarrow y_1=3$$" "\n"
    r"$$M_2=\frac{360}8=45\equiv5\pmod8,\quad 5y_2\equiv1\pmod8\Rightarrow y_2=5$$" "\n"
    r"$$M_3=\frac{360}9=40\equiv4\pmod9,\quad 4y_3\equiv1\pmod9\Rightarrow y_3=7$$" "\n"
    r"$$x\equiv3\cdot72\cdot3+2\cdot45\cdot5+4\cdot40\cdot7=648+450+1120=2218\equiv58\pmod{360}$$" "\n"
    r"בדיקה: $58=5\cdot11+3=8\cdot7+2=9\cdot6+4$." "\n"
    r"$$\left\{58+360k\ \middle|\ k\in\mathbb{Z}\right\}$$"
)

questions = [
    Q(1, "computation", "orthogonality",
      r"סעיף א.1. בצעו תהליך גרם-שמידט עבור המערכת $\left\{A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ B=\begin{pmatrix}1&1\\0&-1\end{pmatrix}\right\}$. (9%)",
      S1A, part="א", points=9, contextId="c1"),
    Q(1, "computation", "projection",
      r"סעיף א.2. חשבו את ההיטל של $C=\begin{pmatrix}2&3\\1&0\end{pmatrix}$ על $U=\mathrm{Sp}\{A,B\}$. (6%)",
      S1B, part="ב", points=6, contextId="c1"),
    Q(1, "proof", "pos_def",
      r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית לחלוטין. הוכיחו כי $A+A^2$ ו-$A+A^{-1}$ הן גם מוגדרות חיובית לחלוטין. (10%)",
      S1C, part="ג", points=10),

    Q(2, "computation", "groups", r"סעיף 1. מהו הסדר של $G$ ? (6%)", S2A, part="א", points=6, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף 2. חשבו את כל האיברים של $H$. (6%)", S2B, part="ב", points=6, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף 3. מצאו את $J^{-1}$. (4%)", S2C, part="ג", points=4, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף 4. מהו הסדר של $H$ ? (3%)", S2D, part="ד", points=3, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף 5. מצאו $A\in G$ כך $AJA^{-1}\notin H$. (6%)", S2E, part="ה", points=6, contextId="c2"),

    Q(3, "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}1&0&2a\\0&4-a^2&0\\2a&0&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (15%)",
      S3A, part="א", points=15),
    Q(3, "computation", "least_squares",
      r"סעיף ב. נתונות 5 נקודות במישור: $(0,2),\ (1,2),\ (2,4),\ (3,8),\ (4,9)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו בעזרת שיטת הריבועים הפחותים. (10%)",
      S3B, part="ב", points=10),

    Q(4, "proof", "groups",
      r"סעיף א. תהי $G$ חבורה בה לכל $x,y\in G$ מתקיים $(xy)^2=x^2y^2$. הוכיחו כי $G$ חבורה אבלית, כלומר לכל $x,y\in G$ מתקיים $x\cdot y=y\cdot x$. (7%)",
      S4A, part="א", points=7),
    Q(4, "proof", "groups",
      r"סעיף ב. תהי $K$ חבורה ו-$x,y\in K$. הוכיחו כי אם $xyx^{-1}=y^2$, אז $x^2yx^{-2}=y^4$. (7%)",
      S4B, part="ב", points=7),
    Q(4, "proof", "cauchy_schwarz",
      r"סעיף ג. הוכיחו את אי השוויון הבא: $\displaystyle\left(\sum_{k=1}^n\sqrt{(2k-1)\ln k}\right)^2\le n^2\ln(n!)$. (11%)",
      S4C, part="ג", points=11),

    Q(5, "computation", "svd", r"סעיף ג. מצאו פירוק SVD עבור המטריצה $A=\begin{pmatrix}3&2\\2&3\\2&-2\end{pmatrix}$. (17%)", S5C, part="ג", points=17),
    Q(5, "computation", "crt",
      r"סעיף ד. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv3\pmod5\\x\equiv2\pmod8\\x\equiv4\pmod9\end{cases}$. (8%)",
      S5D, part="ד", points=8),
]

exam = {
    "examCode": "26B-A",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ו מועד א'",
    "year": 2026,
    "examDate": "17.6.2026",
    "sourceFile": "algebra-2-26B-A-exam",
    "solutionFile": "none",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
