# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-B.json -- algebra-2 (20079), semester A 2023, moed B (1.03.2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-B.py

Source: exam 2 pp. + typed official solution 12 pp. (read from the rendered pages). 5 printed questions
(solve 4 of 5, 25% each), 10 items, all shipped.

Part letters: Q1..Q5 each have the printed parts a, b (Hebrew alef, bet); no numbered sub-parts.
Every question text starts with its printed label.

Checked with tools/verify/23A-B/check.py (sympy + brute force): every official answer is right, no final answer
is wrong. Notes on the official solution:
- Q3a: the official writes A = P D P^{-1} with P orthogonal; transcribed as printed (P^{-1} = P^T). D = diag(5,2,2)
  matches the column order of P (checked).
- Q3a: the official's first-row cofactor expansion is printed unsimplified; the characteristic polynomial
  (x-2)^2 (x-5) is the same.
- Q5a is a pasted calculator output (U, Sigma, V with A = U Sigma V^T); transcribed with the same matrices.
- Q5b: the official prints 94 mod 140 after a check; the sum before reduction is 794.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ------------------------------------------------------------------ contexts
CTX = {
    "c2a": {"kind": "text", "title": "שאלה 2 סעיף א",
            "text": r"במרחב $C[-1,1]$ של כל הפונקציות הרציפות בקטע $[-1,1]$ נגדיר את המכפלה הפנימית הבאה: $\langle f,g\rangle=\displaystyle\int_{-1}^{1}f(x)\cdot g(x)\,dx$. יהי $W=Sp\{1,|x|\}$ תת-מרחב של $C[-1,1]$."},
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף ב",
            "text": r"נתבונן בחבורה $G=\left\{A\in M_2(\mathbb{Z}_5)\ \middle|\ \det(A)\ne0\right\}$ ביחס לכפל מטריצות (חבורת המטריצות ההפיכות מגודל $2\times2$ עם רכיבים מ-$\mathbb{Z}_5$). תהי $H=\left\{\begin{pmatrix}a&c\\0&b\end{pmatrix}\in M_2(\mathbb{Z}_5)\ \middle|\ a\cdot b\ne0\right\}$ תת-חבורה של $G$. (כמובן שהכפל והחיבור של רכיבי המטריצות הם מודולו 5)."},
    "c4a": {"kind": "text", "title": "שאלה 4 סעיף א",
            "text": "נתון מבנה אלגברי $(A,*)$ שמקיים את התכונות הבאות:\n1. סגירות\n2. אסוציאטיביות\n3. קיום איבר נטרלי $e\\in A$\n4. לכל $x\\in A$ מתקיים $x*x=e$"},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"$$A=\begin{pmatrix}1&-2\\-1&2\\0&3\\2&5\end{pmatrix}\ \Rightarrow\ A^T=\begin{pmatrix}1&-1&0&2\\-2&2&3&5\end{pmatrix}\ \Rightarrow\ \left(A^TA\right)\vec x=A^T\vec b,\quad\vec x=\begin{pmatrix}m\\n\end{pmatrix}$$" "\n"
    "נחשב את המכפלות:\n"
    r"$$A^TA=\begin{pmatrix}1&-1&0&2\\-2&2&3&5\end{pmatrix}\begin{pmatrix}1&-2\\-1&2\\0&3\\2&5\end{pmatrix}=\begin{pmatrix}6&6\\6&42\end{pmatrix};\qquad A^T\vec b=\begin{pmatrix}1&-1&0&2\\-2&2&3&5\end{pmatrix}\begin{pmatrix}3\\1\\-4\\2\end{pmatrix}=\begin{pmatrix}6\\-6\end{pmatrix}$$" "\n"
    "נציב במשוואה:\n"
    r"$$\begin{pmatrix}6&6\\6&42\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}6\\-6\end{pmatrix}\ \Rightarrow\ \begin{pmatrix}1&1\\1&7\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}1\\-1\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\ \begin{cases}m+n=1\\m+7n=-1\end{cases}\ \Rightarrow\ n=-\frac13,\quad m=\frac43$$"
)

S1B = (
    "נבחר\n"
    r"$$\vec u=\left(\sqrt{\ln1},\sqrt{\ln2},\dots,\sqrt{\ln(n-1)},\sqrt{\ln n}\right),\qquad\vec v=\left(\sqrt{\ln n},\sqrt{\ln(n-1)},\dots,\sqrt{\ln2},\sqrt{\ln1}\right)$$" "\n"
    "אזי נקבל:\n"
    r"$$\vec u\cdot\vec v=\sqrt{\ln1}\cdot\sqrt{\ln n}+\sqrt{\ln2}\cdot\sqrt{\ln(n-1)}+\dots+\sqrt{\ln n}\cdot\sqrt{\ln1}=\sum_{k=1}^n\sqrt{(\ln k)\cdot\ln(n-k+1)}$$" "\n"
    "מצד שני:\n"
    r"$$\|\vec u\|^2=\|\vec v\|^2=\sqrt{\ln1}\sqrt{\ln1}+\sqrt{\ln2}\sqrt{\ln2}+\dots+\sqrt{\ln n}\sqrt{\ln n}=\ln1+\ln2+\dots+\ln n=\ln(1\cdot2\cdots n)=\ln(n!)$$" "\n"
    r"לפי אי-שיוויון קושי-שוורץ מתקיים $|\vec u\cdot\vec v|\le\|\vec u\|\cdot\|\vec v\|$. נציב ונקבל:" "\n"
    r"$$\sum_{k=1}^n\sqrt{(\ln k)\cdot\ln(n-k+1)}\le\sqrt{\ln(n!)}\sqrt{\ln(n!)}=\ln(n!)$$" "\n"
    "כנדרש!"
)

