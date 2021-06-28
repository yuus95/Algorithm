import sys

sys.stdin=open("00.txt","r")

sys.setrecursionlimit(1000000)
#월요일 다시풀기

n = int(input())

a = [list(input()) for _ in range(n)]

color = [[-1] * n for _ in range(n)]

dx=[-1,-1,0,0,1,1]
dy= [0,1,-1,1,-1,0]

ans = 0

# c 컬러?  --
def dfs(x,y,c):
    global ans
    color[x][y]= c
    ans = max(ans,1)
    for k in range(6):
        nx,ny = x+dx[k],y+dy[k]

        # 방문한 곳 또 방문하는지 체크
        if 0 <= nx < n and 0<= ny < n :
            if a[nx][ny] == 'X':
                #방문 하지 않았을 경우
                if color[nx][ny]== -1:
                    # color[nx][ny] = 1-c
                    dfs(nx,ny,1-c)
                    ans =max(ans,2)
                if color[nx][ny] == c:
                    ans = max(ans,3)




for i in range(n):
    for j in range(n):
        if a[i][j] == 'X' and color[i][j] == -1:
            dfs(i,j,0)

print(ans)

