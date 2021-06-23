import sys
sys.stdin=open("00.txt", "r")
def DFS(L,sum,time):
    global result
    if time > m:
        return

    if L == n :
        if sum > result :
            result = sum
    else:

                DFS(L+1,sum+res[L][0],time+res[L][1])
                DFS(L+1,sum,time)

n,m = map(int,input().split())

result = -2147000000
res = []
ch=[0]*(n+1)

for _ in range(n):
    a,b= map(int,input().split())
    res.append((a,b))
DFS(0,0,0)
print(result)
