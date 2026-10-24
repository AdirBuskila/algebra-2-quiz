# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-B.json -- algebra-2 (20079), semester B 2024, moed B (18.08.2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-B.py

Source: the typed official solution inside the 275-page compilation (pp. 233-240); it repeats every question
statement, so the exam text is read from there. 5 questions, 15 items, all shipped.

Part letters: single letters only, so numbered sub-parts get letters in order.
  Q1: a, b.1 -> b, b.2 -> c.

Typos in the official solution (checked with tools/verify/24B-B/check.py):
- Q1b.1: the text says the basis is "for W" (the space is U = Sp{A,B}); written as U. The official basis is the
  scaled form {I, [[-1,2],[0,1]]} of u2 = [[-0.5,1],[0,0.5]] (kept).
- Q3a: the determinant is printed with an entry c in place of 0; the factorisation that follows is right.
- Q5a (FINAL ANSWER): the third column of U is printed (-2/sqrt3, 4/sqrt3, sqrt5/3): not a unit vector and not
  orthogonal to the others. The correct column is (-2,4,5)/(3 sqrt5). Per the typo ruling: solutionSource "solved",
  official false, prefix "הפתרון הרשמי עם תיקון ...". Logged in docs/ASK_ADIR.md.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-B.json"


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CTX = {
    "c2": {"kind": "text", "title": "שאלה 2",
           "text": r"נסתכל בקבוצה $G=\left\{A=\begin{pmatrix}1&a&b\\0&1&a\\0&0&1\end{pmatrix}\in M_3(\mathbb{R})\ \middle|\ a,b\in\mathbb{Z}_3\right\}$ עם פעולת כפל מטריצות. (הכפל והחיבור של רכיבי המטריצות הם מודולו 3)."},
    "c4": {"kind": "text", "title": "שאלה 4",
           "text": r"נסתכל ב-$(A,*)$ כאשר $A=\{(x,y)\mid x,y\in\mathbb{R}\ \wedge\ x\neq0\}$ והפעולה $*$ מוגדרת באופן הבא:" "\n"
                   r"$\forall (x,y),(u,v)\in A\ ,\quad (x,y)*(u,v)=(2xu,\ y+v)$."},
}

S1A = (
    r"נעזר באי שוויון קושי-שוורץ עבור $\vec u=\left(\sqrt1,\sqrt2,\dots,\sqrt n\right)$ ו-$\vec v=\left(\frac1{\sqrt n},\frac1{\sqrt n},\dots,\frac1{\sqrt n}\right)$ עם המכפלה הפנימית הסטנדרטית ב-$\mathbb{R}^n$." "\n"
    r"$$\|\vec u\|=\sqrt{1+2+\dots+n}=\sqrt{\frac{n(n+1)}2}$$" "\n"
    r"$$\|\vec v\|=\sqrt{\frac1n+\frac1n+\dots+\frac1n}=\sqrt{n\cdot\frac1n}=1$$" "\n"
    r"$$\langle\vec u,\vec v\rangle=\frac{\sqrt1}{\sqrt n}+\frac{\sqrt2}{\sqrt n}+\dots+\frac{\sqrt n}{\sqrt n}=\sum_{k=1}^n\sqrt{\frac kn}$$" "\n"
    "אי השוויון המבוקש מתקבל ע\"י הצבה באי שוויון קושי-שוורץ:" "\n"
    r"$$\left|\langle\vec u,\vec v\rangle\right|\le\|\vec u\|\cdot\|\vec v\|\ \to\ \sum_{k=1}^n\sqrt{\frac kn}\le\sqrt{\frac{n(n+1)}2}\cdot1\ \to\ \sum_{k=1}^n\sqrt{\frac kn}\le\sqrt{\frac{n^2+n}2}$$"
)

S1B1 = (
    r"נמצא בסיס אורתוגונלי עבור $U$ בעזרת תהליך גרם-שמידט:" "\n"
    r"$$\vec u_1=\vec e_1=\begin{pmatrix}1&0\\0&1\end{pmatrix}$$" "\n"
    r"$$\vec u_2=\vec e_2-\frac{\langle\vec e_2,\vec u_1\rangle}{\|\vec u_1\|^2}\cdot\vec u_1=\begin{pmatrix}0&1\\0&1\end{pmatrix}-\frac{\left\langle\begin{pmatrix}0&1\\0&1\end{pmatrix},\begin{pmatrix}1&0\\0&1\end{pmatrix}\right\rangle}{2}\cdot\begin{pmatrix}1&0\\0&1\end{pmatrix}=\begin{pmatrix}-0.5&1\\0&0.5\end{pmatrix}$$" "\n"
    r"לכן $B=\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}-1&2\\0&1\end{pmatrix}\right\}$ הוא בסיס אורתוגונלי עבור $U$."
)

