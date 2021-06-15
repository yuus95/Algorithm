import sys

sys.stdin=open("00.txt","r")

N = 4000000

a = int(input())

ch= [True] * (N+1)

#소수리스트
p_list = []

for i in range(2,N+1):
    if ch[i] == True:
        p_list.append(i)
        j = i
        while i + j <= N:
            ch[i+j] = False
            j += i


left = right = 0
sum = p_list[0]
ans = 0

if a == 1:
    ans = 0

else:
    while left <= right and right < len(p_list):

        if sum < a :
            right +=1
            if right < len(p_list):
                sum+=p_list[right]
        elif sum == a :

            ans +=1
            right +=1
            if right < len(p_list):
                sum += p_list[right]

        elif sum  > a :
            sum -=p_list[left]
            left +=1

            if left > right and left < len(p_list):
                right = left
                sum = p_list[left]

print(ans)

