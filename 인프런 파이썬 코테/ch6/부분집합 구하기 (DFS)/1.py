import sys
sys.stdin = open("00.txt","r")

def DFS(L):
    global cnt
    if L== m:
        for j in range(m):
            print(res[j],end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i] == 0 :
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0




n,m= map(int,input().split())
cnt = 0
ch=[0]*(n+1)
res=[0]*m

DFS(0)
