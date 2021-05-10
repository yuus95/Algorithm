import sys

sys.stdin=open("00.txt","r")

n,m,k = map(int,input().split())

max_a = -2147000000

for i in range(k+1):
    if i > n :
        continue
    if k - i > m :
        continue

    a = n- i

    b = m -k +i

    if a >= 2*b :
        c = b
    else :
        c = a//2
    max_a=max(max_a,c)

print(max_a)