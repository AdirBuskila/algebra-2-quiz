/* orthodiag, level 1 - symmetric matrices and the spectral theorem. */
COURSE_LEVEL("orthodiag", {
  id: "C01", order: 1, icon: "🪞", title: "מטריצות סימטריות והמשפט הספקטרלי",
  goal: "לזהות מטריצה שאפשר ללכסן אורתוגונלית, ולחשב ערכים עצמיים של מטריצה סימטרית $2\\times2$ מהעקבה והדטרמיננטה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>מטריצה ממשית $A$ היא <b>סימטרית</b> אם $A=A^T$, כלומר $a_{ij}=a_{ji}$ לכל $i,j$. האיברים מעל האלכסון משתקפים בדיוק לאיברים שמתחתיו.</p>
    <div class="lesson-rule">🔑 <b>המשפט הספקטרלי:</b> מטריצה ממשית $A$ ניתנת ללכסון אורתוגונלי אם ורק אם היא סימטרית. אז יש מטריצה אורתוגונלית $Q$ ומטריצה אלכסונית $D$ כך ש-$A=QDQ^T$. בנוסף, כל הערכים העצמיים של מטריצה סימטרית ממשית הם מספרים ממשיים.</div>
    <p><b>ערכים עצמיים של מטריצה $2\times2$:</b> הפולינום האופייני הוא $\lambda^2-(\operatorname{tr}A)\lambda+\det A$. לכן סכום הערכים העצמיים הוא העקבה, והמכפלה שלהם היא הדטרמיננטה.</p>
    <div class="lesson-ex">דוגמה: $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ סימטרית, העקבה $4$ והדטרמיננטה $3$. מחפשים שני מספרים שסכומם $4$ ומכפלתם $3$: הערכים העצמיים הם $1$ ו-$3$.</div>
    <div class="lesson-trap">⚠️ מטריצה לא סימטרית אי אפשר ללכסן אורתוגונלית, גם אם היא ניתנת ללכסון רגיל. בודקים סימטריה לפני כל חישוב אחר.</div>
    ` },
  questions: [
    { id: "C01-Q1",
      question: String.raw`איזו מהמטריצות הבאות ניתנת ללכסון אורתוגונלי?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}2&3\\1&1\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}2&3\\3&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}1&2\\-2&1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}0&1\\0&0\end{pmatrix}$` },
      ],
      correctId: "b",
      explanation: String.raw`לפי המשפט הספקטרלי צריך מטריצה סימטרית. המטריצה $\begin{pmatrix}2&3\\3&1\end{pmatrix}$ סימטרית ($3=3$). במטריצה $\begin{pmatrix}2&3\\1&1\end{pmatrix}$ יוצא $3\ne1$. במטריצה $\begin{pmatrix}1&2\\-2&1\end{pmatrix}$ יוצא $2\ne-2$ (היא אנטי-סימטרית). המטריצה $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ אינה סימטרית, ולמעשה גם לא ניתנת ללכסון כלל.`,
      recap: "לכסון אורתוגונלי אפשרי בדיוק עבור מטריצה סימטרית." },
    { id: "C01-Q2",
      step: { type: "numeric",
        prompt: String.raw`עבור איזה ערך של $t$ המטריצה $\begin{pmatrix}1&t\\5&2\end{pmatrix}$ סימטרית?`,
        answer: 5, tol: 0,
        explain: String.raw`סימטריה דורשת $a_{12}=a_{21}$, כלומר $t=5$.` },
      recap: "סימטריה: $a_{12}=a_{21}$." },
    { id: "C01-Q3",
      step: { type: "numeric",
        prompt: String.raw`מהו הערך העצמי הגדול של $\begin{pmatrix}2&1\\1&2\end{pmatrix}$?`,
        answer: 3, tol: 0,
        explain: String.raw`עקבה $4$ ודטרמיננטה $3$. הפולינום $\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$ נותן $1$ ו-$3$. הגדול הוא $3$.` },
      recap: "$\\lambda^2-(\\operatorname{tr}A)\\lambda+\\det A=0$." },
    { id: "C01-Q4",
      question: String.raw`$A$ מטריצה סימטרית $2\times2$ עם עקבה $7$ ודטרמיננטה $10$. מהם הערכים העצמיים שלה?`,
      options: [
        { id: "a", value: String.raw`$3$ ו-$4$` },
        { id: "b", value: String.raw`$1$ ו-$10$` },
        { id: "c", value: String.raw`$-2$ ו-$-5$` },
        { id: "d", value: String.raw`$2$ ו-$5$` },
      ],
      correctId: "d",
      explanation: String.raw`צריך שני מספרים שסכומם $7$ ומכפלתם $10$: $2$ ו-$5$. הזוג $3,4$ מסכם ל-$7$ אבל מכפלתו $12$. הזוג $1,10$ מכפלתו $10$ אבל סכומו $11$. הזוג $-2,-5$ מכפלתו $10$ אבל סכומו $-7$.`,
      recap: "סכום הערכים העצמיים הוא העקבה, והמכפלה היא הדטרמיננטה." },
    { id: "C01-Q5",
      question: String.raw`איזה תנאי על מטריצה ממשית $A$ שקול לכך שהיא ניתנת ללכסון אורתוגונלי?`,
      options: [
        { id: "a", value: String.raw`$A$ הפיכה` },
        { id: "b", value: String.raw`$A=A^T$` },
        { id: "c", value: String.raw`כל הערכים העצמיים של $A$ שונים זה מזה` },
        { id: "d", value: String.raw`$A$ אורתוגונלית` },
      ],
      correctId: "b",
      explanation: String.raw`המשפט הספקטרלי: לכסון אורתוגונלי אפשרי אם ורק אם $A=A^T$. הפיכות לא מספיקה (למשל $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ הפיכה אבל אינה סימטרית) ולא נדרשת (מטריצת האפס מלכסנת אורתוגונלית). ערכים עצמיים שונים לא נדרשים: $I$ סימטרית עם ערך עצמי חוזר, ומטריצה לא סימטרית יכולה להיות עם ערכים שונים. מטריצת סיבוב אורתוגונלית אינה סימטרית בדרך כלל.`,
      recap: "לכסון אורתוגונלי $\\iff$ $A=A^T$." },
    { id: "C01-Q6",
      step: { type: "numeric",
        prompt: String.raw`המטריצה $A=\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$ סימטרית. מהי העקבה שלה, כלומר סכום כל הערכים העצמיים (עם ריבוי)?`,
        answer: 9, tol: 0,
        explain: String.raw`העקבה היא סכום איברי האלכסון: $3+3+3=9$, והיא שווה לסכום הערכים העצמיים.` },
      recap: "העקבה = סכום איברי האלכסון = סכום הערכים העצמיים." },
  ],
});
