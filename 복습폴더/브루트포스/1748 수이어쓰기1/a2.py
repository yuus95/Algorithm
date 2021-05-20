import sys
sys.stdin=open("00.txt","r")

n = int(input())


ans = 0

start = 1
len = 1

while start <= n:
    end = start * 10 - 1
    if end >= n :
        end = n

    ans += (end-start +1) * len

    len+=1
    start *=10


print(ans)
