import sys
from collections import deque
sys.stdin=open("00.txt","r")

n = 8
a = [list(input()) for _ in range(n)]

dx = [-1,-1,0,1,1,1,0,-1,0]
dy = [0,1,1,1,0,-1,-1,-1,0]


# t 초후에 다음칸으로 이동할 수 있는지 체크
d = [[[-1]* (n+1) for _ in range(n)]for _ in range(n)]


q = deque()
# x, y, t (시간)
q.append((7,0,0))
d[7][0][0] =1

ans = 0
# 2가지 조건 체크하고 이동할 수 있으면 체크하기 
while q:
    x,y,t = q.popleft()

    if x== 0 and y == 7 :
        ans = 1
    for k in range(9):
        nx,ny = x +dx[k],y+dy[k]
        nt = min(t+1,8) # 다음 시간이 8초이상이면 의미가 없다.

        if 0<= nx < n and 0<= ny < n and d[nx][ny][nt] == -1 :

            if nx-t >=0 and a[nx-t][ny] == '#':
                continue
            if nx-t-1 >=0 and a[nx-t-1][ny] =='#':
                continue

            d[nx][ny][nt] = 1
            q.append((nx,ny,nt))


print(ans if ans == 1 else 0)




