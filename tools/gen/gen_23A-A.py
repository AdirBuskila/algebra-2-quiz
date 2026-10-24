# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-A.json -- algebra-2 (20079), semester A 2023, moed A (29.01.2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-A.py

Source: exam 2 pp. + typed official solution 8 pp. (both read from the rendered pages). Header: "4 of 5", 25% each;
all 5 questions are transcribed, 13 items, all shipped (Q5a solver-written).

Part letters: single-letter parts only, so numbered sub-parts get letters in order.
  Q3: a, b.1 -> b, b.2 -> c (the printed "b" setup is a context).   Q4: a.1, a.2, a.3, b -> a, b, c, d.
  Every question text starts with its printed label.

Typos in the official solution (checked with tools/verify/23A-A/check.py; no FINAL answer is wrong):
- Q1a: the boxed slope "a = 21.5" and "y(x) = 21.5x + 16" are slips: the slope is 43/10 (21.5 is 5a, the term
  actually added to b at x = 5). The printed y(5) = 37.5 is right. Written with a = 4.3.
- Q1b: the printed middle matrix of the second trace is (2 -2; 3 2); u2^T v is (2 -2; 4 2). Trace (4) unchanged.
- Q2a / Q4b: transcribed as printed (Q2a does not argue that <f,f> = 0 forces f = 0; Q4b drops absolute values
  before squaring). No answer changes.
Q5a (SVD of a 3x2 matrix): the "solution" is a link to an online SVD calculator and no worked answer (no partial
  evidence). Written by the solver: solutionSource "solved", official false; A = U S V^T checked in
  tools/verify/23A-A/solve_Q5a.py. Pending the refuter.
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
    r"$$\langle\alpha f,g\rangle=\int_0^1e^x\big(\alpha f(x)\big)g(x)\,dx=\alpha\int_0^1e^xf(x)g(x)\,dx=\alpha\langle f,g\rangle$$" "\n"
    r"**הערה:** הפתרון הרשמי מראה רק ש-$\langle f,f\rangle\ge0$. כדי שהנוסחה תהיה מכפלה פנימית יש להראות גם ש-$\langle f,f\rangle=0$ גורר $f=0$: הפונקציה $e^xf^2(x)$ רציפה ואי-שלילית ב-$[0,1]$, ולכן אם האינטגרל שלה שווה $0$ היא מתאפסת בכל נקודה. מכיוון ש-$e^x>0$ נקבל $f(x)=0$ לכל $x\in[0,1]$."
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
    r"מכאן $ab+ba\le\sqrt{a^2+b^2}\cdot\sqrt{a^2+b^2}$, ז״א $ab+ba\le a^2+b^2$ ולכן $(ab+ba)^2\le(a^2+b^2)^2$." "\n"
    r"**הערה:** קושי-שוורץ נותן אי-שוויון עם ערך מוחלט, $|ab+ba|\le a^2+b^2$. רק בגלל הערך המוחלט מותר להעלות בריבוע (אם $ab+ba<0$, האי-שוויון $ab+ba\le a^2+b^2$ לבדו אינו מספיק)."
)

