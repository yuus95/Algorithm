import sys
sys.stdin=open("00.txt")
#
n = int(input())
d_list=[]
for i in range(n):
    a ,b =input().split()
    a = int(a)
    d_list.append((i,a,b))


d_list.sort(key = lambda x: (x[1],x[0]))

for a,b,c in d_list:
    print(b,c)
