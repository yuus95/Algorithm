import sys
sys.stdin = open("00.txt","r")


n = int(input())

a = list(map(int,input().split()))

count = int(input())
a.sort()
for _ in range(count):
    a[n-1] -=1
    a[0]+=1
    a.sort()

print(a[n-1]-a[0])