# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-A.json -- algebra-2 (20079), semester A 2023, moed A (29.01.2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-A.py

Source: exam 2 pp. + typed official solution 8 pp. (both read from the rendered pages). Header: "4 of 5", 25% each;
all 5 questions are transcribed, 13 items (12 shipped + 1 held).

Part letters: single-letter parts only, so numbered sub-parts get letters in order.
  Q3: a, b.1 -> b, b.2 -> c (the printed "b" setup is a context).   Q4: a.1, a.2, a.3, b -> a, b, c, d.
  Every question text starts with its printed label.

Typos in the official solution (checked with tools/verify/23A-A/check.py; no FINAL answer is wrong):
- Q1a: the boxed slope "a = 21.5" and "y(x) = 21.5x + 16" are slips: the slope is 43/10 (21.5 is 5a, the term
  actually added to b at x = 5). The printed y(5) = 37.5 is right. Written with a = 4.3.
- Q1b: the printed middle matrix of the second trace is (2 -2; 3 2); u2^T v is (2 -2; 4 2). Trace (4) unchanged.
- Q2a / Q4b: transcribed as printed (Q2a does not argue that <f,f> = 0 forces f = 0; Q4b drops absolute values
  before squaring). No answer changes.
HOLD: Q5a (SVD of a 3x2 matrix). The "solution" is a link to an online SVD calculator and no worked answer, so there
  is no key: hold "no-key" (the orchestrator routes it to the solver).
Checks: tools/verify/23A-A/check.py (sympy + brute force), all OK.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-A.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ------------------------------------------------------------------ contexts
CTX = {
    "c3": {"kind": "text", "title": "שאלה 3 סעיף ב",
           "text": r"יהי $V$ מרחב מכפלה פנימית ממשי ותהי $\{\vec u,\vec v,\vec w\}\subset V$ מערכת אורתונורמלית. נסמן: $\vec\alpha=\vec u+2\vec v+\vec w$ , $\ \vec\beta=\vec u-\vec w$."},
    "c4": {"kind": "text", "title": "שאלה 4 סעיף א",
           "text": r"נתון מבנה אלגברי $\left(\mathbb{R}^2\setminus\{(0,0)\},\ *\right)$, כאשר הפעולה $*$ מוגדרת באופן הבא: $\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ay+bx\\by\end{pmatrix}$ לכל $\begin{pmatrix}a\\b\end{pmatrix},\begin{pmatrix}x\\y\end{pmatrix}\in\mathbb{R}^2\setminus\{(0,0)\}$."},
}

# ------------------------------------------------------------------ solutions
S1A = (
    "יש לנו מידע על מספר התלמידים הפונים בכל שבוע. ניתן לארגן זאת כך:" "\n"
    r"$$\begin{array}{c|c}x&y\\\hline1&20\\2&24\\3&31\\4&32\\5&?\end{array}$$" "\n"
    r"שרטוט הנקודות במישור מתאים למודל לינארי מהצורה: $y=ax+b$." "\n"
    r"$$\begin{pmatrix}1&1\\2&1\\3&1\\4&1\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}20\\24\\31\\32\end{pmatrix}\ \Rightarrow\ \begin{pmatrix}1&2&3&4\\1&1&1&1\end{pmatrix}\begin{pmatrix}1&1\\2&1\\3&1\\4&1\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}30&10\\10&4\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}1&2&3&4\\1&1&1&1\end{pmatrix}\begin{pmatrix}20\\24\\31\\32\end{pmatrix}=\begin{pmatrix}289\\107\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\left(\begin{array}{cc|c}30&10&289\\10&4&107\end{array}\right)\xrightarrow{3R_2-R_1\to R_2}\left(\begin{array}{cc|c}30&10&289\\0&2&32\end{array}\right)\xrightarrow{\frac12R_2\to R_2}\left(\begin{array}{cc|c}30&10&289\\0&1&16\end{array}\right)\Rightarrow b=16\ \Rightarrow\ a=4.3$$" "\n"
    "נציב ונקבל:" "\n"
    r"$$y(x)=4.3x+16\ \Rightarrow\ y(x=5)=37.5$$" "\n"
    "לפי המודל הזה, מספר הסטודנטים שהגיעו בשבוע החמישי הוא 37 (עיגול למטה) או 38 (עיגול למעלה)."
)

