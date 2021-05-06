from itertools import combinations
from collections import Counter

orders= [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],["XYZ", "XWY", "WXA"] ]
course =[[2,3,4],[2,3,5],[2,3,4]]

def solution(orders,course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order),c)
            temp += combi
        counter = Counter(temp)
        print(counter)
        print(counter.values())
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f  in counter if counter[f] == max(counter.values())]
    return sorted(answer)


for i in range(3):
    ans = solution(orders[i],course[i])
    print(ans)