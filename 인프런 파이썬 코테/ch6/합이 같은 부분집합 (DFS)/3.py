import sys
sys.stdin=open("00.txt","r")

def DFS(x,sum):
    if sum > total//2:
        return
    if x >= n+1:
        if total-sum == sum :
            print("YES")
            sys.exit(0)

    else:
        DFS(x+1,sum+a[x])
        DFS(x+1,sum)



n = int(input())

a = list(map(int,input().split()))
total = sum(a)

DFS(0,0)
print("NO")