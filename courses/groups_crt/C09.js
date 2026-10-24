/* groups_crt, level 9: CRT with coefficients, large remainders and non-coprime moduli. */
COURSE_LEVEL("groups_crt", {
  id: "C09", order: 9, icon: "🛠️", title: "מקדמים, שאריות גדולות ומודולים לא זרים",
  goal: "להכין כל מערכת לצורה הרגילה, ולזהות מערכת שאין לה פתרון כי המודולים אינם זרים.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>במבחן המערכת לא תמיד מגיעה בצורה הנקייה. לפני שמפעילים את המתכון מכינים כל שורה:</p>
<ul>
<li><b>שארית גדולה מהמודול:</b> מחליפים בשארית. $x\equiv23\pmod9$ הופך ל-$x\equiv5\pmod9$.</li>
<li><b>מקדם לפני $x$:</b> כופלים בהופכי של המקדם. $5x\equiv2\pmod9$: ההופכי של $5$ הוא $2$, ולכן $x\equiv4\pmod9$.</li>
</ul>
<div class="lesson-ex">המערכת $3x\equiv4\pmod7,\ x\equiv10\pmod4$ הופכת ל-$x\equiv5\cdot4=20\equiv6\pmod7$ ול-$x\equiv2\pmod4$ (כי $3^{-1}=5$ מודולו $7$). רק עכשיו מפעילים את המתכון.</div>
<h3>מודולים שאינם זרים</h3>
<p>אם המודולים אינם זרים, אסור להפעיל את הנוסחה ישירות. מוצאים את $g=\gcd(m,n)$ של כל שני מודולים ובודקים <b>תאימות</b>: למערכת $x\equiv a\pmod m,\ x\equiv b\pmod n$ יש פתרון אם ורק אם $a\equiv b\pmod g$. כשיש פתרון, הוא יחיד מודולו $\operatorname{lcm}(m,n)$. אפשר למצוא אותו בניסוי: בודקים את הערכים $b,\ b+n,\ b+2n,\dots$ עד שאחד מהם מקיים את הקונגרואנציה $x\equiv a\pmod m$.</p>
<div class="lesson-ex">$x\equiv1\pmod4$ ו-$x\equiv2\pmod6$: כאן $g=2$ ו-$1\not\equiv2\pmod2$. המשוואה מודולו $4$ מחייבת $x$ אי-זוגי והמשוואה מודולו $6$ מחייבת $x$ זוגי, ולכן <b>אין פתרון</b>.</div>
<div class="lesson-ex">$x\equiv2\pmod4$ ו-$x\equiv0\pmod6$: $g=2$ ו-$2\equiv0\pmod2$, יש פתרון. הערכים $0,6,12,\dots$ מקיימים את המשוואה מודולו $6$, ו-$6\equiv2\pmod4$. לכן $x\equiv6\pmod{12}$.</div>
<div class="lesson-trap">⚠️ לא לדלג על השלב הראשון. מקדם או שארית גדולה שלא טופלו מובילים לתשובה שגויה גם אם כל שאר החישוב נכון.</div>
` },
  questions: [
    { id: "C09-Q1",
      step: { type: "numeric",
        prompt: String.raw`פתרו $4x\equiv3\pmod7$ וכתבו את הפתרון בין $0$ ל-$6$.`,
        answer: 6, tol: 0,
        explain: String.raw`$4^{-1}\equiv2\pmod7$ כי $4\cdot2=8\equiv1$. לכן $x\equiv2\cdot3=6\pmod7$. בדיקה: $4\cdot6=24=3\cdot7+3$.` },
      recap: "קודם מבטלים את המקדם בעזרת ההופכי שלו." },
    { id: "C09-Q2",
      step: { type: "numeric",
        prompt: String.raw`פתרו את המערכת $2x\equiv3\pmod7,\ \ x\equiv11\pmod4,\ \ x\equiv4\pmod5$ וכתבו את הפתרון בין $0$ ל-$139$.`,
        answer: 19, tol: 0,
        explain: String.raw`מכינים: $2^{-1}=4$ מודולו $7$, ולכן $x\equiv4\cdot3=12\equiv5\pmod7$. ו-$11\equiv3\pmod4$. המערכת הופכת ל-$x\equiv5\pmod7,\ x\equiv3\pmod4,\ x\equiv4\pmod5$ עם $M=140$. הפתרון הוא $x\equiv19\pmod{140}$. בדיקה: $2\cdot19=38\equiv3\pmod7$, $19\equiv3\pmod4$ ו-$19\equiv4\pmod5$.` },
      recap: "מכינים את המערכת לצורה הרגילה ורק אז מפעילים את הנוסחה." },
    { id: "C09-Q3",
      question: String.raw`מה נכון לגבי המערכת $x\equiv1\pmod4,\ \ x\equiv2\pmod6$ ?`,
      options: [
        { id: "a", value: "אין לה פתרון, כי לפי המשוואה מודולו $4$ המספר $x$ אי-זוגי, ולפי המשוואה מודולו $6$ הוא זוגי" },
        { id: "b", value: "יש לה פתרון יחיד מודולו $24$, לפי משפט השאריות הסיני" },
        { id: "c", value: "יש לה פתרון יחיד מודולו $12$" },
        { id: "d", value: "יש לה אינסוף פתרונות שונים מודולו $12$, כי המודולים אינם זרים" },
      ],
      correctId: "a",
      explanation: String.raw`$\gcd(4,6)=2$, והשאריות $1$ ו-$2$ אינן שוות מודולו $2$. המשוואה מודולו $4$ נותנת $x=4k+1$ אי-זוגי, והמשוואה מודולו $6$ נותנת $x=6j+2$ זוגי, ואין מספר שהוא גם וגם. משפט השאריות הסיני אינו חל על מודולים שאינם זרים, ולכן אסור להסיק ממנו פתרון מודולו $24$ (המכפלה). הטענות על פתרון יחיד מודולו $12$ ועל אינסוף פתרונות שגויות, כי בבדיקה של $x=0,\dots,11$ אף ערך אינו מקיים את שתי המשוואות.`,
      recap: "מודולים לא זרים: בודקים תאימות מודולו ה-gcd." },
    { id: "C09-Q4",
      step: { type: "numeric",
        prompt: String.raw`למערכת $x\equiv3\pmod4,\ \ x\equiv1\pmod6$ יש פתרון, והוא יחיד מודולו $12$. מהו הפתרון בין $0$ ל-$11$ ?`,
        answer: 7, tol: 0,
        explain: String.raw`$\gcd(4,6)=2$ ו-$3\equiv1\pmod2$, ולכן המערכת תואמת. הערכים שמקיימים את המשוואה מודולו $6$: $1,7,13,\dots$. הערך $1$ נותן $1\bmod4=1\ne3$, והערך $7$ נותן $7\bmod4=3$. לכן $x\equiv7\pmod{12}$.` },
      recap: String.raw`כשהמערכת תואמת, הפתרון יחיד מודולו $\operatorname{lcm}$.` },
    { id: "C09-Q5",
      step: { type: "findbug",
        prompt: String.raw`פותרים את $x\equiv1\pmod3,\ x\equiv2\pmod5,\ x\equiv5\pmod7$. שורה אחת בחישוב שגויה. מצאו אותה.`,
        lines: [
          String.raw`$M=3\cdot5\cdot7=105,\quad M_1=35,\ M_2=21,\ M_3=15$`,
          String.raw`$35x_1\equiv1\pmod3$, כלומר $2x_1\equiv1$ ולכן $x_1=1$`,
          String.raw`$21x_2\equiv1\pmod5$, כלומר $x_2\equiv1$ ולכן $x_2=1$`,
          String.raw`$15x_3\equiv1\pmod7$, כלומר $x_3\equiv1$ ולכן $x_3=1$`,
          String.raw`$x=1\cdot35\cdot x_1+2\cdot21\cdot x_2+5\cdot15\cdot x_3\pmod{105}$`,
        ],
        bugIndex: 1,
        explain: String.raw`בשורה של $35x_1\equiv1\pmod3$ נכתב $x_1=1$, אבל $2\cdot1=2\not\equiv1\pmod3$. ההופכי של $2$ מודולו $3$ הוא $2$ (כי $2\cdot2=4\equiv1$), ולכן $x_1=2$.` },
      recap: "בודקים כל $x_i$ בהצבה במשוואה שלו." },
    { bankId: "24A-C-Q4b", recap: "שארית גדולה מהמודול, ומודול 2: מצמצמים לפני שמפעילים את המתכון." },
  ],
});
