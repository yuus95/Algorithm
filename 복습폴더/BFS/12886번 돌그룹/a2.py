import sys

sys.stdin=open("00.txt","r")

from collections import deque

a,b,c =map(int,input().split())

#돌의 개수합
s = a+b+c

q = deque()

q.append((a,b))
q.append((a,c))
q.append((b,c))


# BFS 체크 돌개수 나눈 횟수에 대해서는 중복 x
ch= [[False] * 1501 for _ in range(1501)]

while q:
    x,y = q.popleft()
    x = min(x,y)
    y = max(x,y)
    # 맥스가 y이고 x이가 최소인 경우가 중복됐을 때 컨티뉴
    if ch[x][y]:
        continue
    ch[x][y] = True
    q.append((x+x,y-x))


if s % 3 != 0 :
    print(0)
else:
    if ch[s//3][s//3]:
        print(1)
    else:
        print(0)


