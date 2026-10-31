# -*- coding: utf-8 -*-
"""P05 · גרהם-שמידט — video script (build: tools/video/vid.py P05).

Source: courses/proj_gs/C05.js (lesson + goal). Exam anchor: 26B-A-Q1a (Gram-Schmidt on A=diag(1,-1),
B=[[1,1],[0,-1]] in M_2 with tr(B^T A)), which no guided quiz uses. Avoided on purpose: the C05 quiz
(v1=(1,1,1), v2=(1,2,3); [[1,1],[1,1]], [[2,0],[0,2]]; (1,1,0),(1,0,1),(0,1,1); (1,0,1),(0,1,1),(1,1,2);
(1,-1,0),(3,1,2): so the dependent example is v1-2v2, not v1+v2), 24B-B-Q1b (a C05 quiz item: A=I, B=[[0,1],[0,1]]) and its projection sibling 24B-B-Q1c.
26B-A-Q1b (the projection that follows the anchor) is solved in the boss video P10.
The algebraic proof that the residual is ⟂ u_1 is not shown (it is the C03 quiz item 26A-A-Q3c); the video relies
on the numeric checks. Every vector and matrix below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R

# ---------------------------------------------------------------- the picture: two vectors in R^2
p1, p2 = V(3, 1), V(1, 3)
assert w.coef(p2, p1, w.dot) == R(3, 5)
PIC, pp, pc = w.proj2d("gs", p1, p2, box=(-1.6, 4.0, -0.6, 3.6), size=(620, 465),
                       names=("u_1", "v_2", "", "u_2"), sides=(-1, 1, -1, 1))
assert list(pc) == [R(-4, 5), R(12, 5)] and w.dot(pc, p1) == 0

# ---------------------------------------------------------------- R^3: three vectors
v1, v2, v3 = V(1, 0, 1), V(2, 1, 0), V(0, 1, 3)
us, cs = w.gram_schmidt([v1, v2, v3], w.dot)
u1, u2, u3 = us
assert u1 == v1 and w.dot(u1, u1) == 2
assert w.dot(v2, u1) == 2 and cs[(1, 0)] == 1 and list(u2) == [1, 1, -1] and w.dot(u2, u2) == 3
assert w.dot(v3, u1) == 3 and cs[(2, 0)] == R(3, 2)
assert w.dot(v3, u2) == -2 and cs[(2, 1)] == R(-2, 3)
assert list(u3) == [R(-5, 6), R(5, 3), R(5, 6)]
u3s = R(6, 5) * u3
assert list(u3s) == [-1, 2, 1] and w.dot(u3s, u1) == 0 and w.dot(u3s, u2) == 0
assert [w.dot(u, u) for u in (u1, u2, u3s)] == [2, 3, 6]
assert sp.simplify(w.dot(u3 / sp.sqrt(w.dot(u3, u3)) - u3s / sp.sqrt(6), V(1, 1, 1))) == 0   # scaling then normalizing
assert sp.simplify(u3 / sp.sqrt(w.dot(u3, u3)) - u3s / sp.sqrt(6)) == sp.zeros(3, 1)
# a dependent third vector: the residual is the zero vector
vd = v1 - 2 * v2
assert list(vd) == [-3, -2, 1]
assert w.coef(vd, u1, w.dot) == -1 and w.coef(vd, u2, w.dot) == -2
assert vd + u1 + 2 * u2 == sp.zeros(3, 1)
# the span is unchanged both ways: each v_m = u_m + a combination of earlier u's
assert v2 == u2 + cs[(1, 0)] * u1 and v3 == u3 + cs[(2, 0)] * u1 + cs[(2, 1)] * u2

# ---------------------------------------------------------------- exam 26B-A-Q1a
A, B = M([[1, 0], [0, -1]]), M([[1, 1], [0, -1]])
assert w.ip_m(B, A) == 2 and w.ip_m(A, A) == 2
(U1, U2), cm = w.gram_schmidt([A, B], w.ip_m)
assert U1 == A and cm[(1, 0)] == 1 and U2 == M([[0, 1], [0, 0]])
assert w.ip_m(U1, U2) == 0 and w.ip_m(U2, U2) == 1 and sp.sqrt(w.ip_m(U1, U1)) == sp.sqrt(2)
# the trap: dividing by |A| instead of |A|^2
Wr = B - (w.ip_m(B, A) / sp.sqrt(w.ip_m(A, A))) * A
assert w.ip_m(Wr, A) == 2 - 2 * sp.sqrt(2) and w.ip_m(Wr, A) != 0

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הקודם ראינו שהיטל על תת מרחב דורש בסיס אורתוגונלי. אבל מה עושים כשהבסיס לא כזה?"),
    P("בונים אחד. בשיטה שנקראת גרהם-שמידט."),
    P("נבנה בסיס אורתוגונלי ב-$\\mathbb{R}^3$, ואחר כך נפתור שאלה ממבחן עם מטריצות.", hold=0.4,
      say="נבנה בסיס אורתוגונלי באר שלוש, ואחר כך נפתור שאלה ממבחן עם מטריצות."),
], stage='<div class="kicker">P05 · היטל וגרהם-שמידט</div><h1>גרהם-שמידט</h1>'
         '<p>להפוך בסיס כלשהו לבסיס אורתוגונלי בשיטת גרהם-שמידט, ב-$\\mathbb{R}^3$ ובמרחב המטריצות, ולזהות תלות לינארית.</p>',
   layout="title")

idea = Scene("idea", "הרעיון", [
    P("הרעיון פשוט: את הוקטור הראשון משאירים כמו שהוא.", do=show("gs-a", "gs-line", "g-0"),
      say="הרעיון פשוט: את הוקטור הראשון משאירים כמו שהוא."),
    P("לוקחים את הוקטור השני, ומטילים אותו על הראשון.", do=show("gs-b", "gs-p")),
    P("ומה שנשאר, **השארית**, הוא הוקטור החדש. הוא ניצב לראשון, בדיוק כמו בהיטל על ישר.", do=show("gs-c", "gs-ra", "g-1"),
      hold=0.3),
    P("וכל וקטור הבא: מחסירים ממנו את ההיטלים על **כל** הוקטורים שכבר בנינו.", do=show("g-2")),
    P("והפרישה לא משתנה: כל וקטור חדש הוא צירוף של הישנים, וגם להפך, כל וקטור ישן הוא הוקטור החדש שלו ועוד צירוף של הקודמים.",
      do=show("g-c1"), hold=0.4),
], stage='<div class="pg-stack">' + PIC + "</div>",
   panel=w.rows("g", [
    r"$u_1=v_1$",
    r"$u_2=v_2-\frac{\langle v_2,u_1\rangle}{\|u_1\|^2}u_1$",
    r"$u_m=v_m-\sum_{i<m}\frac{\langle v_m,u_i\rangle}{\|u_i\|^2}u_i$"], "sm")
   + st.card("g-c1", "rule", "🔑 כל $u_m$ = השארית של $v_m$ אחרי ההיטלים על הקודמים"))

r3 = Scene("r3", "ב-ℝ³", [
    P("שלושה וקטורים ב-$\\mathbb{R}^3$. הראשון נשאר: $u_1=(1,0,1)$, והנורמה שלו בריבוע שתיים.", do=show("r-0", "r-1"),
      say="שלושה וקטורים באר שלוש. הראשון נשאר: יוּ אחת הוא אחת, אפס, אחת, והנורמה שלו בריבוע שתיים."),
    P("הוקטור השני: המכפלה שלו עם $u_1$ היא שתיים. המקדם הוא שתיים חלקי שתיים, כלומר אחת.", do=show("r-2"),
      say="הוקטור השני: המכפלה שלו עם יוּ אחת היא שתיים. המקדם הוא שתיים חלקי שתיים, כלומר אחת."),
    P("אז $u_2=(1,1,-1)$. והנורמה שלו בריבוע שלוש.", do=show("r-3"),
      say="אז יוּ שתיים הוא אחת, אחת, מינוס אחת. והנורמה שלו בריבוע שלוש."),
    P("הוקטור השלישי: מחסירים היטל על $u_1$ **וגם** על $u_2$.", do=show("r-4"),
      say="הוקטור השלישי: מחסירים היטל על יוּ אחת וגם על יוּ שתיים."),
    P("המקדמים: שלוש חצאים, ומינוס שני שליש. שימו לב לסימן: מחסירים מינוס, כלומר מוסיפים.", do=show("r-5")),
    P("יוצאים שברים. ומותר להכפיל בסקלר שונה מאפס: כפול שש חמישיות, ומקבלים $(-1,2,1)$.", do=show("r-6", "r-c1"),
      say="יוצאים שברים. ומותר להכפיל בסקלר שונה מאפס: כפול שש חמישיות, ומקבלים מינוס אחת, שתיים, אחת."),
    P("בדיקה: המכפלה עם $u_1$ היא מינוס אחת ועוד אחת, ועם $u_2$ מינוס אחת ועוד שתיים פחות אחת. שתיהן אפס.",
      do=show("r-7"), say="בדיקה: המכפלה עם יוּ אחת היא מינוס אחת ועוד אחת, ועם יוּ שתיים מינוס אחת ועוד שתיים פחות אחת. "
                          "שתיהן אפס.", hold=0.4),
], stage='<div class="pg-stack">' + w.rows("r", [
    f"$v_1={w.tup(v1)},\\ v_2={w.tup(v2)},\\ v_3={w.tup(v3)}$",
    r"$u_1=(1,0,1),\quad \|u_1\|^2=2$",
    r"$\langle v_2,u_1\rangle=2\ \Rightarrow\ u_2=v_2-\frac22u_1$",
    r"$u_2=(1,1,-1),\quad \|u_2\|^2=3$",
    r"$u_3=v_3-\frac{\langle v_3,u_1\rangle}{2}u_1-\frac{\langle v_3,u_2\rangle}{3}u_2$",
    r"$u_3=v_3-\frac32u_1+\frac23u_2=\left(-\frac56,\frac53,\frac56\right)$",
    r"$u_3\to\frac65u_3=(-1,2,1)$",
    r"$\langle u_3,u_1\rangle=0,\ \ \langle u_3,u_2\rangle=0\ \checkmark$"], "sm") + "</div>",
   panel=st.card("r-c1", "ex", "מותר להכפיל בסקלר שונה מאפס: הניצבות והפרישה לא משתנות"))

norm = Scene("norm", "נרמול", [
    P("ואם מבקשים בסיס **אורתונורמלי**, מחלקים כל וקטור בנורמה שלו. זה הצעד האחרון, לא לפני.", do=show("n-0")),
    P("הנורמות כאן: שורש שתיים, שורש שלוש, ושורש שש.", do=show("n-1")),
    P("ושימו לב: את הכפל בשש חמישיות עשינו לפני הנרמול, אז הנרמול מבטל אותו בכל מקרה.", do=show("n-c"), hold=0.4),
], stage='<div class="pg-stack">' + w.rows("n", [
    r"$g_i=\frac{u_i}{\|u_i\|}$",
    r"$\frac{1}{\sqrt2}(1,0,1),\ \ \frac{1}{\sqrt3}(1,1,-1),\ \ \frac{1}{\sqrt6}(-1,2,1)$"]) + "</div>",
   panel=st.card("n-c", "ex", "כפל בסקלר חיובי ואז נרמול: אותו וקטור יחידה"))

dep = Scene("dep", "תלות לינארית", [
    P("ומה אם הוקטור השלישי הוא $(-3,-2,1)$, שזה בדיוק $v_1-2v_2$?", do=show("d-0"),
      say="ומה אם הוקטור השלישי הוא מינוס שלוש, מינוס שתיים, אחת, שזה בדיוק וִי אחת פחות פעמיים וִי שתיים?"),
    P("המקדמים יוצאים מינוס אחת ומינוס שתיים, ואחרי ההחסרה נשאר וקטור האפס.", do=show("d-1")),
    P("זה הסימן: הקבוצה תלויה לינארית. את הוקטור הזה זורקים, והפרישה לא נפגעת.", do=show("d-c"), hold=0.4),
], stage='<div class="pg-stack">' + w.rows("d", [
    r"$v_3'=(-3,-2,1)=v_1-2v_2$",
    r"$v_3'+u_1+2u_2=(0,0,0)$"]) + "</div>",
   panel=st.card("d-c", "trap", "⚠️ שארית אפס ⟸ הוקטור תלוי בקודמים"))

EX_STEM = ("ב-$M_2(\\mathbb{R})$ עם $\\langle A,B\\rangle=\\operatorname{tr}(B^TA)$, בצעו גרהם-שמידט על "
           "$A=\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$, $B=\\begin{pmatrix}1&1\\\\0&-1\\end{pmatrix}$.")
exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: גרהם-שמידט על שתי מטריצות, עם המכפלה הפנימית של העקבה.",
      say="שאלה ממבחן: גרהם-שמידט על שתי מטריצות, עם המכפלה הפנימית של העקבה."),
    P("זכרו: המכפלה היא סכום מכפלות של רכיבים באותו מקום.", do=show("x-c1")),
    P("הראשונה נשארת: $u_1=A$. הנורמה בריבוע: אחת ועוד אחת, שתיים.", do=show("x-0"),
      say="הראשונה נשארת: יוּ אחת שווה אֵיי. הנורמה בריבוע: אחת ועוד אחת, שתיים."),
    P("המכפלה של $B$ עם $A$: אחת, ועוד מינוס אחת כפול מינוס אחת. שוב שתיים.", do=show("x-1"),
      say="המכפלה של בִּי עם אֵיי: אחת, ועוד מינוס אחת כפול מינוס אחת. שוב שתיים."),
    P("המקדם הוא שתיים חלקי שתיים, אחת. אז $u_2=B-A$.", do=show("x-2"),
      say="המקדם הוא שתיים חלקי שתיים, אחת. אז יוּ שתיים הוא בִּי פחות אֵיי."),
    P("ויוצאת מטריצה עם אחת למעלה מימין, ואפסים בשאר.", do=show("x-3")),
    P("בדיקה: המכפלה עם $A$ היא אפס בכל מקום. ניצבות.", do=show("x-4"), say="בדיקה: המכפלה עם אֵיי היא אפס בכל מקום. ניצבות."),
    P("ולבסיס אורתונורמלי מחלקים בנורמות: $u_1$ בשורש שתיים, ו-$u_2$ כבר באורך אחת.", do=show("x-5"),
      say="ולבסיס אורתונורמלי מחלקים בנורמות: יוּ אחת בשורש שתיים, ויוּ שתיים כבר באורך אחת.", hold=0.3),
    P("המלכודת: לחלק בנורמה ולא בנורמה בריבוע. אז המקדם הוא שורש שתיים, והתוצאה לא ניצבת.", do=show("x-c2"), hold=0.5),
], stage='<div class="pg-stack">' + w.rows("x", [
    r"$u_1=A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad \|u_1\|^2=2$",
    r"$\langle B,u_1\rangle=1\cdot1+1\cdot0+0\cdot0+(-1)(-1)=2$",
    r"$u_2=B-\frac22\,u_1=B-A$",
    r"$u_2=\begin{pmatrix}0&1\\0&0\end{pmatrix}$",
    r"$\langle u_2,u_1\rangle=0\ \checkmark$",
    r"$\left\{\frac1{\sqrt2}\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ \begin{pmatrix}0&1\\0&0\end{pmatrix}\right\}$"],
    "sm") + "</div>",
   panel=w.stem("26B-A-Q1a", EX_STEM)
         + st.card("x-c1", "rule", "🔑 $\\langle A,B\\rangle=\\sum a_{ij}b_{ij}$")
         + st.card("x-c2", "trap", "⚠️ $\\frac{2}{\\sqrt2}$ במקום $\\frac22$: $\\langle u_2,u_1\\rangle=2-2\\sqrt2\\ne0$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: הוקטור הראשון נשאר. כל וקטור הבא הוא השארית שלו אחרי ההיטלים על כל הקודמים.", do=show("c-1")),
    P("מחלקים בנורמה **בריבוע**, ומותר להכפיל בסקלר שונה מאפס כדי להיפטר משברים.", do=show("c-2")),
    P("שארית אפס אומרת שהוקטור תלוי. ובסוף בודקים ניצבות, ומנרמלים רק אם מבקשים אורתונורמלי. נתראה ברמה הבאה.",
      do=show("c-3"), hold=0.6),
], stage='<div class="pg-stack">' + w.big("c-0", r"u_m=v_m-\sum_{i<m}\frac{\langle v_m,u_i\rangle}{\|u_i\|^2}u_i", "sm",
                                          hidden=False) + "</div>",
   panel=st.card("c-1", "rule", "🔑 $u_1=v_1$, ואז שאריות")
         + st.card("c-2", "trap", "⚠️ חלקי $\\|u_i\\|^2$")
         + st.card("c-3", "rule", "🔑 בדיקה: $\\langle u_i,u_j\\rangle=0$"))

VIDEO = Video("P05", "proj_gs", "גרהם-שמידט", [title, idea, r3, norm, dep, exam, recap], bank={"26B-A-Q1a": None})
