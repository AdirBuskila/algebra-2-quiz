/* SVD course, level 4 - the columns of V */
COURSE_LEVEL("svd", {
  id: "C04", order: 4, icon: "🧭", title: "העמודות של V",
  goal: "אחרי השלב הזה אפשר למצוא את $v_1,\\dots,v_n$ כווקטורים עצמיים מנורמלים של $A^TA$ ולסדר אותם נכון בעמודות $V$.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>העמודות של $V$ הן וקטורים עצמיים <b>מנורמלים</b> של $A^TA$. לכל ערך עצמי $\lambda_i$:</p>
    <ol>
      <li>פותרים את המערכת ההומוגנית $(A^TA-\lambda_iI)x=0$ ומקבלים וקטור $x$ (או כמה).</li>
      <li><b>מנרמלים</b>: $v_i=\dfrac{x}{\|x\|}$, כדי שהאורך יהיה 1.</li>
      <li>מסדרים את העמודות <b>באותו סדר</b> כמו הערכים הסינגולריים: $v_1$ שייך ל-$\sigma_1$ הגדול, $v_2$ ל-$\sigma_2$, וכן הלאה.</li>
    </ol>
    <div class="lesson-ex"><b>דוגמה.</b> $A^TA=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ עם $\lambda_1=3$, $\lambda_2=1$.<br>
    עבור $\lambda_1=3$: $\begin{pmatrix}-1&1\\1&-1\end{pmatrix}x=0$ נותן $x=(1,1)$, ולכן $v_1=\frac{1}{\sqrt2}(1,1)$.<br>
    עבור $\lambda_2=1$: $\begin{pmatrix}1&1\\1&1\end{pmatrix}x=0$ נותן $x=(1,-1)$, ולכן $v_2=\frac{1}{\sqrt2}(1,-1)$.
    $$V=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$</div>
    <div class="lesson-rule">🔑 ל-$A^TA$ סימטרית, וקטורים עצמיים של ערכים עצמיים <b>שונים</b> ניצבים זה לזה מעצמם, ולכן אחרי נירמול אפשר לשים אותם ישר כעמודות של $V$.</div>
    <h3>ערך עצמי כפול</h3>
    <p>אם ערך עצמי חוזר פעמיים, שני וקטורים עצמיים שלו אינם בהכרח ניצבים זה לזה. בוחרים בתוך המרחב העצמי בסיס <b>אורתונורמלי</b>: מוצאים וקטור אחד, ואת השני בוחרים בתוך אותו מרחב כך שיהיה ניצב לראשון (למשל בגרהם-שמידט), ומנרמלים.</p>
    <div class="lesson-trap">⚠️ סימן: $-v_i$ גם הוא וקטור עצמי מנורמלי, ולכן הסימן של $v_i$ חופשי. אבל <b>אחרי שבחרתם</b>, את $u_i$ מחשבים ממנו (בשלב הבא), וכך הסימנים תואמים. ועוד: בפירוק מופיעה $V^T$, ולכן $v_i$ הם השורות שלה.</div>` },
  questions: [
    { id: "C04-Q1",
      step: { type: "numeric",
        prompt: String.raw`מהו האורך (הנורמה) של הווקטור $x=(1,2,2)$? זה הגורם שבו מחלקים כדי לנרמל אותו.`,
        answer: 3, tol: 0,
        explain: String.raw`$\|x\|=\sqrt{1^2+2^2+2^2}=\sqrt9=3$, ולכן הווקטור המנורמל הוא $\frac13(1,2,2)$.` },
      recap: String.raw`מנרמלים בחלוקה ב-$\|x\|$.` },
    { id: "C04-Q2",
      question: String.raw`$A^TA=\begin{pmatrix}5&4\\4&5\end{pmatrix}$ עם הערך העצמי $\lambda_1=9$. מהו $v_1$ ?`,
      options: [
        { id: "a", value: String.raw`$\frac{1}{\sqrt2}(1,-1)$` },
        { id: "b", value: String.raw`$(1,1)$` },
        { id: "c", value: String.raw`$\frac{1}{\sqrt2}(1,1)$` },
        { id: "d", value: String.raw`$\frac{1}{\sqrt{41}}(4,5)$` },
      ],
      correctId: "c",
      explanation: String.raw`$A^TA-9I=\begin{pmatrix}-4&4\\4&-4\end{pmatrix}$, והפתרון הוא $x=(1,1)$, שאורכו $\sqrt2$, ולכן $v_1=\frac1{\sqrt2}(1,1)$. הווקטור $(1,-1)$ הוא וקטור עצמי של $\lambda=1$ ולא של $9$. הווקטור $(1,1)$ הוא וקטור עצמי נכון אבל לא מנורמל. הווקטור $(4,5)$ הוא השורה השנייה של המטריצה ולא וקטור עצמי.`,
      recap: "פותרים (M - λI)x = 0 ומנרמלים." },
    { id: "C04-Q3",
      question: String.raw`ל-$A^TA=\begin{pmatrix}5&4\\4&5\end{pmatrix}$ הערכים העצמיים $\lambda_1=9$ ו-$\lambda_2=1$. איזו מהמטריצות הבאות היא $V$ תקינה בפירוק SVD (עמודות מנורמלות ובסדר המתאים לערכים הסינגולריים)?`,
      options: [
        { id: "a", value: String.raw`$\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$` },
        { id: "b", value: String.raw`$\frac1{\sqrt2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}1&1\\1&-1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$` },
      ],
      correctId: "d",
      explanation: String.raw`העמודות של התשובה הנכונה הן $v_1=\frac1{\sqrt2}(1,1)$ עבור $9$ ו-$v_2=\frac1{\sqrt2}(1,-1)$ עבור $1$, בסדר יורד של הערכים. במטריצה שעמודותיה $\frac1{\sqrt2}(1,-1)$ ואחריה $\frac1{\sqrt2}(1,1)$ הסדר הפוך. במטריצה עם שתי עמודות זהות העמודות אינן ניצבות. במטריצה בלי הגורם $\frac1{\sqrt2}$ העמודות אינן מנורמלות.`,
      recap: "עמודות V מנורמלות, ניצבות, ובסדר הערכים הסינגולריים." },
    { id: "C04-Q4",
      step: { type: "findbug",
        prompt: String.raw`בחישוב $v_2$ עבור $A^TA=\begin{pmatrix}5&4\\4&5\end{pmatrix}$ ו-$\lambda_2=1$ שורה אחת שגויה. איזו?`,
        lines: [
          String.raw`$(A^TA-I)x=0$ נותן $\begin{pmatrix}4&4\\4&4\end{pmatrix}x=0$`,
          String.raw`כלומר $x_1+x_2=0$`,
          String.raw`הפתרון: $x=t\,(1,1)$`,
          String.raw`מנרמלים: $v_2=\frac1{\sqrt2}(1,-1)$`,
        ],
        bugIndex: 2,
        explain: String.raw`מהמשוואה $x_1+x_2=0$ נובע $x_2=-x_1$, כלומר $x=t(1,-1)$ ולא $t(1,1)$. הווקטור $(1,1)$ הוא וקטור עצמי של $\lambda=9$.` },
      recap: String.raw`בודקים שהווקטור מקיים $(A^TA-\lambda I)x=0$.` },
    { id: "C04-Q5",
      question: String.raw`$A^TA=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}$ עם הערכים העצמיים $4,1,1$, והווקטור $v_1=\frac1{\sqrt3}(1,1,1)$. הערך $1$ כפול, והמרחב העצמי שלו הוא $x_1+x_2+x_3=0$. איזה זוג יכול לשמש כ-$v_2,v_3$ ?`,
      options: [
        { id: "a", value: String.raw`$\frac1{\sqrt2}(1,-1,0)$ ו-$\frac1{\sqrt2}(1,0,-1)$` },
        { id: "b", value: String.raw`$\frac1{\sqrt2}(1,-1,0)$ ו-$\frac1{\sqrt3}(1,1,1)$` },
        { id: "c", value: String.raw`$\frac1{\sqrt2}(1,-1,0)$ ו-$\frac1{\sqrt6}(1,1,-2)$` },
        { id: "d", value: String.raw`$(1,-1,0)$ ו-$(1,1,-2)$` },
      ],
      correctId: "c",
      explanation: String.raw`שני הווקטורים $\frac1{\sqrt2}(1,-1,0)$ ו-$\frac1{\sqrt6}(1,1,-2)$ שייכים למרחב העצמי, מנורמלים, וניצבים זה לזה (מכפלתם הפנימית $1-1+0=0$). בזוג $(1,-1,0)$ ו-$(1,0,-1)$ שני הווקטורים עצמיים ומנורמלים אבל מכפלתם הפנימית היא $\frac12\ne0$, אז העמודות אינן ניצבות. בזוג עם $\frac1{\sqrt3}(1,1,1)$ הווקטור השני הוא וקטור עצמי של $4$ ולא של $1$. בזוג האחרון הווקטורים אינם מנורמלים.`,
      recap: "בערך עצמי כפול בוחרים בסיס אורתונורמלי של המרחב העצמי." },
  ],
});
