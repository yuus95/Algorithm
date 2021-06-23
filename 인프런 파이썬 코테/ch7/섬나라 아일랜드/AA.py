import sys
from collections import deque

sys.stdin = open("00.txt","r")


n = int(input())

d_list = [list(map(int,input().split())) for _ in range(n)]
Q= deque()
res=[]
cnt = 0

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(n):
    for j in range(n):
        if d_list[i][j] == 1:
            cnt+=1
            d_list[i][j] = 0
            Q.append((i,j))
            while Q:
                now = Q.popleft()
                for k in range(8):
                    xx = now[0] +dx[k]
                    yy = now[1]+dy[k]
                    if 0<= xx <n and 0<= yy <n and d_list[xx][yy] >0:
                        d_list[xx][yy]=0
                        Q.append((xx,yy))

print(cnt)