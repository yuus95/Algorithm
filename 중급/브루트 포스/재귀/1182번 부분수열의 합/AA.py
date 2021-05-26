import sys
sys.stdin=open("00.txt","r")


def DFS(L,SUM):
    global ans
    if L == N :
        if SUM == S :
            ans +=1
        return

    else:
        DFS(L+1,SUM+a[L])
        DFS(L+1,SUM)


N , S = map(int,input().split())

a = list(map(int,input().split()))
ans = 0
if S == 0 :
    ans -=1
DFS(0,0)
print(ans)
