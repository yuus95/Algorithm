import sys
sys.stdin=open("00.txt","r")

# (이전값 나머지 X 10 + 1)% n = 나머지
while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    while True:
        num= num*10 +1;
        num %= n
        if num ==0 :
            print(i)
            break
        i+=1
