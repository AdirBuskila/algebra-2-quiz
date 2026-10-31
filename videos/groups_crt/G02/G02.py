# -*- coding: utf-8 -*-
"""G02 · איבר ניטרלי והופכי — video script (build: tools/video/vid.py G02).

Source: courses/groups_crt/C02.js (lesson + goal). Exam anchors: 25A-A-Q2c (the neutral element of
(a,b)*(c,d) = (a+c+1, bd/3) on A = {(x,y) : y != 0}) and 25A-A-Q2d (inverses, so (A,*) is a group); no guided quiz uses
them. Avoided on purpose: the C02 quiz/lesson operations (a+b-3, a+b+1, a+b-ab, a+b+ab), 23A-A-Q4b / 24A-A-Q4b-twins
(the (ay+bx, by) operation of the C02 and C03 quizzes), 24A-B-Q2c, and 24B-B-Q4 ((2xu, y+v): its first component
2ab is the C01 / C03 quiz parts 24B-B-Q4b/d). Worked examples are new: the table of
{1,2,3,4} under multiplication mod 5, ab/3 on the nonzero rationals, 3ab on the nonzero integers, a^2+b and a+3b.
"""
from fractions import Fraction as F
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

a, b, e, x = sp.symbols("a b e x")

# ---------------------------------------------------------------- verified facts
Z5 = [1, 2, 3, 4]
m5 = lambda u, v: (u * v) % 5
R5 = w.group_report(Z5, m5)
assert R5["group"] and R5["neutral"] == 1
assert {k: v[0] for k, v in R5["inverses"].items()} == {1: 1, 2: 3, 3: 2, 4: 4}

# ab/3 on Q\{0}: e = 3, inverse 9/a; 3ab on Z\{0}: the equation gives e = 1/3, not an integer
assert sp.solve(sp.Eq(a * e / 3, a), e) == [3]
assert sp.solve(sp.Eq(a * x / 3, 3), x) == [9 / a]
assert all(q * 3 / 3 == q and q * (F(9) / q) / 3 == 3 for q in (F(3), F(-2, 7), F(5, 3)))
assert sp.solve(sp.Eq(3 * a * e, a), e) == [sp.Rational(1, 3)]

# a^2 + b: e would depend on a; a + 3b: e = 0 from the right only
assert [sp.expand(r) for r in sp.solve(sp.Eq(a**2 + e, a), e)] == [a - a**2]
assert sp.solve(sp.Eq(a + 3 * e, a), e) == [0] and (lambda u: 0 + 3 * u)(2) == 6 != 2

# exam 25A-A-Q2c / Q2d
assert "bd" in BANK["25A-A-Q2c"]["solution"] or "e_2b" in BANK["25A-A-Q2c"]["solution"]
op = lambda p, q: (p[0] + q[0] + 1, F(p[1]) * F(q[1]) / 3)
E = (-1, F(3))
samples = [(0, F(1)), (5, F(-2)), (F(-7, 2), F(9, 4)), (3, F(1, 3))]
for s in samples:
    assert op(E, s) == (s[0], s[1]) and op(s, E) == (s[0], s[1])
    inv = (-2 - s[0], F(9) / F(s[1]))
    assert inv[1] != 0 and op(s, inv) == E and op(inv, s) == E
assert op((0, F(1)), (0, F(1))) != (0, F(1))           # (0,1) is not neutral (the guess the pitfall warns about)
e1, e2 = sp.symbols("e1 e2")
assert sp.solve([sp.Eq(a + e1 + 1, a), sp.Eq(b * e2 / 3, b)], [e1, e2], dict=True) == [{e1: -1, e2: 3}]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הקודם בדקנו סגירות ואסוציאטיביות."),
    P("עכשיו שתי הדרישות הבאות: איבר ניטרלי, והופכי לכל איבר."),
    P("נלמד איך מוצאים אותם, ואיך מזהים שהם לא קיימים.", hold=0.4),
], stage='<div class="kicker">G02 · חבורות ומשפט השאריות הסיני</div><h1>איבר ניטרלי והופכי</h1>'
         '<p>למצוא איבר ניטרלי והופכי לפעולה מומצאת, ולזהות כשאחד מהם לא קיים.</p>', layout="title")

