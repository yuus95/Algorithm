import sys
sys.stdin=open("00.txt","r")

n = int(input())
a = list(input())

m = n//2

for i in range(0,n,2):
    a[i] = int(a[i])

ans = -2147000000

# 3+8*7-9*2
for i in range(1<<m):

    ok = True

    for j in range(m-1):
        if i &(1<<j) > 0 and i & (1<<j+1) > 0 :
            ok = False
            break
    if not ok :
        continue

    b= a[:]
    for j in range(m):
        if i & (1<<j) > 0 :
            k = 2 * j + 1

            if a[k] == '+':
                b[k-1] += a[k+1]
                b[k+1] = 0
            elif a[k] =='-':
                b[k-1]-= b[k+1]
                b[k] = '+'
                b[k+1] = 0
            elif a[k] =='*':
                b[k-1]*=b[k+1]
                b[k]= '+'
                b[k+1]= 0

    temp = b[0]
    for j in range(m):
        k = j * 2 + 1
        if b[k] == '+':
            temp+=b[k+1]
        elif b[k] =='-':
            temp-=b[k+1]
        elif b[k] =='*':
            temp *= b[k+1]

    ans = max(ans,temp)


print(ans)



