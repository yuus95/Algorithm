from collections import deque
import sys
sys.stdin=open("00.txt")

sys.setrecursionlimit(1000000)
# t = int(sys.stdin.readline())


def dfs(x, c):
    color[x] = c
    for y in a[x]:
        if color[y] == 0:
            if not dfs(y, 3 - c):
                return False
        elif color[y] == color[x]:
            return False
    return True

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = [[] for _ in range(n)]
    color = [0] * n
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)


    ans = True
    for i in range(n):
        if color[i] == 0:
            if not dfs(i,1):
                ans = False
    print('YES' if ans else 'NO')
