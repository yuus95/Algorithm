import sys
from collections import deque
sys.stdin=open("00.txt","r")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]  # 입력값
group = [[-1] * m for _ in range(n)]  # i,j 의 그룹 번호
check = [[False] * m for _ in range(n)] # bfs 체크
group_size = [] # k번 그룹의 크기 


def bfs(sx, sy):
    g = len(group_size)
    q = deque()
    q.append((sx, sy))
    group[sx][sy] = g
    check[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False and a[nx][ny] == 0:
                    check[nx][ny] = True
                    group[nx][ny] = g  # 그룹번호 지정
                    q.append((nx, ny)) 
                    cnt += 1

    group_size.append(cnt)


# 빈 벽 그룹 지정
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False: 
            bfs(i, j)

# 이동할 수 있는 칸 갯수 세기
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans % 10, end='')
    print()
