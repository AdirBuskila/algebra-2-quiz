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

# ---------------------------------------------------------------------------------------------------------
# Phase 4 (step author): rubric / pitfalls / guided steps, all derived from the stored student solutions above.
# Numeric values are re-checked by tools/verify/25A-B/steps_check.py (sympy / brute force).
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


S25AB = {
    (1, "א"): dict(
        rubric=rub((r"הצבת המערכת $A\binom mn=\vec b$ עם עמודת איקסים ועמודת אחדות", 3),
                   (r"מעבר למשוואות הנורמליות $A^TA\binom mn=A^T\vec b$ וחישוב שני האגפים", 4),
                   (r"פתרון המערכת: $m=0.4$, $n=3.6$ והישר", 3)),
        pitfalls=[r"לפתור את $A\vec x=\vec b$ ישירות: חמש הנקודות אינן על ישר אחד, ולכן אין פתרון.",
                  r"לבלבל בין סדר העמודות: העמודה הראשונה היא ערכי $x$ (המקדם $m$) והשנייה עמודת אחדות (המקדם $n$)."],
        steps=[
            ch("איזו מערכת פותרים כדי למצוא את הישר הקרוב ביותר בשיטת הריבועים הפחותים?",
               r"$A^TA\binom mn=A^T\vec b$", [r"$A\binom mn=\vec b$ (פתרון מדויק)", r"$AA^T\binom mn=\vec b$"],
               r"הפתרון כופל ב-$A^T$ משמאל. המערכת $A\vec x=\vec b$ אינה פתירה, ו-$AA^T$ היא מטריצה $5\times5$ ולא מתאימה.", 0),
            num(r"מהו האיבר הימני-העליון ב-$A^TA$, כלומר $\sum x_i^2$?", 165, r"$1+9+25+49+81=165$."),
            num(r"מהו האיבר הראשון ב-$A^T\vec b$, כלומר $\sum x_iy_i$?", 156, r"$4+15+30+35+72=156$."),
            num(r"מהו השיפוע $m$?", 0.4, r"פתרון $\begin{pmatrix}165&25\\25&5\end{pmatrix}\binom mn=\binom{156}{28}$ נותן $m=0.4$.", 0.001),
            num(r"מהו חיתוך הצירים $n$?", 3.6, r"מאותה מערכת $n=3.6$.", 0.001),
        ]),
    (1, "ב"): dict(
        rubric=rub((r"חישוב $A^TA=\begin{pmatrix}6&2\\2&6\end{pmatrix}$ וערכיה העצמיים $8,4$", 4),
                   (r"ערכים סינגולריים $\sigma_1=2\sqrt2$, $\sigma_2=2$ ומטריצה $\Sigma$ בגודל $3\times2$", 3),
                   (r"מטריצה $V$ מווקטורים עצמיים אורתונורמליים של $A^TA$", 4),
                   (r"מטריצה $U$: $u_i=Av_i/\sigma_i$ והשלמה לבסיס אורתונורמלי", 4)),
        pitfalls=[r"לכתוב את הערכים העצמיים $8,4$ במקום את השורשים שלהם $2\sqrt2,2$ ב-$\Sigma$.",
                  r"לשכוח להשלים את $U$ לבסיס אורתונורמלי של $\mathbb{R}^3$ (העמודה השלישית).",
                  r"לכתוב $V$ במקום $V^T$ בפירוק $A=U\Sigma V^T$."],
        steps=[
            num(r"מהו הערך העצמי הגדול של $A^TA=\begin{pmatrix}6&2\\2&6\end{pmatrix}$?", 8, r"$\lambda=6\pm2$, כלומר $8$ ו-$4$."),
            num(r"מהו הערך הסינגולרי הגדול $\sigma_1$ (כתבו ערך מספרי)?", 2.8284271, r"$\sigma_1=\sqrt8=2\sqrt2\approx2.828$.", 0.001),
            num(r"מהו הערך הסינגולרי $\sigma_2$?", 2, r"$\sigma_2=\sqrt4=2$."),
            num(r"$v_1=\frac1{\sqrt2}(1,1)^T$. מהו הרכיב השני של $u_1=Av_1/\sigma_1$?", 1,
                r"$Av_1=\frac1{\sqrt2}(0,4,0)^T=(0,2\sqrt2,0)^T$, ולכן $u_1=(0,1,0)^T$."),
        ]),
    (2, "א"): dict(
        rubric=rub((r"שימוש בכך ש-$(xy)^2=e$ (הנתון חל על כל איבר, כולל $xy$)", 2),
                   (r"כפל ב-$x$ משמאל וב-$y$ מימין ושימוש ב-$x^2=y^2=e$", 2),
                   (r"הסקה $yx=xy$", 1)),
        pitfalls=[r"להניח שהחבורה אבלית כדי להוכיח שהיא אבלית.",
                  r"לכפול בצד אחד בלבד: צריך $x$ משמאל ו-$y$ מימין כדי לחסל את שני הריבועים."],
        steps=[
            ch(r"מדוע מותר להסיק ש-$(xy)^2=e$?",
               r"כי $xy\in G$ והנתון $a^2=e$ מתקיים לכל איבר $a\in G$",
               [r"כי $G$ אבלית", r"כי $xy=e$"],
               r"הנתון חל על כל איבר, ו-$xy$ איבר ב-$G$. אבלית היא מה שמוכיחים, ו-$xy=e$ אינו נכון בדרך כלל.", 1),
            order("סדרו את שלבי ההוכחה.",
                  [r"$xyxy=e$ (כי $(xy)^2=e$)",
                   r"נכפול ב-$x$ משמאל וב-$y$ מימין: $x^2\,y\,x\,y^2=x\,e\,y=xy$",
                   r"נציב $x^2=y^2=e$: $yx=xy$"],
                  "קודם הנתון על $xy$, אחר כך הכפל, ואחר כך הצבת הריבועים."),
            bug("באיזו שורה יש טעות?",
                [r"$xyxy=e$ (כי $(xy)^2=e$)",
                 r"נכפול ב-$x$ משמאל וב-$y$ מימין: $x^2\,y\,x\,y^2=x\,e\,y=yx$",
                 r"נציב $x^2=y^2=e$: $yx=xy$"],
                1, r"$x\,e\,y=xy$ ולא $yx$."),
        ]),
    (2, "ב"): dict(
        rubric=rub((r"$x^2=e\Rightarrow x^4=e$ ו-$y^2=e\Rightarrow y^8=e$", 2),
                   (r"$x^5=x^4x=x$ ו-$y^9=y^8y=y$", 2),
                   (r"הסקה $x=y$", 1)),
        pitfalls=[r"לצמצם חזקות כמו במספרים: בחבורה אין חילוק, רק כפל בהופכי.",
                  r"לשכוח שהנתון $x^2=e$ חל גם על $y$."],
        steps=[
            num(r"$x^5=x^k$ כאשר $x^2=e$. מהו $k$ הקטן ביותר ($k\ge0$)?", 1, r"$x^5=x^4x=ex=x$, ולכן $k=1$."),
            num(r"$y^9=y^k$ כאשר $y^2=e$. מהו $k$ הקטן ביותר ($k\ge0$)?", 1, r"$y^9=y^8y=y$, ולכן $k=1$."),
            order("סדרו את שלבי ההוכחה.",
                  [r"$x^2=e$ ו-$y^2=e$ נותנים $x^4=e$ ו-$y^8=e$",
                   r"$x^5=x^4\cdot x=x$ ו-$y^9=y^8\cdot y=y$",
                   r"מ-$x^5=y^9$ נקבל $x=y$"],
                  "צריך קודם את $x^4=e$ ו-$y^8=e$, אחר כך מצמצמים את החזקות, ולבסוף משווים."),
        ]),
    (2, "ג"): dict(
        rubric=rub((r"סגירות: $ac\cdot bd=1$", 4), ("אסוציאטיביות כפל מטריצות", 3),
                   (r"איבר ניטרלי $I\in G$", 3), (r"הופכי $\operatorname{diag}(1/a,1/b)\in G$", 5)),
        pitfalls=[r"לשכוח להראות שהמכפלה והמטריצה ההופכית שייכות ל-$G$ (כלומר שמכפלת איברי האלכסון שלהן היא $1$).",
                  r"להניח הפיכות בלי להסביר: $ab=1$ גורר $a,b\ne0$."],
        steps=[
            ch(r"איזו אקסיומה דורשת במפורש ש-$a,b\ne0$?", "קיום איבר הופכי",
               ["סגירות", "אסוציאטיביות", "איבר ניטרלי"],
               r"ההופכי $\operatorname{diag}(1/a,1/b)$ מוגדר רק כש-$a,b\ne0$, וזה נובע מ-$ab=1$. שאר האקסיומות לא מחלקות.", 3),
            num(r"$A=\operatorname{diag}(2,\frac12)$ ו-$B=\operatorname{diag}(3,\frac13)$. מהי מכפלת שני איברי האלכסון של $AB$?", 1,
                r"$AB=\operatorname{diag}(6,\frac16)$ והמכפלה $6\cdot\frac16=1$, לכן $AB\in G$."),
            num(r"מהו האיבר הראשון באלכסון של $A^{-1}$ עבור $A=\operatorname{diag}(2,\frac12)$?", 0.5, r"$A^{-1}=\operatorname{diag}(\frac12,2)$."),
            bug("באיזו שורה בהוכחת ההופכי יש טעות?",
                [r"$ab=1$, ולכן $a,b\ne0$",
                 r"נגדיר $A^{-1}=\operatorname{diag}\left(\frac1a,\frac1b\right)$",
                 r"$\frac1a\cdot\frac1b=\frac1{a+b}=1$",
                 r"לכן $A^{-1}\in G$"],
                2, r"$\frac1a\cdot\frac1b=\frac1{ab}=1$, ולא $\frac1{a+b}$."),
        ]),
    (3, "א"): dict(
        rubric=rub((r"ערכים עצמיים $a-1,\ a+1,\ 2a$", 5), (r"חיובית: $a\ge1$, וחיובית לחלוטין: $a>1$", 4),
                   (r"שלילית: $a\le-1$, ושלילית לחלוטין: $a<-1$", 4), (r"אף אחת מהן: $-1<a<1$", 2)),
        pitfalls=[r"לבלבל בין מוגדרת (אי-שוויון חלש, $\ge$) למוגדרת לחלוטין (אי-שוויון חזק).",
                  r"לפתור את אי-השוויונות בנפרד ולשכוח לחתוך אותם: צריכים כולם יחד."],
        steps=[
            num(r"עבור $a=5$, מהו הערך העצמי הקטן ביותר של המטריצה?", 4, r"הערכים העצמיים $4,6,10$; הקטן הוא $a-1=4$."),
            ch("עבור אילו ערכי $a$ המטריצה מוגדרת חיובית (לא בהכרח לחלוטין)?", r"$a\ge1$",
               [r"$a\ge-1$", r"$a\ge0$", r"$a>1$"],
               r"צריך $a-1\ge0$, $a+1\ge0$, $2a\ge0$ יחד, כלומר $a\ge1$. עבור $a=0$ הערך $a-1<0$; ועבור $a=1$ הערכים $0,2,2$ מקיימים את ההגדרה החלשה.", 0),
            ch("מתי המטריצה אינה מוגדרת חיובית ואינה מוגדרת שלילית?", r"$-1<a<1$",
               [r"$a<-1$", r"$a>1$", r"$a=0$ בלבד"],
               r"בתחום הזה $a-1<0<a+1$, ולכן יש ערך עצמי שלילי וערך עצמי חיובי.", 1),
        ]),
    (3, "ב"): dict(
        rubric=rub((r"פיתוח הצורה הריבועית $a^2+6ab+8b^2$", 3), (r"בדיקת סימן הפולינום $t^2+6t+8$ עם $t=a/b$", 4),
                   (r"וקטור $\bar y$ עם ערך חיובי", 1), (r"וקטור $\bar x$ עם ערך שלילי", 2)),
        pitfalls=[r"לבדוק רק וקטורים בעלי רכיבים חיוביים: הצורה שלילית רק כאשר $a$ ו-$b$ בסימנים הפוכים.",
                  r"לשכוח שהרכיב הצולב מופיע פעמיים: $6ab$ ולא $3ab$."],
        steps=[
            num(r"מהו $\bar v^TC\bar v$ עבור $\bar v=(1,1)^T$?", 15, r"$1+6+8=15>0$."),
            num(r"מהו $\bar v^TC\bar v$ עבור $\bar v=(-3,1)^T$?", -1, r"$9-18+8=-1<0$."),
            ch(r"עבור אילו ערכי $t=a/b$ הביטוי $t^2+6t+8$ שלילי?", r"$-4<t<-2$",
               [r"$t<-4$", r"$-2<t<2$", r"$t>-2$"],
               r"השורשים הם $-4,-2$ והפרבולה פתוחה כלפי מעלה, ולכן היא שלילית בין השורשים בלבד.", 2),
        ]),
    (4, "א"): dict(
        rubric=rub((r"$\left(y^{-1}xy\right)^n=y^{-1}x^ny=e$ ולכן $m\le n$", 3), (r"$y^{-1}x^my=e\Rightarrow x^m=e$ ולכן $n\le m$", 3),
                   (r"מסקנה $n=m$", 2)),
        pitfalls=[r"להראות רק כיוון אחד של אי-השוויון (הסדר מוגדר כמינימום, ולכן צריך $m\le n$ וגם $n\le m$).",
                  r"לכתוב $\left(y^{-1}xy\right)^n=y^{-1}x\,y^n$: ה-$y$ מצטמצמים בין העותקים הסמוכים."],
        steps=[
            ch(r"איזו זהות נכונה לכל $k\ge1$?", r"$\left(y^{-1}xy\right)^k=y^{-1}x^ky$",
               [r"$\left(y^{-1}xy\right)^k=y^{-k}x^ky^k$", r"$\left(y^{-1}xy\right)^k=y^{-1}xy^k$"],
               r"בכל מכפלה $y\,y^{-1}$ בין עותקים סמוכים מצטמצם ל-$e$, ונשארים $y^{-1}$ בקצה השמאלי ו-$y$ בקצה הימני.", 0),
            bug("באיזו שורה בהוכחה יש טעות?",
                [r"$\left(y^{-1}xy\right)^n=y^{-1}x^ny$",
                 r"$=y^{-1}ey=y$",
                 r"לכן $\left(y^{-1}xy\right)^n=e$ ו-$m\le n$"],
                1, r"$y^{-1}ey=y^{-1}y=e$ ולא $y$."),
            num(r"ב-$S_4$ נתון $x=(1\,2\,3\,4)$ ו-$y=(1\,2)$. מהו הסדר של $y^{-1}xy$?", 4, r"צמידה שומרת על הסדר, וסדר $x$ הוא $4$."),
        ]),
    (4, "ב"): dict(
        rubric=rub((r"כפל שני האגפים ב-$y^{-1}$ משמאל ומימין", 4), (r"צמצום $yy^{-1}=e$ ו-$y^{-1}y=e$ וקבלת $y^{-1}x=xy^{-1}$", 3)),
        pitfalls=[r"לכפול ב-$y^{-1}$ רק מצד אחד: זה לא נותן את הצורה המבוקשת.",
                  r"לצמצם בצד שמאל כאילו $y^{-1}$ עוברת ל-$x$ מימין: בחבורה כללית אין חילוף."],
        steps=[
            order("סדרו את שלבי ההוכחה.",
                  [r"נתון $xy=yx$",
                   r"נכפול ב-$y^{-1}$ משמאל ומימין: $y^{-1}(xy)y^{-1}=y^{-1}(yx)y^{-1}$",
                   r"נצמצם $yy^{-1}=y^{-1}y=e$: $y^{-1}x=xy^{-1}$"],
                  "הנתון, הכפל משני הצדדים, ואז צמצום."),
            bug("באיזו שורה יש טעות?",
                [r"$y^{-1}(xy)y^{-1}=y^{-1}x\,(yy^{-1})$",
                 r"$y^{-1}x\,(yy^{-1})=y^{-1}xy$",
                 r"$y^{-1}(yx)y^{-1}=(y^{-1}y)\,x\,y^{-1}=xy^{-1}$"],
                1, r"$yy^{-1}=e$, ולכן $y^{-1}x(yy^{-1})=y^{-1}x$ ולא $y^{-1}xy$."),
        ]),
    (4, "ג"): dict(
        rubric=rub((r"בדיקת זרות בזוגות וחישוב $m=140$", 2), (r"חישוב $M_i=m/m_i$: $35,28,20$", 2),
                   (r"פתרון $M_ix_i\equiv1$: $x_i=3,2,6$", 3), (r"הרכבה $x_0=\sum a_iM_ix_i=779\equiv79\pmod{140}$", 3)),
        pitfalls=[r"לדלג על בדיקת הזרות בזוגות לפני שימוש במשפט.",
                  r"לשכוח להשתמש ב-$a_i$ (השאריות $3,4,2$) בסכום הסופי, או לשכוח לצמצם מודולו $140$."],
        steps=[
            num(r"מהו $m=4\cdot5\cdot7$?", 140, r"המודולים זרים בזוגות, ו-$m=140$."),
            num(r"פתרו $35x_1\equiv1\pmod4$ ($0\le x_1<4$). מהו $x_1$?", 3, r"$35\equiv3\pmod4$ ו-$3\cdot3=9\equiv1$."),
            num(r"פתרו $20x_3\equiv1\pmod7$ ($0\le x_3<7$). מהו $x_3$?", 6, r"$20\equiv6\pmod7$ ו-$6\cdot6=36\equiv1$."),
            num(r"מהו הסכום $3\cdot35\cdot3+4\cdot28\cdot2+2\cdot20\cdot6$ לפני הצמצום?", 779, r"$315+224+240=779$."),
            num(r"מהו הפתרון $x_0$ ($0\le x_0<140$) של המערכת?", 79, r"$779=5\cdot140+79$."),
        ]),
    (5, "א"): dict(
        rubric=rub((r"ערכים עצמיים $2,2,0$", 4), ("וקטורים עצמיים בלתי תלויים לכל ערך עצמי", 4),
                   ("אורתונורמליזציה של הווקטורים העצמיים", 4), (r"כתיבת $A=PDP^T$ עם $P$ אורתוגונלית", 3)),
        pitfalls=[r"לא לנרמל את הווקטורים העצמיים: $P$ חייבת להיות אורתוגונלית ($P^{-1}=P^T$).",
                  r"לסדר את הערכים העצמיים ב-$D$ בסדר שונה מסדר העמודות ב-$P$."],
        steps=[
            num(r"מהו הערך העצמי הגדול של $A$?", 2, r"$\det(A-\lambda I)=(2-\lambda)^2(-\lambda)$, כלומר $2,2,0$."),
            ch(r"איזה וקטור עצמי מתאים לערך העצמי $0$?", r"$(1,-1,0)^T$", [r"$(1,1,0)^T$", r"$(0,0,1)^T$", r"$(1,0,0)^T$"],
               r"$A(1,-1,0)^T=0$. הווקטורים $(1,1,0)^T$ ו-$(0,0,1)^T$ מתאימים ל-$2$, ו-$(1,0,0)^T$ אינו עצמי.", 1),
            num(r"מהו האורך של $(1,1,0)^T$ (הוא מנורמל בבניית $P$)?", 1.4142136, r"$\sqrt2\approx1.414$.", 0.001),
        ]),
    (5, "ב"): dict(
        rubric=rub((r"אי-שוויון ימני: $\left(\sqrt x+\sqrt y+\sqrt z\right)^2>x+y+z$ כי המחוברים הנוספים חיוביים", 4),
                   (r"הגדרת $\bar u,\bar v$ ויישום קושי-שוורץ", 4), (r"הסקת $\frac13\le\frac{x+y+z}{(\cdots)^2}$", 2)),
        pitfalls=[r"להוכיח רק אחד משני האי-שוויונות.",
                  r"לשכוח שהאי-שוויון הימני חזק ($<$) והשמאלי חלש ($\le$, שוויון כש-$x=y=z$)."],
        steps=[
            ch("לאילו וקטורים מיישמים את קושי-שוורץ בחלק השמאלי?",
               r"$\bar u=(\sqrt x,\sqrt y,\sqrt z)$ ו-$\bar v=(1,1,1)$",
               [r"$\bar u=(x,y,z)$ ו-$\bar v=(1,1,1)$", r"$\bar u=(\sqrt x,\sqrt y,\sqrt z)$ ו-$\bar v=(x,y,z)$"],
               r"בבחירה הראשונה $\langle\bar u,\bar v\rangle=\sqrt x+\sqrt y+\sqrt z$ ו-$\|\bar u\|^2=x+y+z$. הבחירות האחרות נותנות אי-שוויונות אחרים.", 0),
            order("סדרו את שלבי החלק השמאלי.",
                  [r"נגדיר $\bar u=(\sqrt x,\sqrt y,\sqrt z)$ ו-$\bar v=(1,1,1)$",
                   r"קושי-שוורץ: $\sqrt x+\sqrt y+\sqrt z\le\sqrt{x+y+z}\cdot\sqrt3$",
                   r"נעלה בריבוע: $\left(\sqrt x+\sqrt y+\sqrt z\right)^2\le3(x+y+z)$",
                   r"נחלק: $\frac13\le\frac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}$"],
                  "הגדרה, קושי-שוורץ, העלאה בריבוע, חלוקה."),
            bug("באיזו שורה בחלק הימני יש טעות?",
                [r"$\left(\sqrt x+\sqrt y+\sqrt z\right)^2=x+y+z+2\sqrt{xy}+2\sqrt{yz}+2\sqrt{xz}$",
                 r"המחוברים $2\sqrt{xy},2\sqrt{yz},2\sqrt{xz}$ חיוביים כי $x,y,z>0$",
                 r"לכן $x+y+z>\left(\sqrt x+\sqrt y+\sqrt z\right)^2$",
                 r"ולכן המנה קטנה מ-$1$"],
                2, r"הסכום עם מחוברים חיוביים גדול מ-$x+y+z$, ולכן $x+y+z<\left(\sqrt x+\sqrt y+\sqrt z\right)^2$."),
            num(r"מהי המנה $\frac{x+y+z}{\left(\sqrt x+\sqrt y+\sqrt z\right)^2}$ עבור $x=y=z=1$?", 0.3333333, r"$\frac{3}{9}=\frac13$ (מקרה השוויון).", 0.0005),
        ]),
}
for _q in questions:
    _s = S25AB.get((_q["num"], _q.get("part")))
    assert _s is not None, ("no steps for", _q["num"], _q.get("part"))
    assert sum(r["points"] for r in _s["rubric"]) == _q["points"], ("rubric sum", _q["num"], _q.get("part"))
    _q["rubric"], _q["rubricSource"] = _s["rubric"], "ai-draft"
    _q["pitfalls"] = _s["pitfalls"]
    _q["steps"], _q["stepsSource"] = _s["steps"], "ai-draft"

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
