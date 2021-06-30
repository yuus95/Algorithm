import sys

sys.stdin=open("00.txt","r")

from collections import deque

dx=[-2,-2,0,0,+2,+2]
dy = [-1,+1,-2,+2,-1,+1]


n = int(input())

x1,y1,x2,y2 = map(int,input().split())

dist = [[-1] * n for _ in range(n)]


d = deque()
d.append((x1,y1))
dist[x1][y1] = 0

while d:
    x,y = d.popleft()

    for k in range(6):
        nx,ny = x+dx[k],y+dy[k]

        if 0<= nx < n and 0<= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y]+1
            d.append((nx,ny))


print(dist[x2][y2])



