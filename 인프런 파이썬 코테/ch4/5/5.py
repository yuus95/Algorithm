import sys
sys.stdin = open("00.txt","r")

n = int(input())
line= []
for _ in range(n):
    n,m = map(int,input().split())
    line.append((n,m))

line.sort(key = lambda x:(x[1],x[0]))

et = 0
cnt = 0

for x, y in line:
    if x>= et:
        et = y
        cnt+=1
print(cnt)