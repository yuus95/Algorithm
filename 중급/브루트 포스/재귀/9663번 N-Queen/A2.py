import sys
sys.stdin=open("00.txt","r")

# 통과코드

def check(row,col):
    if check_col[col]:
        return False

    if check_dig[row+col]:
        return False

    if check_dig2[row-col+n -1] :
        return False

    return  True

def calc(row):
    if row == n :
        return 1
    ans = 0

    for col in range(n):
        if check(row,col):
            check_dig[row+col] = True
            check_dig2[row+n -col - 1 ] = True
            check_col[col] = True

            # a[row][col] = True
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n -1 ] = False
            check_col[col] = False
            # a[row][col] = False

    return ans

n = int(input())
a = [[False] * n for _ in range(n)]
check_col  = [False] * n # 열 검사
check_dig = [False] * (2*n-1) # 대각선 검사
check_dig2=[False] * (2*n-1) # 대각선2 검사

print(calc(0))
