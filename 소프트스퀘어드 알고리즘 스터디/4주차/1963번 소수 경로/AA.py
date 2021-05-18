import sys
from itertools import permutations
sys.stdin=open("00.txt","r")

from collections import deque


d = [False] *10000
prime= []


for i in range(2,10000):

    if d[i]== False:
        if i >=1000:
            prime.append(i)
        j = 2
        while i*j < 10000:
            d[i*j] =True
            j+=1


n = int(input())

a = str(10)
a = list(a)
a[0] ='2'


#
# for _ in range(n):
#     n,m = input().split()
#     d=[-1] * 10000
#     n = list(n)
#     m= list(m)
#     a = deque()
#     a.append(n)
#     cnt = 1
#
#     while a:
#         x = a.popleft()
#
#         for i in range(4):
#             for j in range(4):
#                 x[i] = m[j]
#                 x = int(x)
#                 if prime(x) == False:
#                     d[x] = cnt
#                     a.append(str(x))
#             cnt+=1
#         if x == int(m):
#             break
#
#
#
