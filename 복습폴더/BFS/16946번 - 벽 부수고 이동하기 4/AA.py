import sys
from collections import deque
sys.stdin=open("00.txt","r")

def bfs(i,j):
    check[i][j] = True
    l = len(group_len)
    cnt = 1
    group[i][j] = l

    q = deque()
    q.append((i,j))

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x +dx[k],y+dy[k]

            if nx<0 or nx >= n or ny <0 or ny >= m :
                continue

            if a[nx][ny] == 0 and check[nx][ny] == False:
                check[nx][ny] =True
                group[nx][ny] = l
                q.append((nx,ny))
                cnt+=1
    group_len.append(cnt)






n , m = map(int,input().split())

dx= [0,0,-1,1]
dy = [1,-1,0,0]


# 입력받은 맵
a = [list(map(int,list(input()))) for _ in range(n)]

# 그룹 배열
group =[[0]* m for _ in range(n)]
check =[[False]* m for _ in range(n)]

#체크배열
group_len = []



for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            bfs(i,j)


for i in range(n):
    for j in range(m):
        if a[i][j] == 0 :
            print(0,end='')

        else :
            num_box=set()
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if nx < 0 or nx >=n or ny <0 or ny>= m :
                    continue
                if a[nx][ny] == 0:
                    num_box.add(group[nx][ny])
            ans = 1
            for x in num_box:
                ans += group_len[x]
            print(ans % 10, end='')
    print()
