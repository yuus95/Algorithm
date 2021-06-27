import sys
sys.setrecursionlimit(1000000)

sys.stdin=open("00.txt","r")

from collections import deque

# 메모리 초과

n = int(input())

a = [[]  for _ in range(n)]

ch= [-1] * n
dist = [-1] * n

for _ in range(n):
    u,v = map(int,input().split())
    u-=1
    v-=1
    a[u].append(v)
    a[v].append(u)


def go(x,p):

    if ch[x] == 1:
        return x

    ch[x] = 1

    for y in a[x]:
        if y == p:
            continue

        res = go(y,x)
        if res == -2:
            return -2
        elif res >= 0:
            ch[x] = 2
            if res == x:
                return -2
            else :
                return res
    return -1

go(0,-1)


de = deque()

for i in range(n):
    if ch[i] ==2  :
        de.append(i)
        dist[i] = 0


while de:
    x = de.popleft()
    for y in a[x]:
        if dist[y] == -1:
            de.append(y)
            dist[y] = dist[x] + 1


print(*dist,end=' ')

