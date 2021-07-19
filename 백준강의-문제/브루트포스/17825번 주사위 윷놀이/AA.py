import sys
sys.stdin=open("00.txt","r")
n = 33


#i번쨰 점수
score = [
    0,2,4,6,8,
    10,13,16,19,25,
    12,14,16,18,20,
    22,24,22,24,26,
    28,26,27,28,30,
    32,34,36,38,30,
    35,40,0
]
t = 10
dice = list(map(int,input().split()))

#윷놀이 위치마다 움직일 수 있는 방법 기록 [0] =  해당 위치에서 시작 [1] 해당 위치를 지나가는길
a = [0]*n
a[0] = [1,1]
a[1] = [2,2]
a[2] = [3,3]
a[3] = [4,4]
a[4] = [5,5]
a[5] = [6,10]
a[6] = [7,7]
a[7] = [8,8]
a[8] = [9,9]
a[9] = [29,29]
a[10] = [11,11]
a[11] = [12,12]
a[12] = [13,13]
a[13] = [14,14]
a[14] = [15,17]
a[15] = [16,16]
a[16] = [9,9]
a[17] = [18,18]
a[18] = [19,19]
a[19] = [20,20]
a[20] = [24,24]
a[21] = [9,9]
a[22] = [21,21]
a[23] = [22,22]
a[24] = [23,25]
a[25] = [26,26]
a[26] = [27,27]
a[27] = [28,28]
a[28] = [31,31]
a[29] = [30,30]
a[30] = [31,31]
a[31] = [32,32]
a[32] = [32,32]

def get_next(start, k):
    now = start
    for i in range(k):
        if i == 0:
            now = a[now][0]
        else:
            now = a[now][1]
    return now

def go(index, horse, s):
    if index == t:
        return s
    ans = 0
    for i in range(4):
        nxt = get_next(horse[i], dice[index])
        ok = True
        if nxt != n-1:
            for j in range(4):
                if i == j:
                    continue
                if nxt == horse[j]:
                    ok = False
        if ok:
            nhorse = horse[:]
            nhorse[i] = nxt
            temp = go(index+1, nhorse, s+score[nxt])
            if ans < temp:
                ans = temp
    return ans

print(go(0, [0, 0, 0, 0], 0))
