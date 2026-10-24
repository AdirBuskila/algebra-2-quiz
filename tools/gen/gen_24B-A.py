# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-A.json -- algebra-2 (20079), semester B 2024, moed A (21.07.2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-A.py

Source: the sitting exists only inside the 250-page compilation "exams + solutions 2021-2024" (pp. 223-232, the exam
with each official solution typed right after its question; the whole sitting is printed a second time at pp.
241-250, same content). Five questions, 25% each ("4 of 5"); all 5 transcribed, 14 items, none held.
Page 223 carries a handwritten "|<u,v>| <= ||u|| ||v||" note from a student: not part of the exam, ignored.

Sitting code: the header says semester B tashpad, moed A, 21.07.24 -> 24B-A (no header typo).

Part letters (single letters only): Q2: a.1..a.4 -> a..d, b.1 -> e, b.2 -> f.

Slips in the official solution (checked with tools/verify/24B-A/check.py; no final answer is wrong):
- Q1a: the copy at p.241 writes sqrt(15) / "<= 15(...)" where p.223 has sqrt(14) / "<= 14(...)": 2^2+1^2+3^2 = 14.
  Written with 14; the conclusion (the inequality > 16(...) never holds) is the same.
- Q4a: the labels (i)-(iv) are used for closure, associativity, neutral, inverse; the commutativity step is also
  labelled (iv) (it is the fifth property). Written as (v).
- Q5a: the basis is named v1, v2, v2 in the official text; the third vector is v3 (written so). The column order of Q
  follows v1=(1,1,0), v2=(0,0,1), v3=(-1,1,0), eigenvalues 2,2,0.
- Q3a: the official summary calls positive SEMI-definiteness "positive definite" (the course's term); kept.
Checks: tools/verify/24B-A/check.py (sympy + brute force), all OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"נסתכל בחבורה (אין צורך להוכיח זאת) $G=\left\{\left(a,a^2\right)\ \middle|\ a\in\mathbb{Z}_7^*\right\}$ עם פעולת הכפל המוגדרת בצורה הבאה: $\left(a,a^2\right)\cdot\left(b,b^2\right)=\left(a\cdot b,a^2\cdot b^2\right)$, כאשר באגף ימין הכפל הוא **מודולו 7**."},
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף ב", "text": r"תהי $A$ מטריצה ריבועית ו-$c\in\mathbb{R}$."},
    "c4": {"kind": "text", "title": "שאלה 4",
           "text": r"נסתכל ב-$(G,*)$ כאשר $G=\{x\in\mathbb{R}:-1<x<1\}$ והפעולה $*$ מוגדרת באופן הבא: $x*y=\dfrac{x+y}{1+xy}$ , $\forall x,y\in G$."},
}

S1A = (
    r"נגדיר את שני הוקטורים הבאים: $\vec u=(\alpha,\beta,\gamma)$, $\vec v=(2,1,3)$. לפי אי-שיוויון קושי-שוורץ:" "\n"
    r"$$\left|(\alpha,\beta,\gamma)\cdot(2,1,3)\right|\le\sqrt{\alpha^2+\beta^2+\gamma^2}\cdot\sqrt{2^2+1^2+3^2},\qquad\left|2\alpha+\beta+3\gamma\right|\le\sqrt{\alpha^2+\beta^2+\gamma^2}\cdot\sqrt{14}$$" "\n"
    r"לכן לכל $\alpha,\beta,\gamma$ מתקיים $(2\alpha+\beta+3\gamma)^2\le14\left(\alpha^2+\beta^2+\gamma^2\right)$, ולכן לא קיימים $\alpha,\beta,\gamma\in\mathbb{R}$ כך ש:" "\n"
    r"$$(2\alpha+\beta+3\gamma)^2>16\left(\alpha^2+\beta^2+\gamma^2\right)$$"
)

S1B = (
    r"נמצא בסיס אורתוגונלי עבור $W=\mathrm{Sp}\left\{\vec e_1=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\vec e_2=\begin{pmatrix}0&1\\0&1\end{pmatrix},\vec e_3=\begin{pmatrix}1&1\\0&0\end{pmatrix}\right\}$ בעזרת תהליך גרם-שמידט:" "\n"
    r"$$\vec u_1=\vec e_1=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$$" "\n"
    r"$$\vec u_2=\vec e_2-\frac{\langle\vec e_2,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1=\begin{pmatrix}0&1\\0&1\end{pmatrix}-\frac24\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\begin{pmatrix}-0.5&0.5\\0.5&0.5\end{pmatrix}$$" "\n"
    r"$$\vec u_3=\vec e_3-\frac{\langle\vec e_3,\vec u_1\rangle}{\|\vec u_1\|^2}\vec u_1-\frac{\langle\vec e_3,\vec u_2\rangle}{\|\vec u_2\|^2}\vec u_2=\begin{pmatrix}1&1\\0&0\end{pmatrix}-\frac24\begin{pmatrix}1&1\\-1&1\end{pmatrix}-\frac01\begin{pmatrix}-0.5&0.5\\0.5&0.5\end{pmatrix}=\begin{pmatrix}0.5&0.5\\0.5&-0.5\end{pmatrix}$$" "\n"
    r"כעת ניתן לחשב את ההיטל המבוקש:" "\n"
    r"$$\mathbf{proj}_W(\vec v)=\frac{\langle\vec v,\vec u_1\rangle}4\vec u_1+\frac{\langle\vec v,\vec u_2\rangle}1\vec u_2+\frac{\langle\vec v,\vec u_3\rangle}1\vec u_3=1.5\begin{pmatrix}1&1\\-1&1\end{pmatrix}+\begin{pmatrix}-0.5&0.5\\0.5&0.5\end{pmatrix}+\begin{pmatrix}0.5&0.5\\0.5&-0.5\end{pmatrix}=\begin{pmatrix}1.5&2.5\\-0.5&1.5\end{pmatrix}$$"
)

