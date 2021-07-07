import sys
sys.stdin=open("00.txt","r")



def next_permutation(a):
    i= len(a)-1
    while  i > 0 and a[i-1] >=a[i]:
         i -=1
    if i <= 0 :
        return False
    j = len(a)-1
    while a[i-1] >=a[j]:
        j-=1 

    a[i-1], a[j] = a[j],a[i-1]

    j = len(a)-1

    while i <j :
        a[i],a[j]= a[j],a[i]
        i+=1
        j-=1
    return True



n = int(input())

a = list(map(int, input().split()))
a.sort()
ans = 0
for i  in range(n-1):
    ans += abs(a[i]-a[i+1])

while True:
    if next_permutation(a):
        temp=0
        for i in range(n - 1):
            temp += abs(a[i] - a[i + 1])
        if temp > ans:
            ans = temp
    else:
        break
print(ans)





