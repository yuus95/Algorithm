import sys

sys.stdin=open("00.txt","r")

from collections import deque

n,m = map(int,input().split())

dist = [-1] * 101

after =list(range(101))


for _ in range(n+m):
    x,y  = map(int,input().split())
    after[x]=  y


d = deque()
d.append(1)
dist[1] = 0

while d:
    x = d.popleft()
    for i in range(1,7):
        y = x+i
        if y > 100:
            continue
        y = after[y]
        if dist[y] == -1:
            dist[y] = dist[x]+1
            d.append(y)

print(dist[100])

