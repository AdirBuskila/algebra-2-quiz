# -*- coding: utf-8 -*-
"""G04 · סדר חבורה וסדר איבר — video script (build: tools/video/vid.py G04).

Source: courses/groups_crt/C04.js (lesson + goal). Exam anchors: 25B-B-Q2b (|H| for 2x2 matrices over Z_5 with nonzero
entries under the entrywise product) and 25B-B-Q2c (the order of (1 2; 2 3) there); no guided quiz uses them.
Avoided on purpose: the C04 quiz items (|Z_9^*|, o(5) in Z_11^*, (3,2) in Z_7^* x Z_5^*, Lagrange with |G| = 24) and
their bank parts 23B-B-Q2c/d, the lesson pair (2,4) in Z_5^* x Z_7^*, and the twins 25A-C-Q2c/d.
Worked examples are new: Z_10^* and the powers of 3 there, and (5,2) in Z_13^* x Z_5^*.
"""
from itertools import product
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

# ---------------------------------------------------------------- verified facts
U10 = w.zstar(10)
assert U10 == [1, 3, 7, 9]
P3 = w.powers_mod(3, 10)
assert P3 == [3, 9, 7, 1] and w.order_mod(3, 10) == 4
assert {u: w.order_mod(u, 10) for u in U10} == {1: 1, 3: 4, 7: 4, 9: 2}
assert all(len(U10) % w.order_mod(u, 10) == 0 for u in U10)

P5 = w.powers_mod(5, 13)
P2 = w.powers_mod(2, 5)
assert P5 == [5, 12, 8, 1] and P2 == [2, 4, 3, 1]
pair_pows = [((5 ** k) % 13, (2 ** k) % 5) for k in range(1, 5)]
assert pair_pows == [(5, 2), (12, 4), (8, 3), (1, 1)]
o_pair = next(k for k in range(1, 100) if pow(5, k, 13) == 1 and pow(2, k, 5) == 1)
assert o_pair == 4 == w.lcm(4, 4) and len(w.zstar(13)) * len(w.zstar(5)) == 48 and 48 % 4 == 0

# exam 25B-B-Q2b/c: H = 2x2 over Z_5 with all entries nonzero, entrywise product mod 5
assert "4^4=256" in BANK["25B-B-Q2b"]["solution"].replace(" ", "")
Hset = list(product(range(1, 5), repeat=4))
assert len(Hset) == 256
had = lambda X, Y: tuple((x * y) % 5 for x, y in zip(X, Y))
ONE = (1, 1, 1, 1)
assert all(had(ONE, X) == X for X in Hset)                       # the neutral is the all-ones matrix, not I
assert had((1, 0, 0, 1), (1, 2, 2, 3)) != (1, 2, 2, 3)           # I is not even in H (0 entries) and not neutral
X = (1, 2, 2, 3)
pw = [X]
while pw[-1] != ONE:
    pw.append(had(pw[-1], X))
assert pw == [(1, 2, 2, 3), (1, 4, 4, 4), (1, 3, 3, 2), (1, 1, 1, 1)]
assert len(pw) == 4 == w.lcm(*(w.order_mod(v, 5) for v in X)) and 256 % 4 == 0
pmx = lambda t: w.pm(((t[0], t[1]), (t[2], t[3])))

CYC3 = w.cycle("c3", [str(v) for v in P3], [("3", str(k)) for k in range(1, 5)], r=150, node=44)
CYC5 = w.cycle("c5", [str(v) for v in P5], [("5", str(k)) for k in range(1, 5)], r=120, node=40, font=30)
CYC2 = w.cycle("c2", [str(v) for v in P2], [("2", str(k)) for k in range(1, 5)], r=120, node=40, font=30)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נספור: כמה איברים יש בחבורה, ואחרי כמה צעדים איבר חוזר לניטרלי."),
    P("נראה את משפט לגרנז', ומה קורה בזוגות."),
    P("ובסוף נפתור שני סעיפים ממבחן.", hold=0.4),
], stage='<div class="kicker">G04 · חבורות ומשפט השאריות הסיני</div><h1>סדר חבורה וסדר איבר</h1>'
         '<p>לחשב את הסדר של חבורה סופית ושל איבר בה, כולל במכפלה ישרה, ולהשתמש במשפט לגרנז\'.</p>', layout="title")

