# -*- coding: utf-8 -*-
"""O08 · שאלות עם פרמטר — video script (build: tools/video/vid.py O08).

Source: courses/orthodiag/C08.js (lesson + goal). Exam anchor: 25A-A-Q3a ((1,w,w;w,1,w;w,w,1): eigenvalues 1+2w once
and 1-w twice; positive for -1/2 <= w <= 1, strictly inside, never negative), which no guided quiz uses.
Avoided on purpose: the C08 quiz/lesson matrices ((3,a;a,3), (1,0,a;0,2,0;a,b,1), (a,0,2;0,a,0;2,0,a), the
eigenvalue lists a^2+1, 2a^2, 3 and (2,a,0;a,2,0;0,0,a+1)), the boss parts 23A-A-Q3a / 24A-B-Q3a and their twins.
The symmetry example is a new matrix (a,2,0;a^2-2,a,0;0,0,a-1). Every eigenvalue, verdict and interval is asserted
with sympy (the course classifier w_orthodiag.classify at every endpoint).
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_orthodiag as w
from w_orthodiag import S, R

# ---------------------------------------------------------------- symmetry example
a = sp.symbols("a", real=True)
M = S([[a, 2, 0], [a**2 - 2, a, 0], [0, 0, a - 1]])
assert set(sp.solve(sp.Eq(M[0, 1], M[1, 0]), a)) == {-2, 2}
M2, Mm2 = M.subs(a, 2), M.subs(a, -2)
assert M2 == M2.T and Mm2 == Mm2.T
assert sorted(M2.eigenvals(multiple=True)) == [0, 1, 4]
assert sorted(Mm2.eigenvals(multiple=True)) == [-4, -3, 0]
assert w.classify(M2) == dict(pos=True, spos=False, neg=False, sneg=False)
assert w.classify(Mm2) == dict(pos=False, spos=False, neg=True, sneg=False)
assert M.subs(a, 1) != M.subs(a, 1).T                                  # any other a: not symmetric

# ---------------------------------------------------------------- exam 25A-A-Q3a
X = BANK["25A-A-Q3a"]
v = sp.symbols("w", real=True)
A = S([[1, v, v], [v, 1, v], [v, v, 1]])
assert "\\begin{pmatrix}1&w&w\\\\w&1&w\\\\w&w&1\\end{pmatrix}" in X["question"]
J = sp.ones(3, 3)
assert A == (1 - v) * sp.eye(3) + v * J
w.eig_pairs(J, [(3, [1, 1, 1]), (0, [1, -1, 0]), (0, [1, 0, -1])])
w.eig_pairs(A, [(1 + 2 * v, [1, 1, 1]), (1 - v, [1, -1, 0]), (1 - v, [1, 0, -1])])
assert sorted(map(sp.expand, A.eigenvals(multiple=True)), key=str) == sorted([1 + 2 * v, 1 - v, 1 - v], key=str)
assert sp.expand((1 + 2 * v) + 2 * (1 - v)) == 3 == A.trace()
EV = [1 + 2 * v, 1 - v]
I = sp.Interval
assert sp.solveset(EV[0] >= 0, v, sp.S.Reals) == I(-R(1, 2), sp.oo)
assert sp.solveset(EV[1] >= 0, v, sp.S.Reals) == I(-sp.oo, 1)
POS = sp.Intersection(*[sp.solveset(e >= 0, v, sp.S.Reals) for e in EV])
SPOS = sp.Intersection(*[sp.solveset(e > 0, v, sp.S.Reals) for e in EV])
NEG = sp.Intersection(*[sp.solveset(e <= 0, v, sp.S.Reals) for e in EV])
assert POS == I(-R(1, 2), 1) and SPOS == I.open(-R(1, 2), 1) and NEG == sp.S.EmptySet
for val, f in ((1, dict(pos=True, spos=False, neg=False, sneg=False)),
               (-R(1, 2), dict(pos=True, spos=False, neg=False, sneg=False)),
               (0, dict(pos=True, spos=True, neg=False, sneg=False)),
               (2, dict(pos=False, spos=False, neg=False, sneg=False)),
               (-1, dict(pos=False, spos=False, neg=False, sneg=False))):
    assert w.classify(A.subs(v, val)) == f, val
assert sorted(A.subs(v, 1).eigenvals(multiple=True)) == [0, 0, 3]
assert sorted(A.subs(v, -R(1, 2)).eigenvals(multiple=True)) == [0, R(3, 2), R(3, 2)]
assert sorted(A.subs(v, 2).eigenvals(multiple=True)) == [-1, -1, 5]

NL = w.numline("nl", -R(3, 2), 2, [(-R(1, 2), "−½"), (0, "0"), (1, "1")], [
    ("e0", "1+2w ≥ 0", [(-R(1, 2), None, True, None, 0)]),
    ("e1", "1−w ≥ 0", [(None, 1, None, True, 0)]),
    ("pos", "חיובית", [(-R(1, 2), 1, True, True, 1)]),
    ("spos", "חיובית לחלוטין", [(-R(1, 2), 1, False, False, 1)]),
    ("none", "אף אחת", [(None, -R(1, 2), None, False, 2), (1, None, False, None, 2)]),
], w=1000)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נפתור שאלת פרמטר מלאה, מהסוג שמופיע כמעט בכל מבחן."),
    P("סימטריה, ערכים עצמיים כפונקציה של הפרמטר, אי שוויונות, ונקודות קצה.", hold=0.4),
], stage='<div class="kicker">O08 · לכסון אורתוגונלי והגדרה חיובית</div><h1>שאלות עם פרמטר</h1>'
         '<p>לפתור שאלת פרמטר מלאה: סימטריה, ערכים עצמיים כפונקציה של הפרמטר, אי-שוויונות ונקודות קצה.</p>',
   layout="title")

recipe = Scene("recipe", "המתכון", [
    P("השאלה תמיד נשמעת אותו דבר: עבור אילו ערכי הפרמטר המטריצה חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת."),
    P("צעד ראשון: סימטריה. אם הפרמטר יושב מחוץ לאלכסון, מוצאים מתי שני הצדדים שווים.", do=show("c-1")),
    P("צעד שני: ערכים עצמיים כפונקציה של הפרמטר. מחפשים שורה מבודדת או מבנה שמקצר את החישוב.", do=show("c-2")),
    P("צעד שלישי: לכל ערך עצמי, מתי הוא גדול או שווה לאפס, ומתי גדול ממש.", do=show("c-3")),
    P("צעד רביעי: נקודות הקצה. שם ערך עצמי מתאפס, ולכן ״לחלוטין״ נופל.", do=show("c-4")),
    P("וכל מה שנשאר בחוץ הוא אף אחת מהן.", do=show("c-5"), hold=0.4),
], stage='<div class="od-stack" style="gap:14px">'
         + "".join(st.card(f"c-{k}", "ex", t) for k, t in (
             (1, "① סימטריה: $a_{ij}=a_{ji}$, אחרת לא מוגדרת"),
             (2, "② ערכים עצמיים כפונקציה של הפרמטר"),
             (3, "③ $\\ge0$ לחיובית, $>0$ לחיובית לחלוטין (וכך גם לשלילית)"),
             (4, "④ נקודות הקצה: ערך עצמי $0$"),
             (5, "⑤ השאר: אף אחת מהן"))) + '</div>', layout="full")

symm = Scene("symm", "סימטריה קודם", [
    P("דוגמה שבה הצעד הראשון עושה כמעט את כל העבודה.", do=show("m")),
    P("מעל האלכסון יש שתיים, ומתחתיו $a$ בריבוע פחות שתיים.", say="מעל האלכסון יש שתיים, ומתחתיו אֵיי בריבוע פחות שתיים.",
      do=show("m-c-0-1", "m-c-1-0")),
    P("הם שווים רק כש-$a$ בריבוע שווה ארבע, כלומר $a$ שווה שתיים או מינוס שתיים.",
      say="הם שווים רק כשאֵיי בריבוע שווה ארבע, כלומר אֵיי שווה שתיים או מינוס שתיים.", do=show("s-0")),
    P("לכל ערך אחר המטריצה לא סימטרית, ולכן לא מוגדרת. נשארו רק שתי בדיקות.", do=show("s-1")),
    P("ב-$a$ שווה שתיים: הבלוק נותן $a$ ועוד או פחות שתיים, כלומר ארבע ואפס, והפינה נותנת אחת. חיובית, לא לחלוטין.",
      say="באֵיי שווה שתיים: הבלוק נותן אֵיי ועוד או פחות שתיים, כלומר ארבע ואפס, והפינה נותנת אחת. חיובית, לא לחלוטין.",
      do=hide("m-c-0-1", "m-c-1-0") + show("s-2")),
    P("ב-$a$ שווה מינוס שתיים: אפס, מינוס ארבע, ומינוס שלוש. שלילית, לא לחלוטין.",
      say="באֵיי שווה מינוס שתיים: אפס, מינוס ארבע, ומינוס שלוש. שלילית, לא לחלוטין.", do=show("s-3"), hold=0.4),
], stage='<div class="od-stack">' + w.mat("m", M, "", hidden=True, size=40)
         + w.lines("s", ["$a^2-2=2\\iff a={\\pm2}$", "$a\\ne{\\pm2}$: לא סימטרית",
                         "$a=2:\\ \\lambda=4,\\ 0,\\ 1$ &nbsp; חיובית", "$a={-2}:\\ \\lambda=0,\\ {-4},\\ {-3}$ &nbsp; שלילית"],
                   size=34) + '</div>', layout="full")

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: אחת על האלכסון, ו-$w$ בכל שאר המקומות. עבור אילו $w$ היא חיובית, לחלוטין, שלילית, או אף אחת?",
      say="שאלה ממבחן: אחת על האלכסון, ודַאבְּלְיוּ בכל שאר המקומות. עבור אילו דַאבְּלְיוּ היא חיובית, לחלוטין, שלילית, או אף אחת?",
      do=show("x")),
    P("היא סימטרית לכל $w$. ובמקום לפתח דטרמיננטה, נשים לב למבנה.",
      say="היא סימטרית לכל דַאבְּלְיוּ. ובמקום לפתח דטרמיננטה, נשים לב למבנה."),
    P("היא $1-w$ כפול היחידה, ועוד $w$ כפול מטריצת האחדות.",
      say="היא, בסוגריים, אחת פחות דַאבְּלְיוּ, כפול היחידה. ועוד דַאבְּלְיוּ כפול מטריצת האחדות.", do=show("e-0")),
    P("מטריצת האחדות שולחת את אחת, אחת, אחת לפי שלוש, וכל וקטור שסכומו אפס לאפס.", do=show("e-1")),
    P("ואם $J$ כופלת וקטור במספר מיו, אז $A$ כופלת אותו באחת פחות $w$, ועוד $w$ כפול מיו. אותם וקטורים עצמיים.",
      say="ואם מטריצת האחדות כופלת וקטור במספר מְיוּ, אז אֵיי כופלת אותו בסוגריים אחת פחות דַאבְּלְיוּ ועוד דַאבְּלְיוּ כפול מְיוּ. אותם וקטורים עצמיים.",
      do=show("e-3")),
    P("לכן הערכים: אחת ועוד פעמיים $w$, פעם אחת. ואחת פחות $w$, פעמיים. בדיקה: הסכום שלוש, כמו העקבה.",
      say="לכן הערכים: אחת ועוד פעמיים דַאבְּלְיוּ, פעם אחת. ואחת פחות דַאבְּלְיוּ, פעמיים. בדיקה: הסכום שלוש, כמו העקבה.",
      do=show("e-2")),
    P("הראשון לא שלילי ממינוס חצי והלאה. השני, עד אחת.", do=show("nl-e0", "nl-e1")),
    P("חיובית: שניהם יחד, מינוס חצי עד אחת, כולל הקצוות.", do=show("nl-pos")),
    P("בקצה אחת הערכים שלוש, אפס, אפס. ובמינוס חצי: אפס, ופעמיים שלוש חצאים. לכן לחלוטין רק בפנים.",
      do=show("y-1", "nl-spos")),
    P("שלילית? צריך $w$ קטן או שווה למינוס חצי, וגם גדול או שווה לאחת. אין כזה.",
      say="שלילית? צריך דַאבְּלְיוּ קטן או שווה למינוס חצי, וגם גדול או שווה לאחת. אין כזה.", do=show("y-2")),
    P("והמלכודת: ב-$w$ גדול מאחת יש ערך עצמי שלילי כפול. אבל אחת ועוד פעמיים $w$ חיובי, אז זו אף אחת, לא שלילית.",
      say="והמלכודת: בדַאבְּלְיוּ גדול מאחת יש ערך עצמי שלילי כפול. אבל אחת ועוד פעמיים דַאבְּלְיוּ חיובי, אז זו אף אחת, לא שלילית.",
      do=show("nl-none", "x-t")),
    P("למשל ב-$w$ שווה שתיים הערכים הם חמש, מינוס אחת, ומינוס אחת. סימנים מעורבים.",
      say="למשל בדַאבְּלְיוּ שווה שתיים הערכים הם חמש, מינוס אחת, ומינוס אחת. סימנים מעורבים.", hold=0.5),
], stage='<div class="od-stack" style="gap:14px"><div class="od-row" style="gap:30px">'
         + w.mat("x", A, "", hidden=True, size=34)
         + w.lines("e", ["$A=(1-w)\\,I+w\\,J$", "$J(1,1,1)=3(1,1,1)$",
                         "$\\lambda=1+2w,\\ 1-w,\\ 1-w$", "$Jv=\\mu v\\ \\Rightarrow\\ Av=(1-w+w\\mu)\\,v$"],
                   size=30) + '</div>' + NL + '</div>',
   panel=w.qstem(X["id"], "עבור אילו ערכי $w$ המטריצה חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?")
         + w.lines("y", ["$w=1:\\ 3,0,0\\qquad w={-\\frac12}:\\ 0,\\frac32,\\frac32$",
                         "שלילית: $w\\le{-\\frac12}$ וגם $w\\ge1$ ✗"], size=30, start=1)
         + st.card("x-t", "trap", "⚠️ ערך עצמי שלילי לבד לא עושה שלילית: צריך את <b>כולם</b>"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: קודם סימטריה. לפעמים היא לבד משאירה רק ערך או שניים לבדוק.", do=show("r-1")),
    P("אחר כך ערכים עצמיים כפונקציה של הפרמטר, בקיצור הכי טוב שיש: שורה מבודדת, או מבנה כמו מטריצת האחדות.", do=show("r-2")),
    P("גדול או שווה לחיובית, ולחיובית לחלוטין: גדול ממש. ונקודות הקצה בנפרד.", do=show("r-3")),
    P("ושלילית רק כשכל הערכים העצמיים לא חיוביים. נתראה במבחן הגמר.", do=show("r-4"), hold=0.6),
], stage='<div class="od-stack"><div class="od-big" style="font-size:44px">$\\lambda_i(w)\\ \\ge 0\\ \\ /\\ \\ >0$</div></div>',
   panel=st.card("r-1", "rule", "🔑 סימטריה לפני הכול")
         + st.card("r-2", "rule", "🔑 ערכים עצמיים כפונקציה של הפרמטר")
         + st.card("r-3", "trap", "⚠️ נקודות קצה: ערך עצמי $0$, ״לחלוטין״ נופל")
         + st.card("r-4", "ex", "שלילית: <b>כל</b> הערכים $\\le0$"))

VIDEO = Video("O08", "orthodiag", "שאלות עם פרמטר", [title, recipe, symm, exam, recap], bank={"25A-A-Q3a": None})
