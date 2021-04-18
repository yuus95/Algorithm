import sys
sys.stdin=open("00.txt","r")


t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    x -= 1 # 나머지를 이용해 정답을 구하므로  x = x- 1 을 해야 나머지
    y -= 1
    k = x

    while k < n * m :
        if k % n == y :
            print(k+1)
            break
        k += m
    else :
        print(-1)
