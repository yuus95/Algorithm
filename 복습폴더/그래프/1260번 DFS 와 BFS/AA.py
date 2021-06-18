import sys

sys.stdin=open("00.txt","r")

from collections import deque

n,m ,s = map(int,input().split())


a = [[] for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    a[x-1].append(y-1)
    a[y-1].append(x-1)

for i in range(n):
    a[i].sort()

ch = [0] * n
d= []

# 모든 정점들이 연결되어있는지 확인하기

def go(x):
        d.append(x)
        for i in a[x]:
            if ch[i] == 0 :
                ch[i] = 1
                go(i)

ch[s-1] = 1
go(s-1)



q = deque()
d2 = []
ch2 = [True] * n
q.append(s-1)
d2.append(s-1)
ch2[s-1] =  False
while q:
    k = q.popleft()
    for i in a[k]:
        if ch2[i] == True:
            ch2[i] = False
            d2.append(i)
            q.append(i)
for x in d:
    print(x+1,end=' ')
print()

for x in d2:
    print(x+1,end=' ')


