# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-A.json -- algebra-2 (20079), semester B 2023, moed A (20.06.2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23B-A.py

Source: this sitting exists only inside the 275-page compilation (pp. 182-197). The pages are the SOLUTION version
of the exam ("פתרון מבחן"): each question is printed followed by its typed official solution, with a grader's red
point marks. The second copy (pp. 191-197) is identical. The exam header (without solution) is not a separate page.
5 printed questions (solve 4 of 5, 25% each); 11 items (Q2 has three), all 11 shipped (Q5a with a typo correction).

Part letters: Q2 items 1,2 of part A -> parts a, b; part B -> c.  Q1, Q3, Q4, Q5 keep printed parts a, b.
Every question text starts with its printed label.

Checked with tools/verify/23B-A/check.py (sympy):
Q5a (FINAL ANSWER typo): the official prints Proj_W = (a+b)/3 * (-1 1; 1 0) + (5b-3a)/51 * (4 -1; 5 3),
  but <(0 a; b 0), (4 -1; 5 3)> = 5b - a (not 5b - 3a). The correct projection is
  [[-7a+b, 6a+4b], [4a+14b, -a+5b]] / 17 (re-derived by the solver: tools/verify/23B-A/solve_Q5a.py). Per the typo
  ruling: solutionSource "solved", official false, prefix "הפתרון הרשמי עם תיקון". Logged in docs/ASK_ADIR.md.
Notes (no change to any answer):
- Q3a: "positive definite" in the official is the course's term for positive SEMIdefinite (|a| <= 1/2).
- Q4a is a pasted calculator output (U, Sigma, V); transcribed as the same matrices (A = U Sigma V^T verified).
- Q4b: the official's last value 918 (mod 280) is not reduced; 918 = 78 (mod 280). Reduction added.
- The red numbers in the source are the grader's point marks (right margin), not part of the solution; they are not
  transcribed (no rubric is built here).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ------------------------------------------------------------------ contexts
CTX = {
    "c2a": {"kind": "text", "title": "שאלה 2 סעיף א",
            "text": r"נסתכל בחבורה $G=\left\{\begin{pmatrix}a&b\\0&c\end{pmatrix}\in M_2(\mathbb{Z}_3)\ \middle|\ a\cdot c\ne0\pmod 3\right\}$ ביחס לכפל (חבורת המטריצות ההפיכות מסדר $2\times2$ עם רכיבים מ-$\mathbb{Z}_3$). תהי $H=\left\{\begin{pmatrix}2&1\\0&2\end{pmatrix}^n\ \middle|\ n\in\mathbb{Z}\right\}$ תת-חבורה ציקלית של $G$. (הכפל והחיבור של רכיבי המטריצות הם מודולו 3)"},
    "c5a": {"kind": "text", "title": "שאלה 5 סעיף א",
            "text": r"במרחב וקטורי $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע״י $\langle A,B\rangle=tr\left(B^TA\right)$ לכל $A,B\in M_2(\mathbb{R})$."},
    "c5b": {"kind": "text", "title": "שאלה 5 סעיף ב",
            "text": r"תהי $(G,*)$ חבורה כך שלכל $x\in G$ מתקיים $x^{-1}=x$, כלומר $x*x=e$. יהיו $a,b\in G$."},
}

# ------------------------------------------------------------------ solutions
S1A = (
    r"נחפש את המודל הליניארי מהצורה $y=mx+n$ לפי שיטת הריבועים הפחותים:" "\n"
    r"$$\begin{pmatrix}-2&1\\-1&1\\0&1\\2&1\\6&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}\approx\begin{pmatrix}4\\0\\0\\2\\8\end{pmatrix}\ \mapsto\ \begin{pmatrix}-2&-1&0&2&6\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}-2&1\\-1&1\\0&1\\2&1\\6&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}-2&-1&0&2&6\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}4\\0\\0\\2\\8\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\ \begin{pmatrix}45&5\\5&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}44\\14\end{pmatrix}\ \Rightarrow\ m=0.75,\ \ n=2.05$$" "\n"
    r"נציב ונקבל: $y=0.75x+2.05$."
)

S1B = (
    r"נגדיר $\vec u=\begin{pmatrix}\sqrt2\\\sqrt4\\\vdots\\\sqrt{2n}\end{pmatrix}$ , $\vec v=\begin{pmatrix}\sqrt{\ln1}\\\sqrt{\ln2}\\\vdots\\\sqrt{\ln n}\end{pmatrix}$, שני וקטורים ב-$\mathbb{R}^n$, וניעזר באי-שוויון קושי-שוורץ:" "\n"
    r"$$\left|\langle\vec u,\vec v\rangle\right|=\sum_{k=1}^{n}\sqrt{2k\cdot\ln k}$$" "\n"
    r"$$\|\vec u\|=\sqrt{\sum_{k=1}^n2k}=\sqrt{2\sum_{k=1}^nk}=\sqrt{n(n+1)}$$" "\n"
    r"$$\|\vec v\|=\sqrt{\sum_{k=1}^n\ln k}=\sqrt{\ln1+\ln2+\dots+\ln n}=\sqrt{\ln(n!)}$$" "\n"
    r"מכאן נובעת התוצאה: $\displaystyle\sum_{k=1}^{n}\sqrt{2k\cdot\ln k}\ \le\ \sqrt{n\cdot(n+1)\cdot\ln(n!)}$."
)

