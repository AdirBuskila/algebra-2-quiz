/* groups_crt, level 7: matrix groups over Z_p. */
COURSE_LEVEL("groups_crt", {
  id: "C07", order: 7, icon: "🧮", title: "חבורות מטריצות מודולו מספר ראשוני",
  goal: "לספור איברים בחבורת מטריצות מעל שדה סופי, למצוא הופכי, ולחשב סדר של מטריצה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>במטריצות מעל $\mathbb{Z}_p$ הרכיבים הם מספרים בין $0$ ל-$p-1$, וכל חיבור וכפל (גם בכפל מטריצות) מחושבים מודולו $p$. הניטרלי בכפל מטריצות הוא מטריצת היחידה $I$.</p>
<h3>הוכחה שקבוצת מטריצות היא חבורה</h3>
<p>בודקים: <b>סגירות</b> (מכפילים שתי מטריצות כלליות מהצורה ורואים שהמכפלה באותה צורה ועומדת באותו תנאי), <b>אסוציאטיביות</b> (כפל מטריצות אסוציאטיבי תמיד), <b>ניטרלי</b> ($I$ שייכת לקבוצה) ו<b>הופכי</b> (מחשבים את ההופכי ובודקים שהוא באותה צורה).</p>
<h3>ספירת איברים</h3>
<p>בעקרון הכפל סופרים כל רכיב בנפרד ומכפילים. למשל מטריצות $\begin{pmatrix}1&b\\0&c\end{pmatrix}$ מעל $\mathbb{Z}_5$ עם $c\ne0$: $5$ ערכים ל-$b$ ו-$4$ ל-$c$, ובסך הכול $5\cdot4=20$.</p>
<h3>הופכי של מטריצה משולשית עליונה</h3>
<p>מחפשים $\begin{pmatrix}x&y\\0&z\end{pmatrix}$ שמקיימת
$$\begin{pmatrix}a&b\\0&c\end{pmatrix}\begin{pmatrix}x&y\\0&z\end{pmatrix}=\begin{pmatrix}ax&ay+bz\\0&cz\end{pmatrix}=I.$$
מכאן $x=a^{-1}$, $z=c^{-1}$ ו-$y=-a^{-1}bz$, הכול מודולו $p$.</p>
<div class="lesson-ex">מעל $\mathbb{Z}_7$: ההופכי של $\begin{pmatrix}2&1\\0&3\end{pmatrix}$. מתקיים $x=2^{-1}=4$, $z=3^{-1}=5$ ו-$y=-4\cdot1\cdot5=-20\equiv1$. לכן ההופכי הוא $\begin{pmatrix}4&1\\0&5\end{pmatrix}$. בדיקה: המכפלה היא $\begin{pmatrix}8&7\\0&15\end{pmatrix}\equiv I$.</div>
<h3>סדר של מטריצה</h3>
<p>מעלים את המטריצה בחזקות, מודולו $p$ בכל שלב, עד שמגיעים ל-$I$. שני קיצורים: מטריצה אלכסונית $\operatorname{diag}(u,v)$ מקיימת $o=\operatorname{lcm}(o(u),o(v))$, ומטריצה $\begin{pmatrix}1&b\\0&1\end{pmatrix}$ עם $b\ne0$ מסדר $p$, כי החזקה ה-$n$ שלה היא $\begin{pmatrix}1&nb\\0&1\end{pmatrix}$.</p>
<div class="lesson-ex">מעל $\mathbb{Z}_7$ נחשב את הסדר של $\operatorname{diag}(2,6)$. מתקיים $o(2)=3$ ו-$o(6)=2$, ולכן הסדר הוא $\operatorname{lcm}(3,2)=6$.</div>
<div class="lesson-trap">⚠️ שוכחים לצמצם מודולו $p$ בכל שלב, ושוכחים ש-$-1$ הוא $p-1$.</div>
` },
  questions: [
    { id: "C07-Q1",
      step: { type: "numeric",
        prompt: String.raw`כמה מטריצות מהצורה $\begin{pmatrix}a&b\\0&a\end{pmatrix}$ עם $a\ne0$ יש מעל $\mathbb{Z}_7$ ?`,
        answer: 42, tol: 0,
        explain: String.raw`ל-$a$ יש $6$ ערכים (כל ערך חוץ מ-$0$), ול-$b$ יש $7$ ערכים. לפי עקרון הכפל $6\cdot7=42$.` },
      recap: "עקרון הכפל: מכפילים את מספר הבחירות לכל רכיב." },
    { id: "C07-Q2",
      step: { type: "numeric",
        prompt: String.raw`מהו הסדר של $\begin{pmatrix}1&3\\0&1\end{pmatrix}$ מעל $\mathbb{Z}_7$ ?`,
        answer: 7, tol: 0,
        explain: String.raw`החזקה ה-$n$ היא $\begin{pmatrix}1&3n\\0&1\end{pmatrix}$. היא שווה ל-$I$ כש-$3n\equiv0\pmod7$, ומכיוון ש-$3$ הפיך מודולו $7$ זה קורה כש-$n\equiv0$. הקטן החיובי הוא $7$.` },
      recap: String.raw`מטריצה $\begin{pmatrix}1&b\\0&1\end{pmatrix}$ עם $b\ne0$ מעל $\mathbb{Z}_p$ היא מסדר $p$.` },
    { id: "C07-Q3",
      question: String.raw`מהו ההופכי של $\begin{pmatrix}1&3\\0&2\end{pmatrix}$ מעל $\mathbb{Z}_5$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&1\\0&3\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}1&2\\0&3\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}1&3\\0&3\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}1&1\\0&2\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`מתקיים $x=1^{-1}=1$ ו-$z=2^{-1}=3$ (כי $2\cdot3=6\equiv1$), ו-$y=-x\cdot b\cdot z=-1\cdot3\cdot3=-9\equiv1$. לכן ההופכי הוא $\begin{pmatrix}1&1\\0&3\end{pmatrix}$. כששוכחים להכפיל ב-$z$ מקבלים $y=-3\equiv2$, וזו המטריצה עם $2$ בפינה הימנית העליונה. כשמשאירים $y=b$ מקבלים $3$ שם. וכשלא הופכים את $2$ מקבלים מטריצה שהמכפלה שלה עם המקורית אינה $I$.`,
      recap: String.raw`$y=-a^{-1}bz$, כאשר $z=c^{-1}$.` },
    { id: "C07-Q4",
      step: { type: "numeric",
        prompt: String.raw`מהו הסדר של $\begin{pmatrix}2&0\\0&4\end{pmatrix}$ מעל $\mathbb{Z}_7$ ?`,
        answer: 3, tol: 0,
        explain: String.raw`$o(2)=3$ כי $2^3=8\equiv1$, וגם $o(4)=3$ כי $4^3=64\equiv1$. הסדר הוא $\operatorname{lcm}(3,3)=3$, ולא המכפלה $9$.` },
      recap: String.raw`הסדר של מטריצה אלכסונית הוא $\operatorname{lcm}$ של סדרי רכיבי האלכסון.` },
    { bankId: "24A-A-Q4a", recap: "מספר האיברים: ספירת בחירות לכל רכיב בלי אפס באלכסון." },
    { bankId: "24A-A-Q4c", recap: "הופכי של מטריצה משולשית: x, z ואז y." },
  ],
});
