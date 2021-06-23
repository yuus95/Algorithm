import sys
sys.stdin = open("00.txt","r")

def DFS(L,sum):
    global cnt
    if sum>m:
        return
    if L==n:
        if sum==m:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1,sum+(cv[L]*i))






m = int(input())
n= int(input())
cv= list()
cn=list()
for i in range(n):
    a,b=map(int,input().split())
    cv.append(a) #동전 금액 coin_value
    cn.append(b) #동전 갯수 coin_number
cnt = 0
DFS(0,0)
print(cnt)