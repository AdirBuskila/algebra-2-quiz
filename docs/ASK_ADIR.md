# ASK_ADIR - algebra-2

Open questions for Adir. One entry per item; the orchestrator moves it to Resolved when answered.

## Open

<!-- Entry format:
### <exam code> Q<number> - <short title>
- Path: <absolute file path>
- Page: <page number>
- Question: <what is unclear or missing>
- Needed: <what Adir must provide or decide>
- Status: hold
-->

### 26A-A Q4c - official answer wrong
- Path: sitting 26A-A official solution
- Page: 10
- Question: Q4c asks for all (a,b) commuting with every (x,y). The official answer says "a even and x even", but x is the free variable and b=0 is missing. Checked by brute force and algebra: the correct set is (a,0) with a even.
- Needed: confirm shipping the corrected answer (a even, b=0) as a non-official solution, or keep held.
- Status: resolved by solver, pending refuter. Re-derived (tools/verify/26A-A/solve_Q4c.py): the official answer is truly wrong. Shipped under the typo ruling as solutionSource "solved", official false, prefix "הפתרון הרשמי עם תיקון".

### 23B-A Q5a - official final answer wrong
- Path: sitting 23B-A official solution (compilation)
- Page: 10 of the sitting (compilation p.190)
- Question: Q5a asks for the projection of (0 a; b 0) onto Sp{(-1 1; 1 0), (1 0; 2 1)} with tr(B^T A). The official final answer is (a+b)/3 (-1 1; 1 0) + (5b-3a)/51 (4 -1; 5 3), but <(0 a; b 0),(4 -1; 5 3)> = 5b-a, not 5b-3a. Checked with sympy: the correct projection is [[-7a+b, 6a+4b],[4a+14b, -a+5b]]/17.
- Needed: confirm shipping the corrected answer as a non-official solution, or keep held.
- Status: resolved by solver, pending refuter. Re-derived (tools/verify/23B-A/solve_Q5a.py): 5b-a is right, the printed 5b-3a is wrong. Shipped under the typo ruling as solutionSource "solved", official false, prefix "הפתרון הרשמי עם תיקון".

### 26B-A (whole sitting) - no answer source
- Path: sitting 26B-A exam, 2 pages (no solution exists)
- Page: 1-2
- Question: all 15 items are held "no-key". A 17-page scan in the folder is a handwritten student solution of this sitting with a student grade-report page (personal data); it is not a distinct sitting and was not used.
- Needed: route to the solver and refuter, or confirm using the scan for the parts that earned full marks.
- Status: hold

### 26A-B (Q1c, Q2d, Q4a-c, Q5a) - no answer source
- Path: sitting 26A-B exam; the only solution is a partial handwritten student solution
- Page: 1-2 (exam)
- Question: 9 items are shipped from the student solution (official false, recomputed with sympy); Q1c, Q2.4, Q4a, Q4b, Q4c and Q5a have no solution and are held no-key. Student slip fixed silently: Q5b last coordinate of u (1/sqrt2 for 1/sqrt n).
- Needed: route the 6 held items to the solver.
- Status: resolved by solver, pending refuter. All 6 solved (solutionSource "solved", official false), sympy checks in tools/verify/26A-B/solve_held.py. Answers: Q1c x = (4/3, -1/3); Q2d yes, x = 2; Q4b |G| = 100; Q4c o(X) = 5; Q5a x = 116 (mod 120).

### 25B-A Q3b - official solution omits the order of G
- Path: sitting 25B-A handwritten solution (the "lecturers' solution" file in the folder belongs to a different exam and was not used)
- Page: 7-8 of the solution
- Question: Q3b asks to prove G is a group AND to find its order; the solution proves the group axioms only. The order (infinite) was added, so the item ships as solved, official false, with the prefix "הפתרון הרשמי עם השלמה". Slips fixed silently: Q6c first line prints (sum a_i^2)^2 for (sum a_i)^2.
- Needed: confirm the completion, or keep it held.
- Status: shipped, to confirm

