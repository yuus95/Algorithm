import sys

sys.stdin=open("00.txt","r")


from collections import Counter


t = int(input())

n = int(input())

a = list(map(int,input().split()))

m= int(input())

b = list(map(int,input().split()))

x = []

y = []

x1 = []

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]
        x1.append(sum)


#1 3 1 2
for i in range(1<<n):

    sum = 0
    for j in range(n):
        if i &(1<<j) > 0 :
            sum += a[j]
    x.append(sum)

#1 3 2
for i in range(1<<m):
    sum = 0
    for j in range(m):
        if i & (1<<j) > 0 :
            sum +=b[j]
    y.append(sum)
cn = Counter(y)
i = 0
j = 0
ans = 0
print(a)
print(x)
print(x1)

x.sort()
y.sort()


while i < len(x):

    if t - x[i] in y :
        i+=1
        ans += cn[t-x[i]]
        while x[i] == x[i-1]:
            i+=1
    else :
        i+=1

print(ans)





