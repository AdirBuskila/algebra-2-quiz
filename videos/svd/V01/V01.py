# -*- coding: utf-8 -*-
"""V01 · מהו פירוק SVD ואיך נראות המטריצות — video script (build: tools/video/vid.py V01).

Source: courses/svd/C01.js (lesson + goal: write A = U S V^T, the sizes of U, S, V, the rank from S).
Exam anchor: none. The svd bank has three exam parts that no level uses (23A-A-Q5a, 24A-C-Q3a, 25A-A-Q5a); each is a
full decomposition and they are solved in V02 and in the boss walkthrough V08. This level's skill (sizes + rank) is
shown on an original question "בסגנון מבחן" (bank={}).
Avoided on purpose: the C01 quiz (4x3 sizes, V of a 2x5, S = diag(4,2,0), the four forms of the product, the four S
candidates of a 2x3) and every quiz/boss matrix of the course.
Examples: the course's running example A = [[1,1],[0,1],[1,0]] (lessons C03-C07) as a finished decomposition, and the
all-ones 3x2 matrix for the rank. Every decomposition shown is asserted by w_svd.check_svd (exact sympy).
"""
import sympy as sp
from vid import P, Scene, Video, show, hide
import stage as st
import w_svd as w

M = sp.Matrix
s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)

# ---------------------------------------------------------------- verified objects
# running example (lessons C03..C07)
A1 = M([[1, 1], [0, 1], [1, 0]])
U1_tex, U1 = w.cols((2, 1, 1), (0, -1, 1), (1, -1, -1))
V1_tex, V1 = w.cols((1, 1), (1, -1))
Vt1_tex, Vt1 = w.cols_T((1, 1), (1, -1))
S1 = w.S_mat(3, 2, [s3, 1])
assert w.check_svd(A1, U1, S1, V1) and Vt1 == V1.T
assert w.eig_desc(A1.T * A1) == [3, 1]

# rank example: all ones, 3x2
A2 = M([[1, 1], [1, 1], [1, 1]])
_, U2 = w.cols((1, 1, 1), (1, -1, 0), (1, 1, -2))
_, V2 = w.cols((1, 1), (1, -1))
S2 = w.S_mat(3, 2, [s6, 0])
assert w.check_svd(A2, U2, S2, V2)
assert A2.rank() == 1 == sum(1 for i in range(2) if S2[i, i] != 0)

# exam-style question: S is given, 2x4
SX = M([[5, 0, 0, 0], [0, 0, 0, 0]])
mX, nX = SX.shape
rX = sum(1 for i in range(min(mX, nX)) if SX[i, i] != 0)
assert (mX, nX, rX) == (2, 4, 1)
OPTS = [("a", "$A$ מסדר $2\\times4$, ודרגתה $1$"),
        ("b", "$A$ מסדר $4\\times2$, ודרגתה $1$"),
        ("c", "$U$ מסדר $4\\times4$ ו-$V$ מסדר $2\\times2$"),
        ("d", "$A$ מסדר $2\\times4$, ודרגתה $2$")]
truth = {"a": (mX, nX) == (2, 4) and rX == 1, "b": (mX, nX) == (4, 2) and rX == 1,
         "c": mX == 4 and nX == 2, "d": (mX, nX) == (2, 4) and rX == 2}
assert [k for k, v in truth.items() if v] == ["a"]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את פירוק SVD: לכל מטריצה, בכל גודל."),
    P("נבין מה הגודל של כל אחת משלוש המטריצות בפירוק, ואיך קוראים ממנו את הדרגה."),
    P("ובסוף נפתור שאלה בסגנון מבחן.", hold=0.4),
], stage='<div class="kicker">V01 · פירוק SVD</div><h1>מהו פירוק SVD ואיך נראות המטריצות</h1>'
         '<p>לכתוב $A=USV^T$, לקבוע את הגדלים של $U$, $S$ ו-$V$, ולקרוא את הדרגה מתוך $S$.</p>', layout="title")

