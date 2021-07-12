import sys
sys.stdin=open("00.txt","r")
from collections import deque

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[[0]*3 for j in range(n)] for i in range(n)]


def solve():
    d[0][1][0] = 1
    for i in range(n):
        for j in range(n):
            if j +1< n and not a[i][j+1]:
                d[i][j+1][0] += d[i][j][0] + d[i][j][2]

            if i+1 < n and not a[i+1][j]:
                d[i+1][j][1] += d[i][j][1] +d[i][j][2]
            if i +1< n and j+1 < n and not (a[i+1][j] or a[i][j+1] or a[i+1][j+1]):
                d[i+1][j+1][2] += d[i][j][0]+d[i][j][1]+d[i][j][2]

solve()
print(sum(d[n-1][n-1]))