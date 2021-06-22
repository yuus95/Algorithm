import sys
sys.stdin=open("00.txt","r")


h,w = map(int,input().split())
n = int(input())

# 스티커의 row
r = [0] * n

# 스티커의 column
c = [0] * n

# N개의 스티커 기록
for i in range(n):
    r[i],c[i] = map(int,input().split())

ans = 0

for i in range(n):
    r1,c1 = r[i],c[i]
    for j in range(i+1,n):
        r2,c2 = r[j],c[j]
        for rot1 in range(2):
            for rot2 in range(2):
                if r1+r2 <= h and max(c1,c2) <= w:
                    temp =r1 * c1 + r2 * c2
                    if ans < temp :
                        ans = temp

                if max(r1,r2) <= h and c1 + c2 <= w:
                    temp = r1*c1 + r2 * c2
                    if ans < temp:
                        ans = temp

                r2 ,c2 = c2 , r2
            r1,c1 = c1,r1

print(ans)
