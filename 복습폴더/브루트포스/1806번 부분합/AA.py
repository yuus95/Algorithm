import sys

sys.stdin=open("00.txt","r")

N,S = map(int,input().split())
d = list(map(int,input().split()))

# 길이 저장하기  R-L +1
ans = N+1
sum = d[0]
left = right = 0

while left <= right and right < N:
    temp =right - left + 1
    if sum < S :
        right +=1
        if right < N :
            sum += d[right]
    elif sum == S:
        if ans > temp :
            ans = temp
        right+=1
        if right < N:
            sum +=d[right]
    elif sum > S:
        if ans > temp:
            ans = temp
        sum -=d[left]
        left +=1
        if left > right and left <N :
            right = left
            sum =d[left]

if ans > N :
    ans = 0
print(ans)