import sys
from itertools import permutations
sys.stdin=open("00.txt","r")


n,m,k = map(int,input().split())

a = k//m
b = k%m


print(a,b)

