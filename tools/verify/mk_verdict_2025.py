import json
def mk(code, notes, stepnotes):
    d=json.load(open(f'raw/{code}.json',encoding='utf8'))
    out={'examCode':code,'refuter':'refute-2025-b','source':'student-solution (official:false); independent solve in tools/verify/%s/refute_mine.py and refute_claims.py'%code,'items':[]}
    for i,q in enumerate(d['questions']):
        sn=stepnotes.get(i,{})
        steps=[]
        for j,s in enumerate(q.get('steps',[])):
            n=sn.get(j)
            steps.append({'step':j,'type':s['type'],'verdict':'disagree' if n and n[0] else 'agree','note':(n[1] if n else '')})
        nt=notes.get(i)
        out['items'].append({'index':i,'num':q['num'],'part':q.get('part'),
            'solution':'agree','rubricSum':'agree','pitfalls':'agree',
            'verdict':'disagree' if (nt and nt[0]) else 'agree','note':(nt[1] if nt else ''),'steps':steps})
    json.dump(out,open(f'raw/_verify_{code}.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
    dis=sum(1 for it in out['items'] for s in it['steps'] if s['verdict']=='disagree')+sum(1 for it in out['items'] if it['verdict']=='disagree')
    print(code,len(out['items']),'items',sum(len(i['steps']) for i in out['items']),'steps',dis,'flags')
mk('25A-B',{
 1:(0,'Independent SVD matches (sigma 2sqrt2,2; U,V verified numerically, orthonormal, U S V^T=A). Final answers only; correct.'),
 3:(0,'Correct. Minor: step S0/S1 ask smallest k>=0, but for x=e k=0 also works; intended general x gives 1.'),
 5:(0,'a>=1 PSD, a>1 PD, a<=-1 NSD, a<-1 ND, -1<a<1 none: matches (eigs a-1,a+1,2a).'),
 7:(0,'Proof is valid but assumes both orders finite; infinite-order case (x^m=e iff (y^-1xy)^m=e) not stated. Chain (y^-1xy)^n=y^-1x^ny rewrite confirmed correct (silent fix OK).'),
 9:(0,'79 mod 140 confirmed (brute force).'),
 11:(0,'Both inequalities correct.')},
 {11:{0:(1,'Explain cites option by position ("בבחירה הראשונה", "הבחירות האחרות"); correct here only if options are not shuffled. Reword without position.')}})
mk('25B-A',{
 0:(0,'y=0.35x+4 confirmed.'),
 7:(0,'Prefix "השלמה לפתרון שבקובץ", solutionSource solved, official false, order infinite: all correct per GATE1 ruling.'),
 11:(0,'Correct (a=-1 has no inverse; e=0).'),
 14:(0,'112 mod 165 confirmed. Final answer only; correct.'),
 13:(0,'SVD final answer verified numerically. Final answer only; correct.'),
 16:(0,'Handwritten key has (sum a_i^2)^2 on the left; transcriber fix to (sum a_i)^2 is right and matches the printed exam. Proof correct.')},
 {2:{2:(1,'findbug: two lines differ from the correct derivation (line 2 has b=y and line 3 repeats the wrong inverse with +y). Only line 2 is the real error, bugIndex 2 right, but "exactly one line changed" is not met; line 3 should keep -y.')},
  11:{1:(1,'explain says "סעיפים ב-ג" but the displayed parts are labelled א.2 and א.3 (exam part ב is the inner-product proof). Wrong part reference.')},
  16:{0:(1,'explain cites options by position and wrongly: says the FIRST choice has <u,v>=sum a_i, but the correct option is b (second). Others are a (sum a_i^2) and c (sum sqrt(a_i b_i)), not "the last two". Remove positional wording.')},
  9:{2:(0,'"הבחירות האחרות" generic, acceptable.')}})
mk('25B-B',{
 8:(0,'e(a-1)=2a confirmed (silent fix right; handwritten key has (a-1)e=a, giving 0=1 at a=1; correct is 0=2).'),
 9:(1,'Rubric and explain refer to "סעיף ב"/"סעיף ג", but in this exam "סעיף ב" is the orthonormal-basis question; displayed labels are א.2 and א.3.'),
 4:(0,'Order 4 correct. Rubric wording "מכפלה משותפת מינימלית" should be "כפולה משותפת מינימלית" (lcm). Cosmetic.'),
 13:(0,'Eigenvalues 1,1+-sqrt2 c confirmed (lambda-for-c fix right; handwriting shows -1/sqrt2<=lambda<=1/sqrt2). Ranges correct.')},
 {5:{0:(1,'explain cites options by position and out of order: says FIRST choice gives <u,v>=sum a_i with ||v||^2=n and SECOND is trivial equality, but correct is option b (second shown), option a (v=u) is the trivial one. Remove positional wording.')},
  9:{0:(1,'explain "בסעיף ב ... בסעיף ג": wrong part labels (see item note).')}})
