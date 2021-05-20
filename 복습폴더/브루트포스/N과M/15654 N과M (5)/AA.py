import sys
sys.stdin=open("00.txt","r")

n,m = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

d=  [0] * m
ch = [0] * n

def DFS(L):
    if L == m :
        for x in d :
            print(x,end= ' ')
        print()
        return
    else:
        for i in range(len(a)):
            if ch[i] == 0 :
                ch[i] = 1
                d[L] = a[i]
                DFS(L+1)
                ch[i]= 0
            else:
                continue

DFS(0)