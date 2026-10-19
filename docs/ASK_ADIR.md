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
- Status: hold

### 23B-A Q5a - official final answer wrong
- Path: sitting 23B-A official solution (compilation)
- Page: 10 of the sitting (compilation p.190)
- Question: Q5a asks for the projection of (0 a; b 0) onto Sp{(-1 1; 1 0), (1 0; 2 1)} with tr(B^T A). The official final answer is (a+b)/3 (-1 1; 1 0) + (5b-3a)/51 (4 -1; 5 3), but <(0 a; b 0),(4 -1; 5 3)> = 5b-a, not 5b-3a. Checked with sympy: the correct projection is [[-7a+b, 6a+4b],[4a+14b, -a+5b]]/17.
- Needed: confirm shipping the corrected answer as a non-official solution, or keep held.
- Status: hold

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
- Status: hold

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
- Status: logged

### 25A-C - no key; Q2b.2 flawed as printed
- Page: 2 of the sitting (compilation p.274)
- All 15 items held as no-key. Q2b.2 asks to prove B^T A B positive definite for any B in M_n(R); false for singular B (only semidefinite).
- Needed: decide whether the solver states "B invertible" as an assumption.
- Status: hold

## Resolved
