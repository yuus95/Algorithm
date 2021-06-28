import sys

sys.stdin=open("00.txt","r")

from collections import deque

n,m = map(int,input().split())

# after 함수 1~101로 초기화
# after함수 : 사다리와 뱀을 통해 이동한 위치에 대한 가중치를 넣어주기 위해서

after = list(range(101))
dist = [-1] * 101

# after 함수에 사다리와 뱀 좌표 업데이트
for _ in range(n+m):
    x,y = map(int,input().split())
    after[x]=y


dist[1]= 0
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1,6+1):
        y = x + i
        if y> 100:
            continue
        y = after[y]
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)

print(dist[100])

