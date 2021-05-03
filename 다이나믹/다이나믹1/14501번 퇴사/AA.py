import sys
sys.stdin=open("00.txt","r")

inf = 10 ** 9
n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
d = [-1] * (n+1)
for i in range(1,n+1):
    t[i],p[i] = map(int,input().split())

ans = 0

def go(day) :
    if day == n+1:
        return 0

    if day > n+1:
        return -inf
    if d[day] != -1:
        return d[day]
    t1 = go(day+1)
    t2 = p[day]+go(day+t[day])
    d[day]=max(t1,t2)
    print(day)
    print(d)
    return d[day]



print(go(1))
