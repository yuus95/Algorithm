import sys
from collections import deque
sys.stdin=open("00.txt","r")

n,m,b = map(int,input().split())

a = [list(map(int,list(input()))) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]


# 거리배열 d[1000][1000][11][2]
d=[[[[0]*2 for _ in range(11)] for _ in range(1000)]for _ in range(1000)]

# 첫칸에서 낮부터 시작
d[0][0][0][0] = 1

q = deque()
q.append((0,0,0,0))

while q:
    x,y,z,night = q.popleft()

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]

        if 0<= nx < n and 0 <= ny < m :
            if a[nx][ny] == 0 and d[nx][ny][z][1-night] == 0 :
                d[nx][ny][z][1 - night] = d[x][y][z][night] +1
                q.append((nx,ny,z,1-night))

            if night == 0 and z+1 <= b and a[nx][ny] == 1 and d[nx][ny][z+1][1-night] == 0 :
                d[nx][ny][z+1][1 - night] = d[x][y][z][night] +1
                q.append((nx,ny,z+1,1-night))

    if d[x][y][z][1-night] == 0 :
        d[x][y][z][1-night] += d[x][y][z][night] + 1
        q.append((x,y,z,1-night))

ans = -1
for i in range(2):
    for j in range(b+1):
        if d[n-1][m-1][i][j] == 0:
            continue
        if ans == -1 :
            ans = d[n-1][m-1][i][j]

        if ans > d[n-1][m-1][i][j]:
            ans = d[n-1][m-1][i][j]

print(ans)



