import sys
sys.stdin=open("00.txt","r")


n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    num = a[i]
    cnt = 0
    while num % 3 == 0 :
        num = n//3
        cnt +=1
    a[i] = (-cnt,a[i])

a.sort()
ans = [x[1] for x in a ]

print(*ans,sep = ' ')