S1B2 = (
    r"כעת ניתן לחשב את ההיטל המבוקש:" "\n"
    r"$$\mathrm{proj}_U\begin{pmatrix}1&1\\1&2\end{pmatrix}=\frac{\left\langle\begin{pmatrix}1&1\\1&2\end{pmatrix},\begin{pmatrix}1&0\\0&1\end{pmatrix}\right\rangle}{2}\cdot\begin{pmatrix}1&0\\0&1\end{pmatrix}+\frac{\left\langle\begin{pmatrix}1&1\\1&2\end{pmatrix},\begin{pmatrix}-1&2\\0&1\end{pmatrix}\right\rangle}{6}\cdot\begin{pmatrix}-1&2\\0&1\end{pmatrix}$$" "\n"
    r"$$=1.5\begin{pmatrix}1&0\\0&1\end{pmatrix}+0.5\begin{pmatrix}-1&2\\0&1\end{pmatrix}=\begin{pmatrix}1&1\\0&2\end{pmatrix}$$"
)

S2A = (
    r"**סגירות ביחס לפעולת הכפל:** תהיינה $A=\begin{pmatrix}1&a&b\\0&1&a\\0&0&1\end{pmatrix}$ ו-$B=\begin{pmatrix}1&x&y\\0&1&x\\0&0&1\end{pmatrix}$ שתי מטריצות מ-$G$. אזי" "\n"
    r"$$AB=\begin{pmatrix}1&a&b\\0&1&a\\0&0&1\end{pmatrix}\begin{pmatrix}1&x&y\\0&1&x\\0&0&1\end{pmatrix}=\begin{pmatrix}1&x+a&y+ax+b\\0&1&x+a\\0&0&1\end{pmatrix}\in G$$" "\n"
    r"**אסוציאטיביות:** ידוע כי כפל מטריצות הוא פעולה אסוציאטיבית." "\n"
    r"**איבר ניטרלי:** מטריצת היחידה $I=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}$ הינה האיבר הניטרלי של $G$: $AI=IA=A$." "\n"
    r"**איבר הופכי:** עלינו לבדוק כי אם $A=\begin{pmatrix}1&a&b\\0&1&a\\0&0&1\end{pmatrix}$ אז $A^{-1}\in G$. נחשב את המטריצה ההופכית:" "\n"
    r"$$\left(\begin{array}{ccc|ccc}1&a&b&1&0&0\\0&1&a&0&1&0\\0&0&1&0&0&1\end{array}\right)\xrightarrow[R_1\to R_1-bR_3]{R_2\to R_2-aR_3}\left(\begin{array}{ccc|ccc}1&a&0&1&0&-b\\0&1&0&0&1&-a\\0&0&1&0&0&1\end{array}\right)\xrightarrow{R_1\to R_1-aR_2}\left(\begin{array}{ccc|ccc}1&0&0&1&-a&a^2-b\\0&1&0&0&1&-a\\0&0&1&0&0&1\end{array}\right)$$" "\n"
    r"כלומר $A^{-1}=\begin{pmatrix}1&-a&a^2-b\\0&1&-a\\0&0&1\end{pmatrix}\in G$."
)

S2B = r"כיוון ש-$a,b\in\mathbb{Z}_3$, הסדר של החבורה $G$ הוא $3^2=9$."

S2C = (
    r"$$\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}^2=\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}\cdot\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}\equiv\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}\pmod 3$$" "\n"
    r"$$\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}^3\equiv\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}\cdot\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}\pmod 3\equiv\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\pmod 3$$" "\n"
    r"מכאן נובע שהסדר של $\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}$ הוא 3."
)

S3A = (
    r"נחשב את הערכים העצמיים של המטריצה:" "\n"
    r"$$\begin{vmatrix}k^2-\lambda&0&2k\\0&k+1-\lambda&0\\2k&0&k^2-\lambda\end{vmatrix}=(k+1-\lambda)\begin{vmatrix}k^2-\lambda&2k\\2k&k^2-\lambda\end{vmatrix}=(k+1-\lambda)\left(\left(k^2-\lambda\right)^2-4k^2\right)$$" "\n"
    r"$$=(k+1-\lambda)\left(\lambda^2-2\lambda k^2+k^4-4k^2\right)$$" "\n"
    r"לכן הערכים העצמיים הם: $\lambda=k+1,\ \lambda=k^2+2k,\ \lambda=k^2-2k$." "\n"
    "**סיכום:**\n"
    r"המטריצה **מוגדרת חיובית** כאשר $\begin{cases}k\ge-1\\k\ge0\ \vee\ k\le-2\\k\ge2\ \vee\ k\le0\end{cases}$ , כלומר $k\in[2,+\infty)\ \vee\ k=0$." "\n"
    r"המטריצה **מוגדרת חיובית לחלוטין** כאשר $\begin{cases}k>-1\\k>0\ \vee\ k<-2\\k>2\ \vee\ k<0\end{cases}$ , כלומר $k\in(2,+\infty)$." "\n"
    "לא קיים $k$ עבורם המטריצה **מוגדרת שלילית** בפרט מוגדרת **שלילית לחלוטין**.\n"
    r"המטריצה **אינה מוגדרת** כאשר $k\in(-\infty,0)\cup(0,2)$."
)

