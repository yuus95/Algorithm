import sys
sys.stdin=open("00.txt")

n = int(input())

d_list = list(map(int,input().split()))

d=[1]*n
max = 0

for i in range(n):

    for j in range(i):
        if d[i] < d[j]+1 and d_list[i] > d_list[j]:
            d[i] = d[j] +1
        if max < d[i] :
            max = d[i]

print(max)
