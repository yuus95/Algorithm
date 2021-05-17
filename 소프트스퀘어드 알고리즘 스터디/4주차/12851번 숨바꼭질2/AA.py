import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100001
visited[n] = 0
count = 0


def solve(visited, n, k):
    global count

    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            count += 1

        for nx in (x + 1, x - 1, 2 * x):
            if 0 <= nx < 100001:

                if visited[nx] == -1 or visited[nx] == visited[x] + 1:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)


solve(visited, n, k)
print(visited[k])
print(count)
