/* orthodiag, level 3 - A = Q D Q^T for 2x2: columns of Q and the diagonal of D in the same order. */
COURSE_LEVEL("orthodiag", {
  id: "C03", order: 3, icon: "🧩", title: "הרכבת Q ו-D ושמירה על הסדר",
  goal: "לבנות $Q$ ו-$D$ מערכים ווקטורים עצמיים כך שסדר העמודות בהתאם לסדר האלכסון, ולחשב $A$ חזרה מהפירוק.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>לכסון אורתוגונלי של $A$ סימטרית:</p>
    <ul>
      <li>העמודות של $Q$ הן וקטורים עצמיים <b>מנורמלים</b>, ניצבים זה לזה (בסיס אורתונורמלי).</li>
      <li>על האלכסון של $D$ הערכים העצמיים, <b>באותו סדר</b>: העמודה ה-$i$ של $Q$ שייכת לערך $d_{ii}$.</li>
      <li>$Q^TQ=I$, ולכן $Q^{-1}=Q^T$, ו-$A=QDQ^T$ וגם $Q^TAQ=D$.</li>
    </ul>
    <div class="lesson-ex">דוגמה: $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ עם ערך עצמי $3$ ווקטור $\frac1{\sqrt2}(1,1)$, וערך עצמי $1$ ווקטור $\frac1{\sqrt2}(1,-1)$. אפשר לבחור
    $$Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad D=\begin{pmatrix}3&0\\0&1\end{pmatrix}.$$
    אם מחליפים את סדר העמודות של $Q$, חייבים להחליף גם את סדר האלכסון של $D$. שני הסדרים נכונים, כל עוד הם תואמים.</div>
    <div class="lesson-trap">⚠️ הנוסחה היא $A=QDQ^T$ כשהעמודות של $Q$ הן הווקטורים העצמיים. החלפת סדר בצד אחד בלבד הורסת את השוויון.</div>
    ` },
  questions: [
    { id: "C03-Q1",
      question: String.raw`$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. העמודה הראשונה של $Q$ היא $\frac1{\sqrt2}(1,1)^T$ (ערך עצמי $3$) והעמודה השנייה היא $\frac1{\sqrt2}(1,-1)^T$ (ערך עצמי $1$). מהי $D$ התואמת?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&0\\0&3\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}3&0\\0&3\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}3&0\\0&1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}3&1\\1&3\end{pmatrix}$` },
      ],
      correctId: "c",
      explanation: String.raw`העמודה הראשונה שייכת לערך $3$ והשנייה לערך $1$, ולכן $D=\operatorname{diag}(3,1)$. האלכסון $\operatorname{diag}(1,3)$ הוא בסדר הפוך ולא מתאים לעמודות האלה. $\operatorname{diag}(3,3)$ מתעלם מהערך $1$. והמטריצה האחרונה אינה אלכסונית.`,
      recap: "עמודה $i$ של $Q$ $\\leftrightarrow$ איבר $i$ באלכסון של $D$." },
    { id: "C03-Q2",
      question: String.raw`לאותה $A$, מחליפים את סדר העמודות: העמודה הראשונה של $Q$ היא $\frac1{\sqrt2}(1,-1)^T$ והשנייה $\frac1{\sqrt2}(1,1)^T$. מהי $D$?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&0\\0&3\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}3&0\\0&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}-1&0\\0&1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}1&0\\0&1\end{pmatrix}$` },
      ],
      correctId: "a",
      explanation: String.raw`הוקטור $(1,-1)$ שייך לערך $1$ והוא בעמודה הראשונה, ולכן $d_{11}=1$ ו-$d_{22}=3$: $D=\operatorname{diag}(1,3)$. האלכסון $\operatorname{diag}(3,1)$ היה נכון לסדר המקורי, לא לסדר החדש. שני האחרים אינם הערכים העצמיים של $A$.`,
      recap: "מחליפים עמודות ב-$Q$ $\\Rightarrow$ מחליפים אותן בסדר גם ב-$D$." },
    { id: "C03-Q3",
      step: { type: "numeric",
        prompt: String.raw`נתון $Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ ו-$D=\begin{pmatrix}5&0\\0&1\end{pmatrix}$. הפירוק $A=QDQ^T$ נותן מטריצה סימטרית. מהו האיבר $a_{12}$ שלה?`,
        answer: 2, tol: 0,
        explain: String.raw`$A=QDQ^T=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}5&0\\0&1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\begin{pmatrix}3&2\\2&3\end{pmatrix}$. לכן $a_{12}=2$.` },
      recap: "$A=QDQ^T$: מחשבים לפי הסדר $QD$ ואז כפל ב-$Q^T$." },
    { id: "C03-Q4",
      question: String.raw`העמודות של $Q$ הן הווקטורים העצמיים המנורמלים של מטריצה סימטרית $A$, ו-$D$ אלכסונית עם הערכים העצמיים בסדר התואם. איזו נוסחה נכונה לכל מטריצה כזו?`,
      options: [
        { id: "a", value: String.raw`$A=Q^TDQ$` },
        { id: "b", value: String.raw`$A=QDQ^T$` },
        { id: "c", value: String.raw`$A=DQQ^T$` },
        { id: "d", value: String.raw`$A=QQ^TD$` },
      ],
      correctId: "b",
      explanation: String.raw`$AQ=QD$ (כל עמודה של $Q$ מוכפלת בערך העצמי שלה), ולכן $A=QDQ^{-1}=QDQ^T$. הנוסחה $Q^TDQ$ נכונה רק כשהשורות של $Q$ הן הווקטורים העצמיים, לא העמודות. בשתי האחרונות $QQ^T=I$, ולכן יוצא $A=D$, וזה נכון רק אם $A$ כבר אלכסונית.`,
      recap: "$AQ=QD$, ולכן $A=QDQ^T$." },
    { id: "C03-Q5",
      step: { type: "findbug",
        prompt: String.raw`מצאו את השורה השגויה בלכסון האורתוגונלי של $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$.`,
        lines: [
          String.raw`העקבה $2$ והדטרמיננטה $-3$, ולכן הערכים העצמיים הם $3$ ו-$-1$.`,
          String.raw`לערך $3$ הווקטור $v_1=\frac1{\sqrt2}(1,1)$, ולערך $-1$ הווקטור $v_2=\frac1{\sqrt2}(1,-1)$.`,
          String.raw`הווקטורים ניצבים כי הערכים העצמיים שונים.`,
          String.raw`נבחר $Q=[\,v_2\ \ v_1\,]$ (העמודה הראשונה $v_2$) ו-$D=\operatorname{diag}(3,-1)$, ואז $A=QDQ^T$.`,
        ],
        bugIndex: 3,
        explain: String.raw`בבחירה $Q=[v_2\ v_1]$ העמודה הראשונה שייכת לערך $-1$, ולכן $D$ חייבת להיות $\operatorname{diag}(-1,3)$. עם $\operatorname{diag}(3,-1)$ מקבלים $QDQ^T=\begin{pmatrix}1&-2\\-2&1\end{pmatrix}\ne A$. שלוש השורות האחרות נכונות.` },
      recap: "סדר העמודות ב-$Q$ וסדר האלכסון ב-$D$ חייבים להתאים." },
    { id: "C03-Q6",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ ו-$q=\frac1{\sqrt2}(1,1)^T$ וקטור עצמי מנורמלי. מהו $q^TAq$?`,
        answer: 3, tol: 0,
        explain: String.raw`$Aq=3q$, ולכן $q^TAq=3\,q^Tq=3$. זה האיבר המתאים על האלכסון של $D=Q^TAQ$.` },
      recap: "$q^TAq=\\lambda$ עבור וקטור עצמי מנורמלי $q$." },
  ],
});
