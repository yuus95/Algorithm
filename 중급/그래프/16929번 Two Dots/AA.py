import sys

sys.stdin=open("00.txt","r")

dx = [0,0,1,-1]
dy =[1,-1,0,0]

n,m = map(int,input().split())

a = [input() for _ in range(n)]
# a = list(input() for _ in range(n))

# 시작점으로 부터의 거리를 기록
# dist = [[0] * m for _ in range(n)]

check = [[False] * m for _ in range(n)]

def go(x,y,cnt,color):
    if check[x][y]:
        if cnt-dist[x][y] >= 4:
            print(cnt)
            return True
        else :
            return False

    check[x][y] = True
    dist[x][y] = cnt
    for k in range(4):
        nx,ny = x+dx[k] ,y+dy[k]
        if 0 <= nx< n and 0 <= ny < m :
            if a[nx][ny] == color:
                if go(nx,ny,cnt+1,color):
                    return True

    return False

# 모든 점에 대해서 DFS검사
for i in range(n):
    for j in range(m):
        if check[i][j] :
            continue
        #거리측정
        dist = [[0] * m  for _ in range(n)]

        ok = go(i,j,1,a[i][j])
        if ok :
            print('Yes')
            exit()

print('No')

