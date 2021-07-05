import sys
sys.stdin=open("00.txt","r")

n,m = map(int,input().split())

a = [[False] * (n+1) for _ in range(n+1)]
degree=[0] * (n+1)
for _ in range(m):
    x,y = map(int,input().split())

    a[x][y]=a[y][x] = True
    degree[x]+=1
    degree[y]+=1


ans = -1

for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j] : #N2 - > m 으로 바뀌는과정 밑에 for문의 시간복잡도
            for k in range(1,n+1):
                if a[i][k] and a[j][k]:
                    s = degree[i] + degree[j] + degree[k] -6
                    if ans == - 1 or ans > s:
                        ans = s


# O(N2 )

print(ans)
