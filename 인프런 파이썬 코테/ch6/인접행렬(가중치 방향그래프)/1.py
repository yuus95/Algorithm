import sys
sys.stdin=open("00.txt","r")



n,m = map(int,input().split())

data_list  = [list(map(int,input().split())) for _ in range(m)]

out_list =list([0]* n for i in range(n))

for i in range(m):
    for j in range(3):
        out_list[data_list[i][0]-1][data_list[i][1]-1] = data_list[i][2]

for x in range(n):
    for y in range(n):
        print(out_list[x][y],end=' ')
    print()
