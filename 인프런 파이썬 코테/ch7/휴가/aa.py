import sys
sys.stdin= open("00.txt","r")

def DFS(L,sum):
    global res
    if L>n+1:
        return

    if L==n+1:
        if sum > res:
            res = sum
    else:
        DFS(L+T[L],sum+AC[L])
        DFS(L+1,sum)



res = -2147000000
n= int(input())
T= list()
AC = list()

for _ in range(n):
    a,b =map(int,input().split())

    T.append(a)
    AC.append(b)

T.insert(0,0)
AC.insert(0,0)

DFS(1,0)
print(res)