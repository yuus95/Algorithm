from collections import deque,Counter
from functools import reduce
import sys
sys.stdin=open("00.txt")

dx = [0,0,1,-1]
dy= [1,-1,0,0]

n , m = map(int,input().split())
d_list =[list(map(int,list(input()))) for _ in range(n)]

dist = [ [-1] * m for _ in range(n) ]

q = deque()
q.append((0,0))
dist[0][0] = 1

while q:
    x,y = q.popleft()
    for k in range(4):
        nx ,ny = x+dx[k],y+dy[k]
        if 0<= nx < n and 0<= ny < m:
            if dist[nx][ny] <0 and d_list[nx][ny] == 1 :
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny))

print(dist[n-1][m-1])