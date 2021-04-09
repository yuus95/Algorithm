import sys
sys.stdin=open("00.txt","r")

number,k = input().split()
numbers = list(map(int,list(number)))
k = int(k)
a=[]


for x in numbers:
    while len(a)>0 and k>0 and a[-1] < x :
        a.pop()
        k-=1
    a.append(x)


if k>0:
    a=a[:-k]

a="".join(map(str,a))
print(a)