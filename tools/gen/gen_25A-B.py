# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-B.json -- algebra-2 (20079), semester A 2025, moed B (23.3.2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25A-B.py

Source: exam 2 pp.; the solution file is a 9-page handwritten/typed student solution (read from the rendered
pages), so every item is solutionSource "student-solution", official false (the refuter checks all of them).
5 questions, 12 items, all shipped. Part letters: Q2: a.1 -> a, a.2 -> b, b -> c. Q4: a.1 -> a, a.2 -> b, b -> c.

Slips fixed silently (checked with tools/verify/25A-B/check.py; no answer changes):
- Q4a.1: the written step "x^m = y^-1 x^m y = (y^-1 x y)^m = e" is a chain of equalities that is only true after
  using y^-1 x^m y = (y^-1 x y)^m = e; written in that order.
- Q4b: the copy of the statement in the solution says (8%); the exam sheet says (10%) (10% used).
- Q3a: the results (PSD a>=1, PD a>1, NSD a<=-1, ND a<-1, otherwise none) are as checked.
The student solution has no worked steps for Q1b (SVD) and Q5a (diagonalization): the final matrices are given
and verified by sympy.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    q.update(kw)
    return q


CTX = {
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף א",
            "text": r"תהי $G$ חבורה. הוכיחו שאם לכל $x\in G$ מתקיים $x^2=e$, כאשר $e$ הוא האיבר הניטרלי של $G$, אז:"},
    "c4a": {"kind": "text", "title": "שאלה 4 סעיף א", "text": r"תהי $(G,\cdot)$ חבורה ויהיו $x,y\in G$. הוכיחו כי"},
}

S1A = (
    r"נחפש $y=mx+n$ הקרוב ביותר לנקודות $(1,4),(3,5),(5,6),(7,5),(9,8)$ בשיטת הריבועים הפחותים:" "\n"
    r"$$\begin{pmatrix}1&1\\3&1\\5&1\\7&1\\9&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}4\\5\\6\\5\\8\end{pmatrix}$$" "\n"
    r"נכפול ב-$A^T$ משמאל:" "\n"
    r"$$\begin{pmatrix}1&3&5&7&9\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}1&1\\3&1\\5&1\\7&1\\9&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}1&3&5&7&9\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}4\\5\\6\\5\\8\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}165&25\\25&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}156\\28\end{pmatrix}\ \Rightarrow\ m=0.4\ ,\ n=3.6$$" "\n"
    r"$$y=0.4x+3.6$$"
)

S1B = (
    r"$$U=\begin{pmatrix}0&-\frac{\sqrt2}2&\frac{\sqrt2}2\\1&0&0\\0&\frac{\sqrt2}2&\frac{\sqrt2}2\end{pmatrix},\qquad\Sigma=\begin{pmatrix}2\sqrt2&0\\0&2\\0&0\end{pmatrix},\qquad V=\begin{pmatrix}\frac{\sqrt2}2&-\frac{\sqrt2}2\\\frac{\sqrt2}2&\frac{\sqrt2}2\end{pmatrix}$$" "\n"
    r"($A=U\Sigma V^T$; הערכים העצמיים של $A^TA=\begin{pmatrix}6&2\\2&6\end{pmatrix}$ הם $8,4$.)"
)

S2A1 = (
    r"נתון $(xy)^2=e$. כלומר $xyxy=e$. נכפול ב-$x$ משמאל וב-$y$ מימין ונשתמש ב-$x^2=e$ וב-$y^2=e$:" "\n"
    r"$$x^2\,y\,x\,y^2=x\,e\,y$$" "\n"
    r"$$e\cdot y\cdot x\cdot e=xy$$" "\n"
    r"$$yx=xy$$"
)