grp = Scene("group", "סדר החבורה", [
    P("הסדר של חבורה הוא פשוט מספר האיברים שבה.", do=show("g-def")),
    P("למשל $\\mathbb{Z}_{10}^*$: המספרים מאחת עד תשע שזרים לעשר, עם כפל מודולו עשר.", do=show("g-0"),
      say="למשל זֶד עשר כוכבית: המספרים מאחת עד תשע שזרים לעשר, עם כפל מודולו עשר."),
    P("אלה אחת, שלוש, שבע ותשע. לכן הסדר של החבורה הוא ארבע.", do=show("g-1")),
    P("הזוגיים וחמש נפסלים, כי יש להם מחלק משותף עם עשר.", hold=0.3),
], stage='<div class="gc-stack">' + w.lines("g", ["$\\mathbb{Z}_{10}^*=\\{1,3,7,9\\}$", "$|\\mathbb{Z}_{10}^*|=4$"], size=50)
         + '</div>',
   panel=st.card("g-def", "rule", "🔑 $|G|$ = מספר האיברים"))

elt = Scene("elt", "סדר איבר", [
    P("הסדר של **איבר** הוא משהו אחר: החזקה החיובית הקטנה ביותר שמחזירה אותו לניטרלי.", do=show("e-def")),
    P("נעלה את שלוש בחזקות, מודולו עשר. שלוש בחזקת אחת זה שלוש.", do=show("c3-n-0")),
    P("בריבוע: תשע.", do=show("c3-a-0", "c3-n-1")),
    P("בשלישית: עשרים ושבע, כלומר שבע.", do=show("c3-a-1", "c3-n-2")),
    P("וברביעית: שבע כפול שלוש, עשרים ואחת, כלומר אחת. חזרנו לניטרלי.", do=show("c3-a-2", "c3-n-3")),
    P("מכאן החזקות רק חוזרות במעגל. לכן הסדר של שלוש הוא ארבע.", do=show("c3-a-3", "e-1")),
    P("ולתשע: תשע בריבוע זה שמונים ואחת, כלומר אחת. הסדר שלו שתיים.", do=show("e-2"), hold=0.3),
    P("משפט לגרנז': בחבורה סופית, הסדר של כל איבר מחלק את סדר החבורה.", do=show("e-l")),
    P("וזה מתאים: ארבע ושתיים מחלקים את ארבע. סדר שלוש, למשל, לא יכול להופיע כאן.", do=show("e-3")),
], stage=f'<div class="gc-stack">{CYC3}</div>',
   panel=st.card("e-def", "rule", "🔑 $o(x)$: הקטן ביותר עם $x^n=e$")
         + st.card("e-1", "ex", "$o(3)=4$ ב-$\\mathbb{Z}_{10}^*$")
         + st.card("e-2", "ex", "$9^2=81\\equiv1$, &nbsp;$o(9)=2$")
         + st.card("e-l", "rule", "🔑 לגרנז': $o(x)\\mid|G|$")
         + st.card("e-3", "plain", "$o(x)\\in\\{1,2,4\\}$ כאן"))

