import sys
from collections import deque
sys.stdin=open("00.txt","r")




# 입력값
n,m,L = map(int,input().split())

# 리스트
a = [list(map(int,list(input()))) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

d = [[[0]* 11 for _ in range(1000)] for _ in range(1000)]


d[0][0][0] = 1

q = deque()
q.append((0,0,0))

while q:
    x,y,z= q.popleft()

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]

        if nx <0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 그냥 이동할 수 있는 경우
        if a[nx][ny] == 0 and d[nx][ny][z] ==0 :
            d[nx][ny][z] = d[x][y][z] +1
            q.append((nx,ny,z))

        # 벽을 부숴야될 경우, 이미 이동했던 경험이 잇으면 continue
        if z+1 <= L and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
            d[nx][ny][z+1] = d[x][y][z] + 1
            q.append((nx,ny,z+1))


ans = -1

for i in range(L+1):
    if d[n-1][m-1][i] == 0 :
        continue

    if ans == -1:
        ans = d[n-1][m-1][i]
    elif ans > d[n-1][m-1][i]:
        ans = d[n-1][m-1][i]


print(ans)