S5A = (
    r"נמצא את פירוק $SVD$ של $A=\begin{pmatrix}-1&1\\-1&1\\1&1\end{pmatrix}$ דרך המטריצה הקטנה $A^TA$ (מסדר $2\times2$)." "\n"
    r"$$A^TA=\begin{pmatrix}-1&-1&1\\1&1&1\end{pmatrix}\begin{pmatrix}-1&1\\-1&1\\1&1\end{pmatrix}=\begin{pmatrix}3&-1\\-1&3\end{pmatrix}$$" "\n"
    r"$$|A^TA-\lambda I|=(3-\lambda)^2-1=(\lambda-4)(\lambda-2)=0\ \Rightarrow\ \lambda_1=4,\ \lambda_2=2$$" "\n"
    r"**וקטור עצמי עבור $\lambda=4$:** $\begin{pmatrix}-1&-1\\-1&-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\vec 0\ \Rightarrow\ y=-x$, ולאחר נרמול $\vec v_1=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$." "\n"
    r"**וקטור עצמי עבור $\lambda=2$:** $\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\vec 0\ \Rightarrow\ y=x$, ולאחר נרמול $\vec v_2=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$." "\n"
    r"הערכים הסינגולריים: $\sigma_1=\sqrt4=2,\ \sigma_2=\sqrt2$, ולכן $\Sigma=\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}$." "\n"
    r"עמודות $U$: $\vec u_i=\dfrac1{\sigma_i}A\vec v_i$ :" "\n"
    r"$$\vec u_1=\frac12\cdot\frac1{\sqrt2}\begin{pmatrix}-1&1\\-1&1\\1&1\end{pmatrix}\begin{pmatrix}1\\-1\end{pmatrix}=\frac1{2\sqrt2}\begin{pmatrix}-2\\-2\\0\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}-1\\-1\\0\end{pmatrix}$$" "\n"
    r"$$\vec u_2=\frac1{\sqrt2}\cdot\frac1{\sqrt2}\begin{pmatrix}-1&1\\-1&1\\1&1\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\frac12\begin{pmatrix}0\\0\\2\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix}$$" "\n"
    r"את $\vec u_3$ נשלים כווקטור יחידה הניצב ל-$\vec u_1,\vec u_2$ (וקטור עצמי של $AA^T$ לערך העצמי $0$): $\vec u_3=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}$ (בדיקה: $A^T\vec u_3=\vec 0$)." "\n"
    r"**תשובה סופית:**" "\n"
    r"$$A=U\Sigma V^T,\qquad U=\begin{pmatrix}-\frac1{\sqrt2}&0&\frac1{\sqrt2}\\-\frac1{\sqrt2}&0&-\frac1{\sqrt2}\\0&1&0\end{pmatrix},\quad\Sigma=\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix},\quad V=\begin{pmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}\\-\frac1{\sqrt2}&\frac1{\sqrt2}\end{pmatrix}$$" "\n"
    r"(הפירוק אינו יחיד: אפשר להחליף סימן של זוג $\vec v_i,\vec u_i$ יחד, או את הסימן של $\vec u_3$.)"
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

    Q(5, "computation", "svd", r"(18%) מצאו פירוק SVD עבור המטריצה $A=\begin{pmatrix}-1&1\\-1&1\\1&1\end{pmatrix}$.",
      S5A, part="א", points=18, solutionSource="solved", official=False),
    Q(5, "computation", "crt",
      r"סעיף ב. פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}2x\equiv1\pmod 3\\x\equiv3\pmod 5\\x\equiv4\pmod 7\end{cases}$. (7%)",
      S5B, part="ב", points=7),
]

# ---------------------------------------------------------------------------------------------------------
# Phase 4 (step author): rubric / pitfalls / guided steps, all derived from the stored solutions above.
# Numeric values and factual claims are re-checked by tools/verify/23A-A/steps_check.py (sympy / brute force).
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


