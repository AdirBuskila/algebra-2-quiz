# -*- coding: utf-8 -*-
"""V07 · סימנים, סדר ובדיקה של U·S·Vᵀ = A — video script (build: tools/video/vid.py V07).

Source: courses/svd/C07.js (lesson + goal: which changes keep a decomposition valid, how to verify one, and how to find
the error in a check). Exam anchor: none (the three free svd exam parts are solved in V02 and V08; 25A-B-Q1b is this
level's quiz item). Original question "בסגנון מבחן" (bank={}): a student's SVD of A = [[3,0],[4,5]] whose u_2 has the
wrong sign: U, V orthogonal and the sigmas right, but A v_2 = -sigma_2 u_2 and U S V^T != A.
Avoided on purpose: the C07 quiz ([[1,2],[2,1],[0,0]] changes, [[2,0],[0,1]], the check of [[1,1],[0,1],[1,0]],
[[3,1],[1,3],[0,0]]) and every quiz/boss matrix. Worked example: [[2,0],[1,1],[0,2]] from the V05 question, now complete.
Every claim (valid / invalid change, the student's error) is decided by w_svd.check_svd in sympy.
"""
import sympy as sp
from vid import P, Scene, Video, show, hide
import stage as st
import w_svd as w

M = sp.Matrix
s2, s3, s5, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(5), sp.sqrt(6)


def valid(A, U, S, V):
    try:
        return w.check_svd(A, U, S, V)
    except AssertionError:
        return False


def prod_ok(A, U, S, V):
    return sp.simplify(U * S * V.T - A) == sp.zeros(*A.shape)


# worked example: complete SVD of [[2,0],[1,1],[0,2]] (the V05 question)
A = M([[2, 0], [1, 1], [0, 2]])
Utex, U = w.cols((1, 1, 1), (1, 0, -1), (1, -2, 1))
Vtex, V = w.cols((1, 1), (1, -1))
S = w.S_mat(3, 2, [s6, 2])
assert valid(A, U, S, V)
assert M([1, 1, 1]).cross(M([1, 0, -1])) == -M([1, -2, 1])
assert sum(x ** 2 for x in A) == 10 == 6 + 4


def flip(Q, *cols_):
    Q = Q.copy()
    for c in cols_:
        Q[:, c] = -Q[:, c]
    return Q


assert valid(A, flip(U, 0), S, flip(V, 0))                           # flip a pair: fine
assert not prod_ok(A, U, S, flip(V, 0))                                # flip v_1 alone: broken
assert sp.simplify(A * flip(V, 0)[:, 0] + s6 * U[:, 0]) == sp.zeros(3, 1)
assert valid(A, flip(U, 2), S, V)                                      # u_3 (sigma = 0 side) is free
Usw = M.hstack(U[:, 1], U[:, 0], U[:, 2])
Vsw = M.hstack(V[:, 1], V[:, 0])
Ssw = w.S_mat(3, 2, [2, s6])
assert prod_ok(A, Usw, Ssw, Vsw) and not valid(A, Usw, Ssw, Vsw)     # swapped order: product ok, not a valid SVD
assert not prod_ok(A, Usw, S, Vsw)                                     # swapping only the columns breaks the product

# exam-style: a student's decomposition of [[3,0],[4,5]]
X = M([[3, 0], [4, 5]])
assert X.T * X == M([[25, 20], [20, 25]]) and w.eig_desc(X.T * X) == [45, 5]
sg = [3 * s5, s5]
assert [w.sig(l) for l in [45, 5]] == sg
assert sum(x ** 2 for x in X) == 50 == 45 + 5
XVtex, XV = w.cols((1, 1), (1, -1))
XU_ok_tex, XU_ok = w.cols((1, 3), (3, -1))
XS = w.S_mat(2, 2, sg)
assert valid(X, XU_ok, XS, XV)
XU_st_tex, XU_st = w.cols((1, 3), (-3, 1))                            # the student's U: u_2 flipped
assert w.is_orth(XU_st) and w.is_orth(XV)
assert not prod_ok(X, XU_st, XS, XV)
assert sp.simplify(X * XV[:, 0] - sg[0] * XU_st[:, 0]) == sp.zeros(2, 1)
assert sp.simplify(X * XV[:, 1] + sg[1] * XU_st[:, 1]) == sp.zeros(2, 1)
assert valid(X, XU_st, XS, flip(XV, 1))                               # fixing either one of the pair works
OPTS = [("a", "הפירוק נכון"),
        ("b", "שגוי: הסימן של $u_2$ לא מתאים ל-$v_2$"),
        ("c", "שגוי: הערכים הסינגולריים"),
        ("d", "שגוי: $V$ אינה אורתוגונלית")]