S2A = (
    r"ראשית, נבצע תהליך גרם-שמידט על $\{v_1,v_2\}=\{1,|x|\}$:" "\n"
    r"$$v_1=1\ \Rightarrow\ e_1=\frac{1}{\|1\|}$$" "\n"
    r"אצלנו:" "\n"
    r"$$\|1\|^2=\langle1,1\rangle=\int_{-1}^{1}1\cdot1\,dx=2\ \Rightarrow\ \|1\|=\sqrt2$$" "\n"
    r"ולכן $e_1=\dfrac1{\sqrt2}$. מכאן נובע:" "\n"
    r"$$v_2=|x|\ \Rightarrow\ e_2=\frac{|x|-\left\langle|x|,\frac1{\sqrt2}\right\rangle\frac1{\sqrt2}}{\left\|\,|x|-\left\langle|x|,\frac1{\sqrt2}\right\rangle\frac1{\sqrt2}\,\right\|}$$" "\n"
    "נחשב את המכפלה הפנימית שבמונה:\n"
    r"$$\left\langle|x|,\frac1{\sqrt2}\right\rangle\frac1{\sqrt2}=\frac12\int_{-1}^{1}|x|\,dx=\frac12\left(-\int_{-1}^{0}x\,dx+\int_0^1x\,dx\right)=\frac12\left(-\left[\frac{x^2}2\right]_{-1}^{0}+\left[\frac{x^2}2\right]_0^1\right)=\frac12$$" "\n"
    r"כלומר $e_2=\dfrac{|x|-\frac12}{\left\|\,|x|-\frac12\,\right\|}$ ; נחשב את הנורמה:" "\n"
    r"$$\left\|\,|x|-\tfrac12\,\right\|^2=\int_{-1}^{1}\left(|x|-\tfrac12\right)^2dx=\int_{-1}^{0}\left(x+\tfrac12\right)^2dx+\int_0^1\left(x-\tfrac12\right)^2dx=\frac13\cdot\frac12+\frac13\cdot\frac12=\frac16$$" "\n"
    r"כלומר $\left\|\,|x|-\frac12\,\right\|=\dfrac1{\sqrt6}$, ולכן $e_2=\sqrt6\left(|x|-\dfrac12\right)$. כעת נוכל לחשב את ההיטל:" "\n"
    r"$$\mathrm{Proj}_W\left(x^2\right)=\frac{\langle x^2,1\rangle}{\|1\|^2}\cdot1+\frac{\left\langle x^2,|x|-\frac12\right\rangle}{\left\|\,|x|-\frac12\,\right\|^2}\left(|x|-\frac12\right)=\frac12\int_{-1}^{1}x^2dx+6\left(|x|-\frac12\right)\int_{-1}^{1}x^2\left(|x|-\frac12\right)dx$$" "\n"
    r"$$=\frac12\cdot\frac23+6\left(|x|-\frac12\right)\left(-\left[\frac{x^4}4+\frac{x^3}6\right]_{-1}^{0}+\left[\frac{x^4}4-\frac{x^3}6\right]_0^1\right)=\frac13+6\left(|x|-\frac12\right)\cdot\frac16=|x|-\frac16$$"
)

S2B = (
    r"ראשית, ל-$c$ יש 5 אפשרויות: $0,1,2,3,4$." "\n"
    r"שנית, ל-$a,b$ יש 25 אפשרויות, ומתוכן אנחנו צריכים להוריד את הזוגות $(a,b)$ שמקיימים $ab=0$. ב-$\mathbb{Z}_5$, $ab=0$ פירושו $a=0$ או $b=0$, ולכן ניוותר עם 16 אפשרויות: 4 אפשרויות ל-$a$ ו-4 ל-$b$: $1,2,3,4$. סה״כ:" "\n"
    r"$$|H|=5\cdot4\cdot4=80$$"
)

S3A = (
    r"ראשית, נמצא ע״ע:" "\n"
    r"$$0=|xI-A|=\begin{vmatrix}x-3&-1&-1\\-1&x-3&-1\\-1&-1&x-3\end{vmatrix}=(x-3)\begin{vmatrix}x-3&-1\\-1&x-3\end{vmatrix}+\begin{vmatrix}-1&-1\\-1&x-3\end{vmatrix}-\begin{vmatrix}-1&x-3\\-1&-1\end{vmatrix}$$" "\n"
    r"$$=(x-3)\left((x-3)^2-1\right)+\left(-(x-3)-1\right)-(1+x-3)=(x-3)(x-4)(x-2)-2(x-2)$$" "\n"
    r"$$=(x-2)\left((x-3)(x-4)-2\right)=(x-2)\left(x^2-7x+10\right)=(x-2)(x-2)(x-5)$$" "\n"
    r"והע״ע הם $\lambda=5,2$ ($2$ מריבוי $2$). כעת, נמצא ו״ע:" "\n"
    r"$$A\vec v=\lambda\vec v\ \Longrightarrow\ \begin{cases}3x+y+z=\lambda x\\x+3y+z=\lambda y\\x+y+3z=\lambda z\end{cases}$$" "\n"
    r"**עבור $\lambda=5$:** $3x+y+z=5x,\ x+3y+z=5y,\ x+y+3z=5z$. כלומר $y=2x-z$ ו-$x=2y-z$; נציב זאת במשוואה השלישית $x+2x-z+3z=5z$ ונקבל $x=z$, ולכן $y=z$. והו״ע הם מהצורה $(t,t,t)$; אפשר לבחור: $(1,1,1)$, $\dfrac1{\sqrt3}(1,1,1)$." "\n"
    r"**עבור $\lambda=2$:** $3x+y+z=2x,\ x+3y+z=2y,\ x+y+3z=2z$. כלומר $x=-y-z$, והו״ע הם מהצורה $(-y-z,y,z)$. נבחר אחד מהם, למשל $(-1,1,0)$. כעת, נחפש אחד אחר שמאונך לו, כלומר:" "\n"
    r"$$0=\langle(-1,1,0),(-y-z,y,z)\rangle=y+z+y\ \Longrightarrow\ z=-2y$$" "\n"
    r"ואפשר לבחור $y=1,\ z=-2$ ולקבל את הוקטור $(1,1,-2)$. נשים לב שהוקטורים שמצאנו $(-1,1,0),(1,1,-2)$ אכן אורתוגונליים, וכעת ננרמל ונקבל: $\dfrac1{\sqrt2}(-1,1,0),\ \dfrac1{\sqrt6}(1,1,-2)$. סה״כ, המטריצות $P,D$ הבאות מקיימות $A=PDP^{-1}$, כאשר $P$ אורתוגונלית ו-$D$ אלכסונית:" "\n"
    r"$$D=\begin{pmatrix}5&0&0\\0&2&0\\0&0&2\end{pmatrix},\qquad P=\begin{pmatrix}\frac1{\sqrt3}&\frac{-1}{\sqrt2}&\frac1{\sqrt6}\\\frac1{\sqrt3}&\frac1{\sqrt2}&\frac1{\sqrt6}\\\frac1{\sqrt3}&0&\frac{-2}{\sqrt6}\end{pmatrix}$$" "\n"
    "כמובן, אפשר לסדר אחרת את הע״ע ו/ע במטריצה ולמצוא ו״ע אחרים."
)

