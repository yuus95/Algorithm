import sys
from collections import deque


sys.stdin=open("00.txt","r")

n ,m = map(int,input().split())


dx = [1,0,-1,0]
dy = [0,1,0,-1]


d_list = [list(input()) for _ in range(m)]

c_box = []
d = [[-2] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if d_list[i][j] == 'C':
            c_box.append((i,j))


queue = deque()
queue.append((c_box[0][0],c_box[0][1],0))
d[c_box[0][0]][c_box[0][1]] = -1


while queue:
    x,y,dir = queue.pop()

    for k in range(4):
        nx ,ny = x+dx[k] , y+dy[k]
        if 0<= nx < m  and 0<= ny < n and d_list[nx][ny] == '.':
            if d[nx][ny] == -2:
                if dir == -1 :
                    d[nx][ny] = 0
                    queue.append((nx,ny,k))
                elif dir == 0 or dir == 2 :
                    if k == 0 or k == 2 :
                        d[nx][ny] = d[x][y]
                        queue.appendleft((nx,ny,k))
                    else :
                        d[nx][ny] = d[x][y]+1
                        queue.append((nx,ny,k))
                elif dir == 1 or dir == 3 :
                    if k == 1 or k== 3:
                        d[nx][ny] = d[x][y]
                        queue.appendleft((nx,ny,k))
                    else :
                        d[nx][ny]  = d[x][y] +1
                        queue.append((nx,ny,k))

print(c_box)
print(d[6][1])

for x in range(m):
    for j in range(n):
        print(d[x][y],end=' ')
    print()

