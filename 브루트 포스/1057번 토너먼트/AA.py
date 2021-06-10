import sys
sys.stdin=open("00.txt","r")

n, a, b = map(int,input().split())

cnt = 1
while True:
    idx1 = a if a % 2 == 0 else a +1
    idx2 = b if b % 2 ==0 else b + 1

    if idx1 == idx2 :
        print(cnt)
        break
    a = idx1//2
    b = idx2//2
    cnt += 1