truth = {"a": prod_ok(X, XU_st, XS, XV),
         "b": sp.simplify(X * XV[:, 1] + sg[1] * XU_st[:, 1]) == sp.zeros(2, 1),
         "c": w.eig_desc(X.T * X) != [s ** 2 for s in sg],
         "d": not w.is_orth(XV)}
assert [k for k, v in truth.items() if v] == ["b"]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("פירוק SVD אינו יחיד. שני פתרונות שונים יכולים להיות נכונים שניהם."),
    P("בסרטון הזה נראה מה מותר לשנות בפירוק ומה אסור, ואיך בודקים פירוק שמצאתם."),
    P("ובסוף נמצא טעות בפירוק של סטודנט.", hold=0.4),
], stage='<div class="kicker">V07 · פירוק SVD</div><h1>סימנים, סדר ובדיקה של $USV^T=A$</h1>'
         '<p>לדעת אילו שינויים בפירוק מותרים, לאמת פירוק שנמצא, ולמצוא טעות בבדיקה.</p>', layout="title")

full = Scene("full", "פירוק מלא", [
    P("נתחיל מפירוק מלא של המטריצה מהשאלה בסרטון על $U$. את $u_3$ השלמנו במכפלה וקטורית.", do=show("e-A", "e-eq", "e-U", "e-S", "e-Vt"),
      say="נתחיל מפירוק מלא של המטריצה מהשאלה בסרטון על יוּ. את יוּ שלוש השלמנו במכפלה וקטורית."),
    P("מה **קבוע** כאן? הערכים הסינגולריים: שורש שש ושתיים, ובסדר יורד.", do=show("e-c1")),
    P("כל השאר תלוי בבחירות שלנו. נעבור עליהן אחת אחת.", hold=0.3),
], stage=w.lines(w.assembly("e", w.pm(A), Utex, w.pm(S), w.cols_T((1, 1), (1, -1))[0]),
                 w.row(st.card("e-c1", "rule", "🔑 קבוע: $\\sigma_1=\\sqrt6\\ge\\sigma_2=2$"))), layout="full")

moves = Scene("moves", "מה מותר", [
    P("שינוי ראשון: הופכים את הסימן של $u_1$ **וגם** של $v_1$.", do=show("m-1"),
      say="שינוי ראשון: הופכים את הסימן של יוּ אחת וגם של וִי אחת."),
    P("בשני הצדדים של $A v_1$ שווה $\\sigma_1 u_1$ מופיע מינוס, והוא מתבטל. הפירוק נשאר נכון.", do=show("m-1v"),
      say="בשני הצדדים של אֵיי וִי אחת שווה סִיגְמָא אחת יוּ אחת מופיע מינוס, והוא מתבטל. הפירוק נשאר נכון."),
    P("שינוי שני: הופכים רק את $v_1$. עכשיו $A v_1$ שווה **מינוס** $\\sigma_1 u_1$, והמכפלה כבר לא $A$.", do=show("m-2", "m-2v"),
      say="שינוי שני: הופכים רק את וִי אחת. עכשיו אֵיי וִי אחת שווה מינוס סִיגְמָא אחת יוּ אחת, והמכפלה כבר לא אֵיי."),
    P("שינוי שלישי: הופכים את $u_3$, העמודה שהשלמנו. מותר: היא נכפלת באפסים של $S$.", do=show("m-3", "m-3v"),
      say="שינוי שלישי: הופכים את יוּ שלוש, העמודה שהשלמנו. מותר: היא נכפלת באפסים של אֶס."),
    P("שינוי רביעי: מחליפים את הסדר של העמודות בשלוש המטריצות יחד. המכפלה עדיין $A$.", do=show("m-4"),
      say="שינוי רביעי: מחליפים את הסדר של העמודות בשלוש המטריצות יחד. המכפלה עדיין אֵיי."),
    P("אבל על האלכסון יופיע קודם שתיים ואז שורש שש: זה לא סדר יורד, ולכן זה לא פירוק SVD תקין.", do=show("m-4v"),
      hold=0.4),
], stage=w.lines(w.line("m-1", r"(u_1,v_1)\to({-u_1},{-v_1})", "small"),
                 w.line("m-2", r"v_1\to{-v_1},\quad u_1\to u_1", "small"),
                 w.line("m-3", r"u_3\to{-u_3}", "small"),
                 w.line("m-4", r"(\sigma_1,\sigma_2)\to(2,\sqrt{6})", "small"), cls="tight"),
   panel=st.card("m-1v", "rule", "✓ זוג יחד: מותר")
         + st.card("m-2v", "trap", "✗ רק אחד מהזוג: אסור")
         + st.card("m-3v", "rule", "✓ עמודה מושלמת ($\\sigma=0$): חופשית")
         + st.card("m-4v", "trap", "✗ סדר שאינו יורד: לא תקין"))