table = Scene("table", "בטבלה", [
    P("איבר ניטרלי $e$ הוא איבר שלא משנה אף אחד: $a*e=e*a=a$ לכל $a$.", do=show("t-def"),
      say="איבר ניטרלי, אִי, הוא איבר שלא משנה אף אחד: אֵיי כוכבית אִי, שווה אִי כוכבית אֵיי, שווה אֵיי, לכל אֵיי."),
    P("נסתכל בטבלה של אחת עד ארבע, עם כפל מודולו חמש.", do=show("t-tab")),
    P("השורה של אחת זהה לשורת הכותרת, וגם העמודה שלה. לכן אחת היא הניטרלי.", do=show("tz-row-0", "tz-col-0")),
    P("ההופכי של $a$ הוא איבר שמחזיר אותנו לניטרלי: $a*x=x*a=e$.", do=hide("tz-row-0", "tz-col-0") + show("t-inv"),
      say="ההופכי של אֵיי הוא איבר שמחזיר אותנו לניטרלי: אֵיי כוכבית אִקְס שווה אִי, משני הצדדים."),
    P("בטבלה מחפשים בכל שורה איפה מופיע אחת.", do=show("tz-c-0-0", "tz-c-1-2", "tz-c-2-1", "tz-c-3-3")),
    P("שתיים ושלוש הופכיים זה לזה, כי שתיים כפול שלוש זה שש, ושש זה אחת מודולו חמש.", do=show("t-ex")),
    P("וארבע הופכי לעצמו: ארבע כפול ארבע זה שש עשרה, שזה אחת.", hold=0.3),
    P("בכל שורה יש אחת, ולכן לכל איבר יש הופכי.", do=show("t-r")),
], stage=f'<div class="gc-stack"><div id="t-tab" class="gc-stack h">{w.cayley("tz", Z5, m5, sym="\\cdot", size=38)}'
         '<div class="gc-note">כפל מודולו 5</div></div></div>',
   panel=st.card("t-def", "rule", "🔑 ניטרלי: $a*e=e*a=a$")
         + st.card("t-inv", "rule", "🔑 הופכי: $a*x=x*a=e$")
         + st.card("t-ex", "ex", "$2\\cdot3=6\\equiv1,\\quad 4\\cdot4=16\\equiv1$")
         + st.card("t-r", "plain", "בכל שורה יש $1$: לכל איבר יש הופכי ✓"))

alg = Scene("alg", "בלי טבלה", [
    P("בקבוצה אינסופית אין טבלה. לכן פותרים משוואה.", do=show("g-op")),
    P("ניקח את הרציונליים בלי אפס, עם הפעולה $ab$ חלקי שלוש.",
      say="ניקח את הרציונליים בלי אפס, עם הפעולה: אֵיי בִּי חלקי שלוש."),
    P("כותבים $a*e=a$, כלומר $a$ כפול $e$ חלקי שלוש שווה $a$. מחלקים ב-$a$, ומקבלים שלוש.", do=show("g-0"),
      say="כותבים אֵיי כוכבית אִי שווה אֵיי, כלומר אֵיי כפול אִי חלקי שלוש שווה אֵיי. מחלקים באֵיי, ומקבלים שלוש."),
    P("ובודקים שלושה דברים: שלוש לא תלוי ב-$a$, הוא רציונלי שונה מאפס, והפעולה קומוטטיבית.", do=show("g-c1"),
      say="ובודקים שלושה דברים: שלוש לא תלוי באֵיי, הוא רציונלי שונה מאפס, והפעולה קומוטטיבית."),
    P("עכשיו ההופכי: פותרים $a*x=3$, ומקבלים תשע חלקי $a$.", do=show("g-1"),
      say="עכשיו ההופכי: פותרים אֵיי כוכבית אִקְס שווה שלוש, ומקבלים תשע חלקי אֵיי."),
    P("גם הוא רציונלי ושונה מאפס. לכן לכל איבר יש הופכי.", do=show("g-c2"), hold=0.3),
    P("ועכשיו פעולה דומה, $3ab$, על השלמים בלי אפס.", do=show("g-z"),
      say="ועכשיו פעולה דומה, שלוש אֵיי בִּי, על השלמים בלי אפס."),
    P("המשוואה נותנת שליש. אבל שליש **אינו** שלם, ולכן כאן אין איבר ניטרלי בכלל.", do=show("g-2", "g-t")),
], stage='<div class="gc-stack"><div id="g-op" class="gc-mid h">$a*b=\\frac{ab}3$</div>'
         + w.lines("g", ["$\\frac{ae}3=a\\ \\Rightarrow\\ e=3$", "$\\frac{ax}3=3\\ \\Rightarrow\\ x=\\frac9a$",
                         "$3ae=a\\ \\Rightarrow\\ e=\\frac13$"], size=46)
         + '</div>',
   panel=st.card("g-c1", "ex", "על $\\mathbb{Q}\\setminus\\{0\\}$: $e=3$ קבוע ושייך ✓")
         + st.card("g-c2", "ex", "$\\frac9a\\in\\mathbb{Q}\\setminus\\{0\\}$ ✓ &nbsp;לכל איבר יש הופכי")
         + st.card("g-z", "plain", "$a*b=3ab$ על $\\mathbb{Z}\\setminus\\{0\\}$:")
         + st.card("g-t", "trap", "⚠️ $\\frac13\\notin\\mathbb{Z}$: אין ניטרלי"))

