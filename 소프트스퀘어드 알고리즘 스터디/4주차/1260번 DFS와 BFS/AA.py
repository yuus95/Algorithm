import sys
from collections import deque
sys.stdin=open("00.txt","r")

n , m , k  = map(int,input().split())


a = [[] for _ in range(n+1)]

for _ in range(m):
    b, c = map(int,input().split())
    a[b].append(c)
    a[c].append(b)

for x in a :
    x.sort()

check=[0] * (n+1)


def dfs(num):
    global check

    check[num] = True
    print(num , end= ' ')
    for x in a[num]:
        if not check[x]:
            dfs(x)

dfs(k)
print()
ch = [False] *(n+1)
d = deque()
d.append(k)
ch[k] =True

while d:

    x = d.popleft()
    print(x,end=' ')

    for i in a[x]:
        if ch[i] == False:
            ch[i] = True
            d.append(i)



