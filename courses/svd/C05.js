/* SVD course, level 5 - the columns of U via u_i = A v_i / sigma_i */
COURSE_LEVEL("svd", {
  id: "C05", order: 5, icon: "🔗", title: "העמודות של U לפי u_i = Av_i / σ_i",
  goal: "אחרי השלב הזה אפשר לחשב כל עמודה $u_i$ מתוך $v_i$ ו-$\\sigma_i\\ne0$, ולהסביר למה לא מוצאים אותה בפירוק נפרד.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>אחרי שיש לנו את $V$ ואת הערכים הסינגולריים, העמודות של $U$ שמתאימות ל-$\sigma_i\ne0$ מתקבלות בנוסחה אחת:</p>
    <div class="lesson-formula">$$u_i=\frac{1}{\sigma_i}\,Av_i$$</div>
    <p>הנוסחה הזו אומרת בדיוק $Av_i=\sigma_iu_i$, וזה מה שהפירוק $A=USV^T$ דורש עמודה אחר עמודה.</p>
    <ul>
      <li><b>האורך כבר 1:</b> $\|Av_i\|=\sigma_i$, ולכן חלוקה ב-$\sigma_i$ נותנת וקטור מנורמלים.</li>
      <li><b>הניצבות מובטחת:</b> כשה-$v_i$ ניצבים זה לזה, גם ה-$u_i$ ניצבים זה לזה.</li>
      <li>אם פירקתם את $AA^T$ במקום $A^TA$, הכיוון הפוך: $v_i=\frac1{\sigma_i}A^Tu_i$.</li>
    </ul>
    <div class="lesson-ex"><b>דוגמה.</b> $A=\begin{pmatrix}1&1\\0&1\\1&0\end{pmatrix}$, $\sigma_1=\sqrt3$, $\sigma_2=1$, $v_1=\frac1{\sqrt2}(1,1)$, $v_2=\frac1{\sqrt2}(1,-1)$.<br>
    $Av_1=\frac1{\sqrt2}(2,1,1)$ ולכן $u_1=\frac{1}{\sqrt3}\cdot\frac1{\sqrt2}(2,1,1)=\frac1{\sqrt6}(2,1,1)$.<br>
    $Av_2=\frac1{\sqrt2}(0,-1,1)$ ו-$\sigma_2=1$ ולכן $u_2=\frac1{\sqrt2}(0,-1,1)$.</div>
    <div class="lesson-rule">🔑 <b>למה לא מוצאים את $U$ בפירוק נפרד של $AA^T$?</b> גם $-u_i$ הוא וקטור עצמי מנורמלי של $AA^T$ עם אותו ערך עצמי. אם בוחרים את הסימן בנפרד מ-$v_i$, אפשר לקבל $Av_i=-\sigma_iu_i$ והפירוק יוצא שגוי. הנוסחה $u_i=\frac1{\sigma_i}Av_i$ קובעת את הסימן אוטומטית.</div>
    <div class="lesson-trap">⚠️ אם $\sigma_i=0$ אי אפשר לחלק ב-$\sigma_i$, ולכן הנוסחה עובדת רק לערכים סינגולריים שונים מאפס. את שאר העמודות של $U$ משלימים בשלב הבא.</div>` },
  questions: [
    { id: "C05-Q1",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&2\\2&1\\0&0\end{pmatrix}$, $\sigma_1=3$ ו-$v_1=\frac1{\sqrt2}(1,1)$. מהו האורך $\|Av_1\|$ ?`,
        answer: 3, tol: 0,
        explain: String.raw`$Av_1=\frac1{\sqrt2}(3,3,0)$ ואורכו $\frac1{\sqrt2}\sqrt{18}=3$, שווה ל-$\sigma_1$. לכן $u_1=\frac13Av_1$ הוא באורך 1.` },
      recap: String.raw`$\|Av_i\|=\sigma_i$, ולכן $u_i$ יוצא באורך 1.` },
    { id: "C05-Q2",
      question: String.raw`באותה מטריצה $A=\begin{pmatrix}1&2\\2&1\\0&0\end{pmatrix}$, עם $\sigma_1=3$ ו-$v_1=\frac1{\sqrt2}(1,1)$: מהו $u_1$ ?`,
      options: [
        { id: "a", value: String.raw`$\frac1{\sqrt2}(3,3,0)$` },
        { id: "b", value: String.raw`$\frac1{\sqrt2}(1,-1,0)$` },
        { id: "c", value: String.raw`$\frac13(1,1,0)$` },
        { id: "d", value: String.raw`$\frac1{\sqrt2}(1,1,0)$` },
      ],
      correctId: "d",
      explanation: String.raw`$Av_1=\frac1{\sqrt2}(3,3,0)$ וחלוקה ב-$\sigma_1=3$ נותנת $u_1=\frac1{\sqrt2}(1,1,0)$. הווקטור $\frac1{\sqrt2}(3,3,0)$ הוא $Av_1$ בלי החלוקה ב-$\sigma_1$ ואורכו 3. הווקטור $\frac13(1,1,0)$ מחלק את הווקטור הלא-מנורמלי $(1,1,0)$ ב-3 במקום ב-$\sqrt2$, ואורכו $\frac{\sqrt2}3$ ולא 1. הווקטור $\frac1{\sqrt2}(1,-1,0)$ אינו כיוון של $Av_1$.`,
      recap: String.raw`$u_1=\frac1{\sigma_1}Av_1$, מחשבים מכפלה ואז מחלקים.` },
    { id: "C05-Q3",
      question: String.raw`באותה מטריצה, עם $\sigma_2=1$ ו-$v_2=\frac1{\sqrt2}(1,-1)$ שנבחר מראש: מהו $u_2$ ?`,
      options: [
        { id: "a", value: String.raw`$\frac1{\sqrt2}(1,-1,0)$` },
        { id: "b", value: String.raw`$\frac1{\sqrt2}(-1,1,0)$` },
        { id: "c", value: String.raw`$\frac1{\sqrt2}(1,1,0)$` },
        { id: "d", value: String.raw`$\frac1{\sqrt2}(-3,3,0)$` },
      ],
      correctId: "b",
      explanation: String.raw`$Av_2=\frac1{\sqrt2}(1-2,\,2-1,\,0)=\frac1{\sqrt2}(-1,1,0)$, ו-$\sigma_2=1$, ולכן $u_2=\frac1{\sqrt2}(-1,1,0)$. הווקטור $\frac1{\sqrt2}(1,-1,0)$ הוא וקטור עצמי תקין של $AA^T$ אבל נותן $Av_2=-\sigma_2u_2$, כלומר סימן הפוך ביחס ל-$v_2$ הנתון. הווקטור $\frac1{\sqrt2}(1,1,0)$ הוא $u_1$. הווקטור האחרון אינו מנורמל.`,
      recap: String.raw`הסימן של $u_i$ נקבע מ-$v_i$ הנבחר, ולא נבחר בנפרד.` },
    { id: "C05-Q4",
      question: String.raw`מדוע מחשבים את $u_i$ מהנוסחה $u_i=\frac1{\sigma_i}Av_i$ ולא מוצאים את העמודות של $U$ בפירוק נפרד של $AA^T$ ?`,
      options: [
        { id: "a", value: String.raw`כי ל-$AA^T$ אין וקטורים עצמיים` },
        { id: "b", value: String.raw`כי הוקטורים העצמיים של $AA^T$ נקבעים עד כדי סימן, ובחירה בלתי תלויה עלולה לתת $Av_i=-\sigma_iu_i$` },
        { id: "c", value: String.raw`כי ל-$AA^T$ ול-$A^TA$ ערכים עצמיים שונים מאפס שונים זה מזה` },
        { id: "d", value: String.raw`כי $u_i$ חייב להיות שווה ל-$v_i$` },
      ],
      correctId: "b",
      explanation: String.raw`וקטור עצמי מנורמלי נקבע רק עד כדי סימן, וזוג $(u_i,v_i)$ שנבחרו בנפרד עלול לקיים $Av_i=-\sigma_iu_i$ ולא $Av_i=\sigma_iu_i$, ואז $USV^T\ne A$. ל-$AA^T$ יש וקטורים עצמיים, כי היא סימטרית. הערכים העצמיים השונים מאפס של שתי המטריצות זהים, ולא שונים. ו-$u_i$ שייך ל-$\mathbb{R}^m$ ו-$v_i$ שייך ל-$\mathbb{R}^n$, ולכן הם בדרך כלל אפילו לא באותו גודל.`,
      recap: String.raw`$u_i$ מחושב מ-$v_i$ כדי שהסימנים יתאימו.` },
    { id: "C05-Q5",
      step: { type: "order",
        prompt: String.raw`סדרו את שלבי החישוב של העמודה $u_i$ לערך סינגולרי $\sigma_i\ne0$.`,
        lines: [
          String.raw`לוקחים את $v_i$ ואת $\sigma_i\neq0$ שחושבו קודם`,
          String.raw`מחשבים את המכפלה $Av_i$`,
          String.raw`מחלקים ב-$\sigma_i$: $u_i=\frac{1}{\sigma_i}Av_i$`,
          String.raw`בודקים ש-$\|u_i\|=1$ ושה-$u_i$ ניצבים זה לזה`,
        ],
        explain: String.raw`צריך את $v_i$ ו-$\sigma_i$ לפני שמכפילים, מכפילים לפני שמחלקים, ובודקים בסוף.` },
      recap: String.raw`מכפילים $Av_i$, מחלקים ב-$\sigma_i$, בודקים.` },
    { id: "C05-Q6",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$ ידוע ש-$\sigma_1=\sqrt3$ ו-$v_1=\frac1{\sqrt2}(1,1)$. מהי הקואורדינטה השנייה של $u_1$ ? (ענו בקירוב עד שתי ספרות אחרי הנקודה)`,
        answer: 0.8165, tol: 0.01,
        explain: String.raw`$Av_1=\frac1{\sqrt2}(1,2,1)$ ולכן $u_1=\frac1{\sqrt3}\cdot\frac1{\sqrt2}(1,2,1)=\frac1{\sqrt6}(1,2,1)$. הקואורדינטה השנייה היא $\frac2{\sqrt6}\approx0.8165$.` },
      recap: String.raw`$u_1=\frac1{\sigma_1}Av_1$, כולל השורש בחלוקה.` },
  ],
});
