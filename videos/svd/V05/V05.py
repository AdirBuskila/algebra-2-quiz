# -*- coding: utf-8 -*-
"""V05 · העמודות של U לפי u_i = Av_i / σ_i — video script (build: tools/video/vid.py V05).

Source: courses/svd/C05.js (lesson + goal: compute u_i = A v_i / sigma_i for sigma_i != 0, and why U is not taken from
a separate decomposition of AA^T). Exam anchor: none (the three free svd exam parts are solved in V02 and V08).
Original question "בסגנון מבחן" (bank={}): the 3x2 A = [[2,0],[1,1],[0,2]] with sigma = sqrt6, 2 and
v = (1,1)/sqrt2, (1,-1)/sqrt2 given; find u_1, u_2 (u_1 = (1,1,1)/sqrt3, u_2 = (1,0,-1)/sqrt2). (An earlier draft used
[[2,1],[1,2],[1,-1]], whose u_1 = (1,1,0)/sqrt2 and sigma_1 = 3 coincide with the C05-Q1/Q2 answers: dropped.)
Avoided on purpose: the C05 quiz ([[1,2],[2,1],[0,0]] and [[1,0],[1,1],[0,1]]) and every quiz/boss matrix.
Worked example: the lesson's [[1,1],[0,1],[1,0]]. The sign trap is computed: flipping u_1 alone breaks U S V^T = A.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide
import stage as st
import w_svd as w

M = sp.Matrix
s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
Z3 = sp.zeros(3, 1)

# worked example (lesson)
A = M([[1, 1], [0, 1], [1, 0]])
v1, v2 = w.unit((1, 1)), w.unit((1, -1))
assert A.T * A * v1 == 3 * v1 and A.T * A * v2 == v2
Av1, Av2 = A * v1, A * v2
assert sp.simplify(Av1 - M([2, 1, 1]) / s2) == Z3 and sp.simplify(Av2 - M([0, -1, 1]) / s2) == Z3
assert sp.simplify(Av1.norm() - s3) == 0 and sp.simplify(Av2.norm() - 1) == 0
u1, u2 = Av1 / s3, Av2 / 1
assert sp.simplify(u1 - w.unit((2, 1, 1))) == Z3 and sp.simplify(u2 - w.unit((0, -1, 1))) == Z3
assert u1.dot(u2) == 0
AAT = A * A.T
assert w.is_eigvec(AAT, 3, u1) and w.is_eigvec(AAT, 3, -u1)             # -u1 is just as good an eigenvector
_, U = w.cols((2, 1, 1), (0, -1, 1), (1, -1, -1))
_, V = w.cols((1, 1), (1, -1))
S = w.S_mat(3, 2, [s3, 1])
assert w.check_svd(A, U, S, V)
Ubad = U.copy()
Ubad[:, 0] = -U[:, 0]
assert w.is_orth(Ubad) and sp.simplify(Ubad * S * V.T - A) != sp.zeros(3, 2)
assert sp.simplify(A * V[:, 0] + s3 * Ubad[:, 0]) == Z3                  # A v1 = -sigma1 u1 with the flipped column
WRONG = sp.simplify(Ubad * S * V.T)
assert WRONG == M([[-1, -1], [-1, 0], [0, -1]]) == A - 2 * s3 * U[:, 0] * V[:, 0].T

# exam-style question
X = M([[2, 0], [1, 1], [0, 2]])
assert X.T * X == M([[5, 1], [1, 5]]) and w.eig_desc(X.T * X) == [6, 4]
xv1, xv2 = w.unit((1, 1)), w.unit((1, -1))
assert w.is_eigvec(X.T * X, 6, xv1) and w.is_eigvec(X.T * X, 4, xv2)
assert X * M([1, 1]) == M([2, 2, 2]) and X * M([1, -1]) == M([2, 0, -2])
xu1, xu2 = X * xv1 / s6, X * xv2 / 2
assert sp.simplify(xu1 - w.unit((1, 1, 1))) == Z3 and sp.simplify(xu2 - w.unit((1, 0, -1))) == Z3
assert xu1.dot(xu2) == 0 and sp.simplify(xu1.norm() - 1) == 0 and sp.simplify(xu2.norm() - 1) == 0
assert w.is_eigvec(X * X.T, 6, xu1) and w.is_eigvec(X * X.T, 4, xu2)
assert sp.simplify((X * xv1 / 6).norm() - 1) != 0                     # dividing by lambda = 6 gives a wrong length

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נבנה את העמודות של $U$, בנוסחה אחת.", say="בסרטון הזה נבנה את העמודות של יוּ, בנוסחה אחת."),
    P("נבין למה הנוסחה נותנת וקטור באורך אחת, ולמה **לא** מוצאים את $U$ בפירוק נפרד.",
      say="נבין למה הנוסחה נותנת וקטור באורך אחת, ולמה לא מוצאים את יוּ בפירוק נפרד."),
    P("ובסוף נפתור שאלה בסגנון מבחן.", hold=0.4),
], stage='<div class="kicker">V05 · פירוק SVD</div><h1>העמודות של $U$: $u_i=\\frac{1}{\\sigma_i}Av_i$</h1>'
         '<p>לחשב כל עמודה $u_i$ מתוך $v_i$ ו-$\\sigma_i\\ne0$, ולהבין למה לא מפרקים בנפרד.</p>', layout="title")

formula = Scene("formula", "הנוסחה", [
    P("יש לנו כבר את $V$ ואת הערכים הסינגולריים. עכשיו $U$.",
      say="יש לנו כבר את וִי ואת הערכים הסינגולריים. עכשיו יוּ."),
    P("הנוסחה: $u_i$ שווה $A$ כפול $v_i$, חלקי $\\sigma_i$.", do=show("f-1"),
      say="הנוסחה: יוּ אַיי שווה אֵיי כפול וִי אַיי, חלקי סִיגְמָא אַיי."),
    P("למה דווקא היא? כופלים את הפירוק ב-$V$ מימין, ומקבלים $A$ כפול $V$ שווה $U$ כפול $S$.", do=show("f-2"),
      say="למה דווקא היא? כופלים את הפירוק בוִי מימין, ומקבלים אֵיי כפול וִי שווה יוּ כפול אֶס."),
    P("ועמודה אחר עמודה זה בדיוק: $A$ כפול $v_i$ שווה $\\sigma_i$ כפול $u_i$.", do=show("f-3"),
      say="ועמודה אחר עמודה זה בדיוק: אֵיי כפול וִי אַיי שווה סִיגְמָא אַיי כפול יוּ אַיי."),
    P("ולמה האורך יוצא אחת? האורך בריבוע של $A v_i$ הוא $v_i^T A^TA v_i$.", do=show("f-4"),
      say="ולמה האורך יוצא אחת? האורך בריבוע של אֵיי וִי אַיי הוא וִי אַיי טְרַנְסְפּוֹז, אֵיי טְרַנְסְפּוֹז אֵיי, וִי אַיי."),
    P("ו-$v_i$ וקטור עצמי, אז יוצא $\\lambda_i$, כלומר $\\sigma_i$ בריבוע. חלוקה ב-$\\sigma_i$ נותנת אורך אחת בדיוק.",
      do=show("f-c1"),
      say="ווִי אַיי וקטור עצמי, אז יוצא לַמְדָא אַיי, כלומר סִיגְמָא אַיי בריבוע. חלוקה בסִיגְמָא אַיי נותנת אורך אחת בדיוק."),
    P("ואם ה-$v_i$ ניצבים זה לזה, גם ה-$u_i$ שיוצאים ניצבים. אין צורך לנרמל, אבל בדיקה קצרה עדיין שווה.",
      do=show("f-c2"), hold=0.4,
      say="ואם הווִי אַיי ניצבים זה לזה, גם היוּ אַיי שיוצאים ניצבים. אין צורך לנרמל, אבל בדיקה קצרה עדיין שווה."),
], stage=w.lines(w.line("f-1", r"u_i=\frac{1}{\sigma_i}Av_i", "big"),
                 w.line("f-2", r"A=USV^T\ \Rightarrow\ AV=US", "small"),
                 w.line("f-3", r"Av_i=\sigma_iu_i", "small"),
                 w.line("f-4", r"\|Av_i\|^2=v_i^TA^TAv_i=\lambda_i\,v_i^Tv_i=\sigma_i^2", "small")),
   panel=st.card("f-c1", "rule", "🔑 $\\|Av_i\\|=\\sigma_i$, ולכן $\\|u_i\\|=1$")
         + st.card("f-c2", "rule", "🔑 $v_i$ ניצבים $\\Rightarrow$ $u_i$ ניצבים"))

ex1 = Scene("ex1", "דוגמה", [
    P("נחזור למטריצה של הקורס. יש לנו $\\sigma_1$ שורש שלוש ו-$\\sigma_2$ אחת, ואת $v_1$ ו-$v_2$.", do=show("a-0"),
      say="נחזור למטריצה של הקורס. יש לנו סִיגְמָא אחת שורש שלוש וסִיגְמָא שתיים אחת, ואת וִי אחת ווִי שתיים."),
    P("$A$ כפול $v_1$: שתיים, אחת, אחת, חלקי שורש שתיים.", do=show("a-1"),
      say="אֵיי כפול וִי אחת: שתיים, אחת, אחת, חלקי שורש שתיים."),
    P("מחלקים בשורש שלוש. שורש שתיים כפול שורש שלוש זה שורש שש, וזו $u_1$.", do=show("a-2"),
      say="מחלקים בשורש שלוש. שורש שתיים כפול שורש שלוש זה שורש שש, וזו יוּ אחת."),
    P("$A$ כפול $v_2$: אפס, מינוס אחת, אחת, חלקי שורש שתיים.", do=show("a-3"),
      say="אֵיי כפול וִי שתיים: אפס, מינוס אחת, אחת, חלקי שורש שתיים."),
    P("$\\sigma_2$ היא אחת, ולכן זו כבר $u_2$.", do=show("a-4"),
      say="סִיגְמָא שתיים היא אחת, ולכן זו כבר יוּ שתיים."),
    P("בדיקה: שתיים כפול אפס, ועוד אחת כפול מינוס אחת, ועוד אחת כפול אחת. אפס. הן ניצבות.", do=show("a-c1"), hold=0.4),
], stage=w.lines(w.line("a-0", "A=" + w.pm(A) + r",\quad v_1=" + w.nvec((1, 1)) + r",\ \ v_2=" + w.nvec((1, -1)), "small"),
                 w.line("a-1", r"Av_1=" + w.svec((2, 1, 1), 2), "small"),
                 w.line("a-2", r"u_1=\frac{1}{\sqrt{3}}\cdot\frac{1}{\sqrt{2}}(2,1,1)=" + w.nvec((2, 1, 1)), "hl"),
                 w.line("a-3", r"Av_2=" + w.nvec((0, -1, 1)), "small"),
                 w.line("a-4", r"u_2=" + w.nvec((0, -1, 1)), "hl"), cls="tight"),
   panel=st.card("a-c1", "ex", "$(2,1,1)\\cdot(0,{-1},1)=0$ ✓"))

trap = Scene("trap", "למה לא בנפרד", [
    P("ולמה לא פשוט לפרק את $AA^T$ ולקחת ממנה את $U$?",
      say="ולמה לא פשוט לפרק את אֵיי אֵיי טְרַנְסְפּוֹז ולקחת ממנה את יוּ?"),
    P("כי גם מינוס $u_1$ הוא וקטור עצמי באורך אחת של $AA^T$, עם אותו ערך עצמי.", do=show("t-1"),
      say="כי גם מינוס יוּ אחת הוא וקטור עצמי באורך אחת של אֵיי אֵיי טְרַנְסְפּוֹז, עם אותו ערך עצמי."),
    P("פירוק נפרד יכול לתת אותו, נקרא לו $u_1'$. ואז $A$ כפול $v_1$ שווה **מינוס** $\\sigma_1$ כפול $u_1'$.", do=show("t-2"),
      say="פירוק נפרד יכול לתת אותו, נקרא לו יוּ אחת תָּג. ואז אֵיי כפול וִי אחת שווה מינוס סִיגְמָא אחת כפול יוּ אחת תָּג."),
    P("נכפיל את שלוש המטריצות עם העמודה ההפוכה. יוצאת מטריצה אחרת לגמרי, ולא $A$.", do=show("t-3"),
      say="נכפיל את שלוש המטריצות עם העמודה ההפוכה. יוצאת מטריצה אחרת לגמרי, ולא אֵיי."),
    P("ושימו לב: $U$ עדיין אורתוגונלית לגמרי. בדיקת אורתוגונליות לא תתפוס את הטעות הזו.", do=show("t-c1"),
      say="ושימו לב: יוּ עדיין אורתוגונלית לגמרי. בדיקת אורתוגונליות לא תתפוס את הטעות הזו."),
    P("הנוסחה קובעת את הסימן לבד, ולכן מחשבים בה, ולא בפירוק נפרד.", do=show("t-c2")),
    P("ועוד דבר: היא עובדת רק כש-$\\sigma_i$ שונה מאפס. על אפס אי אפשר לחלק, ואת זה נשלים בשלב הבא.", do=show("t-c3"),
      hold=0.4, say="ועוד דבר: היא עובדת רק כשסִיגְמָא אַיי שונה מאפס. על אפס אי אפשר לחלק, ואת זה נשלים בשלב הבא."),
], stage=w.lines(w.line("t-1", r"u_1'={-u_1}:\quad AA^Tu_1'=3\,u_1'", "small"),
                 w.line("t-2", r"Av_1={-\sigma_1}\,u_1'", "bad"),
                 w.line("t-3", r"U'SV^T=" + w.pm(WRONG) + r"\ne A", "bad")),
   panel=st.card("t-c1", "trap", "⚠️ $U'$ אורתוגונלית, ובכל זאת הפירוק שגוי")
         + st.card("t-c2", "rule", "🔑 הנוסחה קובעת את הסימן של $u_i$")
         + st.card("t-c3", "trap", "⚠️ רק ל-$\\sigma_i\\ne0$"))

QSTEM = ('<div class="qstem sv-small"><span class="qid">בסגנון מבחן</span>'
         f'$A={w.pm(X)}$, $\\sigma_1=\\sqrt6$, $\\sigma_2=2$, $v_1={w.nvec((1, 1))}$, $v_2={w.nvec((1, -1))}$. '
         'מצאו את $u_1$ ואת $u_2$.</div>')
exam = Scene("exam", "שאלה בסגנון מבחן", [
    P("שאלה בסגנון מבחן: נתונים הערכים הסינגולריים ו-$V$. מצאו את שתי העמודות הראשונות של $U$.",
      say="שאלה בסגנון מבחן: נתונים הערכים הסינגולריים ווִי. מצאו את שתי העמודות הראשונות של יוּ."),
    P("$A$ כפול אחת אחת: סכום העמודות. שתיים, שתיים, שתיים. ומחלקים בשורש שתיים.", do=show("x-1"),
      say="אֵיי כפול אחת, אחת: סכום העמודות. שתיים, שתיים, שתיים. ומחלקים בשורש שתיים."),
    P("חלקי $\\sigma_1$, שורש שש: יוצא $u_1$, הווקטור אחת, אחת, אחת, חלקי שורש שלוש.", do=show("x-2"),
      say="חלקי סִיגְמָא אחת, שורש שש: יוצא יוּ אחת: הווקטור אחת, אחת, אחת, חלקי שורש שלוש."),
    P("$A$ כפול אחת, מינוס אחת: הפרש העמודות. שתיים, אפס, מינוס שתיים, חלקי שורש שתיים.", do=show("x-3"),
      say="אֵיי כפול אחת, מינוס אחת: הפרש העמודות. שתיים, אפס, מינוס שתיים, חלקי שורש שתיים."),
    P("חלקי $\\sigma_2$, שתיים: יוצא $u_2$, הווקטור אחת, אפס, מינוס אחת, חלקי שורש שתיים.", do=show("x-4"),
      say="חלקי סִיגְמָא שתיים, שתיים: יוצא יוּ שתיים: הווקטור אחת, אפס, מינוס אחת, חלקי שורש שתיים."),
    P("בדיקה: אחת ועוד אפס פחות אחת, אפס. ניצבות. והאורכים אחת, כמו שהבטחנו.", do=show("x-c1")),
    P("והמלכודת: מי שמחלק ב-$\\lambda$ במקום ב-$\\sigma$, למשל בשש במקום בשורש שש, מקבל וקטור באורך לא נכון.",
      do=show("x-c2"), hold=0.6,
      say="והמלכודת: מי שמחלק בלַמְדָא במקום בסִיגְמָא, למשל בשש במקום בשורש שש, מקבל וקטור באורך לא נכון."),
], stage=w.lines(w.line("x-1", r"Av_1=" + w.svec((2, 2, 2), 2), "small"),
                 w.line("x-2", r"u_1=\frac{1}{\sqrt{6}}Av_1=" + w.nvec((1, 1, 1)), "hl"),
                 w.line("x-3", r"Av_2=" + w.svec((2, 0, -2), 2), "small"),
                 w.line("x-4", r"u_2=\frac{1}{2}Av_2=" + w.nvec((1, 0, -1)), "hl"), cls="tight"),
   panel=QSTEM + st.card("x-c1", "ex", "$u_1\\cdot u_2=0$, $\\|u_1\\|=\\|u_2\\|=1$ ✓")
         + st.card("x-c2", "trap", "⚠️ מחלקים ב-$\\sigma_i$, לא ב-$\\lambda_i$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $u_i$ שווה $A$ כפול $v_i$, חלקי $\\sigma_i$.", do=show("r-1"),
      say="לסיכום: יוּ אַיי שווה אֵיי כפול וִי אַיי, חלקי סִיגְמָא אַיי."),
    P("האורך יוצא אחת, והניצבות מובטחת.", do=show("r-2")),
    P("הנוסחה קובעת את הסימן. פירוק נפרד של $AA^T$ יכול להפוך סימן ולהרוס את הפירוק.", do=show("r-3"),
      say="הנוסחה קובעת את הסימן. פירוק נפרד של אֵיי אֵיי טְרַנְסְפּוֹז יכול להפוך סימן ולהרוס את הפירוק."),
    P("והיא רק לערכים סינגולריים שונים מאפס. את השאר נשלים בשלב הבא.", do=show("r-4"), hold=0.6),
], stage=w.lines(w.line("r-f", r"u_i=\frac{1}{\sigma_i}Av_i", "big", hidden=False)),
   panel=st.card("r-1", "rule", "🔑 $u_i=\\frac{1}{\\sigma_i}Av_i$")
         + st.card("r-2", "rule", "🔑 אורך $1$, ניצבות מובטחת")
         + st.card("r-3", "trap", "⚠️ לא בפירוק נפרד: סימנים")
         + st.card("r-4", "trap", "⚠️ רק ל-$\\sigma_i\\ne0$"))

VIDEO = Video("V05", "svd", "העמודות של U: uᵢ = Avᵢ / σᵢ",
              [title, formula, ex1, trap, exam, recap], bank={})
