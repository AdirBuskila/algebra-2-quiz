# דף נוסחאות ומשפטים לכל הקורס

דף חוזר מרוכז, בסדר ובסימונים של דף הנוסחאות של הקורס. בכל סעיף הפניה לפרק המלא.

> ⚠️ **ההסכמה בקורס:** "מוגדרת חיובית" פירושה $\ge0$, ו"מוגדרת חיובית לחלוטין" פירושה $>0$ (וכך גם בשלילי). מטריצה חייבת להיות סימטרית כדי להיות מוגדרת. ([[pos_def]])

## מכפלה פנימית ונורמה ([[inner_product]], [[cauchy_schwarz]])
- אקסיומות: סימטריה, לינאריות, $\langle u,u\rangle\ge0$ עם שוויון רק ל-$u=0$.
- $\mathbb{R}^n$: $\sum u_kv_k$. $C[a,b]$: $\int_a^bfg$ (עם משקל $w>0$ אפשרי). $M_n$: $\operatorname{tr}(B^TA)=\sum a_{ij}b_{ij}$.
- $\|u\pm v\|^2=\|u\|^2\pm2\langle u,v\rangle+\|v\|^2$. מקבילית: $\|u+v\|^2+\|u-v\|^2=2\|u\|^2+2\|v\|^2$. פולריזציה: $\langle u,v\rangle=\frac14(\|u+v\|^2-\|u-v\|^2)$.
- קושי-שוורץ: $|\langle u,v\rangle|\le\|u\|\|v\|$, שוויון אם ורק אם תלויים. משולש: $\|u+v\|\le\|u\|+\|v\|$. $\cos\theta=\frac{\langle u,v\rangle}{\|u\|\|v\|}$.

## אורתוגונליות, גרהם-שמידט, היטל ([[orthogonality]], [[projection]])
$$u_1=v_1,\quad u_m=v_m-\sum_{i<m}\frac{\langle v_m,u_i\rangle}{\|u_i\|^2}u_i,\qquad\operatorname{Proj}_W(v)=\sum_i\frac{\langle v,u_i\rangle}{\|u_i\|^2}u_i$$
- ההיטל נוסחה רק על בסיס **אורתוגונלי**. השארית ניצבת ל-$W$. $\|v\|^2=\|\operatorname{Proj}v\|^2+\|v-\operatorname{Proj}v\|^2$.
- בבסיס אורתונורמלי: $v=\sum\langle v,g_i\rangle g_i$.
- פרסבל (בסיס): $\|v\|^2=\sum\langle v,g_i\rangle^2$. בסל (מערכת): $\sum\langle v,g_i\rangle^2\le\|v\|^2$. ([[parseval_bessel]])
- $Q$ אורתוגונלית: $Q^TQ=I$, שומרת מכפלה ונורמה, $\det=\pm1$. אם $\|u\|=1$ אז $uu^T$ היא היטל, ו-$\sum u_iu_i^T=I$ לבסיס אורתונורמלי.

## ריבועים פחותים ([[least_squares]])
$$A^TA\hat x=A^T\vec b,\qquad\hat x=(A^TA)^{-1}A^T\vec b$$
הנוסחה השנייה כשעמודות $A$ בלתי תלויות.
$A\hat x=\operatorname{Proj}_{\operatorname{Col}A}\vec b$. ישר: עמודות $x_i$ ו-$1$, $A^TA=\begin{pmatrix}\sum x^2&\sum x\\\sum x&k\end{pmatrix}$, $A^T\vec b=\binom{\sum xy}{\sum y}$.

## לכסון אורתוגונלי ומוגדרות ([[orthodiag]], [[pos_def]])
- סימטרית אם ורק אם ניתנת ללכסון אורתוגונלי: $A=QDQ^T$. ערכים עצמיים ממשיים. מערכים עצמיים שונים הווקטורים ניצבים. במרחב עצמי מרובה: גרהם-שמידט.
- חיובית לחלוטין: $\langle Av,v\rangle>0$ ($v\ne0$), כל $\lambda>0$, כל המינורים המובילים $\Delta_k>0$ (סילבסטר). חיובית: $\ge0$, כל $\lambda\ge0$.
- $\langle A^2v,v\rangle=\|Av\|^2$. $B^TAB$ חיובית כש-$A$ חיובית; לחלוטין אם $B$ הפיכה. ערכי $cI-A$: $c-\lambda$. ערכי $A^{-1}$: $1/\lambda$.

## QR ו-SVD ([[qr]], [[svd]])
- $A=QR$: $Q$ מגרהם-שמידט על העמודות, $R=Q^TA$ משולשת עליונה, $r_{ii}=\|u_i\|$.
- $A=USV^T$, $S$ אלכסונית $m\times n$ עם $\sigma_i=\sqrt{\lambda_i(A^TA)}$ בסדר יורד. $V$: וקטורים עצמיים של $A^TA$. $u_i=\frac1{\sigma_i}Av_i$ ל-$\sigma_i\ne0$, ואת השאר משלימים. דרגה $=$ מספר ה-$\sigma_i\ne0$.

## חבורות ([[groups]])
- חבורה: סגירות, אסוציאטיביות, ניטרלי, הופכי. אבלית: גם קומוטטיבית.
- תת-חבורה: $e\in H$, סגורה לפעולה ולהופכי. $\langle a\rangle=\{a^n\}$, $|\langle a\rangle|=o(a)$.
- לגרנז': $|H|\mid|G|$, ולכן $o(x)\mid|G|$. $(xy)^{-1}=y^{-1}x^{-1}$.
- מכפלה רכיב-רכיב: $o((a,b))=\operatorname{lcm}(o(a),o(b))$. $|\mathbb{Z}_n^*|=\varphi(n)$, $\varphi(p^k)=p^k-p^{k-1}$.
- פרמה: $a^{p-1}\equiv1\pmod p$, כלומר $a^{-1}\equiv a^{p-2}$.

## משוואות מודולריות ומשפט השאריות הסיני ([[crt]])
- $ax\equiv b\pmod n$ פתירה אם ורק אם $\gcd(a,n)\mid b$. עם $\gcd=1$: $x\equiv a^{-1}b$.
- CRT לזרים בזוגות: $x=\sum a_iM_ix_i\pmod M$ עם $M_i=M/m_i$ ו-$M_ix_i\equiv1\pmod{m_i}$.

## איזה כלי מתי
| השאלה | הכלי |
|---|---|
| הוכחת אי-שוויון עם סכום או אינטגרל | קושי-שוורץ, בחירת וקטורים |
| היטל על $\operatorname{Sp}$ | גרהם-שמידט אם צריך, ואז הנוסחה |
| ישר קרוב ביותר לנקודות | משוואות נורמל $A^TA\hat x=A^T\vec b$ |
| לכסון אורתוגונלי | ערכים עצמיים, גרהם-שמידט בתוך מרחב עצמי, נרמול |
| "עבור אילו פרמטר מוגדרת" | סימטריה, ערכים עצמיים, טבלת סימנים |
| הוכחה על מוגדרת | $\langle Av,v\rangle$ ו-$\|Av\|^2$ |
| SVD | $A^TA$ או $AA^T$ (הקטנה), $u_i=Av_i/\sigma_i$ |
| מערכת קונגרואנציות | צמצום מקדמים, CRT, בדיקה |
| חבורה | ארבע אקסיומות, ספירה לסדר, חזקות לסדר איבר |
