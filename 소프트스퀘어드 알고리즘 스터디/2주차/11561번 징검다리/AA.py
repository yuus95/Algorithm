import sys
sys.stdin=open("00.txt")


t = int(input())

for _ in range(t):
    num = int(input())
    a = 1
    cnt = 1
    sum= 1
    while True :
        if num - sum <= a :
            print(cnt)
            break
        a+=1
        sum+=a
        cnt+=1