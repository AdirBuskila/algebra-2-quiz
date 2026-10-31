# -*- coding: utf-8 -*-
"""O03 · הרכבת Q ו-D ושמירה על הסדר — video script (build: tools/video/vid.py O03).

Source: courses/orthodiag/C03.js (lesson + goal). Exam anchor: 26A-A-Q1a (orthogonal diagonalization of
(3,1,0;1,3,0;0,0,1), eigenvalues 4, 2, 1), which no guided quiz uses.
Avoided on purpose: the C03 quiz matrices ((2,1;1,2) with Q = (1,1;1,-1)/sqrt2, D = diag(5,1), (1,2;2,1)) and every
bank id used by a quiz or boss. The worked example is (6,2;2,3) with eigenvalues 7 and 2. Every Q, D and product
shown is computed and asserted with sympy (Q^T Q = I, Q^T A Q = D, Q D Q^T = A, and the wrong order giving another
matrix).
"""
import sympy as sp
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_orthodiag as w
from w_orthodiag import S, R

r5 = sp.sqrt(5)

# ---------------------------------------------------------------- worked example
A = S([[6, 2], [2, 3]])
Q, D = w.orth_diag(A, [(7, [2, 1]), (2, [1, -2])])
assert Q == S([[2, 1], [1, -2]]) / r5 and D == sp.diag(7, 2)
QD = Q * D
assert QD == S([[14, 2], [7, -4]]) / r5                      # Q D: column j of Q times d_j
assert sp.simplify(QD * Q.T) == A
assert S([[14, 2], [7, -4]]) * S([[2, 1], [1, -2]]) == S([[30, 10], [10, 15]])      # = 5 A
# the wrong order: columns swapped, D kept
Qs = S.hstack(Q[:, 1], Q[:, 0])
W = sp.simplify(Qs * D * Qs.T)
assert W == S([[3, -2], [-2, 6]]) and W != A
assert W.trace() == A.trace() and W.det() == A.det()           # same eigenvalues, different matrix
# swapping both keeps it right
assert sp.simplify(Qs * sp.diag(2, 7) * Qs.T) == A

# ---------------------------------------------------------------- exam 26A-A-Q1a
X = BANK["26A-A-Q1a"]
B = S([[3, 1, 0], [1, 3, 0], [0, 0, 1]])
assert "\\begin{pmatrix}3&1&0\\\\1&3&0\\\\0&0&1\\end{pmatrix}" in X["question"]
assert B * S([0, 0, 1]) == S([0, 0, 1])
blk = B[:2, :2]
assert blk.trace() == 6 and blk.det() == 8 and sorted(blk.eigenvals(multiple=True)) == [2, 4]
assert sorted(B.eigenvals(multiple=True)) == [1, 2, 4] and B.det() == 8
QB, DB = w.orth_diag(B, [(4, [1, 1, 0]), (2, [-1, 1, 0]), (1, [0, 0, 1])])
assert DB == sp.diag(4, 2, 1)
assert (B - 4 * sp.eye(3)) == S([[-1, 1, 0], [1, -1, 0], [0, 0, -3]])
assert (B - 2 * sp.eye(3)) == S([[1, 1, 0], [1, 1, 0], [0, 0, -1]])
# the official answer's Q (same columns, same order)
assert QB == S([[1 / sp.sqrt(2), -1 / sp.sqrt(2), 0], [1 / sp.sqrt(2), 1 / sp.sqrt(2), 0], [0, 0, 1]])

TQ = [[w.ent(Q[i, j]) for j in range(2)] for i in range(2)]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נרכיב את שתי המטריצות של הלכסון: $Q$ ו-$D$.", say="בסרטון הזה נרכיב את שתי המטריצות של הלכסון: קְיוּ ודִּי."),
    P("נראה למה הסדר שלהן חייב להתאים, ואיך מחשבים את $A$ בחזרה מהפירוק.",
      say="נראה למה הסדר שלהן חייב להתאים, ואיך מחשבים את אֵיי בחזרה מהפירוק."),
    P("ובסוף נפתור שאלה ממבחן.", hold=0.4),
], stage='<div class="kicker">O03 · לכסון אורתוגונלי והגדרה חיובית</div><h1>הרכבת $Q$ ו-$D$ ושמירה על הסדר</h1>'
         '<p>לבנות $Q$ ו-$D$ מערכים ווקטורים עצמיים כך שסדר העמודות בהתאם לסדר האלכסון, ולחשב $A$ חזרה מהפירוק.</p>',
   layout="title")

