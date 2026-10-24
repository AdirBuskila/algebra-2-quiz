/* proj_gs, level 4 - orthogonal / orthonormal bases and projection onto a subspace (orthogonal basis only) */
COURSE_LEVEL("proj_gs", {
  id: "C04", order: 4, icon: "🧭", title: "בסיס אורתוגונלי והיטל על תת-מרחב",
  goal: "לחשב קואורדינטות בבסיס אורתונורמלי והיטל על תת-מרחב שנתון בבסיס אורתוגונלי, ולזהות מתי הנוסחה אסורה.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p><b>מערכת אורתוגונלית</b> היא וקטורים שונים מאפס שכל שניים מהם ניצבים. מערכת כזו בלתי תלויה לינארית. <b>אורתונורמלית</b> היא מערכת אורתוגונלית שבה בנוסף כל הנורמות שוות $1$.</p>
<p>אם $g_1,\dots,g_k$ אורתונורמלית ו-$x=\alpha_1g_1+\dots+\alpha_kg_k$ אז הקואורדינטות הן $\alpha_i=\langle x,g_i\rangle$ ו-$\|x\|^2=\alpha_1^2+\dots+\alpha_k^2$ (פיתגורס).</p>
<p><b>היטל על תת-מרחב.</b> אם $u_1,\dots,u_k$ בסיס <b>אורתוגונלי</b> של $W$, אז
$$\operatorname{Proj}_W(v)=\sum_{i=1}^k\frac{\langle v,u_i\rangle}{\|u_i\|^2}\,u_i.$$
זה סכום של היטלים על כל וקטור בנפרד. ההיטל שייך ל-$W$, והשארית $v-\operatorname{Proj}_W(v)$ ניצבת לכל $W$. גם כאן $\|v\|^2=\|\operatorname{Proj}_Wv\|^2+\|v-\operatorname{Proj}_Wv\|^2$.</p>
<div class="lesson-ex">דוגמה: $u_1=(1,1,0)$, $u_2=(1,-1,2)$ ניצבים ($1-1+0=0$). עבור $v=(3,1,5)$: $\langle v,u_1\rangle=4$ עם $\|u_1\|^2=2$, ו-$\langle v,u_2\rangle=12$ עם $\|u_2\|^2=6$. לכן $\operatorname{Proj}_W(v)=2u_1+2u_2=(4,0,4)$.</div>
<div class="lesson-trap">⚠️ הנוסחה נכונה <b>רק</b> כשהבסיס אורתוגונלי. על בסיס שאינו אורתוגונלי היא נותנת וקטור שגוי. בודקים ניצבות לפני שמציבים, ואם אין, עוברים לגרהם-שמידט (הרמה הבאה).</div>
` },
  questions: [
    { id: "C04-Q1",
      step: { type: "numeric",
        prompt: String.raw`נתון $W=\operatorname{Sp}\{u_1,u_2\}$ עם $u_1=(1,1,0)$ ו-$u_2=(1,-1,2)$, והם ניצבים. חשבו את הרכיב הראשון של $\operatorname{Proj}_W(v)$ עבור $v=(3,1,5)$.`,
        answer: 4, tol: 0,
        explain: String.raw`$\operatorname{Proj}_W(v)=\frac42u_1+\frac{12}6u_2=2(1,1,0)+2(1,-1,2)=(4,0,4)$. הרכיב הראשון הוא $4$.` },
      recap: "בבסיס אורתוגונלי: מסכמים היטל על כל וקטור בנפרד." },
    { id: "C04-Q2",
      question: String.raw`הוקטורים $g_1=\frac1{\sqrt2}(1,1,0)$, $g_2=\frac1{\sqrt2}(1,-1,0)$, $g_3=(0,0,1)$ הם בסיס אורתונורמלי של $\mathbb{R}^3$. מהו המקדם של $g_1$ בהצגה של $v=(3,1,5)$ ?`,
      options: [
        { id: "a", value: String.raw`$2\sqrt2$` },
        { id: "b", value: String.raw`$4$` },
        { id: "c", value: String.raw`$2$` },
        { id: "d", value: String.raw`$\sqrt2$` }],
      correctId: "a",
      explanation: String.raw`בבסיס אורתונורמלי המקדם הוא $\langle v,g_1\rangle=\frac{3+1}{\sqrt2}=2\sqrt2$. הערך $4$ הוא $\langle v,(1,1,0)\rangle$ בלי נרמול. הערך $2$ הוא המקדם של הוקטור הלא מנורמל $(1,1,0)$. והערך $\sqrt2$ הוא המקדם של $g_2$.`,
      recap: String.raw`אורתונורמלי: $\alpha_i=\langle v,g_i\rangle$, בלי חילוק.` },
    { id: "C04-Q3",
      question: String.raw`נתון $W=\operatorname{Sp}\{(1,0,0),(1,1,0)\}$ ו-$v=(2,3,5)$. מהו $\operatorname{Proj}_W(v)$ ?`,
      options: [
        { id: "a", value: String.raw`$(2,3,0)$` },
        { id: "b", value: String.raw`$\left(\frac92,\frac52,0\right)$` },
        { id: "c", value: String.raw`$(2,0,0)$` },
        { id: "d", value: String.raw`$(2,3,5)$` }],
      correctId: "a",
      explanation: String.raw`שני הוקטורים אינם ניצבים ($\langle(1,0,0),(1,1,0)\rangle=1$), ולכן אסור להציב בנוסחה. אבל $W$ הוא המישור $z=0$, וההיטל עליו מאפס את הרכיב השלישי: $(2,3,0)$. הוקטור $\left(\frac92,\frac52,0\right)$ מתקבל מהנוסחה על בסיס שאינו אורתוגונלי, והוא אינו ניצב לשארית. הוקטור $(2,0,0)$ הוא ההיטל על הוקטור הראשון בלבד. והוקטור $(2,3,5)$ הוא $v$ עצמו, ו-$v$ אינו ב-$W$.`,
      recap: "לפני שמציבים בנוסחה: האם הבסיס אורתוגונלי ?" },
    { id: "C04-Q4",
      step: { type: "numeric",
        prompt: String.raw`עבור איזה ערך של $a$ הוקטורים $(1,2,1)$ ו-$(a,1,-1)$ ניצבים ?`,
        answer: -1, tol: 0,
        explain: String.raw`$\langle(1,2,1),(a,1,-1)\rangle=a+2-1=a+1$. השוויון ל-$0$ נותן $a=-1$.` },
      recap: "ניצבות עם פרמטר: מכפלה פנימית שווה אפס." },
    { id: "C04-Q5",
      step: { type: "numeric",
        prompt: String.raw`באותו תת-מרחב $W=\operatorname{Sp}\{(1,1,0),(1,-1,2)\}$ ועם $v=(3,1,5)$, חשבו את $\|\operatorname{Proj}_W(v)\|^2$.`,
        answer: 32, tol: 0,
        explain: String.raw`$\operatorname{Proj}_W(v)=(4,0,4)$ ו-$\|\cdot\|^2=16+0+16=32$. בדיקה לפי פיתגורס: השארית $(-1,1,1)$ בעלת נורמה בריבוע $3$, ו-$\|v\|^2=35=32+3$.` },
      recap: "פיתגורס: $\\|v\\|^2$ מתפצל להיטל ושארית." },
    { bankId: "23A-A-Q3c", recap: "במערכת אורתונורמלית $\\|x\\|^2$ הוא סכום ריבועי המקדמים." },
  ],
});
