/* orthodiag, level 2 - orthogonality of eigenvectors, Gram-Schmidt inside an eigenspace, normalising. */
COURSE_LEVEL("orthodiag", {
  id: "C02", order: 2, icon: "📐", title: "ניצבות של וקטורים עצמיים וגרהם-שמידט",
  goal: "לדעת מתי וקטורים עצמיים ניצבים מעצמם, ומתי צריך גרהם-שמידט בתוך מרחב עצמי, ולנרמל וקטור.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>המכפלה הפנימית הרגילה: $\langle u,v\rangle=u_1v_1+u_2v_2+u_3v_3$. הווקטורים ניצבים אם $\langle u,v\rangle=0$.</p>
    <div class="lesson-rule">🔑 <b>ערכים עצמיים שונים:</b> אם $A$ סימטרית, $Au=\lambda u$, $Av=\mu v$ ו-$\lambda\ne\mu$, אז $u\perp v$ אוטומטית.<br>
    <b>אותו ערך עצמי:</b> שני וקטורים עצמיים של אותו ערך עצמי הם בלתי תלויים, אבל <b>לא בהכרח ניצבים</b>.</div>
    <p>ההוכחה בקצרה: $\lambda\langle u,v\rangle=\langle Au,v\rangle=\langle u,Av\rangle=\mu\langle u,v\rangle$. השוויון האמצעי הוא הסימטריה של $A$. לכן $(\lambda-\mu)\langle u,v\rangle=0$, ומכיוון ש-$\lambda\ne\mu$ מקבלים $\langle u,v\rangle=0$.</p>
    <p><b>גרהם-שמידט בתוך מרחב עצמי:</b> אם $w_1,w_2$ בסיס של אותו מרחב עצמי, משאירים את $w_1$ ומחליפים
    $$w_2'=w_2-\frac{\langle w_2,w_1\rangle}{\langle w_1,w_1\rangle}\,w_1 .$$
    צירוף של וקטורים מאותו מרחב עצמי נשאר בו, ולכן $w_2'$ עדיין וקטור עצמי של אותו ערך עצמי.</p>
    <p><b>נרמול:</b> מחלקים וקטור באורכו, $\frac{v}{\|v\|}$, כדי לקבל אורך $1$.</p>
    <div class="lesson-ex">דוגמה: $A=\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$ מקבלת את הערך העצמי $2$ עם הווקטורים $w_1=(1,-1,0)$ ו-$w_2=(1,0,-1)$. הם לא ניצבים: $\langle w_2,w_1\rangle=1$ ו-$\langle w_1,w_1\rangle=2$, ולכן $w_2'=w_2-\tfrac12 w_1=(\tfrac12,\tfrac12,-1)$. בהכפלה ב-$2$ מקבלים $(1,1,-2)$.</div>
    <div class="lesson-trap">⚠️ מכפילים וקטור עצמי בסקלר ונשאר עצמי, ולכן מותר "לנקות מכנים". אבל נרמול חייב להיות אחרון.</div>
    ` },
  questions: [
    { id: "C02-Q1",
      question: String.raw`$A$ מטריצה סימטרית. $u$ וקטור עצמי של הערך העצמי $2$, ו-$v$ וקטור עצמי של הערך העצמי $5$. מה נכון תמיד?`,
      options: [
        { id: "a", value: String.raw`$\langle u,v\rangle=0$` },
        { id: "b", value: String.raw`$\langle u,v\rangle=10$` },
        { id: "c", value: String.raw`$\langle u,v\rangle\ne0$` },
        { id: "d", value: String.raw`אי אפשר לדעת, צריך לחשב את הווקטורים` },
      ],
      correctId: "a",
      explanation: String.raw`ערכים עצמיים שונים של מטריצה סימטרית נותנים וקטורים ניצבים: $\langle u,v\rangle=0$. הערך $10$ הוא מכפלת הערכים העצמיים ואין לו קשר למכפלה הפנימית. הטענה שהמכפלה שונה מאפס הפוכה למשפט. ואין צורך לחשב: המשפט תקף לכל זוג כזה.`,
      recap: "ערכים עצמיים שונים של סימטרית $\\Rightarrow$ וקטורים ניצבים." },
    { id: "C02-Q2",
      step: { type: "numeric",
        prompt: String.raw`ב-$A=\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$ שני הווקטורים $w_1=(1,-1,0)$ ו-$w_2=(1,0,-1)$ הם וקטורים עצמיים של אותו ערך עצמי. מהו $\langle w_1,w_2\rangle$?`,
        answer: 1, tol: 0,
        explain: String.raw`$\langle w_1,w_2\rangle=1\cdot1+(-1)\cdot0+0\cdot(-1)=1\ne0$. הם לא ניצבים, ולכן צריך גרהם-שמידט.` },
      recap: "אותו ערך עצמי: אפשר לקבל וקטורים שאינם ניצבים." },
    { id: "C02-Q3",
      step: { type: "numeric",
        prompt: String.raw`באותו מרחב עצמי, מה המקדם $\dfrac{\langle w_2,w_1\rangle}{\langle w_1,w_1\rangle}$ שבו מכפילים את $w_1$ בגרהם-שמידט ($w_1=(1,-1,0)$, $w_2=(1,0,-1)$)?`,
        answer: 0.5, tol: 0,
        explain: String.raw`$\langle w_2,w_1\rangle=1$ ו-$\langle w_1,w_1\rangle=2$, ולכן המקדם $\frac12$. כך $w_2'=w_2-\frac12w_1=(\frac12,\frac12,-1)$.` },
      recap: "$w_2'=w_2-\\frac{\\langle w_2,w_1\\rangle}{\\langle w_1,w_1\\rangle}w_1$." },
    { id: "C02-Q4",
      step: { type: "numeric",
        prompt: String.raw`אחרי גרהם-שמידט וניקוי מכנים קיבלנו את הווקטור $(1,1,-2)$. מהו $\|(1,1,-2)\|^2$?`,
        answer: 6, tol: 0,
        explain: String.raw`$1+1+4=6$, ולכן האורך הוא $\sqrt6$.` },
      recap: "האורך בריבוע הוא סכום ריבועי הרכיבים." },
    { id: "C02-Q5",
      question: String.raw`מהו הווקטור המנורמל שנקבל מ-$(1,1,-2)$?`,
      options: [
        { id: "a", value: String.raw`$\frac{1}{6}(1,1,-2)$` },
        { id: "b", value: String.raw`$\frac{1}{\sqrt2}(1,1,-2)$` },
        { id: "c", value: String.raw`$\frac{1}{\sqrt6}(1,1,-2)$` },
        { id: "d", value: String.raw`$(1,1,-2)$, הוא כבר מנורמל` },
      ],
      correctId: "c",
      explanation: String.raw`האורך הוא $\sqrt6$, ולכן מחלקים ב-$\sqrt6$. חילוק ב-$6$ נותן אורך $\frac{1}{\sqrt6}$ ולא $1$. חילוק ב-$\sqrt2$ נותן אורך $\sqrt3$. והווקטור המקורי באורך $\sqrt6$, לא $1$.`,
      recap: "מנרמלים בחלוקה באורך $\\|v\\|$, לא בריבוע שלו." },
    { id: "C02-Q6",
      step: { type: "order",
        prompt: String.raw`סדרו את ההוכחה שוקטורים עצמיים של מטריצה סימטרית $A$ עם ערכים עצמיים שונים $\lambda\ne\mu$ ניצבים.`,
        lines: [
          String.raw`נתון $Au=\lambda u$ ו-$Av=\mu v$, כאשר $\lambda\ne\mu$.`,
          String.raw`מחשבים $\lambda\langle u,v\rangle=\langle Au,v\rangle$.`,
          String.raw`מהסימטריה של $A$: $\langle Au,v\rangle=\langle u,Av\rangle$.`,
          String.raw`ומכאן $\langle u,Av\rangle=\mu\langle u,v\rangle$.`,
          String.raw`לכן $(\lambda-\mu)\langle u,v\rangle=0$, ומכיוון ש-$\lambda\ne\mu$ מתקבל $\langle u,v\rangle=0$.`,
        ],
        explain: String.raw`זו שרשרת שוויונות: כל שלב משתמש בקודם. את המסקנה אפשר לכתוב רק אחרי שני הצדדים של השוויון מופיעים.` },
      recap: "הוכחה: $\\lambda\\langle u,v\\rangle=\\langle Au,v\\rangle=\\langle u,Av\\rangle=\\mu\\langle u,v\\rangle$." },
  ],
});
