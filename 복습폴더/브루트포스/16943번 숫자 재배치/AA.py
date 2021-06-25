import sys
sys.stdin=open("00.txt","r")


a,b = input().split()

a = list(map(int,a))
a.sort()
b =int(b)
#다음순열
def next_permutation(x):
    i = len(x) -1

    while x[i] < x[i-1]  and i > 0:
        i-=1

    if i <= 0:
        return False

    j = len(x) - 1

    while x[i-1] >= x[j] :
        j-=1
    x[i-1] ,x[j] = x[j],x[i-1]

    j = len(x) -1
    while i< j :
        x[i] , x[j] = x[j] , x[i]
        i +=1
        j -= 1

    return True

while True:
     temp = int("".join(map(str,a)))
     if temp > b :
         print(-1)
         break

     if next_permutation(a):
         ans = int("".join(map(str,a)))
         if ans > b :
             print(temp)
             break
     else :
         break