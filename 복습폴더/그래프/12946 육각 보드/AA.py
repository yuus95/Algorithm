import sys

sys.stdin=open("00.txt","r")

sys.setrecursionlimit(1000000)
dx = [-1,0,+1,+1,0,-1]
dy = [0,-1,-1,0,+1,+1]


def dfs(x,y,c):
    global ans
    ans = max(1,ans)
    for k in range(6):
        nx,ny = x + dx[k] ,y+dy[k]
        if 0<= nx < n and 0<= ny < n :
            if color[nx][ny] == -1:
                color[nx][ny] = 1 -c
                dfs(nx,ny,1-c)
            ans = max(2,ans)
            if color[nx][ny] == c:
                ans= max(3,ans)



n = int(input())

a = [list(input()) for _ in range(n)]
color = [[-1] * n for _ in range(n)]
ans = 0


for i in range(n):
    for j in range(n):
        if a[i][j] == 'X' and color[i][j] == -1:
            dfs(i,j,0)
            color[i][j] = 0


print(ans)