build = Scene("build", "ההרכבה", [
    P("נתחיל במטריצה שש, שתיים, שתיים, שלוש.", do=show("a")),
    P("העקבה תשע והדטרמיננטה ארבע עשרה, ולכן הערכים העצמיים הם שבע ושתיים.", do=show("b-0")),
    P("עבור שבע: הווקטור שתיים, אחת. עבור שתיים: אחת, מינוס שתיים. האורך של שניהם הוא שורש חמש.", do=show("b-1")),
    P("עכשיו ההרכבה. הווקטור המנורמל של שבע נכנס לעמודה הראשונה של $Q$.",
      say="עכשיו ההרכבה. הווקטור המנורמל של שבע נכנס לעמודה הראשונה של קְיוּ.", do=show("q", "q-col-0")),
    P("ולכן שבע נכנס למקום הראשון באלכסון של $D$.", say="ולכן שבע נכנס למקום הראשון באלכסון של דִּי.",
      do=show("d", "d-col-0")),
    P("הווקטור של שתיים בעמודה השנייה, והערך שתיים במקום השני. כל עמודה והערך שלה, באותו צבע.",
      do=hide("q-col-0", "d-col-0") + show("q-col-1", "d-col-1")),
    P("העמודות ניצבות ובאורך אחת, ולכן $Q^TQ$ שווה ליחידה.", say="העמודות ניצבות ובאורך אחת, ולכן קְיוּ טרנספוז קְיוּ שווה ליחידה.",
      do=hide("q-col-1", "d-col-1") + show("b-r")),
    P("כלומר ההופכית של $Q$ היא פשוט השחלוף שלה. וזה נותן את שתי הנוסחאות.",
      say="כלומר ההופכית של קְיוּ היא פשוט השחלוף שלה. וזה נותן את שתי הנוסחאות.", do=show("b-f"), hold=0.4),
], stage='<div class="od-stack">' + w.mat("a", A, "A=", hidden=True, size=40)
         + w.lines("b", ["$\\operatorname{tr}=9,\\ \\det=14\\ \\Rightarrow\\ \\lambda=7,\\ 2$",
                         "$\\lambda=7:\\ (2,1)\\qquad \\lambda=2:\\ (1,{-2})$"], size=34)
         + '<div class="od-row" style="gap:40px">'
         + w.mat("q", TQ, "Q=", cols={0: 0, 1: 1}, hidden=True, size=36, tex=True)
         + w.mat("d", D, "D=", cols={0: 0, 1: 1}, hidden=True, size=36) + '</div></div>',
   panel=st.card("b-r", "rule", "🔑 $Q^TQ=I$, ולכן $Q^{-1}=Q^T$")
         + st.card("b-f", "rule", "🔑 $A=QDQ^T$ &nbsp; וגם &nbsp; $Q^TAQ=D$"))

order = Scene("order", "הסדר", [
    P("מה אם נחליף את סדר העמודות של $Q$, ונשאיר את $D$ כמו שהיא?",
      say="מה אם נחליף את סדר העמודות של קְיוּ, ונשאיר את דִּי כמו שהיא?", do=show("o-q")),
    P("נחשב את המכפלה, ונקבל שלוש, מינוס שתיים, מינוס שתיים, שש. זו בכלל לא $A$.",
      say="נחשב את המכפלה, ונקבל שלוש, מינוס שתיים, מינוס שתיים, שש. זו בכלל לא אֵיי.", do=show("o-w", "o-x")),
    P("שימו לב: יש לה אותה עקבה ואותה דטרמיננטה. אותם ערכים עצמיים, אבל וקטורים עצמיים אחרים.", do=show("o-c")),
    P("כי עכשיו הערך שבע הוצמד לווקטור הלא נכון.", hold=0.3),
    P("הכלל: מחליפים סדר בשני הצדדים יחד, או לא מחליפים בכלל. כל סדר נכון, כל עוד הוא תואם.", do=show("o-r"),
      hold=0.4),
], stage='<div class="od-stack"><div id="o-q" class="od-mid h">'
         '$\\frac{1}{\\sqrt5}\\begin{pmatrix}1&2\\\\{-2}&1\\end{pmatrix}\\begin{pmatrix}7&0\\\\0&2\\end{pmatrix}'
         '\\frac{1}{\\sqrt5}\\begin{pmatrix}1&{-2}\\\\2&1\\end{pmatrix}$</div>'
         '<div id="o-w" class="od-big h">$=' + w.pm(W) + '$</div>'
         + w.chip("o-x", "$\\ne A$", 2) + '</div>',
   panel=st.card("o-c", "ex", "$\\operatorname{tr}=9,\\ \\det=14$: אותם ערכים עצמיים, מטריצה אחרת")
         + st.card("o-r", "trap", "⚠️ החלפת סדר בצד אחד בלבד הורסת את השוויון"))