S1B = (
    r"המכפלה הפנימית הוגדרה כך: $\langle A,B\rangle=\mathrm{tr}(B^TA)$ לכל $A,B\in M_2(\mathbb{R})$. נגדיר תת מרחב" "\n"
    r"$$W=\mathrm{Sp}\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}1&3\\1&1\end{pmatrix}\right\}=\mathrm{Sp}\{\vec w_1,\vec w_2\}\ ,\qquad W\subset M_2(\mathbb{R})$$" "\n"
    r"נבדוק אם $\vec w_1\perp\vec w_2$:" "\n"
    r"$$\langle\vec w_1,\vec w_2\rangle=\mathrm{tr}\left(\begin{pmatrix}1&3\\1&1\end{pmatrix}^T\begin{pmatrix}1&1\\0&0\end{pmatrix}\right)=\mathrm{tr}\left(\begin{pmatrix}1&1\\3&1\end{pmatrix}\begin{pmatrix}1&1\\0&0\end{pmatrix}\right)=\mathrm{tr}\left(\begin{pmatrix}1&1\\3&3\end{pmatrix}\right)=4\ne0$$" "\n"
    r"משמע הם לא מאונכים זה לזה. נבנה בסיס אורתוגונלי ל-$W$ ע״י תהליך גרם-שמידט. נבחר $\vec u_1=\begin{pmatrix}1&1\\0&0\end{pmatrix}$. אז" "\n"
    r"$$\vec u_2=\vec w_2-\frac{\langle\vec w_2,\vec u_1\rangle}{\langle\vec u_1,\vec u_1\rangle}\vec u_1=\begin{pmatrix}1&3\\1&1\end{pmatrix}-\frac42\begin{pmatrix}1&1\\0&0\end{pmatrix}=\begin{pmatrix}-1&1\\1&1\end{pmatrix}$$" "\n"
    r"לפיכך, ההיטל של $\vec v=\begin{pmatrix}1&2\\3&0\end{pmatrix}$ על $W$ הוא:" "\n"
    r"$$\mathrm{proj}_W\begin{pmatrix}1&2\\3&0\end{pmatrix}=\frac{\left\langle\begin{pmatrix}1&2\\3&0\end{pmatrix},\begin{pmatrix}1&1\\0&0\end{pmatrix}\right\rangle}{\left\|\begin{pmatrix}1&1\\0&0\end{pmatrix}\right\|^2}\begin{pmatrix}1&1\\0&0\end{pmatrix}+\frac{\left\langle\begin{pmatrix}1&2\\3&0\end{pmatrix},\begin{pmatrix}-1&1\\1&1\end{pmatrix}\right\rangle}{\left\|\begin{pmatrix}-1&1\\1&1\end{pmatrix}\right\|^2}\begin{pmatrix}-1&1\\1&1\end{pmatrix}$$" "\n"
    r"$$=\frac{\mathrm{tr}\left(\begin{pmatrix}1&0\\1&0\end{pmatrix}\begin{pmatrix}1&2\\3&0\end{pmatrix}\right)}{\mathrm{tr}\left(\begin{pmatrix}1&0\\1&0\end{pmatrix}\begin{pmatrix}1&1\\0&0\end{pmatrix}\right)}\begin{pmatrix}1&1\\0&0\end{pmatrix}+\frac{\mathrm{tr}\left(\begin{pmatrix}-1&1\\1&1\end{pmatrix}\begin{pmatrix}1&2\\3&0\end{pmatrix}\right)}{\mathrm{tr}\left(\begin{pmatrix}-1&1\\1&1\end{pmatrix}\begin{pmatrix}-1&1\\1&1\end{pmatrix}\right)}\begin{pmatrix}-1&1\\1&1\end{pmatrix}$$" "\n"
    r"$$=\frac{\mathrm{tr}\begin{pmatrix}1&2\\1&2\end{pmatrix}}{\mathrm{tr}\begin{pmatrix}1&1\\1&1\end{pmatrix}}\begin{pmatrix}1&1\\0&0\end{pmatrix}+\frac{\mathrm{tr}\begin{pmatrix}2&-2\\4&2\end{pmatrix}}{\mathrm{tr}\begin{pmatrix}2&0\\0&2\end{pmatrix}}\begin{pmatrix}-1&1\\1&1\end{pmatrix}=\frac32\begin{pmatrix}1&1\\0&0\end{pmatrix}+\frac44\begin{pmatrix}-1&1\\1&1\end{pmatrix}=\frac12\begin{pmatrix}1&5\\2&2\end{pmatrix}$$"
)

