import sys
sys.stdin=open("00.txt","r")

from copy import deepcopy

n,m,d = map(int,input().split())

b = [list(map(int,input().split())) for _ in range(n)]



# 시물
def go(i,j,k):
    k_arr = [i, j, k]
    a = deepcopy(b)
    cnt = 0
    while True:
        # 처음으로 제거하는 행렬 체크
        check_list=[(-1,-1)]*3
        ok =False
        check_ok = False
        for k in range(3):
            dist = -1
            dx = n
            dy = k_arr[k]
            for j in range(m):
                for i in range(n):
                    if a[i][j] == 1:
                        ok = True
                        ny = abs(dy - j)
                        nx = abs(dx-i)
                        dd  = nx + ny
                        if dd > d :
                            continue
                        else:
                            if dist > dd or dist == -1:
                                dist = dd
                                check_list[k]=(i,j)
                                check_ok = True

        if ok == False:
            break


        if check_ok == True:
            for x,y in check_list:
                if x != -1 and y != -1:
                    if a[x][y] != 0 :
                        a[x][y] = 0
                        cnt+=1



        for i in range(n-1,-1,-1):
            for j in range(m):
                if i == 0 :
                    a[i][j] = 0
                else:
                    a[i][j] = a[i-1][j]
    return cnt








# 위치 바꾸기
#
ans = 0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            temp = go(i,j,k)
            if ans < temp:
                ans = temp

print(ans)
