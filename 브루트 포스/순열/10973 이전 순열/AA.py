import sys
sys.stdin=open("00.txt","r")

# 내일 다시풀기


def next_permutation(a):
    i = len(a)-1

    while i > 0 and a[i-1] <= a[i] : # 이전 순열 찾기
        i -= 1
    if i <= 0 : # 이전순열이 없다
        return False
    j = len(a)-1

    while a[j] >= a[i-1]: #a[j] 보다는 작지만 제일 큰 수  찾기
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a) -1

    while i < j :
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = list(map(int,input().split()))
if next_permutation(a):
    print(' '.join(map(str,a)))
else :
    print(-1)

