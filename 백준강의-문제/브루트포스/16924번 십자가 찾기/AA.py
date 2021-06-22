import sys
sys.stdin=open("00.txt","r")


n, m = map(int,input().split())
a = [input() for _ in range(n)]
check = [[False]*m for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            l = 0
            k = 1
            while True:
                #범위검사
                if i+k < n and i-k >= 0 and j+k < m and j-k >= 0:
                    if a[i+k][j] == '*' and a[i-k][j] == '*' and a[i][j+k] == '*' and a[i][j-k] == '*':
                        l = k
                    else:
                        break
                else:
                    break
                k += 1
            if l > 0:
                ans.append((i+1,j+1,l))
                check[i][j] = True
                for k in range(1, l+1):
                    check[i+k][j] = True
                    check[i-k][j] = True
                    check[i][j+k] = True
                    check[i][j-k] = True

for i in range(n):
    for j in range(m):
        if a[i][j] == '*' and check[i][j] == False:
            print(-1)
            exit()
print(len(ans))
for p in ans:
    print(' '.join(map(str,p)))