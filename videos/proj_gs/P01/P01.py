# -*- coding: utf-8 -*-
"""P01 · מכפלה פנימית ונורמה — video script (build: tools/video/vid.py P01).

Source: courses/proj_gs/C01.js (lesson + goal). Exam anchor: 23A-S-Q1b (|u|=3, |u+v|=4, |u-v|=6, find |v|), which no
guided quiz uses. Avoided on purpose: the C01 quiz (its matrices, the formulas x1y1-x2y2 / x1y2+x2y1 /
(x1+x2)(y1+y2), |u|=2,|v|=3,<u,v>=-1) and 23A-B-Q3b / 24A-C-Q3b / 25A-C-Q3b (the polarization proof, a C01 quiz item
and its twins). Every number below is computed with sympy and asserted.
"""
from vid import P, Scene, Video, show, hide
import stage as st
import sympy as sp
import w_proj_gs as w
from w_proj_gs import V, M, R

# ---------------------------------------------------------------- R^n: u ⟂ v, |u| = 3
u, v = V(1, 2, -2), V(4, 1, 3)
assert [a * b for a, b in zip(u, v)] == [4, 2, -6] and w.dot(u, v) == 0
assert w.dot(u, u) == 9 and sp.sqrt(w.dot(u, u)) == 3

# ---------------------------------------------------------------- matrices: <A,B> = tr(B^T A)
A, B = M([[2, 1], [0, -1]]), M([[1, 3], [2, 1]])
assert [a * b for a, b in zip(A, B)] == [2, 3, 0, -1] and w.ip_m(A, B) == 4
assert w.ip_m(A, A) == 6
assert (A * B).trace() != 4              # the trap: the product AB is a different thing

# ---------------------------------------------------------------- a formula that is not an inner product
x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2", real=True)
G = sp.Matrix([[1, 2], [2, 1]])
form = lambda a, b: (sp.Matrix(a).T * G * sp.Matrix(b))[0]
assert sp.expand(form([x1, x2], [y1, y2]) - (x1 * y1 + 2 * x1 * y2 + 2 * x2 * y1 + x2 * y2)) == 0
assert sp.expand(form([x1, x2], [y1, y2]) - form([y1, y2], [x1, x2])) == 0          # symmetric
assert sp.expand(form([x1, x2], [x1, x2]) - (x1 ** 2 + 4 * x1 * x2 + x2 ** 2)) == 0
assert form([1, -1], [1, -1]) == -2                                                  # positivity fails
assert form([1, 0], [1, 0]) == 1                                                     # a "good" vector exists too

# ---------------------------------------------------------------- the expansion |u ± v|^2
a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2", real=True)
uu, vv = sp.Matrix([a1, a2]), sp.Matrix([b1, b2])
for s in (1, -1):
    assert sp.expand(w.dot(uu + s * vv, uu + s * vv) - (w.dot(uu, uu) + 2 * s * w.dot(uu, vv) + w.dot(vv, vv))) == 0

