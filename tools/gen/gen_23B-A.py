# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-A.json -- algebra-2 (20079), semester B 2023, moed A (20.06.2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23B-A.py

Source: this sitting exists only inside the 275-page compilation (pp. 182-197). The pages are the SOLUTION version
of the exam ("פתרון מבחן"): each question is printed followed by its typed official solution, with a grader's red
point marks. The second copy (pp. 191-197) is identical. The exam header (without solution) is not a separate page.
5 printed questions (solve 4 of 5, 25% each); 11 items (Q2 has three), 10 shipped + 1 held.

Part letters: Q2 items 1,2 of part A -> parts a, b; part B -> c.  Q1, Q3, Q4, Q5 keep printed parts a, b.
Every question text starts with its printed label.

Checked with tools/verify/23B-A/check.py (sympy):
HOLD: Q5a. The official FINAL answer is wrong. It prints Proj_W = (a+b)/3 * (-1 1; 1 0) + (5b-3a)/51 * (4 -1; 5 3),
  but <(0 a; b 0), (4 -1; 5 3)> = 5b - a (not 5b - 3a). The correct projection is
  [[-7a+b, 6a+4b], [4a+14b, -a+5b]] / 17. The Gram-Schmidt step above it (U2 = (4/3 -1/3; 5/3 1)) is right.
  Official answers are never fixed, so the item is held and listed in docs/ASK_ADIR.md.
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
    r"זאת אומרת ש-$A^2$ מוגדרת חיובית."
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

    {"num": 5, "part": "א", "kind": "computation", "topic": "projection", "points": 15, "contextId": "c5a",
     "question": r"(15%) חשבו את ההיטל של $\begin{pmatrix}0&a\\b&0\end{pmatrix}$ על $Sp\left\{\begin{pmatrix}-1&1\\1&0\end{pmatrix},\begin{pmatrix}1&0\\2&1\end{pmatrix}\right\}$, לכל $a,b\in\mathbb{R}$.",
     "hold": "official final answer wrong: it prints (a+b)/3 (-1 1; 1 0) + (5b-3a)/51 (4 -1; 5 3), but <(0 a; b 0),(4 -1; 5 3)> = 5b-a; the correct projection is [[-7a+b, 6a+4b],[4a+14b, -a+5b]]/17"},
    Q(5, "proof", "groups", r"(10%) נסמן $c=(a*b)*a$. הוכיחו כי $c=b$.", S5B, part="ב", points=10, contextId="c5b"),
]

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
