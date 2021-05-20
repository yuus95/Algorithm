import sys
sys.stdin=open("00.txt","r")


def dfs(L,start):
    if L == m :
        for x  in d:
            print(x,end= ' ')
        print()
    else :
        for i in range(start,n+1):
            if not ch[i] :
                ch[i] =True
                d[L] = i
                dfs(L+1,i+1)
                ch[i] = 0
            else :
                continue


n,m = map(int,input().split())

ch = [False] *(n+1)
d = [0] * (m)


dfs(0,1)