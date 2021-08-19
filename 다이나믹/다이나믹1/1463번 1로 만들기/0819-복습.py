import sys
sys.stdin= open("00.txt")


n = int(input())

d =[0] * 1000001

d[2] = 1
d[3] = 1

for i in range(4,n+1):

    if i % 3 == 0 :
        if d[i] == 0 or d[i] > d[i//3] + 1 :
            d[i] = d[i//3] +1

    if i % 2 ==0 :
        if d[i] == 0 or d[i] > d[i//2] + 1 :
            d[i] = d[i//2] +1

    if i - 1 >=1:
        if d[i] == 0 or d[i] > d[i-1] + 1 :
            d[i] = d[i-1] +1


print(d[n])