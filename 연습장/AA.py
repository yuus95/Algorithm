import sys
from itertools import permutations
sys.stdin=open("00.txt","r")

n , m = map(int,input().split())


d =[0]* m
check= [0] *(n+1)


def dfs(num):
    global check

    check[num] = True
    d.append(num)
    for x in a[num] :
        if check[x] == False:
            dfs(num)


dfs(k)