S2A1 = (
    r"התנאי $a\cdot c\ne0\pmod 3$ מתקיים אם ורק אם $a\ne0\pmod 3\ \wedge\ c\ne0\pmod 3$. לכן $\begin{pmatrix}a&b\\0&c\end{pmatrix}\in G$ כאשר $a=1,2\pmod 3$ (2 אפשרויות), $c=1,2\pmod 3$ (2 אפשרויות) ו-$b=0,1,2\pmod 3$ (3 אפשרויות). לפי עקרון הכפל: $|G|=2\cdot2\cdot3=12$."
)

S2A2 = (
    r"הסדר של תת החבורה $H$ שווה לסדר האיבר $\begin{pmatrix}2&1\\0&2\end{pmatrix}$. כלומר $|H|=o\left(\begin{pmatrix}2&1\\0&2\end{pmatrix}\right)$. מתקיים:" "\n"
    r"$$\begin{pmatrix}2&1\\0&2\end{pmatrix}^2=\begin{pmatrix}2&1\\0&2\end{pmatrix}\cdot\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}1&1\\0&1\end{pmatrix}\pmod 3$$" "\n"
    r"$$\begin{pmatrix}2&1\\0&2\end{pmatrix}^3=\begin{pmatrix}1&1\\0&1\end{pmatrix}\cdot\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}2&0\\0&2\end{pmatrix}\pmod 3$$" "\n"
    r"$$\begin{pmatrix}2&1\\0&2\end{pmatrix}^4=\begin{pmatrix}2&0\\0&2\end{pmatrix}\cdot\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}1&2\\0&1\end{pmatrix}\pmod 3$$" "\n"
    r"$$\begin{pmatrix}2&1\\0&2\end{pmatrix}^5=\begin{pmatrix}1&2\\0&1\end{pmatrix}\cdot\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}2&2\\0&2\end{pmatrix}\pmod 3$$" "\n"
    r"$$\begin{pmatrix}2&1\\0&2\end{pmatrix}^6=\begin{pmatrix}2&2\\0&2\end{pmatrix}\cdot\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod 3$$" "\n"
    r"לכן $|H|=6$."
)

S2B = (
    r"יהי $\vec v\in\mathbb{R}^n$ כאשר $n$ הוא סדר המטריצה $A$. מתקיים:" "\n"
    r"$$\langle(I+A)\vec v,\vec v\rangle=\vec v^T(I+A)\vec v=\vec v^TI\vec v+\vec v^TA\vec v=\vec v^T\vec v+\vec v^TA\vec v=\|\vec v\|^2+\langle A\vec v,\vec v\rangle\ge0$$" "\n"
    r"לכן $I+A$ מוגדרת חיובית." "\n"
    r"באופן דומה:" "\n"
    r"$$\langle A^2\vec v,\vec v\rangle=\vec v^TA^2\vec v=\vec v^TA^TA\vec v=(A\vec v)^TA\vec v=\|A\vec v\|^2\ge0$$" "\n"
    r"זאת אומרת ש-$A^2$ מוגדרת חיובית." "\n"
    r"**הערה:** בקורס מוגדרת חיובית היא מטריצה סימטרית. הפתרון הרשמי בודק רק את התנאי $\vec v^TM\vec v\ge0$; הסימטריה נובעת מ-$A=A^T$: $(I+A)^T=I+A^T=I+A$ וגם $(A^2)^T=A^TA^T=A^2$."
)

S3A = (
    r"נחשב את הערכים העצמיים של המטריצה:" "\n"
    r"$$\begin{vmatrix}1-\lambda&0&2a\\0&4-a^2-\lambda&0\\2a&0&1-\lambda\end{vmatrix}=\left(4-a^2-\lambda\right)\begin{vmatrix}1-\lambda&2a\\2a&1-\lambda\end{vmatrix}=\left(4-a^2-\lambda\right)\left(\lambda^2-2\lambda+1-4a^2\right)$$" "\n"
    r"לכן הערכים העצמיים הם: $\lambda=4-a^2$ , $\lambda=1+2a$ , $\lambda=1-2a$." "\n"
    r"המטריצה **מוגדרת חיובית** כאשר" "\n"
    r"$$\begin{cases}4-a^2\ge0\\1+2a\ge0\\1-2a\ge0\end{cases}\ \Rightarrow\ \begin{cases}-2\le a\le2\\a\ge-0.5\\a\le0.5\end{cases}\ \Rightarrow\ -0.5\le a\le0.5$$" "\n"
    r"המטריצה **מוגדרת חיובית לחלוטין** כאשר $-0.5<a<0.5$." "\n"
    r"המטריצה **מוגדרת שלילית** כאשר" "\n"
    r"$$\begin{cases}4-a^2\le0\\1+2a\le0\\1-2a\le0\end{cases}\ \Rightarrow\ \begin{cases}a\le-2\ \vee\ a\ge2\\a\le-0.5\\a\ge0.5\end{cases}$$" "\n"
    r"כלומר **אין** ערכי $a$ עבורם המטריצה מוגדרת שלילית, בפרט שלילית לחלוטין."
)

