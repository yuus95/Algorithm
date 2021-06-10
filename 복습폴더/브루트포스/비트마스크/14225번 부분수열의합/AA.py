import sys
sys.stdin=open("00.txt","r")
#5 1 2


n = int(input())

d = list(map(int,input().split()))


check = [True] * (100000 * 20 + 10)

for i in range(1<<n):
    s = 0
    for j in range(n):
        if i &(1<<j):
            s +=d[j]

    check[s] = False
i = 1

while True:
    if check[i] == True:
        print(i)
        break
    i+=1


