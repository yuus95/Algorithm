import sys
sys.stdin=open("00.txt","r")



h, w = map(int,input().split())

n = int(input())

r = []
c = []

ans = -2147000000

for _ in range(n):
    a,b = map(int,input().split())

    r.append(a)
    c.append(b)


for i in range(n-1):
    r1,c1 = r[i],c[i]
    for j in range(i+1,n):
        r2,c2 = r[j],c[j]
        #회전
        for _ in range(2):
            for _ in range(2):
                if c1+c2 <= w and max(r1,r2) <= h :
                    temp = c1*r1 + c2 * r2
                    if temp > ans :
                        ans = temp

                if r1+r2 <= h and max(c1,c2) <= w:
                    temp = c1 * r1 + c2 * r2
                    if temp > ans:
                        ans = temp

                r2,c2 = c2,r2
            r1,c1= c1,r1


if ans < 0 :
    print(0)
else :
    print(ans)