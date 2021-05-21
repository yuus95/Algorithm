import sys
sys.stdin=open("00.txt","r")

dx = [0,1,1]
dy = [1,1,0]


n,m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

d = [ [0] * m  for _ in range(n)]

d[0][0] = a[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and  j == 0 :
            continue
        if i -1 >= 0 :
            d[i][j] = d[i-1][j] + a[i][j]

        if j -1 >= 0:
            d[i][j]= max(d[i][j],d[i][j-1]+a[i][j])

        if i -1 >= 0 and j -1 >= 0 :
            d[i][j]=max(d[i][j] , d[i-1][j-1] + a[i][j])

print(d[n-1][m-1])


