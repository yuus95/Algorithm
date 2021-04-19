import sys
sys.stdin = open("00.txt","r")

n , m , k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

c = [[False] * m for _ in range(n)]

ans = -2147000000
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def go(prev,cnt,s):
    if cnt == k :
        global ans
        if ans < s:
            ans = s
        return

    for j in range(prev+1,n*m):
        x = j//m # 행
        y = j%m # 열
        if c[x][y]:
            continue
        ok = True

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<= nx < n and 0 <= ny < n :
                if c[nx][ny]:
                    ok = False

        if ok:
            c[x][y] = True
            go(x*m+y,cnt+1,s+a[x][y])
            c[x][y] = False

go(-1,0,0)
print(ans)