check = Scene("check", "בדיקה", [
    P("איך בודקים פירוק שמצאתם? שלוש בדיקות, מהמהירה לאיטית."),
    P("מהירה: לכל ערך סינגולרי שונה מאפס, $A v_i$ שווה $\\sigma_i u_i$. היא בודקת גם את הסימנים.", do=show("k-1"),
      say="מהירה: לכל ערך סינגולרי שונה מאפס, אֵיי וִי אַיי שווה סִיגְמָא אַיי יוּ אַיי. היא בודקת גם את הסימנים."),
    P("כאן: $A v_1$ יוצא שתיים, שתיים, שתיים, חלקי שורש שתיים. וזה בדיוק שורש שש כפול $u_1$.", do=show("k-1e"),
      say="כאן: אֵיי וִי אחת יוצא שתיים, שתיים, שתיים, חלקי שורש שתיים. וזה בדיוק שורש שש כפול יוּ אחת."),
    P("בדיקת ביטחון: סכום ריבועי הערכים הסינגולריים שווה לסכום ריבועי כל הכניסות של $A$.", do=show("k-2"),
      say="בדיקת ביטחון: סכום ריבועי הערכים הסינגולריים שווה לסכום ריבועי כל הכניסות של אֵיי."),
    P("שש ועוד ארבע זה עשר. וארבע ועוד אחת ועוד אחת ועוד ארבע, גם עשר.", do=show("k-2e")),
    P("והבדיקה המלאה: לכפול $U S V^T$, ולוודא ש-$U$ ו-$V$ אורתוגונליות.", do=show("k-3"),
      say="והבדיקה המלאה: לכפול יוּ אֶס וִי טְרַנְסְפּוֹז, ולוודא שיוּ ווִי אורתוגונליות."),
    P("שימו לב: אורתוגונליות לבדה לא מספיקה. היא לא רואה סימן הפוך.", do=show("k-c1"), hold=0.4),
], stage=w.lines(w.line("k-1", r"Av_i=\sigma_iu_i", "big"),
                 w.line("k-1e", r"Av_1=" + w.svec((2, 2, 2), 2) + r"=\sqrt{6}\cdot" + w.nvec((1, 1, 1)), "small"),
                 w.line("k-2", r"\textstyle\sum\sigma_i^2=\sum a_{ij}^2", "small"),
                 w.line("k-2e", r"6+4=10=4+1+1+4", "small"),
                 w.line("k-3", r"USV^T=A,\quad U^TU=I,\quad V^TV=I", "small"), cls="tight"),
   panel=st.card("k-c1", "trap", "⚠️ $U$, $V$ אורתוגונליות ≠ פירוק נכון"))

QSTEM = ('<div class="qstem sv-small"><span class="qid">בסגנון מבחן</span>'
         f'סטודנט פירק את $A={w.pm(X)}$ וקיבל את $U$, $S$, $V$ שעל המסך. מה נכון?</div>')
