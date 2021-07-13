from itertools import combinations

from collections import defaultdict


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info,querie):
    answer = []
    db={}

    # 문자열 하나에 대한 만들수 있는  모든 조합 만들어서 DB {}에 넣기
    for i in info:
        temp=i.split()
        conditions = temp[:-1] # 조건
        score = int(temp[-1]) # 점수
        for n in range(5): # 조건들에 대해 조합을 이용
            combi = list(combinations(range(4),n)) # 번호 조합 만들기
           #문자열과 '-' 로 만들 수 있는 조합 만들기
            for c in combi:
                t_c = conditions.copy()
                for v in c:
                    t_c[v]='-'
                changed_t_c = '/'.join(t_c)
                print(changed_t_c)
                if changed_t_c in db:
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values(): #딕셔너리 내 모든 값 정렬
        value.sort()


    for q  in query: #query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score=int(qry[-1])


        if qry_cnd in db:
            data = db[qry_cnd]

            if len(data)>0:
                start,end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start+end)//2] > qry_score:
                        end=(start+end)//2
                    else:
                        start = (start+end)//2 +1
                answer.append(len(data)-start)
        else :
            answer.append(0)
    return answer


ans = solution(info,query)

print(ans)