import sys
from collections import deque
sys.stdin=open("00.txt","r")


a = [[0]*1000 for _ in range(1000)]
d = [[[[0]*2 for k in range(11)] for i in range(1000)] for j in range(1000)] # d[1000][1000][11][2]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,l = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,list(input()))))
q = deque()
d[0][0][0][0] = 1 # (0,0) 에서 시작
q.append((0,0,0,0))
while q:
    x,y,z,night = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == 0 and d[nx][ny][z][1-night] == 0: # 벽이 아닌경우
            d[nx][ny][z][1-night] = d[x][y][z][night] + 1
            q.append((nx,ny,z,1-night)) # 1이면 나이트  0 이면 낮  처음엔 낮부터시작
        if night == 0 and z+1 <= l and a[nx][ny] == 1 and d[nx][ny][z+1][1-night] == 0: # 벽이고 낮인 경우
            d[nx][ny][z+1][1-night] = d[x][y][z][night] + 1
            q.append((nx,ny,z+1,1-night))
    if d[x][y][z][1-night] == 0:
        d[x][y][z][1-night] = d[x][y][z][night] + 1
        q.append((x,y,z,1-night))
ans = -1
for j in range(2):
    for i in range(l+1):
        if d[n-1][m-1][i][j] == 0:
            continue
        if ans == -1:
            ans = d[n-1][m-1][i][j]
        elif ans > d[n-1][m-1][i][j]: # 벽을 부순횟수로 최단경로 있는지 조회
            ans = d[n-1][m-1][i][j]
print(ans)