S3B = (
    r"נפתח את אגף ימין ונסדר עד שנגיע לאגף שמאל; מכיוון שמרחב המכפלה הפנימית הוא ממשי, אפשר להשתמש בלינאריות גם ברכיב הימני:" "\n"
    r"$$\frac14\left(\|u+v\|^2-\|u-v\|^2\right)=\frac14\left(\langle u+v,u+v\rangle-\langle u-v,u-v\rangle\right)=$$" "\n"
    r"$$=\frac14\Big(\langle u,u\rangle+\langle u,v\rangle+\langle v,u\rangle+\langle v,v\rangle-\big(\langle u,u\rangle-\langle u,v\rangle-\langle v,u\rangle+\langle v,v\rangle\big)\Big)=$$" "\n"
    r"סימטריות $\langle u,v\rangle=\langle v,u\rangle$ תיתן לנו:" "\n"
    r"$$=\frac14\Big(\langle u,u\rangle+\langle u,v\rangle+\langle u,v\rangle+\langle v,v\rangle-\langle u,u\rangle+\langle u,v\rangle+\langle u,v\rangle-\langle v,v\rangle\Big)=\langle u,v\rangle$$" "\n"
    "כנדרש."
)

S4A = (
    r"נתון $c=(a*b)*a$." "\n"
    r"$$c*b=\big((a*b)*a\big)*b\overset{(1)}{=}(a*b)*(a*b)\overset{(2)}{=}e$$" "\n"
    r"(1) אסוציאטיביות (2) שימוש בנתון $x*x=e$." "\n"
    r"קיבלנו כי $c*b=e$." "\n"
    r"$$c=c*e=c*(c*b)\overset{(1)}{=}(c*c)*b\overset{(2)}{=}e*b=b$$" "\n"
    r"הוכחנו כי $c=b$."
)

S4B = (
    r"נסמן $\vec x=\begin{pmatrix}a\\b\end{pmatrix}$:" "\n"
    r"$$\begin{pmatrix}a&b\end{pmatrix}\begin{pmatrix}4&5\\5&6\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=4a^2+10ab+6b^2=2b^2\left(2\left(\frac ab\right)^2+5\left(\frac ab\right)+3\right)$$" "\n"
    r"נבדוק עבור אלו ערכים של $a,b$ מתקיים $\left(2\left(\frac ab\right)^2+5\left(\frac ab\right)+3\right)<0$ (כי $2b^2\ge0$)." "\n"
    r"נסמן $t=\dfrac ab$, נקבל את אי השוויון הבא: $2t^2+5t+3<0$." "\n"
    r"נק' החיתוך של הפרבולה עם ציר ה-$x$ הן: $t_1=-1.5,\ t_2=-1$. מכאן $-1.5<t=\dfrac ab<-1$." "\n"
    r"נבחר שני ערכים $a,b$ כלשהם שמקיימים את אי השוויון הנ״ל. למשל עבור $a=-5,\ b=4$ בדיקה: $4a^2+10ab+6b^2=100-200+96=-4<0$."
)

S5A = (
    r"נמצא את פירוק $SVD$ של $A=\begin{pmatrix}1&0\\0&3\\0&4\end{pmatrix}$." "\n"
    r"$$A^T=\begin{pmatrix}1&0&0\\0&3&4\end{pmatrix},\qquad W=AA^T=\begin{pmatrix}1&0&0\\0&9&12\\0&12&16\end{pmatrix}$$" "\n"
    r"הערכים העצמיים של $W$ והוקטורים העצמיים המתאימים:" "\n"
    r"$$\lambda=25:\ \begin{pmatrix}0\\\frac34\\1\end{pmatrix},\qquad\lambda=1:\ \begin{pmatrix}1\\0\\0\end{pmatrix},\qquad\lambda=0:\ \begin{pmatrix}0\\-\frac43\\1\end{pmatrix}$$" "\n"
    r"הערכים הסינגולריים (שורשי הערכים העצמיים השונים מאפס): $\sigma_1=5,\ \sigma_2=1$." "\n"
    r"$$\Sigma=\begin{pmatrix}5&0\\0&1\\0&0\end{pmatrix}$$" "\n"
    r"עמודות $U$ הן הוקטורים העצמיים המנורמלים, ו-$\vec v_i=\dfrac1{\sigma_i}A^T\vec u_i$:" "\n"
    r"$$\vec v_1=\frac15\begin{pmatrix}1&0&0\\0&3&4\end{pmatrix}\begin{pmatrix}0\\\frac35\\\frac45\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix},\qquad\vec v_2=\frac11\begin{pmatrix}1&0&0\\0&3&4\end{pmatrix}\begin{pmatrix}1\\0\\0\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}$$" "\n"
    r"לכן $V=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ ותשובה סופית:" "\n"
    r"$$U=\begin{pmatrix}0&1&0\\\frac35&0&-\frac45\\\frac45&0&\frac35\end{pmatrix}=\begin{pmatrix}0&1&0\\0.6&0&-0.8\\0.8&0&0.6\end{pmatrix},\quad\Sigma=\begin{pmatrix}5&0\\0&1\\0&0\end{pmatrix},\quad V=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad A=U\Sigma V^T$$"
)

