import sys
sys.stdin=open("00.txt","r")


def DFS(L):
    if L == M :
        for x in d :
            print(x,end=' ')
        print()

    else :
        for i in range(1,N+1):
            if ch[i] == 0:
                ch[i] = 1
                d[L]  = i
                DFS(L+1)
                ch[i]= 0


N,M = map(int,input().split())

d=[0] * M

ch= [0] * (N+1)

DFS(0)
