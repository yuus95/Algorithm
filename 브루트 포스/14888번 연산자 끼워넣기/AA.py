import sys

sys.stdin = open("00.txt", "r")


def go(d, cur, idx, plus, minus, mul, div):
    global n, max_num, min_num

    if idx == n:
        max_num = max(max_num, cur)
        min_num = min(min_num, cur)
    else:
        if plus > 0:
            go(d, cur + d[idx], idx + 1, plus - 1, minus, mul, div)
        if minus > 0:
            go(d, cur - d[idx], idx + 1, plus, minus - 1, mul, div)
        if mul > 0:
            go(d, cur * d[idx], idx + 1, plus, minus, mul - 1, div)
        if div:
            go(d,cur //d[idx], idx + 1, plus, minus, mul, div - 1)

n = int(input())

d = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_num = -2147000000
min_num = 2147000000

go(d, d[0], 1, plus, minus, mul, div)

print(max_num)
print(min_num)