### 25B-B Q3a.3 / Q5a - slips in intermediate lines
- Path: sitting 25B-B handwritten solution
- Page: 5 and 8 of the solution
- Question: Q3a.3 prints "(a-1)e = a" where the equation is e(a-1) = 2a (at a=1: 0 = 2, printed 0 = 1); the conclusion is unchanged. Q5a writes the range with lambda instead of c. Q1a gives decimals only; exact 37/59 and 99/59 added. All fixed silently in the transcription; no final answer is wrong.
- Needed: nothing, FYI.
- Status: resolved in transcription

### 24B-B Q5a - official final answer wrong (U, third column)
- Path: sitting 24B-B official solution (compilation)
- Page: 7 of the sitting (compilation p.240)
- Question: the SVD answer prints the third column of U as (-2/sqrt3, 4/sqrt3, sqrt5/3), not a unit vector and not orthogonal to the others. Checked with sympy: the correct column is (-2,4,5)/(3 sqrt5); S and V are right. Q1b.1 also says "for W" (space is U) and Q3a prints c in place of 0 in the determinant; fixed silently.
- Needed: nothing blocking. Shipped as solutionSource "solved", official false, prefix "הפתרון הרשמי עם תיקון". Confirm or revert.
- Status: shipped with correction

### 25A-A, 25A-B - handwritten student solutions
- Page: whole sittings
- 25A-A has no solution for Q4b (CRT) and Q5b: held as no-key for the solver. Other items ship as student-solution, official false. 25A-A Q3b (=>) used "cos = 1 so the angle is 0"; a direct argument was added as a labelled remark. 25A-B Q4a.1 had equalities in the wrong order (rewritten). 25A-B Q4b is (10%) on the sheet, (8%) in the solution copy.
- Status: logged. 25A-A Q4b and Q5b: resolved by solver, pending refuter (solutionSource "solved", official false, sympy checks in tools/verify/25A-A/solve_Q4b_Q5b.py; Q4b x = 87 (mod 385), Q5b via Cauchy-Schwarz).

### 23A-A Q5a - no key (SVD)
- Page: 2 of the exam; the official solution gives only a link to an online SVD calculator.
- Status: resolved by solver, pending refuter. Solved (solutionSource "solved", official false), sympy check in tools/verify/23A-A/solve_Q5a.py: singular values 2, sqrt2.

### 25A-C - no key; Q2b.2 flawed as printed
- Page: 2 of the sitting (compilation p.274)
- All 15 items held as no-key. Q2b.2 asks to prove B^T A B positive definite for any B in M_n(R); false for singular B (only semidefinite).
- Needed: decide whether the solver states "B invertible" as an assumption.
- Status: resolved by solver, pending refuter. All 15 solved (solutionSource "solved", official false). Q2b.2 is not flawed in the course's terms ("מוגדרת חיובית" = v^T M v >= 0, "לחלוטין" = strict, see Q4a), so it holds for any B; a visible "הערה:" covers the strict reading (needs B invertible).

### 23A-S - no key; student Q1a wrong
- Page: compilation pp.149-150 (exam); the only solution is a partial student scan (Q1a, Q3b).
- 8 items were held: Q1a (the student's answer "PD for a >= 1+sqrt3" is wrong: the matrix is not symmetric unless a=1, and at a=1 it is indefinite) and 7 with no key. Q3b ships as the student solution.
- Status: resolved by solver, pending refuter. All 8 solved (solutionSource "solved", official false), sympy checks in tools/verify/23A-S/solve_23AS.py. Q1a answer: no such a (course definition is for symmetric matrices). A visible "הערה:" gives the quadratic-form reading (symmetric part: PD iff a>3, ND iff a<-1).

### 24A-C Q3a, Q3b, Q5a, Q5b - no key
- Page: 7 of the solution file (exam page 2)
- The student solution does not cover Q3 or Q5; these 4 items were held no-key. The other 8 ship as student solutions.
- Status: resolved by solver, pending refuter. All 4 solved (solutionSource "solved", official false), sympy checks in tools/verify/24A-C/solve_24AC.py.

## Resolved
