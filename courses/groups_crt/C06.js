/* groups_crt, level 6: modular inverse, solving ax = b (mod m), reducing a congruence. */
COURSE_LEVEL("groups_crt", {
  id: "C06", order: 6, icon: "🔁", title: "הופכי מודולרי וצמצום קונגרואנציה",
  goal: "למצוא הופכי מודולרי, לפתור משוואה עם מקדם לפני x ולצמצם כל קונגרואנציה לצורה עם שארית קטנה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<h3>הופכי מודולרי</h3>
<p>ההופכי $a^{-1}\bmod m$ הוא המספר $x$ בין $0$ ל-$m-1$ שמקיים $ax\equiv1\pmod m$. הוא קיים אם ורק אם $\gcd(a,m)=1$. שלוש דרכים למצוא אותו:</p>
<ul>
<li><b>ניסוי</b> (מודול קטן): בודקים $a\cdot1,\ a\cdot2,\dots$ עד שמקבלים שארית $1$.</li>
<li><b>אוקלידס מורחב:</b> כותבים $1=aq+mt$ ואז $a^{-1}\equiv q$.</li>
<li><b>מודול ראשוני $p$:</b> לפי פרמה $a^{-1}\equiv a^{p-2}$.</li>
</ul>
<div class="lesson-ex">ניסוי: $4^{-1}\bmod9$. מתקיים $4\cdot7=28=3\cdot9+1$, ולכן $4^{-1}=7$.</div>
<div class="lesson-ex">אוקלידס: $7^{-1}\bmod30$. מחלקים: $30=4\cdot7+2$ ו-$7=3\cdot2+1$. מחזירים לאחור: $1=7-3\cdot2=7-3(30-4\cdot7)=13\cdot7-3\cdot30$. לכן $7^{-1}\equiv13\pmod{30}$, ואכן $7\cdot13=91=3\cdot30+1$.</div>
<h3>משוואה $ax\equiv b\pmod m$</h3>
<p>כש-$\gcd(a,m)=1$ כופלים את שני האגפים ב-$a^{-1}$ ומקבלים $x\equiv a^{-1}b\pmod m$. אם $\gcd(a,m)>1$ ייתכן שאין פתרון בכלל: למשל $2x\equiv1\pmod4$, כי אגף שמאל תמיד זוגי.</p>
<div class="lesson-ex">$2x\equiv5\pmod9$. מתקיים $2^{-1}=5$ (כי $2\cdot5=10\equiv1$), ולכן $x\equiv5\cdot5=25\equiv7\pmod9$. בדיקה: $2\cdot7=14\equiv5$.</div>
<h3>צמצום שארית</h3>
<p>כותבים כל קונגרואנציה בצורה $x\equiv r\pmod m$ עם $0\le r<m$, כלומר מחליפים את $r$ בשארית שלו בחלוקה ב-$m$. למשל $x\equiv23\pmod9$ הופך ל-$x\equiv5$, ו-$x\equiv-2\pmod5$ הופך ל-$x\equiv3$.</p>
<div class="lesson-trap">⚠️ $2x\equiv1\pmod5$ אינו $x\equiv1$. קודם כופלים בהופכי של המקדם: $x\equiv2^{-1}\cdot1=3$.</div>
<div class="lesson-rule">🔑 בסוף תמיד בודקים בהצבה במשוואה המקורית.</div>
` },
  questions: [
    { id: "C06-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהו ההופכי של $3$ מודולו $7$ (ערך בין $1$ ל-$6$) ?`,
        answer: 5, tol: 0,
        explain: String.raw`$3\cdot5=15=2\cdot7+1\equiv1\pmod7$, ולכן $3^{-1}=5$.` },
      recap: String.raw`מחפשים $k$ עם $ak\equiv1$.` },
    { id: "C06-Q2",
      question: String.raw`לאיזה מהמספרים הבאים אין הופכי מודולו $12$ ?`,
      options: [
        { id: "a", value: "$9$" },
        { id: "b", value: "$5$" },
        { id: "c", value: "$7$" },
        { id: "d", value: "$11$" },
      ],
      correctId: "a",
      explanation: String.raw`הופכי קיים בדיוק כש-$\gcd(a,12)=1$. מתקיים $\gcd(9,12)=3$, ולכן ל-$9$ אין הופכי. המספרים $5,7,11$ זרים ל-$12$: $5\cdot5=25\equiv1$, $7\cdot7=49\equiv1$ ו-$11\cdot11=121\equiv1$.`,
      recap: "הופכי קיים רק למספר זר למודול." },
    { id: "C06-Q3",
      step: { type: "numeric",
        prompt: String.raw`פתרו $5x\equiv3\pmod8$ וכתבו את הפתרון בין $0$ ל-$7$.`,
        answer: 7, tol: 0,
        explain: String.raw`$5^{-1}\equiv5\pmod8$ כי $5\cdot5=25\equiv1$. לכן $x\equiv5\cdot3=15\equiv7\pmod8$. בדיקה: $5\cdot7=35=4\cdot8+3$.` },
      recap: String.raw`$x\equiv a^{-1}b$.` },
    { id: "C06-Q4",
      question: String.raw`מצמצמים את הקונגרואנציות $x\equiv17\pmod5$, $x\equiv6\pmod2$ ו-$x\equiv-1\pmod7$ לצורה שבה כל שארית היא בין $0$ למודול פחות $1$. מה מתקבל?`,
      options: [
        { id: "a", value: String.raw`$x\equiv2\pmod5,\ \ x\equiv0\pmod2,\ \ x\equiv6\pmod7$` },
        { id: "b", value: String.raw`$x\equiv2\pmod5,\ \ x\equiv1\pmod2,\ \ x\equiv6\pmod7$` },
        { id: "c", value: String.raw`$x\equiv3\pmod5,\ \ x\equiv0\pmod2,\ \ x\equiv1\pmod7$` },
        { id: "d", value: String.raw`$x\equiv17\pmod5,\ \ x\equiv6\pmod2,\ \ x\equiv-1\pmod7$` },
      ],
      correctId: "a",
      explanation: String.raw`$17=3\cdot5+2$ ולכן השארית היא $2$. $6$ מתחלק ב-$2$ ולכן השארית היא $0$. $-1=-7+6$ ולכן השארית היא $6$. הצורה עם שארית $1$ מודולו $2$ שגויה, כי $6$ זוגי. הצורה עם שארית $3$ מודולו $5$ ושארית $1$ מודולו $7$ שגויה בשני הרכיבים. והמערכת שלא שונתה שקולה למקורית אבל אינה מצומצמת, והשאלה ביקשה שארית בתחום.`,
      recap: String.raw`שארית בין $0$ ל-$m-1$, גם למספר שלילי.` },
    { id: "C06-Q5",
      step: { type: "findbug",
        prompt: String.raw`מחשבים את $5^{-1}\bmod17$ באוקלידס המורחב. שורה אחת מכילה טעות חישוב. מצאו אותה.`,
        lines: [
          String.raw`$17=3\cdot5+2$`,
          String.raw`$5=2\cdot2+1$`,
          String.raw`$1=5-2\cdot2=5-2(17-3\cdot5)$`,
          String.raw`$1=5\cdot5-2\cdot17$`,
          String.raw`לכן $5^{-1}\equiv7\pmod{17}$`,
        ],
        bugIndex: 3,
        explain: String.raw`בפתיחת הסוגריים $5-2(17-3\cdot5)=5-2\cdot17+6\cdot5=7\cdot5-2\cdot17$. השורה $1=5\cdot5-2\cdot17$ שגויה: אגף ימין שלה שווה $25-34=-9$ ולא $1$. הערך הנכון $7\cdot5-2\cdot17=35-34=1$ נותן $5^{-1}\equiv7$.` },
      recap: "אוקלידס מורחב: בודקים בסוף שהמקדם כפול התוצאה נותן שארית $1$." },
    { bankId: "23B-B-Q2b", recap: "הופכי במכפלה ישרה: מוצאים הופכי בכל רכיב לפי המודול שלו." },
  ],
});
