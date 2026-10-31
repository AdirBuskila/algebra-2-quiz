# -*- coding: utf-8 -*-
"""P07 · ריבועים פחותים ומשוואות הנורמל — video script (build: tools/video/vid.py P07).

Source: courses/proj_gs/C07.js (lesson + goal). Exam anchor: 26B-A-Q3b (best line for (0,2),(1,2),(2,4),(3,8),(4,9)),
which no guided quiz uses. Avoided on purpose: the C07 quiz (x=1..4 with (1,2),(2,3),(3,5),(4,6), y=1.4x+0.5),
the lesson example (0,1),(1,2),(2,2),(3,4), the quiz/boss items 24A-B-Q1a (and its twin 25A-B-Q1a, same points),
24B-B-Q3b, 23B-B-Q1a, 23A-A-Q1a. 24B-A-Q3b is solved in P08 and 24A-C-Q1a in the boss video P10.
Every sum, solution and residual below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R


def fit(pts):
    """normal equations for y = m x + n: A = [x | 1], returns (A^T A, A^T b, (m, n), residuals)"""
    A = M([[x, 1] for x, _ in pts])
    b = V(*[y for _, y in pts])
    AtA, Atb = A.T * A, A.T * b
    sol = AtA.LUsolve(Atb)
    res = b - A * sol
    assert A.T * res == sp.zeros(2, 1)                    # the residual is ⟂ both columns
    # cross-check: the least-squares solution minimizes |Ax-b|^2 (gradient zero, A^T A positive definite)
    m_, n_ = sp.symbols("m_ n_")
    E = sum((y - m_ * x - n_) ** 2 for x, y in pts)
    assert sp.solve([sp.diff(E, m_), sp.diff(E, n_)], [m_, n_]) == {m_: sol[0], n_: sol[1]}
    return AtA, Atb, (sol[0], sol[1]), res


# ---------------------------------------------------------------- example: (0,1),(1,1),(2,3)
E1 = [(0, 1), (1, 1), (2, 3)]
AtA1, Atb1, (m1, n1), r1 = fit(E1)
assert AtA1 == M([[5, 3], [3, 3]]) and Atb1 == V(7, 5) and AtA1.det() == 6
assert (m1, n1) == (1, R(2, 3))
assert list(r1) == [R(1, 3), R(-2, 3), R(1, 3)] and sum(r1) == 0
assert sum(x * r for (x, _), r in zip(E1, r1)) == 0
PLOT1 = w.lsplot("l1", E1, box=(-0.7, 3.2, -0.6, 3.6), size=(520, 480), line=(m1, n1))

# ---------------------------------------------------------------- exam 26B-A-Q3b
E2 = [(0, 2), (1, 2), (2, 4), (3, 8), (4, 9)]
xs, ys = [p[0] for p in E2], [p[1] for p in E2]
assert (sum(xs), sum(x * x for x in xs), sum(ys), sum(x * y for x, y in E2)) == (10, 30, 25, 70)
AtA2, Atb2, (m2, n2), r2 = fit(E2)
assert AtA2 == M([[30, 10], [10, 5]]) and Atb2 == V(70, 25) and AtA2.det() == 50
assert (m2, n2) == (2, 1)
assert list(r2) == [1, -1, -1, 1, 0] and sum(r2) == 0 and sum(x * r for x, r in zip(xs, r2)) == 0
# Cramer, as written on screen
assert R(70 * 5 - 10 * 25, 50) == 2 and R(30 * 25 - 10 * 70, 50) == 1
# the trap: columns [1 | x] give the unknowns in the order (n, m)
A_sw = M([[1, x] for x in xs])
sw = (A_sw.T * A_sw).LUsolve(A_sw.T * V(*ys))
assert A_sw.T * A_sw == M([[5, 10], [10, 30]]) and list(sw) == [1, 2]
PLOT2 = w.lsplot("l2", E2, box=(-0.8, 4.8, -0.8, 10.2), size=(460, 560), line=(m2, n2), step=2)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("לפעמים למערכת משוואות אין פתרון בכלל. למשל, כשיש יותר נקודות מאשר פרמטרים: בדרך כלל אין ישר שעובר בכולן."),
    P("בסרטון הזה נמצא את הפתרון **הכי קרוב**: שיטת הריבועים הפחותים."),
    P("נמצא ישר שעובר הכי קרוב לנקודות, ונפתור שאלה ממבחן.", hold=0.4),
], stage='<div class="kicker">P07 · היטל וגרהם-שמידט</div><h1>ריבועים פחותים ומשוואות הנורמל</h1>'
         '<p>למצוא את הישר הקרוב ביותר לנקודות ופתרון ריבועים פחותים כללי באמצעות $A^TA\\hat x=A^T\\vec b$, '
         'ולבדוק אותו דרך ניצבות השארית.</p>', layout="title")

idea = Scene("idea", "הרעיון", [
    P("כשאין פתרון ל-$A\\vec x=\\vec b$, מחפשים את $\\hat x$ שהשגיאה שלו הכי קטנה.", do=show("i-0"),
      say="כשאין פתרון למערכת אֵיי אִקְס שווה בִּי, מחפשים את אִקְס כובע, שהשגיאה שלו הכי קטנה."),
    P("השגיאה היא הנורמה בריבוע של $A\\hat x-\\vec b$: סכום ריבועי הסטיות. מכאן השם.", do=show("i-1"),
      say="השגיאה היא הנורמה בריבוע של, בסוגריים, אֵיי אִקְס כובע פחות בִּי: סכום ריבועי הסטיות. מכאן השם."),
    P("והפתרון מקיים את **משוואות הנורמל**: כופלים את שני האגפים ב-$A^T$.", do=show("i-2"),
      say="והפתרון מקיים את משוואות הנורמל: כופלים את שני האגפים באֵיי טְרַנְסְפּוֹז."),
    P("למה? כי בפתרון הכי טוב, השארית ניצבת לכל עמודה של $A$. וזה בדיוק מה שהמשוואה אומרת.", do=show("i-3", "i-c1"),
      say="למה? כי בפתרון הכי טוב, השארית ניצבת לכל עמודה של אֵיי. וזה בדיוק מה שהמשוואה אומרת."),
    P("ואם העמודות בלתי תלויות, המטריצה $A^TA$ הפיכה, והפתרון יחיד.", do=show("i-c2"), hold=0.4,
      say="ואם העמודות בלתי תלויות, המטריצה אֵיי טְרַנְסְפּוֹז אֵיי הפיכה, והפתרון יחיד."),
], stage='<div class="pg-stack">' + w.rows("i", [
    r"$A\vec x=\vec b\quad$ (אין פתרון)",
    r"$\min\ \|A\hat x-\vec b\|^2$",
    r"$A^TA\,\hat x=A^T\vec b$",
    r"$A^T(\vec b-A\hat x)=\vec 0$"]) + "</div>",
   panel=st.card("i-c1", "rule", "🔑 השארית $\\vec b-A\\hat x$ ניצבת לעמודות של $A$")
         + st.card("i-c2", "ex", "עמודות בלתי תלויות ⟸ $A^TA$ הפיכה ⟸ פתרון יחיד"))

line = Scene("line", "ישר", [
    P("המקרה הנפוץ במבחן: ישר $y=mx+n$ שעובר הכי קרוב לנקודות.", do=show("n-0"),
      say="המקרה הנפוץ במבחן: ישר, וַואי שווה אֶם אִקְס ועוד אֶן, שעובר הכי קרוב לנקודות."),
    P("כל נקודה נותנת משוואה אחת. בעמודה הראשונה של $A$ שמים את ה-$x$, ובשנייה אחדות.", do=show("n-1"),
      say="כל נקודה נותנת משוואה אחת. בעמודה הראשונה של אֵיי שמים את האִקְסים, ובשנייה אחדות."),
    P("ואז $A^TA$ ו-$A^T\\vec b$ הם פשוט סכומים: של $x$, של $x$ בריבוע, של $y$ ושל $xy$.", do=show("n-2"),
      say="ואז אֵיי טְרַנְסְפּוֹז אֵיי ואֵיי טְרַנְסְפּוֹז בִּי הם פשוט סכומים: של אִקְס, של אִקְס בריבוע, של וַואי, "
          "ושל אִקְס כפול וַואי."),
    P("ובפינה התחתונה: מספר הנקודות.", do=show("n-c"), hold=0.4),
], stage='<div class="pg-stack">' + w.rows("n", [
    r"$y=mx+n$",
    r"$A=\begin{pmatrix}x_1&1\\ \vdots&\vdots\\ x_k&1\end{pmatrix},\quad \hat x=\begin{pmatrix}m\\n\end{pmatrix}$",
    r"$\begin{pmatrix}\sum x_i^2&\sum x_i\\ \sum x_i&k\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}\sum x_iy_i\\ \sum y_i\end{pmatrix}$"],
    "sm") + "</div>",
   panel=st.card("n-c", "rule", "🔑 $k$ = מספר הנקודות"))

ex = Scene("ex", "דוגמה", [
    P("שלוש נקודות: $(0,1)$, $(1,1)$ ו-$(2,3)$. אין ישר שעובר דרך שלושתן.", do=show("e-0"),
      say="שלוש נקודות: אפס אחת, אחת אחת, ושתיים שלוש. אין ישר שעובר דרך שלושתן."),
    P("הסכומים: $\\sum x=3$, $\\sum x^2=5$, $\\sum y=5$, $\\sum xy=7$.", say="הסכומים: סכום האִקְסים שלוש, סכום הריבועים חמש, סכום הוַואים חמש, וסכום המכפלות שבע.", do=show("e-1")),
    P("מקבלים מערכת של שתי משוואות. הדטרמיננטה שש.", do=show("e-2")),
    P("והפתרון: השיפוע אחת, והחיתוך שני שליש.", do=show("e-3", "l1-line")),
    P("בדיקה: השאריות הן שליש, מינוס שני שליש, ושליש. הסכום שלהן אפס.", do=show("e-4", "l1-res")),
    P("וגם $\\sum x_i\\,\\text{res}_i=0$. השארית ניצבת לשתי העמודות, כמו שהבטחנו.", say="וגם הסכום של אִקְס כפול שארית הוא אפס. השארית ניצבת לשתי העמודות, כמו שהבטחנו.", do=show("e-5", "e-c"), hold=0.4),
], stage='<div class="pg-stack">' + PLOT1 + "</div>",
   panel=w.rows("e", [
       r"$(0,1),\ (1,1),\ (2,3)$",
       r"$\sum x=3,\ \sum x^2=5,\ \sum y=5,\ \sum xy=7$",
       r"$\begin{pmatrix}5&3\\3&3\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}7\\5\end{pmatrix}$",
       r"$m=1,\quad n=\frac23$",
       r"$\text{res}=\left(\frac13,-\frac23,\frac13\right),\ \sum=0$",
       r"$\sum x_i\,\text{res}_i=0-\frac23+\frac23=0$"], "sm")
   + st.card("e-c", "rule", "🔑 בדיקה: $\\sum\\text{res}_i=0$ וגם $\\sum x_i\\text{res}_i=0$"))

EX_STEM = ("נתונות 5 נקודות במישור: $(0,2),\\ (1,2),\\ (2,4),\\ (3,8),\\ (4,9)$. מצאו את משוואת הישר הקרוב ביותר "
           "לנקודות בשיטת הריבועים הפחותים.")
exam = Scene("exam", "שאלה ממבחן", [
    P("ועכשיו שאלה ממבחן: חמש נקודות, והישר הקרוב ביותר אליהן."),
    P("נבנה טבלת סכומים: $\\sum x=10$ ו-$\\sum x^2=30$.", say="נבנה טבלת סכומים. סכום האִקְסים עשר, וסכום הריבועים שלושים.", do=show("x-0")),
    P("$\\sum y=25$ ו-$\\sum xy=70$. ויש חמש נקודות.", say="סכום הוַואים עשרים וחמש, וסכום המכפלות שבעים. ויש חמש נקודות.", do=show("x-1")),
    P("המערכת: שלושים, עשר, עשר, חמש. הדטרמיננטה: מאה חמישים פחות מאה, כלומר חמישים.", do=show("x-2")),
    P("בכלל קרמר: השיפוע הוא מאה חלקי חמישים, שתיים. והחיתוך חמישים חלקי חמישים, אחת.", do=show("x-3")),
    P("אז הישר הוא $y=2x+1$.", do=show("x-4", "l2-line"), say="אז הישר הוא וַואי שווה שתיים אִקְס ועוד אחת."),
    P("בדיקה: השאריות הן אחת, מינוס אחת, מינוס אחת, אחת ואפס. הסכום אפס.", do=show("x-5", "l2-res")),
    P("וגם $\\sum x_i\\,\\text{res}_i=0-1-2+3+0=0$. הישר נכון.", say="וגם סכום האִקְס כפול שארית: אפס, מינוס אחת, מינוס שתיים, שלוש ואפס. גם הוא אפס. הישר נכון.", do=show("x-c1"),
      hold=0.3),
    P("המלכודת: אם שמים את עמודת האחדות ראשונה, הנעלמים מתחלפים. הפתרון יוצא אחת, שתיים, אבל זה החיתוך ואז השיפוע.",
      do=show("x-c2"), hold=0.5),
], stage='<div class="pg-two">' + PLOT2 + w.rows("x", [
    r"$\sum x=10,\ \sum x^2=30$",
    r"$\sum y=25,\ \sum xy=70,\ k=5$",
    r"$\begin{pmatrix}30&10\\10&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}70\\25\end{pmatrix}$",
    r"$m=\frac{350-250}{50}=2,\ \ n=\frac{750-700}{50}=1$",
    r"$y=2x+1$",
    r"$\text{res}=(1,-1,-1,1,0)$"], "sm") + "</div>",
   panel=w.stem("26B-A-Q3b", EX_STEM)
         + st.card("x-c1", "rule", "🔑 $\\sum\\text{res}=0,\\ \\sum x\\,\\text{res}=0$ ✓")
         + st.card("x-c2", "trap", "⚠️ עמודות $[1\\,|\\,x]$: הפתרון הוא $(n,m)$, לא $(m,n)$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: כשאין פתרון, פותרים את משוואות הנורמל.", do=show("c-1")),
    P("לישר: עמודה של ערכי $x$ ועמודת אחדות, והמערכת בנויה מארבעה סכומים ומספר הנקודות.", say="לישר: עמודה של אִקְסים ועמודת אחדות, והמערכת בנויה מארבעה סכומים ומספר הנקודות.", do=show("c-2")),
    P("ובסוף בודקים: $\\sum\\text{res}_i=0$ וגם $\\sum x_i\\,\\text{res}_i=0$. נתראה ברמה הבאה.", say="ובסוף בודקים: סכום השאריות אפס, וגם סכום אִקְס כפול שארית. נתראה ברמה הבאה.", do=show("c-3"), hold=0.6),
], stage='<div class="pg-stack">' + w.big("c-0", r"A^TA\,\hat x=A^T\vec b", hidden=False) + "</div>",
   panel=st.card("c-1", "rule", "🔑 $\\hat x$ מקטין את $\\|A\\hat x-\\vec b\\|^2$")
         + st.card("c-2", "rule", "🔑 $\\begin{pmatrix}\\sum x^2&\\sum x\\\\\\sum x&k\\end{pmatrix}$")
         + st.card("c-3", "trap", "⚠️ סדר העמודות = סדר הנעלמים"))

VIDEO = Video("P07", "proj_gs", "ריבועים פחותים ומשוואות הנורמל", [title, idea, line, ex, exam, recap],
              bank={"26B-A-Q3b": None})
