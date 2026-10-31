# -*- coding: utf-8 -*-
"""G03 · חבורה או לא, ומה נכשל — video script (build: tools/video/vid.py G03).

Source: courses/groups_crt/C03.js (lesson + goal). Exam anchor: 26A-B-Q2c (is (R\\{1}, a⊙b = ab-a-b+2) a commutative
group?), solved through all four requirements; it leans on 26A-B-Q2a (associativity) and 26A-B-Q2b (neutral 2), which
the video also shows. No guided quiz uses any of them.
Avoided on purpose: the C03 quiz structures ((Z,·), the mod-4 / mod-8 options, a+2b) and its bank parts 24A-A-Q2b,
23A-A-Q4c, 24B-B-Q4d, plus the lesson table rows. Worked examples are new: (Q\\{0}, ÷) and ({0,1,2,3}, max).
"""
from fractions import Fraction as F
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

a, b, c, e, y = sp.symbols("a b c e y")

# ---------------------------------------------------------------- verified facts
div = lambda u, v: F(u) / F(v)
assert div(div(8, 4), 2) == 1 and div(8, div(4, 2)) == 4      # ÷ is not associative on Q\{0}
assert div(5, 1) == 5 and div(1, 5) != 5                        # 1 is neutral only from the right

E4 = [0, 1, 2, 3]
R4 = w.group_report(E4, max)
assert R4["closed"] and R4["assoc"] and R4["neutral"] == 0 and R4["comm"] and not R4["group"]
assert [k for k, v in R4["inverses"].items() if not v] == [1, 2, 3]   # only 0 has an inverse

# exam 26A-B-Q2c on M = R \ {1}
assert "ab-a-b+2" in BANK["26A-B-Q2c"]["question"] or "ab-a-b+2" in str(BANK["26A-B-Q2c"].get("solution", "")) \
    or "a\\odot b" in BANK["26A-B-Q2c"]["solution"]
od = lambda u, v: u * v - u - v + 2
assert sp.expand(od(a, b) - 1 - (a - 1) * (b - 1)) == 0                  # a⊙b - 1 = (a-1)(b-1)
assert sp.expand(od(od(a, b), c) - od(a, od(b, c))) == 0                 # associative
assert sp.expand(od(od(a, b), c) - 1 - (a - 1) * (b - 1) * (c - 1)) == 0
assert sp.solve(sp.Eq(od(a, e), a), e) == [2] and sp.expand(od(2, a) - a) == 0
inv = sp.solve(sp.Eq(od(a, y), 2), y)
assert len(inv) == 1 and sp.simplify(inv[0] - a / (a - 1)) == 0
assert sp.solve(sp.Eq(a / (a - 1), 1), a) == []                           # the inverse is never 1
assert sp.expand(od(a, b) - od(b, a)) == 0
for u in (F(3), F(-2), F(1, 2), F(7, 3)):
    v = u / (u - 1)
    assert v != 1 and od(u, v) == 2 and od(v, u) == 2

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("עכשיו מחברים את ארבע הדרישות."),
    P("נלמד להחליט אם מבנה הוא חבורה, ואם לא, לומר בדיוק מה נכשל."),
    P("ונבחין בין חבורה לבין חבורה אבלית.", hold=0.4),
], stage='<div class="kicker">G03 · חבורות ומשפט השאריות הסיני</div><h1>חבורה או לא, ומה נכשל</h1>'
         '<p>להחליט אם מבנה הוא חבורה, לנקוב בדרישה שנכשלת עם דוגמה נגדית, ולהבחין בין חבורה לחבורה אבלית.</p>',
   layout="title")

