import sys
sys.stdin=open("00.txt","r")


a,b = input().split()

a = list(map(int,a))
a.sort()
b =int(b)
#다음순열
def next_permutation(x):
    i = len(x) - 1
    while i > 0 and a[i-1] >= a[i]:
         i-= 1

    j = len(x) -1
    while a[i-1] >= a[j]:
        j-=1

    a[i-1] ,a[j] = a[j],a[i-1]

    j = len(x) - 1
    while  i< j :
        a[i],a[j] = a[j] ,a[i]
        i +=1
        j -=1


    return True

while True:
    c=int(''.join(a))
    if a[0] != '0' and c <b :
        if ans == -1 or ans <c :
            ans =c

    if not next_permutation(a):
        break


print(ans)

