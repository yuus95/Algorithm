from collections import deque
import sys
sys.stdin=open("00.txt")


#큐소스
MAX = 200000
check = [False] * MAX
dist = [-1] * MAX
n,m = map(int,input().split())

check[n] = True
dist[n] = 0
q= deque()
next_queue = deque()
q.append(n)

while q:
    now = q.popleft()
    if now * 2 < MAX and check[now*2] == False:
        q.append(now*2)
        check[now*2] = True
        dist[now*2 ] = dist[now]

    if now -1 >= 0 and check[now-1] == False:
        next_queue.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] +1

    if now + 1 < MAX and check[now+1] == False:
        next_queue.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now]+1

    if not q:
        q= next_queue
        next_queue = deque()

print(dist[m])
