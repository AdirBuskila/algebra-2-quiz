# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-B.json -- algebra-2 (20079), semester A 2024, moed B (21.04.2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-B.py

Source: exam 2 pp. + typed official solution 8 pp. (both read from the rendered pages). Five questions, 25% each
("4 of 5"); all 5 are transcribed, 16 items, none held.

SITTING-CODE FIX: the printed header (exam and solution) says "semester B, tashpad" but the date 21.04.24, the
three-week gap after 24A-A (28.03.24), the title "moed B" and the file's folder/name all show semester A moed B.
Code fixed to 24A-B (no 24B- code is used for this sitting).

Part letters (single letters only): Q2: a.1..a.4 -> a..d, b.1 -> e, b.2 -> f.  Q4: a.1..a.3 -> a..c, printed b -> d.

Slips in the official solution (all checked with tools/verify/24A-B/check.py; no final answer is wrong):
- Q2a.3: with a=1 the official gets 1+e=e and writes "e=0"; that equation has no solution at all (1=0). The
  conclusion (no neutral element) stands; written as the contradiction.
- Q2a.2: the official shows the two sides differ without a numeric example; (1,2,3) gives 1 versus 11/5 (added in
  the check script only).
Checks: tools/verify/24A-B/check.py (sympy + brute force), all OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2 סעיף א",
           "text": r"נסמן $\mathbb{R}^*=\{x\in\mathbb{R}:x>0\}$. לכל $a,b\in\mathbb{R}^*$ נגדיר פעולה: $a\odot b=\dfrac{a+b}{ab}$."},
    "c2b": {"kind": "text", "title": "שאלה 2 סעיף ב", "text": r"תהי $A$ מטריצה מוגדרת חיובית לחלוטין."},
    "c4": {"kind": "text", "title": "שאלה 4 סעיף א",
           "text": r"תהי $H=\left\{\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}\in M_2(\mathbb{Z}_5)\ \middle|\ a\ne0\right\}$. נסמן ב-$a^{-1}$ את האיבר ההופכי של $a$ ב-$\mathbb{Z}_5$. נגדיר על $H$ פעולה בינארית - כפל מטריצות (כמובן שהכפל והחיבור של רכיבי המטריצות הם מודולו 5)."},
}

S1A = (
    r"$y=mx+n$" "\n"
    r"$$\begin{cases}m+n=4\\3m+n=5\\5m+n=6\\7m+n=5\\9m+n=8\end{cases}\Rightarrow\begin{pmatrix}1&1\\3&1\\5&1\\7&1\\9&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}4\\5\\6\\5\\8\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\begin{pmatrix}165&25\\25&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}156\\28\end{pmatrix}\Rightarrow\begin{cases}165m+25n=156\\25m+5n=28\end{cases}\Rightarrow m=0.4,\ n=3.6$$" "\n"
    r"$$y=0.4x+3.6$$"
)

S1B = (
    r"נמצא בסיס אורתוגונלי עבור $W=\mathrm{Sp}\left\{e_1=\begin{pmatrix}1&-1\\0&1\end{pmatrix},e_2=\begin{pmatrix}0&1\\0&1\end{pmatrix},e_3=\begin{pmatrix}1&1\\1&1\end{pmatrix}\right\}$ בעזרת תהליך גרם-שמידט:" "\n"
    r"$$v_1=e_1=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$$" "\n"
    r"$$v_2=e_2-\frac{\langle e_2,v_1\rangle}{\langle v_1,v_1\rangle}v_1=\begin{pmatrix}0&1\\0&1\end{pmatrix}-0\cdot v_1=\begin{pmatrix}0&1\\0&1\end{pmatrix}$$" "\n"
    r"$$v_3=e_3-\frac{\langle e_3,v_1\rangle}{\langle v_1,v_1\rangle}v_1-\frac{\langle e_3,v_2\rangle}{\langle v_2,v_2\rangle}v_2=\begin{pmatrix}1&1\\1&1\end{pmatrix}-\frac13\begin{pmatrix}1&-1\\0&1\end{pmatrix}-\frac22\begin{pmatrix}0&1\\0&1\end{pmatrix}=\begin{pmatrix}\frac23&\frac13\\1&-\frac13\end{pmatrix}$$" "\n"
    r"על מנת להקל את המשך החישובים, נכפיל את המטריצה ב-3: $\begin{pmatrix}2&1\\3&-1\end{pmatrix}$. קיבלנו את הבסיס האורתוגונלי $\left\{v_1=\begin{pmatrix}1&-1\\0&1\end{pmatrix},v_2=\begin{pmatrix}0&1\\0&1\end{pmatrix},v_3=\begin{pmatrix}2&1\\3&-1\end{pmatrix}\right\}$." "\n"
    r"כעת נחשב את ההיטל של $\vec v=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ על $W$:" "\n"
    r"$$\mathbf{proj}_W(\vec v)=\frac{\langle\vec v,v_1\rangle}{\langle v_1,v_1\rangle}v_1+\frac{\langle\vec v,v_2\rangle}{\langle v_2,v_2\rangle}v_2+\frac{\langle\vec v,v_3\rangle}{\langle v_3,v_3\rangle}v_3=\begin{pmatrix}1&-1\\0&1\end{pmatrix}+\frac32\begin{pmatrix}0&1\\0&1\end{pmatrix}+\frac25\begin{pmatrix}2&1\\3&-1\end{pmatrix}$$" "\n"
    r"תשובה סופית: $$\mathbf{proj}_W(\vec v)=\begin{pmatrix}\frac95&\frac9{10}\\\frac65&\frac{21}{10}\end{pmatrix}$$"
)

S2A1 = (
    r"עבור $a,b\in\mathbb{R}^*$ מתקיים $a+b,\ ab>0$ ולכן $a\odot b=\dfrac{a+b}{ab}\in\mathbb{R}^*$."
)

S2A2 = (
    r"נבדוק האם $(a\odot b)\odot c=a\odot(b\odot c)$:" "\n"
    r"$$(a\odot b)\odot c=\frac{a+b}{ab}\odot c=\frac{\frac{a+b}{ab}+c}{\frac{a+b}{ab}\cdot c}=\frac{a+b+abc}{ac+bc}$$" "\n"
    r"$$a\odot(b\odot c)=a\odot\frac{b+c}{bc}=\frac{a+\frac{b+c}{bc}}{a\cdot\frac{b+c}{bc}}=\frac{abc+b+c}{ab+ac}$$" "\n"
    "לכן הפעולה אינה אסוציאטיבית."
)

