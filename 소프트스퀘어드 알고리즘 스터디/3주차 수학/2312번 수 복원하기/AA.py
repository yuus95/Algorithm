import sys
from itertools import permutations
sys.stdin=open("00.txt","r")


n = int(input())

for _ in range(n):
    a = int(input())
    for i in range(2,a+1):
        cnt = 0
        if a % i == 0 :
            while True:
                if a  % i == 0 :
                    cnt+=1
                    a //=i
                else :
                    break
            print(i,cnt)
        elif i == 1:
            break
