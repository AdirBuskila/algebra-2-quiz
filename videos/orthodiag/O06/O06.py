# -*- coding: utf-8 -*-
"""O06 · המלכודת: חיובית מול חיובית לחלוטין — video script (build: tools/video/vid.py O06).

Source: courses/orthodiag/C06.js (lesson + goal). Exam part: an ORIGINAL exam-style question (bank={}):
(a,2;2,a-3) has eigenvalues a+1 and a-4; positive for a >= 4, strictly for a > 4, negative for a <= -1, strictly for
a < -1, none of them in between. The bank part first used here, 23B-A-Q3a ((1,0,2a;0,4-a^2,0;2a,0,1)), was dropped on
purpose: an isolated middle row plus a corner block with eigenvalues 1±2a is a near-twin of the boss item 23A-A-Q3a
((a,0,1;0,2a,0;1,0,a)); its own twin 26B-A-Q3a likewise.
Avoided on purpose: the C06 quiz matrices ((1,1;1,1), the zero matrix, I, (2,a;a,2), (a,0;0,4)), the C08 quiz
(3,a;a,3) and the boss parts. The classification examples are new 2x2 matrices. Every eigenvalue, every verdict
(through w_orthodiag.classify, the course convention) and every interval is asserted with sympy.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_orthodiag as w
from w_orthodiag import S, R

# ---------------------------------------------------------------- 2x2 examples
M1 = S([[1, 2], [2, 4]])
M2 = S([[-3, 1], [1, -3]])
M3 = S([[2, 3], [3, 2]])
assert sorted(M1.eigenvals(multiple=True)) == [0, 5]
assert sorted(M2.eigenvals(multiple=True)) == [-4, -2]
assert sorted(M3.eigenvals(multiple=True)) == [-1, 5]
assert w.classify(M1) == dict(pos=True, spos=False, neg=False, sneg=False)
assert w.classify(M2) == dict(pos=False, spos=False, neg=True, sneg=True)
assert w.classify(M3) == dict(pos=False, spos=False, neg=False, sneg=False)
# M1: the eigenvector of 0 is a nonzero x with x^T A x = 0, so "strictly" fails
z = S([2, -1])
w.eig_pairs(M1, [(0, z)])
assert z.dot(M1 * z) == 0
# the zero matrix and I (only mentioned in words: one matrix can be in two classes)
assert w.classify(sp.zeros(2, 2)) == dict(pos=True, spos=False, neg=True, sneg=False)

# why eigenvalues decide: x^T A x = sum lambda_i y_i^2 with y = Q^T x (checked on M3)
Q3, D3 = w.orth_diag(M3, [(5, [1, 1]), (-1, [1, -1])])
xs = S(sp.symbols("p q"))
y = Q3.T * xs
assert sp.expand((xs.T * M3 * xs)[0] - (5 * y[0]**2 - y[1]**2)) == 0

# ---------------------------------------------------------------- exam-style question (original)
a = sp.symbols("a", real=True)
lam = sp.symbols("lambda")
A = S([[a, 2], [2, a - 3]])
assert A == A.T
assert A.trace() == 2 * a - 3 and sp.expand(A.det()) == a**2 - 3 * a - 4 == sp.expand((a - 4) * (a + 1))
cp = sp.expand((A - lam * sp.eye(2)).det())
assert cp == sp.expand(lam**2 - (2 * a - 3) * lam + a**2 - 3 * a - 4)
assert sp.expand((2 * a - 3)**2 - 4 * (a**2 - 3 * a - 4)) == 25
assert sp.expand(cp - (lam - (a + 1)) * (lam - (a - 4))) == 0
EV = [a + 1, a - 4]
I = sp.Interval
solve = lambda conds: sp.Intersection(*[sp.solveset(c, a, sp.S.Reals) for c in conds])
POS, SPOS = solve([e >= 0 for e in EV]), solve([e > 0 for e in EV])
NEG, SNEG = solve([e <= 0 for e in EV]), solve([e < 0 for e in EV])
assert POS == I(4, sp.oo) and SPOS == I.open(4, sp.oo)
assert NEG == I(-sp.oo, -1) and SNEG == I.open(-sp.oo, -1)
for val, f in ((4, dict(pos=True, spos=False, neg=False, sneg=False)),
               (-1, dict(pos=False, spos=False, neg=True, sneg=False)),
               (5, dict(pos=True, spos=True, neg=False, sneg=False)),
               (-2, dict(pos=False, spos=False, neg=True, sneg=True)),
               (0, dict(pos=False, spos=False, neg=False, sneg=False)),
               (3, dict(pos=False, spos=False, neg=False, sneg=False))):
    assert w.classify(A.subs(a, val)) == f, val
assert sorted(A.subs(a, 4).eigenvals(multiple=True)) == [0, 5]
assert sorted(A.subs(a, -1).eigenvals(multiple=True)) == [-5, 0]

NL = w.numline("nl", -3, 6, [(-1, "−1"), (0, "0"), (4, "4")], [
    ("e0", "a+1 ≥ 0", [(-1, None, True, None, 0)]),
    ("e1", "a−4 ≥ 0", [(4, None, True, None, 0)]),
    ("pos", "חיובית", [(4, None, True, None, 1)]),
    ("spos", "חיובית לחלוטין", [(4, None, False, None, 1)]),
    ("neg", "שלילית", [(None, -1, None, True, 3)]),
    ("sneg", "שלילית לחלוטין", [(None, -1, None, False, 3)]),
    ("none", "אף אחת", [(-1, 4, False, False, 2)]),
], w=1000, rh=48)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נלמד את המלכודת הכי נפוצה בשאלות הגדרה חיובית."),
    P("בקורס שלנו, מוגדרת חיובית ומוגדרת חיובית לחלוטין הן שני דברים שונים."),
    P("נראה איך מסווגים לפי ערכים עצמיים, ונפתור שאלה ממבחן.", hold=0.4),
], stage='<div class="kicker">O06 · לכסון אורתוגונלי והגדרה חיובית</div><h1>המלכודת: חיובית מול חיובית לחלוטין</h1>'
         '<p>לסווג מטריצה סימטרית לפי הערכים העצמיים בהתאם להסכמה של הקורס: חיובית פירושה $\\ge0$, '
         'וחיובית לחלוטין פירושה $>0$.</p>', layout="title")

conv = Scene("conv", "ההסכמה של הקורס", [
    P("שימו לב, זה שונה מהרבה ספרים: בקורס שלנו, מוגדרת חיובית פירושה שהתבנית $x^TAx$ גדולה או שווה לאפס לכל $x$.", do=show("t-0-0", "t-0-1", "t-0-2")),
    P("ומוגדרת חיובית לחלוטין פירושה שהיא גדולה ממש מאפס לכל $x$ שונה מאפס. כך גם בדף הנוסחאות.", do=show("t-1-0", "t-1-1", "t-1-2")),
    P("ובאותו אופן לשלילית: קטנה או שווה, ולחלוטין: קטנה ממש.",
      do=show("t-2-0", "t-2-1", "t-2-2", "t-3-0", "t-3-1", "t-3-2")),
    P("ואם יש ערך עצמי חיובי וגם שלילי, המטריצה אף אחת מהן.", do=show("t-4-0", "t-4-1", "t-4-2")),
    P("למה הערכים העצמיים מכריעים? כי אחרי לכסון, התבנית היא סכום של ערכים עצמיים כפול ריבועים.", do=show("c-0")),
    P("אם כולם לא שליליים, הסכום לא שלילי. ואם אחד מהם אפס, הווקטור העצמי שלו נותן תבנית אפס, בלי להיות אפס.",
      do=show("c-1")),
    P("ולכן ערך עצמי אפס מוציא את ״לחלוטין״, אבל אם כל השאר לא שליליים, המטריצה עדיין חיובית.", do=show("c-r"), hold=0.4),
], stage=w.table("t", ["", "$x^TAx$ לכל $x\\ne0$", "ערכים עצמיים"],
                 [["חיובית", "$\\ge0$", "כולם $\\ge0$"],
                  ["חיובית לחלוטין", "$>0$", "כולם $>0$"],
                  ["שלילית", "$\\le0$", "כולם $\\le0$"],
                  ["שלילית לחלוטין", "$<0$", "כולם $<0$"],
                  ["אף אחת", "גם $+$ וגם $-$", "גם $+$ וגם $-$"]], size=32)
         + w.lines("c", ["$x^TAx=\\lambda_1y_1^2+\\lambda_2y_2^2+\\dots,\\quad y=Q^Tx$",
                         "$\\lambda_i=0:\\ x=v_i\\ne0,\\ \\ x^TAx=0$"], size=34),
   panel=st.card("c-r", "rule", "🔑 ערך עצמי $0$ והשאר $\\ge0$: חיובית כן, לחלוטין לא"))

ex = Scene("ex", "שלוש דוגמאות", [
    P("שלוש דוגמאות. הראשונה: אחת, שתיים, שתיים, ארבע. עקבה חמש, דטרמיננטה אפס, ולכן הערכים חמש ואפס.",
      do=show("m1", "v1")),
    P("כולם גדולים או שווים לאפס, אז היא חיובית. אבל יש אפס, אז לא לחלוטין.", do=show("k1")),
    P("והווקטור שתיים, מינוס אחת מראה את זה: הוא לא אפס, והתבנית שלו יוצאת אפס.", do=show("z1")),
    P("השנייה: מינוס שלוש, אחת, אחת, מינוס שלוש. הערכים מינוס שתיים ומינוס ארבע.", do=show("m2", "v2")),
    P("כולם שליליים ממש, אז שלילית לחלוטין. וגם שלילית: ״לחלוטין״ גורר את הגרסה הרגילה.", do=show("k2")),
    P("השלישית: שתיים, שלוש, שלוש, שתיים. הערכים חמש ומינוס אחת. סימנים מעורבים: אף אחת מהן.",
      do=show("m3", "v3", "k3"), hold=0.4),
], stage='<div class="od-row" style="gap:46px;align-items:flex-start">'
         + "".join(f'<div class="od-stack" style="gap:14px;width:300px">{w.mat(m, M, "", hidden=True, size=36)}'
                   f'<div id="{v}" class="od-mid h" style="font-size:32px">$\\lambda={lam}$</div>'
                   f'{w.chip(k, txt, col)}{extra}</div>'
                   for m, M, v, lam, k, txt, col, extra in (
                       ("m1", M1, "v1", "5,\\ 0", "k1", "חיובית, לא לחלוטין", 0,
                        '<div id="z1" class="od-note h">$x=(2,{-1}):\\ x^TAx=0$</div>'),
                       ("m2", M2, "v2", "{-2},\\ {-4}", "k2", "שלילית לחלוטין", 1, ""),
                       ("m3", M3, "v3", "5,\\ {-1}", "k3", "אף אחת", 2, "")))
         + '</div>',
   layout="full")

exam = Scene("exam", "שאלה בסגנון מבחן", [
    P("שאלה בסגנון מבחן: עבור אילו ערכי $a$ המטריצה הזו חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?",
      say="שאלה בסגנון מבחן: עבור אילו ערכי אֵיי המטריצה הזו חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?",
      do=show("x")),
    P("היא סימטרית לכל $a$. העקבה פעמיים $a$ פחות שלוש, והדטרמיננטה $a$ בריבוע, פחות שלוש $a$, פחות ארבע.",
      say="היא סימטרית לכל אֵיי. העקבה פעמיים אֵיי פחות שלוש, והדטרמיננטה אֵיי בריבוע, פחות שלוש אֵיי, פחות ארבע.",
      do=show("q-0")),
    P("בנוסחת השורשים הדיסקרימיננטה יוצאת עשרים וחמש, קבוע. ולכן הערכים העצמיים הם $a+1$ ו-$a-4$.",
      say="בנוסחת השורשים הדיסקרימיננטה יוצאת עשרים וחמש, קבוע. ולכן הערכים העצמיים הם אֵיי ועוד אחת, ואֵיי פחות ארבע.",
      do=show("q-1")),
    P("הראשון לא שלילי ממינוס אחת והלאה. השני, מארבע והלאה.", do=show("nl-e0", "nl-e1")),
    P("חיובית: שניהם יחד, כלומר $a$ גדול או שווה לארבע, **כולל** ארבע.",
      say="חיובית: שניהם יחד, כלומר אֵיי גדול או שווה לארבע, כולל ארבע.", do=show("nl-pos")),
    P("ב-$a$ שווה ארבע הערכים חמש ואפס. ערך עצמי מתאפס, ולכן ״לחלוטין״ רק כש-$a$ גדול ממש מארבע.",
      say="באֵיי שווה ארבע הערכים חמש ואפס. ערך עצמי מתאפס, ולכן לחלוטין רק כשאֵיי גדול ממש מארבע.",
      do=show("q-2", "nl-spos")),
    P("שלילית: שניהם קטנים או שווים לאפס, כלומר $a$ קטן או שווה למינוס אחת.",
      say="שלילית: שניהם קטנים או שווים לאפס, כלומר אֵיי קטן או שווה למינוס אחת.", do=show("nl-neg")),
    P("וב-$a$ שווה מינוס אחת הערכים אפס ומינוס חמש. שוב ערך עצמי מתאפס, אז שלילית לחלוטין רק משמאל למינוס אחת.",
      say="ובאֵיי שווה מינוס אחת הערכים אפס ומינוס חמש. שוב ערך עצמי מתאפס, אז שלילית לחלוטין רק משמאל למינוס אחת.",
      do=show("q-3", "nl-sneg", "x-t")),
    P("ובין מינוס אחת לארבע, ערך אחד חיובי והשני שלילי: אף אחת מהן.", do=show("nl-none"), hold=0.5),
], stage='<div class="od-stack" style="gap:12px"><div class="od-row" style="gap:36px">'
         + w.mat("x", A, "", hidden=True, size=34)
         + w.lines("q", ["$\\operatorname{tr}=2a-3,\\ \\det=a^2-3a-4$", "$\\lambda=a+1,\\ \\ a-4$"], size=32)
         + '</div>' + NL + '</div>',
   panel=w.qstem("בסגנון מבחן", "עבור אילו ערכי $a$ המטריצה חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?")
         + w.lines("q", ["$a=4:\\ \\lambda=5,\\ 0$", "$a={-1}:\\ \\lambda=0,\\ {-5}$"], size=30, start=2)
         + st.card("x-t", "trap", "⚠️ בשתי נקודות הקצה ערך עצמי $0$: חיובית (או שלילית), אבל לא לחלוטין"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: חיובית פירושה כל הערכים העצמיים גדולים או שווים לאפס. לחלוטין: גדולים ממש.", do=show("r-1")),
    P("ערך עצמי אפס תמיד מוציא את ״לחלוטין״.", do=show("r-2")),
    P("״לחלוטין״ גורר את הרגילה, ומטריצה אחת יכולה לעמוד בכמה הגדרות.", do=show("r-3")),
    P("ובשאלת פרמטר: בודקים את הקצוות, כי שם בדיוק ערך עצמי מתאפס. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="od-stack"><div class="od-big" style="font-size:44px">$x^TAx=\\sum\\lambda_i\\,y_i^2$</div></div>',
   panel=st.card("r-1", "rule", "🔑 חיובית: $\\lambda\\ge0$. לחלוטין: $\\lambda>0$")
         + st.card("r-2", "trap", "⚠️ $\\lambda=0$: אף פעם לא ״לחלוטין״")
         + st.card("r-3", "rule", "🔑 לחלוטין $\\Rightarrow$ רגילה")
         + st.card("r-4", "ex", "פרמטר: נקודות הקצה בנפרד"))

VIDEO = Video("O06", "orthodiag", "המלכודת: חיובית מול חיובית לחלוטין", [title, conv, ex, exam, recap],
              bank={})
