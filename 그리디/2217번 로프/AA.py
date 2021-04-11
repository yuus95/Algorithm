# import sys
# sys.stdin=open("00.txt","r")


#로프를 다 사용할 필요가 없다는걸 인식 못했다. 다시풀어보기
k= int(input())
a=[]
max = 0
for _ in range(k):
    a.append(int(input()))

a.sort(reverse=True)

for i in range(k):
    tmp = a[i] * (i+1)
    if max < tmp:
        max = tmp


print(max)