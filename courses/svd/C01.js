/* SVD course, level 1 - what the decomposition is and what the matrices look like */
COURSE_LEVEL("svd", {
  id: "C01", order: 1, icon: "🧬", title: "מהו פירוק SVD ואיך נראות המטריצות",
  goal: "אחרי השלב הזה אפשר לכתוב את הפירוק $A=USV^T$, לקבוע את גדולי $U,S,V$ ולקרוא את הדרגה מתוך $S$.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>לכל מטריצה ממשית $A$ מסדר $m\times n$ (גם לא ריבועית, גם לא הפיכה) קיים <b>פירוק לערכים סינגולריים</b>, בקיצור <b>SVD</b>:</p>
    <div class="lesson-formula">$$A=USV^T$$</div>
    <p>הסימון בדף הנוסחאות של הקורס הוא $S$ למטריצה האלכסונית. בספרים רבים כותבים במקומה $\Sigma$, וזה אותו דבר.</p>
    <ul>
      <li>$U$ היא מטריצה <b>אורתוגונלית</b> מסדר $m\times m$. כלומר העמודות שלה $u_1,\dots,u_m$ הן וקטורים באורך 1 שניצבים זה לזה, ומתקיים $U^TU=I$.</li>
      <li>$V$ היא אורתוגונלית מסדר $n\times n$, עם העמודות $v_1,\dots,v_n$. בפירוק מופיעה $V^T$, כלומר העמודות $v_i$ כתובות שם כשורות.</li>
      <li>$S$ היא מטריצה מסדר $m\times n$ (אותו גודל כמו $A$). כל הכניסות שלה אפסים חוץ מהאלכסון הראשי, ושם עומדים <b>הערכים הסינגולריים</b> $\sigma_1\ge\sigma_2\ge\dots\ge0$: אי-שליליים ומסודרים מהגדול לקטן.</li>
    </ul>
    <div class="lesson-ex"><b>דוגמה לגדלים.</b> אם $A$ היא $3\times2$ אז $U$ היא $3\times3$, $S$ היא $3\times2$ ו-$V$ היא $2\times2$. ב-$S$ יש שני ערכים סינגולריים על האלכסון, ושורה אחרונה של אפסים:
    $$S=\begin{pmatrix}\sigma_1&0\\0&\sigma_2\\0&0\end{pmatrix}$$
    שורת אפסים כזו היא תקינה לגמרי ולא טעות.</div>
    <div class="lesson-rule">🔑 <b>הדרגה</b> של $A$ היא מספר הערכים הסינגולריים השונים מאפס. אם על אלכסון $S$ יש $4,2,0$ אז הדרגה היא 2.</div>
    <div class="lesson-trap">⚠️ בפירוק כותבים $V^T$ ולא $V$, והסדר הוא $U$ ואז $S$ ואז $V^T$. הערכים הסינגולריים לא שליליים, ובסדר יורד.</div>
    <p>בשלבים הבאים נלמד לבנות כל אחת מהמטריצות האלה: קודם הערכים הסינגולריים, אחר כך $V$, אחר כך $U$.</p>` },
  questions: [
    { id: "C01-Q1",
      question: String.raw`$A$ היא מטריצה מסדר $4\times3$ ו-$A=USV^T$ הוא פירוק SVD שלה. מהם הגדלים של $U$, של $S$ ושל $V$?`,
      options: [
        { id: "a", value: String.raw`$U$ מסדר $4\times4$, $S$ מסדר $4\times3$, $V$ מסדר $3\times3$` },
        { id: "b", value: String.raw`$U$ מסדר $3\times3$, $S$ מסדר $4\times3$, $V$ מסדר $4\times4$` },
        { id: "c", value: String.raw`$U$ מסדר $4\times4$, $S$ מסדר $3\times3$, $V$ מסדר $3\times3$` },
        { id: "d", value: String.raw`$U$ מסדר $4\times3$, $S$ מסדר $3\times3$, $V$ מסדר $3\times3$` },
      ],
      correctId: "a",
      explanation: String.raw`$U$ אורתוגונלית ושייכת לצד השורות, לכן $4\times4$. $V$ שייכת לצד העמודות, לכן $3\times3$. $S$ היא בגודל של $A$ עצמה, $4\times3$. התשובה שבה $U$ ו-$V$ מוחלפות סותרת את כפל המטריצות. התשובה עם $S$ מסדר $3\times3$ מתעלמת מהשורה הנוספת של אפסים, ובלעדיה המכפלה $USV^T$ בכלל לא הייתה בגודל $4\times3$. $U$ מסדר $4\times3$ אינה ריבועית, ולכן אינה אורתוגונלית.`,
      recap: String.raw`$A$ מסדר $m\times n$: $U$ היא $m\times m$, $S$ היא $m\times n$, $V$ היא $n\times n$.` },
    { id: "C01-Q2",
      step: { type: "numeric",
        prompt: String.raw`$A$ היא מטריצה מסדר $2\times5$. כמה עמודות יש ב-$V$ בפירוק $A=USV^T$?`,
        answer: 5, tol: 0,
        explain: String.raw`$V$ אורתוגונלית מסדר $n\times n$ כש-$n$ הוא מספר העמודות של $A$. כאן $n=5$, ולכן $V$ היא $5\times5$ ויש בה 5 עמודות.` },
      recap: String.raw`$V$ היא $n\times n$ כש-$n$ מספר העמודות של $A$.` },
    { id: "C01-Q3",
      step: { type: "numeric",
        prompt: String.raw`בפירוק SVD של מטריצה $A$ המטריצה $S$ היא $S=\begin{pmatrix}4&0&0\\0&2&0\\0&0&0\end{pmatrix}$. מהי הדרגה של $A$?`,
        answer: 2, tol: 0,
        explain: String.raw`הדרגה היא מספר הערכים הסינגולריים השונים מאפס. על האלכסון עומדים $4,2,0$, ושניים מהם שונים מאפס, לכן הדרגה היא 2.` },
      recap: "הדרגה = מספר הערכים הסינגולריים השונים מאפס." },
    { id: "C01-Q4",
      question: "איזה מהביטויים הבאים הוא הצורה הנכונה של פירוק SVD של $A$?",
      options: [
        { id: "a", value: String.raw`$A=U^TSV$` },
        { id: "b", value: String.raw`$A=USV^T$` },
        { id: "c", value: String.raw`$A=VSU^T$` },
        { id: "d", value: String.raw`$A=USV$` },
      ],
      correctId: "b",
      explanation: String.raw`הצורה הנכונה היא $A=USV^T$: $U$ משמאל, $V$ מועברת (transpose) מימין. בתשובה $VSU^T$ הגדלים אינם מתאימים כשהמטריצה לא ריבועית: ב-$3\times2$ למשל אי אפשר לכפול $V$ מסדר $2\times2$ ב-$S$ מסדר $3\times2$. בתשובות $U^TSV$ ו-$USV$ הגדלים אולי מסתדרים, אבל המכפלה אינה שווה ל-$A$ בדרך כלל.`,
      recap: String.raw`הפירוק הוא $A=USV^T$, עם $V^T$ ולא $V$.` },
    { id: "C01-Q5",
      question: String.raw`איזו מהמטריצות הבאות יכולה להיות המטריצה $S$ בפירוק SVD של מטריצה $A$ מסדר $2\times3$?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&0&0\\0&\sqrt5&0\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}\sqrt5&0\\0&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}\sqrt5&0&0\\0&1&0\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}\sqrt5&0&0\\0&-1&0\end{pmatrix}$` },
      ],
      correctId: "c",
      explanation: String.raw`$S$ חייבת להיות $2\times3$, אלכסונית, עם ערכים אי-שליליים בסדר יורד, וזה מתקיים רק במטריצה $\mathrm{diag}(\sqrt5,1)$ עם עמודת אפסים. המטריצה שבה $1$ מופיע לפני $\sqrt5$ מפרה את הסדר היורד. המטריצה $2\times2$ היא בגודל לא נכון. המטריצה עם $-1$ מפרה את אי-השליליות של ערך סינגולרי.`,
      recap: String.raw`$S$ בגודל של $A$, ערכים אי-שליליים בסדר יורד על האלכסון.` },
  ],
});