S2A = (
    r"אנחנו נראה ש-$\langle f,g\rangle=\int_0^1e^xf(x)g(x)\,dx$ אכן מגדירה מכפלה פנימית במרחב $C[0,1]$." "\n"
    r"עבור $\langle f,f\rangle=\int_0^1e^xf^2(x)\,dx$, האינטגרנד $e^xf^2(x)$ תמיד אי-שלילי, מלבד במקרה שבו $f(x)=0$, ולכן מתקיים $\langle f,f\rangle=\|f\|^2\ge0$ לכל $f\in C[0,1]$." "\n"
    r"כמו-כן, מתקיים לכל $f,g,h\in C[0,1]$: $\langle f,g\rangle=\int_0^1e^xf(x)g(x)\,dx=\int_0^1e^xg(x)f(x)\,dx=\langle g,f\rangle$, וכן" "\n"
    r"$$\langle f+h,g\rangle=\int_0^1e^x\big(f(x)+h(x)\big)g(x)\,dx=\int_0^1e^x\big(f(x)g(x)+h(x)g(x)\big)dx$$" "\n"
    r"$$=\int_0^1e^xf(x)g(x)\,dx+\int_0^1e^xh(x)g(x)\,dx=\langle f,g\rangle+\langle h,g\rangle$$" "\n"
    r"לבסוף, מתקיים לכל $\alpha\in\mathbb{R}$ ולכל $f\in C[0,1]$:" "\n"
    r"$$\langle\alpha f,g\rangle=\int_0^1e^x\big(\alpha f(x)\big)g(x)\,dx=\alpha\int_0^1e^xf(x)g(x)\,dx=\alpha\langle f,g\rangle$$"
)

S2B = (
    r"החבורה $H=\left\{\begin{pmatrix}4&0\\0&3\end{pmatrix}^n\ \middle|\ n\in\mathbb{Z}\right\}$ הינה תת חבורה ציקלית של $G$. נמצא את הסדר של $H$ ע״י מיפוי איבריה." "\n"
    r"נבחין שהאיבר הניטרלי של $G$ ביחס לפעולה של כפל מטריצות הוא מטריצת היחידה, $e=\begin{pmatrix}1&0\\0&1\end{pmatrix}$. לפי הגדרה, $\begin{pmatrix}4&0\\0&3\end{pmatrix}^0=\begin{pmatrix}1&0\\0&1\end{pmatrix}$. נחשב את הערכים הבאים:" "\n"
    r"$$\begin{pmatrix}4&0\\0&3\end{pmatrix}^1=\begin{pmatrix}4&0\\0&3\end{pmatrix},\quad\begin{pmatrix}4&0\\0&3\end{pmatrix}^2=\begin{pmatrix}4^2\ (\mathrm{mod}\ 5)&0\\0&3^2\ (\mathrm{mod}\ 5)\end{pmatrix}=\begin{pmatrix}1&0\\0&4\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}4&0\\0&3\end{pmatrix}^3=\begin{pmatrix}4^3\ (\mathrm{mod}\ 5)&0\\0&3^3\ (\mathrm{mod}\ 5)\end{pmatrix}=\begin{pmatrix}4&0\\0&2\end{pmatrix},\quad\begin{pmatrix}4&0\\0&3\end{pmatrix}^4=\begin{pmatrix}4^4\ (\mathrm{mod}\ 5)&0\\0&3^4\ (\mathrm{mod}\ 5)\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$$" "\n"
    "לפיכך" "\n"
    r"$$H=\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}4&0\\0&3\end{pmatrix},\begin{pmatrix}1&0\\0&4\end{pmatrix},\begin{pmatrix}4&0\\0&2\end{pmatrix}\right\}\ \Rightarrow\ |H|=4$$"
)

