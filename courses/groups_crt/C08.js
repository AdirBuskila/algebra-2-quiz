/* groups_crt, level 8: the Chinese remainder theorem recipe on a clean system. */
COURSE_LEVEL("groups_crt", {
  id: "C08", order: 8, icon: "🧭", title: "משפט השאריות הסיני: המתכון",
  goal: "לפתור מערכת של שלוש קונגרואנציות עם מודולים זרים בזוגות, שכל אחת מהן כבר בצורה מצומצמת.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p><b>משפט השאריות הסיני:</b> אם $m_1,\dots,m_k$ זרים בזוגות, אז למערכת $x\equiv a_i\pmod{m_i}$ יש פתרון, והוא <b>יחיד מודולו</b> $M=m_1m_2\cdots m_k$. את הפתרון נותנת הנוסחה
$$x\equiv a_1M_1x_1+\dots+a_kM_kx_k\pmod M,\qquad M_i=\frac M{m_i},\quad M_ix_i\equiv1\pmod{m_i}.$$
כלומר $x_i$ הוא ההופכי של $M_i$ מודולו $m_i$ (בעזרת מה שלמדנו בשלב הקודם).</p>
<h3>המתכון</h3>
<ul>
<li>מוודאים שהמודולים זרים בזוגות, ומחשבים $M=m_1\cdots m_k$.</li>
<li>מחשבים $M_i=M/m_i$ לכל $i$.</li>
<li>לכל $i$ פותרים $M_ix_i\equiv1\pmod{m_i}$. כדאי קודם לצמצם את $M_i$ מודולו $m_i$.</li>
<li>מחשבים $x=\sum a_iM_ix_i$ ומצמצמים מודולו $M$, לתחום $0$ עד $M-1$.</li>
<li><b>בודקים</b> בהצבה בכל אחת מהקונגרואנציות המקוריות.</li>
</ul>
<div class="lesson-ex">נפתור $x\equiv2\pmod3,\ x\equiv3\pmod5,\ x\equiv2\pmod7$. מתקיים $M=105$ ו-$M_1=35,\ M_2=21,\ M_3=15$. נצמצם: $35\equiv2\pmod3$ ולכן $x_1=2$ (כי $2\cdot2=4\equiv1$). $21\equiv1\pmod5$ ולכן $x_2=1$. $15\equiv1\pmod7$ ולכן $x_3=1$. אז $x=2\cdot35\cdot2+3\cdot21\cdot1+2\cdot15\cdot1=233\equiv23\pmod{105}$. בדיקה: $23\equiv2\pmod3$, $23\equiv3\pmod5$, $23\equiv2\pmod7$.</div>
<div class="lesson-trap">⚠️ $x_i$ הוא ההופכי של $M_i$ מודולו $m_i$, ולא של $m_i$ מודולו $M_i$. ובסוף חייבים לצמצם מודולו $M$.</div>
<div class="lesson-rule">🔑 אפשר לסדר את החישוב בטבלה: $m_i,\ a_i,\ M_i,\ M_i\bmod m_i,\ x_i$.</div>
` },
  questions: [
    { id: "C08-Q1",
      step: { type: "numeric",
        prompt: String.raw`פותרים את המערכת $x\equiv2\pmod3,\ x\equiv3\pmod4,\ x\equiv1\pmod5$. מתקיים $M=60$. מהו $M_2$ ?`,
        answer: 15, tol: 0,
        explain: String.raw`$M_2=\dfrac{M}{m_2}=\dfrac{60}{4}=15$.` },
      recap: String.raw`$M_i=M/m_i$.` },
    { id: "C08-Q2",
      step: { type: "numeric",
        prompt: String.raw`באותה מערכת, $M_3=12$. מהו $x_3$ שמקיים $12x_3\equiv1\pmod5$ (ערך בין $0$ ל-$4$) ?`,
        answer: 3, tol: 0,
        explain: String.raw`$12\equiv2\pmod5$, לכן צריך $2x_3\equiv1$. ההופכי של $2$ מודולו $5$ הוא $3$, כי $2\cdot3=6\equiv1$. בדיקה: $12\cdot3=36=7\cdot5+1$.` },
      recap: String.raw`$x_i$ הוא ההופכי של $M_i$ מודולו $m_i$.` },
    { id: "C08-Q3",
      step: { type: "numeric",
        prompt: String.raw`באותה מערכת, $x_1=2$, $x_2=3$ ו-$x_3=3$ (עם $M_1=20,\ M_2=15,\ M_3=12$). מהו הפתרון $x$ בין $0$ ל-$59$ ?`,
        answer: 11, tol: 0,
        explain: String.raw`$x=2\cdot20\cdot2+3\cdot15\cdot3+1\cdot12\cdot3=80+135+36=251$, ומצמצמים: $251=4\cdot60+11$, לכן $x\equiv11\pmod{60}$. בדיקה: $11\equiv2\pmod3$, $11\equiv3\pmod4$, $11\equiv1\pmod5$.` },
      recap: "מחברים את שלושת המחוברים ומצמצמים מודולו $M$." },
    { id: "C08-Q4",
      step: { type: "order",
        prompt: "סדרו את שלבי הפתרון של מערכת קונגרואנציות עם מודולים זרים.",
        lines: [
          String.raw`מוודאים שהמודולים זרים בזוגות ומחשבים $M=m_1m_2m_3$`,
          String.raw`מחשבים $M_i=M/m_i$ לכל $i$`,
          String.raw`לכל $i$ מוצאים $x_i$ מתוך $M_ix_i\equiv1\pmod{m_i}$`,
          String.raw`מחשבים $x=a_1M_1x_1+a_2M_2x_2+a_3M_3x_3$ ומצמצמים מודולו $M$`,
          "מציבים את התוצאה בכל אחת מהקונגרואנציות המקוריות לבדיקה",
        ],
        explain: String.raw`כל שלב משתמש בתוצאה של הקודם: $M_i$ דורש את $M$, $x_i$ דורש את $M_i$, הסכום דורש את $x_i$, והבדיקה דורשת את התוצאה הסופית.` },
      recap: String.raw`הסדר: $M$, אחר כך $M_i$, אחר כך $x_i$, אחר כך הסכום, ובסוף בדיקה.` },
    { bankId: "23B-B-Q3b", recap: String.raw`מערכת רגילה: טבלה של $m_i,\ a_i,\ M_i,\ x_i$, ואז סכום וצמצום.` },
    { bankId: "23A-B-Q5b", recap: "גם מודול שאינו ראשוני (כמו 4) מתאים, העיקר שהמודולים זרים בזוגות." },
  ],
});
