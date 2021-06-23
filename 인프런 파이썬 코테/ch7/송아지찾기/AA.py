import sys
from collections import deque

sys.stdin=open("00.txt","r")

MAX= 10000
ch=[0]*(MAX+1) #체크 리스트
dis=[0]*(MAX+1) # 최단거리 구하는 리스트

n,m = map(int,input().split())

ch[n]=1
dis[n]=0
dQ=deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now-1,now+1,now+5):
        if 1<= next <= MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]= dis[now]+1

print(dis[m])