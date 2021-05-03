import sys
sys.stdin=open("00.txt")

n,m = map(int,input().split())
a={}

for _ in range(n+m):
    temp=input()
    if temp in a:
        a[temp] +=1
    else:
        a[temp] = 1

ans = [x for x,y in a.items() if y == 2 ]

print(len(ans))
ans.sort()
for x in ans:
    print(x)