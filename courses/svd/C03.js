/* SVD course, level 3 - singular values and the matrix S */
COURSE_LEVEL("svd", {
  id: "C03", order: 3, icon: "📏", title: "ערכים סינגולריים והמטריצה S",
  goal: "אחרי השלב הזה אפשר לחשב את הערכים הסינגולריים של מטריצה ולבנות ממנה את $S$ בגודל הנכון.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>הערכים הסינגולריים נגזרים מהערכים העצמיים של המטריצה הקטנה מבין $A^TA$ ו-$AA^T$ (שנלמדו בשלב הקודם):</p>
    <div class="lesson-formula">$$\sigma_i=\sqrt{\lambda_i}$$</div>
    <p>הערכים העצמיים של מטריצה מהצורה $A^TA$ הם תמיד אי-שליליים, ולכן אפשר להוציא שורש.</p>
    <h3>המתכון</h3>
    <ol>
      <li>מחשבים את $A^TA$ (או את $AA^T$ אם היא קטנה יותר).</li>
      <li>מוצאים את הערכים העצמיים $\lambda_i$ מתוך הפולינום האופייני $\det(M-\lambda I)=0$.</li>
      <li>מסדרים אותם בסדר יורד $\lambda_1\ge\lambda_2\ge\dots$ ומוציאים שורש: $\sigma_i=\sqrt{\lambda_i}$.</li>
      <li>בונים את $S$ בגודל $m\times n$: את $\sigma_i$ שמים במקום $(i,i)$ ואפסים בכל שאר הכניסות.</li>
    </ol>
    <div class="lesson-ex"><b>דוגמה.</b> $A=\begin{pmatrix}1&1\\0&1\\1&0\end{pmatrix}$. אז $A^TA=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ ופולינום אופייני $(2-\lambda)^2-1=0$, כלומר $\lambda=3$ או $\lambda=1$. לכן $\sigma_1=\sqrt3$ ו-$\sigma_2=1$, ו-$A$ היא $3\times2$ ולכן
    $$S=\begin{pmatrix}\sqrt3&0\\0&1\\0&0\end{pmatrix}.$$</div>
    <div class="lesson-rule">🔑 אפס כערך עצמי נותן $\sigma=0$, ו<b>מספר הערכים הסינגולריים השונים מאפס הוא הדרגה</b> של $A$.</div>
    <div class="lesson-trap">⚠️ על האלכסון של $S$ עומדים הערכים הסינגולריים $\sigma_i=\sqrt{\lambda_i}$ ולא הערכים העצמיים $\lambda_i$. ושוכחים לפעמים את הסדר היורד.</div>` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&2\\2&1\\0&0\end{pmatrix}$ ו-$A^TA=\begin{pmatrix}5&4\\4&5\end{pmatrix}$. מהו הערך הסינגולרי הגדול ביותר $\sigma_1$?`,
        answer: 3, tol: 0,
        explain: String.raw`$(5-\lambda)^2-16=0$ נותן $5-\lambda=\pm4$, כלומר $\lambda=9$ או $\lambda=1$. הגדול הוא $\sigma_1=\sqrt9=3$.` },
      recap: String.raw`$\sigma_1=\sqrt{\lambda_{\max}}$.` },
    { id: "C03-Q2",
      question: String.raw`עבור אותה מטריצה $A=\begin{pmatrix}1&2\\2&1\\0&0\end{pmatrix}$ שערכיה העצמיים של $A^TA$ הם $9,1$: מהי $S$?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&0\\0&3\\0&0\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}3&0&0\\0&1&0\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}9&0\\0&1\\0&0\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}3&0\\0&1\\0&0\end{pmatrix}$` },
      ],
      correctId: "d",
      explanation: String.raw`$\sigma_1=\sqrt9=3$ ו-$\sigma_2=\sqrt1=1$, ו-$A$ היא $3\times2$, ולכן $S$ היא $3\times2$ עם $3,1$ על האלכסון ושורת אפסים. המטריצה עם $9$ מציבה את הערך העצמי במקום השורש. המטריצה עם $1,3$ מפרה את הסדר היורד. המטריצה מסדר $2\times3$ היא בגודל שגוי.`,
      recap: String.raw`$S$ בגודל $A$, עם $\sqrt{\lambda_i}$ בסדר יורד על האלכסון.` },
    { id: "C03-Q3",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&2\\2&4\end{pmatrix}$ ו-$A^TA=\begin{pmatrix}5&10\\10&20\end{pmatrix}$ שערכיה העצמיים הם $25$ ו-$0$. מהי הדרגה של $A$?`,
        answer: 1, tol: 0,
        explain: String.raw`$\sigma_1=\sqrt{25}=5$ ו-$\sigma_2=0$. רק ערך סינגולרי אחד שונה מאפס, ולכן הדרגה היא 1. אכן העמודה השנייה של $A$ היא פעמיים הראשונה.` },
      recap: "הדרגה = מספר הערכים הסינגולריים השונים מאפס." },
    { id: "C03-Q4",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$, כלומר $2\times3$. חשבו את $\sigma_1$ (ענו בקירוב עד שתי ספרות אחרי הנקודה).`,
        answer: 1.7321, tol: 0.01,
        explain: String.raw`$m<n$, ולכן נוח לפרק את $AA^T=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. הערכים העצמיים הם $3$ ו-$1$, ולכן $\sigma_1=\sqrt3\approx1.73$.` },
      recap: String.raw`למטריצה רחבה מפרקים את $AA^T$ ומקבלים אותם $\sigma$.` },
    { id: "C03-Q5",
      step: { type: "order",
        prompt: "סדרו את שלבי החישוב של הערכים הסינגולריים ושל $S$.",
        lines: [
          String.raw`מחשבים את $A^TA$ (או את $AA^T$ אם היא קטנה יותר)`,
          String.raw`מוצאים את הערכים העצמיים $\lambda_i$ מהפולינום האופייני`,
          String.raw`מסדרים בסדר יורד ומוציאים שורש: $\sigma_i=\sqrt{\lambda_i}$`,
          String.raw`שמים את $\sigma_i$ על האלכסון של $S$ בגודל $m\times n$`,
        ],
        explain: "כל שלב דורש את תוצאת קודמו: אי אפשר למצוא ערכים עצמיים בלי המטריצה, ואי אפשר להוציא שורש בלי הערכים, ואי אפשר לבנות את S בלי הערכים הסינגולריים." },
      recap: String.raw`מטריצה, ערכים עצמיים, שורש בסדר יורד, ואז $S$.` },
    { id: "C03-Q6",
      step: { type: "findbug",
        prompt: String.raw`בפתרון הבא לחישוב הערכים הסינגולריים של $A=\begin{pmatrix}1&2\\2&1\\0&0\end{pmatrix}$ שורה אחת שגויה. איזו?`,
        lines: [
          String.raw`$A^TA=\begin{pmatrix}5&4\\4&5\end{pmatrix}$`,
          String.raw`הפולינום האופייני: $(5-\lambda)^2-16=0$`,
          String.raw`הערכים העצמיים: $\lambda_1=9$ ו-$\lambda_2=1$`,
          String.raw`הערכים הסינגולריים: $\sigma_1=9$ ו-$\sigma_2=1$`,
        ],
        bugIndex: 3,
        explain: String.raw`הערך הסינגולרי הוא השורש של הערך העצמי: $\sigma_1=\sqrt9=3$ ולא $9$. שלוש השורות האחרות נכונות.` },
      recap: String.raw`$\sigma=\sqrt\lambda$, לא $\lambda$ עצמו.` },
  ],
});
