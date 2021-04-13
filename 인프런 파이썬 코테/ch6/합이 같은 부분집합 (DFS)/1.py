import sys
sys.stdin=open("00.txt","r")

def DFS(x):
    if x == n :
        sum_a = 0
        sum_b = 0
        for i in range(n):
            if box[i] == 1:
                sum_a += data[i]
            else :
                sum_b += data[i]

            if sum_a == sum_b:
                print("YES")
                sys.exit(0)
    else :
        box[x]= 1
        DFS(x+1)
        box[x]=0
        DFS(x+1)





n = int(input())
data = list(map(int,input().split()))

box = [0]*(n)

DFS(0)
print("NO")