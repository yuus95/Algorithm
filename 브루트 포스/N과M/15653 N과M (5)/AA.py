import sys
sys.stdin=open("00.txt","r")


def DFS(L):
    if L == m :
        for x in d_list:
            print(x , end=' ')
        print()
    else:
        for i in n_list:
            if ch[i] == 1 :
                continue
            else:
                ch[i] = 1
                d_list[L] = i
                DFS(L+1)
                ch[i] = 0


n ,m =map(int,input().split())
n_list = list(map(int,input().split()))
n_list.sort()

d_list = [0] * m

ch = [0] *(100001)

DFS(0)




