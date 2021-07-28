import  sys
sys.stdin=open("00.txt")


N,M,K = map(int,input().split())

a = list(map(int,input().split()))


a.sort(reverse=True)


i = 0
sum = 0
while i < M :

    for _ in range(K):
        sum += a[0]
        i+=1
    sum+=a[1]
    i+=1


print(sum)