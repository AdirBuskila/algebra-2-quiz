# היטל אורתוגונלי

## מה המבחן שואל
כמעט בכל מבחן: "חשבו את ההיטל של וקטור על $\operatorname{Sp}\{\dots\}$".
- **מטריצות** עם $\langle A,B\rangle=\operatorname{tr}(B^TA)$ ופרישה של שתיים או שלוש מטריצות: `24A-A-Q1b`, `24A-B-Q1b`, `24B-A-Q1b`, `24B-B-Q1c`, `23A-S-Q5b`, `26B-A-Q1b`.
- **פונקציות** ב-$C[-1,1]$: `23A-B-Q2a` (היטל של $x^2$ על $\operatorname{Sp}\{1,|x|\}$).
- **הוכחות על היטל:** `23B-B-Q5c` (עבור $P=vv^T$, הוקטור $u-Pu$ ניצב ל-$v$), `26A-A-Q3c` ו-`26A-A-Q3d` (השארית ניצבת, ופיתגורס).

## הגדרות ומשפטים
אם $u_1,\dots,u_k$ בסיס **אורתוגונלי** של $W$:
$$\operatorname{Proj}_W(v)=\sum_{i=1}^k\frac{\langle v,u_i\rangle}{\|u_i\|^2}u_i$$
בבסיס אורתונורמלי $g_i$ זה $\sum\langle v,g_i\rangle g_i$. על וקטור יחיד: $\operatorname{Proj}_a(b)=\frac{\langle b,a\rangle}{\|a\|^2}a$.

תכונות: ההיטל שייך ל-$W$; השארית $v-\operatorname{Proj}_W(v)$ ניצבת לכל $W$; $P^2=P$; פיתגורס $\|v\|^2=\|\operatorname{Proj}_Wv\|^2+\|v-\operatorname{Proj}_Wv\|^2$; ההיטל הוא הוקטור ב-$W$ הקרוב ביותר ל-$v$, והמרחק הוא $\|v-\operatorname{Proj}_Wv\|$. אם $\|v\|=1$ אז ההיטל על $\operatorname{Sp}\{v\}$ הוא $vv^T$.

## מתכון
1. **בדקו אם הוקטורים הנפרשים ניצבים** זה לזה. אם כן, עברו ישר לנוסחה.
2. אם לא: **גרהם-שמידט** ([[orthogonality]]). זהו הצעד שבו נופלים. הנוסחה הפשוטה על בסיס שאינו אורתוגונלי נותנת תשובה שגויה.
3. אם יש שלושה וקטורים והשלישי תלוי בקודמים, גרהם-שמידט נותן $0$. מוותרים עליו.
4. חשבו את המכפלות $\langle v,u_i\rangle$ והנורמות $\|u_i\|^2$ ואז סכמו.
5. **בדיקה:** $\langle v-\operatorname{Proj},u_i\rangle=0$ לכל $i$.

פונקציות על קטע סימטרי $[-a,a]$: מכפלת זוגית באי-זוגית נותנת אינטגרל $0$, ומכפלת זוגית בזוגית שווה פעמיים האינטגרל על $[0,a]$. עם $|x|$ מפצלים ל-$[-a,0]$ ו-$[0,a]$.

## מלכודות
> 🪤 לא לוודא אורתוגונליות לפני שימוש בנוסחה.

> 🪤 $\operatorname{tr}(B^TA)$ הוא סכום מכפלות רכיבים, לא מכפלת מטריצות.

> 🪤 חילוק ב-$\|u_i\|$ במקום ב-$\|u_i\|^2$ כשהבסיס אינו מנורמל.

> 🪤 מקדם ההיטל אינו סקלר אחד: לכל וקטור בבסיס יש מקדם משלו.

## דוגמאות פתורות
**מטריצות.** $W=\operatorname{Sp}\left\{\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}1&3\\1&1\end{pmatrix}\right\}$ ו-$V=\begin{pmatrix}2&0\\3&1\end{pmatrix}$. גרהם-שמידט נותן $B_1=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ ו-$B_2=\begin{pmatrix}-1&1\\1&1\end{pmatrix}$ עם $\|B_1\|^2=2$, $\|B_2\|^2=4$. אז $\langle V,B_1\rangle=2$ ו-$\langle V,B_2\rangle=2$, ולכן
$$\operatorname{Proj}_W(V)=1\cdot B_1+\tfrac12B_2=\begin{pmatrix}\tfrac12&\tfrac32\\\tfrac12&\tfrac12\end{pmatrix}.$$
בדיקה: השארית $\begin{pmatrix}\tfrac32&-\tfrac32\\\tfrac52&\tfrac12\end{pmatrix}$ ניצבת ל-$B_1$ ול-$B_2$. פיתגורס: $\|V\|^2=14$ ואילו $\|\operatorname{Proj}\|^2=3$ ו-$\|\text{res}\|^2=11$.

**פונקציות.** ב-$C[-1,1]$ עם $\int_{-1}^1fg$: היטל של $x^2$ על $\operatorname{Sp}\{1,x\}$. הוקטורים ניצבים ($x$ אי-זוגית). $\langle x^2,1\rangle=\frac23$, $\|1\|^2=2$, $\langle x^2,x\rangle=0$. ההיטל הוא $\frac13$.

אם $W=\operatorname{Sp}\{1,|x|\}$ אז $1$ ו-$|x|$ אינם ניצבים ($\int_{-1}^1|x|=1$), וגרהם-שמידט נותן $|x|-\frac12$ עם נורמה בריבוע $\frac16$. כך מקבלים את ההיטל של $x^2$ על $W$, שהוא $|x|-\frac16$ (`23A-B-Q2a`).
