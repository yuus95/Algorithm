import sys
sys.stdin=open("00.txt","r")

def check(password): # 모음 자음 갯수 확인하는 경우
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja>= 2 and mo >= 1


def go(n,alpha,password,i):
    if len(password) == n : #정답을 찾은 경우
        if check(password):
            print(password)
        return

    if i == len(alpha): # 불가능한 경우
        return

    go(n,alpha,password+alpha[i],i+1)
    go(n,alpha,password,i+1)



n,m = map(int,input().split())
a = input().split()

a.sort()

go(n,a,"",0)