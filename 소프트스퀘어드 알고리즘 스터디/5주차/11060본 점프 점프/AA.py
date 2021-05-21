import sys
sys.stdin=open("00.txt","r")

n = int(input())

a = list(map(int,input().split()))

d = [2147000] * n
d[0] = 0
for i in range(n):
    for j in range(a[i]):
        if  a[i] +j < n :
            if d[a[i]+j]  > d[i] +1 :
                d[a[i]+j] = d[i] + 1



print(d)




