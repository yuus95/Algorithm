import sys
sys.stdin=open("00.txt","r")


n = int(input())

for _ in range(n):
    k = int(input())
    tmp = []
    max = 2147000000
    cnt = 0
    for _ in range(k):
        a,b = map(int,input().split())
        tmp.append((a,b))

    tmp.sort()
    for a,b in tmp:
        if max > b:
            max = b
            cnt+=1
    print(cnt)