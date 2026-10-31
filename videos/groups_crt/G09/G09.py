# -*- coding: utf-8 -*-
"""G09 · מקדמים, שאריות גדולות ומודולים לא זרים — video script (build: tools/video/vid.py G09).

Source: courses/groups_crt/C09.js (lesson + goal). Exam anchor: 24A-B-Q4d (3x = 14 mod 8, x = 4 mod 9, x = 22 mod 25;
answer 922 mod 1800), which no guided quiz uses (24A-B-Q4a, the same exam's group part, is a boss item; this CRT part
is unrelated to it).
Avoided on purpose: 26A-A-Q5d and 25B-B-Q4b (their line 2x = 3 mod 7 is the first line of the C09-Q2 quiz system), the
C09 quiz items (4x = 3 mod 7, the system 2x = 3 (7) / 11 (4) / 4 (5), the moduli 4 and 6, the findbug system
1 (3) / 2 (5) / 5 (7)) and its bank part 24A-C-Q4b, 5^-1 mod 7 (it reveals C06-Q1), the lesson's 23 mod 9, 5x = 2 mod 9
and 3x = 4 mod 7, and the boss's 24A-A-Q5b / 24B-A-Q5b. Worked examples are new: 3x = 5 mod 8, 19 mod 4, the compatible
pair 3 (6) / 5 (8) -> 21 mod 24, and the incompatible pair 2 (6) / 4 (9).
"""
from math import gcd
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

# ---------------------------------------------------------------- verified facts
assert w.inv_mod(3, 8) == 3 and w.solve_linear(3, 5, 8) == [7] and 3 * 5 == 15 and 15 % 8 == 7 and 3 * 7 == 21 == 16 + 5
assert 19 % 4 == 3
both = lambda a, m, b, n: [v for v in range(m * n // gcd(m, n)) if v % m == a and v % n == b]
assert gcd(6, 8) == 2 and (3 - 5) % 2 == 0 and both(3, 6, 5, 8) == [21]
assert [v for v in (5, 13, 21)] == [5 + 8 * k for k in range(3)] and [v % 6 for v in (5, 13, 21)] == [5, 1, 3]
assert gcd(6, 9) == 3 and 2 % 3 == 2 and 4 % 3 == 1 and both(2, 6, 4, 9) == []
assert all(not (v % 6 == 2 and v % 9 == 4) for v in range(1000))

# exam 24A-B-Q4d
assert "922" in BANK["24A-B-Q4d"]["solution"] and "1800" in BANK["24A-B-Q4d"]["solution"]
assert 14 % 8 == 6 and w.inv_mod(3, 8) == 3 and (3 * 6) % 8 == 2 and w.solve_linear(3, 14, 8) == [2]
X = w.crt([2, 4, 22], [8, 9, 25])
assert X["M"] == 1800 and X["x"] == 922 and X["total"] == 17122 and 17122 - 9 * 1800 == 922
assert X["rows"] == [(8, 2, 225, 1, 1, 450), (9, 4, 200, 2, 5, 4000), (25, 22, 72, 22, 8, 12672)]
assert 72 % 25 == 22 and (22 - 25) == -3 and (-3 * 8) % 25 == 1 and (22 * 8) == 176 == 7 * 25 + 1
assert (3 * 922 - 14) % 8 == 0 and 922 % 9 == 4 and 922 % 25 == 22 and 3 * 922 == 2766
BAD = w.crt([6, 4, 22], [8, 9, 25])                               # the trap: copying 14 -> 6 without the coefficient
assert BAD["x"] == 22 and (3 * 22) % 8 == 2 != 6

HEAD = ["$m_i$", "$a_i$", "$M_i$", "$M_i\\bmod m_i$", "$x_i$", "$a_iM_ix_i$"]
TX = w.table("tx", HEAD, [[f"${v}$" for v in r] for r in X["rows"]], size=32)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("במבחן המערכת לא תמיד מגיעה מוכנה למתכון."),
    P("נלמד להכין כל שורה, ולזהות מתי למערכת אין פתרון בכלל."),
    P("ובסוף מערכת ממבחן שבה בשורה הראשונה יש מקדם.", hold=0.4),
], stage='<div class="kicker">G09 · חבורות ומשפט השאריות הסיני</div><h1>מקדמים, שאריות גדולות ומודולים לא זרים</h1>'
         '<p>להכין כל מערכת לצורה הרגילה, ולזהות מערכת שאין לה פתרון כי המודולים אינם זרים.</p>', layout="title")