S2A1 = r"האיבר הניטרלי של $G$ הוא $(1,1)$. הרי לכל $\left(a,a^2\right)\in G$ מתקיים: $(1,1)\cdot\left(a,a^2\right)=\left(1\cdot a,1\cdot a^2\right)=\left(a,a^2\right)$."

S2A2 = r"כיוון ש-$2\cdot4=1\pmod7$ ו-$4\cdot2=1\pmod7$, אנו מקבלים ש-$(2,4)^{-1}=(4,2)$."

S2A3 = r"הסדר של $\mathbb{Z}_7^*$ הוא 6. לכן הסדר של $G$ הוא גם 6."

S2A4 = (
    r"הסדר של $\langle(3,2)\rangle$ שווה לסדר האיבר $(3,2)$. הסדר של 3 ב-$\mathbb{Z}_7^*$ הוא 6 והסדר של 2 ב-$\mathbb{Z}_7^*$ הוא 3. הכפולה המינימלית היא 6. לכן ההסדר של $(3,2)$ הוא 6."
)

S2B1 = (
    r"$\lambda$ הוא ערך עצמי של $A$ אם ורק אם קיים וקטור $\vec v\ne\vec0$ כך ש-$A\vec v=\lambda\vec v$. השוויון האחרון מתקיים אם ורק אם $(cI-A)\vec v=c\vec v-\lambda\vec v=(c-\lambda)\vec v$. פירוש הדבר: $c-\lambda$ הוא ערך עצמי של $cI-A$."
)

S2B2 = (
    r"ברור שהמטריצה $cI-A$ היא מטריצה סימטרית. כל ערך עצמי של המטריצה הוא מהצורה $c-\lambda$. נבחר $c$ כך ש-$c-\lambda>0$ לכל ערך עצמי $\lambda$ של $A$. נקבל ש-$cI-A$ היא מטריצה סימטרית בעלת ערכים עצמיים חיוביים. זאת אומרת ש-$cI-A$ מוגדרת חיובית לחלוטין."
)

S3A = (
    r"נחשב את הערכים העצמיים של המטריצה:" "\n"
    r"$$\begin{vmatrix}1-\lambda&c&0\\c&1-\lambda&c\\0&c&1-\lambda\end{vmatrix}=(1-\lambda)\begin{vmatrix}1-\lambda&c\\c&1-\lambda\end{vmatrix}-c\begin{vmatrix}c&c\\0&1-\lambda\end{vmatrix}=(1-\lambda)\left((1-\lambda)^2-c^2\right)-c\left(c(1-\lambda)\right)$$" "\n"
    r"$$=(1-\lambda)\left((1-\lambda)^2-2c^2\right)=(1-\lambda)\left(1-\lambda-\sqrt2c\right)\left(1-\lambda+\sqrt2c\right)$$" "\n"
    r"לכן הערכים העצמיים הם $\lambda=1,\ \lambda=1+\sqrt2c,\ \lambda=1-\sqrt2c$." "\n"
    r"**סיכום:** המטריצה **מוגדרת חיובית** כאשר $\begin{cases}1\ge0\\c\ge-\frac1{\sqrt2}\\c\le\frac1{\sqrt2}\end{cases}$, $\ c\in\left[-\dfrac1{\sqrt2},\dfrac1{\sqrt2}\right]$." "\n"
    r"המטריצה **מוגדרת חיובית לחלוטין** כאשר $\begin{cases}1>0\\c>-\frac1{\sqrt2}\\c<\frac1{\sqrt2}\end{cases}$, $\ c\in\left(-\dfrac1{\sqrt2},\dfrac1{\sqrt2}\right)$." "\n"
    r"לא קיים $c$ עבורו המטריצה מוגדרת שלילית, בפרט שלילית לחלוטין כיוון שקיים $\lambda=1$ חיובי." "\n"
    r"המטריצה **אינה מוגדרת** כאשר $c<-\dfrac1{\sqrt2}$ או $c>\dfrac1{\sqrt2}$."
)

S3B = (
    r"$y=mx+n$" "\n"
    r"$$\begin{cases}4m+n=6\\3m+n=3\\m+n=3\\n=1\\-3m+n=-1\end{cases}\Rightarrow\begin{pmatrix}4&1\\3&1\\1&1\\0&1\\-3&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}6\\3\\3\\1\\-1\end{pmatrix}\qquad A^TA\vec x=A^T\vec b$$" "\n"
    r"$$\Rightarrow\begin{pmatrix}35&5\\5&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}39\\12\end{pmatrix}\Rightarrow\begin{cases}35m+5n=39\\5m+5n=12\end{cases}\Rightarrow30m=27,\ m=0.9,\ n=1.5$$" "\n"
    r"$$y=0.9x+1.5$$"
)

