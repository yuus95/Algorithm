import sys
sys.stdin = open("00.txt","r")


n = int(input())

a = list()

for _ in range(n):
    s ,e = map(int,input().split())
    a.append((s,e))
cnt = 0
a.sort(reverse=True)
max = - 2147000000
for s,e in a :
    if e > max :
        cnt +=1
        max = e

print(cnt)