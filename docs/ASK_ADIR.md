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

## Resolved
