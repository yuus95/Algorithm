import sys
sys.stdin=open("00.txt","r")


def DFS(L):
    if L == m :
        for x in a:
            print(x,end=' ')
        print()
        return
    else:
        for i in range(1,n+1):
            a[L] = i
            DFS(L+1)











n,m = map(int,input().split())

a=[0] * m

DFS(0)