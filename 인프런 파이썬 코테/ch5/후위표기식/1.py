import sys
sys.stdin=open("00.txt", "r")
a=input()
stack = []
res = ""
for x in a :
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x=='*' or x =='/':
            while stack and (stack[-1]== '*' or stack[-1]=='/'):
                res += stack.pop()
            stack.append(x)
        elif x =='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x ==')': # 우선순위 ) 로 마감할 경우  스택 ( 제거
            while stack and stack[-1]!= '(':
                res+=stack.pop()
            stack.pop()
while stack: # stack 에 남아있는 데이터가 있을 경우 res에 더하기
    res+= stack.pop()
print(res)


