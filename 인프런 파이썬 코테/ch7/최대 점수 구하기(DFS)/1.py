import sys
sys.stdin= open("00.txt","r")

def DFS(L,time,sum):
    global res
    if time>m:
        return
    if L==n:
        if sum > res :
            res = sum

    else:
        DFS(L+1,time+b_list[L],sum+a_list[L])
        DFS(L+1,time,sum)



n,m = map(int,input().split())
res = -2147000000
a_list=[]
b_list=[]


for _ in range(n):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)


DFS(0,0,0)
print(res)