/* proj_gs, level 1 - inner product and norm: R^n, matrices (trace form), the axioms, norm of a sum */
COURSE_LEVEL("proj_gs", {
  id: "C01", order: 1, icon: "📏", title: "מכפלה פנימית ונורמה",
  goal: "לחשב מכפלה פנימית ונורמה ב-$\\mathbb{R}^n$ ובמרחב המטריצות, לזהות וקטורים ניצבים, ולהבחין בין נוסחה שהיא מכפלה פנימית לנוסחה שאינה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p><b>מכפלה פנימית</b> היא כלל שמקבל שני וקטורים ומחזיר מספר, $\langle u,v\rangle$. כדי להיות מכפלה פנימית הוא חייב לקיים שלוש תכונות: <b>סימטריה</b> $\langle u,v\rangle=\langle v,u\rangle$, <b>לינאריות</b> $\langle \alpha u+\beta w,v\rangle=\alpha\langle u,v\rangle+\beta\langle w,v\rangle$, ו<b>חיוביות</b> $\langle u,u\rangle\ge 0$ עם שוויון רק עבור $u=0$.</p>
<p>הנורמה (האורך) נגזרת מהמכפלה: $\|u\|=\sqrt{\langle u,u\rangle}$. שני וקטורים <b>ניצבים</b> אם $\langle u,v\rangle=0$.</p>
<table>
<thead><tr><th>המרחב</th><th>המכפלה הפנימית</th></tr></thead>
<tbody>
<tr><td>$\mathbb{R}^n$</td><td>$\langle u,v\rangle=\sum u_kv_k$</td></tr>
<tr><td>$M_n(\mathbb{R})$</td><td>$\langle A,B\rangle=\operatorname{tr}(B^TA)=\sum_{i,j}a_{ij}b_{ij}$</td></tr>
</tbody></table>
<div class="lesson-rule">🔑 במרחב המטריצות המכפלה היא <b>סכום מכפלות של רכיבים מתאימים</b>. לכן $\|A\|^2$ הוא סכום ריבועי כל הרכיבים.</div>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}1&0\\2&3\end{pmatrix}$ ו-$B=\begin{pmatrix}4&1\\1&0\end{pmatrix}$. אז $\langle A,B\rangle=1\cdot4+0\cdot1+2\cdot1+3\cdot0=6$ וגם $\|A\|^2=1+0+4+9=14$.</div>
<p><b>פתיחת סוגריים.</b> מהסימטריה והלינאריות מקבלים
$$\|u\pm v\|^2=\|u\|^2\pm2\langle u,v\rangle+\|v\|^2.$$
אם מחסרים את שני המקרים מתקבלת נוסחת הקיטוב: $\langle u,v\rangle=\frac14\left(\|u+v\|^2-\|u-v\|^2\right)$.</p>
<div class="lesson-trap">⚠️ לא כל נוסחה עם שני וקטורים היא מכפלה פנימית. בודקים את החיוביות: אם יש וקטור שונה מאפס עם $\langle u,u\rangle\le 0$, הנוסחה נפסלת.</div>
` },
  questions: [
    { id: "C01-Q1",
      step: { type: "numeric",
        prompt: String.raw`ב-$M_2(\mathbb{R})$ עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ נתונות $A=\begin{pmatrix}1&2\\0&3\end{pmatrix}$ ו-$B=\begin{pmatrix}2&1\\1&0\end{pmatrix}$. חשבו $\langle A,B\rangle$.`,
        answer: 4, tol: 0,
        explain: String.raw`סוכמים מכפלות של רכיבים מתאימים: $1\cdot2+2\cdot1+0\cdot1+3\cdot0=4$. זה לא מכפלת המטריצות $AB$ אלא עקבה של $B^TA$, שהיא אותו סכום.` },
      recap: "במרחב המטריצות: סכום מכפלות רכיב-רכיב." },
    { id: "C01-Q2",
      question: String.raw`ב-$M_2(\mathbb{R})$ עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ נתונה $A=\begin{pmatrix}1&-2\\3&0\end{pmatrix}$. מהי $\|A\|$ ?`,
      options: [
        { id: "a", value: String.raw`$\sqrt{14}$` },
        { id: "b", value: String.raw`$14$` },
        { id: "c", value: String.raw`$2$` },
        { id: "d", value: String.raw`$\sqrt{10}$` }],
      correctId: "a",
      explanation: String.raw`$\|A\|^2=1+4+9+0=14$, ולכן $\|A\|=\sqrt{14}$. הערך $14$ הוא הנורמה בריבוע, שוכחים את השורש. הערך $2$ הוא סכום הרכיבים $1-2+3+0$. והערך $\sqrt{10}$ מתקבל כשמדלגים על הרכיב $-2$.`,
      recap: "הנורמה היא שורש סכום ריבועי הרכיבים." },
    { id: "C01-Q3",
      question: String.raw`ב-$M_2(\mathbb{R})$ עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ נתונה $A=\begin{pmatrix}1&2\\3&1\end{pmatrix}$. איזו מטריצה ניצבת ל-$A$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}2&-1\\0&0\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}1&0\\0&1\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}1&1\\1&1\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}0&1\\1&0\end{pmatrix}$` }],
      correctId: "a",
      explanation: String.raw`המכפלה עם $\begin{pmatrix}2&-1\\0&0\end{pmatrix}$ היא $2-2+0+0=0$. מטריצת היחידה נותנת $1+1=2$, מטריצת האחדות נותנת $7$, והמטריצה $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ נותנת $5$. אף אחת מהן אינה אפס.`,
      recap: "ניצבות פירושה מכפלה פנימית אפס, לא שהמטריצות מתאפסות." },
    { id: "C01-Q4",
      step: { type: "choice",
        prompt: String.raw`איזו נוסחה מגדירה מכפלה פנימית על $\mathbb{R}^2$ (עבור $u=(x_1,x_2)$ ו-$v=(y_1,y_2)$) ?`,
        options: [
          { id: "a", value: String.raw`$2x_1y_1+3x_2y_2$` },
          { id: "b", value: String.raw`$x_1y_1-x_2y_2$` },
          { id: "c", value: String.raw`$x_1y_2+x_2y_1$` },
          { id: "d", value: String.raw`$(x_1+x_2)(y_1+y_2)$` }],
        correctId: "a",
        explain: String.raw`הנוסחה $2x_1y_1+3x_2y_2$ סימטרית, לינארית וחיובית: $\langle u,u\rangle=2x_1^2+3x_2^2>0$ לכל $u\ne0$. בשלוש האחרות החיוביות נכשלת: הנוסחה $x_1y_1-x_2y_2$ נותנת $-1$ עבור $u=(0,1)$. הנוסחה $x_1y_2+x_2y_1$ נותנת $-2$ עבור $u=(1,-1)$. והנוסחה $(x_1+x_2)(y_1+y_2)$ נותנת $0$ עבור $u=(1,-1)$ שאינו הוקטור האפס.` },
      recap: "חיוביות: $\\langle u,u\\rangle>0$ לכל $u\\ne0$. מחפשים וקטור שמפיל אותה." },
    { id: "C01-Q5",
      step: { type: "numeric",
        prompt: String.raw`נתון $\|u\|=2$, $\|v\|=3$ ו-$\langle u,v\rangle=-1$. חשבו $\|u+v\|^2$.`,
        answer: 11, tol: 0,
        explain: String.raw`$\|u+v\|^2=\|u\|^2+2\langle u,v\rangle+\|v\|^2=4-2+9=11$.` },
      recap: String.raw`$\|u+v\|^2=\|u\|^2+2\langle u,v\rangle+\|v\|^2$` },
    { bankId: "23A-B-Q3b", recap: "פותחים את $\\|u\\pm v\\|^2$ ומחסרים: נוסחת הקיטוב." },
  ],
});
