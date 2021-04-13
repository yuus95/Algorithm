import sys
sys.stdin=open("00.txt","r")

def DFS(L,s):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j],end=' ')
        print()
        cnt+=1
    else :
        for i in range(s,n+1):
            res[L]=i
            DFS(L+1,i+1)



n,m = map(int,input().split())
res = [0]*(n+1)
cnt = 0
DFS(0,1)