S2A3 = (
    r"נחפש אם קיים $e\in\mathbb{R}^*$ כך ש-$a\odot e=a$ וגם $e\odot a=a$. נקבל:" "\n"
    r"$$a\odot e=\frac{a+e}{ae}=a\ \Rightarrow\ a+e=a^2e$$" "\n"
    r"נבחר $a=1$ ונקבל ש-$1+e=e$, כלומר $1=0$, סתירה (אין פתרון). לכן ב-$(\mathbb{R}^*,\odot)$ לא קיים איבר ניטרלי."
)

S2A4 = (
    r"נדרוש ש-$x\odot x=x$ ונקבל ש-$x\odot x=\dfrac{x+x}{x^2}\overset{x\ne0}{=}\dfrac2x=x$. מכאן $x^2=2$ ו-$x=\sqrt2$." "\n"
    r"כלומר קיים $x$ כזה: $x=\sqrt2$."
)

S2B1 = (
    r"כיוון ש-$A$ מוגדרת חיובית לחלוטין, אנו מסיקים כי אין לה ערך עצמי $0$. כלומר המטריצה הפיכה."
)

S2B2 = (
    r"מתקיים $\left(A^{-1}\right)^T=\left(A^T\right)^{-1}=A^{-1}$, כלומר $A^{-1}$ סימטרית. נותר לבדוק כי כל הערכים העצמיים שלה חיוביים. יהי $\lambda$ ערך עצמי של $A^{-1}$. אזי קיים $\vec v\ne\vec0$ (וקטור עצמי) כך ש-$A^{-1}\vec v=\lambda\vec v$. נכפיל ב-$A$ משמאל ונקבל $\vec v=\lambda A\vec v$. מכאן רואים ש-$\lambda\ne0$, אחרת $\vec v=\vec0$. לכן $\dfrac1\lambda\vec v=A\vec v$. זאת אומרת ש-$\dfrac1\lambda$ הוא ערך עצמי של $A$ ו-$\dfrac1\lambda>0$ ולכן $\lambda>0$. הוכחנו ש-$A^{-1}$ גם מוגדרת חיובית לחלוטין."
)

S3A = (
    r"הערכים העצמיים של המטריצה הם $\lambda_1=2a^2$, $\lambda_2=2a^2+1$, $\lambda=0$. לכן המטריצה מוגדרת חיובית לכל $a\in\mathbb{R}$. אין ערכי $a$ עבורם המטריצה מוגדרת חיובית לחלוטין, שלילית או שלילית לחלוטין."
)

S3B = (
    "**כיוון אחד:** נניח ש-$\\langle\\vec u,\\vec v\\rangle=0$. אזי\n"
    r"$$\|\vec u+t\vec v\|^2=\langle\vec u+t\vec v,\vec u+t\vec v\rangle=\|\vec u\|^2+2t\underbrace{\langle\vec u,\vec v\rangle}_{0}+t^2\|\vec v\|^2=\|\vec u\|^2+t^2\|\vec v\|^2\ge\|\vec u\|^2$$" "\n"
    r"ולכן $\|\vec u+t\vec v\|\ge\|\vec u\|$." "\n"
    r"**כיוון שני:** נניח ש-$\|\vec u\|\le\|\vec u+t\vec v\|$ לכל $t\in\mathbb{R}$. אזי לכל $t\in\mathbb{R}$ מתקיים" "\n"
    r"$$\|\vec u+t\vec v\|^2=\|\vec u\|^2+2t\langle\vec u,\vec v\rangle+t^2\|\vec v\|^2\ge\|\vec u\|^2$$" "\n"
    r"זאת אומרת ש-$2t\langle\vec u,\vec v\rangle+t^2\|\vec v\|^2\ge0$ או $-2t\langle\vec u,\vec v\rangle\le t^2\|\vec v\|^2$ לכל $t\in\mathbb{R}$." "\n"
    r"מפני שאי-השוויון נכון לכל $t$, חיובי או שלילי, אפשר להסיק כי $\left|\langle\vec u,\vec v\rangle\right|\le\dfrac{|t|}2\|\vec v\|^2$ לכל $t$ קרוב ל-0 כרצוננו. פירוש הדבר: $\langle\vec u,\vec v\rangle=0$."
)

S4A1 = (
    "נבדוק את 4 התנאים של חבורה.\n"
    r"**סגירות:** אם $\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix},\begin{pmatrix}b&d\\0&b^{-1}\end{pmatrix}\in H$ אז $\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}\cdot\begin{pmatrix}b&d\\0&b^{-1}\end{pmatrix}=\begin{pmatrix}ab&ad+cb^{-1}\\0&a^{-1}b^{-1}\end{pmatrix}\in H$." "\n"
    "**אסוציאטיביות:** כפל מטריצות פעולה אסוציאטיבית.\n"
    r"**קיום איבר ניטרלי:** מטריצת היחידה, $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}\in H$, מהווה את האיבר הניטרלי ב-$H$." "\n"
    r"**קיום איבר הופכי:** לכל $X=\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}\in H$ מתקיים (לפי נוסחת המטריצה ההופכית 2x2): $X^{-1}=\begin{pmatrix}a^{-1}&-c\\0&a\end{pmatrix}\in H$." "\n"
    r"**דרך נוספת:** נמצא את $X^{-1}=\begin{pmatrix}b&d\\0&b^{-1}\end{pmatrix}$ – לפי ההגדרה נדרוש ש" "\n"
    r"$$\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}\cdot\begin{pmatrix}b&d\\0&b^{-1}\end{pmatrix}=\begin{pmatrix}ab&ad+cb^{-1}\\0&a^{-1}b^{-1}\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$$" "\n"
    r"מכאן $b=a^{-1}$ ו-$ad+cb^{-1}=ad+ca=0$. קיבלנו ש-$d=-c$." "\n"
    r"הוכחנו ש-$H$ חבורה."
)

S4A2 = (
    r"לאיבר $a$ ישנן 4 אפשרויות: כל ערך מ-$\mathbb{Z}_5$ חוץ מ-0. בעוד שאיבר $c$ יכול לקבל כל ערך מ-$\mathbb{Z}_5$, כלומר יש לו 5 אפשרויות. לפי עקרון המכפלה, סדר החבורה $H$ הוא 20."
)

S4A3 = (
    r"מתקיים: $\begin{pmatrix}2&4\\0&2^{-1}\end{pmatrix}^{-1}=\begin{pmatrix}2&4\\0&3\end{pmatrix}^{-1}=\begin{pmatrix}3&-4\\0&2\end{pmatrix}=\begin{pmatrix}3&1\\0&2\end{pmatrix}$."
)

