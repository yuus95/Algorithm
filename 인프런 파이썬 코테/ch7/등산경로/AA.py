import sys
sys.stdin= open("00.txt","r")

def DFS(x,y):
    global cnt
    if x  == MAX_X and y == MAX_Y:
        cnt +=1
    else :
        for i in range(4):
            xx = x + dx[i]
            yy = y+dy[i]
            if 0<=xx< n and 0<= yy <n and d_list[xx][yy] > d_list[x][y] and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                DFS(xx,yy)
                ch[xx][yy]= 0



cnt = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
d_list = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
N_MAX = -2147000000
N_MIN = 2147000000

for i in range(n):
    for j in range(n):
        if N_MAX < d_list[i][j]:
            N_MAX = d_list[i][j]
            MAX_X = i
            MAX_Y = j
        if N_MIN > d_list[i][j]:
            N_MIN = d_list[i][j]
            MIN_X = i
            MIN_Y = j

ch[MIN_X][MIN_Y] = 1
DFS(MIN_X,MIN_Y)

print(cnt)