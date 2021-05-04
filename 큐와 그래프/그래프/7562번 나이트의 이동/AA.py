from collections import deque,Counter
from functools import reduce
import sys
sys.stdin=open("00.txt")

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]


t = int(input())

for _ in range(t):
    l = int(input())
    x,y = map(int,input().split())
    res_x,res_y = map(int,input().split())

    dist = [ [-1] * l for _ in range(l)]

    q=deque()
    q.append((x,y))
    dist[x][y] = 0
    if x == res_x and y == res_y :
        print(0)
        continue

    while q:
        x,y = q.popleft()

        for k in range(8):
            nx,ny = x+dx[k],y+dy[k]
            if 0<= nx < l and 0<= ny < l :
                if dist[nx][ny] == -1 :
                    q.append((nx,ny))
                    dist[nx][ny]  = dist[x][y] +1
    print(dist[res_x][res_y])



