import sys
sys.stdin = open("00.txt","r")

def DFS(L,x,y):
    global cnt
    if x> 9 or y >9 :
        return
    if d_list[x][y] == 2 :
        cnt = L

    if x-1 > 0 and d_list[x-1][y] == 1 :
        DFS(L,x,y-2)
    elif x+1 >9 and d_list[x+1][y] == 1 :
        DFS(L,x,y+2)
    else :
        DFS(L,x+1,y)



d_list = [list(map(int,input().split())) for _ in range(10)]
cnt = 0


for i in range(10):
    d_list[0][i] == 1
    DFS(i,0,0)

print(cnt)