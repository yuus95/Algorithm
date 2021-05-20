import sys
sys.stdin=open("00.txt","r")


n = int(input())

for _ in range(n):
    M,N,x,y= map(int,input().split())
    year = 1

    while year<N*M:
        if year % M == x and year % N == y:
            print(year)
            break
        year+=1
    else:
        print(-1)
        break