idea = Scene("idea", "הרעיון", [
    P("לכסון רגיל עובד רק למטריצות ריבועיות, וגם אז לא תמיד.", do=show("i-c0")),
    P("לפירוק SVD אין הגבלה: **לכל** מטריצה ממשית, גם לא ריבועית, יש פירוק כזה.", do=show("i-f")),
    P("$A$ שווה $U$ כפול $S$ כפול $V^T$.",
      say="אֵיי שווה יוּ, כפול אֶס, כפול וִי טְרַנְסְפּוֹז."),
    P("$U$ ו-$V$ הן מטריצות **אורתוגונליות**: העמודות שלהן באורך אחת, וניצבות זו לזו.", do=show("i-c1")),
    P("$S$ אלכסונית: על האלכסון שלה עומדים **הערכים הסינגולריים**, וכל השאר אפסים.", do=show("i-c2")),
    P("בדף הנוסחאות של הקורס כותבים $S$. בספרים רבים כותבים במקומה סיגמא גדולה, וזה אותו דבר.", do=show("i-c3"),
      hold=0.4),
], stage=w.lines(w.line("i-f", "A = U\\,S\\,V^T", "big"),
                 w.note("i-c3", "בספרים: $A=U\\Sigma V^T$, אותו פירוק")),
   panel=st.card("i-c0", "plain", "לכסון: רק מטריצה ריבועית, ולא כל אחת")
         + st.card("i-c1", "rule", "$U$, $V$ אורתוגונליות: $U^TU=I$, $V^TV=I$")
         + st.card("i-c2", "rule", "$S$ אלכסונית: $\\sigma_1\\ge\\sigma_2\\ge\\dots\\ge0$"))

sizes = Scene("sizes", "הגדלים", [
    P("נניח ש-$A$ היא מטריצה עם שלוש שורות ושתי עמודות.", do=show("z-A"),
      say="נניח שאֵיי היא מטריצה עם שלוש שורות ושתי עמודות."),
    P("$U$ שייכת לצד של השורות, ולכן היא ריבועית בגודל שלוש על שלוש.", do=show("z-eq", "z-U", "z-c1")),
    P("$V$ שייכת לצד של העמודות, ולכן היא שתיים על שתיים.", do=show("z-Vt", "z-c2")),
    P("ו-$S$, באמצע, היא **בגודל של $A$ עצמה**: שלוש על שתיים.", do=show("z-S", "z-c3"),
      say="ואֶס, באמצע, היא בגודל של אֵיי עצמה: שלוש על שתיים."),
    P("רק כך הכפל מסתדר: שלוש על שלוש, כפול שלוש על שתיים, כפול שתיים על שתיים, נותן שלוש על שתיים.", do=show("z-m")),
    P("ב-$S$ יש רק שני מקומות על האלכסון, ולכן שני ערכים סינגולריים.", do=show("z-ex")),
    P("והשורה השלישית של $S$ כולה אפסים. זה תקין לגמרי, ולא טעות.", hold=0.4),
], stage=w.lines(w.shapes("z", 3, 2),
                 w.line("z-m", "(3\\times3)(3\\times2)(2\\times2) = 3\\times2", "small"),
                 w.line("z-ex", "S=\\begin{pmatrix}\\sigma_1&0\\\\0&\\sigma_2\\\\0&0\\end{pmatrix}", "small")),
   panel=st.card("z-c1", "rule", "$U$: מסדר $m\\times m$ (שורות)")
         + st.card("z-c2", "rule", "$V$: מסדר $n\\times n$ (עמודות)")
         + st.card("z-c3", "rule", "🔑 $S$: מסדר $m\\times n$, כמו $A$"))

example = Scene("example", "פירוק אמיתי", [
    P("הנה פירוק אמיתי, של המטריצה שתלווה אותנו לאורך כל הקורס.", do=show("e-A", "e-eq")),
    P("$U$ שלוש על שלוש. כל עמודה שלה באורך אחת, והן ניצבות זו לזו.", do=show("e-U"),
      say="יוּ שלוש על שלוש. כל עמודה שלה באורך אחת, והן ניצבות זו לזו."),
    P("$S$ שלוש על שתיים, עם שורש שלוש ואחת על האלכסון, ושורת אפסים בסוף.", do=show("e-S"),
      say="אֶס שלוש על שתיים, עם שורש שלוש ואחת על האלכסון, ושורת אפסים בסוף."),
    P("ובסוף $V^T$, שתיים על שתיים: העמודות של $V$ כתובות בה כשורות.", do=show("e-Vt"),
      say="ובסוף וִי טְרַנְסְפּוֹז, שתיים על שתיים: העמודות של וִי כתובות בה כשורות."),
    P("אם תכפילו את שלושתן, תקבלו בדיוק את $A$.", do=show("e-c1")),
    P("הערכים הסינגולריים, $\\sqrt3$ ו-$1$, אי שליליים ובסדר יורד. כך זה תמיד.", do=show("e-c2"),
      say="הערכים הסינגולריים, שורש שלוש ואחת, אי שליליים ובסדר יורד. כך זה תמיד."),
    P("איך מוצאים את המטריצות האלה? את זה נבנה צעד אחר צעד בשלבים הבאים.", hold=0.4),
], stage=w.assembly("e", w.pm(A1), U1_tex, w.pm(S1), Vt1_tex),
   panel=st.card("e-c1", "ex", "$U\\cdot S\\cdot V^T = A$ בדיוק")
         + st.card("e-c2", "rule", "🔑 $\\sigma_1=\\sqrt3\\ \\ge\\ \\sigma_2=1\\ \\ge 0$"))

