import sys
sys.stdin = open("00.txt","r")


n = int(input())

d = list(range(n+1))

for i in range(1,n+1):
     j = 1
     while j*j <= i :
         if d[i] > d[i- j*j]+1:
             d[i] = d[i- j * j] + 1
         j+=1


print(d[n])