back = Scene("back", "חזרה ל-A", [
    P("ועכשיו בכיוון ההפוך: יש לנו $Q$ ו-$D$, ורוצים את $A$.", say="ועכשיו בכיוון ההפוך: יש לנו קְיוּ ודִּי, ורוצים את אֵיי."),
    P("קיצור דרך: כפל ב-$D$ מימין פשוט כופל כל עמודה של $Q$ בערך העצמי שלה.",
      say="קיצור דרך: כפל בדִּי מימין פשוט כופל כל עמודה של קְיוּ בערך העצמי שלה.", do=show("k-0", "k-r")),
    P("העמודה הראשונה כפול שבע: ארבע עשרה, שבע. השנייה כפול שתיים: שתיים, מינוס ארבע.", do=show("k-1")),
    P("עכשיו כופלים ב-$Q^T$. שני השורשים של חמש נותנים חמש במכנה.",
      say="עכשיו כופלים בקְיוּ טרנספוז. שני השורשים של חמש נותנים חמש במכנה.", do=show("k-2")),
    P("ויוצא שלושים, עשר, עשר, חמש עשרה, חלקי חמש. כלומר שש, שתיים, שתיים, שלוש. בדיוק $A$.",
      say="ויוצא שלושים, עשר, עשר, חמש עשרה, חלקי חמש. כלומר שש, שתיים, שתיים, שלוש. בדיוק אֵיי.", do=show("k-3"),
      hold=0.4),
], stage=w.lines("k", ["$A=Q\\,D\\,Q^T$",
                       "$QD=\\frac{1}{\\sqrt5}\\begin{pmatrix}14&2\\\\7&{-4}\\end{pmatrix}$",
                       "$QDQ^T=\\frac15\\begin{pmatrix}14&2\\\\7&{-4}\\end{pmatrix}\\begin{pmatrix}2&1\\\\1&{-2}\\end{pmatrix}$",
                       "$=\\frac15\\begin{pmatrix}30&10\\\\10&15\\end{pmatrix}=\\begin{pmatrix}6&2\\\\2&3\\end{pmatrix}$"],
                 size=38),
   panel=st.card("k-r", "rule", "🔑 $QD$: עמודה $j$ של $Q$ כפול $d_{jj}$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: בצעו לכסון אורתוגונלי למטריצה שלוש, אחת, אפס. אחת, שלוש, אפס. אפס, אפס, אחת.", do=show("x")),
    P("השורה והעמודה השלישית מבודדות, ולכן אחת הוא ערך עצמי עם הווקטור אפס, אפס, אחת.",
      do=show("x-row-2", "x-col-2", "e-0")),
    P("הבלוק שלוש, אחת, אחת, שלוש: עקבה שש ודטרמיננטה שמונה. שני מספרים: ארבע ושתיים.",
      do=hide("x-row-2", "x-col-2") + show("e-1")),
    P("עבור ארבע: $x$ שווה $y$, ו-$z$ אפס. הווקטור אחת, אחת, אפס.",
      say="עבור ארבע: אִקְס שווה וַואי, וזֶד אפס. הווקטור אחת, אחת, אפס.", do=show("t-0-0", "t-0-1")),
    P("עבור שתיים: $x$ שווה מינוס $y$. הווקטור מינוס אחת, אחת, אפס.",
      say="עבור שתיים: אִקְס שווה מינוס וַואי. הווקטור מינוס אחת, אחת, אפס.", do=show("t-1-0", "t-1-1")),
    P("ועבור אחת: אפס, אפס, אחת. שלושה ערכים שונים, ולכן הווקטורים ניצבים מעצמם.", do=show("t-2-0", "t-2-1")),
    P("מנרמלים: אחד חלקי שורש שתיים לשני הראשונים. השלישי כבר באורך אחת.", do=show("t-0-2", "t-1-2", "t-2-2")),
    P("נבחר סדר: ארבע, שתיים, אחת, ובאותו סדר נכניס את הווקטורים המנורמלים לעמודות של $Q$.",
      say="נבחר סדר: ארבע, שתיים, אחת, ובאותו סדר נכניס את הווקטורים המנורמלים לעמודות של קְיוּ.", do=show("x-ans")),
    P("בדיקה מהירה: מכפלת הערכים העצמיים היא שמונה, והדטרמיננטה של $A$ היא, בסוגריים, תשע פחות אחת, כפול אחת. שמונה.",
      say="בדיקה מהירה: מכפלת הערכים העצמיים היא שמונה, והדטרמיננטה של אֵיי היא, בסוגריים, תשע פחות אחת, כפול אחת. שמונה.",
      do=show("x-chk")),
    P("והמלכודת: לכתוב את $D$ בסדר עולה, אחת, שתיים, ארבע, ולהשאיר את $Q$ בסדר אחר. אז השוויון נשבר.",
      say="והמלכודת: לכתוב את דִּי בסדר עולה, אחת, שתיים, ארבע, ולהשאיר את קְיוּ בסדר אחר. אז השוויון נשבר.",
      do=show("x-t"), hold=0.5),
], stage='<div class="od-stack"><div class="od-row" style="gap:40px">' + w.mat("x", B, "A=", hidden=True, size=36)
         + w.lines("e", ["$\\lambda=1:\\ e_3$", "$\\operatorname{tr}=6,\\ \\det=8\\ \\Rightarrow\\ 4,\\ 2$"], size=32)
         + '</div>'
         + w.table("t", ["$\\lambda$", "וקטור", "מנורמל"],
                   [["$4$", "$(1,1,0)$", "$\\frac{1}{\\sqrt2}(1,1,0)$"],
                    ["$2$", "$({-1},1,0)$", "$\\frac{1}{\\sqrt2}({-1},1,0)$"],
                    ["$1$", "$(0,0,1)$", "$(0,0,1)$"]], colors=[0, 1, 2], size=30) + '</div>',
   panel=w.qstem(X["id"], "בצעו לכסון אורתוגונלי למטריצה $A$.")
         + st.card("x-ans", "ex", w.qd(QB, DB))
         + st.card("x-chk", "plain", "בדיקה: $4\\cdot2\\cdot1=8=\\det\\,A$")
         + st.card("x-t", "trap", "⚠️ $D$ בסדר אחד ו-$Q$ בסדר אחר: $QDQ^T\\ne A$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: העמודות של $Q$ הן וקטורים עצמיים מנורמלים וניצבים.", say="לסיכום: העמודות של קְיוּ הן וקטורים עצמיים מנורמלים וניצבים.",
      do=show("r-1")),
    P("על האלכסון של $D$ הערכים העצמיים, באותו סדר בדיוק.", say="על האלכסון של דִּי הערכים העצמיים, באותו סדר בדיוק.",
      do=show("r-2")),
    P("ההופכית של $Q$ היא השחלוף, ולכן $A$ שווה $QDQ^T$.", say="ההופכית של קְיוּ היא השחלוף, ולכן אֵיי שווה קְיוּ דִּי קְיוּ טרנספוז.",
      do=show("r-3")),
    P("ומחליפים סדר רק בשני הצדדים יחד. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="od-stack"><div class="od-big">$A=QDQ^T$</div></div>',
   panel=st.card("r-1", "rule", "🔑 עמודות $Q$: וקטורים עצמיים, אורך $1$, ניצבים")
         + st.card("r-2", "rule", "🔑 $d_{jj}$ = הערך של העמודה ה-$j$")
         + st.card("r-3", "rule", "🔑 $Q^{-1}=Q^T$")
         + st.card("r-4", "trap", "⚠️ סדר תואם בשני הצדדים"))

VIDEO = Video("O03", "orthodiag", "הרכבת Q ו-D ושמירה על הסדר", [title, build, order, back, exam, recap],
              bank={"26A-A-Q1a": None})