# ---------------------------------------------------------------- exam 23A-S-Q1b
nv2 = sp.Symbol("nv2", positive=True)              # |v|^2
ip = sp.Symbol("ip", real=True)                    # <u,v>
sol = sp.solve([sp.Eq(16, 9 + 2 * ip + nv2), sp.Eq(36, 9 - 2 * ip + nv2)], [nv2, ip], dict=True)
assert sol == [{nv2: 17, ip: -5}]
assert 16 + 36 == 2 * 9 + 2 * 17
# a real pair with these lengths (for the picture, and to show the data is consistent): u=(3,0), v=(-5/3, 8√2/3)
U = V(3, 0)
Vv = sp.Matrix([R(-5, 3), 8 * sp.sqrt(2) / 3])
assert w.dot(U, U) == 9 and sp.simplify(w.dot(Vv, Vv)) == 17 and w.dot(U, Vv) == -5
assert sp.simplify(w.dot(U + Vv, U + Vv)) == 16 and sp.simplify(w.dot(U - Vv, U - Vv)) == 36
assert 3 + sp.sqrt(17) != 4                         # the trap: |u+v| is not |u|+|v|
PARA = w.para("pa", [float(t) for t in U], [float(t) for t in Vv], box=(-2.6, 4.9, -1.0, 5.3), size=(640, 540))

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את הכלי שכל הקורס בנוי עליו: המכפלה הפנימית."),
    P("נחשב מכפלה ונורמה של וקטורים ושל מטריצות, ונראה איך מזהים נוסחה שאינה מכפלה פנימית."),
    P("ובסוף נפתור שאלה ממבחן, עם מלכודת קטנה.", hold=0.4),
], stage='<div class="kicker">P01 · היטל וגרהם-שמידט</div><h1>מכפלה פנימית ונורמה</h1>'
         '<p>לחשב מכפלה פנימית ונורמה ב-$\\mathbb{R}^n$ ובמרחב המטריצות, לזהות וקטורים ניצבים, '
         'ולהבחין בין נוסחה שהיא מכפלה פנימית לנוסחה שאינה.</p>', layout="title")

idea = Scene("idea", "הרעיון", [
    P("מכפלה פנימית היא כלל שמקבל שני וקטורים ומחזיר מספר אחד.", do=show("i-def"),
      say="מכפלה פנימית היא כלל שמקבל שני וקטורים ומחזיר מספר אחד."),
    P("כדי שכלל כזה ייקרא מכפלה פנימית, הוא חייב לקיים שלוש תכונות."),
    P("**סימטריה**: לא משנה באיזה סדר כותבים את שני הוקטורים.", do=show("i-1")),
    P("**לינאריות**: אפשר להוציא סקלרים ולפרק סכומים, כמו בכפל רגיל.", do=show("i-2")),
    P("ו**חיוביות**: מכפלה של וקטור בעצמו היא אי שלילית, ושווה לאפס רק לוקטור האפס.", do=show("i-3"), hold=0.3),
    P("מהמכפלה נגזרת הנורמה, כלומר האורך: השורש של המכפלה של הוקטור בעצמו.", do=show("i-n")),
    P("ושני וקטורים נקראים **ניצבים** כשהמכפלה הפנימית שלהם היא אפס.", do=show("i-p"), hold=0.4),
], stage='<div class="pg-stack">'
         + w.big("i-def", r"\langle u,v\rangle \in \mathbb{R}")
         + w.big("i-n", r"\|u\|=\sqrt{\langle u,u\rangle}")
         + w.big("i-p", r"u\perp v \iff \langle u,v\rangle=0")
         + "</div>",
   panel=st.card("i-1", "rule", "סימטריה: $\\langle u,v\\rangle=\\langle v,u\\rangle$")
         + st.card("i-2", "rule", "לינאריות: $\\langle \\alpha u+\\beta w,v\\rangle=\\alpha\\langle u,v\\rangle+\\beta\\langle w,v\\rangle$")
         + st.card("i-3", "rule", "חיוביות: $\\langle u,u\\rangle\\ge 0$, ושוויון רק עבור $u=0$"))

