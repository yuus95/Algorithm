import sys
sys.stdin=open("00.txt","r")
from collections import deque

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

def go(x,y,direction):
    ans = 0
    if x == n-1 and y == n-1:
        return 1

    if direction == 0 :
        if y+1 < n and a[x][y+1] == 0 :
            ans += go(x,y+1,0)

        if x+1 < n and y+1 <n  and a[x][y+1] == 0 and a[x+1][y] == 0 and a[x+1][y+1] == 0 :
            ans += go(x+1,y+1,2)

    elif direction == 1 :
        if x+1 < n and a[x+1][y] == 0 :
            ans += go(x+1,y,1)

        if x + 1 < n and y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
            ans += go(x + 1, y + 1, 2)

    elif direction == 2:
        if y+1 < n and y+1 < n and a[x][y+1] == 0 :
            ans += go(x,y+1,0)
        if x+1 < n and a[x+1][y] == 0 :
            ans += go(x+1,y,1)

        if x + 1 < n and y + 1 < n and a[x][y + 1] == 0 and a[x + 1][y] == 0 and a[x + 1][y + 1] == 0:
            ans += go(x + 1, y + 1, 2)
    return ans




print(go(0,1,0))

