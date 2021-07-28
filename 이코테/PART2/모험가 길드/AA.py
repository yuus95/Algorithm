import  sys
sys.stdin=open("00.txt")

n = int(input())

a = list(map(int,input().split()))

a.sort()

# 다시풀어보기
count = 0
group = 0
for i in a:
    count+=1
    if count >= i:
        group +=1
        count = 0

print(group)