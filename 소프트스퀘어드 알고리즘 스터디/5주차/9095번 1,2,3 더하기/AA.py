from collections import deque
import sys
sys.stdin=open("00.txt","r")



t = int(input())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 12):
    if i - 3 > 0:
        d[i] += d[i - 3]

    if i - 2 > 0:
        d[i] += d[i - 2]

    if i - 1 > 0:
        d[i] += d[i - 1]

for _ in range(t):
    n = int(input())
    print(d[n])