S2A2 = (
    r"נתון $x^5=y^9$. מכיוון ש-$x^2=e$ נקבל $x^4=e$, ומכיוון ש-$y^2=e$ נקבל $y^8=e$. לכן" "\n"
    r"$$x^4\cdot x=y^8\cdot y\ \Rightarrow\ e\cdot x=e\cdot y\ \Rightarrow\ x=y$$"
)

S2B = (
    r"**סגירות ביחס לפעולה:** $A=\begin{pmatrix}a&0\\0&b\end{pmatrix},\ B=\begin{pmatrix}c&0\\0&d\end{pmatrix}\in G,\ ab=1,\ cd=1\ \to\ AB=\begin{pmatrix}ac&0\\0&bd\end{pmatrix}$ ומתקיים $acbd=1$, לכן $AB\in G$." "\n"
    r"**אסוציאטיביות:** $(AB)C=\begin{pmatrix}ace&0\\0&bdf\end{pmatrix}=A(BC)$ (לכל $A,B,C\in G$ עם $C=\begin{pmatrix}e&0\\0&f\end{pmatrix}$)." "\n"
    r"**איבר ניטרלי:** $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}\in G$ ומתקיים $AI=IA=A$." "\n"
    r"**איבר הופכי:** כיוון ש-$ab=1$, מתקיים $a,b\ne0$ וניתן להגדיר $A^{-1}=\begin{pmatrix}\frac1a&0\\0&\frac1b\end{pmatrix}$, ומתקיים $\frac1a\cdot\frac1b=1$ ולכן $A^{-1}\in G$." "\n"
    "ובכן $G$ חבורה."
)

S3A = (
    r"הערכים העצמיים של המטריצה הם: $\lambda_1=a-1,\ \lambda_2=a+1,\ \lambda_3=2a$." "\n"
    r"המטריצה מוגדרת חיובית כאשר $\begin{cases}a-1\ge0\\a+1\ge0\\2a\ge0\end{cases}\Rightarrow\begin{cases}a\ge1\\a\ge-1\\a\ge0\end{cases}$ כלומר כאשר $a\ge1$." "\n"
    r"המטריצה מוגדרת חיובית לחלוטין כאשר $a>1$." "\n"
    r"המטריצה מוגדרת שלילית כאשר $\begin{cases}a-1\le0\\a+1\le0\\2a\le0\end{cases}\Rightarrow\begin{cases}a\le1\\a\le-1\\a\le0\end{cases}$ ומכאן $a\le-1$." "\n"
    r"המטריצה מוגדרת שלילית לחלוטין כאשר $a<-1$." "\n"
    r"המטריצה לא מוגדרת כלל כאשר $-1<a<1$."
)

S3B = (
    r"יהי $\bar v=\begin{pmatrix}a\\b\end{pmatrix}\in\mathbb{R}^2$. מתקיים:" "\n"
    r"$$\bar v^TC\bar v=\begin{pmatrix}a&b\end{pmatrix}\begin{pmatrix}1&3\\3&8\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=a^2+6ab+8b^2$$" "\n"
    r"בהנחה ש-$b\ne0$ נוציא את $b^2$ ונקבל $b^2\left[\left(\frac ab\right)^2+6\frac ab+8\right]$. נסמן $t=\frac ab$ ונבדוק את הביטוי $t^2+6t+8$, שהשורשים שלו הם $t_1=-2,\ t_2=-4$. הביטוי שלילי בדיוק עבור $-4<t<-2$ וחיובי מחוץ לקטע." "\n"
    r"למשל $t=1$, כלומר $a=b=1$, נותן $\bar v^TC\bar v=15>0$ ולכן $\bar y=\begin{pmatrix}1\\1\end{pmatrix}$ מתאים." "\n"
    r"למשל $t=-3$, כלומר $a=-3,\ b=1$ (או $a=3,\ b=-1$), נותן $\bar v^TC\bar v=9-18+8=-1<0$ ולכן $\bar x=\begin{pmatrix}-3\\1\end{pmatrix}$ מתאים."
)

