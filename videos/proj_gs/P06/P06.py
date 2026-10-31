# -*- coding: utf-8 -*-
"""P06 · היטל על פרישה: מטריצות ופונקציות — video script (build: tools/video/vid.py P06).

Source: courses/proj_gs/C06.js (lesson + goal). Exam anchor: 23A-A-Q1b (projection of [[1,2],[3,0]] on
Sp{[[1,1],[0,0]], [[1,3],[1,1]]} in M_2), which no guided quiz uses. Its twin 23A-S-Q5b (same matrices) is not
used by any quiz either. Avoided on purpose: the C06 quiz (Sp{I, diag(1,-1)} with V=[[3,1],[2,5]];
Sp{[[1,1],[0,0]],[[0,1],[1,0]]} with V=[[1,0],[2,2]]; GS of {1,x} on [0,1]; x^3+1 on Sp{1,x}), 24B-B-Q1c and
24A-A-Q1b (C06 quiz items), the boss items 24B-A-Q1b, 24A-B-Q1b, 23A-B-Q2a (x^2 on Sp{1,|x|}: so no |x| against 1
here). The function example is x^4 on Sp{1, x^2}, which needs Gram-Schmidt.
Every value below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R, X

x = X
# ---------------------------------------------------------------- functions: x^4 on Sp{1, x^2} in C[-1,1]
h = x ** 4
ipf = lambda f, g: w.ip_f(f, g, -1, 1)
assert ipf(1, x ** 2) == R(2, 3) and ipf(1, 1) == 2           # not orthogonal: Gram-Schmidt first
(g1, g2), cf = w.gram_schmidt([sp.Integer(1), x ** 2], ipf)
assert cf[(1, 0)] == R(1, 3) and sp.expand(g2 - (x ** 2 - R(1, 3))) == 0
assert ipf(g2, g2) == R(8, 45)
assert ipf(h, 1) == R(2, 5) and ipf(h, g2) == R(16, 105)
assert R(2, 5) / 2 == R(1, 5) and R(16, 105) / R(8, 45) == R(6, 7)
pf = sp.expand(w.proj(h, [g1, g2], ipf))
assert sp.expand(pf - (R(6, 7) * x ** 2 - R(3, 35))) == 0
assert sp.expand(R(1, 5) + R(6, 7) * (x ** 2 - R(1, 3)) - pf) == 0
assert ipf(h - pf, 1) == 0 and ipf(h - pf, x ** 2) == 0
PLOT = w.fplot("fp", [("h", h, "a", "", (0, 0)), ("p", pf, "p", "", (0, 0))],
               box=(-1.3, 1.3, -0.35, 1.3), size=(560, 350), dom=(-1, 1))

# ---------------------------------------------------------------- exam 23A-A-Q1b
W1, W2, Vm = M([[1, 1], [0, 0]]), M([[1, 3], [1, 1]]), M([[1, 2], [3, 0]])
assert w.ip_m(W1, W2) == 4
(U1, U2), cm = w.gram_schmidt([W1, W2], w.ip_m)
assert w.ip_m(W1, W1) == 2 and cm[(1, 0)] == 2 and U2 == M([[-1, 1], [1, 1]]) and w.ip_m(U2, U2) == 4
assert w.ip_m(Vm, U1) == 3 and w.ip_m(Vm, U2) == 4
Pv = w.proj(Vm, [U1, U2], w.ip_m)
assert Pv == R(3, 2) * U1 + U2 == M([[R(1, 2), R(5, 2)], [1, 1]]) == R(1, 2) * M([[1, 5], [2, 2]])
Rv = Vm - Pv
assert Rv == M([[R(1, 2), R(-1, 2)], [2, -1]])
assert w.ip_m(Rv, W1) == 0 and w.ip_m(Rv, W2) == 0 and w.ip_m(Rv, Rv) == R(11, 2)
# the trap: the formula on the non-orthogonal W1, W2
assert w.ip_m(Vm, W2) == 10 and w.ip_m(W2, W2) == 12
Bad = R(3, 2) * W1 + R(10, 12) * W2
assert Bad == M([[R(7, 3), R(4, 1)], [R(5, 6), R(5, 6)]])
assert w.ip_m(Vm - Bad, W1) == R(-10, 3) and w.ip_m(Vm - Bad, W1) != 0

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("זו שאלת המבחן הכי קבועה בנושא: חשבו את ההיטל של וקטור על פרישה של כמה וקטורים."),
    P("נבנה מתכון של ארבעה צעדים, וננסה אותו על פונקציות ועל מטריצות."),
    P("ונראה מה קורה למי שמדלג על צעד.", hold=0.4),
], stage='<div class="kicker">P06 · היטל וגרהם-שמידט</div><h1>היטל על פרישה: מטריצות ופונקציות</h1>'
         '<p>לחשב היטל על $\\operatorname{Sp}\\{\\dots\\}$ במרחב מטריצות ובמרחב פונקציות: לבדוק ניצבות, לבצע '
         'גרהם-שמידט אם צריך, ולהציב בנוסחה.</p>', layout="title")

recipe = Scene("recipe", "המתכון", [
    P("תזכורת: ההיטל הוא הוקטור בתוך תת המרחב שהכי קרוב ל-$V$, והשארית שלו ניצבת לכל תת המרחב.",
      say="תזכורת: ההיטל הוא הוקטור בתוך תת המרחב שהכי קרוב לוִי, והשארית שלו ניצבת לכל תת המרחב."),
    P("והנוסחה שמחשבת אותו דורשת בסיס אורתוגונלי. מכאן המתכון.", hold=0.2),
    P("צעד ראשון: בודקים אם הוקטורים הפורשים ניצבים זה לזה.", do=show("s-1")),
    P("צעד שני: אם לא, עושים גרהם-שמידט, ומקבלים בסיס אורתוגונלי של אותה פרישה.", do=show("s-2")),
    P("צעד שלישי: מציבים בנוסחת ההיטל, סכום של היטלים על כל וקטור בסיס.", do=show("s-3")),
    P("וצעד רביעי, שחוסך נקודות: בודקים שהשארית ניצבת לכל וקטור פורש.", do=show("s-4"), hold=0.4),
], stage='<div class="pg-stack">' + w.big("s-0", r"\operatorname{Proj}=\sum_i\frac{\langle V,u_i\rangle}{\|u_i\|^2}\,u_i",
                                          "sm", hidden=False) + "</div>",
   panel=st.card("s-1", "ex", "1. ניצבות בין הפורשים?")
         + st.card("s-2", "ex", "2. אם לא: גרהם-שמידט")
         + st.card("s-3", "ex", "3. מציבים בנוסחה")
         + st.card("s-4", "rule", "🔑 4. בדיקה: $\\langle V-\\operatorname{Proj},u_i\\rangle=0$"))

func = Scene("func", "פונקציות", [
    P("נתחיל בפונקציות. ב-$C[-1,1]$ נטיל את $x^4$ על הפרישה של $1$ ושל $x^2$.", do=show("f-0", "fp-h"),
      say="נתחיל בפונקציות. בסִי ממינוס אחת עד אחת נטיל את אִקְס ברביעית על הפרישה של אחת ושל אִקְס בריבוע."),
    P("צעד ראשון: שתיהן זוגיות, אז אין ניצבות אוטומטית. המכפלה שלהן היא $\\frac23$, לא אפס.", do=show("f-1"),
      say="צעד ראשון: שתיהן זוגיות, אז אין ניצבות אוטומטית. המכפלה שלהן היא שני שליש, לא אפס."),
    P("צעד שני, גרהם-שמידט: המקדם הוא $\\frac23$ חלקי שתיים, שליש. ולכן $u_2=x^2-\\frac13$.", do=show("f-2"),
      say="צעד שני, גרהם-שמידט: המקדם הוא שני שליש חלקי שתיים, שליש. ולכן יוּ שתיים הוא אִקְס בריבוע פחות שליש."),
    P("הנורמה שלו בריבוע: שמונה חלקי ארבעים וחמש.", do=show("f-3")),
    P("צעד שלישי: המקדם של $1$ הוא $\\frac15$, והמקדם של $u_2$ יוצא $\\frac67$.", do=show("f-4"),
      say="צעד שלישי: המקדם של אחת הוא חמישית, והמקדם של יוּ שתיים יוצא שש שביעיות."),
    P("אחרי פתיחת סוגריים, ההיטל הוא $\\frac67x^2-\\frac{3}{35}$. בגרף רואים כמה הוא קרוב לפונקציה.",
      do=show("f-5", "fp-p"),
      say="אחרי פתיחת סוגריים, ההיטל הוא שש שביעיות אִקְס בריבוע, פחות שלוש חלקי שלושים וחמש. "
          "בגרף רואים כמה הוא קרוב לפונקציה."),
    P("ובדיקה: השארית ניצבת גם ל-$1$ וגם ל-$x^2$. שתי המכפלות יוצאות אפס.", do=show("f-6"), hold=0.4,
      say="ובדיקה: השארית ניצבת גם לאחת וגם לאִקְס בריבוע. שתי המכפלות יוצאות אפס."),
], stage='<div class="pg-stack">' + PLOT + "</div>", panel=w.rows("f", [
    r"$\operatorname{Proj}_{\operatorname{Sp}\{1,x^2\}}x^4$",
    r"$\langle 1,x^2\rangle=\frac23\ne0$",
    r"$u_2=x^2-\frac{2/3}{2}=x^2-\frac13$",
    r"$\|u_2\|^2=\frac{8}{45}$",
    r"$\frac{\langle x^4,1\rangle}{2}=\frac15,\ \ \frac{\langle x^4,u_2\rangle}{\|u_2\|^2}=\frac{16/105}{8/45}=\frac67$",
    r"$\operatorname{Proj}=\frac15+\frac67\left(x^2-\frac13\right)=\frac67x^2-\frac{3}{35}$",
    r"$\langle x^4-\operatorname{Proj},1\rangle=\langle x^4-\operatorname{Proj},x^2\rangle=0$"], "sm"))

EX_STEM = ("ב-$M_2(\\mathbb{R})$ עם $\\langle A,B\\rangle=\\operatorname{tr}(B^TA)$, חשבו את ההיטל של "
           "$\\begin{pmatrix}1&2\\\\3&0\\end{pmatrix}$ על $\\operatorname{Sp}\\left\\{\\begin{pmatrix}1&1\\\\0&0\\end{pmatrix},"
           "\\begin{pmatrix}1&3\\\\1&1\\end{pmatrix}\\right\\}$.")
exam = Scene("exam", "שאלה ממבחן", [
    P("ועכשיו שאלה ממבחן, במטריצות. נלך לפי המתכון."),
    P("צעד ראשון: המכפלה של שתי המטריצות הפורשות: אחת, ועוד שלוש. ארבע. לא ניצבות.", do=show("x-0")),
    P("צעד שני, גרהם-שמידט: המקדם הוא ארבע חלקי שתיים, ולכן $u_2=w_2-2w_1$.", do=show("x-1"),
      say="צעד שני, גרהם-שמידט: המקדם הוא ארבע חלקי שתיים, ולכן יוּ שתיים שווה דַאבְּלְיוּ שתיים פחות פעמיים דַאבְּלְיוּ אחת."),
    P("יוצאת המטריצה מינוס אחת, ושלוש אחדות. הנורמה בריבוע שלה ארבע.", do=show("x-2")),
    P("צעד שלישי: המכפלה של $V$ עם $u_1$ היא שלוש, ועם $u_2$ היא ארבע.", do=show("x-3"),
      say="צעד שלישי: המכפלה של וִי עם יוּ אחת היא שלוש, ועם יוּ שתיים היא ארבע."),
    P("אז ההיטל הוא שלוש חצאים $u_1$, ועוד $u_2$.", do=show("x-4"),
      say="אז ההיטל הוא שלוש חצאים יוּ אחת, ועוד יוּ שתיים."),
    P("ומקבלים חצי כפול המטריצה אחת, חמש, שתיים, שתיים.", do=show("x-5"), hold=0.3),
    P("צעד רביעי, בדיקה: השארית היא המטריצה הזו, והמכפלות שלה עם שתי המטריצות הפורשות הן אפס.", do=show("x-6", "x-c1")),
    P("ובונוס: המרחק בריבוע מ-$V$ לתת המרחב הוא $\\frac14+\\frac14+4+1=\\frac{11}{2}$, ולכן המרחק $\\sqrt{11/2}$.",
      do=show("x-7"), hold=0.5,
      say="ובונוס: המרחק בריבוע מוִי לתת המרחב הוא רבע ועוד רבע ועוד ארבע ועוד אחת, כלומר אחת עשרה חצאים. "
          "ולכן המרחק הוא שורש של אחת עשרה חצאים."),
], stage='<div class="pg-stack">' + w.rows("x", [
    r"$\langle w_1,w_2\rangle=1+3=4\ne0$",
    r"$u_1=w_1,\quad u_2=w_2-\frac42\,w_1$",
    f"$u_2={w.mat(U2)},\\quad \\|u_2\\|^2=4$",
    r"$\langle V,u_1\rangle=3,\quad \langle V,u_2\rangle=-1+2+3+0=4$",
    r"$\operatorname{Proj}=\frac32u_1+\frac44u_2$",
    r"$=\frac12\begin{pmatrix}1&5\\2&2\end{pmatrix}$",
    f"$V-\\operatorname{{Proj}}={w.mat(Rv)}\\perp w_1,w_2$",
    r"$\|V-\operatorname{Proj}\|^2=\frac14+\frac14+4+1=\frac{11}{2},\ \ d=\sqrt{11/2}$"], "sm") + "</div>",
   panel=w.stem("23A-A-Q1b", EX_STEM)
         + st.card("x-c1", "rule", "🔑 בדיקה: שתי מכפלות אפס ✓"))

trap = Scene("trap", "מלכודת", [
    P("ומה קורה למי שמדלג על גרהם-שמידט, ומציב בנוסחה את שתי המטריצות המקוריות?", do=show("t-c0")),
    P("המקדם הראשון יוצא שלוש חצאים, כמו קודם. השני: עשר חלקי שתים עשרה, חמש שישיות.", do=show("t-0")),
    P("והסכום הוא המטריצה הזו. שונה לגמרי מהתשובה הנכונה.", do=show("t-1")),
    P("הבדיקה תופסת את זה מיד: המכפלה של השארית עם הפורש הראשון היא מינוס עשר שלישים. לא אפס.", do=show("t-2", "t-c1")),
    P("למה? שתי המטריצות חולקות כיוון משותף, והנוסחה סופרת אותו פעמיים. גרהם-שמידט מוציא אותו מהשנייה.",
      do=show("t-c2"), hold=0.5),
], stage='<div class="pg-stack">' + w.rows("t", [
    r"$\frac{\langle V,w_1\rangle}{\|w_1\|^2}=\frac32,\qquad \frac{\langle V,w_2\rangle}{\|w_2\|^2}=\frac{10}{12}=\frac56$",
    f"$\\frac32w_1+\\frac56w_2={w.mat(Bad)}$",
    r"$\langle V-\operatorname{Proj}',w_1\rangle=-\frac{10}{3}\ne0$"], "sm") + "</div>",
   panel=st.card("t-c0", "trap", "⚠️ נוסחת ההיטל על פורשים שאינם ניצבים")
         + st.card("t-c1", "ex", "הבדיקה נכשלת ⟸ התשובה שגויה")
         + st.card("t-c2", "rule", "🔑 גרהם-שמידט מסיר את החלק המשותף"))

recap = Scene("recap", "סיכום", [
    P("לסיכום, ארבעה צעדים: בודקים ניצבות, עושים גרהם-שמידט אם צריך, מציבים, ובודקים את השארית.", do=show("c-1")),
    P("בפונקציות זה אותו מתכון, רק שהמכפלה היא אינטגרל. וזוגית ואי זוגית על קטע סימטרי ניצבות מיד.", do=show("c-2")),
    P("ובמטריצות, המכפלה היא סכום רכיב מול רכיב. נתראה ברמה הבאה.", do=show("c-3"), hold=0.6),
], stage='<div class="pg-stack">' + w.big("c-0", r"\langle V-\operatorname{Proj},u_i\rangle=0", hidden=False) + "</div>",
   panel=st.card("c-1", "rule", "🔑 ניצבות → גרהם-שמידט → נוסחה → בדיקה")
         + st.card("c-2", "rule", "🔑 זוגית ⟂ אי-זוגית על $[-1,1]$")
         + st.card("c-3", "trap", "⚠️ נוסחה על פורשים לא ניצבים: תשובה שגויה"))

VIDEO = Video("P06", "proj_gs", "היטל על פרישה: מטריצות ופונקציות", [title, recipe, func, exam, trap, recap],
              bank={"23A-A-Q1b": None})
