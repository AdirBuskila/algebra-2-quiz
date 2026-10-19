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