REQ = [("o-1", "1. סגירות"), ("o-2", "2. אסוציאטיביות"), ("o-3", "3. איבר ניטרלי"), ("o-4", "4. הופכי לכל איבר")]
order = Scene("order", "סדר הבדיקה", [
    P("בודקים את ארבע הדרישות לפי הסדר.", do=show("o-1", "o-2", "o-3", "o-4")),
    P("אם כולן מתקיימות, המבנה הוא חבורה."),
    P("אם אחת נכשלת, עוצרים. כותבים **איזו** דרישה נכשלת, ומביאים דוגמה נגדית אחת.", do=show("o-r")),
    P("וקומוטטיביות? היא לא אחת מהדרישות. היא תכונה נוספת.", do=show("o-c")),
    P("חבורה שהפעולה שלה קומוטטיבית נקראת חבורה אבלית.", hold=0.3),
], stage='<div class="gc-stack">' + "".join(st.card(i, "ex", t) for i, t in REQ) + '</div>',
   panel=st.card("o-r", "rule", "🔑 נכשלה דרישה: שם הדרישה + דוגמה נגדית")
         + st.card("o-c", "plain", "קומוטטיבית: $a*b=b*a$. חבורה כזו נקראת <b>אבלית</b>"))

dv = Scene("div", "דוגמה: חילוק", [
    P("המבנה הראשון: הרציונליים בלי אפס, עם חילוק.", do=show("d-op")),
    P("סגירות: מנה של שני רציונליים שונים מאפס היא רציונלי שונה מאפס. עוברת.", do=show("d-0")),
    P("אסוציאטיביות: בסוגריים שמונה חלקי ארבע, ואז חלקי שתיים, זה אחת.", do=show("d-1")),
    P("אבל שמונה חלקי, בסוגריים, ארבע חלקי שתיים, זה שמונה חלקי שתיים, שזה ארבע.", do=show("d-2")),
    P("אחת שונה מארבע. אסוציאטיביות נכשלת, ולכן זו **לא** חבורה.", do=show("d-v")),
    P("זו כל התשובה: הדרישה שנכשלה, ודוגמה נגדית אחת. לא צריך להמשיך לבדוק.", hold=0.3),
], stage='<div class="gc-stack"><div id="d-op" class="gc-mid h">$(\\mathbb{Q}\\setminus\\{0\\},\\ \\div)$</div>'
         + w.lines("d", ["$a\\div b\\in\\mathbb{Q}\\setminus\\{0\\}\\ \\ \\checkmark$", "$(8\\div4)\\div2=2\\div2=1$",
                         "$8\\div(4\\div2)=8\\div2=4$"], size=42) + '</div>',
   panel=st.card("d-v", "trap", "⚠️ נכשלה <b>אסוציאטיביות</b>: $1\\ne4$. לא חבורה"))

mx = Scene("max", "דוגמה: מקסימום", [
    P("המבנה השני: אפס עד שלוש, והפעולה היא המקסימום.", do=show("m-tab")),
    P("כל התוצאות בטבלה הן בין אפס לשלוש, ולכן יש סגירות. ומקסימום הוא אסוציאטיבי.", do=show("m-1")),
    P("השורה של אפס זהה לכותרת. אפס הוא הניטרלי.", do=show("mt-row-0", "m-2")),
    P("עכשיו הופכי לשתיים: צריך איבר שהמקסימום שלו עם שתיים יוצא אפס.", do=hide("mt-row-0") + show("mt-row-2")),
    P("בשורה של שתיים אין אפס בכלל. לשתיים אין הופכי, ולכן זו לא חבורה.", do=show("m-3")),
    P("שימו לב: הטבלה סימטרית, כלומר הפעולה קומוטטיבית. ובכל זאת אין חבורה.", do=show("m-t")),
], stage=f'<div class="gc-stack"><div id="m-tab" class="gc-stack h">{w.cayley("mt", E4, max, sym="\\max", size=38)}'
         '</div></div>',
   panel=st.card("m-1", "ex", "סגירות ✓ &nbsp; אסוציאטיביות ✓")
         + st.card("m-2", "ex", "ניטרלי: $0$ ✓")
         + st.card("m-3", "trap", "⚠️ אין $x$ עם $\\max(2,x)=0$: נכשל <b>ההופכי</b>")
         + st.card("m-t", "trap", "⚠️ קומוטטיבית ועדיין לא חבורה"))

