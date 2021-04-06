import sys
sys.stdin= open("00.txt","r")


n = int(input())

d_list=list(map(int,input().split()))

d_list.sort()
sum = 0
res = 0
for i in range(n):
   sum += d_list[i]
   res += sum

print(res)