S23AA = {
    (1, "א"): dict(
        rubric=rub((r"בניית המטריצה $X$ ווקטור הנתונים $\vec y$ למודל $y=ax+b$", 3),
                   (r"המשוואות הנורמליות $X^TX\binom ab=X^T\vec y$ וחישוב שני האגפים", 4),
                   (r"פתרון המערכת: $b=16$ , $a=4.3$", 4),
                   (r"הצבה $x=5$ ותשובה $y=37.5$", 4)),
        pitfalls=[r"לפתור את $X\binom ab=\vec y$ ישירות: ארבע הנקודות אינן על ישר אחד.",
                  r"לשכוח שהשיפוע הוא $a=4.3$ ולא $21.5$ (ערך זה הוא $5a$)."],
        steps=[
            num(r"מהו האיבר השמאלי-העליון ב-$X^TX$ (כלומר $\sum x_i^2$)?", 30, r"$1+4+9+16=30$."),
            num(r"מהו האיבר הראשון ב-$X^T\vec y$ (כלומר $\sum x_iy_i$)?", 289, r"$20+48+93+128=289$."),
            num("מהו השיפוע $a$ (עיגול עד $0.001$)?", 4.3, r"פתרון $\begin{pmatrix}30&10\\10&4\end{pmatrix}\binom ab=\binom{289}{107}$ נותן $b=16$ ו-$a=4.3$.", 0.001),
            num("מהו הצפי לשבוע החמישי לפי המודל?", 37.5, r"$y(5)=4.3\cdot5+16=37.5$.", 0.001),
        ]),
    (1, "ב"): dict(
        rubric=rub((r"בדיקה שהווקטורים הנתונים אינם אורתוגונליים: $\langle\vec w_1,\vec w_2\rangle=4$", 2),
                   (r"גרם-שמידט: $\vec u_2=\vec w_2-2\vec u_1$", 3),
                   (r"המקדם $\frac32$ של $\vec u_1$", 2),
                   (r"המקדם $1$ של $\vec u_2$", 1),
                   (r"הצבה: ההיטל $\frac12\begin{pmatrix}1&5\\2&2\end{pmatrix}$", 2)),
        pitfalls=[r"להשתמש בנוסחת ההיטל על בסיס שאינו אורתוגונלי: קודם יש לבצע גרם-שמידט.",
                  r"לחשב את המכפלה הפנימית כמכפלת מטריצות רגילה ולא כ-$\mathrm{tr}(B^TA)$ (סכום מכפלות הרכיבים המתאימים)."],
        steps=[
            num(r"מהי המכפלה הפנימית $\langle\vec w_1,\vec w_2\rangle$ של $\begin{pmatrix}1&1\\0&0\end{pmatrix}$ ו-$\begin{pmatrix}1&3\\1&1\end{pmatrix}$ ?", 4, r"$\mathrm{tr}(B^TA)=1\cdot1+1\cdot3+0+0=4\ne0$, ולכן הווקטורים אינם ניצבים."),
            num(r"מהו המקדם של $\vec u_1=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ בהיטל, כלומר $\frac{\langle\vec v,\vec u_1\rangle}{\|\vec u_1\|^2}$ עבור $\vec v=\begin{pmatrix}1&2\\3&0\end{pmatrix}$ ?", 1.5, r"$\frac{1+2}{2}=\frac32$."),
            num(r"מהו המקדם של $\vec u_2=\begin{pmatrix}-1&1\\1&1\end{pmatrix}$ בהיטל?", 1, r"$\langle\vec v,\vec u_2\rangle=-1+2+3+0=4$ ו-$\|\vec u_2\|^2=4$."),
            num(r"מהו האיבר הימני-העליון בהיטל?", 2.5, r"$\frac32\cdot1+1\cdot1=\frac52$."),
        ]),
    (2, "א"): dict(
        rubric=rub((r"אי-שליליות: $\langle f,f\rangle=\int_0^1e^xf^2\ge0$", 2), (r"מוגדרות: $\langle f,f\rangle=0$ גורר $f=0$ (רציפות ו-$e^x>0$)", 2), (r"סימטריה $\langle f,g\rangle=\langle g,f\rangle$", 3),
                   (r"חיבוריות ברכיב הראשון", 4), (r"הומוגניות $\langle\alpha f,g\rangle=\alpha\langle f,g\rangle$", 4)),
        pitfalls=[r"לבדוק רק אי-שליליות ולשכוח את ההגדרה המלאה: $\langle f,f\rangle=0$ רק עבור $f=0$ (פונקציה רציפה).",
                  r"לשכוח שהפונקציה $e^x$ חיובית תמיד, ולכן היא אינה משנה את סימן האינטגרנד."],
        steps=[
            num(r"עבור $f=g=1$, מהו $\langle f,g\rangle=\int_0^1e^x\,dx$ (עיגול עד $0.001$)?", 1.71828, r"$e-1\approx1.718$.", 0.001),
            num(r"עבור $f(x)=x$ ו-$g=1$, מהו $\langle f,g\rangle=\int_0^1xe^x\,dx$ ?", 1, r"$\left[(x-1)e^x\right]_0^1=0-(-1)=1$."),
            order("סדרו את שלבי הוכחת החיבוריות.",
                  [r"$\langle f+h,g\rangle=\int_0^1e^x\big(f(x)+h(x)\big)g(x)\,dx$",
                   r"$=\int_0^1e^x\big(f(x)g(x)+h(x)g(x)\big)dx$",
                   r"$=\int_0^1e^xf(x)g(x)\,dx+\int_0^1e^xh(x)g(x)\,dx$",
                   r"$=\langle f,g\rangle+\langle h,g\rangle$"],
                  "הצבת ההגדרה, פתיחת סוגריים, פיצול האינטגרל, וזיהוי שני המחוברים."),
            bug("באיזו שורה בהוכחת ההומוגניות יש טעות?",
                [r"$\langle\alpha f,g\rangle=\int_0^1e^x\big(\alpha f(x)\big)g(x)\,dx$",
                 r"$=\alpha^2\int_0^1e^xf(x)g(x)\,dx$",
                 r"$=\alpha\langle f,g\rangle$"],
                1, r"הקבוע $\alpha$ יוצא מהאינטגרל פעם אחת: $\alpha\int_0^1e^xf(x)g(x)\,dx$ ולא $\alpha^2$."),
        ]),
    (2, "ב"): dict(
        rubric=rub((r"האיבר הניטרלי $I=\begin{pmatrix}4&0\\0&3\end{pmatrix}^0$ ב-$H$", 2), (r"חישוב החזקות $2,3$ מודולו $5$", 4), (r"החזקה הרביעית שווה ל-$I$", 2), (r"$|H|=4$", 2)),
        pitfalls=[r"לשכוח שכל הרכיבים מחושבים מודולו $5$.",
                  r"לספור את $I$ פעמיים, או לשכוח לכלול אותו."],
        steps=[
            num(r"מהו הסדר של $4$ בחבורה $\mathbb{Z}_5^*$ (החזקה הקטנה $k$ עם $4^k\equiv1\pmod5$) ?", 2, r"$4^2=16\equiv1$."),
            num(r"מהו הסדר של $3$ ב-$\mathbb{Z}_5^*$ ?", 4, r"$3,4,2,1$: $3^2=9\equiv4$, $3^3=27\equiv2$, $3^4=81\equiv1$."),
            num(r"מהו הסדר של $H$ ?", 4, r"האיבר $\begin{pmatrix}4&0\\0&3\end{pmatrix}$ חוזר ליחידה בחזקת $\mathrm{lcm}(2,4)=4$ לראשונה, ולכן $|H|=4$."),
        ]),
    (3, "א"): dict(
        rubric=rub((r"פולינום אופייני $(x-2a)\left((x-a)^2-1\right)$", 4), (r"ערכים עצמיים $2a$ , $a-1$ , $a+1$", 3),
                   (r"חיובית: $a\ge1$ וחיובית לחלוטין: $a>1$", 2), (r"שלילית: $a\le-1$ ושלילית לחלוטין: $a<-1$", 2), (r"אף אחת מהן: $-1<a<1$", 2)),
        pitfalls=[r"לבלבל בין חיובית ($a\ge1$) לחיובית לחלוטין ($a>1$).",
                  r"לשכוח את הערך העצמי $2a$, שמשפיע רק כאשר $a>0$ (אך מתקיים אוטומטית כאשר $a\ge1$)."],
        steps=[
            num(r"עבור $a=3$, מהו הערך העצמי $a-1$ ?", 2, r"$3-1=2$."),
            ch("עבור אילו $a$ המטריצה מוגדרת חיובית לחלוטין?", r"$a>1$", [r"$a>0$", r"$a\ge1$", r"$a>-1$"],
               r"נדרש $2a>0$ , $a-1>0$ , $a+1>0$, כלומר $a>1$. עבור $a=1$ יש ערך עצמי $0$ (רק חיובית), ועבור $0<a<1$ הערך $a-1$ שלילי."),
            ch("עבור אילו $a$ המטריצה מוגדרת שלילית לחלוטין?", r"$a<-1$", [r"$a<0$", r"$a\le-1$", r"$a<1$"],
               r"נדרש $2a<0$ , $a-1<0$ , $a+1<0$, כלומר $a<-1$. עבור $-1\le a<0$ הערך $a+1$ אינו שלילי."),
            num(r"עבור $a=0$, כמה ערכים עצמיים חיוביים ממש יש למטריצה?", 1, r"הערכים העצמיים הם $0,-1,1$, ולכן ערך אחד חיובי, והמטריצה אינה אף אחת מהסוגים."),
        ]),
    (3, "ב"): dict(
        rubric=rub((r"פתיחת $\langle\vec\alpha,\vec\beta\rangle$ לפי לינאריות", 2), (r"שימוש באורתונורמליות", 2), (r"התוצאה $1-1=0$ והמסקנה $\vec\beta\perp\vec\alpha$", 2)),
        pitfalls=[r"לשכוח את האיבר $2\langle\vec v,\vec u\rangle$ (המקדם $2$ של $\vec v$ ב-$\vec\alpha$).",
                  r"לחשב $\langle\vec u,\vec u\rangle=0$ במקום $1$."],
        steps=[
            num(r"במערכת אורתונורמלית, מהו הסכום $\sum\alpha_i\beta_i$ למקדמים $(1,2,1)$ ו-$(1,0,-1)$ ?", 0, r"$1\cdot1+2\cdot0+1\cdot(-1)=0$."),
            order("סדרו את שלבי החישוב.",
                  [r"$\langle\vec\alpha,\vec\beta\rangle=\langle\vec u+2\vec v+\vec w,\ \vec u-\vec w\rangle$",
                   r"לפי לינאריות: $\langle\vec u,\vec u\rangle-\langle\vec u,\vec w\rangle+2\langle\vec v,\vec u\rangle-2\langle\vec v,\vec w\rangle+\langle\vec w,\vec u\rangle-\langle\vec w,\vec w\rangle$",
                   r"אורתונורמליות: $1-0+2\cdot0-2\cdot0+0-1$",
                   r"התוצאה $0$, ולכן $\vec\beta\perp\vec\alpha$"],
                  "הצבה, פתיחה, אורתונורמליות, תוצאה."),
        ]),
    (3, "ג"): dict(
        rubric=rub((r"הנוסחה $\|\vec x\|^2=\sum\alpha_i^2$ במערכת אורתונורמלית", 2), (r"$\|\vec\alpha\|=\sqrt6$", 2), (r"$\|\vec\beta\|=\sqrt2$", 2)),
        pitfalls=[r"לחשב $\|\vec\alpha\|=\sqrt{1+2+1}$ (בלי להעלות את $2$ בריבוע).",
                  r"לכתוב $\|\vec\beta\|=0$ בגלל המקדם $-1$: הריבוע של $-1$ הוא $1$."],
        steps=[
            ch(r"אם $\vec x=\sum\alpha_i\vec u_i$ במערכת אורתונורמלית, כמה שווה $\|\vec x\|^2$ ?", r"$\sum\alpha_i^2$",
               [r"$\left(\sum\alpha_i\right)^2$", r"$\sum\alpha_i$", r"$\sum|\alpha_i|$"],
               r"בגלל האורתונורמליות המכפלות המעורבות מתאפסות. עבור $(1,2,1)$ מתקבל $6$, אך $\left(\sum\alpha_i\right)^2=16$, $\sum\alpha_i=4$ ו-$\sum|\alpha_i|=4$."),
            num(r"מהו $\|\vec\alpha\|^2$ ?", 6, r"$1+4+1=6$."),
            num(r"מהו $\|\vec\beta\|^2$ ?", 2, r"$1+1=2$."),
        ]),
    (4, "א"): dict(
        rubric=rub((r"חישוב שני הצדדים $\binom xy*\binom ab$ ו-$\binom ab*\binom xy$", 3), (r"השוואה: $xb+ya=ay+bx$ ולכן הפעולה קומוטטיבית", 2)),
        pitfalls=[r"לבדוק רק זוג מספרים אחד: זו אינה הוכחה.",
                  r"להשוות את הרכיב הראשון בלבד ולשכוח את השני $by=yb$."],
        steps=[
            num(r"מהו הרכיב הראשון של $\binom12*\binom34$ ?", 10, r"$ay+bx=1\cdot4+2\cdot3=10$. גם $\binom34*\binom12=\binom{3\cdot2+4\cdot1}{8}$ נותן $10$."),
            ch("מדוע הפעולה קומוטטיבית?", r"הביטוי $ay+bx$ אינו משתנה כאשר מחליפים בין $(a,b)$ ל-$(x,y)$",
               [r"כי הפעולה אסוציאטיבית", r"כי יש איבר ניטרלי", r"כי כל איבר הפיך"],
               r"מחליפים $(a,b)\leftrightarrow(x,y)$ ומקבלים $xb+ya=ay+bx$ וגם $yb=by$. אסוציאטיביות, איבר ניטרלי והפיכות אינם גוררים קומוטטיביות."),
        ]),
    (4, "ב"): dict(
        rubric=rub((r"משוואת האיבר הניטרלי $\binom ab*\binom{e_1}{e_2}=\binom ab$", 2), (r"פתרון $e_2=1$ ו-$e_1=0$", 3), (r"בדיקה ש-$(0,1)$ שייך לקבוצה (שונה מאפס)", 1)),
        pitfalls=[r"לשכוח שהאיבר הניטרלי חייב להשתייך ל-$\mathbb{R}^2\setminus\{(0,0)\}$.",
                  r"לחשב את $e_1$ לפני $e_2$: המשוואה השנייה $be_2=b$ קובעת קודם את $e_2$."],
        steps=[
            num(r"מהמשוואה $be_2=b$ (לכל $b\ne0$), מהו $e_2$ ?", 1, r"מחלקים ב-$b$."),
            num(r"אחרי הצבת $e_2=1$, המשוואה $a\cdot1+be_1=a$ נותנת $be_1=0$. מהו $e_1$ ?", 0, r"$b\ne0$ לכן $e_1=0$."),
            num(r"מהו הרכיב הראשון של $\binom52*\binom01$ ?", 5, r"$ay+bx=5\cdot1+2\cdot0=5$, והרכיב השני $2\cdot1=2$."),
        ]),
    (4, "ג"): dict(
        rubric=rub((r"משוואות ההופכי $ay+bx=0$ ו-$by=1$", 3), (r"פתרון $y=\frac1b$ , $x=-\frac a{b^2}$ כאשר $b\ne0$", 2), (r"עבור $b=0$ אין הופכי", 1), (r"דוגמה: $\binom50$", 1)),
        pitfalls=[r"להסיק שהמבנה חבורה אחרי שמצאנו הופכי רק עבור $b\ne0$.",
                  r"לחפש הופכי של $\binom50$: המשוואה $by=1$ נותנת $0=1$."],
        steps=[
            num(r"עבור $\binom ab=\binom12$, מהו $y$ בהופכי $\binom xy$ (מ-$by=1$) ?", 0.5, r"$y=\frac1b=\frac12$.", 0.001),
            num(r"עבור אותו האיבר, מהו $x=-\frac{a}{b^2}$ ?", -0.25, r"$-\frac14$.", 0.001),
            ch("מה הסיבה לכך שהמבנה אינו חבורה?", r"לאיברים עם $b=0$ (כמו $\binom50$) אין הופכי",
               [r"אין איבר ניטרלי", r"הפעולה אינה קומוטטיבית", r"לכל איבר יש שני הופכיים שונים"],
               r"האיבר הניטרלי $\binom01$ קיים והפעולה קומוטטיבית, ולאיבר עם $b\ne0$ יש הופכי יחיד. עבור $b=0$ המשוואה $by=1$ אינה פתירה."),
        ]),
    (4, "ד"): dict(
        rubric=rub((r"הפעלת קושי-שוורץ על $\binom ab$ ו-$\binom ba$", 2), (r"חישוב המכפלה הפנימית $ab+ba$", 1), (r"שוויון הנורמות $\sqrt{a^2+b^2}$", 2), (r"העלאה בריבוע", 2)),
        pitfalls=[r"לבחור את הווקטורים $\binom ab$ ו-$\binom{-b}{a}$: המכפלה הפנימית שלהם $0$.",
                  r"להעלות בריבוע בלי לשים לב שהאגף השמאלי עלול להיות שלילי; מספיק להשתמש בערך מוחלט."],
        steps=[
            ch("אילו שני וקטורים לוקחים בקושי-שוורץ?", r"$\binom ab$ ו-$\binom ba$", [r"$\binom ab$ ו-$\binom{-b}{a}$", r"$\binom ab$ ו-$\binom ab$", r"$\binom aa$ ו-$\binom bb$"],
               r"רק הזוג $\binom ab,\binom ba$ נותן מכפלה פנימית $2ab$. הזוג $\binom ab,\binom{-b}{a}$ נותן $0$, הזוג $\binom ab,\binom ab$ נותן $a^2+b^2$ (ללא אי-שוויון חדש), והזוג $\binom aa,\binom bb$ נותן $2ab\le2|ab|$."),
            num(r"עבור $a=1$ ו-$b=2$, מהו $ab+ba$ ?", 4, r"$2+2=4$ ואילו $a^2+b^2=5$."),
            order("סדרו את שלבי ההוכחה.",
                  [r"לפי קושי-שוורץ עבור $\binom ab,\binom ba$: $\left|\left\langle\binom ab,\binom ba\right\rangle\right|\le\left\|\binom ab\right\|\left\|\binom ba\right\|$",
                   r"שתי הנורמות שוות ל-$\sqrt{a^2+b^2}$",
                   r"לכן $|ab+ba|\le a^2+b^2$",
                   r"נעלה בריבוע ונקבל $(ab+ba)^2\le(a^2+b^2)^2$"],
                  "קושי-שוורץ, שוויון הנורמות, צמצום, ואז העלאה בריבוע."),
        ]),
    (5, "א"): dict(
        rubric=rub((r"חישוב $A^TA=\begin{pmatrix}3&-1\\-1&3\end{pmatrix}$", 3), (r"ערכים עצמיים $4,2$", 4), (r"וקטורים עצמיים מנורמלים (עמודות $V$)", 4),
                   (r"ערכים סינגולריים $\sigma_1=2$ , $\sigma_2=\sqrt2$ ומטריצה $\Sigma$", 2), (r"עמודות $U$: $\vec u_i=\frac1{\sigma_i}A\vec v_i$", 3), (r"השלמת $\vec u_3$ ל-$U$ אורתוגונלית", 2)),
        pitfalls=[r"להשתמש ב-$\lambda_i$ במקום $\sigma_i=\sqrt{\lambda_i}$ בעמודות $U$ וב-$\Sigma$.",
                  r"לשכוח להשלים את $\vec u_3$ כך ש-$U$ תהיה אורתוגונלית מסדר $3\times3$."],
        steps=[
            num(r"מהו האיבר שמחוץ לאלכסון ב-$A^TA$ ?", -1, r"$(-1)(1)+(-1)(1)+(1)(1)=-1$."),
            num(r"מהו הערך העצמי הגדול של $A^TA$ ?", 4, r"$(3-\lambda)^2=1$ נותן $\lambda=4,2$."),
            num(r"מהו הערך הסינגולרי $\sigma_2$ (עיגול עד $0.001$)?", 1.41421, r"$\sigma_2=\sqrt{\lambda_2}=\sqrt2$.", 0.001),
            num(r"אם $\vec v_1=\frac1{\sqrt2}(1,-1)^T$, מהו הרכיב הראשון של $\vec u_1=\frac1{\sigma_1}A\vec v_1$ (עיגול עד $0.001$)?", -0.70711,
                r"$\vec u_1=\frac1{\sqrt2}(-1,-1,0)^T$.", 0.001),
        ]),
    (5, "ב"): dict(
        rubric=rub((r"צמצום המשוואה הראשונה ל-$x\equiv2\pmod3$", 1), (r"$m=105$ ו-$M_1=35,M_2=21,M_3=15$", 2), (r"$x_1=2,x_2=1,x_3=1$", 2), (r"הרכבה: $263\equiv53\pmod{105}$", 2)),
        pitfalls=[r"להציב את השאריות בלי לצמצם את $2x\equiv1\pmod3$.",
                  r"לשכוח את הצמצום מודולו $105$ בסוף."],
        steps=[
            num(r"מהי $a_1$ , כלומר פתרון $2x\equiv1\pmod3$ ?", 2, r"$2\cdot2=4\equiv1\pmod3$."),
            num(r"מהו $x_1$ , פתרון $35x_1\equiv1\pmod3$ ?", 2, r"$35\equiv2$ ו-$2\cdot2\equiv1$."),
            num(r"מהו הסכום $a_1M_1x_1+a_2M_2x_2+a_3M_3x_3$ לפני הצמצום?", 263, r"$2\cdot35\cdot2+3\cdot21\cdot1+4\cdot15\cdot1=140+63+60=263$."),
            num(r"מהו הפתרון $x$ בין $0$ ל-$104$ ?", 53, r"$263-210=53$."),
        ]),
}
for _q in questions:
    _s = S23AA.get((_q["num"], _q.get("part")))
    assert _s is not None, ("no steps for", _q["num"], _q.get("part"))
    assert sum(r["points"] for r in _s["rubric"]) == _q["points"], ("rubric sum", _q["num"], _q.get("part"))
    _q["rubric"], _q["rubricSource"] = _s["rubric"], "ai-verified"
    _q["pitfalls"] = _s["pitfalls"]
    _q["steps"], _q["stepsSource"] = _s["steps"], "ai-verified"

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
