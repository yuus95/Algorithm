import sys
sys.stdin = open("00.txt","r")

def DFS(L,sum,tsum):
    global  res
    if sum+(total-tsum) <res  :
        return
    if sum > wei:
        return
    if L == n:
       if sum >res:
           res = sum
    else:
        DFS(L+1,sum+data_list[L],tsum+data_list[L])
        DFS(L + 1, sum , tsum + data_list[L])


wei ,n = map(int,input().split())
data_list = [0]*n
res = -2147000000
for i in range(n):
    data_list[i]=int(input())


total = sum(data_list)

DFS(0,0,0)
print(res)

