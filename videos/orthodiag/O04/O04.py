# -*- coding: utf-8 -*-
"""O04 · לכסון 3×3 עם ערך עצמי כפול — video script (build: tools/video/vid.py O04).

Source: courses/orthodiag/C04.js (lesson + goal). Exam anchor: 24A-B-Q5a (orthogonal diagonalization of
(3,-2,4;-2,6,2;4,2,3): eigenvalue 7 twice and -2; Gram-Schmidt inside the eigenspace of 7), which no guided quiz uses.
Avoided on purpose: the C04 quiz/lesson matrix (5,0,0;0,4,2;0,2,1) and its block (4,2;2,1) (also the boss 23B-B-Q4a),
(3,1,1;1,3,1;1,1,3) (boss 23A-B-Q3a) and their twins 25A-C-Q5a / 25B-A-Q6b. The block example is a new matrix
(4,0,0;0,1,3;0,3,1). Every eigenvalue, eigenvector, inner product and the final Q^T A Q = D are asserted with sympy.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_orthodiag as w
from w_orthodiag import S, R

lam = sp.symbols("lambda")

# ---------------------------------------------------------------- block example
E = S([[4, 0, 0], [0, 1, 3], [0, 3, 1]])
blk = E[1:, 1:]
assert blk.trace() == 2 and blk.det() == -8 and sorted(blk.eigenvals(multiple=True)) == [-2, 4]
assert sorted(E.eigenvals(multiple=True)) == [-2, 4, 4]
QE, DE = w.orth_diag(E, [(4, [1, 0, 0]), (4, [0, 1, 1]), (-2, [0, 1, -1])])
assert (E - 4 * sp.eye(3)).rank() == 1 and (E + 2 * sp.eye(3)).rank() == 2

# ---------------------------------------------------------------- exam 24A-B-Q5a
X = BANK["24A-B-Q5a"]
A = S([[3, -2, 4], [-2, 6, 2], [4, 2, 3]])
assert "\\begin{pmatrix}3&-2&4\\\\-2&6&2\\\\4&2&3\\end{pmatrix}" in X["question"]
assert A.trace() == 12 and A.det() == -98
p = sp.expand((A - lam * sp.eye(3)).det())
assert p == -(lam**3 - 12 * lam**2 + 21 * lam + 98)
assert 7**3 - 12 * 7**2 + 21 * 7 + 98 == 0 and (343, 588, 147) == (7**3, 12 * 49, 21 * 7)
assert sp.factor(p) == -(lam - 7)**2 * (lam + 2)
assert sp.expand((lam - 7) * (lam + 2)) == lam**2 - 5 * lam - 14
assert sp.div(lam**3 - 12 * lam**2 + 21 * lam + 98, lam - 7) == (lam**2 - 5 * lam - 14, 0)
M7 = A - 7 * sp.eye(3)
assert M7 == S([[-4, -2, 4], [-2, -1, 2], [4, 2, -4]]) and M7.rank() == 1
assert all(M7.row(i) == k * S([[2, 1, -2]]) for i, k in ((0, -2), (1, -1), (2, 2)))
w1, w2 = S([1, -2, 0]), S([1, 0, 1])
w.eig_pairs(A, [(7, w1), (7, w2)])
assert w1.dot(w2) == 1 and w1.dot(w1) == 5
w2p = w2 - R(1, 5) * w1
assert w2p == S([R(4, 5), R(2, 5), 1]) and 5 * w2p == S([4, 2, 5])
w3 = S([2, 1, -2])
w.eig_pairs(A, [(7, 5 * w2p), (-2, w3)])
assert w3.dot(w1) == 0 and w3.dot(5 * w2p) == 0 and w1.dot(5 * w2p) == 0
assert w.norm(w1) == sp.sqrt(5) and w.norm(5 * w2p) == 3 * sp.sqrt(5) and w.norm(w3) == 3
QA, DA = w.orth_diag(A, [(-2, [2, 1, -2]), (7, [1, -2, 0]), (7, [4, 2, 5])])
assert DA == sp.diag(-2, 7, 7)
# the official answer: the same columns up to sign, same order
off = S([[-R(2, 3), -1 / sp.sqrt(5), -4 / (3 * sp.sqrt(5))],
         [-R(1, 3), 2 / sp.sqrt(5), -2 / (3 * sp.sqrt(5))],
         [R(2, 3), 0, -sp.sqrt(5) / 3]])
assert sp.simplify(off + QA) == sp.zeros(3, 3)
assert sp.simplify(off.T * A * off) == DA
# without Gram-Schmidt the matrix of (unit) eigenvectors is not orthogonal
Qbad = S.hstack(w3 / 3, w1 / sp.sqrt(5), w2 / sp.sqrt(2))
assert sp.simplify(Qbad.T * Qbad) != sp.eye(3)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נלכסן אורתוגונלית מטריצה שלוש על שלוש מההתחלה ועד הסוף."),
    P("נכיר את קיצור הבלוקים, ונראה מה עושים כשערך עצמי מופיע פעמיים."),
    P("ואז נפתור שאלה מלאה ממבחן.", hold=0.4),
], stage='<div class="kicker">O04 · לכסון אורתוגונלי והגדרה חיובית</div><h1>לכסון 3×3 עם ערך עצמי כפול</h1>'
         '<p>ללכסן אורתוגונלית מטריצה סימטרית $3\\times3$, כולל קיצור בלוקים וערך עצמי בריבוי $2$.</p>',
   layout="title")

recipe = Scene("recipe", "המתכון", [
    P("המתכון בארבעה צעדים.", do=show("c-0")),
    P("אחד: מוצאים את הערכים העצמיים, ובודקים: הסכום שווה לעקבה, והמכפלה לדטרמיננטה.", do=show("c-1")),
    P("שתיים: לכל ערך עצמי מוצאים בסיס למרחב העצמי שלו.", do=show("c-2")),
    P("שלוש: בתוך מרחב של ערך כפול בודקים ניצבות, ואם צריך, גרהם-שמידט.", do=show("c-3")),
    P("ארבע: מנרמלים, ומרכיבים את $Q$ ואת $D$ באותו סדר.",
      say="ארבע: מנרמלים, ומרכיבים את קְיוּ ואת דִּי באותו סדר.", do=show("c-4")),
    P("ועובדה שמחזיקה את כל זה: בסימטרית, הריבוי של ערך עצמי שווה תמיד למימד המרחב העצמי שלו.",
      do=show("c-r")),
    P("ערך כפול נותן בדיוק שני וקטורים בלתי תלויים. אף פעם לא פחות.", hold=0.4),
], stage='<div class="od-stack" style="gap:16px">'
         '<div id="c-0" class="od-note h" style="font-size:36px;color:var(--ink)">לכסון אורתוגונלי של $A$ סימטרית $3\\times3$</div>'
         + "".join(st.card(f"c-{k}", "ex", t) for k, t in (
             (1, "① ערכים עצמיים. בדיקה: $\\sum\\lambda=\\operatorname{tr}$, $\\prod\\lambda=\\det$"),
             (2, "② בסיס לכל מרחב עצמי"),
             (3, "③ ערך כפול: ניצבות, ואם צריך גרהם-שמידט"),
             (4, "④ נרמול, ואז $Q$ ו-$D$ באותו סדר"))) + '</div>',
   panel=st.card("c-r", "rule", "🔑 סימטרית: ריבוי $=$ מימד המרחב העצמי"))

block = Scene("block", "קיצור בלוקים", [
    P("קיצור ראשון: בלוקים. במטריצה הזו, בשורה ובעמודה הראשונה יש רק את הארבע שעל האלכסון.",
      do=show("b", "b-row-0", "b-col-0")),
    P("לכן $A$ כפול $e_1$ הוא בדיוק ארבע כפול $e_1$. הווקטור $e_1$ עצמי, עם הערך ארבע.",
      say="לכן אֵיי כפול אִי אחת הוא בדיוק ארבע כפול אִי אחת. הווקטור אִי אחת עצמי, עם הערך ארבע.", do=show("k-0")),
    P("את השאר מלכסנים בבלוק הקטן: אחת, שלוש, שלוש, אחת.",
      do=hide("b-row-0", "b-col-0") + show("b-c-1-1", "b-c-1-2", "b-c-2-1", "b-c-2-2")),
    P("העקבה שתיים והדטרמיננטה מינוס שמונה. הערכים: ארבע ומינוס שתיים.", do=show("k-1")),
    P("ארבע מופיע שוב! סך הכול: ארבע, ארבע, מינוס שתיים. ערך כפול.", do=show("k-2")),
    P("הווקטורים מהבלוק: אפס, אחת, אחת עבור ארבע, ואפס, אחת, מינוס אחת עבור מינוס שתיים.",
      do=hide("b-c-1-1", "b-c-1-2", "b-c-2-1", "b-c-2-2") + show("k-3")),
    P("שני הווקטורים של ארבע הם $e_1$ ואפס, אחת, אחת. הם יוצאים ניצבים, בגלל מבנה הבלוקים.",
      say="שני הווקטורים של ארבע הם אִי אחת ואפס, אחת, אחת. הם יוצאים ניצבים, בגלל מבנה הבלוקים.", do=show("k-r")),
    P("אבל זה מתנה של המבנה, לא חוק. במטריצה מלאה צריך לבדוק.", do=show("k-t"), hold=0.4),
], stage='<div class="od-stack">' + w.mat("b", E, "A=", hidden=True, size=40)
         + w.lines("k", ["$Ae_1=4e_1$", "$\\begin{pmatrix}1&3\\\\3&1\\end{pmatrix}:\\ \\operatorname{tr}=2,\\ \\det={-8}\\ \\Rightarrow\\ 4,\\ {-2}$",
                         "$\\lambda=4,\\ 4,\\ {-2}$",
                         "$\\lambda=4:\\ (0,1,1)\\qquad \\lambda={-2}:\\ (0,1,{-1})$"], size=34) + '</div>',
   panel=st.card("k-r", "rule", "🔑 שורה ועמודה עם איבר אלכסוני בלבד: $e_i$ וקטור עצמי")
         + st.card("k-t", "trap", "⚠️ וקטורים של ערך כפול לא חייבים לצאת ניצבים"))

exam1 = Scene("ex1", "שאלה ממבחן: הערכים", [
    P("ועכשיו שאלה ממבחן: בצעו לכסון אורתוגונלי למטריצה הזו. אין כאן אפסים, אז אין קיצור.", do=show("x")),
    P("מפתחים את הדטרמיננטה של $A$ פחות למדא $I$, ומקבלים פולינום ממעלה שלוש.",
      say="מפתחים את הדטרמיננטה של אֵיי פחות למדא כפול היחידה, ומקבלים פולינום ממעלה שלוש.", do=show("p-0")),
    P("שורש שלם חייב לחלק את תשעים ושמונה. מנסים, ושבע עובד: הכול מתבטל לאפס.", do=show("p-1")),
    P("מחלקים בלמדא פחות שבע, ונשאר גורם ריבועי שהשורשים שלו שבע ומינוס שתיים.", do=show("p-2")),
    P("הערכים: שבע, שבע, ומינוס שתיים. בדיקה: הסכום שתים עשרה, כמו העקבה.", do=show("p-3")),
    P("והמכפלה מינוס תשעים ושמונה, כמו הדטרמיננטה. הכול מסתדר.", hold=0.4),
], stage='<div class="od-stack">' + w.mat("x", A, "A=", hidden=True, size=38)
         + w.lines("p", ["$\\det(A-\\lambda I)={-(\\lambda^3-12\\lambda^2+21\\lambda+98)}$",
                         "$\\lambda=7:\\ 343-588+147+98=0$",
                         "$={-(\\lambda-7)(\\lambda^2-5\\lambda-14)}={-(\\lambda-7)^2(\\lambda+2)}$",
                         "$7+7-2=12=\\operatorname{tr},\\quad 7\\cdot7\\cdot({-2})={-98}=\\det$"], size=32) + '</div>',
   panel=w.qstem(X["id"], "בצעו לכסון אורתוגונלי של המטריצה $A$."))

exam2 = Scene("ex2", "שאלה ממבחן: הווקטורים", [
    P("עבור שבע: כל השורות של $A$ פחות שבע $I$ הן כפולות של שתיים, אחת, מינוס שתיים.",
      say="עבור שבע: כל השורות של אֵיי פחות שבע כפול היחידה הן כפולות של שתיים, אחת, מינוס שתיים.", do=show("m")),
    P("נשארת משוואה אחת, ולכן המרחב העצמי הוא מישור. ריבוי שתיים, מימד שתיים, כמו שהבטחנו.", do=show("v-0")),
    P("שני פתרונות: אחת, מינוס שתיים, אפס. ואחת, אפס, אחת.", do=show("v-1")),
    P("המכפלה הפנימית שלהם אחת. הם לא ניצבים! וזו בדיוק המלכודת של השאלה.", do=show("v-2", "y-t")),
    P("גרהם-שמידט: מורידים מהשני חמישית מהראשון, כי המכפלה אחת והנורמה בריבוע חמש.", do=show("v-3")),
    P("יוצא ארבע חמישיות, שתי חמישיות, אחת. כפול חמש: ארבע, שתיים, חמש.", do=show("v-4")),
    P("עבור מינוס שתיים: הווקטור שתיים, אחת, מינוס שתיים. הוא ניצב לשניהם בלי חישוב, כי הערך שונה.",
      do=show("v-5")),
    P("מנרמלים: מחלקים בשלוש, בשורש חמש ובשלוש שורש חמש, בהתאמה. וקבענו סדר: מינוס שתיים, שבע, שבע.", do=show("y-ans")),
    P("בפתרון הרשמי העמודות הפוכות בסימן. זה אותו לכסון, כי מינוס וקטור עצמי הוא עדיין עצמי.", do=show("y-s"),
      hold=0.5),
], stage='<div class="od-stack" style="gap:18px">'
         '<div id="m" class="od-mid h" style="font-size:30px">$A-7I=' + w.pm(M7) + '$</div>'
         + w.lines("v", ["$2x+y-2z=0$",
                         "$w_1=(1,{-2},0),\\quad w_2=(1,0,1)$",
                         "$\\langle w_2,w_1\\rangle=1\\ne0$",
                         "$w_2'=w_2-\\frac15\\,w_1=\\left(\\frac45,\\frac25,1\\right)\\ \\to\\ (4,2,5)$",
                         "$\\langle (4,2,5),(1,{-2},0)\\rangle=0$ &nbsp;✓",
                         "$\\lambda={-2}:\\ (2,1,{-2})$"], size=32) + '</div>',
   panel=st.card("y-t", "trap", "⚠️ שני וקטורים של $7$ בלי גרהם-שמידט: $Q^TQ\\ne I$")
         + st.card("y-ans", "ex", w.qd(QA, DA, size=26))
         + st.card("y-s", "plain", "הרשמי: אותן עמודות עם סימן הפוך. גם נכון."))

recap = Scene("recap", "סיכום", [
    P("לסיכום: ערכים עצמיים, ובדיקה מול העקבה והדטרמיננטה.", do=show("r-1")),
    P("שורה ועמודה עם איבר אלכסוני בלבד נותנות וקטור עצמי מיידי, ואת השאר מלכסנים בבלוק.", do=show("r-2")),
    P("ערך כפול נותן מישור. בוחרים בו שני וקטורים, ואם הם לא ניצבים, גרהם-שמידט.", do=show("r-3")),
    P("נרמול בסוף, וסדר תואם ב-$Q$ וב-$D$. נתראה ברמה הבאה.", say="נרמול בסוף, וסדר תואם בקְיוּ ובדִּי. נתראה ברמה הבאה.",
      do=show("r-4"), hold=0.6),
], stage='<div class="od-stack"><div class="od-big">$A=QDQ^T$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $\\sum\\lambda=\\operatorname{tr},\\ \\prod\\lambda=\\det$")
         + st.card("r-2", "rule", "🔑 קיצור בלוקים: $e_i$ עצמי")
         + st.card("r-3", "trap", "⚠️ ערך כפול: בודקים ניצבות, גרהם-שמידט")
         + st.card("r-4", "rule", "🔑 נרמול אחרון, סדר תואם"))

VIDEO = Video("O04", "orthodiag", "לכסון 3×3 עם ערך עצמי כפול", [title, recipe, block, exam1, exam2, recap],
              bank={"24A-B-Q5a": None})
