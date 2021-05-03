import sys
sys.stdin=open("00.txt","r")

n = int(input())

d_list =  list(map(int,input().split()))

d = [0] * n


for i in range(n):
    d[i] = d_list[i]
    if i == 0:
        continue
    if d_list[i] < d[i-1] + d_list[i]:
        d[i] = d[i-1] + d_list[i]

print(max(d))
