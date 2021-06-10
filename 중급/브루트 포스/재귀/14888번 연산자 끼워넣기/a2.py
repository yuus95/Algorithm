import sys
sys.stdin=open("00.txt","r")

def calc(num, idx, plus,minus,mul,div):
    global n ,max_num,min_num
    if idx == n :
        max_num= max(max_num,num)
        min_num = min(min_num,num)

    else :
        if plus:
            calc(num + a[idx],idx+1,plus-1,minus,mul,div)
        if minus:
            calc(num - a[idx],idx+1,plus , minus-1,mul,div)
        if mul:
            calc(num * a[idx],idx+1,plus,minus,mul -1 , div)
        if div :
            calc(int(num/a[idx]),idx+1,plus,minus,mul,div-1)



n = int(input())
a = list(map(int,input().split()))

max_num = -2147000000
min_num = 2147000000


plus,minus,mul,div = map(int,input().split())
ans = calc(a[0],1,plus,minus,mul,div)
print(max_num)
print(min_num)