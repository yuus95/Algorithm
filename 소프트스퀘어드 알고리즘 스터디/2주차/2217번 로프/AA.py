import sys
sys.stdin=open("00.txt")

max= 0
n = int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)

for i in range(n):
    temp = a[i] *(i+1)
    if max < temp:
        max = temp

print(max)