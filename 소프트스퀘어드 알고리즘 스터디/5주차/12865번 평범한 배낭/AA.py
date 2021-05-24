import sys
sys.stdin=open("00.txt","r")

n = int(input())

a = list(map(int,input().split()))

d = [2147000] * n
d[0] = 0
for i in range(1,n):
    for j in range(i):
        for k in range(1,a[j]+1):
            if i == j + k:
                if d[i] > d[j] + 1:
                    d[i] = d[j] +1


if d[-1] == 2147000:
    print(-1)
else:
    print(d[-1])



