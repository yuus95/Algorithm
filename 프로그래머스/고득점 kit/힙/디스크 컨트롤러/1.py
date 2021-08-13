from itertools import combinations

# 순열풀이 실패

def next_permutation(a):
    i = len(a)-1

    while i > 0 and a[i-1] >= a[i] : #다음순열 찾기
        i -= 1
    if i<= 0 : # 다음순열이 없다
        return False
    j = len(a)-1

    while a[j] <= a[i-1]: #a[i] 보다는 크지만 제일 작은수 찾기
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a) -1

    while i < j :
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True





def solution(jobs):
    answer = 2147000000
    data = []
    n = len(jobs)

    test = list(range(n))
    while True:
        temp = 0
        sum = 0
        for x in test:
            sum += jobs[x][1]
            temp += sum - jobs[x][0]
        if  answer > temp//n:
            answer= temp//n

        if not next_permutation(test):
            break

    return answer



print(solution([[0, 3], [1, 9], [2, 6]]))