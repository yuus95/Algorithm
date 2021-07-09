import sys

sys.stdin=open("00.txt","r")

sys.setrecursionlimit(1500*1500)
from collections import deque


n, m = map(int,input().split())

a = [list(map(int,input())) for _ in range(n)]

d = [[[0] *2  for j in range(m)] for i in range(n) ]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

q = deque()
q.append((0,0,0))
d[0][0][0] = 1

while q:
    x,y,z = q.popleft()

    for k in range(4):
        nx,ny = x+ dx[k],y + dy[k]

        if 0<= nx < n and 0<= ny < m :
            if a[nx][ny] == 0 and d[nx][ny][z] == 0:
                d[nx][ny][z] = d[x][y][z] + 1
                q.append((nx, ny, z))

            if z == 0 and a[nx][ny] == 1 and d[nx][ny][1] == 0 :
                d[nx][ny][1] = d[x][y][z] +1
                q.append((nx,ny,z+1))



if d[n-1][m-1][0] != 0 and d[n-1][m-1][1] != 0:
    print(min(d[n-1][m-1][0],d[n-1][m-1][1]))
elif d[n-1][m-1][0] != 0 :
    print(d[n-1][m-1][0])

elif d[n-1][m-1][1] != 0 :
    print(d[n-1][m-1][1])

else :
    print(-1)