S4B = (
    r"נסדר את המקדמים במשוואות:" "\n"
    r"$$\begin{cases}x\equiv2\pmod8\\x\equiv4\pmod9\\x\equiv22\pmod{25}\end{cases}$$" "\n"
    r"נסמן: $m_1=8,\ m_2=9,\ m_3=25$ והם אכן זרים בזוגות. נסמן $m=m_1m_2m_3=8\cdot9\cdot25=1800$, ולכן $M_1=225,\ M_2=200,\ M_3=72$. לכן הפתרון למערכת הוא:" "\n"
    r"$$x=(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3)\bmod m=(2\cdot225\cdot x_1+4\cdot200\cdot x_2+22\cdot72\cdot x_3)\bmod1800$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$225x_1\equiv1\pmod8\Rightarrow x_1\equiv1\pmod8\Rightarrow x_1=1$$" "\n"
    r"$$200x_2\equiv1\pmod9\Rightarrow2x_2\equiv1\pmod9\Rightarrow x_2=5$$" "\n"
    r"$$72x_3\equiv1\pmod{25}\Rightarrow-3x_3\equiv1\pmod{25}\Rightarrow x_3=8$$" "\n"
    r"מכאן: $x=(2\cdot225\cdot1+4\cdot200\cdot5+22\cdot72\cdot8)\bmod1800=17122\bmod1800$, כלומר $x=922\bmod1800$." "\n"
    r"בדיקה: $922\equiv2\pmod8$, $922\equiv4\pmod9$, $922\equiv22\pmod{25}$."
)

S5A = (
    r"$$Q=\begin{pmatrix}-\frac23&-\frac1{\sqrt5}&-\frac4{3\sqrt5}\\-\frac13&\frac2{\sqrt5}&-\frac2{3\sqrt5}\\\frac23&0&-\frac{\sqrt5}3\end{pmatrix},\qquad P=\begin{pmatrix}-2&0&0\\0&7&0\\0&0&7\end{pmatrix},\qquad A=QPQ^T$$"
)

S5B = (
    r"נשתמש באי-שוויון קושי-שוורץ $|\vec x\cdot\vec y|\le\|\vec x\|\|\vec y\|$ עבור הוקטורים $\vec x=(x_1,x_2,\dots,x_n)$ ו-$\vec y=(1,1,\dots,1)$. אזי מתקיים:" "\n"
    r"$$\vec x\cdot\vec y=x_1+x_2+\dots+x_n\le\|\vec x\|\|\vec y\|=\sqrt{x_1^2+x_2^2+\dots+x_n^2}\ \sqrt{1+1+\dots+1}$$" "\n"
    r"$$1=x_1+x_2+\dots+x_n\le\sqrt{x_1^2+x_2^2+\dots+x_n^2}\ \sqrt n$$" "\n"
    r"$$\frac1{\sqrt n}\le\sqrt{x_1^2+x_2^2+\dots+x_n^2}\ \Rightarrow\ x_1^2+x_2^2+\dots+x_n^2\ge\frac1n$$"
)

questions = [
    Q(1, "computation", "least_squares",
      r"נתונות 5 נקודות במישור: $(1,4),\ (3,5),\ (5,6),\ (7,5),\ (9,8)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו במובן של הריבועים הפחותים. (10%)",
      S1A, part="א", points=10),
    Q(1, "computation", "projection",
      r"(15%) במרחב $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע\"י $\langle A,B\rangle=\mathrm{tr}\left(B^TA\right)$ לכל $A,B\in M_2(\mathbb{R})$. חשבו את ההיטל של $\vec v=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ על $\mathrm{Sp}\left\{\begin{pmatrix}1&-1\\0&1\end{pmatrix},\begin{pmatrix}0&1\\0&1\end{pmatrix},\begin{pmatrix}1&1\\1&1\end{pmatrix}\right\}$.",
      S1B, part="ב", points=15),

    Q(2, "proof", "groups", r"סעיף א.1. הראו כי $\odot$ היא פעולה בינארית על $\mathbb{R}^*$. (4%)", S2A1, part="א", points=4, contextId="c2"),
    Q(2, "truefalse", "groups", r"סעיף א.2. האם הפעולה אסוציאטיבית? (5%)", S2A2, part="ב", points=5, contextId="c2", verdict=False),
    Q(2, "truefalse", "groups", r"סעיף א.3. האם במבנה $(\mathbb{R}^*,\odot)$ קיים איבר ניטרלי? (5%)", S2A3, part="ג", points=5,
      contextId="c2", verdict=False),
    Q(2, "computation", "groups",
      r"סעיף א.4. האם קיים $x\in\mathbb{R}^*$ המקיים $x\odot x=x$ ? אם כן - מצאו אותו, אחרת - הוכיחו ש הוא לא קיים. (4%)", S2A4,
      part="ד", points=4, contextId="c2"),
    Q(2, "proof", "pos_def", r"סעיף ב.1. הוכיחו כי $A$ הפיכה. (3%)", S2B1, part="ה", points=3, contextId="c2b"),
    Q(2, "proof", "pos_def", r"סעיף ב.2. הוכיחו כי $A^{-1}$ מוגדרת חיובית לחלוטין. (4%)", S2B2, part="ו", points=4, contextId="c2b"),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}2a^2&a&0\\a&1&a\\0&a&2a^2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "proof", "cauchy_schwarz",
      r"(10%) יהיו $\vec u,\vec v\in\mathbb{R}^n$. הוכיחו כי $\langle\vec u,\vec v\rangle=0$ אם ורק אם $\|\vec u\|\le\|\vec u+t\vec v\|$ לכל $t\in\mathbb{R}$.",
      S3B, part="ב", points=10),

    Q(4, "proof", "groups", r"סעיף א.1. הוכיחו כי $H$ היא חבורה. (7%)", S4A1, part="א", points=7, contextId="c4"),
    Q(4, "computation", "groups", r"סעיף א.2. מהו הסדר של $H$ ? (4%)", S4A2, part="ב", points=4, contextId="c4"),
    Q(4, "computation", "groups",
      r"סעיף א.3. מצאו את האיבר ההופכי של $\begin{pmatrix}2&4\\0&2^{-1}\end{pmatrix}$ ב-$H$. **שימו לב: כל הרכיבים בתשובות אמורים להיות מ-$\{0,1,2,3,4\}$.** (6%)",
      S4A3, part="ג", points=6, contextId="c4"),
    Q(4, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}3x\equiv14\pmod8\\x\equiv4\pmod9\\x\equiv22\pmod{25}\end{cases}$. (8%)",
      S4B, part="ד", points=8),

    Q(5, "computation", "orthodiag", r"סעיף א. בצעו לכסון אורתוגונלי של המטריצה הבאה: $\begin{pmatrix}3&-2&4\\-2&6&2\\4&2&3\end{pmatrix}$. (17%)",
      S5A, part="א", points=17),
    Q(5, "proof", "cauchy_schwarz",
      r"סעיף ב. יהיו $x_1,x_2,\dots,x_n\in\mathbb{R}$ כך ש-$x_1+x_2+\cdots+x_n=1$. הוכיחו כי $x_1^2+x_2^2+\cdots+x_n^2\ge\dfrac1n$. (8%)",
      S5B, part="ב", points=8),
]