S4A1 = (
    r"נסמן $o(x)=n$ ו-$o\left(y^{-1}xy\right)=m$. נוכיח כי $n=m$." "\n"
    r"לפי הגדרת הסדר, $n$ ו-$m$ הם המספרים הטבעיים המינימליים המקיימים $x^n=e$ ו-$\left(y^{-1}xy\right)^m=e$ בהתאמה." "\n"
    r"מתקיים" "\n"
    r"$$\left(y^{-1}xy\right)^n=\left(y^{-1}xy\right)\cdots\left(y^{-1}xy\right)=y^{-1}x^ny=y^{-1}ey=e$$" "\n"
    r"כלומר $m\le n$." "\n"
    r"מצד שני" "\n"
    r"$$y^{-1}x^my=\left(y^{-1}xy\right)^m=e\ \Rightarrow\ x^m=yey^{-1}=e$$" "\n"
    r"ולכן $n\le m$. הוכחנו $n=m$."
)

S4A2 = (
    r"נתון $xy=yx$. נכפול את שני האגפים ב-$y^{-1}$ מימין וב-$y^{-1}$ משמאל:" "\n"
    r"$$y^{-1}(xy)y^{-1}=y^{-1}(yx)y^{-1}$$" "\n"
    r"ונקבל את התוצאה המבוקשת: $y^{-1}x=xy^{-1}$."
)

S4B = (
    r"נסמן $m_1=4,\ m_2=5,\ m_3=7$ והם אכן זרים בזוגות. נסמן $m=m_1m_2m_3=140$, ולכן:" "\n"
    r"$$M_1=\frac m{m_1}=35,\qquad M_2=\frac m{m_2}=28,\qquad M_3=\frac m{m_3}=20$$" "\n"
    r"כעת יש למצוא פתרונות לשלוש משוואות:" "\n"
    r"$$35x_1\equiv1\pmod4,\qquad28x_2\equiv1\pmod5,\qquad20x_3\equiv1\pmod7$$" "\n"
    r"למשוואה הראשונה הפתרון הוא $x_1\equiv3\pmod4$, למשוואה השנייה הפתרון הוא $x_2\equiv2\pmod5$, ולמשוואה השלישית הפתרון הוא $x_3\equiv6\pmod7$." "\n"
    r"לכן הפתרון למערכת הוא:" "\n"
    r"$$x_0=(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3)\pmod m=(3\cdot35\cdot3+4\cdot28\cdot2+2\cdot20\cdot6)\pmod{140}=(315+224+240)\pmod{140}=79\pmod{140}$$"
)

S5A = (
    r"$$D=\begin{pmatrix}2&0&0\\0&2&0\\0&0&0\end{pmatrix},\qquad P=\begin{pmatrix}\frac1{\sqrt2}&0&-\frac1{\sqrt2}\\\frac1{\sqrt2}&0&\frac1{\sqrt2}\\0&1&0\end{pmatrix},\qquad A=PDP^{-1}=PDP^T$$" "\n"
    r"(הערכים העצמיים של $A$ הם $2,2,0$; עמודות $P$ הן וקטורים עצמיים אורתונורמליים.)"
)

S5B = (
    r"**אי השוויון הימני:** מכיוון ש-$x,y,z>0$:" "\n"
    r"$$x+y+z<\left(\sqrt x+\sqrt y+\sqrt z\right)^2=x+y+z+2\sqrt{xy}+2\sqrt{xz}+2\sqrt{yz}\iff2\left(\sqrt{xy}+\sqrt{yz}+\sqrt{xz}\right)>0$$" "\n"
    r"וזה נכון. לכן $\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}<1$." "\n"
    r"**אי השוויון השמאלי:** נגדיר $\bar u=\begin{pmatrix}\sqrt x\\\sqrt y\\\sqrt z\end{pmatrix},\ \bar v=\begin{pmatrix}1\\1\\1\end{pmatrix}$. לפי אי-שוויון קושי-שוורץ:" "\n"
    r"$$\bar u\cdot\bar v=\sqrt x\cdot1+\sqrt y\cdot1+\sqrt z\cdot1\le\sqrt{x+y+z}\cdot\sqrt3=\|\bar u\|\cdot\|\bar v\|$$" "\n"
    r"ולכן, בריבוע, $\left(\sqrt x+\sqrt y+\sqrt z\right)^2\le3(x+y+z)$, כלומר $\dfrac13\le\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}$."
)

