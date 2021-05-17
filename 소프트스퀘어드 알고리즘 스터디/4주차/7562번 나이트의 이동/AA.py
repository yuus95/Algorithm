import sys
from itertools import permutations
sys.stdin=open("00.txt","r")

from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]



n = int(input())

for _ in range(n):
    l = int(input())
    si,sj = map(int,input().split())
    ei,ej = map(int,input().split())
    d = deque()
    a= [[-1] * l for _ in range(l)]
    a[si][sj] = 0
    d.append((si,sj))


    while d:
        x,y = d.popleft()
        ok = True
        for k in range(8):
            nx,ny = x+dx[k] ,y+dy[k]

            if 0<= nx < l and 0<= ny < l and a[nx][ny] == -1:
                a[nx][ny] = a[x][y] +1
                d.append((nx,ny))

            if nx == ei and ny == ej:
                ok = False
                break
        if ok == False:
            break

    print(a[ei][ej])





