import sys
sys.stdin=open("00.txt","r")

n,m = map(int,input().split())

dx=[0,0,1,-1]
dy= [1,-1,0,0]


a = [list(input()) for _ in range(n)]

ans_num = -1
ans = []

ch =[[False] * m for _ in range(n)]

for  i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            k = 1
            l = 0
            while True:
                if 0<= i+k < n and 0<= i-k and 0<= j-k and j+k < m:
                    if a[i-k][j] == '*' and a[i+k][j] == '*' and a[i][j-k] == '*' and a[i][j+k] == '*':
                        l = k
                        k=k+1
                    else:
                        break
                else :
                    break
            if l >= 1:
                ch[i][j] = True
                for L in range(1,l+1):
                    ans.append((i+1,j+1,L))
                    ch[i+L][j] = True
                    ch[i-L][j] = True
                    ch[i][j+L] = True
                    ch[i][j-L] = True


ans_num = max(ans_num,len(ans))

for i in range(n):
    for j in range(m):
        if a[i][j] == '*' and ch[i][j] == False:
            ans_num = -1




print(ans_num)
if ans_num != -1:
    for x,y,z in ans:
        print(x,y,z,end=' ')
        print()


