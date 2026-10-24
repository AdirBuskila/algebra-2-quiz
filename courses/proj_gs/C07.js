/* proj_gs, level 7 - least squares: normal equations A^T A x = A^T b, best-fit line, residual orthogonal to Col(A) */
COURSE_LEVEL("proj_gs", {
  id: "C07", order: 7, icon: "📈", title: "ריבועים פחותים ומשוואות הנורמל",
  goal: "למצוא את הישר הקרוב ביותר לנקודות ופתרון ריבועים פחותים כללי באמצעות $A^TA\\hat x=A^T\\vec b$, ולבדוק אותו דרך ניצבות השארית.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כשהמערכת $A\vec x=\vec b$ אין לה פתרון, מחפשים את $\hat x$ שמקטין את השגיאה $\|A\vec x-\vec b\|^2$. הוא הפתרון של <b>משוואות הנורמל</b>:
$$A^TA\,\hat x=A^T\vec b,\qquad\hat x=(A^TA)^{-1}A^T\vec b.$$
הנוסחה השנייה נכונה כשעמודות $A$ בלתי תלויות, ואז $A^TA$ הפיכה והפתרון יחיד.</p>
<p><b>למה זה נכון.</b> הוקטור $A\hat x$ הוא ההיטל של $\vec b$ על $\operatorname{Col}(A)$, ולכן השארית $\vec b-A\hat x$ ניצבת לכל עמודה של $A$, כלומר $A^T(\vec b-A\hat x)=0$. זו משוואות הנורמל עצמן.</p>
<p><b>ישר $y=mx+n$.</b> לנקודות $(x_i,y_i)$ בונים $A$ עם עמודה של ה-$x_i$ ועמודה של אחדות, והנעלם הוא $\binom mn$. אז
$$A^TA=\begin{pmatrix}\sum x_i^2&\sum x_i\\\sum x_i&k\end{pmatrix},\qquad A^T\vec b=\binom{\sum x_iy_i}{\sum y_i},$$
כש-$k$ מספר הנקודות.</p>
<div class="lesson-ex">דוגמה: $(0,1),(1,2),(2,2),(3,4)$. הסכומים $\sum x=6$, ‏$\sum x^2=14$, ‏$\sum y=9$, ‏$\sum xy=18$, ‏$k=4$. מקבלים $\begin{pmatrix}14&6\\6&4\end{pmatrix}\binom mn=\binom{18}{9}$, ולכן $m=n=0.9$. תחזית ל-$x=4$: ‏$4.5$.</div>
<div class="lesson-rule">🔑 בדיקה: סכום השאריות הוא $0$ וגם $\sum x_i\cdot\text{res}_i=0$ (השארית ניצבת לשתי העמודות).</div>
<div class="lesson-trap">⚠️ סדר העמודות קובע את סדר הנעלמים. העמודה השנייה היא עמודת אחדות, לא ה-$x_i$ שוב. ובשאלה מילולית התחזית היא ערך הישר בנקודה החדשה.</div>
` },
  questions: [
    { id: "C07-Q1",
      question: String.raw`מתאימים ישר $y=mx+n$ לארבע נקודות עם $x=1,2,3,4$. העמודות של $A$ הן ה-$x_i$ ועמודת אחדות, והנעלם הוא $\binom mn$. מהי $A^TA$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}30&10\\10&4\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}30&10\\10&10\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}100&10\\10&4\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}30&10\\10&1\end{pmatrix}$` }],
      correctId: "a",
      explanation: String.raw`$\sum x_i^2=1+4+9+16=30$, ‏$\sum x_i=10$, ו-$k=4$ (סכום של ארבע אחדות). הערך $100$ הוא $(\sum x_i)^2$. בערכים השגויים האחרים סוכמים את האחדות כ-$10$ או כ-$1$ במקום $4$.`,
      recap: String.raw`$A^TA=\begin{pmatrix}\sum x^2&\sum x\\\sum x&k\end{pmatrix}$` },
    { id: "C07-Q2",
      step: { type: "numeric",
        prompt: String.raw`הנקודות הן $(1,2),(2,3),(3,5),(4,6)$ והישר הוא $y=mx+n$. חשבו את $m$ מתוך משוואות הנורמל.`,
        answer: 1.4, tol: 0.001,
        explain: String.raw`$\sum x=10$, ‏$\sum x^2=30$, ‏$\sum y=16$, ‏$\sum xy=2+6+15+24=47$, ‏$k=4$. המערכת $\begin{pmatrix}30&10\\10&4\end{pmatrix}\binom mn=\binom{47}{16}$ עם $\det=20$ נותנת $m=\frac{4\cdot47-10\cdot16}{20}=1.4$ וגם $n=\frac{30\cdot16-10\cdot47}{20}=0.5$.` },
      recap: "משוואות הנורמל הן מערכת $2\\times2$ בנעלמים $m,n$." },
    { id: "C07-Q3",
      step: { type: "numeric",
        prompt: String.raw`עבור אותן נקודות, $(1,2),(2,3),(3,5),(4,6)$, הישר הקרוב ביותר הוא $y=1.4x+0.5$. מהי התחזית עבור $x=5$ ?`,
        answer: 7.5, tol: 0.001,
        explain: String.raw`מציבים בישר: $1.4\cdot5+0.5=7.5$.` },
      recap: "תחזית: מציבים את הנקודה החדשה בישר." },
    { id: "C07-Q4",
      step: { type: "choice",
        prompt: String.raw`עבור הישר $y=1.4x+0.5$ ו-$x=1,2,3,4$ השאריות $y_i-\hat y_i$ הן $0.1,\ -0.3,\ 0.3,\ -0.1$. איזו טענה על השארית נכונה בפתרון ריבועים פחותים ?`,
        options: [
          { id: "a", value: String.raw`היא ניצבת לשתי עמודות $A$: סכום השאריות $0$ וגם $\sum x_ir_i=0$` },
          { id: "b", value: String.raw`היא ניצבת לוקטור $\vec b$ של ערכי $y$` },
          { id: "c", value: String.raw`כל השאריות שוות זו לזו` },
          { id: "d", value: String.raw`סכום ריבועי השאריות הוא $0$` }],
        correctId: "a",
        explain: String.raw`זו משוואות הנורמל $A^T(\vec b-A\hat x)=0$. בדוגמה: $0.1-0.3+0.3-0.1=0$ ו-$0.1-0.6+0.9-0.4=0$. הטענה על ניצבות ל-$\vec b$ שגויה: $\langle r,\vec b\rangle=0.2-0.9+1.5-0.6=0.2\ne0$. השאריות אינן שוות זו לזו. וסכום הריבועים הוא $0.2$, הוא היה $0$ רק אילו כל הנקודות על הישר.` },
      recap: "השארית ניצבת לעמודות $A$, לא ל-$\\vec b$." },
    { bankId: "24A-B-Q1a", recap: "בונים טבלת סכומים, פותרים מערכת $2\\times2$, ובודקים את השאריות." },
    { bankId: "24B-B-Q3b", recap: "אותו מתכון עם נקודה בראשית: $\\sum x_i=15$, ‏$\\sum x_i^2=65$." },
  ],
});
