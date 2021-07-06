import sys
sys.stdin=open("00.txt","r")

from copy import deepcopy

n,m,d = map(int,input().split())

b = [list(map(int,input().split())) for _ in range(n)]


def clac(l1,l2,l3):
    a = deepcopy(b)
    ans = 0
    while True:
        cnt = 0

        # 게임 종료 조건
        for i in range(n):
            for j in range(m):
                cnt +=a[i][j]
        if cnt == 0 :
            break

        # i 번 궁수의 공격대상
        deleted = [(-1,-1)]  * 3
        archer = [l1,l2,l3]

        #최소 거리
        for k in range(3):
            rx,ry = n,archer[k]
            x=y=dist=-1
            for j in range(m):
                for i in range(n):
                    if a[i][j] != 0 :
                        dx = abs(rx-i)
                        dy = abs(ry-j)
                        dd = dx+dy
                        if dd <= d:
                            if dist == -1 or dist > dd:
                                x=i
                                y=j
                                dist = dd
            deleted[k] = (x,y)

        # 적이 근처에오면 제거
        for x,y in deleted:
            if x == -1:
                continue
            if a[x][y] != 0 :
                ans +=1
            a[x][y]= 0

        # 한칸씩 내리기
        for i in range(n-1,-1,-1):
            for j in range(m):
                if i == 0 :
                    a[i][j] = 0
                else:
                    a[i][j] = a[i-1][j]

    return ans


ans = 0


# 궁수 m개중 3개 뽑기
for l1 in range(m):
    for l2 in range(l1+1,m):
        for l3 in range(l2+1,m):
            temp = clac(l1,l2,l3)
            if ans< temp:
                ans = temp

print(ans)
