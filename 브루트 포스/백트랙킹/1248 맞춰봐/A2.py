import sys
sys.stdin= open("00.txt","r")

def ok():
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += ans[j]
            if sign[i][j] == 0:
                if s != 0:
                    return False
            elif sign[i][j] > 0:
                if s <= 0:
                    return False
            elif sign[i][j] < 0:
                if s >= 0:
                    return False
    return True

def go(index):
    if index == n:
        return ok()
    if sign[index][index] == 0:
        ans[index] = 0
        return go(index+1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if go(index+1):
            return True
    return False

n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(' '.join(map(str,ans)))