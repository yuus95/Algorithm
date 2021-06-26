import sys

sys.stdin=open("00.txt","r")

from collections import deque

n = int(input())
a  =[[]for _ in range(n)]
for _ in range(n):
    u,v = map(int,input().split())
    u -= 1
    v -= 1

    #  그래프 정점 사이의 이어진 간선 체크
    a[u].append(v)
    a[v].append(u)


check = [0] * n # 0 : not visited , 1: visited, 2: cycle


# x = 현재 y = 이전
def go(x,p):

    if check[x] == 1:
        return x
    check[x]=1

# 1234
    for y in a[x]:
        if y == p :
            continue
        res = go(y,x)
        # 싸이클에 포함되어 있지않으면 다 마이너스2 리턴
        if res == -2:
            return -2
        #싸이클 시작점 까지만 res 가 0이상임 
        if res >= 0 :
            check[x] = 2
            if x == res:
                return -2
            else :
                return res
    return - 1


go(0,-1)


q = deque()
dist = [-1]* n

for i in range(n):
    #순환선에 있을 경우
    if check[i] == 2 :
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = - 1

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x]+1

print(*dist,sep=' ')

