import sys
sys.stdin=open("00.txt","r")

def go(a,l):
    #한줄 검사
    n = len(a)

    c = [False] * n
    for i in range(1,n):
        #인접한 칸의 높이가 다를 경우, 경사로를 놓아야한다.
        if a[i-1] != a[i]:

            #높이차이
            diff = abs(a[i]-a[i-1])

            if diff != 1:
                return False
            #  i - 1 < i 높은 경우의 경사로 검사
            if a[i-1] < a[i]:
                for j in range(1,l+1):
                    # 경사로를 놓다가 범위를 벗어나는 경우
                    if i-j < 0:
                        return False
                    #낮은 지점의 칸의 높이가 모두 같지 않는 경우
                    if a[i-1] != a[i-j]:
                        return False

                    #경사로가 이미 높여있는 경우
                    if c[i-j] :
                        return False
                    c[i-j] = True
            # i - 1 > i 높은 경우의 경사로 검사
            else :
                for j in range(l):
                    #경사로를 놓다가 범위를 벗어나는 경우
                    if i+j >= n :
                        return False

                    # 낮은 지점의 칸의 높이가 모두 같지 않는 경우
                    if a[i] != a[i+j]:
                        return False

                    #경사로가 이미 놓여 있는 경우
                    if c[i+j] :
                        return False
                    c[i+j] = True
    return True

n, l = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    d = a[i]
    if go(d,l):
        ans +=1

for j in range(n):
    d = [a[i][j] for i in range(n)]
    if go(d,l):
        ans+=1

print(ans)