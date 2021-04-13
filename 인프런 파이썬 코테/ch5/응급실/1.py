import sys
from collections import deque
sys.stdin = open("00.txt","r")
n,m = map(int,input().split())
Q=[(pos,val) for pos,val in  enumerate(list(map(int,input().split())))] # enumerate 알아두기!! 리스트 튜플값으로 저장
Q=deque(Q)
cnt= 0

while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break