import sys
# sys.stdin = open("00.txt","r")

def DFS(x):
    global num,cnt

    if num%data[x] == 0:
        return  num//data[x]
    else :
        return num//data[x] + DFS(num%data[x+1])





n = int(input())
data = list(map(int,input().split()))
num = int(input())
cnt = 0
result = -2147000000
data.sort(reverse=True)


print(DFS(0))
