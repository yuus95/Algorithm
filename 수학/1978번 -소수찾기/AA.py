import sys
sys.stdin=open("00.txt","r")

def is_prime(x):
    if x<2:
        return False
    i = 2
    while i*i <=x: #루트 N 까지 약수가 있는지 검사하는방법
        if x % i == 0 : # 2~ 루트N까지 나누어지는 수가 있다면 False
            return False
        i+=1
    return True # 나누어지는 수가 없다면 False


n = int(input())
a = list(map(int,input().split()))

ans = 0
for x in a :
    if is_prime(x):
        ans+=1

print(ans)
