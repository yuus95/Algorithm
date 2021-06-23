import sys
sys.stdin = open("00.txt","r")

n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]
sum_list = 0
m = (n//2 )

s=e=m

for i in range(n):
    for j in range(s,e+1):
        sum_list += data[i][j]
        print(data[i][j])
    if i<m:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(sum_list)