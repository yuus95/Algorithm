from itertools import combinations
from collections import Counter

orders= [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],["XYZ", "XWY", "WXA"] ]
course =[[2,3,4],[2,3,5],[2,3,4]]

def solution(orders,course):
    answer= []

    for cos in course:
        temp = []
        for order in orders:
            #"ABCFG" - > sorted(order) : ['A', 'B', 'C', 'F', 'G']
            combi = combinations(sorted(order),cos)
            temp += combi
        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            answer +=[''.join(f)  for f in counter if counter[f] == max(counter.values())]


    return sorted(answer)


for i in range(3):
    ans = solution(orders[i],course[i])
    print(ans)