import sys
from itertools import permutations
sys.stdin=open("00.txt","r")

from collections import deque


n , m = map(int,input().split())

d = [ list(map(int,input().split())) for _ in range(m)]

bfs= [ [0] * n for _  in range(m)]
dx= [0,0,-1,1]
dy = [1,-1,0,0]
ans = 0

a = deque()
cnt = 0
clear = 0
for i in range(m):
    for j in range(n):
        if d[i][j] == 1 :
            a.append((i,j))
        elif d[i][j] == - 1:
            cnt +=1


if clear == n * m -cnt :
    print(0)
    sys.exit(1)

while a:
    x,y = a.popleft()

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]

        if 0<= nx < m and 0<= ny < n and d[nx][ny] == 0 :
            d[nx][ny] = d[x][y]+1
            a.append((nx,ny))

ok = True
ans = -2147000000

for i in range(m):
    for j in range(n):
        if ans < d[i][j] :
            ans = d[i][j]

        if d[i][j] == 0 :
            ok = False


if ok == False:
    print(-1)
else:
    print(ans-1)