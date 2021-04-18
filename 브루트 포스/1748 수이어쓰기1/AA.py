import sys
sys.stdin=open("00.txt","r")


n = int(input())

ans = 0
start = 1
length = 1

while start <= n :
    end = start * 10 - 1 # 끝자리
    if end > n :
        end = n
    ans += (end - start + 1 ) * length
    start *= 10
    length += 1

print(ans)