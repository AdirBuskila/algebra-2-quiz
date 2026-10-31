# -*- coding: utf-8 -*-
"""G05 · תת-חבורות והוכחות קצרות — video script (build: tools/video/vid.py G05).

Source: courses/groups_crt/C05.js (lesson + goal). Exam anchor: 26B-A-Q4a (if (xy)^2 = x^2 y^2 for all x, y then G is
abelian), which no guided quiz uses.
Avoided on purpose: the C05 quiz items (subgroups of (Z,+), <4> in Z_13^*, the H∩K proof = 25B-B-Q5b's twin) and its
bank parts 23B-B-Q4b and 24B-A-Q4b, the lesson's <2> in Z_7^*, and every "x^2 = e" exam part (23B-B-Q4c is a boss item;
25A-B-Q2a/b and 25A-C-Q5b/c are its twins). Worked examples are new: {1,6} and {1,3} inside Z_7^*, <3> and <6> there.
"""
from itertools import permutations
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

# ---------------------------------------------------------------- verified facts
m7 = lambda u, v: (u * v) % 7
U7 = w.zstar(7)
assert U7 == [1, 2, 3, 4, 5, 6]
R16 = w.group_report([1, 6], m7)
assert R16["group"] and R16["neutral"] == 1                     # {1,6} is a subgroup
R13 = w.group_report([1, 3], m7)
assert not R13["closed"] and m7(3, 3) == 2                       # {1,3}: 3*3 = 2 leaves the set
P3 = w.powers_mod(3, 7)
assert P3 == [3, 2, 6, 4, 5, 1] and len(P3) == w.order_mod(3, 7) == 6 and sorted(P3) == U7
assert w.powers_mod(6, 7) == [6, 1] and sorted(w.powers_mod(6, 7)) == [1, 6]
assert sorted({w.order_mod(u, 7) for u in U7}) == [1, 2, 3, 6] and all(6 % w.order_mod(u, 7) == 0 for u in U7)

# exam 26B-A-Q4a: the hypothesis is not vacuous (S3 breaks it), and in every abelian group it holds
assert "(xy)^2=x^2y^2" in BANK["26B-A-Q4a"]["question"].replace(" ", "")
S3 = list(permutations(range(3)))
comp = lambda p, q: tuple(p[q[i]] for i in range(3))
sq = lambda p: comp(p, p)
assert any(sq(comp(x, y)) != comp(sq(x), sq(y)) for x in S3 for y in S3)
assert any(comp(x, y) != comp(y, x) for x in S3 for y in S3)
# the cancellation steps on a concrete abelian group (Z_7^*): x y x y = x x y y  ->  y x y = x y y  ->  y x = x y
for x in U7:
    for y in U7:
        xi, yi = w.inv_mod(x, 7), w.inv_mod(y, 7)
        assert (x * y * x * y) % 7 == (x * x * y * y) % 7
        assert (xi * x * y * x * y) % 7 == (y * x * y) % 7 and (y * x * y * yi) % 7 == (y * x) % 7

CYC = w.cycle("c3", [str(v) for v in P3], [("3", str(k)) for k in range(1, 7)], r=170, node=42)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר חבורות שיושבות בתוך חבורות."),
    P("נבדוק מתי תת-קבוצה היא תת-חבורה, ונחשב גודל של תת-חבורה ציקלית."),
    P("ובסוף נכתוב הוכחה קצרה מתוך מבחן.", hold=0.4),
], stage='<div class="kicker">G05 · חבורות ומשפט השאריות הסיני</div><h1>תת-חבורות והוכחות קצרות</h1>'
         '<p>לבדוק אם תת-קבוצה היא תת-חבורה, לחשב גודל תת-חבורה ציקלית, ולכתוב הוכחה קצרה בחבורה.</p>', layout="title")