rank = Scene("rank", "הדרגה", [
    P("ומה עוד אפשר לקרוא מ-$S$? את **הדרגה** של $A$."),
    P("הדרגה שווה למספר הערכים הסינגולריים **השונים מאפס**.", do=show("r-c1")),
    P("קחו את המטריצה שכל הכניסות שלה אחדות, שלוש על שתיים.", do=show("r-A"),
      say="קחו את המטריצה שכל הכניסות שלה אחדות, שלוש על שתיים."),
    P("בפירוק שלה, על האלכסון של $S$ עומדים שורש שש ואפס.", do=show("r-S"),
      say="בפירוק שלה, על האלכסון של אֶס עומדים שורש שש ואפס."),
    P("רק ערך אחד שונה מאפס, ולכן הדרגה היא אחת.", do=show("r-r")),
    P("וזה מתאים: כל השורות של $A$ שוות, ולכן יש רק שורה אחת בלתי תלויה.", do=show("r-c2"),
      say="וזה מתאים: כל השורות של אֵיי שוות, ולכן יש רק שורה אחת בלתי תלויה."),
    P("שימו לב: אפס על האלכסון הוא ערך סינגולרי חוקי. הוא פשוט לא נספר בדרגה.", do=show("r-c3"), hold=0.4),
], stage=w.lines(w.line("r-A", "A=" + w.pm(A2)),
                 w.line("r-S", "S=" + w.pm(S2)),
                 w.line("r-r", "\\operatorname{rank}\\,A = 1", "hl")),
   panel=st.card("r-c1", "rule", "🔑 דרגה = מספר ה-$\\sigma_i\\ne0$")
         + st.card("r-c2", "ex", "כל השורות שוות: דרגה $1$")
         + st.card("r-c3", "trap", "⚠️ $\\sigma=0$ חוקי, אבל לא נספר"))

traps = Scene("traps", "מלכודות", [
    P("שלוש מלכודות שחוזרות במבחנים."),
    P("ראשונה: בפירוק כתוב $V^T$, לא $V$. העמודות של $V$ מופיעות שם כשורות.", do=show("t-1"),
      say="ראשונה: בפירוק כתוב וִי טְרַנְסְפּוֹז, לא וִי. העמודות של וִי מופיעות שם כשורות."),
    P("שנייה: הסדר. קודם $U$, אחר כך $S$, ובסוף $V^T$.", do=show("t-2"),
      say="שנייה: הסדר. קודם יוּ, אחר כך אֶס, ובסוף וִי טְרַנְסְפּוֹז."),
    P("שלישית: הערכים הסינגולריים לא שליליים, ומסודרים מהגדול לקטן.", do=show("t-3")),
    P("$S$ שבה ערך קטן עומד לפני ערך גדול, או עם מספר שלילי, היא לא $S$ של פירוק תקין.", hold=0.4,
      say="אֶס שבה ערך קטן עומד לפני ערך גדול, או עם מספר שלילי, היא לא אֶס של פירוק תקין."),
], stage=w.lines(w.line("t-f", "A = U\\,S\\,V^T", "big", hidden=False)),
   panel=st.card("t-1", "trap", "⚠️ $V^T$ ולא $V$")
         + st.card("t-2", "trap", "⚠️ הסדר: $U$, $S$, $V^T$")
         + st.card("t-3", "trap", "⚠️ $\\sigma_i\\ge0$, בסדר יורד"))

