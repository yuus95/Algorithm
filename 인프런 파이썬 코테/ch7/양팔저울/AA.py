import sys
sys.stdin= open("00.txt","r")

def DFS(L):
    global cnt
    if any(L == D[k] for k in range(n)):
        cnt+=1
    else :
        for i in range(n):
            for j in range(n):
                if L+D[j] == D[i]:
                    cnt+=1

    if L == n:
        print(sum(D) - cnt)
        sys.exit(0)
    else :
            DFS(L+1)


n = int(input())
cnt = 0
D = list(map(int,input().split()))

DFS(1)
