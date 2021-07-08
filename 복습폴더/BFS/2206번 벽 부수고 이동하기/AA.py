import sys

sys.stdin=open("00.txt","r")

sys.setrecursionlimit(1500*1500)
from collections import deque


#시간초과

n,m = map(int,input().split())

a = [list(map(int,input())) for _ in range(n)]

#체크
ch= [[False] * m for _ in range(n)]


dx=[0,0,-1,1]
dy = [1,-1,0,0]

ans = 2147000000

def dfs(x,y,z,num):
    global ans
    if x == n-1 and y == m-1:
        if num != 0 :
            if num < ans :
                ans = num
        return

    if ans != 2147000000 and num >= ans :
        return

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]

        if 0<= nx < n and 0<= ny <m:
            if z == 0 and a[nx][ny] == 1 and ch[nx][ny] == False:
                ch[nx][ny]=True
                dfs(nx,ny,1,num+1)
                ch[nx][ny]=False
            if ch[nx][ny] == False and a[nx][ny] == 0 :
                ch[nx][ny] = True
                dfs(nx, ny, z, num + 1)
                ch[nx][ny] = False



dfs(0,0,0,1)
if ans != 2147000000:
    print(ans)
else:
    print(-1)



