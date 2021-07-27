import sys
from collections import deque
sys.stdin=open("00.txt","r")


a = [[0]*1000 for _ in range(1000)]

# 거리체크 배열 d[1000][1000][11][2]  행, 열, 벽 ,낮과밤
d = [[[[0]*2 for _ in range(11)] for _ in range(1000)] for _ in range(1000)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,m,k = map(int,input().split())

a = [list(map(int,list(input()))) for _ in range(n)]

q = deque()

# 낮부터 시작
d[0][0][0][0] = 1

q.append((0,0,0,0))

while q:
    x,y,z,night = q.popleft()

    for L in range(4):
        nx,ny = x+dx[L],y+dy[L]

        if nx < 0 or nx >= n or ny < 0 or ny >= m :
            continue

        # 벽이 아닐 경우
        if a[nx][ny] == 0 and d[nx][ny][z][1-night] == 0 :
            d[nx][ny][z][1-night] = d[x][y][z][night] +1
            q.append((nx,ny,z,1-night)) # 1이면 나이트  0 이면 낮  처음엔 낮부터시작

        # 다음칸이 벽이고, 현재가 낯일 경우
        if night == 0 and z+1 <= k and a[nx][ny] == 1 and d[nx][ny][z+1][1-night] == 0 :
            d[nx][ny][z+1][1-night] = d[x][y][z][night] + 1
            q.append((nx,ny,z+1,1-night))

    # 다음칸이 벽이고 현재 밤일 경우
    if d[x][y][z][1-night] == 0 :
        d[x][y][z][1-night] = d[x][y][z][night] +1
        q.append((x,y,z,1-night))


ans = -1
for j in range(2):
    for i in range(k+1):
        if d[n-1][m-1][i][j] ==0 :
            continue
        if ans == -1:
            ans = d[n-1][m-1][i][j]
        elif ans > d[n-1][m-1][i][j]:
            ans = d[n-1][m-1][i][j]

print(ans)