S4A = (
    r"נבדוק סגירות, אסוציאטיביות, קיום איבר ניטרלי, קיום איבר הופכי, חילופיות של הפעולה $*$." "\n"
    r"**(i) סגירות:** ראשית נבדוק סגירות של הקבוצה $G$ תחת הפעולה $*$. בהתאם לרמז שבשאלה נתבונן ב-$1\pm x*y$:" "\n"
    r"$$1\pm x*y=1\pm\frac{x+y}{1+xy}=\frac{1+xy\pm x\pm y}{1+xy}=\frac{(1\pm x)(1\pm y)}{1+xy}$$" "\n"
    r"בנוסף, $|x|,|y|<1\Rightarrow1\pm x>0,\ 1\pm y>0,\ 0<1+xy\Rightarrow1\pm x*y=\dfrac{(1\pm x)(1\pm y)}{1+xy}>0$." "\n"
    r"מכאן נקבל: $1-x*y>0\Rightarrow x*y<1$, $\ 1+x*y>0\Rightarrow x*y>-1$, כלומר $-1<x*y<1\Rightarrow x*y\in G$. יש לנו סגירות." "\n"
    r"**(ii) אסוציאטיביות:** עלינו להראות שלכל $x,y,z\in G$ מתקיים $(x*y)*z=x*(y*z)$. נחשב את שני האגפים:" "\n"
    r"$$(x*y)*z=\frac{\frac{x+y}{1+xy}+z}{1+\frac{x+y}{1+xy}z}=\frac{x+y+z(1+xy)}{1+xy+(x+y)z}=\frac{x+y+z+xyz}{1+xy+xz+yz}$$" "\n"
    r"$$x*(y*z)=\frac{x+\frac{y+z}{1+yz}}{1+x\frac{y+z}{1+yz}}=\frac{(1+yz)x+y+z}{1+yz+x(y+z)}=\frac{x+y+z+xyz}{1+xy+xz+yz}$$" "\n"
    r"מכאן נקבל $(x*y)*z=x*(y*z)$, כלומר $*$ היא פעולה אסוציאטיבית." "\n"
    r"**(iii)** האיבר הניטרלי הוא $e=0$ כיוון ש-$0\in(-1,1)=G$ ובנוסף, $\forall x\in(-1,1),\ x*e=e*x=\dfrac{x+0}{1+0\cdot x}=x$." "\n"
    r"**(iv)** האיבר ההופכי ל-$x\in G$ הוא $x^{-1}=-x$ כיוון שאם $x\in G=(-1,1)$ אז $-x\in G=(-1,1)$ ובנוסף $x^{-1}*x=x*x^{-1}=\dfrac{x+(-x)}{1+x(-1)}=\dfrac0{1-x^2}=0=e$." "\n"
    r"נקבל שהזוג $(G,*)$ הוא חבורה. נותר לנו לבדוק האם חבורה זו היא אבלית." "\n"
    r"**(v) חילופיות (אבליות):** $\forall x,y\in(-1,1),\ x*y=\dfrac{x+y}{1+xy}=\dfrac{y+x}{1+yx}=y*x$. מכאן שהפעולה $*$ היא חילופית ו-$(G,*)$ היא חבורה אבלית."
)

S4B = (
    r"יהיו $x,y\in G\cap\mathbb{Q}$. מתקיים $(x+y\in\mathbb{Q})\wedge(xy\in\mathbb{Q})\Rightarrow x*y=\dfrac{x+y}{1+xy}\in\mathbb{Q}$. ידוע לנו כבר שאם $x,y\in G$ אז $x*y\in G$. מכאן נקבל ש-$x,y\in G\cap\mathbb{Q}\Rightarrow x*y\in G\cap\mathbb{Q}$." "\n"
    r"בנוסף, $x\in G\cap\mathbb{Q}\Rightarrow x^{-1}=-x\in G\cap\mathbb{Q}$. (גם $e=0\in G\cap\mathbb{Q}$.)" "\n"
    r"על-כן $H=G\cap\mathbb{Q}$ היא תת-חבורה של $G$."
)

S5A = (
    r"נמצא את הערכים העצמיים:" "\n"
    r"$$\begin{vmatrix}1-\lambda&1&0\\1&1-\lambda&0\\0&0&2-\lambda\end{vmatrix}=(2-\lambda)\left((1-\lambda)^2-1\right)=(2-\lambda)(1-\lambda-1)(1-\lambda+1)$$" "\n"
    r"$$\lambda_1=\lambda_2=2,\qquad\lambda_3=0$$" "\n"
    r"נחשב את הוקטורים העצמיים המתאימים. **$\lambda=2$:** $\begin{pmatrix}-1&1&0\\1&-1&0\\0&0&0\end{pmatrix}\leftrightarrow\begin{pmatrix}-1&1&0\\0&0&0\\0&0&0\end{pmatrix}$," "\n"
    r"$$\begin{cases}x=t\\y=t\\z=s\end{cases}\Rightarrow\begin{pmatrix}x\\y\\z\end{pmatrix}=t\begin{pmatrix}1\\1\\0\end{pmatrix}+s\begin{pmatrix}0\\0\\1\end{pmatrix}\Rightarrow v_1=\begin{pmatrix}1\\1\\0\end{pmatrix},\ v_2=\begin{pmatrix}0\\0\\1\end{pmatrix}$$" "\n"
    r"**$\lambda=0$:** $\begin{pmatrix}1&1&0\\1&1&0\\0&0&2\end{pmatrix}\leftrightarrow\begin{pmatrix}1&1&0\\0&0&0\\0&0&2\end{pmatrix}\leftrightarrow\begin{pmatrix}1&1&0\\0&0&2\\0&0&0\end{pmatrix}$, $\ \begin{cases}x=-t\\y=t\\z=0\end{cases}$, $\ v_3=\begin{pmatrix}-1\\1\\0\end{pmatrix}$." "\n"
    r"הבסיס האורתוגונלי שקיבלנו: $\left\{v_1=\begin{pmatrix}1\\1\\0\end{pmatrix},v_2=\begin{pmatrix}0\\0\\1\end{pmatrix},v_3=\begin{pmatrix}-1\\1\\0\end{pmatrix}\right\}$, כלומר $\hat v_1=\dfrac{v_1}{\|v_1\|}=\dfrac1{\sqrt2}(1,1,0)=\left(\dfrac1{\sqrt2},\dfrac1{\sqrt2},0\right)$ ומטריצת המעבר $Q=\begin{pmatrix}\frac1{\sqrt2}&0&-\frac1{\sqrt2}\\\frac1{\sqrt2}&0&\frac1{\sqrt2}\\0&1&0\end{pmatrix}$." "\n"
    r"**תשובה סופית:**" "\n"
    r"$$\begin{pmatrix}1&1&0\\1&1&0\\0&0&2\end{pmatrix}=\begin{pmatrix}\frac1{\sqrt2}&0&-\frac1{\sqrt2}\\\frac1{\sqrt2}&0&\frac1{\sqrt2}\\0&1&0\end{pmatrix}\begin{pmatrix}2&0&0\\0&2&0\\0&0&0\end{pmatrix}\begin{pmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}&0\\0&0&1\\-\frac1{\sqrt2}&\frac1{\sqrt2}&0\end{pmatrix}$$"
)

