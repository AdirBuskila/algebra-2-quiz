/* proj_gs, level 2 - inner product on function spaces: integral form, weights, even/odd on symmetric intervals */
COURSE_LEVEL("proj_gs", {
  id: "C02", order: 2, icon: "∫", title: "מכפלה פנימית של פונקציות",
  goal: "לחשב מכפלה פנימית ונורמה של פונקציות באמצעות אינטגרל, ולנצל זוגיות ואי-זוגיות כדי לזהות ניצבות מיד.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>במרחב $C[a,b]$ של הפונקציות הרציפות בקטע, המכפלה הפנימית הרגילה היא אינטגרל של המכפלה:
$$\langle f,g\rangle=\int_a^b f(x)g(x)\,dx,\qquad \|f\|^2=\int_a^b f(x)^2\,dx.$$
לפעמים מוסיפים <b>משקל</b> חיובי $w(x)$: $\langle f,g\rangle=\int_a^b w(x)f(x)g(x)\,dx$. המשקל נשאר בתוך כל אינטגרל, גם בנורמה.</p>
<div class="lesson-ex">דוגמה ב-$C[-1,1]$: $\langle 1,1\rangle=\int_{-1}^{1}1\,dx=2$, ולכן $\|1\|=\sqrt2$. וגם $\langle x^2,1\rangle=\int_{-1}^{1}x^2\,dx=\frac23$.</div>
<p><b>קיצור בקטע סימטרי $[-a,a]$.</b> פונקציה $f$ היא זוגית אם $f(-x)=f(x)$, ואי-זוגית אם $f(-x)=-f(x)$. האינטגרל של אי-זוגית על קטע סימטרי הוא $0$, והאינטגרל של זוגית הוא פעמיים האינטגרל על $[0,a]$.</p>
<ul>
<li>אי-זוגית כפול זוגית היא אי-זוגית, ולכן <b>הפונקציות ניצבות</b>: למשל $x$ ו-$x^2$ ב-$C[-1,1]$.</li>
<li>זוגית כפול זוגית היא זוגית: אין ניצבות אוטומטית.</li>
<li>הפונקציה $|x|$ <b>זוגית</b>, אף שהיא נראית כמו $x$.</li>
</ul>
<div class="lesson-rule">🔑 כדי להראות שנוסחה היא מכפלה פנימית בודקים סימטריה, לינאריות וחיוביות. החיוביות היא החלק הקשה: $\int w f^2\ge0$ ושווה לאפס רק כש-$f\equiv0$ (כי $f$ רציפה ו-$w>0$).</div>
<div class="lesson-trap">⚠️ אינטגרל על קטע סימטרי נותן אפס רק לאי-זוגית. $\int_{-1}^{1}|x|\,dx=1$ ולא $0$.</div>
` },
  questions: [
    { id: "C02-Q1",
      step: { type: "numeric",
        prompt: String.raw`ב-$C[0,1]$ עם $\langle f,g\rangle=\int_0^1 f(x)g(x)\,dx$ חשבו $\langle x,x^2\rangle$.`,
        answer: 0.25, tol: 0.001,
        explain: String.raw`$\int_0^1 x\cdot x^2\,dx=\int_0^1x^3\,dx=\frac14$.` },
      recap: "מכפלה פנימית של פונקציות: אינטגרל של המכפלה." },
    { id: "C02-Q2",
      question: String.raw`ב-$C[-1,1]$ עם $\langle f,g\rangle=\int_{-1}^{1}f(x)g(x)\,dx$, איזה זוג פונקציות ניצב ?`,
      options: [
        { id: "a", value: String.raw`$x$ ו-$x^2$` },
        { id: "b", value: String.raw`$1$ ו-$x^2$` },
        { id: "c", value: String.raw`$1$ ו-$|x|$` },
        { id: "d", value: String.raw`$x^2$ ו-$|x|$` }],
      correctId: "a",
      explanation: String.raw`$x$ אי-זוגית ו-$x^2$ זוגית, ולכן המכפלה $x^3$ אי-זוגית והאינטגרל שלה על הקטע הסימטרי הוא $0$. בשאר הזוגות שתי הפונקציות זוגיות והמכפלה חיובית: $\int x^2=\frac23$, $\int|x|=1$, $\int x^2|x|=\frac12$.`,
      recap: "אי-זוגית כפול זוגית על קטע סימטרי: אינטגרל אפס." },
    { id: "C02-Q3",
      step: { type: "numeric",
        prompt: String.raw`ב-$C[0,3]$ עם $\langle f,g\rangle=\int_0^3 f(x)g(x)\,dx$ חשבו את $\|x\|^2$.`,
        answer: 9, tol: 0,
        explain: String.raw`$\|x\|^2=\int_0^3x^2\,dx=\left[\frac{x^3}{3}\right]_0^3=9$.` },
      recap: "נורמה בריבוע: אינטגרל של הריבוע." },
    { id: "C02-Q4",
      step: { type: "numeric",
        prompt: String.raw`ב-$C[0,1]$ עם $\langle f,g\rangle=\int_0^1 f(x)g(x)\,dx$ נתונות $f(x)=x$ ו-$g(x)=3x+c$. עבור איזה $c$ הפונקציות ניצבות ?`,
        answer: -2, tol: 0,
        explain: String.raw`$\langle f,g\rangle=\int_0^1(3x^2+cx)\,dx=1+\frac c2$. השוויון ל-$0$ נותן $c=-2$.` },
      recap: "ניצבות עם פרמטר: מחשבים את המכפלה כפונקציה של הפרמטר ומשווים לאפס." },
    { id: "C02-Q5",
      question: String.raw`ב-$C[0,1]$ מגדירים $\langle f,g\rangle=\int_0^1e^x f(x)g(x)\,dx$. מהו $\|1\|^2$ ?`,
      options: [
        { id: "a", value: String.raw`$e-1$` },
        { id: "b", value: String.raw`$1$` },
        { id: "c", value: String.raw`$e$` },
        { id: "d", value: String.raw`$\frac{e-1}{2}$` }],
      correctId: "a",
      explanation: String.raw`המשקל $e^x$ נכנס לאינטגרל: $\int_0^1e^x\cdot1\cdot1\,dx=e-1$. הערך $1$ הוא התוצאה בלי המשקל. הערך $e$ שוכח את הגבול התחתון. והערך $\frac{e-1}{2}$ מחלק בלי סיבה.`,
      recap: "המשקל נשאר בכל אינטגרל, כולל בנורמה." },
    { bankId: "23A-A-Q2a", recap: "בודקים סימטריה, לינאריות וחיוביות של האינטגרל עם המשקל." },
  ],
});
