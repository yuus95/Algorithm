# 백준 숏코딩 답안

import sys

sys.stdin = open("00.txt","r")


def f(n):
    if n <= 2 : return n- 1
    return 1+ min(f(n//3)+n%3,f(n//2)+n%2)



print(f(int(input())))

