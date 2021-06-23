import sys
sys.stdin = open("00.txt","r")

def DFS(x,y):
    global cnt
    d_list[x][y] = 0
    cnt +=1

    for k in range(4):
        xx = x+dx[k]
        yy=y+dy[k]

        if 0<=xx <n and 0<= yy <n and d_list[xx][yy]>0:
            DFS(xx,yy)




dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
d_list = [list(map(int,input())) for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if d_list[i][j] == 1:
            cnt = 0
            DFS(i,j)
            res.append(cnt)
print(len(res))
res.sort()
for x in res:
    print(x)