import sys
sys.stdin=open("00.txt","r")

n = int(input())
a = [ list(input()) for _ in range(n)]

#회전 횟수
k = int(input())

#회전하는 동안 반복
for _ in range(k):
    #톱니바퀴 번호, 도는방향
    no,dir = map(int,input().split())
    no -= 1

    #회전 방향 저장하는 배열
    d=[0] * n
    d[no] = dir

    # 지정된 톱니바퀴 뒤에있는 톱니바퀴 회전 검사
    for i in range(no-1,-1,-1):
        if a[i][2] != a[i+1][6]:
            d[i]= -d[i+1]
        else:
            break
    #지정된 톱니바퀴 앞에 있는 톱니바퀴 회전 검사
    for i in range(no+1,n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break
    #톱니바퀴 회전
    for i in range(n):
        #i == 0 이면 회전 x
        if d[i] == 0:
            continue
        # 1이면 시계방향으로 회전
        if d[i] == 1:
            temp=a[i][7]
            for j in range(7,0,-1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        # -1 이면 반시계 방향으로 회전
        elif d[i] ==-1:
            temp = a[i][0]
            for j in range(0,7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp

ans = 0
#비트 체크
for i in range(n):
    if a[i][0] == '1':
        ans +=1

print(ans)
