from collections import deque
import sys
sys.stdin=open("00.txt","r")


t = int(input())




for _ in range(t):
    n = int(input())

    a = [[0] +list(map(int,input().split())) for _ in range(2)]

    d=[[0] * (n+1) for _ in range(2)]
    for i in range(1,n+1):
        if i >2 :
            d[0][i] = max(d[1][i-1]+a[0][i], d[0][i-2]+a[0][i],d[1][i-2]+a[0][i])
            d[1][i] = max(d[0][i - 1] + a[1][i], d[0][i - 2] + a[1][i], d[1][i - 2] + a[1][i])
        else:
            d[0][i] = d[1][i-1]+a[0][i]
            d[1][i]= d[0][i-1]+a[1][i]



    print(max(d[0][n],d[1][n]))