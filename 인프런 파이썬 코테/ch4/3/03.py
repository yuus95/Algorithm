import sys
sys.stdin = open("00.txt","r")


def count(a):
    cnt = 1
    sum = 0

    for i in data:
        if sum+i > a:
            sum=i
            cnt +=1
        else :
            sum+= i
    return cnt

n,m = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

lt = 1
rt = sum(data)
res = 0

while lt<= rt:
    mid =(lt+rt)//2
    if count(mid) <= m :
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
print(res)