import sys
sys.stdin=open("00.txt","r")

n = int(input())


ans = 0


for i in range(1,n+1):
    if i <= 9 :
        ans += 1
    elif i <= 99 :
        ans += 2
    elif i <= 999:
        ans +=3
    elif i <= 9999:
        ans +=4
    elif i<= 99999:
        ans += 5
    elif i<= 999999:
        ans +=6
    elif i<= 9999999:
        ans +=7
    elif i<= 99999999:
        ans+=8
    else:
        ans+=9

print(ans)