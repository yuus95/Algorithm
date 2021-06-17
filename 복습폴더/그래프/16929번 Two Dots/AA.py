import sys

sys.stdin=open("00.txt","r")

dx = [0,0,1,-1]
dy =[1,-1,0,0]

n,m = map(int,input().split())

a = [input() for _ in range(n)]

# 길이,색

def go(x,y,cnt,color):

    if ch[x][y] == True:
        if cnt - dist[x][y] >= 4:
            return True
        else:
            return False
    ch[x][y] = True
    dist[x][y]=cnt
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0<= nx < n and 0<= ny < m and a[nx][ny] ==color:
            if go(nx,ny,cnt+1,color):
                return True


    return False

for i in range(n):
    for j in range(m):
        ch = [[False] * m for _ in range(n)]
        dist=[[0] * m for _ in range(n)]
        if go(i,j,1,a[i][j]):
            print('Yes')
            exit()

print('No')
