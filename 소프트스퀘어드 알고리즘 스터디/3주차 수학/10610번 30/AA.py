import sys
from itertools import permutations
sys.stdin=open("00.txt","r")


a = input()

s = 0

if '0' not in a:
    print(-1)
else :
    for i in a: # 각 자릿수 더해서 3의 배수 만들기
        s+=int(i)
    if s % 3 != 0: #각자릿수 더햇는데 3의 배수면 통과 아니면 -1
        print(-1)
    else :
        print(''.join(sorted(a,reverse=True)))

