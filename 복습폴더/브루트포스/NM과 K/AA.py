import sys
sys.stdin=open("00.txt","r")

def dfs(l):
    global ans
    if l == k :
        if ans < sum(d):
            ans = sum(d)
        return
    else :
        for i in range(n):
            for j in range(m):
                if ch[i][j] == 0 :
                    d[l] = a[i][j]
                    for x in range(4):
                        nx ,ny = i+dx[x],j+dy[x]
                        if 0<= nx <n and 0<= ny < m :
                            ch[nx][ny] = 1
                        dfs(l+1)
                        for x in range(4):
                            nx, ny = i + dx[x], j + dy[x]
                            if 0 <= nx < n and 0 <= ny < m:
                                ch[nx][ny] = 0

n,m,k = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

ans = 0
dx=[0,0,-1,1]
dy =[1,-1,0,0]

ch = [[0] * m for _ in range(n)]
d = [0] * k

num = k
test=[1,2,3,4]

dfs(0)

print(ans)