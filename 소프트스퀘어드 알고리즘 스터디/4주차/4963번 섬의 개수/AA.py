import sys
from itertools import permutations

sys.stdin = open("00.txt", "r")

from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    a = [list(map(int, input().split())) for _ in range(m)]
    ch = [[0] * n for _ in range(m)]

    d = deque()
    cnt = 0
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1 and ch[i][j] == 0:
                cnt += 1
                d.append((i, j))
                ch[i][j] = cnt
                while d:
                    x, y = d.popleft()

                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < m and 0 <= ny < n and a[nx][ny] == 1:
                            if ch[nx][ny] == 0:
                                ch[nx][ny] = cnt
                                d.append((nx, ny))

    print(cnt)