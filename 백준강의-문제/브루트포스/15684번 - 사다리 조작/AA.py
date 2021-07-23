import sys
sys.stdin=open("00.txt","r")

# i번이 i번으로 가는지 검사
def start(c):
    r = 1
    while r <= h:
        if garo[r][c] == 1:
            c += 1
        elif garo[r][c] == 2:
            c -= 1
        r += 1
    return c
# 세로선 모두검사
def go():
    for i in range(1, w):
        res = start(i)
        if res != i:
            return False
    return True
w,m,h = map(int,input().split())
garo = [[0]*(w+1) for _ in range(h+1)]
for _ in range(m):
    x,y = map(int,input().split())
    garo[x][y] = 1
    garo[x][y+1] = 2
a = []

# 가로선을 만들 수 있는 가능한 경우의 수 체크
for i in range(1, h+1):
    for j in range(1, w):
        if garo[i][j] != 0:
            continue
        if garo[i][j+1] != 0:
            continue
        a.append((i,j))
ans = -1

# 추가 가로선을 넣지 않고 성공할 경우.
if go():
    print(0)
    sys.exit(0)

# 추가 가로선 넣기
for i in range(len(a)):
    
    #1번쨰 가로선
    x1,y1 = a[i]
    if garo[x1][y1] != 0 or garo[x1][y1+1] != 0:
        continue
    garo[x1][y1] = 1
    garo[x1][y1+1] = 2
    if go():
        if ans == -1 or ans > 1:
            ans = 1
            continue
    for j in range(i+1, len(a)):
        x2,y2 = a[j]
        if garo[x2][y2] != 0 or garo[x2][y2+1] != 0:
            continue
        garo[x2][y2] = 1
        garo[x2][y2+1] = 2
        if go():
            if ans == -1 or ans > 2:
                ans = 2
                continue
        for k in range(j+1, len(a)):
            x3,y3 = a[k]
            if garo[x3][y3] != 0 or garo[x3][y3+1] != 0:
                continue
            garo[x3][y3] = 1
            garo[x3][y3+1] = 2
            if go():
                if ans == -1 or ans > 3:
                    ans = 3
                    continue
            garo[x3][y3] = 0
            garo[x3][y3+1] = 0
        garo[x2][y2] = 0
        garo[x2][y2+1] = 0
    garo[x1][y1] = 0
    garo[x1][y1+1] = 0
print(ans)