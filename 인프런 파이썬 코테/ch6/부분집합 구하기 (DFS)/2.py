import sys
sys.stdin = open("00.txt","r")

def DFS(x):
    if x>=n+1:
        for i in range(1,n+1):
            if check[i] ==1 :
                print(i,end=' ')
        print()

    else:
        check[x]=1
        DFS(x+1)
        check[x]=0
        DFS(x+1)



n = int(input())
check=[0]*(n+1)

DFS(1)