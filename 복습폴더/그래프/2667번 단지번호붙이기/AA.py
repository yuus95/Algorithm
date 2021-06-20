import sys

sys.stdin=open("00.txt","r")

from collections import deque

def dfs(x,y,cnt):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx < n and 0<= ny <n:
            if d[nx][ny] == '1' and dist[nx][ny] == -1:
                dist[nx][ny] = cnt
                dfs(nx,ny,cnt)


dx=[0,0,-1,1]
dy=[1,-1,0,0]

cnt = 0
n = int(input())

d= [list(input()) for _ in range(n)]

ch = [[False] * n for _ in range(n)]

dist = [[-1] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if d[i][j] == '1' and dist[i][j] == -1:
            cnt+=1
            dist[i][j] = cnt
            dfs(i,j,cnt)

print(cnt)

res= [0] * (cnt+1)

for k in range(1,cnt+1):
    temp = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] == k:
                temp+=1
    res[k] =temp
res.sort()
for k in range(1,cnt+1):
    print(res[k])
