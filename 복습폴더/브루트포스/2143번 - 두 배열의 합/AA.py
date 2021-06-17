import sys

sys.stdin=open("00.txt","r")


from collections import Counter



t = int(input())

n =int(input())

a = list(map(int,input().split()))

m = int(input())

b = list(map(int,input().split()))

# a 누적합
x = []


# b 누적합
y = []


for i in range(n):
    sum = 0

    for j in range(i,n):
        sum += a[j]
        x.append(sum)


for i in range(m):
    sum = 0
    for j in range(i,m):
        sum +=b[j]
        y.append(sum)

x.sort()
y.sort()

cn = Counter(y)
i = 0
ans = 0


for i in x:
    ans += cn[t-i]
    
# 아침에 시간복잡도 다시 계산하기

# while i < len(x):
#     if t - x[i] in y:
#         ans += cn[t-x[i]]
#         i+=1
#         # while i<len(x) and x[i] == x[i-1]:
#         #     i+=1
#
#     else :
#         i+=1

print(ans)


