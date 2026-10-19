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
