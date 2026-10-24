/* orthodiag, level 5 - quadratic forms x^T A x. */
COURSE_LEVEL("orthodiag", {
  id: "C05", order: 5, icon: "📈", title: "תבניות ריבועיות",
  goal: "לכתוב את התבנית הריבועית $x^TAx$ של מטריצה סימטרית, לחשב אותה, ולמצוא וקטור שנותן ערך שלילי.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>לכל מטריצה סימטרית $A$ ולכל וקטור $x$, הביטוי $x^TAx$ הוא <b>מספר</b>, ונקרא התבנית הריבועית של $A$. עבור $2\times2$:
    $$x^TAx=a_{11}x_1^2+2a_{12}x_1x_2+a_{22}x_2^2 .$$
    איברי האלכסון נותנים את הריבועים, והאיבר מחוץ לאלכסון מופיע <b>פעמיים</b> (פעם כ-$a_{12}$ ופעם כ-$a_{21}$).</p>
    <div class="lesson-rule">🔑 אם $v$ וקטור עצמי באורך $1$ עם ערך עצמי $\lambda$, אז $v^TAv=\lambda\,v^Tv=\lambda$. לכן ערך עצמי שלילי נותן מיד וקטור עם תבנית שלילית, וערך עצמי חיובי נותן תבנית חיובית.</div>
    <div class="lesson-ex">דוגמה: $A=\begin{pmatrix}1&3\\3&8\end{pmatrix}$ נותנת $x_1^2+6x_1x_2+8x_2^2=(x_1+3x_2)^2-x_2^2$. עבור $x=(-3,1)$ יוצא $0-1=-1<0$, ועבור $x=(1,1)$ יוצא $15>0$.</div>
    <div class="lesson-trap">⚠️ אי אפשר להסיק על הסימן של התבנית מהסימנים של איברי האלכסון בלבד. האיבר מחוץ לאלכסון יכול להפוך אותה לשלילית.</div>
    ` },
  questions: [
    { id: "C05-Q1",
      question: String.raw`מהי התבנית הריבועית $x^TAx$ של $A=\begin{pmatrix}1&3\\3&8\end{pmatrix}$?`,
      options: [
        { id: "a", value: String.raw`$x_1^2+3x_1x_2+8x_2^2$` },
        { id: "b", value: String.raw`$x_1^2+9x_1x_2+8x_2^2$` },
        { id: "c", value: String.raw`$x_1^2+8x_2^2$` },
        { id: "d", value: String.raw`$x_1^2+6x_1x_2+8x_2^2$` },
      ],
      correctId: "d",
      explanation: String.raw`$x^TAx=1\cdot x_1^2+3x_1x_2+3x_2x_1+8x_2^2=x_1^2+6x_1x_2+8x_2^2$. המקדם $3$ שוכח לספור פעמיים את האיבר מחוץ לאלכסון. המקדם $9$ נובע מכפל לא נכון ($3\cdot3$). והביטוי $x_1^2+8x_2^2$ מתעלם לגמרי מהאיברים מחוץ לאלכסון.`,
      recap: "האיבר מחוץ לאלכסון נספר פעמיים: $2a_{12}x_1x_2$." },
    { id: "C05-Q2",
      step: { type: "numeric",
        prompt: String.raw`חשבו $x^TAx$ עבור $A=\begin{pmatrix}1&3\\3&8\end{pmatrix}$ ו-$x=(-3,1)^T$.`,
        answer: -1, tol: 0,
        explain: String.raw`$x_1^2+6x_1x_2+8x_2^2=9-18+8=-1$. הערך שלילי, ולכן התבנית של $A$ אינה חיובית.` },
      recap: "מציבים בביטוי $a_{11}x_1^2+2a_{12}x_1x_2+a_{22}x_2^2$." },
    { id: "C05-Q3",
      step: { type: "numeric",
        prompt: String.raw`התבנית הריבועית $q(x)=3x_1^2-4x_1x_2+2x_2^2$ שייכת למטריצה סימטרית $A$. מהו $a_{12}$?`,
        answer: -2, tol: 0,
        explain: String.raw`המקדם של $x_1x_2$ הוא $2a_{12}=-4$, ולכן $a_{12}=-2$ (וגם $a_{21}=-2$).` },
      recap: "מחלקים את מקדם $x_1x_2$ ב-$2$ כדי לקבל $a_{12}$." },
    { id: "C05-Q4",
      question: String.raw`$B=\begin{pmatrix}1&2\\2&1\end{pmatrix}$. עבור איזה וקטור $x^TBx<0$?`,
      options: [
        { id: "a", value: String.raw`$(1,1)$` },
        { id: "b", value: String.raw`$(1,-1)$` },
        { id: "c", value: String.raw`$(2,1)$` },
        { id: "d", value: String.raw`$(1,0)$` },
      ],
      correctId: "b",
      explanation: String.raw`התבנית היא $x_1^2+4x_1x_2+x_2^2$. עבור $(1,-1)$: $1-4+1=-2<0$. עבור $(1,1)$ יוצא $6$, עבור $(2,1)$ יוצא $13$ ועבור $(1,0)$ יוצא $1$. כולם חיוביים.`,
      recap: "וקטור עצמי של ערך שלילי נותן תבנית שלילית." },
    { id: "C05-Q5",
      question: String.raw`ל-$A$ סימטרית יש ערכים עצמיים $5$ ו-$-2$. האם קיים $x$ עם $x^TAx<0$?`,
      options: [
        { id: "a", value: String.raw`לא, כי הערך העצמי $5$ גדול ומאזן את $-2$` },
        { id: "b", value: String.raw`לא, כי העקבה $3$ חיובית` },
        { id: "c", value: String.raw`כן, כל וקטור עצמי של הערך $-2$ מתאים` },
        { id: "d", value: String.raw`כן, אבל רק אם $A$ אלכסונית` },
      ],
      correctId: "c",
      explanation: String.raw`אם $Av=-2v$ אז $v^TAv=-2\|v\|^2<0$ לכל $v\ne0$. הערכים העצמיים לא "מאזנים" זה את זה: התבנית בוחנת כל כיוון בנפרד. גם העקבה החיובית לא מונעת זאת. ואין צורך באלכסוניות.`,
      recap: "ערך עצמי שלילי $\\Rightarrow$ יש וקטור עם $x^TAx<0$." },
    { id: "C05-Q6",
      question: String.raw`ל-$A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ כל איברי האלכסון חיוביים. האם $x^TAx>0$ לכל $x\ne0$?`,
      options: [
        { id: "a", value: String.raw`כן, כי איברי האלכסון חיוביים` },
        { id: "b", value: String.raw`לא, כי $x=(1,-1)$ נותן ערך שלילי` },
        { id: "c", value: String.raw`כן, כי $A$ סימטרית` },
        { id: "d", value: String.raw`לא, כי $A$ אינה סימטרית` },
      ],
      correctId: "b",
      explanation: String.raw`$x=(1,-1)$ נותן $1-4+1=-2<0$, ולכן לא. איברי האלכסון החיוביים לא מבטיחים כלום, וסימטריה לא מבטיחה חיוביות. והטענה האחרונה שגויה, כי $A$ כן סימטרית.`,
      recap: "אלכסון חיובי לא מספיק לחיוביות." },
  ],
});
