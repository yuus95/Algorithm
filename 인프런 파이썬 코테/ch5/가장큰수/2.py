import sys
sys.stdin = open("00.txt","r")

n,m = map(int,input().split())

num = list(map(int,str(n)))
stack = []


for x in num :
        while stack and  stack[-1] < x and m>0 :
            stack.pop()
            m -= 1
        stack.append(x)
if m != 0:
    stack = stack[:-m]
else :
    res = ''.join(map(str,stack))
    print(res)