import sys

sys.stdin=open("00.txt","r")

n = int(input()) # 부등호 개수
sign = input().split()
check = [False] * 10
mx,mn = "",""

def possible(i,j,k):
    if k == '<':
        return i<j
    if k == '>' :
        return i>j
    return True

def solve(cnt,z):
    global mx,mn
    if cnt == n+1:
        if not len(mn):
            mn= z
        else:
            mx = z
        return
    for i in range(10):
        if not check[i] :
            if cnt == 0 or  possible(z[-1],str(i),sign[cnt-1]):
                check[i]=True
                solve(cnt+1,z+str(i))
                check[i] = False


solve(0,"")
print(mx)
print(mn)