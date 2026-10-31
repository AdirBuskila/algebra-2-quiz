# -*- coding: utf-8 -*-
"""P03 · היטל על וקטור יחיד — video script (build: tools/video/vid.py P03).

Source: courses/proj_gs/C03.js (lesson + goal). Exam anchor: 23B-B-Q5c (P = v v^T for a unit v; prove u - Pu ⟂ v),
which no guided quiz uses. Avoided on purpose: the C03 quiz (a=(1,1,1), b=(2,3,7); a=(3,4), b=(2,11);
a=(3/5,4/5) with P=aa^T) and 26A-A-Q3c / 26A-A-Q3d (c ⟂ a and Pythagoras for the abstract p, c: C03 quiz items).
23B-B-Q5b (P^2 = P, positive semidefinite) belongs to the pos_def topic and is not solved here.
Every vector below is computed with sympy and asserted; the picture is drawn from the same numbers.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R

# ---------------------------------------------------------------- example: a = (2,1), b = (3,4)
a, b = V(2, 1), V(3, 4)
assert w.dot(b, a) == 10 and w.dot(a, a) == 5 and w.coef(b, a, w.dot) == 2
p = w.proj(b, [a], w.dot)
c = b - p
assert list(p) == [4, 2] and list(c) == [-1, 2] and w.dot(c, a) == 0 and w.dot(c, p) == 0
assert w.dot(b, b) == 25 == w.dot(p, p) + w.dot(c, c) and w.dot(p, p) == 20 and w.dot(c, c) == 5
PIC, _, _ = w.proj2d("pj", a, b, box=(-1.6, 5.4, -0.8, 5.0), size=(640, 530), sides=(-1, 1, -1, 1))

# the trap: dividing by |a| instead of |a|^2
wrong = (w.dot(b, a) / sp.sqrt(w.dot(a, a))) * a
assert sp.simplify(wrong - 2 * sp.sqrt(5) * a) == sp.zeros(2, 1)
assert sp.simplify(w.dot(b - wrong, a) - (10 - 10 * sp.sqrt(5))) == 0 and w.dot(b - wrong, a) != 0
PIC2, _, _ = w.proj2d("pw", a, b, box=(-1.2, 9.8, -0.8, 5.6), size=(700, 410), wrong=[float(t) for t in wrong],
                      sides=(-1, 1, -1, 1))

# matrix form: q = a/|a|, P = q q^T
q = a / sp.sqrt(5)
Pm = sp.simplify(q * q.T)
assert Pm == M([[R(4, 5), R(2, 5)], [R(2, 5), R(1, 5)]]) and Pm * b == p
assert Pm == a * a.T / w.dot(a, a)
assert 5 * Pm == M([[4, 2], [2, 1]]) and list(5 * Pm * b) == [20, 10]

# ---------------------------------------------------------------- exam 23B-B-Q5c
vv = V(R(2, 3), R(1, 3), R(2, 3))
assert w.dot(vv, vv) == 1
u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
uu = sp.Matrix([u1, u2, u3])
PP = vv * vv.T
assert sp.simplify(PP * uu - w.dot(uu, vv) * vv) == sp.zeros(3, 1)          # Pu = <u,v> v: the projection
assert sp.simplify((vv.T * (uu - PP * uu))[0]) == 0                        # u - Pu ⟂ v for every u
assert (vv.T * vv)[0] == 1
# not a unit vector: the claim fails
v2, uq = V(1, 1), V(1, 0)
r2 = uq - v2 * v2.T * uq
assert list(r2) == [0, -1] and w.dot(r2, v2) == -1

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את הפעולה החשובה ביותר בקורס: **היטל**."),
    P("נטיל וקטור על ישר, נמצא את השארית ואת המרחק, ונראה למה השארית תמיד ניצבת."),
    P("ובסוף נוכיח טענה ממבחן, בשלוש שורות.", hold=0.4),
], stage='<div class="kicker">P03 · היטל וגרהם-שמידט</div><h1>היטל על וקטור יחיד</h1>'
         '<p>לחשב את ההיטל של וקטור על וקטור אחר, את השארית ואת המרחק, ולהשתמש בניצבות השארית ובפיתגורס.</p>',
   layout="title")

idea = Scene("idea", "הרעיון", [
    P("יש לנו וקטור $b$, וישר שנפרש על ידי וקטור $a$.", do=show("pj-a", "pj-line", "pj-b"),
      say="יש לנו וקטור בִּי, וישר שנפרש על ידי וקטור אֵיי."),
    P("ההיטל של $b$ על הישר הוא הנקודה על הישר שהכי קרובה ל-$b$.", do=show("pj-p"),
      say="ההיטל של בִּי על הישר הוא הנקודה על הישר שהכי קרובה לבִּי."),
    P("ההיטל הוא כפולה של $a$. המקדם הוא מספר אחד: המכפלה של $b$ ו-$a$, חלקי הנורמה של $a$ **בריבוע**.",
      do=show("i-f"), say="ההיטל הוא כפולה של אֵיי. המקדם הוא מספר אחד: המכפלה של בִּי ואֵיי, חלקי הנורמה של אֵיי בריבוע."),
    P("מה שנשאר, $c=b-p$, נקרא **השארית**.", do=show("pj-c"),
      say="מה שנשאר, סִי, שהוא בִּי פחות פִּי, נקרא השארית."),
    P("והשארית תמיד ניצבת לישר. זו הסיבה שזו הנקודה הכי קרובה.", do=show("pj-ra", "i-c1")),
    P("אז יש משולש ישר זווית, ומקבלים פיתגורס. והמרחק מ-$b$ לישר הוא האורך של $c$.", do=show("i-c2"), hold=0.4,
      say="אז יש משולש ישר זווית, ומקבלים פיתגורס. והמרחק מבִּי לישר הוא האורך של סִי."),
], stage='<div class="pg-stack">' + PIC + "</div>",
   panel=w.big("i-f", r"p=\frac{\langle b,a\rangle}{\|a\|^2}\,a")
         + st.card("i-c1", "rule", "🔑 $\\langle c,a\\rangle=0$")
         + st.card("i-c2", "rule", "🔑 $\\|b\\|^2=\\|p\\|^2+\\|c\\|^2$"))

ex = Scene("ex", "דוגמה", [
    P("בתמונה: $a=(2,1)$ ו-$b=(3,4)$.", do=show("e-0"),
      say="בתמונה: אֵיי הוא שתיים, אחת, ובִּי הוא שלוש, ארבע."),
    P("המכפלה של $b$ ו-$a$: שש ועוד ארבע, עשר. והנורמה של $a$ בריבוע: ארבע ועוד אחת, חמש.", do=show("e-1"),
      say="המכפלה של בִּי ואֵיי: שש ועוד ארבע, עשר. והנורמה של אֵיי בריבוע: ארבע ועוד אחת, חמש."),
    P("המקדם הוא עשר חלקי חמש, שתיים. אז ההיטל הוא פעמיים $a$: ארבע, שתיים.", do=show("e-2"),
      say="המקדם הוא עשר חלקי חמש, שתיים. אז ההיטל הוא פעמיים אֵיי: ארבע, שתיים."),
    P("השארית היא $b$ פחות ההיטל: מינוס אחת, שתיים.", do=show("e-3"),
      say="השארית היא בִּי פחות ההיטל: מינוס אחת, שתיים."),
    P("בדיקה: המכפלה של השארית עם $a$ היא מינוס שתיים ועוד שתיים. אפס. ניצבת.", do=show("e-4"),
      say="בדיקה: המכפלה של השארית עם אֵיי היא מינוס שתיים ועוד שתיים. אפס. ניצבת."),
    P("ופיתגורס: עשרים וחמש שווה עשרים ועוד חמש. והמרחק מ-$b$ לישר הוא שורש חמש.", do=show("e-5"), hold=0.4,
      say="ופיתגורס: עשרים וחמש שווה עשרים ועוד חמש. והמרחק מבִּי לישר הוא שורש חמש."),
], stage='<div class="pg-two">' + PIC.replace('id="pj', 'id="pk').replace('pj-', 'pk-').replace(' h"', '"')
         .replace('class="h"', '') + "</div>",
   panel=w.rows("e", [
       r"$a=(2,1),\ b=(3,4)$",
       r"$\langle b,a\rangle=10,\ \|a\|^2=5$",
       r"$p=\frac{10}{5}a=(4,2)$",
       r"$c=b-p=(-1,2)$",
       r"$\langle c,a\rangle=-2+2=0$",
       r"$25=20+5,\quad \|c\|=\sqrt5$"]))

trap = Scene("trap", "מלכודת", [
    P("הטעות הנפוצה: לחלק בנורמה של $a$, ולא בנורמה **בריבוע**.", do=show("t-0"),
      say="הטעות הנפוצה: לחלק בנורמה של אֵיי, ולא בנורמה בריבוע."),
    P("אז המקדם הוא עשר חלקי שורש חמש, שזה שתיים שורש חמש, בערך ארבע וחצי.", do=show("t-1"),
      say="אז המקדם הוא עשר חלקי שורש חמש, שזה שתיים שורש חמש, בערך ארבע וחצי."),
    P("ובתמונה רואים: הוקטור האדום ארוך מדי, הרבה מעבר לנקודה הנכונה.", do=show("pw-w")),
    P("והשארית כבר לא ניצבת: המכפלה שלה עם $a$ היא עשר פחות עשר שורש חמש, לא אפס.", do=show("t-2", "t-c"),
      say="והשארית כבר לא ניצבת: המכפלה שלה עם אֵיי היא עשר פחות עשר שורש חמש, לא אפס.", hold=0.4),
], stage='<div class="pg-stack">' + PIC2.replace('id="pw-a" class="h"', 'id="pw-a"')
         .replace('id="pw-b" class="h"', 'id="pw-b"').replace('id="pw-p" class="h"', 'id="pw-p"')
         .replace('id="pw-line" class="pg-line h"', 'id="pw-line" class="pg-line"') + "</div>",
   panel=w.rows("t", [
       r"$\frac{\langle b,a\rangle}{\|a\|}=\frac{10}{\sqrt5}=2\sqrt5$",
       r"$p'=2\sqrt5\,a$",
       r"$\langle b-p',a\rangle=10-10\sqrt5\ne0$"], "sm")
         + st.card("t-c", "trap", "⚠️ מחלקים ב-$\\|a\\|^2$, לא ב-$\\|a\\|$"))

matrix = Scene("matrix", "כמטריצה", [
    P("אם $a$ הוא וקטור יחידה, המכנה הוא אחת, וההיטל הוא פשוט המכפלה כפול $a$.", do=show("m-0"),
      say="אם אֵיי הוא וקטור יחידה, המכנה הוא אחת, וההיטל הוא פשוט המכפלה כפול אֵיי."),
    P("ובכתיב מטריצות: המכפלה היא $a^T b$, ולכן ההיטל הוא $a\\,a^Tb$. המטריצה $P=aa^T$ היא **מטריצת ההיטל**.",
      do=show("m-1"),
      say="ובכתיב מטריצות: המכפלה היא אֵיי טְרַנְסְפּוֹז בִּי, ולכן ההיטל הוא אֵיי אֵיי טְרַנְסְפּוֹז בִּי. "
          "המטריצה פִּי, אֵיי אֵיי טְרַנְסְפּוֹז, היא מטריצת ההיטל."),
    P("בדוגמה שלנו מנרמלים את $a$: מחלקים בשורש חמש.", do=show("m-2"),
      say="בדוגמה שלנו מנרמלים את אֵיי: מחלקים בשורש חמש."),
    P("מקבלים את המטריצה הזו. וכשכופלים אותה ב-$b$, יוצא בדיוק ארבע, שתיים. אותו היטל.", do=show("m-3", "m-4"),
      say="מקבלים את המטריצה הזו. וכשכופלים אותה בבִּי, יוצא בדיוק ארבע, שתיים. אותו היטל.", hold=0.4),
], stage='<div class="pg-stack">' + w.rows("m", [
    r"$\|a\|=1:\quad p=\langle b,a\rangle\,a$",
    r"$p=a\,(a^Tb)=(aa^T)\,b=Pb$",
    r"$q=\frac{1}{\sqrt5}(2,1)$",
    f"$P=qq^T=\\frac15{w.mat(5 * Pm)}$",
    f"$Pb=\\frac15{w.mat(5 * Pm)}{w.col(b)}=\\frac15{w.col(5 * Pm * b)}={w.col(p)}$"]) + "</div>",
   panel=st.card("m-c", "rule", "🔑 וקטור יחידה $q$: מטריצת ההיטל היא $P=qq^T$").replace(" h\"", "\""))

EX_STEM = ("יהי $\\vec v$ וקטור יחידה ב-$\\mathbb{R}^n$ ו-$P=\\vec v\\,\\vec v^T$. הוכיחו שלכל $\\vec u$ "
           "הוקטור $\\vec u-P\\vec u$ אורתוגונלי ל-$\\vec v$.")
exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $\\vec v$ וקטור יחידה ו-$P=\\vec v\\vec v^T$. צריך להוכיח ש-$\\vec u-P\\vec u$ ניצב ל-$\\vec v$.",
      say="שאלה ממבחן: וִי הוא וקטור יחידה, ופִּי שווה וִי כפול וִי טְרַנְסְפּוֹז. צריך להוכיח שיוּ פחות פִּי יוּ ניצב לוִי."),
    P("קודם נבין מה זה. $P\\vec u$ הוא בדיוק ההיטל של $\\vec u$ על $\\vec v$, ולכן $\\vec u-P\\vec u$ הוא השארית.",
      do=show("x-0", "x-c1"),
      say="קודם נבין מה זה. פִּי יוּ הוא בדיוק ההיטל של יוּ על וִי, ולכן יוּ פחות פִּי יוּ הוא השארית."),
    P("אז הטענה היא: השארית ניצבת. אבל צריך להוכיח, לא רק להבין. נחשב את המכפלה הפנימית.", do=show("x-1")),
    P("פותחים סוגריים, ומציבים את $P$.", do=show("x-2"), say="פותחים סוגריים, ומציבים את פִּי."),
    P("וכאן הנקודה: $\\vec v^T\\vec v$ הוא הנורמה בריבוע, והיא אחת, כי $\\vec v$ וקטור יחידה.", do=show("x-3", "x-c2"),
      say="וכאן הנקודה: וִי טְרַנְסְפּוֹז וִי הוא הנורמה בריבוע, והיא אחת, כי וִי וקטור יחידה."),
    P("נשאר אותו ביטוי פחות עצמו, וזה אפס. הוכחנו.", do=show("x-4"), hold=0.3),
    P("והמלכודת: בלי וקטור יחידה זה לא עובד. ניקח $\\vec v=(1,1)$ ו-$\\vec u=(1,0)$.", do=show("x-5"),
      say="והמלכודת: בלי וקטור יחידה זה לא עובד. ניקח את וִי, אחת אחת, ואת יוּ, אחת אפס."),
    P("השארית יוצאת $(0,-1)$, והמכפלה שלה עם $\\vec v$ היא מינוס אחת. לא ניצבת.", do=show("x-6", "x-c3"), hold=0.5,
      say="השארית יוצאת אפס, מינוס אחת, והמכפלה שלה עם וִי היא מינוס אחת. לא ניצבת."),
], stage='<div class="pg-stack">' + w.rows("x", [
    r"$P\vec u=\vec v\,(\vec v^T\vec u)=\langle\vec u,\vec v\rangle\,\vec v$",
    r"$\langle\vec u-P\vec u,\vec v\rangle=\vec v^T(\vec u-P\vec u)$",
    r"$=\vec v^T\vec u-(\vec v^T\vec v)\,\vec v^T\vec u$",
    r"$=\vec v^T\vec u-1\cdot\vec v^T\vec u$",
    r"$=0$",
    r"$\vec v=(1,1),\ \vec u=(1,0):\quad \vec u-P\vec u=(0,-1)$",
    r"$\langle(0,-1),(1,1)\rangle=-1\ne0$"], "sm") + "</div>",
   panel=w.stem("23B-B-Q5c", EX_STEM)
         + st.card("x-c1", "ex", "$P\\vec u$ = ההיטל, $\\vec u-P\\vec u$ = השארית")
         + st.card("x-c2", "rule", "🔑 $\\vec v^T\\vec v=\\|\\vec v\\|^2=1$")
         + st.card("x-c3", "trap", "⚠️ בלי $\\|\\vec v\\|=1$ הטענה נופלת"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: ההיטל על $a$ הוא המכפלה עם $a$, חלקי הנורמה **בריבוע**, כפול $a$.", do=show("c-1"),
      say="לסיכום: ההיטל על אֵיי הוא המכפלה עם אֵיי, חלקי הנורמה בריבוע, כפול אֵיי."),
    P("השארית ניצבת לישר, והמרחק לישר הוא האורך שלה.", do=show("c-2")),
    P("ופיתגורס קושר את שלושתם.", do=show("c-3")),
    P("ועבור וקטור יחידה $q$, מטריצת ההיטל היא $qq^T$. נתראה ברמה הבאה.", say="ועבור וקטור יחידה, מטריצת ההיטל היא הוקטור כפול הטְרַנְסְפּוֹז שלו. נתראה ברמה הבאה.", do=show("c-4"), hold=0.6),
], stage='<div class="pg-stack">' + w.big("c-0", r"p=\frac{\langle b,a\rangle}{\|a\|^2}\,a", hidden=False) + "</div>",
   panel=st.card("c-1", "trap", "⚠️ חלקי $\\|a\\|^2$")
         + st.card("c-2", "rule", "🔑 $c=b-p\\perp a$, המרחק $\\|c\\|$")
         + st.card("c-3", "rule", "🔑 $\\|b\\|^2=\\|p\\|^2+\\|c\\|^2$")
         + st.card("c-4", "rule", "🔑 $\\|q\\|=1$: $P=qq^T$"))

VIDEO = Video("P03", "proj_gs", "היטל על וקטור יחיד", [title, idea, ex, trap, matrix, exam, recap],
              bank={"23B-B-Q5c": None})
