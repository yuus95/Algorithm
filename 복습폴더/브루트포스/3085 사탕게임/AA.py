import sys
sys.stdin=open("00.txt","r")

n= int(input())


a = [list(input()) for _ in range(n)]

ans = 0
#a,0,0,0,1
def make_sum(a,start_row, end_row, start_col,end_col):
    n = len(a)
    ans = 1
    for i in range(start_row,end_row+1):
        cnt = 1
        for j in range(1,n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else :
                cnt =1
            if ans < cnt :
                ans = cnt
    for i in range(start_col,end_col+1):
        cnt = 1
        for j in range(1,n):
            if  a[j][i] == a[j-1][i]:
                cnt+=1
            else:
                cnt= 1
            if ans < cnt:
                ans = cnt
    return ans





for i in range(n):
    for j in range(n):
        if j +1 < n  and a[i][j] != a[i][j+1]:
            a[i][j] ,a[i][j+1]  = a[i][j+1],a[i][j]
            temp = make_sum(a,i,i,j,j+1)
            a[i][j] , a[i][j+1] = a[i][j+1],a[i][j]
            if temp > ans:
                ans = temp
        if i+1 < n and a[i][j] != a[i+1][j]:
            a[i][j] , a[i+1][j] = a[i+1][j],a[i][j]
            temp = make_sum(a,i,i+1,j,j)
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
            if temp > ans:
                ans = temp


print(ans)