S5B = (
    r"נסדר את המקדמים במשוואות: $\begin{cases}x\equiv2\pmod5\\x\equiv3\pmod7\\x\equiv8\pmod{11}\end{cases}$" "\n"
    r"נסמן: $m_1=5,\ m_2=7,\ m_3=11$ והם אכן זרים בזוגות. נסמן $m=m_1m_2m_3=5\cdot7\cdot11=385$, ולכן $M_1=77,\ M_2=55,\ M_3=35$. לכן הפתרון למערכת הוא:" "\n"
    r"$$x=(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3)\bmod m=(2\cdot77\cdot x_1+3\cdot55\cdot x_2+8\cdot35\cdot x_3)\bmod385$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$77x_1\equiv1\pmod5\Rightarrow2x_1\equiv1\pmod5\Rightarrow x_1=3$$" "\n"
    r"$$55x_2\equiv1\pmod7\Rightarrow6x_2\equiv1\pmod7\Rightarrow x_2=6$$" "\n"
    r"$$35x_3\equiv1\pmod{11}\Rightarrow2x_3\equiv1\pmod{11}\Rightarrow x_3=6$$" "\n"
    r"מכאן: $x\equiv(2\cdot77\cdot3+3\cdot55\cdot6+8\cdot35\cdot6)\pmod{385}\equiv3132\pmod{385}$. לכן פתרון המערכת הוא" "\n"
    r"$$x\equiv52\pmod{385}$$"
)

questions = [
    Q(1, "truefalse", "cauchy_schwarz", r"(10%) האם קיימים $\alpha,\beta,\gamma\in\mathbb{R}$ כך ש-$(2\alpha+\beta+3\gamma)^2>16\left(\alpha^2+\beta^2+\gamma^2\right)$ ?",
      S1A, part="א", points=10, verdict=False),
    Q(1, "computation", "projection",
      r"(15%) במרחב $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע\"י $\langle A,B\rangle=\mathrm{tr}\left(B^TA\right)$ לכל $A,B\in M_2(\mathbb{R})$. חשבו את ההיטל של $\vec v=\begin{pmatrix}2&2\\0&2\end{pmatrix}$ על $\mathrm{Sp}\left\{\begin{pmatrix}1&1\\-1&1\end{pmatrix},\begin{pmatrix}0&1\\0&1\end{pmatrix},\begin{pmatrix}1&1\\0&0\end{pmatrix}\right\}$.",
      S1B, part="ב", points=15),

    Q(2, "computation", "groups", r"סעיף א.1. מהו האיבר הניטרלי של $G$ ? (3%)", S2A1, part="א", points=3, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.2. מצאו את האיבר ההופכי של $(2,4)$ ? (4%)", S2A2, part="ב", points=4, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.3. מהו הסדר של $G$ ? (4%)", S2A3, part="ג", points=4, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף א.4. מהו הסדר של תת-החבורה הציקלית $\langle(3,2)\rangle$ ? (4%)", S2A4, part="ד", points=4,
      contextId="c2"),
    Q(2, "proof", "pos_def", r"סעיף ב.1. הוכיחו כי $\lambda$ הוא ערך עצמי של $A$ אם ורק אם $c-\lambda$ הוא ערך עצמי של $cI-A$. (5%)", S2B1,
      part="ה", points=5, contextId="c2b"),
    Q(2, "proof", "pos_def", r"סעיף ב.2. אם $A$ מוגדרת חיובית, אז קיים $c\in\mathbb{R}$ כך ש-$cI-A$ מוגדרת חיובית לחלוטין. (5%)", S2B2,
      part="ו", points=5, contextId="c2b"),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $c$ המטריצה $\begin{pmatrix}1&c&0\\c&1&c\\0&c&1\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "computation", "least_squares",
      r"נתונות 5 נקודות במישור: $(-3,-1),\ (0,1),\ (1,3),\ (3,3),\ (4,6)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו בעזרת שיטת הריבועים הפחותים. (10%)",
      S3B, part="ב", points=10),

    Q(4, "proof", "groups", r"סעיף א. הוכיחו כי $G$ היא חבורה אבלית. (18%)", S4A, part="א", points=18, contextId="c4"),
    Q(4, "truefalse", "groups",
      r"סעיף ב. קבעו האם $H=G\cap\mathbb{Q}$ היא תת-חבורה של החבורה $G$. כלומר, קבוצת כל המספרים הרציונאליים בקטע $(-1,1)$ מהווה תת-חבורה של $(G,*)$. (7%)",
      S4B, part="ב", points=7, contextId="c4", verdict=True),

    Q(5, "computation", "orthodiag", r"סעיף א. בצעו לכסון אורתוגונלי של המטריצה הבאה: $\begin{pmatrix}1&1&0\\1&1&0\\0&0&2\end{pmatrix}$. (17%)", S5A,
      part="א", points=17),
    Q(5, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv2\pmod5\\x\equiv3\pmod7\\x\equiv19\pmod{11}\end{cases}$. (8%)",
      S5B, part="ב", points=8),
]

# ---- rubric / pitfalls / steps (ai-draft). Every expected value is recomputed by tools/verify/24B-A/steps_check.py ----
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def num(prompt, answer, explain, tol=0):
    return {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain}


