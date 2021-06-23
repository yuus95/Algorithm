import sys
sys.stdin = open("00.txt", 'r')

def DFS(L,P):
    global cnt
    if L== n:
        cnt+=1
        for j in range(P):
            print(chr(ch[j]+64),end="")
        print()
    else:
        for i in range(1,27):
            if i<10 and i == a[L]:
                ch[P] = i
                DFS(L+1,P+1)
            elif i>=10 and a[L] == i//10 and a[L+1] == i%10:
                ch[P] = i
                DFS(L+2,P+1)

cnt = 0

a = list(map(int,input()))
n = len(a)
a.insert(n,-1)
ch = [0]*(n+1)
DFS(0,0)
print(cnt)