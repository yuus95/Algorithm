import sys
sys.stdin=open("00.txt", "r")
from collections import deque

MAX= 10000

ch = [0] *(MAX+1)
dis=[0] * (MAX+1)

n,m = map(int,input().split())
ch[n]=1 #갔던 거리 체크하기 위해
dis[n]=0 #현재거리 레벨?



Q=deque()
Q.append(n)
cnt = 0


while Q:
    now = Q.popleft()
    if now == m:
        break
    for next in (now-1,now+1,now+5):
        if 1<= next <= MAX:
            if ch[next]==0:
                Q.append(next)
                ch[next]=1
                dis[next] = dis[now]+1

print(dis[m])