# ---- rubric / pitfalls / steps (ai-draft). Every expected value is recomputed by tools/verify/24A-B/steps_check.py ----
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
            q["rubricSource"] = "ai-verified"
            q["stepsSource"] = "ai-verified"
            assert sum(r["points"] for r in q["rubric"]) == q["points"], (n, part)
            return
    raise KeyError((n, part))


add(1, "א",
    rubric=rub(("הצבת הנקודות $y=mx+n$ ובניית המערכת $A\\vec x=\\vec b$ עם $A$ בעלת עמודות $x_i$ ו-1", 3),
               (r"משוואות נורמליות $A^TA\vec x=A^T\vec b$: $\begin{pmatrix}165&25\\25&5\end{pmatrix}$ ו-$\begin{pmatrix}156\\28\end{pmatrix}$", 4),
               ("פתרון המערכת: $m=0.4$ ו-$n=3.6$", 2),
               ("כתיבת הישר $y=0.4x+3.6$", 1)),
    pitfalls=["לנסות לפתור ישירות $A\\vec x=\\vec b$ (חמש משוואות בשני נעלמים), במקום המשוואות הנורמליות.",
              r"טעות חשבונית בסכומים $\sum x_i^2$ ו-$\sum x_iy_i$, ולכן במטריצה $A^TA$ ובווקטור $A^T\vec b$."],
    steps=[num(r"מהו הערך של $\sum x_i^2$ עבור $x=1,3,5,7,9$ (הכניסה השמאלית העליונה של $A^TA$)?", 165,
               "$1+9+25+49+81=165$."),
           num(r"מהו הערך של $\sum x_iy_i$ (הכניסה העליונה של $A^T\vec b$)?", 156, "$4+15+30+35+72=156$."),
           num(r"פתרו את $\begin{cases}165m+25n=156\\25m+5n=28\end{cases}$. מהו $m$?", 0.4,
               "מהמשוואה השנייה כפול 5 מחסרים: $40m=16$, ולכן $m=0.4$.", tol=1e-9),
           num("מהו $n$?", 3.6, "מ-$25m+5n=28$ עם $m=0.4$ נקבל $5n=18$ ולכן $n=3.6$.", tol=1e-9)],
    )

G1B = [r"$v_1=e_1$",
       r"$v_2=e_2-\frac{\langle e_2,v_1\rangle}{\langle v_1,v_1\rangle}v_1=e_2$",
       r"$v_3=e_3-\frac{\langle e_3,v_1\rangle}{\langle v_1,v_1\rangle}v_1-\frac{\langle e_3,v_2\rangle}{\langle v_2,v_2\rangle}v_2$, ומכפילים ב-3 להקלה",
       r"$\mathbf{proj}_W(\vec v)=\sum_{i=1}^3\frac{\langle\vec v,v_i\rangle}{\langle v_i,v_i\rangle}v_i$"]
add(1, "ב",
    rubric=rub(("תהליך גרם-שמידט: $v_1=e_1$ ו-$v_2=e_2$ (כי $\\langle e_2,v_1\\rangle=0$)", 4),
               (r"$v_3=\frac13\begin{pmatrix}2&1\\3&-1\end{pmatrix}$, ושימוש בכפולה $\begin{pmatrix}2&1\\3&-1\end{pmatrix}$", 4),
               ("שימוש בנוסחת ההיטל על בסיס אורתוגונלי עם המקדמים $1,\\ \\frac32,\\ \\frac25$", 4),
               (r"התשובה הסופית $\begin{pmatrix}\frac95&\frac9{10}\\\frac65&\frac{21}{10}\end{pmatrix}$", 3)),
    pitfalls=["להשתמש בנוסחת ההיטל עם בסיס שאינו אורתוגונלי (בלי גרם-שמידט קודם).",
              r"לחשב את המכפלה הפנימית $\mathrm{tr}(B^TA)$ בטעות כמכפלת מטריצות ולא כסכום מכפלות האיברים התואמים."],
    steps=[num(r"מהו $\langle e_2,v_1\rangle=\mathrm{tr}(v_1^Te_2)$ (סכום מכפלות האיברים התואמים)?", 0,
               "$0\\cdot1+1\\cdot(-1)+0\\cdot0+1\\cdot1=0$, ולכן $v_2=e_2$."),
           num(r"מהו $\langle e_3,v_1\rangle$?", 1, "$1\\cdot1+1\\cdot(-1)+1\\cdot0+1\\cdot1=1$, ו-$\\langle v_1,v_1\\rangle=3$."),
           num(r"במקדם של $v_3=\begin{pmatrix}2&1\\3&-1\end{pmatrix}$ בהיטל, מהו $\frac{\langle\vec v,v_3\rangle}{\langle v_3,v_3\rangle}$?", 0.4,
               "$\\langle\\vec v,v_3\\rangle=4+1+3-2=6$ ו-$\\langle v_3,v_3\\rangle=15$, ולכן $\\frac6{15}=\\frac25$.", tol=1e-9),
           num(r"מהי הכניסה הימנית העליונה של ההיטל?", 0.9, "$1\\cdot(-1)+\\frac32\\cdot1+\\frac25\\cdot1=0.9$.", tol=1e-9),
           order("סדרו את שלבי החישוב.", G1B, "כל וקטור תלוי בקודמים: $v_2$ ב-$v_1$, $v_3$ ב-$v_1,v_2$, וההיטל נחשב רק על הבסיס האורתוגונלי.")])

