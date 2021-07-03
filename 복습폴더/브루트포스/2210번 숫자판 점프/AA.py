import sys
sys.stdin=open("00.txt","r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def go(x,y,num,index):
    if index == 5 :
        d.add(num)
        return

    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]

        if 0<= nx < 5 and 0<= ny < 5 :
            go(nx,ny,num*10 + a[nx][ny],index+1)



d = set()
a = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
       go(i,j,a[i][j],0)


print(len(d))