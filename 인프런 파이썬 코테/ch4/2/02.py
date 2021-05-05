import sys

sys.stdin= open("00.txt","r")


def check(a):
    cnt = 0
    for x in line:
         cnt += x//a
    return cnt
n,m = map(int,input().split())
line =[]
for _ in range(n):
    tmp = int(input())
    line.append(tmp)

line.sort()
largest = line[-1]
lt = 1
rt = largest
res= 0
while lt<=rt:
    mid = (lt+rt)//2
    if check(mid) >=m:
      res = mid
      lt = mid +1
    else :
        rt = mid -1

print(res)
