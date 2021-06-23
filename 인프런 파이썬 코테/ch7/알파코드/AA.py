import sys
sys.stdin=open("00.txt", "r")

def DFS(L,P):
    global cnt
    if L ==n :
        cnt +=1
        for j in range(P):
            print(chr(res[j]+64),end="")
        print()
    else:
        for i in range(1,27): #알파벳 갯수
            if code[L]==i:
                res[P]=i
                DFS(L+1,P+1)
            elif i>=10 and code[L] == i//10 and code[L+1] == i%10:
                res[P]=i
                DFS(L+2,P+1)

code = list(map(int,input()))
n = len(code)
code.insert(n,-1) #마지막값  2자릿수 체크할 떄 false 값나오게 하기 위해서
res=[0]*(n+3)
cnt = 0
DFS(0,0) # L , P포지션

print(cnt)