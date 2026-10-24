/* proj_gs, level 5 - Gram-Schmidt in R^3 and in M_2 (trace inner product) */
COURSE_LEVEL("proj_gs", {
  id: "C05", order: 5, icon: "⚙️", title: "גרהם-שמידט",
  goal: "להפוך בסיס כלשהו לבסיס אורתוגונלי בשיטת גרהם-שמידט, ב-$\\mathbb{R}^3$ ובמרחב המטריצות, ולזהות תלות לינארית.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>נתונים $v_1,\dots,v_k$ בלתי תלויים. גרהם-שמידט בונה מהם $u_1,\dots,u_k$ אורתוגונליים עם אותה פרישה:
$$u_1=v_1,\qquad u_m=v_m-\sum_{i<m}\frac{\langle v_m,u_i\rangle}{\|u_i\|^2}\,u_i.$$
כל וקטור חדש הוא ה<b>שארית</b> של $v_m$ אחרי שמחסירים ממנו את ההיטלים על כל הוקטורים שכבר נבנו. לכן הוא ניצב להם.</p>
<div class="lesson-rule">🔑 מתכון: (1) $u_1=v_1$. (2) לכל וקטור הבא מחשבים מקדם $\frac{\langle v_m,u_i\rangle}{\|u_i\|^2}$ לכל $u_i$ הקודם ומחסירים. (3) בודקים $\langle u_i,u_j\rangle=0$. (4) מנרמלים $g_i=\frac{u_i}{\|u_i\|}$ רק אם מבקשים אורתונורמלי.</div>
<p>מותר להכפיל כל $u_m$ בסקלר חיובי כדי להיפטר משברים. זה לא משנה את הניצבות ואת הפרישה, ורק מעדכנים את $\|u_m\|^2$.</p>
<div class="lesson-ex">דוגמה: $v_1=(1,1,0)$, $v_2=(1,0,1)$. $\langle v_2,u_1\rangle=1$ ו-$\|u_1\|^2=2$, לכן $u_2=v_2-\frac12u_1=\left(\frac12,-\frac12,1\right)$, ובכפל ב-$2$ מקבלים $(1,-1,2)$. בדיקה: $\langle u_1,u_2\rangle=1-1+0=0$.</div>
<p>אם אחד הוקטורים תלוי בקודמים לו, השארית שלו היא <b>וקטור האפס</b>. זה סימן שהקבוצה תלויה, ואת הוקטור הזה זורקים.</p>
<div class="lesson-trap">⚠️ מחסירים את <b>ההיטל</b> ולא את המקדם בלבד, ומחלקים ב-$\|u_i\|^2$ ולא ב-$\|u_i\|$. ובמטריצות המכפלה היא סכום מכפלות רכיבים.</div>
` },
  questions: [
    { id: "C05-Q1",
      step: { type: "numeric",
        prompt: String.raw`ב-$\mathbb{R}^3$ נתונים $v_1=(1,1,1)$ ו-$v_2=(1,2,3)$. בגרהם-שמידט $u_1=v_1$. מהו הרכיב הראשון של $u_2$ ?`,
        answer: -1, tol: 0,
        explain: String.raw`$\langle v_2,u_1\rangle=6$ ו-$\|u_1\|^2=3$, ולכן $u_2=v_2-2u_1=(-1,0,1)$. הרכיב הראשון הוא $-1$.` },
      recap: String.raw`$u_2=v_2-\frac{\langle v_2,u_1\rangle}{\|u_1\|^2}u_1$` },
    { id: "C05-Q2",
      question: String.raw`ב-$M_2(\mathbb{R})$ עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ נתונות $v_1=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ ו-$v_2=\begin{pmatrix}2&0\\0&2\end{pmatrix}$. בגרהם-שמידט $u_1=v_1$. מהו $u_2$ ?`,
      options: [
        { id: "a", value: String.raw`$\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$` },
        { id: "b", value: String.raw`$\begin{pmatrix}-2&-4\\-4&-2\end{pmatrix}$` },
        { id: "c", value: String.raw`$\begin{pmatrix}0&-2\\-2&0\end{pmatrix}$` },
        { id: "d", value: String.raw`$\begin{pmatrix}1&1\\1&1\end{pmatrix}$` }],
      correctId: "a",
      explanation: String.raw`$\langle v_2,u_1\rangle=4$ ו-$\|u_1\|^2=4$, המקדם הוא $1$ ו-$u_2=v_2-u_1=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. המטריצה $v_2-4u_1$ מתקבלת כשמשמיטים את החילוק. המטריצה $v_2-2u_1$ מתקבלת כשמחלקים ב-$\|u_1\|=2$ במקום ב-$\|u_1\|^2=4$. והמטריצה $u_1$ היא ההיטל עצמו, לא השארית.`,
      recap: "הוקטור החדש הוא השארית, לא ההיטל." },
    { id: "C05-Q3",
      step: { type: "numeric",
        prompt: String.raw`ב-$\mathbb{R}^3$ נתונים $v_1=(1,1,0)$, $v_2=(1,0,1)$, $v_3=(0,1,1)$. בגרהם-שמידט (בלי להכפיל בסקלרים) $u_1=(1,1,0)$ ו-$u_2=\left(\frac12,-\frac12,1\right)$. מהו הרכיב השלישי של $u_3$ ? (תשובה עשרונית, בעיגול לשתי ספרות)`,
        answer: 0.667, tol: 0.01,
        explain: String.raw`$\langle v_3,u_1\rangle=1$ עם $\|u_1\|^2=2$, ו-$\langle v_3,u_2\rangle=\frac12$ עם $\|u_2\|^2=\frac32$. לכן $u_3=v_3-\frac12u_1-\frac13u_2=\left(-\frac23,\frac23,\frac23\right)$. הרכיב השלישי הוא $\frac23\approx0.67$.` },
      recap: "לוקטור השלישי מחסירים היטלים על שני הקודמים." },
    { id: "C05-Q4",
      question: String.raw`נתונים $v_1=(1,0,1)$, $v_2=(0,1,1)$, $v_3=(1,1,2)$. מה יוצא כשמבצעים גרהם-שמידט על $v_3$ אחרי שנבנו $u_1$ ו-$u_2$ ?`,
      options: [
        { id: "a", value: "וקטור האפס, כי $v_3$ נמצא בפרישה של $v_1,v_2$" },
        { id: "b", value: "הוקטור $v_3$ עצמו, כי הוא כבר ניצב לקודמים" },
        { id: "c", value: "וקטור יחידה בכיוון $v_3$" },
        { id: "d", value: "וקטור שונה מאפס שניצב ל-$u_1$ ול-$u_2$" }],
      correctId: "a",
      explanation: String.raw`$v_3=v_1+v_2$, ולכן ההיטל של $v_3$ על $\operatorname{Sp}\{u_1,u_2\}=\operatorname{Sp}\{v_1,v_2\}$ הוא $v_3$ עצמו והשארית היא $0$. $v_3$ אינו ניצב ל-$v_1$ (המכפלה $3$). וקטור שונה מאפס שניצב לשני הראשונים אמנם קיים ב-$\mathbb{R}^3$, אבל גרהם-שמידט לא מחזיר אותו כאן: השארית היא בדיוק $0$. והתוצאה אינה וקטור יחידה, כי אי אפשר לנרמל את האפס.`,
      recap: "שארית אפס פירושה שהוקטור תלוי בקודמים." },
    { id: "C05-Q5",
      step: { type: "findbug",
        prompt: String.raw`נתון $v_1=(1,-1,0)$ ו-$v_2=(3,1,2)$. הפתרון הבא של $u_2$ בגרהם-שמידט מכיל שורה שגויה אחת. מצאו אותה.`,
        lines: [
          String.raw`$u_1=v_1=(1,-1,0)$`,
          String.raw`$\langle v_2,u_1\rangle=3-1+0=2$`,
          String.raw`$\|u_1\|^2=1+1+0=2$`,
          String.raw`$u_2=v_2-2\,u_1=(3,1,2)-(2,-2,0)=(1,3,2)$`,
          String.raw`בדיקה: צריך לקבל $\langle u_1,u_2\rangle=0$`
        ],
        bugIndex: 3,
        explain: String.raw`המקדם הוא $\frac{\langle v_2,u_1\rangle}{\|u_1\|^2}=\frac22=1$ ולא $2$. השורה הנכונה: $u_2=v_2-u_1=(2,2,2)$, ואז $\langle u_1,u_2\rangle=2-2+0=0$. עם התוצאה השגויה $(1,3,2)$ המכפלה היא $-2$ ולא $0$, ולכן הבדיקה בשורה האחרונה הייתה חושפת את הטעות.` },
      recap: "בודקים $\\langle u_i,u_j\\rangle=0$ בסוף כל שלב." },
    { bankId: "24B-B-Q1b", recap: "גרהם-שמידט בין שתי מטריצות, עם הכפלה בסקלר כדי להיפטר משברים." },
  ],
});
