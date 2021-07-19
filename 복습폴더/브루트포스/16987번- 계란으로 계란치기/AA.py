import sys
sys.stdin=open("00.txt","r")
n = int(input())
# 내구도
s = [0]*n
# 무게
w = [0]*n
for i in range(n):
    s[i], w[i] = map(int, input().split())

ans = 0

def go(index):
    global ans
    if index == n:
        cnt = 0
        for i in range(n):
            if s[i] <= 0 :
                cnt+=1
        return cnt

    i = index
    if s[i] <= 0 :
        return go(index+1)

    for  j in range(n):
        if i == j :
            continue

        if s[j] <= 0 :
            continue

        s[i] -= w[j]
        s[j] -= w[i]
        temp = go(index+1)
        s[i]+= w[j]
        s[j] += w[i]

        if ans  < temp:
            ans = temp


    return

print(go(0))
