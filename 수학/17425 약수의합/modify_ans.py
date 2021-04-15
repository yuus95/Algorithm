import sys
sys.stdin=open("00.txt","r")
#  1 2

MAX = 100000

d = [1] * (MAX+1) # 각숫자마다 약수들의 합 f(x)
s = [0] * (MAX+1) #  주어진 x보다 작거나 같은 수의f(x) 의합 g(x)

for i in range(2,MAX+1):
    j = 1
    while i* j <= MAX:
        d[i*j] += i
        j+=1


for i in range(1,MAX+1):
    s[i] = s[i-1] + d[i]
    # d[i] = f(i)
    # s[i]  = g(i)
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(s[n])

print('\n'.join(map(str,ans))+'\n')