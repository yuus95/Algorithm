import sys
sys.stdin = open("00.txt","r")


def DFS(L,s):
    global cnt
    if L == m :
        if sum(res) % a == 0:
            cnt+=1

    else :
        for i in range(s,n):
            res[L] = data[i]
            DFS(L+1,i+1)



n,m= map(int,input().split())
data = list(map(int,input().split()))
a = int(input())
res =[0]* m

cnt = 0
DFS(0,0)
print(cnt)