def choice(prompt, values, correct, explain):
    return {"type": "choice", "prompt": prompt, "options": opts(*values), "correctId": IDS[correct], "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def findbug(prompt, lines, idx, new, explain):
    bad = list(lines)
    bad[idx] = new
    return {"type": "findbug", "prompt": prompt, "lines": bad, "bugIndex": idx, "explain": explain}


def add(n, part, **kw):
    for q in questions:
        if q["num"] == n and q.get("part") == part:
            q.update(kw)
            q["rubricSource"] = "ai-draft"
            q["stepsSource"] = "ai-draft"
            assert sum(r["points"] for r in q["rubric"]) == q["points"], (n, part)
            return
    raise KeyError((n, part))


G1A = [r"נגדיר $\vec u=(\alpha,\beta,\gamma)$ ו-$\vec v=(2,1,3)$",
       r"קושי-שוורץ: $|\vec u\cdot\vec v|\le\|\vec u\|\|\vec v\|$",
       r"$\|\vec v\|^2=14$, ולכן $(2\alpha+\beta+3\gamma)^2\le14\left(\alpha^2+\beta^2+\gamma^2\right)$",
       r"$14\left(\alpha^2+\beta^2+\gamma^2\right)\le16\left(\alpha^2+\beta^2+\gamma^2\right)$, ולכן אין $\alpha,\beta,\gamma$ המקיימים את אי-השוויון המבוקש"]
add(1, "א",
    rubric=rub(("בחירת הווקטורים $\\vec u=(\\alpha,\\beta,\\gamma)$ ו-$\\vec v=(2,1,3)$", 3), ("הפעלת אי-שוויון קושי-שוורץ", 3),
               ("חישוב $\\|\\vec v\\|^2=14$", 2), ("מסקנה: $\\le14(\\dots)\\le16(\\dots)$, ולכן אין פתרון", 2)),
    pitfalls=["לענות 'כן' אחרי בדיקת ערכים ספציפיים בלבד, בלי להוכיח את החסם לכל שלישייה.",
              "לחשב $\\|\\vec v\\|^2$ בטעות כ-$2+1+3=6$ במקום $4+1+9=14$."],
    steps=[num(r"מהו $\|\vec v\|^2$ עבור $\vec v=(2,1,3)$?", 14, "$4+1+9=14$."),
           num(r"עבור $(\alpha,\beta,\gamma)=(2,1,3)$ מהו $(2\alpha+\beta+3\gamma)^2$?", 196, "$(4+1+9)^2=196=14\\cdot14$, כלומר $14\\left(\\alpha^2+\\beta^2+\\gamma^2\\right)$: זה מקרה השוויון בקושי-שוורץ."),
           order("סדרו את שלבי ההוכחה.", G1A, "הווקטורים נבחרים לפני ההפעלה, והחסם $14\\le16$ נשאר אחרון.")])

G1B = [r"$u_1=e_1$",
       r"$u_2=e_2-\frac{\langle e_2,u_1\rangle}{\|u_1\|^2}u_1$",
       r"$u_3=e_3-\frac{\langle e_3,u_1\rangle}{\|u_1\|^2}u_1-\frac{\langle e_3,u_2\rangle}{\|u_2\|^2}u_2$",
       r"$\mathbf{proj}_W(\vec v)=\sum_{i=1}^3\frac{\langle\vec v,u_i\rangle}{\|u_i\|^2}u_i$"]
add(1, "ב",
    rubric=rub(("חישוב $u_2=\\begin{pmatrix}-0.5&0.5\\\\0.5&0.5\\end{pmatrix}$ בגרם-שמידט", 4), ("חישוב $u_3=\\begin{pmatrix}0.5&0.5\\\\0.5&-0.5\\end{pmatrix}$ (כאשר $\\langle e_3,u_2\\rangle=0$)", 4),
               ("שימוש בנוסחת ההיטל על הבסיס האורתוגונלי עם המקדמים $1.5,\\ 1,\\ 1$", 4), ("התשובה $\\begin{pmatrix}1.5&2.5\\\\-0.5&1.5\\end{pmatrix}$", 3)),
    pitfalls=["להשתמש בנוסחת ההיטל על $e_1,e_2,e_3$ ישירות, אף שאינם אורתוגונליים.",
              "לשכוח לחלק ב-$\\|u_i\\|^2$ (למשל $\\|u_1\\|^2=4$) ולקבל מקדמים גדולים מדי."],
    steps=[num(r"מהו $\langle e_2,u_1\rangle$ עבור $e_2=\begin{pmatrix}0&1\\0&1\end{pmatrix}$ ו-$u_1=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$?", 2,
               "$0+1+0+1=2$, ו-$\\|u_1\\|^2=4$, ולכן המקדם $\\frac24$."),
           num(r"מהו $\langle e_3,u_2\rangle$ עבור $e_3=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ ו-$u_2=\begin{pmatrix}-0.5&0.5\\0.5&0.5\end{pmatrix}$?", 0, "$-0.5+0.5+0+0=0$."),
           num(r"מהו המקדם $\frac{\langle\vec v,u_1\rangle}{\|u_1\|^2}$ בהיטל, עבור $\vec v=\begin{pmatrix}2&2\\0&2\end{pmatrix}$?", 1.5, "$\\langle\\vec v,u_1\\rangle=2+2+0+2=6$, ולכן $\\frac64=1.5$.", tol=1e-9),
           num("מהי הכניסה הימנית העליונה של ההיטל?", 2.5, "$1.5\\cdot1+1\\cdot0.5+1\\cdot0.5=2.5$.", tol=1e-9),
           order("סדרו את שלבי החישוב.", G1B, "כל וקטור $u_i$ תלוי בקודמים, וההיטל נחשב על הבסיס האורתוגונלי הסופי.")])

add(2, "א",
    rubric=rub(("זיהוי האיבר הניטרלי $(1,1)$", 1), ("בדיקה ש-$(1,1)\\cdot(a,a^2)=(a,a^2)$ לכל $a$", 2)),
    pitfalls=["לבחור $(0,0)$ כאיבר ניטרלי: $0\\notin\\mathbb{Z}_7^*$, ולכן הוא אינו ב-$G$.",
              "לבדוק רק מצד אחד; בחבורה אבלית זה מספיק, אך כדאי לציין שהכפל חילופי."],
    steps=[choice("מהו האיבר הניטרלי של $G$?", ["$(1,1)$", "$(0,0)$", "$(1,0)$", "$(0,1)$"], 0,
                  "$(0,0),(1,0),(0,1)$ אינם ב-$G$, כי $G$ מכילה זוגות $(a,a^2)$ עם $a\\ne0$; ו-$(1,1)\\cdot(a,a^2)=(a,a^2)$."),
           num(r"מהו הרכיב השני במכפלה $(1,1)\cdot(3,2)$ (מודולו 7)?", 2, "$1\\cdot2=2$.")])

add(2, "ב",
    rubric=rub(("ההופכי נלקח ברכיבים: ההופכי של 2 והופכי של 4 מודולו 7", 2), ("$2\\cdot4=8\\equiv1$", 1), ("$4\\cdot2\\equiv1$, ולכן ההופכי הוא $(4,2)$", 1)),
    pitfalls=["לכתוב את ההופכי כ-$(-2,-4)$ בלי להפחית מודולו 7: $(5,3)$ אינו הופכי של $(2,4)$.",
              "להשאיר שברים כמו $\\frac12$ במקום הערכים הנכונים ב-$\\mathbb{Z}_7$."],
    steps=[num("מהו ההופכי של 2 ב-$\\mathbb{Z}_7^*$ (ערך בין 1 ל-6)?", 4, "$2\\cdot4=8\\equiv1\\pmod7$."),
           num("מהו ההופכי של 4 ב-$\\mathbb{Z}_7^*$?", 2, "$4\\cdot2=8\\equiv1\\pmod7$.")])

add(2, "ג",
    rubric=rub(("הסדר של $\\mathbb{Z}_7^*$ הוא 6", 2), ("כל $a\\in\\mathbb{Z}_7^*$ קובע איבר יחיד $(a,a^2)$ ב-$G$, ולכן $|G|=6$", 2)),
    pitfalls=["לענות 49 או 36, כלומר לספור כל זוג $(a,b)$ ולא רק זוגות מהצורה $(a,a^2)$.", "לענות 7 ולשכוח שהאפס אינו ב-$\\mathbb{Z}_7^*$."],
    steps=[choice("מה קובע את מספר האיברים של $G$?", ["הערך $a\\in\\mathbb{Z}_7^*$ קובע את הזוג $(a,a^2)$ באופן יחיד, ולכן $|G|=6$",
                                                   "יש 7 אפשרויות ל-$a$, ולכן $|G|=7$", "יש 6 אפשרויות לכל רכיב, ולכן $|G|=36$", "$|G|=49$ כי זהו מכפלת $\\mathbb{Z}_7\\times\\mathbb{Z}_7$"], 0,
                  "הרכיב השני נקבע מהראשון, ו-$a$ אינו 0. בשאר האפשרויות סופרים גם זוגות שאינם מהצורה $(a,a^2)$ או את 0."),
           num("כמה איברים יש ל-$\\mathbb{Z}_7^*$?", 6, "$\\{1,2,3,4,5,6\\}$.")])

add(2, "ד",
    rubric=rub(("הסדר של $\\langle(3,2)\\rangle$ שווה לסדר של $(3,2)$", 1), ("הסדר של 3 ב-$\\mathbb{Z}_7^*$ הוא 6", 1), ("הסדר של 2 ב-$\\mathbb{Z}_7^*$ הוא 3", 1),
               ("הסדר של $(3,2)$ הוא $\\mathrm{lcm}(6,3)=6$", 1)),
    pitfalls=["לכפול את הסדרים ולקבל $18$ במקום להשתמש בכפולה המשותפת המינימלית.", "לחשוב שסדר הזוג הוא המקסימום או הסכום של הסדרים."],
    steps=[num("מהו הסדר של 3 ב-$\\mathbb{Z}_7^*$ (החזקה הקטנה $k\\ge1$ עם $3^k\\equiv1\\pmod7$)?", 6, "החזקות של 3 מודולו 7: 3, 2, 6, 4, 5, 1."),
           num("מהו הסדר של 2 ב-$\\mathbb{Z}_7^*$?", 3, "החזקות של 2 מודולו 7: 2, 4, 1."),
           num("מהו הסדר של $(3,2)$?", 6, "$\\mathrm{lcm}(6,3)=6$.")])

G2B1 = [r"$\lambda$ ערך עצמי של $A$ אם ורק אם קיים $\vec v\ne\vec0$ עם $A\vec v=\lambda\vec v$",
        r"$(cI-A)\vec v=c\vec v-A\vec v$",
        r"$=c\vec v-\lambda\vec v=(c-\lambda)\vec v$",
        r"לכן $c-\lambda$ ערך עצמי של $cI-A$"]
add(2, "ה",
    rubric=rub(("כתיבת הגדרת ערך עצמי עם וקטור עצמי $\\vec v\\ne\\vec0$", 1), ("חישוב $(cI-A)\\vec v=c\\vec v-A\\vec v$", 2), ("הצבת $A\\vec v=\\lambda\\vec v$ וקבלת $(c-\\lambda)\\vec v$", 1), ("מסקנה: $c-\\lambda$ ערך עצמי, ובשני הכיוונים", 1)),
    pitfalls=["לחשב $(cI-A)\\vec v$ כ-$c\\vec v+A\\vec v$ (טעות סימן).", "להוכיח כיוון אחד בלבד של ה'אם ורק אם'."],
    steps=[num("אם 3 ערך עצמי של $A$ ו-$c=5$, איזה ערך עצמי של $cI-A$ מתקבל?", 2, "$c-\\lambda=5-3=2$."),
           order("סדרו את שלבי ההוכחה.", G2B1, "כל שלב נשען על הקודם."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G2B1, 2, r"$=c\vec v+\lambda\vec v=(c+\lambda)\vec v$",
                   "$(cI-A)\\vec v=c\\vec v-A\\vec v$, ולכן מחסרים: $(c-\\lambda)\\vec v$.")])

add(2, "ו",
    rubric=rub(("$cI-A$ סימטרית כי $A$ סימטרית", 1), ("הערכים העצמיים של $cI-A$ הם $c-\\lambda$", 1), ("בחירת $c$ גדול מכל הערכים העצמיים של $A$", 2), ("מסקנה: סימטרית עם ערכים עצמיים חיוביים, כלומר מוגדרת חיובית לחלוטין", 1)),
    pitfalls=["לבחור $c=0$ או $c$ קטן: אז $c-\\lambda$ אינו חיובי עבור הערכים העצמיים הגדולים.", "לבחור $c$ שווה לערך העצמי הגדול ביותר: מתקבל ערך עצמי $0$ ולא חיובי."],
    steps=[choice("איך בוחרים את $c$ לפי הפתרון הרשמי?",
                  ["$c$ גדול ממש מכל הערכים העצמיים של $A$", "$c$ שווה לערך העצמי הגדול ביותר של $A$", "$c=0$", "$c$ קטן מכל הערכים העצמיים של $A$"], 0,
                  "צריך $c-\\lambda>0$ לכל $\\lambda$. שוויון נותן ערך עצמי $0$; $c=0$ נותן ערכים אי-חיוביים; $c$ קטן נותן ערכים שליליים."),
           num(r"אם הערכים העצמיים של $A$ הם $0,2,5$, מהו ה-$c$ השלם הקטן ביותר שעבורו $cI-A$ מוגדרת חיובית לחלוטין?", 6, "צריך $c>5$, ולכן $c=6$.")])

add(3, "א",
    rubric=rub(("חישוב הדטרמיננטה $(1-\\lambda)\\left((1-\\lambda)^2-2c^2\\right)$", 5), ("הערכים העצמיים $1,\\ 1+\\sqrt2c,\\ 1-\\sqrt2c$", 2),
               ("מוגדרת חיובית: $c\\in\\left[-\\frac1{\\sqrt2},\\frac1{\\sqrt2}\\right]$", 3), ("מוגדרת חיובית לחלוטין: הקטע הפתוח", 2), ("לא מוגדרת שלילית (בגלל $\\lambda=1$) ואינה מוגדרת מחוץ לקטע", 3)),
    pitfalls=["לכלול את הקצוות $\\pm\\frac1{\\sqrt2}$ במוגדרת חיובית לחלוטין: שם יש ערך עצמי $0$.", "להסיק שהמטריצה שלילית עבור $|c|$ גדול, אף שהערך העצמי $1$ תמיד חיובי (היא אינה מוגדרת)."],
    steps=[num(r"עבור איזה $c>0$ מתאפס הערך העצמי $1-\sqrt2c$? (תשובה עשרונית)", 0.70710678, "$1-\\sqrt2c=0$ נותן $c=\\frac1{\\sqrt2}\\approx0.7071$.", tol=1e-6),
           num("מהו הערך העצמי הקטן ביותר עבור $c=1$? (תשובה עשרונית)", -0.41421356, "$1-\\sqrt2\\approx-0.4142$, ולכן המטריצה אינה מוגדרת.", tol=1e-6),
           choice("איזה סיווג נכון?",
                  ["חיובית לחלוטין בדיוק עבור $|c|<\\frac1{\\sqrt2}$, וחיובית בדיוק עבור $|c|\\le\\frac1{\\sqrt2}$",
                   "חיובית לחלוטין בדיוק עבור $|c|\\le\\frac1{\\sqrt2}$", "חיובית לחלוטין לכל $c$", "שלילית לחלוטין עבור $|c|>\\frac1{\\sqrt2}$"], 0,
                  "בקצוות יש ערך עצמי $0$, ולכן חיובית אך לא חיובית לחלוטין. מחוץ לקטע יש ערך עצמי שלילי וגם $1$ חיובי, ולכן אינה מוגדרת.")])

add(3, "ב",
    rubric=rub(("בניית המערכת $A\\vec x=\\vec b$ מהנקודות", 2), ("המשוואות הנורמליות $\\begin{pmatrix}35&5\\\\5&5\\end{pmatrix}\\vec x=\\begin{pmatrix}39\\\\12\\end{pmatrix}$", 4), ("פתרון: $m=0.9,\\ n=1.5$", 3), ("הישר $y=0.9x+1.5$", 1)),
    pitfalls=["לפתור ישירות את מערכת חמש המשוואות בשני נעלמים.", "טעות בסכום $\\sum x_iy_i$ עקב הסימנים השליליים של הנקודה $(-3,-1)$."],
    steps=[num(r"מהו $\sum x_i^2$ עבור $x=-3,0,1,3,4$?", 35, "$9+0+1+9+16=35$."),
           num(r"מהו $\sum x_iy_i$ עבור הנקודות $(-3,-1),(0,1),(1,3),(3,3),(4,6)$?", 39, "$3+0+3+9+24=39$."),
           num("מהו השיפוע $m$?", 0.9, "$35m+5n=39$ פחות $5m+5n=12$ נותן $30m=27$.", tol=1e-9),
           num("מהו $n$?", 1.5, "$5m+5n=12$ עם $m=0.9$ נותן $5n=7.5$.", tol=1e-9)])

G4Acl = [r"$1\pm x*y=1\pm\frac{x+y}{1+xy}$",
         r"$=\frac{1+xy\pm x\pm y}{1+xy}$",
         r"$=\frac{(1\pm x)(1\pm y)}{1+xy}$",
         r"$1\pm x>0,\ 1\pm y>0,\ 1+xy>0$, ולכן $1\pm x*y>0$",
         r"מכאן $-1<x*y<1$, כלומר $x*y\in G$"]
add(4, "א",
    rubric=rub(("סגירות: פירוק $1\\pm x*y=\\frac{(1\\pm x)(1\\pm y)}{1+xy}$ והסקת $-1<x*y<1$", 6), ("אסוציאטיביות: שני האגפים שווים ל-$\\frac{x+y+z+xyz}{1+xy+xz+yz}$", 4), ("איבר ניטרלי $e=0$", 2),
               ("הופכי $x^{-1}=-x$, ושייך ל-$G$", 3), ("חילופיות ומסקנה שהחבורה אבלית", 3)),
    pitfalls=["לשכוח להראות סגירות (ש-$x*y$ נשאר בקטע $(-1,1)$) ולהתחיל ישר באסוציאטיביות.", "לחשב את ההופכי כ-$\\frac1x$ (הופכי כפלי): הפעולה היא לא כפל, והאיבר הניטרלי הוא $0$."],
    steps=[order("סדרו את הוכחת הסגירות.", G4Acl, "כל שורה נובעת מהקודמת, וההסקה על $G$ אחרונה."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G4Acl, 2, r"$=\frac{(1\pm x)(1\mp y)}{1+xy}$",
                   "הפירוק הנכון הוא $(1\\pm x)(1\\pm y)=1\\pm x\\pm y+xy$; עם $\\mp$ מתקבל $1\\pm x\\mp y-xy$."),
           num(r"עבור $x=0.5,\ y=0.2,\ z=0.1$ מהו $(x*y)*z$? (תשובה עשרונית)", 0.6923077, "$x*y=\\frac7{11}$, ואז $\\frac{7/11+0.1}{1+0.7/11}=\\frac9{13}\\approx0.6923$ (זהה ל-$x*(y*z)$).", tol=1e-6),
           choice("מהו ההופכי של $x$ בחבורה $(G,*)$?", ["$-x$", "$\\frac1x$", "$-\\frac1x$", "$1-x$"], 0,
                  "האיבר הניטרלי הוא $0$, ו-$x*(-x)=\\frac{0}{1-x^2}=0$. עבור $\\frac1x$ מתקבל $\\frac{x+1/x}{2}\\ne0$ (וגם $\\frac1x\\notin G$).")])

add(4, "ב",
    rubric=rub(("סגירות: סכום ומכפלה של רציונליים רציונליים, ולכן $\\frac{x+y}{1+xy}\\in\\mathbb{Q}$", 2), ("$x*y\\in G$ כבר ידוע", 1), ("ההופכי $-x\\in G\\cap\\mathbb{Q}$", 2), ("$0\\in G\\cap\\mathbb{Q}$", 1), ("מסקנה: תת-חבורה", 1)),
    pitfalls=["לבדוק רק שהקבוצה מכילה את $0$ בלי סגירות והופכי.", "לשכוח שהתוצאה צריכה להיות גם בקטע $(-1,1)$, לא רק רציונלית."],
    steps=[choice("מה מספיק להראות כדי ש-$H$ תהיה תת-חבורה של $G$?",
                  ["ש-$H$ מכילה את $e$, סגורה לפעולה וסגורה להופכי", "ש-$H$ סגורה לפעולה בלבד", "ש-$H$ מכילה את $e$ בלבד", "ש-$H$ סופית"], 0,
                  "סגירות לבדה אינה מספיקה (למשל $\\mathbb{N}$ ביחס לחיבור), ואיבר ניטרלי לבדו אינו מספיק; סופיות אינה נדרשת."),
           num(r"מהו $\frac12*\frac13$ (תשובה עשרונית)? הוא רציונלי, כנדרש לסגירות.", 0.7142857, "$\\frac{5/6}{1+1/6}=\\frac57\\approx0.7143$.", tol=1e-6)])

add(5, "א",
    rubric=rub(("חישוב הערכים העצמיים $2,2,0$", 4), ("הוקטורים העצמיים של $\\lambda=2$: $(1,1,0)$ ו-$(0,0,1)$", 3), ("הוקטור העצמי של $\\lambda=0$: $(-1,1,0)$", 3),
               ("בדיקת אורתוגונליות ונרמול העמודות", 4), ("כתיבת $A=QPQ^T$ עם $P=\\mathrm{diag}(2,2,0)$", 3)),
    pitfalls=["לשכוח לנרמל: עמודות כמו $(1,1,0)$ צריכות להיות מחולקות ב-$\\sqrt2$.", "לא לוודא שהוקטורים העצמיים של $\\lambda=2$ אורתוגונליים זה לזה (כאן הם כן)."],
    steps=[num("מהו הערך העצמי שאינו 2? (עקבת המטריצה היא 4)", 0, "העקבה $1+1+2=4$ שווה לסכום הערכים העצמיים $2+2+\\lambda$, ולכן $\\lambda=0$."),
           num("מהו המימד של המרחב העצמי של $\\lambda=2$?", 2, "הוא נפרש על ידי $(1,1,0)$ ו-$(0,0,1)$."),
           num(r"מהו המכפלה הפנימית $(1,1,0)\cdot(-1,1,0)$ (אורתוגונליות בין הערך העצמי 2 ל-0)?", 0, "$-1+1+0=0$."),
           num(r"מהו האורך $\|(-1,1,0)\|$? (תשובה עשרונית)", 1.41421356, "$\\sqrt2$, ולכן העמודה המנורמלת היא $\\frac1{\\sqrt2}(-1,1,0)$.", tol=1e-6)])

add(5, "ב",
    rubric=rub(("העברת המשוואה השלישית ל-$x\\equiv8\\pmod{11}$", 1), ("חישוב $m=385$ ו-$M_1=77,\\ M_2=55,\\ M_3=35$", 2), ("חישוב $x_1=3,\\ x_2=6,\\ x_3=6$", 3), ("הצבה בנוסחה והפחתה מודולו 385: $x\\equiv52$", 2)),
    pitfalls=["להשאיר $x\\equiv19\\pmod{11}$ בלי להפחית ל-8.", "לחשב הופכי שגוי (למשל $2x\\equiv1\\pmod5$ נותן 3, לא 2)."],
    steps=[num("מהו 19 מודולו 11 (ערך בין 0 ל-10)?", 8, "$19=11+8$."),
           num("מהו $x_1$ המקיים $77x_1\\equiv1\\pmod5$?", 3, "$77\\equiv2$, ו-$2\\cdot3=6\\equiv1$."),
           num("מהו $x_3$ המקיים $35x_3\\equiv1\\pmod{11}$?", 6, "$35\\equiv2$, ו-$2\\cdot6=12\\equiv1$."),
           num("מהו הפתרון $x$ מודולו 385 (ערך בין 0 ל-384)?", 52, "$3132\\bmod385=52$.")])

exam = {
    "examCode": "24B-A",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ד מועד א'",
    "year": 2024,
    "examDate": "21.7.2024",
    "sourceFile": "algebra-2-24B-A-exam",
    "solutionFile": "algebra-2-24B-A-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
