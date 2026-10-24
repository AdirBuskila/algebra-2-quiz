import json,sys
d=json.load(open(sys.argv[1],encoding='utf8'))
for i,q in enumerate(d['questions']):
    print('=== Q',i,q['num'],q.get('part'),q['kind'],q.get('solutionSource'),q.get('official'))
    print('SOL:',q.get('solution'))
    print('MCQ:',{k:q[k] for k in q if k in('options','correctId','answer','explain','key')})
    print('RUB:',[(r['text'],r['points']) for r in q.get('rubric',[])])
    print('PIT:',q.get('pitfalls'))
    for j,s in enumerate(q.get('steps',[])):
        s=dict(s)
        t=s.pop('type');print(f'  S{j} {t}:',json.dumps(s,ensure_ascii=False))
