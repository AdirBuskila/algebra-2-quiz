# -*- coding: utf-8 -*-
"""O09 · מבחן גמר: לכסון והגדרה חיובית (boss walkthrough) — video script (build: tools/video/vid.py O09).

Source: courses/orthodiag/C09.js (boss: real exam parts). Three exam parts the boss quiz does NOT use (the gate refuses
quiz/boss ids), each a different skill of the course:
  25B-B-Q6a  orthogonal diagonalization of (3,2,0;2,2,2;0,2,1): eigenvalues 5, 2, -1, columns (2,2,1)/3, (-2,1,2)/3,
             (1,-2,2)/3 (the official Q, same order)
  26A-A-Q3a  the parameter matrix (1,x,0;x,2,x;0,x,1): the characteristic polynomial factored, eigenvalues 1 and
             (3±sqrt(8x^2+1))/2; positive for |x| <= 1, strictly for |x| < 1, never negative. Solved through the
             factored polynomial on purpose (not "guess an eigenvector, then trace/det"), because that shortcut would
             directly solve the boss item 24A-B-Q3a, whose matrix belongs to the same tridiagonal family.
  24A-A-Q2e  A positive and c > 0  =>  cI + A + A^2 strictly positive (a quadratic-form proof)
Avoided on purpose: the boss ids 23A-B-Q3a, 23B-B-Q4a, 23A-A-Q3a, 24A-B-Q3a, 23A-B-Q4b, 24A-B-Q2f and their twins
(25B-A-Q6b, 25A-C-Q5a, 25A-B-Q3a), and every part used in O01-O08. Note: 26A-A-Q3a is in the same family as the
boss 24A-B-Q3a (tridiagonal, parameter off the diagonal) but not the same matrix. Everything is asserted with sympy.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_orthodiag as w
from w_orthodiag import S, R

lam = sp.symbols("lambda")

# ---------------------------------------------------------------- part 1: 25B-B-Q6a
X1 = BANK["25B-B-Q6a"]
A = S([[3, 2, 0], [2, 2, 2], [0, 2, 1]])
assert "\\begin{pmatrix}3&2&0\\\\2&2&2\\\\0&2&1\\end{pmatrix}" in X1["question"]
p = sp.expand((A - lam * sp.eye(3)).det())
assert p == -(lam**3 - 6 * lam**2 + 3 * lam + 10)
assert (-1)**3 - 6 * (-1)**2 + 3 * (-1) + 10 == 0
assert sp.div(lam**3 - 6 * lam**2 + 3 * lam + 10, lam + 1) == (lam**2 - 7 * lam + 10, 0)
assert sp.factor(lam**2 - 7 * lam + 10) == (lam - 5) * (lam - 2)
assert A.trace() == 6 == 5 + 2 - 1 and A.det() == -10 == 5 * 2 * (-1)
assert A - 5 * sp.eye(3) == S([[-2, 2, 0], [2, -3, 2], [0, 2, -4]])
assert A - 2 * sp.eye(3) == S([[1, 2, 0], [2, 0, 2], [0, 2, -1]])
assert A + sp.eye(3) == S([[4, 2, 0], [2, 3, 2], [0, 2, 2]])
QA, DA = w.orth_diag(A, [(5, [2, 2, 1]), (2, [-2, 1, 2]), (-1, [1, -2, 2])])
assert QA == S([[2, -2, 1], [2, 1, -2], [1, 2, 2]]) / 3 and DA == sp.diag(5, 2, -1)

# ---------------------------------------------------------------- part 2: 26A-A-Q3a
X2 = BANK["26A-A-Q3a"]
x = sp.symbols("x", real=True)
B = S([[1, x, 0], [x, 2, x], [0, x, 1]])
assert "\\begin{pmatrix}1&x&0\\\\x&2&x\\\\0&x&1\\end{pmatrix}" in X2["question"]
# first-row expansion as shown on screen, then the factored characteristic polynomial and its roots
cp = sp.expand((B - lam * sp.eye(3)).det())
assert cp == sp.expand((1 - lam) * ((2 - lam) * (1 - lam) - x**2) - x**2 * (1 - lam))
assert cp == sp.expand((1 - lam) * (lam**2 - 3 * lam + 2 - 2 * x**2))
r = sp.sqrt(8 * x**2 + 1)
assert sp.expand((lam - (3 + r) / 2) * (lam - (3 - r) / 2)) == lam**2 - 3 * lam + 2 - 2 * x**2
assert sp.solveset((3 - r) / 2 >= 0, x, sp.S.Reals) == sp.Interval(-1, 1)
assert sp.solveset((3 - r) / 2 > 0, x, sp.S.Reals) == sp.Interval.open(-1, 1)
assert sp.solveset(8 * x**2 + 1 <= 9, x, sp.S.Reals) == sp.Interval(-1, 1)
for val, f in ((1, dict(pos=True, spos=False, neg=False, sneg=False)),
               (-1, dict(pos=True, spos=False, neg=False, sneg=False)),
               (0, dict(pos=True, spos=True, neg=False, sneg=False)),
               (R(1, 2), dict(pos=True, spos=True, neg=False, sneg=False)),
               (2, dict(pos=False, spos=False, neg=False, sneg=False))):
    assert w.classify(B.subs(x, val)) == f, val
assert sorted(B.subs(x, 1).eigenvals(multiple=True)) == [0, 1, 3]

NL = w.numline("nl", -2, 2, [(-1, "−1"), (0, "0"), (1, "1")], [
    ("pos", "חיובית", [(-1, 1, True, True, 1)]),
    ("spos", "חיובית לחלוטין", [(-1, 1, False, False, 1)]),
    ("none", "אף אחת", [(None, -1, None, False, 2), (1, None, False, None, 2)]),
], w=960, rh=50)

# ---------------------------------------------------------------- part 3: 24A-A-Q2e (identities for a general symmetric 3x3)
X3 = BANK["24A-A-Q2e"]
assert "cI+A+A^2" in X3["question"]
c = sp.symbols("c", positive=True)
g = sp.symbols("g0:6")
G = S([[g[0], g[1], g[2]], [g[1], g[3], g[4]], [g[2], g[4], g[5]]])
y = S(sp.symbols("y0:3"))
Mq = c * sp.eye(3) + G + G**2
assert Mq.T == Mq
assert sp.expand((y.T * Mq * y)[0] - (c * y.dot(y) + (y.T * G * y)[0] + (G * y).dot(G * y))) == 0
# the strict part: c * ||y||^2 > 0 for every y != 0 (c > 0)
assert c.is_positive and sp.expand(y.dot(y) - sum(t**2 for t in y)) == 0      # ||y||^2 = sum of squares, > 0 if y != 0

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("זה מבחן הגמר של הקורס: שלוש שאלות אמיתיות ממבחנים, כל אחת בנושא אחר."),
    P("לכסון אורתוגונלי מלא, שאלת פרמטר, והוכחה עם תבנית ריבועית. נפתור אותן יחד, צעד אחר צעד.", hold=0.4),
], stage='<div class="kicker">O09 · לכסון אורתוגונלי והגדרה חיובית</div><h1>מבחן גמר: לכסון והגדרה חיובית</h1>'
         '<p>שאלות אמיתיות מהמבחנים: לכסון אורתוגונלי, שאלת פרמטר והוכחה.</p>', layout="title")

d1 = Scene("d1", "שאלה 1: הערכים", [
    P("שאלה ראשונה: בצעו לכסון אורתוגונלי למטריצה הזו. אין שורה מבודדת, אז מפתחים דטרמיננטה.", do=show("a")),
    P("הפיתוח לפי השורה הראשונה נותן פולינום ממעלה שלוש.", do=show("p-0")),
    P("שורש שלם מחלק את עשר. מנסים מינוס אחת, והכול מתאפס.", do=show("p-1")),
    P("מחלקים, ונשאר גורם ריבועי שהשורשים שלו חמש ושתיים.", do=show("p-2")),
    P("בדיקה: חמש ועוד שתיים פחות אחת זה שש, כמו העקבה. והמכפלה מינוס עשר, כמו הדטרמיננטה.", do=show("p-3")),
    P("שלושה ערכים שונים. אז הווקטורים העצמיים ייצאו ניצבים מעצמם, ואין צורך בגרהם-שמידט.", do=show("p-r"),
      hold=0.4),
], stage='<div class="od-stack">' + w.mat("a", A, "A=", hidden=True, size=38)
         + w.lines("p", ["$\\det(A-\\lambda I)={-(\\lambda^3-6\\lambda^2+3\\lambda+10)}$",
                         "$\\lambda={-1}:\\ {-1}-6-3+10=0$",
                         "$\\lambda^2-7\\lambda+10=(\\lambda-5)(\\lambda-2)$",
                         "$5+2-1=6=\\operatorname{tr},\\quad 5\\cdot2\\cdot({-1})={-10}=\\det$"], size=32) + '</div>',
   panel=w.qstem(X1["id"], "בצעו לכסון אורתוגונלי למטריצה $A$.")
         + st.card("p-r", "rule", "🔑 ערכים שונים בסימטרית: וקטורים ניצבים אוטומטית"))

d2 = Scene("d2", "שאלה 1: הווקטורים", [
    P("עבור חמש: מהשורה הראשונה של $A$ פחות חמש $I$, $x$ שווה $y$. מהשלישית, $y$ שווה פעמיים $z$.",
      say="עבור חמש: מהשורה הראשונה של אֵיי פחות חמש כפול היחידה, אִקְס שווה וַואי. מהשלישית, וַואי שווה פעמיים זֶד.",
      do=show("t-0-0", "t-0-1")),
    P("הווקטור שתיים, שתיים, אחת.", hold=0.1),
    P("עבור שתיים: $x$ שווה מינוס פעמיים $y$, ו-$z$ שווה פעמיים $y$. הווקטור מינוס שתיים, אחת, שתיים.",
      say="עבור שתיים: אִקְס שווה מינוס פעמיים וַואי, וזֶד שווה פעמיים וַואי. הווקטור מינוס שתיים, אחת, שתיים.",
      do=show("t-1-0", "t-1-1")),
    P("עבור מינוס אחת: $y$ שווה מינוס פעמיים $x$, ו-$z$ שווה מינוס $y$. הווקטור אחת, מינוס שתיים, שתיים.",
      say="עבור מינוס אחת: וַואי שווה מינוס פעמיים אִקְס, וזֶד שווה מינוס וַואי. הווקטור אחת, מינוס שתיים, שתיים.",
      do=show("t-2-0", "t-2-1")),
    P("לכל השלושה אורך שלוש: שורש של ארבע ועוד ארבע ועוד אחת. מחלקים בשלוש.", do=show("t-0-2", "t-1-2", "t-2-2")),
    P("ובאותו סדר: חמש, שתיים, מינוס אחת על האלכסון, והעמודות של $Q$ בהתאם. בדיוק הפתרון הרשמי.",
      say="ובאותו סדר: חמש, שתיים, מינוס אחת על האלכסון, והעמודות של קְיוּ בהתאם. בדיוק הפתרון הרשמי.",
      do=show("q-ans"), hold=0.5),
], stage='<div class="od-stack">'
         + w.table("t", ["$\\lambda$", "וקטור", "מנורמל"],
                   [["$5$", "$(2,2,1)$", "$\\frac13(2,2,1)$"],
                    ["$2$", "$({-2},1,2)$", "$\\frac13({-2},1,2)$"],
                    ["${-1}$", "$(1,{-2},2)$", "$\\frac13(1,{-2},2)$"]], colors=[0, 1, 2], size=34) + '</div>',
   panel=st.card("q-ans", "ex", w.qd(QA, DA, size=30)))

pq = Scene("pq", "שאלה 2: פרמטר", [
    P("שאלה שנייה: עבור אילו ערכי $x$ המטריצה הזו חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?",
      say="שאלה שנייה: עבור אילו ערכי אִקְס המטריצה הזו חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?",
      do=show("b")),
    P("היא סימטרית לכל $x$. מפתחים את הדטרמיננטה לפי השורה הראשונה.",
      say="היא סימטרית לכל אִקְס. מפתחים את הדטרמיננטה לפי השורה הראשונה.", do=show("b-0")),
    P("אחרי כינוס, אחת פחות למדא יוצא גורם משותף, ונשאר גורם ריבועי.", do=show("b-1")),
    P("מהגורם הראשון: למדא שווה אחת. ומהגורם הריבועי, לפי נוסחת השורשים, שני ערכים עם שורש של שמונה $x$ בריבוע ועוד אחת.",
      say="מהגורם הראשון: למדא שווה אחת. ומהגורם הריבועי, לפי נוסחת השורשים, שני ערכים עם שורש של שמונה אִקְס בריבוע ועוד אחת.",
      do=show("b-2")),
    P("הערך עם הפלוס תמיד חיובי. הכול תלוי בערך עם המינוס: הוא לא שלילי כששורש של שמונה $x$ בריבוע ועוד אחת קטן או שווה לשלוש.",
      say="הערך עם הפלוס תמיד חיובי. הכול תלוי בערך עם המינוס: הוא לא שלילי כששורש של שמונה אִקְס בריבוע ועוד אחת קטן או שווה לשלוש.",
      do=show("b-3")),
    P("מעלים בריבוע: שמונה $x$ בריבוע ועוד אחת קטן או שווה לתשע, כלומר $x$ בריבוע קטן או שווה לאחת. חיובית בין מינוס אחת לאחת.",
      say="מעלים בריבוע: שמונה אִקְס בריבוע ועוד אחת קטן או שווה לתשע, כלומר אִקְס בריבוע קטן או שווה לאחת. חיובית בין מינוס אחת לאחת.",
      do=show("nl-pos")),
    P("בקצוות השורש שווה לשלוש, וערך עצמי מתאפס: אחת, שלוש ואפס. לכן לחלוטין רק בפנים.", do=show("b-4", "nl-spos")),
    P("שלילית אף פעם, כי הערך אחת תמיד שם. ומחוץ לקטע, אף אחת מהן.", do=show("nl-none", "b-t"), hold=0.5),
], stage='<div class="od-stack" style="gap:12px">'
         + w.mat("b", B, "", hidden=True, size=34)
         + w.lines("b", ["$\\det(B-\\lambda I)=(1-\\lambda)\\big[(2-\\lambda)(1-\\lambda)-x^2\\big]-x^2(1-\\lambda)$",
                         "$=(1-\\lambda)(\\lambda^2-3\\lambda+2-2x^2)$",
                         "$\\lambda=1,\\quad \\lambda=\\frac{3\\pm\\sqrt{8x^2+1}}{2}$",
                         "$\\frac{3-\\sqrt{8x^2+1}}{2}\\ge0\\iff 8x^2+1\\le9\\iff x^2\\le1$"], size=28)
         + NL + '</div>',
   panel=w.qstem(X2["id"], "עבור אילו ערכי $x$ המטריצה חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?")
         + w.lines("b", ["$x={\\pm1}:\\\\lambda=1,\\ 3,\\ 0$"], size=30, start=4)
         + st.card("b-t", "trap", "⚠️ חיובית: $|x|\\le1$. לחלוטין: $|x|<1$. שלילית: אף פעם"))

pf = Scene("pf", "שאלה 3: הוכחה", [
    P("שאלה שלישית: $A$ מוגדרת חיובית, ו-$c$ חיובי. הוכיחו ש-$cI+A+A^2$ חיובית לחלוטין.",
      say="שאלה שלישית: אֵיי מוגדרת חיובית, וסִי חיובי. הוכיחו שסִי כפול היחידה, ועוד אֵיי, ועוד אֵיי בריבוע, חיובית לחלוטין."),
    P("קודם סימטריה: כל אחד משלושת המחוברים סימטרי, ולכן גם הסכום.", do=show("f-0")),
    P("עכשיו ניקח וקטור $x$ **שונה מאפס**, ונפרק את התבנית לשלושה חלקים.",
      say="עכשיו ניקח וקטור אִקְס שונה מאפס, ונפרק את התבנית לשלושה חלקים.", do=show("f-1")),
    P("החלק הראשון: $c$ כפול הנורמה בריבוע. $c$ חיובי ו-$x$ לא אפס, ולכן הוא חיובי **ממש**.",
      say="החלק הראשון: סִי כפול הנורמה בריבוע. סִי חיובי ואִקְס לא אפס, ולכן הוא חיובי ממש.", do=show("f-2")),
    P("השני לא שלילי, כי $A$ מוגדרת חיובית. והשלישי הוא הנורמה של $Ax$ בריבוע, כי $A$ סימטרית.",
      say="השני לא שלילי, כי אֵיי מוגדרת חיובית. והשלישי הוא הנורמה של אֵיי אִקְס בריבוע, כי אֵיי סימטרית.", do=show("f-3")),
    P("חיובי ממש ועוד שני דברים לא שליליים: חיובי ממש. וזו בדיוק חיוביות לחלוטין.", do=show("f-4")),
    P("המלכודת: להסתפק בגדול או שווה. בלי האיבר עם $c$ אין ״לחלוטין״.",
      say="המלכודת: להסתפק בגדול או שווה. בלי האיבר עם סִי אין לחלוטין.", do=show("f-t"), hold=0.5),
], stage=w.lines("f", ["$(cI+A+A^2)^T=cI+A+A^2$",
                       "$x^T(cI+A+A^2)x=c\\,x^Tx+x^TAx+x^TA^TAx$",
                       "$c\\|x\\|^2>0$",
                       "$x^TAx\\ge0,\\qquad x^TA^TAx=\\|Ax\\|^2\\ge0$",
                       "$c\\|x\\|^2+x^TAx+\\|Ax\\|^2>0$"], size=38),
   panel=w.qstem(X3["id"], "תהי $A$ מוגדרת חיובית ו-$c>0$. הוכיחו כי $cI+A+A^2$ מוגדרת חיובית לחלוטין.")
         + st.card("f-t", "trap", "⚠️ ״לחלוטין״ דורש איבר חיובי <b>ממש</b>: $c\\|x\\|^2$ עם $x\\ne0$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום הקורס: מטריצה סימטרית ניתנת ללכסון אורתוגונלי, ו-$Q$ ו-$D$ נבנות באותו סדר.",
      say="לסיכום הקורס: מטריצה סימטרית ניתנת ללכסון אורתוגונלי, וקְיוּ ודִּי נבנות באותו סדר.", do=show("r-1")),
    P("בערך כפול בודקים ניצבות, ואם צריך גרהם-שמידט.", do=show("r-2")),
    P("חיובית פירושה כל הערכים העצמיים גדולים או שווים לאפס, ולחלוטין, גדולים ממש. ובודקים קצוות.", do=show("r-3")),
    P("ובהוכחות: מפרקים את התבנית הריבועית לחלקים שהסימן שלהם ידוע. בהצלחה במבחן!", do=show("r-4"), hold=0.8),
], stage='<div class="od-stack"><div class="od-big">$A=QDQ^T$</div>'
         '<div class="od-mid">$x^TAx=\\sum\\lambda_i\\,y_i^2$</div></div>',
   panel=st.card("r-1", "rule", "🔑 סימטרית $\\iff$ לכסינה אורתוגונלית, סדר תואם")
         + st.card("r-2", "trap", "⚠️ ערך כפול: גרהם-שמידט אם צריך")
         + st.card("r-3", "rule", "🔑 חיובית $\\ge0$, לחלוטין $>0$, קצוות בנפרד")
         + st.card("r-4", "ex", "הוכחות: פירוק התבנית הריבועית"))

VIDEO = Video("O09", "orthodiag", "מבחן גמר: לכסון והגדרה חיובית", [title, d1, d2, pq, pf, recap],
              bank={"25B-B-Q6a": None, "26A-A-Q3a": None, "24A-A-Q2e": None})