S5B = (
    r"נתון: $x\equiv4\pmod 5,\ x\equiv3\pmod 7,\ x\equiv2\pmod 4$." "\n"
    r"נסמן: $a_1=4,\ a_2=3,\ a_3=2$ ; $m_1=5,\ m_2=7,\ m_3=4$ והם אכן זרים בזוגות. נסמן: $m=m_1m_2m_3=5\cdot7\cdot4=140$, ולכן: $M_1=28,\ M_2=20,\ M_3=35$." "\n"
    "לכן הפתרון למערכת הוא:\n"
    r"$$x=\left(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3\right)\bmod m=\left(4\cdot28\cdot x_1+3\cdot20\cdot x_2+2\cdot35\cdot x_3\right)\bmod140$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$28x_1\equiv1\pmod 5\Rightarrow3x_1\equiv1\pmod 5\Rightarrow x_1=2$$" "\n"
    r"$$20x_2\equiv1\pmod 7\Rightarrow6x_2\equiv1\pmod 7\Rightarrow x_2=6$$" "\n"
    r"$$35x_3\equiv1\pmod 4\Rightarrow3x_3\equiv1\pmod 4\Rightarrow x_3=3$$" "\n"
    "מכאן:\n"
    r"$$x=\left(4\cdot28\cdot2+3\cdot20\cdot6+2\cdot35\cdot3\right)\bmod140=94\bmod140$$" "\n"
    r"בדיקה: $94\equiv4\pmod 5$, $94\equiv3\pmod 7$, $94\equiv2\pmod 4$."
)

questions = [
    Q(1, "computation", "least_squares",
      r"(15%) פתרו את בעיית הריבועים הפחותים עבור המערכת $A\vec x=\vec b$ כאשר $A=\begin{pmatrix}1&-2\\-1&2\\0&3\\2&5\end{pmatrix}$ ו-$\vec b=\begin{pmatrix}3\\1\\-4\\2\end{pmatrix}$.",
      S1A, part="א", points=15),
    Q(1, "proof", "cauchy_schwarz",
      r"(10%) בעזרת אי-שוויון קושי-שוורץ הוכיחו כי $\displaystyle\sum_{k=1}^{n}\sqrt{\ln k\cdot\ln(n-k+1)}\ \le\ \ln(n!)$.",
      S1B, part="ב", points=10),

    Q(2, "computation", "projection", r"(15%) מצאו את ההיטל של $h(x)=x^2$ על $W$.", S2A, part="א", points=15, contextId="c2a"),
    Q(2, "computation", "groups", r"(10%) מצאו את הסדר של $H$.", S2B, part="ב", points=10, contextId="c2b"),

    Q(3, "computation", "orthodiag", r"(18%) בצעו לכסון אורתוגונלי למטריצה הבאה: $A=\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$.",
      S3A, part="א", points=18),
    Q(3, "proof", "inner_product",
      r"(7%) יהי $V$ מרחב מכפלה פנימית ממשי. הוכיחו כי עבור כל $\vec v,\vec u\in V$ מתקיים $\langle\vec u,\vec v\rangle=\dfrac14\left(\|\vec u+\vec v\|^2-\|\vec u-\vec v\|^2\right)$.",
      S3B, part="ב", points=7),

    Q(4, "proof", "groups",
      r"(15%) יהיו $a,b\in A$ שני איברים נתונים של $A$. נסמן: $c=(a*b)*a$. הוכיחו כי $c=b$.",
      S4A, part="א", points=15, contextId="c4a"),
    Q(4, "computation", "pos_def",
      r"(10%) תהי $B=\begin{pmatrix}4&5\\5&6\end{pmatrix}$. מצאו וקטור $\vec x\in\mathbb{R}^2$ כך ש: $\vec x^TB\vec x<0$.",
      S4B, part="ב", points=10),

    Q(5, "computation", "svd", r"(18%) מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}1&0\\0&3\\0&4\end{pmatrix}$.", S5A, part="א", points=18),
    Q(5, "computation", "crt",
      r"(7%) פתרו את המערכות הבאות באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv4\pmod 5\\x\equiv3\pmod 7\\x\equiv2\pmod 4\end{cases}$.",
      S5B, part="ב", points=7),
]

# ---- rubric / pitfalls / steps (ai-draft). Every numeric value is recomputed in tools/verify/23A-B/steps_check.py ----
IDS = "abcdefgh"


def ch(prompt, right, wrong, explain, pos=0):
    vals = list(wrong)
    vals.insert(pos, right)
    return {"type": "choice", "prompt": prompt, "options": [{"id": IDS[i], "value": v} for i, v in enumerate(vals)],
            "correctId": IDS[pos], "explain": explain}


