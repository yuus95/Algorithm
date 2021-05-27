import sys
sys.stdin=open("00.txt","r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]



def f_sum(cnt,x,y,sum):
    global f_value
    if cnt == 3 :
        if f_value  < sum :
            f_value = sum
        return
    if cnt == 2 and sum + 1000 < f_value:
        return
    ch[x][y] = True
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0<= nx < N and 0<= ny < M and ch[nx][ny] == False:
            f_sum(cnt+1,nx,ny,sum+a[nx][ny])
    ch[x][y] = False







N,M = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(N)]
ch =[[False] * M for _ in range(N)]
f_value = -2147000

for  i in range(N):
    for j in range(M):
         f_sum(0,i,j,a[i][j])
         if j + 2 < M :
             if i + 1 < N :
                 temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]
                 if temp > f_value :
                     f_value = temp
             if i - 1 >= 0:
                 temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i - 1][j + 1]
                 if temp > f_value:
                     f_value = temp
         if i + 2  < N :
             if j + 1 < M :
                 temp = a[i][j] + a[i+1][j] + a[i+1][j + 1] + a[i + 2][j]
                 if temp > f_value:
                     f_value = temp

             if j - 1 >= 0 :
                 temp = a[i][j] + a[i+1][j] + a[i+2][j ] + a[i + 1][j - 1]
                 if temp > f_value:
                     f_value = temp



print(f_value)