questions = [
    Q(1, "computation", "least_squares",
      r"סעיף א. נתונות 5 נקודות במישור: $(9,8),(7,5),(5,6),(3,5),(1,4)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן של הריבועים הפחותים. (10%)",
      S1A, part="א", points=10),
    Q(1, "computation", "svd", r"סעיף ב. מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}1&-1\\2&2\\-1&1\end{pmatrix}$. (15%)",
      S1B, part="ב", points=15),

    Q(2, "proof", "groups", r"סעיף א.1. $G$ חבורה אבלית, כלומר לכל $x,y\in G$ מתקיים $x\cdot y=y\cdot x$. (5%)", S2A1, part="א",
      points=5, contextId="c2b"),
    Q(2, "proof", "groups", r"סעיף א.2. אם $x,y\in G$ ו-$x^5=y^9$ אז $x=y$. (5%)", S2A2, part="ב", points=5, contextId="c2b"),
    Q(2, "proof", "groups",
      r"סעיף ב. הוכיחו כי הקבוצה $G=\left\{A=\begin{pmatrix}a&0\\0&b\end{pmatrix}\in M_2(\mathbb{R})\ \middle|\ ab=1\right\}$ עם כפל מטריצות מהווה חבורה. (15%)",
      S2B, part="ג", points=15),

    Q(3, "computation", "pos_def",
      r"סעיף א. עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}a&0&1\\0&2a&0\\1&0&a\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן? (15%)",
      S3A, part="א", points=15),
    Q(3, "computation", "pos_def",
      r"סעיף ב. תהי $C=\begin{pmatrix}1&3\\3&8\end{pmatrix}$. מצאו וקטורים $\vec x,\vec y\in\mathbb{R}^2$ כך ש: $\vec x^TC\vec x<0$ ו-$\vec y^TC\vec y>0$. (10%)",
      S3B, part="ב", points=10),

    Q(4, "proof", "groups", r"סעיף א.1. $o(x)=o\left(y^{-1}xy\right)$, כלומר ל-$x$ ול-$y^{-1}xy$ אותו סדר. (8%)", S4A1, part="א",
      points=8, contextId="c4a"),
    Q(4, "proof", "groups", r"סעיף א.2. אם $xy=yx$ אז $xy^{-1}=y^{-1}x$. (7%)", S4A2, part="ב", points=7, contextId="c4a"),
    Q(4, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv3\pmod4\\x\equiv4\pmod5\\x\equiv2\pmod7\end{cases}$. (10%)",
      S4B, part="ג", points=10),

    Q(5, "computation", "orthodiag", r"סעיף א. בצעו לכסון אורתוגונלי למטריצה הבאה: $A=\begin{pmatrix}1&1&0\\1&1&0\\0&0&2\end{pmatrix}$. (15%)",
      S5A, part="א", points=15),
    Q(5, "proof", "cauchy_schwarz",
      r"סעיף ב. הוכיחו כי לכל שלושה מספרים ממשיים חיוביים $x,y,z$ מתקיים: $\dfrac13\le\dfrac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}<1$. (10%)",
      S5B, part="ב", points=10),
]

exam = {
    "examCode": "25A-B",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ה מועד ב'",
    "year": 2025,
    "examDate": "23.3.2025",
    "sourceFile": "algebra-2-25A-B-exam",
    "solutionFile": "student-solution-1",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