sub = Scene("sub", "תת-חבורה", [
    P("תת-חבורה היא תת-קבוצה שהיא בעצמה חבורה, עם אותה פעולה.", do=show("s-def")),
    P("את האסוציאטיביות היא יורשת מהחבורה הגדולה. נשארים שלושה תנאים.", do=show("s-1", "s-2", "s-3")),
    P("הניטרלי שייך אליה, יש סגירות, וההופכי של כל איבר שלה שייך אליה.", hold=0.2),
    P("ניקח את $\\mathbb{Z}_7^*$ עם כפל מודולו שבע, ואת התת-קבוצה אחת ושש.", do=show("s-t1"),
      say="ניקח את זֶד שבע כוכבית, עם כפל מודולו שבע, ואת התת-קבוצה אחת ושש."),
    P("אחת נמצאת בה. שש כפול שש זה שלושים ושש, כלומר אחת. ושש הופכי לעצמו. זו תת-חבורה.", do=show("s-v1")),
    P("ועכשיו אחת ושלוש. שלוש כפול שלוש זה תשע, כלומר שתיים.", do=show("s-t2", "q2-x-1-1")),
    P("שתיים לא בתת-הקבוצה. הסגירות נופלת, ולכן זו לא תת-חבורה.", do=show("s-v2")),
], stage='<div class="gc-stack"><div class="gc-row">'
         f'<div id="s-t1" class="gc-stack h">{w.cayley("q1", [1, 6], m7, sym="\\cdot", size=40)}'
         '<span class="gc-chip h" id="s-v1" style="border-color:#34d399;color:#34d399">תת-חבורה ✓</span></div>'
         f'<div id="s-t2" class="gc-stack h">{w.cayley("q2", [1, 3], m7, sym="\\cdot", size=40)}'
         '<span class="gc-chip h" id="s-v2" style="border-color:#fb7185;color:#fb7185">לא ✗</span></div>'
         '</div><div class="gc-note">כפל מודולו 7</div></div>',
   panel=st.card("s-def", "rule", "🔑 $H\\le G$: תת-קבוצה שהיא חבורה")
         + st.card("s-1", "ex", "1. $e\\in H$")
         + st.card("s-2", "ex", "2. $a,b\\in H\\ \\Rightarrow\\ ab\\in H$")
         + st.card("s-3", "ex", "3. $a\\in H\\ \\Rightarrow\\ a^{-1}\\in H$"))

cyc = Scene("cyc", "תת-חבורה ציקלית", [
    P("דרך בטוחה לייצר תת-חבורה: לוקחים איבר אחד, ואוספים את כל החזקות שלו.", do=show("y-def")),
    P("נאסוף את החזקות של שלוש מודולו שבע: שלוש, שתיים, שש.",
      do=show("c3-n-0", "c3-a-0", "c3-n-1", "c3-a-1", "c3-n-2")),
    P("ואז ארבע, חמש, ואחת. חזרנו לניטרלי אחרי שש חזקות.",
      do=show("c3-a-2", "c3-n-3", "c3-a-3", "c3-n-4", "c3-a-4", "c3-n-5", "c3-a-5")),
    P("הגודל של התת-חבורה הזו שווה לסדר של שלוש, כלומר שש. כאן היא כל החבורה.", do=show("y-1")),
    P("ומשש מקבלים רק שש ואחת. זו בדיוק התת-חבורה שראינו קודם, בגודל שתיים.", do=show("y-2")),
    P("ושוב לגרנז': שש ושתיים מחלקים את שש, הגודל של החבורה כולה.", do=show("y-l"), hold=0.3),
], stage=f'<div class="gc-stack">{CYC}</div>',
   panel=st.card("y-def", "rule", "🔑 $\\langle a\\rangle=\\{a^n\\mid n\\in\\mathbb{Z}\\}$")
         + st.card("y-1", "ex", "$|\\langle3\\rangle|=o(3)=6$")
         + st.card("y-2", "ex", "$\\langle6\\rangle=\\{6,1\\}$, &nbsp;$|\\langle6\\rangle|=2$")
         + st.card("y-l", "rule", "🔑 $|\\langle a\\rangle|=o(a)$ מחלק את $|G|$"))

