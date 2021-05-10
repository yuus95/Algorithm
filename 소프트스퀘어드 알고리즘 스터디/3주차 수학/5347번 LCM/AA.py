import sys
from itertools import permutations
sys.stdin=open("00.txt","r")


n = int(input())

def gcd(x,y):
    if y == 0 :
        return x
    return gcd(y,x%y)


for _ in range(n):
    a,b = map(int,input().split())
    if a>b :
        c = gcd(a,b)
    else :
        c = gcd(b,a)
    print(a*b // c)
