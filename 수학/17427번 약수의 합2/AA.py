import sys
sys.stdin=open("00.txt","r")

n = int(input())
res = 0
for i in range(1,n+1):
    tmp = n//i * i
    res += tmp


print(res)