S3A = (
    r"נמצא את הע״ע:" "\n"
    r"$$0=|xI-A|=\begin{vmatrix}x-a&0&-1\\0&x-2a&0\\-1&0&x-a\end{vmatrix}=(x-2a)\begin{vmatrix}x-a&-1\\-1&x-a\end{vmatrix}=(x-2a)\left((x-a)^2-1\right)=(x-2a)(x-a-1)(x-a+1)$$" "\n"
    r"כלומר, יש שלושה ערכים עצמיים: $2a,\ a-1,\ a+1$." "\n"
    r"בשביל שהמטריצה תהיה מוגדרת חיובית לחלוטין, כולם צריכים להיות חיוביים: $0<2a,\ a-1,\ a+1$, כלומר: $1<a$." "\n"
    r"באופן דומה, המטריצה מוגדרת חיובית כאשר: $1\le a$." "\n"
    r"מצד שני, המטריצה שלילית לחלוטין כאשר כולם שליליים: $0>2a,\ a-1,\ a+1$, כלומר: $-1>a$." "\n"
    r"באופן דומה, המטריצה מוגדרת שלילית כאשר $-1\ge a$." "\n"
    r"הערכים שנותרו - ומתאימים למטריצה שאינה חיובית, שלילית וכו' - הם $-1<a<1$."
)

S3B1 = (
    "נבדוק האם המכפלה מתאפסת:" "\n"
    r"$$\langle\vec\alpha,\vec\beta\rangle=\langle\vec u+2\vec v+\vec w,\ \vec u-\vec w\rangle=$$" "\n"
    "נפתח לפי תכונות הלינאריות והסימטריות ונקבל:" "\n"
    r"$$\langle\vec u,\vec u\rangle-\langle\vec u,\vec w\rangle+2\langle\vec v,\vec u\rangle-2\langle\vec v,\vec w\rangle+\langle\vec w,\vec u\rangle-\langle\vec w,\vec w\rangle$$" "\n"
    "מכיוון שהמערכת אורתונורמלית, מכפלת וקטורים שונים זה מזה שווה ל-0, בעוד שמכפלת וקטור בעצמו שווה ל-1. נקבל:" "\n"
    r"$$1-0+2\cdot0-2\cdot0+0-1=0$$" "\n"
    r"כלומר $\langle\vec\alpha,\vec\beta\rangle=0$, ולכן $\vec\beta\perp\vec\alpha$."
)

S3B2 = (
    "נורמה היא שורש של המכפלה הפנימית; אפשר לפתוח לפי ההגדרה ולפי תכונות המכפלה הפנימית, שימוש באורתונורמליות יוביל לתוצאה, כמו בסעיף הקודם." "\n"
    r"באופן כללי, אם $\{\vec u_1,\dots,\vec u_k\}$ קבוצה אורתונורמלית ו-$\vec x=\alpha_1\vec u_1+\dots+\alpha_k\vec u_k$ אז: $\|\vec x\|=\sqrt{\alpha_1^2+\dots+\alpha_k^2}$. במקרה שלנו:" "\n"
    r"$$\|\vec\alpha\|=\sqrt{1^2+2^2+1^2}=\sqrt6,\qquad\|\vec\beta\|=\sqrt{1^2+(-1)^2}=\sqrt2$$"
)

S4A1 = (
    r"נראה כי הפעולה קומוטטיבית, ז״א מתקיים $\begin{pmatrix}x\\y\end{pmatrix}*\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}$." "\n"
    r"$$\begin{pmatrix}x\\y\end{pmatrix}*\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}xb+ya\\yb\end{pmatrix}\ ,\qquad\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ay+bx\\by\end{pmatrix}$$" "\n"
    r"מכיוון שלכל $a,b,x,y\in\mathbb{R}$ מתקיימת סגירות לפעולות כפל וחיבור נובע $\begin{pmatrix}x\\y\end{pmatrix}*\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}$."
)

S4A2 = (
    r"נחפש $e=\begin{pmatrix}e_1\\e_2\end{pmatrix}\in\mathbb{R}^2\setminus\{(0,0)\}$ שמקיים לכל $\begin{pmatrix}a\\b\end{pmatrix}\in\mathbb{R}^2\setminus\{(0,0)\}$:" "\n"
    r"$$\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}e_1\\e_2\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}$$" "\n"
    r"$$\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}e_1\\e_2\end{pmatrix}=\begin{pmatrix}ae_2+be_1\\be_2\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}\ \Rightarrow\ \begin{cases}ae_2+be_1=a\\be_2=b\end{cases}\ \Rightarrow\ \begin{cases}e_1=0\\e_2=1\end{cases}$$" "\n"
    r"$$e=\begin{pmatrix}0\\1\end{pmatrix}\in\mathbb{R}^2\setminus\{(0,0)\}$$" "\n"
    r"*מכיוון שהפעולה קומוטטיבית (הוכחנו בסעיף א) אין צורך להראות כי $\begin{pmatrix}e_1\\e_2\end{pmatrix}*\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}a\\b\end{pmatrix}$ מתקיים."
)

