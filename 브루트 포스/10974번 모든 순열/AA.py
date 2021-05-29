import sys
sys.stdin=open("00.txt","r")


def go(L):
    if L == n :
        for x in d :
            print(x,end=' ')
        print()
        return
    if L > n :
        return

    else :
        for i in range(1,n+1):
            if ch[i] == False:
                ch[i] = True
                d[L] = i
                go(L+1)
                ch[i]= False








n = int(input())
d = [0] * n
ch= [False] * (n+1)
go(0)