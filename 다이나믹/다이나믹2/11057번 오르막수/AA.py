import sys
sys.stdin=open("00.txt","r")


n = int(input())

d = [[0] * 10 for _ in range(1001)]
mod = 10007
d[0][0] = 1


for i in range(1,n+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]
            d[i][j] %= mod

ans = sum(d[n])
print(ans%mod)