rn = Scene("rn", "ב-ℝⁿ", [
    P("נתחיל מהמרחב הרגיל. ב-$\\mathbb{R}^n$ מכפילים רכיב ברכיב, וסוכמים.", do=show("r-f"),
      say="נתחיל מהמרחב הרגיל. באר אֶן מכפילים רכיב ברכיב, וסוכמים."),
    P("ניקח את $u=(1,2,-2)$ ואת $v=(4,1,3)$.", do=show("r-0"),
      say="ניקח את יוּ, אחת, שתיים, מינוס שתיים, ואת וִי, ארבע, אחת, שלוש."),
    P("המכפלות של הרכיבים: ארבע, שתיים, ומינוס שש.", do=show("r-1")),
    P("הסכום הוא אפס. ולכן $u$ ו-$v$ **ניצבים**.", do=show("r-2", "r-c1"), hold=0.3),
    P("ועכשיו הנורמה של $u$: מכפילים את $u$ בעצמו.", do=show("r-3")),
    P("אחת ועוד ארבע ועוד ארבע, זה תשע. והשורש של תשע הוא שלוש.", do=show("r-4")),
    P("שימו לב לסימן המינוס: בריבוע הוא נעלם, ולכן הנורמה תמיד חיובית.", do=show("r-c2"), hold=0.4),
], stage='<div class="pg-stack">' + w.big("r-f", r"\langle u,v\rangle=\sum_k u_k v_k", "sm")
         + w.rows("r", [
             r"$u=(1,2,-2),\quad v=(4,1,3)$",
             r"$\langle u,v\rangle=1\cdot4+2\cdot1+(-2)\cdot3$",
             r"$=4+2-6=0$",
             r"$\|u\|^2=1^2+2^2+(-2)^2=9$",
             r"$\|u\|=\sqrt9=3$"]) + "</div>",
   panel=st.card("r-c1", "rule", "🔑 מכפלה אפס: $u\\perp v$")
         + st.card("r-c2", "ex", "הנורמה בריבוע היא סכום הריבועים"))

mat = Scene("mat", "מטריצות", [
    P("עכשיו מרחב המטריצות. המכפלה הפנימית המקובלת היא $\\operatorname{tr}(B^TA)$.", do=show("m-f"),
      say="עכשיו מרחב המטריצות. המכפלה הפנימית המקובלת היא העקבה של בִּי טְרַנְסְפּוֹז כפול אֵיי."),
    P("נשמע מסובך, אבל בפועל זה פשוט: מכפילים כל רכיב ברכיב שנמצא באותו מקום, וסוכמים.", do=show("m-c1")),
    P("ניקח שתי מטריצות.", do=show("m-0")),
    P("מכפילים מקום מול מקום: שתיים, שלוש, אפס, ומינוס אחת.", do=show("m-1")),
    P("הסכום הוא ארבע. זו המכפלה הפנימית.", do=show("m-2"), hold=0.3),
    P("והנורמה בריבוע של המטריצה הראשונה: סכום הריבועים של כל הרכיבים, שש.", do=show("m-3")),
    P("וזו המלכודת: זו **לא** מכפלת המטריצות $AB$. היא לא מטריצה, היא מספר אחד.", do=show("m-c2"),
      say="וזו המלכודת: זו לא מכפלת המטריצות אֵיי בִּי. היא לא מטריצה, היא מספר אחד.", hold=0.4),
], stage='<div class="pg-stack">' + w.big("m-f", r"\langle A,B\rangle=\operatorname{tr}(B^TA)=\sum_{i,j}a_{ij}b_{ij}", "sm")
         + w.rows("m", [
             f"$A={w.mat(A)},\\quad B={w.mat(B)}$",
             r"$\langle A,B\rangle=2\cdot1+1\cdot3+0\cdot2+(-1)\cdot1$",
             r"$=2+3+0-1=4$",
             r"$\|A\|^2=4+1+0+1=6$"]) + "</div>",
   panel=st.card("m-c1", "rule", "🔑 רכיב מול רכיב באותו מקום, וסכום")
         + st.card("m-c2", "trap", "⚠️ זו לא המכפלה $AB$: התוצאה היא מספר"))

