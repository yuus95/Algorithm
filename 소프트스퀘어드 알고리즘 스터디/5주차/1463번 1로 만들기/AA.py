import sys
sys.stdin=open("00.txt","r")


n = int(input())


d = [0] * (n+1)

d[1] = 0


for i in range(1,n+1):
    x1,x2,x3,=0,0,0
    if i % 3 == 0 :
        if d[i] == 0 or d[i] > d[i//3] +1 :
            d[i] = d[i//3] +1
    if i % 2 == 0 :
        if d[i] == 0 or d[i] > d[i//2]+1:
            d[i] = d[i//2]+1

    if i - 1 >=1 :
        if d[i] == 0 or d[i] > d[i-1]+1:
            d[i] = d[i-1] +1

print(d[n])