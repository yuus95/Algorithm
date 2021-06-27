import sys
sys.stdin=open("00.txt","r")

def go(index,num):
    ans = -1
    if index == n :
        return num
    for i in range(n):
        if ch[i] == True:
            continue
        if index == 0 and a[i] == '0':
            continue
        ch[i]=True
        temp = go(index+1, num * 10 + int(a[i]) )

        if temp < b:
            if temp> ans :
                ans = temp
        ch[i] = False
    return ans




a,b= input().split()

a = list(a)
b= int(b)
n = len(a)
ch=[False] * n

print(go(0,0))