S3B = (
    r"**כיוון ראשון:** נניח כי $\|\vec u\|=\|\vec v\|$. אזי" "\n"
    r"$$\|\alpha\vec u+\beta\vec v\|^2=\langle\alpha\vec u+\beta\vec v,\ \alpha\vec u+\beta\vec v\rangle=\alpha^2\|\vec u\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec v\|^2$$" "\n"
    r"$$=\alpha^2\|\vec v\|^2+2\langle\beta\vec u,\alpha\vec v\rangle+\beta^2\|\vec u\|^2=\|\beta\vec u+\alpha\vec v\|^2$$" "\n"
    r"ולכן $\|\alpha\vec u+\beta\vec v\|=\|\beta\vec u+\alpha\vec v\|$." "\n"
    r"**כיוון שני:** נניח כי $\|\alpha\vec u+\beta\vec v\|=\|\beta\vec u+\alpha\vec v\|$ לכל $\alpha,\beta\in\mathbb{R}$. אזי" "\n"
    r"$$\|\alpha\vec u+\beta\vec v\|^2=\langle\alpha\vec u+\beta\vec v,\ \alpha\vec u+\beta\vec v\rangle=\alpha^2\|\vec u\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec v\|^2$$" "\n"
    r"$$\|\beta\vec u+\alpha\vec v\|^2=\langle\beta\vec u+\alpha\vec v,\ \beta\vec u+\alpha\vec v\rangle=\alpha^2\|\vec v\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec u\|^2$$" "\n"
    "ולכן\n"
    r"$$\alpha^2\|\vec u\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec v\|^2=\alpha^2\|\vec v\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec u\|^2$$" "\n"
    r"$$\alpha^2\|\vec u\|^2+\beta^2\|\vec v\|^2=\alpha^2\|\vec v\|^2+\beta^2\|\vec u\|^2$$" "\n"
    r"$$\alpha^2\left(\|\vec u\|^2-\|\vec v\|^2\right)=\beta^2\left(\|\vec u\|^2-\|\vec v\|^2\right)$$" "\n"
    r"השוויון מתקיים לכל $\alpha,\beta\in\mathbb{R}$, לכן $\|\vec u\|=\|\vec v\|$."
)

S4A = (
    r"נמצא את פירוק ה-$SVD$ של $A=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}$." "\n"
    r"$$A^T=\begin{pmatrix}1&2\\0&0\\2&1\end{pmatrix},\qquad Y=A^TA=\begin{pmatrix}5&0&4\\0&0&0\\4&0&5\end{pmatrix}$$" "\n"
    r"ערכים עצמיים ווקטורים עצמיים של $Y$:" "\n"
    r"$$\lambda=9:\ \begin{pmatrix}1\\0\\1\end{pmatrix},\qquad\lambda=1:\ \begin{pmatrix}-1\\0\\1\end{pmatrix},\qquad\lambda=0:\ \begin{pmatrix}0\\1\\0\end{pmatrix}$$" "\n"
    r"הערכים הסינגולריים (שורשי הערכים העצמיים השונים מאפס): $\sigma_1=3,\ \sigma_2=1$." "\n"
    r"$$U=\begin{pmatrix}\frac{\sqrt2}2&\frac{\sqrt2}2\\\frac{\sqrt2}2&-\frac{\sqrt2}2\end{pmatrix},\qquad V=\begin{pmatrix}\frac{\sqrt2}2&-\frac{\sqrt2}2&0\\0&0&1\\\frac{\sqrt2}2&\frac{\sqrt2}2&0\end{pmatrix},\qquad\Sigma=\begin{pmatrix}3&0&0\\0&1&0\end{pmatrix}$$" "\n"
    r"כלומר $A=U\Sigma V^T$."
)

S4B = (
    r"נסמן: $a_1=3,\ a_2=1,\ a_3=6$ ($a_i$ הן השאריות הנתונות) והמודולים $m_1=5,\ m_2=7,\ m_3=8$ הם אכן זרים בזוגות. כמו כן נסמן: $m=m_1m_2m_3=5\cdot7\cdot8=280$, ולכן: $M_1=56,\ M_2=40,\ M_3=35$." "\n"
    "הפתרון למערכת הוא:\n"
    r"$$x=\left(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3\right)\pmod m=\left(3\cdot56\cdot x_1+1\cdot40\cdot x_2+6\cdot35\cdot x_3\right)\pmod{280}$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$56x_1\equiv1\pmod 5\ \Rightarrow\ x_1\equiv1\pmod 5\ \Rightarrow\ x_1=1$$" "\n"
    r"$$40x_2\equiv1\pmod 7\ \Rightarrow\ 5x_2\equiv1\pmod 7\ \Rightarrow\ x_2=3$$" "\n"
    r"$$35x_3\equiv1\pmod 8\ \Rightarrow\ 3x_3\equiv1\pmod 8\ \Rightarrow\ x_3=3$$" "\n"
    "מכאן:\n"
    r"$$x=\left(3\cdot56\cdot1+1\cdot40\cdot3+6\cdot35\cdot3\right)\pmod{280}=918\pmod{280}$$" "\n"
    r"כלומר $x\equiv78\pmod{280}$."
)

