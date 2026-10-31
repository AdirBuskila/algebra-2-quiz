# -*- coding: utf-8 -*-
"""P08 · ריבועים פחותים דרך היטל — video script (build: tools/video/vid.py P08).

Source: courses/proj_gs/C08.js (lesson + goal). Exam anchor: 24B-A-Q3b (best line for (-3,-1),(0,1),(1,3),(3,3),(4,6)),
which no guided quiz uses; it is solved here through the projection (Gram-Schmidt on the columns x, 1 makes them
orthogonal: x - x̄ and 1), and cross-checked against the normal equations of the official solution.
Avoided on purpose: the C08 quiz (a1=(1,1,0), a2=(1,-1,2) with b=(4,0,1); columns (1,0,1),(0,1,1) with b=(1,1,0)),
the lesson example (b=(2,0,5)), 23A-B-Q1a (a C08 quiz item) and its twin 26A-B-Q1c (same A and b).
Every vector and number below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R

# ---------------------------------------------------------------- the picture: one column in R^2
a, b0 = V(3, 1), V(1, 3)
assert w.coef(b0, a, w.dot) == R(3, 5)                      # 3x = 1, x = 3 has no solution; x̂ = 3/5
PIC, p0, c0 = w.proj2d("lp", a, b0, box=(-1.6, 4.0, -0.6, 3.6), size=(620, 465),
                       names=("Col(A)", "b", "Ax̂", "b−Ax̂"), sides=(-1, 1, 1, -1), at=(0.88, 0.5, 0.45, 0.5))
assert list(p0) == [R(9, 5), R(3, 5)] and w.dot(c0, a) == 0

# ---------------------------------------------------------------- orthogonal columns: no inverse needed
a1, a2, b = V(1, 1, 1), V(1, 0, -1), V(1, 2, 6)
assert w.dot(a1, a2) == 0
x1, x2 = w.coef(b, a1, w.dot), w.coef(b, a2, w.dot)
assert (w.dot(b, a1), w.dot(a1, a1), w.dot(b, a2), w.dot(a2, a2)) == (9, 3, -5, 2) and (x1, x2) == (3, R(-5, 2))
A = a1.row_join(a2)
assert (A.T * A).LUsolve(A.T * b) == V(3, R(-5, 2))           # same as the normal equations
p = x1 * a1 + x2 * a2
r = b - p
assert list(p) == [R(1, 2), 3, R(11, 2)] and list(r) == [R(1, 2), -1, R(1, 2)]
assert w.dot(r, a1) == 0 and w.dot(r, a2) == 0 and w.dot(r, r) == R(3, 2)

# the trap: the shortcut on columns that are not orthogonal
c1, c2 = V(1, 1, 1), V(0, 1, 2)
assert w.dot(c1, c2) == 3
short = w.coef(b, c2, w.dot)
B = c1.row_join(c2)
true = (B.T * B).LUsolve(B.T * b)
assert short == R(14, 5) and list(true) == [R(1, 2), R(5, 2)] and short != true[1]

# ---------------------------------------------------------------- exam 24B-A-Q3b through the projection
pts = [(-3, -1), (0, 1), (1, 3), (3, 3), (4, 6)]
X = V(*[q[0] for q in pts])
Y = V(*[q[1] for q in pts])
one = V(1, 1, 1, 1, 1)
xbar, ybar = R(sum(X), 5), R(sum(Y), 5)
assert (sum(X), sum(Y), xbar, ybar) == (5, 12, 1, R(12, 5))
(u1, u2), cg = w.gram_schmidt([one, X], w.dot)
assert u1 == one and cg[(1, 0)] == xbar and list(u2) == [-4, -1, 0, 2, 3]       # x - x̄
assert w.dot(u2, u2) == 30 and w.dot(Y, u2) == 27 and w.coef(Y, u1, w.dot) == ybar
m = w.coef(Y, u2, w.dot)
n = ybar - m * xbar
assert m == R(9, 10) and n == R(3, 2)
# cross-check with the normal equations (the official solution)
Afull = X.row_join(one)
assert Afull.T * Afull == M([[35, 5], [5, 5]]) and Afull.T * Y == V(39, 12)
assert (Afull.T * Afull).LUsolve(Afull.T * Y) == V(m, n)
res = Y - (m * X + n * one)
assert list(res) == [R(1, 5), R(-1, 2), R(3, 5), R(-6, 5), R(9, 10)] and sum(res) == 0 and w.dot(res, X) == 0
assert m * xbar + n == ybar                                   # the line passes through (x̄, ȳ)
PLOT = w.lsplot("ls", pts, box=(-3.8, 4.8, -1.8, 6.8), size=(560, 560), line=(m, n), xbar=xbar,
                extra={"flat": (0, ybar, "v")})

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("ברמה הקודמת פתרנו ריבועים פחותים בעזרת משוואות הנורמל. עכשיו נבין **מה** הן מחשבות."),
    P("נראה שהפתרון הוא בעצם היטל, ושכשהעמודות ניצבות לא צריך להפוך שום מטריצה."),
    P("ונפתור שאלת מבחן על ישר, בדרך של היטל.", hold=0.4),
], stage='<div class="kicker">P08 · היטל וגרהם-שמידט</div><h1>ריבועים פחותים דרך היטל</h1>'
         '<p>להבין ש-$A\\hat x$ הוא ההיטל של $\\vec b$ על $\\operatorname{Col}(A)$, לחשב $\\hat x$ בלי הפיכת מטריצה '
         'כשהעמודות ניצבות, ולחשב את השגיאה.</p>', layout="title")

idea = Scene("idea", "הרעיון", [
    P("הוקטור $A\\vec x$ הוא תמיד צירוף של העמודות של $A$. כלומר הוא נמצא במרחב העמודות.", do=show("lp-a", "lp-line"),
      say="הוקטור אֵיי אִקְס הוא תמיד צירוף של העמודות של אֵיי. כלומר הוא נמצא במרחב העמודות."),
    P("אם אין פתרון, זה אומר ש-$\\vec b$ פשוט לא נמצא שם.", do=show("lp-b"),
      say="אם אין פתרון, זה אומר שבִּי פשוט לא נמצא שם."),
    P("הנקודה הכי קרובה ל-$\\vec b$ במרחב העמודות היא ההיטל. ולכן $A\\hat x$ הוא ההיטל של $\\vec b$.",
      do=show("lp-p", "i-0"), say="הנקודה הכי קרובה לבִּי במרחב העמודות היא ההיטל. ולכן אֵיי אִקְס כובע הוא ההיטל של בִּי."),
    P("והשארית ניצבת למרחב העמודות. זה בדיוק התנאי של משוואות הנורמל.", do=show("lp-c", "lp-ra", "i-1")),
    P("והשגיאה של הריבועים הפחותים היא הנורמה בריבוע של השארית.", do=show("i-2"), hold=0.4),
], stage='<div class="pg-stack">' + PIC + "</div>",
   panel=w.rows("i", [
       r"$A\hat x=\operatorname{Proj}_{\operatorname{Col}(A)}\vec b$",
       r"$\vec b-A\hat x\perp\operatorname{Col}(A)$",
       r"$\text{err}=\|\vec b-A\hat x\|^2$"], "sm"))

orth = Scene("orth", "עמודות ניצבות", [
    P("וכשהעמודות של $A$ **ניצבות** זו לזו, ההיטל פשוט: כל מקדם הוא מקדם ההיטל על העמודה שלו.", do=show("o-0"),
      say="וכשהעמודות של אֵיי ניצבות זו לזו, ההיטל פשוט: כל מקדם הוא מקדם ההיטל על העמודה שלו."),
    P("דוגמה: העמודות $(1,1,1)$ ו-$(1,0,-1)$. המכפלה שלהן אפס.", do=show("o-1"),
      say="דוגמה: העמודות אחת אחת אחת, ואחת אפס מינוס אחת. המכפלה שלהן אפס."),
    P("ו-$\\vec b=(1,2,6)$. המקדם הראשון: תשע חלקי שלוש, שלוש. השני: מינוס חמש חלקי שתיים.", do=show("o-2"),
      say="ובִּי הוא אחת, שתיים, שש. המקדם הראשון: תשע חלקי שלוש, שלוש. השני: מינוס חמש חלקי שתיים."),
    P("בלי מטריצה הפוכה, ובלי מערכת. ההיטל עצמו הוא הצירוף הזה של העמודות.", do=show("o-3")),
    P("השארית היא חצי, מינוס אחת, חצי, והיא ניצבת לשתי העמודות. השגיאה: שלוש חצאים.", do=show("o-4", "o-5"), hold=0.3),
    P("ושימו לב: העמודה הראשונה היא אחדות, והשנייה היא ערכי $x$: $1,0,-1$. זה בעצם ישר!", say="ושימו לב: העמודה הראשונה היא אחדות, והשנייה היא אִקְסים: אחת, אפס, מינוס אחת. זה בעצם ישר!", do=show("o-c")),
    P("כש-$\\sum x_i=0$, שתי העמודות ניצבות. ואת זה ננצל עוד רגע בשאלת המבחן.", say="כשסכום האִקְסים הוא אפס, שתי העמודות ניצבות. ואת זה ננצל עוד רגע בשאלת המבחן.", hold=0.4),
], stage='<div class="pg-stack">' + w.rows("o", [
    r"$\hat x_1=\frac{\langle\vec b,a_1\rangle}{\|a_1\|^2},\ \hat x_2=\frac{\langle\vec b,a_2\rangle}{\|a_2\|^2}$",
    r"$a_1=(1,1,1),\ a_2=(1,0,-1),\ \langle a_1,a_2\rangle=0$",
    r"$\vec b=(1,2,6):\quad \hat x_1=\frac93=3,\ \hat x_2=\frac{-5}{2}$",
    r"$A\hat x=3a_1-\frac52a_2=\left(\frac12,3,\frac{11}{2}\right)$",
    r"$\vec b-A\hat x=\left(\frac12,-1,\frac12\right)\perp a_1,a_2$",
    r"$\text{err}=\frac14+1+\frac14=\frac32$"], "sm") + "</div>",
   panel=st.card("o-c", "ex", "$a_1$ = אחדות, $a_2$ = ערכי $x$: ישר דרך $(1,1),(0,2),(-1,6)$"))

trap = Scene("trap", "מלכודת", [
    P("והמלכודת: הקיצור הזה נכון **רק** לעמודות ניצבות.", do=show("t-c0")),
    P("נחליף את העמודה השנייה ל-$(0,1,2)$. עכשיו המכפלה עם עמודת האחדות היא שלוש, לא אפס.", do=show("t-0"),
      say="נחליף את העמודה השנייה לאפס, אחת, שתיים. עכשיו המכפלה עם עמודת האחדות היא שלוש, לא אפס."),
    P("הקיצור נותן ארבע עשרה חמישיות. אבל משוואות הנורמל נותנות חמש חצאים.", do=show("t-1", "t-2")),
    P("כשהעמודות לא ניצבות, פותרים את משוואות הנורמל. או קודם עושים גרהם-שמידט על העמודות.", do=show("t-c1"), hold=0.4),
], stage='<div class="pg-stack">' + w.rows("t", [
    r"$c_1=(1,1,1),\ c_2=(0,1,2):\ \langle c_1,c_2\rangle=3\ne0$",
    r"$\frac{\langle\vec b,c_2\rangle}{\|c_2\|^2}=\frac{14}{5}\quad$ ✗",
    r"$A^TA\hat x=A^T\vec b:\quad \hat x=\left(\frac12,\frac52\right)$"], "sm") + "</div>",
   panel=st.card("t-c0", "trap", "⚠️ $\\hat x_i=\\frac{\\langle\\vec b,a_i\\rangle}{\\|a_i\\|^2}$ רק לעמודות ניצבות")
         + st.card("t-c1", "rule", "🔑 אחרת: משוואות הנורמל, או גרהם-שמידט על העמודות"))

EX_STEM = ("נתונות 5 נקודות במישור: $(-3,-1),\\ (0,1),\\ (1,3),\\ (3,3),\\ (4,6)$. מצאו את משוואת הישר הקרוב "
           "ביותר לנקודות בשיטת הריבועים הפחותים.")
exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: חמש נקודות, והישר הקרוב ביותר. נפתור אותה דרך היטל."),
    P("העמודות הן ערכי $x$ ועמודת אחדות. הן לא ניצבות, כי $\\sum x_i=5$.", say="העמודות הן האִקְסים ועמודת אחדות. הן לא ניצבות, כי סכום האִקְסים הוא חמש.", do=show("x-0")),
    P("אז נעשה גרהם-שמידט על העמודות: מעמודת $x$ מחסירים את ההיטל על האחדות, כלומר את הממוצע $\\bar x=1$.", say="אז נעשה גרהם-שמידט על העמודות: מאִקְס מחסירים את ההיטל על האחדות, כלומר את הממוצע, אחת.", do=show("x-1", "ls-xbar")),
    P("מקבלים את העמודה מינוס ארבע, מינוס אחת, אפס, שתיים, שלוש. הסכום שלה אפס, אז היא ניצבת לאחדות.", do=show("x-2")),
    P("עכשיו כל מקדם לבד. על עמודת האחדות: הממוצע $\\bar y=\\frac{12}{5}$.", say="עכשיו כל מקדם לבד. על עמודת האחדות: הממוצע של הוַואים, שתים עשרה חמישיות.", do=show("x-3", "ls-flat")),
    P("ועל העמודה הממורכזת: עשרים ושבע חלקי שלושים, כלומר תשע עשיריות. זה השיפוע.", do=show("x-4")),
    P("אז הישר הוא $y=\\frac{9}{10}(x-1)+\\frac{12}{5}$.", say="אז הישר הוא תשע עשיריות כפול, בסוגריים, אִקְס פחות אחת, ועוד שתים עשרה חמישיות.", do=show("x-5")),
    P("ובפתיחת סוגריים: $y=0.9x+1.5$.", do=show("x-6", "ls-line"), say="ובפתיחת סוגריים: וַואי שווה אפס נקודה תשע אִקְס, ועוד אחת נקודה חמש."),
    P("בדיקה מול משוואות הנורמל: אותו פתרון בדיוק. והשאריות מסתכמות לאפס.", do=show("x-c1", "ls-res"), hold=0.3),
    P("שימו לב: הישר תמיד עובר בנקודת הממוצעים, אחת ושתים עשרה חמישיות. זו בדיקה מהירה לכל ישר כזה.", do=show("x-c2"),
      hold=0.5),
], stage='<div class="pg-two">' + PLOT + w.rows("x", [
    r"$\sum x=5\ne0$",
    r"$u_2=x-\frac{\langle x,\mathbf 1\rangle}{5}\mathbf 1=x-1$",
    r"$u_2=(-4,-1,0,2,3)\perp\mathbf 1$",
    r"$\frac{\langle y,\mathbf 1\rangle}{5}=\frac{12}{5}$",
    r"$m=\frac{\langle y,u_2\rangle}{\|u_2\|^2}=\frac{27}{30}=\frac{9}{10}$",
    r"$y=\frac{9}{10}(x-1)+\frac{12}{5}$",
    r"$y=0.9x+1.5$"], "sm") + "</div>",
   panel=w.stem("24B-A-Q3b", EX_STEM)
         + st.card("x-c1", "rule", "🔑 $\\begin{pmatrix}35&5\\\\5&5\\end{pmatrix}\\hat x=\\begin{pmatrix}39\\\\12\\end{pmatrix}$ ⟸ אותו ישר")
         + st.card("x-c2", "ex", "הישר עובר ב-$(\\bar x,\\bar y)=\\left(1,\\frac{12}{5}\\right)$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $A\\hat x$ הוא ההיטל של $\\vec b$ על מרחב העמודות, והשארית ניצבת לו.", do=show("c-1"),
      say="לסיכום: אֵיי אִקְס כובע הוא ההיטל של בִּי על מרחב העמודות, והשארית ניצבת לו."),
    P("כשהעמודות ניצבות, כל מקדם מחושב לבד. השגיאה היא הנורמה בריבוע של השארית.", do=show("c-2")),
    P("וכשהן לא ניצבות: משוואות הנורמל, או גרהם-שמידט על העמודות. ובשביל זה בדיוק יש פירוק QR, ברמה הבאה.",
      do=show("c-3"), hold=0.6, say="וכשהן לא ניצבות: משוואות הנורמל, או גרהם-שמידט על העמודות. "
                                    "ובשביל זה בדיוק יש פירוק קְיוּ אָר, ברמה הבאה."),
], stage='<div class="pg-stack">' + w.big("c-0", r"A\hat x=\operatorname{Proj}_{\operatorname{Col}(A)}\vec b", hidden=False)
         + "</div>",
   panel=st.card("c-1", "rule", "🔑 $\\vec b-A\\hat x\\perp\\operatorname{Col}(A)$")
         + st.card("c-2", "rule", "🔑 עמודות ניצבות: $\\hat x_i=\\frac{\\langle\\vec b,a_i\\rangle}{\\|a_i\\|^2}$")
         + st.card("c-3", "trap", "⚠️ לא ניצבות: משוואות הנורמל"))

VIDEO = Video("P08", "proj_gs", "ריבועים פחותים דרך היטל", [title, idea, orth, trap, exam, recap],
              bank={"24B-A-Q3b": None})
