import sys

sys.stdin=open("00.txt","r")

n,s = map(int,input().split())

a = list(map(int,input().split()))
m = n //2
n = n-m

x = []
y = []


for i in range(1<<m):
    sum = 0
    for j in range(m):
        if i&(1<<j) > 0 :
            sum+=a[j]
    x.append(sum)



for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i&(1<<j) > 0 :
            sum+=a[j+m]
    y.append(sum)

x.sort()
y.sort()
y.reverse()

i = j = 0
sum = x[i] + y[j]
ans = 0
n = (1<<n)
m = (1<<m)
while i < m and j < n:
    if sum < s :
        i +=1
        if i < m :
            sum = x[i] + y[j]

    elif sum == s:
        cnt1= 1
        cnt2= 1

        i += 1
        j += 1
        while i < m and x[i] == x[i-1]:
            cnt1+=1
            i += 1

        while j < n and  y[j] == y[j-1]:
            cnt2+=1
            j += 1
        ans +=(cnt1*cnt2)
        if i < m and j < n :
            sum = x[i] + y[j]

    elif sum > s :
        j += 1
        if j < n :
            sum = x[i] + y[j]


if s == 0 :
    ans -= 1


print(ans)