add(2, "א",
    rubric=rub(("$a,b>0\\Rightarrow a+b>0$", 1), ("$a,b>0\\Rightarrow ab>0$", 1),
               ("מנה של חיוביים חיובית, ולכן $a\\odot b\\in\\mathbb{R}^*$", 2)),
    pitfalls=["לבדוק רק דוגמה מספרית אחת במקום להוכיח לכל $a,b\\in\\mathbb{R}^*$.",
              "לבלבל בין סגירות לבין אסוציאטיביות: כאן נדרש רק שהתוצאה שייכת ל-$\\mathbb{R}^*$."],
    steps=[choice("מה צריך להראות כדי להוכיח ש-$\\odot$ היא פעולה בינארית על $\\mathbb{R}^*$?",
                  ["שלכל $a,b\\in\\mathbb{R}^*$ גם $a\\odot b\\in\\mathbb{R}^*$", "שלכל $a,b,c$ מתקיים $(a\\odot b)\\odot c=a\\odot(b\\odot c)$",
                   "שקיים $e$ עם $a\\odot e=a$", "שלכל $a$ קיים $b$ עם $a\\odot b=e$"], 0,
                  "פעולה בינארית פירושה סגירות: התוצאה נשארת בקבוצה. שאר האפשרויות הן אסוציאטיביות, איבר ניטרלי והופכי."),
           order("סדרו את שלבי ההוכחה.",
                 [r"יהיו $a,b\in\mathbb{R}^*$, כלומר $a,b>0$", r"אז $a+b>0$ וגם $ab>0$",
                  r"המנה $\frac{a+b}{ab}$ חיובית", r"לכן $a\odot b\in\mathbb{R}^*$"],
                 "כל שלב נשען על הקודם.")])

G2A2 = [r"$(a\odot b)\odot c=\frac{a+b+abc}{ac+bc}$", r"$a\odot(b\odot c)=\frac{abc+b+c}{ab+ac}$",
        "שני הביטויים שונים, ולכן הפעולה אינה אסוציאטיבית."]
add(2, "ב",
    rubric=rub(("חישוב $(a\\odot b)\\odot c=\\frac{a+b+abc}{ac+bc}$", 2), ("חישוב $a\\odot(b\\odot c)=\\frac{abc+b+c}{ab+ac}$", 2),
               ("מסקנה: הביטויים שונים ולכן הפעולה אינה אסוציאטיבית", 1)),
    pitfalls=["לטעון שהפעולה אסוציאטיבית כי היא חילופית ($a\\odot b=b\\odot a$): אלה תכונות שונות.",
              "לחשב רק אגף אחד ולהסיק מסקנה בלי להשוות."],
    steps=[num(r"הציבו $a=1,b=2,c=3$ בביטוי $\frac{a+b+abc}{ac+bc}$. מה התוצאה?", 1, "$\\frac{3+6}{3+6}=1$."),
           num(r"הציבו אותם ערכים בביטוי $\frac{abc+b+c}{ab+ac}$. מה התוצאה?", 2.2, "$\\frac{6+2+3}{2+3}=\\frac{11}5=2.2$, שונה מ-1.", tol=1e-9),
           findbug("בגרסה הבאה של הפתרון שורה אחת שגויה. מצאו אותה.", G2A2, 1,
                   r"$a\odot(b\odot c)=\frac{abc+a+c}{ab+ac}$",
                   "הצבת $b\\odot c=\\frac{b+c}{bc}$ נותנת במונה $abc+b+c$ ולא $abc+a+c$.")])

add(2, "ג",
    rubric=rub(("הגדרת איבר ניטרלי: $a\\odot e=a$ לכל $a$", 1), ("הפיכת המשוואה ל-$a+e=a^2e$", 1),
               ("הצבת $a=1$ וקבלת $1+e=e$, כלומר סתירה", 2), ("מסקנה: אין איבר ניטרלי", 1)),
    pitfalls=["לבדוק רק את $a\\odot e=a$ עבור $a$ אחד ולהסיק שיש איבר ניטרלי, בלי לבדוק את כל ה-$a$.",
              "להציב $e=1$ מתוך הרגל (איבר ניטרלי של כפל) בלי לבדוק ש-$1\\odot a=a$."],
    steps=[choice("לאיזו משוואה מגיעים מהדרישה $a\\odot e=a$?",
                  ["$a+e=a^2e$", "$a+e=ae$", "$a+e=a$", "$1+e=ae$"], 0,
                  "$\\frac{a+e}{ae}=a$, מכפילים ב-$ae$ ומקבלים $a+e=a^2e$."),
           num("כמה פתרונות $e\\in\\mathbb{R}^*$ יש למשוואה $1+e=e$ (המקרה $a=1$)?", 0, "המשוואה מצטמצמת ל-$1=0$, ולכן אין פתרון."),
           order("סדרו את שלבי ההוכחה שאין איבר ניטרלי.",
                 [r"נניח שקיים $e$ עם $a\odot e=a$ לכל $a$", r"אז $a+e=a^2e$ לכל $a$",
                  r"בפרט עבור $a=1$: $1+e=e$, כלומר $1=0$", "סתירה, ולכן אין איבר ניטרלי"],
                 "ההצבה $a=1$ אפשרית רק אחרי שהגענו למשוואה.")])

add(2, "ד",
    rubric=rub(("חישוב $x\\odot x=\\frac{2x}{x^2}=\\frac2x$", 2), ("פתרון $\\frac2x=x$ ולכן $x^2=2$", 1), ("בחירת השורש החיובי $x=\\sqrt2\\in\\mathbb{R}^*$", 1)),
    pitfalls=["לכתוב $x=\\pm\\sqrt2$ ולשכוח ש-$-\\sqrt2\\notin\\mathbb{R}^*$.",
              "לצמצם את $x$ בלי לציין ש-$x\\ne0$ (כאן $x>0$)."],
    steps=[choice("מהו $x\\odot x$ לכל $x\\in\\mathbb{R}^*$?", ["$\\frac2x$", "$2x$", "$\\frac x2$", "$\\frac1x$"], 0,
                  "$x\\odot x=\\frac{x+x}{x\\cdot x}=\\frac{2x}{x^2}=\\frac2x$."),
           num("מהו הפתרון $x\\in\\mathbb{R}^*$ של $x\\odot x=x$? (תשובה עשרונית)", 1.41421356, "$\\frac2x=x$ נותן $x^2=2$, ורק $x=\\sqrt2>0$ שייך ל-$\\mathbb{R}^*$.", tol=1e-6)])

