
# 실패 내일다시풀기
from collections import Counter
from itertools import combinations


def solution(clothes):
    answer = 0
    temp = dict()

    for x,y in clothes:
        temp[x] = y

    test1 = Counter(temp.values())
    if len(test1) == 1 :
        test1 = list(test1.values())
        print(test1[0])

    return answer




clothes = [[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]]


for x in clothes:
    print(solution(x))
