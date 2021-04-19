import sys
sys.stdin=open("00.txt","r")

inf  = -10 ** 9

n =int(input())
t = [0] *(n)
p = [0] * (n)

for i in range(0,n):
    t[i],p[i] = map(int,input().split())

ans = 0

def go(day,s):
    global ans
    if day == n  :
        ans = max(ans,s)
        return
    if day > n:
        return

    go(day+1,s) # 지금날짜를 선택 안하는경우
    go(day+t[day],s+p[day])

go(0,0)
print(ans)