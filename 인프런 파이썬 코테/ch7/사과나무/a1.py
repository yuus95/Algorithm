import sys
sys.stdin = open("00.txt","r")

from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]

ch=[[0]*n for _ in range(n)] # 체크리스트

sum = 0
Q=deque()
ch[n//2][n//2] =1 # 중심부 L 0 에 해당
sum+= a[n//2][n//2]
Q.append((n//2,n//2)) # 레벨에 해당하는 값들을 나타내기 위해서 L0에서는 중심부만 L1 에서는 시계방향 4개의 데이터들 모두
L=0

while True:
    if L==n//2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y]==0:
                ch[x][y]=1
                sum+= a[x][y]
                Q.append((x,y))
    for k in ch:
        print(k)
    print()
    L+=1
print(sum)