A1 = sp.Matrix([[1, 1], [0, 1]])
B1 = sp.Matrix([[1, 0], [1, 1]])
assert A1 * B1 == sp.Matrix([[2, 1], [1, 1]]) and B1 * A1 == sp.Matrix([[1, 1], [1, 2]]) and A1.det() == B1.det() == 1
ab = Scene("abel", "חבורה לא אבלית", [
    P("ולהפך: יש חבורות שאינן קומוטטיביות.", do=show("b-0")),
    P("המטריצות ההפיכות מסדר שתיים על שתיים, עם כפל מטריצות, הן חבורה. הניטרלי הוא מטריצת היחידה."),
    P("אבל כאן, $A$ כפול $B$ שונה מ-$B$ כפול $A$.", do=show("b-1", "b-2"),
      say="אבל כאן, אֵיי כפול בִּי שונה מבִּי כפול אֵיי."),
    P("לכן זו חבורה, אבל לא חבורה אבלית. זה לא סותר שום דרישה.", do=show("b-c"), hold=0.3),
], stage='<div class="gc-stack"><div id="b-0" class="gc-mid h">$A=' + w.pm(((1, 1), (0, 1))) + r',\quad '
         'B=' + w.pm(((1, 0), (1, 1))) + '$</div>'
         + w.lines("b", ["$AB=" + w.pm(((2, 1), (1, 1))) + "$", "$BA=" + w.pm(((1, 1), (1, 2))) + "$"],
                   size=40, start=1) + '</div>',
   panel=st.card("b-c", "rule", r"🔑 $AB\ne BA$: חבורה, אבל לא אבלית"))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: הממשיים בלי אחת, עם הפעולה $ab-a-b+2$. האם זו חבורה קומוטטיבית?", do=show("x-op"),
      say="שאלה ממבחן: הממשיים בלי אחת, עם הפעולה אֵיי בִּי, פחות אֵיי, פחות בִּי, ועוד שתיים. האם זו חבורה קומוטטיבית?"),
    P("טריק שחוסך עבודה: הפעולה פחות אחת היא המכפלה של $a-1$ ו-$b-1$.", do=show("x-0"),
      say="טריק שחוסך עבודה: הפעולה פחות אחת היא המכפלה של: בסוגריים אֵיי פחות אחת, כפול בסוגריים בִּי פחות אחת."),
    P("סגירות: התוצאה שווה אחת רק אם אחד הגורמים אפס, כלומר $a=1$ או $b=1$. אבל שניהם שונים מאחת.",
      do=show("x-1", "x-c1"),
      say="סגירות: התוצאה שווה אחת רק אם אחד הגורמים אפס, כלומר אֵיי שווה אחת או בִּי שווה אחת. אבל שניהם שונים מאחת."),
    P("אסוציאטיביות: הוכחה בסעיף הראשון. ובזכות הטריק, שני האגפים פחות אחת שווים לאותה מכפלה.",
      do=show("x-2", "x-c2")),
    P("ניטרלי: מסעיף שני, $e=2$. הוא שייך, כי שתיים שונה מאחת.", do=show("x-3", "x-c3"),
      say="ניטרלי: מסעיף שני, אִי שווה שתיים. הוא שייך, כי שתיים שונה מאחת."),
    P("הופכי: פותרים $a\\odot y=2$, ומקבלים $y$ שווה $a$ חלקי $a-1$.", do=show("x-4"),
      say="הופכי: פותרים אֵיי עיגול וַואי שווה שתיים, ומקבלים וַואי שווה אֵיי חלקי, בסוגריים, אֵיי פחות אחת."),
    P("ומוודאים שהוא בקבוצה: אם הוא היה שווה אחת, היינו מקבלים $a=a-1$. סתירה.", do=show("x-c4"),
      say="ומוודאים שהוא בקבוצה: אם הוא היה שווה אחת, היינו מקבלים אֵיי שווה אֵיי פחות אחת. סתירה."),
    P("ולבסוף קומוטטיביות: הביטוי סימטרי ב-$a$ וב-$b$.", do=show("x-c5"),
      say="ולבסוף קומוטטיביות: הביטוי סימטרי באֵיי ובבִּי."),
    P("התשובה: כן, חבורה קומוטטיבית.", do=show("x-ans")),
    P("והמלכודת: שוכחים לבדוק שהתוצאה וההופכי אינם אחת. בלי זה ההוכחה חסרה.", do=show("x-t"), hold=0.5),
], stage='<div class="gc-stack"><div id="x-op" class="gc-mid h">$a\\odot b=ab-a-b+2$</div>'
         + w.lines("x", ["$a\\odot b-1=(a-1)(b-1)$", "$(a-1)(b-1)\\ne0\\ \\Rightarrow\\ a\\odot b\\ne1$",
                         "$(a\\odot b)\\odot c-1=(a-1)(b-1)(c-1)$", "$a\\odot2=(a-1)\\cdot1+1=a$",
                         "$(a-1)(y-1)=1\\ \\Rightarrow\\ y=\\frac{a}{a-1}$"], size=38)
         + '</div>',
   panel=w.ctx_stem("26A-B-Q2c", "$M=\\{x\\in\\mathbb{R}:x\\ne1\\}$, &nbsp;$a\\odot b=ab-a-b+2$.",
                    "האם המבנה $(M,\\odot)$ הוא חבורה קומוטטיבית?")
         + '<div class="gc-lines" style="font-size:31px;direction:rtl;align-items:flex-start">'
         + "".join(f'<div id="{i}" class="h">{t}</div>' for i, t in [
             ("x-c1", "1. סגירות ✓"), ("x-c2", "2. אסוציאטיביות ✓"), ("x-c3", "3. ניטרלי $e=2$ ✓"),
             ("x-c4", "4. הופכי $\\frac{a}{a-1}\\ne1$ ✓"), ("x-c5", "וגם קומוטטיבית ✓")])
         + '</div>'
         + w.chip("x-ans", "חבורה קומוטטיבית", 0)
         + st.card("x-t", "trap", "⚠️ לבדוק: התוצאה וההופכי שונים מ-$1$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: ארבע דרישות, לפי הסדר.", do=show("r-1")),
    P("דרישה שנכשלת: שם הדרישה ודוגמה נגדית אחת, וזו התשובה.", do=show("r-2")),
    P("קומוטטיביות היא לא דרישה. היא מה שהופך חבורה לחבורה אבלית.", do=show("r-3")),
    P("ובקבוצה עם ערך אסור, כמו אחת, בודקים שהתוצאה וההופכי לא נופלים עליו. נתראה ברמה הבאה.", do=show("r-4"),
      hold=0.6),
], stage='<div class="gc-stack">' + "".join(st.card("r" + i, "ex", t).replace(" h\"", "\"") for i, t in REQ) + '</div>',
   panel=st.card("r-1", "rule", "🔑 סגירות, אסוציאטיביות, ניטרלי, הופכי")
         + st.card("r-2", "rule", "🔑 נכשל: דרישה + דוגמה נגדית")
         + st.card("r-3", "plain", "קומוטטיבית = אבלית, לא דרישה")
         + st.card("r-4", "trap", "⚠️ ערך אסור: לבדוק תוצאה והופכי"))

VIDEO = Video("G03", "groups_crt", "חבורה או לא, ומה נכשל", [title, order, dv, mx, ab, ex, recap],
              bank={"26A-B-Q2a": None, "26A-B-Q2b": None, "26A-B-Q2c": None})