add(2, "ה",
    rubric=rub(("$A$ מוגדרת חיובית לחלוטין, ולכן כל ערכיה העצמיים חיוביים", 1), ("בפרט $0$ אינו ערך עצמי", 1), ("מטריצה ללא ערך עצמי $0$ הפיכה", 1)),
    pitfalls=["להסתמך על כך ש-$A$ סימטרית בלבד: מטריצה סימטרית יכולה להיות לא הפיכה.",
              "לבלבל בין מוגדרת חיובית לחלוטין לבין מוגדרת חיובית (שמאפשרת ערך עצמי $0$)."],
    steps=[choice("איזו עובדה על הערכים העצמיים של $A$ מבטיחה ש-$A$ הפיכה?",
                  ["$0$ אינו ערך עצמי של $A$", "$0$ הוא ערך עצמי של $A$", "כל הערכים העצמיים של $A$ שווים זה לזה", "כל הערכים העצמיים של $A$ שלמים"], 0,
                  "ערך עצמי $0$ פירושו $A\\vec v=\\vec0$ עם $\\vec v\\ne\\vec0$, ואז $A$ לא הפיכה. שוויון או שלמות של הערכים העצמיים אינם קשורים להפיכות."),
           order("סדרו את שלבי ההוכחה.",
                 [r"$A$ מוגדרת חיובית לחלוטין, ולכן כל ערכיה העצמיים חיוביים", r"בפרט $0$ אינו ערך עצמי של $A$", r"לכן $A$ הפיכה"],
                 "כל שלב נובע מהקודם.")])

G2B2 = [r"יהי $\lambda$ ערך עצמי של $A^{-1}$ עם וקטור עצמי $\vec v\ne\vec0$: $A^{-1}\vec v=\lambda\vec v$",
        r"נכפיל ב-$A$ משמאל: $\vec v=\lambda A\vec v$",
        r"$\lambda\ne0$, אחרת $\vec v=\vec0$",
        r"$A\vec v=\frac1\lambda\vec v$, כלומר $\frac1\lambda$ ערך עצמי של $A$",
        r"$\frac1\lambda>0$ ולכן $\lambda>0$"]
add(2, "ו",
    rubric=rub(("$A^{-1}$ סימטרית: $(A^{-1})^T=(A^T)^{-1}=A^{-1}$", 1), ("הוכחה ש-$\\lambda\\ne0$", 1),
               ("$\\frac1\\lambda$ ערך עצמי של $A$", 1), ("$\\frac1\\lambda>0$ ולכן $\\lambda>0$, ומסקנה", 1)),
    pitfalls=["לבדוק רק שהערכים העצמיים חיוביים ולשכוח לבדוק ש-$A^{-1}$ סימטרית.",
              "לטעון ש-$\\lambda$ ערך עצמי של $A^{-1}$ בלי להראות ש-$\\lambda\\ne0$ לפני החילוק."],
    steps=[choice("לפי הפתרון הרשמי, מה מראים כדי להוכיח ש-$A^{-1}$ מוגדרת חיובית לחלוטין?",
                  ["שהיא סימטרית ושכל ערכיה העצמיים חיוביים", "שרק עקבתה חיובית", "שרק הדטרמיננטה שלה חיובית", "שהיא הפיכה"], 0,
                  "העקבה לבדה לא מספיקה ($\\mathrm{diag}(3,-1)$), ודטרמיננטה חיובית לבדה לא מספיקה ($\\mathrm{diag}(-1,-1)$), והפיכות לא מבטיחה חיוביות."),
           order("סדרו את הוכחת החיוביות של הערכים העצמיים של $A^{-1}$.", G2B2, "כל שלב משתמש בקודם; החילוק ב-$\\lambda$ מותר רק אחרי שהראינו $\\lambda\\ne0$."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G2B2, 3,
                   r"$A\vec v=\lambda\vec v$, כלומר $\lambda$ ערך עצמי של $A$",
                   "מ-$\\vec v=\\lambda A\\vec v$ מקבלים $A\\vec v=\\frac1\\lambda\\vec v$ ולא $\\lambda\\vec v$.")])

add(3, "א",
    rubric=rub(("חישוב הערכים העצמיים $2a^2,\\ 2a^2+1,\\ 0$", 6), ("שהערך העצמי $0$ מופיע לכל $a$ (הדטרמיננטה אפס)", 3),
               ("כל הערכים העצמיים אי-שליליים, ולכן מוגדרת חיובית לכל $a$", 3), ("אין $a$ שעבורו חיובית לחלוטין, שלילית או שלילית לחלוטין", 3)),
    pitfalls=["להסיק שהמטריצה מוגדרת חיובית לחלוטין לכל $a\\ne0$, ולשכוח שתמיד יש ערך עצמי $0$.",
              "לבדוק רק את המינורים הראשיים ולא את כל הערכים העצמיים (או לבלבל בין $\\ge0$ ל-$>0$)."],
    steps=[num(r"מהי הדטרמיננטה של $\begin{pmatrix}2a^2&a&0\\a&1&a\\0&a&2a^2\end{pmatrix}$ עבור $a=1$?", 0, "הדטרמיננטה היא $0$ לכל $a$, כי $0$ ערך עצמי."),
           num("מהו הערך העצמי $2a^2+1$ עבור $a=2$?", 9, "$2\\cdot4+1=9$."),
           choice("איזה סיווג נכון למטריצה?",
                  ["מוגדרת חיובית לכל $a$, ואינה מוגדרת חיובית לחלוטין לאף $a$", "מוגדרת חיובית לחלוטין לכל $a\\ne0$",
                   "מוגדרת חיובית לחלוטין לכל $a$", "מוגדרת שלילית לכל $a$"], 0,
                  "הערכים העצמיים $2a^2,2a^2+1,0$ אי-שליליים, ו-$0$ תמיד מופיע, ולכן אין חיוביות לחלוטין.")])

G3B = [r"$\|\vec u+t\vec v\|^2=\|\vec u\|^2+2t\langle\vec u,\vec v\rangle+t^2\|\vec v\|^2\ge\|\vec u\|^2$",
       r"$2t\langle\vec u,\vec v\rangle+t^2\|\vec v\|^2\ge0$ לכל $t$",
       r"$-2t\langle\vec u,\vec v\rangle\le t^2\|\vec v\|^2$ לכל $t$",
       r"$|\langle\vec u,\vec v\rangle|\le\frac{|t|}2\|\vec v\|^2$ לכל $t$",
       r"נשאיף $t\to0$ ונקבל $\langle\vec u,\vec v\rangle=0$"]