prepS = Scene("prep", "הכנה", [
    P("המתכון דורש שכל שורה תהיה $x$ שקול לשארית קטנה. שני דברים יכולים להפריע.", do=show("p-r"),
      say="המתכון דורש שכל שורה תהיה אִקְס שקול לשארית קטנה. שני דברים יכולים להפריע."),
    P("שארית גדולה מהמודול: תשע עשרה מודולו ארבע. מחליפים בשארית: שלוש.", do=show("p-0")),
    P("ומקדם לפני $x$: שלוש $x$ שקול לחמש, מודולו שמונה.", do=show("p-1"),
      say="ומקדם לפני אִקְס: שלוש אִקְס שקול לחמש, מודולו שמונה."),
    P("ההופכי של שלוש מודולו שמונה הוא שלוש, כי תשע זה אחת. כופלים בו את שני האגפים.", do=show("p-2", "p-t")),
    P("יוצא $x$ שקול לחמש עשרה, כלומר לשבע. ובדיקה: שלוש כפול שבע זה עשרים ואחת, שזה חמש.", do=show("p-3"),
      say="יוצא אִקְס שקול לחמש עשרה, כלומר לשבע. ובדיקה: שלוש כפול שבע זה עשרים ואחת, שזה חמש."),
], stage='<div class="gc-stack">'
         + w.lines("p", ["$x\\equiv19\\pmod4\\ \\Rightarrow\\ x\\equiv3\\pmod4$", "$3x\\equiv5\\pmod8$",
                         "$3^{-1}\\equiv3:\\quad 3\\cdot3x\\equiv3\\cdot5$", "$x\\equiv15\\equiv7\\pmod8$"], size=42)
         + '</div>',
   panel=st.card("p-r", "rule", "🔑 כל שורה: $x\\equiv a_i\\pmod{m_i}$, $0\\le a_i&lt;m_i$")
         + st.card("p-t", "trap", "⚠️ מקדם: כופלים בהופכי שלו, לא מוחקים אותו"))

