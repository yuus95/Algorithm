import sys
sys.stdin=open("00.txt","r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def go(cnt,x1,y1,x2,y2):
    if cnt == 11 :
        return - 1
    fall1 = False
    fall2 = False

    if x1< 0 or x1>= n or y1 <0 or y1 >= m :
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m :
        fall2 = True

    if fall1 and fall2 :
        return - 1
    if fall1 or fall2 :
        return cnt

    ans = -1
    for k in range(4):
        nx1,ny1= x1 + dx[k],y1+dy[k]
        nx2,ny2= x2 +dx[k],y2+dy[k]

        if 0<= nx1< n and 0<= ny1 < m and a[nx1][ny1]=='#':
            nx1,ny1 = x1,y1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2, ny2 = x2, y2

        temp = go(cnt+1,nx1,ny1,nx2,ny2)
        if temp == -1:
            continue
        if ans == -1 or ans > temp:
            ans = temp

    return ans

n , m = map(int,input().split())

a = [list(input()) for _ in range(n)]

x1=y1=x2=y2 = -1
for x in range(n):
    for y in range(m):
        if a[x][y] == 'o':
            if x1 == - 1:
                x1,y1 = x,y
            else:
                x2,y2 = x,y
            a[x][y] = '.'


print(go(0,x1,y1,x2,y2))
