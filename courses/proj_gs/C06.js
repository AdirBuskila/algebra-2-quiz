/* proj_gs, level 6 - projection onto Sp{...} when the spanning set is not orthogonal: matrices and functions */
COURSE_LEVEL("proj_gs", {
  id: "C06", order: 6, icon: "🧩", title: "היטל על פרישה: מטריצות ופונקציות",
  goal: "לחשב היטל על $\\operatorname{Sp}\\{\\dots\\}$ במרחב מטריצות ובמרחב פונקציות: לבדוק ניצבות, לבצע גרהם-שמידט אם צריך, ולהציב בנוסחה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>זו שאלת המבחן הקבועה: "חשבו את ההיטל של $V$ על $\operatorname{Sp}\{W_1,\dots,W_k\}$". מתכון בארבעה צעדים:</p>
<ol>
<li><b>בדקו ניצבות</b> בין הוקטורים הפורשים. אם הם ניצבים, עברו לצעד 3.</li>
<li>אם לא: בצעו <b>גרהם-שמידט</b> וקבלו בסיס אורתוגונלי $u_1,\dots,u_k$ של אותה פרישה.</li>
<li>חשבו $\operatorname{Proj}=\sum\frac{\langle V,u_i\rangle}{\|u_i\|^2}u_i$.</li>
<li><b>בדיקה:</b> $\langle V-\operatorname{Proj},u_i\rangle=0$ לכל $i$.</li>
</ol>
<div class="lesson-ex">מטריצות, עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$: $W=\operatorname{Sp}\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix}\right\}$ ו-$V=\begin{pmatrix}1&0\\2&2\end{pmatrix}$. הוקטורים הפורשים אינם ניצבים (המכפלה $1$), לכן גרהם-שמידט: $u_1=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, וגם $u_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}-\frac12u_1$, ובכפל ב-$2$ נקבל $u_2=\begin{pmatrix}-1&1\\2&0\end{pmatrix}$ עם $\|u_2\|^2=6$.</div>
<p>בקטע סימטרי $[-1,1]$ משתמשים בזוגיות: $\langle f,g\rangle=0$ כשאחת הפונקציות זוגית והשנייה אי-זוגית, וגם $\|1\|^2=2$ ו-$\|x\|^2=\frac23$. אם הפורשים כבר ניצבים, כמו $1$ ו-$x$, מדלגים על גרהם-שמידט.</p>
<div class="lesson-trap">⚠️ אם מציבים בנוסחה על פורשים שאינם ניצבים מקבלים תשובה שגויה, והבדיקה $\langle V-\operatorname{Proj},u_i\rangle=0$ תיכשל. תמיד בודקים.</div>
` },
  questions: [
    { id: "C06-Q1",
      step: { type: "numeric",
        prompt: String.raw`ב-$M_2(\mathbb{R})$ עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ נתון $W=\operatorname{Sp}\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}1&0\\0&-1\end{pmatrix}\right\}$ (הפורשים ניצבים) ו-$V=\begin{pmatrix}3&1\\2&5\end{pmatrix}$. חשבו את $\|V-\operatorname{Proj}_W(V)\|^2$.`,
        answer: 5, tol: 0,
        explain: String.raw`המקדמים: $\frac{3+5}{2}=4$ ו-$\frac{3-5}{2}=-1$, לכן $\operatorname{Proj}_W(V)=4I-\operatorname{diag}(1,-1)=\begin{pmatrix}3&0\\0&5\end{pmatrix}$. השארית היא $\begin{pmatrix}0&1\\2&0\end{pmatrix}$ ונורמתה בריבוע $1+4=5$.` },
      recap: "ההיטל על מטריצות אלכסוניות משאיר את האלכסון, והשארית היא מה שמחוץ לו." },
    { id: "C06-Q2",
      question: String.raw`ב-$M_2(\mathbb{R})$ עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ נתונים $W=\operatorname{Sp}\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix}\right\}$ ו-$V=\begin{pmatrix}1&0\\2&2\end{pmatrix}$. מהו $\operatorname{Proj}_W(V)$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}0&1\\1&0\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}\frac12&\frac32\\1&0\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}\frac12&\frac12\\0&0\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}1&0\\2&2\end{pmatrix}$` }],
      correctId: "a",
      explanation: String.raw`אחרי גרהם-שמידט: $u_1=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ עם $\langle V,u_1\rangle=1$ ו-$\|u_1\|^2=2$, ו-$u_2=\begin{pmatrix}-1&1\\2&0\end{pmatrix}$ עם $\langle V,u_2\rangle=3$ ו-$\|u_2\|^2=6$. ההיטל הוא $\frac12u_1+\frac12u_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. המטריצה $\begin{pmatrix}\frac12&\frac32\\1&0\end{pmatrix}$ היא תוצאת הנוסחה על הפורשים המקוריים שאינם ניצבים. המטריצה $\begin{pmatrix}\frac12&\frac12\\0&0\end{pmatrix}$ היא ההיטל על הוקטור הראשון בלבד. והמטריצה $V$ עצמה אינה ב-$W$.`,
      recap: "פורשים לא ניצבים ← גרהם-שמידט לפני ההיטל." },
    { id: "C06-Q3",
      step: { type: "numeric",
        prompt: String.raw`ב-$C[0,1]$ עם $\langle f,g\rangle=\int_0^1f(x)g(x)\,dx$ מבצעים גרהם-שמידט על $\{1,x\}$. מקבלים $u_1=1$ ו-$u_2=x-c$. מהו $c$ ?`,
        answer: 0.5, tol: 0.001,
        explain: String.raw`$c=\frac{\langle x,1\rangle}{\|1\|^2}=\frac{\int_0^1x\,dx}{\int_0^11\,dx}=\frac{1/2}{1}=\frac12$.` },
      recap: "בקטע שאינו סימטרי $1$ ו-$x$ אינם ניצבים." },
    { id: "C06-Q4",
      question: String.raw`ב-$C[-1,1]$ עם $\langle f,g\rangle=\int_{-1}^{1}f(x)g(x)\,dx$ מהו ההיטל של $h(x)=x^3+1$ על $\operatorname{Sp}\{1,x\}$ ?`,
      options: [
        { id: "a", value: String.raw`$1+\frac35x$` },
        { id: "b", value: String.raw`$1+x$` },
        { id: "c", value: String.raw`$\frac35x$` },
        { id: "d", value: String.raw`$1+\frac53x$` }],
      correctId: "a",
      explanation: String.raw`הפורשים $1$ ו-$x$ ניצבים (אי-זוגית כפול זוגית). $\frac{\langle h,1\rangle}{\|1\|^2}=\frac{2}{2}=1$ ו-$\frac{\langle h,x\rangle}{\|x\|^2}=\frac{2/5}{2/3}=\frac35$. הפונקציה $1+x$ מתקבלת מהנחה שגויה ש-$h$ כבר ב-$W$. הפונקציה $\frac35x$ שוכחת את המרכיב הקבוע. והמקדם $\frac53$ הוא ההופכי של המקדם הנכון.`,
      recap: String.raw`$\int_{-1}^{1}x^4=\frac25$, $\|x\|^2=\frac23$.` },
    { bankId: "24B-B-Q1c", recap: "ההיטל על $\\operatorname{Sp}\\{A,B\\}$ אחרי גרהם-שמידט של הסעיף הקודם." },
    { bankId: "24A-A-Q1b", recap: "גרהם-שמידט, נרמול, ואז סכום ההיטלים." },
  ],
});