exam = Scene("exam", "שאלה בסגנון מבחן", [
    P("שאלה בסגנון מבחן: בפירוק SVD של מטריצה $A$, המטריצה $S$ היא זו שעל המסך. איזו טענה נכונה?"),
    P("$S$ היא בגודל של $A$. ל-$S$ יש שתי שורות וארבע עמודות, ולכן גם ל-$A$.", do=show("x-1"),
      say="אֶס היא בגודל של אֵיי. לאֶס יש שתי שורות וארבע עמודות, ולכן גם לאֵיי."),
    P("אז $A$ היא שתיים על ארבע, ולא ארבע על שתיים.", do=show("q-x-b", "q-n-b"),
      say="אז אֵיי היא שתיים על ארבע, ולא ארבע על שתיים."),
    P("מכאן $U$ שתיים על שתיים, לפי השורות, ו-$V$ ארבע על ארבע, לפי העמודות.", do=show("x-2", "q-x-c", "q-n-c"),
      say="מכאן יוּ שתיים על שתיים, לפי השורות, ווִי ארבע על ארבע, לפי העמודות."),
    P("וזו המלכודת: מי שמחליף בין $U$ ל-$V$ בוחר בטענה עם הגדלים ההפוכים.", do=show("x-t"),
      say="וזו המלכודת: מי שמחליף בין יוּ לוִי בוחר בטענה עם הגדלים ההפוכים."),
    P("ועכשיו הדרגה. על האלכסון עומדים חמש ואפס.", do=show("x-3")),
    P("רק ערך אחד שונה מאפס, ולכן הדרגה היא אחת ולא שתיים.", do=show("q-x-d", "q-n-d")),
    P("אז הטענה הנכונה: $A$ שתיים על ארבע, ודרגתה אחת.", do=show("q-ok-a"), hold=0.6,
      say="אז הטענה הנכונה: אֵיי שתיים על ארבע, ודרגתה אחת."),
], stage=w.lines(w.line("x-S", "S=" + w.pm(SX), "big", hidden=False),
                 w.line("x-1", "A:\\ 2\\times4", "small"),
                 w.line("x-2", "U:\\ 2\\times2,\\qquad V:\\ 4\\times4", "small"),
                 w.line("x-3", "\\sigma_1=5,\\ \\sigma_2=0\\ \\Rightarrow\\ \\operatorname{rank}\\,A=1", "small"),
                 st.card("x-t", "trap", "⚠️ $U$ לפי השורות, $V$ לפי העמודות")),
   panel='<div class="qstem"><span class="qid">בסגנון מבחן</span>בפירוק SVD של $A$ נתון '
         '$S$ שעל המסך. איזו טענה נכונה?</div>'
         + st.options("q", OPTS, notes={"b": "גדלים הפוכים", "c": "הפוך", "d": "$\\sigma_2=0$"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: לכל מטריצה יש פירוק $A=USV^T$.", do=show("c-1"),
      say="לסיכום: לכל מטריצה יש פירוק אֵיי שווה יוּ אֶס וִי טְרַנְסְפּוֹז."),
    P("$U$ לפי מספר השורות, $V$ לפי מספר העמודות, ו-$S$ בגודל של $A$.", do=show("c-2"),
      say="יוּ לפי מספר השורות, וִי לפי מספר העמודות, ואֶס בגודל של אֵיי."),
    P("הערכים הסינגולריים לא שליליים ובסדר יורד.", do=show("c-3")),
    P("והדרגה היא מספר הערכים הסינגולריים השונים מאפס. נתראה בשלב הבא.", do=show("c-4"), hold=0.6),
], stage=w.lines(w.shapes("cz", 3, 2, hidden=False)),
   panel=st.card("c-1", "rule", "🔑 $A=USV^T$, לכל מטריצה")
         + st.card("c-2", "rule", "🔑 $U$: $m\\times m$, $S$: $m\\times n$, $V$: $n\\times n$")
         + st.card("c-3", "rule", "🔑 $\\sigma_1\\ge\\sigma_2\\ge\\dots\\ge0$")
         + st.card("c-4", "rule", "🔑 דרגה = מספר ה-$\\sigma_i\\ne0$"))

VIDEO = Video("V01", "svd", "מהו פירוק SVD ואיך נראות המטריצות",
              [title, idea, sizes, example, rank, traps, exam, recap], bank={})
