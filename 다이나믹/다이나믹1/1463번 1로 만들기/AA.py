import sys
sys.stdin=open("00.txt","r")


n = int(input())
d = [0]*(n+1)
d[1] = 0

for i in range(2,n+1):
    d[i]= d[i-1] + 1
    if i%2 == 0 and d[i] > d[i//2] +1:
        d[i] = d[i//2] +1
    if i % 3 == 0 and d[i] > d[i//3] +1:
        d[i] = d[i//3] +1
print(d[n])
