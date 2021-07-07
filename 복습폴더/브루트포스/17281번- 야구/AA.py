import sys
sys.stdin=open("00.txt","r")


# 이닝 시뮬
def go():
    global ans
    temp = 0
    k=0
    for i in range(n):
        b1=b2=b3=0
        out=0
        while True:
            if k >= 9 :
                k = 0
            if out == 3 :
                break

            if a[i][d[k]] == 0 :
                out+=1

            elif a[i][d[k]] == 1 :
                temp += b3
                b3,b2,b1= b2,b1,1

            elif a[i][d[k]] == 2:
                temp +=b3+b2
                b3,b2,b1=b1,1,0

            elif a[i][d[k]] == 3:
                temp += b3 + b2 +b1
                b3, b2, b1 = 1 ,0, 0

            elif a[i][d[k]] == 4:
                temp +=b3+b2+b1+1
                b3=b2=b1=0

            k+=1

    if ans < temp:
        ans = temp
    return


# 선수 순서
def shuffle(idx):
    if idx == 9 :
        go()
        return
    if idx == 3:
        d[idx]= 0
        shuffle(idx+1)
        return

    for i in range(1,9):
        if ch[i] == True:
            continue
        ch[i] = True
        d[idx]= i
        shuffle(idx+1)
        ch[i] = False
    return


n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
d = [0] * 9
ch=[False] * 9

shuffle(0)
print(ans)