nope = Scene("nope", "מתי אין ניטרלי", [
    P("עוד שתי דרכים שבהן ניטרלי נכשל.", do=show("n-0")),
    P("הפעולה $a^2+b$ על הממשיים. מהמשוואה $a*e=a$ יוצא ש-$e$ שווה $a$ פחות $a$ בריבוע.", do=show("n-1"),
      say="הפעולה אֵיי בריבוע ועוד בִּי, על הממשיים. מהמשוואה אֵיי כוכבית אִי שווה אֵיי, יוצא שאִי שווה אֵיי פחות אֵיי בריבוע."),
    P("זה תלוי ב-$a$: לכל איבר יוצא מועמד אחר. ניטרלי חייב להיות אחד לכולם, ולכן אין.",
      say="זה תלוי באֵיי: לכל איבר יוצא מועמד אחר. ניטרלי חייב להיות אחד לכולם, ולכן אין.", do=show("n-c1"), hold=0.3),
    P("והפעולה $a+3b$ על השלמים. מימין, $a*0=a$, ולכן אפס נראה כמו ניטרלי.", do=show("n-2", "n-3"),
      say="והפעולה אֵיי ועוד שלוש בִּי, על השלמים. מימין, אֵיי כוכבית אפס שווה אֵיי, ולכן אפס נראה כמו ניטרלי."),
    P("והמשוואה מימין נותנת רק אפס, אז אין מועמד אחר. אבל משמאל, אפס כוכבית שתיים זה שש, ולא שתיים.", do=show("n-4")),
    P("הפעולה לא קומוטטיבית, ולכן חייבים לבדוק את שני הצדדים. גם כאן אין ניטרלי.", do=show("n-c2")),
], stage='<div class="gc-stack">'
         + w.lines("n", ["$a*b=a^2+b$", "$a^2+e=a\\ \\Rightarrow\\ e=a-a^2$", "$a*b=a+3b$",
                         "$a*0=a+0=a\\ \\ \\checkmark$", "$0*2=0+6=6\\ne2\\ \\ \\times$"], size=44, shown=())
         + '</div>',
   panel=st.card("n-c1", "trap", "⚠️ $e$ שתלוי ב-$a$: אין ניטרלי")
         + st.card("n-c2", "trap", "⚠️ לא קומוטטיבית: בודקים $a*e$ <b>וגם</b> $e*a$"))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן. הקבוצה: זוגות של ממשיים שהרכיב השני שלהם שונה מאפס.", do=show("x-op")),
    P("והפעולה: ברכיב הראשון $a+c+1$, וברכיב השני $bd$ חלקי שלוש.",
      say="והפעולה: ברכיב הראשון אֵיי ועוד סִי ועוד אחת, וברכיב השני בִּי דִּי חלקי שלוש."),
    P("האם יש ניטרלי? מחפשים זוג $e_1, e_2$, ופותרים כל רכיב לחוד.", do=show("x-0"),
      say="האם יש ניטרלי? מחפשים זוג, אִי אחת ואִי שתיים, ופותרים כל רכיב לחוד."),
    P("ברכיב הראשון: $a+e_1+1=a$, ולכן $e_1={-1}$.", do=show("x-1"),
      say="ברכיב הראשון: אֵיי ועוד אִי אחת ועוד אחת שווה אֵיי, ולכן אִי אחת שווה מינוס אחת."),
    P("ברכיב השני: $b$ כפול $e_2$ חלקי שלוש שווה $b$. מותר לחלק ב-$b$ כי הוא שונה מאפס, ולכן $e_2=3$.",
      do=show("x-2"),
      say="ברכיב השני: בִּי כפול אִי שתיים חלקי שלוש שווה בִּי. מותר לחלק בבִּי כי הוא שונה מאפס, ולכן אִי שתיים שווה שלוש."),
    P("הניטרלי הוא מינוס אחת ושלוש. הוא קבוע, הרכיב השני שלו שונה מאפס, והפעולה קומוטטיבית.", do=show("x-3", "x-c1")),
    P("המלכודת: לנחש אפס ואחת מתוך הרגל. בפעולה הזו הזוג אפס ואחת לא משאיר אף זוג במקום.", do=show("x-t1")),
    P("הסעיף הבא: האם זו חבורה? סגירות ואסוציאטיביות כבר הוכחו בסעיפים הקודמים. נשאר ההופכי.", do=show("x-4")),
    P("ההופכי צריך להחזיר את הניטרלי, מינוס אחת ושלוש. ולא אפס ואחת.", do=show("x-t2")),
    P("ברכיב הראשון יוצא מינוס שתיים פחות $a$. ברכיב השני תשע חלקי $b$.", do=show("x-5"),
      say="ברכיב הראשון יוצא מינוס שתיים פחות אֵיי. ברכיב השני, תשע חלקי בִּי."),
    P("תשע חלקי $b$ אף פעם לא אפס, ולכן ההופכי שייך לקבוצה. כן, זו חבורה.", do=show("x-ans"),
      say="תשע חלקי בִּי אף פעם לא אפס, ולכן ההופכי שייך לקבוצה. כן, זו חבורה.", hold=0.5),
], stage='<div class="gc-stack"><div id="x-op" class="gc-mid h">$(a,b)*(c,d)=\\left(a+c+1,\\ \\frac{bd}3\\right)$</div>'
         + w.lines("x", ["$(a,b)*(e_1,e_2)=(a,b)$", "$a+e_1+1=a\\ \\Rightarrow\\ e_1={-1}$",
                         "$\\frac{b\\,e_2}3=b,\\ b\\ne0\\ \\Rightarrow\\ e_2=3$", "$e=({-1},3)$",
                         "$(a,b)*(x,y)=({-1},3)$", "$x={-2}-a,\\quad y=\\frac9b\\ne0$"], size=38)
         + '</div>',
   panel=w.ctx_stem("25A-A-Q2c/d", "$A=\\{(x,y)\\mid x,y\\in\\mathbb{R},\\ y\\ne0\\}$ עם הפעולה שמשמאל.",
                    "<div>ג. האם ב-$A$ קיים איבר ניטרלי?</div><div>ד. האם $(A,*)$ חבורה?</div>")
         + st.card("x-c1", "ex", "$e=({-1},3)\\in A$ ✓")
         + st.card("x-t1", "trap", "⚠️ $(0,1)$ אינו ניטרלי כאן")
         + st.card("x-t2", "trap", "⚠️ ההופכי מחזיר את $({-1},3)$")
         + w.chip("x-ans", "$(a,b)^{-1}=\\left({-2}-a,\\ \\frac9b\\right)$: חבורה", 0))

