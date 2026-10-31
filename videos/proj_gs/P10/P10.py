# -*- coding: utf-8 -*-
"""P10 · מבחן גמר: היטל, גרהם-שמידט, ריבועים פחותים — boss walkthrough (build: tools/video/vid.py P10).

Source: courses/proj_gs/C10.js (boss level). Exam anchors, none used by any guided quiz or boss:
  26B-A-Q1b  projection of C=[[2,3],[1,0]] on Sp{A,B} (the Gram-Schmidt basis of 26B-A-Q1a, solved in P05)
  23B-A-Q5a  projection of [[0,a],[b,0]] on Sp{[[-1,1],[1,0]], [[1,0],[2,1]]} for every a, b
  24A-C-Q1a  best line for (-4,-1),(-2,0),(2,4),(4,5),(5,6)   (its twin 25A-C-Q1a is not used anywhere either)
Avoided on purpose: the six C10 boss items (24B-A-Q1b, 23A-B-Q2a, 24A-B-Q1b, 23B-B-Q1a, 23A-A-Q1a, 23B-B-Q5a) and every
anchor of P01-P09. The bank solution of 23B-A-Q5a already carries the correction of the official misprint
((5b-a)/51, not (5b-3a)/51); the value below is recomputed from scratch.
Every matrix, coefficient and sum below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R

# ---------------------------------------------------------------- 26B-A-Q1b
A1, B1, C1 = M([[1, 0], [0, -1]]), M([[1, 1], [0, -1]]), M([[2, 3], [1, 0]])
(U1, U2), _ = w.gram_schmidt([A1, B1], w.ip_m)
assert U2 == M([[0, 1], [0, 0]])
assert (w.ip_m(C1, U1), w.ip_m(U1, U1), w.ip_m(C1, U2), w.ip_m(U2, U2)) == (2, 2, 3, 1)
P1 = w.proj(C1, [U1, U2], w.ip_m)
assert P1 == M([[1, 3], [0, -1]])
R1 = C1 - P1
assert R1 == M([[1, 0], [1, 1]]) and w.ip_m(R1, A1) == 0 and w.ip_m(R1, B1) == 0

# ---------------------------------------------------------------- 23B-A-Q5a
a, b = sp.symbols("a b", real=True)
X2 = M([[0, a], [b, 0]])
V1, V2 = M([[-1, 1], [1, 0]]), M([[1, 0], [2, 1]])
assert w.ip_m(V2, V1) == 1 and w.ip_m(V1, V1) == 3
(W1, W2), cg = w.gram_schmidt([V1, V2], w.ip_m)
assert cg[(1, 0)] == R(1, 3) and W2 == M([[R(4, 3), R(-1, 3)], [R(5, 3), 1]])
W2s = 3 * W2
assert W2s == M([[4, -1], [5, 3]]) and w.ip_m(W2s, W2s) == 51 and w.ip_m(W2s, V1) == 0
assert sp.expand(w.ip_m(X2, W1) - (a + b)) == 0 and sp.expand(w.ip_m(X2, W2s) - (5 * b - a)) == 0
P2 = w.proj(X2, [W1, W2s], w.ip_m)
ANS = M([[-7 * a + b, 6 * a + 4 * b], [4 * a + 14 * b, -a + 5 * b]]) / 17
assert sp.simplify(P2 - ANS) == sp.zeros(2, 2)
assert sp.simplify(w.ip_m(X2 - P2, V1)) == 0 and sp.simplify(w.ip_m(X2 - P2, V2)) == 0
# one entry by hand, as said on screen: (a+b)/3 * (-1) + (5b-a)/51 * 4 = (-7a+b)/17
assert sp.simplify(-(a + b) / 3 + 4 * (5 * b - a) / 51 - (-7 * a + b) / 17) == 0
# a sanity point: a = 1, b = 1 -> X = [[0,1],[1,0]]
assert ANS.subs({a: 1, b: 1}) == M([[R(-6, 17), R(10, 17)], [R(18, 17), R(4, 17)]])

# ---------------------------------------------------------------- 24A-C-Q1a
pts = [(-4, -1), (-2, 0), (2, 4), (4, 5), (5, 6)]
xs, ys = [p[0] for p in pts], [p[1] for p in pts]
assert (sum(xs), sum(x * x for x in xs), sum(ys), sum(x * y for x, y in pts)) == (5, 65, 14, 62)
Am = M([[x, 1] for x in xs])
NtN, Ntb = Am.T * Am, Am.T * V(*ys)
assert NtN == M([[65, 5], [5, 5]]) and Ntb == V(62, 14) and NtN.det() == 300
m, n = NtN.LUsolve(Ntb)
assert (m, n) == (R(4, 5), 2)
assert R(62 * 5 - 5 * 14, 300) == m and R(65 * 14 - 5 * 62, 300) == n
res = [y - (m * x + n) for x, y in pts]
assert res == [R(1, 5), R(-2, 5), R(2, 5), R(-1, 5), 0] and sum(res) == 0
assert sum(x * r for x, r in zip(xs, res)) == 0
assert [x * r for x, r in zip(xs, res)] == [R(-4, 5), R(4, 5), R(4, 5), R(-4, 5), 0]
# the residual sum alone is not a check: any line through (x̄, ȳ) = (1, 14/5) has residual sum 0
assert sum(y - (5 * (x - 1) + R(14, 5)) for x, y in pts) == 0
PLOT = w.lsplot("bl", pts, box=(-5, 6, -2, 7.4), size=(470, 430), line=(m, n), step=2)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("זה מבחן הגמר של הקורס: שלוש שאלות אמיתיות ממבחנים, בלי קיצורי דרך."),
    P("היטל על פרישה של מטריצות, אותו דבר עם פרמטרים, וישר בריבועים פחותים."),
    P("לפני כל שאלה, נסו לפתור לבד. ואחר כך נפתור יחד.", hold=0.4),
], stage='<div class="kicker">P10 · היטל וגרהם-שמידט</div><h1>מבחן גמר</h1>'
         '<p>לפתור שאלות אמיתיות מהמבחנים, בלי רמזים: היטל על פרישה, גם עם פרמטרים, וישר בריבועים פחותים.</p>', layout="title")

plan = Scene("plan", "סדר העבודה", [
    P("נזכיר את סדר העבודה. היטל על פרישה: בודקים ניצבות, גרהם-שמידט אם צריך, מציבים, ובודקים שהשארית ניצבת.",
      do=show("p-1")),
    P("ריבועים פחותים: משוואות הנורמל עם עמודת אחדות. ובסוף בודקים: $\\sum\\text{res}_i=0$ וגם $\\sum x_i\\text{res}_i=0$.", say="ריבועים פחותים: משוואות הנורמל עם עמודת אחדות. ובסוף בודקים שתי משוואות: סכום השאריות אפס, וגם סכום אִקְס כפול שארית.", do=show("p-2")),
    P("וקודם כל: כותבים איזו מכפלה פנימית נתונה בשאלה.", do=show("p-3"), hold=0.4),
], stage='<div class="pg-stack">' + w.big("p-0", r"\operatorname{Proj}=\sum_i\frac{\langle V,u_i\rangle}{\|u_i\|^2}u_i", "sm",
                                          hidden=False)
         + w.big("p-00", r"A^TA\,\hat x=A^T\vec b", "sm", hidden=False) + "</div>",
   panel=st.card("p-1", "rule", "🔑 ניצבות → גרהם-שמידט → נוסחה → בדיקה")
         + st.card("p-2", "rule", "🔑 $\\sum\\text{res}_i=0$ וגם $\\sum x_i\\text{res}_i=0$")
         + st.card("p-3", "trap", "⚠️ איזו מכפלה פנימית? כאן: $\\operatorname{tr}(B^TA)$"))

S1 = ("ב-$M_2(\\mathbb{R})$ עם $\\operatorname{tr}(B^TA)$: חשבו את ההיטל של $C=\\begin{pmatrix}2&3\\\\1&0\\end{pmatrix}$ על "
      "$\\operatorname{Sp}\\{A,B\\}$, כאשר $A=\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$, $B=\\begin{pmatrix}1&1\\\\0&-1\\end{pmatrix}$.")
q1 = Scene("q1", "שאלה 1", [
    P("שאלה ראשונה: היטל של המטריצה $C$ על הפרישה של $A$ ושל $B$.", say="שאלה ראשונה: היטל של המטריצה סִי על הפרישה של אֵיי ושל בִּי."),
    P("עצרו כאן ונסו לבד.", hold=1.2),
    P("צעד ראשון: המכפלה של $A$ ו-$B$ היא שתיים. לא ניצבות, אז גרהם-שמידט.", do=show("a-0"),
      say="צעד ראשון: המכפלה של אֵיי ובִּי היא שתיים. לא ניצבות, אז גרהם-שמידט."),
    P("המקדם הוא שתיים חלקי שתיים, ולכן $u_2=B-A$: מטריצה עם אחת למעלה מימין.", do=show("a-1"),
      say="המקדם הוא שתיים חלקי שתיים, ולכן יוּ שתיים הוא בִּי פחות אֵיי: מטריצה עם אחת למעלה מימין."),
    P("עכשיו המקדמים: המכפלה של $C$ עם $u_1$ היא שתיים, חלקי שתיים. ועם $u_2$ שלוש, חלקי אחת.", do=show("a-2"),
      say="עכשיו המקדמים: המכפלה של סִי עם יוּ אחת היא שתיים, חלקי שתיים. ועם יוּ שתיים שלוש, חלקי אחת."),
    P("ההיטל: $u_1$ ועוד שלוש $u_2$.", do=show("a-3"), say="ההיטל: יוּ אחת ועוד שלוש יוּ שתיים."),
    P("בדיקה: השארית ניצבת גם ל-$A$ וגם ל-$B$. התשובה נכונה.", do=show("a-4", "a-c"), hold=0.4,
      say="בדיקה: השארית ניצבת גם לאֵיי וגם לבִּי. התשובה נכונה."),
], stage='<div class="pg-stack">' + w.rows("a", [
    r"$\langle A,B\rangle=1+0+0+1=2\ne0$",
    r"$u_1=A,\quad u_2=B-\frac22A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$",
    r"$\frac{\langle C,u_1\rangle}{\|u_1\|^2}=\frac22=1,\quad \frac{\langle C,u_2\rangle}{\|u_2\|^2}=\frac31=3$",
    r"$\operatorname{Proj}=u_1+3u_2=\begin{pmatrix}1&3\\0&-1\end{pmatrix}$",
    r"$C-\operatorname{Proj}=\begin{pmatrix}1&0\\1&1\end{pmatrix}\perp A,B$"], "sm") + "</div>",
   panel=w.stem("26B-A-Q1b", S1) + st.card("a-c", "rule", "🔑 $1-1=0$ ו-$1+0+0-1=0$ ✓"))

S2 = ("חשבו את ההיטל של $\\begin{pmatrix}0&a\\\\b&0\\end{pmatrix}$ על $\\operatorname{Sp}\\left\\{\\begin{pmatrix}-1&1\\\\1&0"
      "\\end{pmatrix},\\begin{pmatrix}1&0\\\\2&1\\end{pmatrix}\\right\\}$, לכל $a,b\\in\\mathbb{R}$.")
q2 = Scene("q2", "שאלה 2", [
    P("שאלה שנייה: אותו דבר, אבל עם **פרמטרים**. ההיטל צריך להיות נוסחה ב-$a$ וב-$b$.",
      say="שאלה שנייה: אותו דבר, אבל עם פרמטרים. ההיטל צריך להיות נוסחה באֵיי ובבִּי."),
    P("עצרו כאן ונסו לבד.", hold=1.2),
    P("הפרמטרים לא משנים את גרהם-שמידט: הוא נעשה על הפורשים, ובהם אין פרמטרים.", do=show("b-c1")),
    P("המכפלה של הפורשים היא אחת, והנורמה של הראשון בריבוע שלוש. אז מחסירים שליש ממנו.", do=show("b-0")),
    P("כופלים בשלוש כדי להיפטר מהשברים: ארבע, מינוס אחת, חמש, שלוש. הנורמה בריבוע: חמישים ואחת.", do=show("b-1")),
    P("המכפלות עם המטריצה שלנו: עם הראשון $a+b$, ועם השני $5b-a$.", do=show("b-2"),
      say="המכפלות עם המטריצה שלנו: עם הראשון אֵיי ועוד בִּי, ועם השני חמש בִּי פחות אֵיי."),
    P("מציבים בנוסחה, ומחברים רכיב רכיב על מכנה משותף, שבע עשרה.", do=show("b-3", "b-4")),
    P("למשל הרכיב הראשון: $-\\frac{a+b}{3}+\\frac{4(5b-a)}{51}=\\frac{-7a+b}{17}$.",
      do=show("b-5"), say="למשל הרכיב הראשון: מינוס, בסוגריים אֵיי ועוד בִּי, חלקי שלוש, ועוד ארבע פעמים, בסוגריים חמש בִּי פחות אֵיי, חלקי "
                          "חמישים ואחת. יוצא, בסוגריים מינוס שבע אֵיי ועוד בִּי, חלקי שבע עשרה."),
    P("ובדיקה מהירה: מציבים $a=b=1$, ובודקים שהשארית ניצבת לשני הפורשים. היא ניצבת.", do=show("b-c2"), hold=0.3,
      say="ובדיקה מהירה: מציבים אֵיי ובִּי שווים אחת, ובודקים שהשארית ניצבת לשני הפורשים. היא ניצבת."),
    P("זהירות: בפתרון הרשמי של השאלה הזו נפלה טעות דפוס במקדם. אל תעתיקו, תחשבו.", do=show("b-c3"), hold=0.5),
], stage='<div class="pg-stack">' + w.rows("b", [
    r"$\langle V_2,V_1\rangle=1,\ \|V_1\|^2=3\ \Rightarrow\ U_2=V_2-\frac13V_1$",
    r"$3U_2=\begin{pmatrix}4&-1\\5&3\end{pmatrix},\quad \|3U_2\|^2=51$",
    r"$\langle X,V_1\rangle=a+b,\quad \langle X,3U_2\rangle=5b-a$",
    r"$\operatorname{Proj}=\frac{a+b}{3}\begin{pmatrix}-1&1\\1&0\end{pmatrix}+\frac{5b-a}{51}\begin{pmatrix}4&-1\\5&3\end{pmatrix}$",
    r"$=\frac{1}{17}\begin{pmatrix}-7a+b&6a+4b\\4a+14b&-a+5b\end{pmatrix}$",
    r"$-\frac{a+b}{3}+\frac{4(5b-a)}{51}=\frac{-7a+b}{17}$"], "sm") + "</div>",
   panel=w.stem("23B-A-Q5a", S2)
         + st.card("b-c1", "ex", "גרהם-שמידט על הפורשים: בלי $a,b$")
         + st.card("b-c2", "rule", "🔑 בדיקה עם $a=b=1$: השארית ⟂ שני הפורשים ✓")
         + st.card("b-c3", "trap", "⚠️ המקדם הנכון: $\\frac{5b-a}{51}$"))

S3 = ("נתונות 5 הנקודות $(-4,-1),(-2,0),(2,4),(4,5),(5,6)$. מצאו את משוואת הישר הקרוב ביותר אליהן במובן הריבועים הפחותים.")
q3 = Scene("q3", "שאלה 3", [
    P("שאלה שלישית: חמש נקודות, והישר הקרוב ביותר.", do=show("bl-pts")),
    P("עצרו כאן ונסו לבד.", hold=1.2),
    P("טבלת הסכומים: $\\sum x=5$ ו-$\\sum x^2=65$.", say="טבלת הסכומים: סכום האִקְסים חמש, וסכום הריבועים שישים וחמש.", do=show("c-0")),
    P("$\\sum y=14$ ו-$\\sum xy=62$.", say="סכום הוַואים ארבע עשרה, וסכום המכפלות שישים ושתיים.", do=show("c-1")),
    P("המערכת: שישים וחמש, חמש, חמש, חמש. הדטרמיננטה שלוש מאות.", do=show("c-2")),
    P("השיפוע: מאתיים ארבעים חלקי שלוש מאות, ארבע חמישיות. והחיתוך: שש מאות חלקי שלוש מאות, שתיים.", do=show("c-3", "c-4")),
    P("הישר: $y=\\frac45x+2$.", do=show("c-5", "bl-line"), say="הישר: וַואי שווה ארבע חמישיות אִקְס, ועוד שתיים."),
    P("בדיקה: השאריות הן חמישית, מינוס שתי חמישיות, שתי חמישיות, מינוס חמישית, ואפס. הסכום אפס.",
      do=show("c-6", "bl-res")),
    P("וזה לא מספיק: כל ישר שעובר בנקודת הממוצעים נותן סכום אפס. לכן בודקים גם את $\\sum x_i\\text{res}_i$.",
      say="וזה לא מספיק: כל ישר שעובר בנקודת הממוצעים נותן סכום אפס. לכן בודקים גם את הסכום של אִקְס כפול שארית."),
    P("מינוס ארבע חמישיות, ועוד ארבע חמישיות, ועוד ארבע חמישיות, פחות ארבע חמישיות, ועוד אפס: אפס. הישר נכון.",
      do=show("c-c"), hold=0.5),
], stage='<div class="pg-two">' + PLOT.replace('id="bl-pts"', 'id="bl-pts" class="h"') + w.rows("c", [
    r"$\sum x=5,\ \sum x^2=65$",
    r"$\sum y=14,\ \sum xy=62$",
    r"$\begin{pmatrix}65&5\\5&5\end{pmatrix}\begin{pmatrix}m\\n\end{pmatrix}=\begin{pmatrix}62\\14\end{pmatrix}$",
    r"$m=\frac{310-70}{300}=\frac45$",
    r"$n=\frac{910-310}{300}=2$",
    r"$y=\frac45x+2$",
    r"$\text{res}=\left(\frac15,-\frac25,\frac25,-\frac15,0\right)$"], "sm") + "</div>",
   panel=w.stem("24A-C-Q1a", S3) + st.card("c-c", "rule", "🔑 $\\sum\\text{res}=0$ וגם $\\sum x\\,\\text{res}=0$ ✓"))

recap = Scene("recap", "סיכום", [
    P("סיימנו. בכל שאלה עבדנו באותו סדר: קודם המכפלה הפנימית, אחר כך הבסיס, ואז הנוסחה.", do=show("r-1")),
    P("ובכל שאלה **בדקנו** שהשארית ניצבת: לפורשים, או לשתי העמודות של הישר. הבדיקה הזו תופסת טעויות חישוב רבות.", do=show("r-2")),
    P("זה הכול בקורס הזה. בהצלחה במבחן!", do=show("r-3"), hold=0.8),
], stage='<div class="pg-stack">' + w.big("r-0", r"\langle V-\operatorname{Proj},u_i\rangle=0", hidden=False) + "</div>",
   panel=st.card("r-1", "rule", "🔑 מכפלה → בסיס אורתוגונלי → נוסחה")
         + st.card("r-2", "rule", "🔑 תמיד בודקים את השארית")
         + st.card("r-3", "ex", "🏆 בהצלחה!"))

VIDEO = Video("P10", "proj_gs", "מבחן גמר: היטל, גרהם-שמידט וריבועים פחותים", [title, plan, q1, q2, q3, recap],
              bank={"26B-A-Q1b": None, "23B-A-Q5a": None, "24A-C-Q1a": None})
