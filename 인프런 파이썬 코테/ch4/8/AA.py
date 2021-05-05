import sys
sys.stdin = open("00.txt","r")

n, m = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

lt = 0
rt = n-1
cnt = 0
while lt<=rt:
    if lt == rt :
        cnt +=1
        break

    if data[lt]+data[rt] > m:
        rt -=1
        cnt +=1
    else :
        lt +=1
        rt-= 1
        cnt +=1

print(cnt)