S4A3 = (
    "ניתן להראות כי לא לכל איבר קיים הופכי ובכך להוכיח שהמבנה הנתון אינו חבורה:" "\n"
    r"אם $\begin{pmatrix}a\\b\end{pmatrix}^{-1}=\begin{pmatrix}x\\y\end{pmatrix}$ אז מתקיים $\begin{pmatrix}a\\b\end{pmatrix}*\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix}$, מכאן" "\n"
    r"$$\begin{cases}ay+bx=0\\by=1\end{cases}\ \Rightarrow\ \begin{cases}x=-\dfrac{a}{b^2}\\[2mm]y=\dfrac1b\end{cases}$$" "\n"
    r"ז״א עבור הוקטורים בהם $b=0$ אין הופכי. למשל $\begin{pmatrix}5\\0\end{pmatrix}\in\mathbb{R}^2\setminus\{(0,0)\}$ אך לא קיים לו הופכי."
)

S4B = (
    r"לפי משפט קושי-שוורץ לכל שני וקטורים $\begin{pmatrix}a\\b\end{pmatrix},\begin{pmatrix}b\\a\end{pmatrix}\in\mathbb{R}^2$ מתקיים:" "\n"
    r"$$\left\langle\begin{pmatrix}a\\b\end{pmatrix},\begin{pmatrix}b\\a\end{pmatrix}\right\rangle\le\left\|\begin{pmatrix}a\\b\end{pmatrix}\right\|\cdot\left\|\begin{pmatrix}b\\a\end{pmatrix}\right\|$$" "\n"
    r"מכאן $ab+ba\le\sqrt{a^2+b^2}\cdot\sqrt{a^2+b^2}$, ז״א $ab+ba\le a^2+b^2$ ולכן $(ab+ba)^2\le(a^2+b^2)^2$."
)

S5B = (
    r"נסדר את המשוואה הראשונה במערכת (על ידי ההכפלה בהופכי של 2):" "\n"
    r"$$\begin{cases}2x\equiv1\pmod 3\\x\equiv3\pmod 5\\x\equiv4\pmod 7\end{cases}\ \Rightarrow\ \begin{cases}x\equiv2\pmod 3\\x\equiv3\pmod 5\\x\equiv4\pmod 7\end{cases}$$" "\n"
    r"נסמן: $m_1=3,\ m_2=5,\ m_3=7$ והם אכן זרים בזוגות. נסמן: $m=m_1m_2m_3=3\cdot5\cdot7=105$, ולכן: $M_1=35,\ M_2=21,\ M_3=15$." "\n"
    r"לכן הפתרון למערכת הוא:" "\n"
    r"$$x=\left(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3\right)\bmod m=\left(2\cdot35\cdot x_1+3\cdot21\cdot x_2+4\cdot15\cdot x_3\right)\bmod105$$" "\n"
    r"נחשב את הערכים של $x_1,x_2,x_3$:" "\n"
    r"$$35x_1\equiv1\pmod 3\Rightarrow2x_1\equiv1\pmod 3\Rightarrow x_1=2$$" "\n"
    r"$$21x_2\equiv1\pmod 5\Rightarrow x_2\equiv1\pmod 5\Rightarrow x_2=1$$" "\n"
    r"$$15x_3\equiv1\pmod 7\Rightarrow x_3\equiv1\pmod 7\Rightarrow x_3=1$$" "\n"
    r"מכאן:" "\n"
    r"$$x=\left(a_1M_1x_1+a_2M_2x_2+a_3M_3x_3\right)\bmod m=\left(2\cdot35\cdot2+3\cdot21\cdot1+4\cdot15\cdot1\right)\bmod105=263\bmod105$$" "\n"
    r"$$x\equiv53\pmod{105}$$" "\n"
    r"בדיקה: $2\cdot53\equiv1\pmod 3$ , $\ 53\equiv3\pmod 5$ , $\ 53\equiv4\pmod 7$."
)

