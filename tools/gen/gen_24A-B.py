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
