import sys
sys.stdin=open("00.txt","r")

n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]

player = [0] * 9

check = [False] * 9

def simulate():
    now = 0
    score = 0
    for inning in range(n):
        b1,b2,b3 = 0,0,0

        out = 0

        while out<3:
            res = a[inning][player[now]]
            if res == 0 :
                out +=1
            elif res == 1:
                score += b3
                b3,b2,b1 = b2,b1,1
            elif res == 2 :
                score += b3+b2
                b3,b2,b1 =b1,1,0
            elif res == 3 :
                score += b3+b2 +b1
                b3,b2,b1 = 1,0,0

            elif res == 4:
                score += b3+b2 +b1 +1
                b3,b2,b1 = 0,0,0

            now +=1
            if now == 9 :
                now = 0

    return score


def go(index):
    if index == 9 :
        return simulate()

    if index == 3 :
        player[index] = 0
        return go(index+1)

    ans = 0
    for i in range(1,9):
        if check[i] :
            continue

        check[i] = True
        player[index]=i
        temp = go(index+1)
        if ans < temp:
            ans = temp
        check[i] = False
    return ans


print(go(0))