def nm(prompt, ans, explain, tol=0.001):
    return {"type": "numeric", "prompt": prompt, "answer": ans, "tol": tol, "explain": explain}


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def add(num, part, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            assert "steps" not in q
            q.update(kw)
            return
    raise KeyError((num, part))


add(1, "א",
    rubric=rub((r"בניית המערכת הנורמלית $A^TA\vec x=A^T\vec b$", 3),
               (r"חישוב $A^TA=\begin{pmatrix}6&6\\6&42\end{pmatrix}$", 4),
               (r"חישוב $A^T\vec b=\begin{pmatrix}6\\-6\end{pmatrix}$", 4),
               (r"פתרון המערכת וקבלת $m=\frac43,\ n=-\frac13$", 4)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב $AA^T$ במקום $A^TA$ (מטריצה $4\times4$ במקום $2\times2$).",
              r"טעות סימן בחישוב המכפלה $A^T\vec b$, בעיקר ברכיבים של $-4$ ושל $-1$.",
              r"לפתור את $A\vec x=\vec b$ ישירות, אף שהמערכת אינה פתירה."],
    steps=[
        nm(r"מהו האיבר בשורה 2 ועמודה 2 של $A^TA$ (סכום ריבועי העמודה השנייה של $A$)?", 42,
           r"$(-2)^2+2^2+3^2+5^2=4+4+9+25=42$."),
        nm(r"מהו הרכיב השני של $A^T\vec b$?", -6,
           r"$-2\cdot3+2\cdot1+3\cdot(-4)+5\cdot2=-6+2-12+10=-6$."),
        nm(r"פתרו את המערכת הנורמלית. מהו $n$?", -1 / 3,
           r"מהמשוואות $m+n=1$ ו-$m+7n=-1$ מקבלים $6n=-2$, כלומר $n=-\frac13$.", 0.002),
        nm(r"מהו $m$?", 4 / 3, r"$m=1-n=\frac43$.", 0.002),
    ],
    stepsSource="ai-verified")

add(1, "ב",
    rubric=rub((r"בחירת הוקטורים $\vec u,\vec v$ (השורשים של $\ln k$ בסדר ישר והפוך)", 4),
               (r"חישוב $\vec u\cdot\vec v$ וזיהויו עם הסכום הנתון", 2),
               (r"חישוב $\|\vec u\|^2=\|\vec v\|^2=\ln(n!)$", 2),
               (r"הצבה באי-שוויון קושי-שוורץ וקבלת הטענה", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לבחור את $\vec v$ באותו סדר כמו $\vec u$: אז המכפלה הפנימית היא $\sum\ln k$ ולא הסכום הנתון.",
              r"לשכוח שהנורמה בריבוע של $\vec u$ היא סכום של $\ln k$, ולהסיק $\ln(n!)$ רק מ-$\ln1+\dots+\ln n$.",
              r"להפעיל קושי-שוורץ בלי לעבור לשורשים, ולא לקבל את הביטוי $\sqrt{\ln k\cdot\ln(n-k+1)}$."],
    steps=[
        ch(r"איזה זוג וקטורים מקיים שהמכפלה הפנימית $\vec u\cdot\vec v$ שווה לסכום $\sum_{k=1}^{n}\sqrt{\ln k\cdot\ln(n-k+1)}$?",
           r"$\vec u=\left(\sqrt{\ln k}\right)_{k=1}^n$ ו-$\vec v=\left(\sqrt{\ln(n-k+1)}\right)_{k=1}^n$ (אותו וקטור בסדר הפוך)",
           [r"$\vec u=\left(\sqrt{\ln k}\right)_{k=1}^n$ ו-$\vec v=\vec u$",
            r"$\vec u=\left(\ln k\right)_{k=1}^n$ ו-$\vec v=\left(\ln(n-k+1)\right)_{k=1}^n$",
            r"$\vec u=\left(\sqrt{\ln k}\right)_{k=1}^n$ ו-$\vec v=(1,1,\dots,1)$"],
           r"רק הזוג שבו $\vec v$ הוא אותו וקטור בסדר הפוך נותן בכל מקום $k$ את $\sqrt{\ln k}\cdot\sqrt{\ln(n-k+1)}$. הזוג עם $\vec v=\vec u$ נותן $\sum\ln k$, הזוג של $\ln k$ ו-$\ln(n-k+1)$ בלי שורשים נותן $\sum\ln k\cdot\ln(n-k+1)$ בלי שורש, והזוג עם וקטור האחדות נותן $\sum\sqrt{\ln k}$.", 1),
        nm(r"עבור $n=3$, מהו הסכום $\sum_{k=1}^{3}\sqrt{\ln k\cdot\ln(4-k)}$?", 0.693147,
           r"האיבר הראשון והשלישי מכילים $\ln1=0$, והאמצעי הוא $\sqrt{\ln2\cdot\ln2}=\ln2\approx0.693$."),
        nm(r"עבור $n=3$, מהו $\|\vec u\|^2=\ln1+\ln2+\ln3$?", 1.791759,
           r"$\ln(1\cdot2\cdot3)=\ln6\approx1.792$, כלומר $\ln(n!)$."),
        {"type": "findbug", "prompt": "בהוכחה הבאה שורה אחת שונתה כך שהיא שגויה. מצאו אותה.",
         "lines": [r"נבחר $\vec u=\left(\sqrt{\ln1},\dots,\sqrt{\ln n}\right)$ ו-$\vec v=\left(\sqrt{\ln n},\dots,\sqrt{\ln1}\right)$.",
                   r"$\vec u\cdot\vec v=\sum_{k=1}^n\sqrt{\ln k\cdot\ln(n-k+1)}$.",
                   r"$\|\vec u\|^2=\|\vec v\|^2=\ln1+\ln2+\dots+\ln n=\ln(n!)$.",
                   r"לפי קושי-שוורץ $|\vec u\cdot\vec v|\ge\|\vec u\|\cdot\|\vec v\|$.",
                   r"לכן $\sum_{k=1}^n\sqrt{\ln k\cdot\ln(n-k+1)}\le\ln(n!)$."],
         "bugIndex": 3,
         "explain": r"קושי-שוורץ הוא $|\vec u\cdot\vec v|\le\|\vec u\|\cdot\|\vec v\|$ ולא $\ge$; עם $\ge$ אי אפשר להגיע לטענה."},
    ],
    stepsSource="ai-verified")

add(2, "א",
    rubric=rub((r"גרם-שמידט: $e_1=\frac1{\sqrt2}$ מחישוב $\|1\|^2=2$", 3),
               (r"$e_2=\sqrt6\left(|x|-\frac12\right)$ מחישוב ההיטל על $e_1$ והנורמה $\frac1{\sqrt6}$", 5),
               (r"נוסחת ההיטל $\mathrm{Proj}_W(x^2)=\sum\langle x^2,e_i\rangle e_i$", 3),
               (r"חישוב האינטגרלים וקבלת $|x|-\frac16$", 4)),
    rubricSource="ai-verified",
    pitfalls=[r"להשתמש ב-$1$ וב-$|x|$ כאילו הם אורתוגונליים: $\langle1,|x|\rangle=1\ne0$.",
              r"לחשב את האינטגרל של $|x|$ בלי לפצל ל-$[-1,0]$ ול-$[0,1]$ ולקבל $0$ במקום $1$.",
              r"לשכוח לנרמל את $e_2$, כלומר להשתמש בנוסחת ההיטל בלי חלוקה בנורמה בריבוע."],
    steps=[
        nm(r"מהו $\|1\|^2=\int_{-1}^{1}1\,dx$ במכפלה הנתונה?", 2, r"האינטגרל של $1$ על קטע באורך $2$ הוא $2$.", 0),
        nm(r"מהו $\dfrac{\langle|x|,1\rangle}{\|1\|^2}$, כלומר המקדם שמחסירים מ-$|x|$ בגרם-שמידט?", 0.5,
           r"$\int_{-1}^{1}|x|\,dx=1$, וחילוק ב-$2$ נותן $\frac12$."),
        nm(r"מהו $\left\||x|-\frac12\right\|^2=\int_{-1}^{1}\left(|x|-\frac12\right)^2dx$?", 1 / 6,
           r"$2\int_0^1\left(x-\frac12\right)^2dx=2\cdot\frac1{12}=\frac16$.", 0.0005),
        nm(r"ההיטל הוא $|x|+c$ עבור קבוע $c$. מהו $c$?", -1 / 6,
           r"ההיטל הוא $\frac13+6\cdot\frac16\left(|x|-\frac12\right)=|x|-\frac16$.", 0.0005),
    ],
    stepsSource="ai-verified")

add(2, "ב",
    rubric=rub((r"מספר האפשרויות ל-$c$: כל איבר של $\mathbb{Z}_5$, כלומר $5$", 3),
               (r"מספר הזוגות $(a,b)$ עם $ab\ne0$: מורידים את אלו עם $a=0$ או $b=0$, ונשארים עם $4\cdot4=16$", 5),
               (r"עקרון הכפל: $|H|=5\cdot16=80$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לדרוש גם $c\ne0$, אף שהתנאי הוא רק $ab\ne0$.",
              r"לספור $5\cdot5\cdot5=125$ ולשכוח את התנאי $ab\ne0$.",
              r"להחסיר רק את הזוגות עם $a=0$ ולשכוח את אלו עם $b=0$."],
    steps=[
        nm(r"כמה ערכים אפשריים יש ל-$c\in\mathbb{Z}_5$?", 5, r"אין תנאי על $c$, ולכן כל $5$ הערכים $0,1,2,3,4$ מותרים.", 0),
        nm(r"כמה זוגות $(a,b)\in\mathbb{Z}_5^2$ מקיימים $ab\ne0$?", 16,
           r"ב-$\mathbb{Z}_5$ המכפלה מתאפסת רק כש-$a=0$ או $b=0$, ולכן $a,b\in\{1,2,3,4\}$: $4\cdot4=16$.", 0),
        nm(r"מהו $|H|$?", 80, r"$5\cdot16=80$.", 0),
    ],
    stepsSource="ai-verified")

add(3, "א",
    rubric=rub((r"פולינום אופייני $(x-2)^2(x-5)$ והערכים העצמיים $5,2,2$", 5),
               (r"וקטור עצמי $(1,1,1)$ עבור $\lambda=5$", 3),
               (r"שני וקטורים עצמיים אורתוגונליים עבור $\lambda=2$: $(-1,1,0)$ ו-$(1,1,-2)$", 5),
               (r"נרמול הוקטורים", 2),
               (r"כתיבת $P$ אורתוגונלית ו-$D$ אלכסונית עם $A=PDP^{-1}$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לבחור שני וקטורים עצמיים של $\lambda=2$ שאינם ניצבים זה לזה, ואז $P$ אינה אורתוגונלית.",
              "לשכוח לנרמל את העמודות של $P$.",
              r"לרשום את $D$ בסדר שאינו תואם את סדר העמודות של $P$."],
    steps=[
        nm(r"מהו $\det A$ (המכפלה של הערכים העצמיים)?", 20, r"הערכים העצמיים הם $5,2,2$ והמכפלה שלהם היא $20$.", 0),
        nm(r"מהו הערך העצמי של הוקטור $(1,1,1)$? (סכום כל שורה של $A$ הוא $5$)", 5,
           r"$A(1,1,1)^T=(5,5,5)^T$.", 0),
        nm(r"מהו המימד של המרחב העצמי של $\lambda=2$?", 2,
           r"לכל שורות $A-2I$ אותה שורה $(1,1,1)$, לכן דרגתה $1$ והגרעין שלה ממימד $2$.", 0),
        nm(r"מצאנו $(-1,1,0)$. הוקטור $(1,1,z)$ שייך למרחב העצמי של $\lambda=2$ (סכום הרכיבים $0$) וניצב לו. מהו $z$?", -2,
           r"$1+1+z=0$ נותן $z=-2$, והמכפלה הפנימית $-1+1+0=0$.", 0),
    ],
    stepsSource="ai-verified")

add(3, "ב",
    rubric=rub((r"מעבר ל-$\frac14\left(\langle u+v,u+v\rangle-\langle u-v,u-v\rangle\right)$", 2),
               (r"פתיחה לפי בילינאריות וסימטריה של שני הביטויים", 3),
               (r"חיסור וחילוק ב-$4$ וקבלת $\langle u,v\rangle$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להשתמש בסימטריה $\langle u,v\rangle=\langle v,u\rangle$ בלי לציין שהמרחב ממשי.",
              r"טעות סימן בפתיחת $\|u-v\|^2$ (המכפלה המעורבת היא $-2\langle u,v\rangle$).",
              "לחלק ב-$2$ במקום ב-$4$ בסוף."],
    steps=[
        ch(r"באיזו תכונה משתמשים כדי לאחד את $\langle u,v\rangle+\langle v,u\rangle$ ל-$2\langle u,v\rangle$?",
           r"סימטריה של המכפלה הפנימית הממשית: $\langle u,v\rangle=\langle v,u\rangle$",
           [r"חיוביות: $\langle u,u\rangle>0$ עבור $u\ne0$", r"אי-שוויון קושי-שוורץ", r"אי-שוויון המשולש"],
           r"רק הסימטריה מאפשרת להחליף את סדר הוקטורים. שלוש האחרות הן תכונת חיוביות ושני אי-שוויונות, ואינן נותנות שוויון בין שני הביטויים.", 2),
        {"type": "order", "prompt": "סדרו את שלבי ההוכחה.",
         "lines": [r"$\|u\pm v\|^2=\langle u\pm v,u\pm v\rangle$, ולכן אגף ימין הוא $\frac14\left(\langle u+v,u+v\rangle-\langle u-v,u-v\rangle\right)$.",
                   r"פותחים את שתי המכפלות לפי בילינאריות וסימטריה: $\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle$ ו-$\langle u,u\rangle-2\langle u,v\rangle+\langle v,v\rangle$.",
                   r"מחסרים: נשאר $4\langle u,v\rangle$ ואיברי $\langle u,u\rangle,\langle v,v\rangle$ מצטמצמים.",
                   r"מחלקים ב-$4$ ומקבלים $\langle u,v\rangle$, כנדרש."],
         "explain": "כל שלב נשען על הקודם: קודם מזהים נורמה כמכפלה פנימית, אחר כך פותחים, מחסרים ומחלקים."},
        nm(r"בדקו על $u=(1,2)$ ו-$v=(3,-1)$ במכפלה הפנימית הרגילה: מהו $\frac14\left(\|u+v\|^2-\|u-v\|^2\right)$?", 1,
           r"$\|(4,1)\|^2=17$ ו-$\|(-2,3)\|^2=13$, ו-$\frac14(17-13)=1=1\cdot3+2\cdot(-1)$.", 0),
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"$\|u+v\|^2=\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle$.",
                   r"$\|u-v\|^2=\langle u,u\rangle-2\langle u,v\rangle+\langle v,v\rangle$.",
                   r"$\|u+v\|^2-\|u-v\|^2=2\langle u,v\rangle$.",
                   r"לכן $\frac14\left(\|u+v\|^2-\|u-v\|^2\right)=\langle u,v\rangle$."],
         "bugIndex": 2,
         "explain": r"ההפרש הוא $\left(2\langle u,v\rangle\right)-\left(-2\langle u,v\rangle\right)=4\langle u,v\rangle$, ולא $2\langle u,v\rangle$."},
    ],
    stepsSource="ai-verified")

add(4, "א",
    rubric=rub((r"חישוב $c*b=\left((a*b)*a\right)*b=(a*b)*(a*b)$ באסוציאטיביות", 5),
               (r"שימוש בתכונה $x*x=e$ עבור $x=a*b$ וקבלת $c*b=e$", 3),
               (r"$c=c*e=c*(c*b)=(c*c)*b$ באסוציאטיביות", 4),
               (r"$(c*c)*b=e*b=b$ ולכן $c=b$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"להניח שהפעולה קומוטטיבית; היא לא נתונה, ולכן אסור להחליף את הסדר של $a$ ו-$b$.",
              r"להפעיל את $x*x=e$ על איברים שאינם זהים, ולא לזהות שב-$(a*b)*(a*b)$ מתקיים $x=a*b$.",
              r"לשכוח את השלב $c=c*e$ שמאפשר להציב $e=c*b$."],
    steps=[
        ch(r"אילו שני איברים זהים ב-$c*b=\left((a*b)*a\right)*b$, אחרי שינוי הסוגריים באסוציאטיביות, כך שאפשר להפעיל את התכונה $x*x=e$?",
           r"$a*b$ ו-$a*b$", [r"$a$ ו-$a$", r"$b$ ו-$b$", r"$c$ ו-$c$"],
           r"$\left((a*b)*a\right)*b=(a*b)*(a*b)$, כלומר $x*x$ עבור $x=a*b$. בשאר האפשרויות אין שני גורמים צמודים זהים.", 3),
        {"type": "order", "prompt": r"סדרו את שלבי ההוכחה ש-$c=b$.",
         "lines": [r"$c*b=\left((a*b)*a\right)*b=(a*b)*(a*b)$, באסוציאטיביות.",
                   r"$(a*b)*(a*b)=e$, כי $x*x=e$ לכל $x$. לכן $c*b=e$.",
                   r"$c=c*e=c*(c*b)$, לפי הנטרלי והשלב הקודם.",
                   r"$c*(c*b)=(c*c)*b=e*b=b$, באסוציאטיביות, בתכונה $x*x=e$ ובנטרלי."],
         "explain": r"השלב השני נשען על הראשון, השלישי על השני (הצבת $e=c*b$), והרביעי על השלישי."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"$c*b=\left((a*b)*a\right)*b=(a*b)*(a*b)$.",
                   r"$(a*b)*(a*b)=a*b$, לפי התכונה $x*x=e$.",
                   r"$c=c*e=c*(c*b)$.",
                   r"$c*(c*b)=(c*c)*b=e*b=b$."],
         "bugIndex": 1,
         "explain": r"התכונה היא $x*x=e$ ולא $x*x=x$; המשוואה $x*x=x$ מתקיימת רק עבור $x=e$."},
    ],
    stepsSource="ai-verified")

add(4, "ב",
    rubric=rub((r"פתיחה: $\vec x^TB\vec x=4a^2+10ab+6b^2$", 3),
               (r"הוצאת $2b^2$ ומעבר לאי-שוויון $2t^2+5t+3<0$ עם $t=\frac ab$", 3),
               (r"פתרון: $-1.5<t<-1$", 2),
               (r"בחירת $a,b$ מתאימים (למשל $-5,4$) ובדיקה שהערך שלילי", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להסיק ש-$B$ חיובית מכך שהאלכסון חיובי: ל-$B$ דטרמיננטה $-1$, ולכן יש לה ערך עצמי שלילי.",
              r"לבחור $a,b$ חיוביים, שנותנים תמיד ערך חיובי.",
              r"שגיאה בפתיחה: $\vec x^TB\vec x$ כולל את $2\cdot5ab=10ab$."],
    steps=[
        nm(r"מהו $\det B$ עבור $B=\begin{pmatrix}4&5\\5&6\end{pmatrix}$?", -1,
           r"$4\cdot6-5\cdot5=-1<0$, ולכן $B$ אינה מוגדרת חיובית וקיים $\vec x$ כנדרש.", 0),
        nm(r"עבור $2t^2+5t+3<0$, מהו השורש הקטן יותר של $2t^2+5t+3$?", -1.5,
           r"השורשים הם $t=\frac{-5\pm1}{4}$, כלומר $-1.5$ ו-$-1$.", 0),
        ch(r"עבור אילו ערכי $t=\frac ab$ מתקיים $2t^2+5t+3<0$?", r"$-1.5<t<-1$",
           [r"$t<-1.5$ או $t>-1$", r"$t>0$", r"$-1<t<1.5$"],
           r"פרבולה פתוחה כלפי מעלה שלילית בין שורשיה, ולכן בקטע בין $-1.5$ ל-$-1$. בשאר הקטעים הערך אי-שלילי.", 0),
        nm(r"עבור $a=-5,\ b=4$, מהו $4a^2+10ab+6b^2$?", -4, r"$100-200+96=-4$.", 0),
    ],
    stepsSource="ai-verified")

add(5, "א",
    rubric=rub((r"חישוב $W=AA^T$ וערכיו העצמיים $25,1,0$", 4),
               (r"הערכים הסינגולריים $\sigma_1=5,\ \sigma_2=1$ וכתיבת $\Sigma$", 3),
               (r"עמודות $U$: הוקטורים העצמיים המנורמלים של $AA^T$", 4),
               (r"עמודות $V$ לפי $\vec v_i=\frac1{\sigma_i}A^T\vec u_i$", 4),
               (r"כתיבת התוצאה $A=U\Sigma V^T$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"להשתמש ב-$A^TA$ כדי למצוא את $U$; המימדים של $U$ ($3\times3$) מתאימים רק ל-$AA^T$.",
              "לרשום את הערכים העצמיים במקום הערכים הסינגולריים, כלומר לשכוח את השורש.",
              r"לבחור סימנים שרירותיים ל-$\vec v_i$ במקום לחשב אותם מ-$\vec u_i$, ואז $A\ne U\Sigma V^T$."],
    steps=[
        ch(r"מהי המטריצה שהוקטורים העצמיים המנורמלים שלה הם העמודות של $U$ (מטריצה $3\times3$)?",
           r"$AA^T$", [r"$A^TA$", r"$A+A^T$", r"$A^{-1}$"],
           r"$AA^T$ היא $3\times3$ כמו $U$. $A^TA$ היא $2\times2$ (נותנת את $V$), ואילו ל-$A+A^T$ ול-$A^{-1}$ אין משמעות כי $A$ אינה ריבועית.", 0),
        nm(r"מהו הערך העצמי הגדול ביותר של $AA^T$?", 25,
           r"$A^TA=\begin{pmatrix}1&0\\0&25\end{pmatrix}$ ול-$AA^T$ אותם ערכים עצמיים השונים מאפס: $25,1$.", 0),
        nm(r"מהו הערך הסינגולרי השני $\sigma_2$?", 1, r"$\sigma_2=\sqrt1=1$.", 0),
        nm(r"נתון $\vec v_1=\begin{pmatrix}0\\1\end{pmatrix}$. מהו הרכיב השלישי של $\vec u_1=\frac1{\sigma_1}A\vec v_1$?", 0.8,
           r"$A\vec v_1=(0,3,4)^T$ ולכן $\vec u_1=\frac15(0,3,4)^T=(0,0.6,0.8)^T$.", 0.0005),
    ],
    stepsSource="ai-verified")

add(5, "ב",
    rubric=rub((r"סימון $m=140$ וחישוב $M_1=28,\ M_2=20,\ M_3=35$", 2),
               (r"חישוב ההופכיים $x_1=2,\ x_2=6,\ x_3=3$", 3),
               (r"הצבה בנוסחה והקטנה מודולו $140$: $x\equiv94$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב את ההופכי $x_i$ מודולו $m$ ולא מודולו $m_i$.",
              r"טעות בחישוב $M_i$, כך ש-$M_ix_i$ אינו $1$ מודולו $m_i$.",
              "לשכוח להקטין את הסכום $794$ מודולו $140$."],
    steps=[
        nm(r"מהו $M_1=\dfrac{m}{m_1}$ עבור $m=5\cdot7\cdot4=140$ ו-$m_1=5$?", 28, r"$140/5=28$.", 0),
        nm(r"מהו $x_1$ שמקיים $28x_1\equiv1\pmod 5$ (בטווח $0$ עד $4$)?", 2, r"$28\equiv3\pmod5$ ו-$3\cdot2=6\equiv1$.", 0),
        nm(r"מהו $x_2$ שמקיים $20x_2\equiv1\pmod 7$ (בטווח $0$ עד $6$)?", 6, r"$20\equiv6\pmod7$ ו-$6\cdot6=36\equiv1$.", 0),
        nm(r"מהו הפתרון $x$ בטווח $0$ עד $139$?", 94,
           r"$4\cdot28\cdot2+3\cdot20\cdot6+2\cdot35\cdot3=224+360+210=794\equiv94\pmod{140}$.", 0),
    ],
    stepsSource="ai-verified")

exam = {
    "examCode": "23A-B",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ״ג מועד ב'",
    "year": 2023,
    "examDate": "1.3.2023",
    "sourceFile": "algebra-2-23A-B-exam",
    "solutionFile": "algebra-2-23A-B-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
