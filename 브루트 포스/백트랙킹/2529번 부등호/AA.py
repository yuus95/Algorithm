import sys
sys.stdin=open("00.txt","r")


def ok(num):
    for i in range(n):
        if a[i] == '<':
            if num[i] > num[i+1]:
                return False
        else :
            if num[i]< num[i+1]:
                return False
        return True



def go(index,num):
    if index == n+1: #숫자를 다채웠을 경우  0-n
        if ok(num):
            ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        check[i] = True
        go(index+1,num+str(i))
        check[i] = False





n = int(input())
a = input().split() # 부등호
ans = []
check = [False] * 10
go(0,"")
ans.sort()
print(ans[-1]) # 최댓값
print(ans[0]) # 최솟값