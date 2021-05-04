from collections import deque

import sys
sys.stdin= open("00.txt","r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]

m,n = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque()
q.append((0,0))
dist[0][0] = 0

while q:
    x,y = q.popleft()
    for k in range(4):
        nx , ny = x+dx[k] , y+dy[k]

        if 0<= nx < n and 0<= ny < m :
            if dist[nx][ny] == -1:
                if a[nx][ny] == 0 :
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
                else :
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))


print(dist[n-1][m-1])