S5A = (
    r"**הפתרון הרשמי עם תיקון:** בפתרון הרשמי המקדם של $\begin{pmatrix}4&-1\\5&3\end{pmatrix}$ בתשובה הסופית מודפס כ-$\frac{5b-3a}{51}$, אבל $\left\langle\begin{pmatrix}0&a\\b&0\end{pmatrix},\begin{pmatrix}4&-1\\5&3\end{pmatrix}\right\rangle=-a+5b$, ולכן המקדם הנכון הוא $\frac{5b-a}{51}$. שאר הפתרון כפי שהודפס." "\n"
    r"קודם כל נמצא בסיס אורתוגונלי עבור $W=Sp\left\{V_1=\begin{pmatrix}-1&1\\1&0\end{pmatrix},V_2=\begin{pmatrix}1&0\\2&1\end{pmatrix}\right\}$ (גרם-שמידט):" "\n"
    r"$$U_1=V_1=\begin{pmatrix}-1&1\\1&0\end{pmatrix}$$" "\n"
    r"$$U_2=V_2-Proj_{U_1}(V_2)=\begin{pmatrix}1&0\\2&1\end{pmatrix}-\frac{\left\langle\begin{pmatrix}1&0\\2&1\end{pmatrix},\begin{pmatrix}-1&1\\1&0\end{pmatrix}\right\rangle}{\left\|\begin{pmatrix}-1&1\\1&0\end{pmatrix}\right\|^2}\begin{pmatrix}-1&1\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\2&1\end{pmatrix}-\frac13\begin{pmatrix}-1&1\\1&0\end{pmatrix}=\begin{pmatrix}\frac43&-\frac13\\\frac53&1\end{pmatrix}$$" "\n"
    r"הבסיס $\left\{\begin{pmatrix}-1&1\\1&0\end{pmatrix},\begin{pmatrix}4&-1\\5&3\end{pmatrix}\right\}$ הוא בסיס אורתוגונלי ב-$W$. כעת ניתן לחשב את ההיטל המבוקש:" "\n"
    r"$$\left\langle\begin{pmatrix}0&a\\b&0\end{pmatrix},\begin{pmatrix}-1&1\\1&0\end{pmatrix}\right\rangle=a+b,\qquad\left\|\begin{pmatrix}-1&1\\1&0\end{pmatrix}\right\|^2=3$$" "\n"
    r"$$\left\langle\begin{pmatrix}0&a\\b&0\end{pmatrix},\begin{pmatrix}4&-1\\5&3\end{pmatrix}\right\rangle=-a+5b,\qquad\left\|\begin{pmatrix}4&-1\\5&3\end{pmatrix}\right\|^2=16+1+25+9=51$$" "\n"
    r"$$Proj_W\begin{pmatrix}0&a\\b&0\end{pmatrix}=\frac{a+b}{3}\begin{pmatrix}-1&1\\1&0\end{pmatrix}+\frac{5b-a}{51}\begin{pmatrix}4&-1\\5&3\end{pmatrix}=\frac1{17}\begin{pmatrix}-7a+b&6a+4b\\4a+14b&-a+5b\end{pmatrix}$$"
)

S5B = (
    r"נתון ש-$c=(a*b)*a$. נכפיל את השוויון ב-$b$ מצד ימין ונקבל" "\n"
    r"$$c*b=\big((a*b)*a\big)*b=(a*b)*(a*b)=e$$" "\n"
    r"כלומר $b=c^{-1}$. אבל $c^{-1}=c$, לכן $c=b$."
)

questions = [
    Q(1, "computation", "least_squares",
      r"(13%) נתונות 5 נקודות במישור $(6,8)$ , $(2,2)$ , $(0,0)$ , $(-1,0)$ , $(-2,4)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן הריבועים הפחותים.",
      S1A, part="א", points=13),
    Q(1, "proof", "cauchy_schwarz",
      r"(12%) הוכיחו כי $\displaystyle\sum_{k=1}^{n}\sqrt{2k\cdot\ln k}\ \le\ \sqrt{n\cdot(n+1)\cdot\ln(n!)}$.",
      S1B, part="ב", points=12),

    Q(2, "computation", "groups", r"סעיף א.1. מהו הסדר של $G$ ? (7%)", S2A1, part="א", points=7, contextId="c2a"),
    Q(2, "computation", "groups", r"סעיף א.2. מהו הסדר של $H$ ? (8%)", S2A2, part="ב", points=8, contextId="c2a"),
    Q(2, "proof", "pos_def",
      r"סעיף ב. תהי $A$ מטריצה מוגדרת חיובית. הוכיחו כי $I+A$ ו-$A^2$ הן גם מוגדרות חיובית. תזכורת: $A=A^T$. (10%)",
      S2B, part="ג", points=10),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}1&0&2a\\0&4-a^2&0\\2a&0&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "proof", "inner_product",
      r"(10%) יהי $V$ מרחב מכפלה פנימית ויהיו $\vec u,\vec v\in V$ שני וקטורים שונים מ-$\vec 0$. הוכיחו כי $\|\vec u\|=\|\vec v\|$ אם ורק אם $\|\alpha\cdot\vec u+\beta\cdot\vec v\|=\|\beta\cdot\vec u+\alpha\cdot\vec v\|$ לכל $\alpha,\beta\in\mathbb{R}$.",
      S3B, part="ב", points=10),

    Q(4, "computation", "svd", r"(18%) מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}$.", S4A, part="א", points=18),
    Q(4, "computation", "crt",
      r"(7%) פתרו את המערכות הבאות באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv3\pmod 5\\x\equiv1\pmod 7\\x\equiv6\pmod 8\end{cases}$.",
      S4B, part="ב", points=7),

    Q(5, "computation", "projection",
      r"(15%) חשבו את ההיטל של $\begin{pmatrix}0&a\\b&0\end{pmatrix}$ על $Sp\left\{\begin{pmatrix}-1&1\\1&0\end{pmatrix},\begin{pmatrix}1&0\\2&1\end{pmatrix}\right\}$, לכל $a,b\in\mathbb{R}$.",
      S5A, part="א", points=15, contextId="c5a", solutionSource="solved", official=False),
    Q(5, "proof", "groups", r"(10%) נסמן $c=(a*b)*a$. הוכיחו כי $c=b$.", S5B, part="ב", points=10, contextId="c5b"),
]