tools = Scene("tools", "כלים להוכחה", [
    P("ועכשיו הוכחות קצרות בחבורה כללית. שני כלים עיקריים."),
    P("צמצום: אם $xa=xb$, כופלים משמאל בהופכי של $x$, ומקבלים $a=b$.",
      say="צמצום: אם אִקְס אֵיי שווה אִקְס בִּי, כופלים משמאל בהופכי של אִקְס, ומקבלים אֵיי שווה בִּי.", do=show("k-1", "k-1a")),
    P("אבל צמצום עובד רק מהקצה: משמאל עם משמאל, ומימין עם מימין.", do=show("k-t")),
    P("והכלי השני: ההופכי של מכפלה הופך את הסדר.", do=show("k-2")),
    P("למה? כופלים את $xy$ ב-$y^{-1}x^{-1}$. ה-$y$ פוגש את ההופכי שלו ונעלם, ואחריו גם ה-$x$.", do=show("k-3"),
      say="למה? כופלים את אִקְס וַואי בוַואי בחזקת מינוס אחת, אִקְס בחזקת מינוס אחת. הוַואי פוגש את ההופכי שלו ונעלם, ואחריו גם האִקְס."),
    P("יוצא הניטרלי, ולכן זה ההופכי. בסדר ההפוך, $x^{-1}y^{-1}$, זה לא עובד בחבורה כללית.", do=show("k-2c"),
      say="יוצא הניטרלי, ולכן זה ההופכי. בסדר ההפוך, אִקְס בחזקת מינוס אחת וַואי בחזקת מינוס אחת, זה לא עובד בחבורה כללית.",
      hold=0.3),
], stage='<div class="gc-stack">'
         + w.lines("k", ["$xa=xb\\ \\Rightarrow\\ x^{-1}xa=x^{-1}xb\\ \\Rightarrow\\ a=b$", "$(xy)^{-1}=y^{-1}x^{-1}$",
                          "$(xy)(y^{-1}x^{-1})=x(yy^{-1})x^{-1}=xx^{-1}=e$"],
                   size=44, start=1)
         + '</div>',
   panel=st.card("k-1a", "rule", "🔑 צמצום: כופלים בהופכי")
         + st.card("k-t", "trap", "⚠️ מוחקים רק את מה שבקצה של <b>שני</b> האגפים")
         + st.card("k-2c", "trap", "⚠️ $(xy)^{-1}\\ne x^{-1}y^{-1}$ בחבורה כללית"))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: בחבורה $G$, לכל $x$ ו-$y$ מתקיים $(xy)^2=x^2y^2$. הוכיחו שהחבורה אבלית.",
      say="שאלה ממבחן: בחבורה גִ'י, לכל אִקְס ווַואי מתקיים: אִקְס וַואי בריבוע, שווה אִקְס בריבוע וַואי בריבוע. הוכיחו שהחבורה אבלית."),
    P("קודם פותחים את הריבועים. בחבורה כללית אסור לסדר מחדש, אז כותבים הכול במפורש.", do=show("x-0")),
    P("משמאל: $xyxy$. מימין: $xxyy$.", say="משמאל: אִקְס וַואי אִקְס וַואי. מימין: אִקְס אִקְס וַואי וַואי.", do=show("x-1")),
    P("כופלים את שני האגפים משמאל בהופכי של $x$. ה-$x$ הראשון נעלם בשני הצדדים.", do=show("x-2"),
      say="כופלים את שני האגפים משמאל בהופכי של אִקְס. האִקְס הראשון נעלם בשני הצדדים."),
    P("נשאר $yxy=xyy$.", say="נשאר: וַואי אִקְס וַואי, שווה אִקְס וַואי וַואי.", do=show("x-3")),
    P("עכשיו כופלים מימין בהופכי של $y$. ה-$y$ האחרון נעלם.", do=show("x-4"),
      say="עכשיו כופלים מימין בהופכי של וַואי. הוַואי האחרון נעלם."),
    P("ונשאר $yx=xy$, לכל שני איברים. החבורה אבלית.", say="ונשאר: וַואי אִקְס שווה אִקְס וַואי, לכל שני איברים. החבורה אבלית.",
      do=show("x-5", "x-ans")),
    P("המלכודת: למחוק את ה-$y$ וה-$x$ שבאמצע ישירות. זה מניח את מה שרוצים להוכיח.", do=show("x-t"),
      say="המלכודת: למחוק את הוַואי והאִקְס שבאמצע ישירות. זה מניח את מה שרוצים להוכיח."),
    P("צמצום חוקי הוא רק כפל בהופכי, מהקצה.", hold=0.5),
], stage='<div class="gc-stack">'
         + w.lines("x", ["$(xy)^2=x^2y^2$", "$xyxy=xxyy$", "$x^{-1}\\cdot xyxy=x^{-1}\\cdot xxyy$", "$yxy=xyy$",
                         "$yxy\\cdot y^{-1}=xyy\\cdot y^{-1}$", "$yx=xy$"], size=44)
         + '</div>',
   panel=w.qstem("26B-A-Q4a", "תהי $G$ חבורה בה לכל $x,y\\in G$ מתקיים $(xy)^2=x^2y^2$. הוכיחו כי $G$ אבלית.")
         + w.chip("x-ans", "$xy=yx$ לכל $x,y$: אבלית", 0)
         + st.card("x-t", "trap", "⚠️ אסור למחוק באמצע. מצמצמים רק מהקצוות"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: תת-חבורה צריכה ניטרלי, סגירות והופכי. אסוציאטיביות עוברת בירושה.", do=show("r-1")),
    P("החזקות של איבר תמיד יוצרות תת-חבורה, והגודל שלה הוא הסדר של האיבר.", do=show("r-2")),
    P("ובהוכחות: מצמצמים רק על ידי כפל בהופכי, מהקצה, וזוכרים שההופכי של מכפלה הופך את הסדר.", do=show("r-3")),
    P("נתראה ברמה הבאה.", hold=0.6),
], stage=f'<div class="gc-stack">{w.cycle("rc", [str(v) for v in P3], [("3", str(k)) for k in range(1, 7)], r=170, node=42, hidden=False)}</div>',
   panel=st.card("r-1", "rule", "🔑 $e\\in H$, סגירות, הופכי")
         + st.card("r-2", "rule", "🔑 $|\\langle a\\rangle|=o(a)$")
         + st.card("r-3", "rule", "🔑 צמצום מהקצה, $(xy)^{-1}=y^{-1}x^{-1}$"))

VIDEO = Video("G05", "groups_crt", "תת-חבורות והוכחות קצרות", [title, sub, cyc, tools, ex, recap],
              bank={"26B-A-Q4a": None})
