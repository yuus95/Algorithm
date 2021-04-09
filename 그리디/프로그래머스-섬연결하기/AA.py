#접근이 잘못된 것 같다.
n = 4
costs =[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

d_list = [[0]*n for _ in range(n)]
ch = [0]*n
for i in range(len(costs)):
    d_list[costs[i][0]][costs[i][1]]=costs[i][2]
    d_list[costs[i][1]][costs[i][0]] = costs[i][2]


print(d_list)
for i in range(n):
    for j in range(n):
        if  i == j :
            continue
        if d_list[i][j] >0 :
            if ch[j] == 0 :
                ch[j] =d_list[i][j]
            if d_list[i][j] < ch[j]:
                ch[j] = d_list[i][j]

