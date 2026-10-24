/* SVD course, level 2 - A^T A versus A A^T: which one to use and when */
COURSE_LEVEL("svd", {
  id: "C02", order: 2, icon: "⚖️", title: "AᵀA או AAᵀ: באיזו מהן משתמשים",
  goal: "אחרי השלב הזה אפשר לבחור את המטריצה הקטנה מבין $A^TA$ ו-$AA^T$ ולדעת מה היא נותנת ואיך משלימים ממנה את הצד השני.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>כל הפירוק נבנה מאחת משתי מטריצות סימטריות שנגזרות מ-$A$:</p>
    <ul>
      <li>$A^TA$ היא מסדר $n\times n$ (מספר העמודות של $A$). הווקטורים העצמיים המנורמלים שלה הם עמודות $V$.</li>
      <li>$AA^T$ היא מסדר $m\times m$ (מספר השורות של $A$). הווקטורים העצמיים המנורמלים שלה הם עמודות $U$.</li>
    </ul>
    <p>לשתיהן <b>אותם ערכים עצמיים שונים מאפס</b>. המטריצה הגדולה יותר פשוט מוסיפה אפסים. הערכים הסינגולריים הם $\sigma_i=\sqrt{\lambda_i}$.</p>
    <div class="lesson-ex"><b>דוגמה.</b> $A=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}$ היא $2\times3$. אז
    $$AA^T=\begin{pmatrix}5&4\\4&5\end{pmatrix},\qquad A^TA=\begin{pmatrix}5&0&4\\0&0&0\\4&0&5\end{pmatrix}.$$
    ל-$AA^T$ הערכים העצמיים $9$ ו-$1$. ל-$A^TA$ הערכים העצמיים $9,1,0$: אותם שניים ועוד אפס.</div>
    <div class="lesson-rule">🔑 <b>כלל הבחירה:</b> מפרקים את <b>הקטנה</b> מבין $A^TA$ ו-$AA^T$ (אם $n\le m$ אז $A^TA$, אם $m<n$ אז $AA^T$). כך מחשבים פולינום אופייני מסדר קטן.</div>
    <h3>איך משלימים את הצד השני</h3>
    <ul>
      <li>אם פירקתם את $A^TA$ וקיבלתם את $v_i$: לכל $\sigma_i\ne0$ מחשבים $u_i=\dfrac{1}{\sigma_i}Av_i$.</li>
      <li>אם פירקתם את $AA^T$ וקיבלתם את $u_i$: לכל $\sigma_i\ne0$ מחשבים $v_i=\dfrac{1}{\sigma_i}A^Tu_i$.</li>
    </ul>
    <p>את הצד השני <b>לא</b> מוצאים בפירוק נפרד, כדי שהסימנים יתאימו (בשלב על $U$ נראה למה).</p>
    <p><b>בדיקה מהירה לערכים העצמיים:</b> סכום הערכים העצמיים של מטריצה ריבועית שווה לעקבה שלה (סכום איברי האלכסון). ב-$A^TA$ ו-$AA^T$ העקבה היא סכום ריבועי כל הכניסות של $A$, ולכן $\sigma_1^2+\sigma_2^2+\dots$ שווה לסכום ריבועי הכניסות של $A$.</p>
    <div class="lesson-trap">⚠️ מטריצה $3\times3$ כמו $AA^T$ של מטריצה $3\times2$ היא עם שלושה ערכים עצמיים. מי שפירק את $A^TA$ מסדר $2\times2$ רואה רק שניים, והשלישי הוא אפס.</div>` },
  questions: [
    { id: "C02-Q1",
      question: String.raw`$A$ היא מטריצה מסדר $2\times6$. מהי המטריצה הקטנה מבין $A^TA$ ו-$AA^T$, ומה גודלה?`,
      options: [
        { id: "a", value: String.raw`$A^TA$ מסדר $2\times2$` },
        { id: "b", value: String.raw`$AA^T$ מסדר $6\times6$` },
        { id: "c", value: String.raw`$AA^T$ מסדר $2\times2$` },
        { id: "d", value: String.raw`$A^TA$ מסדר $6\times6$` },
      ],
      correctId: "c",
      explanation: String.raw`$AA^T$ היא $m\times m$, כלומר כאן $2\times2$, וזו הקטנה. $A^TA$ היא $n\times n=6\times6$ והיא הגדולה. התשובות שבהן $A^TA$ היא $2\times2$ או $AA^T$ היא $6\times6$ מחליפות בין $m$ ל-$n$.`,
      recap: String.raw`$AA^T$ היא $m\times m$ ו-$A^TA$ היא $n\times n$. מפרקים את הקטנה.` },
    { id: "C02-Q2",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$. מהו סכום הערכים העצמיים של $AA^T$?`,
        answer: 4, tol: 0,
        explain: String.raw`$AA^T=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, והעקבה היא $2+2=4$. זה גם סכום ריבועי הכניסות של $A$: $1+1+1+1=4$. הערכים העצמיים הם $3$ ו-$1$, וסכומם $4$.` },
      recap: "סכום הערכים העצמיים = העקבה = סכום ריבועי הכניסות של A." },
    { id: "C02-Q3",
      question: String.raw`$A$ היא מטריצה מסדר $3\times2$ ול-$A^TA$ יש הערכים העצמיים $3$ ו-$1$. מהם שלושת הערכים העצמיים של $AA^T$?`,
      options: [
        { id: "a", value: String.raw`$9,\ 1,\ 0$` },
        { id: "b", value: String.raw`$\sqrt3,\ 1,\ 0$` },
        { id: "c", value: String.raw`$3,\ 1,\ 1$` },
        { id: "d", value: String.raw`$3,\ 1,\ 0$` },
      ],
      correctId: "d",
      explanation: String.raw`הערכים העצמיים השונים מאפס של $A^TA$ ושל $AA^T$ זהים, ולכן $3$ ו-$1$ מופיעים גם ב-$AA^T$. מטריצה $3\times3$ היא עם שלושה ערכים עצמיים, והשלישי הוא $0$, כי הדרגה של $AA^T$ היא 2. התשובה עם $9$ מעלה בריבוע את הערכים, והתשובה עם $\sqrt3$ היא הערכים הסינגולריים ולא העצמיים. הערך השלישי $1$ אינו אפס, ואז הדרגה הייתה 3, מה שאי אפשר כי ל-$A$ יש רק שתי עמודות.`,
      recap: String.raw`ל-$A^TA$ ול-$AA^T$ אותם ערכים עצמיים שונים מאפס, והשאר אפסים.` },
    { id: "C02-Q4",
      step: { type: "order",
        prompt: String.raw`$A$ היא מטריצה $2\times4$, כלומר $m<n$. סדרו את שלבי בניית הפירוק בדרך הקצרה.`,
        lines: [
          String.raw`בוחרים את הקטנה מבין $A^TA$ ו-$AA^T$: כאן $AA^T$, כי $m<n$`,
          String.raw`מוצאים ערכים עצמיים ווקטורים עצמיים מנורמלים של $AA^T$: אלה עמודות $U$ והערכים $\sigma_i^2$`,
          String.raw`מחשבים $v_i=\frac{1}{\sigma_i}A^Tu_i$ לכל $\sigma_i\neq0$`,
          String.raw`משלימים את $V$ לבסיס אורתונורמלי של $\mathbb{R}^4$`,
          String.raw`בונים את $S$ מסדר $2\times4$ ובודקים ש-$USV^T=A$`,
        ],
        explain: String.raw`כל שלב מסתמך על קודמו: הבחירה קודמת לפירוק, $U$ ו-$\sigma_i$ נדרשים כדי לחשב את $v_i$, ורק אז יודעים כמה עמודות של $V$ חסרות ואפשר להשלים. $S$ והבדיקה באים אחרונים.` },
      recap: String.raw`מפרקים את הקטנה, מחשבים את הצד השני בנוסחה, משלימים, בונים $S$ ובודקים.` },
    { id: "C02-Q5",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}1&0&2\\2&0&1\end{pmatrix}$. מהו הערך העצמי הגדול ביותר של המטריצה $A^TA$ מסדר $3\times3$?`,
        answer: 9, tol: 0,
        explain: String.raw`קל יותר לחשב את $AA^T=\begin{pmatrix}5&4\\4&5\end{pmatrix}$, שערכיה העצמיים $9$ ו-$1$. הערכים העצמיים השונים מאפס של $A^TA$ זהים להם, ולכן הגדול ביותר הוא $9$.` },
      recap: "מחשבים ערכים עצמיים מהמטריצה הקטנה, והם זהים בצד השני." },
  ],
});