add(3, "ב",
    rubric=rub(("פתיחת $\\|\\vec u+t\\vec v\\|^2=\\|\\vec u\\|^2+2t\\langle\\vec u,\\vec v\\rangle+t^2\\|\\vec v\\|^2$", 3),
               ("כיוון ראשון: אם $\\langle\\vec u,\\vec v\\rangle=0$ אז $\\|\\vec u+t\\vec v\\|^2\\ge\\|\\vec u\\|^2$", 2),
               ("כיוון שני: קבלת $2t\\langle\\vec u,\\vec v\\rangle+t^2\\|\\vec v\\|^2\\ge0$ לכל $t$", 2),
               ("שימוש בכך שהאי-שוויון נכון גם ל-$t$ חיובי וגם שלילי וקרוב ל-0, והסקת $\\langle\\vec u,\\vec v\\rangle=0$", 3)),
    pitfalls=["להוכיח רק כיוון אחד של ה'אם ורק אם'.",
              "לבחור $t$ קבוע אחד במקום להשתמש בכך שהאי-שוויון נכון לכל $t$ (כולל $t$ שליליים וקרובים ל-0)."],
    steps=[choice("מהו הפיתוח של $\\|\\vec u+t\\vec v\\|^2$?",
                  ["$\\|\\vec u\\|^2+2t\\langle\\vec u,\\vec v\\rangle+t^2\\|\\vec v\\|^2$", "$\\|\\vec u\\|^2+t^2\\|\\vec v\\|^2$",
                   "$\\|\\vec u\\|^2+2t\\|\\vec u\\|\\|\\vec v\\|+t^2\\|\\vec v\\|^2$", "$\\|\\vec u\\|^2+t\\langle\\vec u,\\vec v\\rangle+t\\|\\vec v\\|^2$"], 0,
                  "פותחים את המכפלה הפנימית $\\langle\\vec u+t\\vec v,\\vec u+t\\vec v\\rangle$. הביטוי $\\|\\vec u\\|^2+t^2\\|\\vec v\\|^2$ נכון רק כאשר $\\langle\\vec u,\\vec v\\rangle=0$, והביטוי עם $2t\\|\\vec u\\|\\|\\vec v\\|$ נכון רק כאשר הווקטורים באותו כיוון."),
           order("סדרו את הכיוון השני של ההוכחה.", G3B, "כל שורה נובעת מהקודמת; ההשאפה $t\\to0$ באה אחרונה."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G3B, 1,
                   r"$2t\langle\vec u,\vec v\rangle+t\|\vec v\|^2\ge0$ לכל $t$",
                   "מהפיתוח בשורה הקודמת האיבר האחרון הוא $t^2\\|\\vec v\\|^2$ ולא $t\\|\\vec v\\|^2$.")])

G4A1 = [r"סגירות: $\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}\begin{pmatrix}b&d\\0&b^{-1}\end{pmatrix}=\begin{pmatrix}ab&ad+cb^{-1}\\0&a^{-1}b^{-1}\end{pmatrix}\in H$",
        "אסוציאטיביות: כפל מטריצות אסוציאטיבי",
        r"איבר ניטרלי: $I\in H$",
        r"הופכי: $\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}^{-1}=\begin{pmatrix}a^{-1}&-c\\0&a\end{pmatrix}\in H$"]
add(4, "א",
    rubric=rub(("סגירות: חישוב המכפלה ושהיא מהצורה של $H$", 2), ("אסוציאטיביות מכפל מטריצות", 1), ("איבר ניטרלי $I\\in H$", 1),
               ("מציאת ההופכי $\\begin{pmatrix}a^{-1}&-c\\\\0&a\\end{pmatrix}$", 2), ("בדיקה שההופכי שייך ל-$H$ ומסקנה", 1)),
    pitfalls=["לשכוח לבדוק שהאלכסון במכפלה ובהופכי עדיין מקיים 'האיבר התחתון הוא ההופכי של העליון'.",
              "לחשב את ההופכי בלי להפחית מודולו 5, או לשכוח את הסימן ב-$-c$."],
    steps=[choice("מהו ההופכי של $\\begin{pmatrix}a&c\\\\0&a^{-1}\\end{pmatrix}$ ב-$H$?",
                  [r"$\begin{pmatrix}a^{-1}&-c\\0&a\end{pmatrix}$", r"$\begin{pmatrix}a^{-1}&c\\0&a\end{pmatrix}$",
                   r"$\begin{pmatrix}a&-c\\0&a^{-1}\end{pmatrix}$", r"$\begin{pmatrix}a^{-1}&0\\-c&a\end{pmatrix}$"], 0,
                  "הדטרמיננטה היא 1, ולכן ההופכי הוא $\\begin{pmatrix}a^{-1}&-c\\\\0&a\\end{pmatrix}$; בשאר האפשרויות המכפלה אינה $I$."),
           num(r"עבור $a=2,c=1,b=2,d=3$ ב-$\mathbb{Z}_5$, מהי הכניסה הימנית העליונה $ad+cb^{-1}$ במכפלה (מודולו 5)?", 4,
               "$b^{-1}=3$, ולכן $2\\cdot3+1\\cdot3=9\\equiv4\\pmod5$."),
           findbug("בגרסה הבאה של ההוכחה שורה אחת שגויה. מצאו אותה.", G4A1, 3,
                   r"הופכי: $\begin{pmatrix}a&c\\0&a^{-1}\end{pmatrix}^{-1}=\begin{pmatrix}a^{-1}&c\\0&a\end{pmatrix}\in H$",
                   "עם $+c$ המכפלה היא $\\begin{pmatrix}1&2ac\\\\0&1\\end{pmatrix}$, שאינה $I$ כאשר $c\\ne0$; ההופכי הנכון הוא עם $-c$.")])

add(4, "ב",
    rubric=rub(("לאיבר $a$ יש 4 אפשרויות ($\\mathbb{Z}_5$ בלי 0)", 2), ("לאיבר $c$ יש 5 אפשרויות", 1), ("עקרון המכפלה: $4\\cdot5=20$", 1)),
    pitfalls=["לספור 5 אפשרויות ל-$a$ ולשכוח ש-$a\\ne0$.", "לספור גם את התא התחתון כבחירה חופשית, אף שהוא נקבע לפי $a^{-1}$."],
    steps=[num("כמה ערכים אפשריים יש ל-$a$ (כל $a\\in\\mathbb{Z}_5$ שאינו 0)?", 4, "הערכים 1,2,3,4."),
           num("מהו הסדר של $H$?", 20, "$4\\cdot5=20$, כי $a$ ו-$c$ נבחרים בנפרד והתא התחתון נקבע.")])

