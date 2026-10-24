/* proj_gs, level 8 - least squares through projection onto Col(A); orthogonal columns need no inverse */
COURSE_LEVEL("proj_gs", {
  id: "C08", order: 8, icon: "🎯", title: "ריבועים פחותים דרך היטל",
  goal: "להבין ש-$A\\hat x$ הוא ההיטל של $\\vec b$ על $\\operatorname{Col}(A)$, לחשב $\\hat x$ בלי הפיכת מטריצה כשהעמודות ניצבות, ולחשב את השגיאה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>במערכת $A\vec x=\vec b$ ללא פתרון, $\vec b$ אינו ב-$\operatorname{Col}(A)$. הוקטור הקרוב ביותר אליו בתוך $\operatorname{Col}(A)$ הוא ההיטל
$$p=\operatorname{Proj}_{\operatorname{Col}(A)}(\vec b)=A\hat x.$$
זו מערכת עם פתרון, כי $p$ בתוך $\operatorname{Col}(A)$. הפתרון $\hat x$ זהה לפתרון משוואות הנורמל. <b>השגיאה</b> של הריבועים הפחותים היא $\|\vec b-A\hat x\|^2=\|\vec b-p\|^2$.</p>
<div class="lesson-rule">🔑 אם עמודות $A$ הן $a_1,\dots,a_k$ ו<b>ניצבות</b> זו לזו, אין צורך להפוך מטריצה: $\hat x_i=\frac{\langle\vec b,a_i\rangle}{\|a_i\|^2}$. כל מקדם הוא מקדם ההיטל על העמודה שלו.</div>
<div class="lesson-ex">דוגמה: $a_1=(1,1,0)$, ‏$a_2=(1,-1,2)$ (ניצבים) ו-$\vec b=(2,0,5)$. אז $\hat x_1=\frac{2}{2}=1$ ו-$\hat x_2=\frac{12}{6}=2$, ‏$p=a_1+2a_2=(3,-1,4)$, והשארית $\vec b-p=(-1,1,1)$ ניצבת לשתי העמודות. השגיאה היא $3$.</div>
<p>כשהעמודות <b>אינן</b> ניצבות, פותרים את משוואות הנורמל $A^TA\hat x=A^T\vec b$ (או עושים קודם גרהם-שמידט על העמודות, ראו את הרמה על QR).</p>
<div class="lesson-trap">⚠️ הקיצור $\hat x_i=\frac{\langle\vec b,a_i\rangle}{\|a_i\|^2}$ נכון רק לעמודות ניצבות. על עמודות שאינן ניצבות הוא נותן תשובה שגויה.</div>
` },
  questions: [
    { id: "C08-Q1",
      step: { type: "numeric",
        prompt: String.raw`העמודות של $A$ הן $a_1=(1,1,0)$ ו-$a_2=(1,-1,2)$ (ניצבות) ו-$\vec b=(4,0,1)$. חשבו את $\hat x_2$, המקדם של $a_2$ בפתרון הריבועים הפחותים.`,
        answer: 1, tol: 0,
        explain: String.raw`העמודות ניצבות, ולכן $\hat x_2=\frac{\langle\vec b,a_2\rangle}{\|a_2\|^2}=\frac{4+0+2}{6}=1$. (וגם $\hat x_1=\frac42=2$.)` },
      recap: "עמודות ניצבות: כל מקדם הוא מנה אחת." },
    { id: "C08-Q2",
      step: { type: "numeric",
        prompt: String.raw`באותה מערכת, $a_1=(1,1,0)$, ‏$a_2=(1,-1,2)$ ו-$\vec b=(4,0,1)$, חשבו את השגיאה $\|\vec b-A\hat x\|^2$.`,
        answer: 3, tol: 0,
        explain: String.raw`$\hat x=(2,1)$ ולכן $A\hat x=2a_1+a_2=(3,1,2)$. השארית היא $\vec b-A\hat x=(1,-1,-1)$ ונורמתה בריבוע $3$.` },
      recap: String.raw`שגיאה $=\|\vec b-A\hat x\|^2$.` },
    { id: "C08-Q3",
      question: String.raw`העמודות של $A$ הן $(1,0,1)$ ו-$(0,1,1)$ (אינן ניצבות) ו-$\vec b=(1,1,0)$. מהו $\hat x$ ?`,
      options: [
        { id: "a", value: String.raw`$\left(\frac13,\frac13\right)$` },
        { id: "b", value: String.raw`$\left(\frac12,\frac12\right)$` },
        { id: "c", value: String.raw`$(1,1)$` },
        { id: "d", value: String.raw`$\left(\frac23,\frac23\right)$` }],
      correctId: "a",
      explanation: String.raw`$A^TA=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ ו-$A^T\vec b=\binom11$, והפתרון הוא $\hat x=\left(\frac13,\frac13\right)$. הזוג $\left(\frac12,\frac12\right)$ מתקבל מהקיצור לעמודות ניצבות ($\frac{1}{2}$ בכל עמודה), שאסור כאן. הזוג $(1,1)$ הוא $A^T\vec b$ בלי לפתור את המערכת. והזוג $\left(\frac23,\frac23\right)$ אינו פותר את משוואות הנורמל.`,
      recap: "עמודות לא ניצבות: משוואות הנורמל." },
    { id: "C08-Q4",
      step: { type: "choice",
        prompt: String.raw`באותה מערכת, עם העמודות $(1,0,1)$, ‏$(0,1,1)$ והוקטור $\vec b=(1,1,0)$, מהו הוקטור $A\hat x$ ?`,
        options: [
          { id: "a", value: String.raw`ההיטל של $\vec b$ על $\operatorname{Col}(A)$` },
          { id: "b", value: String.raw`ההיטל של $\vec b$ על $\operatorname{Null}(A)$` },
          { id: "c", value: String.raw`הוקטור $\vec b$ עצמו` },
          { id: "d", value: String.raw`השארית $\vec b-A\hat x$` }],
        correctId: "a",
        explain: String.raw`$A\hat x=\left(\frac13,\frac13,\frac23\right)$ והוא ההיטל של $\vec b$ על $\operatorname{Col}(A)$. הוא שונה מ-$\vec b$ כי המערכת אינה פתירה. הוא שונה מהשארית $\left(\frac23,\frac23,-\frac23\right)$. והמרחב $\operatorname{Null}(A)$ כאן הוא $\{0\}$, וההיטל עליו הוא $0$.` },
      recap: String.raw`$A\hat x=\operatorname{Proj}_{\operatorname{Col}(A)}(\vec b)$` },
    { id: "C08-Q5",
      step: { type: "numeric",
        prompt: String.raw`באותה מערכת (עמודות $(1,0,1)$, ‏$(0,1,1)$ ו-$\vec b=(1,1,0)$, עם $\hat x=\left(\frac13,\frac13\right)$) חשבו את השגיאה $\|\vec b-A\hat x\|^2$. (תשובה עשרונית)`,
        answer: 1.333, tol: 0.01,
        explain: String.raw`השארית היא $\left(\frac23,\frac23,-\frac23\right)$ ו-$\|\cdot\|^2=3\cdot\frac49=\frac43\approx1.33$.` },
      recap: "השגיאה היא אורך השארית בריבוע." },
    { bankId: "23A-B-Q1a", recap: "מערכת כללית: משוואות הנורמל $A^TA\\hat x=A^T\\vec b$." },
  ],
});
