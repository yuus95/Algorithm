n = int(input())
a=[]

for _ in range(n):
    a.append(int(input()))

res=sum(a)
res = res - n + 1
print(res)