add(4, "ג",
    rubric=rub(("חישוב $2^{-1}=3$ ב-$\\mathbb{Z}_5$ ולכן המטריצה היא $\\begin{pmatrix}2&4\\\\0&3\\end{pmatrix}$", 2), ("שימוש בנוסחת ההופכי של $H$: $\\begin{pmatrix}a^{-1}&-c\\\\0&a\\end{pmatrix}$", 2),
               ("חישוב $-4\\equiv1\\pmod5$", 1), ("התשובה $\\begin{pmatrix}3&1\\\\0&2\\end{pmatrix}$", 1)),
    pitfalls=["להשאיר $-4$ בתשובה, אף שהרכיבים אמורים להיות מ-$\\{0,1,2,3,4\\}$.", "לטעות בהופכי של 2 ב-$\\mathbb{Z}_5$ (הוא 3, כי $2\\cdot3=6\\equiv1$)."],
    steps=[num("מהו $2^{-1}$ ב-$\\mathbb{Z}_5$?", 3, "$2\\cdot3=6\\equiv1\\pmod5$."),
           num("מהי הכניסה הימנית העליונה של ההופכי, $-c$ עבור $c=4$, מודולו 5 (ערך בין 0 ל-4)?", 1, "$-4\\equiv1\\pmod5$."),
           num("מהי הכניסה הימנית התחתונה של ההופכי?", 2, "היא $a=2$.")])

add(4, "ד",
    rubric=rub(("העברת המשוואה הראשונה ל-$x\\equiv2\\pmod8$", 2), ("חישוב $m=1800$ ו-$M_1=225,\\ M_2=200,\\ M_3=72$", 2),
               ("חישוב ההופכיים $x_1=1,\\ x_2=5,\\ x_3=8$", 2), ("הצבה בנוסחה: $x\\equiv922\\pmod{1800}$", 2)),
    pitfalls=["להשאיר את $3x\\equiv14$ בלי לפשט ל-$x\\equiv2\\pmod8$ (3 הפיך מודולו 8).", "לחשב הופכי כפלי שגוי, כמו $72x\\equiv1\\pmod{25}$, ולקבל פתרון שאינו מקיים את המערכת."],
    steps=[num("מהו $x$ מודולו 8 מתוך $3x\\equiv14\\pmod8$ (ערך בין 0 ל-7)?", 2, "$3\\cdot2=6\\equiv14\\pmod8$, ו-3 הפיך מודולו 8."),
           num("מהו $M_2=\\frac{1800}{9}$?", 200, "$1800/9=200$."),
           num("מהו $x_3$ המקיים $72x_3\\equiv1\\pmod{25}$ (ערך בין 0 ל-24)?", 8, "$72\\equiv-3$, ו-$-3\\cdot8=-24\\equiv1\\pmod{25}$."),
           num("מהו הפתרון $x$ מודולו 1800 (ערך בין 0 ל-1799)?", 922, "$17122\\bmod1800=922$.")])

add(5, "א",
    rubric=rub(("חישוב הערכים העצמיים $-2,7,7$", 4), ("וקטור עצמי ל-$-2$, למשל $(2,1,-2)$", 3), ("בסיס אורתוגונלי למרחב העצמי של 7 (גרם-שמידט)", 4),
               ("נרמול העמודות לקבלת $Q$ אורתוגונלית", 3), ("כתיבת $A=QPQ^T$ עם $P=\\mathrm{diag}(-2,7,7)$", 3)),
    pitfalls=["לקחת שני וקטורים עצמיים של $\\lambda=7$ שאינם אורתוגונליים זה לזה בלי לבצע גרם-שמידט.", "לשכוח לנרמל את העמודות של $Q$, כך ש-$Q^TQ\\ne I$."],
    steps=[num("מהו הערך העצמי השלילי של המטריצה?", -2, "הפולינום האופייני הוא $(\\lambda+2)(\\lambda-7)^2$."),
           num("מהי הריבוי האלגברי של הערך העצמי 7?", 2, "הערכים העצמיים הם $-2,7,7$."),
           num("מהו האורך $\\|(2,1,-2)\\|$ של הווקטור העצמי של $-2$ (לפני הנרמול)?", 3, "$\\sqrt{4+1+4}=3$, ולכן העמודה בנורמה 1 היא $\\frac13(2,1,-2)$ עד כדי סימן.")])

G5B = [r"$1=\sum x_i=\vec x\cdot\vec y\le\|\vec x\|\|\vec y\|$ עבור $\vec y=(1,\dots,1)$ (קושי-שוורץ)",
       r"$\|\vec y\|=\sqrt n$, ולכן $1\le\sqrt{\sum x_i^2}\sqrt n$",
       r"$\frac1{\sqrt n}\le\sqrt{\sum x_i^2}$",
       r"נעלה בריבוע: $\sum x_i^2\ge\frac1n$"]
add(5, "ב",
    rubric=rub(("בחירת $\\vec y=(1,1,\\dots,1)$ ושימוש באי-שוויון קושי-שוורץ", 3), ("חישוב $\\vec x\\cdot\\vec y=1$ ו-$\\|\\vec y\\|=\\sqrt n$", 2),
               ("חילוק ב-$\\sqrt n$", 1), ("העלאה בריבוע וקבלת $\\sum x_i^2\\ge\\frac1n$", 2)),
    pitfalls=["להעלות בריבוע לפני חילוק ב-$\\sqrt n$ ולקבל $\\frac1n$ במקום $\\frac1{\\sqrt n}$ בשורה הביניים.", "לבחור וקטור $\\vec y$ שאינו מניב את הסכום $x_1+\\dots+x_n$ במכפלה הפנימית."],
    steps=[choice("באיזה וקטור $\\vec y$ משתמש הפתרון הרשמי יחד עם $\\vec x=(x_1,\\dots,x_n)$ באי-שוויון קושי-שוורץ?",
                  ["$(1,1,\\dots,1)$", "$(x_1^2,\\dots,x_n^2)$", "$(1,2,\\dots,n)$", "$(0,\\dots,0,1)$"], 0,
                  "עם $\\vec y=(1,\\dots,1)$ המכפלה $\\vec x\\cdot\\vec y$ היא הסכום $x_1+\\dots+x_n=1$."),
           num("עבור $n=4$, מהו $\\|\\vec y\\|$ של $\\vec y=(1,1,1,1)$?", 2, "$\\sqrt4=2$."),
           order("סדרו את שלבי ההוכחה.", G5B, "כל שורה נובעת מהקודמת, והעלאה בריבוע (בשני אגפים אי-שליליים) באה אחרונה."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G5B, 2, r"$\frac1n\le\sqrt{\sum x_i^2}$",
                   "חילוק של $1\\le\\sqrt n\\sqrt{\\sum x_i^2}$ ב-$\\sqrt n$ נותן $\\frac1{\\sqrt n}$ ולא $\\frac1n$.")])

exam = {
    "examCode": "24A-B",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ד מועד ב'",
    "year": 2024,
    "examDate": "21.4.2024",
    "sourceFile": "algebra-2-24A-B-exam",
    "solutionFile": "algebra-2-24A-B-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