S3B = (
    r"$y=mx+n$" "\n"
    r"$$\begin{cases}0m+n=0\\2m+n=1\\3m+n=4\\4m+n=6\\6m+n=9\end{cases}\ \Rightarrow\ \begin{pmatrix}0&1\\2&1\\3&1\\4&1\\6&1\end{pmatrix}\cdot\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}0\\1\\4\\6\\9\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\begin{pmatrix}0&2&3&4&6\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}0&1\\2&1\\3&1\\4&1\\6&1\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}0&2&3&4&6\\1&1&1&1&1\end{pmatrix}\begin{pmatrix}0\\1\\4\\6\\9\end{pmatrix}$$" "\n"
    r"$$\Rightarrow\begin{pmatrix}65&15\\15&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}92\\20\end{pmatrix}\ \Rightarrow\ m=1.6\ ,\ n=-0.8\ \Rightarrow\ y=1.6x-0.8$$"
)

S4A = (
    r"אם $(x,y),(u,v)\in A$ אז $x\neq0,\ u\neq0$ וניתן להסיק כי $2xu\neq0$. לכן $(2xu,\ y+v)\in A$. זאת אומרת ש-$A$ סגורה ביחס לפעולה הנ\"ל."
)

S4B = (
    r"$$\big((x,y)*(u,v)\big)*(a,b)=(2xu,\ y+v)*(a,b)=(4xua,\ y+v+b)$$" "\n"
    r"$$(x,y)*\big((u,v)*(a,b)\big)=(x,y)*(2ua,\ v+b)=(4xua,\ y+v+b)$$" "\n"
    "לכן הפעולה אסוציאטיבית."
)

S4C = (
    r"האיבר הניטרלי של $G$ הוא $e=\left(\frac12,0\right)$. הרי לכל $(x,y)\in A$ מתקיים" "\n"
    r"$$e*(x,y)=\left(\frac12,0\right)\cdot(x,y)=\left(2\cdot\frac12\cdot x,\ 0+y\right)=(x,y)$$"
)

S4D = (
    r"לכל $(x,y)\in A$ קיים איבר הופכי $\left(\dfrac1{4x},-y\right)$. מתקיים" "\n"
    r"$$(x,y)*\left(\frac1{4x},-y\right)=\left(2\cdot x\cdot\frac1{4x},\ y-y\right)=\left(\frac12,0\right)=e$$" "\n"
    r"לכן $(A,*)$ היא חבורה."
)

S4E = (
    r"נדרוש $(x,y)*(x,y)*(x,y)=(x,y)$. מתקיים" "\n"
    r"$$(x,y)*(x,y)*(x,y)=\left(2x^2,2y\right)*(x,y)=\left(4x^3,3y\right)$$" "\n"
    r"כלומר $\left(4x^3,3y\right)=(x,y)$ ונקבל $\begin{cases}4x^3=x\\3y=y\end{cases}$." "\n"
    r"כיוון ש-$x\neq0$ נקבל את שני הפתרונות הבאים: הראשון $\left(\dfrac12,0\right)$ ושני $\left(-\dfrac12,0\right)$."
)

S5A = (
    r"**הפתרון הרשמי עם תיקון:** בפתרון הרשמי העמודה השלישית של $U$ מודפסת כ-$\left(-\frac2{\sqrt3},\frac4{\sqrt3},\frac{\sqrt5}3\right)^T$. זה אינו וקטור יחידה ואינו אורתוגונלי לשתי העמודות האחרות. העמודה הנכונה היא $\frac1{3\sqrt5}(-2,4,5)^T$ (מכפלה וקטורית של שתי העמודות הראשונות, מנורמלת). שאר הפתרון כפי שהודפס." "\n"
    r"$$S=\begin{pmatrix}3&0\\0&\sqrt5\\0&0\end{pmatrix},\qquad U=\begin{pmatrix}\frac13&\frac2{\sqrt5}&-\frac2{3\sqrt5}\\-\frac23&\frac1{\sqrt5}&\frac4{3\sqrt5}\\\frac23&0&\frac{\sqrt5}3\end{pmatrix},\qquad V=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$"
)

S5B = r"$$\left\{134+360k\ \middle|\ k\in\mathbb{Z}\right\}$$"

