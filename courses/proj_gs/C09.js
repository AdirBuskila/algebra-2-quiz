/* proj_gs, level 9 - QR decomposition from Gram-Schmidt, R = Q^T A, solving with QR */
COURSE_LEVEL("proj_gs", {
  id: "C09", order: 9, icon: "🧱", title: "פירוק QR",
  goal: "לבנות פירוק $A=QR$ מגרהם-שמידט, לקרוא את $R$ מהמכפלות, ולפתור $A\\vec x=\\vec b$ וריבועים פחותים בעזרתו.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>לכל מטריצה $A$ עם עמודות בלתי תלויות קיים פירוק $A=QR$: ל-$Q$ עמודות <b>אורתונורמליות</b> ($Q^TQ=I$), ו-$R$ היא <b>משולשת עליונה</b> הפיכה.</p>
<div class="lesson-rule">🔑 בניה: מבצעים גרהם-שמידט על עמודות $A$ ומנרמלים: $q_i=\frac{u_i}{\|u_i\|}$ הן עמודות $Q$. אז
$$R=Q^TA,\qquad r_{ii}=\|u_i\|,\qquad r_{ij}=\langle a_j,q_i\rangle\ \ (i<j),$$
ומתחת לאלכסון יש אפסים.</div>
<div class="lesson-ex">דוגמה: $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$, עמודות $a_1=(1,1)$, ‏$a_2=(1,0)$. אז $u_1=a_1$, ‏$r_{11}=\sqrt2$, ‏$q_1=\frac1{\sqrt2}(1,1)$. כמו כן $r_{12}=\langle a_2,q_1\rangle=\frac1{\sqrt2}$ ו-$u_2=a_2-\frac12a_1=\left(\frac12,-\frac12\right)$ עם $r_{22}=\|u_2\|=\frac1{\sqrt2}$, ‏$q_2=\frac1{\sqrt2}(1,-1)$. בדיקה: $r_{11}q_1=(1,1)=a_1$.</div>
<p><b>שימושים.</b> מכיוון ש-$Q^TQ=I$, המערכת $A\vec x=\vec b$ הופכת ל-$R\vec x=Q^T\vec b$, שאותה פותרים בהצבה לאחור. בריבועים פחותים $A^TA=R^TR$, ולכן $R\hat x=Q^T\vec b$ בלי להפוך מטריצה.</p>
<div class="lesson-trap">⚠️ $r_{ij}$ הוא המכפלה עם $q_i$ המנורמל, ולא עם $u_i$. ואם $R$ אינה משולשת עליונה, יש טעות בגרהם-שמידט.</div>
` },
  questions: [
    { id: "C09-Q1",
      question: String.raw`נתונה $A=\begin{pmatrix}3&5\\4&0\end{pmatrix}$. עמודותיה $a_1=(3,4)$ ו-$a_2=(5,0)$. איזו מטריצה היא ה-$R$ של פירוק $A=QR$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}5&3\\0&4\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}5&0\\3&4\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}5&15\\0&4\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}5&3\\0&16\end{pmatrix}$` }],
      correctId: "a",
      explanation: String.raw`$r_{11}=\|a_1\|=5$ ו-$q_1=\left(\frac35,\frac45\right)$. אז $r_{12}=\langle a_2,q_1\rangle=3$, ‏$u_2=a_2-3q_1=\left(\frac{16}5,-\frac{12}5\right)$ ו-$r_{22}=\|u_2\|=4$. המטריצה השנייה אינה משולשת עליונה. הערך $15$ הוא $\langle a_2,a_1\rangle$, בלי לנרמל את $a_1$. והערך $16$ הוא $\|u_2\|^2$ ולא $\|u_2\|$.`,
      recap: String.raw`$r_{ii}=\|u_i\|$, ‏$r_{ij}=\langle a_j,q_i\rangle$` },
    { id: "C09-Q2",
      step: { type: "numeric",
        prompt: String.raw`בפירוק $A=QR$ של $A=\begin{pmatrix}3&5\\4&0\end{pmatrix}$ מתקבל $q_1=\left(\frac35,\frac45\right)$ ו-$q_2=\left(\frac45,-\frac35\right)$. נתון $\vec b=(5,10)$. חשבו את הרכיב השני של $Q^T\vec b$.`,
        answer: -2, tol: 0,
        explain: String.raw`הרכיב השני הוא $\langle\vec b,q_2\rangle=\frac45\cdot5-\frac35\cdot10=4-6=-2$. (הרכיב הראשון הוא $\langle\vec b,q_1\rangle=3+8=11$.)` },
      recap: String.raw`$Q^T\vec b$ הוא וקטור המכפלות $\langle\vec b,q_i\rangle$.` },
    { id: "C09-Q3",
      step: { type: "numeric",
        prompt: String.raw`המשך: $R=\begin{pmatrix}5&3\\0&4\end{pmatrix}$ ו-$Q^T\vec b=\binom{11}{-2}$. פותרים $R\vec x=Q^T\vec b$ בהצבה לאחור. מהו $x_1$ ?`,
        answer: 2.5, tol: 0.001,
        explain: String.raw`מהשורה התחתונה $4x_2=-2$, ולכן $x_2=-0.5$. מהשורה העליונה $5x_1+3x_2=11$, ולכן $x_1=\frac{11+1.5}{5}=2.5$. בדיקה: $A\vec x=(7.5-2.5,\ 10)=(5,10)=\vec b$.` },
      recap: "משולשת עליונה: מתחילים מהמשוואה האחרונה." },
    { id: "C09-Q4",
      step: { type: "findbug",
        prompt: String.raw`נתונה $A=\begin{pmatrix}2&1\\0&1\\1&1\end{pmatrix}$ עם עמודות $a_1=(2,0,1)$ ו-$a_2=(1,1,1)$. בפתרון הבא של פירוק $QR$ יש שורה שגויה אחת. מצאו אותה.`,
        lines: [
          String.raw`$u_1=a_1=(2,0,1)$, ‏$\|u_1\|^2=5$`,
          String.raw`$\langle a_2,u_1\rangle=2+0+1=3$`,
          String.raw`$u_2=a_2-\frac35u_1=\left(-\frac15,1,\frac25\right)$`,
          String.raw`$\|u_2\|^2=\frac1{25}+1+\frac4{25}=\frac65$`,
          String.raw`$r_{11}=\sqrt5,\ \ r_{12}=3,\ \ r_{22}=\sqrt{\frac65}$`
        ],
        bugIndex: 4,
        explain: String.raw`האיבר $r_{12}$ הוא $\langle a_2,q_1\rangle=\frac{\langle a_2,u_1\rangle}{\|u_1\|}=\frac{3}{\sqrt5}$ ולא $3$: צריך להשתמש ב-$q_1$ המנורמל. השורות האחרות נכונות. בדיקה: $a_2=r_{12}q_1+r_{22}q_2$ מתקיים רק עם $r_{12}=\frac3{\sqrt5}$.` },
      recap: String.raw`$r_{12}=\langle a_2,q_1\rangle$ עם $q_1$ מנורמל.` },
    { id: "C09-Q5",
      question: String.raw`נתון $A=QR$ עם $Q^TQ=I$ ו-$R$ משולשת עליונה. מהי $A^TA$ ?`,
      options: [
        { id: "a", value: String.raw`$R^TR$` },
        { id: "b", value: String.raw`$RR^T$` },
        { id: "c", value: String.raw`$R^2$` },
        { id: "d", value: String.raw`$I$` }],
      correctId: "a",
      explanation: String.raw`$A^TA=(QR)^T(QR)=R^TQ^TQR=R^TR$. המכפלה $RR^T$ בסדר הפוך אינה שווה לה בדרך כלל (בדוגמה של $A=\begin{pmatrix}3&5\\4&0\end{pmatrix}$ היא $\begin{pmatrix}34&12\\12&16\end{pmatrix}$ לעומת $\begin{pmatrix}25&15\\15&25\end{pmatrix}$). הריבוע $R^2$ אינו סימטרי. והמטריצה $I$ היא $Q^TQ$, לא $A^TA$.`,
      recap: String.raw`$A^TA=R^TR$, ולכן $A^TA\hat x=A^T\vec b$ הופך ל-$R\hat x=Q^T\vec b$.` },
    { bankId: "25B-B-Q4a", recap: "גרהם-שמידט על שלוש עמודות, נרמול, ו-$R=Q^TA$ משולשת עליונה." },
  ],
});
