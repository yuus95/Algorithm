import sys
sys.stdin=open("00.txt","r")

# 다른방식으로 풀기 실패 

n = int(input())
a = list(input())

m = n//2

stack = []
for i in range(0,n,2):
    a[i] = int(a[i])


for i in range(1<<m):
    ok = True
    for j in range(m-1):
        if (i & (1<<j) > 0 and (i & (1<<j+1))):
            ok = False
            break

    if not ok :
        continue

    b=a[:]


    for j in range(m):
        if i & (1<<j):
            k = j* 2 + 1
            if b[k] == '+':
                b[k-1] +=b[k+1]

            elif b[k] == '-':
                b[k-1] -= b[k+1]
            elif b[k] == '*':
                b[k-1] *= b[k+1]

            b[k] = '+'
            b[k+1]= 0

    # print(b)
    for i in range(n):
        if type(b[i]) == int:
            if b[i] == 0 :
                if stack and type(stack[-1]) ==int:
                    continue
                else :
                    stack.pop()
            else:
                stack.append(b[i])

        else:
            if b[i] =='+':
                stack.append(b[i])
            elif b[i] == '*':
                temp = stack.pop()
                temp *= b[i+1]
                b[i+1] = 0
                stack.append(temp)
            elif b[i] == '-':
                stack.append(b[i])

    print(stack)






