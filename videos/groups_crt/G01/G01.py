# -*- coding: utf-8 -*-
"""G01 · סגירות ואסוציאטיביות — video script (build: tools/video/vid.py G01).

Source: courses/groups_crt/C01.js (lesson + goal). Exam anchors: 25B-B-Q3a + 25B-B-Q3b (a⊗b = ab - a - b on Z:
a binary operation, not associative), which no guided quiz uses.
Avoided on purpose: the C01 quiz and lesson operations (a-b on the positive integers, max(a,b)+1, 2a+b, a+b+ab), the
C03 quiz operation a+2b, 24A-B-Q2a and 24B-B-Q4b (C01 quiz) and 25B-A-Q4* (a⊙b = ab+a+b, the twin of C01's a+b+ab).
Worked examples are new: Cayley tables of {1,3,5,7} mod 8 and {1,2,3} mod 4, the integers = 1 mod 3 under + (not the odd integers: a C05-Q1 option), a+b+5 and ab+1.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_groups_crt as w

a, b, c = sp.symbols("a b c")

# ---------------------------------------------------------------- verified facts
S8 = [1, 3, 5, 7]
m8 = lambda x, y: (x * y) % 8
R8 = w.group_report(S8, m8)
assert R8["closed"]
T4 = [1, 2, 3]
m4 = lambda x, y: (x * y) % 4
bad4 = [(x, y) for x in T4 for y in T4 if m4(x, y) not in T4]
assert bad4 == [(2, 2)] and m4(2, 2) == 0
assert (1 + 1) % 3 == 2 != 1                               # 1 + 1 = 2: {x = 1 mod 3} is not closed under +

op1 = lambda x, y: x + y + 5                              # associative
assert sp.expand(op1(op1(a, b), c) - op1(a, op1(b, c))) == 0
assert sp.expand(op1(op1(a, b), c)) == a + b + c + 10
op2 = lambda x, y: x * y + 1                              # not associative
assert op2(op2(1, 2), 3) == 10 and op2(1, op2(2, 3)) == 8

# exam 25B-B-Q3a / Q3b: a ⊗ b = ab - a - b on Z
Q = BANK["25B-B-Q3b"]
assert "ab-a-b" in BANK["25B-B-Q3a"]["question"] or "\\otimes" in BANK["25B-B-Q3a"]["question"]
ot = lambda x, y: x * y - x - y
L = sp.expand(ot(ot(a, b), c))
R = sp.expand(ot(a, ot(b, c)))
assert L == a*b*c - a*c - b*c - a*b + a + b - c
assert R == a*b*c - a*b - a*c - a - b*c + b + c
assert sp.expand(L - R) == 2 * a - 2 * c                   # differ unless a = c
assert ot(ot(1, 0), 0) == 1 and ot(1, ot(0, 0)) == -1      # a numeric witness: a=1, b=c=0
assert all(isinstance(ot(x, y), int) for x in range(-5, 6) for y in range(-5, 6))

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נתחיל לבנות את המושג חבורה."),
    P("נבדוק מתי פעולה נשארת בתוך הקבוצה, ומתי מותר להזיז סוגריים."),
    P("ובסוף נפתור שני סעיפים ממבחן.", hold=0.4),
], stage='<div class="kicker">G01 · חבורות ומשפט השאריות הסיני</div><h1>סגירות ואסוציאטיביות</h1>'
         '<p>לבדוק אם פעולה על קבוצה נשארת בתוך הקבוצה, ואם היא אסוציאטיבית.</p>', layout="title")

REQ = [("i-1", "1. סגירות"), ("i-2", "2. אסוציאטיביות"), ("i-3", "3. איבר ניטרלי"), ("i-4", "4. הופכי לכל איבר")]
idea = Scene("idea", "הרעיון", [
    P("חבורה היא קבוצה עם פעולה. נסמן את הקבוצה $G$ ואת הפעולה בכוכבית.", do=show("i-g")),
    P("הפעולה לוקחת שני איברים ומחזירה תוצאה אחת.", do=show("i-op")),
    P("כדי שזו תהיה חבורה צריך לעמוד בארבע דרישות.", do=show("i-1", "i-2", "i-3", "i-4")),
    P("היום נטפל בשתי הראשונות: סגירות ואסוציאטיביות.", do=show("i-hl")),
    P("את הניטרלי ואת ההופכי נשאיר לשלב הבא.", hold=0.3),
], stage='<div class="gc-stack"><div id="i-g" class="gc-big h">$(G,*)$</div>'
         '<div id="i-op" class="gc-mid h">$a,b\\in G\\ \\Rightarrow\\ a*b$</div></div>',
   panel="".join(st.card(i, "plain" if i in ("i-3", "i-4") else "ex", t) for i, t in REQ)
         + st.card("i-hl", "rule", "🔑 היום: דרישות 1 ו-2"))

cl = Scene("closure", "סגירות", [
    P("סגירות פירושה: לכל שני איברים בקבוצה, גם התוצאה שייכת לקבוצה.", do=show("c-def")),
    P("בקבוצה סופית אפשר פשוט לבנות טבלת פעולה. הנה אחת, שלוש, חמש ושבע, עם כפל מודולו שמונה.",
      do=show("c-t1")),
    P("כל התוצאות בטבלה הן שוב אחת, שלוש, חמש או שבע. לכן יש סגירות.", do=show("c-v1")),
    P("עכשיו אחת, שתיים ושלוש עם כפל מודולו ארבע.", do=show("c-t2")),
    P("שתיים כפול שתיים זה ארבע, ומודולו ארבע זה אפס. ואפס לא בקבוצה.",
      do=show("t2-row-1", "t2-col-1", "t2-x-1-1")),
    P("מספיקה משבצת אחת כזו, והסגירות נופלת.", do=show("c-v2"), hold=0.3),
    P("ובקבוצה אינסופית? המספרים שנותנים שארית אחת בחלוקה בשלוש, עם חיבור: אחת ועוד אחת זה שתיים.",
      do=hide("t2-row-1", "t2-col-1") + show("c-odd")),
    P("דוגמה נגדית אחת מספיקה כדי להפריך סגירות.", do=show("c-r")),
], stage='<div class="gc-stack"><div class="gc-row">'
         f'<div id="c-t1" class="gc-stack h">{w.cayley("t1", S8, m8, sym="\\cdot", size=34)}'
         '<div class="gc-note">כפל מודולו 8</div></div>'
         f'<div id="c-t2" class="gc-stack h">{w.cayley("t2", T4, m4, sym="\\cdot", size=34)}'
         '<div class="gc-note">כפל מודולו 4</div></div></div>'
         '<div class="gc-row"><span id="c-v1" class="gc-chip h" style="border-color:#34d399;color:#34d399">סגורה ✓</span>'
         '<span id="c-v2" class="gc-chip h" style="border-color:#fb7185;color:#fb7185">לא סגורה ✗</span></div></div>',
   panel=st.card("c-def", "rule", "🔑 $a,b\\in G\\ \\Rightarrow\\ a*b\\in G$")
         + st.card("c-odd", "ex", "$x\\equiv1\\pmod3$ עם $+$: &nbsp;$1+1=2\\not\\equiv1$ ✗")
         + st.card("c-r", "rule", "🔑 להפריך: דוגמה נגדית אחת"))

asc = Scene("assoc", "אסוציאטיביות", [
    P("הדרישה השנייה: אסוציאטיביות. לא משנה איפה שמים את הסוגריים.", do=show("a-def")),
    P("כדי **להוכיח** אותה, מחשבים את שני האגפים על אותיות.", do=show("a-op1")),
    P("נגדיר $a*b=a+b+5$ על השלמים.", say="נגדיר: אֵיי כוכבית בִּי שווה אֵיי ועוד בִּי ועוד חמש, על השלמים."),
    P("באגף שמאל: קודם $a*b$, ואז עם $c$. יוצא $a+b+c+10$.", do=show("a-0"),
      say="באגף שמאל: קודם אֵיי כוכבית בִּי, ואז עם סִי. יוצא אֵיי ועוד בִּי ועוד סִי ועוד עשר."),
    P("ובאגף ימין: קודם $b*c$. יוצא בדיוק אותו ביטוי.", do=show("a-1")),
    P("השוויון נכון לכל שלושה מספרים, ולכן הפעולה אסוציאטיבית.", do=show("a-2"), hold=0.3),
    P("וכדי **להפריך**, מספיקה שלשה אחת. נגדיר $a*b=ab+1$.", do=show("a-op2"),
      say="וכדי להפריך, מספיקה שלשה אחת. נגדיר: אֵיי כוכבית בִּי שווה אֵיי בִּי ועוד אחת."),
    P("אחת כוכבית שתיים זה שלוש, ושלוש כוכבית שלוש זה עשר.", do=show("a-3")),
    P("מהצד השני, שתיים כוכבית שלוש זה שבע, ואחת כוכבית שבע זה שמונה.", do=show("a-4")),
    P("עשר שונה משמונה, ולכן הפעולה הזו לא אסוציאטיבית.", do=show("a-5")),
], stage='<div class="gc-stack">'
         '<div id="a-op1" class="gc-mid h">$a*b=a+b+5$</div>'
         + w.lines("a", ["$(a*b)*c=(a+b+5)+c+5=a+b+c+10$", "$a*(b*c)=a+(b+c+5)+5=a+b+c+10$",
                         "$(a*b)*c=a*(b*c)\\ \\checkmark$"], size=34)
         + '<div id="a-op2" class="gc-mid h">$a*b=ab+1$</div>'
         + w.lines("a", ["$(1*2)*3=3*3=10$", "$1*(2*3)=1*7=8$", "$10\\ne8\\ \\ \\times$"], size=34, start=3)
         + '</div>',
   panel=st.card("a-def", "rule", "🔑 $(a*b)*c=a*(b*c)$ לכל $a,b,c\\in G$")
         + st.card("a-r", "rule", "🔑 להוכיח: חישוב כללי על אותיות. להפריך: שלשה אחת"))
asc.phrases.append(P("זה הכלל: הוכחה דורשת אותיות, והפרכה דורשת דוגמה אחת.", do=show("a-r"), hold=0.4))

ex = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: על השלמים מגדירים $a\\otimes b=ab-a-b$.", do=show("x-op"),
      say="שאלה ממבחן: על השלמים מגדירים פעולה: אֵיי בִּי, פחות אֵיי, פחות בִּי."),
    P("בסעיף הראשון מראים שזו פעולה בינארית על השלמים, כלומר שיש סגירות."),
    P("מכפלה של שלמים היא שלם, וגם הפרש של שלמים. לכן התוצאה תמיד שלם.", do=show("x-c1")),
    P("שימו לב: לא מספיק לומר שהביטוי מוגדר. צריך לומר שהתוצאה **שייכת** לשלמים.", do=show("x-t1")),
    P("הסעיף השני: האם הפעולה אסוציאטיבית? נפתח את אגף שמאל.", do=show("x-0")),
    P("מציבים את $ab-a-b$ במקום הראשון, ופותחים סוגריים.", do=show("x-1"),
      say="מציבים את אֵיי בִּי פחות אֵיי פחות בִּי במקום הראשון, ופותחים סוגריים."),
    P("היזהרו כאן: המינוס שלפני הסוגריים הופך את כל הסימנים בפנים.", do=show("x-t2")),
    P("עכשיו אגף ימין: מציבים את $bc-b-c$ במקום השני.", do=show("x-2", "x-3"),
      say="עכשיו אגף ימין: מציבים את בִּי סִי פחות בִּי פחות סִי במקום השני."),
    P("משווים: בשמאל יש $+a-c$, ובימין $-a+c$. הביטויים שונים.", do=show("x-4"),
      say="משווים: בשמאל יש ועוד אֵיי ומינוס סִי, ובימין מינוס אֵיי ועוד סִי. הביטויים שונים."),
    P("וכדי לסגור את זה, דוגמה מספרית: $a=1$, ו-$b=c=0$.", do=show("x-5"),
      say="וכדי לסגור את זה, דוגמה מספרית: אֵיי שווה אחת, ובִּי וסִי שווים אפס."),
    P("בשמאל יוצא אחת, ובימין מינוס אחת. לכן הפעולה **אינה** אסוציאטיבית.", do=show("x-6", "x-ans"), hold=0.5),
], stage='<div class="gc-stack"><div id="x-op" class="gc-mid h">$a\\otimes b=ab-a-b$</div>'
         + w.lines("x", ["$(a\\otimes b)\\otimes c=(ab-a-b)c-(ab-a-b)-c$",
                         "$=abc-ac-bc-ab+a+b-c$",
                         "$a\\otimes(b\\otimes c)=a(bc-b-c)-a-(bc-b-c)$",
                         "$=abc-ab-ac-a-bc+b+c$",
                         "$+a-c\\ \\ \\ne\\ \\ -a+c$",
                         "$a=1,\\ b=c=0:$",
                         "$(1\\otimes0)\\otimes0=1,\\quad 1\\otimes(0\\otimes0)=-1$"], size=32)
         + '</div>',
   panel=w.ctx_stem("25B-B-Q3a/b", "לכל $a,b\\in\\mathbb{Z}$ נגדיר $a\\otimes b=ab-a-b$.",
                    '<div>א.1. הראו כי $\\otimes$ היא פעולה בינארית על $\\mathbb{Z}$.</div>'
                    '<div>א.2. האם הפעולה אסוציאטיבית?</div>')
         + st.card("x-c1", "ex", "$ab-a-b\\in\\mathbb{Z}$ לכל $a,b\\in\\mathbb{Z}$ ✓")
         + st.card("x-t1", "trap", "⚠️ לא רק מוגדר: התוצאה <b>שייכת</b> לקבוצה")
         + st.card("x-t2", "trap", "⚠️ $-(ab-a-b)=-ab+a+b$")
         + w.chip("x-ans", "לא אסוציאטיבית", 2))

recap = Scene("recap", "סיכום", [
    P("לסיכום: סגירות פירושה שהתוצאה נשארת בקבוצה. בקבוצה סופית בודקים בטבלה.", do=show("r-1")),
    P("להפריך סגירות או אסוציאטיביות: מספיקה דוגמה נגדית אחת.", do=show("r-2")),
    P("להוכיח אסוציאטיביות: מחשבים את שני האגפים על אותיות, ופותחים סוגריים בזהירות.", do=show("r-3")),
    P("בשלב הבא: איבר ניטרלי והופכי. נתראה שם.", do=show("r-4"), hold=0.6),
], stage='<div class="gc-stack"><div class="gc-big">$(a*b)*c\\overset{?}{=}a*(b*c)$</div></div>',
   panel=st.card("r-1", "rule", "🔑 סגירות: $a*b\\in G$")
         + st.card("r-2", "rule", "🔑 להפריך: דוגמה אחת")
         + st.card("r-3", "rule", "🔑 להוכיח: אותיות, שני האגפים")
         + st.card("r-4", "plain", "הבא: ניטרלי והופכי"))

VIDEO = Video("G01", "groups_crt", "סגירות ואסוציאטיביות", [title, idea, cl, asc, ex, recap],
              bank={"25B-B-Q3a": None, "25B-B-Q3b": None})
