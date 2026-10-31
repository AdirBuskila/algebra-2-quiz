# -*- coding: utf-8 -*-
"""G07 · חבורות מטריצות מודולו מספר ראשוני — video script (build: tools/video/vid.py G07).

Source: courses/groups_crt/C07.js (lesson + goal). Exam anchors: 26B-A-Q2a (|G| for the invertible upper-triangular
2x2 matrices over Z_5), 26B-A-Q2b (all elements of H = <J>, J = (1 1; 0 2)) and 26B-A-Q2d (|H|); no guided quiz uses
them. Not used: 26B-A-Q2c (J^-1), to stay clear of the C07 quiz's inverse of (1 3; 0 2) over Z_5.
Avoided on purpose: the C07 quiz items ((a b; 0 a) over Z_7, (1 3; 0 1) and diag(2,4) over Z_7, the inverse above) and
its bank parts 24A-A-Q4a/c, the lesson's examples ((1 b; 0 c) over Z_5, (2 1; 0 3) over Z_7, diag(2,6)), the boss's
23B-A-Q2b and 24A-B-Q4a. Worked examples are new: the 3x3 unipotent matrices over Z_3 and the inverse of (3 2; 0 4)
over Z_5.
"""
from itertools import product
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

# ---------------------------------------------------------------- verified facts
U3 = [((1, a, b), (0, 1, c), (0, 0, 1)) for a, b, c in product(range(3), repeat=3)]
assert len(U3) == 27 == 3 ** 3
assert all(w.mmul(X, Y, 3) in set(U3) for X in U3 for Y in U3)            # closed (a group, brute force)

A = ((3, 2), (0, 4))
x, z = w.inv_mod(3, 5), w.inv_mod(4, 5)
y = (-x * 2 * z) % 5
assert (x, z, y) == (2, 4, 4) and -x * 2 * z == -16
Ainv = ((x, y), (0, z))
assert Ainv == ((2, 4), (0, 4)) and w.mmul(A, Ainv, 5) == w.eye(2) == w.mmul(Ainv, A, 5)
raw = tuple(tuple(sum(A[i][k] * Ainv[k][j] for k in range(2)) for j in range(2)) for i in range(2))
assert raw == ((6, 20), (0, 16))

# exam 26B-A-Q2a/b/d over Z_5
assert "80" in BANK["26B-A-Q2a"]["solution"] and "|H|=4" in BANK["26B-A-Q2d"]["solution"].replace(" ", "")
G = [((a, b), (0, c)) for a in range(5) for b in range(5) for c in range(5) if (a * c) % 5 != 0]
assert len(G) == 80 == 4 * 5 * 4
J = ((1, 1), (0, 2))
pows = [w.mpow(J, k, 5) for k in range(1, 5)]
assert pows == [((1, 1), (0, 2)), ((1, 3), (0, 4)), ((1, 2), (0, 3)), ((1, 0), (0, 1))]
assert w.morder(J, 5) == 4 and len(set(pows)) == 4 and 80 % 4 == 0
rawJ3 = ((1, 7), (0, 8))                                                    # J^3 before reducing mod 5
assert tuple(tuple(v % 5 for v in r) for r in rawJ3) == pows[2]
assert all(J[0][0] * B[0][0] == 1 for B in pows)                            # the top-left entry stays 1

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה החבורה בנויה ממטריצות, וכל החשבון נעשה מודולו מספר ראשוני."),
    P("נספור איברים, נמצא הופכי, ונחשב סדר של מטריצה."),
    P("ובסוף שלושה סעיפים ממבחן.", hold=0.4),
], stage='<div class="kicker">G07 · חבורות ומשפט השאריות הסיני</div><h1>חבורות מטריצות מודולו מספר ראשוני</h1>'
         '<p>לספור איברים בחבורת מטריצות מעל שדה סופי, למצוא הופכי, ולחשב סדר של מטריצה.</p>', layout="title")