pair = Scene("pair", "מכפלה ישרה", [
    P("מכפלה ישרה: זוגות, והפעולה נעשית בכל רכיב בנפרד.", do=show("p-def")),
    P("ניקח את הזוג חמש ושתיים: חמש מודולו שלוש עשרה, ושתיים מודולו חמש.", do=show("p-0")),
    P("ברכיב הראשון: חמש, שתים עשרה, שמונה, אחת. סדר ארבע.", do=show(*[f"c5-n-{k}" for k in range(4)],
                                                                       *[f"c5-a-{k}" for k in range(4)])),
    P("ברכיב השני: שתיים, ארבע, שלוש, אחת. גם סדר ארבע.", do=show(*[f"c2-n-{k}" for k in range(4)],
                                                                   *[f"c2-a-{k}" for k in range(4)])),
    P("הזוג חוזר לאחת ואחת כששני הרכיבים חוזרים יחד. זה קורה בחזקה הרביעית.", do=show("p-1")),
    P("לכן הסדר של הזוג הוא הכפולה המשותפת הקטנה ביותר של הסדרים, כלומר ארבע.", do=show("p-r")),
    P("והמלכודת: לכפול את הסדרים ולקבל שש עשרה. שש עשרה היא חזקה שמחזירה, אבל לא הקטנה ביותר.",
      do=show("p-t")),
], stage=f'<div class="gc-stack"><div id="p-0" class="gc-mid h">$(5,2)\\in\\mathbb{{Z}}_{{13}}^*\\times\\mathbb{{Z}}_5^*$</div>'
         f'<div class="gc-row">{CYC5}{CYC2}</div></div>',
   panel=st.card("p-def", "rule", "🔑 $(g,h)\\cdot(g',h')=(gg',hh')$")
         + st.card("p-1", "ex", "$(5,2)^4=(1,1)$")
         + st.card("p-r", "rule", "🔑 $o((g,h))=\\operatorname{lcm}(o(g),o(h))$")
         + st.card("p-t", "trap", "⚠️ לא המכפלה: $\\operatorname{lcm}(4,4)=4$, לא $16$"))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: מטריצות שתיים על שתיים מעל $\\mathbb{Z}_5$, שכל הרכיבים שלהן שונים מאפס.", do=show("x-0")),
    P("והפעולה היא כפל **רכיב-רכיב**, מודולו חמש. בדיוק כמו מכפלה ישרה של ארבעה עותקים."),
    P("הסדר של החבורה: לכל רכיב יש ארבעה ערכים, אחת עד ארבע. לכן ארבע בחזקת ארבע, מאתיים חמישים ושש.",
      do=show("x-1")),
    P("המלכודת: לספור גם את האפס, ולקבל חמש בחזקת ארבע.", do=show("x-t1"), hold=0.3),
    P("ועכשיו הסדר של המטריצה אחת, שתיים, שתיים, שלוש. קודם: מהו הניטרלי?", do=show("x-2")),
    P("בכפל רכיב-רכיב, הניטרלי הוא המטריצה שכל רכיביה אחת. לא מטריצת היחידה.", do=show("x-3", "x-t2")),
    P("מעלים בחזקות, וכל רכיב לחוד: שתיים בריבוע ארבע, שלוש בריבוע תשע, כלומר ארבע.", do=show("x-4")),
    P("בשלישית: שמונה הוא שלוש, ועשרים ושבע הוא שתיים.", do=show("x-5")),
    P("וברביעית כל הרכיבים אחת. הגענו לניטרלי.", do=show("x-6")),
    P("וזה בדיוק הכפולה המשותפת של הסדרים: אחת, ארבע, ארבע, ארבע. הסדר הוא ארבע.", do=show("x-ans")),
    P("ולגרנז' מאשר: ארבע מחלק את מאתיים חמישים ושש.", do=show("x-l"), hold=0.5),
], stage='<div class="gc-stack">'
         + w.lines("x", ["$|H|=4^4=256$", "$X=" + pmx(pw[0]) + "$", "$e=" + pmx(ONE) + "$",
                         "$X^2=" + pmx(pw[1]) + "$", "$X^3=" + pmx(pw[2]) + "$", "$X^4=" + pmx(pw[3]) + "=e$"],
                   size=36, start=1)
         + '</div>',
   panel=w.ctx_stem("25B-B-Q2b/c", "$H$: מטריצות $2\\times2$ מעל $\\mathbb{Z}_5$ שכל רכיביהן שונים מאפס, עם כפל רכיב-רכיב.",
                    "<div>א.2. מהו הסדר של $H$?</div><div>א.3. מצאו את הסדר של $" + pmx(X) + "$.</div>")
         + st.card("x-0", "plain", "$a,b,c,d\\in\\{1,2,3,4\\}$")
         + st.card("x-t1", "trap", "⚠️ $0$ אסור: לא $5^4$")
         + st.card("x-t2", "trap", "⚠️ הניטרלי: כל הרכיבים $1$, לא $I$")
         + w.chip("x-ans", "$o(X)=\\operatorname{lcm}(1,4,4,4)=4$", 0)
         + st.card("x-l", "plain", "$4\\mid256$ ✓"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: סדר חבורה הוא מספר האיברים. סופרים בעקרון הכפל.", do=show("r-1")),
    P("סדר איבר: מעלים בחזקות עד שחוזרים לניטרלי.", do=show("r-2")),
    P("בזוג, או בפעולה רכיב-רכיב: הכפולה המשותפת הקטנה ביותר של הסדרים.", do=show("r-3")),
    P("ולגרנז': סדר של איבר תמיד מחלק את סדר החבורה. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage=f'<div class="gc-stack">{w.cycle("rc", [str(v) for v in P3], [("3", str(k)) for k in range(1, 5)], r=150, node=44, hidden=False)}</div>',
   panel=st.card("r-1", "rule", "🔑 $|G|$: ספירה")
         + st.card("r-2", "rule", "🔑 $o(x)$: חזקות עד $e$")
         + st.card("r-3", "rule", "🔑 זוג: $\\operatorname{lcm}$ של הסדרים")
         + st.card("r-4", "rule", "🔑 $o(x)\\mid|G|$"))

VIDEO = Video("G04", "groups_crt", "סדר חבורה וסדר איבר", [title, grp, elt, pair, ex, recap],
              bank={"25B-B-Q2b": None, "25B-B-Q2c": None})
