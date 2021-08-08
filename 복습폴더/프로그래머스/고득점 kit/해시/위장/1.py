
from collections import Counter
from itertools import combinations


def solution(clothes):
    answer = 1
    temp = {}


    # temp 딕셔너리에 key값으로 옷종류를 넣고  value값으로 옷value 넣어주기
    for value in clothes:
        if value[1] not in temp:
            temp[value[1]] = [value[0]]
        else:
            temp[value[1]].append(value[0])


    # 의상종류를 안입을 수 있는 확률 +1
    for key in temp:
        answer*= (len(temp[key])+1)

    # 의상종류 하나는 반드시 입어야 하므로 -1
    return answer-1





clothes = [[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]]


for x in clothes:
    print(solution(x))