questions = [
    Q(1, "proof", "cauchy_schwarz",
      r"(10%) הוכיחו את אי השוויון הבא: $\displaystyle\sum_{k=1}^n\sqrt{\frac kn}\le\sqrt{\frac{n^2+n}2}$.",
      S1A, part="א", points=10),
    Q(1, "computation", "orthogonality",
      r"סעיף ב.1. במרחב $M_2(\mathbb{R})$ נגדיר מכפלה פנימית (אין צורך להוכיח זאת) ע\"י $\langle A,B\rangle=tr\left(B^TA\right)$. בצעו תהליך גרם-שמידט עבור המערכת $\left\{A=\begin{pmatrix}1&0\\0&1\end{pmatrix}\ ,\ B=\begin{pmatrix}0&1\\0&1\end{pmatrix}\right\}$. (9%)",
      S1B1, part="ב", points=9),
    Q(1, "computation", "projection",
      r"סעיף ב.2. במרחב $M_2(\mathbb{R})$ עם המכפלה הפנימית $\langle A,B\rangle=tr\left(B^TA\right)$, חשבו את ההיטל של $C=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ על $U=\mathrm{Sp}\{A,B\}$ כאשר $A=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ , $B=\begin{pmatrix}0&1\\0&1\end{pmatrix}$. (6%)",
      S1B2, part="ג", points=6),

    Q(2, "proof", "groups", r"סעיף א. הוכיחו כי $G$ היא חבורה. (15%)", S2A, part="א", points=15, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף ב. מהו הסדר של $G$ ? (5%)", S2B, part="ב", points=5, contextId="c2"),
    Q(2, "computation", "groups", r"סעיף ג. מהו הסדר של $\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}$ ? (5%)", S2C, part="ג", points=5,
      contextId="c2"),

    Q(3, "computation", "pos_def",
      r"(15%) עבור אילו ערכי הפרמטר $k$ המטריצה $\begin{pmatrix}k^2&0&2k\\0&k+1&0\\2k&0&k^2\end{pmatrix}$ היא: מוגדרת חיובית, מוגדרת חיובית לחלוטין, מוגדרת שלילית, מוגדרת שלילית לחלוטין, או אף אחת מהן?",
      S3A, part="א", points=15),
    Q(3, "computation", "least_squares",
      r"(10%) נתונות 5 נקודות במישור: $(0,0),(2,1),(3,4),(4,6),(6,9)$. מצאו את משוואת הישר הקרוב ביותר לנקודות הללו בעזרת שיטת הריבועים הפחותים.",
      S3B, part="ב", points=10),

    Q(4, "truefalse", "groups", r"סעיף א. האם $A$ סגורה ביחס לפעולה $*$ ? (5%)", S4A, part="א", points=5, contextId="c4", verdict=True),
    Q(4, "truefalse", "groups", r"סעיף ב. האם הפעולה $*$ היא פעולה אסוציאטיבית? (5%)", S4B, part="ב", points=5, contextId="c4", verdict=True),
    Q(4, "truefalse", "groups", r"סעיף ג. האם ב-$A$ קיים איבר ניטרלי ביחס לפעולה הנ\"ל? (5%)", S4C, part="ג", points=5, contextId="c4",
      verdict=True),
    Q(4, "truefalse", "groups", r"סעיף ד. האם $(A,*)$ היא חבורה? (5%)", S4D, part="ד", points=5, contextId="c4", verdict=True),
    Q(4, "computation", "groups",
      r"סעיף ה. מצאו את כל האברים $(x,y)\in A$ המקיימים $(x,y)*(x,y)*(x,y)=(x,y)$. (5%)", S4E, part="ה", points=5, contextId="c4"),

    Q(5, "computation", "svd", r"(17%) מצאו פירוק $SVD$ עבור המטריצה $A=\begin{pmatrix}2&1\\1&-2\\0&2\end{pmatrix}$.",
      S5A, part="א", points=17, solutionSource="solved", official=False),
    Q(5, "computation", "crt",
      r"(8%) פתרו את המערכת הבאה באמצעות משפט השאריות הסיני: $\begin{cases}x\equiv4\pmod5\\x\equiv6\pmod8\\x\equiv8\pmod9\end{cases}$.",
      S5B, part="ב", points=8),
]

# ---- rubric / pitfalls / steps (ai-draft). Every expected value is recomputed by tools/verify/24B-B/steps_check.py ----
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


G1A = [r"נבחר $\vec u=\left(\sqrt1,\sqrt2,\dots,\sqrt n\right)$ ו-$\vec v=\left(\frac1{\sqrt n},\dots,\frac1{\sqrt n}\right)$",
       r"$\|\vec u\|=\sqrt{\frac{n(n+1)}2}$, $\ \|\vec v\|=1$, $\ \langle\vec u,\vec v\rangle=\sum_{k=1}^n\sqrt{\frac kn}$",
       r"קושי-שוורץ: $\sum_{k=1}^n\sqrt{\frac kn}\le\sqrt{\frac{n(n+1)}2}\cdot1$",
       r"$\sum_{k=1}^n\sqrt{\frac kn}\le\sqrt{\frac{n^2+n}2}$"]
add(1, "א",
    rubric=rub(("בחירת הווקטורים $\\vec u=(\\sqrt k)_k$ ו-$\\vec v=\\left(\\frac1{\\sqrt n}\\right)_k$", 3), ("חישוב $\\|\\vec u\\|^2=\\frac{n(n+1)}2$ ו-$\\|\\vec v\\|=1$", 3),
               ("חישוב $\\langle\\vec u,\\vec v\\rangle=\\sum\\sqrt{\\frac kn}$", 2), ("הצבה בקושי-שוורץ וסיום", 2)),
    pitfalls=["לבחור וקטורים שהמכפלה הפנימית שלהם אינה הסכום הנתון (למשל בלי הגורם $\\frac1{\\sqrt n}$).", "לשכוח את הנוסחה $1+2+\\dots+n=\\frac{n(n+1)}2$ ולכן לא לקבל $\\|\\vec u\\|^2$."],
    steps=[num(r"עבור $n=4$, מהו $\|\vec u\|^2=1+2+3+4$?", 10, "$\\frac{4\\cdot5}2=10$."),
           num(r"עבור $n=4$, מהו $\|\vec v\|$?", 1, "$\\sqrt{4\\cdot\\frac14}=1$."),
           order("סדרו את שלבי ההוכחה.", G1A, "הבחירה באה ראשונה, אחריה החישובים, ואז קושי-שוורץ."),
           findbug("בגרסה הבאה שורה אחת שגויה. מצאו אותה.", G1A, 1,
                   r"$\|\vec u\|=\sqrt{\frac{n(n+1)}2}$, $\ \|\vec v\|=n$, $\ \langle\vec u,\vec v\rangle=\sum_{k=1}^n\sqrt{\frac kn}$",
                   "$\\|\\vec v\\|^2=n\\cdot\\frac1n=1$, ולא $n^2$.")])

add(1, "ב",
    rubric=rub(("$\\vec u_1=A=I$", 2), ("חישוב $\\langle B,\\vec u_1\\rangle=1$ ו-$\\|\\vec u_1\\|^2=2$", 3), ("$\\vec u_2=B-\\frac12I=\\begin{pmatrix}-0.5&1\\\\0&0.5\\end{pmatrix}$", 3), ("הכפלה ב-2 לבסיס $\\left\\{I,\\begin{pmatrix}-1&2\\\\0&1\\end{pmatrix}\\right\\}$", 1)),
    pitfalls=["לחשב את המכפלה הפנימית $\\mathrm{tr}(B^TA)$ כמכפלת מטריצות רגילה בלי העקבה.", "לשכוח להפחית את ההיטל: $\\vec u_2=B$ אינו אורתוגונלי ל-$I$ (המכפלה הפנימית שלהם 1)."],
    steps=[num(r"מהו $\langle B,I\rangle$ עבור $B=\begin{pmatrix}0&1\\0&1\end{pmatrix}$?", 1, "סכום מכפלות האיברים התואמים: $0+0+0+1=1$."),
           num(r"מהו $\|I\|^2$ במכפלה הפנימית $\mathrm{tr}(B^TA)$?", 2, "$1+0+0+1=2$."),
           num(r"מהי הכניסה הימנית העליונה של $\vec u_2$?", -0.5, "$0-\\frac12\\cdot1=-0.5$.", tol=1e-9)])

add(1, "ג",
    rubric=rub(("המקדם של $I$: $\\frac{\\langle C,I\\rangle}{2}=1.5$", 2), ("המקדם של $\\begin{pmatrix}-1&2\\\\0&1\\end{pmatrix}$: $\\frac36=0.5$", 2), ("חיבור ותשובה $\\begin{pmatrix}1&1\\\\0&2\\end{pmatrix}$", 2)),
    pitfalls=["להשתמש ב-$B$ במקום בווקטור האורתוגונלי $\\vec u_2$ (או כפולתו) בנוסחת ההיטל.", "לחלק ב-$\\|\\vec u_2\\|^2=1.5$ במקום ב-6 כשמשתמשים בווקטור המוכפל ב-2."],
    steps=[num(r"מהו $\langle C,I\rangle$ עבור $C=\begin{pmatrix}1&1\\1&2\end{pmatrix}$?", 3, "$1+0+0+2=3$, ולכן המקדם $\\frac32=1.5$."),
           num(r"מהו המקדם $\frac{\langle C,w\rangle}{\|w\|^2}$ עבור $w=\begin{pmatrix}-1&2\\0&1\end{pmatrix}$?", 0.5, "$\\langle C,w\\rangle=-1+2+0+2=3$ ו-$\\|w\\|^2=6$.", tol=1e-9),
           num("מהי הכניסה הימנית התחתונה של ההיטל?", 2, "$1.5\\cdot1+0.5\\cdot1=2$.")])

G2A = [r"סגירות: $AB=\begin{pmatrix}1&x+a&y+ax+b\\0&1&x+a\\0&0&1\end{pmatrix}\in G$",
       "אסוציאטיביות: כפל מטריצות אסוציאטיבי",
       r"איבר ניטרלי: $I\in G$",
       r"הופכי: $A^{-1}=\begin{pmatrix}1&-a&a^2-b\\0&1&-a\\0&0&1\end{pmatrix}\in G$"]
add(2, "א",
    rubric=rub(("סגירות: חישוב $AB$ ושהוא מהצורה של $G$", 4), ("אסוציאטיביות מכפל מטריצות", 2), ("איבר ניטרלי $I\\in G$", 2), ("חישוב ההופכי בעזרת דירוג", 5), ("ההופכי שייך ל-$G$ ומסקנה", 2)),
    pitfalls=["לשכוח שהאיבר הימני העליון במכפלה הוא $y+ax+b$ (ולא $y+b$).", "לבדוק את ההופכי מעל $\\mathbb{R}$ ולא להסביר שהכניסות נשארות ב-$\\mathbb{Z}_3$."],
    steps=[num(r"עבור $a=1,b=2$ ו-$x=2,y=1$ ב-$\mathbb{Z}_3$, מהי הכניסה הימנית העליונה $y+ax+b$ במכפלה (מודולו 3)?", 2, "$1+2+2=5\\equiv2\\pmod3$."),
           choice("מהו ההופכי של $\\begin{pmatrix}1&a&b\\\\0&1&a\\\\0&0&1\\end{pmatrix}$?",
                  [r"$\begin{pmatrix}1&-a&a^2-b\\0&1&-a\\0&0&1\end{pmatrix}$", r"$\begin{pmatrix}1&-a&-b\\0&1&-a\\0&0&1\end{pmatrix}$",
                   r"$\begin{pmatrix}1&-a&a^2+b\\0&1&-a\\0&0&1\end{pmatrix}$", r"$\begin{pmatrix}1&a&-b\\0&1&a\\0&0&1\end{pmatrix}$"], 0,
                  "בדיקה בכפל: רק הראשונה נותנת $I$. בשאר האפשרויות המכפלה אינה $I$ (למשל, בשנייה הכניסה הימנית העליונה היא $-a^2$)."),
           findbug("בגרסה הבאה של ההוכחה שורה אחת שגויה. מצאו אותה.", G2A, 3,
                   r"הופכי: $A^{-1}=\begin{pmatrix}1&-a&a^2+b\\0&1&-a\\0&0&1\end{pmatrix}\in G$",
                   "בדירוג מתקבל $a^2-b$ בכניסה הימנית העליונה. עם $a^2+b$ המכפלה $AA^{-1}$ נותנת $2b$ במקום 0.")])

add(2, "ב",
    rubric=rub(("כל אחד מ-$a,b$ מקבל 3 ערכים ב-$\\mathbb{Z}_3$", 3), ("עקרון המכפלה: $3\\cdot3=9$", 2)),
    pitfalls=["לספור גם את הכניסות הקבועות (1 ו-0) כבחירות חופשיות ולקבל $3^3$ או יותר.", "לחשוב שהסדר הוא 3, כי יש רק פרמטר אחד ($a$ קובע שתי כניסות, אך $b$ בלתי תלוי)."],
    steps=[num("כמה ערכים אפשריים יש ל-$a$ ב-$\\mathbb{Z}_3$?", 3, "הערכים 0, 1, 2."),
           num("מהו הסדר של $G$?", 9, "$3\\cdot3=9$.")])

add(2, "ג",
    rubric=rub(("חישוב $A^2\\equiv\\begin{pmatrix}1&1&1\\\\0&1&1\\\\0&0&1\\end{pmatrix}\\pmod3$", 2), ("חישוב $A^3\\equiv I\\pmod3$", 2), ("מסקנה: הסדר 3, כי $A\\ne I$ ו-$A^2\\ne I$", 1)),
    pitfalls=["לשכוח להפחית מודולו 3 (כגון $4\\equiv1$) ולכן לא לקבל $A^3=I$.", "להסיק שהסדר 3 בלי לבדוק ש-$A^2\\ne I$."],
    steps=[num(r"מהי הכניסה הימנית העליונה של $A^2$ מודולו 3, עבור $A=\begin{pmatrix}1&2&0\\0&1&2\\0&0&1\end{pmatrix}$?", 1, "$1\\cdot0+2\\cdot2+0\\cdot1=4\\equiv1\\pmod3$."),
           num("מהי הכניסה האמצעית העליונה של $A^3$ מודולו 3?", 0, "$A^3\\equiv I$, ולכן הכניסה 0."),
           num("מהו הסדר של $A$?", 3, "$A^3=I$, ו-$A,A^2\\ne I$ (ל-$A^2$ יש כניסות 1 מעל האלכסון).")])

add(3, "א",
    rubric=rub(("חישוב הדטרמיננטה: $(k+1-\\lambda)\\left((k^2-\\lambda)^2-4k^2\\right)$", 5), ("הערכים העצמיים $k+1,\\ k^2+2k,\\ k^2-2k$", 2), ("מוגדרת חיובית: $k\\in[2,\\infty)$ או $k=0$", 3), ("מוגדרת חיובית לחלוטין: $k>2$", 2), ("אינה שלילית, ואינה מוגדרת עבור $k\\in(-\\infty,0)\\cup(0,2)$", 3)),
    pitfalls=["לשכוח את $k=0$: המטריצה היא $\\mathrm{diag}(0,1,0)$ שהיא מוגדרת חיובית (אך לא לחלוטין).", "לכלול את $k=2$ במוגדרת חיובית לחלוטין: שם $k^2-2k=0$."],
    steps=[num("מהו הערך העצמי $k^2+2k$ עבור $k=3$?", 15, "$9+6=15$."),
           num("מהו הערך העצמי הקטן ביותר עבור $k=1$? (הערכים $k+1,\\ k^2+2k,\\ k^2-2k$)", -1, "$2,\\ 3,\\ -1$, ולכן המינימום $-1$ והמטריצה אינה מוגדרת."),
           choice("לאילו $k$ המטריצה מוגדרת חיובית (אי-שלילית)?",
                  ["$k\\ge2$ או $k=0$", "$k\\ge2$ בלבד", "$k\\ge0$", "$k>2$ בלבד"], 0,
                  "עבור $k=0$ המטריצה $\\mathrm{diag}(0,1,0)$ אי-שלילית; עבור $k=1$ יש ערך עצמי $-1$; עבור $k=2$ הערכים $3,8,0$ אי-שליליים.")])

add(3, "ב",
    rubric=rub(("בניית $A\\vec x=\\vec b$", 2), ("המשוואות הנורמליות $\\begin{pmatrix}65&15\\\\15&5\\end{pmatrix}\\vec x=\\begin{pmatrix}92\\\\20\\end{pmatrix}$", 4), ("פתרון $m=1.6,\\ n=-0.8$", 3), ("הישר $y=1.6x-0.8$", 1)),
    pitfalls=["להשמיט את הנקודה $(0,0)$ מהסכומים, או לשכוח שהיא תורמת 1 לכניסת ה-5 ב-$A^TA$.", "טעות חשבונית ב-$\\sum x_iy_i=92$."],
    steps=[num(r"מהו $\sum x_i^2$ עבור $x=0,2,3,4,6$?", 65, "$0+4+9+16+36=65$."),
           num(r"מהו $\sum x_iy_i$ עבור $(0,0),(2,1),(3,4),(4,6),(6,9)$?", 92, "$0+2+12+24+54=92$."),
           num("מהו השיפוע $m$?", 1.6, "$65m+15n=92$ ו-$15m+5n=20$; מהשנייה כפול 3: $45m+15n=60$, ולכן $20m=32$.", tol=1e-9),
           num("מהו $n$?", -0.8, "$5n=20-15\\cdot1.6=-4$.", tol=1e-9)])

add(4, "א",
    rubric=rub(("$x\\ne0$ ו-$u\\ne0$", 1), ("$2xu\\ne0$ ולכן $(2xu,y+v)\\in A$", 3), ("מסקנה: $A$ סגורה לפעולה", 1)),
    pitfalls=["לדרוש $2xu>0$: אין חיוביות ב-$A$, רק $x\\ne0$.", "לבדוק גם שהרכיב השני שונה מאפס, אף שאין הגבלה עליו."],
    steps=[choice("מה צריך להראות כדי ש-$A$ תהיה סגורה ביחס ל-$*$?",
                  ["שהרכיב הראשון $2xu$ שונה מאפס", "שהרכיב השני $y+v$ שונה מאפס", "שהרכיב הראשון $2xu$ חיובי", "ש-$x=u$"], 0,
                  "ב-$A$ רק הרכיב הראשון מוגבל ($x\\ne0$). חיוביות אינה נדרשת: $x=-1,u=1$ נותן $2xu=-2$ וגם $(-2,\\cdot)\\in A$."),
           num(r"מהו הרכיב הראשון של $(1,2)*(3,4)$?", 6, "$2\\cdot1\\cdot3=6$.")])

add(4, "ב",
    rubric=rub(("חישוב $\\big((x,y)*(u,v)\\big)*(a,b)=(4xua,y+v+b)$", 2), ("חישוב $(x,y)*\\big((u,v)*(a,b)\\big)=(4xua,y+v+b)$", 2), ("השוואה ומסקנה: אסוציאטיבית", 1)),
    pitfalls=["לחשב רק אגף אחד ולהסיק מסקנה.", "לשכוח את גורם 2 בכל כפל: ביטוי כמו $2xua$ במקום $4xua$ (מכפילים פעמיים)."],
    steps=[num(r"עבור $(x,y)=(1,0),\ (u,v)=(2,1),\ (a,b)=(3,2)$, מהו הרכיב הראשון של $\big((x,y)*(u,v)\big)*(a,b)$?", 24, "$(1,0)*(2,1)=(4,1)$ ואז $(4,1)*(3,2)=(24,3)$."),
           num("ומהו הרכיב השני של אותה מכפלה?", 3, "$1+2=3$. גם בצד השני: $(2,1)*(3,2)=(12,3)$ ואז $(1,0)*(12,3)=(24,3)$.")])

add(4, "ג",
    rubric=rub(("דרישה $e*(x,y)=(x,y)$ ופתרון הרכיב הראשון: $2e_1x=x$", 2), ("הרכיב השני $e_2=0$", 1), ("הצבה ובדיקה ש-$e=\\left(\\frac12,0\\right)$ ניטרלי", 2)),
    pitfalls=["לבחור $e=(1,0)$ מתוך הרגל: $(1,0)*(x,y)=(2x,y)$.", "לבדוק רק את $e*(x,y)$; כאן הפעולה חילופית ולכן מספיק."],
    steps=[num("מהו $e_1$ המקיים $2e_1x=x$ לכל $x\\ne0$?", 0.5, "$2e_1=1$.", tol=1e-9),
           choice("מהו הרכיב השני של האיבר הניטרלי?", ["$0$", "$1$", "$y$", "$-y$"], 0,
                  "צריך $e_2+y=y$ לכל $y$, ולכן $e_2=0$.")])

add(4, "ד",
    rubric=rub(("סגירות, אסוציאטיביות ואיבר ניטרלי מהסעיפים הקודמים", 2), ("מציאת ההופכי $\\left(\\frac1{4x},-y\\right)$", 2), ("בדיקת $(x,y)*\\left(\\frac1{4x},-y\\right)=e$ ושההופכי ב-$A$", 1)),
    pitfalls=["לתת הופכי $\\left(\\frac1x,-y\\right)$: אז הרכיב הראשון במכפלה הוא $2$ ולא $\\frac12$.", "לשכוח להראות שההופכי שייך ל-$A$ (הרכיב הראשון $\\frac1{4x}\\ne0$)."],
    steps=[num("מהו הרכיב הראשון של ההופכי של $(2,3)$? (תשובה עשרונית)", 0.125, "$\\frac1{4x}=\\frac18$.", tol=1e-9),
           num("מהו הרכיב השני של ההופכי של $(2,3)$?", -3, "$y+(-y)=0$, ולכן $-3$.")])

add(4, "ה",
    rubric=rub(("חישוב $(x,y)*(x,y)*(x,y)=(4x^3,3y)$", 2), ("פתרון $4x^3=x$ עם $x\\ne0$ ולכן $x=\\pm\\frac12$", 2), ("פתרון $3y=y$ ולכן $y=0$", 1)),
    pitfalls=["לשכוח את הפתרון השלילי $x=-\\frac12$.", "לצמצם ב-$x$ מבלי לציין ש-$x\\ne0$ (כך נפסלת $x=0$)."],
    steps=[num("מהו הערך החיובי של $x$ המקיים $4x^3=x$, $x\\ne0$? (תשובה עשרונית)", 0.5, "$4x^2=1$ ולכן $x=\\pm\\frac12$.", tol=1e-9),
           num("מהו $y$ המקיים $3y=y$?", 0, "$2y=0$."),
           choice("כמה פתרונות $(x,y)\\in A$ יש?", ["2", "1", "3", "אינסוף"], 0, "$\\left(\\frac12,0\\right)$ ו-$\\left(-\\frac12,0\\right)$.")])

add(5, "א",
    rubric=rub(("חישוב $A^TA=\\mathrm{diag}(5,9)$ וערכיה העצמיים", 3), ("ערכים סינגולריים $3,\\ \\sqrt5$ ו-$S$", 3), ("$V=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$", 3),
               ("עמודות $U$ הראשונות $\\vec u_i=\\frac1{\\sigma_i}A\\vec v_i$", 4), ("העמודה השלישית של $U$ היא $\\frac1{3\\sqrt5}(-2,4,5)^T$ (הושלמה)", 3), ("$A=USV^T$", 1)),
    pitfalls=["לסדר את הערכים הסינגולריים בסדר עולה בלי להתאים את העמודות של $V$ ו-$U$.", "להעתיק את העמודה השלישית של $U$ כפי שהיא מודפסת בפתרון הרשמי: היא אינה וקטור יחידה."],
    steps=[num(r"מהו הערך העצמי של $A^TA$ שמתאים לערך הסינגולרי הגדול $\sigma_1=3$?", 9, "$\\sigma_1^2=9$. אכן $A^TA=\\mathrm{diag}(5,9)$."),
           num(r"עבור $\vec v_1=(0,1)^T$, מהי הכניסה הראשונה של $\vec u_1=\frac13A\vec v_1$? (תשובה עשרונית)", 0.3333333, "$A\\vec v_1=(1,-2,2)^T$, ולכן $\\vec u_1=\\left(\\frac13,-\\frac23,\\frac23\\right)^T$.", tol=1e-6),
           num(r"מהו האורך $\|(-2,4,5)\|$ של הווקטור שמנרמלים כדי לקבל את העמודה השלישית של $U$? (תשובה עשרונית)", 6.7082039, "$\\sqrt{4+16+25}=\\sqrt{45}=3\\sqrt5$.", tol=1e-6)])

add(5, "ב",
    rubric=rub(("שהמודולים 5, 8, 9 זרים בזוגות והמודולו המשותף 360", 2), ("פתרון המערכת בעזרת המשפט הסיני", 4), ("התשובה $\\{134+360k\\mid k\\in\\mathbb{Z}\\}$", 2)),
    pitfalls=["לתת פתרון אחד בלבד ($134$) בלי המחלקה $134+360k$.", "לבדוק את הפתרון רק מול משוואה אחת במקום שלוש."],
    steps=[num("מהו מודולו הפתרון (המודולים 5, 8, 9 זרים בזוגות)?", 360, "$5\\cdot8\\cdot9=360$."),
           num("מהי השארית של 134 בחלוקה ב-8 (צריך להתאים ל-$x\\equiv6\\pmod8$)?", 6, "$134=16\\cdot8+6$."),
           num("מהי השארית של 134 בחלוקה ב-9 (צריך להתאים ל-$x\\equiv8\\pmod9$)?", 8, "$134=14\\cdot9+8$.")])

exam = {
    "examCode": "24B-B",
    "examLabel": "אלגברה 2 - סמסטר ב' תשפ\"ד מועד ב'",
    "year": 2024,
    "examDate": "18.8.2024",
    "sourceFile": "algebra-2-24B-B-exam",
    "solutionFile": "algebra-2-24B-B-official-solution",
    "contexts": CTX,
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} items")
