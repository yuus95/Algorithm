import sys
from itertools import permutations
sys.stdin=open("00.txt","r")

from collections import deque


F,S,G,U,D = map(int,input().split())


d = [-1] * (F+1)

d[S] = 0


q= deque()

q.append(S)

while q:
    x = q.popleft()

    if x + U <= F and d[x + U] ==  -1 :
        d[x+U] = d[x]+1
        q.append(x+U)

    if x - D  >= 1 and d[x - D]== -1 :
        d[x-D] = d[x] + 1
        q.append(x-D)


if d[G] == -1 :
    print("use the stairs")
else:
    print(d[G])