cnt = Scene("count", "ספירה", [
    P("מעל $\\mathbb{Z}_p$ כל רכיב הוא מספר מאפס עד $p$ פחות אחת, וכל חיבור וכפל מצמצמים מודולו $p$.",
      do=show("c-def"), say="מעל זֶד פִּי כל רכיב הוא מספר מאפס עד פִּי פחות אחת, וכל חיבור וכפל מצמצמים מודולו פִּי."),
    P("הניטרלי בכפל מטריצות הוא מטריצת היחידה.", do=show("c-e")),
    P("כמה איברים יש בחבורה? סופרים לפי עקרון הכפל: כמה בחירות לכל רכיב, ומכפילים.", do=show("c-r")),
    P("למשל מטריצות שלוש על שלוש מעל $\\mathbb{Z}_3$, עם אחדות על האלכסון ואפסים מתחתיו.", do=show("c-0"),
      say="למשל מטריצות שלוש על שלוש מעל זֶד שלוש, עם אחדות על האלכסון ואפסים מתחתיו."),
    P("נשארו שלושה רכיבים חופשיים, ולכל אחד שלוש אפשרויות. בסך הכול שלוש בחזקת שלוש, עשרים ושבע.",
      do=show("c-1")),
], stage='<div class="gc-stack">'
         + w.lines("c", ["$\\begin{pmatrix}1&a&b\\\\0&1&c\\\\0&0&1\\end{pmatrix},\\quad a,b,c\\in\\mathbb{Z}_3$",
                         "$3\\cdot3\\cdot3=27$"], size=44)
         + '</div>',
   panel=st.card("c-def", "rule", "🔑 כל פעולה מודולו $p$")
         + st.card("c-e", "ex", "ניטרלי: $I$")
         + st.card("c-r", "rule", "🔑 עקרון הכפל: בחירות לכל רכיב"))

inv = Scene("inv", "הופכי", [
    P("הופכי של מטריצה משולשית עליונה: יש נוסחה קצרה.", do=show("i-0")),
    P("הרכיבים על האלכסון מתהפכים: $x$ הוא ההופכי של $a$, ו-$z$ הוא ההופכי של $c$.", do=show("i-1"),
      say="הרכיבים על האלכסון מתהפכים: אִקְס הוא ההופכי של אֵיי, וזֶד הוא ההופכי של סִי."),
    P("והרכיב שמעליהם: מינוס $x$, כפול $b$, כפול $z$.", do=show("i-2"),
      say="והרכיב שמעליהם: מינוס אִקְס, כפול בִּי, כפול זֶד."),
    P("נפעיל על שלוש, שתיים, אפס, ארבע, מעל $\\mathbb{Z}_5$.", do=show("i-3"),
      say="נפעיל על שלוש, שתיים, אפס, ארבע, מעל זֶד חמש."),
    P("ההופכי של שלוש הוא שתיים, וההופכי של ארבע הוא ארבע. כי שש ושש עשרה הם אחת, מודולו חמש.", do=show("i-4")),
    P("ולמעלה: מינוס שתיים כפול שתיים כפול ארבע, מינוס שש עשרה. ומודולו חמש זה ארבע.", do=show("i-5")),
    P("ובדיקה: המכפלה יוצאת שש, עשרים, אפס, שש עשרה. ומודולו חמש זו בדיוק מטריצת היחידה.", do=show("i-6")),
    P("שימו לב: מינוס שש עשרה שקול לארבע. כותבים ארבע: התשובה צריכה להיות בין אפס לארבע.", do=show("i-t")),
], stage='<div class="gc-stack">'
         + w.lines("i", ["$\\begin{pmatrix}a&b\\\\0&c\\end{pmatrix}^{-1}=\\begin{pmatrix}x&y\\\\0&z\\end{pmatrix}$",
                         "$x=a^{-1},\\quad z=c^{-1}$", "$y=-x\\,b\\,z$",
                         "$A=" + w.pm(A) + "$ &nbsp;מעל $\\mathbb{Z}_5$",
                         "$x=3^{-1}=2,\\quad z=4^{-1}=4$", "$y=-2\\cdot2\\cdot4=-16\\equiv4$",
                         "$" + w.pm(A) + w.pm(Ainv) + "=" + w.pm(raw) + "\\equiv I$"], size=36)
         + '</div>',
   panel=st.card("i-t", "trap", "⚠️ מצמצמים כל רכיב לתחום $0..p-1$, גם מספר שלילי"))

