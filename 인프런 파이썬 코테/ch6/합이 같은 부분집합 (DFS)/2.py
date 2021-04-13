import sys
sys.stdin = open("00.txt","r")

def DFS(L,sum):
    if sum > total//2:  #시간복잡도를 줄이기 위해 작성
        return
    if L == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0) # 시스템을 종료하는 함수

    else :
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)



n = int(input())
a = list(map(int,input().split()))
total = sum(a)
DFS(0,0)
print("NO")