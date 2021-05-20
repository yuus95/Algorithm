import sys
sys.stdin=open("00.txt","r")


def DFS(L,start):
    if L == m :
        for x in a :
            print(x,end=' ')
        print()
    else:
        for i in range(start,n+1):
            a[L] = i
            DFS(L+1,i)




n,m = map(int,input().split())

a =[0] * m

DFS(0,1)