D = ((3, 0), (0, 4))
Dp = [w.mpow(D, k, 5) for k in range(1, 5)]
assert Dp == [((3, 0), (0, 4)), ((4, 0), (0, 1)), ((2, 0), (0, 4)), ((1, 0), (0, 1))]
assert w.morder(D, 5) == 4 == w.lcm(w.order_mod(3, 5), w.order_mod(4, 5)) and w.order_mod(4, 5) == 2
ordr = Scene("order", "סדר של מטריצה", [
    P("סדר של מטריצה: מעלים בחזקות, מצמצמים בכל שלב, עד שמגיעים למטריצת היחידה.", do=show("o-r")),
    P("במטריצה אלכסונית כל רכיב על האלכסון עולה בחזקה לבד. ניקח שלוש וארבע, מעל $\\mathbb{Z}_5$.", do=show("o-0"),
      say="במטריצה אלכסונית כל רכיב על האלכסון עולה בחזקה לבד. ניקח שלוש וארבע, מעל זֶד חמש."),
    P("בריבוע: תשע ושש עשרה, כלומר ארבע ואחת.", do=show("o-1")),
    P("בשלישית: שתיים וארבע. וברביעית: אחת ואחת. זו מטריצת היחידה, והסדר הוא ארבע.", do=show("o-2", "o-3")),
    P("וזה בדיוק הכפולה המשותפת הקטנה ביותר של הסדרים: ארבע לשלוש, ושתיים לארבע.", do=show("o-c"), hold=0.3),
], stage='<div class="gc-stack">'
         + w.lines("o", ["$D=" + w.pm(Dp[0]) + "$", "$D^2=" + w.pm(Dp[1]) + "$",
                         "$D^3=" + w.pm(Dp[2]) + "$", "$D^4=" + w.pm(Dp[3]) + "=I$"], size=34)
         + '</div>',
   panel=st.card("o-r", "rule", "🔑 $o(A)$: הקטן ביותר עם $A^n=I$")
         + st.card("o-c", "ex", "$o(D)=\\operatorname{lcm}(o(3),o(4))=\\operatorname{lcm}(4,2)=4$"))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: המטריצות המשולשיות העליונות ההפיכות מעל $\\mathbb{Z}_5$. מהו הסדר של $G$?",
      say="שאלה ממבחן: המטריצות המשולשיות העליונות ההפיכות מעל זֶד חמש. מהו הסדר של גִ'י?"),
    P("התנאי $ac\\ne0$, ומעל שדה זה אומר ש-$a$ ו-$c$ שניהם שונים מאפס. ארבע אפשרויות לכל אחד.", do=show("x-0"),
      say="התנאי, אֵיי סִי שונה מאפס, ומעל שדה זה אומר שאֵיי וסִי שניהם שונים מאפס. ארבע אפשרויות לכל אחד."),
    P("ול-$b$ אין הגבלה: חמש אפשרויות. לכן ארבע כפול חמש כפול ארבע, שמונים.", do=show("x-1"),
      say="ולבִּי אין הגבלה: חמש אפשרויות. לכן ארבע כפול חמש כפול ארבע, שמונים."),
    P("עכשיו $H$: כל החזקות של $J$, המטריצה אחת, אחת, אפס, שתיים.", do=show("x-2"),
      say="עכשיו אֵייץ': כל החזקות של גֵ'יי, המטריצה אחת, אחת, אפס, שתיים."),
    P("בריבוע: אחת, שלוש, אפס, ארבע.", do=show("x-3")),
    P("בשלישית יוצא שבע ושמונה. מודולו חמש: שתיים ושלוש.", do=show("x-4")),
    P("וברביעית: מטריצת היחידה. מכאן החזקות רק חוזרות.", do=show("x-5")),
    P("לכן ב-$H$ יש בדיוק ארבע מטריצות: היחידה, ושלוש החזקות הראשונות של $J$.", do=show("x-ans"),
      say="לכן באֵייץ' יש בדיוק ארבע מטריצות: היחידה, ושלוש החזקות הראשונות של גֵ'יי."),
    P("והסדר של $H$ הוא ארבע, כי הוא שווה לסדר של $J$. ולגרנז' מאשר: ארבע מחלק את שמונים.", do=show("x-l"),
      say="והסדר של אֵייץ' הוא ארבע, כי הוא שווה לסדר של גֵ'יי. ולגרנז' מאשר: ארבע מחלק את שמונים."),
    P("המלכודות: לענות שמונים, שזה הסדר של $G$. או חמש, שזה המודולו.", do=show("x-t"),
      say="המלכודות: לענות שמונים, שזה הסדר של גִ'י. או חמש, שזה המודולו.", hold=0.5),
], stage='<div class="gc-stack">'
         + w.lines("x", ["$a,c\\in\\{1,2,3,4\\},\\ \\ b\\in\\{0,\\dots,4\\}$", "$|G|=4\\cdot5\\cdot4=80$",
                         "$J=" + w.pm(pows[0]) + "$", "$J^2=" + w.pm(pows[1]) + "$",
                         "$J^3=" + w.pm(rawJ3) + "\\equiv" + w.pm(pows[2]) + "$", "$J^4=" + w.pm(pows[3]) + "=I$"],
                   size=34)
         + '</div>',
   panel=w.ctx_stem("26B-A-Q2a/b/d", "<div>$G=\\left\\{" + "\\begin{pmatrix}a&b\\\\0&c\\end{pmatrix}" + "\\in M_2(\\mathbb{Z}_5)"
                    "\\ \\middle|\\ ac\\ne0\\right\\}$</div><div>$H=\\{J^n\\mid n\\in\\mathbb{Z}\\},\\ \\ J=" + w.pm(J) + "$</div>",
                    "<div>1. מהו הסדר של $G$?</div><div>2. חשבו את כל האיברים של $H$.</div><div>4. מהו הסדר של $H$?</div>")
         + w.chip("x-ans", "$H=\\{I,J,J^2,J^3\\}$", 0)
         + st.card("x-l", "ex", "$|H|=o(J)=4$, &nbsp;$4\\mid80$")
         + st.card("x-t", "trap", "⚠️ לא $80$ (זה $|G|$) ולא $5$ (המודולו)"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: במטריצות מעל $\\mathbb{Z}_p$ כל חישוב מצמצמים מודולו $p$, בכל שלב.", do=show("r-1"),
      say="לסיכום: במטריצות מעל זֶד פִּי כל חישוב מצמצמים מודולו פִּי, בכל שלב."),
    P("סופרים איברים בעקרון הכפל, ושמים לב לרכיבים שאסור להם להיות אפס.", do=show("r-2")),
    P("הופכי של משולשית: הופכים את האלכסון, ולמעלה מינוס $x$ בִּי $z$.", do=show("r-3"),
      say="הופכי של משולשית: הופכים את האלכסון, ולמעלה מינוס אִקְס בִּי זֶד."),
    P("וסדר של מטריצה: חזקות עד מטריצת היחידה. ברמה הבאה: משפט השאריות הסיני. נתראה.", do=show("r-4"), hold=0.6),
], stage='<div class="gc-stack"><div class="gc-mid">$J^4=I\\ \\Rightarrow\\ o(J)=4$</div></div>',
   panel=st.card("r-1", "rule", "🔑 מודולו $p$ בכל שלב")
         + st.card("r-2", "rule", "🔑 עקרון הכפל")
         + st.card("r-3", "rule", "🔑 $x=a^{-1},\\ z=c^{-1},\\ y=-xbz$")
         + st.card("r-4", "rule", "🔑 $o(A)$: חזקות עד $I$"))

VIDEO = Video("G07", "groups_crt", "חבורות מטריצות מודולו מספר ראשוני", [title, cnt, inv, ordr, ex, recap],
              bank={"26B-A-Q2a": None, "26B-A-Q2b": None, "26B-A-Q2d": None})
