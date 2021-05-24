# 숏코딩 답안

import sys

sys.stdin=open("00.txt","r")

for _ in range(int(input())):
    N = int(input())
    m = [list(map(int,input().split())) for _ in range(2)]

    for i in range(N-1):
        m[0][i+1]=max(m[0][i],m[1][i] +m[0][i+1])
        m[1][i+1] = max(m[1][i],m[0][i]+m[1][i+1])

    print(max(m[0][-1],m[1][-1]))

