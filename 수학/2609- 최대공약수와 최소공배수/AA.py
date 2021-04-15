import sys
sys.stdin=open("00.txt","r")

def gcd(x,y):
    if y == 0 :
        return x
    else:
        return gcd(y,x%y)

a,b = map(int,input().split())
g = gcd(a,b)

print(g) # 최대 공약수
print(a*b//g) # 최대 공배수





