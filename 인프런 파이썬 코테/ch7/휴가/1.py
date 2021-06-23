import sys
sys.stdin=open("00.txt","r")

def DFS(L,time,sum):
    global res
    if time > n-1:
        return
    if L == n:
        if sum> res :
           res = sum

    else :
        DFS(ch[a[L]-1],time+a[L],sum+b[L])
        DFS(L+1,time,sum)



n = int(input())


res = -2147000000
ch=[]
a=[]
b=[]

for i in range(n):
    x,y = map(int,input().split())
    a.append(x) # 걸리는 일수
    b.append(y) # 상금
    ch.append(i)
DFS(0,0,0,)

print(res)