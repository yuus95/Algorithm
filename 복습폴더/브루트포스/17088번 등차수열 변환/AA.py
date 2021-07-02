import sys
sys.stdin=open("00.txt","r")

n = int(input())
a = list(map(int,input().split()))

ans = 2147000000
count = 0


# 예외처리를 까먹음
if n == 1 :
    print(0)
    exit()

for i in range(-1,2):
    for j in range(-1,2):
        cnt = 0
        ok = True
        a0 = a[0] + i
        a1 = a[1] + j

        if i != 0 :
            cnt+=1
        if j != 0 :
            cnt+=1
        diff = a1 - a0

        d = a1
        for k in range(2,n):
            d = d+diff
            if a[k] == d:
                continue
            elif a[k] +1 ==  d:
                cnt+=1
            elif a[k] - 1 == d:
                cnt+=1
            else :
                ok = False
                break

        if ok == False:
            continue

        count+=1
        ans = min(ans,cnt)

if count == 0 :
    print(-1)
else :
    print(ans)