axiom = Scene("axiom", "נוסחה חשודה", [
    P("האם כל נוסחה עם שני וקטורים היא מכפלה פנימית? בואו נבדוק נוסחה אחת ב-$\\mathbb{R}^2$.", do=show("a-0"),
      say="האם כל נוסחה עם שני וקטורים היא מכפלה פנימית? בואו נבדוק נוסחה אחת באר שתיים."),
    P("היא סימטרית: אם מחליפים בין הוקטורים, מקבלים את אותו סכום.", do=show("a-c1")),
    P("והיא לינארית, כי כל איבר בה הוא מכפלה של רכיב אחד מכל וקטור.", do=show("a-c2")),
    P("נשארה החיוביות, והיא החלק הקשה. נציב את אותו וקטור בשני המקומות.", do=show("a-1")),
    P("ננסה את הוקטור אחת, מינוס אחת: אחת, פחות ארבע, ועוד אחת.", do=show("a-2")),
    P("יוצא מינוס שתיים. וקטור שונה מאפס, עם מכפלה שלילית בעצמו!", do=show("a-3"), hold=0.3),
    P("ולכן הנוסחה הזו **אינה** מכפלה פנימית, אף שהיא סימטרית ולינארית.", do=show("a-c3")),
    P("הכלל: כדי לפסול נוסחה, מספיק למצוא וקטור אחד שמפיל את החיוביות.", hold=0.4),
], stage='<div class="pg-stack">'
         + w.rows("a", [
             r"$\langle u,v\rangle=x_1y_1+2x_1y_2+2x_2y_1+x_2y_2$",
             r"$\langle u,u\rangle=x_1^2+4x_1x_2+x_2^2$",
             r"$u=(1,-1):\quad 1-4+1$",
             r"$=-2<0$"], "sm") + "</div>",
   panel=st.card("a-c1", "ex", "סימטריה ✓")
         + st.card("a-c2", "ex", "לינאריות ✓")
         + st.card("a-c3", "trap", "⚠️ חיוביות ✗: $u\\ne0$ אבל $\\langle u,u\\rangle<0$"))

expand = Scene("expand", "פתיחת סוגריים", [
    P("עוד כלי אחד לפני המבחן: הנורמה של סכום.", do=show("e-0")),
    P("פותחים סוגריים בעזרת הלינאריות: מכפלה של סכום בעצמו נותנת ארבעה איברים.", do=show("e-1")),
    P("ובזכות הסימטריה, שני האיברים האמצעיים שווים. אז מקבלים פעמיים המכפלה הפנימית.", do=show("e-2"), hold=0.3),
    P("עם מינוס זה אותו דבר, רק שהאיבר האמצעי מחליף סימן.", do=show("e-3")),
    P("שימו לב: הנורמה של הסכום היא **לא** סכום הנורמות. יש את האיבר האמצעי.", do=show("e-c"), hold=0.4),
], stage='<div class="pg-stack">' + w.rows("e", [
    r"$\|u+v\|^2=\langle u+v,u+v\rangle$",
    r"$=\langle u,u\rangle+\langle u,v\rangle+\langle v,u\rangle+\langle v,v\rangle$",
    r"$\|u+v\|^2=\|u\|^2+2\langle u,v\rangle+\|v\|^2$",
    r"$\|u-v\|^2=\|u\|^2-2\langle u,v\rangle+\|v\|^2$"], "sm") + "</div>",
   panel=st.card("e-c", "trap", "⚠️ $\\|u+v\\|\\ne\\|u\\|+\\|v\\|$ באופן כללי"))

