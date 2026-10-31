# -*- coding: utf-8 -*-
"""V03 · ערכים סינגולריים והמטריצה S — video script (build: tools/video/vid.py V03).

Source: courses/svd/C03.js (lesson + goal: compute the singular values and build S of the right size).
Exam anchor: none (the three free svd exam parts are solved in full in V02 and V08). The skill is shown on an original
question "בסגנון מבחן" (bank={}): the 2x3 [[2,1,1],[1,2,-1]], AA^T = [[6,3],[3,6]], lambda = 9, 3, S = diag(3, sqrt3)
padded with a zero column; the options are the classic mistakes (lambda instead of sigma, wrong order, wrong size).
Avoided on purpose: the C03 quiz matrices ([[1,2],[2,1],[0,0]], [[1,2],[2,4]], [[1,1,0],[0,1,1]]) and every quiz/boss
matrix of the course. Worked examples: the lesson's [[1,1],[0,1],[1,0]] and the original rank-1 [[2,0],[2,0],[1,0]].
All eigenvalues, sigmas and S are computed with sympy and asserted below.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide
import stage as st
import w_svd as w

M = sp.Matrix
L = sp.Symbol("lambda")
s3 = sp.sqrt(3)

# example 1 (lesson)
A1 = M([[1, 1], [0, 1], [1, 0]])
B1 = A1.T * A1
assert B1 == M([[2, 1], [1, 2]])
assert sp.expand((B1 - L * sp.eye(2)).det() - ((2 - L) ** 2 - 1)) == 0
assert w.eig_desc(B1) == [3, 1]
S1 = w.S_mat(3, 2, [s3, 1])

# example 2: rank 1
A2 = M([[2, 0], [2, 0], [1, 0]])
B2 = A2.T * A2
assert B2 == M([[9, 0], [0, 0]]) and w.eig_desc(B2) == [9, 0]
S2 = w.S_mat(3, 2, [3, 0])
assert A2.rank() == 1

# exam-style question
X = M([[2, 1, 1], [1, 2, -1]])
XX = X * X.T
assert XX == M([[6, 3], [3, 6]])
assert sp.expand((XX - L * sp.eye(2)).det() - ((6 - L) ** 2 - 9)) == 0
assert w.eig_desc(XX) == [9, 3] and w.eig_desc(X.T * X) == [9, 3, 0]
assert XX.trace() == sum(x ** 2 for x in X) == 12
SX = w.S_mat(2, 3, [3, s3])
assert sp.diag(*[w.sig(l) for l in w.eig_desc(XX)]) == SX[:, :2] and SX[:, 2] == sp.zeros(2, 1)
cand = {"a": SX, "b": w.S_mat(2, 3, [9, 3]), "c": w.S_mat(2, 3, [s3, 3]), "d": M([[3, 0], [0, s3]])}
assert [k for k, S in cand.items() if S.shape == X.shape and S == SX] == ["a"]
OPTS = [(k, f"${w.pm(S)}$") for k, S in cand.items()]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נחשב ערכים סינגולריים, ונבנה מהם את המטריצה $S$."),
    P("נראה מתכון בארבעה צעדים, מה קורה כשיש ערך עצמי אפס, ואיפה כולם טועים."),
    P("ובסוף נפתור שאלה בסגנון מבחן.", hold=0.4),
], stage='<div class="kicker">V03 · פירוק SVD</div><h1>ערכים סינגולריים והמטריצה $S$</h1>'
         '<p>לחשב את הערכים הסינגולריים של מטריצה, ולבנות מהם את $S$ בגודל הנכון.</p>', layout="title")

recipe = Scene("recipe", "המתכון", [
    P("הערכים הסינגולריים באים מהערכים העצמיים של הקטנה מבין $A^TA$ ו-$AA^T$.",
      say="הערכים הסינגולריים באים מהערכים העצמיים של הקטנה מבין אֵיי טְרַנְסְפּוֹז אֵיי ואֵיי אֵיי טְרַנְסְפּוֹז."),
    P("צעד ראשון: מחשבים את המטריצה הקטנה.", do=show("m-1")),
    P("צעד שני: מוצאים את הערכים העצמיים, מהפולינום האופייני.", do=show("m-2")),
    P("צעד שלישי: מסדרים אותם מהגדול לקטן, ומוציאים שורש.", do=show("m-3")),
    P("למה מותר להוציא שורש? כי לערכים העצמיים של $A^TA$ אין אף פעם ערך שלילי.", do=show("m-c1"),
      say="למה מותר להוציא שורש? כי לערכים העצמיים של אֵיי טְרַנְסְפּוֹז אֵיי אין אף פעם ערך שלילי."),
    P("צעד רביעי: בונים את $S$ בגודל של $A$, עם הערכים הסינגולריים על האלכסון, ואפסים בכל השאר.", do=show("m-4"),
      say="צעד רביעי: בונים את אֶס בגודל של אֵיי, עם הערכים הסינגולריים על האלכסון, ואפסים בכל השאר."),
], stage=w.lines(w.line("m-1", r"1.\ \ A^TA\ \ /\ \ AA^T", "small"),
                 w.line("m-2", r"2.\ \ \det(M-\lambda I)=0", "small"),
                 w.line("m-3", r"3.\ \ \lambda_1\ge\lambda_2\ge\dots,\quad \sigma_i=\sqrt{\lambda_i}", "small"),
                 w.line("m-4", r"4.\ \ S_{m\times n}:\ \ S_{ii}=\sigma_i", "small"), cls="left"),
   panel=st.card("m-c1", "rule", "🔑 הערכים העצמיים של $A^TA$ תמיד $\\ge 0$"))

ex1 = Scene("ex1", "דוגמה", [
    P("נתחיל במטריצה של הקורס: שלוש שורות ושתי עמודות.", do=show("a-A")),
    P("שתי עמודות, ולכן הקטנה היא $A^TA$, שתיים על שתיים: שתיים, אחת, אחת, שתיים.", do=show("a-1"),
      say="שתי עמודות, ולכן הקטנה היא אֵיי טְרַנְסְפּוֹז אֵיי, שתיים על שתיים: שתיים, אחת, אחת, שתיים."),
    P("הפולינום האופייני: שתיים פחות למדא, בריבוע, פחות אחת. הוא מתאפס בשלוש ובאחת.", do=show("a-2")),
    P("ולכן $\\sigma_1$ שורש שלוש, ו-$\\sigma_2$ אחת.", do=show("a-3"),
      say="ולכן סִיגְמָא אחת שורש שלוש, וסִיגְמָא שתיים אחת."),
    P("$A$ היא שלוש על שתיים, ולכן גם $S$: שני הערכים על האלכסון, ושורת אפסים מתחת.", do=show("a-4"),
      say="אֵיי היא שלוש על שתיים, ולכן גם אֶס: שני הערכים על האלכסון, ושורת אפסים מתחת."),
    P("ושימו לב: על האלכסון עומד שורש שלוש, ולא שלוש. שם יושב $\\sigma$, לא $\\lambda$.", do=show("a-c1"),
      hold=0.4, say="ושימו לב: על האלכסון עומד שורש שלוש, ולא שלוש. שם יושב סִיגְמָא, לא לַמְדָא."),
], stage=w.lines(w.line("a-A", "A=" + w.pm(A1)),
                 w.line("a-1", "A^TA=" + w.pm(B1), "small"),
                 w.line("a-2", r"(2-\lambda)^2-1=0\ \Rightarrow\ \lambda=3,\ 1", "small"),
                 w.line("a-3", r"\sigma_1=\sqrt{3},\quad \sigma_2=1", "hl"),
                 w.line("a-4", "S=" + w.pm(S1)), cls="tight"),
   panel=st.card("a-c1", "trap", "⚠️ על האלכסון $\\sqrt{\\lambda}$, לא $\\lambda$"))

ex2 = Scene("ex2", "ערך עצמי אפס", [
    P("ועכשיו מטריצה שבה העמודה השנייה כולה אפסים.", do=show("b-A")),
    P("$A^TA$ יוצאת אלכסונית: תשע ואפס. הערכים העצמיים תשע ואפס.", do=show("b-1"),
      say="אֵיי טְרַנְסְפּוֹז אֵיי יוצאת אלכסונית: תשע ואפס. הערכים העצמיים תשע ואפס."),
    P("ולכן $\\sigma_1$ שלוש, ו-$\\sigma_2$ אפס.", do=show("b-2"),
      say="ולכן סִיגְמָא אחת שלוש, וסִיגְמָא שתיים אפס."),
    P("אפס הוא ערך סינגולרי חוקי. הוא נכנס לאלכסון של $S$, במקום השני.", do=show("b-3"),
      say="אפס הוא ערך סינגולרי חוקי. הוא נכנס לאלכסון של אֶס, במקום השני."),
    P("ומספר הערכים הסינגולריים השונים מאפס הוא הדרגה: כאן אחת.", do=show("b-c1")),
    P("וזה מתאים: העמודה השנייה אפס, ולכן יש רק עמודה אחת בלתי תלויה.", hold=0.4),
], stage=w.lines(w.line("b-A", "A=" + w.pm(A2)),
                 w.line("b-1", "A^TA=" + w.pm(B2) + r"\ \Rightarrow\ \lambda=9,\ 0", "small"),
                 w.line("b-2", r"\sigma_1=3,\quad \sigma_2=0", "hl"),
                 w.line("b-3", "S=" + w.pm(S2)), cls="tight"),
   panel=st.card("b-c1", "rule", "🔑 מספר ה-$\\sigma_i\\ne0$ = הדרגה. כאן $1$"))

traps = Scene("traps", "מלכודות", [
    P("שלוש טעויות שחוזרות בבניית $S$.", say="שלוש טעויות שחוזרות בבניית אֶס."),
    P("ראשונה: לשים על האלכסון את $\\lambda$ במקום את השורש שלו.", do=show("t-1"),
      say="ראשונה: לשים על האלכסון את לַמְדָא במקום את השורש שלו."),
    P("שנייה: לשכוח את הסדר היורד. הגדול תמיד ראשון.", do=show("t-2")),
    P("שלישית: לבנות $S$ ריבועית. היא תמיד בגודל של $A$, גם כשזה אומר שורה או עמודה של אפסים.", do=show("t-3"),
      hold=0.4, say="שלישית: לבנות אֶס ריבועית. היא תמיד בגודל של אֵיי, גם כשזה אומר שורה או עמודה של אפסים."),
], stage=w.lines(w.line("t-f", r"S_{ii}=\sigma_i=\sqrt{\lambda_i}", "big", hidden=False)),
   panel=st.card("t-1", "trap", "⚠️ $\\sigma_i=\\sqrt{\\lambda_i}$, לא $\\lambda_i$")
         + st.card("t-2", "trap", "⚠️ $\\sigma_1\\ge\\sigma_2\\ge\\dots$")
         + st.card("t-3", "trap", "⚠️ $S$ בגודל $m\\times n$ של $A$"))

QSTEM = ('<div class="qstem sv-small"><span class="qid">בסגנון מבחן</span>'
         f'$A={w.pm(X)}$. מהי $S$ בפירוק SVD של $A$?</div>')
exam = Scene("exam", "שאלה בסגנון מבחן", [
    P("שאלה בסגנון מבחן: מהי $S$ בפירוק של המטריצה הזו?", say="שאלה בסגנון מבחן: מהי אֶס בפירוק של המטריצה הזו?"),
    P("שתי שורות ושלוש עמודות, ולכן עובדים עם $AA^T$, שתיים על שתיים.", do=show("x-1"),
      say="שתי שורות ושלוש עמודות, ולכן עובדים עם אֵיי אֵיי טְרַנְסְפּוֹז, שתיים על שתיים."),
    P("יוצא שש, שלוש, שלוש, שש. הפולינום: שש פחות למדא, בריבוע, פחות תשע.", do=show("x-2")),
    P("הוא מתאפס בתשע ובשלוש. בדיקה: תשע ועוד שלוש זה שתים עשרה, סכום הריבועים של הכניסות.", do=show("x-3")),
    P("שורש תשע זה שלוש, ושורש שלוש נשאר שורש שלוש.", do=show("x-4")),
    P("מי ששם תשע ושלוש על האלכסון, שכח להוציא שורש.", do=show("q-x-b", "q-n-b")),
    P("מי ששם קודם את שורש שלוש, שכח את הסדר היורד.", do=show("q-x-c", "q-n-c")),
    P("ו-$S$ שתיים על שתיים היא בגודל לא נכון: $A$ שתיים על שלוש, ולכן צריך עמודת אפסים.", do=show("q-x-d", "q-n-d"),
      say="ואֶס שתיים על שתיים היא בגודל לא נכון: אֵיי שתיים על שלוש, ולכן צריך עמודת אפסים."),
    P("התשובה: שלוש ושורש שלוש על האלכסון, ועמודה שלישית של אפסים.", do=show("q-ok-a"), hold=0.6),
], stage=w.lines(w.line("x-1", r"m=2<n=3\ \Rightarrow\ AA^T", "small"),
                 w.line("x-2", "AA^T=" + w.pm(XX) + r",\quad (6-\lambda)^2-9=0", "small"),
                 w.line("x-3", r"\lambda_1=9,\ \lambda_2=3,\qquad 9+3=12=\textstyle\sum a_{ij}^2", "small"),
                 w.line("x-4", r"\sigma_1=3,\quad \sigma_2=\sqrt{3}", "hl"), cls="tight"),
   panel=QSTEM + '<div class="sv-optgrid">' + st.options("q", OPTS, notes={"b": "בלי שורש", "c": "סדר הפוך", "d": "גודל שגוי"}) + "</div>")

recap = Scene("recap", "סיכום", [
    P("לסיכום: מוצאים ערכים עצמיים של המטריצה הקטנה, ומסדרים מהגדול לקטן.", do=show("r-1")),
    P("$\\sigma_i$ הוא השורש של $\\lambda_i$, ועליו בונים את האלכסון של $S$.", do=show("r-2"),
      say="סִיגְמָא אַיי הוא השורש של לַמְדָא אַיי, ועליו בונים את האלכסון של אֶס."),
    P("$S$ בגודל של $A$, עם אפסים בכל השאר.", do=show("r-3"),
      say="אֶס בגודל של אֵיי, עם אפסים בכל השאר."),
    P("ומספר הערכים הסינגולריים השונים מאפס הוא הדרגה. נתראה בשלב הבא.", do=show("r-4"), hold=0.6),
], stage=w.lines(w.line("r-f", r"\sigma_i=\sqrt{\lambda_i}", "big", hidden=False)),
   panel=st.card("r-1", "rule", "🔑 $\\lambda_1\\ge\\lambda_2\\ge\\dots$ של הקטנה")
         + st.card("r-2", "rule", "🔑 $S_{ii}=\\sigma_i=\\sqrt{\\lambda_i}$")
         + st.card("r-3", "rule", "🔑 $S$ מסדר $m\\times n$")
         + st.card("r-4", "rule", "🔑 דרגה = מספר ה-$\\sigma_i\\ne0$"))

VIDEO = Video("V03", "svd", "ערכים סינגולריים והמטריצה S",
              [title, recipe, ex1, ex2, traps, exam, recap], bank={})
