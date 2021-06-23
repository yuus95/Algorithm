import sys
sys.stdin = open("00.txt",'r')

def DFS(x,y):
    global cnt
    if x > 6 or y >6 or x<0  or y<0:
        return
    if x == 6 and y == 6 :
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and d_list[xx][yy]==0:
                d_list[xx][yy]=1
                DFS(xx,yy)
                d_list[xx][yy]=0

dx = [-1,0,1,0]
dy=[0,1,0,-1]
d_list =[list(map(int,input().split())) for _ in range(7) ]
cnt = 0
d_list[0][0]=1
DFS(0,0)
print(cnt)