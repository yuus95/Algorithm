import sys
sys.stdin=open("00.txt","r")


def DFS(L):
    if L == m :
        for x in d_list:
            print(x , end=' ')
        print()
    else:
        for i in range(1,n+1):
            # if ch[i] == 1 :
            #     continue
                ch[i] = 1
                d_list[L] = i
                DFS(L+1)
                ch[i] = 0


n ,m =map(int,input().split())

d_list = [0] * m

ch = [0] *(n+1)

DFS(0)