EX_STEM = ("במרחב מכפלה פנימית נתונים $\\|u\\|=3$, $\\|u+v\\|=4$, $\\|u-v\\|=6$. מצאו את $\\|v\\|$.")
exam = Scene("exam", "שאלה ממבחן", [
    P("ועכשיו שאלה ממבחן: $\\|u\\|=3$, $\\|u+v\\|=4$ ו-$\\|u-v\\|=6$.",
      say="ועכשיו שאלה ממבחן. הנורמה של יוּ היא שלוש, של, בסוגריים, יוּ ועוד וִי, ארבע, ושל, בסוגריים, יוּ פחות וִי, שש."),
    P("צריך למצוא את $\\|v\\|$. ואין לנו את הוקטורים עצמם, רק אורכים.", do=show("pa-u", "pa-v", "pa-sides"),
      say="צריך למצוא את הנורמה של וִי. ואין לנו את הוקטורים עצמם, רק אורכים."),
    P("$u+v$ ו-$u-v$ הם שני האלכסונים של המקבילית.", do=show("pa-s", "pa-d"),
      say="יוּ ועוד וִי, ויוּ פחות וִי, הם שני האלכסונים של המקבילית."),
    P("נכתוב את שתי הפתיחות, ונציב את מה שידוע.", do=show("x-0", "x-1")),
    P("נחבר את שתי השורות: האיבר האמצעי מתבטל.", do=show("x-2")),
    P("זה **כלל המקבילית**: סכום ריבועי האלכסונים שווה לפעמיים סכום ריבועי הצלעות.", do=show("x-c1")),
    P("מציבים: שש עשרה ועוד שלושים ושש, זה חמישים ושתיים.", do=show("x-3")),
    P("פחות שמונה עשרה, ונחלק בשתיים: $\\|v\\|^2=17$.", do=show("x-4"),
      say="פחות שמונה עשרה, ונחלק בשתיים: הנורמה של וִי בריבוע היא שבע עשרה."),
    P("ולכן $\\|v\\|=\\sqrt{17}$.", do=show("x-5"), hold=0.3, say="ולכן הנורמה של וִי היא שורש שבע עשרה."),
    P("המלכודת: לחשוב ש-$4=3+\\|v\\|$. נורמה של סכום איננה סכום נורמות.", do=show("x-c2"),
      hold=0.5, say="המלכודת: לחשוב שארבע שווה שלוש ועוד הנורמה של וִי. נורמה של סכום איננה סכום נורמות."),
], stage='<div class="pg-two">' + PARA + w.rows("x", [
    r"$16=9+2\langle u,v\rangle+\|v\|^2$",
    r"$36=9-2\langle u,v\rangle+\|v\|^2$",
    r"$16+36=2\cdot9+2\|v\|^2$",
    r"$52=18+2\|v\|^2$",
    r"$\|v\|^2=17$",
    r"$\|v\|=\sqrt{17}$"], "sm left") + "</div>",
   panel=w.stem("23A-S-Q1b", EX_STEM)
         + st.card("x-c1", "rule", "$\\|u+v\\|^2+\\|u-v\\|^2=2\\|u\\|^2+2\\|v\\|^2$")
         + st.card("x-c2", "trap", "⚠️ לא $4=3+\\|v\\|$"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: מכפלה פנימית חייבת להיות סימטרית, לינארית וחיובית.", do=show("c-1")),
    P("ב-$\\mathbb{R}^n$ ובמטריצות: מכפילים רכיב מול רכיב וסוכמים. הנורמה היא שורש המכפלה העצמית.", do=show("c-2"),
      say="באר אֶן ובמטריצות: מכפילים רכיב מול רכיב וסוכמים. הנורמה היא שורש המכפלה העצמית."),
    P("ניצבים פירושו מכפלה אפס. ונוסחה נפסלת אם וקטור אחד שונה מאפס מפיל את החיוביות.", do=show("c-3")),
    P("ובפתיחת סוגריים: יש את האיבר האמצעי. נתראה ברמה הבאה.", do=show("c-4"), hold=0.6),
], stage='<div class="pg-stack">' + w.big("c-0", r"\|u\pm v\|^2=\|u\|^2\pm2\langle u,v\rangle+\|v\|^2", "sm", hidden=False)
         + "</div>",
   panel=st.card("c-1", "rule", "🔑 סימטריה, לינאריות, חיוביות")
         + st.card("c-2", "rule", "🔑 $\\|u\\|=\\sqrt{\\langle u,u\\rangle}$")
         + st.card("c-3", "rule", "🔑 $u\\perp v\\iff\\langle u,v\\rangle=0$")
         + st.card("c-4", "trap", "⚠️ $\\|u+v\\|\\ne\\|u\\|+\\|v\\|$"))

VIDEO = Video("P01", "proj_gs", "מכפלה פנימית ונורמה", [title, idea, rn, mat, axiom, expand, exam, recap],
              bank={"23A-S-Q1b": None})
