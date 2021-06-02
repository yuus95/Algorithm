import sys

sys.stdin=open("00.txt","r")

def next_permutation(a):
    i = len(a)-1

    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0 :
        return False

    j = len(a) - 1

    while a[j] < a[i-1]:
        j-=1

    a[i-1] ,a[j] = a[j] ,a[i-1]

    j = len(a)-1

    while i < j :
        a[i],a[j] = a[j],a[i]
        i+=1
        j -=1

    return True

def prev_permutation(a):
    i = len(a)-1

    while i > 0 and a[i-1] <= a[i] :
        i -= 1
    j = len(a)-1

    while a[j] > a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j] ,a[i-1]

    j = len(max_ans) - 1

    while i < j :
        a[i],a[j] = a[j] , a[i]

        i +=1
        j -=1
    return True


def check(min_ans,a):
    for i in range(1,n+1):
        if a[i-1] == '<' and min_ans[i-1] > min_ans[i] :
            return 0
        if a[i - 1] == '>' and min_ans[i - 1] < min_ans[i]:
            return 0
    return True



n = int(input())
a = list(input().split())

#순열 배열
max_ans = [i for i in range(9,9-n-1,-1)]
min_ans = [ i for i in range(n+1)]



#최솟값
while True:
    if check(min_ans, a):
        break

    if not next_permutation(min_ans):# min_ans는 배열이라 참조객체이다 그래서 함수에서 객체를 변경시키면 참조객체 자체가 변경된다.
        break

#최댓값
while True:
    if check(max_ans,a):
        break
    if not prev_permutation(max_ans):
        break


print(''.join(map(str,max_ans)))
print(''.join(map(str,min_ans)))

