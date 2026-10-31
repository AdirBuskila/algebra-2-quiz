# -*- coding: utf-8 -*-
"""O07 · מינורים מובילים וקריטריון סילבסטר — video script (build: tools/video/vid.py O07).

Source: courses/orthodiag/C07.js (lesson + goal). Exam anchor: 24B-A-Q3a ((1,c,0;c,1,c;0,c,1): leading minors 1,
1-c^2, 1-2c^2 decide "strictly"; at c = ±1/sqrt2 the criterion is silent and the eigenvalues 1, 1±sqrt2 c decide),
which no guided quiz uses (its twin 25B-B-Q5a is not used anywhere either).
Avoided on purpose: the C07 quiz/lesson matrices ((2,1;1,3), (2,1,0;1,2,1;0,1,2), (1,1;1,1), (0,0;0,-1), (1,2;2,a),
(-2,1;1,-2)) and the boss parts. The examples are new: (3,1,1;1,2,0;1,0,1), its negative, and (1,1,0;1,1,0;0,0,-1).
Every minor, eigenvalue, verdict and interval is asserted with sympy.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_orthodiag as w
from w_orthodiag import S, R

lam = sp.symbols("lambda")

# ---------------------------------------------------------------- examples
M = S([[3, 1, 1], [1, 2, 0], [1, 0, 1]])
assert w.lead_minors(M) == [3, 5, 3]
assert (3 * 2 - 1 * 1) == 5 and 3 * (2 * 1 - 0) - 1 * (1 * 1 - 0) + 1 * (0 - 2 * 1) == 3
assert w.classify(M)["spos"]
Nm = -M
assert w.lead_minors(Nm) == [-3, 5, -3] and w.classify(Nm)["sneg"]
Z = S([[1, 1, 0], [1, 1, 0], [0, 0, -1]])
assert w.lead_minors(Z) == [1, 0, 0]
assert sorted(Z.eigenvals(multiple=True)) == [-1, 0, 2]
assert w.classify(Z) == dict(pos=False, spos=False, neg=False, sneg=False)
assert (S([0, 0, 1]).T * Z * S([0, 0, 1]))[0] == -1

# ---------------------------------------------------------------- exam 24B-A-Q3a
X = BANK["24B-A-Q3a"]
c = sp.symbols("c", real=True)
A = S([[1, c, 0], [c, 1, c], [0, c, 1]])
assert "\\begin{pmatrix}1&c&0\\\\c&1&c\\\\0&c&1\\end{pmatrix}" in X["question"]
D1, D2, D3 = w.lead_minors(A)
assert D1 == 1 and sp.expand(D2) == 1 - c**2 and sp.expand(D3) == 1 - 2 * c**2
SPOS = sp.Intersection(sp.solveset(D2 > 0, c, sp.S.Reals), sp.solveset(D3 > 0, c, sp.S.Reals))
r2 = 1 / sp.sqrt(2)
assert SPOS == sp.Interval.open(-r2, r2)
assert sp.solveset(D3 > 0, c, sp.S.Reals) == SPOS                      # Delta_3 > 0 already forces Delta_2 > 0
assert sp.factor(sp.expand((A - lam * sp.eye(3)).det())) == sp.factor((1 - lam) * ((1 - lam)**2 - 2 * c**2))
EV = [1, 1 + sp.sqrt(2) * c, 1 - sp.sqrt(2) * c]
assert sorted(map(sp.simplify, A.eigenvals(multiple=True)), key=str) == sorted(map(sp.simplify, EV), key=str)
POS = sp.Intersection(*[sp.solveset(e >= 0, c, sp.S.Reals) for e in EV[1:]])
assert POS == sp.Interval(-r2, r2)
for val, f in ((r2, dict(pos=True, spos=False, neg=False, sneg=False)),
               (-r2, dict(pos=True, spos=False, neg=False, sneg=False)),
               (R(1, 2), dict(pos=True, spos=True, neg=False, sneg=False)),
               (1, dict(pos=False, spos=False, neg=False, sneg=False))):
    assert w.classify(A.subs(c, val)) == f, val
assert sorted(A.subs(c, r2).eigenvals(multiple=True)) == [0, 1, 2]
assert w.lead_minors(A.subs(c, r2))[2] == 0

NL = w.numline("nl", -R(3, 2), R(3, 2), [(-r2, "−1/√2"), (0, "0"), (r2, "1/√2")], [
    ("d3", "Δ₃ > 0", [(-r2, r2, False, False, 0)]),
    ("pos", "חיובית", [(-r2, r2, True, True, 1)]),
    ("none", "אף אחת", [(None, -r2, None, False, 2), (r2, None, False, None, 2)]),
], w=980)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נלמד דרך מהירה להכריע חיוביות לחלוטין, בלי לחשב ערכים עצמיים."),
    P("נכיר את המינורים המובילים ואת הקריטריון של סילבסטר, וגם את מה שהוא **לא** יודע להכריע.", hold=0.4),
], stage='<div class="kicker">O07 · לכסון אורתוגונלי והגדרה חיובית</div><h1>מינורים מובילים וקריטריון סילבסטר</h1>'
         '<p>להשתמש במינורים המובילים כדי להכריע חיוביות לחלוטין, ולדעת מה הקריטריון לא יכול להכריע.</p>',
   layout="title")

minors = Scene("minors", "מינורים מובילים", [
    P("המינור המוביל דלתא $k$ הוא הדטרמיננטה של הפינה השמאלית העליונה, בגודל $k$ על $k$.",
      say="המינור המוביל דלתא קֵיי הוא הדטרמיננטה של הפינה השמאלית העליונה, בגודל קֵיי על קֵיי.", do=show("m")),
    P("דלתא אחת: רק האיבר הראשון. שלוש.", do=show("m-c-0-0", "k-0")),
    P("דלתא שתיים: הפינה שתיים על שתיים. שש פחות אחת, כלומר חמש.",
      do=show("m-c-0-1", "m-c-1-0", "m-c-1-1", "k-1")),
    P("דלתא שלוש: כל המטריצה. פיתוח לפי השורה הראשונה נותן שלוש.",
      do=show("m-c-0-2", "m-c-1-2", "m-c-2-0", "m-c-2-1", "m-c-2-2", "k-2")),
    P("וזה הקריטריון של סילבסטר: מטריצה סימטרית חיובית לחלוטין אם ורק אם **כל** המינורים המובילים חיוביים ממש.",
      do=show("s-r")),
    P("כאן שלוש, חמש ושלוש. כולם חיוביים, ולכן היא חיובית לחלוטין. בלי פולינום אופייני.", do=show("k-v")),
    P("ולשלילית לחלוטין: הסימנים מתחלפים, ומתחילים בשלילי. מינוס, פלוס, מינוס.", do=show("s-n")),
    P("למשל המטריצה הנגדית: מינוס שלוש, חמש, מינוס שלוש. שלילית לחלוטין.", hold=0.4),
], stage='<div class="od-stack">' + w.mat("m", M, "A=", hidden=True, size=42)
         + w.lines("k", ["$\\Delta_1=3$", "$\\Delta_2=3\\cdot2-1\\cdot1=5$", "$\\Delta_3=3$"], size=38)
         + w.chip("k-v", "חיובית לחלוטין", 0) + '</div>',
   panel=st.card("s-r", "rule", "🔑 <b>סילבסטר:</b> חיובית לחלוטין $\\iff$ $\\Delta_1,\\Delta_2,\\dots,\\Delta_n>0$")
         + st.card("s-n", "rule", "🔑 שלילית לחלוטין $\\iff$ $\\Delta_1<0,\\ \\Delta_2>0,\\ \\Delta_3<0,\\dots$"))

why = Scene("why", "למה הסימנים מתחלפים", [
    P("למה בשלילית הסימנים מתחלפים, ולא כולם שליליים? נבין את הכיוון הקל.", do=show("n")),
    P("אם $A$ שלילית לחלוטין, גם כל פינה שלה שלילית לחלוטין: מציבים וקטורים שמסתיימים באפסים.",
      say="אם אֵיי שלילית לחלוטין, גם כל פינה שלה שלילית לחלוטין: מציבים וקטורים שמסתיימים באפסים.", do=show("w-0")),
    P("הדטרמיננטה של פינה $k$ על $k$ היא מכפלה של $k$ ערכים עצמיים שליליים.",
      say="הדטרמיננטה של פינה קֵיי על קֵיי היא מכפלה של קֵיי ערכים עצמיים שליליים.", do=show("w-1")),
    P("מכפלה של מספר אי זוגי של שליליים היא שלילית, ושל מספר זוגי היא חיובית. ומכאן מינוס, פלוס, מינוס.",
      do=show("w-2")),
    P("וכאן: מינוס שלוש, חמש, מינוס שלוש. בדיוק הדפוס.", do=show("n-v"), hold=0.4),
], stage='<div class="od-stack">' + w.mat("n", Nm, "{-A}=", hidden=True, size=40)
         + w.lines("w", ["$x=(y,0,\\dots,0)\\ \\Rightarrow\\ x^TAx=y^TA_ky$",
                         "$\\Delta_k=\\det A_k=\\mu_1\\mu_2\\cdots\\mu_k,\\quad \\mu_i<0$",
                         "$\\operatorname{sign}\\Delta_k=({-1})^k$"], size=36)
         + w.chip("n-v", "$\\Delta={-3},\\ 5,\\ -3$", 1) + '</div>',
   panel=st.card("w-r", "rule", "🔑 שלילית לחלוטין: $\\Delta_1<0,\\ \\Delta_2>0,\\ \\Delta_3<0,\\dots$").replace(" h\"", "\""))

limit = Scene("limit", "מה הוא לא מכריע", [
    P("אבל שימו לב: הקריטריון מדבר רק על ״לחלוטין״.", do=show("z")),
    P("ובמטריצה הזו? המינורים שלה: אחת, אפס ואפס. כולם גדולים או שווים לאפס.", do=show("z-0")),
    P("מפתה לומר שהיא חיובית. אבל הווקטור אפס, אפס, אחת נותן מינוס אחת.", do=show("z-1")),
    P("ואכן הערכים העצמיים שלה הם שתיים, אפס ומינוס אחת. היא אף אחת מהן.", do=show("z-2")),
    P("המסקנה: מינור שמתאפס לא אומר כלום על ״חיובית״. שם חוזרים לערכים העצמיים.", do=show("z-t"), hold=0.4),
], stage='<div class="od-stack">' + w.mat("z", Z, "B=", hidden=True, size=42)
         + w.lines("z", ["$\\Delta_1=1,\\ \\Delta_2=0,\\ \\Delta_3=0$",
                         "$x=(0,0,1):\\ x^TBx={-1}<0$",
                         "$\\lambda=2,\\ 0,\\ {-1}$"], size=38) + '</div>',
   panel=st.card("z-t", "trap", "⚠️ מינורים $\\ge0$ <b>לא</b> מבטיחים חיובית. מינור $0$: עוברים לערכים עצמיים."))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: עבור אילו ערכי $c$ המטריצה הזו חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?",
      say="שאלה ממבחן: עבור אילו ערכי סִי המטריצה הזו חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?",
      do=show("x")),
    P("נתחיל בסילבסטר. דלתא אחת היא אחת. דלתא שתיים: אחת פחות $c$ בריבוע.",
      say="נתחיל בסילבסטר. דלתא אחת היא אחת. דלתא שתיים: אחת פחות סִי בריבוע.", do=show("e-0")),
    P("דלתא שלוש: אחת פחות פעמיים $c$ בריבוע.", say="דלתא שלוש: אחת פחות פעמיים סִי בריבוע.", do=show("e-1")),
    P("כולם חיוביים כש-$c$ בריבוע קטן מחצי, כלומר בין מינוס אחת חלקי שורש שתיים לאחת חלקי שורש שתיים.",
      say="כולם חיוביים כשסִי בריבוע קטן מחצי, כלומר בין מינוס אחת חלקי שורש שתיים לאחת חלקי שורש שתיים.",
      do=show("nl-d3")),
    P("אז זה בדיוק התחום של חיובית לחלוטין, בלי הקצוות.", do=show("y-1")),
    P("שלילית לחלוטין לא תהיה אף פעם: דלתא אחת היא אחת, ולא שלילית.", do=show("y-2")),
    P("ומה בקצוות? שם דלתא שלוש מתאפסת, וסילבסטר שותק. עוברים לערכים עצמיים.", do=show("e-2", "x-t")),
    P("הפולינום האופייני מתפרק, והערכים הם אחת, ואחת ועוד או פחות שורש שתיים כפול $c$.",
      say="הפולינום האופייני מתפרק, והערכים הם אחת, ואחת ועוד או פחות שורש שתיים כפול סִי.", do=show("e-3")),
    P("בקצוות הערכים הם אחת, שתיים ואפס. כולם לא שליליים: חיובית, אבל לא לחלוטין.", do=show("nl-pos", "y-3")),
    P("ומחוץ לקטע, אחד מהערכים אחת ועוד או פחות שורש שתיים $c$ שלילי, לצד הערך אחת שתמיד חיובי. אף אחת מהן.",
      say="ומחוץ לקטע, אחד מהערכים אחת ועוד או פחות שורש שתיים סִי שלילי, לצד הערך אחת שתמיד חיובי. אף אחת מהן.", do=show("nl-none"), hold=0.5),
], stage='<div class="od-stack" style="gap:14px"><div class="od-row" style="gap:30px">'
         + w.mat("x", A, "", hidden=True, size=34)
         + w.lines("e", ["$\\Delta_1=1,\\ \\Delta_2=1-c^2$", "$\\Delta_3=1-2c^2$",
                         "$c=\\pm\\frac{1}{\\sqrt2}:\\ \\Delta_3=0$",
                         "$\\lambda=1,\\ 1\\pm\\sqrt2\\,c$"], size=30) + '</div>' + NL + '</div>',
   panel=w.qstem(X["id"], "עבור אילו ערכי $c$ המטריצה חיובית, חיובית לחלוטין, שלילית, שלילית לחלוטין, או אף אחת?")
         + w.lines("y", ["לחלוטין: $|c|<\\frac{1}{\\sqrt2}$", "שלילית: אף פעם ($\\lambda=1>0$)",
                         "חיובית: $|c|\\le\\frac{1}{\\sqrt2}$"], size=32, start=1)
         + st.card("x-t", "trap", "⚠️ $\\Delta_3=0$: סילבסטר לא מכריע ״חיובית״"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: המינורים המובילים הם הדטרמיננטות של הפינות השמאליות העליונות.", do=show("r-1")),
    P("כולם חיוביים ממש: חיובית לחלוטין. סימנים מתחלפים, מתחילים במינוס: שלילית לחלוטין.", do=show("r-2")),
    P("ומינור שמתאפס? הקריטריון שותק. שם מחשבים ערכים עצמיים. נתראה ברמה הבאה.", do=show("r-3"), hold=0.6),
], stage='<div class="od-stack"><div class="od-big" style="font-size:46px">'
         '$\\Delta_1,\\ \\Delta_2,\\ \\dots,\\ \\Delta_n>0$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $\\Delta_k$ = דטרמיננטה של הפינה $k\\times k$")
         + st.card("r-2", "rule", "🔑 כולם $>0$: לחלוטין. $-,+,-$: שלילית לחלוטין")
         + st.card("r-3", "trap", "⚠️ מינור $0$: עוברים לערכים עצמיים"))

VIDEO = Video("O07", "orthodiag", "מינורים מובילים וקריטריון סילבסטר", [title, minors, why, limit, exam, recap],
              bank={"24B-A-Q3a": None})
