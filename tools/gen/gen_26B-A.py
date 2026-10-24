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

# ---- rubric / pitfalls / steps (ai-draft). Every value and distractor is checked in tools/verify/26B-A/steps_26B-A.py ----
IDS = "abcdefgh"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def mat(a, b, c, d):
    return r"$\begin{pmatrix}%s&%s\\%s&%s\end{pmatrix}$" % (a, b, c, d)


def add(num, part, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError((num, part))


def num_step(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


add(1, "א",
    rubric=rub((r"חישוב $\langle B,A\rangle=tr\left(A^TB\right)$ ו-$\|A\|^2$", 2),
               (r"$\vec u_1=A$ ו-$\vec u_2=B-\frac{\langle B,A\rangle}{\|A\|^2}A$ ומתקבל $\begin{pmatrix}0&1\\0&0\end{pmatrix}$", 4),
               (r"נרמול: חלוקה של כל וקטור באורכו ($\sqrt2$ ו-$1$)", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב את המכפלה הפנימית כמכפלת מטריצות רגילה ולא כסכום מכפלות הרכיבים המתאימים, $tr\left(B^TA\right)$.",
              r"לשכוח לחלק ב-$\|\vec u_1\|^2$ בהיטל, או לשכוח את שלב הנרמול ולהשאיר בסיס אורתוגונלי בלבד."],
    steps=[
        num_step(r"חשבו $\langle B,A\rangle=tr\left(A^TB\right)$ עבור $A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ ו-$B=\begin{pmatrix}1&1\\0&-1\end{pmatrix}$.", 2,
                 r"המכפלה הפנימית היא סכום מכפלות הרכיבים המתאימים: $1\cdot1+0\cdot1+0\cdot0+(-1)(-1)=2$. וגם $\|A\|^2=1+0+0+1=2$ (נבדק ב-sympy)."),
        {"type": "choice", "prompt": r"מהו $\vec u_2=B-\frac{\langle B,A\rangle}{\|A\|^2}A$ ?",
         "options": opts(mat(0, 1, 0, 0), mat(-1, 1, 0, 1), mat(2, 1, 0, -2), mat(1, 1, 0, -1)), "correctId": "a",
         "explain": r"$B-\frac22A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. האפשרויות האחרות אינן אורתוגונליות ל-$A$: $B-2A$, $B+A$ ו-$B$ נותנות מכפלה פנימית עם $A$ שאינה אפס (נבדק ב-sympy)."},
        num_step(r"מהו האורך $\|\vec u_1\|$ של $\vec u_1=A$ (תשובה עשרונית)? בו מחלקים בשלב הנרמול.", 1.4142,
                 r"$\|A\|=\sqrt2\approx1.4142$, ואילו $\|\vec u_2\|=1$ ולכן הוא כבר מנורמל.", tol=0.001),
    ],
    stepsSource="ai-verified")

add(1, "ב",
    rubric=rub((r"חישוב $\langle C,\vec u_1\rangle=2$ ו-$\langle C,\vec u_2\rangle=3$ מול הבסיס האורתוגונלי", 2),
               (r"הצבה בנוסחת ההיטל עם החלוקה ב-$\|\vec u_i\|^2$", 2),
               (r"התוצאה $\begin{pmatrix}1&3\\0&-1\end{pmatrix}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשתמש ב-$A$ וב-$B$ המקוריים בנוסחת ההיטל הפשוטה, אף שאינם אורתוגונליים זה לזה; חובה להשתמש בבסיס מגרם-שמידט.",
              r"לשכוח לחלק ב-$\|\vec u_i\|^2$ (כאן $2$ עבור הראשון)."],
    steps=[
        num_step(r"חשבו $\langle C,\vec u_1\rangle$ עבור $C=\begin{pmatrix}2&3\\1&0\end{pmatrix}$ ו-$\vec u_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$.", 2,
                 r"$2\cdot1+3\cdot0+1\cdot0+0\cdot(-1)=2$."),
        num_step(r"חשבו $\langle C,\vec u_2\rangle$ עבור $\vec u_2=\begin{pmatrix}0&1\\0&0\end{pmatrix}$.", 3,
                 r"רק הרכיב $(1,2)$ תורם: $3\cdot1=3$."),
        {"type": "choice", "prompt": r"מהו ההיטל של $C$ על $U=\mathrm{Sp}\{A,B\}$ ?",
         "options": opts(mat(1, 3, 0, -1), mat(2, 3, 0, 0), mat(1, 3, 0, 1), mat(1, 3, 1, -1)), "correctId": "a",
         "explain": r"$\frac22\vec u_1+\frac31\vec u_2=\begin{pmatrix}1&3\\0&-1\end{pmatrix}$. שלוש האפשרויות האחרות אינן שייכות ל-$U$ (איברי $U$ הם מהצורה $\begin{pmatrix}p&q\\0&-p\end{pmatrix}$), ולכן אינן יכולות להיות היטל (נבדק ב-sympy)."},
    ],
    stepsSource="ai-verified")

add(1, "ג",
    rubric=rub((r"הגדרה: $A$ סימטרית ו-$x^TAx>0$ לכל $x\neq0$; $A$ הפיכה, ושתי המטריצות החדשות סימטריות", 2),
               (r"$A+A^2$: $x^TAx+\|Ax\|^2>0$", 4),
               (r"$A+A^{-1}$: הצבת $y=A^{-1}x\neq0$ ומתקבל $x^TA^{-1}x=y^TAy>0$", 4)),
    rubricSource="ai-verified",
    pitfalls=["לבדוק רק את הדטרמיננטה או רק את סימני האיברים, שאינם מספיקים להגדרת חיוביות לחלוטין.",
              r"לכתוב $\left(A^2\right)^T=A^2$ בלי לנמק, או לשכוח לבדוק סימטריה של $A+A^{-1}$.",
              r"בשלב $x^TA^{-1}x$ לשכוח שצריך $y\neq0$, ולכן לא להסיק $y^TAy>0$."],
    steps=[
        {"type": "choice", "prompt": r"מה צריך להראות עבור מטריצה $M$ כדי להוכיח שהיא מוגדרת חיובית לחלוטין?",
         "options": opts(r"$M$ סימטרית וגם $x^TMx>0$ לכל $x\neq0$", r"$\det M>0$", r"כל איברי $M$ חיוביים", r"$M$ הפיכה"), "correctId": "a",
         "explain": r"זו ההגדרה. $\det M>0$ אינו מספיק ($M=-I$), וחיוביות האיברים אינה הכרחית ($\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ מוגדרת חיובית); הפיכות לבדה אינה מספיקה (נבדק ב-sympy)."},
        {"type": "order", "prompt": r"סדרו את ההוכחה ש-$A+A^2$ מוגדרת חיובית לחלוטין (לכל $x\neq0$).",
         "lines": [r"יהי $x\neq0$. מפתחים: $x^T\left(A+A^2\right)x=x^TAx+x^TA^TAx$ (כי $A$ סימטרית)",
                   r"$x^TA^TAx=(Ax)^T(Ax)=\|Ax\|^2\ge0$ וכן $x^TAx>0$ כי $A$ מוגדרת חיובית לחלוטין",
                   r"לכן $x^T\left(A+A^2\right)x>0$, ביחד עם הסימטריה של $A+A^2$ זה מראה שהיא מוגדרת חיובית לחלוטין"],
         "explain": "קודם מפתחים את הביטוי, אחר כך מסווגים את שני המחוברים, ורק בסוף מסיקים."},
        {"type": "findbug", "prompt": r"בהוכחה ש-$A+A^{-1}$ מוגדרת חיובית לחלוטין שורה אחת שגויה. מצאו אותה.",
         "lines": [r"יהי $x\neq0$ ונסמן $y=A^{-1}x$; אז $y\neq0$ כי $x=Ay$",
                   r"$x^TA^{-1}x=(Ay)^TA^{-1}(Ay)$",
                   r"$=y^TA^TA^{-1}Ay=y^Ty$",
                   r"$y^TAy>0$ כי $A$ מוגדרת חיובית לחלוטין ו-$y\neq0$",
                   r"לכן $x^T\left(A+A^{-1}\right)x=x^TAx+x^TA^{-1}x>0$"],
         "bugIndex": 2,
         "explain": r"$A^T=A$ ולכן $A^TA^{-1}A=A$, והשורה הנכונה היא $=y^TAy$. השורה שנכתבה ($y^Ty$) שגויה כי $A^TA^{-1}A$ אינה $I$ (נבדק ב-sympy)."},
    ],
    stepsSource="ai-verified")

add(2, "א",
    rubric=rub((r"$a\cdot c\neq0$ מודולו 5 ראשוני אם ורק אם $a\neq0$ וגם $c\neq0$: 4 אפשרויות לכל אחד", 3),
               (r"$b$ חופשי: 5 אפשרויות", 1),
               (r"$|G|=4\cdot5\cdot4=80$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לספור $5\cdot5\cdot5=125$ או לשכוח שהתנאי $a\cdot c\neq0$ מוציא את הערך $0$ מכל אחד מהם.",
              r"להגביל גם את $b$ לערכים שונים מאפס."],
    steps=[
        num_step(r"כמה ערכים אפשריים יש ל-$a\in\mathbb{Z}_5$ (בלי $b$ ו-$c$) כך שהמטריצה הפיכה, כלומר $a\cdot c\neq0$ מודולו 5?", 4,
                 r"$5$ ראשוני, ולכן $a\cdot c\neq0$ אם ורק אם $a\neq0$ וגם $c\neq0$: $4$ ערכים לכל אחד (נבדק במניית כל המטריצות)."),
        num_step(r"כמה ערכים אפשריים יש ל-$b\in\mathbb{Z}_5$ ?", 5, r"$b$ חופשי לגמרי."),
        num_step(r"מהו $|G|$ ?", 80, r"$4\cdot5\cdot4=80$ (נבדק במניית כל המטריצות מעל $\mathbb{Z}_5$)."),
    ],
    stepsSource="ai-verified")

add(2, "ב",
    rubric=rub((r"חישוב $J^2$ ו-$J^3$ מודולו 5", 3),
               (r"$J^4=I$ ולכן החזקות חוזרות (כולל חזקות שליליות)", 2),
               (r"רישום ארבעת האיברים של $H$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח לצמצם מודולו 5, ולכתוב $J^3=\begin{pmatrix}1&7\\0&8\end{pmatrix}$.",
              r"להמשיך לחשב חזקות אחרי $J^4=I$ ולא להבחין שהן חוזרות."],
    steps=[
        num_step(r"מהו הרכיב $(1,2)$ של $J^2$, מודולו 5, כאשר $J=\begin{pmatrix}1&1\\0&2\end{pmatrix}$ ?", 3,
                 r"$J^2=\begin{pmatrix}1&3\\0&4\end{pmatrix}$ (נבדק ב-sympy)."),
        num_step(r"מהו הרכיב $(1,2)$ של $J^3$, מודולו 5?", 2,
                 r"$J^3=\begin{pmatrix}1&7\\0&8\end{pmatrix}\equiv\begin{pmatrix}1&2\\0&3\end{pmatrix}$."),
        num_step(r"כמה איברים שונים יש ב-$H$ ? (רמז: $J^4=I$.)", 4,
                 r"$I,J,J^2,J^3$ שונים זה מזה, ו-$J^4=I$ סוגר את המחזור."),
    ],
    stepsSource="ai-verified")

add(2, "ג",
    rubric=rub((r"שימוש ב-$J^4=I$ כדי לקבל $J^{-1}=J^3$", 2),
               (r"התוצאה $\begin{pmatrix}1&2\\0&3\end{pmatrix}$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להפוך את המטריצה מעל $\mathbb{R}$ ולקבל $\begin{pmatrix}1&-1/2\\0&1/2\end{pmatrix}$ במקום לעבוד מודולו 5."],
    steps=[
        num_step(r"אם $J^4=I$, אז $J^{-1}=J^k$ עבור איזה $k$ בין $1$ ל-$3$ ?", 3, r"$J\cdot J^3=J^4=I$."),
        num_step(r"מהו הרכיב $(1,2)$ של $J^{-1}$, מודולו 5?", 2,
                 r"$J^{-1}=J^3=\begin{pmatrix}1&2\\0&3\end{pmatrix}$, ו-$J\cdot J^{-1}\equiv I$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

add(2, "ד",
    rubric=rub((r"$|H|$ שווה לסדר של $J$ (חבורה ציקלית)", 1),
               (r"$J,J^2,J^3\neq I$ ו-$J^4=I$ ולכן הסדר $4$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לענות $80$ (הסדר של $G$) או $5$ (המודולו)."],
    steps=[
        {"type": "choice", "prompt": r"מה הקשר בין $|H|$ לסדר $o(J)$ של $J$ בחבורה הציקלית $H=\{J^n\}$ ?",
         "options": opts(r"$|H|=o(J)$", r"$|H|=o(J)+1$", r"$|H|=2\,o(J)$", r"$|H|=o(J)-1$"), "correctId": "a",
         "explain": r"החבורה הנוצרת ע״י $J$ מורכבת מ-$I,J,\dots,J^{o(J)-1}$. כאן ארבעת האיברים $I,J,J^2,J^3$ שונים, כלומר $|H|=4=o(J)$ ולא $5$, $8$ או $3$."},
        num_step(r"מהו $|H|$ ?", 4, r"$J^4=I$ ו-$J,J^2,J^3\neq I$, ולכן $o(J)=4$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

add(2, "ה",
    rubric=rub((r"זיהוי שכל איברי $H$ הם מהצורה $\begin{pmatrix}1&c-1\\0&c\end{pmatrix}$, כלומר $J$ הוא האיבר היחיד עם $2$ בפינה", 2),
               (r"בחירת $A\in G$ (למשל $\begin{pmatrix}1&1\\0&1\end{pmatrix}$) וחישוב $A^{-1}$", 2),
               (r"חישוב $AJA^{-1}=\begin{pmatrix}1&2\\0&2\end{pmatrix}\notin H$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לבחור $A$ ששייכת ל-$H$ (למשל $J^2$) או כזו שמתחלפת עם $J$, ואז $AJA^{-1}=J\in H$.",
              r"לבחור מטריצה שאינה משולשת עליונה, שאינה שייכת ל-$G$.",
              r"לשכוח לחשב $A^{-1}$ מודולו 5."],
    steps=[
        {"type": "choice", "prompt": r"איזה איבר של $H$ הוא היחיד שהרכיב $(2,2)$ שלו הוא $2$ (מודולו 5)?",
         "options": opts(r"$J$", r"$J^2$", r"$J^3$", r"$I$"), "correctId": "a",
         "explain": r"הרכיב $(2,2)$ של $I,J,J^2,J^3$ הוא $1,2,4,3$ בהתאמה. ולכל $A\in G$ הצמוד $AJA^{-1}$ שומר על $2$ בפינה, ולכן הוא ב-$H$ אם ורק אם הוא $J$ (נבדק לכל 80 האיברים של $G$)."},
        {"type": "choice", "prompt": r"לאיזו מהמטריצות הבאות $A$ מתקיים $A\in G$ וגם $AJA^{-1}\notin H$ ?",
         "options": opts(r"$\begin{pmatrix}1&1\\0&1\end{pmatrix}$", r"$I$", r"$J^2$", r"$\begin{pmatrix}1&0\\1&1\end{pmatrix}$"), "correctId": "a",
         "explain": r"עבור $I$ ו-$J^2$ מתקבל $AJA^{-1}=J\in H$ (הן מתחלפות עם $J$); המטריצה $\begin{pmatrix}1&0\\1&1\end{pmatrix}$ אינה משולשת עליונה ולכן אינה ב-$G$. (יש עוד תשובות שונות לשאלה המקורית, אך כאן רק $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ מתאימה.)"},
        num_step(r"עבור $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ חשבו את הרכיב $(1,2)$ של $AJA^{-1}$, מודולו 5.", 2,
                 r"$AJA^{-1}=\begin{pmatrix}1&2\\0&2\end{pmatrix}$, שאינה $J$ ולכן אינה ב-$H$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

add(3, "א",
    rubric=rub((r"חישוב הערכים העצמיים $4-a^2,\ 1+2a,\ 1-2a$ (המטריצה סימטרית)", 5),
               (r"מוגדרת חיובית לחלוטין אם ורק אם $-\frac12<a<\frac12$", 3),
               (r"מוגדרת חיובית (חצי-מוגדרת) אם ורק אם $-\frac12\le a\le\frac12$", 3),
               (r"אין $a$ שעבורו המטריצה מוגדרת שלילית או שלילית לחלוטין", 2),
               (r"אף אחת מהן כאשר $|a|>\frac12$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לבדוק רק את הערך העצמי $4-a^2$ ולהסיק $|a|<2$ ולשכוח את $1\pm2a$.",
              "לא להבדיל בין מוגדרת חיובית (אי-שוויון חלש, ערך עצמי $0$ מותר) לבין מוגדרת חיובית לחלוטין.",
              r"לשכוח שהמטריצה אף פעם אינה שלילית: $1+2a$ ו-$1-2a$ לא יכולים להיות שניהם אי-חיוביים."],
    steps=[
        {"type": "choice", "prompt": "מהם הערכים העצמיים של המטריצה?",
         "options": opts(r"$4-a^2,\ 1+2a,\ 1-2a$", r"$4-a^2,\ 1+a,\ 1-a$", r"$4-a^2,\ 2a,\ -2a$", r"$4-a^2,\ 1+4a^2,\ 1-4a^2$"), "correctId": "a",
         "explain": r"פיתוח לפי השורה האמצעית נותן $\left(4-a^2-\lambda\right)\left((1-\lambda)^2-4a^2\right)$ (נבדק ב-sympy); שאר האפשרויות אינן הערכים העצמיים."},
        {"type": "choice", "prompt": "עבור אילו ערכי $a$ המטריצה מוגדרת חיובית לחלוטין?",
         "options": opts(r"$-\frac12<a<\frac12$", r"$|a|<2$", r"$-\frac12\le a\le\frac12$", r"$a>-\frac12$"), "correctId": "a",
         "explain": r"נדרש $4-a^2>0$, $1+2a>0$ ו-$1-2a>0$. התנאי $|a|<2$ מתעלם מ-$1\pm2a$; התחום $-\frac12\le a\le\frac12$ מכיל את $a=\frac12$ שבו ערך עצמי הוא $0$; והתחום $a>-\frac12$ כולל $a=1$ שבו $1-2a<0$."},
        {"type": "choice", "prompt": r"מה סוג המטריצה עבור $a=\frac12$ ?",
         "options": opts("מוגדרת חיובית אך לא לחלוטין", "מוגדרת חיובית לחלוטין", "מוגדרת שלילית", "אף אחת מהן"), "correctId": "a",
         "explain": r"הערכים העצמיים הם $\frac{15}4,\ 2,\ 0$: אי-שליליים ואחד מהם $0$ (נבדק ב-sympy)."},
        {"type": "choice", "prompt": r"מה סוג המטריצה עבור $a=1$ ?",
         "options": opts("אף אחת מהן", "מוגדרת חיובית אך לא לחלוטין", "מוגדרת חיובית לחלוטין", "מוגדרת שלילית"), "correctId": "a",
         "explain": r"הערכים העצמיים הם $3,\ 3,\ -1$: יש גם חיובי וגם שלילי, ולכן אינה אף אחת מהן (נבדק ב-sympy)."},
    ],
    stepsSource="ai-verified")

add(3, "ב",
    rubric=rub((r"בניית $A$ ו-$\vec y$ מהנקודות והמשוואות הנורמליות $A^TA\vec v=A^T\vec y$", 3),
               (r"חישוב $A^TA=\begin{pmatrix}30&10\\10&5\end{pmatrix}$ ו-$A^T\vec y=\begin{pmatrix}70\\25\end{pmatrix}$", 3),
               (r"פתרון המערכת: $m=2$, $n=1$ ולכן $y=2x+1$", 4)),
    rubricSource="ai-verified",
    pitfalls=["לשים את עמודת האחדות לפני עמודת ה-$x$ ולהחליף בין השיפוע לחותך.",
              r"לפתור את המערכת $A\vec v=\vec y$ ישירות (אין לה פתרון) במקום את המשוואות הנורמליות."],
    steps=[
        num_step(r"בנו את $A$ בעלת השורות $(x_i,1)$. מהו הרכיב $(1,1)$ של $A^TA$, כלומר $\sum x_i^2$ ?", 30,
                 r"$0+1+4+9+16=30$ (נבדק ב-sympy)."),
        num_step(r"מהו הרכיב הראשון של $A^T\vec y$, כלומר $\sum x_iy_i$ ?", 70,
                 r"$0\cdot2+1\cdot2+2\cdot4+3\cdot8+4\cdot9=70$."),
        num_step(r"מהו השיפוע $m$ של הישר?", 2, r"פתרון $\begin{pmatrix}30&10\\10&5\end{pmatrix}\binom mn=\binom{70}{25}$ נותן $m=2$."),
        num_step(r"מהו החותך $n$ של הישר עם ציר ה-$y$?", 1, r"$n=1$ ולכן $y=2x+1$."),
    ],
    stepsSource="ai-verified")

add(4, "א",
    rubric=rub((r"פתיחת הנתון $(xy)^2=x^2y^2$ לצורה $xyxy=xxyy$", 2),
               (r"כפל משמאל ב-$x^{-1}$ ומימין ב-$y^{-1}$ וצמצום", 3),
               (r"המסקנה $yx=xy$ ולכן $G$ אבלית", 2)),
    rubricSource="ai-verified",
    pitfalls=["לצמצם את האיברים האמצעיים ישירות כאילו החבורה אבלית; צמצום חוקי רק מהקצוות, ע״י כפל בהופכי.",
              r"להוכיח את השוויון רק עבור איברים מסוימים ולא לכל $x,y\in G$."],
    steps=[
        {"type": "order", "prompt": "סדרו את שלבי ההוכחה.",
         "lines": [r"יהיו $x,y\in G$. מהנתון $xyxy=xxyy$",
                   r"נכפול משמאל ב-$x^{-1}$ ומימין ב-$y^{-1}$ ונקבל $yx=xy$",
                   r"לכן $G$ אבלית"],
         "explain": "הנתון נפתח קודם, אחר כך מצמצמים מהקצוות, ורק בסוף מסיקים."},
        {"type": "findbug", "prompt": "בגרסה הבאה של ההוכחה שורה אחת שגויה. מצאו אותה.",
         "lines": [r"מהנתון: $xyxy=xxyy$",
                   r"כפל משמאל ב-$x^{-1}$: $yxy=xyy$",
                   r"כפל מימין ב-$y^{-1}$: $yx=xy^2$",
                   r"לכן $yx=xy$ לכל $x,y$, כלומר $G$ אבלית"],
         "bugIndex": 2,
         "explain": r"$xyy\cdot y^{-1}=xy$ ולא $xy^2$. השורה הנכונה היא $yx=xy$."},
    ],
    stepsSource="ai-verified")

add(4, "ב",
    rubric=rub((r"כתיבת $x^2yx^{-2}=x\left(xyx^{-1}\right)x^{-1}$ והצבת הנתון: $xy^2x^{-1}$", 3),
               (r"פירוק $xy^2x^{-1}=\left(xyx^{-1}\right)\left(xyx^{-1}\right)$ בעזרת $x^{-1}x=e$", 2),
               (r"הצבה שנייה של הנתון: $y^2\cdot y^2=y^4$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להניח $xy=yx$ ולצמצם, בלי שהחבורה אבלית.",
              r"לטעות ב-$y^2\cdot y^2$ ולכתוב $y^3$ או $y^2$."],
    steps=[
        num_step(r"אם $x^2yx^{-2}=y^k$ מתקבל משני שימושים בנתון $xyx^{-1}=y^2$, מהו $k$ ?", 4,
                 r"כל שימוש מרבע את החזקה: $y\to y^2\to\left(y^2\right)^2=y^4$."),
        {"type": "order", "prompt": r"סדרו את שלבי החישוב של $x^2yx^{-2}$.",
         "lines": [r"$x^2yx^{-2}=x\left(xyx^{-1}\right)x^{-1}=xy^2x^{-1}$",
                   r"$xy^2x^{-1}=xy\left(x^{-1}x\right)yx^{-1}=\left(xyx^{-1}\right)\left(xyx^{-1}\right)$",
                   r"$=y^2\cdot y^2=y^4$"],
         "explain": r"הצבה ראשונה של הנתון, אחר כך הכנסת $x^{-1}x$ באמצע, ואז הצבה שנייה."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שגויה. מצאו אותה.",
         "lines": [r"$x^2yx^{-2}=x\left(xyx^{-1}\right)x^{-1}=xy^2x^{-1}$",
                   r"$xy^2x^{-1}=xy\left(x^{-1}x\right)yx^{-1}=\left(xyx^{-1}\right)\left(xyx^{-1}\right)$",
                   r"$=y^2\cdot y^2=y^3$"],
         "bugIndex": 2,
         "explain": r"$y^2\cdot y^2=y^4$ ולא $y^3$."},
    ],
    stepsSource="ai-verified")

add(4, "ג",
    rubric=rub((r"בחירת הווקטורים $\vec u=\left(\sqrt{2k-1}\right)$ ו-$\vec v=\left(\sqrt{\ln k}\right)$ ושימוש בקושי-שוורץ", 4),
               (r"חישוב $\langle\vec u,\vec v\rangle$, $\|\vec u\|^2=n^2$ ו-$\|\vec v\|^2=\ln(n!)$", 4),
               ("הצבה בקושי-שוורץ והמסקנה", 3)),
    rubricSource="ai-verified",
    pitfalls=["לבחור וקטורים שהמכפלה הפנימית שלהם אינה הסכום הנתון (למשל לשכוח את השורשים).",
              r"לשכוח ש-$\sum_{k=1}^n\ln k=\ln(n!)$, או לטעות בסכום $\sum(2k-1)=n^2$.",
              "להשתמש בנורמות עצמן במקום בריבועיהן."],
    steps=[
        {"type": "choice", "prompt": "באיזה אי-שוויון משתמש הפתרון?",
         "options": opts("קושי-שוורץ", "אי-שוויון הממוצעים (ממוצע חשבוני-הנדסי)", "אי-שוויון המשולש", "אי-שוויון ינסן"), "correctId": "a",
         "explain": r"הסכום $\sum\sqrt{2k-1}\sqrt{\ln k}$ הוא מכפלה פנימית של שני וקטורים, והאגף הימני הוא מכפלת ריבועי הנורמות שלהם: זו צורת קושי-שוורץ."},
        num_step(r"מהו $\sum_{k=1}^n(2k-1)$ עבור $n=7$ ? (הכללה: $n^2$.)", 49, r"$1+3+5+7+9+11+13=49=7^2$."),
        num_step(r"מהו $\sum_{k=1}^n\ln k$ עבור $n=4$ (תשובה עשרונית)? זה $\ln(n!)$.", 3.1781,
                 r"$\ln1+\ln2+\ln3+\ln4=\ln24\approx3.1781$.", tol=0.001),
        {"type": "order", "prompt": "סדרו את שלבי ההוכחה.",
         "lines": [r"נגדיר $\vec u=\left(\sqrt1,\sqrt3,\dots,\sqrt{2n-1}\right)$ ו-$\vec v=\left(\sqrt{\ln1},\dots,\sqrt{\ln n}\right)$",
                   r"נחשב $\langle\vec u,\vec v\rangle=\sum\sqrt{(2k-1)\ln k}$, $\|\vec u\|^2=n^2$ ו-$\|\vec v\|^2=\ln(n!)$",
                   r"קושי-שוורץ: $\langle\vec u,\vec v\rangle^2\le\|\vec u\|^2\|\vec v\|^2$",
                   r"נציב ונקבל $\left(\sum\sqrt{(2k-1)\ln k}\right)^2\le n^2\ln(n!)$"],
         "explain": "מגדירים את הווקטורים, מחשבים את שלוש הכמויות, ואז מפעילים את האי-שוויון ומציבים."},
    ],
    stepsSource="ai-verified")

add(5, "ג",
    rubric=rub((r"חישוב $A^TA=\begin{pmatrix}17&8\\8&17\end{pmatrix}$", 3),
               (r"ערכים עצמיים $25,9$ וערכים סינגולריים $\sigma_1=5,\ \sigma_2=3$", 4),
               ("וקטורים עצמיים מנורמלים ו-$V$", 3),
               (r"$\vec u_i=\frac1{\sigma_i}A\vec v_i$ והשלמת $\vec u_3$ אורתונורמלי", 5),
               (r"הרכבת $A=USV^T$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב את $AA^T$ ולהתאים את הווקטורים העצמיים ל-$V$ בצורה שגויה; לכן עדיף $\vec u_i=\frac1{\sigma_i}A\vec v_i$.",
              r"לשכוח לנרמל את הווקטורים העצמיים, או לשכוח שה-$\sigma_i$ הם שורשי הערכים העצמיים ($5$ ו-$3$, לא $25$ ו-$9$).",
              r"לשכוח להשלים עמודה שלישית ל-$U$ ($3\times3$) ולהשאיר $U$ בגודל $3\times2$."],
    steps=[
        num_step(r"מהו הרכיב $(1,2)$ של $A^TA$ עבור $A=\begin{pmatrix}3&2\\2&3\\2&-2\end{pmatrix}$ ?", 8,
                 r"$3\cdot2+2\cdot3+2\cdot(-2)=8$, ולכן $A^TA=\begin{pmatrix}17&8\\8&17\end{pmatrix}$ (נבדק ב-sympy)."),
        num_step(r"מהו הערך העצמי הגדול של $A^TA$ ?", 25, r"$(17-\lambda)^2=64$ נותן $\lambda=25$ או $\lambda=9$."),
        num_step(r"מהו הערך הסינגולרי הקטן $\sigma_2$ ?", 3, r"$\sigma_2=\sqrt9=3$."),
        {"type": "choice", "prompt": r"עבור $\vec v_2=\frac1{\sqrt2}\binom1{-1}$ ו-$\sigma_2=3$, מהו $\vec u_2=\frac1{\sigma_2}A\vec v_2$ ?",
         "options": opts(r"$\frac1{3\sqrt2}\begin{pmatrix}1\\-1\\4\end{pmatrix}$", r"$\frac13\begin{pmatrix}1\\-1\\4\end{pmatrix}$",
                         r"$\frac1{\sqrt2}\begin{pmatrix}1\\-1\\4\end{pmatrix}$", r"$\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}$"), "correctId": "a",
         "explain": r"$A\vec v_2=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\4\end{pmatrix}$, וחלוקה ב-$3$ נותנת וקטור יחידה. שאר האפשרויות שונות מ-$\frac1{\sigma_2}A\vec v_2$ (נבדק ב-sympy)."},
        num_step(r"להשלמת $\vec u_3$ מחשבים את המכפלה הווקטורית $\begin{pmatrix}1\\1\\0\end{pmatrix}\times\begin{pmatrix}1\\-1\\4\end{pmatrix}$. מהו הרכיב השלישי שלה?", -2,
                 r"$1\cdot(-1)-1\cdot1=-2$; הווקטור הוא $\begin{pmatrix}4\\-4\\-2\end{pmatrix}$, ולאחר נרמול $\vec u_3=\frac13\begin{pmatrix}2\\-2\\-1\end{pmatrix}$."),
    ],
    stepsSource="ai-verified")

add(5, "ד",
    rubric=rub(("המודולים זרים בזוגות ולכן קיים פתרון יחיד מודולו $360$", 1),
               (r"חישוב $M_i$ וההופכיים $y_1=3,\ y_2=5,\ y_3=7$", 4),
               (r"הרכבת $x=\sum a_iM_iy_i\equiv58\pmod{360}$", 2),
               (r"כתיבת קבוצת הפתרונות $58+360k$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב את $M_i$ אבל לשכוח להפוך אותו מודולו $m_i$.",
              r"לשכוח לצמצם בסוף מודולו $360$, או לכתוב את התוצאה $2218$ בלי להוסיף את כל $58+360k$."],
    steps=[
        num_step(r"מהו $M=5\cdot8\cdot9$ ?", 360, r"המודולים זרים בזוגות, ולכן $M=360$."),
        num_step(r"מצאו $y_1\in\{1,2,3,4\}$ כך ש-$72\,y_1\equiv1\pmod5$.", 3, r"$72\cdot3=216=43\cdot5+1$."),
        num_step(r"מצאו $y_2\in\{1,\dots,7\}$ כך ש-$45\,y_2\equiv1\pmod8$.", 5, r"$45\cdot5=225=28\cdot8+1$."),
        num_step(r"מצאו $y_3\in\{1,\dots,8\}$ כך ש-$40\,y_3\equiv1\pmod9$.", 7, r"$40\cdot7=280=31\cdot9+1$."),
        num_step(r"מהו הפתרון $x$ בתחום $0\le x<360$ ?", 58, r"$3\cdot72\cdot3+2\cdot45\cdot5+4\cdot40\cdot7=2218\equiv58\pmod{360}$ (נבדק עם crt של sympy)."),
    ],
    stepsSource="ai-verified")

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
