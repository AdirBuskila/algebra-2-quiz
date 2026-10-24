/* SVD course, level 8 - boss: real exam SVD questions */
COURSE_LEVEL("svd", {
  id: "C08", order: 8, icon: "🏆", title: "שלב אחרון: שאלות SVD ממבחנים",
  goal: "אחרי השלב הזה אפשר לפתור שאלת SVD מלאה ממבחן: ערכים סינגולריים, $V$, $U$, השלמה ובדיקה.",
  boss: true,
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>הנה כל מה שלמדתם, בסדר העבודה במבחן:</p>
    <ol>
      <li>בוחרים את הקטנה מבין $A^TA$ ($n\times n$) ו-$AA^T$ ($m\times m$).</li>
      <li>ערכים עצמיים בסדר יורד, ו-$\sigma_i=\sqrt{\lambda_i}$.</li>
      <li>וקטורים עצמיים מנורמלים הם עמודות $V$ (או $U$ אם פירקתם את $AA^T$), באותו סדר כמו הערכים.</li>
      <li>את הצד השני מחשבים בנוסחה: $u_i=\frac1{\sigma_i}Av_i$ או $v_i=\frac1{\sigma_i}A^Tu_i$.</li>
      <li>משלימים עמודות חסרות: ב-$U$ מכפלה וקטורית (ב-$\mathbb{R}^3$) או ניצבות; ב-$V$ מהגרעין של $A$.</li>
      <li>בונים $S$ בגודל $m\times n$, כותבים $A=USV^T$, ובודקים $Av_i=\sigma_iu_i$ או $USV^T=A$.</li>
    </ol>
    <div class="lesson-rule">🔑 בכל שאלה כאן: נסו לפתור על דף, ורק אז פתחו את הפתרון ובדקו את עצמכם. השאלות מופיעות כפי שהן במבחנים.</div>
    <div class="lesson-trap">⚠️ מלכודות במבחן: $V^T$ ולא $V$, גודל $S$ כגודל $A$, סימנים תואמים בין $u_i$ ל-$v_i$, וסדר יורד של הערכים.</div>` },
  questions: [
    { bankId: "23A-B-Q5a", recap: "SVD מלא ל-3×2: AᵀA, σ, V, U בנוסחה והשלמה." },
    { bankId: "23B-A-Q4a", recap: "SVD ל-2×3: AAᵀ קטנה, v_i בנוסחה והשלמת V מהגרעין." },
    { bankId: "24A-A-Q5a", recap: "SVD עם שורש: ערכים סינגולריים, V, U והשלמה." },
    { bankId: "24B-B-Q5a", recap: "SVD ל-3×2 עם שני ערכים סינגולריים והשלמת U." },
    { bankId: "26B-A-Q5c", recap: "SVD ל-3×2: מוצאים σ, V, U בנוסחה ומשלימים u_3." },
  ],
});