exam = Scene("exam", "שאלה בסגנון מבחן", [
    P("שאלה בסגנון מבחן: סטודנט פירק את המטריצה הזו. האם הפירוק שלו נכון?"),
    P("קודם, בדיקת ביטחון: תשע ועוד שש עשרה ועוד עשרים וחמש, חמישים.", do=show("x-1")),
    P("והערכים הסינגולריים בריבוע: ארבעים וחמש ועוד חמש, גם חמישים. הערכים נכונים.", do=show("q-x-c", "q-n-c")),
    P("העמודות של $V$ באורך אחת וניצבות, וגם של $U$. אז $V$ אורתוגונלית.", do=show("q-x-d", "q-n-d"),
      say="העמודות של וִי באורך אחת וניצבות, וגם של יוּ. אז וִי אורתוגונלית."),
    P("עכשיו הבדיקה המהירה. $A v_1$ שווה שלוש שורש חמש כפול $u_1$. מצוין.", do=show("x-2"),
      say="עכשיו הבדיקה המהירה. אֵיי וִי אחת שווה שלוש שורש חמש כפול יוּ אחת. מצוין."),
    P("אבל $A v_2$ יוצא שלוש, מינוס אחת, חלקי שורש שתיים. וזה **מינוס** שורש חמש כפול $u_2$ של הסטודנט.", do=show("x-3"),
      say="אבל אֵיי וִי שתיים יוצא שלוש, מינוס אחת, חלקי שורש שתיים. וזה מינוס שורש חמש כפול יוּ שתיים של הסטודנט."),
    P("הסימן של $u_2$ לא מתאים ל-$v_2$, ולכן המכפלה לא נותנת את $A$.", do=show("q-x-a", "q-n-a", "q-ok-b"),
      say="הסימן של יוּ שתיים לא מתאים לוִי שתיים, ולכן המכפלה לא נותנת את אֵיי."),
    P("כנראה הוא מצא את $U$ בפירוק נפרד של $AA^T$. התיקון: להפוך את $u_2$, או את $v_2$. רק אחד מהם.", do=show("x-c1"),
      hold=0.6, say="כנראה הוא מצא את יוּ בפירוק נפרד של אֵיי אֵיי טְרַנְסְפּוֹז. התיקון: להפוך את יוּ שתיים, או את וִי שתיים. רק אחד מהם."),
], stage=w.lines(w.line("x-0", "U=" + XU_st_tex + r",\ \ S=" + w.pm(XS) + r",\ \ V=" + XVtex, "small", hidden=False),
                 w.line("x-1", r"9+16+25=50=45+5", "small"),
                 w.line("x-2", r"Av_1=" + w.svec((3, 9), 2) + r"=3\sqrt{5}\,u_1\ \checkmark", "small"),
                 w.line("x-3", r"Av_2=" + w.svec((3, -1), 2) + r"={-\sqrt{5}}\,u_2", "bad"),
                 st.card("x-c1", "trap", "⚠️ מתקנים את <b>אחד</b> מהזוג: $u_2$ או $v_2$"), cls="tight"),
   panel=QSTEM + st.options("q", OPTS, notes={"a": "$Av_2={-\\sigma_2}u_2$", "c": "$45+5=50$", "d": "היא כן"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: הערכים הסינגולריים קבועים, ובסדר יורד.", do=show("r-1")),
    P("מותר להפוך סימן של זוג, $u_i$ ו-$v_i$ יחד, ולבחור בחופשיות את העמודות המושלמות.", do=show("r-2"),
      say="מותר להפוך סימן של זוג, יוּ אַיי ווִי אַיי יחד, ולבחור בחופשיות את העמודות המושלמות."),
    P("אסור להפוך רק אחד מהזוג.", do=show("r-3")),
    P("ובודקים עם $A v_i$ שווה $\\sigma_i u_i$, כי אורתוגונליות לבדה לא תופסת סימן. נתראה בשלב האחרון.", do=show("r-4"),
      hold=0.6, say="ובודקים עם אֵיי וִי אַיי שווה סִיגְמָא אַיי יוּ אַיי, כי אורתוגונליות לבדה לא תופסת סימן. נתראה בשלב האחרון."),
], stage=w.lines(w.line("r-f", r"Av_i=\sigma_iu_i", "big", hidden=False)),
   panel=st.card("r-1", "rule", "🔑 $\\sigma_1\\ge\\sigma_2\\ge\\dots$ קבועים")
         + st.card("r-2", "rule", "🔑 $(u_i,v_i)\\to(-u_i,-v_i)$ מותר")
         + st.card("r-3", "trap", "⚠️ רק $u_i$ או רק $v_i$: אסור")
         + st.card("r-4", "rule", "🔑 בודקים $Av_i=\\sigma_iu_i$"))

VIDEO = Video("V07", "svd", "סימנים, סדר ובדיקה של U·S·Vᵀ = A",
              [title, full, moves, check, exam, recap], bank={})
