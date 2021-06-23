import sys
from  collections import deque
sys.stdin = open("00.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
d_list = [list(map(int,input())) for _ in range(n)]
Q= deque()
res = []
for i in range(n):
    for j in range(n):
       if d_list[i][j] == 1:
           d_list[i][j]=0
           Q.append((i,j))
           cnt = 1
           while Q:
                now = Q.popleft()
                for k in range(4):
                        xx = now[0] + dx[k]
                        yy = now[1]+dy[k]
                        if 0<= xx <n and 0<= yy < n and d_list[xx][yy] ==1 :
                            d_list[xx][yy]=0
                            cnt+=1
                            Q.append((xx,yy))
           res.append(cnt)

print(res)
