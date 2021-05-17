import sys
from itertools import permutations
sys.stdin=open("00.txt","r")

n , m = map(int,input().split())


d =[0]* m
check= [0] *(n+1)


def dfs(L):
    if L == m :
        for x in d:
            print(x,end= ' ')
        print()
        return

    else:
        for i in range(1,n+1):
            if check[i] == 0:
                check[i] = 1
                d[L] = i
                dfs(L+1)
                check[i]=0


dfs(0)