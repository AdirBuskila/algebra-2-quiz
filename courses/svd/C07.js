/* SVD course, level 7 - signs, ordering conventions and checking U S V^T = A */
COURSE_LEVEL("svd", {
  id: "C07", order: 7, icon: "✅", title: "סימנים, סדר ובדיקה של U·S·Vᵀ = A",
  goal: "אחרי השלב הזה אפשר לדעת אילו שינויים בפירוק מותרים, לאמת פירוק שנמצא, ולמצוא טעות בבדיקה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>פירוק SVD <b>אינו יחיד</b>, ולכן שני פתרונות שונים של אותה שאלה יכולים להיות נכונים. מה כן קבוע ומה חופשי:</p>
    <ul>
      <li><b>הערכים הסינגולריים</b> קבועים: $\sigma_1\ge\sigma_2\ge\dots\ge0$ בסדר יורד, לפי המוסכמה.</li>
      <li><b>סימנים:</b> אפשר להחליף יחד $u_i\to-u_i$ ו-$v_i\to-v_i$ והמכפלה $USV^T$ לא משתנה. להחליף רק אחד מהם אסור: זה הופך את $Av_i=\sigma_iu_i$ ל-$Av_i=-\sigma_iu_i$.</li>
      <li><b>סדר:</b> העמודות $u_i,v_i$ חייבות להישאר באותו סדר כמו $\sigma_i$. אם מחליפים שתי עמודות של $V$ צריך להחליף גם את העמודות של $U$ ואת הערכים ב-$S$.</li>
      <li><b>העמודות המושלמות</b> (עם $\sigma=0$) הן בחירה חופשית בתוך המרחב המתאים, אחרי שהן אורתונורמליות.</li>
    </ul>
    <h3>בדיקה</h3>
    <p>שתי דרכים לבדוק פירוק שמצאתם:</p>
    <ol>
      <li>לכל $\sigma_i\ne0$ לבדוק $Av_i=\sigma_iu_i$ (מהיר, ובודק את הסימנים).</li>
      <li>לחשב $USV^T$ ולראות שמתקבלת $A$. אפשר גם לכתוב $A=\sum_{i\le r}\sigma_iu_iv_i^T$, ויש לבדוק ש-$U^TU=I$ ו-$V^TV=I$.</li>
    </ol>
    <div class="lesson-ex"><b>דוגמה.</b> ב-$A=\begin{pmatrix}1&1\\0&1\\1&0\end{pmatrix}$ עם $v_1=\frac1{\sqrt2}(1,1)$, $\sigma_1=\sqrt3$, $u_1=\frac1{\sqrt6}(2,1,1)$: $Av_1=\frac1{\sqrt2}(2,1,1)$ ו-$\sigma_1u_1=\sqrt3\cdot\frac1{\sqrt6}(2,1,1)=\frac1{\sqrt2}(2,1,1)$. הבדיקה עוברת.</div>
    <div class="lesson-rule">🔑 בדיקת בטחון נוספת: $\sigma_1^2+\sigma_2^2+\dots$ שווה לסכום ריבועי כל הכניסות של $A$.</div>
    <div class="lesson-trap">⚠️ הערכים הסינגולריים בסדר יורד. מטריצה $S$ שבה $\sigma$ קטן עומד לפני גדול היא טעות בהצגה, גם אם אפשר לתקן אותה בהחלפת עמודות.</div>` },
  questions: [
    { id: "C07-Q1",
      question: String.raw`נתון פירוק תקין $A=USV^T$ של $A=\begin{pmatrix}1&2\\2&1\\0&0\end{pmatrix}$ עם $\sigma_1=3$, $\sigma_2=1$. איזה שינוי משאיר אותו פירוק תקין של אותה $A$ ?`,
      options: [
        { id: "a", value: String.raw`מחליפים את $u_1$ ב-$-u_1$ בלבד` },
        { id: "b", value: String.raw`מחליפים את $v_2$ ב-$2v_2$` },
        { id: "c", value: String.raw`מחליפים את $u_1$ ב-$-u_1$ וגם את $v_1$ ב-$-v_1$` },
        { id: "d", value: String.raw`מחליפים את $\sigma_1$ ו-$\sigma_2$ ב-$S$ בלבד, ו-$U,V$ נשארות` },
      ],
      correctId: "c",
      explanation: String.raw`$u_1v_1^T$ נשאר זהה כשמחליפים את שני הווקטורים בסימן ההפוך, ולכן $USV^T$ לא משתנה. החלפת $u_1$ לבד הופכת את סימן האיבר $\sigma_1u_1v_1^T$ והמכפלה כבר אינה $A$. הכפלת $v_2$ ב-2 פוגעת בניצבות ובאורך. החלפת הערכים ב-$S$ בלבד משנה את המכפלה ופוגעת גם בסדר היורד.`,
      recap: String.raw`מותר להפוך סימן ל-$u_i$ ול-$v_i$ ביחד, לא לאחד מהם.` },
    { id: "C07-Q2",
      question: String.raw`$A=\begin{pmatrix}2&0\\0&1\end{pmatrix}$. איזה פירוק הוא פירוק SVD תקין של $A$ ?`,
      options: [
        { id: "a", value: String.raw`$U=I,\ S=\begin{pmatrix}1&0\\0&2\end{pmatrix},\ V=I$` },
        { id: "b", value: String.raw`$U=-I,\ S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\ V=I$` },
        { id: "c", value: String.raw`$U=\begin{pmatrix}0&1\\1&0\end{pmatrix},\ S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\ V=I$` },
        { id: "d", value: String.raw`$U=I,\ S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\ V=I$` },
      ],
      correctId: "d",
      explanation: String.raw`רק כאן $USV^T=S=A$ עם ערכים בסדר יורד. כשהערכים בסדר עולה המכפלה היא $\mathrm{diag}(1,2)$, שאינה $A$. כש-$U=-I$ המכפלה היא $-A$. כש-$U$ מחליפת שורות המכפלה היא $\begin{pmatrix}0&1\\2&0\end{pmatrix}$.`,
      recap: String.raw`מכפילים $USV^T$ ובודקים שמתקבלת $A$.` },
    { id: "C07-Q3",
      step: { type: "findbug",
        prompt: String.raw`$A=\begin{pmatrix}1&1\\0&1\\1&0\end{pmatrix}$ עם $v_1=\frac1{\sqrt2}(1,1)$, $v_2=\frac1{\sqrt2}(1,-1)$, $\sigma_1=\sqrt3$, $\sigma_2=1$, $u_1=\frac1{\sqrt6}(2,1,1)$, $u_2=\frac1{\sqrt2}(0,-1,1)$. בבדיקת $Av_i=\sigma_iu_i$ שורה אחת שגויה. איזו?`,
        lines: [
          String.raw`$Av_1=\frac1{\sqrt2}(2,1,1)$`,
          String.raw`$\sigma_1u_1=\sqrt3\cdot\frac1{\sqrt6}(2,1,1)=\frac1{\sqrt2}(2,1,1)$`,
          String.raw`$Av_2=\frac1{\sqrt2}(0,-1,1)$`,
          String.raw`$\sigma_2u_2=1\cdot\frac1{\sqrt2}(0,1,-1)$`,
        ],
        bugIndex: 3,
        explain: String.raw`$u_2=\frac1{\sqrt2}(0,-1,1)$, ולכן $\sigma_2u_2=\frac1{\sqrt2}(0,-1,1)$ ולא $\frac1{\sqrt2}(0,1,-1)$. השורה שגויה בסימן, והבדיקה הנכונה מראה $Av_2=\sigma_2u_2$.` },
      recap: String.raw`בבדיקה משווים את $Av_i$ ל-$\sigma_iu_i$ כולל הסימן.` },
    { id: "C07-Q4",
      question: String.raw`שני סטודנטים פירקו את אותה מטריצה, קיבלו שתי $U$ ושתי $V$ שונות (בסימנים של עמודה אחת), ושניהם בדקו ש-$USV^T=A$. מה נכון?`,
      options: [
        { id: "a", value: String.raw`לפחות אחד מהם טעה, כי פירוק SVD יחיד` },
        { id: "b", value: String.raw`שניהם יכולים להיות צודקים, כי פירוק SVD אינו יחיד (למשל הפיכת סימן של $u_i$ ושל $v_i$ יחד)` },
        { id: "c", value: String.raw`רק מי שהכניסות בעמודה הראשונה של $U$ אצלו חיוביות צודק` },
        { id: "d", value: String.raw`אי אפשר, כי הערכים הסינגולריים שלהם בהכרח שונים זה מזה` },
      ],
      correctId: "b",
      explanation: String.raw`אם $USV^T=A$ הפירוק תקין, וההפיכה המשותפת של $u_i$ ו-$v_i$ נותנת פירוק שני תקין עם אותה $A$. הערכים הסינגולריים זהים בשניהם. אין דרישת סימן על הכניסות של $U$.`,
      recap: "SVD אינו יחיד: בדיקת U·S·Vᵀ = A היא ההכרעה." },
    { id: "C07-Q5",
      step: { type: "numeric",
        prompt: String.raw`$A=\begin{pmatrix}3&1\\1&3\\0&0\end{pmatrix}$. מהו הסכום $\sigma_1^2+\sigma_2^2$ ? (בדיקת בטחון, בלי למצוא את הפירוק)`,
        answer: 20, tol: 0,
        explain: String.raw`הסכום שווה לסכום ריבועי כל הכניסות של $A$: $9+1+1+9=20$. אכן $A^TA=\begin{pmatrix}10&6\\6&10\end{pmatrix}$ עם ערכים עצמיים $16,4$, וסכומם $20$.` },
      recap: String.raw`$\sum\sigma_i^2$ = סכום ריבועי הכניסות של $A$.` },
    { bankId: "25A-B-Q1b", recap: "חישוב SVD מלא למטריצה 3×2: ערכים, V, U, השלמה ובדיקה." },
  ],
});
