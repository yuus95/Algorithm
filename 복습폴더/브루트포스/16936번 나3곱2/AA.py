import sys
sys.stdin=open("00.txt","r")

n = int(input())


a = list(map(int,input().split()))
d = []
for x in a:
    cnt = 0
    temp = x
    if x%3 == 0 :
        while temp % 3 ==  0 :
            temp //= 3
            cnt +=1
    d.append((-cnt,x))

d.sort(key=lambda x:(x[0],x[1]))

for x,y in d :
    print(y,end=' ')




