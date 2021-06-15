import sys

sys.stdin=open("00.txt","r")

n,s = map(int,input().split())

d = list(map(int,input().split()))


left = right = 0

ans = 0
sum = d[0]

while left <= right and right < n :
    if sum < s :
        right +=1
        if right < n :
            sum +=d[right]

    elif sum == s:
        right +=1
        ans +=1
        if right < n :
            sum +=d[right]

    elif sum > s:
        sum -= d[left]
        left +=1

        if left > right and left < n:
            right = left
            sum  =d[left]

print(ans)