import sys
sys.stdin=open("00.txt","r")

d_list = [list(map(int,input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = d_list[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if d_list[i+k][j]!= d_list[i+5-k-1][j]:
                break;
        else:
             cnt+=1

print(cnt)