recap = Scene("recap", "סיכום", [
    P("לסיכום: מוצאים ניטרלי בפתרון $a*e=a$.", do=show("r-1"),
      say="לסיכום: מוצאים ניטרלי בפתרון אֵיי כוכבית אִי שווה אֵיי."),
    P("ובודקים שהוא קבוע, ששייך לקבוצה, ושעובד משני הצדדים.", do=show("r-2")),
    P("רק אחרי שיש ניטרלי מחפשים הופכי, ופותרים $a*x=e$.", do=show("r-3"),
      say="רק אחרי שיש ניטרלי מחפשים הופכי, ופותרים אֵיי כוכבית אִקְס שווה אִי."),
    P("וגם ההופכי חייב להיות בקבוצה. בשלב הבא נחבר את ארבע הדרישות. נתראה שם.", do=show("r-4"), hold=0.6),
], stage='<div class="gc-stack"><div class="gc-big">$a*e=e*a=a$</div><div class="gc-big">$a*x=x*a=e$</div></div>',
   panel=st.card("r-1", "rule", "🔑 פותרים $a*e=a$")
         + st.card("r-2", "rule", "🔑 קבוע, שייך, משני הצדדים")
         + st.card("r-3", "rule", "🔑 קודם ניטרלי, אחר כך הופכי")
         + st.card("r-4", "trap", "⚠️ ההופכי חייב להיות בקבוצה"))

VIDEO = Video("G02", "groups_crt", "איבר ניטרלי והופכי", [title, table, alg, nope, ex, recap],
              bank={"25A-A-Q2c": None, "25A-A-Q2d": None})
