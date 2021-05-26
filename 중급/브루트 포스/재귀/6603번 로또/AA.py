import sys
sys.stdin=open("00.txt","r")


def dfs(L,index):
    if len(L) == 6:
        for x in L :
            print(x,end=' ')
        print()
        return

    if index == len(n) :
         return

    dfs(L+[n[index]],index+1)
    dfs(L,index+1)






while True:
    n = list(map(int,input().split()))
    if n[0] == 0 :
        break
    n = n[1:]
    dfs([],0)
    print()