questions = [
    Q(1, "computation", "least_squares",
      r"(15%) במחלקה למדעי המחשב במכון הטכנולוגי חולון פתחו בקמפיין פרסומי חדש למשיכת סטודנטים. לאחר שבוע אחד של קמפיין פנו למחלקה 20 סטודנטים מתעניינים, אחרי שבועיים פנו 24, אחרי שלושה שבועות פנו 31 ואחרי 4 שבועות פנו 32 סטודנטים. מהו צפי מספר הסטודנטים המתעניינים שיפנו למחלקה בשבוע החמישי? השתמשו בריבועים פחותים.",
      S1A, part="א", points=15),
    Q(1, "computation", "projection",
      r"(10%) במרחב וקטורי $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע״י $\langle A,B\rangle=\mathrm{tr}(B^TA)$ לכל $A,B\in M_2(\mathbb{R})$. חשבו את ההיטל של $\begin{pmatrix}1&2\\3&0\end{pmatrix}$ על $\mathrm{Sp}\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}1&3\\1&1\end{pmatrix}\right\}$.",
      S1B, part="ב", points=10),

    Q(2, "proof", "inner_product",
      r"(15%) במרחב $C[0,1]$ של כל הפונקציות הרציפות בקטע $[0,1]$ נגדיר את הנוסחה הבאה: $\langle f,g\rangle=\displaystyle\int_0^1e^x\cdot f(x)\cdot g(x)\,dx$. בדקו האם הנוסחה מגדירה מכפלה פנימית על $C[0,1]$.",
      S2A, part="א", points=15),
    Q(2, "computation", "groups",
      r"(10%) נתבונן בחבורה $G=\{A\in M_2(\mathbb{Z}_5)\mid\det(A)\ne0\}$ ביחס לכפל מטריצות (חבורת המטריצות ההפיכות מגודל 2x2 עם רכיבים מ-$\mathbb{Z}_5$). תהי $H=\left\{\begin{pmatrix}4&0\\0&3\end{pmatrix}^n\ \middle|\ n\in\mathbb{Z}\right\}$ תת-חבורה ציקלית של $G$. מצאו את הסדר של $H$. (כמובן שהכפל והחיבור של רכיבי המטריצות הם מודולו 5).",
      S2B, part="ב", points=10),

    Q(3, "computation", "pos_def",
      r"(13%) עבור אילו ערכי הפרמטר $a$ המטריצה $\begin{pmatrix}a&0&1\\0&2a&0\\1&0&a\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=13),
    Q(3, "truefalse", "orthogonality", r"סעיף ב.1. האם $\vec\beta\perp\vec\alpha$ ? (6%)", S3B1, part="ב", points=6,
      contextId="c3", verdict=True),
    Q(3, "computation", "orthogonality", r"סעיף ב.2. חשבו את $\|\vec\alpha\|$ ו-$\|\vec\beta\|$. (6%)", S3B2, part="ג", points=6,
      contextId="c3"),

    Q(4, "truefalse", "groups", r"סעיף א.1. האם הפעולה היא קומוטטיבית? (5%)", S4A1, part="א", points=5,
      contextId="c4", verdict=True),
    Q(4, "computation", "groups", r"סעיף א.2. מצאו את האיבר הניטרלי ביחס לפעולת $*$ (במידה וקיים). (6%)", S4A2, part="ב",
      points=6, contextId="c4"),
    Q(4, "truefalse", "groups", r"סעיף א.3. האם המבנה $\left(\mathbb{R}^2\setminus\{(0,0)\},*\right)$ הוא חבורה? (7%)", S4A3,
      part="ג", points=7, contextId="c4", verdict=False),
    Q(4, "proof", "cauchy_schwarz",
      r"סעיף ב. בעזרת אי-שוויון קושי-שוורץ הוכיחו ש: $(ab+ba)^2\le(a^2+b^2)^2$ לכל $a,b\in\mathbb{R}$. (7%)",
      S4B, part="ד", points=7),

    {"num": 5, "part": "א", "kind": "computation", "topic": "svd", "points": 18,
     "question": r"(18%) מצאו פירוק SVD עבור המטריצה $A=\begin{pmatrix}-1&1\\-1&1\\1&1\end{pmatrix}$.",
     "hold": "no-key: the official solution for 5a is only a link to an online SVD calculator, no worked answer"},
    Q(5, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}2x\equiv1\pmod 3\\x\equiv3\pmod 5\\x\equiv4\pmod 7\end{cases}$. (7%)",
      S5B, part="ב", points=7),
]

exam = {
    "examCode": "23A-A",
    "examLabel": "אלגברה 2 - סמסטר א' תשפ\"ג מועד א'",
    "year": 2023,
    "examDate": "29.1.2023",
    "sourceFile": "algebra-2-23A-A-exam",
    "solutionFile": "algebra-2-23A-A-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
