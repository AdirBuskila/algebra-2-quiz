/* proj_gs, level 3 - projection onto a single vector: formula, residual, Pythagoras, P = a a^T */
COURSE_LEVEL("proj_gs", {
  id: "C03", order: 3, icon: "↗", title: "היטל על וקטור יחיד",
  goal: "לחשב את ההיטל של וקטור על וקטור אחר, את השארית ואת המרחק, ולהשתמש בניצבות השארית ובפיתגורס.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>ההיטל של $b$ על הישר שנפרש על ידי $a\ne0$ הוא הכפולה של $a$ שהכי קרובה ל-$b$:
$$\operatorname{Proj}_a(b)=\frac{\langle b,a\rangle}{\|a\|^2}\,a.$$
המקדם $\frac{\langle b,a\rangle}{\|a\|^2}$ הוא מספר אחד. הנוסחה עובדת בכל מרחב מכפלה פנימית: וקטורים, מטריצות ופונקציות.</p>
<p>נסמן $p=\operatorname{Proj}_a(b)$ ואת <b>השארית</b> $c=b-p$. מתקיימות שתי עובדות:</p>
<ul>
<li>השארית ניצבת ל-$a$ (ולכן גם ל-$p$): $\langle c,a\rangle=0$.</li>
<li>פיתגורס: $\|b\|^2=\|p\|^2+\|c\|^2$. המרחק מ-$b$ לישר הוא $\|c\|$.</li>
</ul>
<div class="lesson-ex">דוגמה: $a=(1,1,1)$ ו-$b=(2,3,7)$. אז $\langle b,a\rangle=12$ ו-$\|a\|^2=3$, ולכן $p=4a=(4,4,4)$ ו-$c=(-2,-1,3)$. בדיקה: $\langle c,a\rangle=0$, ו-$\|b\|^2=62=48+14=\|p\|^2+\|c\|^2$.</div>
<div class="lesson-rule">🔑 אם $\|a\|=1$ המכנה הוא $1$, וההיטל הוא $\langle b,a\rangle a$. בכתיב מטריצות זה $P=aa^T$, כלומר $p=aa^Tb$.</div>
<div class="lesson-trap">⚠️ מחלקים ב-$\|a\|^2$ ולא ב-$\|a\|$. הטעות הזו נותנת וקטור באורך שגוי, והשארית כבר לא ניצבת.</div>
` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: String.raw`ב-$\mathbb{R}^3$ נתונים $a=(1,1,1)$ ו-$b=(2,3,7)$. מהו הרכיב הראשון של $\operatorname{Proj}_a(b)$ ?`,
        answer: 4, tol: 0,
        explain: String.raw`$\langle b,a\rangle=12$, $\|a\|^2=3$, המקדם הוא $4$ ולכן $\operatorname{Proj}_a(b)=(4,4,4)$.` },
      recap: String.raw`$\operatorname{Proj}_a(b)=\frac{\langle b,a\rangle}{\|a\|^2}a$` },
    { id: "C03-Q2",
      question: String.raw`ב-$\mathbb{R}^2$ נתונים $a=(3,4)$ ו-$b=(2,11)$. מהו $\operatorname{Proj}_a(b)$ ?`,
      options: [
        { id: "a", value: String.raw`$(6,8)$` },
        { id: "b", value: String.raw`$(30,40)$` },
        { id: "c", value: String.raw`$(150,200)$` },
        { id: "d", value: String.raw`$(2,11)$` }],
      correctId: "a",
      explanation: String.raw`$\langle b,a\rangle=6+44=50$ ו-$\|a\|^2=25$, המקדם הוא $2$ ולכן ההיטל הוא $2a=(6,8)$. הוקטור $(30,40)$ מתקבל כשמחלקים ב-$\|a\|=5$ במקום ב-$25$. הוקטור $(150,200)$ מתקבל כשמשמיטים את החילוק. והוקטור $(2,11)$ הוא $b$ עצמו, וזה היה נכון רק אילו $b$ היה על הישר.`,
      recap: "מחלקים ב-$\\|a\\|^2$, לא ב-$\\|a\\|$." },
    { id: "C03-Q3",
      step: { type: "numeric",
        prompt: String.raw`באותם וקטורים של הדוגמה, $a=(1,1,1)$ ו-$b=(2,3,7)$, חשבו את $\|b-\operatorname{Proj}_a(b)\|^2$, כלומר את ריבוע המרחק מ-$b$ אל הישר.`,
        answer: 14, tol: 0,
        explain: String.raw`השארית היא $b-p=(2,3,7)-(4,4,4)=(-2,-1,3)$ ו-$\|c\|^2=4+1+9=14$. בדרך אחרת, לפי פיתגורס: $62-48=14$.` },
      recap: String.raw`$\|b\|^2=\|p\|^2+\|c\|^2$` },
    { id: "C03-Q4",
      step: { type: "numeric",
        prompt: String.raw`הוקטור $a=\left(\frac35,\frac45\right)$ הוא וקטור יחידה ב-$\mathbb{R}^2$ ו-$P=aa^T$. חשבו את הרכיב השני של $P\binom{5}{0}$.`,
        answer: 2.4, tol: 0.01,
        explain: String.raw`$a^T\binom50=3$, ולכן $P\binom50=3a=\left(\frac95,\frac{12}5\right)$. הרכיב השני הוא $\frac{12}{5}=2.4$.` },
      recap: String.raw`לוקטור יחידה: $\operatorname{Proj}_a(b)=aa^Tb$.` },
    { bankId: "26A-A-Q3c", recap: "מציבים את הגדרת ההיטל ומקבלים $\\langle b,a\\rangle-\\langle b,a\\rangle=0$." },
    { bankId: "26A-A-Q3d", recap: "השארית ניצבת להיטל, ולכן פיתגורס." },
  ],
});
