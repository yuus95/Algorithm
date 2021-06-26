import sys
sys.stdin=open("00.txt","r")

# 재귀함수버전

def go(index):
    global ans
    if index == n :
        num = int("".join(d))
        if d[0] != '0'  and num < b :
            if num > ans :
                ans = num
        return


    for i in range(n):
        if ch[i] == False:
            ch[i] = True
            d[index] = a[i]
            go(index+1)
            ch[i] = False



a,b = input().split()

a =list(a)
b = int(b)
n = len(a)
ch = [False] * n
d = [0]* n
ans = -1
go(0)
print(ans)