import sys

sys.stdin=open("00.txt","r")

from collections import deque

#  BFS 문제풀이 실패 다시 풀기

a,b,c = map(int,input().split())

s = a+b+c
q = deque()
q.append((a,b))
q.append((a,c))
q.append((b,c))

ch = [[False] * 1501 for _ in range(1501)]

while q:
    x,y = q.popleft()
    x = min(x,y)
    y = max(x,y)
    if ch[x][y] :
        continue
    ch[x][y]= True
    q.append((x+x,y-x))


if s % 3 != 0 :
    print(0)
else :
    if ch[s//3][s//3]:
        print(1)
    else :
        print(0)