# ---------------------------------------------------------------------------------------------------------
# Phase 4 (step author): rubric / pitfalls / guided steps, all derived from the stored solutions above.
# Q5a steps follow the CORRECTED solution (coefficient (5b-a)/51).
# Numeric values and factual claims are re-checked by tools/verify/23B-A/steps_check.py (sympy / brute force).
IDS = "abcdef"


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def ch(prompt, right, wrongs, explain, pos=0):
    vals = list(wrongs)
    vals.insert(pos, right)
    return {"type": "choice", "prompt": prompt, "options": [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)],
            "correctId": IDS[pos], "explain": explain}


def num(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def bug(prompt, lines, i, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": i, "explain": explain}


S23BA = {
    (1, "א"): dict(
        rubric=rub((r"בניית המטריצה $X$ (עמודת $x$ ועמודת אחדות) ווקטור $\vec y$", 3),
                   (r"המשוואות הנורמליות $X^TX\binom mn=X^T\vec y$ וחישוב שני האגפים", 4),
                   (r"פתרון: $m=0.75$ , $n=2.05$", 4),
                   (r"כתיבת הישר $y=0.75x+2.05$", 2)),
        pitfalls=[r"לפתור את $X\binom mn=\vec y$ ישירות: חמש הנקודות אינן על ישר אחד.",
                  r"לשכוח שיש נקודה עם $x=-2$ וש-$\sum x_i=5$ (ולא $0$)."],
        steps=[
            num(r"מהו $\sum x_i^2$ , האיבר השמאלי-העליון ב-$X^TX$ (בנקודות $x=-2,-1,0,2,6$) ?", 45, r"$4+1+0+4+36=45$."),
            num(r"מהו $\sum x_iy_i$ , האיבר הראשון ב-$X^T\vec y$ (עם $y=4,0,0,2,8$) ?", 44, r"$-8+0+0+4+48=44$."),
            num(r"מהו השיפוע $m$ ?", 0.75, r"פתרון $\begin{pmatrix}45&5\\5&5\end{pmatrix}\binom mn=\binom{44}{14}$ נותן $m=0.75$.", 0.001),
            num(r"מהו חיתוך הצירים $n$ ?", 2.05, r"מאותה מערכת $n=2.05$.", 0.001),
        ]),
    (1, "ב"): dict(
        rubric=rub((r"בחירת הווקטורים $\vec u=\left(\sqrt{2k}\right)$ ו-$\vec v=\left(\sqrt{\ln k}\right)$", 4),
                   (r"המכפלה הפנימית $\sum\sqrt{2k\ln k}$", 2),
                   (r"הנורמות $\|\vec u\|=\sqrt{n(n+1)}$ ו-$\|\vec v\|=\sqrt{\ln(n!)}$", 4),
                   (r"הפעלת קושי-שוורץ והמסקנה", 2)),
        pitfalls=[r"לשכוח ש-$\sum_{k=1}^n\ln k=\ln(n!)$.",
                  r"לשכוח ש-$\sum_{k=1}^n2k=n(n+1)$ (ולא $n^2$)."],
        steps=[
            ch(r"איזה זוג וקטורים בוחר הפתרון הרשמי, כך שהמכפלה הפנימית היא $\sum\sqrt{2k\ln k}$ ?",
               r"$\vec u=\left(\sqrt{2k}\right)$ , $\vec v=\left(\sqrt{\ln k}\right)$",
               [r"$\vec u=\left(\sqrt k\right)$ , $\vec v=\left(\sqrt{\ln k}\right)$", r"$\vec u=(2k)$ , $\vec v=(\ln k)$", r"$\vec u=\left(\sqrt{2k\ln k}\right)$ , $\vec v=(1,\dots,1)$"],
               r"רק הזוג הנבחר נותן מכפלה פנימית $\sum\sqrt{2k}\sqrt{\ln k}=\sum\sqrt{2k\ln k}$ ונורמות בריבוע $\sum2k$ ו-$\sum\ln k$. הזוג $\left(\sqrt k\right),\left(\sqrt{\ln k}\right)$ נותן מכפלה $\sum\sqrt{k\ln k}$, הזוג $(2k),(\ln k)$ נותן $\sum2k\ln k$, והזוג $\left(\sqrt{2k\ln k}\right),(1,\dots,1)$ נותן נורמה $\sum2k\ln k$ במקום $n(n+1)\ln(n!)$.", 1),
            num(r"עבור $n=4$, מהו $\|\vec u\|^2=\sum_{k=1}^42k$ ?", 20, r"$2+4+6+8=20=n(n+1)$."),
            num(r"עבור $n=4$, מהו $\|\vec v\|^2=\sum_{k=1}^4\ln k$ (עיגול עד $0.001$)?", 3.17805, r"$\ln1+\ln2+\ln3+\ln4=\ln24\approx3.178$.", 0.001),
        ]),
    (2, "א"): dict(
        rubric=rub((r"התנאי: $a\ne0$ וגם $c\ne0$ מודולו $3$", 2), (r"מספר האפשרויות: $a$ ב-$2$ , $c$ ב-$2$ , $b$ ב-$3$", 3), (r"עקרון הכפל: $|G|=12$", 2)),
        pitfalls=[r"לדרוש גם $b\ne0$: האיבר $b$ חופשי.",
                  r"לספור $3$ אפשרויות ל-$a$ ול-$c$ (כולל $0$): אז $\det=ac=0$ אפשרי."],
        steps=[
            num(r"כמה אפשרויות יש ל-$a$ (עם $a\ne0$ ב-$\mathbb{Z}_3$) ?", 2, r"$a=1,2$."),
            num(r"כמה אפשרויות יש ל-$b$ ב-$\mathbb{Z}_3$ ?", 3, r"$b=0,1,2$."),
            num(r"מהו הסדר של $G$ ?", 12, r"$2\cdot3\cdot2=12$."),
        ]),
    (2, "ב"): dict(
        rubric=rub((r"הסדר של $H$ שווה לסדר האיבר $\begin{pmatrix}2&1\\0&2\end{pmatrix}$", 2), (r"חישוב $A^2,A^3$", 2), (r"חישוב $A^4,A^5$", 2), (r"$A^6=I$ ולכן $|H|=6$", 2)),
        pitfalls=[r"לעצור ב-$A^3=2I$ ולחשוב שהסדר $3$: $2I\ne I$ מודולו $3$.",
                  r"לחשב את החזקות מעל $\mathbb{Z}$ במקום מודולו $3$."],
        steps=[
            num(r"מהו האיבר הימני-העליון ב-$A^2$ (מודולו $3$) ?", 1, r"$A^2=\begin{pmatrix}1&1\\0&1\end{pmatrix}$."),
            num(r"מהו האיבר השמאלי-העליון ב-$A^3$ (מודולו $3$) ?", 2, r"$A^3=\begin{pmatrix}2&0\\0&2\end{pmatrix}=2I\ne I$."),
            num(r"מהו האיבר הימני-העליון ב-$A^4$ (מודולו $3$) ?", 2, r"$A^4=\begin{pmatrix}1&2\\0&1\end{pmatrix}$."),
            num(r"מהו הסדר של $H$ ?", 6, r"$A^6=(2I)^2=I$ ואין חזקה קטנה יותר שווה ל-$I$."),
        ]),
    (2, "ג"): dict(
        rubric=rub((r"חישוב $\langle(I+A)\vec v,\vec v\rangle=\|\vec v\|^2+\langle A\vec v,\vec v\rangle$", 4), (r"מסקנה: $I+A$ מוגדרת חיובית", 1),
                   (r"שימוש ב-$A=A^T$: $\vec v^TA^2\vec v=(A\vec v)^T(A\vec v)$", 2), (r"$\|A\vec v\|^2\ge0$ ולכן $A^2$ מוגדרת חיובית", 1),
                   (r"סימטריה: $(I+A)^T=I+A$ ו-$(A^2)^T=A^2$", 2)),
        pitfalls=[r"לשכוח את $A=A^T$ במעבר $\vec v^TA^2\vec v=\vec v^TA^TA\vec v$.",
                  r"לשכוח שגם $\|\vec v\|^2\ge0$ וגם $\langle A\vec v,\vec v\rangle\ge0$ נדרשים בחיבור."],
        steps=[
            num(r"עבור $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ ו-$\vec v=(1,-1)^T$, מהו $\vec v^T(I+A)\vec v$ ?", 4, r"$I+A=\begin{pmatrix}3&1\\1&3\end{pmatrix}$ ו-$3-1-1+3=4=\|\vec v\|^2+\langle A\vec v,\vec v\rangle=2+2$."),
            order("סדרו את שלבי ההוכחה ש-$A^2$ מוגדרת חיובית.",
                  [r"$\langle A^2\vec v,\vec v\rangle=\vec v^TA^2\vec v$",
                   r"$=\vec v^TA^TA\vec v$ (כי $A=A^T$)",
                   r"$=(A\vec v)^T(A\vec v)=\|A\vec v\|^2$",
                   r"$\|A\vec v\|^2\ge0$, ולכן $A^2$ מוגדרת חיובית"],
                  "פתיחת ההגדרה, שימוש בסימטריה, זיהוי נורמה, ומסקנה."),
            bug("באיזו שורה יש טעות?",
                [r"$\langle(I+A)\vec v,\vec v\rangle=\vec v^T(I+A)\vec v$",
                 r"$=\vec v^T\vec v-\vec v^TA\vec v=\|\vec v\|^2-\langle A\vec v,\vec v\rangle$",
                 r"$\|\vec v\|^2\ge0$ ו-$\langle A\vec v,\vec v\rangle\ge0$, ולכן $I+A$ מוגדרת חיובית"],
                1, r"$\vec v^T(I+A)\vec v=\vec v^T\vec v+\vec v^TA\vec v$ (חיבור ולא חיסור)."),
        ]),
    (3, "א"): dict(
        rubric=rub((r"חישוב הפולינום האופייני $\left(4-a^2-\lambda\right)\left(\lambda^2-2\lambda+1-4a^2\right)$", 5), (r"ערכים עצמיים $4-a^2$ , $1+2a$ , $1-2a$", 3),
                   (r"חיובית: $-0.5\le a\le0.5$", 3), (r"חיובית לחלוטין: $-0.5<a<0.5$", 2), (r"אין ערך $a$ שבו שלילית או שלילית לחלוטין", 2)),
        pitfalls=[r"לבלבל בין חיובית ($|a|\le0.5$) לחיובית לחלוטין ($|a|<0.5$).",
                  r"לבדוק רק את הערך העצמי $4-a^2$, שהוא חיובי עבור $|a|<2$, ולשכוח את $1\pm2a$."],
        steps=[
            num(r"עבור $a=1$, מהו הערך העצמי $4-a^2$ ?", 3, r"$4-1=3$."),
            ch("עבור אילו $a$ המטריצה מוגדרת חיובית לחלוטין?", r"$-0.5<a<0.5$", [r"$-2<a<2$", r"$-0.5\le a\le0.5$", r"$a>0.5$"],
               r"נדרש $4-a^2>0$ , $1+2a>0$ , $1-2a>0$, כלומר $|a|<0.5$. עבור $a=1$ יש ערך עצמי $1-2a=-1$, ועבור $a=0.5$ יש ערך עצמי $0$ (רק חיובית)."),
            num(r"מהו הסכום $(1+2a)+(1-2a)$ ?", 2, r"הסכום קבוע ושווה $2>0$, ולכן שני הערכים העצמיים אינם יכולים להיות שניהם $\le0$ ואין $a$ שבו המטריצה שלילית."),
        ]),
    (3, "ב"): dict(
        rubric=rub((r"כיוון ראשון: פתיחת $\|\alpha\vec u+\beta\vec v\|^2$ והצבת $\|\vec u\|=\|\vec v\|$", 4), (r"כיוון שני: פתיחת שני האגפים בריבוע", 3), (r"פירוק $(\alpha^2-\beta^2)\left(\|\vec u\|^2-\|\vec v\|^2\right)=0$ והמסקנה $\|\vec u\|=\|\vec v\|$", 3)),
        pitfalls=[r"להוכיח רק כיוון אחד של ה״אם ורק אם״.",
                  r"לצמצם בגורם $\alpha^2-\beta^2$ בלי לוודא שהוא שונה מאפס: יש לבחור $\alpha,\beta$ מתאימים."],
        steps=[
            ch(r"בכיוון השני, איזו הצבה של $\alpha,\beta$ מסיימת את ההוכחה?", r"$\alpha=1,\ \beta=0$",
               [r"$\alpha=\beta=1$", r"$\alpha=\beta=0$", r"$\alpha=1,\ \beta=-1$"],
               r"עבור $\alpha=1,\beta=0$ השוויון הופך ל-$\|\vec u\|^2=\|\vec v\|^2$. בשאר ההצבות השוויון $\alpha^2(\cdot)=\beta^2(\cdot)$ מתקיים לכל $\vec u,\vec v$ ואינו מוסיף מידע."),
            num(r"אם $\|\vec u\|^2=5$ ו-$\|\vec v\|^2=3$ , מהו $\|2\vec u+\vec v\|^2-\|\vec u+2\vec v\|^2$ ?", 6, r"$(\alpha^2-\beta^2)\left(\|\vec u\|^2-\|\vec v\|^2\right)=(4-1)(5-3)=6$."),
            order("סדרו את שלבי הכיוון הראשון.",
                  [r"$\|\alpha\vec u+\beta\vec v\|^2=\alpha^2\|\vec u\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec v\|^2$",
                   r"נציב $\|\vec u\|=\|\vec v\|$ ונקבל $\alpha^2\|\vec v\|^2+2\alpha\beta\langle\vec u,\vec v\rangle+\beta^2\|\vec u\|^2$",
                   r"זהו $\|\beta\vec u+\alpha\vec v\|^2$",
                   r"נוציא שורש ונקבל $\|\alpha\vec u+\beta\vec v\|=\|\beta\vec u+\alpha\vec v\|$"],
                  "פתיחה, הצבת השוויון, זיהוי הביטוי השני, ושורש."),
        ]),
    (4, "א"): dict(
        rubric=rub((r"חישוב $A^TA=\begin{pmatrix}5&0&4\\0&0&0\\4&0&5\end{pmatrix}$", 3), (r"ערכים עצמיים $9,1,0$ ווקטורים עצמיים", 6), (r"ערכים סינגולריים $\sigma_1=3,\sigma_2=1$ ו-$\Sigma$", 3), (r"עמודות $U$: $\vec u_i=\frac1{\sigma_i}A\vec v_i$", 3), (r"הרכבת $A=U\Sigma V^T$", 3)),
        pitfalls=[r"להשתמש בערכים העצמיים $9,1$ ב-$\Sigma$ במקום בשורשיהם $3,1$.",
                  r"לשכוח שהערך העצמי $0$ של $A^TA$ נותן עמודה של $V$ אך לא ערך סינגולרי."],
        steps=[
            num(r"מהו האיבר ב-$A^TA$ בשורה $1$ ובעמודה $3$ ?", 4, r"השורה הראשונה של $A^T$ היא $(1,2)$ והעמודה השלישית של $A$ היא $(2,1)^T$: $1\cdot2+2\cdot1=4$."),
            num(r"מהו הערך העצמי הגדול של $A^TA$ ?", 9, r"$\begin{pmatrix}5&4\\4&5\end{pmatrix}$ על הציר $x,z$ נותנת $5\pm4=9,1$."),
            num(r"מהו הערך הסינגולרי הראשון $\sigma_1$ ?", 3, r"$\sqrt9=3$."),
            num(r"אם $\vec v_1=\frac1{\sqrt2}(1,0,1)^T$ , מהו הרכיב הראשון של $\vec u_1=\frac1{\sigma_1}A\vec v_1$ (עיגול עד $0.001$)?", 0.70711, r"$A\vec v_1=\frac1{\sqrt2}(3,3)^T$ ולכן $\vec u_1=\frac1{\sqrt2}(1,1)^T$.", 0.001),
        ]),
    (4, "ב"): dict(
        rubric=rub((r"המודולים $5,7,8$ זרים בזוגות ו-$M=280$", 2), (r"$M_1=56,M_2=40,M_3=35$", 2), (r"$x_1=1,x_2=3,x_3=3$", 2), (r"הרכבה והצמצום $918\equiv78\pmod{280}$", 1)),
        pitfalls=[r"להשאיר את התשובה $918$ בלי לצמצם מודולו $280$.",
                  r"לפתור $M_ix_i\equiv a_i$ במקום $M_ix_i\equiv1$."],
        steps=[
            num(r"מהו $M_2=\frac{280}{7}$ ?", 40, r"$280/7=40$."),
            num(r"מהו $x_2$ , פתרון $40x_2\equiv1\pmod7$ ?", 3, r"$40\equiv5$ ו-$5\cdot3=15\equiv1\pmod7$."),
            num(r"מהו $x_3$ , פתרון $35x_3\equiv1\pmod8$ ?", 3, r"$35\equiv3$ ו-$3\cdot3=9\equiv1\pmod8$."),
            num(r"מהו הפתרון $x$ בין $0$ ל-$279$ ?", 78, r"$3\cdot56\cdot1+1\cdot40\cdot3+6\cdot35\cdot3=918$ ו-$918-840=78$."),
        ]),
    (5, "א"): dict(
        rubric=rub((r"גרם-שמידט: $U_2=V_2-\frac13V_1$ וכתיבת הבסיס האורתוגונלי", 4), (r"$\langle M,U_1\rangle=a+b$ , $\|U_1\|^2=3$", 4), (r"$\langle M,U_2\rangle=5b-a$ , $\|U_2\|^2=51$", 3), (r"הרכבת ההיטל $\frac1{17}\begin{pmatrix}-7a+b&6a+4b\\4a+14b&-a+5b\end{pmatrix}$", 4)),
        pitfalls=[r"לכתוב את המקדם $\frac{5b-3a}{51}$ (טעות הדפסה בפתרון הרשמי): המכפלה הפנימית היא $5b-a$.",
                  r"להשתמש בנוסחת ההיטל על בסיס שאינו אורתוגונלי, בלי גרם-שמידט."],
        steps=[
            num(r"מהי $\langle V_2,U_1\rangle$ עבור $V_2=\begin{pmatrix}1&0\\2&1\end{pmatrix}$ ו-$U_1=\begin{pmatrix}-1&1\\1&0\end{pmatrix}$ ?", 1, r"$-1+0+2+0=1$, ו-$\|U_1\|^2=3$, ולכן $U_2=V_2-\frac13U_1$."),
            num(r"מהו $\left\|\begin{pmatrix}4&-1\\5&3\end{pmatrix}\right\|^2$ ?", 51, r"$16+1+25+9=51$."),
            num(r"עבור $a=1$ ו-$b=2$, מהי $\left\langle\begin{pmatrix}0&a\\b&0\end{pmatrix},\begin{pmatrix}4&-1\\5&3\end{pmatrix}\right\rangle$ ?", 9, r"$-a+5b=-1+10=9$ (ולא $5b-3a=7$, כפי שמודפס בפתרון הרשמי)."),
            num(r"עבור $a=1$ ו-$b=2$, מהו האיבר השמאלי-העליון בהיטל (עיגול עד $0.001$)?", -0.29412, r"$\frac{-7a+b}{17}=\frac{-5}{17}\approx-0.294$.", 0.001),
        ]),
    (5, "ב"): dict(
        rubric=rub((r"כפל השוויון $c=(a*b)*a$ ב-$b$ מימין", 3), (r"אסוציאטיביות: $((a*b)*a)*b=(a*b)*(a*b)$", 3), (r"$x*x=e$ ולכן $c*b=e$", 2), (r"$b=c^{-1}=c$", 2)),
        pitfalls=[r"להניח קומוטטיביות כדי להחליף את הסדר: היא אינה נתונה.",
                  r"לשכוח שהתכונה $x^{-1}=x$ מופעלת פעמיים: על $a*b$ ועל $c$."],
        steps=[
            ch(r"איזו תכונה של חבורה מאפשרת לעבור מ-$((a*b)*a)*b$ ל-$(a*b)*(a*b)$ ?", "אסוציאטיביות",
               [r"סגירות בלבד", r"קיום איבר ניטרלי", r"יחידות ההופכי"],
               r"המעבר הוא שינוי סוגריים בלבד, וזו אסוציאטיביות. סגירות, איבר ניטרלי ויחידות ההופכי אינם משנים סוגריים."),
            order("סדרו את שלבי ההוכחה.",
                  [r"$c*b=\big((a*b)*a\big)*b$",
                   r"$=(a*b)*(a*b)$ לפי אסוציאטיביות",
                   r"$=e$ כי $x*x=e$ לכל $x$",
                   r"לכן $b=c^{-1}$ , ומכיוון ש-$c^{-1}=c$ מתקבל $c=b$"],
                  "כפל ב-$b$, אסוציאטיביות, $x*x=e$, ואז הופכי."),
            bug("באיזו שורה יש טעות?",
                [r"$c*b=\big((a*b)*a\big)*b$",
                 r"$=(a*b)*(a*b)$ לפי אסוציאטיביות",
                 r"$=a*b$ כי $x*x=e$ לכל $x$",
                 r"לכן $b=c^{-1}=c$"],
                2, r"$x*x=e$ ולכן $(a*b)*(a*b)=e$ ולא $a*b$."),
        ]),
}
for _q in questions:
    _s = S23BA.get((_q["num"], _q.get("part")))
    assert _s is not None, ("no steps for", _q["num"], _q.get("part"))
    assert sum(r["points"] for r in _s["rubric"]) == _q["points"], ("rubric sum", _q["num"], _q.get("part"))
    _q["rubric"], _q["rubricSource"] = _s["rubric"], "ai-verified"
    _q["pitfalls"] = _s["pitfalls"]
    _q["steps"], _q["stepsSource"] = _s["steps"], "ai-verified"

exam = {
    "examCode": "23B-A",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ״ג מועד א'",
    "year": 2023,
    "examDate": "20.6.2023",
    "sourceFile": "algebra-2-23B-A-exam",
    "solutionFile": "algebra-2-23B-A-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
