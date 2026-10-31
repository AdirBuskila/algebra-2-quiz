# -*- coding: utf-8 -*-
"""P04 · בסיס אורתוגונלי והיטל על תת-מרחב — video script (build: tools/video/vid.py P04).

Source: courses/proj_gs/C04.js (lesson + goal). Exam anchor: 25B-A-Q2d ({u,v,w} orthonormal basis of R^3 ⇒
uu^T+vv^T+ww^T = I), which no guided quiz uses. Avoided on purpose: the C04 quiz (u1=(1,1,0), u2=(1,-1,2),
v=(3,1,5); the g1,g2,g3 basis; Sp{(1,0,0),(1,1,0)}; (1,2,1)⟂(a,1,-1)), 23A-A-Q3c (a C04 quiz item) and its sibling
23A-A-Q3b (same alpha, beta). 26A-A-Q5a (P = uu^T+vv^T) is a close cousin of the anchor and is left alone.
Every vector below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R

# ---------------------------------------------------------------- an orthogonal basis of R^3, all norms 3
u1, u2, u3 = V(1, 2, 2), V(2, 1, -2), V(2, -2, 1)
assert w.dot(u1, u2) == 0 and w.dot(u1, u3) == 0 and w.dot(u2, u3) == 0
assert w.dot(u1, u1) == w.dot(u2, u2) == w.dot(u3, u3) == 9
# coordinates of x
x = V(1, 5, -1)
cs = [w.coef(x, u, w.dot) for u in (u1, u2, u3)]
assert [w.dot(x, u) for u in (u1, u2, u3)] == [9, 9, -9] and cs == [1, 1, -1]
assert u1 + u2 - u3 == x
assert w.dot(x, x) == 27 == 9 * (1 + 1 + 1)
g = [u / 3 for u in (u1, u2, u3)]
assert [w.dot(x, gi) for gi in g] == [3, 3, -3] and 3 ** 2 + 3 ** 2 + 3 ** 2 == 27

# ---------------------------------------------------------------- projection on W = Sp{u1, u2}
v = V(9, 0, 0)
assert [w.dot(v, u1), w.dot(v, u2)] == [9, 18]
p = w.proj(v, [u1, u2], w.dot)
assert list(p) == [5, 4, -2] and p == u1 + 2 * u2
r = v - p
assert list(r) == [4, -4, 2] and r == 2 * u3 and w.dot(r, u1) == 0 and w.dot(r, u2) == 0
assert w.dot(v, v) == 81 == w.dot(p, p) + w.dot(r, r) and w.dot(p, p) == 45 and w.dot(r, r) == 36

# ---------------------------------------------------------------- the trap: a basis that is not orthogonal
w1, w2, vt = V(1, 1, 0), V(0, 1, 1), V(0, 0, 3)
assert w.dot(w1, w2) == 1
bad = w.coef(vt, w1, w.dot) * w1 + w.coef(vt, w2, w.dot) * w2
assert list(bad) == [0, R(3, 2), R(3, 2)]
assert w.dot(vt - bad, w1) == R(-3, 2)                       # the residual is not ⟂ W: wrong
us, _ = w.gram_schmidt([w1, w2], w.dot)
good = w.proj(vt, us, w.dot)
assert list(good) == [-1, 1, 2] and w.dot(vt - good, w1) == 0 and w.dot(vt - good, w2) == 0

# ---------------------------------------------------------------- exam 25B-A-Q2d
Asum = sum((gi * gi.T for gi in g), sp.zeros(3, 3))
assert Asum == sp.eye(3)
assert sum((u * u.T for u in (u1, u2, u3)), sp.zeros(3, 3)) == 9 * sp.eye(3)    # not normalized: 9I
xs = sp.Matrix(sp.symbols("x1 x2 x3", real=True))
assert sp.simplify(Asum * xs - sum((w.dot(xs, gi) * gi for gi in g), sp.zeros(3, 1))) == sp.zeros(3, 1)
assert (g[0].T * g[0])[0] == 1 and (g[0] * g[0].T).shape == (3, 3)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נעבור מהיטל על ישר להיטל על **תת מרחב** שלם."),
    P("נראה למה בסיס אורתוגונלי הופך את החישוב לפשוט, ומתי אסור להשתמש בנוסחה."),
    P("ובסוף נוכיח טענה ממבחן על בסיס אורתונורמלי.", hold=0.4),
], stage='<div class="kicker">P04 · היטל וגרהם-שמידט</div><h1>בסיס אורתוגונלי והיטל על תת-מרחב</h1>'
         '<p>לחשב קואורדינטות בבסיס אורתונורמלי והיטל על תת-מרחב שנתון בבסיס אורתוגונלי, ולזהות מתי הנוסחה אסורה.</p>',
   layout="title")

idea = Scene("idea", "הרעיון", [
    P("מערכת **אורתוגונלית** היא קבוצה של וקטורים שונים מאפס, שכל זוג מהם ניצב.", do=show("i-0")),
    P("מערכת כזו תמיד בלתי תלויה לינארית.", do=show("i-c1")),
    P("ואם בנוסף כל הנורמות שוות אחת, המערכת נקראת **אורתונורמלית**.", do=show("i-1")),
    P("היתרון הגדול: את המקדמים של וקטור בבסיס כזה לא צריך למצוא ממערכת משוואות.", hold=0.2),
    P("כל מקדם הוא היטל על וקטור אחד: המכפלה עם הוקטור, חלקי הנורמה שלו בריבוע.", do=show("i-2")),
    P("ובבסיס אורתונורמלי המכנה הוא אחת, אז המקדם הוא פשוט המכפלה הפנימית.", do=show("i-3"), hold=0.4),
], stage='<div class="pg-stack">' + w.rows("i", [
    r"$\langle u_i,u_j\rangle=0\quad (i\ne j)$",
    r"$\|g_i\|=1$",
    r"$x=\sum_i \alpha_i u_i,\qquad \alpha_i=\frac{\langle x,u_i\rangle}{\|u_i\|^2}$",
    r"$\alpha_i=\langle x,g_i\rangle$"]) + "</div>",
   panel=st.card("i-c1", "rule", "🔑 אורתוגונלית ⟸ בלתי תלויה"))

coords = Scene("coords", "קואורדינטות", [
    P("שלושה וקטורים ב-$\\mathbb{R}^3$. נבדוק: כל שתי מכפלות יוצאות אפס, ולכל אחד נורמה בריבוע תשע.", do=show("k-0", "k-1"),
      say="שלושה וקטורים באר שלוש. נבדוק: כל שתי מכפלות יוצאות אפס, ולכל אחד נורמה בריבוע תשע."),
    P("אז זה בסיס אורתוגונלי. נכתוב בו את הוקטור $x=(1,5,-1)$.", do=show("k-2"),
      say="אז זה בסיס אורתוגונלי. נכתוב בו את הוקטור אִקְס: אחת, חמש, מינוס אחת."),
    P("המכפלות של $x$ עם שלושת הוקטורים: תשע, תשע, ומינוס תשע.", do=show("k-3"),
      say="המכפלות של אִקְס עם שלושת הוקטורים: תשע, תשע, ומינוס תשע."),
    P("מחלקים בתשע, ומקבלים את המקדמים: אחת, אחת, ומינוס אחת.", do=show("k-4")),
    P("בדיקה: $u_1+u_2-u_3$ נותן בדיוק $(1,5,-1)$.", do=show("k-5"),
      say="בדיקה: יוּ אחת ועוד יוּ שתיים פחות יוּ שלוש נותן בדיוק אחת, חמש, מינוס אחת."),
    P("ופיתגורס: הנורמה בריבוע של $x$ היא עשרים ושבע, וזה תשע כפול סכום ריבועי המקדמים.", do=show("k-6", "k-c"),
      say="ופיתגורס: הנורמה בריבוע של אִקְס היא עשרים ושבע, וזה תשע כפול סכום ריבועי המקדמים.", hold=0.4),
], stage='<div class="pg-stack">' + w.rows("k", [
    f"$u_1={w.tup(u1)},\\ u_2={w.tup(u2)},\\ u_3={w.tup(u3)}$",
    r"$\langle u_i,u_j\rangle=0,\quad \|u_i\|^2=9$",
    f"$x={w.tup(x)}$",
    r"$\langle x,u_1\rangle=9,\ \langle x,u_2\rangle=9,\ \langle x,u_3\rangle=-9$",
    r"$\alpha=\left(\frac99,\frac99,\frac{-9}{9}\right)=(1,1,-1)$",
    r"$u_1+u_2-u_3=(1,5,-1)\ \checkmark$",
    r"$\|x\|^2=27=9\,(1+1+1)$"], "sm") + "</div>",
   panel=st.card("k-c", "rule", "🔑 בלי מערכת משוואות: כל מקדם בנפרד"))

projw = Scene("projw", "היטל על תת-מרחב", [
    P("עכשיו היטל על תת מרחב. אם יש לו בסיס **אורתוגונלי**, ההיטל הוא סכום ההיטלים על כל וקטור בנפרד.", do=show("p-f")),
    P("ניקח את $W$, הפרישה של $u_1$ ו-$u_2$, ואת $v=(9,0,0)$.", do=show("p-0"),
      say="ניקח את דַאבְּלְיוּ, הפרישה של יוּ אחת ויוּ שתיים, ואת וִי: תשע, אפס, אפס."),
    P("המכפלות: תשע, ושמונה עשרה. מחלקים בתשע: המקדמים הם אחת ושתיים.", do=show("p-1")),
    P("אז ההיטל הוא $u_1+2u_2=(5,4,-2)$.", do=show("p-2"),
      say="אז ההיטל הוא יוּ אחת ועוד פעמיים יוּ שתיים: חמש, ארבע, מינוס שתיים."),
    P("השארית היא $(4,-4,2)$. והיא ניצבת גם ל-$u_1$ וגם ל-$u_2$, כלומר לכל $W$.", do=show("p-3", "p-c1"),
      say="השארית היא ארבע, מינוס ארבע, שתיים. והיא ניצבת גם ליוּ אחת וגם ליוּ שתיים, כלומר לכל דַאבְּלְיוּ."),
    P("למעשה היא פעמיים $u_3$, הוקטור שלא בתת המרחב. ופיתגורס: שמונים ואחת שווה ארבעים וחמש ועוד שלושים ושש.",
      do=show("p-4"), say="למעשה היא פעמיים יוּ שלוש, הוקטור שלא בתת המרחב. ופיתגורס: שמונים ואחת שווה ארבעים וחמש ועוד שלושים ושש.",
      hold=0.4),
], stage='<div class="pg-stack">' + w.big("p-f", r"\operatorname{Proj}_W(v)=\sum_i\frac{\langle v,u_i\rangle}{\|u_i\|^2}\,u_i", "sm")
         + w.rows("p", [
             r"$W=\operatorname{Sp}\{u_1,u_2\},\quad v=(9,0,0)$",
             r"$\frac{\langle v,u_1\rangle}{9}=\frac99=1,\quad \frac{\langle v,u_2\rangle}{9}=\frac{18}{9}=2$",
             r"$\operatorname{Proj}_W(v)=u_1+2u_2=(5,4,-2)$",
             r"$v-\operatorname{Proj}_W(v)=(4,-4,2)\perp u_1,u_2$",
             r"$=2u_3,\qquad 81=45+36$"], "sm") + "</div>",
   panel=st.card("p-c1", "rule", "🔑 השארית ניצבת לכל וקטור ב-$W$"))

trap = Scene("trap", "מלכודת", [
    P("והנה המלכודת. הנוסחה עובדת **רק** לבסיס אורתוגונלי.", do=show("t-c0")),
    P("ניקח את $(1,1,0)$ ו-$(0,1,1)$. המכפלה שלהם היא אחת, לא אפס.", do=show("t-0"),
      say="ניקח את אחת, אחת, אפס, ואת אפס, אחת, אחת. המכפלה שלהם היא אחת, לא אפס."),
    P("אם בכל זאת נציב בנוסחה את $v=(0,0,3)$, נקבל $(0,\\frac32,\\frac32)$.", do=show("t-1"),
      say="אם בכל זאת נציב בנוסחה את וִי: אפס, אפס, שלוש, נקבל אפס, שלוש חצאים, שלוש חצאים."),
    P("נבדוק את השארית מול הוקטור הראשון: יוצא מינוס שלוש חצאים. לא אפס, אז זה לא ההיטל.", do=show("t-2", "t-c1")),
    P("ההיטל הנכון הוא $(-1,1,2)$. כדי להגיע אליו צריך קודם להפוך את הבסיס לאורתוגונלי, בגרהם-שמידט.", do=show("t-3"),
      say="ההיטל הנכון הוא מינוס אחת, אחת, שתיים. כדי להגיע אליו צריך קודם להפוך את הבסיס לאורתוגונלי, בגרהם-שמידט.",
      hold=0.5),
], stage='<div class="pg-stack">' + w.rows("t", [
    r"$w_1=(1,1,0),\ w_2=(0,1,1):\quad \langle w_1,w_2\rangle=1\ne0$",
    r"$\frac{0}{2}w_1+\frac32 w_2=\left(0,\frac32,\frac32\right)$",
    r"$\left\langle (0,0,3)-\left(0,\frac32,\frac32\right),\,w_1\right\rangle=-\frac32\ne0$",
    r"$\operatorname{Proj}_W(v)=(-1,1,2)$"], "sm") + "</div>",
   panel=st.card("t-c0", "trap", "⚠️ קודם בודקים ניצבות, ורק אז מציבים")
         + st.card("t-c1", "ex", "בדיקת השארית תופסת את הטעות"))

EX_STEM = ("יהי $\\{\\vec u,\\vec v,\\vec w\\}$ בסיס <b>אורתונורמלי</b> של $\\mathbb{R}^3$, ונגדיר "
           "$A=\\vec u\\vec u^T+\\vec v\\vec v^T+\\vec w\\vec w^T$. הוכיחו כי $A=I$.")
exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: שלושה וקטורים שהם בסיס אורתונורמלי, ומטריצה שהיא סכום של שלוש מכפלות. צריך להוכיח שהיא מטריצת היחידה."),
    P("שימו לב: $\\vec u\\vec u^T$ היא **מטריצה**, שלוש על שלוש. לא מספר.", do=show("x-c1"),
      say="שימו לב: יוּ כפול יוּ טְרַנְסְפּוֹז היא מטריצה, שלוש על שלוש. לא מספר."),
    P("נכפול את $A$ בוקטור כלשהו $\\vec x$. כל איבר נותן וקטור כפול מכפלה פנימית.", do=show("x-0", "x-1"),
      say="נכפול את אֵיי בוקטור כלשהו אִקְס. כל איבר נותן וקטור כפול מכפלה פנימית."),
    P("וזו בדיוק ההצגה של $\\vec x$ בבסיס האורתונורמלי: כל מקדם הוא המכפלה עם וקטור הבסיס.", do=show("x-2"),
      say="וזו בדיוק ההצגה של אִקְס בבסיס האורתונורמלי: כל מקדם הוא המכפלה עם וקטור הבסיס."),
    P("אז $A\\vec x=\\vec x$ לכל $\\vec x$.", do=show("x-3"), say="אז אֵיי אִקְס שווה אִקְס לכל אִקְס."),
    P("ומטריצה שלא משנה אף וקטור היא מטריצת היחידה: הציבו את וקטורי היחידה, וקבלו את העמודות שלה.", do=show("x-4"),
      hold=0.3),
    P("נבדוק על הבסיס שלנו, אחרי חלוקה בשלוש: סכום שלוש המכפלות יוצא בדיוק מטריצת היחידה.", do=show("x-5")),
    P("והמלכודת: בלי נרמול זה נשבר. עם הוקטורים המקוריים, שהנורמה שלהם שלוש, יוצא תשע כפול היחידה.",
      do=show("x-6", "x-c2"), hold=0.5),
], stage='<div class="pg-stack">' + w.rows("x", [
    r"$A\vec x=\vec u(\vec u^T\vec x)+\vec v(\vec v^T\vec x)+\vec w(\vec w^T\vec x)$",
    r"$=\langle\vec x,\vec u\rangle\vec u+\langle\vec x,\vec v\rangle\vec v+\langle\vec x,\vec w\rangle\vec w$",
    r"$=\vec x$",
    r"$A\vec x=\vec x\ \ \forall\vec x$",
    r"$A\vec e_j=\vec e_j\ \Rightarrow\ A=I$",
    r"$g_i=\tfrac13u_i:\quad g_1g_1^T+g_2g_2^T+g_3g_3^T=I\ \checkmark$",
    r"$u_1u_1^T+u_2u_2^T+u_3u_3^T=9I$"], "sm") + "</div>",
   panel=w.stem("25B-A-Q2d", EX_STEM)
         + st.card("x-c1", "ex", "$\\vec u\\vec u^T$: מטריצה. $\\vec u^T\\vec u$: מספר")
         + st.card("x-c2", "trap", "⚠️ צריך <b>אורתונורמלי</b>, לא רק אורתוגונלי"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: בבסיס אורתוגונלי, כל מקדם הוא מכפלה חלקי נורמה בריבוע. בבסיס אורתונורמלי, רק המכפלה.", do=show("c-1")),
    P("ההיטל על תת מרחב הוא סכום ההיטלים על וקטורי בסיס **אורתוגונלי**, והשארית ניצבת לכל תת המרחב.", do=show("c-2")),
    P("ואם הבסיס לא אורתוגונלי, הנוסחה אסורה. את הפתרון, גרהם-שמידט, נראה ברמה הבאה.", do=show("c-3"), hold=0.6),
], stage='<div class="pg-stack">' + w.big("c-0", r"\operatorname{Proj}_W(v)=\sum_i\frac{\langle v,u_i\rangle}{\|u_i\|^2}\,u_i",
                                          "sm", hidden=False) + "</div>",
   panel=st.card("c-1", "rule", "🔑 $\\alpha_i=\\frac{\\langle x,u_i\\rangle}{\\|u_i\\|^2}$")
         + st.card("c-2", "rule", "🔑 $v-\\operatorname{Proj}_W(v)\\perp W$")
         + st.card("c-3", "trap", "⚠️ בסיס לא אורתוגונלי: קודם גרהם-שמידט"))

VIDEO = Video("P04", "proj_gs", "בסיס אורתוגונלי והיטל על תת-מרחב", [title, idea, coords, projw, trap, exam, recap],
              bank={"25B-A-Q2d": None})