nc = Scene("coprime", "מודולים לא זרים", [
    P("ומה אם המודולים לא זרים? אז הנוסחה לא עובדת: חלק מה-$M_i$ לא הפיכים.", do=show("n-0"),
      say="ומה אם המודולים לא זרים? אז הנוסחה לא עובדת: חלק מהאֶם אַיי לא הפיכים."),
    P("בודקים **תאימות**: מוצאים את המחלק המשותף הגדול של שני המודולים.", do=show("n-r")),
    P("יש פתרון בדיוק כשהשאריות שקולות מודולו המחלק הזה. ואז הוא יחיד מודולו הכפולה המשותפת הקטנה.", hold=0.2),
    P("דוגמה: שלוש מודולו שש, וחמש מודולו שמונה. המחלק המשותף שתיים, ושלוש וחמש שניהם אי-זוגיים. תואם.",
      do=show("n-1")),
    P("מחפשים בין חמש, שלוש עשרה ועשרים ואחת, שכולם חמש מודולו שמונה. רק עשרים ואחת נותן שלוש מודולו שש.",
      do=show("n-2")),
    P("לכן $x$ שקול לעשרים ואחת, מודולו עשרים וארבע.", do=show("n-3"),
      say="לכן אִקְס שקול לעשרים ואחת, מודולו עשרים וארבע."),
    P("ועכשיו שתיים מודולו שש, וארבע מודולו תשע. המחלק המשותף שלוש.", do=show("n-4")),
    P("הראשונה אומרת ששארית החלוקה בשלוש היא שתיים, והשנייה אומרת שהיא אחת. סתירה: **אין פתרון**.",
      do=show("n-5", "n-t"), hold=0.3),
], stage='<div class="gc-stack">'
         + w.lines("n", ["$\\gcd(m,n)=g$", "$x\\equiv3\\ (6),\\ \\ x\\equiv5\\ (8):\\quad g=2,\\ \\ 3\\equiv5\\pmod2$",
                         "$5,\\ 13,\\ 21:\\quad 21\\equiv3\\pmod6$", "$x\\equiv21\\pmod{24}$",
                         "$x\\equiv2\\ (6),\\ \\ x\\equiv4\\ (9):\\quad g=3$", "$x\\equiv2\\pmod3$ &nbsp;אבל&nbsp; $x\\equiv1\\pmod3$"],
                   size=36)
         + '</div>',
   panel=st.card("n-r", "rule", "🔑 יש פתרון אם ורק אם $a\\equiv b\\pmod g$<br>ואז הוא יחיד מודולו $\\operatorname{lcm}(m,n)$")
         + st.card("n-t", "trap", "⚠️ מודולים לא זרים: קודם תאימות, ורק אז מחפשים"))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: בשורה הראשונה גם מקדם וגם שארית גדולה מהמודול. קודם מכינים.", do=show("x-sys")),
    P("שלוש $x$ שקול לארבע עשרה מודולו שמונה. ארבע עשרה מודולו שמונה זה שש.", do=show("x-0"),
      say="שלוש אִקְס שקול לארבע עשרה מודולו שמונה. ארבע עשרה מודולו שמונה זה שש."),
    P("ההופכי של שלוש הוא שלוש. לכן $x$ שקול לשמונה עשרה, כלומר לשתיים.", do=show("x-1"),
      say="ההופכי של שלוש הוא שלוש. לכן אִקְס שקול לשמונה עשרה, כלומר לשתיים."),
    P("שתי השורות האחרות כבר מוכנות. שמונה, תשע ועשרים וחמש זרים בזוגות, ו-$M$ הוא אלף ושמונה מאות.",
      do=show("x-2"), say="שתי השורות האחרות כבר מוכנות. שמונה, תשע ועשרים וחמש זרים בזוגות, ואֶם הוא אלף ושמונה מאות."),
    P("$M_i$: מאתיים עשרים וחמש, מאתיים, ושבעים ושתיים.",
      do=show(*[f"tx-{r}-{c}" for r in range(3) for c in range(3)]),
      say="אֶם אַיי: מאתיים עשרים וחמש, מאתיים, ושבעים ושתיים."),
    P("מאתיים עשרים וחמש מודולו שמונה זה אחת. מאתיים מודולו תשע זה שתיים, וההופכי של שתיים הוא חמש.",
      do=show("tx-0-3", "tx-0-4", "tx-1-3", "tx-1-4")),
    P("שבעים ושתיים מודולו עשרים וחמש זה עשרים ושתיים, כלומר מינוס שלוש. ומינוס שלוש כפול שמונה זה מינוס עשרים וארבע, שזה אחת.",
      do=show("tx-2-3", "tx-2-4", "x-c")),
    P("המחוברים: ארבע מאות וחמישים, ארבעת אלפים, ושתים עשרה אלף שש מאות שבעים ושתיים.",
      do=show("tx-0-5", "tx-1-5", "tx-2-5")),
    P("הסכום שבעה עשר אלף מאה עשרים ושתיים. מודולו אלף ושמונה מאות: תשע מאות עשרים ושתיים.",
      do=show("x-4", "x-ans")),
    P("והבדיקה במשוואה **המקורית**: שלוש כפול תשע מאות עשרים ושתיים נותן שש מודולו שמונה, כמו ארבע עשרה.",
      do=show("x-5")),
    P("המלכודת: להעתיק את ארבע עשרה, או את שש, כשארית בלי לבטל את המקדם. יוצא עשרים ושתיים, והבדיקה נכשלת.",
      do=show("x-t"), hold=0.5),
], stage='<div class="gc-stack">'
         + w.lines("x", ["$3x\\equiv14\\equiv6\\pmod8$", "$x\\equiv3\\cdot6=18\\equiv2\\pmod8$",
                         "$M=8\\cdot9\\cdot25=1800$"], size=34)
         + TX
         + w.lines("x", ["$450+4000+12672=17122\\equiv922\\pmod{1800}$",
                         "$3\\cdot922=2766\\equiv6\\equiv14\\ (8),\\ \\ 922\\equiv4\\ (9),\\ \\ 922\\equiv22\\ (25)$"],
                   size=30, start=4)
         + '</div>',
   panel=w.qstem("24A-B-Q4d", "פתרו באמצעות משפט השאריות הסיני:")
         + '<div id="x-sys" class="gc-mid h">$\\begin{cases}3x\\equiv14\\pmod8\\\\x\\equiv4\\pmod9\\\\x\\equiv22\\pmod{25}'
           '\\end{cases}$</div>'
         + st.card("x-c", "ex", "$72\\equiv-3\\pmod{25}$, &nbsp;$(-3)\\cdot8=-24\\equiv1$")
         + w.chip("x-ans", "$x\\equiv922\\pmod{1800}$", 0)
         + st.card("x-t", "trap", "⚠️ בלי לבטל את המקדם יוצא $22$, ו-$3\\cdot22\\equiv2\\not\\equiv6\\pmod8$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: לפני המתכון מכינים כל שורה. שארית גדולה מצמצמים, ומקדם מבטלים בהופכי שלו.", do=show("r-1")),
    P("מודולים לא זרים: בודקים תאימות מודולו המחלק המשותף. אם אין תאימות, אין פתרון.", do=show("r-2")),
    P("ואם יש, הפתרון יחיד מודולו הכפולה המשותפת הקטנה.", do=show("r-3")),
    P("ותמיד בודקים במשוואות המקוריות. בשלב הבא, מבחן הגמר. בהצלחה.", do=show("r-4"), hold=0.6),
], stage='<div class="gc-stack"><div class="gc-mid">$cx\\equiv r\\ \\Rightarrow\\ x\\equiv c^{-1}r$</div></div>',
   panel=st.card("r-1", "rule", "🔑 שארית לתחום, מקדם בהופכי")
         + st.card("r-2", "rule", "🔑 לא זרים: $a\\equiv b\\pmod{\\gcd}$?")
         + st.card("r-3", "rule", "🔑 פתרון יחיד מודולו $\\operatorname{lcm}$")
         + st.card("r-4", "rule", "🔑 בדיקה במקור"))

VIDEO = Video("G09", "groups_crt", "מקדמים, שאריות גדולות ומודולים לא זרים", [title, prepS, nc, ex, recap],
              bank={"24A-B-Q4d": None})
