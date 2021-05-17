import sys
from collections import deque


sys.stdin=open("00.txt","r")

n ,m = map(int,input().split())


d = [-1] * 100001
d[n] = 0

a = deque()
a.append(n)


while a:
    i = a.popleft()

    if  i +1 <= 100000  and d[i+1] == -1 :
        d[i+1] = d[i]+1
        a.append(i+ 1)
    if   i - 1 >=0  and d[i-1] == -1:
        d[i-1] = d[i] + 1
        a.append(i-1)

    if   i*2 <= 100000 and d[i*2] == -1:
        d[i*2] = d[i] +1
        a.append(i*2)

    if not d[m] == -1:
        break

print(d[m])
