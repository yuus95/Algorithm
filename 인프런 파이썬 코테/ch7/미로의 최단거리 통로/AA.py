import sys
from collections import deque

sys.stdin = open("00.txt",'r')


d_list = [list(map(int,input().split())) for _ in range(7)]
dx= [-1,0,1,0]
dy =[0,1,0,-1]
ch =[[0]*7 for _ in range(7)]


Q = deque()
Q.append((0,0))
d_list[0][0]=1



while Q:
    now = Q.popleft()
    for i in range(4):
        x = now[0]+dx[i]
        y = now[1]+dy[i]
        if 0<= x  <= 6 and 0<= y<=6 and d_list[x][y] == 0 :
            d_list[x][y]=1
            ch[x][y]=ch[now[0]][now[1]]+1
            Q.append((x,y))
if ch[6][6]==0:
    print(-1)

else:
    print(ch[6][6])



