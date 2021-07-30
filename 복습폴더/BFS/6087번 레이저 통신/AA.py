import sys
from collections import deque
sys.stdin=open("00.txt","r")

dx = [-1,1,0,0]
dy = [0,0,-1,1]
m,n = map(int,input().split())

a = [list(input()) for _ in range(n)]


# 시작점 끝점 찾기
sx=sy=ex=ey = -1
for x in range(n):
    for y in range(m):
        if a[x][y] =='C':
            if sx ==-1 and sy == -1 :
                sx,sy= x,y
            else:
                ex,ey=x,y


d =[[-1] * m for _ in range(n)]


q= deque()
q.append((sx,sy))

while q:
    x,y = q.popleft()

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        # 한 방향에 대하여 쭉검사하기 -> 벽이만나면 break, 직선을 만나면 그전 직선갯수 +1
        while 0<= nx < n and 0<= ny < m :
            if a[nx][ny] == '*':
                break
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y]+1
                q.append((nx,ny))
            nx +=dx[k]
            ny +=dy[k]
# 거울의 개수 : 두 C를 연결하는데 필요한 직선의 최소 개수 -1
# 거울 설치: 직선의 방향을 변경
print(d[ex][ey-1])



