import sys
sys.stdin=open("00.txt","r")

#단점 행 열 이 중복된다.
n , m , k = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

c = [[False] * m for _ in range(n)]

res = -2147000000
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def go(cnt,s): # cnt 선택한 칸의 개수,  s: 선택한 칸의 합
    if cnt == k :
        global res

        if res < s:
            res = s
        return


    # x 와 y 가 1부터 다시 시작하는것이 문제 
    for x in range(n):
        for y in range(m):
            if c[x][y]:
                continue
            ok = True

            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<= nx < n and 0 <= ny < m:
                    if c[nx][ny]:
                        ok = False

            if ok:
                c[x][y] = True
                go(cnt+1,s+a[x][y])
                c[x][y] = False

go(0,0)
print(res)

