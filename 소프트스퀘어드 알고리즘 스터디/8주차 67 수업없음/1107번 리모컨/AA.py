def click_num(num):

    if num == 0 :
        if broekn[num] :
            return 0
        else :
            return 1
    len = 0
    while num > 0 :
        if broekn[num%10] :
            return 0
        len+=1
        num//=10
    return len

broekn = [False] * 10

n = int(input())

k = int(input())

if k > 0 :
    a= list(map(int,input().split()))
else:
    a = []

for x in a :
    broekn[x] = True

ans = abs(n-100)

for i in range(0,1000001):
    l = click_num(i)

    if l > 0 :
        press = abs(n-i)
        if ans > press+l:
            ans = press+l


print(ans)
